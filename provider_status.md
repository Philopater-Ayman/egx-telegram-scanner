# Provider Status

Generated UTC: 2026-11-02T13:52:33.671606+00:00
Generated Cairo: 2026-11-02 15:52
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-11-02 15:52 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-11-02 15:48

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 0.0% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 166/187 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 181/187
- Current/Yahoo technical mismatches blocked: 21/187
- DirectFN public table health only, not trusted for action tickets: 245 rows | as_of=2026-11-02T13:49:03.199615+00:00 | error=none
- Data quality issues: 3
- Evidence sources found: 15
- AI narrative: OpenRouter ERROR (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20261102T135233Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- Evidence for SCEM.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for POUL.CA matches the company but no source/report date was detected.
- Evidence for GTWL.CA matches the company but no source/report date was detected.
- Evidence rejected for PRMH.CA: source text did not clearly match PRMH.CA / Prime Holding S.A.E.
- Evidence for MCQE.CA matches the company but appears old; latest detected date is 2025-01-01.
