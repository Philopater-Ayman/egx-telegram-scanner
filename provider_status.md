# Provider Status

Generated UTC: 2026-08-19T08:37:56.510198+00:00
Generated Cairo: 2026-08-19 11:37
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-08-19 11:37 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-08-19 11:29

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 BULLISH / EGX70 MIXED / sector breadth 38.1% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 179/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 179/189
- Current/Yahoo technical mismatches blocked: 10/189
- DirectFN public table health only, not trusted for action tickets: 232 rows | as_of=2026-08-19T08:29:30.035576+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 21
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260819T083756Z_BUY_CLHO.CA, 20260819T083756Z_BUY_MOED.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for RTVC.CA: source text did not clearly match RTVC.CA / Remco Tourism Villages Construction.
- Evidence for MILS.CA matches the company but no source/report date was detected.
- Evidence for ACGC.CA matches the company but no source/report date was detected.
