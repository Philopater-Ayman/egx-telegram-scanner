# Provider Status

Generated UTC: 2026-10-19T15:15:44.235762+00:00
Generated Cairo: 2026-10-19 18:15
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-10-19 18:15 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-10-19 18:12

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 0.0% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 173/187 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 178/187
- Current/Yahoo technical mismatches blocked: 14/187
- DirectFN public table health only, not trusted for action tickets: 252 rows | as_of=2026-10-19T15:12:18.734237+00:00 | error=none
- Data quality issues: 3
- Evidence sources found: 15
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20261019T151544Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for CPCI.CA matches the company but no source/report date was detected.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence for SIPC.CA matches the company but appears old; latest detected date is 2020-01-01.
- Evidence for ARCC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
