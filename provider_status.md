# Provider Status

Generated UTC: 2026-07-12T17:35:11.832329+00:00
Generated Cairo: 2026-07-12 20:35
- Scan phase: Evening tomorrow plan
- Run timing: target 19:30 Cairo | generated Cairo 2026-07-12 20:35 | cron 30 16 * * 0-4
- Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-07-12 20:30

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 CONSTRUCTIVE / EGX70 BULLISH / sector breadth 61.9% / risk mode BROAD_RISK_ON
- Market data: 174/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 184/189
- Current/Yahoo technical mismatches blocked: 15/189
- DirectFN public table health only, not trusted for action tickets: 250 rows | as_of=2026-07-12T17:30:54.738138+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 12
- AI narrative: OpenRouter OK (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260712T173511Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence rejected for RREI.CA: source text did not clearly match RREI.CA / Arab Real Estate Investment Co..
- Evidence for CAED.CA matches the company but no source/report date was detected.
- Evidence rejected for IDRE.CA: source text did not clearly match IDRE.CA / Ismailia Development and Real Estate Co.
- Evidence for ELSH.CA matches the company but no source/report date was detected.
- Evidence for ELEC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for AFDI.CA matches the company but no source/report date was detected.
- Evidence rejected for EBSC.CA: source text did not clearly match EBSC.CA / Osool ESB Securities Brokerage.
