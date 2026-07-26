# Provider Status

Generated UTC: 2026-07-26T08:02:17.213848+00:00
Generated Cairo: 2026-07-26 11:02
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-07-26 11:02 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-07-26 10:56

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BULLISH / EGX70 BULLISH / sector breadth 57.14% / risk mode BROAD_RISK_ON
- Market data: 183/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 169/189
- Current/Yahoo technical mismatches blocked: 6/189
- DirectFN public table health only, not trusted for action tickets: 232 rows | as_of=2026-07-26T07:57:08.697463+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 20
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260726T080217Z_BUY_SAUD.CA, 20260726T080217Z_BUY_CANA.CA, 20260726T080217Z_BUY_BTFH.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for SWDY.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
