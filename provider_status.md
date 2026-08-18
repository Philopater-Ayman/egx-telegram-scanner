# Provider Status

Generated UTC: 2026-08-18T08:33:04.264873+00:00
Generated Cairo: 2026-08-18 11:33
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-08-18 11:33 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-08-18 11:28

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 MIXED / EGX70 BULLISH / sector breadth 57.14% / risk mode SELECTIVE_SMALL_MID_SWINGS
- Market data: 141/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 175/189
- Current/Yahoo technical mismatches blocked: 48/189
- DirectFN public table health only, not trusted for action tickets: 234 rows | as_of=2026-08-18T08:28:41.559656+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 24
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260818T083304Z_BUY_ETEL.CA, 20260818T083304Z_BUY_SCTS.CA, 20260818T083304Z_BUY_CIEB.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
