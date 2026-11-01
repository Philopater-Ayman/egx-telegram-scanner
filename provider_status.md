# Provider Status

Generated UTC: 2026-11-01T14:44:05.889450+00:00
Generated Cairo: 2026-11-01 16:44
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-11-01 16:44 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-11-01 16:40

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 0.0% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 173/186 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 180/186
- Current/Yahoo technical mismatches blocked: 13/186
- DirectFN public table health only, not trusted for action tickets: 250 rows | as_of=2026-11-01T14:40:17.470793+00:00 | error=none
- Data quality issues: 4
- Evidence sources found: 15
- AI narrative: OpenRouter ERROR (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20261101T144405Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- EDFM.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- Evidence for SCEM.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for MCQE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ADIB.CA matches the company but no source/report date was detected.
- Evidence rejected for MPCI.CA: source text did not clearly match MPCI.CA / Memphis Pharmaceuticals & Chemical Industries.
