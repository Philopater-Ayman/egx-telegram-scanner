from datetime import datetime, timezone

import pandas as pd

from config import (
    FLOW_BUY_BLOCK_THRESHOLD_EGP,
    FLOW_SELL_PRESSURE_THRESHOLD_EGP,
    DATA_QUALITY_FILE,
    INDICATORS_FILE,
    INSTITUTION_FLOW_FILE,
    MARKET_PRICES_FILE,
    MIN_DAILY_LIQUIDITY_EGP,
    REQUIRE_FLOW_FOR_BUY,
    SCAN_RESULTS_FILE,
    SECTOR_SCORES_FILE,
    WATCHLIST_SIGNALS_FILE,
    get_index_tags_map,
)


FLOW_COLUMNS = [
    "date",
    "source_label",
    "source_url",
    "egyptian_institutions_net",
    "arab_institutions_net",
    "foreign_institutions_net",
    "egyptian_individuals_net",
    "arab_individuals_net",
    "foreign_individuals_net",
    "notes",
]


def ensure_institution_flow_file():
    if not INSTITUTION_FLOW_FILE.exists():
        pd.DataFrame(columns=FLOW_COLUMNS).to_csv(INSTITUTION_FLOW_FILE, index=False)


def _float(value, default=0.0):
    try:
        value = float(value)
        if value != value:
            return default
        return value
    except Exception:
        return default


def _is_tradeable_price(row):
    return row.get("Price_Freshness") in {"FRESH", "DELAYED_CURRENT"}


def get_latest_institution_flow():
    ensure_institution_flow_file()
    try:
        df = pd.read_csv(INSTITUTION_FLOW_FILE)
        if df.empty:
            return {
                "status": "FLOW_MISSING",
                "source_label": "MISSING",
                "source_url": "",
                "date": "",
                "total_institution_net": 0.0,
                "foreign_institution_net": 0.0,
                "regime": "MISSING",
                "warnings": [],
            }
        latest = df.dropna(how="all").iloc[-1].to_dict()
        egyptian = _float(latest.get("egyptian_institutions_net"))
        arab = _float(latest.get("arab_institutions_net"))
        foreign = _float(latest.get("foreign_institutions_net"))
        total = egyptian + arab + foreign
        source_label = str(latest.get("source_label") or "MISSING").upper()
        if source_label not in {"OFFICIAL", "PUBLIC_REPORT", "MANUAL_IMPORT"}:
            status = "FLOW_WEAK_SOURCE"
        else:
            status = "FLOW_AVAILABLE"
        if total <= FLOW_SELL_PRESSURE_THRESHOLD_EGP or foreign <= FLOW_SELL_PRESSURE_THRESHOLD_EGP:
            regime = "INSTITUTION_SELL_PRESSURE"
        elif total < FLOW_BUY_BLOCK_THRESHOLD_EGP:
            regime = "INSTITUTION_OUTFLOW"
        elif total > 0:
            regime = "INSTITUTION_INFLOW"
        else:
            regime = "FLOW_NEUTRAL"
        return {
            "status": status,
            "source_label": source_label,
            "source_url": latest.get("source_url") or "",
            "date": latest.get("date") or "",
            "egyptian_institution_net": egyptian,
            "arab_institution_net": arab,
            "foreign_institution_net": foreign,
            "total_institution_net": total,
            "regime": regime,
            "warnings": [] if status == "FLOW_AVAILABLE" else ["Institution-flow source is not execution-grade."],
        }
    except Exception as exc:
        return {
            "status": "FLOW_ERROR",
            "source_label": "MISSING",
            "source_url": "",
            "date": "",
            "total_institution_net": 0.0,
            "foreign_institution_net": 0.0,
            "regime": "MISSING",
            "warnings": [f"Institution-flow file could not be read: {exc}"],
        }


