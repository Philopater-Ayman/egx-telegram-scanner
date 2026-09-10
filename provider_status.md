# Provider Status

Generated UTC: 2026-09-10T11:16:33.265521+00:00
Generated Cairo: 2026-09-10 14:16
- Scan phase: Open liquidity confirmation
- Run timing: target 09:15 Cairo | generated Cairo 2026-09-10 14:16 | cron 15 6 * * 0-4
- Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-09-10 14:12

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 CONSTRUCTIVE / EGX70 BEARISH / sector breadth 47.62% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 176/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 183/189
- Current/Yahoo technical mismatches blocked: 13/189
- DirectFN public table health only, not trusted for action tickets: 253 rows | as_of=2026-09-10T11:12:56.618928+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 6
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260910T111633Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for EFIC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence rejected for EASB.CA: source text did not clearly match EASB.CA / Egyptian Arabian Company (Themar) for securities Brokerage EAC.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for POUL.CA matches the company but no source/report date was detected.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- Evidence rejected for SKPC.CA: source text did not clearly match SKPC.CA / Sidi Kerir Petrochemicals.
