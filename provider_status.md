# Provider Status

Generated UTC: 2026-09-01T10:28:54.895544+00:00
Generated Cairo: 2026-09-01 13:28
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-09-01 13:28 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-01 13:25

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bullish
- Market regime: EGX30 MIXED / EGX70 MIXED / sector breadth 19.05% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 176/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 182/189
- Current/Yahoo technical mismatches blocked: 13/189
- DirectFN public table health only, not trusted for action tickets: 252 rows | as_of=2026-09-01T10:25:10.291251+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 9
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260901T102854Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for EBSC.CA: source text did not clearly match EBSC.CA / Osool ESB Securities Brokerage.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for PRDC.CA: source text did not clearly match PRDC.CA / Pioneers Properties For Urban Development.
- Evidence for SVCE.CA matches the company but no source/report date was detected.
- Evidence rejected for CIEB.CA: source text did not clearly match CIEB.CA / Credit Agricole Egypt.
- Evidence for ELKA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for DAPH.CA: source text did not clearly match DAPH.CA / Development & Engineering Consultants.
- Evidence rejected for SKPC.CA: source text did not clearly match SKPC.CA / Sidi Kerir Petrochemicals.
- Evidence for CLHO.CA matches the company but appears old; latest detected date is 2025-01-01.
