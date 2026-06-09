# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-06-09T08:52:48.698053+00:00
Generated Cairo: 2026-06-09 11:52
Run timing: target 08:45 Cairo | generated Cairo 2026-06-09 11:52 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-06-09 11:49

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 184/190
- Top sector: Investment Holding

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, June 09
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 20.0% / above MA50 75.0%
- EGX70 regime: MIXED / above MA20 60.0% / above MA50 85.0%
- Sector breadth: 19.05%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- ZMID.CA: liquidity=340545280.0 spike=1.63 score=25.58
- COMI.CA: liquidity=317355168.0 spike=0.47 score=18.65
- CCAP.CA: liquidity=300326592.0 spike=0.35 score=26.4
- ELSH.CA: liquidity=244557136.0 spike=2.09 score=22.36
- PHDC.CA: liquidity=156130032.0 spike=0.37 score=20.32

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The local scanner kept all tickets on HOLD because the EGX30 is in a bearish regime and sector breadth is weak (19%). EGX70 is mixed but still showing negative 5‑day returns. Risk mode is set to DEFENSIVE_NO_NEW_BUY, so no new entries are allowed despite several stocks showing bullish watch outlooks and decent liquidity.
- Liquidity is decent (e.g., CCAP, ZMID) but cooling or near resistance, limiting short‑term upside.
- Support levels are 8‑20% below current price; resistance is close (1‑5% above), so price may stall in the next 1‑3 days.
- Leading sectors (Investment Holding, Technology & Distribution, Real Estate) have modest returns and mixed MA‑20/MA‑50 coverage, reinforcing the defensive stance.
- EGX30 bearish trend and low breadth increase market risk; EGX70 mixed trend adds uncertainty to sector‑specific moves.

