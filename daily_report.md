# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-07-16T07:41:06.314166+00:00
Generated Cairo: 2026-07-16 10:41
Run timing: target 08:45 Cairo | generated Cairo 2026-07-16 10:41 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-07-16 10:38

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 159/189
- Top sector: Technology & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, July 16
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 65.0% / above MA50 45.0%
- EGX70 regime: MIXED / above MA20 77.78% / above MA50 75.0%
- Sector breadth: 33.33%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- TMGH.CA: liquidity=172939648.0 spike=0.5 score=23.04
- PHDC.CA: liquidity=108113872.0 spike=0.35 score=16.04
- BTFH.CA: liquidity=81317656.0 spike=0.42 score=22.62
- OFH.CA: liquidity=80063176.0 spike=3.38 score=10.6
- ARAB.CA: liquidity=76725216.0 spike=0.83 score=20.04

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner holds all tickets because EGX30/EGX70 show mixed trends, sector breadth is weak (33%), and risk mode is defensive (no new buys); top-ranked stocks display accumulation spikes and bullish watch outlooks but liquidity is cooling and they sit outside leading sectors, so near‑term price action remains uncertain.
- Tickets were prioritized by high rank_score and accumulation‑spike liquidity regimes, with outlooks labeled BULLISH_WATCH or CONSTRUCTIVE despite cooling liquidity spikes.
- Liquidity spikes suggest short‑term buying interest, but cooling liquidity and small support/resistance distances (≈5‑18%) imply price may test these levels within the next 1‑3 days with limited follow‑through.
- Most tickets lie outside the leading sectors (Technology & Distribution, Automotive & Distribution, Textiles), reducing sector‑based confidence and reinforcing the defensive stance.
- EGX30 trend is mixed with weak MA50 breadth; EGX70 shows a negative 5‑day return; together they shift risk mode to DEFENSIVE_NO_NEW_BUY, adding uncertainty to any short‑term bullish bias.

