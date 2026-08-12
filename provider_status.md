# Provider Status

Generated UTC: 2026-08-12T09:10:45.029038+00:00
Generated Cairo: 2026-08-12 12:10
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-08-12 12:10 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-08-12 12:06

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BULLISH / EGX70 BULLISH / sector breadth 61.9% / risk mode BROAD_RISK_ON
- Market data: 169/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 179/189
- Current/Yahoo technical mismatches blocked: 20/189
- DirectFN public table health only, not trusted for action tickets: 248 rows | as_of=2026-08-12T09:06:22.741863+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 24
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260812T091045Z_BUY_SUGR.CA, 20260812T091045Z_BUY_SAUD.CA, 20260812T091045Z_BUY_PHDC.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for EHDR.CA matches the company but appears old; latest detected date is 2025-01-01.
