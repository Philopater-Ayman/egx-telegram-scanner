# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-07-08T08:01:30.196957+00:00
Generated Cairo: 2026-07-08 11:01
Run timing: target 08:45 Cairo | generated Cairo 2026-07-08 11:01 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-07-08 10:57

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 57
- Data quality issues: 0
- Tradeable price/liquidity tickers: 175/190
- Top sector: Technology & Distribution

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, July 08
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 65.0% / above MA50 60.0%
- EGX70 regime: BULLISH / above MA20 75.0% / above MA50 77.78%
- Sector breadth: 85.71%
- Risk mode: BROAD_RISK_ON

## Top Liquidity
- CCAP.CA: liquidity=441741312.0 spike=0.69 score=25.9
- BTFH.CA: liquidity=93584384.0 spike=0.5 score=25.9
- COMI.CA: liquidity=92653632.0 spike=0.21 score=25.9
- GTWL.CA: liquidity=86743432.0 spike=1.73 score=12.34
- ORAS.CA: liquidity=60056704.0 spike=1.0 score=9.1

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b-20230311:free
- Summary: EGX30 and EGX70 are bullish with sector breadth at 85.7%, putting the market in a BROAD_RISK_ON mode, but the local scanner’s evidence, liquidity‑freshness and technical gates were not satisfied, so it defaults to a HOLD stance.
- Top‑ranked tickets (e.g., ETEL.CA, OLFI.CA, TMGH.CA) show bullish outlooks and tradeable liquidity, yet many exhibit cooling liquidity, extended momentum and sit close to resistance, limiting near‑term upside.
- Sector leadership lies in Technology & Distribution, Automotive & Distribution and Fintech & Payments, giving those stocks stronger support while others lack sector backing.
- Support‑to‑resistance distances are mostly single‑digit percent and RSI values range from 55 to 70, indicating modest room for rapid moves over the next 1‑3 days.
- Despite the bullish index regime and high sector breadth, uncertainty remains due to weak evidence, liquidity cooling and mixed technical signals, keeping the scanner in a cautious HOLD posture.

## Top Liquidity Spikes
- SEIG.CA: spike=16.27 liquidity=42050764.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SMFR.CA: spike=3.53 liquidity=5719505.37 outlook=BULLISH_WATCH score=87.94 buy_ready=True
- MIPH.CA: spike=3.14 liquidity=4354700.0 outlook=BULLISH_WATCH score=82.74 buy_ready=True
- NAHO.CA: spike=2.95 liquidity=64330.24 outlook=WEAK_OR_RISKY score=23.94 buy_ready=False
- UEFM.CA: spike=2.24 liquidity=2079210.4 outlook=BULLISH_WATCH score=81.94 buy_ready=True

## Sector Leaderboard
- #1 Technology & Distribution: score=14.61 5d=16.29% 20d=7.25% aboveMA50=100.0%
- #2 Automotive & Distribution: score=10.5 5d=3.96% 20d=13.81% aboveMA50=100.0%
- #3 Fintech & Payments: score=10.23 5d=10.43% 20d=6.39% aboveMA50=50.0%
- #4 Investment Holding: score=8.84 5d=6.98% 20d=4.41% aboveMA50=66.67%
- #5 Telecommunications: score=8.08 5d=3.08% 20d=0.38% aboveMA50=100.0%
- #6 Transportation & Logistics: score=7.91 5d=3.57% 20d=1.52% aboveMA50=100.0%
- #7 Real Estate: score=7.64 5d=5.62% 20d=4.46% aboveMA50=76.92%
- #8 Tourism & Leisure: score=7.5 5d=0.0% 20d=0.0% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MTIE.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- SMFR.CA: BULLISH_WATCH score=87.94 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ACAMD.CA: BULLISH_WATCH score=84.94 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- MIPH.CA: BULLISH_WATCH score=82.74 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended; close to resistance; sector is not leading
- UEFM.CA: BULLISH_WATCH score=81.94 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended; close to resistance; sector is not leading
- SDTI.CA: BULLISH_WATCH score=81.94 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- TMGH.CA: BULLISH_WATCH score=79.64 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; close to resistance
- OLFI.CA: BULLISH_WATCH score=79.29 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- CCAP.CA: BULLISH_WATCH score=78.84 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ETEL.CA: BULLISH_WATCH score=78.08 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended

