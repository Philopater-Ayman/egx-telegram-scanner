# Provider Status

Generated UTC: 2026-08-10T06:58:06.636520+00:00
Generated Cairo: 2026-08-10 09:58
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-08-10 09:58 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-08-10 09:54

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BULLISH / EGX70 BULLISH / sector breadth 85.71% / risk mode BROAD_RISK_ON
- Market data: 168/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 180/189
- Current/Yahoo technical mismatches blocked: 21/189
- DirectFN public table health only, not trusted for action tickets: 0 rows | as_of=2026-08-10T06:54:07.481962+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 12
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260810T065806Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for CIEB.CA: source text did not clearly match CIEB.CA / Credit Agricole Egypt.
- Gemini batch evidence failed: 'NoneType' object has no attribute 'strip'
- Evidence for MIPH.CA matches the company but no source/report date was detected.
- Evidence for CSAG.CA matches the company but no source/report date was detected.
- Evidence rejected for EGAL.CA: source text did not clearly match EGAL.CA / Egypt Aluminum.
- Evidence for CLHO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
- Evidence for FAIT.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
