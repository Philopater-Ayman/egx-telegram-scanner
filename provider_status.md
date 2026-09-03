# Provider Status

Generated UTC: 2026-09-03T10:07:25.697134+00:00
Generated Cairo: 2026-09-03 13:07
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-09-03 13:07 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-03 13:04

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BULLISH / EGX70 MIXED / sector breadth 42.86% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 178/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 181/189
- Current/Yahoo technical mismatches blocked: 11/189
- DirectFN public table health only, not trusted for action tickets: 252 rows | as_of=2026-09-03T10:04:10.110957+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 12
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260903T100725Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence for FERC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for EGCH.CA: source text did not clearly match EGCH.CA / Egyptian Chemical Industries Kima.
- Evidence for MBSC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ARCC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- Evidence for ISMQ.CA matches the company but no source/report date was detected.