def build_sector_scores(market_rows):
    if not market_rows:
        return {}
    df = pd.DataFrame(market_rows)
    if df.empty:
        return {}
    rows = []
    for sector, group in df.groupby("Sector", dropna=False):
        above_ma20 = (group["Current_Price"].astype(float) > group["MA20"].astype(float)).mean() * 100
        above_ma50 = (group["Current_Price"].astype(float) > group["MA50"].astype(float)).mean() * 100
        median_5d = group.get("Return_5D_%", pd.Series([0])).astype(float).median()
        median_20d = group.get("Return_20D_%", pd.Series([0])).astype(float).median()
        median_liquidity_spike = group.get("Liquidity_Spike", pd.Series([0])).astype(float).median()
        score = (median_5d * 0.4) + (median_20d * 0.2) + (above_ma20 * 0.03) + (above_ma50 * 0.03) + (median_liquidity_spike * 1.5)
        top_stocks = (
            group.sort_values("Daily_Liquidity_EGP", ascending=False)
            .head(5)["Ticker"]
            .astype(str)
            .tolist()
        )
        rows.append(
            {
                "Sector": sector or "General",
                "Ticker_Count": len(group),
                "Median_5D_Return_%": round(float(median_5d), 2),
                "Median_20D_Return_%": round(float(median_20d), 2),
                "Above_MA20_%": round(float(above_ma20), 2),
                "Above_MA50_%": round(float(above_ma50), 2),
                "Median_Liquidity_Spike": round(float(median_liquidity_spike), 2),
                "Top_Liquidity_Stocks": ", ".join(top_stocks),
                "Sector_Score": round(float(score), 2),
            }
        )
    ranked = sorted(rows, key=lambda item: item["Sector_Score"], reverse=True)
    return {row["Sector"]: {**row, "Sector_Rank": index + 1} for index, row in enumerate(ranked)}


def _regime_for_group(label, rows):
    if not rows:
        return {
            "label": label,
            "trend": "UNAVAILABLE",
            "ticker_count": 0,
            "fresh_count": 0,
            "above_ma20_pct": 0.0,
            "above_ma50_pct": 0.0,
            "median_5d_return_pct": 0.0,
            "median_20d_return_pct": 0.0,
            "median_liquidity_spike": 0.0,
            "notes": "No tagged stocks available.",
        }
    df = pd.DataFrame(rows)
    above_ma20 = (df["Current_Price"].astype(float) > df["MA20"].astype(float)).mean() * 100
    above_ma50 = (df["Current_Price"].astype(float) > df["MA50"].astype(float)).mean() * 100
    median_5d = df.get("Return_5D_%", pd.Series([0])).astype(float).median()
    median_20d = df.get("Return_20D_%", pd.Series([0])).astype(float).median()
    median_liquidity_spike = df.get("Liquidity_Spike", pd.Series([0])).astype(float).median()
    fresh_count = int(df.apply(lambda row: _is_tradeable_price(row), axis=1).sum())

    if above_ma20 >= 60 and above_ma50 >= 55 and median_5d > 0 and median_20d > 0:
        trend = "BULLISH"
    elif above_ma20 >= 50 and above_ma50 >= 45 and median_5d >= 0:
        trend = "CONSTRUCTIVE"
    elif above_ma20 < 45 or above_ma50 < 45 or (median_5d < 0 and median_20d < 0):
        trend = "BEARISH"
    else:
        trend = "MIXED"

    notes = []
    if above_ma20 < 50:
        notes.append("below MA20 breadth weak")
    if above_ma50 < 50:
        notes.append("below MA50 breadth weak")
    if median_5d < 0:
        notes.append("5d return negative")
    if median_liquidity_spike >= 1.2:
        notes.append("liquidity expanding")
    return {
        "label": label,
        "trend": trend,
        "ticker_count": len(rows),
        "fresh_count": fresh_count,
        "above_ma20_pct": round(float(above_ma20), 2),
        "above_ma50_pct": round(float(above_ma50), 2),
        "median_5d_return_pct": round(float(median_5d), 2),
        "median_20d_return_pct": round(float(median_20d), 2),
        "median_liquidity_spike": round(float(median_liquidity_spike), 2),
        "notes": "; ".join(notes) or "Index breadth supports normal selection.",
    }


