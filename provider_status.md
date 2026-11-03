# Provider Status

Generated UTC: 2026-11-03T15:47:07.209948+00:00
Generated Cairo: 2026-11-03 17:47
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-11-03 17:47 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-11-03 17:43

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 0.0% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 165/185 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 177/185
- Current/Yahoo technical mismatches blocked: 20/185
- DirectFN public table health only, not trusted for action tickets: 251 rows | as_of=2026-11-03T15:43:21.271058+00:00 | error=none
- Data quality issues: 5
- Evidence sources found: 15
- AI narrative: OpenRouter ERROR (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20261103T154707Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GDWA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- MILS.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for EMFD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for SCEM.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for JUFO.CA: source text did not clearly match JUFO.CA / Juhayna Food Industries.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- Evidence for MCQE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for GTWL.CA matches the company but no source/report date was detected.
- Evidence for POUL.CA matches the company but no source/report date was detected.
