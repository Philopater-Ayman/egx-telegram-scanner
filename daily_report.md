# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-09-20T11:19:53.144114+00:00
Generated Cairo: 2026-09-20 14:19
Run timing: target 09:15 Cairo | generated Cairo 2026-09-20 14:19 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-09-20 14:16

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 165/187
- Top sector: Investment Holding

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, September 20
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 50.0% / above MA50 61.11%
- EGX70 regime: BEARISH / above MA20 39.47% / above MA50 55.26%
- Sector breadth: 14.29%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=810808640.0 spike=0.97 score=23.4
- MPCO.CA: liquidity=396287232.0 spike=2.57 score=8.22
- ABUK.CA: liquidity=279908800.0 spike=1.78 score=7.11
- MFPC.CA: liquidity=227876944.0 spike=1.6 score=20.75
- TMGH.CA: liquidity=187372896.0 spike=0.67 score=14.46

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with low sector breadth (14.29%), triggering a DEFENSIVE_NO_NEW_BUY risk mode; the scanner prioritized tickets showing accumulation spikes and bullish‑watch outlooks despite the overall bearish regime.
- Tickets were selected for highest rank_score, liquidity accumulation spikes, and bullish‑watch outlooks, indicating short‑term buying interest even though buy_ready is false under defensive rules.
- Liquidity spikes suggest possible near‑term inflows; support/resistance distances show many stocks close to resistance, while sector breadth is weak, limiting sustained upside in the next 1‑3 days.
- The bearish EGX30/EGX70 regime switches risk mode to defensive, blocking new buys; uncertainty remains due to mixed signals from strong sectors (Investment Holding, Telecom, Energy) and potential regime shifts.

