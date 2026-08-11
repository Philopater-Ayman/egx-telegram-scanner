# Provider Status

Generated UTC: 2026-08-11T08:55:44.373678+00:00
Generated Cairo: 2026-08-11 11:55
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-08-11 11:55 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-08-11 11:47

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 BULLISH / EGX70 BULLISH / sector breadth 47.62% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 131/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 179/189
- Current/Yahoo technical mismatches blocked: 58/189
- DirectFN public table health only, not trusted for action tickets: 232 rows | as_of=2026-08-11T08:48:07.588588+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 24
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260811T085544Z_BUY_GBCO.CA, 20260811T085544Z_BUY_HRHO.CA, 20260811T085544Z_BUY_EFIH.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
