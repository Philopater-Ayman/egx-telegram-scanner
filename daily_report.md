# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-11-22T14:31:00.099811+00:00
Generated Cairo: 2026-11-22 16:31
Run timing: target 09:15 Cairo | generated Cairo 2026-11-22 16:31 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-11-22 16:28

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 5
- Tradeable price/liquidity tickers: 185/185
- Top sector: Telecommunications

## Market Context
- Market trend: Unavailable
- Source: Market context unavailable
- As of: None
- Freshness: MISSING
- EGX30 regime: MIXED / above MA20 75.0% / above MA50 45.0%
- EGX70 regime: BEARISH / above MA20 55.0% / above MA50 17.5%
- Sector breadth: 9.52%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=363125899.63 spike=0.97 score=14.4
- AMES.CA: liquidity=318955921.58 spike=1.32 score=16.14
- COMI.CA: liquidity=288549967.5 spike=0.59 score=20.06
- BIOC.CA: liquidity=218875793.82 spike=1.11 score=19.72
- AJWA.CA: liquidity=212828724.22 spike=5.42 score=23.5

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- COSG.CA: spike=7.43 liquidity=93141852.53 outlook=NEUTRAL score=44.24 buy_ready=False
- MOSC.CA: spike=7.13 liquidity=61615347.79 outlook=BULLISH_WATCH score=73.24 buy_ready=False
- AJWA.CA: spike=5.42 liquidity=212828724.22 outlook=CONSTRUCTIVE score=59.24 buy_ready=False
- ZEOT.CA: spike=5.35 liquidity=52871741.11 outlook=NEUTRAL score=47.24 buy_ready=False
- ETRS.CA: spike=4.31 liquidity=79015669.3 outlook=BULLISH_WATCH score=77.24 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=6.72 5d=0.74% 20d=-1.56% aboveMA50=100.0%
- #2 Fintech & Payments: score=6.12 5d=-0.45% 20d=0.19% aboveMA50=50.0%
- #3 Transportation & Logistics: score=5.63 5d=0.44% 20d=0.08% aboveMA50=50.0%
- #4 Banking & Financials: score=5.14 5d=-0.27% 20d=1.57% aboveMA50=50.0%
- #5 Food, Beverages & Tobacco: score=4.71 5d=-1.61% 20d=1.56% aboveMA50=57.14%
- #6 Building Materials: score=4.62 5d=-3.0% 20d=5.38% aboveMA50=50.0%
- #7 Education: score=3.57 5d=-2.61% 20d=6.82% aboveMA50=33.33%
- #8 Industrial Goods & Cables: score=3.5 5d=-4.52% 20d=1.87% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- EFIH.CA: BULLISH_WATCH score=79.12 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support
- ETRS.CA: BULLISH_WATCH score=77.24 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- MOSC.CA: BULLISH_WATCH score=73.24 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support; sector is not leading
- FAIT.CA: CONSTRUCTIVE score=69.14 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MPCI.CA: CONSTRUCTIVE score=67.24 liquidity=TRADEABLE sector=IMPROVING risk=far above support; sector is not leading
- SUGR.CA: CONSTRUCTIVE score=66.71 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended
- PRMH.CA: CONSTRUCTIVE score=66.24 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support; sector is not leading
- CSAG.CA: CONSTRUCTIVE score=65.63 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; overheated RSI
- HRHO.CA: CONSTRUCTIVE score=65.48 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance; sector is not leading
- CIEB.CA: CONSTRUCTIVE score=65.14 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA50

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- AFMC.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=11.88 buy_ready=False sector_rank=12 price=231.87 support=171.02 resistance=269.99 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=57.3 liquidity=3388779.98 spike=0.18
- ABUK.CA: score=7.66 buy_ready=False sector_rank=17 price=76.36 support=73.6 resistance=95.69 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=27.57 liquidity=18527303.31 spike=0.15
- ACAMD.CA: score=14.32 buy_ready=False sector_rank=12 price=1.93 support=1.86 resistance=2.16 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=49.06 liquidity=94042424.22 spike=1.41
- ACGC.CA: score=11.47 buy_ready=False sector_rank=13 price=13.61 support=11.6 resistance=14.2 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=54.92 liquidity=2994975.69 spike=0.38
- ADCI.CA: score=9.8 buy_ready=False sector_rank=12 price=260.35 support=221.0 resistance=280.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=41.16 liquidity=1305655.28 spike=0.49
- ADIB.CA: score=15.06 buy_ready=False sector_rank=4 price=46.2 support=43.16 resistance=50.49 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=49.56 liquidity=44889399.14 spike=0.58
- ADPC.CA: score=8.69 buy_ready=False sector_rank=12 price=2.88 support=2.53 resistance=3.25 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=43.43 liquidity=3195080.77 spike=0.4
- AFDI.CA: score=7.29 buy_ready=False sector_rank=12 price=42.66 support=34.8 resistance=47.5 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=48.46 liquidity=1795431.41 spike=0.64
- AJWA.CA: score=23.5 buy_ready=False sector_rank=12 price=282.01 support=190.2 resistance=294.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=87.27 liquidity=212828724.22 spike=5.42
- ALCN.CA: score=16.82 buy_ready=False sector_rank=3 price=32.31 support=27.11 resistance=33.89 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=55.03 liquidity=5572021.29 spike=0.51
- ALUM.CA: score=9.26 buy_ready=False sector_rank=12 price=19.53 support=16.02 resistance=21.8 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=60.89 liquidity=1766351.85 spike=0.61
- AMER.CA: score=14.89 buy_ready=False sector_rank=15 price=3.99 support=3.21 resistance=4.74 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=37.41 liquidity=92583884.41 spike=1.35
- AMES.CA: score=16.14 buy_ready=False sector_rank=12 price=38.59 support=28.0 resistance=54.49 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=57.64 liquidity=318955921.58 spike=1.32
- AMIA.CA: score=11.26 buy_ready=False sector_rank=12 price=16.91 support=14.0 resistance=18.77 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=44.53 liquidity=6763966.12 spike=0.5
- AMOC.CA: score=10.35 buy_ready=False sector_rank=10 price=13.14 support=12.6 resistance=15.15 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=34.31 liquidity=62008200.36 spike=0.43
- APSW.CA: score=5.61 buy_ready=False sector_rank=12 price=7.4 support=7.1 resistance=8.07 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=48.76 liquidity=111947.2 spike=0.24
- ARAB.CA: score=18.19 buy_ready=False sector_rank=15 price=0.25 support=0.2 resistance=0.26 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=63.64 liquidity=32202679.83 spike=0.41
- ARCC.CA: score=19.85 buy_ready=False sector_rank=6 price=67.5 support=58.01 resistance=74.2 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=61.54 liquidity=17126505.0 spike=0.63
- AREH.CA: score=12.08 buy_ready=False sector_rank=12 price=1.04 support=0.91 resistance=1.17 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=46.88 liquidity=6580351.2 spike=0.89
- ASCM.CA: score=10.6 buy_ready=False sector_rank=12 price=44.2 support=38.2 resistance=50.4 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=52.13 liquidity=5102757.49 spike=0.87
- ASPI.CA: score=14.65 buy_ready=False sector_rank=12 price=0.32 support=0.27 resistance=0.36 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=58.12 liquidity=7155283.33 spike=0.32
- ATLC.CA: score=14.65 buy_ready=False sector_rank=14 price=5.4 support=3.93 resistance=6.06 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=60.58 liquidity=6455473.31 spike=0.53
- ATQA.CA: score=16.12 buy_ready=False sector_rank=17 price=10.12 support=8.25 resistance=11.01 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=70.5 liquidity=53395760.72 spike=1.23
- AXPH.CA: score=15.14 buy_ready=False sector_rank=12 price=1473.95 support=1135.0 resistance=1497.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=62.63 liquidity=3645078.23 spike=0.71
- BINV.CA: score=3.79 buy_ready=False sector_rank=21 price=50.8 support=50.6 resistance=59.45 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=41.98 liquidity=1387144.78 spike=0.14
- BIOC.CA: score=19.72 buy_ready=False sector_rank=12 price=392.11 support=212.05 resistance=447.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=67.18 liquidity=218875793.82 spike=1.11
- BTFH.CA: score=15.29 buy_ready=False sector_rank=14 price=2.25 support=2.05 resistance=2.64 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=39.62 liquidity=132097284.0 spike=1.05
- CAED.CA: score=18.5 buy_ready=False sector_rank=12 price=97.68 support=64.0 resistance=116.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=56.31 liquidity=10484873.55 spike=0.38
- CANA.CA: score=10.06 buy_ready=False sector_rank=4 price=33.13 support=29.33 resistance=48.49 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=25.06 liquidity=13310408.62 spike=0.62
- CCAP.CA: score=14.4 buy_ready=False sector_rank=21 price=5.93 support=5.55 resistance=6.44 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=43.98 liquidity=363125899.63 spike=0.97
- CCRS.CA: score=14.97 buy_ready=False sector_rank=12 price=2.0 support=1.3 resistance=2.49 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=66.04 liquidity=9478534.0 spike=0.5
- CEFM.CA: score=9.1 buy_ready=False sector_rank=12 price=125.13 support=97.79 resistance=138.99 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=58.85 liquidity=606505.1 spike=0.21
- CERA.CA: score=15.5 buy_ready=False sector_rank=12 price=1.04 support=0.93 resistance=1.23 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=46.88 liquidity=13983226.93 spike=0.23
- CFGH.CA: score=2.5 buy_ready=False sector_rank=12 price=0.11 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=80.0 liquidity=29.96 spike=0.01
- CICH.CA: score=7.53 buy_ready=False sector_rank=14 price=10.2 support=9.91 resistance=11.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=40.38 liquidity=2334096.56 spike=0.98
- CIEB.CA: score=20.62 buy_ready=False sector_rank=4 price=23.03 support=21.35 resistance=23.9 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=56.6 liquidity=16810265.37 spike=1.78
- CIRA.CA: score=13.93 buy_ready=False sector_rank=7 price=38.36 support=32.01 resistance=40.11 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=67.13 liquidity=3502229.7 spike=0.2
- CLHO.CA: score=17.7 buy_ready=False sector_rank=11 price=14.04 support=12.51 resistance=15.15 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=56.4 liquidity=25066454.33 spike=0.69
- CNFN.CA: score=13.73 buy_ready=False sector_rank=14 price=3.87 support=3.25 resistance=4.32 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=55.15 liquidity=8253881.58 spike=1.14
- COMI.CA: score=20.06 buy_ready=False sector_rank=4 price=127.5 support=117.41 resistance=131.36 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=67.15 liquidity=288549967.5 spike=0.59
- COPR.CA: score=6.91 buy_ready=False sector_rank=12 price=0.38 support=0.33 resistance=0.45 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=44.36 liquidity=3418838.42 spike=0.18
- COSG.CA: score=22.5 buy_ready=False sector_rank=12 price=1.41 support=1.11 resistance=1.49 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=62.75 liquidity=93141852.53 spike=7.43
- CPCI.CA: score=11.76 buy_ready=False sector_rank=12 price=575.3 support=550.84 resistance=597.07 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=36.39 liquidity=2264956.05 spike=0.54
- CSAG.CA: score=18.96 buy_ready=False sector_rank=3 price=36.09 support=30.1 resistance=37.36 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=71.73 liquidity=4709636.75 spike=0.74
- DAPH.CA: score=15.5 buy_ready=False sector_rank=12 price=86.25 support=65.2 resistance=98.1 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=65.7 liquidity=11439337.5 spike=0.54
- DEIN.CA: score=7.5 buy_ready=False sector_rank=12 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=12.1 buy_ready=False sector_rank=5 price=25.61 support=20.27 resistance=26.5 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=76.52 liquidity=2215239.44 spike=0.83
- DSCW.CA: score=15.5 buy_ready=False sector_rank=12 price=1.48 support=1.23 resistance=1.66 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=47.73 liquidity=11888470.15 spike=0.76
- DTPP.CA: score=15.5 buy_ready=False sector_rank=12 price=57.78 support=36.0 resistance=69.99 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=69.59 liquidity=19676400.78 spike=0.37
- EALR.CA: score=9.59 buy_ready=False sector_rank=12 price=303.46 support=236.01 resistance=337.99 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=63.06 liquidity=2092963.56 spike=0.27
- EASB.CA: score=8.32 buy_ready=False sector_rank=12 price=5.81 support=5.03 resistance=7.2 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=44.0 liquidity=3820353.84 spike=0.59
- EAST.CA: score=21.88 buy_ready=False sector_rank=5 price=34.08 support=28.3 resistance=35.2 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=58.28 liquidity=19707613.06 spike=0.37
- EBSC.CA: score=8.08 buy_ready=False sector_rank=12 price=1.51 support=1.2 resistance=1.7 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=52.83 liquidity=588514.95 spike=0.15
- ECAP.CA: score=8.41 buy_ready=False sector_rank=12 price=28.12 support=24.8 resistance=30.4 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=58.7 liquidity=909119.63 spike=0.35
- EDFM.CA: score=6.65 buy_ready=False sector_rank=12 price=362.76 support=326.73 resistance=378.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=66.39 liquidity=154535.76 spike=0.13
- EEII.CA: score=18.92 buy_ready=False sector_rank=12 price=2.02 support=1.42 resistance=2.29 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=68.0 liquidity=18520581.93 spike=1.21
- EFIC.CA: score=10.16 buy_ready=False sector_rank=17 price=160.27 support=121.0 resistance=174.88 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=62.9 liquidity=3503021.48 spike=0.14
- EFID.CA: score=23.66 buy_ready=False sector_rank=5 price=21.0 support=16.01 resistance=21.35 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=74.07 liquidity=74947551.0 spike=1.89
- EFIH.CA: score=23.52 buy_ready=False sector_rank=2 price=25.53 support=20.3 resistance=26.18 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=91.74 liquidity=92638058.37 spike=1.56
- EGAL.CA: score=15.66 buy_ready=False sector_rank=17 price=304.99 support=270.1 resistance=318.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=65.03 liquidity=34484303.23 spike=0.41
- EGAS.CA: score=14.42 buy_ready=False sector_rank=10 price=50.67 support=43.0 resistance=61.68 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=61.99 liquidity=4883878.44 spike=1.09
- EGBE.CA: score=10.1 buy_ready=False sector_rank=4 price=0.5 support=0.47 resistance=0.51 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=40.38 liquidity=42670.0 spike=0.88
- EGCH.CA: score=14.66 buy_ready=False sector_rank=17 price=10.2 support=9.66 resistance=11.64 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=44.63 liquidity=14955464.12 spike=0.36
- EGSA.CA: score=14.4 buy_ready=False sector_rank=1 price=9.0 support=8.7 resistance=9.06 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=74.36 liquidity=1890.0 spike=0.33
- EGTS.CA: score=18.13 buy_ready=False sector_rank=15 price=12.77 support=10.19 resistance=14.45 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=53.55 liquidity=33441796.26 spike=1.47
- EHDR.CA: score=10.13 buy_ready=False sector_rank=12 price=2.09 support=1.8 resistance=2.28 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=53.97 liquidity=2634574.47 spike=0.3
- ELEC.CA: score=18.4 buy_ready=False sector_rank=8 price=1.63 support=1.34 resistance=1.78 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=60.42 liquidity=13765558.6 spike=0.37
- ELKA.CA: score=18.5 buy_ready=False sector_rank=12 price=1.49 support=1.21 resistance=1.63 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=55.32 liquidity=11575179.8 spike=0.96
- ELNA.CA: score=7.58 buy_ready=False sector_rank=12 price=41.28 support=35.01 resistance=44.2 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=68.04 liquidity=79587.84 spike=0.1
- ELSH.CA: score=19.52 buy_ready=False sector_rank=12 price=10.71 support=8.57 resistance=11.8 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=57.41 liquidity=22175676.26 spike=1.51
- ELWA.CA: score=-0.94 buy_ready=False sector_rank=12 price=1.23 support=1.16 resistance=1.59 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=24.24 liquidity=560145.7 spike=0.42
- EMFD.CA: score=18.19 buy_ready=False sector_rank=15 price=12.8 support=10.6 resistance=12.96 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=76.04 liquidity=21794035.52 spike=0.32
- ENGC.CA: score=21.5 buy_ready=False sector_rank=12 price=39.52 support=26.91 resistance=43.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=58.9 liquidity=11776643.98 spike=0.58
- EOSB.CA: score=7.56 buy_ready=False sector_rank=12 price=1.61 support=1.55 resistance=1.72 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=66847.2 spike=0.63
- EPCO.CA: score=8.57 buy_ready=False sector_rank=12 price=8.53 support=7.0 resistance=9.98 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=62.31 liquidity=1077654.58 spike=0.18
- EPPK.CA: score=7.5 buy_ready=False sector_rank=12 price=9.78 support=9.78 resistance=9.78 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ETEL.CA: score=24.4 buy_ready=False sector_rank=1 price=137.02 support=115.0 resistance=147.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=72.58 liquidity=191732777.08 spike=0.65
- ETRS.CA: score=26.5 buy_ready=False sector_rank=12 price=11.23 support=9.51 resistance=11.58 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=69.12 liquidity=79015669.3 spike=4.31
- EXPA.CA: score=16.26 buy_ready=False sector_rank=4 price=14.63 support=12.43 resistance=15.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=61.11 liquidity=7203358.53 spike=0.35
- FAIT.CA: score=14.13 buy_ready=False sector_rank=4 price=45.43 support=40.0 resistance=47.46 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=61.2 liquidity=1070739.68 spike=0.45
- FAITA.CA: score=18.77 buy_ready=False sector_rank=4 price=1.01 support=0.98 resistance=1.03 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=58.33 liquidity=91036.01 spike=2.81
- FERC.CA: score=7.24 buy_ready=False sector_rank=17 price=65.65 support=52.63 resistance=72.69 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=56.14 liquidity=582578.11 spike=0.07
- FWRY.CA: score=21.4 buy_ready=False sector_rank=2 price=17.3 support=15.27 resistance=18.5 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=52.12 liquidity=95836996.07 spike=0.79
- GBCO.CA: score=13.4 buy_ready=False sector_rank=20 price=22.4 support=20.9 resistance=26.5 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=41.41 liquidity=53851256.68 spike=0.51
- GDWA.CA: score=7.93 buy_ready=False sector_rank=12 price=0.53 support=0.46 resistance=0.59 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=49.12 liquidity=2434940.05 spike=0.23
- GGCC.CA: score=15.5 buy_ready=False sector_rank=12 price=0.55 support=0.49 resistance=0.63 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=52.27 liquidity=11059264.53 spike=0.56
- GIHD.CA: score=16.5 buy_ready=False sector_rank=12 price=50.62 support=32.1 resistance=57.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=66.45 liquidity=12577095.55 spike=0.72
- GMCI.CA: score=8.53 buy_ready=False sector_rank=12 price=1.69 support=1.34 resistance=1.75 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=73.33 liquidity=32610.24 spike=0.08
- GRCA.CA: score=11.25 buy_ready=False sector_rank=12 price=31.45 support=22.57 resistance=37.32 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=63.52 liquidity=3751544.79 spike=0.32
- GSSC.CA: score=9.91 buy_ready=False sector_rank=12 price=265.59 support=211.52 resistance=296.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=60.07 liquidity=1417453.81 spike=0.62
- HDBK.CA: score=17.06 buy_ready=False sector_rank=4 price=108.5 support=83.01 resistance=111.2 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=75.18 liquidity=24060417.5 spike=0.76
- HELI.CA: score=16.19 buy_ready=False sector_rank=15 price=6.6 support=5.72 resistance=7.2 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=53.33 liquidity=16925389.56 spike=0.24
- HRHO.CA: score=21.51 buy_ready=False sector_rank=14 price=25.5 support=21.87 resistance=26.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=61.59 liquidity=109222441.5 spike=1.66
- ICID.CA: score=8.75 buy_ready=False sector_rank=12 price=17.28 support=14.26 resistance=17.98 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=46.37 liquidity=2255109.21 spike=0.57
- IDRE.CA: score=10.12 buy_ready=False sector_rank=12 price=41.78 support=29.11 resistance=47.25 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=66.5 liquidity=4625171.2 spike=0.56
- IFAP.CA: score=3.02 buy_ready=False sector_rank=19 price=16.04 support=15.12 resistance=19.4 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=44.73 liquidity=1134140.34 spike=0.17
- INFI.CA: score=20.08 buy_ready=False sector_rank=12 price=160.11 support=93.44 resistance=178.25 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=84.05 liquidity=156048490.22 spike=2.79
- IRON.CA: score=14.21 buy_ready=False sector_rank=17 price=24.52 support=23.13 resistance=27.22 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=49.66 liquidity=9315712.13 spike=1.12
- ISMA.CA: score=9.98 buy_ready=False sector_rank=12 price=20.63 support=14.11 resistance=22.54 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=58.97 liquidity=2481087.48 spike=0.21
- ISMQ.CA: score=8.09 buy_ready=False sector_rank=17 price=6.89 support=5.68 resistance=7.34 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=68.88 liquidity=3434582.25 spike=0.28
- ISPH.CA: score=17.7 buy_ready=False sector_rank=11 price=10.4 support=9.02 resistance=10.72 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=57.04 liquidity=26518376.63 spike=0.39
- JUFO.CA: score=16.88 buy_ready=False sector_rank=5 price=23.16 support=21.01 resistance=25.51 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=48.73 liquidity=18269812.2 spike=0.67
- KABO.CA: score=15.34 buy_ready=False sector_rank=13 price=7.07 support=5.58 resistance=7.74 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=62.38 liquidity=7869801.01 spike=0.4
- KWIN.CA: score=11.2 buy_ready=False sector_rank=12 price=70.13 support=44.02 resistance=85.83 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=64.16 liquidity=3701601.52 spike=0.28
- KZPC.CA: score=16.5 buy_ready=False sector_rank=12 price=11.5 support=11.45 resistance=14.77 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=38.25 liquidity=22423735.0 spike=2.0
- LCSW.CA: score=20.18 buy_ready=False sector_rank=6 price=39.79 support=28.0 resistance=42.14 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=64.43 liquidity=7333416.54 spike=0.32
- LUTS.CA: score=15.5 buy_ready=False sector_rank=12 price=0.67 support=0.47 resistance=0.84 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=51.28 liquidity=28597250.34 spike=0.41
- MAAL.CA: score=15.5 buy_ready=False sector_rank=12 price=6.24 support=4.88 resistance=7.64 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=35.9 liquidity=12911913.61 spike=0.5
- MASR.CA: score=15.5 buy_ready=False sector_rank=12 price=6.51 support=5.6 resistance=7.11 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=37.79 liquidity=17193730.86 spike=0.49
- MBSC.CA: score=17.85 buy_ready=False sector_rank=6 price=350.0 support=262.0 resistance=397.9 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=77.46 liquidity=53386550.0 spike=0.74
- MCQE.CA: score=18.85 buy_ready=False sector_rank=6 price=178.0 support=145.0 resistance=205.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=59.98 liquidity=21801618.0 spike=0.4
- MCRO.CA: score=17.5 buy_ready=False sector_rank=12 price=1.34 support=1.07 resistance=1.48 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=51.22 liquidity=27639296.29 spike=0.56
- MENA.CA: score=18.81 buy_ready=False sector_rank=15 price=7.16 support=5.45 resistance=7.9 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=78.95 liquidity=20947166.67 spike=2.31
- MEPA.CA: score=9.98 buy_ready=False sector_rank=12 price=1.33 support=1.14 resistance=1.55 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=54.55 liquidity=4484550.0 spike=0.25
- MFPC.CA: score=7.66 buy_ready=False sector_rank=17 price=38.22 support=37.23 resistance=47.63 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=23.79 liquidity=48047471.91 spike=0.57
- MFSC.CA: score=15.33 buy_ready=False sector_rank=12 price=35.64 support=28.55 resistance=42.4 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=58.21 liquidity=5537315.43 spike=2.15
- MHOT.CA: score=16.9 buy_ready=False sector_rank=18 price=15.18 support=13.0 resistance=17.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=48.8 liquidity=12998679.8 spike=2.22
- MICH.CA: score=15.21 buy_ready=False sector_rank=12 price=44.73 support=37.35 resistance=48.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=71.98 liquidity=5710321.2 spike=0.76
- MILS.CA: score=13.17 buy_ready=False sector_rank=12 price=139.91 support=94.24 resistance=163.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=63.85 liquidity=5670552.45 spike=0.49
- MIPH.CA: score=9.42 buy_ready=False sector_rank=11 price=773.08 support=610.0 resistance=820.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=54.78 liquidity=715099.02 spike=0.37
- MOED.CA: score=8.94 buy_ready=False sector_rank=12 price=0.48 support=0.39 resistance=0.56 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=51.72 liquidity=3448881.45 spike=0.24
- MOIL.CA: score=12.4 buy_ready=False sector_rank=10 price=0.69 support=0.6 resistance=0.71 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=61.96 liquidity=44044.33 spike=0.21
- MOIN.CA: score=20.04 buy_ready=False sector_rank=12 price=32.4 support=25.7 resistance=35.5 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=64.19 liquidity=18552370.47 spike=1.77
- MOSC.CA: score=26.5 buy_ready=False sector_rank=12 price=295.73 support=198.01 resistance=308.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=69.43 liquidity=61615347.79 spike=7.13
- MPCI.CA: score=21.98 buy_ready=False sector_rank=12 price=349.05 support=238.6 resistance=382.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=57.63 liquidity=152789302.11 spike=1.24
- MPCO.CA: score=16.89 buy_ready=False sector_rank=19 price=1.99 support=1.55 resistance=2.58 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=58.65 liquidity=66469188.3 spike=0.64
- MPRC.CA: score=19.5 buy_ready=False sector_rank=12 price=38.34 support=27.0 resistance=40.7 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=69.98 liquidity=16263559.68 spike=0.72
- MTIE.CA: score=11.4 buy_ready=False sector_rank=20 price=6.55 support=6.05 resistance=7.72 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=41.31 liquidity=14174226.61 spike=0.64
- NAHO.CA: score=6.5 buy_ready=False sector_rank=12 price=0.13 support=0.12 resistance=0.13 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=53.85 liquidity=3690.43 spike=0.31
- NCCW.CA: score=17.5 buy_ready=False sector_rank=12 price=5.6 support=4.05 resistance=6.34 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=59.36 liquidity=10202729.43 spike=0.52
- NEDA.CA: score=5.58 buy_ready=False sector_rank=12 price=2.46 support=2.26 resistance=2.58 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=47.62 liquidity=88181.16 spike=0.44
- NHPS.CA: score=9.27 buy_ready=False sector_rank=12 price=59.74 support=50.0 resistance=69.97 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=58.42 liquidity=1770096.25 spike=0.22
- NINH.CA: score=14.2 buy_ready=False sector_rank=12 price=15.08 support=12.36 resistance=18.5 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=8708202.32 spike=0.78
- NIPH.CA: score=21.7 buy_ready=False sector_rank=11 price=306.2 support=205.0 resistance=365.5 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=57.8 liquidity=113883745.74 spike=0.68
- OBRI.CA: score=8.47 buy_ready=False sector_rank=12 price=22.69 support=18.11 resistance=26.2 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=48.65 liquidity=2970007.62 spike=0.36
- OCDI.CA: score=18.19 buy_ready=False sector_rank=15 price=25.02 support=21.0 resistance=26.64 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=58.91 liquidity=14275886.84 spike=0.49
- OCPH.CA: score=9.65 buy_ready=False sector_rank=12 price=198.97 support=147.96 resistance=224.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=60.32 liquidity=2156635.84 spike=0.38
- ODIN.CA: score=8.78 buy_ready=False sector_rank=12 price=2.02 support=1.7 resistance=2.28 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=44.44 liquidity=3281277.87 spike=0.4
- OFH.CA: score=16.97 buy_ready=False sector_rank=12 price=0.73 support=0.61 resistance=0.81 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=57.39 liquidity=8471599.02 spike=0.42
- OIH.CA: score=12.4 buy_ready=False sector_rank=21 price=1.6 support=1.5 resistance=1.84 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=42.55 liquidity=18310064.27 spike=0.41
- OLFI.CA: score=14.78 buy_ready=False sector_rank=5 price=20.22 support=17.86 resistance=21.24 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=63.46 liquidity=5898315.34 spike=0.64
- ORAS.CA: score=5.0 buy_ready=False sector_rank=16 price=71.05 support=71.05 resistance=71.05 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ORHD.CA: score=17.19 buy_ready=False sector_rank=15 price=10.33 support=8.5 resistance=10.71 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=59.64 liquidity=51583567.39 spike=0.52
- ORWE.CA: score=18.47 buy_ready=False sector_rank=13 price=25.09 support=22.2 resistance=26.75 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=62.81 liquidity=10383772.55 spike=0.42
- PHAR.CA: score=18.7 buy_ready=False sector_rank=11 price=104.1 support=90.2 resistance=113.97 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=51.98 liquidity=25655028.22 spike=0.35
- PHDC.CA: score=15.35 buy_ready=False sector_rank=15 price=11.62 support=10.33 resistance=13.05 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=52.68 liquidity=129353571.47 spike=1.08
- PHTV.CA: score=6.52 buy_ready=False sector_rank=12 price=328.78 support=300.0 resistance=349.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=72.53 liquidity=22028.26 spike=0.02
- POUL.CA: score=11.88 buy_ready=False sector_rank=5 price=7.58 support=7.51 resistance=10.4 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=26.49 liquidity=96800533.05 spike=0.85
- PRCL.CA: score=14.13 buy_ready=False sector_rank=6 price=18.64 support=16.65 resistance=23.06 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=41.04 liquidity=9285031.06 spike=0.34
- PRDC.CA: score=17.98 buy_ready=False sector_rank=15 price=6.5 support=5.08 resistance=7.2 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=57.33 liquidity=9787973.0 spike=0.56
- PRMH.CA: score=20.64 buy_ready=False sector_rank=12 price=2.26 support=1.7 resistance=2.66 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=67.59 liquidity=20602103.41 spike=2.07
- RACC.CA: score=8.72 buy_ready=False sector_rank=12 price=7.88 support=6.1 resistance=8.55 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=68.75 liquidity=3222305.41 spike=0.51
- RAKT.CA: score=5.62 buy_ready=False sector_rank=12 price=22.47 support=20.4 resistance=23.1 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=98.21 liquidity=119091.0 spike=0.53
- RAYA.CA: score=18.8 buy_ready=False sector_rank=9 price=5.98 support=5.02 resistance=6.33 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=57.79 liquidity=33042878.81 spike=1.21
- RMDA.CA: score=14.7 buy_ready=False sector_rank=11 price=5.16 support=4.5 resistance=5.72 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=48.61 liquidity=15678313.82 spike=0.52
- ROTO.CA: score=9.71 buy_ready=False sector_rank=12 price=31.97 support=25.0 resistance=36.8 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=54.1 liquidity=2212228.04 spike=0.21
- RREI.CA: score=8.74 buy_ready=False sector_rank=12 price=2.65 support=1.96 resistance=3.2 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=3239338.92 spike=0.27
- RTVC.CA: score=5.5 buy_ready=False sector_rank=12 price=3.11 support=2.66 resistance=3.4 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=73.68 liquidity=0.0 spike=0.0
- RUBX.CA: score=16.5 buy_ready=False sector_rank=12 price=13.25 support=10.51 resistance=18.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=54.02 liquidity=40211948.0 spike=0.69
- SAUD.CA: score=21.06 buy_ready=False sector_rank=4 price=23.46 support=19.3 resistance=24.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=73.96 liquidity=19031900.8 spike=0.85
- SCEM.CA: score=17.85 buy_ready=False sector_rank=6 price=97.52 support=73.9 resistance=106.55 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=80.64 liquidity=26973640.99 spike=0.59
- SCFM.CA: score=8.53 buy_ready=False sector_rank=12 price=220.21 support=153.02 resistance=240.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=60.04 liquidity=1032344.51 spike=0.27
- SCTS.CA: score=6.81 buy_ready=False sector_rank=7 price=475.39 support=410.0 resistance=555.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=45.13 liquidity=383164.35 spike=0.06
- SDTI.CA: score=17.5 buy_ready=False sector_rank=12 price=83.0 support=75.01 resistance=90.99 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=16141923.0 spike=0.86
- SEIG.CA: score=10.66 buy_ready=False sector_rank=12 price=231.23 support=142.0 resistance=280.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=65.24 liquidity=1166786.56 spike=0.11
- SIPC.CA: score=18.5 buy_ready=False sector_rank=12 price=5.11 support=3.73 resistance=5.89 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=58.17 liquidity=16807597.82 spike=0.39
- SKPC.CA: score=14.66 buy_ready=False sector_rank=17 price=14.61 support=14.01 resistance=15.75 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=41.41 liquidity=20610852.48 spike=0.61
- SMFR.CA: score=11.58 buy_ready=False sector_rank=12 price=216.65 support=165.0 resistance=264.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=66.47 liquidity=2085472.84 spike=0.27
- SNFC.CA: score=18.23 buy_ready=False sector_rank=12 price=11.38 support=10.08 resistance=11.48 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=71.43 liquidity=8736983.71 spike=0.8
- SPIN.CA: score=8.37 buy_ready=False sector_rank=13 price=14.5 support=12.0 resistance=16.48 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=51.75 liquidity=2902494.0 spike=0.51
- SPMD.CA: score=9.25 buy_ready=False sector_rank=12 price=0.33 support=0.3 resistance=0.37 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=40.43 liquidity=3756294.69 spike=0.25
- SUGR.CA: score=22.88 buy_ready=False sector_rank=5 price=52.08 support=44.62 resistance=55.99 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=62.71 liquidity=17026931.64 spike=0.79
- SVCE.CA: score=18.5 buy_ready=False sector_rank=12 price=9.1 support=7.01 resistance=10.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=58.93 liquidity=51482451.36 spike=0.88
- SWDY.CA: score=22.4 buy_ready=False sector_rank=8 price=117.5 support=97.0 resistance=123.45 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=60.83 liquidity=11865620.0 spike=0.21
- TALM.CA: score=12.54 buy_ready=False sector_rank=7 price=20.12 support=17.0 resistance=21.5 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=57.49 liquidity=3115079.13 spike=0.17
- TMGH.CA: score=17.19 buy_ready=False sector_rank=15 price=82.55 support=76.5 resistance=89.91 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=57.27 liquidity=110792257.75 spike=0.51
- TRTO.CA: score=4.5 buy_ready=False sector_rank=12 price=0.06 support=0.05 resistance=0.06 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=840.0 spike=0.16
- UEFM.CA: score=10.7 buy_ready=False sector_rank=12 price=502.74 support=422.0 resistance=540.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=70.29 liquidity=1200040.36 spike=0.62
- UEGC.CA: score=17.5 buy_ready=False sector_rank=12 price=1.48 support=1.21 resistance=1.59 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=56.1 liquidity=15678982.56 spike=0.52
- UNIP.CA: score=9.59 buy_ready=False sector_rank=12 price=0.31 support=0.25 resistance=0.33 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=62.82 liquidity=2093556.68 spike=0.32
- UNIT.CA: score=3.73 buy_ready=False sector_rank=15 price=15.22 support=15.0 resistance=19.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=29.25 liquidity=3737331.95 spike=1.4
- WCDF.CA: score=7.74 buy_ready=False sector_rank=12 price=513.48 support=450.56 resistance=565.0 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=57.45 liquidity=248010.83 spike=0.2
- WKOL.CA: score=7.97 buy_ready=False sector_rank=12 price=172.01 support=145.33 resistance=275.8 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=58.79 liquidity=2471439.6 spike=0.23
- ZEOT.CA: score=26.5 buy_ready=False sector_rank=12 price=12.92 support=7.9 resistance=13.16 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=71.26 liquidity=52871741.11 spike=5.35
- ZMID.CA: score=18.19 buy_ready=False sector_rank=15 price=6.69 support=5.91 resistance=7.2 source=Yahoo Finance as_of=2026-11-18T22:00:00+00:00 freshness=FRESH RSI=51.7 liquidity=23809670.06 spike=0.31

