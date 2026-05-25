# EGX Scanner Automation Guide

This system should run automatically, but it must stay advisor-only. It does not place broker orders.

## Daily Schedule

Use Cairo local time and keep the exact hours configurable because EGX hours can change during Ramadan, holidays, and exchange rule updates.

- Pre-market scan: 08:45
  - Refresh universe data.
  - Check data quality.
  - Review watchlist and scanner context.
  - Send a Telegram brief if enabled.
- Open-prep scan: 09:15
  - Re-run scanner close to market open.
  - Highlight watched names and blocked BUY reasons.
- Midday scan: 12:00
  - Refresh prices and liquidity.
  - Detect unusual liquidity spikes.
  - Do not create aggressive BUY tickets without valid institution-flow data.
- Post-close scan: 15:30
  - Run full scanner after the regular session.
  - Produce `daily_report.md`, `data_quality.csv`, `scan_results.csv`, and `action_tickets.csv`.
- Evening maintenance: 20:00
  - Review provider failures.
  - Update `stock_universe.csv` if symbols failed.
  - Record institution-flow data when available.

## Free Always-On Automation

Use GitHub Actions for scans when the laptop is closed or off. Put API keys in repository secrets, not in code:

- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`
- `GEMINI_API_KEY`

Scheduled GitHub Actions use UTC cron. The included workflow maps the core Cairo scan times to UTC and still lets `market_calendar.csv` block closed days.

## What Can Run Automatically

- Market data collection.
- Indicator calculation.
- Sector ranking.
- Data quality checks.
- Watchlist tier updates.
- Scanner action tickets.
- Telegram notifications.

## What Must Stay Manual

- Actual Thndr order execution.
- Fixing incorrect or stale symbols in `stock_universe.csv`.
- Adding official holidays and special Ramadan trading hours to `market_calendar.csv` when EGX announces them.
