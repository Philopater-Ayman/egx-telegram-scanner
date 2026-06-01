import json
from datetime import datetime, timezone

import requests

from config import AUTOMATION_STATUS_FILE, PROVIDER_STATUS_FILE, REPORT_FILE, SEND_TELEGRAM, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from providers import get_directfn_health


def _is_tradeable_price(row):
    return row.get("Price_Freshness") in {"FRESH", "DELAYED_CURRENT"}


PHASE_LABELS = {
    "pre_market": "Pre-market risk check",
    "open_confirm": "Open liquidity confirmation",
    "intraday": "Intraday liquidity update",
    "post_close": "Post-close tomorrow tickets",
    "evening_plan": "Evening tomorrow plan",
    "manual": "Manual scan",
    "daily": "Daily scan",
}


def _phase_label(scan_phase):
    return PHASE_LABELS.get(str(scan_phase or "daily").lower(), str(scan_phase or "daily").replace("_", " ").title())


def _phase_instruction(scan_phase):
    phase = str(scan_phase or "daily").lower()
    if phase == "pre_market":
        return "Before the open, use this as a risk/news check only; wait for live or delayed open liquidity before buying."
    if phase == "open_confirm":
        return "This is the first tradeability check. Only consider candidates with confirmed liquidity, clean spread, and unchanged risk in Thndr."
    if phase == "intraday":
        return "Use this to confirm whether liquidity appeared after the open; do not chase names near resistance."
    if phase == "post_close":
        return "Use this as the main preparation list for the next EGX session."
    if phase == "evening_plan":
        return "Use this as tomorrow's watchlist plan; morning should confirm risk, not invent trades from stale data."
    return "Signal-only mode. Verify price/spread in Thndr and choose size manually."


def _unique(items):
    seen = set()
    unique_items = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        unique_items.append(item)
    return unique_items


