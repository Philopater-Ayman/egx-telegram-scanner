# Provider Status

Generated UTC: 2026-10-20T13:16:30.323246+00:00
Generated Cairo: 2026-10-20 16:16
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-10-20 16:16 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-10-20 16:12

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 0.0% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 161/186 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 176/186
- Current/Yahoo technical mismatches blocked: 25/186
- DirectFN public table health only, not trusted for action tickets: 252 rows | as_of=2026-10-20T13:12:43.137035+00:00 | error=none
- Data quality issues: 4
- Evidence sources found: 18
- AI narrative: OpenRouter ERROR (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20261020T131630Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence for POUL.CA matches the company but no source/report date was detected.
- Evidence for SCEM.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for KZPC.CA matches the company but appears old; latest detected date is 2024-01-01.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence for SWDY.CA matches the company but no source/report date was detected.
