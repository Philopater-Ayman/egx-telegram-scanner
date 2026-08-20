# Provider Status

Generated UTC: 2026-08-20T08:35:49.665831+00:00
Generated Cairo: 2026-08-20 11:35
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-08-20 11:35 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-08-20 11:30

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 CONSTRUCTIVE / EGX70 MIXED / sector breadth 28.57% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 144/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 173/189
- Current/Yahoo technical mismatches blocked: 45/189
- DirectFN public table health only, not trusted for action tickets: 229 rows | as_of=2026-08-20T08:30:36.247216+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 12
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260820T083549Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for SCEM.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for PHTV.CA matches the company but appears old; latest detected date is 2020-01-01.
- Evidence for MILS.CA matches the company but no source/report date was detected.
- Evidence rejected for RACC.CA: source text did not clearly match RACC.CA / Raya Customer Experience.
- Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
