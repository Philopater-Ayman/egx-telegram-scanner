# Provider Status

Generated UTC: 2026-10-19T11:17:35.866068+00:00
Generated Cairo: 2026-10-19 14:17
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-10-19 14:17 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-10-19 14:13

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 0.0% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 176/187 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 178/187
- Current/Yahoo technical mismatches blocked: 11/187
- DirectFN public table health only, not trusted for action tickets: 252 rows | as_of=2026-10-19T11:13:48.750808+00:00 | error=none
- Data quality issues: 3
- Evidence sources found: 15
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20261019T111735Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for CPCI.CA matches the company but no source/report date was detected.
- Evidence for ARCC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
