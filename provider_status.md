# Provider Status

Generated UTC: 2026-07-30T08:04:21.244959+00:00
Generated Cairo: 2026-07-30 11:04
- Scan phase: Pre-market risk check
- Run timing: target 08:45 Cairo | generated Cairo 2026-07-30 11:04 | cron 45 5 * * 0-4
- Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-07-30 10:56

- Macro source: Mubasher EGX market page (delayed public data)
- Macro freshness: DELAYED
- Macro trend: Bearish
- Market regime: EGX30 BEARISH / EGX70 MIXED / sector breadth 42.86% / risk mode SELECTIVE_SWING_TRADES_ONLY
- Market data: 159/189 tickers have tradeable current/delayed price data
- Mubasher delayed current rows used: 174/189
- Current/Yahoo technical mismatches blocked: 30/189
- DirectFN public table health only, not trusted for action tickets: 229 rows | as_of=2026-07-30T07:56:26.877876+00:00 | error=none
- Data quality issues: 1
- Evidence sources found: 9
- AI narrative: OpenRouter OK (nvidia/nemotron-3-super-120b-a12b:free)
- Telegram sent on latest run: True
- Latest ticket id(s): 20260730T080421Z_HOLD_NONE
- Latest history write(s): /home/runner/work/egx-telegram-scanner/egx-telegram-scanner/trade_history.csv

## Warnings
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- Gemini batch evidence failed: Server disconnected without sending a response.
- Evidence for GSSC.CA matches the company but no source/report date was detected.
- Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ADIB.CA matches the company but no source/report date was detected.
- Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- Evidence rejected for ORHD.CA: source text did not clearly match ORHD.CA / Orascom Development Egypt.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
