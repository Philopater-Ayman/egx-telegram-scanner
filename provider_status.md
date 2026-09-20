# Provider Status

Generated UTC: 2026-09-20T11:19:54.846773+00:00
Generated Cairo: 2026-09-20 14:19
- Scan phase: Open liquidity confirmation
- Run timing: target 09:15 Cairo | generated Cairo 2026-09-20 14:19 | cron 15 6 * * 0-4
- Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-09-20 14:16

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 14.29% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 165/187 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 182/187
- Current/Yahoo technical mismatches blocked: 22/187
- DirectFN public table health only, not trusted for action tickets: 252 rows | as_of=2026-09-20T11:16:25.099325+00:00 | error=none
- Data quality issues: 3
- Evidence sources found: 6
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260920T111954Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for ZEOT.CA matches the company but no source/report date was detected.
- Evidence rejected for EGCH.CA: source text did not clearly match EGCH.CA / Egyptian Chemical Industries Kima.
- Evidence rejected for HELI.CA: source text did not clearly match HELI.CA / Heliopolis Housing.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
