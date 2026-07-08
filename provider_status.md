# Provider Status

Generated UTC: 2026-07-08T10:15:35.433730+00:00
Generated Cairo: 2026-07-08 13:15
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-07-08 13:15 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-07-08 13:11

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 CONSTRUCTIVE / EGX70 BULLISH / sector breadth 71.43% / risk mode BROAD_RISK_ON
- Market data: 185/190 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 178/190
- Current/Yahoo technical mismatches blocked: 4/190
- DirectFN public table health only, not trusted for action tickets: 252 rows | as_of=2026-07-08T10:11:27.880018+00:00 | error=none
- Data quality issues: 0
- Evidence sources found: 9
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b-20230311:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260708T101535Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- Evidence rejected for RREI.CA: source text did not clearly match RREI.CA / Arab Real Estate Investment Co..
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence rejected for BIOC.CA: source text did not clearly match BIOC.CA / GlaxoSmithKline S.A.E.
- Evidence for MIPH.CA matches the company but no source/report date was detected.
- Evidence rejected for PRDC.CA: source text did not clearly match PRDC.CA / Pioneers Properties For Urban Development.
- Evidence rejected for TMGH.CA: source text did not clearly match TMGH.CA / Talaat Moustafa Group Holding.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence for AMER.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for EALR.CA matches the company but no source/report date was detected.
