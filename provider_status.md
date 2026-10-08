# Provider Status

Generated UTC: 2026-10-08T21:29:03.889012+00:00
Generated Cairo: 2026-10-09 00:29
- Scan phase: Evening tomorrow plan
- Run timing: target 19:30 Cairo | generated Cairo 2026-10-09 00:29 | cron 30 16 * * 0-4
- Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-10-09 00:24

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 38.1% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 185/187 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 179/187
- Current/Yahoo technical mismatches blocked: 2/187
- DirectFN public table health only, not trusted for action tickets: 139 rows | as_of=2026-10-08T21:24:56.677407+00:00 | error=none
- Data quality issues: 3
- Evidence sources found: 9
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20261008T212903Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence for SIPC.CA matches the company but appears old; latest detected date is 2020-01-01.
- Evidence for MBSC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence rejected for IRON.CA: source text did not clearly match IRON.CA / Egyptian Iron and Steel.