## BUY-Ready Candidates
- ETEL.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=78.08 sector_rank=5 price=98.56 support=89.01 resistance=96.63 liquidity=17987148.0
- OLFI.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=79.29 sector_rank=14 price=23.18 support=21.0 resistance=23.08 liquidity=11273787.0
- TMGH.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=79.64 sector_rank=7 price=98.0 support=92.1 resistance=98.98 liquidity=36993260.0
- EFIH.CA: rank=28.9 outlook=BULLISH_WATCH outlook_score=78 sector_rank=3 price=23.23 support=20.0 resistance=23.65 liquidity=12135605.0
- MIPH.CA: rank=28.53 outlook=BULLISH_WATCH outlook_score=82.74 sector_rank=10 price=700.0 support=630.13 resistance=710.0 liquidity=4354700.0
- ARAB.CA: rank=27.9 outlook=BULLISH_WATCH outlook_score=71.64 sector_rank=7 price=0.23 support=0.2 resistance=0.23 liquidity=25619190.0
- ADIB.CA: rank=27.9 outlook=CONSTRUCTIVE outlook_score=65.48 sector_rank=13 price=47.93 support=44.01 resistance=48.49 liquidity=32201258.0
- HELI.CA: rank=27.9 outlook=BULLISH_WATCH outlook_score=71.64 sector_rank=7 price=6.72 support=6.28 resistance=6.83 liquidity=30623064.0
- ACAMD.CA: rank=27.88 outlook=BULLISH_WATCH outlook_score=84.94 sector_rank=15 price=2.37 support=2.14 resistance=2.6 liquidity=20274580.0
- MASR.CA: rank=27.88 outlook=CONSTRUCTIVE outlook_score=64.94 sector_rank=15 price=7.73 support=6.54 resistance=7.73 liquidity=28756962.0

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=24.45 buy_ready=False sector_rank=15 price=227.05 support=196.0 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=73.0 liquidity=6574919.0 spike=0.91
- ABUK.CA: score=21.0 buy_ready=False sector_rank=21 price=70.68 support=66.66 resistance=83.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=37.12 liquidity=34104680.0 spike=0.28
- ACAMD.CA: score=27.88 buy_ready=True sector_rank=15 price=2.37 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=58.54 liquidity=20274580.0 spike=0.17
- ACGC.CA: score=19.66 buy_ready=True sector_rank=9 price=9.59 support=8.92 resistance=10.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=54.8 liquidity=3758148.5 spike=0.13
- ADCI.CA: score=14.29 buy_ready=False sector_rank=15 price=234.57 support=212.52 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=65.51 liquidity=414582.44 spike=0.04
- ADIB.CA: score=27.9 buy_ready=True sector_rank=13 price=47.93 support=44.01 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=48.45 liquidity=32201258.0 spike=0.44
- ADPC.CA: score=13.36 buy_ready=False sector_rank=15 price=3.58 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=49.54 liquidity=2482811.75 spike=0.16
- AFDI.CA: score=16.51 buy_ready=False sector_rank=15 price=45.83 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=59.64 liquidity=631222.13 spike=0.04
- AFMC.CA: score=18.32 buy_ready=False sector_rank=15 price=72.97 support=66.0 resistance=74.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=53.35 liquidity=446027.81 spike=0.21
- AJWA.CA: score=14.37 buy_ready=False sector_rank=15 price=178.01 support=132.15 resistance=190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=65.75 liquidity=489563.84 spike=0.02
- ALCN.CA: score=19.69 buy_ready=True sector_rank=6 price=29.09 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=52.32 liquidity=1792568.88 spike=0.16
- ALUM.CA: score=20.06 buy_ready=True sector_rank=15 price=23.56 support=20.55 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=41.17 liquidity=4183598.5 spike=0.48
- AMER.CA: score=10.9 buy_ready=False sector_rank=7 price=2.86 support=2.77 resistance=2.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48213876.0 spike=0.82
- AMES.CA: score=17.52 buy_ready=True sector_rank=15 price=58.75 support=45.15 resistance=69.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=67.53 liquidity=1641819.0 spike=0.1
- AMIA.CA: score=19.15 buy_ready=True sector_rank=15 price=9.18 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:36 AM market time freshness=DELAYED_CURRENT RSI=38.16 liquidity=3277570.75 spike=0.32
- AMOC.CA: score=21.87 buy_ready=False sector_rank=19 price=7.82 support=7.42 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=47.75 liquidity=17379948.0 spike=0.38
- ANFI.CA: score=12.21 buy_ready=False sector_rank=15 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=STALE RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=11.13 buy_ready=False sector_rank=15 price=8.51 support=8.0 resistance=9.0 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=46.56 liquidity=932661.99 spike=1.16
- ARAB.CA: score=27.9 buy_ready=True sector_rank=7 price=0.23 support=0.2 resistance=0.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=25619190.0 spike=0.35
- ARCC.CA: score=20.85 buy_ready=True sector_rank=16 price=55.95 support=53.0 resistance=58.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=46.87 liquidity=5118182.5 spike=0.17
- AREH.CA: score=17.94 buy_ready=True sector_rank=15 price=1.59 support=1.42 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=2063046.25 spike=0.05
- ARVA.CA: score=9.87 buy_ready=False sector_rank=15 price=11.16 support=10.3 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=31.58 liquidity=996101.13 spike=0.04
- ASCM.CA: score=21.9 buy_ready=True sector_rank=15 price=59.53 support=54.12 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=45.28 liquidity=6028497.5 spike=0.06
- ASPI.CA: score=15.84 buy_ready=False sector_rank=15 price=0.32 support=0.3 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=54.12 liquidity=1967983.25 spike=0.03
- ATLC.CA: score=18.89 buy_ready=False sector_rank=11 price=5.23 support=4.7 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:36 AM market time freshness=DELAYED_CURRENT RSI=55.07 liquidity=985002.63 spike=0.14
- ATQA.CA: score=20.12 buy_ready=False sector_rank=21 price=9.7 support=9.02 resistance=10.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=59.23 liquidity=7123200.5 spike=0.19
- AXPH.CA: score=18.26 buy_ready=False sector_rank=15 price=1182.69 support=1073.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=60.78 liquidity=385985.16 spike=0.14
- BINV.CA: score=18.38 buy_ready=False sector_rank=4 price=48.59 support=44.02 resistance=51.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=58.7 liquidity=481224.34 spike=0.07
- BIOC.CA: score=18.31 buy_ready=True sector_rank=15 price=72.09 support=66.75 resistance=75.5 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=54.02 liquidity=2349412.98 spike=1.04
- BTFH.CA: score=25.9 buy_ready=True sector_rank=11 price=3.1 support=2.91 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=93584384.0 spike=0.5
- CAED.CA: score=16.77 buy_ready=False sector_rank=15 price=73.88 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=53.17 liquidity=897363.38 spike=0.2
- CANA.CA: score=16.31 buy_ready=False sector_rank=13 price=36.64 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=36.95 liquidity=407274.56 spike=0.04
- CCAP.CA: score=25.9 buy_ready=True sector_rank=4 price=5.25 support=4.65 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=51.58 liquidity=441741312.0 spike=0.69
- CCRS.CA: score=15.05 buy_ready=False sector_rank=15 price=2.36 support=2.18 resistance=2.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=49.21 liquidity=1170780.88 spike=0.08
- CEFM.CA: score=11.57 buy_ready=False sector_rank=15 price=100.79 support=95.75 resistance=108.6 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=37.69 liquidity=695047.85 spike=0.61
- CERA.CA: score=18.47 buy_ready=True sector_rank=15 price=1.25 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=64.29 liquidity=2595225.5 spike=0.14
- CFGH.CA: score=6.88 buy_ready=False sector_rank=15 price=0.1 support=0.1 resistance=0.1 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=635.0 spike=0.11
- CICH.CA: score=15.3 buy_ready=False sector_rank=11 price=11.97 support=11.1 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:29 AM market time freshness=DELAYED_CURRENT RSI=61.09 liquidity=400480.28 spike=0.12
- CIEB.CA: score=18.43 buy_ready=False sector_rank=13 price=24.23 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=68.12 liquidity=525026.63 spike=0.08
- CIRA.CA: score=17.04 buy_ready=True sector_rank=12 price=29.2 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=65.42 liquidity=3135620.0 spike=0.17
- CLHO.CA: score=19.74 buy_ready=True sector_rank=10 price=16.41 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=63.81 liquidity=1843639.38 spike=0.05
- CNFN.CA: score=21.8 buy_ready=True sector_rank=11 price=4.85 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=65.47 liquidity=5903500.0 spike=0.14
- COMI.CA: score=25.9 buy_ready=True sector_rank=13 price=134.82 support=126.21 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=49.46 liquidity=92653632.0 spike=0.21
- COPR.CA: score=14.22 buy_ready=False sector_rank=15 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=50.79 liquidity=1341254.38 spike=0.06
- COSG.CA: score=23.23 buy_ready=True sector_rank=15 price=1.62 support=1.47 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=7356514.0 spike=0.13
- CPCI.CA: score=14.4 buy_ready=False sector_rank=15 price=396.33 support=354.0 resistance=434.99 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=75.89 liquidity=1524285.13 spike=0.61
- CSAG.CA: score=16.28 buy_ready=False sector_rank=6 price=32.65 support=30.08 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=80.97 liquidity=1379099.75 spike=0.08
- DAPH.CA: score=18.32 buy_ready=False sector_rank=15 price=82.45 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=68.77 liquidity=448297.66 spike=0.05
- DEIN.CA: score=0.88 buy_ready=False sector_rank=15 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=1.0
- DOMT.CA: score=13.4 buy_ready=False sector_rank=14 price=27.01 support=23.7 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=81.86 liquidity=501769.88 spike=0.1
- DSCW.CA: score=18.25 buy_ready=False sector_rank=15 price=1.8 support=1.71 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT RSI=42.31 liquidity=6374269.5 spike=0.2
- DTPP.CA: score=26.0 buy_ready=False sector_rank=15 price=207.86 support=114.0 resistance=234.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=95.93 liquidity=38779456.0 spike=1.56
- EALR.CA: score=10.76 buy_ready=False sector_rank=15 price=379.28 support=376.18 resistance=389.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7687902.5 spike=2.1
- EASB.CA: score=18.11 buy_ready=True sector_rank=15 price=7.0 support=4.87 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=63.62 liquidity=2236276.5 spike=0.15
- EAST.CA: score=7.17 buy_ready=False sector_rank=14 price=37.55 support=36.63 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=27.19 liquidity=2269215.25 spike=0.06
- EBSC.CA: score=17.52 buy_ready=True sector_rank=15 price=1.99 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=66.13 liquidity=1645170.5 spike=0.31
- ECAP.CA: score=16.96 buy_ready=True sector_rank=15 price=32.64 support=30.02 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=57.09 liquidity=1079886.75 spike=0.11
- EDFM.CA: score=6.29 buy_ready=False sector_rank=15 price=326.2 support=310.2 resistance=355.0 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=30.43 liquidity=413621.62 spike=0.88
- EEII.CA: score=20.21 buy_ready=False sector_rank=15 price=2.81 support=2.3 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=74.29 liquidity=4333507.0 spike=0.22
- EFIC.CA: score=3.35 buy_ready=False sector_rank=21 price=183.61 support=180.02 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=16.23 liquidity=350671.59 spike=0.14
- EFID.CA: score=21.63 buy_ready=True sector_rank=14 price=28.47 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=49.58 liquidity=3733511.75 spike=0.05
- EFIH.CA: score=28.9 buy_ready=True sector_rank=3 price=23.23 support=20.0 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=69.95 liquidity=12135605.0 spike=0.3
- EGAL.CA: score=21.0 buy_ready=False sector_rank=21 price=295.73 support=272.28 resistance=325.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=48.45 liquidity=10377365.0 spike=0.21
- EGAS.CA: score=14.27 buy_ready=False sector_rank=19 price=50.15 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=40.77 liquidity=1393770.38 spike=0.19
- EGBE.CA: score=16.45 buy_ready=False sector_rank=13 price=0.46 support=0.43 resistance=0.47 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=74.07 liquidity=73777.85 spike=1.24
- EGCH.CA: score=19.0 buy_ready=False sector_rank=21 price=12.82 support=12.13 resistance=14.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=41.39 liquidity=11205994.0 spike=0.25
- EGSA.CA: score=10.91 buy_ready=False sector_rank=5 price=8.87 support=8.55 resistance=8.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 July 01:10 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=7755.35 spike=0.76
- EGTS.CA: score=25.9 buy_ready=True sector_rank=7 price=19.39 support=15.1 resistance=20.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=55.96 liquidity=20920656.0 spike=0.31
- EHDR.CA: score=25.88 buy_ready=True sector_rank=15 price=2.64 support=2.37 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=10907483.0 spike=0.19
- EKHO.CA: score=11.87 buy_ready=False sector_rank=19 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=10.44 buy_ready=False sector_rank=18 price=2.11 support=2.04 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=1481186.63 spike=0.09
- ELKA.CA: score=22.46 buy_ready=False sector_rank=15 price=1.43 support=1.19 resistance=1.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT RSI=72.92 liquidity=5580811.0 spike=0.11
- ELNA.CA: score=9.91 buy_ready=False sector_rank=15 price=37.81 support=35.55 resistance=41.51 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=50.49 liquidity=38641.82 spike=0.1
- ELSH.CA: score=25.88 buy_ready=True sector_rank=15 price=13.75 support=11.1 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT RSI=54.05 liquidity=24536288.0 spike=0.13
- ELWA.CA: score=9.77 buy_ready=False sector_rank=15 price=1.98 support=1.94 resistance=2.22 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=33.33 liquidity=894900.61 spike=0.49
- EMFD.CA: score=23.9 buy_ready=False sector_rank=7 price=11.8 support=11.11 resistance=12.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=45.65 liquidity=16975508.0 spike=0.07
- ENGC.CA: score=6.62 buy_ready=False sector_rank=15 price=39.0 support=37.9 resistance=39.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5747390.0 spike=0.42
- EOSB.CA: score=17.96 buy_ready=False sector_rank=15 price=1.48 support=1.42 resistance=1.55 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=87457.64 spike=0.8
- EPCO.CA: score=13.99 buy_ready=False sector_rank=15 price=9.04 support=8.5 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=36.57 liquidity=1110144.0 spike=0.14
- EPPK.CA: score=1.6 buy_ready=False sector_rank=15 price=14.35 support=14.31 resistance=14.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=723466.56 spike=0.59
- ETEL.CA: score=29.9 buy_ready=True sector_rank=5 price=98.56 support=89.01 resistance=96.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=62.31 liquidity=17987148.0 spike=0.27
- ETRS.CA: score=20.34 buy_ready=True sector_rank=15 price=10.72 support=8.75 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=60.85 liquidity=4463278.5 spike=0.06
- EXPA.CA: score=17.52 buy_ready=False sector_rank=13 price=18.49 support=18.03 resistance=19.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=53.06 liquidity=1623160.38 spike=0.06
- FAIT.CA: score=15.15 buy_ready=False sector_rank=13 price=36.6 support=35.01 resistance=37.7 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=41.05 liquidity=1247986.75 spike=0.59
- FAITA.CA: score=5.92 buy_ready=False sector_rank=13 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:00 AM market time freshness=DELAYED_CURRENT RSI=34.09 liquidity=15728.0 spike=0.38
- FERC.CA: score=8.52 buy_ready=False sector_rank=21 price=74.74 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=39.36 liquidity=528242.25 spike=0.14
- FWRY.CA: score=25.9 buy_ready=False sector_rank=3 price=19.26 support=17.71 resistance=19.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=65.12 liquidity=16054989.0 spike=0.07
- GBCO.CA: score=21.55 buy_ready=False sector_rank=2 price=31.37 support=25.25 resistance=32.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=70.59 liquidity=3653843.75 spike=0.04
- GDWA.CA: score=10.94 buy_ready=False sector_rank=15 price=0.78 support=0.76 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=39.8 liquidity=1063021.5 spike=0.07
- GGCC.CA: score=15.19 buy_ready=False sector_rank=15 price=0.51 support=0.4 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT RSI=99.2 liquidity=1311970.88 spike=0.08
- GIHD.CA: score=18.58 buy_ready=False sector_rank=15 price=44.18 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:30 AM market time freshness=DELAYED_CURRENT RSI=67.14 liquidity=701176.13 spike=0.07
- GMCI.CA: score=1.36 buy_ready=False sector_rank=15 price=2.16 support=2.09 resistance=2.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:37 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=481428.91 spike=0.68
- GRCA.CA: score=9.3 buy_ready=False sector_rank=15 price=51.61 support=50.2 resistance=58.74 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=14.42 liquidity=3060627.87 spike=1.18
- GSSC.CA: score=16.08 buy_ready=False sector_rank=15 price=254.19 support=240.0 resistance=255.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=54.24 liquidity=1203503.38 spike=0.43
- GTWL.CA: score=12.34 buy_ready=False sector_rank=15 price=103.14 support=101.01 resistance=108.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=86743432.0 spike=1.73
- HDBK.CA: score=25.9 buy_ready=True sector_rank=13 price=83.23 support=82.52 resistance=82.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=13254371.0 spike=1.0
- HELI.CA: score=27.9 buy_ready=True sector_rank=7 price=6.72 support=6.28 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=65.18 liquidity=30623064.0 spike=0.28
- HRHO.CA: score=24.9 buy_ready=False sector_rank=11 price=27.0 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=55.08 liquidity=14642057.0 spike=0.11
- ICID.CA: score=26.6 buy_ready=True sector_rank=15 price=7.96 support=5.86 resistance=8.47 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=64.91 liquidity=13252803.06 spike=1.36
- IDRE.CA: score=16.35 buy_ready=False sector_rank=15 price=43.73 support=41.1 resistance=46.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=57.39 liquidity=477302.81 spike=0.04
- IFAP.CA: score=15.32 buy_ready=False sector_rank=17 price=19.53 support=18.47 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=52.05 liquidity=1114510.88 spike=0.21
- INFI.CA: score=12.82 buy_ready=False sector_rank=15 price=95.45 support=88.51 resistance=103.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT RSI=38.98 liquidity=940660.31 spike=0.16
- IRON.CA: score=10.91 buy_ready=False sector_rank=21 price=32.02 support=30.51 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=49.57 liquidity=912985.63 spike=0.11
- ISMA.CA: score=11.09 buy_ready=False sector_rank=15 price=27.0 support=27.6 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT RSI=3.68 liquidity=2218856.5 spike=0.07
- ISMQ.CA: score=21.0 buy_ready=False sector_rank=21 price=9.84 support=7.56 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=78.5 liquidity=12775573.0 spike=0.09
- ISPH.CA: score=20.9 buy_ready=False sector_rank=10 price=11.6 support=11.2 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=38.4 liquidity=10912845.0 spike=0.11
- JUFO.CA: score=20.07 buy_ready=True sector_rank=14 price=31.69 support=28.5 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=45.14 liquidity=4166947.75 spike=0.14
- KABO.CA: score=22.55 buy_ready=False sector_rank=9 price=7.35 support=5.96 resistance=7.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=82.91 liquidity=7648572.0 spike=0.37
- KWIN.CA: score=9.26 buy_ready=False sector_rank=15 price=68.81 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=32.23 liquidity=3380897.25 spike=0.27
- KZPC.CA: score=5.37 buy_ready=False sector_rank=15 price=8.52 support=8.26 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT RSI=10.35 liquidity=492902.72 spike=0.08
- LCSW.CA: score=27.49 buy_ready=True sector_rank=16 price=30.35 support=26.0 resistance=31.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=66.79 liquidity=9762195.0 spike=0.22
- LUTS.CA: score=25.88 buy_ready=True sector_rank=15 price=0.75 support=0.62 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT RSI=45.21 liquidity=14578373.0 spike=0.29
- MAAL.CA: score=16.3 buy_ready=False sector_rank=15 price=7.8 support=5.52 resistance=7.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT RSI=99.49 liquidity=1424098.5 spike=0.09
- MASR.CA: score=27.88 buy_ready=True sector_rank=15 price=7.73 support=6.54 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT RSI=65.62 liquidity=28756962.0 spike=0.4
- MBSC.CA: score=14.31 buy_ready=False sector_rank=16 price=245.15 support=222.66 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=43.21 liquidity=3585064.0 spike=0.13
- MCQE.CA: score=17.37 buy_ready=False sector_rank=16 price=179.11 support=166.66 resistance=194.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=48.41 liquidity=2638954.75 spike=0.19
- MCRO.CA: score=23.65 buy_ready=True sector_rank=15 price=1.25 support=1.17 resistance=1.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=6777969.0 spike=0.22
- MENA.CA: score=3.5 buy_ready=False sector_rank=7 price=7.07 support=7.06 resistance=7.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2599192.0 spike=0.23
- MEPA.CA: score=10.13 buy_ready=False sector_rank=15 price=1.66 support=1.52 resistance=1.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT RSI=34.62 liquidity=2255193.5 spike=0.2
- MFPC.CA: score=21.0 buy_ready=False sector_rank=21 price=36.18 support=34.22 resistance=43.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=37.85 liquidity=15728132.0 spike=0.19
- MFSC.CA: score=16.53 buy_ready=False sector_rank=15 price=48.89 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT RSI=58.28 liquidity=649985.13 spike=0.08
- MHOT.CA: score=20.05 buy_ready=True sector_rank=8 price=17.83 support=17.55 resistance=17.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=4154194.0 spike=1.0
- MICH.CA: score=25.88 buy_ready=True sector_rank=15 price=38.5 support=34.0 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT RSI=56.13 liquidity=13082970.0 spike=0.88
- MILS.CA: score=10.51 buy_ready=False sector_rank=15 price=133.0 support=126.31 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=22.12 liquidity=1632247.63 spike=0.19
- MIPH.CA: score=28.53 buy_ready=True sector_rank=10 price=700.0 support=630.13 resistance=710.0 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=62.83 liquidity=4354700.0 spike=3.14
- MOED.CA: score=16.6 buy_ready=False sector_rank=15 price=0.7 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=49.59 liquidity=2725355.25 spike=0.29
- MOIL.CA: score=17.1 buy_ready=False sector_rank=19 price=0.53 support=0.46 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=71.79 liquidity=226325.81 spike=0.85
- MOIN.CA: score=10.23 buy_ready=False sector_rank=15 price=23.8 support=22.6 resistance=25.3 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=35.86 liquidity=358142.39 spike=0.52
- MOSC.CA: score=13.21 buy_ready=False sector_rank=15 price=273.52 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=45.41 liquidity=333957.0 spike=0.04
- MPCI.CA: score=20.62 buy_ready=True sector_rank=15 price=239.37 support=213.0 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT RSI=66.83 liquidity=4748568.0 spike=0.05
- MPCO.CA: score=17.39 buy_ready=False sector_rank=17 price=1.82 support=1.66 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=26.32 liquidity=9178886.0 spike=0.08
- MPRC.CA: score=24.88 buy_ready=False sector_rank=15 price=40.32 support=31.15 resistance=40.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=90.59 liquidity=14757873.0 spike=0.34
- MTIE.CA: score=25.12 buy_ready=True sector_rank=2 price=9.25 support=8.65 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=64.29 liquidity=3215645.5 spike=0.16
- NAHO.CA: score=17.84 buy_ready=False sector_rank=15 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=62.5 liquidity=64330.24 spike=2.95
- NCCW.CA: score=17.35 buy_ready=False sector_rank=15 price=6.2 support=5.82 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:45 AM market time freshness=DELAYED_CURRENT RSI=45.8 liquidity=3477972.75 spike=0.1
- NEDA.CA: score=11.06 buy_ready=False sector_rank=15 price=2.75 support=2.7 resistance=2.84 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=179146.0 spike=0.79
- NHPS.CA: score=18.34 buy_ready=False sector_rank=15 price=71.11 support=61.55 resistance=75.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT RSI=67.64 liquidity=462748.91 spike=0.03
- NINH.CA: score=13.71 buy_ready=False sector_rank=15 price=17.79 support=16.8 resistance=18.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT RSI=72.07 liquidity=830255.44 spike=0.13
- NIPH.CA: score=25.9 buy_ready=True sector_rank=10 price=175.87 support=157.01 resistance=185.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=65.38 liquidity=15268222.0 spike=0.17
- OBRI.CA: score=20.28 buy_ready=False sector_rank=15 price=35.78 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT RSI=52.31 liquidity=5403406.5 spike=0.21
- OCDI.CA: score=24.9 buy_ready=False sector_rank=7 price=27.0 support=20.0 resistance=27.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=87.46 liquidity=23131644.0 spike=0.26
- OCPH.CA: score=15.33 buy_ready=False sector_rank=15 price=353.17 support=337.0 resistance=374.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=62.22 liquidity=451653.38 spike=0.07
- ODIN.CA: score=20.93 buy_ready=False sector_rank=15 price=2.38 support=2.01 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:36 AM market time freshness=DELAYED_CURRENT RSI=70.83 liquidity=3051832.0 spike=0.22
- OFH.CA: score=21.03 buy_ready=True sector_rank=15 price=0.63 support=0.57 resistance=0.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=58.82 liquidity=3156653.75 spike=0.14
- OIH.CA: score=19.7 buy_ready=False sector_rank=4 price=1.42 support=1.33 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=77.78 liquidity=7798789.5 spike=0.11
- OLFI.CA: score=29.9 buy_ready=True sector_rank=14 price=23.18 support=21.0 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=11273787.0 spike=0.48
- ORAS.CA: score=9.1 buy_ready=False sector_rank=20 price=692.0 support=689.0 resistance=706.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=60056704.0 spike=1.0
- ORHD.CA: score=25.9 buy_ready=True sector_rank=7 price=39.33 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=61.23 liquidity=29132068.0 spike=0.18
- ORWE.CA: score=16.77 buy_ready=False sector_rank=9 price=22.9 support=21.95 resistance=23.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=47.89 liquidity=2871634.25 spike=0.12
- PHAR.CA: score=18.85 buy_ready=False sector_rank=10 price=87.93 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=61.96 liquidity=947075.63 spike=0.04
- PHDC.CA: score=18.9 buy_ready=False sector_rank=7 price=14.78 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=18.28 liquidity=19396506.0 spike=0.06
- PHTV.CA: score=13.52 buy_ready=False sector_rank=15 price=267.05 support=201.55 resistance=277.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=87.94 liquidity=640595.94 spike=0.05
- POUL.CA: score=19.41 buy_ready=True sector_rank=14 price=39.73 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=66.25 liquidity=1506469.13 spike=0.04
- PRCL.CA: score=6.66 buy_ready=False sector_rank=16 price=35.67 support=34.8 resistance=35.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5932692.0 spike=0.13
- PRDC.CA: score=27.9 buy_ready=False sector_rank=7 price=8.5 support=5.91 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=71.58 liquidity=27783664.0 spike=0.2
- PRMH.CA: score=15.14 buy_ready=False sector_rank=15 price=2.6 support=2.34 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=39.19 liquidity=1262274.25 spike=0.04
- RACC.CA: score=23.75 buy_ready=False sector_rank=15 price=10.05 support=9.36 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT RSI=71.11 liquidity=5875403.0 spike=0.72
- RAKT.CA: score=10.66 buy_ready=False sector_rank=15 price=22.75 support=21.4 resistance=23.98 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=51.94 liquidity=328419.0 spike=1.23
- RAYA.CA: score=27.9 buy_ready=False sector_rank=1 price=7.9 support=6.7 resistance=8.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=75.6 liquidity=41891032.0 spike=0.43
- RMDA.CA: score=15.65 buy_ready=False sector_rank=10 price=5.06 support=4.81 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=49.02 liquidity=1749444.5 spike=0.02
- ROTO.CA: score=17.14 buy_ready=False sector_rank=15 price=42.49 support=33.06 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=73.64 liquidity=1262801.5 spike=0.04
- RREI.CA: score=12.68 buy_ready=False sector_rank=15 price=3.86 support=3.73 resistance=3.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:45 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30621402.0 spike=1.9
- RTVC.CA: score=13.38 buy_ready=False sector_rank=15 price=3.75 support=3.55 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=48.53 liquidity=507507.41 spike=0.1
- RUBX.CA: score=24.88 buy_ready=False sector_rank=15 price=13.29 support=9.8 resistance=14.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:45 AM market time freshness=DELAYED_CURRENT RSI=87.66 liquidity=29891742.0 spike=0.65
- SAUD.CA: score=15.84 buy_ready=False sector_rank=13 price=21.54 support=19.99 resistance=22.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=43.89 liquidity=939803.81 spike=0.13
- SCEM.CA: score=19.15 buy_ready=True sector_rank=16 price=63.39 support=59.3 resistance=67.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=58.22 liquidity=1420137.38 spike=0.08
- SCFM.CA: score=13.92 buy_ready=False sector_rank=15 price=249.12 support=226.5 resistance=265.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=37.51 liquidity=1045624.81 spike=0.28
- SCTS.CA: score=18.56 buy_ready=False sector_rank=12 price=619.3 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=60.23 liquidity=659040.94 spike=0.14
- SDTI.CA: score=22.38 buy_ready=True sector_rank=15 price=47.0 support=45.45 resistance=49.5 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=50.42 liquidity=6502779.0 spike=0.96
- SEIG.CA: score=15.88 buy_ready=False sector_rank=15 price=248.95 support=242.0 resistance=259.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:45 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42050764.0 spike=16.27
- SIPC.CA: score=13.6 buy_ready=False sector_rank=15 price=3.51 support=3.25 resistance=3.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=48.39 liquidity=728286.06 spike=0.08
- SKPC.CA: score=20.0 buy_ready=False sector_rank=21 price=16.25 support=15.58 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=43.39 liquidity=13621062.0 spike=0.43
- SMFR.CA: score=26.6 buy_ready=True sector_rank=15 price=204.78 support=187.01 resistance=210.5 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=51.0 liquidity=5719505.37 spike=3.53
- SNFC.CA: score=6.19 buy_ready=False sector_rank=15 price=11.41 support=11.55 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=27.27 liquidity=312840.91 spike=0.03
- SPIN.CA: score=18.76 buy_ready=False sector_rank=9 price=14.65 support=13.3 resistance=14.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=71.97 liquidity=857527.56 spike=0.1
- SPMD.CA: score=26.36 buy_ready=True sector_rank=15 price=0.45 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:45 AM market time freshness=DELAYED_CURRENT RSI=61.19 liquidity=22974842.0 spike=1.24
- SUGR.CA: score=10.73 buy_ready=False sector_rank=14 price=46.97 support=45.31 resistance=50.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=35.46 liquidity=831649.0 spike=0.14
- SVCE.CA: score=23.19 buy_ready=True sector_rank=15 price=9.39 support=8.11 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:45 AM market time freshness=DELAYED_CURRENT RSI=61.34 liquidity=5318979.5 spike=0.07
- SWDY.CA: score=20.18 buy_ready=True sector_rank=18 price=89.44 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=58.77 liquidity=3223750.5 spike=0.24
- TALM.CA: score=12.19 buy_ready=False sector_rank=12 price=15.68 support=15.38 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=35.43 liquidity=1293319.75 spike=0.17
- TMGH.CA: score=29.9 buy_ready=True sector_rank=7 price=98.0 support=92.1 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=59.74 liquidity=36993260.0 spike=0.11
- TRTO.CA: score=11.88 buy_ready=False sector_rank=15 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=20.4 spike=0.04
- UEFM.CA: score=22.44 buy_ready=True sector_rank=15 price=499.45 support=460.0 resistance=505.0 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=65.78 liquidity=2079210.4 spike=2.24
- UEGC.CA: score=20.71 buy_ready=False sector_rank=15 price=1.61 support=1.33 resistance=1.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:45 AM market time freshness=DELAYED_CURRENT RSI=72.34 liquidity=2829552.5 spike=0.1
- UNIP.CA: score=16.31 buy_ready=False sector_rank=15 price=0.33 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=436723.66 spike=0.02
- UNIT.CA: score=5.66 buy_ready=False sector_rank=7 price=17.06 support=17.0 resistance=17.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4762351.5 spike=0.66
- WCDF.CA: score=11.14 buy_ready=False sector_rank=15 price=506.06 support=450.0 resistance=544.99 source=Yahoo Finance as_of=2026-07-05T21:00:00+00:00 freshness=FRESH RSI=48.87 liquidity=265175.44 spike=0.87
- WKOL.CA: score=3.05 buy_ready=False sector_rank=15 price=321.76 support=317.0 resistance=324.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:45 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2174185.0 spike=0.71
- ZEOT.CA: score=17.31 buy_ready=True sector_rank=15 price=11.19 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:45 AM market time freshness=DELAYED_CURRENT RSI=66.93 liquidity=3431079.0 spike=0.09
- ZMID.CA: score=25.9 buy_ready=False sector_rank=7 price=6.77 support=6.03 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=71.03 liquidity=21216710.0 spike=0.1