def build_market_regime(market_rows, sector_scores):
    index_tags_map = get_index_tags_map()
    tagged_rows = []
    for row in market_rows:
        enriched = dict(row)
        enriched["Index_Tags"] = index_tags_map.get(row.get("Ticker"), "")
        tagged_rows.append(enriched)

    egx30_rows = [row for row in tagged_rows if "EGX30" in str(row.get("Index_Tags", "")).upper()]
    egx70_rows = [row for row in tagged_rows if "EGX70" in str(row.get("Index_Tags", "")).upper()]
    egx30 = _regime_for_group("EGX30", egx30_rows)
    egx70 = _regime_for_group("EGX70", egx70_rows)
    sector_rows = list((sector_scores or {}).values())
    if sector_rows:
        improving = [
            row for row in sector_rows
            if _float(row.get("Median_5D_Return_%")) > 0 and _float(row.get("Above_MA50_%")) >= 50
        ]
        sector_breadth_pct = round((len(improving) / len(sector_rows)) * 100, 2)
        leading_sectors = [row.get("Sector") for row in sorted(sector_rows, key=lambda item: item.get("Sector_Rank", 99))[:3]]
    else:
        sector_breadth_pct = 0.0
        leading_sectors = []

    bullishish = {"BULLISH", "CONSTRUCTIVE"}
    if egx30["trend"] in bullishish and egx70["trend"] in bullishish and sector_breadth_pct >= 55:
        risk_mode = "BROAD_RISK_ON"
        buy_support = "MARKET_SUPPORTS_BUYS"
    elif egx70["trend"] in bullishish and egx30["trend"] in {"BEARISH", "MIXED"}:
        risk_mode = "SELECTIVE_SMALL_MID_SWINGS"
        buy_support = "SELECTIVE_ONLY"
    elif egx30["trend"] == "BEARISH" and egx70["trend"] == "BEARISH":
        risk_mode = "DEFENSIVE_NO_NEW_BUY"
        buy_support = "MARKET_DOES_NOT_SUPPORT_NEW_BUYS"
    elif sector_breadth_pct < 35:
        risk_mode = "DEFENSIVE_NO_NEW_BUY"
        buy_support = "BREADTH_TOO_WEAK"
    else:
        risk_mode = "SELECTIVE_SWING_TRADES_ONLY"
        buy_support = "SELECTIVE_ONLY"

    return {
        "egx30": egx30,
        "egx70": egx70,
        "sector_breadth_pct": sector_breadth_pct,
        "leading_sectors": leading_sectors,
        "risk_mode": risk_mode,
        "buy_support": buy_support,
        "summary": (
            f"EGX30 {egx30['trend']} / EGX70 {egx70['trend']} / "
            f"sector breadth {sector_breadth_pct}% / risk mode {risk_mode}"
        ),
    }


def _outlook_fields(row, sector_rank, sector_score):
    price = _float(row.get("Current_Price"))
    ma20 = _float(row.get("MA20"))
    ma50 = _float(row.get("MA50"))
    ma200 = _float(row.get("MA200"))
    rsi = _float(row.get("RSI"), 50)
    liquidity = _float(row.get("Daily_Liquidity_EGP"))
    avg20_liquidity = _float(row.get("Avg20_Liquidity_EGP"))
    liquidity_spike = _float(row.get("Liquidity_Spike"))
    volatility = _float(row.get("Volatility_20D_%"))
    support_distance = _float(row.get("Support_Distance_%"))
    resistance_distance = _float(row.get("Resistance_Distance_%"))
    score = 0
    risk_notes = []

    if _is_tradeable_price(row):
        score += 15
    else:
        score -= 30
        risk_notes.append("price data is not fresh")
    if liquidity >= MIN_DAILY_LIQUIDITY_EGP:
        score += 15
    else:
        score -= 20
        risk_notes.append("liquidity below minimum")
    if avg20_liquidity > 0 and liquidity_spike >= 1.5:
        score += 12
    elif liquidity_spike < 0.8:
        score -= 5
        risk_notes.append("liquidity is cooling")
    if price > ma20:
        score += 10
    else:
        score -= 8
        risk_notes.append("below MA20")
    if price >= ma50:
        score += 12
    else:
        score -= 10
        risk_notes.append("below MA50")
    if price > ma200:
        score += 5
    if 40 <= rsi <= 62:
        score += 12
    elif 62 < rsi <= 70:
        score += 4
        risk_notes.append("momentum is extended")
    elif rsi < 35:
        score -= 8
        risk_notes.append("weak RSI")
    else:
        score -= 10
        risk_notes.append("overheated RSI")
    if row.get("Breakout_20D"):
        score += 8
    if 2 <= support_distance <= 12:
        score += 6
    elif support_distance > 20:
        score -= 4
        risk_notes.append("far above support")
    if resistance_distance >= 5:
        score += 6
    elif 0 < resistance_distance < 2:
        score -= 6
        risk_notes.append("close to resistance")
    if sector_rank <= 3:
        score += 10
    elif sector_rank >= 8:
        score -= 5
        risk_notes.append("sector is not leading")
    if sector_score > 0:
        score += min(sector_score, 10)
    if volatility > 7:
        score -= 6
        risk_notes.append("high short-term volatility")

    score = round(max(0, min(100, score)), 2)
    if score >= 70:
        label = "BULLISH_WATCH"
    elif score >= 50:
        label = "CONSTRUCTIVE"
    elif score >= 35:
        label = "NEUTRAL"
    else:
        label = "WEAK_OR_RISKY"

    if liquidity >= MIN_DAILY_LIQUIDITY_EGP * 5 and liquidity_spike >= 1.5:
        liquidity_regime = "ACCUMULATION_SPIKE"
    elif liquidity >= MIN_DAILY_LIQUIDITY_EGP:
        liquidity_regime = "TRADEABLE"
    elif liquidity > 0:
        liquidity_regime = "THIN"
    else:
        liquidity_regime = "MISSING"

    if sector_rank <= 3 and sector_score > 0:
        sector_momentum = "LEADING"
    elif sector_score > 0:
        sector_momentum = "IMPROVING"
    elif sector_rank >= 8:
        sector_momentum = "LAGGING"
    else:
        sector_momentum = "NEUTRAL"

    return {
        "Outlook_Label": label,
        "Outlook_Score": score,
        "Liquidity_Regime": liquidity_regime,
        "Sector_Momentum": sector_momentum,
        "Risk_Notes": "; ".join(risk_notes[:4]) or "No major short-term scanner risk flags.",
    }


