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
    }


def build_local_fallback_decision(ranked_rows, current_watchlist, egx30_data, evidence_packets, flow_status=None):
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

    for row in ranked_rows:
        ticker = row.get("Ticker")
        evidence_items = (evidence_packets.get(ticker, {}) or {}).get("items", [])
        price = _float(row.get("Current_Price"))
        ma20 = _float(row.get("MA20"))
        ma50 = _float(row.get("MA50"))
        rsi = _float(row.get("RSI"), 50)
        liquidity = _float(row.get("Daily_Liquidity_EGP"))
        support_20d = _float(row.get("Support_20D"))
        resistance_20d = _float(row.get("Resistance_20D"))
        resistance_distance = _float(row.get("Resistance_Distance_%"))
        fresh = row.get("Price_Freshness") == "FRESH"

        if not evidence_items or not fresh or liquidity < MIN_DAILY_LIQUIDITY_EGP:
            continue
        if not row.get("Buy_Ready"):
            continue
        if not (price > ma20 and price >= ma50 and 35 <= rsi <= 65):
            continue
        if resistance_20d and resistance_20d > price and resistance_distance < 2:
            continue

        support_stop = support_20d * 0.985 if support_20d and support_20d < price else 0
        stop_loss = round(max(price * 0.96, ma20 * 0.98, support_stop), 2)
        if stop_loss >= price:
            stop_loss = round(price * 0.97, 2)
        risk = price - stop_loss
        risk_reward_target = price + (risk * 2)
        resistance_target = resistance_20d * 0.995 if resistance_20d and resistance_20d > price else 0
        take_profit = round(max(risk_reward_target, resistance_target), 2)
        confidence = "MEDIUM" if macro_trend != "Bearish" else "LOW"
        if flow_status.get("status") != "FLOW_AVAILABLE":
            confidence = "LOW"
        return {
            "updated_watchlist": [ticker] + [item for item in current_watchlist if item != ticker],
            "watchlist_changes_reason": "Local fallback selected the highest-ranked fresh ticker with evidence and acceptable technicals.",
            "trade_recommendation": {
                "action": "BUY",
                "ticker": ticker,
                "entry": round(price, 2),
                "take_profit": take_profit,
                "stop_loss": stop_loss,
                "confidence": confidence,
                "trade_reason": (
                    f"Local fallback BUY candidate: {ticker} has fresh Yahoo price data, liquidity above threshold, "
                    f"price above MA20/MA50, RSI {rsi}, support {support_20d}, resistance {resistance_20d}, and evidence sources. Macro trend is {macro_trend}; "
                    "this is a signal-only ticket, so choose any position size manually in Thndr."
                ),
            },
        }

    return _hold(current_watchlist, "Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.")
