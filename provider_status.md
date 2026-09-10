# Provider Status

Generated UTC: 2026-09-10T10:05:50.950418+00:00
Generated Cairo: 2026-09-10 13:05
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-09-10 13:05 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-10 13:01

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 CONSTRUCTIVE / EGX70 BEARISH / sector breadth 47.62% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 179/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 182/189
- Current/Yahoo technical mismatches blocked: 10/189
- DirectFN public table health only, not trusted for action tickets: 253 rows | as_of=2026-09-10T10:01:30.554590+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 18
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260910T100550Z_BUY_EFIC.CA, 20260910T100550Z_BUY_POUL.CA, 20260910T100550Z_BUY_FWRY.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for EASB.CA: source text did not clearly match EASB.CA / Egyptian Arabian Company (Themar) for securities Brokerage EAC.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