def rank_candidates(market_rows, sector_scores, flow_status, market_regime=None):
    ranked = []
    market_regime = market_regime or {}
    flow_regime = flow_status.get("regime", "MISSING")
    flow_bonus = 2 if flow_regime == "INSTITUTION_INFLOW" else -4 if flow_regime in {"INSTITUTION_OUTFLOW", "INSTITUTION_SELL_PRESSURE"} else 0
    risk_mode = market_regime.get("risk_mode", "UNKNOWN")
    regime_bonus = 1.5 if risk_mode == "BROAD_RISK_ON" else -3 if risk_mode == "DEFENSIVE_NO_NEW_BUY" else 0
    hard_negative_flow = flow_regime in {"INSTITUTION_OUTFLOW", "INSTITUTION_SELL_PRESSURE"}
    flow_gate = not hard_negative_flow and risk_mode != "DEFENSIVE_NO_NEW_BUY" and (not REQUIRE_FLOW_FOR_BUY or flow_status.get("status") == "FLOW_AVAILABLE")
    for row in market_rows:
        price = _float(row.get("Current_Price"))
        ma20 = _float(row.get("MA20"))
        ma50 = _float(row.get("MA50"))
        ma200 = _float(row.get("MA200"))
        rsi = _float(row.get("RSI"), 50)
        macd = _float(row.get("MACD"))
        macd_signal = _float(row.get("MACD_Signal"))
        liquidity = _float(row.get("Daily_Liquidity_EGP"))
        avg20_liquidity = _float(row.get("Avg20_Liquidity_EGP"))
        liquidity_spike = _float(row.get("Liquidity_Spike"))
        sector = row.get("Sector") or "General"
        sector_score = sector_scores.get(sector, {}).get("Sector_Score", 0)
        sector_rank = sector_scores.get(sector, {}).get("Sector_Rank", 99)
        outlook = _outlook_fields(row, sector_rank, sector_score)

        liquidity_score = min(liquidity / max(MIN_DAILY_LIQUIDITY_EGP, 1), 10)
        liquidity_expansion_score = min(max(liquidity_spike - 1, 0) * 2, 5)
        trend_score = 0
        if price > ma20:
            trend_score += 2
        if price > ma50:
            trend_score += 3
        if price > ma200:
            trend_score += 1
        momentum_score = 2 if macd > macd_signal else 0
        rsi_score = 3 if 35 <= rsi <= 65 else 1 if 65 < rsi <= 75 else -2
        breakout_score = 2 if row.get("Breakout_20D") else 0
        freshness_score = 3 if _is_tradeable_price(row) else -6
        sector_component = max(4 - min(sector_rank, 4), 0) + min(max(sector_score, -4), 6) * 0.4

        score = (
            liquidity_score
            + liquidity_expansion_score
            + trend_score
            + momentum_score
            + rsi_score
            + breakout_score
            + freshness_score
            + sector_component
            + flow_bonus
            + regime_bonus
        )
        buy_ready = (
            flow_gate
            and _is_tradeable_price(row)
            and liquidity >= MIN_DAILY_LIQUIDITY_EGP
            and avg20_liquidity > 0
            and price > ma20
            and price >= ma50
            and 35 <= rsi <= 70
        )
        reasons = []
        if not flow_gate:
            reasons.append(f"flow_or_market_gate={flow_status.get('regime')}/{risk_mode}")
        if liquidity < MIN_DAILY_LIQUIDITY_EGP:
            reasons.append("liquidity_below_min")
        if not _is_tradeable_price(row):
            reasons.append("price_not_fresh")
        if price <= ma50:
            reasons.append("below_MA50")
        enriched = dict(row)
        enriched.update(
            {
                "Sector_Rank": sector_rank,
                "Sector_Score": round(float(sector_score), 2),
                "Flow_Regime": flow_regime,
                "Market_Risk_Mode": risk_mode,
                "Buy_Ready": buy_ready,
                "Buy_Block_Reasons": ";".join(reasons),
                "Rank_Score": round(float(score), 2),
                **outlook,
            }
        )
        ranked.append(enriched)
    return sorted(ranked, key=lambda item: item["Rank_Score"], reverse=True)


