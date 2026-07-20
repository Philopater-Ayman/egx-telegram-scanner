# Provider Status

Generated UTC: 2026-07-20T10:52:21.719014+00:00
Generated Cairo: 2026-07-20 13:52
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-07-20 13:52 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-07-20 13:45

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 CONSTRUCTIVE / EGX70 BULLISH / sector breadth 47.62% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 169/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 184/189
- Current/Yahoo technical mismatches blocked: 20/189
- DirectFN public table health only, not trusted for action tickets: 249 rows | as_of=2026-07-20T10:46:01.051190+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 21
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260720T105221Z_BUY_ARCC.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence for WKOL.CA matches the company but no source/report date was detected.
- Evidence for EALR.CA matches the company but no source/report date was detected.
