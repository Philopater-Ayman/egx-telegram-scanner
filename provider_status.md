# Provider Status

Generated UTC: 2026-08-31T19:14:44.658995+00:00
Generated Cairo: 2026-08-31 22:14
- Scan phase: Post-close tomorrow tickets
- Run timing: target 15:30 Cairo | generated Cairo 2026-08-31 22:14 | cron 30 12 * * 0-4
- Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-08-31 22:10

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 MIXED / EGX70 BEARISH / sector breadth 42.86% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 154/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 183/189
- Current/Yahoo technical mismatches blocked: 35/189
- DirectFN public table health only, not trusted for action tickets: 250 rows | as_of=2026-08-31T19:10:36.239956+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 21
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260831T191444Z_BUY_SPIN.CA, 20260831T191444Z_BUY_ORWE.CA, 20260831T191444Z_BUY_SKPC.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Evidence for FAIT.CA matches the company but appears old; latest detected date is 2025-01-01.
