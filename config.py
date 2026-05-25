import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

ADVISOR_ONLY = True
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "").strip()
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "openai/gpt-oss-120b:free").strip()
OPENROUTER_FALLBACK_MODELS = [
    item.strip()
    for item in os.getenv(
        "OPENROUTER_FALLBACK_MODELS",
        "deepseek/deepseek-v4-flash:free,nvidia/nemotron-3-super-120b-a12b:free",
    ).split(",")
    if item.strip()
]
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "").strip()
SEND_TELEGRAM = os.getenv("SEND_TELEGRAM", "true").strip().lower() in {"1", "true", "yes", "on"}

WATCHLIST_FILE = BASE_DIR / "watchlist.csv"
HISTORY_FILE = BASE_DIR / "trade_history.csv"
REPORT_FILE = BASE_DIR / "daily_report.md"
ACTION_TICKETS_FILE = BASE_DIR / "action_tickets.csv"
PROVIDER_STATUS_FILE = BASE_DIR / "provider_status.md"
STOCK_UNIVERSE_FILE = BASE_DIR / "stock_universe.csv"
MARKET_PRICES_FILE = BASE_DIR / "market_prices.csv"
INDICATORS_FILE = BASE_DIR / "indicators.csv"
SECTOR_SCORES_FILE = BASE_DIR / "sector_scores.csv"
INSTITUTION_FLOW_FILE = BASE_DIR / "institution_flow.csv"
WATCHLIST_SIGNALS_FILE = BASE_DIR / "watchlist_signals.csv"
SCAN_RESULTS_FILE = BASE_DIR / "scan_results.csv"
DATA_QUALITY_FILE = BASE_DIR / "data_quality.csv"
DATA_HEALTH_FILE = DATA_QUALITY_FILE
MARKET_CALENDAR_FILE = BASE_DIR / "market_calendar.csv"

DEFAULT_WATCHLIST = ["COMI.CA", "TMGH.CA", "SWDY.CA", "FWRY.CA", "ABUK.CA"]
MAX_WATCHLIST_SIZE = 5
MAX_POSITION_CASH_PCT = 0.30
MIN_DAILY_LIQUIDITY_EGP = 1_000_000
MAX_PRICE_AGE_DAYS = int(os.getenv("MAX_PRICE_AGE_DAYS", "5"))
EVIDENCE_TOP_N = int(os.getenv("EVIDENCE_TOP_N", "8"))
USE_GEMINI_GROUNDING = os.getenv("USE_GEMINI_GROUNDING", "true").strip().lower() in {"1", "true", "yes", "on"}
USE_OPENROUTER_NARRATIVE = os.getenv("USE_OPENROUTER_NARRATIVE", "true").strip().lower() in {"1", "true", "yes", "on"}
USE_AI_DECISION = os.getenv("USE_AI_DECISION", "false").strip().lower() in {"1", "true", "yes", "on"}
NEWSDATA_API_KEY = os.getenv("NEWSDATA_API_KEY", "").strip()
FLOW_BUY_BLOCK_THRESHOLD_EGP = float(os.getenv("FLOW_BUY_BLOCK_THRESHOLD_EGP", "-50000000"))
FLOW_SELL_PRESSURE_THRESHOLD_EGP = float(os.getenv("FLOW_SELL_PRESSURE_THRESHOLD_EGP", "-100000000"))
REQUIRE_FLOW_FOR_BUY = os.getenv("REQUIRE_FLOW_FOR_BUY", "false").strip().lower() in {"1", "true", "yes", "on"}

EGX_SECTOR_MAP = {
    "COMI.CA": "Banking & Financials",
    "ADIB.CA": "Banking & Financials",
    "CIEB.CA": "Banking & Financials",
    "QNBA.CA": "Banking & Financials",
    "SAUD.CA": "Banking & Financials",
    "TMGH.CA": "Real Estate",
    "MASR.CA": "Real Estate",
    "OCDI.CA": "Real Estate",
    "HELI.CA": "Real Estate",
    "SWDY.CA": "Industrial Goods & Cables",
    "ORAS.CA": "Industrial Goods & Construction",
    "ABUK.CA": "Basic Resources & Chemicals",
    "EGAL.CA": "Basic Resources & Chemicals",
    "MFPC.CA": "Basic Resources & Chemicals",
    "EFID.CA": "Food, Beverages & Tobacco",
    "EAST.CA": "Food, Beverages & Tobacco",
    "FWRY.CA": "Fintech & Payments",
    "EFIH.CA": "Fintech & Payments",
    "HRHO.CA": "Non-bank Financial Services",
    "CIRA.CA": "Education",
    "ETEL.CA": "Telecommunications",
    "CLHO.CA": "Healthcare",
    "JUFO.CA": "Food, Beverages & Tobacco",
}

def load_stock_universe():
    if not STOCK_UNIVERSE_FILE.exists():
        rows = []
        for ticker, sector in EGX_SECTOR_MAP.items():
            rows.append(
                {
                    "Ticker": ticker,
                    "Company Name": ticker.replace(".CA", "") + " Company",
                    "Sector": sector,
                    "Index Tags": "LEGACY_SEED",
                    "Yahoo Symbol": ticker,
                    "Active": "TRUE",
                }
            )
        return pd.DataFrame(rows)

    df = pd.read_csv(STOCK_UNIVERSE_FILE)
    required = {"Ticker", "Company Name", "Sector", "Yahoo Symbol", "Active"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"stock_universe.csv is missing columns: {', '.join(sorted(missing))}")
    df["Ticker"] = df["Ticker"].astype(str).str.strip()
    df["Yahoo Symbol"] = df["Yahoo Symbol"].fillna(df["Ticker"]).astype(str).str.strip()
    df["Sector"] = df["Sector"].fillna("General")
    df["Active"] = df["Active"].astype(str).str.strip().str.upper()
    return df


def get_active_universe_records():
    df = load_stock_universe()
    active = df[df["Active"].isin({"TRUE", "1", "YES", "Y", "ACTIVE"})].copy()
    return active.to_dict(orient="records")


def get_sector_map():
    records = get_active_universe_records()
    if not records:
        return dict(EGX_SECTOR_MAP)
    return {row["Ticker"]: row.get("Sector") or "General" for row in records}


def get_yahoo_symbol_map():
    records = get_active_universe_records()
    return {row["Ticker"]: row.get("Yahoo Symbol") or row["Ticker"] for row in records}


def get_company_name_map():
    records = get_active_universe_records()
    return {row["Ticker"]: row.get("Company Name") or row["Ticker"] for row in records}


EGX_CANDIDATE_POOL = [row["Ticker"] for row in get_active_universe_records()] or list(EGX_SECTOR_MAP.keys())