## Top Liquidity Spikes
- NCCW.CA: spike=3.39 liquidity=69800784.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ELSH.CA: spike=2.09 liquidity=244557136.0 outlook=CONSTRUCTIVE score=62.44 buy_ready=False
- ANFI.CA: spike=1.93 liquidity=39216123.4 outlook=BULLISH_WATCH score=94.44 buy_ready=False
- ENGC.CA: spike=1.84 liquidity=21878426.0 outlook=BULLISH_WATCH score=84.44 buy_ready=False
- ZMID.CA: spike=1.63 liquidity=340545280.0 outlook=BULLISH_WATCH score=90.79 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=7.61 5d=2.57% 20d=12.11% aboveMA50=66.67%
- #2 Technology & Distribution: score=6.58 5d=-0.67% 20d=2.76% aboveMA50=100.0%
- #3 Real Estate: score=5.79 5d=-0.41% 20d=5.37% aboveMA50=76.92%
- #4 Tourism & Leisure: score=5.78 5d=-8.23% 20d=13.34% aboveMA50=100.0%
- #5 Healthcare: score=5.72 5d=2.38% 20d=0.11% aboveMA50=100.0%
- #6 General / Verified EGX Expansion: score=5.44 5d=1.06% 20d=0.0% aboveMA50=84.62%
- #7 Automotive & Distribution: score=5.43 5d=-1.33% 20d=-5.43% aboveMA50=100.0%
- #8 Energy & Petrochemicals: score=4.85 5d=-0.1% 20d=1.04% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ANFI.CA: BULLISH_WATCH score=94.44 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- RAYA.CA: BULLISH_WATCH score=92.58 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ZMID.CA: BULLISH_WATCH score=90.79 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=close to resistance
- SEIG.CA: BULLISH_WATCH score=86.44 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- KWIN.CA: BULLISH_WATCH score=86.44 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- GBCO.CA: BULLISH_WATCH score=86.43 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- TMGH.CA: BULLISH_WATCH score=85.79 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ENGC.CA: BULLISH_WATCH score=84.44 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- AMER.CA: BULLISH_WATCH score=81.79 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- CCAP.CA: BULLISH_WATCH score=81.61 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=13.44 buy_ready=False sector_rank=6 price=215.2 support=195.1 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=65.5 liquidity=4259703.5 spike=0.37
- ABUK.CA: score=9.8 buy_ready=False sector_rank=18 price=81.93 support=81.2 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=18.89 liquidity=15582981.0 spike=0.12
- ACAMD.CA: score=23.4 buy_ready=False sector_rank=6 price=2.29 support=2.03 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 June 01:29 PM market time freshness=DELAYED_CURRENT RSI=60.34 liquidity=133482416.0 spike=1.11
- ACGC.CA: score=20.82 buy_ready=False sector_rank=11 price=10.0 support=8.51 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=60.49 liquidity=30702086.0 spike=0.55
- ADCI.CA: score=11.73 buy_ready=False sector_rank=6 price=218.04 support=202.22 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=66.05 liquidity=2549532.25 spike=0.38
- ADIB.CA: score=18.65 buy_ready=False sector_rank=13 price=46.43 support=45.0 resistance=50.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=46.78 liquidity=26972936.0 spike=0.17
- ADPC.CA: score=6.83 buy_ready=False sector_rank=6 price=3.71 support=3.54 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=23.16 liquidity=2654375.75 spike=0.11
- AFDI.CA: score=14.5 buy_ready=False sector_rank=6 price=44.35 support=38.51 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=65.42 liquidity=3324505.5 spike=0.18
- AFMC.CA: score=12.37 buy_ready=False sector_rank=6 price=72.8 support=69.33 resistance=80.89 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=43.25 liquidity=3197084.93 spike=0.51
- AJWA.CA: score=21.2 buy_ready=False sector_rank=6 price=137.01 support=130.01 resistance=139.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=53.04 liquidity=10540283.0 spike=1.01
- ALCN.CA: score=8.74 buy_ready=False sector_rank=20 price=28.83 support=28.4 resistance=30.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=43.44 liquidity=4690099.5 spike=0.2
- ALUM.CA: score=23.18 buy_ready=False sector_rank=6 price=25.68 support=22.52 resistance=26.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=56.9 liquidity=10256244.0 spike=0.46
- AMER.CA: score=22.32 buy_ready=False sector_rank=3 price=2.8 support=2.32 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=55.95 liquidity=69714456.0 spike=0.6
- AMES.CA: score=6.3 buy_ready=False sector_rank=6 price=51.27 support=48.0 resistance=57.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=30.81 liquidity=2123561.0 spike=0.27
- AMIA.CA: score=21.18 buy_ready=False sector_rank=6 price=9.11 support=8.54 resistance=10.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=60.44 liquidity=10829032.0 spike=0.36
- AMOC.CA: score=13.94 buy_ready=False sector_rank=8 price=8.28 support=8.12 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=27.42 liquidity=16548109.0 spike=0.2
- ANFI.CA: score=25.04 buy_ready=False sector_rank=6 price=15.52 support=13.5 resistance=16.04 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=59.56 liquidity=39216123.4 spike=1.93
- APSW.CA: score=3.81 buy_ready=False sector_rank=6 price=8.9 support=8.62 resistance=9.38 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=29.21 liquidity=638619.47 spike=0.73
- ARAB.CA: score=17.12 buy_ready=False sector_rank=3 price=0.2 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=8806370.0 spike=0.11
- ARCC.CA: score=15.71 buy_ready=False sector_rank=9 price=57.96 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=66.79 liquidity=4852012.0 spike=0.11
- AREH.CA: score=20.18 buy_ready=False sector_rank=6 price=1.53 support=1.27 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=78.57 liquidity=18217710.0 spike=0.68
- ARVA.CA: score=20.18 buy_ready=False sector_rank=6 price=11.32 support=7.71 resistance=11.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=80.46 liquidity=14704582.0 spike=0.6
- ASCM.CA: score=18.18 buy_ready=False sector_rank=6 price=56.23 support=46.2 resistance=59.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=75.21 liquidity=23448740.0 spike=0.36
- ASPI.CA: score=6.8 buy_ready=False sector_rank=6 price=0.37 support=0.35 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=74396720.0 spike=1.31
- ATLC.CA: score=10.06 buy_ready=False sector_rank=17 price=5.01 support=4.71 resistance=5.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=67.27 liquidity=2087592.5 spike=0.29
- ATQA.CA: score=21.8 buy_ready=False sector_rank=18 price=9.96 support=9.41 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=54.35 liquidity=11022129.0 spike=0.27
- AXPH.CA: score=14.38 buy_ready=False sector_rank=6 price=1159.22 support=1023.0 resistance=1239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=48.22 liquidity=3204040.0 spike=0.55
- BINV.CA: score=14.79 buy_ready=False sector_rank=1 price=46.19 support=40.53 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=65.88 liquidity=388651.09 spike=0.03
- BIOC.CA: score=11.82 buy_ready=False sector_rank=6 price=73.82 support=70.0 resistance=79.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=60.99 liquidity=647742.88 spike=0.09
- BTFH.CA: score=11.97 buy_ready=False sector_rank=17 price=3.07 support=3.03 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=34.78 liquidity=47060536.0 spike=0.2
- CAED.CA: score=9.87 buy_ready=False sector_rank=6 price=73.05 support=70.41 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=32.89 liquidity=5696997.5 spike=0.38
- CANA.CA: score=12.12 buy_ready=False sector_rank=13 price=38.22 support=33.15 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=75.35 liquidity=2470163.75 spike=0.17
- CCAP.CA: score=26.4 buy_ready=False sector_rank=1 price=5.55 support=4.66 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=60.87 liquidity=300326592.0 spike=0.35
- CCRS.CA: score=13.34 buy_ready=False sector_rank=6 price=2.5 support=2.05 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=51.32 liquidity=2160681.5 spike=0.08
- CEFM.CA: score=5.41 buy_ready=False sector_rank=6 price=106.58 support=103.07 resistance=119.89 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=34.03 liquidity=1233556.94 spike=0.34
- CERA.CA: score=24.7 buy_ready=False sector_rank=6 price=1.21 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=19538646.0 spike=1.26
- CFGH.CA: score=0.96 buy_ready=False sector_rank=6 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=6248.1 spike=1.39
- CICH.CA: score=9.38 buy_ready=False sector_rank=17 price=12.03 support=11.45 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=35.0 liquidity=1411062.38 spike=0.31
- CIEB.CA: score=12.28 buy_ready=False sector_rank=13 price=23.64 support=23.31 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=47.01 liquidity=1633988.38 spike=0.15
- CIRA.CA: score=10.59 buy_ready=False sector_rank=16 price=26.62 support=21.0 resistance=28.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=41.34 liquidity=2491886.5 spike=0.09
- CLHO.CA: score=14.61 buy_ready=False sector_rank=5 price=15.2 support=14.58 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=40.9 liquidity=5320210.0 spike=0.15
- CNFN.CA: score=8.56 buy_ready=False sector_rank=17 price=4.6 support=4.47 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=37.7 liquidity=1592932.38 spike=0.09
- COMI.CA: score=18.65 buy_ready=False sector_rank=13 price=132.9 support=129.8 resistance=144.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=45.93 liquidity=317355168.0 spike=0.47
- COPR.CA: score=15.26 buy_ready=False sector_rank=6 price=0.36 support=0.32 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=5083666.5 spike=0.13
- COSG.CA: score=21.18 buy_ready=False sector_rank=6 price=1.66 support=1.45 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=65.71 liquidity=18303908.0 spike=0.31
- CPCI.CA: score=10.89 buy_ready=False sector_rank=6 price=364.82 support=340.01 resistance=370.0 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=86.18 liquidity=2675225.11 spike=1.02
- CSAG.CA: score=8.74 buy_ready=False sector_rank=20 price=31.41 support=30.4 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=52.62 liquidity=1685161.0 spike=0.09
- DAPH.CA: score=6.66 buy_ready=False sector_rank=6 price=81.19 support=79.25 resistance=96.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=21.61 liquidity=2487271.75 spike=0.08
- DEIN.CA: score=7.18 buy_ready=False sector_rank=6 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=1.91 buy_ready=False sector_rank=12 price=24.78 support=24.24 resistance=26.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=25.1 liquidity=1167721.88 spike=0.5
- DSCW.CA: score=18.1 buy_ready=False sector_rank=6 price=1.83 support=1.71 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=43.33 liquidity=8922053.0 spike=0.14
- DTPP.CA: score=5.11 buy_ready=False sector_rank=6 price=124.05 support=123.0 resistance=139.7 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=31.36 liquidity=934964.87 spike=0.35
- EALR.CA: score=12.81 buy_ready=False sector_rank=6 price=356.86 support=346.01 resistance=392.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=41.47 liquidity=3634696.75 spike=0.36
- EASB.CA: score=9.83 buy_ready=False sector_rank=6 price=5.06 support=4.61 resistance=5.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=70.31 liquidity=654190.56 spike=0.44
- EAST.CA: score=16.09 buy_ready=False sector_rank=12 price=39.73 support=37.01 resistance=39.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=61.61 liquidity=1345474.13 spike=0.02
- EBSC.CA: score=12.29 buy_ready=False sector_rank=6 price=1.84 support=1.64 resistance=2.09 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=1113814.58 spike=0.44
- ECAP.CA: score=10.17 buy_ready=False sector_rank=6 price=31.86 support=28.7 resistance=32.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=88.64 liquidity=1996662.13 spike=0.38
- EDFM.CA: score=9.29 buy_ready=False sector_rank=6 price=333.99 support=320.2 resistance=347.0 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=39.0 liquidity=115560.54 spike=0.23
- EEII.CA: score=21.64 buy_ready=False sector_rank=6 price=2.51 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=47.5 liquidity=22897278.0 spike=1.23
- EFIC.CA: score=1.77 buy_ready=False sector_rank=18 price=207.98 support=203.01 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=6.06 liquidity=1965567.13 spike=0.49
- EFID.CA: score=18.74 buy_ready=False sector_rank=12 price=28.17 support=27.49 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=59.78 liquidity=15669126.0 spike=0.21
- EFIH.CA: score=14.24 buy_ready=False sector_rank=21 price=21.29 support=21.0 resistance=22.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=43.85 liquidity=8590117.0 spike=0.13
- EGAL.CA: score=17.8 buy_ready=False sector_rank=18 price=319.45 support=303.05 resistance=344.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=49.35 liquidity=18387356.0 spike=0.17
- EGAS.CA: score=11.44 buy_ready=False sector_rank=8 price=50.05 support=46.51 resistance=51.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=495488.03 spike=0.04
- EGBE.CA: score=3.75 buy_ready=False sector_rank=13 price=0.44 support=0.42 resistance=0.47 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=31.41 liquidity=97103.89 spike=0.75
- EGCH.CA: score=21.8 buy_ready=False sector_rank=18 price=14.75 support=12.26 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=55.07 liquidity=13621485.0 spike=0.12
- EGSA.CA: score=8.65 buy_ready=False sector_rank=14 price=8.83 support=8.3 resistance=9.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=74.7 liquidity=11854.4 spike=0.78
- EGTS.CA: score=7.32 buy_ready=False sector_rank=3 price=19.79 support=18.35 resistance=19.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=82741184.0 spike=0.75
- EHDR.CA: score=18.18 buy_ready=False sector_rank=6 price=2.7 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=83.08 liquidity=22548270.0 spike=0.42
- EKHO.CA: score=10.94 buy_ready=False sector_rank=8 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=14.93 buy_ready=False sector_rank=15 price=2.17 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=3413000.5 spike=0.12
- ELKA.CA: score=22.18 buy_ready=False sector_rank=6 price=1.28 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=64.52 liquidity=14236584.0 spike=0.35
- ELNA.CA: score=4.24 buy_ready=False sector_rank=6 price=39.54 support=37.11 resistance=42.79 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=31.97 liquidity=64885.14 spike=0.21
- ELSH.CA: score=22.36 buy_ready=False sector_rank=6 price=13.36 support=7.92 resistance=13.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=86.84 liquidity=244557136.0 spike=2.09
- ELWA.CA: score=10.53 buy_ready=False sector_rank=6 price=2.15 support=1.79 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:01 AM market time freshness=DELAYED_CURRENT RSI=91.43 liquidity=352651.56 spike=0.11
- EMFD.CA: score=22.32 buy_ready=False sector_rank=3 price=12.03 support=9.83 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=74.1 liquidity=76185656.0 spike=0.33
- ENGC.CA: score=22.86 buy_ready=False sector_rank=6 price=34.85 support=32.31 resistance=35.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=67.31 liquidity=21878426.0 spike=1.84
- EOSB.CA: score=9.28 buy_ready=False sector_rank=6 price=1.42 support=1.34 resistance=1.54 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=100002.08 spike=0.84
- EPCO.CA: score=21.18 buy_ready=False sector_rank=6 price=9.54 support=8.56 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=49.69 liquidity=10282709.0 spike=0.82
- EPPK.CA: score=10.57 buy_ready=False sector_rank=6 price=12.5 support=11.67 resistance=13.6 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=51.79 liquidity=1530000.0 spike=1.43
- ETEL.CA: score=18.64 buy_ready=False sector_rank=14 price=94.41 support=92.17 resistance=101.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=53.45 liquidity=27713674.0 spike=0.25
- ETRS.CA: score=6.18 buy_ready=False sector_rank=6 price=9.39 support=9.0 resistance=9.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=43255256.0 spike=0.84
- EXPA.CA: score=20.65 buy_ready=False sector_rank=13 price=19.16 support=18.34 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=55.02 liquidity=19909082.0 spike=0.48
- FAIT.CA: score=11.44 buy_ready=False sector_rank=13 price=37.4 support=33.94 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=51.95 liquidity=788704.81 spike=0.12
- FAITA.CA: score=8.66 buy_ready=False sector_rank=13 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=61.11 liquidity=7805.4 spike=0.15
- FERC.CA: score=0.43 buy_ready=False sector_rank=18 price=77.45 support=76.5 resistance=83.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=629418.31 spike=0.1
- FWRY.CA: score=12.65 buy_ready=False sector_rank=21 price=18.63 support=18.32 resistance=21.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=38.25 liquidity=64104716.0 spike=0.22
- GBCO.CA: score=21.53 buy_ready=False sector_rank=7 price=27.6 support=25.25 resistance=29.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=134768608.0 spike=1.18
- GDWA.CA: score=15.08 buy_ready=False sector_rank=6 price=0.82 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=61.11 liquidity=2903231.5 spike=0.28
- GGCC.CA: score=18.53 buy_ready=False sector_rank=6 price=0.43 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=63.33 liquidity=6358558.5 spike=0.96
- GIHD.CA: score=13.59 buy_ready=False sector_rank=6 price=41.96 support=39.1 resistance=44.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=53.59 liquidity=414579.0 spike=0.07
- GMCI.CA: score=11.45 buy_ready=False sector_rank=6 price=1.78 support=1.67 resistance=1.84 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=65.38 liquidity=274689.6 spike=0.84
- GRCA.CA: score=1.79 buy_ready=False sector_rank=6 price=54.75 support=53.16 resistance=60.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=27.6 liquidity=616749.75 spike=0.07
- GSSC.CA: score=1.64 buy_ready=False sector_rank=6 price=249.35 support=228.1 resistance=272.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=7.12 liquidity=461742.44 spike=0.05
- GTWL.CA: score=2.88 buy_ready=False sector_rank=6 price=48.71 support=46.5 resistance=50.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6700341.5 spike=0.89
- HDBK.CA: score=11.2 buy_ready=False sector_rank=13 price=142.93 support=138.75 resistance=150.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=58.6 liquidity=2548195.75 spike=0.16
- HELI.CA: score=20.32 buy_ready=False sector_rank=3 price=6.46 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=48.78 liquidity=26214144.0 spike=0.16
- HRHO.CA: score=13.97 buy_ready=False sector_rank=17 price=26.5 support=26.05 resistance=30.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=17651266.0 spike=0.09
- ICID.CA: score=20.48 buy_ready=False sector_rank=6 price=6.35 support=4.43 resistance=6.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=87.56 liquidity=14613034.0 spike=1.15
- IDRE.CA: score=13.23 buy_ready=False sector_rank=6 price=44.44 support=39.72 resistance=49.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=50.96 liquidity=2052708.38 spike=0.06
- IFAP.CA: score=2.42 buy_ready=False sector_rank=10 price=19.49 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=2568694.75 spike=0.16
- INFI.CA: score=10.1 buy_ready=False sector_rank=6 price=100.93 support=99.51 resistance=112.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=45.63 liquidity=1922761.63 spike=0.11
- IRON.CA: score=7.27 buy_ready=False sector_rank=18 price=32.57 support=31.83 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=55.6 liquidity=1466771.38 spike=0.18
- ISMA.CA: score=18.18 buy_ready=False sector_rank=6 price=29.84 support=20.15 resistance=29.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=91.81 liquidity=47700984.0 spike=0.98
- ISMQ.CA: score=21.8 buy_ready=False sector_rank=18 price=8.0 support=7.27 resistance=8.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=62.07 liquidity=38646400.0 spike=0.79
- ISPH.CA: score=23.29 buy_ready=False sector_rank=5 price=12.5 support=11.12 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=64.73 liquidity=27614018.0 spike=0.18
- JUFO.CA: score=22.74 buy_ready=False sector_rank=12 price=30.5 support=26.51 resistance=30.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=71.6 liquidity=25442704.0 spike=0.56
- KABO.CA: score=14.24 buy_ready=False sector_rank=11 price=6.35 support=5.92 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=70.11 liquidity=3419927.75 spike=0.17
- KWIN.CA: score=14.66 buy_ready=False sector_rank=6 price=73.33 support=69.0 resistance=81.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=44.62 liquidity=3481790.5 spike=0.93
- KZPC.CA: score=11.29 buy_ready=False sector_rank=6 price=10.67 support=10.3 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=44.2 liquidity=2117191.25 spike=0.18
- LCSW.CA: score=11.97 buy_ready=False sector_rank=9 price=27.44 support=26.16 resistance=29.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=45.55 liquidity=3115496.0 spike=0.19
- LUTS.CA: score=17.64 buy_ready=False sector_rank=6 price=0.63 support=0.54 resistance=0.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=71.69 liquidity=6463009.0 spike=0.4
- MAAL.CA: score=22.96 buy_ready=False sector_rank=6 price=5.96 support=4.44 resistance=6.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=7788980.5 spike=0.66
- MASR.CA: score=16.43 buy_ready=False sector_rank=6 price=6.9 support=6.63 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=50.48 liquidity=7254188.0 spike=0.12
- MBSC.CA: score=20.86 buy_ready=False sector_rank=9 price=275.86 support=261.52 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=51.41 liquidity=21366072.0 spike=0.43
- MCQE.CA: score=15.13 buy_ready=False sector_rank=9 price=188.69 support=188.01 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=52.24 liquidity=6271653.5 spike=0.33
- MCRO.CA: score=20.66 buy_ready=False sector_rank=6 price=1.27 support=1.21 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=8480360.0 spike=0.1
- MENA.CA: score=15.11 buy_ready=False sector_rank=3 price=6.85 support=5.76 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=60.26 liquidity=790540.0 spike=0.05
- MEPA.CA: score=20.38 buy_ready=False sector_rank=6 price=1.74 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=46.43 liquidity=9205981.0 spike=0.43
- MFPC.CA: score=12.8 buy_ready=False sector_rank=18 price=42.6 support=42.3 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=26.96 liquidity=10479380.0 spike=0.11
- MFSC.CA: score=5.99 buy_ready=False sector_rank=6 price=47.06 support=33.01 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=25.62 liquidity=1818611.5 spike=0.12
- MHOT.CA: score=16.68 buy_ready=False sector_rank=4 price=31.52 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=60.73 liquidity=5363208.0 spike=0.27
- MICH.CA: score=15.41 buy_ready=False sector_rank=6 price=36.87 support=35.01 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=60.8 liquidity=2231902.0 spike=0.25
- MILS.CA: score=14.86 buy_ready=False sector_rank=6 price=144.32 support=127.01 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=48.66 liquidity=3685445.25 spike=0.13
- MIPH.CA: score=9.77 buy_ready=False sector_rank=5 price=666.86 support=640.0 resistance=729.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=39.8 liquidity=479054.97 spike=0.13
- MOED.CA: score=4.34 buy_ready=False sector_rank=6 price=0.69 support=0.68 resistance=0.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=18.28 liquidity=4168941.5 spike=0.31
- MOIL.CA: score=12.98 buy_ready=False sector_rank=8 price=0.48 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=61.43 liquidity=37245.8 spike=0.2
- MOIN.CA: score=11.61 buy_ready=False sector_rank=6 price=24.99 support=23.13 resistance=26.4 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=60.0 liquidity=1429452.98 spike=0.8
- MOSC.CA: score=5.32 buy_ready=False sector_rank=6 price=266.91 support=268.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=20.91 liquidity=1148529.75 spike=0.08
- MPCI.CA: score=23.18 buy_ready=False sector_rank=6 price=230.0 support=192.01 resistance=233.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=68.01 liquidity=34975320.0 spike=0.35
- MPCO.CA: score=20.85 buy_ready=False sector_rank=10 price=1.84 support=1.54 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=65518876.0 spike=0.97
- MPRC.CA: score=17.04 buy_ready=False sector_rank=6 price=33.96 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=73.66 liquidity=5867705.0 spike=0.27
- MTIE.CA: score=16.11 buy_ready=False sector_rank=7 price=9.16 support=8.71 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=47.29 liquidity=4934402.5 spike=0.22
- NAHO.CA: score=5.21 buy_ready=False sector_rank=6 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=37.5 liquidity=32042.99 spike=0.92
- NCCW.CA: score=10.96 buy_ready=False sector_rank=6 price=6.65 support=6.3 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=69800784.0 spike=3.39
- NEDA.CA: score=11.5 buy_ready=False sector_rank=6 price=2.8 support=2.65 resistance=2.87 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=60.0 liquidity=326233.59 spike=0.62
- NHPS.CA: score=13.08 buy_ready=False sector_rank=6 price=69.9 support=67.53 resistance=73.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=44.84 liquidity=2907774.5 spike=0.27
- NINH.CA: score=10.13 buy_ready=False sector_rank=6 price=17.89 support=17.53 resistance=20.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=50.55 liquidity=951794.19 spike=0.08
- NIPH.CA: score=21.29 buy_ready=False sector_rank=5 price=170.52 support=155.1 resistance=186.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=63.13 liquidity=45681488.0 spike=0.37
- OBRI.CA: score=4.01 buy_ready=False sector_rank=6 price=34.63 support=33.63 resistance=39.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=30.2 liquidity=2834201.25 spike=0.27
- OCDI.CA: score=14.89 buy_ready=False sector_rank=3 price=20.88 support=20.19 resistance=23.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=45.23 liquidity=7573618.0 spike=0.18
- OCPH.CA: score=8.48 buy_ready=False sector_rank=6 price=365.6 support=350.0 resistance=409.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=32.47 liquidity=4302531.5 spike=0.39
- ODIN.CA: score=14.88 buy_ready=False sector_rank=6 price=2.08 support=1.89 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=67.74 liquidity=3699550.5 spike=0.37
- OFH.CA: score=19.54 buy_ready=False sector_rank=6 price=0.63 support=0.6 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=46.46 liquidity=6367447.0 spike=0.29
- OIH.CA: score=14.4 buy_ready=False sector_rank=1 price=1.41 support=1.35 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=12836193.0 spike=0.11
- OLFI.CA: score=12.56 buy_ready=False sector_rank=12 price=21.61 support=21.0 resistance=22.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=55.17 liquidity=3811148.5 spike=0.17
- ORAS.CA: score=4.6 buy_ready=False sector_rank=19 price=730.01 support=717.0 resistance=740.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=88880472.0 spike=1.0
- ORHD.CA: score=20.32 buy_ready=False sector_rank=3 price=37.35 support=32.9 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=65.64 liquidity=70825368.0 spike=0.35
- ORWE.CA: score=20.82 buy_ready=False sector_rank=11 price=23.8 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=69.79 liquidity=13257035.0 spike=0.29
- PHAR.CA: score=11.66 buy_ready=False sector_rank=5 price=86.51 support=83.96 resistance=92.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=2370748.75 spike=0.07
- PHDC.CA: score=20.32 buy_ready=False sector_rank=3 price=15.24 support=13.01 resistance=16.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=67.27 liquidity=156130032.0 spike=0.37
- PHTV.CA: score=13.91 buy_ready=False sector_rank=6 price=211.5 support=201.5 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=42.92 liquidity=2736292.0 spike=0.18
- POUL.CA: score=14.8 buy_ready=False sector_rank=12 price=37.34 support=34.06 resistance=39.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=60.74 liquidity=4053176.75 spike=0.08
- PRCL.CA: score=23.6 buy_ready=False sector_rank=9 price=26.47 support=21.01 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=68.29 liquidity=49139488.0 spike=1.37
- PRDC.CA: score=13.9 buy_ready=False sector_rank=3 price=6.12 support=5.3 resistance=6.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=72.93 liquidity=1583080.88 spike=0.08
- PRMH.CA: score=16.36 buy_ready=False sector_rank=6 price=2.8 support=2.17 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=83.52 liquidity=8179714.0 spike=0.5
- RACC.CA: score=10.59 buy_ready=False sector_rank=6 price=9.87 support=9.56 resistance=12.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=55.19 liquidity=1412702.75 spike=0.06
- RAKT.CA: score=9.44 buy_ready=False sector_rank=6 price=23.79 support=22.1 resistance=25.0 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=54.9 liquidity=262070.65 spike=0.99
- RAYA.CA: score=23.4 buy_ready=False sector_rank=2 price=7.49 support=6.94 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=22802868.0 spike=0.2
- RMDA.CA: score=21.29 buy_ready=False sector_rank=5 price=5.29 support=4.91 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=29490484.0 spike=0.27
- ROTO.CA: score=23.88 buy_ready=False sector_rank=6 price=35.5 support=32.66 resistance=36.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=63.13 liquidity=16341032.0 spike=1.35
- RREI.CA: score=15.75 buy_ready=False sector_rank=6 price=3.59 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=60.27 liquidity=2578918.75 spike=0.11
- RTVC.CA: score=15.67 buy_ready=False sector_rank=6 price=3.97 support=3.75 resistance=4.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=50.82 liquidity=2494895.5 spike=0.39
- RUBX.CA: score=17.08 buy_ready=False sector_rank=6 price=10.63 support=9.8 resistance=11.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=17.0 liquidity=20996350.0 spike=1.45
- SAUD.CA: score=11.64 buy_ready=False sector_rank=13 price=22.25 support=21.8 resistance=25.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=49.51 liquidity=2994439.25 spike=0.21
- SCEM.CA: score=12.24 buy_ready=False sector_rank=9 price=64.09 support=62.5 resistance=72.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=39.53 liquidity=3383736.5 spike=0.08
- SCFM.CA: score=6.97 buy_ready=False sector_rank=6 price=260.39 support=255.7 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=25.91 liquidity=2795089.5 spike=0.1
- SCTS.CA: score=9.96 buy_ready=False sector_rank=16 price=634.38 support=590.01 resistance=709.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=17.82 liquidity=6861835.0 spike=0.63
- SDTI.CA: score=18.24 buy_ready=False sector_rank=6 price=46.52 support=43.4 resistance=46.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=60.94 liquidity=5061018.5 spike=0.27
- SEIG.CA: score=17.95 buy_ready=False sector_rank=6 price=189.53 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=56.06 liquidity=4771179.0 spike=0.84
- SIPC.CA: score=23.18 buy_ready=False sector_rank=6 price=3.69 support=3.4 resistance=3.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=59.09 liquidity=12470482.0 spike=0.81
- SKPC.CA: score=13.8 buy_ready=False sector_rank=18 price=17.3 support=16.8 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=35.68 liquidity=18190978.0 spike=0.26
- SMFR.CA: score=5.3 buy_ready=False sector_rank=6 price=207.43 support=203.51 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=30.74 liquidity=1127449.5 spike=0.15
- SNFC.CA: score=11.35 buy_ready=False sector_rank=6 price=12.01 support=11.66 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=45.24 liquidity=2177217.0 spike=0.08
- SPIN.CA: score=6.85 buy_ready=False sector_rank=11 price=14.05 support=13.69 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=43.23 liquidity=1033406.81 spike=0.21
- SPMD.CA: score=18.54 buy_ready=False sector_rank=6 price=0.42 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=64.1 liquidity=5359287.5 spike=0.21
- SUGR.CA: score=15.68 buy_ready=False sector_rank=12 price=49.97 support=48.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=37.22 liquidity=2932331.25 spike=0.18
- SVCE.CA: score=19.18 buy_ready=False sector_rank=6 price=8.78 support=8.33 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=36.44 liquidity=12682619.0 spike=0.1
- SWDY.CA: score=13.23 buy_ready=False sector_rank=15 price=87.47 support=85.25 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=62.8 liquidity=4708369.5 spike=0.13
- TALM.CA: score=10.62 buy_ready=False sector_rank=16 price=15.93 support=15.12 resistance=17.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=51.08 liquidity=521733.38 spike=0.04
- TMGH.CA: score=22.32 buy_ready=False sector_rank=3 price=96.69 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=60.15 liquidity=92651952.0 spike=0.18
- TRTO.CA: score=7.18 buy_ready=False sector_rank=6 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=211.38 spike=0.44
- UEFM.CA: score=5.55 buy_ready=False sector_rank=6 price=474.08 support=455.6 resistance=505.9 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=36.58 liquidity=377841.75 spike=0.45
- UEGC.CA: score=21.0 buy_ready=False sector_rank=6 price=1.46 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=69.23 liquidity=9821585.0 spike=0.4
- UNIP.CA: score=18.98 buy_ready=False sector_rank=6 price=0.32 support=0.28 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=67.69 liquidity=8805645.0 spike=0.56
- UNIT.CA: score=17.33 buy_ready=False sector_rank=3 price=14.12 support=10.89 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=65.67 liquidity=5017543.5 spike=0.47
- WCDF.CA: score=4.93 buy_ready=False sector_rank=6 price=539.17 support=535.0 resistance=559.0 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=13.84 liquidity=370948.95 spike=1.19
- WKOL.CA: score=8.53 buy_ready=False sector_rank=6 price=299.89 support=290.0 resistance=339.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=34.27 liquidity=2353022.0 spike=0.38
- ZEOT.CA: score=14.33 buy_ready=False sector_rank=6 price=9.33 support=8.43 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=58.16 liquidity=1149771.5 spike=0.16
- ZMID.CA: score=25.58 buy_ready=False sector_rank=3 price=6.5 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=57.94 liquidity=340545280.0 spike=1.63

