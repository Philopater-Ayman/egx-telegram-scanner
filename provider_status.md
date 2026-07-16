# Provider Status

Generated UTC: 2026-07-16T07:41:07.567689+00:00
Generated Cairo: 2026-07-16 10:41
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-07-16 10:41 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-07-16 10:38

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 MIXED / EGX70 MIXED / sector breadth 33.33% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 159/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 161/189
- Current/Yahoo technical mismatches blocked: 30/189
- DirectFN public table health only, not trusted for action tickets: 228 rows | as_of=2026-07-16T07:38:13.864165+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 9
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260716T074107Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for FERC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence rejected for TMGH.CA: source text did not clearly match TMGH.CA / Talaat Moustafa Group Holding.
- Evidence rejected for BTFH.CA: source text did not clearly match BTFH.CA / Beltone Holding.
- Evidence for RAYA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- Evidence for MCRO.CA matches the company but no source/report date was detected.
- Evidence rejected for ORHD.CA: source text did not clearly match ORHD.CA / Orascom Development Egypt.
