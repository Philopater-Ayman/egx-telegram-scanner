import csv
from datetime import datetime, timezone

import pandas as pd

from config import (
    ACTION_TICKETS_FILE,
    DEFAULT_WATCHLIST,
    HISTORY_FILE,
    WATCHLIST_FILE,
    get_company_name_map,
    get_sector_map,
)


HISTORY_COLUMNS = [
    "timestamp_utc",
    "advisor_only",
    "action",
    "ticker",
    "entry",
    "take_profit",
    "stop_loss",
    "confidence",
    "source_freshness",
    "model",
    "telegram_sent",
    "reason",
    "warnings",
]

ACTION_TICKET_COLUMNS = [
    "ticket_id",
    "timestamp_utc",
    "status",
    "action",
    "ticker",
    "entry",
    "take_profit",
    "stop_loss",
    "confidence",
    "source_freshness",
    "evidence_count",
    "reason",
    "warnings",
    "next_step",
]


def _write_csv_header_if_missing(path, columns):
    if not path.exists():
        with path.open("w", newline="", encoding="utf-8") as handle:
            csv.DictWriter(handle, fieldnames=columns).writeheader()
        return
    try:
        existing = list(pd.read_csv(path, nrows=0).columns)
        if existing != columns:
            backup = path.with_name(f"{path.stem}_legacy_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}{path.suffix}")
            path.replace(backup)
            with path.open("w", newline="", encoding="utf-8") as handle:
                csv.DictWriter(handle, fieldnames=columns).writeheader()
            print(f"Archived legacy CSV schema to {backup.name} and created a signal-only {path.name}.")
    except Exception as exc:
        print(f"Warning: could not verify {path.name} schema: {exc}")


def get_local_watchlist():
    if not WATCHLIST_FILE.exists():
        update_local_watchlist(DEFAULT_WATCHLIST)
        return DEFAULT_WATCHLIST

    try:
        df = pd.read_csv(WATCHLIST_FILE)
        if "Watchlist Tier" in df.columns:
            active = df.loc[df["Watchlist Tier"].isin(["CORE", "WATCH"]), "Ticker"].dropna().tolist()
        else:
            active = df.loc[df["AI Status"] == "Active Tracking", "Ticker"].dropna().tolist()
        return active or DEFAULT_WATCHLIST
    except Exception as exc:
        print(f"Warning: could not read watchlist, using defaults. Details: {exc}")
        return DEFAULT_WATCHLIST


def _existing_watchlist_tiers():
    if not WATCHLIST_FILE.exists():
        return {}
    try:
        df = pd.read_csv(WATCHLIST_FILE)
        if "Watchlist Tier" in df.columns:
            return {row["Ticker"]: row.get("Watchlist Tier", "WATCH") for _, row in df.iterrows()}
        return {row["Ticker"]: "CORE" for _, row in df.iterrows() if row.get("AI Status") == "Active Tracking"}
    except Exception:
        return {}


def update_local_watchlist(new_watchlist, signal_rows=None):
    sector_map = get_sector_map()
    company_map = get_company_name_map()
    existing_tiers = _existing_watchlist_tiers()
    signal_map = {row.get("Ticker"): row for row in signal_rows or []}
    rows = []
    for ticker in new_watchlist:
        signal = signal_map.get(ticker, {})
        tier = existing_tiers.get(ticker) or signal.get("Watchlist_Tier") or "WATCH"
        if tier not in {"CORE", "WATCH", "CANDIDATE", "DISABLED"}:
            tier = "WATCH"
        rows.append(
            [
                ticker,
                company_map.get(ticker, f"{ticker.replace('.CA', '')} Company"),
                sector_map.get(ticker, "General"),
                "Active Tracking",
                tier,
                signal.get("Signal_Status", "ACTIVE_TRACKING"),
            ]
        )
    pd.DataFrame(
        rows,
        columns=["Ticker", "Company Name", "Sector", "AI Status", "Watchlist Tier", "Signal Status"],
    ).to_csv(WATCHLIST_FILE, index=False)


