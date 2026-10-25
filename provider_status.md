# Provider Status

Generated UTC: 2026-10-25T12:57:21.316399+00:00
Generated Cairo: 2026-10-25 15:57
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-10-25 15:57 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-10-25 15:54

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 4.76% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 49/187 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 182/187
- Current/Yahoo technical mismatches blocked: 138/187
- DirectFN public table health only, not trusted for action tickets: 252 rows | as_of=2026-10-25T12:54:10.810340+00:00 | error=none
- Data quality issues: 3
- Evidence sources found: 18
- AI narrative: OpenRouter ERROR (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20261025T125721Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- Evidence for ELNA.CA matches the company but no source/report date was detected.
- Evidence for CPCI.CA matches the company but no source/report date was detected.
- Evidence for SDTI.CA matches the company but no source/report date was detected.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- Evidence for EOSB.CA matches the company but no source/report date was detected.
