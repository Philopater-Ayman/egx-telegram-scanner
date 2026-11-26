# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-11-26T21:48:18.368866+00:00
Generated Cairo: 2026-11-26 23:48
Run timing: target 15:30 Cairo | generated Cairo 2026-11-26 23:48 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-11-26 23:46

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
- EGX30 regime: BEARISH / above MA20 45.0% / above MA50 30.0%
- EGX70 regime: BEARISH / above MA20 35.9% / above MA50 12.82%
- Sector breadth: 9.52%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=392931469.46 spike=1.12 score=14.04
- TMGH.CA: liquidity=362771762.18 spike=1.68 score=14.03
- HRHO.CA: liquidity=258227366.77 spike=2.61 score=23.39
- ETEL.CA: liquidity=240457833.13 spike=0.9 score=24.4
- COMI.CA: liquidity=232795332.0 spike=0.57 score=16.0

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- EGSA.CA: spike=5.35 liquidity=56745.0 outlook=NEUTRAL score=44 buy_ready=False
- ZEOT.CA: spike=4.6 liquidity=81933434.38 outlook=BULLISH_WATCH score=79.33 buy_ready=False
- MTIE.CA: spike=4.44 liquidity=170077394.25 outlook=NEUTRAL score=45.16 buy_ready=False
- COSG.CA: spike=4.41 liquidity=75174066.23 outlook=CONSTRUCTIVE score=56.33 buy_ready=False
- MICH.CA: spike=3.49 liquidity=28478044.73 outlook=BULLISH_WATCH score=75.33 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=11.53 5d=-0.97% 20d=6.15% aboveMA50=100.0%
- #2 Textiles: score=8.68 5d=2.16% 20d=6.84% aboveMA50=25.0%
- #3 Fintech & Payments: score=6.92 5d=1.0% 20d=7.19% aboveMA50=50.0%
- #4 Technology & Distribution: score=6.02 5d=0.52% 20d=3.41% aboveMA50=0.0%
- #5 Transportation & Logistics: score=5.97 5d=1.57% 20d=8.7% aboveMA50=50.0%
- #6 Building Materials: score=3.94 5d=-2.48% 20d=7.22% aboveMA50=33.33%
- #7 Food, Beverages & Tobacco: score=3.23 5d=-3.08% 20d=3.57% aboveMA50=42.86%
- #8 Banking & Financials: score=2.49 5d=-1.5% 20d=1.81% aboveMA50=20.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ETEL.CA: BULLISH_WATCH score=87 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- ACGC.CA: BULLISH_WATCH score=85.68 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended; close to resistance
- ETRS.CA: BULLISH_WATCH score=83.33 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ZEOT.CA: BULLISH_WATCH score=79.33 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support; sector is not leading
- SMFR.CA: BULLISH_WATCH score=79.33 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- SPIN.CA: BULLISH_WATCH score=78.68 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=below MA50
- MICH.CA: BULLISH_WATCH score=75.33 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- DOMT.CA: BULLISH_WATCH score=73.23 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- EFIH.CA: BULLISH_WATCH score=72.92 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- MOSC.CA: BULLISH_WATCH score=71.33 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- PRDC.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- MPCI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=4.08 buy_ready=False sector_rank=11 price=219.62 support=201.06 resistance=269.99 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=34.04 liquidity=5550675.76 spike=0.3
- ABUK.CA: score=7.81 buy_ready=False sector_rank=17 price=73.56 support=73.01 resistance=92.33 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=31.08 liquidity=23146756.63 spike=0.21
- ACAMD.CA: score=8.53 buy_ready=False sector_rank=11 price=1.87 support=1.87 resistance=2.16 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=34.62 liquidity=34958215.8 spike=0.5
- ACGC.CA: score=25.1 buy_ready=False sector_rank=2 price=13.99 support=12.2 resistance=14.2 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=67.93 liquidity=13975701.99 spike=1.85
- ADCI.CA: score=6.33 buy_ready=False sector_rank=11 price=242.73 support=217.26 resistance=269.17 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=46.42 liquidity=1801056.57 spike=0.72
- ADIB.CA: score=8.73 buy_ready=False sector_rank=8 price=45.93 support=44.5 resistance=50.49 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=31.23 liquidity=9734128.68 spike=0.17
- ADPC.CA: score=8.6 buy_ready=False sector_rank=11 price=2.87 support=2.71 resistance=3.25 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=39.78 liquidity=3067880.64 spike=0.46
- AFDI.CA: score=17.52 buy_ready=False sector_rank=11 price=44.71 support=40.0 resistance=48.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=52.91 liquidity=6827842.8 spike=2.08
- AFMC.CA: score=14.53 buy_ready=False sector_rank=11 price=129.01 support=108.53 resistance=166.23 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=43.94 liquidity=12516033.63 spike=0.41
- AJWA.CA: score=17.53 buy_ready=False sector_rank=11 price=266.01 support=200.0 resistance=294.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=71.11 liquidity=17122000.29 spike=0.36
- ALCN.CA: score=8.3 buy_ready=False sector_rank=5 price=31.26 support=30.0 resistance=33.89 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=43.55 liquidity=1914612.49 spike=0.21
- ALUM.CA: score=4.63 buy_ready=False sector_rank=11 price=18.42 support=17.13 resistance=21.8 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=42.94 liquidity=1102565.94 spike=0.42
- AMER.CA: score=8.67 buy_ready=False sector_rank=19 price=3.52 support=3.51 resistance=4.74 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=21.05 liquidity=42478310.81 spike=0.57
- AMES.CA: score=13.53 buy_ready=False sector_rank=11 price=37.31 support=31.21 resistance=54.49 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=54.15 liquidity=137063438.82 spike=0.53
- AMIA.CA: score=2.21 buy_ready=False sector_rank=11 price=15.38 support=15.02 resistance=18.77 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=19.48 liquidity=2673136.3 spike=0.21
- AMOC.CA: score=9.54 buy_ready=False sector_rank=13 price=11.9 support=11.73 resistance=15.15 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=23.62 liquidity=148447889.94 spike=1.01
- APSW.CA: score=5.79 buy_ready=False sector_rank=11 price=7.5 support=7.18 resistance=8.07 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=52.78 liquidity=253747.5 spike=0.63
- ARAB.CA: score=15.67 buy_ready=False sector_rank=19 price=0.25 support=0.22 resistance=0.26 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=61.54 liquidity=35900201.81 spike=0.52
- ARCC.CA: score=11.87 buy_ready=False sector_rank=6 price=65.95 support=61.05 resistance=74.2 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=47.93 liquidity=6293872.01 spike=0.25
- AREH.CA: score=9.54 buy_ready=False sector_rank=11 price=1.0 support=0.97 resistance=1.17 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=38.89 liquidity=6009794.0 spike=0.85
- ASCM.CA: score=8.9 buy_ready=False sector_rank=11 price=44.47 support=41.0 resistance=50.4 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=49.27 liquidity=3372427.01 spike=0.64
- ASPI.CA: score=10.24 buy_ready=False sector_rank=11 price=0.31 support=0.28 resistance=0.36 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=45.16 liquidity=4709899.0 spike=0.22
- ATLC.CA: score=7.94 buy_ready=False sector_rank=15 price=5.08 support=4.5 resistance=6.06 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=51.68 liquidity=2770291.6 spike=0.26
- ATQA.CA: score=14.81 buy_ready=False sector_rank=17 price=9.74 support=8.67 resistance=11.01 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=58.27 liquidity=18892317.18 spike=0.44
- AXPH.CA: score=8.42 buy_ready=False sector_rank=11 price=1314.18 support=1179.35 resistance=1415.42 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=57.01 liquidity=1889790.92 spike=0.41
- BINV.CA: score=10.4 buy_ready=False sector_rank=18 price=52.42 support=49.0 resistance=57.98 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=49.32 liquidity=2598302.05 spike=0.33
- BIOC.CA: score=19.53 buy_ready=False sector_rank=11 price=370.01 support=259.51 resistance=446.13 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=60.07 liquidity=70109126.64 spike=0.34
- BTFH.CA: score=13.17 buy_ready=False sector_rank=15 price=2.17 support=2.08 resistance=2.59 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=35.59 liquidity=80822588.11 spike=0.67
- CAED.CA: score=18.53 buy_ready=False sector_rank=11 price=101.85 support=75.1 resistance=116.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=49.28 liquidity=13754638.59 spike=0.47
- CANA.CA: score=9.06 buy_ready=False sector_rank=8 price=32.89 support=29.33 resistance=48.49 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=60.7 liquidity=3064821.7 spike=0.14
- CCAP.CA: score=14.04 buy_ready=False sector_rank=18 price=5.62 support=5.55 resistance=6.35 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=37.75 liquidity=392931469.46 spike=1.12
- CCRS.CA: score=13.11 buy_ready=False sector_rank=11 price=2.0 support=1.54 resistance=2.49 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=54.95 liquidity=5576768.0 spike=0.29
- CEFM.CA: score=11.73 buy_ready=False sector_rank=11 price=126.55 support=106.0 resistance=138.99 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=61.51 liquidity=194001.15 spike=0.07
- CERA.CA: score=15.53 buy_ready=False sector_rank=11 price=1.0 support=0.96 resistance=1.19 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=45.24 liquidity=12326399.0 spike=0.27
- CFGH.CA: score=2.53 buy_ready=False sector_rank=11 price=0.11 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=88.89 liquidity=995.1 spike=0.32
- CICH.CA: score=4.88 buy_ready=False sector_rank=15 price=10.1 support=9.88 resistance=11.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=38.19 liquidity=1707506.06 spike=0.72
- CIEB.CA: score=9.32 buy_ready=False sector_rank=8 price=22.69 support=21.9 resistance=23.95 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=50.12 liquidity=3328781.91 spike=0.38
- CIRA.CA: score=14.63 buy_ready=False sector_rank=10 price=37.0 support=33.7 resistance=40.11 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=51.97 liquidity=14028883.0 spike=0.78
- CLHO.CA: score=17.53 buy_ready=False sector_rank=12 price=14.2 support=12.88 resistance=15.15 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=62.84 liquidity=20072367.13 spike=0.62
- CNFN.CA: score=5.09 buy_ready=False sector_rank=15 price=3.79 support=3.47 resistance=4.32 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=48.15 liquidity=1918001.49 spike=0.3
- COMI.CA: score=16.0 buy_ready=False sector_rank=8 price=126.0 support=117.41 resistance=131.36 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=48.18 liquidity=232795332.0 spike=0.57
- COPR.CA: score=18.53 buy_ready=False sector_rank=11 price=0.42 support=0.36 resistance=0.46 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=52.51 liquidity=21595973.96 spike=0.99
- COSG.CA: score=22.53 buy_ready=False sector_rank=11 price=1.37 support=1.21 resistance=1.49 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=57.14 liquidity=75174066.23 spike=4.41
- CPCI.CA: score=1.8 buy_ready=False sector_rank=11 price=550.05 support=550.01 resistance=597.07 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=21.52 liquidity=2266756.0 spike=0.68
- CSAG.CA: score=12.69 buy_ready=False sector_rank=5 price=38.03 support=31.54 resistance=39.7 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=83.25 liquidity=4299747.72 spike=0.6
- DAPH.CA: score=13.72 buy_ready=False sector_rank=11 price=82.0 support=73.45 resistance=98.1 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=48.55 liquidity=8185076.0 spike=0.41
- DEIN.CA: score=13.53 buy_ready=False sector_rank=11 price=10.35 support=7.9 resistance=10.35 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=15.42 buy_ready=False sector_rank=7 price=24.77 support=22.0 resistance=26.5 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=57.07 liquidity=3571289.13 spike=1.28
- DSCW.CA: score=9.52 buy_ready=False sector_rank=11 price=1.41 support=1.38 resistance=1.66 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=45.65 liquidity=5992611.25 spike=0.45
- DTPP.CA: score=17.53 buy_ready=False sector_rank=11 price=57.7 support=42.5 resistance=69.99 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=63.05 liquidity=16109436.31 spike=0.31
- EALR.CA: score=8.5 buy_ready=False sector_rank=11 price=287.81 support=247.0 resistance=337.99 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=44.13 liquidity=2963579.54 spike=0.37
- EASB.CA: score=2.1 buy_ready=False sector_rank=11 price=5.5 support=5.34 resistance=7.2 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=24.1 liquidity=3564022.0 spike=0.56
- EAST.CA: score=17.29 buy_ready=False sector_rank=7 price=33.03 support=29.31 resistance=35.2 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=48.83 liquidity=29345106.06 spike=0.65
- EBSC.CA: score=4.3 buy_ready=False sector_rank=11 price=1.45 support=1.33 resistance=1.7 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=42.31 liquidity=771114.38 spike=0.22
- ECAP.CA: score=7.87 buy_ready=False sector_rank=11 price=28.03 support=25.51 resistance=30.4 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=54.2 liquidity=338546.35 spike=0.13
- EDFM.CA: score=7.35 buy_ready=False sector_rank=11 price=357.32 support=312.0 resistance=378.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=55.28 liquidity=818620.14 spike=0.71
- EEII.CA: score=12.94 buy_ready=False sector_rank=11 price=1.97 support=1.55 resistance=2.29 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=57.94 liquidity=5410285.94 spike=0.36
- EFIC.CA: score=12.81 buy_ready=False sector_rank=17 price=153.72 support=130.04 resistance=174.88 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=57.93 liquidity=14612469.6 spike=0.61
- EFID.CA: score=21.29 buy_ready=False sector_rank=7 price=20.7 support=17.5 resistance=21.35 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=60.32 liquidity=13063936.08 spike=0.35
- EFIH.CA: score=24.4 buy_ready=False sector_rank=3 price=25.0 support=21.4 resistance=26.18 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=62.31 liquidity=16701550.0 spike=0.27
- EGAL.CA: score=15.81 buy_ready=False sector_rank=17 price=293.35 support=276.75 resistance=318.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=37.74 liquidity=45796042.85 spike=0.65
- EGAS.CA: score=9.39 buy_ready=False sector_rank=13 price=48.58 support=43.81 resistance=61.68 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=56.58 liquidity=1869747.11 spike=0.45
- EGBE.CA: score=7.02 buy_ready=False sector_rank=8 price=0.5 support=0.48 resistance=0.51 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=58.06 liquidity=19868.27 spike=0.33
- EGCH.CA: score=14.81 buy_ready=False sector_rank=17 price=9.69 support=9.66 resistance=11.3 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=37.17 liquidity=21824873.26 spike=0.65
- EGSA.CA: score=16.46 buy_ready=False sector_rank=1 price=9.0 support=8.7 resistance=9.12 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=93.94 liquidity=56745.0 spike=5.35
- EGTS.CA: score=5.89 buy_ready=False sector_rank=19 price=11.97 support=11.31 resistance=14.45 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=39.72 liquidity=3223401.37 spike=0.15
- EHDR.CA: score=10.43 buy_ready=False sector_rank=11 price=2.01 support=1.86 resistance=2.28 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=46.67 liquidity=4896454.45 spike=0.62
- ELEC.CA: score=13.5 buy_ready=False sector_rank=14 price=1.53 support=1.45 resistance=1.78 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=42.86 liquidity=13831078.87 spike=0.52
- ELKA.CA: score=13.05 buy_ready=False sector_rank=11 price=1.39 support=1.36 resistance=1.63 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=42.59 liquidity=9519677.61 spike=0.81
- ELNA.CA: score=7.53 buy_ready=False sector_rank=11 price=41.28 support=37.26 resistance=44.2 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=65.3 liquidity=1073.28 spike=0.0
- ELSH.CA: score=7.64 buy_ready=False sector_rank=11 price=10.44 support=9.4 resistance=11.8 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=51.9 liquidity=4112127.91 spike=0.28
- ELWA.CA: score=-0.74 buy_ready=False sector_rank=11 price=1.09 support=1.07 resistance=1.57 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=21.82 liquidity=726143.85 spike=0.47
- EMFD.CA: score=13.67 buy_ready=False sector_rank=19 price=12.03 support=11.41 resistance=12.96 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=45.74 liquidity=35201210.79 spike=0.45
- ENGC.CA: score=14.81 buy_ready=False sector_rank=11 price=37.0 support=30.54 resistance=43.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=53.99 liquidity=5274720.0 spike=0.25
- EOSB.CA: score=9.55 buy_ready=False sector_rank=11 price=1.61 support=1.55 resistance=1.69 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=19278.14 spike=0.26
- EPCO.CA: score=4.07 buy_ready=False sector_rank=11 price=8.29 support=7.66 resistance=9.98 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=47.25 liquidity=538725.65 spike=0.11
- EPPK.CA: score=7.53 buy_ready=False sector_rank=11 price=9.78 support=9.78 resistance=9.78 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ETEL.CA: score=24.4 buy_ready=False sector_rank=1 price=139.2 support=116.83 resistance=147.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=68.17 liquidity=240457833.13 spike=0.9
- ETRS.CA: score=23.25 buy_ready=False sector_rank=11 price=11.15 support=10.25 resistance=11.58 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=59.8 liquidity=33396333.91 spike=1.86
- EXPA.CA: score=14.52 buy_ready=False sector_rank=8 price=14.42 support=13.13 resistance=15.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=62.25 liquidity=6520161.65 spike=0.46
- FAIT.CA: score=11.26 buy_ready=False sector_rank=8 price=46.15 support=42.03 resistance=47.46 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=65.79 liquidity=1259525.84 spike=0.57
- FAITA.CA: score=8.0 buy_ready=False sector_rank=8 price=1.0 support=0.98 resistance=1.03 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=58.33 liquidity=3000.0 spike=0.1
- FERC.CA: score=6.6 buy_ready=False sector_rank=17 price=62.98 support=56.0 resistance=72.69 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=56.23 liquidity=1795370.85 spike=0.17
- FWRY.CA: score=20.4 buy_ready=False sector_rank=3 price=17.25 support=15.27 resistance=18.5 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=51.96 liquidity=51559956.75 spike=0.5
- GBCO.CA: score=15.86 buy_ready=False sector_rank=9 price=21.8 support=20.9 resistance=23.85 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=46.86 liquidity=24494566.34 spike=0.28
- GDWA.CA: score=8.08 buy_ready=False sector_rank=11 price=0.51 support=0.45 resistance=0.59 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=37.2 liquidity=4543291.54 spike=0.48
- GGCC.CA: score=13.87 buy_ready=False sector_rank=11 price=0.51 support=0.5 resistance=0.62 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=36.25 liquidity=8337143.7 spike=0.43
- GIHD.CA: score=12.47 buy_ready=False sector_rank=11 price=46.07 support=37.07 resistance=57.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=53.51 liquidity=6938556.58 spike=0.4
- GMCI.CA: score=8.58 buy_ready=False sector_rank=11 price=1.61 support=1.34 resistance=1.75 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=72.73 liquidity=47998.93 spike=0.12
- GRCA.CA: score=21.19 buy_ready=False sector_rank=11 price=33.55 support=24.18 resistance=37.32 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=50.79 liquidity=19814696.65 spike=1.33
- GSSC.CA: score=0.58 buy_ready=False sector_rank=11 price=225.87 support=225.03 resistance=296.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=30.83 liquidity=2044123.46 spike=0.85
- GTWL.CA: score=16.53 buy_ready=False sector_rank=11 price=128.29 support=88.2 resistance=158.99 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=51.66 liquidity=209248163.29 spike=0.75
- HDBK.CA: score=18.0 buy_ready=False sector_rank=8 price=102.7 support=92.9 resistance=111.2 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=61.5 liquidity=22500234.23 spike=0.74
- HELI.CA: score=12.67 buy_ready=False sector_rank=19 price=6.23 support=5.93 resistance=7.2 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=39.08 liquidity=17643017.4 spike=0.29
- HRHO.CA: score=23.39 buy_ready=False sector_rank=15 price=26.33 support=21.87 resistance=26.9 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=71.28 liquidity=258227366.77 spike=2.61
- ICID.CA: score=5.65 buy_ready=False sector_rank=11 price=16.73 support=15.66 resistance=17.98 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=45.42 liquidity=1115974.62 spike=0.35
- IDRE.CA: score=7.38 buy_ready=False sector_rank=11 price=38.28 support=32.1 resistance=47.25 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=48.93 liquidity=1844406.9 spike=0.25
- IFAP.CA: score=6.55 buy_ready=False sector_rank=20 price=15.82 support=15.12 resistance=19.4 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=46.75 liquidity=3888429.36 spike=0.57
- INFI.CA: score=19.53 buy_ready=False sector_rank=11 price=148.28 support=105.5 resistance=178.25 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=70.61 liquidity=32311397.97 spike=0.49
- IRON.CA: score=7.75 buy_ready=False sector_rank=17 price=23.82 support=23.13 resistance=27.22 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=48.4 liquidity=2942270.18 spike=0.39
- ISMA.CA: score=8.1 buy_ready=False sector_rank=11 price=18.85 support=18.01 resistance=22.54 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=46.53 liquidity=2569160.8 spike=0.23
- ISMQ.CA: score=0.14 buy_ready=False sector_rank=17 price=6.45 support=6.2 resistance=7.34 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=28.62 liquidity=2335422.38 spike=0.21
- ISPH.CA: score=15.53 buy_ready=False sector_rank=12 price=10.03 support=9.02 resistance=10.72 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=48.09 liquidity=37225180.53 spike=0.6
- JUFO.CA: score=11.19 buy_ready=False sector_rank=7 price=21.85 support=21.54 resistance=25.51 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=29.33 liquidity=53231866.78 spike=1.95
- KABO.CA: score=28.34 buy_ready=False sector_rank=2 price=7.75 support=6.34 resistance=7.87 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=64.22 liquidity=58824298.0 spike=2.97
- KWIN.CA: score=7.95 buy_ready=False sector_rank=11 price=66.21 support=50.52 resistance=85.83 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=42.5 liquidity=2413884.15 spike=0.18
- KZPC.CA: score=2.03 buy_ready=False sector_rank=11 price=10.32 support=10.1 resistance=14.77 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=32.53 liquidity=3497922.62 spike=0.32
- LCSW.CA: score=22.58 buy_ready=False sector_rank=6 price=41.39 support=33.45 resistance=42.14 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=72.34 liquidity=14267381.13 spike=0.7
- LUTS.CA: score=13.53 buy_ready=False sector_rank=11 price=0.63 support=0.58 resistance=0.84 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=36.24 liquidity=17949884.19 spike=0.28
- MAAL.CA: score=8.53 buy_ready=False sector_rank=11 price=5.85 support=5.66 resistance=7.55 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=25.33 liquidity=18002994.46 spike=0.65
- MASR.CA: score=8.53 buy_ready=False sector_rank=11 price=6.23 support=6.0 resistance=7.11 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=34.29 liquidity=16833329.22 spike=0.58
- MBSC.CA: score=19.58 buy_ready=False sector_rank=6 price=333.45 support=293.6 resistance=397.9 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=58.58 liquidity=22531884.22 spike=0.38
- MCQE.CA: score=18.58 buy_ready=False sector_rank=6 price=174.31 support=157.11 resistance=205.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=56.0 liquidity=11938143.11 spike=0.27
- MCRO.CA: score=13.69 buy_ready=False sector_rank=11 price=1.3 support=1.21 resistance=1.48 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=47.5 liquidity=51399907.71 spike=1.08
- MENA.CA: score=12.58 buy_ready=False sector_rank=19 price=6.56 support=5.5 resistance=7.9 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=59.72 liquidity=1912141.58 spike=0.19
- MEPA.CA: score=8.14 buy_ready=False sector_rank=11 price=1.29 support=1.19 resistance=1.5 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=2608022.59 spike=0.19
- MFPC.CA: score=7.81 buy_ready=False sector_rank=17 price=37.01 support=36.02 resistance=47.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=26.76 liquidity=44344269.69 spike=0.55
- MFSC.CA: score=6.08 buy_ready=False sector_rank=11 price=34.47 support=31.12 resistance=39.48 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=45.31 liquidity=543247.22 spike=0.28
- MHOT.CA: score=2.83 buy_ready=False sector_rank=21 price=14.88 support=13.62 resistance=17.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=35.01 liquidity=553000.32 spike=0.1
- MICH.CA: score=24.51 buy_ready=False sector_rank=11 price=44.85 support=39.0 resistance=48.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=67.58 liquidity=28478044.73 spike=3.49
- MILS.CA: score=8.7 buy_ready=False sector_rank=11 price=132.21 support=108.45 resistance=163.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=52.78 liquidity=3168280.6 spike=0.3
- MIPH.CA: score=12.25 buy_ready=False sector_rank=12 price=788.35 support=730.0 resistance=820.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=47.65 liquidity=721340.23 spike=0.57
- MOED.CA: score=9.07 buy_ready=False sector_rank=11 price=0.47 support=0.43 resistance=0.54 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=47.49 liquidity=3538543.3 spike=0.28
- MOIL.CA: score=8.41 buy_ready=False sector_rank=13 price=0.66 support=0.61 resistance=0.71 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=60.87 liquidity=350707.1 spike=1.77
- MOIN.CA: score=8.83 buy_ready=False sector_rank=11 price=30.04 support=27.01 resistance=35.5 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=54.34 liquidity=2299471.95 spike=0.23
- MOSC.CA: score=25.77 buy_ready=False sector_rank=11 price=292.4 support=227.0 resistance=309.1 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=62.5 liquidity=36137130.45 spike=3.12
- MPCO.CA: score=14.66 buy_ready=False sector_rank=20 price=1.88 support=1.67 resistance=2.58 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=51.82 liquidity=56539213.86 spike=0.58
- MPRC.CA: score=12.79 buy_ready=False sector_rank=11 price=36.3 support=30.58 resistance=40.7 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=57.72 liquidity=4262019.21 spike=0.2
- MTIE.CA: score=18.86 buy_ready=False sector_rank=9 price=6.75 support=6.15 resistance=7.72 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=49.04 liquidity=170077394.25 spike=4.44
- NAHO.CA: score=3.74 buy_ready=False sector_rank=11 price=0.12 support=0.12 resistance=0.13 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=11586.5 spike=1.1
- NCCW.CA: score=9.26 buy_ready=False sector_rank=11 price=5.17 support=4.81 resistance=6.34 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=45.0 liquidity=5724560.13 spike=0.3
- NEDA.CA: score=7.61 buy_ready=False sector_rank=11 price=2.46 support=2.26 resistance=2.54 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=75640.08 spike=0.4
- NHPS.CA: score=5.13 buy_ready=False sector_rank=11 price=55.86 support=53.0 resistance=69.97 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=39.36 liquidity=1595585.06 spike=0.22
- NINH.CA: score=6.89 buy_ready=False sector_rank=11 price=14.83 support=13.71 resistance=18.5 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=47.35 liquidity=1355461.99 spike=0.12
- NIPH.CA: score=14.53 buy_ready=False sector_rank=12 price=277.03 support=239.59 resistance=364.88 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=49.85 liquidity=61571025.35 spike=0.38
- OBRI.CA: score=5.12 buy_ready=False sector_rank=11 price=21.45 support=20.25 resistance=26.2 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=40.12 liquidity=1585820.01 spike=0.23
- OCDI.CA: score=12.67 buy_ready=False sector_rank=19 price=23.6 support=21.6 resistance=26.64 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=44.86 liquidity=15718119.45 spike=0.6
- OCPH.CA: score=7.15 buy_ready=False sector_rank=11 price=189.2 support=163.01 resistance=224.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=51.62 liquidity=1614254.37 spike=0.3
- ODIN.CA: score=6.8 buy_ready=False sector_rank=11 price=2.03 support=1.84 resistance=2.28 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=47.83 liquidity=1269308.23 spike=0.16
- OFH.CA: score=11.3 buy_ready=False sector_rank=11 price=0.7 support=0.67 resistance=0.81 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=48.11 liquidity=5771840.1 spike=0.31
- OIH.CA: score=12.8 buy_ready=False sector_rank=18 price=1.56 support=1.46 resistance=1.84 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=37.68 liquidity=25571490.98 spike=0.64
- OLFI.CA: score=10.97 buy_ready=False sector_rank=7 price=20.38 support=18.17 resistance=21.24 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=64.49 liquidity=2677687.33 spike=0.36
- ORAS.CA: score=5.0 buy_ready=False sector_rank=16 price=71.05 support=71.05 resistance=71.05 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ORHD.CA: score=17.25 buy_ready=False sector_rank=19 price=10.38 support=9.16 resistance=10.71 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=56.31 liquidity=112563638.02 spike=1.29
- ORWE.CA: score=18.4 buy_ready=False sector_rank=2 price=24.0 support=22.2 resistance=26.75 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=39.4 liquidity=13389792.0 spike=0.65
- PHAR.CA: score=14.53 buy_ready=False sector_rank=12 price=99.49 support=92.11 resistance=113.97 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=46.58 liquidity=16794210.11 spike=0.26
- PHDC.CA: score=14.75 buy_ready=False sector_rank=19 price=11.35 support=10.33 resistance=12.8 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=51.04 liquidity=133396985.78 spike=1.04
- PHTV.CA: score=8.59 buy_ready=False sector_rank=11 price=335.0 support=307.0 resistance=349.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=87.8 liquidity=60635.0 spike=0.05
- POUL.CA: score=11.29 buy_ready=False sector_rank=7 price=6.73 support=6.71 resistance=10.4 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=11.79 liquidity=55192191.76 spike=0.5
- PRCL.CA: score=9.58 buy_ready=False sector_rank=6 price=17.9 support=16.78 resistance=23.06 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=29.65 liquidity=18364379.31 spike=0.66
- PRMH.CA: score=5.55 buy_ready=False sector_rank=11 price=2.05 support=1.78 resistance=2.66 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=53.91 liquidity=2015682.95 spike=0.18
- RACC.CA: score=11.33 buy_ready=False sector_rank=11 price=7.51 support=6.9 resistance=8.55 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=43.19 liquidity=5675660.14 spike=1.06
- RAKT.CA: score=6.91 buy_ready=False sector_rank=11 price=22.47 support=20.4 resistance=23.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=87.5 liquidity=296716.34 spike=1.54
- RAYA.CA: score=20.24 buy_ready=False sector_rank=4 price=5.76 support=5.02 resistance=6.33 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=55.76 liquidity=44592890.73 spike=1.42
- RMDA.CA: score=6.44 buy_ready=False sector_rank=12 price=5.05 support=4.86 resistance=5.72 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=30.63 liquidity=6913278.56 spike=0.26
- ROTO.CA: score=5.35 buy_ready=False sector_rank=11 price=30.18 support=28.37 resistance=36.8 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=43.78 liquidity=1820699.06 spike=0.2
- RREI.CA: score=10.79 buy_ready=False sector_rank=11 price=2.55 support=2.35 resistance=3.06 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=37.0 liquidity=5259775.25 spike=0.51
- RTVC.CA: score=4.53 buy_ready=False sector_rank=11 price=3.11 support=2.66 resistance=3.15 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=96.97 liquidity=0.0 spike=0.0
- RUBX.CA: score=14.53 buy_ready=False sector_rank=11 price=12.27 support=11.75 resistance=15.98 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=39.85 liquidity=14730147.82 spike=0.33
- SAUD.CA: score=19.0 buy_ready=False sector_rank=8 price=21.95 support=19.3 resistance=24.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=62.91 liquidity=13853764.93 spike=0.64
- SCEM.CA: score=22.58 buy_ready=False sector_rank=6 price=97.51 support=80.12 resistance=106.55 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=61.42 liquidity=12097578.42 spike=0.27
- SCFM.CA: score=6.35 buy_ready=False sector_rank=11 price=210.72 support=183.03 resistance=240.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=40.41 liquidity=819068.64 spike=0.23
- SCTS.CA: score=-0.86 buy_ready=False sector_rank=10 price=457.04 support=450.0 resistance=547.9 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=32.84 liquidity=511427.77 spike=0.15
- SDTI.CA: score=5.62 buy_ready=False sector_rank=11 price=83.58 support=79.5 resistance=90.99 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=34.09 liquidity=3084603.55 spike=0.16
- SEIG.CA: score=7.7 buy_ready=False sector_rank=11 price=219.3 support=149.57 resistance=280.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=27.55 liquidity=5163199.27 spike=0.47
- SIPC.CA: score=13.58 buy_ready=False sector_rank=11 price=4.66 support=4.2 resistance=5.89 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=49.83 liquidity=9043340.16 spike=0.23
- SKPC.CA: score=16.95 buy_ready=False sector_rank=17 price=14.76 support=13.85 resistance=15.46 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=51.17 liquidity=31958765.78 spike=1.07
- SMFR.CA: score=24.13 buy_ready=False sector_rank=11 price=216.03 support=178.0 resistance=264.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=61.97 liquidity=20432549.34 spike=2.3
- SNFC.CA: score=12.43 buy_ready=False sector_rank=11 price=11.31 support=10.15 resistance=11.48 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=70.89 liquidity=2895099.98 spike=0.28
- SPIN.CA: score=24.9 buy_ready=False sector_rank=2 price=15.14 support=13.3 resistance=16.48 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=56.22 liquidity=12906835.15 spike=2.75
- SPMD.CA: score=11.58 buy_ready=False sector_rank=11 price=0.32 support=0.31 resistance=0.37 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=35.87 liquidity=8048171.4 spike=0.6
- SUGR.CA: score=14.02 buy_ready=False sector_rank=7 price=49.68 support=46.5 resistance=55.99 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=54.81 liquidity=4727846.91 spike=0.22
- SVCE.CA: score=13.53 buy_ready=False sector_rank=11 price=8.46 support=7.97 resistance=10.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=41.95 liquidity=17604008.0 spike=0.32
- SWDY.CA: score=17.5 buy_ready=False sector_rank=14 price=116.02 support=106.0 resistance=123.45 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=58.33 liquidity=23917754.35 spike=0.49
- TALM.CA: score=18.36 buy_ready=False sector_rank=10 price=20.12 support=17.9 resistance=21.5 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=56.16 liquidity=9733915.57 spike=0.57
- TMGH.CA: score=14.03 buy_ready=False sector_rank=19 price=78.95 support=76.5 resistance=86.48 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=43.21 liquidity=362771762.18 spike=1.68
- TRTO.CA: score=4.53 buy_ready=False sector_rank=11 price=0.06 support=0.05 resistance=0.06 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=1.98 spike=0.0
- UEFM.CA: score=11.71 buy_ready=False sector_rank=11 price=496.27 support=422.11 resistance=540.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=63.45 liquidity=180642.28 spike=0.1
- UEGC.CA: score=11.64 buy_ready=False sector_rank=11 price=1.4 support=1.3 resistance=1.59 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=42.55 liquidity=8104382.86 spike=0.31
- UNIP.CA: score=8.96 buy_ready=False sector_rank=11 price=0.29 support=0.27 resistance=0.33 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=49.51 liquidity=3423187.49 spike=0.59
- UNIT.CA: score=-0.36 buy_ready=False sector_rank=19 price=15.52 support=14.16 resistance=19.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=28.43 liquidity=976332.19 spike=0.39
- WCDF.CA: score=5.72 buy_ready=False sector_rank=11 price=501.26 support=478.0 resistance=565.0 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=49.72 liquidity=189977.54 spike=0.17
- WKOL.CA: score=2.39 buy_ready=False sector_rank=11 price=164.62 support=153.53 resistance=194.85 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=28.96 liquidity=1858559.74 spike=0.19
- ZEOT.CA: score=26.53 buy_ready=False sector_rank=11 price=13.31 support=9.87 resistance=13.98 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=69.34 liquidity=81933434.38 spike=4.6
- ZMID.CA: score=8.75 buy_ready=False sector_rank=19 price=6.09 support=6.01 resistance=7.2 source=Yahoo Finance as_of=2026-11-24T22:00:00+00:00 freshness=FRESH RSI=30.81 liquidity=133370254.27 spike=1.54

