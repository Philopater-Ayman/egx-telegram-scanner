# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-09-01T10:28:52.422785+00:00
Generated Cairo: 2026-09-01 13:28
Run timing: target 08:45 Cairo | generated Cairo 2026-09-01 13:28 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-01 13:25

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 176/189
- Top sector: Investment Holding

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, September 01
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 55.56% / above MA50 77.78%
- EGX70 regime: MIXED / above MA20 45.95% / above MA50 72.97%
- Sector breadth: 19.05%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=668226624.0 spike=1.32 score=22.04
- CCAP.CA: liquidity=567626432.0 spike=0.93 score=23.4
- SVCE.CA: liquidity=478766496.0 spike=4.58 score=27.74
- EMFD.CA: liquidity=311227776.0 spike=2.61 score=8.65
- AMES.CA: liquidity=269188992.0 spike=4.12 score=10.74

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 show mixed trends with weak sector breadth (19%), triggering a defensive risk mode that blocks new BUY signals despite accumulation spikes in several stocks.
- EGX30: 55% above MA20, 78% above MA50, median 5‑day return –0.4%; EGX70: 46% above MA20, 73% above MA50, median 5‑day return –1.0% → mixed short‑term momentum.
- Sector breadth low; only Investment Holding, Textiles, and Transportation & Logistics show strength, leaving most sectors without leadership.
- Top tickets (EBSC.CA, PRDC.CA, SVCE.CA, etc.) display ACCUMULATION_SPIKE liquidity and BULLISH_WATCH outlook, but prices sit near support/resistance or far above support with RSI 42‑70, limiting near‑term upside.
- Risk mode set to DEFENSIVE_NO_NEW_BUY because breadth is too weak; uncertainty remains high and no new BUY is allowed.

