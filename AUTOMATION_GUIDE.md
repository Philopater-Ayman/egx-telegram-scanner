# EGX Scanner Automation Guide

This project uses GitHub Actions as the only scheduled automation path. The laptop does not need to be open for scheduled Telegram updates.

## Scheduled Cairo Runs

The workflow targets these Africa/Cairo times from Sunday through Thursday:

| Cairo target | Telegram phase | Goal | Your action |
| --- | --- | --- | --- |
| 08:45 | Pre-market risk check | Check overnight/news/evidence risk before the EGX session. This is not a trade-entry confirmation because the market has not opened. | Read the risk notes and candidate list only. Do not buy from this message alone; wait for open liquidity and Thndr price/spread confirmation. |
| 09:15 | Open liquidity confirmation | Prepare the likely open watchlist shortly before the normal 10:00 session. Public data can still be delayed or stale. | Mark candidates to watch in Thndr. Still wait for actual market activity before entering. |
| 11:00 | Intraday liquidity update | Confirm that liquidity/turnover appeared after the session started and detect changing sector breadth. | Consider only candidates that still have clean price action, liquidity, and spread in Thndr. Avoid chasing names already near resistance. |
| 15:30 | Post-close tomorrow tickets | Build the main next-session preparation list after the normal close. | Use it as the first tomorrow watchlist and risk plan. No same-day execution is expected. |
| 19:30 | Evening tomorrow plan | Refresh evidence/narrative and tomorrow's watchlist using end-of-day data. | Treat it as the final evening plan. The next morning message should confirm risk, not invent trades from stale data. |

GitHub cron is UTC, so `.github/workflows/egx-scanner.yml` maps each UTC cron directly to a `SCAN_PHASE`. The old loose Cairo-time gate was removed because delayed GitHub starts could skip or misclassify runs.

GitHub scheduled workflows are not exact alarms. A run may start late, and on rare occasions GitHub may skip a scheduled run during platform load. Future Telegram message 1/3 includes a `Run timing` line showing the intended Cairo target, actual generated Cairo time, and the cron that triggered it. If the target and generated time differ heavily, the scan phase is still the intended phase, but the delivery was delayed.

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

The scanner checks `market_calendar.csv`, loads `stock_universe.csv`, fetches Yahoo/yfinance history for indicators, overlays Mubasher delayed per-stock trading data for current price/volume/turnover when available, calculates indicators, ranks candidates, sends Telegram, and writes local CSV/Markdown outputs in the GitHub runner. DirectFN public table data is treated as provider-health context only, not as a trusted action-ticket price source.

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