## Top Liquidity Spikes
- BIOC.CA: spike=7.86 liquidity=25824804.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- NINH.CA: spike=6.71 liquidity=66846892.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SIPC.CA: spike=5.03 liquidity=35303140.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CAED.CA: spike=4.8 liquidity=54463676.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CFGH.CA: spike=4.73 liquidity=37753.57 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Technology & Distribution: score=9.73 5d=0.99% 20d=16.14% aboveMA50=100.0%
- #2 Automotive & Distribution: score=8.57 5d=2.21% 20d=7.8% aboveMA50=100.0%
- #3 Textiles: score=7.81 5d=1.67% 20d=4.98% aboveMA50=100.0%
- #4 Energy & Petrochemicals: score=7.65 5d=5.07% 20d=5.05% aboveMA50=75.0%
- #5 Telecommunications: score=7.55 5d=-0.07% 20d=3.37% aboveMA50=100.0%
- #6 Transportation & Logistics: score=6.82 5d=0.32% 20d=2.7% aboveMA50=100.0%
- #7 Investment Holding: score=5.83 5d=0.0% 20d=3.65% aboveMA50=66.67%
- #8 Agriculture & Food Production: score=5.79 5d=2.68% 20d=-2.04% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ORWE.CA: BULLISH_WATCH score=87.81 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- GBCO.CA: BULLISH_WATCH score=82.57 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- BINV.CA: BULLISH_WATCH score=81.83 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- RAYA.CA: BULLISH_WATCH score=81.73 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- ELWA.CA: BULLISH_WATCH score=80.59 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- MTIE.CA: BULLISH_WATCH score=80.57 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- ETEL.CA: BULLISH_WATCH score=77.55 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MPCO.CA: BULLISH_WATCH score=76.79 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- EMFD.CA: BULLISH_WATCH score=76.09 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- MENA.CA: BULLISH_WATCH score=76.09 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=13.66 buy_ready=False sector_rank=11 price=232.74 support=196.0 resistance=247.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:21 AM market time freshness=DELAYED_CURRENT RSI=63.12 liquidity=823195.94 spike=0.06
- ABUK.CA: score=19.67 buy_ready=False sector_rank=13 price=72.04 support=66.66 resistance=73.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=65.59 liquidity=19895922.0 spike=0.12
- ACAMD.CA: score=14.66 buy_ready=False sector_rank=11 price=2.32 support=2.14 resistance=2.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=54.29 liquidity=3827362.75 spike=0.04
- ACGC.CA: score=16.52 buy_ready=False sector_rank=3 price=10.01 support=8.92 resistance=10.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=63.37 liquidity=2120780.0 spike=0.1
- ADCI.CA: score=11.6 buy_ready=False sector_rank=11 price=239.43 support=223.15 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=41.79 liquidity=768210.5 spike=0.07
- ADIB.CA: score=14.05 buy_ready=False sector_rank=16 price=46.46 support=44.1 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=53.63 liquidity=6982890.5 spike=0.07
- ADPC.CA: score=15.83 buy_ready=False sector_rank=11 price=3.87 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=57.47 liquidity=2990649.25 spike=0.14
- AFDI.CA: score=15.41 buy_ready=False sector_rank=11 price=47.9 support=41.84 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=51.25 liquidity=2577514.75 spike=0.19
- AFMC.CA: score=14.62 buy_ready=False sector_rank=11 price=76.48 support=66.0 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=60.05 liquidity=1788679.0 spike=0.46
- AJWA.CA: score=9.73 buy_ready=False sector_rank=11 price=177.32 support=172.1 resistance=192.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=52.08 liquidity=898785.56 spike=0.05
- ALCN.CA: score=14.06 buy_ready=False sector_rank=6 price=29.78 support=27.7 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=65.35 liquidity=2656167.0 spike=0.14
- ALUM.CA: score=10.24 buy_ready=False sector_rank=11 price=23.13 support=20.55 resistance=23.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=48.19 liquidity=401216.28 spike=0.07
- AMER.CA: score=6.04 buy_ready=False sector_rank=10 price=3.65 support=3.58 resistance=3.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=38291700.0 spike=0.49
- AMES.CA: score=19.84 buy_ready=False sector_rank=11 price=125.37 support=45.15 resistance=120.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=89.2 liquidity=28104862.0 spike=0.44
- AMIA.CA: score=12.6 buy_ready=False sector_rank=11 price=9.16 support=8.4 resistance=9.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT RSI=53.85 liquidity=1764688.5 spike=0.21
- AMOC.CA: score=20.78 buy_ready=False sector_rank=4 price=8.19 support=7.42 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=70.95 liquidity=7382788.0 spike=0.13
- APSW.CA: score=7.43 buy_ready=False sector_rank=11 price=8.45 support=8.0 resistance=8.73 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=45.67 liquidity=591728.14 spike=0.75
- ARAB.CA: score=20.04 buy_ready=False sector_rank=10 price=0.26 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=80.56 liquidity=76725216.0 spike=0.83
- ARCC.CA: score=6.24 buy_ready=False sector_rank=20 price=54.31 support=53.0 resistance=56.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=47.2 liquidity=2095817.25 spike=0.11
- AREH.CA: score=4.2 buy_ready=False sector_rank=11 price=1.58 support=1.56 resistance=1.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8368605.5 spike=0.24
- ARVA.CA: score=10.64 buy_ready=False sector_rank=11 price=10.93 support=10.5 resistance=12.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=38.99 liquidity=1801132.63 spike=0.09
- ASCM.CA: score=19.16 buy_ready=False sector_rank=11 price=62.58 support=56.29 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=46.48 liquidity=8321890.5 spike=0.11
- ASPI.CA: score=11.19 buy_ready=False sector_rank=11 price=0.32 support=0.3 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=2355015.75 spike=0.1
- ATLC.CA: score=9.4 buy_ready=False sector_rank=14 price=5.2 support=4.92 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:17 AM market time freshness=DELAYED_CURRENT RSI=54.31 liquidity=782355.13 spike=0.11
- ATQA.CA: score=8.57 buy_ready=False sector_rank=13 price=9.51 support=9.21 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=59.29 liquidity=1899228.13 spike=0.06
- AXPH.CA: score=16.53 buy_ready=False sector_rank=11 price=1207.82 support=1073.0 resistance=1342.9 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=64.09 liquidity=3478521.45 spike=1.11
- BINV.CA: score=13.94 buy_ready=False sector_rank=7 price=48.34 support=45.01 resistance=51.38 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=54.25 liquidity=2605961.07 spike=0.53
- BIOC.CA: score=10.84 buy_ready=False sector_rank=11 price=105.7 support=97.25 resistance=105.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25824804.0 spike=7.86
- BTFH.CA: score=22.62 buy_ready=False sector_rank=14 price=3.1 support=2.91 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=51.43 liquidity=81317656.0 spike=0.42
- CAED.CA: score=10.84 buy_ready=False sector_rank=11 price=106.09 support=102.0 resistance=117.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=54463676.0 spike=4.8
- CANA.CA: score=7.76 buy_ready=False sector_rank=16 price=36.18 support=34.7 resistance=38.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=40.96 liquidity=687398.56 spike=0.07
- CCAP.CA: score=23.33 buy_ready=False sector_rank=7 price=5.39 support=4.65 resistance=5.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=66.94 liquidity=34875812.0 spike=0.05
- CCRS.CA: score=13.55 buy_ready=False sector_rank=11 price=2.55 support=2.18 resistance=2.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT RSI=56.76 liquidity=714573.81 spike=0.05
- CEFM.CA: score=-3.66 buy_ready=False sector_rank=11 price=109.98 support=107.25 resistance=110.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=500789.28 spike=0.23
- CERA.CA: score=2.74 buy_ready=False sector_rank=11 price=1.4 support=1.38 resistance=1.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6900243.0 spike=0.33
- CFGH.CA: score=0.87 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=15 July 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37753.57 spike=4.73
- CICH.CA: score=11.56 buy_ready=False sector_rank=14 price=12.07 support=11.45 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:19 AM market time freshness=DELAYED_CURRENT RSI=47.95 liquidity=940174.0 spike=0.23
- CIEB.CA: score=12.71 buy_ready=False sector_rank=16 price=24.31 support=23.3 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=50.52 liquidity=641191.56 spike=0.1
- CIRA.CA: score=17.54 buy_ready=False sector_rank=9 price=32.98 support=26.0 resistance=32.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=71.78 liquidity=4227822.0 spike=0.15
- CLHO.CA: score=20.32 buy_ready=False sector_rank=15 price=16.94 support=15.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=47.18 liquidity=16402305.0 spike=0.42
- CNFN.CA: score=15.24 buy_ready=False sector_rank=14 price=4.97 support=4.4 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=35.8 liquidity=2623497.25 spike=0.06
- COMI.CA: score=22.07 buy_ready=False sector_rank=16 price=135.42 support=126.21 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=52.61 liquidity=10003641.0 spike=0.02
- COPR.CA: score=13.67 buy_ready=False sector_rank=11 price=0.38 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=64.58 liquidity=3833037.0 spike=0.17
- COSG.CA: score=17.97 buy_ready=False sector_rank=11 price=1.68 support=1.47 resistance=1.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=5129981.5 spike=0.12
- CPCI.CA: score=-1.41 buy_ready=False sector_rank=11 price=468.52 support=465.0 resistance=488.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2749793.0 spike=0.48
- CSAG.CA: score=10.41 buy_ready=False sector_rank=6 price=32.9 support=30.87 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=67.16 liquidity=1012324.0 spike=0.06
- DAPH.CA: score=-1.01 buy_ready=False sector_rank=11 price=86.97 support=86.01 resistance=87.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3152491.25 spike=0.36
- DEIN.CA: score=-4.16 buy_ready=False sector_rank=11 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=11.06 buy_ready=False sector_rank=19 price=26.82 support=24.26 resistance=27.83 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=38.95 liquidity=1495724.56 spike=0.32
- DSCW.CA: score=16.81 buy_ready=False sector_rank=11 price=1.87 support=1.71 resistance=1.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=4969343.0 spike=0.15
- DTPP.CA: score=17.43 buy_ready=False sector_rank=11 price=206.75 support=114.67 resistance=234.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=84.84 liquidity=9594782.0 spike=0.24
- EALR.CA: score=14.84 buy_ready=False sector_rank=11 price=369.94 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=54.11 liquidity=2006818.75 spike=0.17
- EASB.CA: score=15.82 buy_ready=False sector_rank=11 price=7.08 support=5.9 resistance=10.17 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=43.73 liquidity=6985262.44 spike=0.43
- EAST.CA: score=-0.11 buy_ready=False sector_rank=19 price=36.5 support=36.33 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=34.03 liquidity=1326648.13 spike=0.03
- EBSC.CA: score=11.23 buy_ready=False sector_rank=11 price=1.91 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT RSI=54.05 liquidity=396138.72 spike=0.06
- ECAP.CA: score=12.64 buy_ready=False sector_rank=11 price=32.7 support=31.3 resistance=34.79 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=48.09 liquidity=3807686.19 spike=0.48
- EDFM.CA: score=10.71 buy_ready=False sector_rank=11 price=365.0 support=310.2 resistance=363.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT RSI=76.81 liquidity=875108.94 spike=0.93
- EEII.CA: score=12.21 buy_ready=False sector_rank=11 price=2.76 support=2.35 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:20 AM market time freshness=DELAYED_CURRENT RSI=67.78 liquidity=1378606.75 spike=0.07
- EFIC.CA: score=7.46 buy_ready=False sector_rank=13 price=187.11 support=180.02 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:21 AM market time freshness=DELAYED_CURRENT RSI=45.66 liquidity=791872.56 spike=0.13
- EFID.CA: score=7.65 buy_ready=False sector_rank=19 price=27.79 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT RSI=53.6 liquidity=1087308.5 spike=0.02
- EFIH.CA: score=13.6 buy_ready=False sector_rank=17 price=21.97 support=20.0 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:21 AM market time freshness=DELAYED_CURRENT RSI=58.35 liquidity=1977217.75 spike=0.04
- EGAL.CA: score=19.85 buy_ready=False sector_rank=13 price=301.11 support=272.28 resistance=303.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=60.9 liquidity=8183093.5 spike=0.18
- EGAS.CA: score=13.72 buy_ready=False sector_rank=4 price=52.44 support=46.51 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT RSI=57.16 liquidity=320931.78 spike=0.03
- EGBE.CA: score=7.16 buy_ready=False sector_rank=16 price=0.44 support=-0.34 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=15 July 01:14 PM market time freshness=DELAYED_CURRENT RSI=96.16 liquidity=91105.88 spike=-2.19
- EGCH.CA: score=12.18 buy_ready=False sector_rank=13 price=13.41 support=12.13 resistance=13.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT RSI=63.16 liquidity=2512386.25 spike=0.05
- EGSA.CA: score=11.73 buy_ready=False sector_rank=5 price=8.97 support=8.67 resistance=9.13 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=70.21 liquidity=5812.56 spike=1.16
- EGTS.CA: score=6.04 buy_ready=False sector_rank=10 price=19.5 support=19.16 resistance=19.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15017440.0 spike=0.29
- EHDR.CA: score=15.69 buy_ready=False sector_rank=11 price=2.74 support=2.37 resistance=2.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=58.54 liquidity=2849458.25 spike=0.08
- EKHO.CA: score=5.4 buy_ready=False sector_rank=4 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=5.86 buy_ready=False sector_rank=12 price=2.25 support=2.24 resistance=2.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29971040.0 spike=1.08
- ELKA.CA: score=5.84 buy_ready=False sector_rank=11 price=1.88 support=1.86 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16499480.0 spike=0.3
- ELNA.CA: score=12.94 buy_ready=False sector_rank=11 price=39.47 support=35.55 resistance=40.65 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=58.32 liquidity=107989.92 spike=0.21
- ELSH.CA: score=15.77 buy_ready=False sector_rank=11 price=14.6 support=11.1 resistance=15.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=70.1 liquidity=4933015.5 spike=0.03
- ELWA.CA: score=13.89 buy_ready=False sector_rank=11 price=2.04 support=1.87 resistance=2.15 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=48.72 liquidity=1055004.34 spike=0.98
- EMFD.CA: score=20.83 buy_ready=False sector_rank=10 price=11.9 support=11.24 resistance=12.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=52.52 liquidity=9794262.0 spike=0.08
- ENGC.CA: score=13.24 buy_ready=False sector_rank=11 price=42.72 support=33.91 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=74.33 liquidity=399214.97 spike=0.02
- EOSB.CA: score=10.86 buy_ready=False sector_rank=11 price=1.48 support=1.42 resistance=1.55 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=22083.08 spike=0.35
- EPCO.CA: score=2.29 buy_ready=False sector_rank=11 price=10.77 support=10.52 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6449799.0 spike=0.47
- EPPK.CA: score=11.42 buy_ready=False sector_rank=11 price=14.13 support=11.75 resistance=15.25 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=69.3 liquidity=579259.35 spike=0.6
- ETEL.CA: score=17.03 buy_ready=False sector_rank=5 price=98.83 support=89.01 resistance=101.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT RSI=54.82 liquidity=3633992.5 spike=0.05
- ETRS.CA: score=11.72 buy_ready=False sector_rank=11 price=10.9 support=9.84 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=56.91 liquidity=888080.38 spike=0.01
- EXPA.CA: score=16.26 buy_ready=False sector_rank=16 price=19.3 support=18.03 resistance=18.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=62.09 liquidity=2195494.0 spike=0.09
- FAIT.CA: score=12.97 buy_ready=False sector_rank=16 price=37.5 support=35.06 resistance=37.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT RSI=54.36 liquidity=905473.31 spike=0.34
- FAITA.CA: score=5.08 buy_ready=False sector_rank=16 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=15 July 12:39 PM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=10057.29 spike=0.31
- FERC.CA: score=23.87 buy_ready=False sector_rank=13 price=76.82 support=72.75 resistance=80.83 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=53.89 liquidity=10360329.26 spike=2.6
- FWRY.CA: score=12.42 buy_ready=False sector_rank=17 price=18.73 support=18.13 resistance=19.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=50.19 liquidity=5798304.5 spike=0.04
- GBCO.CA: score=15.94 buy_ready=False sector_rank=2 price=33.16 support=27.77 resistance=32.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT RSI=55.44 liquidity=2537895.5 spike=0.04
- GDWA.CA: score=19.84 buy_ready=False sector_rank=11 price=0.86 support=0.76 resistance=0.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=14994832.0 spike=0.57
- GGCC.CA: score=-1.11 buy_ready=False sector_rank=11 price=0.68 support=0.67 resistance=0.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3057882.75 spike=0.16
- GIHD.CA: score=3.03 buy_ready=False sector_rank=11 price=51.56 support=51.45 resistance=53.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7191503.0 spike=0.28
- GMCI.CA: score=11.52 buy_ready=False sector_rank=11 price=1.97 support=1.66 resistance=2.26 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=68.06 liquidity=683984.01 spike=0.64
- GRCA.CA: score=10.21 buy_ready=False sector_rank=11 price=52.57 support=48.0 resistance=58.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:19 AM market time freshness=DELAYED_CURRENT RSI=42.56 liquidity=378521.34 spike=0.11
- GSSC.CA: score=17.43 buy_ready=False sector_rank=11 price=267.87 support=240.0 resistance=263.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=63.14 liquidity=4557424.0 spike=1.02
- GTWL.CA: score=5.84 buy_ready=False sector_rank=11 price=101.91 support=100.07 resistance=105.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18247722.0 spike=0.18
- HDBK.CA: score=0.22 buy_ready=False sector_rank=16 price=79.44 support=75.3 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=6.93 liquidity=1147624.88 spike=0.03
- HELI.CA: score=1.66 buy_ready=False sector_rank=10 price=7.73 support=7.71 resistance=7.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5621265.5 spike=0.04
- HRHO.CA: score=6.41 buy_ready=False sector_rank=14 price=26.41 support=26.09 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=44.62 liquidity=1794944.25 spike=0.01
- ICID.CA: score=11.89 buy_ready=False sector_rank=11 price=8.18 support=6.55 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:18 AM market time freshness=DELAYED_CURRENT RSI=60.6 liquidity=1056824.75 spike=0.12
- IDRE.CA: score=13.46 buy_ready=False sector_rank=11 price=46.0 support=41.1 resistance=47.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:21 AM market time freshness=DELAYED_CURRENT RSI=49.67 liquidity=622808.31 spike=0.05
- IFAP.CA: score=13.5 buy_ready=False sector_rank=8 price=19.59 support=18.47 resistance=20.0 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=63.03 liquidity=3187253.84 spike=0.8
- INFI.CA: score=12.33 buy_ready=False sector_rank=11 price=101.82 support=88.51 resistance=106.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=61.67 liquidity=497552.56 spike=0.05
- IRON.CA: score=7.03 buy_ready=False sector_rank=13 price=31.74 support=30.45 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT RSI=56.09 liquidity=362599.63 spike=0.05
- ISMA.CA: score=13.84 buy_ready=False sector_rank=11 price=27.22 support=26.54 resistance=36.45 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=20.05 liquidity=12752324.7 spike=0.64
- ISMQ.CA: score=17.81 buy_ready=False sector_rank=13 price=9.57 support=8.06 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=67.68 liquidity=9146867.0 spike=0.06
- ISPH.CA: score=3.94 buy_ready=False sector_rank=15 price=11.42 support=11.2 resistance=12.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=29.73 liquidity=3620532.75 spike=0.06
- JUFO.CA: score=10.01 buy_ready=False sector_rank=19 price=30.01 support=29.1 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=40.92 liquidity=2445104.25 spike=0.11
- KABO.CA: score=12.45 buy_ready=False sector_rank=3 price=7.72 support=6.04 resistance=7.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT RSI=95.56 liquidity=1051634.0 spike=0.03
- KWIN.CA: score=16.35 buy_ready=False sector_rank=11 price=74.02 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=63.72 liquidity=3518631.0 spike=0.25
- KZPC.CA: score=20.63 buy_ready=False sector_rank=11 price=8.7 support=8.26 resistance=9.24 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=44.92 liquidity=9875169.68 spike=1.96
- LCSW.CA: score=11.9 buy_ready=False sector_rank=20 price=32.38 support=26.66 resistance=32.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=65.75 liquidity=2754593.75 spike=0.05
- LUTS.CA: score=15.27 buy_ready=False sector_rank=11 price=0.75 support=0.69 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=49.55 liquidity=4433298.5 spike=0.09
- MAAL.CA: score=11.97 buy_ready=False sector_rank=11 price=8.45 support=5.82 resistance=8.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=98.94 liquidity=2136150.0 spike=0.13
- MASR.CA: score=20.84 buy_ready=False sector_rank=11 price=8.45 support=6.71 resistance=8.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=73.52 liquidity=12396575.0 spike=0.15
- MBSC.CA: score=6.09 buy_ready=False sector_rank=20 price=233.03 support=222.66 resistance=254.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=40.9 liquidity=1941390.38 spike=0.09
- MCQE.CA: score=8.7 buy_ready=False sector_rank=20 price=175.94 support=166.66 resistance=182.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=57.42 liquidity=548426.25 spike=0.04
- MCRO.CA: score=21.84 buy_ready=False sector_rank=11 price=1.34 support=1.17 resistance=1.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=73.33 liquidity=10841042.0 spike=0.22
- MENA.CA: score=12.85 buy_ready=False sector_rank=10 price=7.01 support=6.59 resistance=7.59 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=59.34 liquidity=1816178.9 spike=0.29
- MEPA.CA: score=16.85 buy_ready=False sector_rank=11 price=1.73 support=1.52 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=53.12 liquidity=4009660.75 spike=0.36
- MFPC.CA: score=18.0 buy_ready=False sector_rank=13 price=37.68 support=34.22 resistance=38.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=65.91 liquidity=8336811.5 spike=0.08
- MFSC.CA: score=-1.22 buy_ready=False sector_rank=11 price=48.27 support=47.2 resistance=48.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2948960.5 spike=0.38
- MHOT.CA: score=6.4 buy_ready=False sector_rank=21 price=16.25 support=16.12 resistance=38.38 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=3.57 liquidity=10652395.0 spike=0.77
- MICH.CA: score=11.18 buy_ready=False sector_rank=11 price=38.53 support=34.0 resistance=39.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=49.35 liquidity=341718.5 spike=0.03
- MILS.CA: score=13.89 buy_ready=False sector_rank=11 price=139.43 support=126.31 resistance=147.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT RSI=60.35 liquidity=1057494.38 spike=0.09
- MIPH.CA: score=13.29 buy_ready=False sector_rank=15 price=740.45 support=630.13 resistance=725.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:18 AM market time freshness=DELAYED_CURRENT RSI=71.55 liquidity=965538.38 spike=0.36
- MOED.CA: score=14.52 buy_ready=False sector_rank=11 price=0.73 support=0.65 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=62.89 liquidity=2688598.25 spike=0.2
- MOIL.CA: score=11.44 buy_ready=False sector_rank=4 price=0.54 support=0.46 resistance=0.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=72.36 liquidity=41833.24 spike=0.12
- MOIN.CA: score=9.3 buy_ready=False sector_rank=11 price=24.04 support=22.6 resistance=24.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=15 July 01:12 PM market time freshness=DELAYED_CURRENT RSI=60.72 liquidity=460115.63 spike=0.52
- MOSC.CA: score=10.3 buy_ready=False sector_rank=11 price=281.04 support=250.0 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=55.66 liquidity=459368.13 spike=0.03
- MPCI.CA: score=17.2 buy_ready=False sector_rank=11 price=247.21 support=217.0 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=44.17 liquidity=6361698.0 spike=0.07
- MPCO.CA: score=15.03 buy_ready=False sector_rank=8 price=1.9 support=1.7 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=3714201.25 spike=0.04
- MPRC.CA: score=10.08 buy_ready=False sector_rank=11 price=43.54 support=31.72 resistance=43.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=83.21 liquidity=2248697.25 spike=0.05
- MTIE.CA: score=18.38 buy_ready=False sector_rank=2 price=9.4 support=8.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=63.37 liquidity=2975122.5 spike=0.13
- NAHO.CA: score=4.85 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=42.86 liquidity=16421.5 spike=0.73
- NCCW.CA: score=15.39 buy_ready=False sector_rank=11 price=6.49 support=5.82 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=50.77 liquidity=2555200.0 spike=0.12
- NEDA.CA: score=13.16 buy_ready=False sector_rank=11 price=2.79 support=2.7 resistance=2.83 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=57.14 liquidity=327054.96 spike=0.97
- NHPS.CA: score=5.84 buy_ready=False sector_rank=11 price=90.98 support=88.78 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28842408.0 spike=0.63
- NINH.CA: score=10.84 buy_ready=False sector_rank=11 price=21.5 support=19.49 resistance=22.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=66846892.0 spike=6.71
- NIPH.CA: score=5.32 buy_ready=False sector_rank=15 price=195.28 support=193.0 resistance=195.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35266300.0 spike=0.38
- OBRI.CA: score=18.37 buy_ready=False sector_rank=11 price=36.89 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=55.1 liquidity=5538402.5 spike=0.17
- OCDI.CA: score=15.87 buy_ready=False sector_rank=10 price=27.76 support=20.66 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=72.62 liquidity=4838677.5 spike=0.05
- OCPH.CA: score=6.02 buy_ready=False sector_rank=11 price=422.0 support=420.99 resistance=433.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10164248.0 spike=1.09
- ODIN.CA: score=9.18 buy_ready=False sector_rank=11 price=2.47 support=2.05 resistance=2.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=75.76 liquidity=1342448.88 spike=0.09
- OFH.CA: score=10.6 buy_ready=False sector_rank=11 price=0.69 support=0.67 resistance=0.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=80063176.0 spike=3.38
- OIH.CA: score=17.49 buy_ready=False sector_rank=7 price=1.42 support=1.35 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=5154137.0 spike=0.07
- OLFI.CA: score=12.23 buy_ready=False sector_rank=19 price=22.91 support=21.0 resistance=23.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=64.53 liquidity=672354.5 spike=0.02
- ORAS.CA: score=4.6 buy_ready=False sector_rank=18 price=703.75 support=703.0 resistance=707.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13033577.0 spike=1.0
- ORHD.CA: score=21.04 buy_ready=False sector_rank=10 price=39.78 support=37.0 resistance=39.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=28106760.0 spike=0.19
- ORWE.CA: score=18.77 buy_ready=False sector_rank=3 price=23.01 support=21.95 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=40.58 liquidity=6365357.5 spike=0.35
- PHAR.CA: score=20.32 buy_ready=False sector_rank=15 price=89.27 support=83.5 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT RSI=46.5 liquidity=10954386.0 spike=0.5
- PHDC.CA: score=16.04 buy_ready=False sector_rank=10 price=15.25 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=27.27 liquidity=108113872.0 spike=0.35
- PHTV.CA: score=9.06 buy_ready=False sector_rank=11 price=293.84 support=216.31 resistance=308.49 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=80.32 liquidity=1222962.06 spike=0.11
- POUL.CA: score=12.13 buy_ready=False sector_rank=19 price=39.43 support=35.28 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=45.97 liquidity=567864.94 spike=0.01
- PRCL.CA: score=-0.06 buy_ready=False sector_rank=20 price=35.83 support=34.97 resistance=35.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5787210.5 spike=0.12
- PRDC.CA: score=6.04 buy_ready=False sector_rank=10 price=9.59 support=9.57 resistance=9.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24854770.0 spike=0.16
- PRMH.CA: score=13.29 buy_ready=False sector_rank=11 price=2.73 support=2.34 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT RSI=51.19 liquidity=449534.69 spike=0.01
- RACC.CA: score=14.43 buy_ready=False sector_rank=11 price=10.41 support=9.36 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=56.76 liquidity=1590964.5 spike=0.09
- RAKT.CA: score=11.64 buy_ready=False sector_rank=11 price=22.22 support=21.25 resistance=23.79 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=40.22 liquidity=806697.08 spike=3.0
- RAYA.CA: score=22.58 buy_ready=False sector_rank=1 price=8.02 support=6.8 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=67.94 liquidity=8182846.0 spike=0.07
- RMDA.CA: score=7.88 buy_ready=False sector_rank=15 price=4.98 support=4.81 resistance=5.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=44.26 liquidity=2560555.0 spike=0.13
- ROTO.CA: score=9.89 buy_ready=False sector_rank=11 price=41.72 support=34.5 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=47.72 liquidity=1054483.0 spike=0.03
- RREI.CA: score=11.82 buy_ready=False sector_rank=11 price=3.91 support=3.34 resistance=3.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT RSI=78.57 liquidity=1979586.75 spike=0.09
- RTVC.CA: score=13.74 buy_ready=False sector_rank=11 price=3.91 support=3.55 resistance=3.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT RSI=52.31 liquidity=905378.06 spike=0.23
- RUBX.CA: score=14.56 buy_ready=False sector_rank=11 price=14.33 support=9.8 resistance=14.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=81.44 liquidity=4719913.0 spike=0.07
- SAUD.CA: score=7.83 buy_ready=False sector_rank=16 price=21.4 support=19.99 resistance=22.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=765110.0 spike=0.13
- SCEM.CA: score=4.48 buy_ready=False sector_rank=20 price=62.21 support=60.14 resistance=67.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=52.98 liquidity=335125.38 spike=0.02
- SCFM.CA: score=13.67 buy_ready=False sector_rank=11 price=259.96 support=226.5 resistance=269.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=59.84 liquidity=831071.88 spike=0.16
- SCTS.CA: score=15.63 buy_ready=False sector_rank=9 price=613.33 support=540.0 resistance=649.0 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=62.19 liquidity=2317774.13 spike=0.5
- SDTI.CA: score=14.04 buy_ready=False sector_rank=11 price=47.0 support=45.55 resistance=49.5 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=53.91 liquidity=3201687.0 spike=0.68
- SEIG.CA: score=8.58 buy_ready=False sector_rank=11 price=240.95 support=181.35 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=79.95 liquidity=744251.88 spike=0.04
- SIPC.CA: score=10.84 buy_ready=False sector_rank=11 price=3.87 support=3.72 resistance=3.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35303140.0 spike=5.03
- SKPC.CA: score=20.67 buy_ready=False sector_rank=13 price=16.33 support=15.58 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=64.08 liquidity=21741302.0 spike=0.67
- SMFR.CA: score=0.73 buy_ready=False sector_rank=11 price=231.26 support=227.01 resistance=237.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4896931.5 spike=0.72
- SNFC.CA: score=6.59 buy_ready=False sector_rank=11 price=11.5 support=11.26 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=44.12 liquidity=755022.06 spike=0.07
- SPIN.CA: score=12.27 buy_ready=False sector_rank=3 price=14.64 support=13.3 resistance=14.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:16 AM market time freshness=DELAYED_CURRENT RSI=81.95 liquidity=874985.56 spike=0.09
- SPMD.CA: score=14.78 buy_ready=False sector_rank=11 price=0.45 support=0.41 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=61.11 liquidity=1940382.25 spike=0.11
- SUGR.CA: score=12.46 buy_ready=False sector_rank=19 price=47.03 support=45.31 resistance=48.95 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=43.62 liquidity=6036911.73 spike=1.43
- SVCE.CA: score=12.45 buy_ready=False sector_rank=11 price=9.5 support=8.76 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=55.48 liquidity=1614338.38 spike=0.02
- SWDY.CA: score=18.8 buy_ready=False sector_rank=12 price=91.32 support=84.3 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT RSI=52.01 liquidity=6096283.5 spike=0.48
- TALM.CA: score=10.19 buy_ready=False sector_rank=9 price=15.83 support=15.27 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=38.86 liquidity=1869823.5 spike=0.16
- TMGH.CA: score=23.04 buy_ready=False sector_rank=10 price=102.5 support=92.1 resistance=99.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=60.07 liquidity=172939648.0 spike=0.5
- TRTO.CA: score=6.84 buy_ready=False sector_rank=11 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=13.44 buy_ready=False sector_rank=11 price=521.04 support=460.0 resistance=529.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=59.37 liquidity=600986.56 spike=0.35
- UEGC.CA: score=19.84 buy_ready=False sector_rank=11 price=2.12 support=1.33 resistance=2.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=92.13 liquidity=15947174.0 spike=0.55
- UNIP.CA: score=2.02 buy_ready=False sector_rank=11 price=0.36 support=0.36 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6185303.0 spike=0.41
- UNIT.CA: score=9.13 buy_ready=False sector_rank=10 price=19.47 support=12.0 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT RSI=77.63 liquidity=1093780.13 spike=0.04
- WCDF.CA: score=10.16 buy_ready=False sector_rank=11 price=525.67 support=504.0 resistance=544.99 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=46.24 liquidity=323287.04 spike=0.91
- WKOL.CA: score=13.46 buy_ready=False sector_rank=11 price=312.91 support=273.1 resistance=334.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=60.52 liquidity=622672.0 spike=0.09
- ZEOT.CA: score=14.1 buy_ready=False sector_rank=11 price=11.78 support=9.47 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=49.86 liquidity=3260355.75 spike=0.07
- ZMID.CA: score=21.04 buy_ready=False sector_rank=10 price=7.35 support=6.11 resistance=7.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=65.74 liquidity=57078148.0 spike=0.26