## Top Liquidity Spikes
- SVCE.CA: spike=4.58 liquidity=478766496.0 outlook=BULLISH_WATCH score=82.36 buy_ready=False
- ATLC.CA: spike=4.3 liquidity=88314400.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AMES.CA: spike=4.12 liquidity=269188992.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- PRDC.CA: spike=3.69 liquidity=239366080.0 outlook=BULLISH_WATCH score=87.58 buy_ready=False
- EBSC.CA: spike=3.58 liquidity=40546912.0 outlook=BULLISH_WATCH score=94.36 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=12.4 5d=7.45% 20d=12.66% aboveMA50=100.0%
- #2 Textiles: score=12.17 5d=3.0% 20d=22.2% aboveMA50=100.0%
- #3 Transportation & Logistics: score=8.79 5d=-2.52% 20d=10.78% aboveMA50=100.0%
- #4 Industrial Goods & Cables: score=7.84 5d=1.62% 20d=14.11% aboveMA50=50.0%
- #5 Basic Resources & Chemicals: score=7.77 5d=0.79% 20d=4.89% aboveMA50=90.0%
- #6 Banking & Financials: score=6.8 5d=0.0% 20d=4.52% aboveMA50=80.0%
- #7 Tourism & Leisure: score=6.05 5d=1.31% 20d=11.57% aboveMA50=0.0%
- #8 General / Verified EGX Expansion: score=4.36 5d=-0.68% 20d=1.96% aboveMA50=72.82%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ALCN.CA: BULLISH_WATCH score=99.79 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- EBSC.CA: BULLISH_WATCH score=94.36 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CLHO.CA: BULLISH_WATCH score=92.2 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ORWE.CA: BULLISH_WATCH score=89 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- FERC.CA: BULLISH_WATCH score=88.77 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ISMQ.CA: BULLISH_WATCH score=88.77 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- BINV.CA: BULLISH_WATCH score=88 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- PRDC.CA: BULLISH_WATCH score=87.58 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CIEB.CA: BULLISH_WATCH score=83.8 liquidity=TRADEABLE sector=IMPROVING risk=close to resistance
- SKPC.CA: BULLISH_WATCH score=82.77 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; close to resistance

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=15.14 buy_ready=False sector_rank=8 price=304.64 support=266.01 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=54.3 liquidity=6395519.5 spike=0.12
- ABUK.CA: score=23.86 buy_ready=False sector_rank=5 price=83.18 support=72.0 resistance=80.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=74.74 liquidity=130484144.0 spike=1.23
- ACAMD.CA: score=10.74 buy_ready=False sector_rank=8 price=1.99 support=1.95 resistance=2.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=15.38 liquidity=14737112.0 spike=0.26
- ACGC.CA: score=23.4 buy_ready=False sector_rank=2 price=14.19 support=10.36 resistance=14.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=72.69 liquidity=13857369.0 spike=0.33
- ADCI.CA: score=15.84 buy_ready=False sector_rank=8 price=300.46 support=274.0 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=56.21 liquidity=5091516.0 spike=0.24
- ADIB.CA: score=19.6 buy_ready=False sector_rank=6 price=53.41 support=51.02 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=61.1 liquidity=73939640.0 spike=1.1
- ADPC.CA: score=18.74 buy_ready=False sector_rank=8 price=3.92 support=3.85 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=38.02 liquidity=10067121.0 spike=0.23
- AFDI.CA: score=18.74 buy_ready=False sector_rank=8 price=56.34 support=52.56 resistance=69.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=45.26 liquidity=22765764.0 spike=0.68
- AFMC.CA: score=13.74 buy_ready=False sector_rank=8 price=183.76 support=174.84 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=32.64 liquidity=28037588.0 spike=0.19
- AJWA.CA: score=15.74 buy_ready=False sector_rank=8 price=181.0 support=179.1 resistance=204.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=37.98 liquidity=21027158.0 spike=0.33
- ALCN.CA: score=22.54 buy_ready=False sector_rank=3 price=31.0 support=29.74 resistance=32.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=43.54 liquidity=27661542.0 spike=1.07
- ALUM.CA: score=14.12 buy_ready=False sector_rank=8 price=28.82 support=23.0 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=68.4 liquidity=3374271.0 spike=0.12
- AMER.CA: score=18.43 buy_ready=False sector_rank=12 price=5.7 support=4.86 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=48.25 liquidity=71334896.0 spike=0.74
- AMES.CA: score=10.74 buy_ready=False sector_rank=8 price=109.84 support=104.59 resistance=126.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=269188992.0 spike=4.12
- AMIA.CA: score=17.74 buy_ready=False sector_rank=8 price=19.06 support=10.6 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=84.21 liquidity=30196670.0 spike=0.55
- AMOC.CA: score=6.06 buy_ready=False sector_rank=17 price=13.2 support=12.25 resistance=13.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=254723408.0 spike=1.54
- APSW.CA: score=5.33 buy_ready=False sector_rank=8 price=8.52 support=8.41 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=44.97 liquidity=586406.75 spike=0.4
- ARAB.CA: score=22.43 buy_ready=False sector_rank=12 price=0.26 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=60.71 liquidity=46956772.0 spike=0.52
- ARCC.CA: score=19.12 buy_ready=False sector_rank=15 price=79.19 support=55.77 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=79.62 liquidity=49708356.0 spike=0.48
- AREH.CA: score=6.03 buy_ready=False sector_rank=8 price=1.45 support=1.4 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=5281542.0 spike=0.18
- ARVA.CA: score=5.74 buy_ready=False sector_rank=8 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=13.74 buy_ready=False sector_rank=8 price=63.13 support=62.01 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=33.38 liquidity=10752562.0 spike=0.24
- ASPI.CA: score=18.9 buy_ready=False sector_rank=8 price=0.44 support=0.43 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=50.95 liquidity=41023124.0 spike=1.08
- ATLC.CA: score=9.5 buy_ready=False sector_rank=19 price=6.8 support=5.76 resistance=6.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=88314400.0 spike=4.3
- ATQA.CA: score=21.7 buy_ready=False sector_rank=5 price=12.22 support=9.77 resistance=11.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=83.33 liquidity=151410896.0 spike=1.65
- AXPH.CA: score=15.15 buy_ready=False sector_rank=8 price=1714.87 support=1246.92 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=88.66 liquidity=7404966.5 spike=0.6
- BINV.CA: score=22.59 buy_ready=False sector_rank=1 price=50.34 support=46.25 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=64.95 liquidity=6188148.5 spike=0.59
- BIOC.CA: score=13.74 buy_ready=False sector_rank=8 price=328.57 support=265.2 resistance=563.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=21.81 liquidity=102253088.0 spike=0.4
- BTFH.CA: score=8.5 buy_ready=False sector_rank=19 price=3.02 support=2.94 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=99208896.0 spike=0.55
- CAED.CA: score=17.46 buy_ready=False sector_rank=8 price=143.98 support=118.01 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=63.01 liquidity=6719164.5 spike=0.17
- CANA.CA: score=15.11 buy_ready=False sector_rank=6 price=42.5 support=37.9 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=69.26 liquidity=5711471.5 spike=0.33
- CCAP.CA: score=23.4 buy_ready=False sector_rank=1 price=5.99 support=5.18 resistance=6.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=76.92 liquidity=567626432.0 spike=0.93
- CCRS.CA: score=22.74 buy_ready=False sector_rank=8 price=2.7 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=55.73 liquidity=27425228.0 spike=0.56
- CEFM.CA: score=12.49 buy_ready=False sector_rank=8 price=144.97 support=131.03 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=61.34 liquidity=1743982.5 spike=0.06
- CERA.CA: score=10.74 buy_ready=False sector_rank=8 price=1.24 support=1.23 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=30.77 liquidity=10574094.0 spike=0.76
- CFGH.CA: score=9.76 buy_ready=False sector_rank=8 price=0.12 support=0.1 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=79.17 liquidity=15651.4 spike=0.85
- CICH.CA: score=4.56 buy_ready=False sector_rank=19 price=12.33 support=12.0 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=34.27 liquidity=2060146.5 spike=0.31
- CIEB.CA: score=26.14 buy_ready=False sector_rank=6 price=25.32 support=23.95 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=61.39 liquidity=18384986.0 spike=1.37
- CIRA.CA: score=12.01 buy_ready=False sector_rank=20 price=34.0 support=32.1 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=30.91 liquidity=21883080.0 spike=0.59
- CLHO.CA: score=24.34 buy_ready=False sector_rank=9 price=18.3 support=16.95 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=55.38 liquidity=181552720.0 spike=2.83
- CNFN.CA: score=17.5 buy_ready=False sector_rank=19 price=4.89 support=4.73 resistance=5.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=12768823.0 spike=0.68
- COMI.CA: score=22.04 buy_ready=False sector_rank=6 price=139.29 support=135.35 resistance=142.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=37.83 liquidity=668226624.0 spike=1.32
- COPR.CA: score=20.74 buy_ready=False sector_rank=8 price=0.51 support=0.4 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=70.36 liquidity=19492870.0 spike=0.22
- COSG.CA: score=18.74 buy_ready=False sector_rank=8 price=1.88 support=1.67 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=65.12 liquidity=25281748.0 spike=0.5
- CPCI.CA: score=11.5 buy_ready=False sector_rank=8 price=549.75 support=483.0 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=71.99 liquidity=2760296.5 spike=0.32
- CSAG.CA: score=20.66 buy_ready=False sector_rank=3 price=42.59 support=33.4 resistance=43.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=65.22 liquidity=26956830.0 spike=1.13
- DAPH.CA: score=24.6 buy_ready=False sector_rank=8 price=138.92 support=99.02 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=62.95 liquidity=124963888.0 spike=1.93
- DEIN.CA: score=8.74 buy_ready=False sector_rank=8 price=10.35 support=10.35 resistance=10.35 source=Yahoo Finance as_of=2026-08-30T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=11.26 buy_ready=False sector_rank=10 price=28.02 support=26.6 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=44.49 liquidity=2638985.0 spike=0.16
- DSCW.CA: score=13.74 buy_ready=False sector_rank=8 price=1.94 support=1.84 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=33.93 liquidity=23704702.0 spike=0.27
- DTPP.CA: score=15.74 buy_ready=False sector_rank=8 price=305.26 support=240.1 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=75.01 liquidity=13126115.0 spike=0.31
- EALR.CA: score=15.38 buy_ready=False sector_rank=8 price=395.43 support=364.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=54.89 liquidity=4634214.5 spike=0.1
- EASB.CA: score=20.52 buy_ready=False sector_rank=8 price=7.4 support=6.71 resistance=8.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=61.18 liquidity=10126870.0 spike=1.39
- EAST.CA: score=14.62 buy_ready=False sector_rank=10 price=36.04 support=35.0 resistance=37.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=39.18 liquidity=22826544.0 spike=0.28
- EBSC.CA: score=29.74 buy_ready=False sector_rank=8 price=2.22 support=1.88 resistance=2.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=61.84 liquidity=40546912.0 spike=3.58
- ECAP.CA: score=11.44 buy_ready=False sector_rank=8 price=32.81 support=32.05 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=45.49 liquidity=5692368.0 spike=0.36
- EDFM.CA: score=11.89 buy_ready=False sector_rank=8 price=406.99 support=390.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=59.15 liquidity=1143693.5 spike=0.4
- EEII.CA: score=16.74 buy_ready=False sector_rank=8 price=3.03 support=2.64 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=60.48 liquidity=5992807.5 spike=0.21
- EFIC.CA: score=17.64 buy_ready=False sector_rank=5 price=199.0 support=188.01 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=44.49 liquidity=9242840.0 spike=0.18
- EFID.CA: score=18.62 buy_ready=False sector_rank=10 price=30.0 support=27.1 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=41.37 liquidity=50392732.0 spike=0.58
- EFIH.CA: score=18.3 buy_ready=False sector_rank=14 price=22.9 support=22.9 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=44.53 liquidity=40306356.0 spike=0.36
- EGAL.CA: score=18.4 buy_ready=False sector_rank=5 price=362.18 support=292.0 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=79.24 liquidity=66931268.0 spike=0.45
- EGAS.CA: score=13.4 buy_ready=False sector_rank=17 price=58.65 support=52.5 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=49.23 liquidity=5424254.5 spike=0.23
- EGBE.CA: score=9.95 buy_ready=False sector_rank=6 price=0.53 support=0.47 resistance=0.57 source=Yahoo Finance as_of=2026-08-30T21:00:00+00:00 freshness=FRESH RSI=44.22 liquidity=226271.83 spike=1.16
- EGCH.CA: score=21.4 buy_ready=False sector_rank=5 price=14.2 support=13.3 resistance=14.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=46.22 liquidity=105205832.0 spike=0.86
- EGSA.CA: score=7.52 buy_ready=False sector_rank=11 price=8.69 support=8.65 resistance=8.93 source=Yahoo Finance as_of=2026-08-30T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=3684.56 spike=0.55
- EGTS.CA: score=10.72 buy_ready=False sector_rank=12 price=17.16 support=16.17 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=40.82 liquidity=5284641.5 spike=0.15
- EHDR.CA: score=18.74 buy_ready=False sector_rank=8 price=2.91 support=2.73 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=11230685.0 spike=0.33
- EKHO.CA: score=5.98 buy_ready=False sector_rank=17 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-30T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=11.82 buy_ready=False sector_rank=4 price=2.14 support=2.04 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=95568784.0 spike=1.71
- ELKA.CA: score=25.04 buy_ready=False sector_rank=8 price=1.93 support=1.69 resistance=1.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=65.0 liquidity=146402880.0 spike=2.15
- ELNA.CA: score=4.93 buy_ready=False sector_rank=8 price=37.0 support=36.1 resistance=38.44 source=Yahoo Finance as_of=2026-08-30T21:00:00+00:00 freshness=FRESH RSI=42.81 liquidity=187923.0 spike=0.58
- ELSH.CA: score=15.74 buy_ready=False sector_rank=8 price=13.6 support=12.97 resistance=14.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=42.05 liquidity=26224134.0 spike=0.48
- ELWA.CA: score=10.37 buy_ready=False sector_rank=8 price=1.85 support=1.62 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=628962.0 spike=0.26
- EMFD.CA: score=8.65 buy_ready=False sector_rank=12 price=13.7 support=12.95 resistance=13.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=311227776.0 spike=2.61
- ENGC.CA: score=17.79 buy_ready=False sector_rank=8 price=43.2 support=41.99 resistance=54.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=43.78 liquidity=9050612.0 spike=0.34
- EOSB.CA: score=15.15 buy_ready=False sector_rank=8 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-08-30T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=103337.4 spike=2.15
- EPCO.CA: score=11.67 buy_ready=False sector_rank=8 price=11.18 support=10.8 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=47.69 liquidity=2928561.0 spike=0.16
- EPPK.CA: score=0.92 buy_ready=False sector_rank=8 price=11.41 support=12.01 resistance=15.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=32.02 liquidity=1118043.13 spike=1.03
- ETEL.CA: score=20.62 buy_ready=False sector_rank=11 price=113.44 support=107.0 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=63.73 liquidity=145551776.0 spike=1.05
- ETRS.CA: score=20.74 buy_ready=False sector_rank=8 price=11.38 support=10.41 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=62.74 liquidity=22241468.0 spike=0.82
- EXPA.CA: score=21.4 buy_ready=False sector_rank=6 price=21.1 support=19.8 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=56.08 liquidity=28465498.0 spike=0.73
- FAIT.CA: score=20.44 buy_ready=False sector_rank=6 price=43.09 support=36.9 resistance=45.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=67.71 liquidity=8655334.0 spike=1.19
- FAITA.CA: score=8.45 buy_ready=False sector_rank=6 price=0.98 support=0.97 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=49.11 liquidity=51278.51 spike=0.92
- FERC.CA: score=21.4 buy_ready=False sector_rank=5 price=80.06 support=76.16 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=47.31 liquidity=15035284.0 spike=0.84
- FWRY.CA: score=20.3 buy_ready=False sector_rank=14 price=19.1 support=18.66 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=39.46 liquidity=72163680.0 spike=0.49
- GBCO.CA: score=13.75 buy_ready=False sector_rank=21 price=28.7 support=27.51 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=42.3 liquidity=45537412.0 spike=0.94
- GDWA.CA: score=8.28 buy_ready=False sector_rank=8 price=0.87 support=0.81 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=126306568.0 spike=2.27
- GGCC.CA: score=13.74 buy_ready=False sector_rank=8 price=0.84 support=0.85 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=29.64 liquidity=44387680.0 spike=0.86
- GIHD.CA: score=20.74 buy_ready=False sector_rank=8 price=69.94 support=57.82 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=65.41 liquidity=17970016.0 spike=0.7
- GMCI.CA: score=1.73 buy_ready=False sector_rank=8 price=1.87 support=1.83 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=13.33 liquidity=650185.06 spike=1.17
- GRCA.CA: score=20.74 buy_ready=False sector_rank=8 price=79.69 support=54.7 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=71.85 liquidity=46469828.0 spike=0.78
- GSSC.CA: score=14.3 buy_ready=False sector_rank=8 price=279.25 support=274.0 resistance=301.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=52.13 liquidity=5557736.0 spike=0.29
- GTWL.CA: score=17.74 buy_ready=False sector_rank=8 price=229.6 support=85.0 resistance=247.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=80.72 liquidity=96580688.0 spike=0.34
- HDBK.CA: score=7.8 buy_ready=False sector_rank=6 price=114.0 support=102.5 resistance=114.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=80398128.0 spike=1.7
- HELI.CA: score=18.43 buy_ready=False sector_rank=12 price=7.82 support=7.34 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=38.5 liquidity=49226564.0 spike=0.31
- HRHO.CA: score=8.5 buy_ready=False sector_rank=19 price=25.99 support=25.33 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=17.61 liquidity=97495320.0 spike=0.8
- ICID.CA: score=5.74 buy_ready=False sector_rank=8 price=17.62 support=16.65 resistance=18.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20587702.0 spike=0.73
- IDRE.CA: score=19.53 buy_ready=False sector_rank=8 price=55.85 support=48.27 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=51.02 liquidity=8789612.0 spike=0.61
- IFAP.CA: score=18.0 buy_ready=False sector_rank=16 price=20.61 support=19.71 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=44.08 liquidity=18767048.0 spike=0.59
- INFI.CA: score=20.74 buy_ready=False sector_rank=8 price=153.0 support=114.05 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=59.09 liquidity=13497822.0 spike=0.19
- IRON.CA: score=9.04 buy_ready=False sector_rank=5 price=29.96 support=29.82 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=29.84 liquidity=8640416.0 spike=0.68
- ISMA.CA: score=5.74 buy_ready=False sector_rank=8 price=32.96 support=32.43 resistance=37.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22026734.0 spike=0.86
- ISMQ.CA: score=21.4 buy_ready=False sector_rank=5 price=9.38 support=9.0 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=47.92 liquidity=47225356.0 spike=0.98
- ISPH.CA: score=13.68 buy_ready=False sector_rank=9 price=13.0 support=11.83 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=24582844.0 spike=0.13
- JUFO.CA: score=19.62 buy_ready=False sector_rank=10 price=27.18 support=23.44 resistance=28.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=48.1 liquidity=19025920.0 spike=0.36
- KABO.CA: score=18.4 buy_ready=False sector_rank=2 price=9.41 support=7.86 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=75.7 liquidity=16450093.0 spike=0.38
- KWIN.CA: score=20.74 buy_ready=False sector_rank=8 price=111.08 support=84.08 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=65.97 liquidity=66166172.0 spike=1.0
- KZPC.CA: score=20.74 buy_ready=False sector_rank=8 price=13.19 support=8.69 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=74.46 liquidity=26287798.0 spike=0.5
- LCSW.CA: score=20.12 buy_ready=False sector_rank=15 price=34.91 support=32.12 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=54.58 liquidity=10230704.0 spike=0.33
- LUTS.CA: score=20.74 buy_ready=False sector_rank=8 price=1.09 support=0.59 resistance=1.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=54.54 liquidity=199306000.0 spike=0.8
- MAAL.CA: score=21.96 buy_ready=False sector_rank=8 price=9.4 support=8.32 resistance=9.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=53.88 liquidity=20388198.0 spike=1.61
- MASR.CA: score=15.74 buy_ready=False sector_rank=8 price=7.73 support=7.45 resistance=8.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=39.34 liquidity=29354010.0 spike=0.46
- MBSC.CA: score=5.56 buy_ready=False sector_rank=15 price=449.6 support=405.0 resistance=449.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=103828112.0 spike=1.22
- MCQE.CA: score=5.12 buy_ready=False sector_rank=15 price=246.96 support=234.1 resistance=247.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30744490.0 spike=0.52
- MCRO.CA: score=20.74 buy_ready=False sector_rank=8 price=1.53 support=1.44 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=52.78 liquidity=54022812.0 spike=0.43
- MENA.CA: score=6.25 buy_ready=False sector_rank=12 price=6.88 support=6.59 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=49.59 liquidity=814425.13 spike=0.14
- MEPA.CA: score=20.74 buy_ready=False sector_rank=8 price=1.97 support=1.8 resistance=2.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=53.06 liquidity=25218956.0 spike=0.82
- MFPC.CA: score=21.6 buy_ready=False sector_rank=5 price=42.69 support=36.81 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=79.68 liquidity=141734592.0 spike=1.6
- MFSC.CA: score=10.22 buy_ready=False sector_rank=8 price=49.75 support=47.47 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=42.27 liquidity=1473790.63 spike=0.13
- MHOT.CA: score=12.05 buy_ready=False sector_rank=7 price=18.64 support=16.81 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=60.66 liquidity=2648191.0 spike=0.14
- MICH.CA: score=22.74 buy_ready=False sector_rank=8 price=50.63 support=42.15 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=54.95 liquidity=12940516.0 spike=0.31
- MILS.CA: score=18.74 buy_ready=False sector_rank=8 price=205.0 support=175.0 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=54.88 liquidity=13072247.0 spike=0.16
- MIPH.CA: score=13.59 buy_ready=False sector_rank=9 price=792.58 support=745.0 resistance=828.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=57.28 liquidity=2914414.0 spike=0.61
- MOED.CA: score=19.74 buy_ready=False sector_rank=8 price=0.87 support=0.66 resistance=0.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=78.47 liquidity=82311248.0 spike=0.81
- MOIL.CA: score=9.99 buy_ready=False sector_rank=17 price=0.69 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=54.41 liquidity=12089.12 spike=0.03
- MOIN.CA: score=16.86 buy_ready=False sector_rank=8 price=33.3 support=24.0 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=8116675.5 spike=0.24
- MOSC.CA: score=14.93 buy_ready=False sector_rank=8 price=316.92 support=290.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=59.86 liquidity=4188680.5 spike=0.26
- MPCI.CA: score=19.74 buy_ready=False sector_rank=8 price=446.42 support=293.06 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=77.21 liquidity=111949016.0 spike=0.59
- MPCO.CA: score=18.0 buy_ready=False sector_rank=16 price=2.12 support=1.91 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=56.7 liquidity=42558716.0 spike=0.34
- MPRC.CA: score=18.74 buy_ready=False sector_rank=8 price=43.83 support=39.5 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=45.79 liquidity=20132612.0 spike=0.58
- MTIE.CA: score=13.75 buy_ready=False sector_rank=21 price=8.56 support=8.25 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=38.7 liquidity=20655422.0 spike=0.31
- NAHO.CA: score=7.76 buy_ready=False sector_rank=8 price=0.14 support=0.1 resistance=0.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=84.48 liquidity=18813.82 spike=0.19
- NCCW.CA: score=12.74 buy_ready=False sector_rank=8 price=6.08 support=5.59 resistance=7.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=34.16 liquidity=10091421.0 spike=0.4
- NEDA.CA: score=6.06 buy_ready=False sector_rank=8 price=2.73 support=2.7 resistance=2.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=52.86 liquidity=312546.28 spike=0.37
- NHPS.CA: score=19.94 buy_ready=False sector_rank=8 price=89.19 support=82.5 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=57.81 liquidity=9193569.0 spike=0.28
- NINH.CA: score=22.74 buy_ready=False sector_rank=8 price=23.83 support=21.53 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=52.78 liquidity=12040647.0 spike=0.28
- NIPH.CA: score=13.68 buy_ready=False sector_rank=9 price=344.76 support=237.15 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=33.34 liquidity=70825048.0 spike=0.2
- OBRI.CA: score=21.74 buy_ready=False sector_rank=8 price=34.09 support=31.61 resistance=34.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=59.17 liquidity=25736004.0 spike=0.88
- OCDI.CA: score=18.43 buy_ready=False sector_rank=12 price=30.9 support=28.82 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=52.16 liquidity=39534564.0 spike=0.29
- OCPH.CA: score=9.19 buy_ready=False sector_rank=8 price=252.13 support=235.0 resistance=341.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=54.12 liquidity=2443543.0 spike=0.11
- ODIN.CA: score=18.74 buy_ready=False sector_rank=8 price=3.02 support=2.87 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=52.84 liquidity=12814124.0 spike=0.26
- OFH.CA: score=17.74 buy_ready=False sector_rank=8 price=1.04 support=0.71 resistance=1.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=76.94 liquidity=48601640.0 spike=0.45
- OIH.CA: score=21.4 buy_ready=False sector_rank=1 price=2.05 support=1.48 resistance=2.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=76.06 liquidity=91257560.0 spike=0.58
- OLFI.CA: score=15.62 buy_ready=False sector_rank=10 price=22.15 support=22.53 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=35.74 liquidity=34628368.0 spike=0.61
- ORAS.CA: score=4.6 buy_ready=False sector_rank=18 price=841.42 support=830.3 resistance=859.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=86289832.0 spike=1.0
- ORHD.CA: score=18.43 buy_ready=False sector_rank=12 price=41.75 support=39.7 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=45.97 liquidity=52760360.0 spike=0.37
- ORWE.CA: score=23.4 buy_ready=False sector_rank=2 price=26.8 support=22.86 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=47.61 liquidity=64196832.0 spike=0.81
- PHAR.CA: score=18.68 buy_ready=False sector_rank=9 price=128.5 support=127.27 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=49.77 liquidity=77181592.0 spike=0.16
- PHDC.CA: score=15.43 buy_ready=False sector_rank=12 price=14.75 support=14.5 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=36.63 liquidity=157989728.0 spike=0.67
- PHTV.CA: score=9.63 buy_ready=False sector_rank=8 price=333.02 support=311.27 resistance=447.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=49.78 liquidity=883379.25 spike=0.34
- POUL.CA: score=22.62 buy_ready=False sector_rank=10 price=39.52 support=36.6 resistance=40.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=56.07 liquidity=12393937.0 spike=0.52
- PRCL.CA: score=15.14 buy_ready=False sector_rank=15 price=30.99 support=31.0 resistance=37.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=35.81 liquidity=23049918.0 spike=1.01
- PRDC.CA: score=29.43 buy_ready=False sector_rank=12 price=9.99 support=8.7 resistance=9.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=61.13 liquidity=239366080.0 spike=3.69
- PRMH.CA: score=17.06 buy_ready=False sector_rank=8 price=2.69 support=2.28 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=44.55 liquidity=6319248.5 spike=0.42
- RACC.CA: score=10.62 buy_ready=False sector_rank=8 price=9.63 support=9.4 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=28.08 liquidity=9875472.0 spike=0.49
- RAKT.CA: score=0.06 buy_ready=False sector_rank=8 price=22.19 support=21.4 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=25.71 liquidity=313007.53 spike=0.9
- RAYA.CA: score=19.38 buy_ready=False sector_rank=13 price=7.28 support=6.95 resistance=7.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=43.66 liquidity=12727831.0 spike=0.19
- RMDA.CA: score=18.68 buy_ready=False sector_rank=9 price=5.94 support=5.6 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=41.04 liquidity=85192840.0 spike=0.72
- ROTO.CA: score=13.43 buy_ready=False sector_rank=8 price=44.03 support=43.7 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=41.23 liquidity=7688148.5 spike=0.36
- RREI.CA: score=14.06 buy_ready=False sector_rank=8 price=4.41 support=4.24 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=43.93 liquidity=5317078.0 spike=0.09
- RTVC.CA: score=15.37 buy_ready=False sector_rank=8 price=4.18 support=3.73 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=66.99 liquidity=4628648.0 spike=0.55
- RUBX.CA: score=18.46 buy_ready=False sector_rank=8 price=12.99 support=12.2 resistance=13.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=55.01 liquidity=5719788.0 spike=0.32
- SAUD.CA: score=21.52 buy_ready=False sector_rank=6 price=23.99 support=21.61 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=56.27 liquidity=21285262.0 spike=1.06
- SCEM.CA: score=5.12 buy_ready=False sector_rank=15 price=102.77 support=97.22 resistance=102.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=115133432.0 spike=0.53
- SCFM.CA: score=11.38 buy_ready=False sector_rank=8 price=282.42 support=273.1 resistance=305.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=52.88 liquidity=2631680.0 spike=0.13
- SCTS.CA: score=11.04 buy_ready=False sector_rank=20 price=617.27 support=603.13 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=61.28 liquidity=2025172.5 spike=0.23
- SDTI.CA: score=13.61 buy_ready=False sector_rank=8 price=68.99 support=59.5 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=54.64 liquidity=4866327.5 spike=0.16
- SEIG.CA: score=10.31 buy_ready=False sector_rank=8 price=260.25 support=252.0 resistance=295.0 source=Yahoo Finance as_of=2026-08-30T21:00:00+00:00 freshness=FRESH RSI=44.21 liquidity=1569047.25 spike=0.34
- SIPC.CA: score=20.74 buy_ready=False sector_rank=8 price=4.97 support=4.1 resistance=5.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=55.05 liquidity=10683545.0 spike=0.19
- SKPC.CA: score=24.52 buy_ready=False sector_rank=5 price=17.89 support=15.71 resistance=18.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=69.93 liquidity=118311424.0 spike=1.56
- SMFR.CA: score=6.43 buy_ready=False sector_rank=8 price=257.53 support=228.88 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=27.65 liquidity=2688078.75 spike=0.1
- SNFC.CA: score=3.9 buy_ready=False sector_rank=8 price=10.37 support=10.3 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=30.16 liquidity=4159775.0 spike=0.29
- SPIN.CA: score=21.27 buy_ready=False sector_rank=2 price=19.48 support=15.32 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=70.14 liquidity=7871269.0 spike=0.19
- SPMD.CA: score=7.02 buy_ready=False sector_rank=8 price=0.45 support=0.45 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=27.27 liquidity=6273391.0 spike=0.31
- SUGR.CA: score=20.62 buy_ready=False sector_rank=10 price=56.5 support=46.53 resistance=61.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=70.97 liquidity=17481270.0 spike=0.31
- SVCE.CA: score=27.74 buy_ready=False sector_rank=8 price=11.29 support=9.11 resistance=12.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=42.15 liquidity=478766496.0 spike=4.58
- SWDY.CA: score=21.4 buy_ready=False sector_rank=4 price=124.94 support=95.48 resistance=133.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=68.98 liquidity=12309132.0 spike=0.12
- TALM.CA: score=12.57 buy_ready=False sector_rank=20 price=18.07 support=17.11 resistance=20.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=46.52 liquidity=5561676.5 spike=0.12
- TMGH.CA: score=15.43 buy_ready=False sector_rank=12 price=96.79 support=94.9 resistance=99.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=40.62 liquidity=170198016.0 spike=0.65
- TRTO.CA: score=18.0 buy_ready=False sector_rank=8 price=0.05 support=0.03 resistance=0.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=31997.24 spike=2.61
- UEFM.CA: score=9.49 buy_ready=False sector_rank=8 price=536.24 support=531.0 resistance=589.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=45.27 liquidity=750358.88 spike=0.16
- UEGC.CA: score=12.18 buy_ready=False sector_rank=8 price=1.77 support=1.8 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=22.76 liquidity=74441272.0 spike=1.72
- UNIP.CA: score=18.74 buy_ready=False sector_rank=8 price=0.38 support=0.35 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=38.6 liquidity=10308393.0 spike=0.31
- UNIT.CA: score=9.27 buy_ready=False sector_rank=12 price=18.59 support=17.8 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=55.19 liquidity=842065.0 spike=0.07
- WCDF.CA: score=7.05 buy_ready=False sector_rank=8 price=640.48 support=580.05 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=78.05 liquidity=1301025.0 spike=0.33
- WKOL.CA: score=16.48 buy_ready=False sector_rank=8 price=345.02 support=315.0 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=58.19 liquidity=3740519.5 spike=0.11
- ZEOT.CA: score=12.45 buy_ready=False sector_rank=8 price=13.84 support=12.2 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=65.9 liquidity=3706779.5 spike=0.16
- ZMID.CA: score=19.43 buy_ready=False sector_rank=12 price=9.2 support=7.06 resistance=9.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=78.11 liquidity=186239600.0 spike=0.73

