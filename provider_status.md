# Provider Status

Generated UTC: 2026-11-09T14:21:48.272208+00:00
Generated Cairo: 2026-11-09 16:21
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-11-09 16:21 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-11-09 16:18

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 19.05% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 169/187 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 177/187
- Current/Yahoo technical mismatches blocked: 18/187
- DirectFN public table health only, not trusted for action tickets: 249 rows | as_of=2026-11-09T14:18:27.120399+00:00 | error=none
- Data quality issues: 3
- Evidence sources found: 12
- AI narrative: OpenRouter ERROR (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20261109T142148Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for KZPC.CA matches the company but appears old; latest detected date is 2024-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for SWDY.CA matches the company but no source/report date was detected.
- Evidence rejected for BIOC.CA: source text did not clearly match BIOC.CA / GlaxoSmithKline S.A.E.
- Evidence rejected for SMFR.CA: source text did not clearly match SMFR.CA / Samad Misr EGYFERT.S.A.E.
- Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence for DOMT.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
