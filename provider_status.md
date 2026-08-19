# Provider Status

Generated UTC: 2026-08-19T06:03:51.147876+00:00
Generated Cairo: 2026-08-19 09:03
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-08-19 09:03 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-08-19 09:00

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BULLISH / EGX70 BULLISH / sector breadth 61.9% / risk mode BROAD_RISK_ON
- Market data: 162/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 186/189
- Current/Yahoo technical mismatches blocked: 27/189
- DirectFN public table health only, not trusted for action tickets: 255 rows | as_of=2026-08-19T06:00:30.004086+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 12
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260819T060351Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for SCTS.CA matches the company but no source/report date was detected.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence rejected for CIEB.CA: source text did not clearly match CIEB.CA / Credit Agricole Egypt.
- Evidence for SWDY.CA matches the company but no source/report date was detected.
- Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for EHDR.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for SUGR.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for RACC.CA: source text did not clearly match RACC.CA / Raya Customer Experience.