def write_daily_report(
    egx30,
    market_data,
    decision,
    evidence_packets,
    warnings,
    backtests=None,
    sector_scores=None,
    flow_status=None,
    scan_failures=None,
    narrative=None,
    market_regime=None,
    scan_phase="daily",
):
    sector_scores = sector_scores or {}
    flow_status = flow_status or {}
    scan_failures = scan_failures or []
    narrative = narrative or {}
    market_regime = market_regime or {}
    trade = decision.get("trade_recommendation", {})
    tickets = decision.get("trade_recommendations") or ([trade] if trade else [])
    buy_ready = [row for row in market_data.values() if row.get("Buy_Ready")]
    tradeable_price_count = sum(1 for row in market_data.values() if _is_tradeable_price(row))
    top_liquidity = sorted(market_data.values(), key=lambda row: float(row.get("Daily_Liquidity_EGP") or 0), reverse=True)[:5]
    top_movers = sorted(market_data.values(), key=lambda row: float(row.get("Liquidity_Spike") or 0), reverse=True)[:5]
    lines = [
        "# Telegram-First EGX Scanner Report",
        "",
        f"Scan phase: {_phase_label(scan_phase)}",
        f"Generated UTC: {datetime.now(timezone.utc).isoformat()}",
        "",
        "## Control Center",
        f"- Action tickets: {len([ticket for ticket in tickets if str(ticket.get('action', '')).upper() in {'BUY', 'SELL'}])} prioritized signal(s)",
        f"- BUY-ready candidates: {len(buy_ready)}",
        f"- Data quality issues: {len(scan_failures)}",
        f"- Tradeable price/liquidity tickers: {tradeable_price_count}/{len(market_data)}",
        f"- Top sector: {next(iter(sorted(sector_scores.values(), key=lambda row: row.get('Sector_Rank', 99))), {}).get('Sector', 'n/a') if sector_scores else 'n/a'}",
        "",
        "## Market Context",
        f"- Market trend: {egx30.get('Trend')}",
        f"- Source: {egx30.get('Source')}",
        f"- As of: {egx30.get('As_Of')}",
        f"- Freshness: {egx30.get('Freshness')}",
        f"- EGX30 regime: {market_regime.get('egx30', {}).get('trend', 'n/a')} / above MA20 {market_regime.get('egx30', {}).get('above_ma20_pct', 'n/a')}% / above MA50 {market_regime.get('egx30', {}).get('above_ma50_pct', 'n/a')}%",
        f"- EGX70 regime: {market_regime.get('egx70', {}).get('trend', 'n/a')} / above MA20 {market_regime.get('egx70', {}).get('above_ma20_pct', 'n/a')}% / above MA50 {market_regime.get('egx70', {}).get('above_ma50_pct', 'n/a')}%",
        f"- Sector breadth: {market_regime.get('sector_breadth_pct', 'n/a')}%",
        f"- Risk mode: {market_regime.get('risk_mode', 'n/a')}",
        "",
        "## Top Liquidity",
    ]
    for row in top_liquidity:
        lines.append(
            f"- {row.get('Ticker')}: liquidity={row.get('Daily_Liquidity_EGP')} spike={row.get('Liquidity_Spike')} score={row.get('Rank_Score')}"
        )
    lines.extend([
        "",
        "## AI Narrative",
        f"- Provider: {narrative.get('provider', 'OpenRouter')} {narrative.get('status', 'NOT_RUN')}",
        f"- Model: {narrative.get('model', '') or 'n/a'}",
        f"- Summary: {narrative.get('summary', 'No AI narrative generated.')}",
    ])
    for bullet in narrative.get("bullets", []):
        lines.append(f"- {bullet}")

    lines.extend([
        "",
        "## Top Liquidity Spikes",
    ])
    for row in top_movers:
        lines.append(
            f"- {row.get('Ticker')}: spike={row.get('Liquidity_Spike')} liquidity={row.get('Daily_Liquidity_EGP')} outlook={row.get('Outlook_Label')} score={row.get('Outlook_Score')} buy_ready={row.get('Buy_Ready')}"
        )
    lines.extend([
        "",
        "## Sector Leaderboard",
    ])
    if sector_scores:
        for item in sorted(sector_scores.values(), key=lambda row: row.get("Sector_Rank", 99))[:8]:
            lines.append(
                f"- #{item.get('Sector_Rank')} {item.get('Sector')}: score={item.get('Sector_Score')} 5d={item.get('Median_5D_Return_%')}% 20d={item.get('Median_20D_Return_%')}% aboveMA50={item.get('Above_MA50_%')}%"
            )
    else:
        lines.append("- No sector scores available.")
    lines.extend([
        "",
        "## Today's Prioritized Action Tickets",
    ])
    active_tickets = [ticket for ticket in tickets if str(ticket.get("action", "HOLD")).upper() in {"BUY", "SELL"}]
    if active_tickets:
        for ticket in active_tickets:
            lines.extend([
                f"- Priority #{ticket.get('priority', '')}: {ticket.get('action', 'HOLD')} {ticket.get('ticker', '')}",
                f"  - Entry: {ticket.get('entry', 0)} | Take profit: {ticket.get('take_profit', 0)} | Stop loss: {ticket.get('stop_loss', 0)}",
                f"  - Confidence: {ticket.get('confidence', 'LOW')} | score={ticket.get('priority_score', '')} | outlook={ticket.get('outlook_label', '')} {ticket.get('outlook_score', '')}",
                f"  - Reason: {ticket.get('trade_reason', '')}",
            ])
    else:
        lines.append(f"- HOLD: {trade.get('trade_reason', 'No ticket passed the final gates.')}")
    lines.extend([
        "",
        "## Thndr Instruction",
        "- Advisor-only signal mode is active. The scanner never executes trades.",
        "- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.",
        "- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.",
        "",
        "## Top 1-3 Day Outlook",
    ])
    for row in sorted(market_data.values(), key=lambda item: float(item.get("Outlook_Score") or 0), reverse=True)[:10]:
        lines.append(
            f"- {row.get('Ticker')}: {row.get('Outlook_Label')} score={row.get('Outlook_Score')} liquidity={row.get('Liquidity_Regime')} sector={row.get('Sector_Momentum')} risk={row.get('Risk_Notes')}"
        )

    lines.extend(["", "## BUY-Ready Candidates"])
    if buy_ready:
        for row in buy_ready[:10]:
            lines.append(
                f"- {row.get('Ticker')}: rank={row.get('Rank_Score')} outlook={row.get('Outlook_Label')} outlook_score={row.get('Outlook_Score')} sector_rank={row.get('Sector_Rank')} price={row.get('Current_Price')} support={row.get('Support_20D')} resistance={row.get('Resistance_20D')} liquidity={row.get('Daily_Liquidity_EGP')}"
            )
    else:
        lines.append("- No BUY-ready candidates. Review block reasons and institution-flow status.")

    lines.extend(["", "## Data Quality Issues"])
    if scan_failures:
        for item in scan_failures:
            lines.append(f"- {item.get('Ticker')}: {item.get('Issue')}")
    else:
        lines.append("- No provider failures.")

    lines.extend(["", "## Ranked Scanner Results"])
    for ticker, data in sorted(market_data.items()):
        lines.append(
            f"- {ticker}: score={data.get('Rank_Score', 'n/a')} buy_ready={data.get('Buy_Ready')} sector_rank={data.get('Sector_Rank')} price={data.get('Current_Price')} support={data.get('Support_20D')} resistance={data.get('Resistance_20D')} source={data.get('Price_Source')} as_of={data.get('Price_As_Of')} freshness={data.get('Price_Freshness')} RSI={data.get('RSI')} liquidity={data.get('Daily_Liquidity_EGP')} spike={data.get('Liquidity_Spike')}"
        )

    lines.extend(["", "## Backtesting Lite"])
    if backtests:
        for item in backtests:
            if item.get("Status") == "OK":
                lines.append(
                    f"- {item.get('Ticker')}: 180d return={item.get('Buy_Hold_Return_%')}%, max drawdown={item.get('Max_Drawdown_%')}%, MA20>MA50 days last20={item.get('MA20_Above_MA50_Days_Last20')}, as_of={item.get('Data_As_Of')}"
                )
            else:
                lines.append(f"- {item.get('Ticker')}: {item.get('Status')} - {item.get('Summary')}")
        lines.append("- These checks are historical context only, not a prediction or guarantee.")
    else:
        lines.append("- No backtesting-lite checks were run.")

    lines.extend(["", "## Evidence"])
    if evidence_packets:
        for ticker, packet in evidence_packets.items():
            latest = packet.get("evidence_latest_date", "") or "n/a"
            age_value = packet.get("evidence_age_days", "")
            age_days = age_value if age_value != "" else "n/a"
            lines.append(
                f"- {ticker}: status={packet.get('evidence_status', 'UNKNOWN')} latest={latest} age_days={age_days} sources={len(packet.get('items', []))} expected={packet.get('expected_company', '')} summary={packet.get('summary', '')}"
            )
            for item in packet.get("items", [])[:3]:
                if isinstance(item, dict):
                    title = item.get("title") or item.get("source") or "source"
                    url = item.get("url") or item.get("link") or ""
                    lines.append(f"  - {title}: {url}")
    else:
        lines.append("- No grounded evidence collected.")

    lines.extend(["", "## Warnings"])
    all_warnings = list(warnings)
    all_warnings.extend(egx30.get("Warnings", []))
    for packet in evidence_packets.values():
        all_warnings.extend(packet.get("warnings", []))
    all_warnings = _unique(all_warnings)
    if all_warnings:
        for warning in all_warnings:
            lines.append(f"- {warning}")
    else:
        lines.append("- No blocking warnings.")

    REPORT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_provider_status(egx30, market_data, evidence_packets, telegram_sent, history_path, ticket_id, flow_status=None, scan_failures=None, narrative=None, market_regime=None, scan_phase="daily"):
    flow_status = flow_status or {}
    scan_failures = scan_failures or []
    narrative = narrative or {}
    market_regime = market_regime or {}
    tradeable_price_count = sum(1 for row in market_data.values() if _is_tradeable_price(row))
    directfn_count = sum(1 for row in market_data.values() if "DirectFN" in str(row.get("Liquidity_Source", "")))
    unaligned_count = sum(1 for row in market_data.values() if row.get("Technical_Source_Status") == "UNALIGNED_BLOCKED")
    directfn_health = get_directfn_health()
    evidence_count = sum(len(packet.get("items", [])) for packet in evidence_packets.values())
    lines = [
        "# Provider Status",
        "",
        f"Generated UTC: {datetime.now(timezone.utc).isoformat()}",
        f"- Scan phase: {_phase_label(scan_phase)}",
        "",
        f"- Macro source: {egx30.get('Source')}",
        f"- Macro freshness: {egx30.get('Freshness')}",
        f"- Macro trend: {egx30.get('Trend')}",
        f"- Market regime: {market_regime.get('summary', 'n/a')}",
        f"- Market data: {tradeable_price_count}/{len(market_data)} tickers have tradeable current/delayed price data",
        f"- DirectFN liquidity rows used: {directfn_count}/{len(market_data)}",
        f"- DirectFN/Yahoo technical mismatches blocked: {unaligned_count}/{len(market_data)}",
        f"- DirectFN health: {directfn_health.get('rows')} rows | as_of={directfn_health.get('as_of') or 'n/a'} | error={directfn_health.get('error') or 'none'}",
        f"- Data quality issues: {len(scan_failures)}",
        f"- Evidence sources found: {evidence_count}",
        f"- AI narrative: {narrative.get('provider', 'OpenRouter')} {narrative.get('status', 'NOT_RUN')} ({narrative.get('model', '') or 'n/a'})",
        f"- Telegram sent on latest run: {telegram_sent}",
        f"- Latest ticket id(s): {', '.join(ticket_id) if isinstance(ticket_id, list) else ticket_id}",
        f"- Latest history write(s): {', '.join(history_path) if isinstance(history_path, list) else history_path}",
        "",
        "## Warnings",
    ]
    warnings = egx30.get("Warnings", [])
    warnings.extend(f"{item.get('Ticker')}: {item.get('Issue')}" for item in scan_failures)
    for packet in evidence_packets.values():
        warnings.extend(packet.get("warnings", []))
    warnings = _unique(warnings)
    if warnings:
        lines.extend(f"- {warning}" for warning in warnings)
    else:
        lines.append("- No provider warnings.")
    PROVIDER_STATUS_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_automation_status(scan_phase, market_day, market_data, telegram_sent):
    directfn_health = get_directfn_health()
    tradeable_price_count = sum(1 for row in market_data.values() if _is_tradeable_price(row))
    directfn_count = sum(1 for row in market_data.values() if "DirectFN" in str(row.get("Liquidity_Source", "")))
    unaligned_count = sum(1 for row in market_data.values() if row.get("Technical_Source_Status") == "UNALIGNED_BLOCKED")
    lines = [
        "# Automation Status",
        "",
        f"Generated UTC: {datetime.now(timezone.utc).isoformat()}",
        f"Scan phase: {_phase_label(scan_phase)}",
        f"Market calendar: {market_day.get('status')} | {market_day.get('label')} | {market_day.get('open_time')}-{market_day.get('close_time')}",
        f"Telegram sent: {telegram_sent}",
        "",
        "## Schedule",
        "- 08:45 Cairo: pre-market risk/news check",
        "- 09:15 Cairo: open preparation",
        "- 11:00 Cairo: delayed liquidity confirmation",
        "- 15:30 Cairo: post-close review",
        "- 19:30 Cairo: tomorrow plan",
        "",
        "## Data Health",
        f"- Tradeable delayed/current price rows: {tradeable_price_count}/{len(market_data)}",
        f"- DirectFN liquidity rows used: {directfn_count}/{len(market_data)}",
        f"- DirectFN/Yahoo technical mismatches blocked: {unaligned_count}/{len(market_data)}",
        f"- DirectFN table rows available: {directfn_health.get('rows')}",
        f"- DirectFN as of: {directfn_health.get('as_of') or 'n/a'}",
        f"- DirectFN error: {directfn_health.get('error') or 'none'}",
    ]
    AUTOMATION_STATUS_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _fmt_num(value):
    try:
        return f"{float(value):,.2f}"
    except Exception:
        return str(value)