def build_watchlist_from_ranked(ranked_rows, current_watchlist, max_size=5):
    promoted = [row["Ticker"] for row in ranked_rows if row.get("Buy_Ready")]
    combined = []
    for ticker in promoted + current_watchlist:
        if ticker and ticker not in combined:
            combined.append(ticker)
        if len(combined) >= max_size:
            break
    return combined


def build_watchlist_signal_rows(ranked_rows, current_watchlist, flow_status):
    watchlist_set = set(current_watchlist)
    rows = []
    for row in ranked_rows:
        tier = "CANDIDATE"
        if row["Ticker"] in watchlist_set:
            tier = "CORE"
        if row.get("Buy_Ready"):
            tier = "WATCH"
        if not _is_tradeable_price(row) or row.get("Daily_Liquidity_EGP", 0) < MIN_DAILY_LIQUIDITY_EGP:
            tier = "DISABLED"
        rows.append(
            {
                "Ticker": row.get("Ticker"),
                "Sector": row.get("Sector"),
                "Watchlist_Tier": tier,
                "Rank_Score": row.get("Rank_Score"),
                "Buy_Ready": row.get("Buy_Ready"),
                "Flow_Regime": flow_status.get("regime"),
                "Signal_Status": "BUY_READY" if row.get("Buy_Ready") else "WATCH_ONLY",
                "Block_Reasons": row.get("Buy_Block_Reasons", ""),
                "Outlook_Label": row.get("Outlook_Label"),
                "Outlook_Score": row.get("Outlook_Score"),
                "Liquidity_Regime": row.get("Liquidity_Regime"),
                "Sector_Momentum": row.get("Sector_Momentum"),
            }
        )
    return rows