## Backtesting Lite
- ETRS.CA: 180d return=59.02%, max drawdown=-16.61%, MA20>MA50 days last20=1, as_of=2026-11-18T22:00:00+00:00
- MOSC.CA: 180d return=82.74%, max drawdown=-37.28%, MA20>MA50 days last20=0, as_of=2026-11-18T22:00:00+00:00
- ZEOT.CA: 180d return=68.85%, max drawdown=-38.04%, MA20>MA50 days last20=0, as_of=2026-11-18T22:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ETRS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Transport and Commercial Services Company S.A.E. summary=Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- MOSC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr Oils & Soap summary=Evidence rejected for MOSC.CA: source text did not clearly match MOSC.CA / Misr Oils & Soap.
- ZEOT.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Extracted Oil & Derivatives Co. summary=Evidence rejected for ZEOT.CA: source text did not clearly match ZEOT.CA / Extracted Oil & Derivatives Co..
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- EFID.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Edita Food Industries summary=Evidence rejected for EFID.CA: source text did not clearly match EFID.CA / Edita Food Industries.
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- AJWA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=AJWA For Food Industries Co. Egypt summary=Evidence rejected for AJWA.CA: source text did not clearly match AJWA.CA / AJWA For Food Industries Co. Egypt.
- SUGR.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Delta Sugar summary=Evidence rejected for SUGR.CA: source text did not clearly match SUGR.CA / Delta Sugar.

