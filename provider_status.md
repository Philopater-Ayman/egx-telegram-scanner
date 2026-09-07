# Provider Status

Generated UTC: 2026-09-07T10:46:48.023202+00:00
Generated Cairo: 2026-09-07 13:46
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-09-07 13:46 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-07 13:42

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BULLISH / EGX70 BULLISH / sector breadth 71.43% / risk mode BROAD_RISK_ON
- Market data: 174/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 181/189
- Current/Yahoo technical mismatches blocked: 15/189
- DirectFN public table health only, not trusted for action tickets: 253 rows | as_of=2026-09-07T10:42:15.460331+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 21
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260907T104648Z_BUY_MIPH.CA, 20260907T104648Z_BUY_FAIT.CA
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv, /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for CICH.CA: source text did not clearly match CICH.CA / CI Capital Holding.
- Evidence for IFAP.CA matches the company but no source/report date was detected.
- Evidence for ACGC.CA matches the company but no source/report date was detected.
