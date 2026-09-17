# Provider Status

Generated UTC: 2026-09-17T10:28:13.706284+00:00
Generated Cairo: 2026-09-17 13:28
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-09-17 13:28 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-17 13:24

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 19.05% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 182/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 178/189
- Current/Yahoo technical mismatches blocked: 7/189
- DirectFN public table health only, not trusted for action tickets: 249 rows | as_of=2026-09-17T10:24:35.858391+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 12
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260917T102813Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for WKOL.CA matches the company but no source/report date was detected.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for AALR.CA matches the company but no source/report date was detected.
- Evidence rejected for HELI.CA: source text did not clearly match HELI.CA / Heliopolis Housing.
- Evidence for UNIT.CA matches the company but appears old; latest detected date is 2025-01-01.
