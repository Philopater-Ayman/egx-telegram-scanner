# Provider Status

Generated UTC: 2026-09-21T11:07:52.657822+00:00
Generated Cairo: 2026-09-21 14:07
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-09-21 14:07 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-21 14:05

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 47.62% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 170/187 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 182/187
- Current/Yahoo technical mismatches blocked: 17/187
- DirectFN public table health only, not trusted for action tickets: 253 rows | as_of=2026-09-21T11:05:06.378253+00:00 | error=none
- Data quality issues: 3
- Evidence sources found: 6
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260921T110752Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for CICH.CA: source text did not clearly match CICH.CA / CI Capital Holding.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
