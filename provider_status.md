# Provider Status

Generated UTC: 2026-06-09T08:52:49.986505+00:00
Generated Cairo: 2026-06-09 11:52
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-06-09 11:52 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-06-09 11:49

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BEARISH / EGX70 MIXED / sector breadth 19.05% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 184/190 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 168/190
- Current/Yahoo technical mismatches blocked: 6/190
- DirectFN public table health only, not trusted for action tickets: 231 rows | as_of=2026-06-09T08:49:20.456954+00:00 | error=none
- Data quality issues: 0
- Evidence sources found: 12
- AI narrative: OpenRouter OK (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260609T085249Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for ZMID.CA matches the company but appears old; latest detected date is 2025-01-01.
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- Evidence for ROTO.CA matches the company but no source/report date was detected.
- Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- Evidence for RAYA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ACAMD.CA matches the company but appears old; latest detected date is 2020-01-01.
