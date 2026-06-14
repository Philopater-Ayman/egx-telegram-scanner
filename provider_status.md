# Provider Status

Generated UTC: 2026-06-14T10:50:05.294104+00:00
Generated Cairo: 2026-06-14 13:50
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-06-14 13:50 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-06-14 13:46

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 4.76% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 178/190 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 179/190
- Current/Yahoo technical mismatches blocked: 12/190
- DirectFN public table health only, not trusted for action tickets: 236 rows | as_of=2026-06-14T10:46:39.039173+00:00 | error=none
- Data quality issues: 0
- Evidence sources found: 12
- AI narrative: OpenRouter OK (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260614T105005Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for ISMQ.CA matches the company but no source/report date was detected.
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- Evidence for ADCI.CA matches the company but no source/report date was detected.
- Evidence for ORWE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for PRMH.CA: source text did not clearly match PRMH.CA / Prime Holding S.A.E.
- Evidence for ASPI.CA matches the company but no source/report date was detected.
- Evidence rejected for JUFO.CA: source text did not clearly match JUFO.CA / Juhayna Food Industries.
