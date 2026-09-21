# Provider Status

Generated UTC: 2026-09-21T12:45:05.417919+00:00
Generated Cairo: 2026-09-21 15:45
- Scan phase: Open liquidity confirmation
- Run timing: target 09:15 Cairo | generated Cairo 2026-09-21 15:45 | cron 15 6 * * 0-4
- Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-09-21 15:41

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 47.62% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 168/187 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 182/187
- Current/Yahoo technical mismatches blocked: 19/187
- DirectFN public table health only, not trusted for action tickets: 253 rows | as_of=2026-09-21T12:41:40.094265+00:00 | error=none
- Data quality issues: 3
- Evidence sources found: 9
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260921T124505Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for SAUD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for CICH.CA: source text did not clearly match CICH.CA / CI Capital Holding.
- Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
