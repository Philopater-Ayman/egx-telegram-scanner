# Provider Status

Generated UTC: 2026-09-03T16:39:00.642715+00:00
Generated Cairo: 2026-09-03 19:39
- Scan phase: Post-close tomorrow tickets
- Run timing: target 15:30 Cairo | generated Cairo 2026-09-03 19:39 | cron 30 12 * * 0-4
- Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-09-03 19:34

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BULLISH / EGX70 MIXED / sector breadth 42.86% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 176/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 184/189
- Current/Yahoo technical mismatches blocked: 13/189
- DirectFN public table health only, not trusted for action tickets: 252 rows | as_of=2026-09-03T16:34:13.092434+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 18
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260903T163900Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence rejected for EGCH.CA: source text did not clearly match EGCH.CA / Egyptian Chemical Industries Kima.
- Evidence for FERC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for MBSC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ARCC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for MASR.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Evidence for MFSC.CA matches the company but no source/report date was detected.
