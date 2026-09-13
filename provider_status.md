# Provider Status

Generated UTC: 2026-09-13T16:35:25.592469+00:00
Generated Cairo: 2026-09-13 19:35
- Scan phase: Post-close tomorrow tickets
- Run timing: target 15:30 Cairo | generated Cairo 2026-09-13 19:35 | cron 30 12 * * 0-4
- Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-09-13 19:30

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 CONSTRUCTIVE / EGX70 BEARISH / sector breadth 42.86% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 176/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 184/189
- Current/Yahoo technical mismatches blocked: 13/189
- DirectFN public table health only, not trusted for action tickets: 245 rows | as_of=2026-09-13T16:30:46.377252+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 6
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260913T163525Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence for MASR.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence for POUL.CA matches the company but no source/report date was detected.
- Evidence rejected for EPCO.CA: source text did not clearly match EPCO.CA / Egypt for Poultry.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
