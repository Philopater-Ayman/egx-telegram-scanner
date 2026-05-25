from ai_agents import build_openrouter_narrative, gather_batch_evidence
from config import EGX_CANDIDATE_POOL, EVIDENCE_TOP_N, MODEL_NAME, USE_AI_DECISION, get_sector_map, get_yahoo_symbol_map
from local_strategy import build_local_fallback_decisions
from market_calendar import should_run_scanner
from market_scanner import (
    build_watchlist_signal_rows,
    build_sector_scores,
    build_market_regime,
    build_watchlist_from_ranked,
    get_latest_institution_flow,
    rank_candidates,
    write_scanner_outputs,
)
from providers import get_backtest_summary, get_macro_status, get_technical_data
from reporting import print_ticket, send_telegram_notification, write_daily_report, write_provider_status
from risk import apply_risk_gates, enforce_watchlist_limits
from storage import (
    append_trade_histories,
    append_action_tickets,
    get_local_watchlist,
    merge_pending_history_files,
    update_local_watchlist,
)


def run_daily_advisor():
    print("=== Running EGX Scanner Advisor (Advisor Only) ===")
    should_run, market_day = should_run_scanner()
    print(f"Market calendar: {market_day.get('status')} | {market_day.get('label')} | {market_day.get('open_time')}-{market_day.get('close_time')}")
    if not should_run:
        print("Market calendar is CLOSED today. Scanner exits without creating a new action ticket.")
        return
    merged = merge_pending_history_files()
    if merged:
        print(f"Merged pending history files: {', '.join(merged)}")
    active_watchlist = get_local_watchlist()
    print(f"Loaded {len(active_watchlist)} active watchlist tickers.")

    print("Fetching EGX30 macro status...")
    egx30 = get_macro_status()
    print(f"EGX30: {egx30.get('Trend')} | {egx30.get('Freshness')} | {egx30.get('Source')}")

    flow_status = get_latest_institution_flow()

    combined_pool = list(dict.fromkeys(active_watchlist + EGX_CANDIDATE_POOL))
    print(f"Scanning {len(combined_pool)} EGX candidates through the deterministic market scanner...")
    market_data = {}
    scan_failures = []
    sector_map = get_sector_map()
    yahoo_symbol_map = get_yahoo_symbol_map()
    for ticker in combined_pool:
        row = get_technical_data(ticker)
        if row:
            market_data[ticker] = row
        else:
            scan_failures.append(
                {
                    "Ticker": ticker,
                    "Sector": sector_map.get(ticker, "General"),
                    "Provider": f"Yahoo {yahoo_symbol_map.get(ticker, ticker)} / manual_market_data.csv",
                    "Issue": "No usable market data returned. Check Yahoo symbol or add a manual fallback row.",
                }
            )

    sector_scores = build_sector_scores(list(market_data.values()))
    market_regime = build_market_regime(list(market_data.values()), sector_scores)
    print(f"Market regime: {market_regime.get('summary')}")
    ranked_rows = rank_candidates(list(market_data.values()), sector_scores, flow_status, market_regime)
    signal_rows = build_watchlist_signal_rows(ranked_rows, active_watchlist, flow_status)
    write_scanner_outputs(ranked_rows, sector_scores, flow_status, scan_failures, active_watchlist)
    top_for_evidence = ranked_rows[:EVIDENCE_TOP_N]
    print(f"Collected usable market data for {len(market_data)} tickers.")

    use_gemini_evidence = market_regime.get("risk_mode") != "DEFENSIVE_NO_NEW_BUY"
    if use_gemini_evidence:
        print(f"Gathering evidence for top {len(top_for_evidence)} candidates...")
    else:
        print(f"Gathering local fallback evidence for top {len(top_for_evidence)} candidates; Gemini skipped because market regime is defensive.")
    evidence_packets = gather_batch_evidence(top_for_evidence, use_gemini=use_gemini_evidence)

    print("Running lightweight historical checks for top candidates...")
    backtests = [get_backtest_summary(row["Ticker"]) for row in top_for_evidence[:3]]

    deterministic_watchlist = build_watchlist_from_ranked(ranked_rows, active_watchlist)
    decision = build_local_fallback_decisions(
        top_for_evidence,
        deterministic_watchlist,
        egx30,
        evidence_packets,
        flow_status,
        market_regime,
        max_tickets=3,
    )
    if USE_AI_DECISION:
        print("USE_AI_DECISION=true is ignored in Telegram-first mode. Gemini is used for evidence/narrative only.")
    else:
        print("AI decision agent disabled by USE_AI_DECISION=false. Using deterministic scanner decision.")

    decision["updated_watchlist"] = enforce_watchlist_limits(decision.get("updated_watchlist", []), sector_map)
    if not decision["updated_watchlist"]:
        decision["updated_watchlist"] = active_watchlist[:5]

    decision, warnings = apply_risk_gates(decision, market_data, egx30, evidence_packets, flow_status, market_regime)
    update_local_watchlist(decision["updated_watchlist"], signal_rows)

    source_freshness = f"market_context={egx30.get('Freshness')}; fresh_tickers={sum(1 for x in market_data.values() if x.get('Price_Freshness') == 'FRESH')}/{len(market_data)}"
    ranked_market_data = {row["Ticker"]: row for row in ranked_rows}
    narrative = build_openrouter_narrative(decision, ranked_rows, sector_scores, evidence_packets, warnings, market_regime)
    for warning in narrative.get("warnings", []):
        warnings.append(warning)
    write_daily_report(egx30, ranked_market_data, decision, evidence_packets, warnings, backtests, sector_scores, flow_status, scan_failures, narrative, market_regime)
    telegram_sent = send_telegram_notification(decision, egx30, warnings, ranked_market_data, sector_scores, evidence_packets, scan_failures, narrative, market_regime)
    history_paths = append_trade_histories(decision, source_freshness, MODEL_NAME, telegram_sent, warnings)
    ticket_ids = append_action_tickets(decision, source_freshness, warnings, evidence_packets)
    write_provider_status(egx30, ranked_market_data, evidence_packets, telegram_sent, history_paths, ticket_ids, flow_status, scan_failures, narrative, market_regime)
    print_ticket(decision, warnings)
    print("\nCreated/updated daily_report.md, action_tickets.csv, provider_status.md, and trade_history.csv.")
    pending_paths = [path for path in history_paths if "pending" in path]
    if pending_paths:
        print(f"History CSV was locked, so the latest rows were saved to: {', '.join(pending_paths)}.")
    print("Advisor-only mode is active. No trade was executed.")


if __name__ == "__main__":
    run_daily_advisor()