def append_trade_history(ticket, source_freshness, model, telegram_sent, warnings):
    _write_csv_header_if_missing(HISTORY_FILE, HISTORY_COLUMNS)

    row = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "advisor_only": True,
        "action": ticket.get("action", "HOLD"),
        "ticker": ticket.get("ticker", ""),
        "entry": ticket.get("entry", 0),
        "take_profit": ticket.get("take_profit", 0),
        "stop_loss": ticket.get("stop_loss", 0),
        "confidence": ticket.get("confidence", "LOW"),
        "source_freshness": source_freshness,
        "model": model,
        "telegram_sent": telegram_sent,
        "reason": ticket.get("trade_reason", ""),
        "warnings": " | ".join(warnings),
    }
    try:
        with HISTORY_FILE.open("a", newline="", encoding="utf-8") as handle:
            csv.DictWriter(handle, fieldnames=HISTORY_COLUMNS).writerow(row)
        return str(HISTORY_FILE)
    except PermissionError:
        fallback = HISTORY_FILE.with_name(f"trade_history_pending_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.csv")
        with fallback.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=HISTORY_COLUMNS)
            writer.writeheader()
            writer.writerow(row)
        print(f"Warning: trade_history.csv is locked. Wrote pending history row to {fallback.name}.")
        return str(fallback)


def merge_pending_history_files():
    pending_files = sorted(HISTORY_FILE.parent.glob("trade_history_pending_*.csv"))
    if not pending_files:
        return []

    _write_csv_header_if_missing(HISTORY_FILE, HISTORY_COLUMNS)
    merged = []
    try:
        with HISTORY_FILE.open("a", newline="", encoding="utf-8") as output:
            writer = csv.DictWriter(output, fieldnames=HISTORY_COLUMNS)
            for pending in pending_files:
                with pending.open("r", newline="", encoding="utf-8") as handle:
                    for row in csv.DictReader(handle):
                        writer.writerow({column: row.get(column, "") for column in HISTORY_COLUMNS})
                pending.unlink()
                merged.append(pending.name)
        return merged
    except PermissionError:
        print("Warning: trade_history.csv is locked. Pending history rows could not be merged yet.")
        return []


def append_action_ticket(ticket, source_freshness, warnings, evidence_packets):
    _write_csv_header_if_missing(ACTION_TICKETS_FILE, ACTION_TICKET_COLUMNS)
    action = str(ticket.get("action", "HOLD")).upper()
    if action in {"BUY", "SELL"}:
        status = "PENDING_REVIEW"
        next_step = "Review the Telegram summary, verify in Thndr, and choose any position size manually."
    else:
        status = "NO_ACTION"
        next_step = "No trade signal. Review watchlist, sector movement, and warnings."
    if any("blocked" in warning.lower() for warning in warnings):
        status = "BLOCKED"
        next_step = "Do not execute. Fix missing data/evidence first."

    ticker = ticket.get("ticker", "")
    evidence_count = len((evidence_packets.get(ticker, {}) or {}).get("items", []))
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    row = {
        "ticket_id": f"{timestamp}_{action}_{ticker or 'NONE'}",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "action": action,
        "ticker": ticker,
        "entry": ticket.get("entry", 0),
        "take_profit": ticket.get("take_profit", 0),
        "stop_loss": ticket.get("stop_loss", 0),
        "confidence": ticket.get("confidence", "LOW"),
        "source_freshness": source_freshness,
        "evidence_count": evidence_count,
        "reason": ticket.get("trade_reason", ""),
        "warnings": " | ".join(warnings),
        "next_step": next_step,
    }
    try:
        with ACTION_TICKETS_FILE.open("a", newline="", encoding="utf-8") as handle:
            csv.DictWriter(handle, fieldnames=ACTION_TICKET_COLUMNS).writerow(row)
        return row["ticket_id"]
    except PermissionError:
        fallback = ACTION_TICKETS_FILE.with_name(f"action_tickets_pending_{timestamp}.csv")
        with fallback.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=ACTION_TICKET_COLUMNS)
            writer.writeheader()
            writer.writerow(row)
        print(f"Warning: action_tickets.csv is locked. Wrote pending ticket to {fallback.name}.")
        return row["ticket_id"]