## Top Liquidity Spikes
- CANA.CA: spike=6.7 liquidity=96109200.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RUBX.CA: spike=5.53 liquidity=107962360.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- IDRE.CA: spike=5.02 liquidity=51414428.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ENGC.CA: spike=4.6 liquidity=55929656.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MOIL.CA: spike=3.73 liquidity=779926.75 outlook=CONSTRUCTIVE score=68.33 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=17.83 5d=12.95% 20d=25.96% aboveMA50=100.0%
- #2 Telecommunications: score=9.78 5d=1.89% 20d=8.38% aboveMA50=100.0%
- #3 Energy & Petrochemicals: score=6.33 5d=-4.2% 20d=3.69% aboveMA50=100.0%
- #4 Education: score=6.27 5d=1.67% 20d=3.61% aboveMA50=66.67%
- #5 Automotive & Distribution: score=5.25 5d=-0.07% 20d=0.23% aboveMA50=50.0%
- #6 Textiles: score=3.95 5d=-4.62% 20d=4.21% aboveMA50=100.0%
- #7 Banking & Financials: score=3.9 5d=-1.77% 20d=-0.53% aboveMA50=70.0%
- #8 Basic Resources & Chemicals: score=3.87 5d=-1.64% 20d=-0.13% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- EGAS.CA: BULLISH_WATCH score=97.33 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- EGCH.CA: BULLISH_WATCH score=85.87 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- BINV.CA: BULLISH_WATCH score=83 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support
- WKOL.CA: BULLISH_WATCH score=81.0 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- KABO.CA: BULLISH_WATCH score=79.95 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ORWE.CA: BULLISH_WATCH score=78.95 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- EXPA.CA: BULLISH_WATCH score=78.9 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- SAUD.CA: BULLISH_WATCH score=78.9 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- GBCO.CA: BULLISH_WATCH score=78.25 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- OIH.CA: BULLISH_WATCH score=78 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended; close to resistance

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=17.8 buy_ready=False sector_rank=11 price=309.57 support=295.0 resistance=345.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=61.15 liquidity=20386876.0 spike=0.96
- ABUK.CA: score=7.11 buy_ready=False sector_rank=8 price=93.99 support=93.0 resistance=96.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=279908800.0 spike=1.78
- ACAMD.CA: score=16.8 buy_ready=False sector_rank=11 price=2.07 support=1.95 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=47160516.0 spike=0.79
- ACGC.CA: score=15.95 buy_ready=False sector_rank=6 price=14.26 support=12.56 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=47.61 liquidity=7370950.0 spike=0.19
- ADCI.CA: score=10.33 buy_ready=False sector_rank=11 price=286.11 support=267.66 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=38.15 liquidity=2529647.0 spike=0.43
- ADIB.CA: score=18.8 buy_ready=False sector_rank=7 price=52.61 support=50.51 resistance=55.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=38.56 liquidity=80176728.0 spike=1.12
- ADPC.CA: score=17.56 buy_ready=False sector_rank=11 price=3.95 support=3.81 resistance=4.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=45.28 liquidity=28164488.0 spike=1.38
- AFDI.CA: score=13.13 buy_ready=False sector_rank=11 price=55.12 support=51.6 resistance=68.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=49.6 liquidity=8325403.0 spike=0.34
- AFMC.CA: score=9.8 buy_ready=False sector_rank=11 price=162.07 support=153.0 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=28.35 liquidity=30546940.0 spike=0.46
- AJWA.CA: score=13.47 buy_ready=False sector_rank=11 price=181.0 support=175.15 resistance=199.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=44.93 liquidity=8674436.0 spike=0.18
- ALCN.CA: score=4.92 buy_ready=False sector_rank=21 price=32.7 support=32.7 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=43735752.0 spike=1.5
- ALUM.CA: score=6.96 buy_ready=False sector_rank=11 price=26.74 support=25.0 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=22.55 liquidity=4156497.25 spike=0.29
- AMER.CA: score=12.46 buy_ready=False sector_rank=16 price=5.44 support=4.8 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=34.13 liquidity=17126276.0 spike=0.27
- AMES.CA: score=4.8 buy_ready=False sector_rank=11 price=49.92 support=49.65 resistance=53.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=84129056.0 spike=0.31
- AMIA.CA: score=17.8 buy_ready=False sector_rank=11 price=18.17 support=15.3 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=36.22 liquidity=16561008.0 spike=0.28
- AMOC.CA: score=20.4 buy_ready=False sector_rank=3 price=14.08 support=10.65 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=74.24 liquidity=135649888.0 spike=0.77
- APSW.CA: score=4.15 buy_ready=False sector_rank=11 price=8.52 support=8.37 resistance=8.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=44.94 liquidity=354170.16 spike=0.34
- ARAB.CA: score=14.46 buy_ready=False sector_rank=16 price=0.25 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=41795252.0 spike=0.38
- ARCC.CA: score=17.24 buy_ready=False sector_rank=18 price=73.12 support=71.5 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=43.26 liquidity=12605009.0 spike=0.3
- AREH.CA: score=13.23 buy_ready=False sector_rank=11 price=1.43 support=1.39 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=8431300.0 spike=0.56
- ASCM.CA: score=8.59 buy_ready=False sector_rank=11 price=61.5 support=60.15 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=36.59 liquidity=3785171.25 spike=0.17
- ASPI.CA: score=18.1 buy_ready=False sector_rank=11 price=0.46 support=0.41 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=38.27 liquidity=64563492.0 spike=1.15
- ATLC.CA: score=17.6 buy_ready=False sector_rank=14 price=7.18 support=5.2 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=66.16 liquidity=10054004.0 spike=0.37
- ATQA.CA: score=6.13 buy_ready=False sector_rank=8 price=13.21 support=12.71 resistance=13.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=134589296.0 spike=1.29
- AXPH.CA: score=15.51 buy_ready=False sector_rank=11 price=1673.69 support=1362.0 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=55.4 liquidity=3705218.5 spike=0.3
- BINV.CA: score=25.34 buy_ready=False sector_rank=1 price=62.57 support=47.07 resistance=62.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=83.0 liquidity=33934744.0 spike=1.97
- BIOC.CA: score=9.8 buy_ready=False sector_rank=11 price=275.03 support=272.01 resistance=506.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=14.21 liquidity=18275700.0 spike=0.16
- BTFH.CA: score=17.46 buy_ready=False sector_rank=14 price=3.03 support=2.87 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=37.93 liquidity=181224448.0 spike=1.93
- CAED.CA: score=12.8 buy_ready=False sector_rank=11 price=129.13 support=123.56 resistance=181.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=29.76 liquidity=10255071.0 spike=0.29
- CANA.CA: score=10.56 buy_ready=False sector_rank=7 price=48.71 support=44.0 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=96109200.0 spike=6.7
- CCAP.CA: score=23.4 buy_ready=False sector_rank=1 price=7.16 support=5.42 resistance=6.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=79.08 liquidity=810808640.0 spike=0.97
- CCRS.CA: score=19.8 buy_ready=False sector_rank=11 price=2.65 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=40.91 liquidity=17730538.0 spike=0.34
- CEFM.CA: score=16.94 buy_ready=False sector_rank=11 price=147.02 support=143.0 resistance=167.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=53.61 liquidity=7142520.5 spike=0.46
- CERA.CA: score=17.8 buy_ready=False sector_rank=11 price=1.43 support=1.22 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=57.63 liquidity=52660124.0 spike=0.48
- CFGH.CA: score=7.81 buy_ready=False sector_rank=11 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=63.16 liquidity=9177.38 spike=0.47
- CICH.CA: score=-1.56 buy_ready=False sector_rank=14 price=13.14 support=12.86 resistance=13.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3841820.25 spike=0.65
- CIEB.CA: score=18.32 buy_ready=False sector_rank=7 price=25.53 support=24.01 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=46.05 liquidity=7760581.0 spike=0.57
- CIRA.CA: score=21.4 buy_ready=False sector_rank=4 price=40.69 support=32.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=33247684.0 spike=0.92
- CLHO.CA: score=9.39 buy_ready=False sector_rank=20 price=15.99 support=15.81 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=33.81 liquidity=88000648.0 spike=1.14
- CNFN.CA: score=15.44 buy_ready=False sector_rank=14 price=4.71 support=4.46 resistance=4.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=39.47 liquidity=17322750.0 spike=1.42
- COMI.CA: score=10.56 buy_ready=False sector_rank=7 price=133.4 support=131.11 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=31.43 liquidity=138648512.0 spike=0.25
- COPR.CA: score=17.8 buy_ready=False sector_rank=11 price=0.51 support=0.46 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=38.82 liquidity=41468804.0 spike=0.57
- COSG.CA: score=19.8 buy_ready=False sector_rank=11 price=1.88 support=1.74 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=48.72 liquidity=23907330.0 spike=0.59
- CPCI.CA: score=3.17 buy_ready=False sector_rank=11 price=558.99 support=546.54 resistance=584.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6966955.0 spike=1.7
- CSAG.CA: score=13.96 buy_ready=False sector_rank=21 price=38.3 support=36.5 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=38.57 liquidity=7032122.0 spike=0.42
- DAPH.CA: score=17.8 buy_ready=False sector_rank=11 price=120.6 support=108.11 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=52.89 liquidity=16521311.0 spike=0.27
- DEIN.CA: score=7.8 buy_ready=False sector_rank=11 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=2.88 buy_ready=False sector_rank=15 price=26.63 support=26.51 resistance=29.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=28.18 liquidity=3379748.25 spike=0.61
- DSCW.CA: score=13.8 buy_ready=False sector_rank=11 price=1.83 support=1.8 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=37.93 liquidity=28189032.0 spike=0.74
- DTPP.CA: score=19.96 buy_ready=False sector_rank=11 price=345.0 support=292.5 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=68.84 liquidity=70572472.0 spike=1.08
- EALR.CA: score=9.49 buy_ready=False sector_rank=11 price=381.2 support=340.0 resistance=415.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=4689129.0 spike=0.33
- EASB.CA: score=18.02 buy_ready=False sector_rank=11 price=8.18 support=7.16 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=56.2 liquidity=6215809.5 spike=0.37
- EAST.CA: score=8.5 buy_ready=False sector_rank=15 price=32.03 support=32.0 resistance=36.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=28.11 liquidity=35426900.0 spike=0.5
- EBSC.CA: score=16.21 buy_ready=False sector_rank=11 price=2.09 support=1.88 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=47.96 liquidity=6409913.0 spike=0.44
- ECAP.CA: score=7.37 buy_ready=False sector_rank=11 price=32.34 support=31.16 resistance=37.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=43.33 liquidity=2567320.5 spike=0.22
- EDFM.CA: score=10.27 buy_ready=False sector_rank=11 price=412.6 support=399.0 resistance=465.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=58.7 liquidity=471350.91 spike=0.25
- EEII.CA: score=4.8 buy_ready=False sector_rank=11 price=2.33 support=2.23 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17089518.0 spike=0.8
- EFIC.CA: score=14.55 buy_ready=False sector_rank=8 price=193.6 support=192.75 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=43788356.0 spike=0.13
- EFID.CA: score=19.5 buy_ready=False sector_rank=15 price=31.74 support=29.71 resistance=33.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=39.83 liquidity=31054652.0 spike=0.5
- EFIH.CA: score=17.39 buy_ready=False sector_rank=17 price=23.47 support=22.16 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=41.65 liquidity=55830592.0 spike=0.89
- EGAL.CA: score=20.55 buy_ready=False sector_rank=8 price=373.87 support=321.01 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=49.36 liquidity=26852438.0 spike=0.26
- EGAS.CA: score=19.68 buy_ready=False sector_rank=3 price=58.51 support=55.0 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=43.63 liquidity=7276144.5 spike=0.85
- EGBE.CA: score=3.63 buy_ready=False sector_rank=7 price=0.51 support=0.49 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=29.63 liquidity=70205.78 spike=0.59
- EGCH.CA: score=21.67 buy_ready=False sector_rank=8 price=14.35 support=13.3 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=58.58 liquidity=179529696.0 spike=1.56
- EGSA.CA: score=11.39 buy_ready=False sector_rank=2 price=9.0 support=8.67 resistance=9.1 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=78.18 liquidity=10413.0 spike=1.49
- EGTS.CA: score=14.86 buy_ready=False sector_rank=16 price=16.89 support=16.17 resistance=17.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=47.02 liquidity=29516936.0 spike=1.2
- EHDR.CA: score=13.01 buy_ready=False sector_rank=11 price=2.8 support=2.73 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=8211704.0 spike=0.41
- ELEC.CA: score=8.78 buy_ready=False sector_rank=12 price=2.02 support=1.93 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=30.56 liquidity=74772744.0 spike=1.09
- ELKA.CA: score=14.8 buy_ready=False sector_rank=11 price=1.74 support=1.7 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=47.17 liquidity=12024669.0 spike=0.28
- ELNA.CA: score=-1.18 buy_ready=False sector_rank=11 price=35.74 support=33.96 resistance=38.99 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=28.76 liquidity=23302.48 spike=0.06
- ELSH.CA: score=14.8 buy_ready=False sector_rank=11 price=13.29 support=12.67 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=41.01 liquidity=31845652.0 spike=0.82
- ELWA.CA: score=5.18 buy_ready=False sector_rank=11 price=1.7 support=1.62 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=380004.84 spike=0.15
- EMFD.CA: score=17.46 buy_ready=False sector_rank=16 price=13.83 support=11.55 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=73.27 liquidity=73449952.0 spike=0.43
- ENGC.CA: score=9.8 buy_ready=False sector_rank=11 price=44.45 support=42.41 resistance=45.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=55929656.0 spike=4.6
- EOSB.CA: score=10.02 buy_ready=False sector_rank=11 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=77512.47 spike=1.07
- EPCO.CA: score=19.8 buy_ready=False sector_rank=11 price=11.28 support=10.8 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=47.6 liquidity=11213162.0 spike=0.6
- EPPK.CA: score=-4.78 buy_ready=False sector_rank=11 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=20.4 buy_ready=False sector_rank=2 price=132.53 support=112.5 resistance=135.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=83.97 liquidity=64999876.0 spike=0.31
- ETRS.CA: score=19.8 buy_ready=False sector_rank=11 price=11.18 support=10.66 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=49.74 liquidity=10411363.0 spike=0.68
- EXPA.CA: score=20.94 buy_ready=False sector_rank=7 price=21.42 support=19.8 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=60.73 liquidity=45184448.0 spike=1.19
- FAIT.CA: score=10.7 buy_ready=False sector_rank=7 price=47.58 support=39.58 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=66.22 liquidity=2137166.25 spike=0.25
- FAITA.CA: score=5.65 buy_ready=False sector_rank=7 price=0.99 support=0.98 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=9.76 liquidity=149800.84 spike=3.47
- FERC.CA: score=20.55 buy_ready=False sector_rank=8 price=80.36 support=76.9 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=48.29 liquidity=11986875.0 spike=0.68
- FWRY.CA: score=14.39 buy_ready=False sector_rank=17 price=18.94 support=18.66 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=50.8 liquidity=32593308.0 spike=0.23
- GBCO.CA: score=26.44 buy_ready=False sector_rank=5 price=31.0 support=27.51 resistance=31.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=62.31 liquidity=153185344.0 spike=2.67
- GDWA.CA: score=13.8 buy_ready=False sector_rank=11 price=0.78 support=0.76 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=43.92 liquidity=22519254.0 spike=0.51
- GGCC.CA: score=13.63 buy_ready=False sector_rank=11 price=0.86 support=0.83 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=35.36 liquidity=8831056.0 spike=0.24
- GIHD.CA: score=17.8 buy_ready=False sector_rank=11 price=72.74 support=58.01 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=65.35 liquidity=12755420.0 spike=0.44
- GMCI.CA: score=1.36 buy_ready=False sector_rank=11 price=1.75 support=1.69 resistance=1.94 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=23.33 liquidity=841701.0 spike=1.86
- GRCA.CA: score=8.8 buy_ready=False sector_rank=11 price=41.81 support=39.0 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=27.52 liquidity=14361946.0 spike=0.17
- GSSC.CA: score=5.96 buy_ready=False sector_rank=11 price=312.59 support=310.6 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14514424.0 spike=1.58
- GTWL.CA: score=19.8 buy_ready=False sector_rank=11 price=235.0 support=181.52 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=62.29 liquidity=76553672.0 spike=0.3
- HDBK.CA: score=18.56 buy_ready=False sector_rank=7 price=120.12 support=89.01 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=66.08 liquidity=29950554.0 spike=0.52
- HELI.CA: score=21.46 buy_ready=False sector_rank=16 price=8.32 support=7.34 resistance=8.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=68.15 liquidity=142223520.0 spike=0.91
- HRHO.CA: score=13.6 buy_ready=False sector_rank=14 price=25.34 support=25.04 resistance=26.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=40.38 liquidity=73514144.0 spike=0.73
- ICID.CA: score=14.54 buy_ready=False sector_rank=11 price=17.99 support=15.25 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=60.06 liquidity=4739130.5 spike=0.29
- IDRE.CA: score=9.8 buy_ready=False sector_rank=11 price=59.0 support=55.7 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51414428.0 spike=5.02
- IFAP.CA: score=18.0 buy_ready=False sector_rank=9 price=20.49 support=20.05 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=40.41 liquidity=9911621.0 spike=0.36
- INFI.CA: score=9.34 buy_ready=False sector_rank=11 price=134.14 support=130.15 resistance=174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=16.41 liquidity=6535005.0 spike=0.21
- IRON.CA: score=9.55 buy_ready=False sector_rank=8 price=28.27 support=26.3 resistance=32.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=2.57 liquidity=11607650.0 spike=0.81
- ISMA.CA: score=9.09 buy_ready=False sector_rank=11 price=30.7 support=28.05 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=18.03 liquidity=9288314.0 spike=0.36
- ISMQ.CA: score=16.07 buy_ready=False sector_rank=8 price=9.14 support=8.68 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=37.6 liquidity=34099176.0 spike=1.26
- ISPH.CA: score=9.11 buy_ready=False sector_rank=20 price=12.2 support=11.9 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=34.75 liquidity=58808700.0 spike=0.85
- JUFO.CA: score=16.57 buy_ready=False sector_rank=15 price=27.15 support=26.45 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=47.98 liquidity=9069351.0 spike=0.43
- KABO.CA: score=20.58 buy_ready=False sector_rank=6 price=9.41 support=8.82 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=53.97 liquidity=20720006.0 spike=0.42
- KWIN.CA: score=9.8 buy_ready=False sector_rank=11 price=90.0 support=84.5 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=32.99 liquidity=15241496.0 spike=0.23
- KZPC.CA: score=17.8 buy_ready=False sector_rank=11 price=14.4 support=12.6 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=72.6 liquidity=13130919.0 spike=0.21
- LCSW.CA: score=13.98 buy_ready=False sector_rank=18 price=33.21 support=32.42 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=45.62 liquidity=9739947.0 spike=0.37
- LUTS.CA: score=4.8 buy_ready=False sector_rank=11 price=0.94 support=0.94 resistance=0.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29586428.0 spike=0.12
- MAAL.CA: score=12.57 buy_ready=False sector_rank=11 price=8.75 support=8.18 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=35.22 liquidity=7767004.0 spike=0.75
- MASR.CA: score=14.8 buy_ready=False sector_rank=11 price=7.77 support=7.49 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=56.91 liquidity=65799256.0 spike=0.7
- MBSC.CA: score=17.24 buy_ready=False sector_rank=18 price=363.88 support=363.0 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=46.6 liquidity=19416486.0 spike=0.37
- MCQE.CA: score=17.24 buy_ready=False sector_rank=18 price=219.23 support=213.0 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=41.55 liquidity=13995379.0 spike=0.4
- MCRO.CA: score=16.8 buy_ready=False sector_rank=11 price=1.69 support=1.44 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=79.49 liquidity=43113928.0 spike=0.34
- MENA.CA: score=4.97 buy_ready=False sector_rank=16 price=6.7 support=6.58 resistance=7.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=508653.44 spike=0.22
- MEPA.CA: score=19.8 buy_ready=False sector_rank=11 price=1.97 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=58.97 liquidity=27949486.0 spike=0.73
- MFPC.CA: score=20.75 buy_ready=False sector_rank=8 price=49.98 support=39.02 resistance=48.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=81.52 liquidity=227876944.0 spike=1.6
- MFSC.CA: score=16.95 buy_ready=False sector_rank=11 price=51.04 support=48.5 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=6525471.0 spike=1.31
- MHOT.CA: score=10.75 buy_ready=False sector_rank=10 price=17.86 support=17.62 resistance=19.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=35.64 liquidity=3748735.25 spike=0.37
- MICH.CA: score=16.56 buy_ready=False sector_rank=11 price=49.38 support=47.2 resistance=53.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=48.52 liquidity=8761425.0 spike=0.42
- MILS.CA: score=10.58 buy_ready=False sector_rank=11 price=200.97 support=198.0 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=32.69 liquidity=7782237.5 spike=0.17
- MIPH.CA: score=17.93 buy_ready=False sector_rank=20 price=834.0 support=700.2 resistance=820.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=60.59 liquidity=7143311.0 spike=1.84
- MOED.CA: score=16.8 buy_ready=False sector_rank=11 price=0.79 support=0.74 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=51.14 liquidity=13386913.0 spike=0.11
- MOIL.CA: score=18.18 buy_ready=False sector_rank=3 price=0.7 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=58.11 liquidity=779926.75 spike=3.73
- MOIN.CA: score=19.8 buy_ready=False sector_rank=11 price=37.13 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=53.32 liquidity=10471730.0 spike=0.34
- MOSC.CA: score=13.74 buy_ready=False sector_rank=11 price=312.7 support=302.0 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=30.09 liquidity=11052870.0 spike=1.47
- MPCI.CA: score=17.8 buy_ready=False sector_rank=11 price=402.87 support=345.0 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=53.38 liquidity=112131920.0 spike=0.71
- MPCO.CA: score=8.22 buy_ready=False sector_rank=9 price=2.92 support=2.72 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=396287232.0 spike=2.57
- MPRC.CA: score=14.8 buy_ready=False sector_rank=11 price=39.7 support=38.31 resistance=46.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=35.32 liquidity=17772618.0 spike=0.43
- MTIE.CA: score=16.1 buy_ready=False sector_rank=5 price=8.51 support=8.1 resistance=8.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=45.86 liquidity=11684404.0 spike=0.31
- NAHO.CA: score=-5.18 buy_ready=False sector_rank=11 price=0.13 support=0.13 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17797.65 spike=0.27
- NCCW.CA: score=4.8 buy_ready=False sector_rank=11 price=7.79 support=7.77 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=56025472.0 spike=0.92
- NEDA.CA: score=10.33 buy_ready=False sector_rank=11 price=2.79 support=2.7 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=40.62 liquidity=530146.63 spike=0.74
- NHPS.CA: score=8.89 buy_ready=False sector_rank=11 price=77.08 support=75.31 resistance=98.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=6.12 liquidity=9087503.0 spike=0.45
- NINH.CA: score=10.9 buy_ready=False sector_rank=11 price=21.48 support=20.5 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=25.28 liquidity=46952960.0 spike=1.55
- NIPH.CA: score=12.11 buy_ready=False sector_rank=20 price=313.44 support=301.0 resistance=414.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=17.33 liquidity=39784728.0 spike=0.21
- OBRI.CA: score=11.4 buy_ready=False sector_rank=11 price=31.41 support=30.1 resistance=34.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=37.87 liquidity=7600570.5 spike=0.45
- OCDI.CA: score=14.46 buy_ready=False sector_rank=16 price=30.4 support=29.25 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=41.46 liquidity=57223700.0 spike=0.7
- OCPH.CA: score=4.38 buy_ready=False sector_rank=11 price=240.59 support=210.0 resistance=277.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=33.91 liquidity=3583282.25 spike=0.43
- ODIN.CA: score=9.96 buy_ready=False sector_rank=11 price=2.87 support=2.55 resistance=3.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=13.51 liquidity=26780272.0 spike=1.08
- OFH.CA: score=19.8 buy_ready=False sector_rank=11 price=1.09 support=0.88 resistance=1.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=115308816.0 spike=0.93
- OIH.CA: score=24.4 buy_ready=False sector_rank=1 price=2.16 support=1.83 resistance=2.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=66.0 liquidity=74848952.0 spike=0.6
- OLFI.CA: score=14.5 buy_ready=False sector_rank=15 price=22.56 support=22.07 resistance=24.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=41.47 liquidity=10247536.0 spike=0.63
- ORAS.CA: score=4.6 buy_ready=False sector_rank=13 price=864.93 support=850.4 resistance=875.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=114376536.0 spike=1.0
- ORHD.CA: score=19.46 buy_ready=False sector_rank=16 price=42.65 support=40.28 resistance=43.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=49.0 liquidity=129972208.0 spike=0.98
- ORWE.CA: score=20.58 buy_ready=False sector_rank=6 price=28.0 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=57.35 liquidity=46217680.0 spike=0.88
- PHAR.CA: score=9.11 buy_ready=False sector_rank=20 price=117.42 support=117.01 resistance=141.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=19.74 liquidity=51954696.0 spike=0.36
- PHDC.CA: score=9.46 buy_ready=False sector_rank=16 price=13.31 support=13.65 resistance=15.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=31.85 liquidity=168862352.0 spike=0.98
- PHTV.CA: score=11.68 buy_ready=False sector_rank=11 price=364.12 support=311.27 resistance=382.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=64.27 liquidity=1881243.13 spike=0.97
- POUL.CA: score=19.5 buy_ready=False sector_rank=15 price=38.95 support=37.03 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=47.07 liquidity=12676115.0 spike=0.53
- PRCL.CA: score=15.42 buy_ready=False sector_rank=18 price=32.0 support=30.9 resistance=35.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=45.64 liquidity=30016778.0 spike=1.59
- PRDC.CA: score=9.46 buy_ready=False sector_rank=16 price=7.8 support=7.68 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=23.25 liquidity=11096107.0 spike=0.16
- PRMH.CA: score=1.44 buy_ready=False sector_rank=11 price=2.72 support=2.66 resistance=2.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6635432.0 spike=0.62
- RACC.CA: score=11.43 buy_ready=False sector_rank=11 price=9.84 support=9.4 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=47.29 liquidity=4630372.0 spike=0.24
- RAKT.CA: score=10.86 buy_ready=False sector_rank=11 price=22.65 support=21.4 resistance=23.02 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=57.94 liquidity=55651.05 spike=0.24
- RAYA.CA: score=14.23 buy_ready=False sector_rank=19 price=7.17 support=6.95 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=29391796.0 spike=0.53
- RMDA.CA: score=17.11 buy_ready=False sector_rank=20 price=6.1 support=5.77 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=16715536.0 spike=0.27
- ROTO.CA: score=3.42 buy_ready=False sector_rank=11 price=41.14 support=35.02 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=21.14 liquidity=3617006.0 spike=0.36
- RREI.CA: score=19.8 buy_ready=False sector_rank=11 price=4.4 support=4.24 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=55.07 liquidity=19730386.0 spike=0.78
- RTVC.CA: score=1.48 buy_ready=False sector_rank=11 price=3.95 support=3.85 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=28.33 liquidity=1678589.25 spike=0.26
- RUBX.CA: score=9.8 buy_ready=False sector_rank=11 price=16.27 support=12.9 resistance=16.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=107962360.0 spike=5.53
- SAUD.CA: score=20.56 buy_ready=False sector_rank=7 price=24.1 support=22.7 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=50.96 liquidity=11543735.0 spike=0.9
- SCEM.CA: score=17.24 buy_ready=False sector_rank=18 price=94.67 support=94.0 resistance=105.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=44.55 liquidity=97046152.0 spike=0.77
- SCFM.CA: score=2.49 buy_ready=False sector_rank=11 price=274.26 support=265.51 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=30.39 liquidity=2687851.5 spike=0.28
- SCTS.CA: score=2.22 buy_ready=False sector_rank=4 price=607.54 support=566.66 resistance=640.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=32.18 liquidity=821448.56 spike=0.25
- SDTI.CA: score=17.8 buy_ready=False sector_rank=11 price=78.0 support=67.0 resistance=76.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=65.18 liquidity=12002214.0 spike=0.58
- SEIG.CA: score=5.61 buy_ready=False sector_rank=11 price=241.17 support=228.13 resistance=274.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=43.16 liquidity=810058.56 spike=0.46
- SIPC.CA: score=19.8 buy_ready=False sector_rank=11 price=5.77 support=4.1 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=65.96 liquidity=17007664.0 spike=0.24
- SKPC.CA: score=20.55 buy_ready=False sector_rank=8 price=18.64 support=17.0 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=63.27 liquidity=92120088.0 spike=0.64
- SMFR.CA: score=1.77 buy_ready=False sector_rank=11 price=241.62 support=236.0 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=27.28 liquidity=1973944.88 spike=0.2
- SNFC.CA: score=20.6 buy_ready=False sector_rank=11 price=11.34 support=10.26 resistance=11.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=65.24 liquidity=20178954.0 spike=1.4
- SPIN.CA: score=4.66 buy_ready=False sector_rank=6 price=17.62 support=17.01 resistance=20.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=28.6 liquidity=1079277.25 spike=0.06
- SPMD.CA: score=4.8 buy_ready=False sector_rank=11 price=0.44 support=0.44 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=41898984.0 spike=0.64
- SUGR.CA: score=17.25 buy_ready=False sector_rank=15 price=58.93 support=50.0 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=58.65 liquidity=9743297.0 spike=0.15
- SVCE.CA: score=19.8 buy_ready=False sector_rank=11 price=12.0 support=10.28 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=56.57 liquidity=78122848.0 spike=0.42
- SWDY.CA: score=19.6 buy_ready=False sector_rank=12 price=127.67 support=115.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=43.09 liquidity=20288458.0 spike=0.26
- TALM.CA: score=18.4 buy_ready=False sector_rank=4 price=21.63 support=17.11 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=80.86 liquidity=35090552.0 spike=0.59
- TMGH.CA: score=14.46 buy_ready=False sector_rank=16 price=94.06 support=94.86 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=40.75 liquidity=187372896.0 spike=0.67
- TRTO.CA: score=-5.18 buy_ready=False sector_rank=11 price=0.06 support=0.06 resistance=0.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19052.08 spike=0.7
- UEFM.CA: score=-3.84 buy_ready=False sector_rank=11 price=507.56 support=500.0 resistance=528.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1359203.38 spike=0.44
- UEGC.CA: score=9.8 buy_ready=False sector_rank=11 price=1.8 support=1.66 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=32.88 liquidity=24508520.0 spike=0.5
- UNIP.CA: score=14.26 buy_ready=False sector_rank=11 price=0.38 support=0.35 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=52.13 liquidity=9457826.0 spike=0.29
- UNIT.CA: score=10.27 buy_ready=False sector_rank=16 price=18.81 support=18.11 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=56.35 liquidity=3809743.75 spike=0.26
- WCDF.CA: score=11.21 buy_ready=False sector_rank=11 price=742.92 support=630.06 resistance=796.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=81.23 liquidity=2409185.25 spike=0.53
- WKOL.CA: score=18.92 buy_ready=False sector_rank=11 price=345.48 support=332.56 resistance=369.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=55.88 liquidity=7120619.0 spike=0.63
- ZEOT.CA: score=21.76 buy_ready=False sector_rank=11 price=13.54 support=13.03 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=35.16 liquidity=19566106.0 spike=2.98
- ZMID.CA: score=17.46 buy_ready=False sector_rank=16 price=8.78 support=7.81 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=62.03 liquidity=135817424.0 spike=0.54