## Backtesting Lite
- KABO.CA: 180d return=41.17%, max drawdown=-38.3%, MA20>MA50 days last20=0, as_of=2026-11-24T22:00:00+00:00
- ZEOT.CA: 180d return=97.66%, max drawdown=-38.04%, MA20>MA50 days last20=0, as_of=2026-11-24T22:00:00+00:00
- MOSC.CA: 180d return=101.35%, max drawdown=-37.28%, MA20>MA50 days last20=0, as_of=2026-11-24T22:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- KABO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=El Nasr Clothing and Textiles summary=Evidence rejected for KABO.CA: source text did not clearly match KABO.CA / El Nasr Clothing and Textiles.
- ZEOT.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Extracted Oil & Derivatives Co. summary=Evidence rejected for ZEOT.CA: source text did not clearly match ZEOT.CA / Extracted Oil & Derivatives Co..
- MOSC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr Oils & Soap summary=Evidence rejected for MOSC.CA: source text did not clearly match MOSC.CA / Misr Oils & Soap.
- ACGC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Arab Cotton Ginning summary=Evidence rejected for ACGC.CA: source text did not clearly match ACGC.CA / Arab Cotton Ginning.
- SPIN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Spinning and Weaving summary=Evidence rejected for SPIN.CA: source text did not clearly match SPIN.CA / Alexandria Spinning and Weaving.
- MICH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr Chemical Industries Co. summary=Evidence rejected for MICH.CA: source text did not clearly match MICH.CA / Misr Chemical Industries Co..
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.