def _evidence_quality(evidence_packets):
    packets = evidence_packets or {}
    source_count = sum(len(packet.get("items", [])) for packet in packets.values())
    gemini_packets = [packet for packet in packets.values() if "GEMINI" in str(packet.get("source_mode", ""))]
    recent_count = sum(1 for packet in packets.values() if packet.get("evidence_status") == "RECENT_ACCEPTED")
    old_count = sum(1 for packet in packets.values() if packet.get("evidence_status") == "OLD_ACCEPTED")
    undated_count = sum(1 for packet in packets.values() if packet.get("evidence_status") == "ACCEPTED_UNDATED")
    rejected_count = sum(1 for packet in packets.values() if str(packet.get("evidence_status", "")).startswith("REJECTED"))
    warning_count = sum(len(packet.get("warnings", [])) for packet in packets.values())
    recency = f"{recent_count} recent, {old_count} old, {undated_count} undated, {rejected_count} rejected"
    if gemini_packets and source_count:
        status = f"Gemini helped with grounded citations ({recency})"
    elif warning_count:
        status = f"Gemini/fallback evidence had warnings; scanner still used local rules ({recency})"
    elif source_count:
        status = f"Fallback evidence found public sources ({recency})"
    else:
        status = "No useful public evidence found"
    return status, source_count


