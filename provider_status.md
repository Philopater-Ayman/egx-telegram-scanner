# Provider Status

Generated UTC: 2026-07-21T10:27:41.263959+00:00
Generated Cairo: 2026-07-21 13:27
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-07-21 13:27 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-07-21 13:20

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BULLISH / EGX70 CONSTRUCTIVE / sector breadth 52.38% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 171/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 182/189
- Current/Yahoo technical mismatches blocked: 18/189
- DirectFN public table health only, not trusted for action tickets: 250 rows | as_of=2026-07-21T10:21:02.622591+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 18
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260721T102741Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for ARCC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini batch evidence failed: 'NoneType' object has no attribute 'strip'
- Evidence for ADIB.CA matches the company but no source/report date was detected.
- Evidence for GRCA.CA matches the company but no source/report date was detected.
- Evidence for MEPA.CA matches the company but no source/report date was detected.
- Evidence rejected for GDWA.CA: source text did not clearly match GDWA.CA / Gadwa for Industrial Development.
- Evidence for FERC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
