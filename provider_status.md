# Provider Status

Generated UTC: 2026-07-20T14:42:51.314605+00:00
Generated Cairo: 2026-07-20 17:42
- Scan phase: Post-close tomorrow tickets
- Run timing: target 15:30 Cairo | generated Cairo 2026-07-20 17:42 | cron 30 12 * * 0-4
- Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-07-20 17:36

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 CONSTRUCTIVE / EGX70 BULLISH / sector breadth 47.62% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 165/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 184/189
- Current/Yahoo technical mismatches blocked: 24/189
- DirectFN public table health only, not trusted for action tickets: 249 rows | as_of=2026-07-20T14:37:03.504273+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 17
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260720T144251Z_BUY_ARCC.CA, 20260720T144251Z_BUY_EALR.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence rejected for RTVC.CA: source text did not clearly match RTVC.CA / Remco Tourism Villages Construction.
- Evidence for WKOL.CA matches the company but appears old; latest detected date is 2025-01-01.