def _line_items(rows, formatter, limit=5):
    return "\n".join(formatter(row) for row in rows[:limit]) or "- None"


def _why_not_ticket_rows(ranked, active_tickers, limit=6):
    rows = []
    for row in ranked:
        ticker = row.get("Ticker")
        if ticker in active_tickers:
            continue
        reasons = []
        try:
            rsi = float(row.get("RSI") or 0)
        except Exception:
            rsi = 0
        try:
            resistance_distance = float(row.get("Resistance_Distance_%") or 0)
        except Exception:
            resistance_distance = 0
        if not row.get("Buy_Ready"):
            reasons.append(row.get("Buy_Block_Reasons") or "not BUY-ready after first filters")
        if rsi > 70:
            reasons.append("RSI is too hot")
        if 0 < resistance_distance < 2:
            reasons.append("too close to resistance")
        if not reasons:
            reasons.append("lower priority than final top tickets")
        rows.append({**row, "Skip_Reasons": "; ".join(reasons)})
        if len(rows) >= limit:
            break
    return rows


def _send_telegram_text(text):
    response = requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
        json={"chat_id": TELEGRAM_CHAT_ID, "text": text[:3900]},
        timeout=20,
    )
    if response.status_code != 200:
        print(f"Telegram API error: {response.status_code} {response.text}")
        return False
    return True


