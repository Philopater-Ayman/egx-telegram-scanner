# Provider Status

Generated UTC: 2026-07-15T10:02:46.568812+00:00
Generated Cairo: 2026-07-15 13:02
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-07-15 13:02 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-07-15 12:56

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 MIXED / EGX70 MIXED / sector breadth 38.1% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 173/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 180/189
- Current/Yahoo technical mismatches blocked: 16/189
- DirectFN public table health only, not trusted for action tickets: 254 rows | as_of=2026-07-15T09:56:29.788470+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 21
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260715T100246Z_BUY_UNIP.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for OFH.CA: source text did not clearly match OFH.CA / O B Financial Holding S.A.E.
- Evidence for MEPA.CA matches the company but appears old; latest detected date is 2025-01-01.
