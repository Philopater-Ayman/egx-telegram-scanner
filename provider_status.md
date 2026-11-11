# Provider Status

Generated UTC: 2026-11-11T15:49:27.083818+00:00
Generated Cairo: 2026-11-11 17:49
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-11-11 17:49 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-11-11 17:46

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 42.86% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 175/186 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 180/186
- Current/Yahoo technical mismatches blocked: 11/186
- DirectFN public table health only, not trusted for action tickets: 251 rows | as_of=2026-11-11T15:46:47.560018+00:00 | error=none
- Data quality issues: 4
- Evidence sources found: 15
- AI narrative: OpenRouter ERROR (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20261111T154927Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for MOSC.CA matches the company but no source/report date was detected.
- Evidence rejected for PRMH.CA: source text did not clearly match PRMH.CA / Prime Holding S.A.E.
- Evidence for ZEOT.CA matches the company but no source/report date was detected.
- Evidence for MOIN.CA matches the company but no source/report date was detected.
- Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
- Evidence for CCRS.CA matches the company but appears old; latest detected date is 2016-01-01.
- Evidence rejected for ENGC.CA: source text did not clearly match ENGC.CA / Industrial Engineering Company for Construction and Development (ICON) (S.A.E).
