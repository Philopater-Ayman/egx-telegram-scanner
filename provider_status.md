# Provider Status

Generated UTC: 2026-08-24T08:45:18.948769+00:00
Generated Cairo: 2026-08-24 11:45
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-08-24 11:45 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-08-24 11:40

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BULLISH / EGX70 MIXED / sector breadth 42.86% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 175/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 174/189
- Current/Yahoo technical mismatches blocked: 14/189
- DirectFN public table health only, not trusted for action tickets: 234 rows | as_of=2026-08-24T08:40:29.197770+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 21
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260824T084518Z_BUY_EFIH.CA, 20260824T084518Z_BUY_FWRY.CA, 20260824T084518Z_BUY_IFAP.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
