# Provider Status

Generated UTC: 2026-07-27T11:20:11.556884+00:00
Generated Cairo: 2026-07-27 14:20
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-07-27 14:20 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-07-27 14:14

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 MIXED / EGX70 MIXED / sector breadth 52.38% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 176/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 183/189
- Current/Yahoo technical mismatches blocked: 13/189
- DirectFN public table health only, not trusted for action tickets: 252 rows | as_of=2026-07-27T11:14:14.200530+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 21
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260727T112011Z_BUY_IDRE.CA, 20260727T112011Z_BUY_ARCC.CA, 20260727T112011Z_BUY_AJWA.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
