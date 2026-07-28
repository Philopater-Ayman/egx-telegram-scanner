# Provider Status

Generated UTC: 2026-07-28T08:09:08.075824+00:00
Generated Cairo: 2026-07-28 11:09
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-07-28 11:09 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-07-28 11:03

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 MIXED / EGX70 MIXED / sector breadth 52.38% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 170/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 165/189
- Current/Yahoo technical mismatches blocked: 19/189
- DirectFN public table health only, not trusted for action tickets: 232 rows | as_of=2026-07-28T08:03:47.369589+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 6
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260728T080908Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Mubasher stock-page evidence failed for ARVA.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ARVA
- No Yahoo or Mubasher evidence found for ARVA.CA.
- Evidence rejected for ARVA.CA: source text did not clearly match ARVA.CA / Arab Valves Company.
- Evidence for ELSH.CA matches the company but no source/report date was detected.
- Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
- Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for DTPP.CA matches the company but appears old; latest detected date is 2025-01-01.
