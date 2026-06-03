# Gemini EGX Copilot

Private advisor-only EGX trading scanner. It scans a local EGX universe, collects market data/history, calculates deterministic liquidity/trend/sector/support-resistance/flow/outlook signals, checks EGX30/EGX70 market regime, creates up to three prioritized signal-only action tickets, sends a full Telegram report, and writes local CSV/Markdown logs. Gemini is used for grounded evidence when available; OpenRouter is used for narrative explanation. Local scanner rules create the tickets.

## Daily Use

1. Edit `watchlist.csv` only if you want to force stocks into active tracking.
2. Run manually only when you want an immediate scan:

```powershell
python trading_bot_core.py
```

3. Read the Telegram message. Local CSV/Markdown files are internal logs only.

The bot never executes trades automatically.

## Telegram-First Tickets

Tickets are signal-only. The scanner can send up to three prioritized tickets, with priority #1 being the highest-ranked swing-trade setup after evidence, liquidity, trend, RSI, support/resistance, sector, and data-quality gates. They include action, ticker, entry, take profit, stop loss, support, resistance, confidence, liquidity context, sector context, evidence quality, warnings, and a transparent 1-3 day outlook. They do not include quantity or cash sizing.

## Automation

GitHub Actions is the only scheduled automation path. Windows Task Scheduler is intentionally not used, so closing the laptop does not stop the scheduled cloud runs.

For GitHub Actions, publish the repo and add these repository secrets: `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`, `GEMINI_API_KEY`, and `OPENROUTER_API_KEY`. The workflow is already in `.github/workflows/egx-scanner.yml`. OpenRouter fallback is capped at 3 models because the API rejects larger fallback arrays.

Scheduled runs target Cairo time:

- 08:45: pre-market risk/news check before the 10:00 session.
- 09:15: open preparation.
- 11:00: delayed liquidity confirmation after the session has started.
- 15:30: post-close report and action-ticket refresh.
- 19:30: evening tomorrow-plan refresh.

GitHub cron runs in UTC. Each scheduled cron maps directly to a `SCAN_PHASE`; the scanner no longer uses a loose Cairo-time gate. GitHub scheduled workflows can start late or occasionally skip during platform load, so Telegram message 1/3 includes the intended Cairo target and actual generated Cairo time for audit.

Add official holidays, Ramadan hours, or special sessions to `market_calendar.csv`. If a date is marked `CLOSED`, scheduled scanner runs exit without creating a new ticket.

Each successful GitHub run commits the generated scanner outputs back to the repository: `daily_report.md`, `provider_status.md`, `automation_status.md`, `action_tickets.csv`, `trade_history.csv`, `market_prices.csv`, `indicators.csv`, `sector_scores.csv`, `scan_results.csv`, `data_quality.csv`, `watchlist_signals.csv`, and `watchlist.csv`.

## Important Files

- `.env`: private API keys and settings. Do not share it.
- `watchlist.csv`: active tracking list with `CORE`, `WATCH`, `CANDIDATE`, or `DISABLED` tiers.
- `action_tickets.csv`: scanner tickets and status.
- `trade_history.csv`: durable recommendation history.
- `daily_report.md`: human-readable daily report.
- `provider_status.md`: source health and warnings.
- `automation_status.md`: latest cloud-run phase, schedule, Telegram status, and provider health.
- `stock_universe.csv`: active EGX candidate universe with sector, index tags, and Yahoo symbol. Expanded rows tagged `YAHOO_VERIFIED_EXPANSION` had usable Yahoo history when added.
- `market_prices.csv`: latest collected price/volume snapshot for scanned tickers.
- `indicators.csv`: deterministic indicators such as MA20/MA50/MA200, RSI, MACD, liquidity spike, returns, volatility, support, and resistance.
- `sector_scores.csv`: sector rotation leaderboard.
- `market_calendar.csv`: local holiday/Ramadan/special-session override file.
- `scan_results.csv`: deterministic scanner ranking and BUY block reasons.
- `watchlist_signals.csv`: latest flow/watchlist signal summary.
- `data_quality.csv`: provider success/failure, freshness, liquidity, and manual-fix recommendations.

## Current Free Sources

- Yahoo/yfinance for EGX ticker OHLCV when available.
- Mubasher delayed per-stock pages for current price, volume, turnover, and liquidity when Yahoo volume is stale or zero.
- DirectFN public table is kept for provider health only and is not trusted for action-ticket prices.
- Mubasher EGX page for delayed EGX30 macro fallback.
- StockAnalysis EGX public list as quote-only fallback when Yahoo has no rows. This has no volume/history, so it cannot support BUY by itself.
- Gemini Google Search grounding for evidence and citations when enabled.
- OpenRouter free-model fallback for Telegram narrative explanation when enabled.
- Yahoo news items as fallback evidence when available.
- Optional NewsData.io key can be added later in `.env`.

## Safety Rules

- Advisor-only mode: manual Thndr execution only.
- BUY must have fresh or delayed-current ticker data, acceptable liquidity, support/resistance-aware stop loss and take profit, and evidence.
- Defensive EGX30/EGX70 market regime blocks new BUY tickets and sends HOLD.
- Tickets are signal-only. Choose position size manually in Thndr.
- Delayed macro data caps confidence.
- Missing or weak evidence downgrades/block BUY.
