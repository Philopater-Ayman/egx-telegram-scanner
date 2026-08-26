# Provider Status

Generated UTC: 2026-08-26T06:08:08.372327+00:00
Generated Cairo: 2026-08-26 09:08
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-08-26 09:08 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-08-26 09:03

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 MIXED / EGX70 MIXED / sector breadth 14.29% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 172/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 183/189
- Current/Yahoo technical mismatches blocked: 17/189
- DirectFN public table health only, not trusted for action tickets: 124 rows | as_of=2026-08-26T06:03:40.649738+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 12
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260826T060808Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for CCRS.CA matches the company but appears old; latest detected date is 2016-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for ALUM.CA matches the company but no source/report date was detected.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Evidence for KABO.CA matches the company but no source/report date was detected.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- Evidence for EMFD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
