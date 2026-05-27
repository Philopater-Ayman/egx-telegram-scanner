# Project Handoff

## Current Product Shape

This is a Telegram-first EGX scanner, not an auto-trading broker. The main command is `python trading_bot_core.py`. It uses deterministic scanner rules for tickets, Gemini for grounded evidence when available, and OpenRouter free-model fallback for Telegram narrative. It produces up to three prioritized signal-only action tickets, a full Telegram summary, report files, and scanner CSV logs.

## Runtime Flow

1. Check `market_calendar.csv`; exit without new tickets if the date is closed.
2. Load watchlist rows from `watchlist.csv`.
3. Fetch market context from the public Mubasher EGX page fallback.
4. Fetch active universe OHLCV through yfinance, with manual fallback data only when available.
5. Calculate deterministic indicators, liquidity spikes, sector scores, EGX30/EGX70 regime, sector breadth, risk mode, and scanner rank.
6. Write scanner artifacts: `market_prices.csv`, `indicators.csv`, `sector_scores.csv`, `scan_results.csv`, `watchlist_signals.csv`, and `data_quality.csv`.
7. Gather evidence for the top candidates with local sources and Gemini grounding only if enabled.
8. Create up to three deterministic advisor-only signal tickets from the evidence-backed candidate pool.
9. Ask OpenRouter for a concise narrative summary when enabled.
10. Apply deterministic risk gates.
11. Write `daily_report.md`, `provider_status.md`, `action_tickets.csv`, and `trade_history.csv`.
12. Send Telegram if enabled.

## Automation

GitHub Actions is the only scheduled automation path. Windows Task Scheduler has been removed to prevent duplicate or confusing Telegram timing.

The workflow targets 09:30, 12:30, 16:00, and 20:00 Africa/Cairo from Sunday through Thursday. Because GitHub cron is UTC, the workflow uses paired UTC schedules for Egypt UTC+2/UTC+3 plus a Cairo-time gate.

Successful cloud runs commit generated scanner outputs back to GitHub. After a long laptop shutdown, pull the repository to receive the latest cloud-generated reports, prices, indicators, tickets, and trade history.

## Non-Negotiable Guardrails

- Never auto-execute trades.
- Never invent live data.
- Never treat delayed/public macro data as live execution-grade data.
- Never allow a quote-only fallback to support BUY by itself because it has no volume/history.
- If evidence is missing or unrelated, do not support BUY.
- If EGX30/EGX70 regime and sector breadth are defensive, send HOLD instead of forcing BUY tickets.
- Keep secrets only in `.env` locally or GitHub repository secrets remotely.
