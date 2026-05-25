# Project Handoff

## Current Product Shape

This is a Telegram-first EGX scanner, not an auto-trading broker. The main command is `python trading_bot_core.py`. It uses deterministic scanner rules for tickets, Gemini for grounded evidence when available, and OpenRouter free-model fallback for Telegram narrative. It produces up to three prioritized signal-only action tickets, a full Telegram summary, report files, and scanner CSV logs.

## Runtime Flow

1. Load watchlist from `watchlist.csv`.
3. Fetch market context from Mubasher delayed EGX page fallback.
4. Fetch active universe OHLCV through yfinance, with `manual_market_data.csv` as an optional fallback and StockAnalysis as quote-only public fallback.
5. Calculate deterministic indicators, liquidity spikes, sector scores, and scanner rank.
7. Write scanner artifacts: `market_prices.csv`, `indicators.csv`, `sector_scores.csv`, `scan_results.csv`, `watchlist_signals.csv`, and `data_quality.csv`.
8. Gather evidence for the top candidates with local sources and Gemini grounding only if enabled. `EVIDENCE_TOP_N=8` is the current default.
9. Create up to three deterministic advisor-only signal tickets from the evidence-backed candidate pool. `USE_AI_DECISION` should stay false; AI is evidence/narrative support only.
10. Ask OpenRouter for a concise narrative summary if `OPENROUTER_API_KEY` and `USE_OPENROUTER_NARRATIVE=true` are set.
10. Apply deterministic risk gates, including institution-flow BUY blocking.
11. Write `daily_report.md`, `provider_status.md`, `action_tickets.csv`, and `trade_history.csv`.
12. Send Telegram if enabled.

## Daily Use Loop

The user reads Telegram only. Local CSV and Markdown files are internal logs. Tickets include priority, action, ticker, entry, TP, SL, confidence, evidence quality, sector movement, liquidity regime, and 1-3 day outlook. Tickets do not include quantity or cash sizing.

## Automation

`AUTOMATION_GUIDE.md` describes the intended schedule. GitHub Actions is the preferred always-on path for a public repo. `install_windows_tasks.ps1` remains a local fallback. `market_calendar.csv` is the override for official holidays, Ramadan hours, and special sessions.

## Non-Negotiable Guardrails

- Never auto-execute trades.
- Never invent live data.
- Never treat delayed/public macro data as live execution-grade data.
- The product no longer asks the user to manually search for institution-flow data every day. If an automated reliable source is added later, confirmed institution outflow can be reintroduced as a risk block.
- Never allow a StockAnalysis quote-only fallback to support BUY by itself because it has no volume/history.
- If evidence is missing or unrelated, do not support BUY.
- Keep secrets only in `.env`.