def send_telegram_notification(decision, egx30, warnings, market_data=None, sector_scores=None, evidence_packets=None, scan_failures=None, narrative=None, market_regime=None, scan_phase="daily"):
    if not SEND_TELEGRAM:
        print("Telegram disabled by SEND_TELEGRAM=false.")
        return False
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram credentials missing; notification skipped.")
        return False

    trade = decision.get("trade_recommendation", {})
    tickets = decision.get("trade_recommendations") or ([trade] if trade else [])
    active_tickets = [ticket for ticket in tickets if str(ticket.get("action", "HOLD")).upper() in {"BUY", "SELL"}]
    active_tickers = {ticket.get("ticker") for ticket in active_tickets}
    rows = list((market_data or {}).values())
    ranked = sorted(rows, key=lambda row: float(row.get("Rank_Score") or 0), reverse=True)
    buy_ready = [row for row in ranked if row.get("Buy_Ready")]
    liquidity_movers = sorted(rows, key=lambda row: float(row.get("Liquidity_Spike") or 0), reverse=True)
    outlook_rows = sorted(rows, key=lambda row: float(row.get("Outlook_Score") or 0), reverse=True)
    skipped_rows = _why_not_ticket_rows(ranked, active_tickers)
    sectors = sorted((sector_scores or {}).values(), key=lambda row: row.get("Sector_Rank", 99))
    narrative = narrative or {}
    market_regime = market_regime or {}
    evidence_status, source_count = _evidence_quality(evidence_packets)
    tradeable_price_count = sum(1 for row in rows if _is_tradeable_price(row))
    directfn_count = sum(1 for row in rows if "DirectFN" in str(row.get("Liquidity_Source", "")))
    warnings = _unique(warnings)
    warning_text = "\n".join(f"- {item}" for item in warnings[:5]) if warnings else "- None"
    data_quality = f"{tradeable_price_count}/{len(rows)} tradeable delayed/current tickers, {directfn_count} DirectFN liquidity rows, {len(scan_failures or [])} data quality issues"
    ticket_text = _line_items(
        active_tickets,
        lambda ticket: (
            f"#{ticket.get('priority', '')} {ticket.get('action', 'HOLD')} {ticket.get('ticker', '')}\n"
            f"Setup: {ticket.get('setup_label', ticket.get('action', 'HOLD'))}\n"
            f"Entry {_fmt_num(ticket.get('entry', 0))} | TP {_fmt_num(ticket.get('take_profit', 0))} | SL {_fmt_num(ticket.get('stop_loss', 0))}\n"
            f"Confidence {ticket.get('confidence', 'LOW')} | rank score {ticket.get('priority_score', '')} | outlook {ticket.get('outlook_label', '')} {ticket.get('outlook_score', '')}\n"
            f"Risk notes: {ticket.get('risk_notes', '') or 'No major scanner risk flags.'}\n"
            f"Reason: {ticket.get('trade_reason', '')}"
        ),
        limit=3,
    )
    if not active_tickets:
        ticket_text = f"- HOLD: {trade.get('trade_reason', 'No ticket passed the final gates.')}"

    summary_message = "\n".join(
        [
            f"EGX Scanner 1/3 - {_phase_label(scan_phase)}",
            "",
            f"Market: {egx30.get('Trend')} | {egx30.get('Freshness')} | {egx30.get('Source')}",
            f"Market regime: {market_regime.get('risk_mode', 'n/a')} | EGX30 {market_regime.get('egx30', {}).get('trend', 'n/a')} | EGX70 {market_regime.get('egx70', {}).get('trend', 'n/a')} | breadth {market_regime.get('sector_breadth_pct', 'n/a')}%",
            f"Data quality: {data_quality}",
            f"Gemini evidence: {evidence_status} ({source_count} sources)",
            f"Universe awareness: scanned {len(rows)} active stocks, {len(buy_ready)} BUY-ready after first scanner filters",
            "",
            "TOP ACTION TICKETS",
            ticket_text,
            "",
            "How to read this:",
            "- Priority #1 is the strongest setup after ranking, liquidity, trend, RSI, evidence, support/resistance, and risk gates.",
            "- WATCH/BUY SETUP means the technical setup exists, but macro or momentum risk requires extra patience.",
            "- LOW confidence means risk exists; it is not a command to trade.",
            f"- {_phase_instruction(scan_phase)}",
            "- Signal-only mode. No quantity is calculated.",
        ]
    )

    market_message = "\n".join(
        [
            "EGX Scanner 2/3 - Market Map",
            "",
            "Market Regime",
            f"- EGX30: {market_regime.get('egx30', {}).get('trend', 'n/a')} / above MA20 {market_regime.get('egx30', {}).get('above_ma20_pct', 'n/a')}% / above MA50 {market_regime.get('egx30', {}).get('above_ma50_pct', 'n/a')}%",
            f"- EGX70: {market_regime.get('egx70', {}).get('trend', 'n/a')} / above MA20 {market_regime.get('egx70', {}).get('above_ma20_pct', 'n/a')}% / above MA50 {market_regime.get('egx70', {}).get('above_ma50_pct', 'n/a')}%",
            f"- Sector breadth: {market_regime.get('sector_breadth_pct', 'n/a')}%",
            f"- Risk mode: {market_regime.get('risk_mode', 'n/a')}",
            f"- Leading sectors: {', '.join(market_regime.get('leading_sectors', []) or []) or 'n/a'}",
            "",
            "Top ranked by scanner",
            _line_items(
                ranked,
                lambda row: f"- {row.get('Ticker')}: rank {row.get('Rank_Score')} | outlook {row.get('Outlook_Label')} {row.get('Outlook_Score')} | RSI {row.get('RSI')} | S/R {_fmt_num(row.get('Support_20D'))}/{_fmt_num(row.get('Resistance_20D'))} | liq {_fmt_num(row.get('Daily_Liquidity_EGP'))}",
                limit=8,
            ),
            "",
            "BUY-ready candidates",
            _line_items(
                buy_ready,
                lambda row: f"- {row.get('Ticker')}: entry {_fmt_num(row.get('Current_Price'))} | S/R {_fmt_num(row.get('Support_20D'))}/{_fmt_num(row.get('Resistance_20D'))} | outlook {row.get('Outlook_Label')} | sector #{row.get('Sector_Rank')}",
                limit=8,
            ),
            "",
            "Why high-ranked names were not final tickets",
            _line_items(
                skipped_rows,
                lambda row: f"- {row.get('Ticker')}: rank {row.get('Rank_Score')} | {row.get('Skip_Reasons')}",
                limit=6,
            ),
            "",
            "Liquidity movers",
            _line_items(
                liquidity_movers,
                lambda row: f"- {row.get('Ticker')}: spike {row.get('Liquidity_Spike')} | regime {row.get('Liquidity_Regime')} | liq {_fmt_num(row.get('Daily_Liquidity_EGP'))} | {row.get('Liquidity_Source', 'n/a')}",
                limit=8,
            ),
            "",
            "Sector rotation",
            _line_items(
                sectors,
                lambda row: f"- #{row.get('Sector_Rank')} {row.get('Sector')}: score {row.get('Sector_Score')} | 5d {row.get('Median_5D_Return_%')}% | 20d {row.get('Median_20D_Return_%')}% | above MA50 {row.get('Above_MA50_%')}%",
                limit=8,
            ),
            "",
            "1-3 day outlook leaders",
            _line_items(
                outlook_rows,
                lambda row: f"- {row.get('Ticker')}: {row.get('Outlook_Label')} {row.get('Outlook_Score')} | {row.get('Risk_Notes')}",
                limit=8,
            ),
        ]
    )

    narrative_message = "\n".join(
        [
            "EGX Scanner 3/3 - AI Evidence & Warnings",
            "",
            f"AI narrative: {narrative.get('provider', 'OpenRouter')} {narrative.get('status', 'NOT_RUN')} | {narrative.get('model', '') or 'n/a'}",
            f"{narrative.get('summary', '')}",
            _line_items([{"bullet": item} for item in narrative.get("bullets", [])], lambda row: f"- {row.get('bullet')}", limit=5),
            "",
            "Evidence quality",
            f"- {evidence_status}",
            f"- Sources found across top evidence candidates: {source_count}",
            f"- Gemini failure does not stop the scanner; local deterministic rules still create or block tickets.",
            "",
            "Evidence packets",
            _line_items(
                [{"ticker": ticker, **packet} for ticker, packet in (evidence_packets or {}).items()],
                lambda packet: f"- {packet.get('ticker')}: {packet.get('evidence_status', 'UNKNOWN')} | latest {packet.get('evidence_latest_date', 'n/a') or 'n/a'} | age {packet.get('evidence_age_days') if packet.get('evidence_age_days') != '' else 'n/a'}d | {len(packet.get('items', []))} source(s) | {packet.get('source_mode', 'n/a')} | {packet.get('summary', '')[:220]}",
                limit=8,
            ),
            "",
            f"Warnings:\n{warning_text}",
            "",
            "Remember: the scanner can improve discipline and awareness, but it cannot guarantee profit.",
        ]
    )
    try:
        sent = [
            _send_telegram_text(summary_message),
            _send_telegram_text(market_message),
            _send_telegram_text(narrative_message),
        ]
        if all(sent):
            print("Telegram notification sent in 3 messages.")
            return True
        return False
    except Exception as exc:
        print(f"Telegram network error: {exc}")
        return False


def print_ticket(decision, warnings):
    print("\nSCANNER ACTION TICKETS")
    print("======================")
    tickets = decision.get("trade_recommendations") or [decision.get("trade_recommendation", {})]
    print(json.dumps(tickets, indent=2))
    if warnings:
        print("\nSAFETY WARNINGS")
        for warning in warnings:
            print(f"- {warning}")
