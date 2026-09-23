# Provider Status

Generated UTC: 2026-09-23T13:17:44.655108+00:00
Generated Cairo: 2026-09-23 16:17
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-09-23 16:17 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-09-23 16:14

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 33.33% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 180/187 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 179/187
- Current/Yahoo technical mismatches blocked: 7/187
- DirectFN public table health only, not trusted for action tickets: 256 rows | as_of=2026-09-23T13:14:31.795233+00:00 | error=none
- Data quality issues: 3
- Evidence sources found: 6
- AI narrative: OpenRouter OK (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260923T131744Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for MHOT.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for EGTS.CA: source text did not clearly match EGTS.CA / Egyptian Resorts Company.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence for SAUD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
