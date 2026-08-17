# Provider Status

Generated UTC: 2026-08-17T08:39:55.394785+00:00
Generated Cairo: 2026-08-17 11:39
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-08-17 11:39 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-08-17 11:35

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 MIXED / EGX70 BULLISH / sector breadth 61.9% / risk mode SELECTIVE_SMALL_MID_SWINGS
- Market data: 165/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 177/189
- Current/Yahoo technical mismatches blocked: 24/189
- DirectFN public table health only, not trusted for action tickets: 232 rows | as_of=2026-08-17T08:35:54.040829+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 18
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260817T083955Z_BUY_COPR.CA, 20260817T083955Z_BUY_ETEL.CA, 20260817T083955Z_BUY_RACC.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for AJWA.CA matches the company but no source/report date was detected.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence rejected for ADPC.CA: source text did not clearly match ADPC.CA / The Arab Dairy Products Co..