## Backtesting Lite
- CCAP.CA: 180d return=118.82%, max drawdown=-25.0%, MA20>MA50 days last20=20, as_of=2026-06-07T21:00:00+00:00
- ZMID.CA: 180d return=57.03%, max drawdown=-19.84%, MA20>MA50 days last20=20, as_of=2026-06-07T21:00:00+00:00
- ANFI.CA: 180d return=137.78%, max drawdown=-19.31%, MA20>MA50 days last20=20, as_of=2026-06-07T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- ZMID.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=524 sources=3 expected=Zahraa Maadi Investment and Development summary=Zahraa Maadi unveils distribution date for 2025 cash dividends; Zahraa Maadi to disburse EGP 250m dividends for 2025; Zahraa Maadi’s stock faces key resistance at EGP 5.22
  - Zahraa Maadi unveils distribution date for 2025 cash dividends: https://english.mubasher.info/news/4594804/Zahraa-Maadi-unveils-distribution-date-for-2025-cash-dividends/
  - Zahraa Maadi to disburse EGP 250m dividends for 2025: https://english.mubasher.info/news/4583591/Zahraa-Maadi-to-disburse-EGP-250m-dividends-for-2025/
  - Zahraa Maadi’s stock faces key resistance at EGP 5.22: https://english.mubasher.info/news/4563531/Zahraa-Maadi-s-stock-faces-key-resistance-at-EGP-5-22/