## Backtesting Lite
- FERC.CA: 180d return=-4.2%, max drawdown=-23.88%, MA20>MA50 days last20=0, as_of=2026-07-13T21:00:00+00:00
- CCAP.CA: 180d return=87.03%, max drawdown=-25.0%, MA20>MA50 days last20=15, as_of=2026-07-13T21:00:00+00:00
- TMGH.CA: 180d return=69.61%, max drawdown=-23.41%, MA20>MA50 days last20=9, as_of=2026-07-13T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- FERC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=561 sources=3 expected=Ferchem Misr Fertilizers and Chemicals summary=Ferchem Misr’s board greenlights EGP 500m dividends for 2025; Ferchem Misr’s profits soar 4,238% in 2025; Ferchem Misr’s profit leaps 75% in 9M
  - Ferchem Misr’s board greenlights EGP 500m dividends for 2025: https://english.mubasher.info/news/4600298/Ferchem-Misr-s-board-greenlights-EGP-500m-dividends-for-2025/
  - Ferchem Misr’s profits soar 4,238% in 2025: https://english.mubasher.info/news/4564349/Ferchem-Misr-s-profits-soar-4-238-in-2025/
  - Ferchem Misr’s profit leaps 75% in 9M: https://english.mubasher.info/news/3560738/Ferchem-Misr-s-profit-leaps-75-in-9M/
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- TMGH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talaat Moustafa Group Holding summary=Evidence rejected for TMGH.CA: source text did not clearly match TMGH.CA / Talaat Moustafa Group Holding.
- BTFH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Beltone Holding summary=Evidence rejected for BTFH.CA: source text did not clearly match BTFH.CA / Beltone Holding.
- RAYA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=561 sources=3 expected=Raya Holding summary=Raya stock maintains bullish momentum above EGP 9; Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt; Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn
  - Raya stock maintains bullish momentum above EGP 9: https://english.mubasher.info/news/4601857/Raya-stock-maintains-bullish-momentum-above-EGP-9/
  - Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt: https://english.mubasher.info/news/4577815/Aman-Holding-MSMEDA-partner-to-inject-EGP-300m-into-SMEs-across-Egypt/
  - Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn: https://english.mubasher.info/news/4564195/Raya-Holding-s-consolidated-profits-surge-in-2025-revenues-hit-EGP-63-8bn/
