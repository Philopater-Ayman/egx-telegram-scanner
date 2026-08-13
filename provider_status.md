# Provider Status

Generated UTC: 2026-08-13T07:05:36.156899+00:00
Generated Cairo: 2026-08-13 10:05
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-08-13 10:05 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-08-13 10:01

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BULLISH / EGX70 BULLISH / sector breadth 52.38% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 170/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 183/189
- Current/Yahoo technical mismatches blocked: 19/189
- DirectFN public table health only, not trusted for action tickets: 0 rows | as_of=2026-08-13T07:01:42.531275+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 20
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260813T070536Z_BUY_FERC.CA, 20260813T070536Z_BUY_SUGR.CA, 20260813T070536Z_BUY_SAUD.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for DSCW.CA: source text did not clearly match DSCW.CA / Dice For Ready-Made Garments (SAE).
- Evidence for MENA.CA matches the company but no source/report date was detected.
