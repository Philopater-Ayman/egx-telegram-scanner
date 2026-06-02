from collections import Counter

from config import MAX_WATCHLIST_SIZE, MIN_DAILY_LIQUIDITY_EGP, REQUIRE_FLOW_FOR_BUY


def enforce_watchlist_limits(watchlist, sector_map):
    clean = []
    sector_counts = Counter()
    for ticker in watchlist:
        if not ticker:
            continue
        sector = sector_map.get(ticker, "General")
        if ticker in clean or sector_counts[sector] >= 2:
            continue
        clean.append(ticker)
        sector_counts[sector] += 1
        if len(clean) >= MAX_WATCHLIST_SIZE:
            break
    return clean


def apply_risk_gates(decision, market_data, egx30_data, evidence_packets, flow_status=None, market_regime=None):
    flow_status = flow_status or {"status": "FLOW_MISSING", "regime": "MISSING"}
    market_regime = market_regime or {}
    warnings = []

    trades = decision.get("trade_recommendations")
    if isinstance(trades, list) and trades:
        accepted = []
        for trade in trades:
            gated_trade, trade_warnings = _apply_single_trade_gate(
                trade,
                market_data,
                egx30_data,
                evidence_packets,
                flow_status,
                market_regime,
            )
            warnings.extend(trade_warnings)
            if str(gated_trade.get("action", "HOLD")).upper() in {"BUY", "SELL"}:
                accepted.append(gated_trade)

        for index, trade in enumerate(accepted, start=1):
            trade["priority"] = index

        if accepted:
            decision["trade_recommendations"] = accepted
            decision["trade_recommendation"] = accepted[0]
            return decision, warnings

        hold_ticker = (trades[0] or {}).get("ticker", "")
        hold = {
            "action": "HOLD",
            "ticker": hold_ticker,
            "entry": 0,
            "take_profit": 0,
            "stop_loss": 0,
            "confidence": "LOW",
            "priority": 1,
            "trade_reason": "All candidate tickets were downgraded by safety gates.",
        }
        decision["trade_recommendations"] = []
        decision["trade_recommendation"] = hold
        return decision, warnings

    trade = decision.get("trade_recommendation", {}) or {}
    gated_trade, trade_warnings = _apply_single_trade_gate(
        trade,
        market_data,
        egx30_data,
        evidence_packets,
        flow_status,
        market_regime,
    )
    warnings.extend(trade_warnings)
    decision["trade_recommendation"] = gated_trade
    decision["trade_recommendations"] = [gated_trade] if str(gated_trade.get("action", "HOLD")).upper() in {"BUY", "SELL"} else []
    return decision, warnings


def _has_tradeable_current_price(row):
    return row.get("Price_Freshness") in {"FRESH", "DELAYED_CURRENT"} and row.get("Technical_Source_Status") != "UNALIGNED_BLOCKED"


def _apply_single_trade_gate(trade, market_data, egx30_data, evidence_packets, flow_status, market_regime):
    warnings = []
    action = str(trade.get("action", "HOLD")).upper()
    ticker = trade.get("ticker") or ""

    if action not in {"BUY", "SELL", "HOLD"}:
        warnings.append(f"{ticker or 'ticket'}: invalid action; changed to HOLD.")
        action = "HOLD"

    if action == "BUY":
        blocking = []
        ticker_data = market_data.get(ticker)
        evidence = evidence_packets.get(ticker, {})
        evidence_items = evidence.get("items") or []
        evidence_status = evidence.get("evidence_status")
        entry = float(trade.get("entry") or 0)
        take_profit = float(trade.get("take_profit") or 0)
        stop_loss = float(trade.get("stop_loss") or 0)

        if not ticker_data:
            blocking.append("BUY blocked: missing market data.")
        else:
            if not _has_tradeable_current_price(ticker_data):
                blocking.append("BUY blocked: price data is stale, missing, or unaligned.")
            if float(ticker_data.get("Daily_Liquidity_EGP") or 0) < MIN_DAILY_LIQUIDITY_EGP:
                blocking.append("BUY blocked: liquidity is below minimum threshold.")
        if egx30_data.get("Freshness") not in {"FRESH", "DELAYED"}:
            blocking.append("BUY blocked: EGX30 macro data is unavailable or stale.")
        elif egx30_data.get("Freshness") == "DELAYED" and str(trade.get("confidence", "LOW")).upper() == "HIGH":
            warnings.append("BUY adjusted: delayed EGX30 macro data caps confidence at MEDIUM.")
            trade["confidence"] = "MEDIUM"
        if flow_status.get("status") != "FLOW_AVAILABLE" and REQUIRE_FLOW_FOR_BUY:
            blocking.append("BUY blocked: institution-flow data is missing or weak.")
        elif flow_status.get("regime") in {"INSTITUTION_OUTFLOW", "INSTITUTION_SELL_PRESSURE"}:
            blocking.append(f"BUY blocked: institution-flow regime is {flow_status.get('regime')}.")
        if market_regime.get("risk_mode") == "DEFENSIVE_NO_NEW_BUY":
            blocking.append("BUY blocked: EGX30/EGX70 market regime is defensive.")
        if not evidence_items:
            blocking.append("BUY blocked: no relevant grounded evidence source.")
        elif evidence_status != "RECENT_ACCEPTED":
            blocking.append(f"BUY blocked: evidence is not recent accepted evidence ({evidence_status or 'UNKNOWN'}).")
        if entry <= 0:
            blocking.append("BUY blocked: invalid entry.")
        if stop_loss <= 0 or take_profit <= 0 or stop_loss >= entry or take_profit <= entry:
            blocking.append("BUY blocked: invalid stop loss or take profit.")

        if blocking:
            warnings.extend(f"{ticker}: {item}" for item in blocking)
            trade = {
                "action": "HOLD",
                "ticker": ticker,
                "entry": 0,
                "take_profit": 0,
                "stop_loss": 0,
                "confidence": "LOW",
                "trade_reason": "BUY was downgraded to HOLD by safety gates. " + " ".join(blocking),
            }

    if action == "SELL" and ticker and ticker not in market_data:
        warnings.append(f"{ticker}: SELL warning: missing fresh market data; verify manually in Thndr before acting.")

    return trade, warnings