- ANFI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tycoon Holding Company For Financial Investments summary=Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- CERA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=The Arab Ceramic Co. summary=Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- ROTO.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Rowad Tourism Company summary=Shareholder raises stake in Rowad Tourism; Target raises stake in Rowad Tourism to 10.68%; Rowad Tourism sees EGP 22.4m block trading deal
  - Shareholder raises stake in Rowad Tourism: https://english.mubasher.info/news/4043645/Shareholder-raises-stake-in-Rowad-Tourism/
  - Target raises stake in Rowad Tourism to 10.68%: https://english.mubasher.info/news/4031744/Target-raises-stake-in-Rowad-Tourism-to-10-68-/
  - Rowad Tourism sees EGP 22.4m block trading deal: https://english.mubasher.info/news/4031133/Rowad-Tourism-sees-EGP-22-4m-block-trading-deal/
- PRCL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Ceramic and Porcelain summary=Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- RAYA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=524 sources=3 expected=Raya Holding summary=Raya stock maintains bullish momentum above EGP 9; Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt; Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn
  - Raya stock maintains bullish momentum above EGP 9: https://english.mubasher.info/news/4601857/Raya-stock-maintains-bullish-momentum-above-EGP-9/
  - Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt: https://english.mubasher.info/news/4577815/Aman-Holding-MSMEDA-partner-to-inject-EGP-300m-into-SMEs-across-Egypt/
  - Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn: https://english.mubasher.info/news/4564195/Raya-Holding-s-consolidated-profits-surge-in-2025-revenues-hit-EGP-63-8bn/
- ACAMD.CA: status=OLD_ACCEPTED latest=2020-01-01 age_days=2351 sources=3 expected=Arab Co.,for asset management and development summary=Arab Company for Asset Management shifts to EGP 7m net profits in 9M-25; Arab Co. for Asset Management approves offer to sell land in El-Minya; Arab Co. Asset Management swings to loss in 2020
  - Arab Company for Asset Management shifts to EGP 7m net profits in 9M-25: https://english.mubasher.info/news/4543171/Arab-Company-for-Asset-Management-shifts-to-EGP-7m-net-profits-in-9M-25/
  - Arab Co. for Asset Management approves offer to sell land in El-Minya: https://english.mubasher.info/news/3777445/Arab-Co-for-Asset-Management-approves-offer-to-sell-land-in-El-Minya/
  - Arab Co. Asset Management swings to loss in 2020: https://english.mubasher.info/news/3767136/Arab-Co-Asset-Management-swings-to-loss-in-2020/

## Warnings
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for ZMID.CA matches the company but appears old; latest detected date is 2025-01-01.
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- Evidence for ROTO.CA matches the company but no source/report date was detected.
- Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- Evidence for RAYA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ACAMD.CA matches the company but appears old; latest detected date is 2020-01-01.
