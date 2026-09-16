# Provider Status

Generated UTC: 2026-09-16T10:19:35.931602+00:00
Generated Cairo: 2026-09-16 13:19
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-09-16 13:19 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-16 13:16

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 19.05% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 179/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 179/189
- Current/Yahoo technical mismatches blocked: 10/189
- DirectFN public table health only, not trusted for action tickets: 251 rows | as_of=2026-09-16T10:16:40.806475+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 12
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260916T101935Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for DTPP.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for UNIT.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
- Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- Evidence rejected for EASB.CA: source text did not clearly match EASB.CA / Egyptian Arabian Company (Themar) for securities Brokerage EAC.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
