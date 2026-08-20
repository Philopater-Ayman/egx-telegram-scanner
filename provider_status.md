# Provider Status

Generated UTC: 2026-08-20T13:28:46.605938+00:00
Generated Cairo: 2026-08-20 16:28
- Scan phase: Post-close tomorrow tickets
- Run timing: target 15:30 Cairo | generated Cairo 2026-08-20 16:28 | cron 30 12 * * 0-4
- Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-08-20 16:24

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 BULLISH / EGX70 MIXED / sector breadth 38.1% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 172/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 183/189
- Current/Yahoo technical mismatches blocked: 17/189
- DirectFN public table health only, not trusted for action tickets: 249 rows | as_of=2026-08-20T13:24:35.916940+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 18
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260820T132846Z_BUY_KABO.CA, 20260820T132846Z_BUY_ALCN.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Mubasher stock page returned no evidence titles for LUTS.CA.
- No Yahoo or Mubasher evidence found for LUTS.CA.
- Evidence rejected for LUTS.CA: source text did not clearly match LUTS.CA / Lotus Agri Capital.
- Evidence for MILS.CA matches the company but no source/report date was detected.
