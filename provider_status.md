# Provider Status

Generated UTC: 2026-08-31T11:53:04.985985+00:00
Generated Cairo: 2026-08-31 14:53
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-08-31 14:53 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-08-31 14:49

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 MIXED / EGX70 BEARISH / sector breadth 33.33% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 151/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 183/189
- Current/Yahoo technical mismatches blocked: 38/189
- DirectFN public table health only, not trusted for action tickets: 250 rows | as_of=2026-08-31T11:49:20.915501+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 12
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260831T115304Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for FAIT.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for MCQE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for KWIN.CA matches the company but no source/report date was detected.
- Evidence rejected for CIEB.CA: source text did not clearly match CIEB.CA / Credit Agricole Egypt.
- Evidence for SWDY.CA matches the company but no source/report date was detected.
- Evidence rejected for SKPC.CA: source text did not clearly match SKPC.CA / Sidi Kerir Petrochemicals.
- Evidence rejected for EASB.CA: source text did not clearly match EASB.CA / Egyptian Arabian Company (Themar) for securities Brokerage EAC.
- Evidence rejected for PRDC.CA: source text did not clearly match PRDC.CA / Pioneers Properties For Urban Development.