## Backtesting Lite
- EBSC.CA: 180d return=30.72%, max drawdown=-23.41%, MA20>MA50 days last20=20, as_of=2026-08-30T21:00:00+00:00
- PRDC.CA: 180d return=133.17%, max drawdown=-14.02%, MA20>MA50 days last20=20, as_of=2026-08-30T21:00:00+00:00
- SVCE.CA: 180d return=35.7%, max drawdown=-36.32%, MA20>MA50 days last20=20, as_of=2026-08-30T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- EBSC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Osool ESB Securities Brokerage summary=Evidence rejected for EBSC.CA: source text did not clearly match EBSC.CA / Osool ESB Securities Brokerage.
- PRDC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Pioneers Properties For Urban Development summary=Evidence rejected for PRDC.CA: source text did not clearly match PRDC.CA / Pioneers Properties For Urban Development.
- SVCE.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=South Valley Cement Company summary=South Valley Cement unveils details of rights issue; FRA grants initial approval for South Valley’s rights issue; South Valley Cement unveils EGP 2.4bn capital hike to expand production
  - South Valley Cement unveils details of rights issue: https://english.mubasher.info/news/4601989/South-Valley-Cement-unveils-details-of-rights-issue/
  - FRA grants initial approval for South Valley’s rights issue: https://english.mubasher.info/news/4593737/FRA-grants-initial-approval-for-South-Valley-s-rights-issue/
  - South Valley Cement unveils EGP 2.4bn capital hike to expand production: https://english.mubasher.info/news/4552043/South-Valley-Cement-unveils-EGP-2-4bn-capital-hike-to-expand-production/