## Backtesting Lite
- ETEL.CA: 180d return=94.13%, max drawdown=-30.44%, MA20>MA50 days last20=11, as_of=2026-07-05T21:00:00+00:00
- OLFI.CA: 180d return=10.34%, max drawdown=-19.25%, MA20>MA50 days last20=20, as_of=2026-07-05T21:00:00+00:00
- TMGH.CA: 180d return=72.16%, max drawdown=-23.41%, MA20>MA50 days last20=15, as_of=2026-07-05T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- OLFI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Obour Land For Food Industries summary=Obour Land stock breaks through historical resistance barrier, settles at record levels – Analysis; Obour Land records over EGP 721.5m consolidated profits in 9M-24; Obour Land’s consolidated profits leap in H1-24; sales exceed EGP 3.8bn
  - Obour Land stock breaks through historical resistance barrier, settles at record levels – Analysis: https://english.mubasher.info/news/4550021/Obour-Land-stock-breaks-through-historical-resistance-barrier-settles-at-record-levels-Analysis/
  - Obour Land records over EGP 721.5m consolidated profits in 9M-24: https://english.mubasher.info/news/4353735/Obour-Land-records-over-EGP-721-5m-consolidated-profits-in-9M-24/
  - Obour Land’s consolidated profits leap in H1-24; sales exceed EGP 3.8bn: https://english.mubasher.info/news/4317274/Obour-Land-s-consolidated-profits-leap-in-H1-24-sales-exceed-EGP-3-8bn/
