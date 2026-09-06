# Provider Status

Generated UTC: 2026-09-06T11:59:10.060153+00:00
Generated Cairo: 2026-09-06 14:59
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-09-06 14:59 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-09-06 14:52

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BULLISH / EGX70 BULLISH / sector breadth 57.14% / risk mode BROAD_RISK_ON
- Market data: 162/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 184/189
- Current/Yahoo technical mismatches blocked: 27/189
- DirectFN public table health only, not trusted for action tickets: 252 rows | as_of=2026-09-06T11:52:40.909765+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 22
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260906T115910Z_BUY_ALCN.CA, 20260906T115910Z_BUY_FAIT.CA, 20260906T115910Z_BUY_MBSC.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for EGCH.CA matches the company but appears old; latest detected date is 2025-01-01.
