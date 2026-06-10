# Provider Status

Generated UTC: 2026-06-10T10:24:20.888273+00:00
Generated Cairo: 2026-06-10 13:24
- Scan phase: Open liquidity confirmation
- Run timing: target 09:15 Cairo | generated Cairo 2026-06-10 13:24 | cron 15 6 * * 0-4
- Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-06-10 13:20

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 BEARISH / EGX70 MIXED / sector breadth 23.81% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 186/190 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 177/190
- Current/Yahoo technical mismatches blocked: 4/190
- DirectFN public table health only, not trusted for action tickets: 252 rows | as_of=2026-06-10T10:20:55.238375+00:00 | error=none
- Data quality issues: 0
- Evidence sources found: 15
- AI narrative: OpenRouter OK (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260610T102420Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- Evidence for ZMID.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for MENA.CA matches the company but no source/report date was detected.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- Evidence for KZPC.CA matches the company but appears old; latest detected date is 2024-01-01.
- Evidence rejected for UNIP.CA: source text did not clearly match UNIP.CA / Universal For Paper and Packaging Materials.
- Mubasher stock page returned no evidence titles for LUTS.CA.
- No Yahoo or Mubasher evidence found for LUTS.CA.
- Evidence rejected for LUTS.CA: source text did not clearly match LUTS.CA / Lotus Agri Capital.
- Evidence for KWIN.CA matches the company but no source/report date was detected.
