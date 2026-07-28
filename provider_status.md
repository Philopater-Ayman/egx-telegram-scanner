# Provider Status

Generated UTC: 2026-07-28T10:35:05.342106+00:00
Generated Cairo: 2026-07-28 13:35
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-07-28 13:35 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-07-28 13:29

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 CONSTRUCTIVE / EGX70 BULLISH / sector breadth 57.14% / risk mode BROAD_RISK_ON
- Market data: 181/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 180/189
- Current/Yahoo technical mismatches blocked: 8/189
- DirectFN public table health only, not trusted for action tickets: 250 rows | as_of=2026-07-28T10:29:05.428901+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 21
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260728T103505Z_BUY_NCCW.CA, 20260728T103505Z_BUY_AJWA.CA, 20260728T103505Z_BUY_COMI.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence for AALR.CA matches the company but no source/report date was detected.
