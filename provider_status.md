# Provider Status

Generated UTC: 2026-09-15T10:28:42.519772+00:00
Generated Cairo: 2026-09-15 13:28
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-09-15 13:28 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-15 13:24

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 19.05% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 177/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 178/189
- Current/Yahoo technical mismatches blocked: 12/189
- DirectFN public table health only, not trusted for action tickets: 251 rows | as_of=2026-09-15T10:24:49.413248+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 12
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260915T102842Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for KABO.CA matches the company but no source/report date was detected.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- Evidence for MASR.CA matches the company but appears old; latest detected date is 2025-01-01.
