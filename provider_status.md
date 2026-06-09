# Provider Status

Generated UTC: 2026-06-09T11:01:23.669735+00:00
Generated Cairo: 2026-06-09 14:01
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-06-09 14:01 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-06-09 13:56

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BEARISH / EGX70 MIXED / sector breadth 19.05% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 181/190 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 180/190
- Current/Yahoo technical mismatches blocked: 9/190
- DirectFN public table health only, not trusted for action tickets: 235 rows | as_of=2026-06-09T10:56:41.420837+00:00 | error=none
- Data quality issues: 0
- Evidence sources found: 9
- AI narrative: OpenRouter OK (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260609T110123Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for MAAL.CA: source text did not clearly match MAAL.CA / Marseille Almasreia Alkhalegeya For Holding Investment SAE.
- Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- Evidence for ZMID.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ASPI.CA matches the company but no source/report date was detected.
- Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- Evidence for ROTO.CA matches the company but no source/report date was detected.
