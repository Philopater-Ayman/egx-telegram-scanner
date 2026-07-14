# Provider Status

Generated UTC: 2026-07-14T09:57:10.814948+00:00
Generated Cairo: 2026-07-14 12:57
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-07-14 12:57 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-07-14 12:52

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 MIXED / EGX70 BULLISH / sector breadth 47.62% / risk mode SELECTIVE_SMALL_MID_SWINGS
- Market data: 177/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 179/189
- Current/Yahoo technical mismatches blocked: 12/189
- DirectFN public table health only, not trusted for action tickets: 231 rows | as_of=2026-07-14T09:52:16.937221+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 21
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260714T095710Z_BUY_GDWA.CA, 20260714T095710Z_BUY_RAYA.CA, 20260714T095710Z_BUY_ADPC.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for AREH.CA matches the company but no source/report date was detected.
- Evidence for ELEC.CA matches the company but appears old; latest detected date is 2025-03-31.
- Evidence rejected for EGAS.CA: source text did not clearly match EGAS.CA / Natural Gas and Mining Project.
