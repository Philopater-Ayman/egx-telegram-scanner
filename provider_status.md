# Provider Status

Generated UTC: 2026-10-29T14:57:29.056822+00:00
Generated Cairo: 2026-10-29 17:57
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-10-29 17:57 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-10-29 17:53

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 0.0% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 164/186 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 176/186
- Current/Yahoo technical mismatches blocked: 22/186
- DirectFN public table health only, not trusted for action tickets: 253 rows | as_of=2026-10-29T14:53:17.447336+00:00 | error=none
- Data quality issues: 4
- Evidence sources found: 15
- AI narrative: OpenRouter ERROR (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20261029T145729Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- CEFM.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Evidence for ADIB.CA matches the company but no source/report date was detected.
- Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- Evidence for SWDY.CA matches the company but no source/report date was detected.
- Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
