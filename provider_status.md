# Provider Status

Generated UTC: 2026-06-18T10:01:13.341502+00:00
Generated Cairo: 2026-06-18 13:01
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-06-18 13:01 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-06-18 12:58

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 MIXED / EGX70 CONSTRUCTIVE / sector breadth 80.95% / risk mode SELECTIVE_SMALL_MID_SWINGS
- Market data: 180/190 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 179/190
- Current/Yahoo technical mismatches blocked: 10/190
- DirectFN public table health only, not trusted for action tickets: 258 rows | as_of=2026-06-18T09:58:19.730219+00:00 | error=none
- Data quality issues: 0
- Evidence sources found: 6
- AI narrative: OpenRouter OK (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260618T100113Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- Evidence for MASR.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- Evidence rejected for ECAP.CA: source text did not clearly match ECAP.CA / Al Ezz Ceramics & Porcelain Co..
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- Evidence rejected for TMGH.CA: source text did not clearly match TMGH.CA / Talaat Moustafa Group Holding.
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
