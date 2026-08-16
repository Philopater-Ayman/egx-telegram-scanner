# Provider Status

Generated UTC: 2026-08-16T08:25:42.605412+00:00
Generated Cairo: 2026-08-16 11:25
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-08-16 11:25 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-08-16 11:21

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 CONSTRUCTIVE / EGX70 BULLISH / sector breadth 66.67% / risk mode BROAD_RISK_ON
- Market data: 174/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 177/189
- Current/Yahoo technical mismatches blocked: 15/189
- DirectFN public table health only, not trusted for action tickets: 232 rows | as_of=2026-08-16T08:21:17.137370+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 18
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260816T082542Z_BUY_ETEL.CA, 20260816T082542Z_BUY_COSG.CA, 20260816T082542Z_BUY_SCEM.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence rejected for ORHD.CA: source text did not clearly match ORHD.CA / Orascom Development Egypt.
