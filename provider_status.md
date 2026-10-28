# Provider Status

Generated UTC: 2026-10-28T12:46:38.774491+00:00
Generated Cairo: 2026-10-28 15:46
- Scan phase: Open liquidity confirmation
- Run timing: target 09:15 Cairo | generated Cairo 2026-10-28 15:46 | cron 15 6 * * 0-4
- Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-10-28 15:43

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 0.0% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 169/186 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 177/186
- Current/Yahoo technical mismatches blocked: 17/186
- DirectFN public table health only, not trusted for action tickets: 253 rows | as_of=2026-10-28T12:43:33.516300+00:00 | error=none
- Data quality issues: 4
- Evidence sources found: 12
- AI narrative: OpenRouter ERROR (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20261028T124638Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- Evidence for ADIB.CA matches the company but no source/report date was detected.
- Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- Evidence for SPMD.CA matches the company but no source/report date was detected.
- Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
