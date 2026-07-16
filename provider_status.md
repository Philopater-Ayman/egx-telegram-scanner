# Provider Status

Generated UTC: 2026-07-16T10:06:55.629963+00:00
Generated Cairo: 2026-07-16 13:06
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-07-16 13:06 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-07-16 13:02

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 CONSTRUCTIVE / EGX70 BULLISH / sector breadth 71.43% / risk mode BROAD_RISK_ON
- Market data: 175/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 182/189
- Current/Yahoo technical mismatches blocked: 14/189
- DirectFN public table health only, not trusted for action tickets: 236 rows | as_of=2026-07-16T10:03:03.408038+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 23
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260716T100655Z_BUY_GBCO.CA, 20260716T100655Z_BUY_MEPA.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
