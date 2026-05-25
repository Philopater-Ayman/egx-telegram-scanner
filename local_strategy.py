from config import MIN_DAILY_LIQUIDITY_EGP, REQUIRE_FLOW_FOR_BUY


def _float(value, default=0.0):
    try:
        value = float(value)
        if value != value:
            return default
        return value
    except Exception:
        return default


def _hold(watchlist, reason):
    return {
        "updated_watchlist": watchlist[:5],
        "watchlist_changes_reason": "Local fallback kept the current watchlist.",
        "trade_recommendation": {
            "action": "HOLD",
            "ticker": "",
            "entry": 0,
            "take_profit": 0,
            "stop_loss": 0,
            "confidence": "LOW",
            "trade_reason": reason,
        },
        "trade_recommendations": [],
    }


def _ticket_from_row(row, macro_trend):
    ticker = row.get("Ticker")
    price = _float(row.get("Current_Price"))
    ma20 = _float(row.get("MA20"))
    ma50 = _float(row.get("MA50"))
    rsi = _float(row.get("RSI"), 50)
    support_20d = _float(row.get("Support_20D"))
    resistance_20d = _float(row.get("Resistance_20D"))

    support_stop = support_20d * 0.985 if support_20d and support_20d < price else 0
    stop_loss = round(max(price * 0.96, ma20 * 0.98, support_stop), 2)
    if stop_loss >= price:
        stop_loss = round(price * 0.97, 2)
    risk = price - stop_loss
    risk_reward_target = price + (risk * 2)
    resistance_target = resistance_20d * 0.995 if resistance_20d and resistance_20d > price else 0
    take_profit = round(max(risk_reward_target, resistance_target), 2)
    confidence = "MEDIUM" if macro_trend != "Bearish" and rsi <= 65 else "LOW"
    setup_label = "BUY SETUP"
    if confidence == "LOW":
        setup_label = "LOW-CONFIDENCE BUY SETUP"
    if macro_trend == "Bearish" or rsi > 65:
        setup_label = "WATCH/BUY SETUP"
    return {
        "action": "BUY",
        "setup_label": setup_label,
        "ticker": ticker,
        "entry": round(price, 2),
        "take_profit": take_profit,
        "stop_loss": stop_loss,
        "confidence": confidence,
        "priority_score": row.get("Rank_Score", 0),
        "outlook_label": row.get("Outlook_Label", ""),
        "outlook_score": row.get("Outlook_Score", 0),
        "risk_notes": row.get("Risk_Notes", ""),
        "trade_reason": (
            f"{setup_label}: {ticker} has fresh Yahoo price data, liquidity above threshold, "
            f"price above MA20/MA50, RSI {rsi}, support {support_20d}, resistance {resistance_20d}, and evidence sources. Macro trend is {macro_trend}; "
            "verify price action in Thndr before treating it as a swing entry."
        ),
    }


def _passes_final_buy_checks(row, evidence_packets):
    ticker = row.get("Ticker")
    evidence_packet = evidence_packets.get(ticker, {}) or {}
    evidence_items = evidence_packet.get("items", [])
    evidence_status = evidence_packet.get("evidence_status")
    price = _float(row.get("Current_Price"))
    ma20 = _float(row.get("MA20"))
    ma50 = _float(row.get("MA50"))
    rsi = _float(row.get("RSI"), 50)
    liquidity = _float(row.get("Daily_Liquidity_EGP"))
    resistance_20d = _float(row.get("Resistance_20D"))
    resistance_distance = _float(row.get("Resistance_Distance_%"))
    fresh = row.get("Price_Freshness") == "FRESH"

    if not evidence_items or evidence_status != "RECENT_ACCEPTED" or not fresh or liquidity < MIN_DAILY_LIQUIDITY_EGP:
        return False
    if not row.get("Buy_Ready"):
        return False
    if not (price > ma20 and price >= ma50 and 35 <= rsi <= 70):
        return False
    if resistance_20d and resistance_20d > price and resistance_distance < 2:
        return False
    return True


def build_local_fallback_decisions(ranked_rows, current_watchlist, egx30_data, evidence_packets, flow_status=None, max_tickets=3):
    flow_status = flow_status or {"status": "FLOW_MISSING", "regime": "MISSING"}

    if flow_status.get("status") != "FLOW_AVAILABLE" and REQUIRE_FLOW_FOR_BUY:
        return _hold(
            current_watchlist,
            "Local scanner HOLD: institution-flow data is missing or weak, so no new BUY is allowed.",
        )
    if flow_status.get("regime") in {"INSTITUTION_OUTFLOW", "INSTITUTION_SELL_PRESSURE"}:
        return _hold(
            current_watchlist,
            f"Local scanner HOLD: institution-flow regime is {flow_status.get('regime')}, so new BUY is blocked.",
        )

    macro_freshness = egx30_data.get("Freshness")
    macro_trend = egx30_data.get("Trend")
    if macro_freshness not in {"FRESH", "DELAYED"}:
        return _hold(current_watchlist, "Local fallback HOLD: macro source is missing, so no new BUY is allowed.")

    tickets = []
    for row in ranked_rows:
        if _passes_final_buy_checks(row, evidence_packets):
            ticket = _ticket_from_row(row, macro_trend)
            if flow_status.get("status") != "FLOW_AVAILABLE":
                ticket["confidence"] = "LOW"
            ticket["priority"] = len(tickets) + 1
            tickets.append(ticket)
        if len(tickets) >= max_tickets:
            break

    if tickets:
        tickers = [ticket["ticker"] for ticket in tickets]
        return {
            "updated_watchlist": tickers + [item for item in current_watchlist if item not in tickers],
            "watchlist_changes_reason": "Local fallback selected the highest-ranked fresh tickers with evidence and acceptable swing-trade technicals.",
            "trade_recommendation": tickets[0],
            "trade_recommendations": tickets,
        }

    return _hold(current_watchlist, "Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.")


def build_local_fallback_decision(ranked_rows, current_watchlist, egx30_data, evidence_packets, flow_status=None):
    return build_local_fallback_decisions(ranked_rows, current_watchlist, egx30_data, evidence_packets, flow_status, max_tickets=1)
