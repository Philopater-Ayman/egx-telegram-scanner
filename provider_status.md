# Provider Status

Generated UTC: 2026-06-21T11:17:02.900004+00:00
Generated Cairo: 2026-06-21 14:17
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-06-21 14:17 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-06-21 14:12

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BEARISH / EGX70 CONSTRUCTIVE / sector breadth 71.43% / risk mode SELECTIVE_SMALL_MID_SWINGS
- Market data: 164/190 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 179/190
- Current/Yahoo technical mismatches blocked: 26/190
- DirectFN public table health only, not trusted for action tickets: 238 rows | as_of=2026-06-21T11:12:39.184647+00:00 | error=none
- Data quality issues: 0
- Evidence sources found: 18
- AI narrative: OpenRouter OK (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260621T111702Z_BUY_KWIN.CA, 20260621T111702Z_BUY_MASR.CA, 20260621T111702Z_BUY_MTIE.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- Evidence rejected for ATLC.CA: source text did not clearly match ATLC.CA / Al Tawfeek Leasing.
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
