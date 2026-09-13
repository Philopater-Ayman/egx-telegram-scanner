# Provider Status

Generated UTC: 2026-09-13T10:41:08.312993+00:00
Generated Cairo: 2026-09-13 13:41
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-09-13 13:41 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-13 13:36

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 CONSTRUCTIVE / EGX70 BEARISH / sector breadth 38.1% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 175/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 182/189
- Current/Yahoo technical mismatches blocked: 14/189
- DirectFN public table health only, not trusted for action tickets: 232 rows | as_of=2026-09-13T10:36:11.037404+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 9
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260913T104108Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Gemini batch evidence failed: 500 INTERNAL. {'error': {'code': 500, 'message': 'An internal error has occurred. Please retry or report in https://developers.generativeai.google/guide/troubleshooting', 'status': 'INTERNAL'}}
- Evidence for MASR.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for POUL.CA matches the company but no source/report date was detected.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence rejected for EPCO.CA: source text did not clearly match EPCO.CA / Egypt for Poultry.
- Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- Evidence for EFIC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for SKPC.CA: source text did not clearly match SKPC.CA / Sidi Kerir Petrochemicals.
