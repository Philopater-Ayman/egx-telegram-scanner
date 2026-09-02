# Provider Status

Generated UTC: 2026-09-02T12:32:51.905362+00:00
Generated Cairo: 2026-09-02 15:32
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-09-02 15:32 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-09-02 15:27

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 MIXED / EGX70 BEARISH / sector breadth 38.1% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 171/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 184/189
- Current/Yahoo technical mismatches blocked: 18/189
- DirectFN public table health only, not trusted for action tickets: 255 rows | as_of=2026-09-02T12:27:31.193759+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 21
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: False
- Latest ticket id(s): 20260902T123251Z_BUY_NCCW.CA, 20260902T123251Z_BUY_LCSW.CA, 20260902T123251Z_BUY_CSAG.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for MAAL.CA: source text did not clearly match MAAL.CA / Marseille Almasreia Alkhalegeya For Holding Investment SAE.
- Evidence for WCDF.CA matches the company but no source/report date was detected.
