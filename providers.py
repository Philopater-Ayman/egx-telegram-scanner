import logging
import re
from datetime import datetime, timedelta, timezone
from html import unescape

import pandas as pd
import requests
import yfinance as yf

from config import (
    BASE_DIR,
    get_sector_map,
    get_yahoo_symbol_map,
    MAX_PRICE_AGE_DAYS,
)

logging.getLogger("yfinance").setLevel(logging.CRITICAL)


MANUAL_MARKET_DATA_FILE = BASE_DIR / "manual_market_data.csv"
STOCKANALYSIS_EGX_URL = "https://stockanalysis.com/list/egyptian-stock-exchange/"
_STOCKANALYSIS_CACHE = {"loaded_at": None, "rows": {}}


def _to_utc_iso(ts):
    if ts is None or pd.isna(ts):
        return None
    if hasattr(ts, "to_pydatetime"):
        ts = ts.to_pydatetime()
    if ts.tzinfo is None:
        ts = ts.replace(tzinfo=timezone.utc)
    return ts.astimezone(timezone.utc).isoformat()


def _age_days(ts):
    if ts is None or pd.isna(ts):
        return None
    if hasattr(ts, "to_pydatetime"):
        ts = ts.to_pydatetime()
    if ts.tzinfo is None:
        ts = ts.replace(tzinfo=timezone.utc)
    return (datetime.now(timezone.utc) - ts.astimezone(timezone.utc)).days


def get_egx30_status():
    try:
        df = yf.Ticker("^EGX30").history(period="60d")
        if df.empty or "Close" not in df.columns:
            raise ValueError("Yahoo returned no EGX30 rows")

        df["MA20"] = df["Close"].rolling(window=20).mean()
        latest = df.iloc[-1]
        prev_close = df["Close"].iloc[-2] if len(df) > 1 else latest["Close"]
        ma20 = latest["MA20"] if not pd.isna(latest["MA20"]) else latest["Close"]
        data_age = _age_days(df.index[-1])
        stale = data_age is None or data_age > MAX_PRICE_AGE_DAYS
        return {
            "Price": round(float(latest["Close"]), 2),
            "MA20": round(float(ma20), 2),
            "Trend": "Bullish" if latest["Close"] > ma20 else "Bearish",
            "Daily_Change_%": round(((latest["Close"] - prev_close) / prev_close) * 100, 2),
            "Source": "Yahoo Finance ^EGX30",
            "As_Of": _to_utc_iso(df.index[-1]),
            "Freshness": "STALE" if stale else "FRESH",
            "Warnings": ["EGX30 data is stale; BUY confidence must be downgraded."] if stale else [],
        }
    except Exception as exc:
        return {
            "Price": None,
            "MA20": None,
            "Trend": "Unavailable",
            "Daily_Change_%": 0.0,
            "Source": "Unavailable",
            "As_Of": None,
            "Freshness": "MISSING",
            "Warnings": [f"EGX30 macro data unavailable from Yahoo: {exc}"],
        }


