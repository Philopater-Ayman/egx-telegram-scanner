# Provider Status

Generated UTC: 2026-06-23T11:02:26.904623+00:00
Generated Cairo: 2026-06-23 14:02
- Scan phase: Intraday liquidity update
- Run timing: target 11:00 Cairo | generated Cairo 2026-06-23 14:02 | cron 0 8 * * 0-4
- Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-06-23 13:58

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 BEARISH / EGX70 BEARISH / sector breadth 38.1% / risk mode DEFENSIVE_NO_NEW_BUY
- Market data: 170/190 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 178/190
- Current/Yahoo technical mismatches blocked: 20/190
- DirectFN public table health only, not trusted for action tickets: 253 rows | as_of=2026-06-23T10:58:17.469317+00:00 | error=none
- Data quality issues: 0
- Evidence sources found: 9
- AI narrative: OpenRouter OK (openai/gpt-oss-120b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260623T110226Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for DOMT.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CLHO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
- Evidence for ISPH.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for MPCI.CA: source text did not clearly match MPCI.CA / Memphis Pharmaceuticals & Chemical Industries.
- Evidence rejected for ATLC.CA: source text did not clearly match ATLC.CA / Al Tawfeek Leasing.
- Evidence rejected for ORHD.CA: source text did not clearly match ORHD.CA / Orascom Development Egypt.