- CIEB.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Credit Agricole Egypt summary=Evidence rejected for CIEB.CA: source text did not clearly match CIEB.CA / Credit Agricole Egypt.
- ELKA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=608 sources=3 expected=Cairo for Housing and Development Company (S.A.E) summary=Cairo for Housing’s consolidated profits near EGP 599m in 2025; Cairo Housing stock tests important demand zone; Cairo Housing unveils EGP 398m capital hike via H1-25’s share premium
  - Cairo for Housing’s consolidated profits near EGP 599m in 2025: https://english.mubasher.info/news/4579798/Cairo-for-Housing-s-consolidated-profits-near-EGP-599m-in-2025/
  - Cairo Housing stock tests important demand zone: https://english.mubasher.info/news/4547365/Cairo-Housing-stock-tests-important-demand-zone/
  - Cairo Housing unveils EGP 398m capital hike via H1-25’s share premium: https://english.mubasher.info/news/4540047/Cairo-Housing-unveils-EGP-398m-capital-hike-via-H1-25-s-share-premium/
- DAPH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Development & Engineering Consultants summary=Evidence rejected for DAPH.CA: source text did not clearly match DAPH.CA / Development & Engineering Consultants.
- SKPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Sidi Kerir Petrochemicals summary=Evidence rejected for SKPC.CA: source text did not clearly match SKPC.CA / Sidi Kerir Petrochemicals.
- CLHO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=608 sources=3 expected=Cleopatra Hospital Group summary=Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025; Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn; Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo
  - Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025: https://english.mubasher.info/news/4594702/Cleopatra-Hospitals-unveils-EGP-84m-dividends-to-employee-for-2025/
  - Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn: https://english.mubasher.info/news/4579844/Cleopatra-Hospitals-posts-higher-consolidated-profits-in-2025-revenues-cross-EGP-7-2bn/
  - Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo: https://english.mubasher.info/news/4553462/Cleopatra-Hospitals-launches-EGP-3-5bn-Sky-hospital-in-East-Cairo/

## Warnings
- Evidence rejected for EBSC.CA: source text did not clearly match EBSC.CA / Osool ESB Securities Brokerage.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for PRDC.CA: source text did not clearly match PRDC.CA / Pioneers Properties For Urban Development.
- Evidence for SVCE.CA matches the company but no source/report date was detected.
- Evidence rejected for CIEB.CA: source text did not clearly match CIEB.CA / Credit Agricole Egypt.
- Evidence for ELKA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for DAPH.CA: source text did not clearly match DAPH.CA / Development & Engineering Consultants.
- Evidence rejected for SKPC.CA: source text did not clearly match SKPC.CA / Sidi Kerir Petrochemicals.
- Evidence for CLHO.CA matches the company but appears old; latest detected date is 2025-01-01.
