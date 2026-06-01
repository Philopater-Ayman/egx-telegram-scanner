# EGX Scanner Automation Guide

This project uses GitHub Actions as the only scheduled automation path. The laptop does not need to be open for scheduled Telegram updates.

## Scheduled Cairo Runs

The workflow targets these Africa/Cairo times from Sunday through Thursday:

- 08:45: pre-market risk/news check. This is not a liquidity confirmation because the session has not opened.
- 09:15: open preparation before the normal 10:00 EGX session.
- 11:00: delayed liquidity confirmation after enough session activity should be visible.
- 15:30: post-close review after the normal 14:30 close.
- 19:30: evening tomorrow-plan refresh.

GitHub cron is UTC, so `.github/workflows/egx-scanner.yml` maps each UTC cron directly to a `SCAN_PHASE`. The old loose Cairo-time gate was removed because delayed GitHub starts could skip or misclassify runs.

## Required GitHub Secrets

Set these in the GitHub repository:

- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`
- `GEMINI_API_KEY`
- `OPENROUTER_API_KEY`

Optional repository variables:

- `GEMINI_MODEL`
- `OPENROUTER_MODEL`
- `OPENROUTER_FALLBACK_MODELS`

## What The Cloud Run Does

Each accepted scheduled run executes:

```powershell
python trading_bot_core.py
```

The scanner checks `market_calendar.csv`, loads `stock_universe.csv`, fetches Yahoo/yfinance history for indicators, overlays DirectFN delayed current trading data for price/volume/turnover when available, calculates indicators, ranks candidates, sends Telegram, and writes local CSV/Markdown outputs in the GitHub runner.

After a successful run, the workflow commits these generated outputs back to the repository:

- `daily_report.md`
- `provider_status.md`
- `automation_status.md`
- `action_tickets.csv`
- `trade_history.csv`
- `market_prices.csv`
- `indicators.csv`
- `sector_scores.csv`
- `scan_results.csv`
- `data_quality.csv`
- `watchlist_signals.csv`
- `watchlist.csv`

When you reopen the laptop after time away, run `git pull` to bring those cloud-generated files into the local project.

## Market Calendar

`market_calendar.csv` blocks official holidays and special closures. The scanner exits without creating new tickets when the date is marked `CLOSED`.

For Eid al-Adha 2026, EGX is marked closed from `2026-05-26` through `2026-05-31`, with trading resuming on `2026-06-01`.

## Manual Only

The scanner never executes broker orders. Any BUY/SELL action remains a manual Thndr decision.
