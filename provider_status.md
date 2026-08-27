# Provider Status

Generated UTC: 2026-08-27T16:50:26.579228+00:00
Generated Cairo: 2026-08-27 19:50
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-08-27 19:50 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-08-27 19:47

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 CONSTRUCTIVE / EGX70 MIXED / sector breadth 42.86% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 186/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 181/189
- Current/Yahoo technical mismatches blocked: 3/189
- DirectFN public table health only, not trusted for action tickets: 255 rows | as_of=2026-08-27T16:47:13.126048+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 22
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260827T165026Z_BUY_EBSC.CA, 20260827T165026Z_BUY_SPIN.CA, 20260827T165026Z_BUY_MCQE.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for CCRS.CA matches the company but appears old; latest detected date is 2016-01-01.
