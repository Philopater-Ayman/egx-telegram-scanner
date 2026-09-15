# Provider Status

Generated UTC: 2026-09-15T17:12:51.268874+00:00
Generated Cairo: 2026-09-15 20:12
- Scan phase: Post-close tomorrow tickets
- Run timing: target 15:30 Cairo | generated Cairo 2026-09-15 20:12 | cron 30 12 * * 0-4
- Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-09-15 20:09

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 9.52% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 173/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 183/189
- Current/Yahoo technical mismatches blocked: 16/189
- DirectFN public table health only, not trusted for action tickets: 251 rows | as_of=2026-09-15T17:09:48.495661+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 15
- AI narrative: OpenRouter OK (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260915T171251Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for KABO.CA matches the company but no source/report date was detected.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence for ACGC.CA matches the company but no source/report date was detected.
- Evidence for MEPA.CA matches the company but no source/report date was detected.
- Evidence for SIPC.CA matches the company but appears old; latest detected date is 2020-01-01.