## Warnings
- OpenRouter API error: 404
- Mubasher stock page returned no evidence titles for KABO.CA.
- No Yahoo or Mubasher evidence found for KABO.CA.
- Evidence rejected for KABO.CA: source text did not clearly match KABO.CA / El Nasr Clothing and Textiles.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Mubasher stock page returned no evidence titles for ZEOT.CA.
- No Yahoo or Mubasher evidence found for ZEOT.CA.
- Evidence rejected for ZEOT.CA: source text did not clearly match ZEOT.CA / Extracted Oil & Derivatives Co..
- Mubasher stock page returned no evidence titles for MOSC.CA.
- No Yahoo or Mubasher evidence found for MOSC.CA.
- Evidence rejected for MOSC.CA: source text did not clearly match MOSC.CA / Misr Oils & Soap.
- Mubasher stock page returned no evidence titles for ACGC.CA.
- No Yahoo or Mubasher evidence found for ACGC.CA.
- Evidence rejected for ACGC.CA: source text did not clearly match ACGC.CA / Arab Cotton Ginning.
- Mubasher stock page returned no evidence titles for SPIN.CA.
- No Yahoo or Mubasher evidence found for SPIN.CA.
- Evidence rejected for SPIN.CA: source text did not clearly match SPIN.CA / Alexandria Spinning and Weaving.
- Mubasher stock page returned no evidence titles for MICH.CA.
- No Yahoo or Mubasher evidence found for MICH.CA.
- Evidence rejected for MICH.CA: source text did not clearly match MICH.CA / Misr Chemical Industries Co..
- Mubasher stock page returned no evidence titles for EFIH.CA.
- No Yahoo or Mubasher evidence found for EFIH.CA.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Mubasher stock page returned no evidence titles for ETEL.CA.
- No Yahoo or Mubasher evidence found for ETEL.CA.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
