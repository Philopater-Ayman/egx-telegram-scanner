# Provider Status

Generated UTC: 2026-08-26T08:38:48.939406+00:00
Generated Cairo: 2026-08-26 11:38
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-08-26 11:38 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-08-26 11:35

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 MIXED / EGX70 MIXED / sector breadth 14.29% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 169/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 173/189
- Current/Yahoo technical mismatches blocked: 20/189
- DirectFN public table health only, not trusted for action tickets: 231 rows | as_of=2026-08-26T08:36:01.184548+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 15
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260826T083848Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for CCRS.CA matches the company but appears old; latest detected date is 2016-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for FAIT.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for KABO.CA matches the company but no source/report date was detected.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for EMFD.CA matches the company but appears old; latest detected date is 2025-01-01.