## Backtesting Lite
- GBCO.CA: 180d return=19.04%, max drawdown=-24.35%, MA20>MA50 days last20=1, as_of=2026-09-15T21:00:00+00:00
- BINV.CA: 180d return=70.75%, max drawdown=-17.77%, MA20>MA50 days last20=20, as_of=2026-09-15T21:00:00+00:00
- OIH.CA: 180d return=86.21%, max drawdown=-14.56%, MA20>MA50 days last20=20, as_of=2026-09-15T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- OIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Investment Holding summary=Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- ZEOT.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Extracted Oil & Derivatives Co. summary=Extracted Oils stock nears record high on strong momentum; Extracted Oils stock witnesses increasing buying power amid current resistance – Analysis; Extracted Oils swings to nearly EGP 14.5m net profits in Q1-25/26
  - Extracted Oils stock nears record high on strong momentum: https://english.mubasher.info/news/4599376/Extracted-Oils-stock-nears-record-high-on-strong-momentum/
  - Extracted Oils stock witnesses increasing buying power amid current resistance – Analysis: https://english.mubasher.info/news/4555925/Extracted-Oils-stock-witnesses-increasing-buying-power-amid-current-resistance-Analysis/
  - Extracted Oils swings to nearly EGP 14.5m net profits in Q1-25/26: https://english.mubasher.info/news/4537956/Extracted-Oils-swings-to-nearly-EGP-14-5m-net-profits-in-Q1-25-26/
