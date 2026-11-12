# Provider Status

Generated UTC: 2026-11-12T14:00:48.734475+00:00
Generated Cairo: 2026-11-12 16:00
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-11-12 16:00 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-11-12 15:58

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 47.62% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 173/185 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 179/185
- Current/Yahoo technical mismatches blocked: 12/185
- DirectFN public table health only, not trusted for action tickets: 251 rows | as_of=2026-11-12T13:58:14.740122+00:00 | error=none
- Data quality issues: 5
- Evidence sources found: 12
- AI narrative: OpenRouter ERROR (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20261112T140048Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- CANA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence for MOIN.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for PRMH.CA: source text did not clearly match PRMH.CA / Prime Holding S.A.E.
- Evidence for SAUD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for MHOT.CA matches the company but no source/report date was detected.
- Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- Evidence rejected for IDRE.CA: source text did not clearly match IDRE.CA / Ismailia Development and Real Estate Co.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