- TMGH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talaat Moustafa Group Holding summary=Evidence rejected for TMGH.CA: source text did not clearly match TMGH.CA / Talaat Moustafa Group Holding.
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- MIPH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Minapharm Pharmaceuticals summary=Minapharm’ consolidated net profits retreat to EGP 62m in 9M-25; Minapharm posts EGP 66.5m standalone net profits in 9M-25; sales hit EGP 2.8bn; Investor buys EGP 1.3bn stake in Minapharm Pharmaceuticals
  - Minapharm’ consolidated net profits retreat to EGP 62m in 9M-25: https://english.mubasher.info/news/4531893/Minapharm-consolidated-net-profits-retreat-to-EGP-62m-in-9M-25/
  - Minapharm posts EGP 66.5m standalone net profits in 9M-25; sales hit EGP 2.8bn: https://english.mubasher.info/news/4528557/Minapharm-posts-EGP-66-5m-standalone-net-profits-in-9M-25-sales-hit-EGP-2-8bn/
  - Investor buys EGP 1.3bn stake in Minapharm Pharmaceuticals: https://english.mubasher.info/news/4295954/Investor-buys-EGP-1-3bn-stake-in-Minapharm-Pharmaceuticals/
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- ADIB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Dhabi Islamic Bank Egypt summary=ADIB Egypt’s consolidated profits leap to EGP 3.6bn in Q1-26; ADIB Egypt stock approaches breakout above EGP 41; ADIB Egypt’s stock holds uptrend despite corrections
  - ADIB Egypt’s consolidated profits leap to EGP 3.6bn in Q1-26: https://english.mubasher.info/news/4607278/ADIB-Egypt-s-consolidated-profits-leap-to-EGP-3-6bn-in-Q1-26/
  - ADIB Egypt stock approaches breakout above EGP 41: https://english.mubasher.info/news/4591391/ADIB-Egypt-stock-approaches-breakout-above-EGP-41/
  - ADIB Egypt’s stock holds uptrend despite corrections: https://english.mubasher.info/news/4562331/ADIB-Egypt-s-stock-holds-uptrend-despite-corrections/
- HELI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Heliopolis Housing summary=Evidence rejected for HELI.CA: source text did not clearly match HELI.CA / Heliopolis Housing.

## Warnings
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence for OLFI.CA matches the company but no source/report date was detected.
- Evidence rejected for TMGH.CA: source text did not clearly match TMGH.CA / Talaat Moustafa Group Holding.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence for MIPH.CA matches the company but no source/report date was detected.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence for ADIB.CA matches the company but no source/report date was detected.
- Evidence rejected for HELI.CA: source text did not clearly match HELI.CA / Heliopolis Housing.
