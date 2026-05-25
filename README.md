# Gemini EGX Copilot

Private advisor-only EGX trading scanner. It scans a local EGX universe, collects market data/history, calculates deterministic liquidity/trend/sector/support-resistance/flow/outlook signals, checks EGX30/EGX70 market regime, creates up to three prioritized signal-only action tickets, sends a full Telegram report, and writes local CSV/Markdown logs. Gemini is used for grounded evidence when available; OpenRouter is used for narrative explanation. Local scanner rules create the tickets.

## Daily Use

1. Edit `watchlist.csv` only if you want to force stocks into active tracking.
2. Run:

```powershell
python trading_bot_core.py
```

3. Read the Telegram message. Local CSV/Markdown files are internal logs only.

The bot never executes trades automatically.

## Telegram-First Tickets

Tickets are signal-only. The scanner can send up to three prioritized tickets, with priority #1 being the highest-ranked swing-trade setup after evidence, liquidity, trend, RSI, support/resistance, sector, and data-quality gates. They include action, ticker, entry, take profit, stop loss, support, resistance, confidence, liquidity context, sector context, evidence quality, warnings, and a transparent 1-3 day outlook. They do not include quantity or cash sizing.

## Automation

Read `AUTOMATION_GUIDE.md` before enabling scheduled runs. GitHub Actions is the preferred always-on free path for public repo automation. Windows Task Scheduler remains a local fallback and only runs while the laptop is awake unless Windows wake settings are configured.

For GitHub Actions, publish the repo and add these repository secrets: `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`, `GEMINI_API_KEY`, and `OPENROUTER_API_KEY`. The workflow is already in `.github/workflows/egx-scanner.yml`. OpenRouter fallback is capped at 3 models because the API rejects larger fallback arrays.

To install default Sunday-Thursday Windows tasks locally, run this manually from PowerShell:

```powershell
.\install_windows_tasks.ps1
```

The scheduled tasks only run the scanner. They do not execute broker orders.

Add official holidays, Ramadan hours, or special sessions to `market_calendar.csv`. If a date is marked `CLOSED`, scheduled scanner runs exit without creating a new ticket.

## Important Files

- `.env`: private API keys and settings. Do not share it.
- `watchlist.csv`: active tracking list with `CORE`, `WATCH`, `CANDIDATE`, or `DISABLED` tiers.
- `action_tickets.csv`: scanner tickets and status.
- `trade_history.csv`: durable recommendation history.
- `daily_report.md`: human-readable daily report.
- `provider_status.md`: source health and warnings.
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
- Mubasher EGX page for delayed EGX30 macro fallback.
- StockAnalysis EGX public list as quote-only fallback when Yahoo has no rows. This has no volume/history, so it cannot support BUY by itself.
- Gemini Google Search grounding for evidence and citations when enabled.
- OpenRouter free-model fallback for Telegram narrative explanation when enabled.
- Yahoo news items as fallback evidence when available.
- Optional NewsData.io key can be added later in `.env`.

## Safety Rules

- Advisor-only mode: manual Thndr execution only.
- BUY must have fresh ticker data, acceptable liquidity, support/resistance-aware stop loss and take profit, and evidence.
- Defensive EGX30/EGX70 market regime blocks new BUY tickets and sends HOLD.
- Tickets are signal-only. Choose position size manually in Thndr.
- Delayed macro data caps confidence.
- Missing or weak evidence downgrades/block BUY.
