# Provider Status

Generated UTC: 2026-08-05T10:32:19.703425+00:00
Generated Cairo: 2026-08-05 13:32
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-08-05 13:32 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-08-05 13:29

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BULLISH / EGX70 BULLISH / sector breadth 33.33% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 154/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 178/189
- Current/Yahoo technical mismatches blocked: 35/189
- DirectFN public table health only, not trusted for action tickets: 251 rows | as_of=2026-08-05T10:29:16.032362+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 15
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260805T103219Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for IFAP.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence rejected for HRHO.CA: source text did not clearly match HRHO.CA / EFG Holding.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence for KZPC.CA matches the company but appears old; latest detected date is 2024-01-01.
- Evidence for ARCC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for MBSC.CA matches the company but appears old; latest detected date is 2025-01-01.
