# Provider Status

Generated UTC: 2026-10-01T11:50:15.714088+00:00
Generated Cairo: 2026-10-01 14:50
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-10-01 14:50 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-10-01 14:47

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 4.76% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 131/186 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 177/186
- Current/Yahoo technical mismatches blocked: 55/186
- DirectFN public table health only, not trusted for action tickets: 230 rows | as_of=2026-10-01T11:47:35.286069+00:00 | error=none
- Data quality issues: 4
- Evidence sources found: 15
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20261001T115015Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- MFSC.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for KABO.CA matches the company but no source/report date was detected.
- Evidence for ACGC.CA matches the company but no source/report date was detected.
- Evidence for ORWE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for SNFC.CA matches the company but no source/report date was detected.
- Evidence for NIPH.CA matches the company but no source/report date was detected.