def write_scanner_outputs(ranked_rows, sector_scores, flow_status, scan_failures=None, current_watchlist=None):
    scan_failures = scan_failures or []
    current_watchlist = current_watchlist or []
    generated_at = datetime.now(timezone.utc).isoformat()
    price_rows = []
    indicator_rows = []
    scan_rows = []
    quality_rows = []
    for row in ranked_rows:
        price_rows.append(
            {
                "timestamp_utc": generated_at,
                "Ticker": row.get("Ticker"),
                "Yahoo_Symbol": row.get("Yahoo_Symbol", row.get("Ticker")),
                "Sector": row.get("Sector"),
                "Current_Price": row.get("Current_Price"),
                "Volume": row.get("Volume"),
                "Daily_Liquidity_EGP": row.get("Daily_Liquidity_EGP"),
                "Liquidity_Source": row.get("Liquidity_Source"),
                "Price_Source": row.get("Price_Source"),
                "Price_As_Of": row.get("Price_As_Of"),
                "Price_Freshness": row.get("Price_Freshness"),
                "DirectFN_Open": row.get("DirectFN_Open"),
                "DirectFN_High": row.get("DirectFN_High"),
                "DirectFN_Low": row.get("DirectFN_Low"),
                "DirectFN_Change_%": row.get("DirectFN_Change_%"),
            }
        )
        indicator_rows.append(
            {
                "timestamp_utc": generated_at,
                "Ticker": row.get("Ticker"),
                "MA20": row.get("MA20"),
                "MA50": row.get("MA50"),
                "MA200": row.get("MA200"),
                "RSI": row.get("RSI"),
                "MACD": row.get("MACD"),
                "MACD_Signal": row.get("MACD_Signal"),
                "Avg20_Liquidity_EGP": row.get("Avg20_Liquidity_EGP"),
                "Liquidity_Spike": row.get("Liquidity_Spike"),
                "Support_20D": row.get("Support_20D"),
                "Resistance_20D": row.get("Resistance_20D"),
                "Support_50D": row.get("Support_50D"),
                "Resistance_50D": row.get("Resistance_50D"),
                "Support_Distance_%": row.get("Support_Distance_%"),
                "Resistance_Distance_%": row.get("Resistance_Distance_%"),
                "Return_5D_%": row.get("Return_5D_%"),
                "Return_20D_%": row.get("Return_20D_%"),
                "Volatility_20D_%": row.get("Volatility_20D_%"),
                "Breakout_20D": row.get("Breakout_20D"),
            }
        )
        scan_rows.append(
            {
                "timestamp_utc": generated_at,
                "Ticker": row.get("Ticker"),
                "Sector": row.get("Sector"),
                "Rank_Score": row.get("Rank_Score"),
                "Sector_Rank": row.get("Sector_Rank"),
                "Flow_Regime": row.get("Flow_Regime"),
                "Market_Risk_Mode": row.get("Market_Risk_Mode"),
                "Buy_Ready": row.get("Buy_Ready"),
                "Buy_Block_Reasons": row.get("Buy_Block_Reasons"),
                "Outlook_Label": row.get("Outlook_Label"),
                "Outlook_Score": row.get("Outlook_Score"),
                "Liquidity_Regime": row.get("Liquidity_Regime"),
                "Sector_Momentum": row.get("Sector_Momentum"),
                "Risk_Notes": row.get("Risk_Notes"),
                "Current_Price": row.get("Current_Price"),
                "Daily_Liquidity_EGP": row.get("Daily_Liquidity_EGP"),
                "Liquidity_Source": row.get("Liquidity_Source"),
                "Liquidity_Spike": row.get("Liquidity_Spike"),
                "RSI": row.get("RSI"),
                "Support_20D": row.get("Support_20D"),
                "Resistance_20D": row.get("Resistance_20D"),
                "Support_Distance_%": row.get("Support_Distance_%"),
                "Resistance_Distance_%": row.get("Resistance_Distance_%"),
            }
        )
        quality_rows.append(
            {
                "timestamp_utc": generated_at,
                "Ticker": row.get("Ticker"),
                "Sector": row.get("Sector"),
                "Data_Status": "OK",
                "Provider": row.get("Price_Source"),
                "Liquidity_Source": row.get("Liquidity_Source"),
                "Price_As_Of": row.get("Price_As_Of"),
                "Freshness": row.get("Price_Freshness"),
                "Volume": row.get("Volume"),
                "Daily_Liquidity_EGP": row.get("Daily_Liquidity_EGP"),
                "Issue": "; ".join(row.get("Warnings", [])),
                "Recommended_Action": "Review manually" if row.get("Warnings") else "No action",
            }
        )
    for failure in scan_failures:
        quality_rows.append(
            {
                "timestamp_utc": generated_at,
                "Ticker": failure.get("Ticker"),
                "Sector": failure.get("Sector", "General"),
                "Data_Status": "FAILED",
                "Provider": failure.get("Provider", "Yahoo/manual fallback"),
                "Price_As_Of": "",
                "Freshness": "MISSING",
                "Volume": 0,
                "Daily_Liquidity_EGP": 0,
                "Issue": failure.get("Issue", "No usable market data returned."),
                "Recommended_Action": "Check Yahoo symbol or add manual_market_data.csv row",
            }
        )
    pd.DataFrame(price_rows).to_csv(MARKET_PRICES_FILE, index=False)
    pd.DataFrame(indicator_rows).to_csv(INDICATORS_FILE, index=False)
    pd.DataFrame(sorted(sector_scores.values(), key=lambda item: item["Sector_Rank"])).to_csv(SECTOR_SCORES_FILE, index=False)
    pd.DataFrame(scan_rows).to_csv(SCAN_RESULTS_FILE, index=False)
    pd.DataFrame(quality_rows).to_csv(DATA_QUALITY_FILE, index=False)
    signal_rows = build_watchlist_signal_rows(ranked_rows, current_watchlist, flow_status)
    pd.DataFrame(signal_rows).to_csv(WATCHLIST_SIGNALS_FILE, index=False)
