# Provider Status

Generated UTC: 2026-08-12T07:01:19.951602+00:00
Generated Cairo: 2026-08-12 10:01
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-08-12 10:01 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-08-12 09:56

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 BULLISH / EGX70 BULLISH / sector breadth 52.38% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 123/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 181/189
- Current/Yahoo technical mismatches blocked: 66/189
- DirectFN public table health only, not trusted for action tickets: 0 rows | as_of=2026-08-12T06:56:57.011200+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 15
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260812T070119Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for ISPH.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence for EALR.CA matches the company but no source/report date was detected.
- Evidence for CNFN.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for SUGR.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for SMFR.CA: source text did not clearly match SMFR.CA / Samad Misr EGYFERT.S.A.E.
- Evidence for SAUD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for MAAL.CA: source text did not clearly match MAAL.CA / Marseille Almasreia Alkhalegeya For Holding Investment SAE.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
