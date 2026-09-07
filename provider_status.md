# Provider Status

Generated UTC: 2026-09-07T20:07:33.997122+00:00
Generated Cairo: 2026-09-07 23:07
- Scan phase: Evening tomorrow plan
- Run timing: target 19:30 Cairo | generated Cairo 2026-09-07 23:07 | cron 30 16 * * 0-4
- Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-09-07 23:03

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 BULLISH / EGX70 BULLISH / sector breadth 71.43% / risk mode BROAD_RISK_ON
- Market data: 178/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 184/189
- Current/Yahoo technical mismatches blocked: 11/189
- DirectFN public table health only, not trusted for action tickets: 253 rows | as_of=2026-09-07T20:03:10.617424+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 21
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260907T200733Z_BUY_IFAP.CA, 20260907T200733Z_BUY_CIEB.CA, 20260907T200733Z_BUY_ARAB.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for CICH.CA: source text did not clearly match CICH.CA / CI Capital Holding.
- Evidence for SIPC.CA matches the company but appears old; latest detected date is 2024-06-25.
- Evidence for FAIT.CA matches the company but appears old; latest detected date is 2025-01-01.