- COMI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Commercial International Bank Egypt summary=Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- MCRO.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Macro Group Pharmaceuticals (Macro Capital) S.A.E summary=Macro Group’s EGP 570m capital increase nearly fully subscribed; Macro Group’s shareholders greenlight EGP 570m capital increase; Macro Group secures EGP 65m loan from FABMISR
  - Macro Group’s EGP 570m capital increase nearly fully subscribed: https://english.mubasher.info/news/4533695/Macro-Group-s-EGP-570m-capital-increase-nearly-fully-subscribed/
  - Macro Group’s shareholders greenlight EGP 570m capital increase: https://english.mubasher.info/news/4508284/Macro-Group-s-shareholders-greenlight-EGP-570m-capital-increase/
  - Macro Group secures EGP 65m loan from FABMISR: https://english.mubasher.info/news/4265398/Macro-Group-secures-EGP-65m-loan-from-FABMISR/
- ORHD.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Development Egypt summary=Evidence rejected for ORHD.CA: source text did not clearly match ORHD.CA / Orascom Development Egypt.

## Warnings
- Evidence for FERC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence rejected for TMGH.CA: source text did not clearly match TMGH.CA / Talaat Moustafa Group Holding.
- Evidence rejected for BTFH.CA: source text did not clearly match BTFH.CA / Beltone Holding.
- Evidence for RAYA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- Evidence for MCRO.CA matches the company but no source/report date was detected.
- Evidence rejected for ORHD.CA: source text did not clearly match ORHD.CA / Orascom Development Egypt.