- EGCH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Chemical Industries Kima summary=Evidence rejected for EGCH.CA: source text did not clearly match EGCH.CA / Egyptian Chemical Industries Kima.
- HELI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Heliopolis Housing summary=Evidence rejected for HELI.CA: source text did not clearly match HELI.CA / Heliopolis Housing.
- CIRA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Investment and Real Estate Development summary=CIRA Education take over 51% of L’École Française Hurghada; CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion; CIRA Education launches Middle East’s 1st initiative for care economy
  - CIRA Education take over 51% of L’École Française Hurghada: https://english.mubasher.info/news/4488666/CIRA-Education-take-over-51-of-L-%C3%89cole-Fran%C3%A7aise-Hurghada/
  - CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion: https://english.mubasher.info/news/4393636/CIRA-s-majority-shareholder-acquires-37-5-additional-equity-backs-regional-expansion/
  - CIRA Education launches Middle East’s 1st initiative for care economy: https://english.mubasher.info/news/4391766/CIRA-Education-launches-Middle-East-s-1st-initiative-for-care-economy/

## Warnings
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for ZEOT.CA matches the company but no source/report date was detected.
- Evidence rejected for EGCH.CA: source text did not clearly match EGCH.CA / Egyptian Chemical Industries Kima.
- Evidence rejected for HELI.CA: source text did not clearly match HELI.CA / Heliopolis Housing.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
