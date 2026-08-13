# Provider Status

Generated UTC: 2026-08-13T09:13:22.466297+00:00
Generated Cairo: 2026-08-13 12:13
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-08-13 12:13 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-08-13 12:06

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BULLISH / EGX70 BULLISH / sector breadth 71.43% / risk mode BROAD_RISK_ON
- Market data: 178/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 180/189
- Current/Yahoo technical mismatches blocked: 11/189
- DirectFN public table health only, not trusted for action tickets: 249 rows | as_of=2026-08-13T09:06:07.956662+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 18
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260813T091322Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for SCEM.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence for MBSC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for EEII.CA matches the company but appears old; latest detected date is 2019-01-01.
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Evidence for MCQE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ADPC.CA: source text did not clearly match ADPC.CA / The Arab Dairy Products Co..
- Evidence rejected for PRMH.CA: source text did not clearly match PRMH.CA / Prime Holding S.A.E.
- Evidence for DOMT.CA matches the company but appears old; latest detected date is 2025-01-01.
