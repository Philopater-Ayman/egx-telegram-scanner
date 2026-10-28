# Provider Status

Generated UTC: 2026-10-28T11:40:03.250477+00:00
Generated Cairo: 2026-10-28 14:40
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-10-28 14:40 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-10-28 14:36

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 0.0% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 172/187 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 177/187
- Current/Yahoo technical mismatches blocked: 15/187
- DirectFN public table health only, not trusted for action tickets: 253 rows | as_of=2026-10-28T11:36:38.212732+00:00 | error=none
- Data quality issues: 3
- Evidence sources found: 15
- AI narrative: OpenRouter ERROR (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20261028T114003Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- Evidence for ADIB.CA matches the company but no source/report date was detected.
- Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- Evidence for SPMD.CA matches the company but no source/report date was detected.
- Evidence for POUL.CA matches the company but no source/report date was detected.
