# Provider Status

Generated UTC: 2026-09-23T10:18:42.806149+00:00
Generated Cairo: 2026-09-23 13:18
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-09-23 13:18 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-23 13:15

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 38.1% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 174/186 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 172/186
- Current/Yahoo technical mismatches blocked: 12/186
- DirectFN public table health only, not trusted for action tickets: 251 rows | as_of=2026-09-23T10:16:00.046932+00:00 | error=none
- Data quality issues: 4
- Evidence sources found: 9
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260923T101842Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- CICH.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for SAUD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- Evidence for ABUK.CA matches the company but no source/report date was detected.
