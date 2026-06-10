# Provider Status

Generated UTC: 2026-06-10T09:10:10.170993+00:00
Generated Cairo: 2026-06-10 12:10
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-06-10 12:10 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-06-10 12:06

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 BEARISH / EGX70 MIXED / sector breadth 23.81% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 187/190 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 171/190
- Current/Yahoo technical mismatches blocked: 3/190
- DirectFN public table health only, not trusted for action tickets: 234 rows | as_of=2026-06-10T09:06:51.514650+00:00 | error=none
- Data quality issues: 0
- Evidence sources found: 15
- AI narrative: OpenRouter OK (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260610T091010Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for ZMID.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Evidence for KZPC.CA matches the company but appears old; latest detected date is 2024-01-01.
- Evidence for ACAMD.CA matches the company but appears old; latest detected date is 2020-01-01.
- Evidence for ASPI.CA matches the company but no source/report date was detected.
- Evidence for COSG.CA matches the company but no source/report date was detected.
- Evidence rejected for MPCI.CA: source text did not clearly match MPCI.CA / Memphis Pharmaceuticals & Chemical Industries.
