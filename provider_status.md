# Provider Status

Generated UTC: 2026-07-20T09:37:28.260634+00:00
Generated Cairo: 2026-07-20 12:37
- Scan phase: Open liquidity confirmation
- Run timing: target 09:15 Cairo | generated Cairo 2026-07-20 12:37 | cron 15 6 * * 0-4
- Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-07-20 12:32

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BULLISH / EGX70 BULLISH / sector breadth 52.38% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 171/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 181/189
- Current/Yahoo technical mismatches blocked: 18/189
- DirectFN public table health only, not trusted for action tickets: 249 rows | as_of=2026-07-20T09:32:09.245708+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 21
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260720T093728Z_BUY_ARCC.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence for FERC.CA matches the company but no source/report date was detected.
- Evidence for MCQE.CA matches the company but appears old; latest detected date is 2025-01-01.
