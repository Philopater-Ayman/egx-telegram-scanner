from datetime import date

import pandas as pd

from config import MARKET_CALENDAR_FILE


CALENDAR_COLUMNS = ["date", "status", "label", "open_time", "close_time", "notes"]


def ensure_market_calendar():
    if not MARKET_CALENDAR_FILE.exists():
        pd.DataFrame(columns=CALENDAR_COLUMNS).to_csv(MARKET_CALENDAR_FILE, index=False)


def get_market_day(target_date=None):
    ensure_market_calendar()
    target_date = target_date or date.today()
    target_text = target_date.isoformat()
    weekday = target_date.weekday()
    default_status = "OPEN" if weekday in {6, 0, 1, 2, 3} else "CLOSED"
    default = {
        "date": target_text,
        "status": default_status,
        "label": "Default Sunday-Thursday calendar" if default_status == "OPEN" else "Default weekend",
        "open_time": "09:30",
        "close_time": "15:00",
        "notes": "Add rows to market_calendar.csv for official holidays, Ramadan hours, and special sessions.",
    }
    try:
        df = pd.read_csv(MARKET_CALENDAR_FILE)
        if df.empty:
            return default
        row = df[df["date"].astype(str) == target_text]
        if row.empty:
            return default
        data = row.iloc[-1].to_dict()
        return {
            "date": target_text,
            "status": str(data.get("status") or default_status).upper(),
            "label": data.get("label") or default["label"],
            "open_time": data.get("open_time") or default["open_time"],
            "close_time": data.get("close_time") or default["close_time"],
            "notes": data.get("notes") or "",
        }
    except Exception as exc:
        default["status"] = "OPEN"
        default["label"] = "Calendar read failed"
        default["notes"] = f"market_calendar.csv could not be read: {exc}"
        return default


def should_run_scanner(target_date=None):
    day = get_market_day(target_date)
    return day.get("status") in {"OPEN", "SPECIAL", "RAMADAN"}, day