## Warnings
- OpenRouter API error: 404
- Mubasher stock page returned no evidence titles for ETRS.CA.
- No Yahoo or Mubasher evidence found for ETRS.CA.
- Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Mubasher stock page returned no evidence titles for MOSC.CA.
- No Yahoo or Mubasher evidence found for MOSC.CA.
- Evidence rejected for MOSC.CA: source text did not clearly match MOSC.CA / Misr Oils & Soap.
- Mubasher stock page returned no evidence titles for ZEOT.CA.
- No Yahoo or Mubasher evidence found for ZEOT.CA.
- Evidence rejected for ZEOT.CA: source text did not clearly match ZEOT.CA / Extracted Oil & Derivatives Co..
- Mubasher stock page returned no evidence titles for ETEL.CA.
- No Yahoo or Mubasher evidence found for ETEL.CA.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Mubasher stock page returned no evidence titles for EFID.CA.
- No Yahoo or Mubasher evidence found for EFID.CA.
- Evidence rejected for EFID.CA: source text did not clearly match EFID.CA / Edita Food Industries.
- Mubasher stock page returned no evidence titles for EFIH.CA.
- No Yahoo or Mubasher evidence found for EFIH.CA.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Mubasher stock page returned no evidence titles for AJWA.CA.
- No Yahoo or Mubasher evidence found for AJWA.CA.
- Evidence rejected for AJWA.CA: source text did not clearly match AJWA.CA / AJWA For Food Industries Co. Egypt.
- Mubasher stock page returned no evidence titles for SUGR.CA.
- No Yahoo or Mubasher evidence found for SUGR.CA.
- Evidence rejected for SUGR.CA: source text did not clearly match SUGR.CA / Delta Sugar.
