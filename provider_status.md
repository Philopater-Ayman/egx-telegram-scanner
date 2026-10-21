# Provider Status

Generated UTC: 2026-10-21T13:25:15.152837+00:00
Generated Cairo: 2026-10-21 16:25
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-10-21 16:25 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-10-21 16:21

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 4.76% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 177/186 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 177/186
- Current/Yahoo technical mismatches blocked: 9/186
- DirectFN public table health only, not trusted for action tickets: 253 rows | as_of=2026-10-21T13:21:42.422194+00:00 | error=none
- Data quality issues: 4
- Evidence sources found: 12
- AI narrative: OpenRouter ERROR (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20261021T132515Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- Evidence for PHDC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for KZPC.CA matches the company but appears old; latest detected date is 2024-01-01.
