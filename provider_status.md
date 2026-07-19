# Provider Status

Generated UTC: 2026-07-19T09:50:54.381031+00:00
Generated Cairo: 2026-07-19 12:50
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-07-19 12:50 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-07-19 12:47

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 CONSTRUCTIVE / EGX70 BULLISH / sector breadth 52.38% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 171/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 179/189
- Current/Yahoo technical mismatches blocked: 18/189
- DirectFN public table health only, not trusted for action tickets: 235 rows | as_of=2026-07-19T09:47:37.308284+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 24
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260719T095054Z_BUY_ELEC.CA, 20260719T095054Z_BUY_SWDY.CA, 20260719T095054Z_BUY_PHAR.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for CCRS.CA matches the company but appears old; latest detected date is 2016-01-01.