def get_mubasher_egx30_status():
    url = "https://english.mubasher.info/markets/EGX"
    try:
        response = requests.get(url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        html = response.text
        price_match = re.search(r'market-summary__last-price[^>]*>([\d,]+(?:\.\d+)?)<', html)
        change_match = re.search(r'market-summary__change-percentage[^>]*>\s*([+-]?\d+(?:\.\d+)?)%', html)
        date_match = re.search(r'market-summary__date">\s*Last update:\s*([^<]+)<', html)
        if not price_match:
            raise ValueError("Could not find EGX30 price in Mubasher HTML")
        price = float(price_match.group(1).replace(",", ""))
        pct_change = float(change_match.group(1)) if change_match else 0.0
        trend = "Bullish" if pct_change >= 0 else "Bearish"
        date_label = date_match.group(1).strip() if date_match else "Mubasher latest delayed page update"
        return {
            "Price": round(price, 2),
            "MA20": None,
            "Trend": trend,
            "Daily_Change_%": round(pct_change, 2),
            "Source": "Mubasher EGX page (delayed public data)",
            "As_Of": date_label,
            "Freshness": "DELAYED",
            "Warnings": [
                "EGX30 macro source is Mubasher delayed public data; it is usable for context but not live execution."
            ],
            "Source_URL": url,
        }
    except Exception as exc:
        return {
            "Price": None,
            "MA20": None,
            "Trend": "Unavailable",
            "Daily_Change_%": 0.0,
            "Source": "Unavailable",
            "As_Of": None,
            "Freshness": "MISSING",
            "Warnings": [f"EGX30 macro data unavailable from Yahoo and Mubasher: {exc}"],
        }


def get_macro_status():
    mubasher_status = get_mubasher_egx30_status()
    if mubasher_status.get("Price") is not None:
        mubasher_status["Source"] = "Mubasher EGX market page (delayed public data)"
        mubasher_status["Warnings"] = []
        return mubasher_status
    return {
        "Price": None,
        "MA20": None,
        "Trend": "Unavailable",
        "Daily_Change_%": 0.0,
        "Source": "Market context unavailable",
        "As_Of": None,
        "Freshness": "MISSING",
        "Warnings": [],
    }


def _clean_html_text(value):
    value = re.sub(r"<.*?>", " ", value or "")
    return " ".join(unescape(value).split())


def _load_stockanalysis_rows():
    loaded_at = _STOCKANALYSIS_CACHE.get("loaded_at")
    if loaded_at and datetime.now(timezone.utc) - loaded_at < timedelta(hours=2):
        return _STOCKANALYSIS_CACHE["rows"]

    try:
        response = requests.get(STOCKANALYSIS_EGX_URL, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        html = response.text
        rows = {}
        row_pattern = re.compile(r"<tr[^>]*>(.*?)</tr>", re.S)
        cell_pattern = re.compile(r"<td[^>]*>(.*?)</td>", re.S)
        for row_html in row_pattern.findall(html):
            symbol_match = re.search(r'/quote/egx/([A-Z0-9]+)/">([^<]+)</a>', row_html)
            if not symbol_match:
                continue
            cells = [_clean_html_text(cell) for cell in cell_pattern.findall(row_html)]
            if len(cells) < 5:
                continue
            symbol = symbol_match.group(1).upper()
            try:
                price = float(cells[4].replace(",", ""))
            except Exception:
                continue
            rows[symbol] = {
                "symbol": symbol,
                "company": cells[2] if len(cells) > 2 else symbol,
                "market_cap": cells[3] if len(cells) > 3 else "",
                "price": price,
                "change": cells[5] if len(cells) > 5 else "",
            }
        _STOCKANALYSIS_CACHE["loaded_at"] = datetime.now(timezone.utc)
        _STOCKANALYSIS_CACHE["rows"] = rows
        return rows
    except Exception:
        return {}


def _stockanalysis_market_row(ticker):
    symbol = ticker.replace(".CA", "").upper()
    row = _load_stockanalysis_rows().get(symbol)
    if not row:
        return None
    price = float(row["price"])
    return {
        "Ticker": ticker,
        "Yahoo_Symbol": ticker,
        "Sector": get_sector_map().get(ticker, "General"),
        "Current_Price": round(price, 2),
        "MA20": round(price, 2),
        "MA50": round(price, 2),
        "MA200": round(price, 2),
        "RSI": 50.0,
        "MACD": 0.0,
        "MACD_Signal": 0.0,
        "Daily_Liquidity_EGP": 0.0,
        "Avg20_Liquidity_EGP": 0.0,
        "Liquidity_Spike": 0.0,
        "Return_5D_%": 0.0,
        "Return_20D_%": 0.0,
        "Volatility_20D_%": 0.0,
        "Breakout_20D": False,
        "Volume": 0.0,
        "Price_Source": "StockAnalysis EGX public list (quote-only fallback)",
        "Price_As_Of": datetime.now(timezone.utc).date().isoformat(),
        "Price_Freshness": "QUOTE_ONLY",
        "Recent_Headlines": [],
        "News_Items": [
            {
                "title": f"StockAnalysis EGX listing for {symbol}",
                "url": STOCKANALYSIS_EGX_URL,
                "source": "StockAnalysis",
            }
        ],
        "Warnings": [
            "StockAnalysis fallback is quote-only and has no volume/history; BUY must remain blocked unless another source provides liquidity."
        ],
    }


def _manual_market_row(ticker):
    if not MANUAL_MARKET_DATA_FILE.exists():
        return None
    try:
        df = pd.read_csv(MANUAL_MARKET_DATA_FILE)
        if df.empty or "Ticker" not in df.columns:
            return None
        row = df[df["Ticker"].astype(str).str.upper() == ticker.upper()]
        if row.empty:
            return None
        latest = row.iloc[-1].to_dict()
        close = float(latest.get("Close") or latest.get("Current_Price") or 0)
        volume = float(latest.get("Volume") or 0)
        if close <= 0:
            return None
        as_of = latest.get("Date") or latest.get("Price_As_Of") or datetime.now(timezone.utc).date().isoformat()
        return {
            "Ticker": ticker,
            "Sector": get_sector_map().get(ticker, "General"),
            "Current_Price": round(close, 2),
            "MA20": round(float(latest.get("MA20") or close), 2),
            "MA50": round(float(latest.get("MA50") or close), 2),
            "MA200": round(float(latest.get("MA200") or close), 2),
            "RSI": round(float(latest.get("RSI") or 50), 2),
            "MACD": round(float(latest.get("MACD") or 0), 4),
            "MACD_Signal": round(float(latest.get("MACD_Signal") or 0), 4),
            "Daily_Liquidity_EGP": round(close * volume, 2),
            "Avg20_Liquidity_EGP": round(float(latest.get("Avg20_Liquidity_EGP") or close * volume), 2),
            "Liquidity_Spike": round(float(latest.get("Liquidity_Spike") or 1), 2),
            "Volume": volume,
            "Price_Source": "manual_market_data.csv",
            "Price_As_Of": str(as_of),
            "Price_Freshness": str(latest.get("Price_Freshness") or "MANUAL"),
            "Recent_Headlines": [],
            "News_Items": [],
            "Warnings": ["Manual market data row used; verify freshness before execution."],
        }
    except Exception as exc:
        print(f"Warning: manual market data failed for {ticker}: {exc}")
        return None


def get_technical_data(ticker):
    try:
        yahoo_symbol = get_yahoo_symbol_map().get(ticker, ticker)
        stock = yf.Ticker(yahoo_symbol)
        df = stock.history(period="260d")
        if df.empty:
            raise ValueError("Yahoo returned no rows")

        df["MA20"] = df["Close"].rolling(window=20).mean()
        df["MA50"] = df["Close"].rolling(window=50).mean()
        df["MA200"] = df["Close"].rolling(window=200).mean()
        delta = df["Close"].diff()
        gain = delta.where(delta > 0, 0).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss.replace(0, pd.NA)
        df["RSI"] = 100 - (100 / (1 + rs))
        ema12 = df["Close"].ewm(span=12, adjust=False).mean()
        ema26 = df["Close"].ewm(span=26, adjust=False).mean()
        df["MACD"] = ema12 - ema26
        df["MACD_Signal"] = df["MACD"].ewm(span=9, adjust=False).mean()
        df["Liquidity"] = df["Close"] * df["Volume"].fillna(0)
        df["Avg20_Liquidity"] = df["Liquidity"].rolling(window=20).mean()
        df["High20"] = df["Close"].rolling(window=20).max()

        latest = df.iloc[-1]
        if pd.isna(latest["Close"]):
            raise ValueError("Latest close price is missing")
        data_age = _age_days(df.index[-1])
        stale = data_age is None or data_age > MAX_PRICE_AGE_DAYS
        current_price = float(latest["Close"])
        raw_volume = latest.get("Volume", 0)
        volume = 0.0 if pd.isna(raw_volume) else float(raw_volume or 0)
        avg20_liquidity = latest["Avg20_Liquidity"] if not pd.isna(latest["Avg20_Liquidity"]) else current_price * volume
        liquidity_spike = (current_price * volume) / avg20_liquidity if avg20_liquidity else 0
        warnings = []
        if stale:
            warnings.append("Price data is stale.")
        if volume <= 0:
            warnings.append("Latest volume is missing or zero.")

        headlines = []
        news_items = []
        try:
            for item in stock.news[:3]:
                headline = item.get("title")
                if headline:
                    headlines.append(headline)
                    news_items.append(
                        {
                            "title": headline,
                            "url": item.get("link") or item.get("clickThroughUrl", {}).get("url") or "",
                            "source": item.get("publisher") or "Yahoo Finance news",
                        }
                    )
        except Exception:
            pass

        return {
            "Ticker": ticker,
            "Yahoo_Symbol": yahoo_symbol,
            "Sector": get_sector_map().get(ticker, "General"),
            "Current_Price": round(current_price, 2),
            "MA20": round(float(latest["MA20"]), 2) if not pd.isna(latest["MA20"]) else round(current_price, 2),
            "MA50": round(float(latest["MA50"]), 2) if not pd.isna(latest["MA50"]) else round(current_price, 2),
            "MA200": round(float(latest["MA200"]), 2) if not pd.isna(latest["MA200"]) else round(current_price, 2),
            "RSI": round(float(latest["RSI"]), 2) if not pd.isna(latest["RSI"]) else 50.0,
            "MACD": round(float(latest["MACD"]), 4) if not pd.isna(latest["MACD"]) else 0.0,
            "MACD_Signal": round(float(latest["MACD_Signal"]), 4) if not pd.isna(latest["MACD_Signal"]) else 0.0,
            "Daily_Liquidity_EGP": round(current_price * volume, 2),
            "Avg20_Liquidity_EGP": round(float(avg20_liquidity), 2) if not pd.isna(avg20_liquidity) else 0,
            "Liquidity_Spike": round(float(liquidity_spike), 2),
            "Return_5D_%": round(((current_price / float(df["Close"].dropna().iloc[-6])) - 1) * 100, 2) if len(df["Close"].dropna()) >= 6 else 0.0,
            "Return_20D_%": round(((current_price / float(df["Close"].dropna().iloc[-21])) - 1) * 100, 2) if len(df["Close"].dropna()) >= 21 else 0.0,
            "Volatility_20D_%": round(float(df["Close"].pct_change().tail(20).std() * 100), 2),
            "Breakout_20D": bool(current_price >= float(df["High20"].iloc[-2])) if len(df) > 21 and not pd.isna(df["High20"].iloc[-2]) else False,
            "Volume": volume,
            "Price_Source": "Yahoo Finance",
            "Price_As_Of": _to_utc_iso(df.index[-1]),
            "Price_Freshness": "STALE" if stale else "FRESH",
            "Recent_Headlines": headlines,
            "News_Items": news_items,
            "Warnings": warnings,
        }
    except Exception as exc:
        manual = _manual_market_row(ticker)
        if manual:
            return manual
        stockanalysis = _stockanalysis_market_row(ticker)
        if stockanalysis:
            return stockanalysis
        print(f"Warning: market data failed for {ticker}: {exc}")
        return None


def get_backtest_summary(ticker):
    try:
        df = yf.Ticker(ticker).history(period="180d")
        if df.empty or "Close" not in df.columns or len(df) < 40:
            return {
                "Ticker": ticker,
                "Status": "INSUFFICIENT_DATA",
                "Summary": "Not enough Yahoo history for a useful lightweight backtest.",
            }

        close = df["Close"].dropna()
        first = float(close.iloc[0])
        last = float(close.iloc[-1])
        peak = close.cummax()
        drawdown = ((close - peak) / peak).min() * 100
        ma20 = close.rolling(20).mean()
        ma50 = close.rolling(50).mean()
        trend_days = int((ma20.tail(20) > ma50.tail(20)).sum()) if len(close) >= 70 else 0
        return {
            "Ticker": ticker,
            "Status": "OK",
            "Period": "180d Yahoo close-price check",
            "Buy_Hold_Return_%": round(((last - first) / first) * 100, 2),
            "Max_Drawdown_%": round(float(drawdown), 2),
            "MA20_Above_MA50_Days_Last20": trend_days,
            "Data_As_Of": _to_utc_iso(df.index[-1]),
            "Warning": "Lightweight historical check only; not a trading guarantee.",
        }
    except Exception as exc:
        return {
            "Ticker": ticker,
            "Status": "FAILED",
            "Summary": f"Backtest-lite failed: {exc}",
        }
