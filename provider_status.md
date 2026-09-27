# Provider Status

Generated UTC: 2026-09-27T19:51:49.200689+00:00
Generated Cairo: 2026-09-27 22:51
- Scan phase: Evening tomorrow plan
- Run timing: target 19:30 Cairo | generated Cairo 2026-09-27 22:51 | cron 30 16 * * 0-4
- Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-09-27 22:48

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 9.52% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 137/187 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 181/187
- Current/Yahoo technical mismatches blocked: 50/187
- DirectFN public table health only, not trusted for action tickets: 251 rows | as_of=2026-09-27T19:48:43.666837+00:00 | error=none
- Data quality issues: 3
- Evidence sources found: 9
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260927T195149Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for MHOT.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence rejected for EGTS.CA: source text did not clearly match EGTS.CA / Egyptian Resorts Company.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
