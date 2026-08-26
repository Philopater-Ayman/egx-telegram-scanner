# Provider Status

Generated UTC: 2026-08-26T18:13:59.074579+00:00
Generated Cairo: 2026-08-26 21:13
- Scan phase: Evening tomorrow plan
- Run timing: target 19:30 Cairo | generated Cairo 2026-08-26 21:13 | cron 30 16 * * 0-4
- Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-08-26 21:10

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 MIXED / EGX70 MIXED / sector breadth 14.29% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 176/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 181/189
- Current/Yahoo technical mismatches blocked: 13/189
- DirectFN public table health only, not trusted for action tickets: 249 rows | as_of=2026-08-26T18:10:26.236588+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 15
- AI narrative: OpenRouter OK (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260826T181359Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for EBSC.CA: source text did not clearly match EBSC.CA / Osool ESB Securities Brokerage.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for SPIN.CA: source text did not clearly match SPIN.CA / Alexandria Spinning and Weaving.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence for FAIT.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CCRS.CA matches the company but appears old; latest detected date is 2016-01-01.
- Evidence for ORWE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for CIEB.CA: source text did not clearly match CIEB.CA / Credit Agricole Egypt.
- Evidence for SAUD.CA matches the company but appears old; latest detected date is 2025-01-01.
