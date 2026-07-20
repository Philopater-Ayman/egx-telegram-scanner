# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-07-20T08:36:25.776319+00:00
Generated Cairo: 2026-07-20 11:36
Run timing: target 08:45 Cairo | generated Cairo 2026-07-20 11:36 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-07-20 11:27

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 39
- Data quality issues: 1
- Tradeable price/liquidity tickers: 173/189
- Top sector: Telecommunications

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, July 20
- Freshness: DELAYED
- EGX30 regime: CONSTRUCTIVE / above MA20 60.0% / above MA50 50.0%
- EGX70 regime: BULLISH / above MA20 80.0% / above MA50 77.5%
- Sector breadth: 52.38%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- SCEM.CA: liquidity=182178160.0 spike=6.12 score=14.4
- CCAP.CA: liquidity=138326096.0 spike=0.22 score=23.4
- MCRO.CA: liquidity=132209520.0 spike=2.31 score=23.02
- OIH.CA: liquidity=116495424.0 spike=1.74 score=29.88
- ZMID.CA: liquidity=112199720.0 spike=0.47 score=24.4

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner found no ticket meeting evidence, liquidity, freshness and technical thresholds; therefore it issued a fallback HOLD for all symbols while noting EGX30 constructive, EGX70 bullish breadth and selective swing‑trade risk mode.
- Liquidity spikes and accumulation signals were present but lacked confirming fundamental evidence or freshness.
- Sector breadth highlights telecom, industrials and real estate as leaders, yet most scanned stocks reside in non‑leading sectors with extended momentum or overheated RSI.
- Support/resistance distances show prices either far above support or close to resistance, limiting near‑term upside for the next 1‑3 days.
- EGX30’s constructive trend and EGX70’s bullish bias maintain a selective swing‑trade mode, adding uncertainty to any breakout attempts.

## Top Liquidity Spikes
- EGSA.CA: spike=10.42 liquidity=113201.64 outlook=CONSTRUCTIVE score=50 buy_ready=False
- AFMC.CA: spike=8.0 liquidity=59051152.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CEFM.CA: spike=7.16 liquidity=46552512.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SCEM.CA: spike=6.12 liquidity=182178160.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SCFM.CA: spike=4.78 liquidity=55732300.0 outlook=CONSTRUCTIVE score=64.39 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=14.65 5d=-0.32% 20d=4.44% aboveMA50=100.0%
- #2 Industrial Goods & Cables: score=10.32 5d=4.73% 20d=6.58% aboveMA50=100.0%
- #3 Real Estate: score=9.45 5d=2.49% 20d=17.06% aboveMA50=84.62%
- #4 Automotive & Distribution: score=8.92 5d=2.34% 20d=8.45% aboveMA50=100.0%
- #5 Textiles: score=8.35 5d=1.13% 20d=4.41% aboveMA50=100.0%
- #6 Transportation & Logistics: score=8.31 5d=1.92% 20d=6.21% aboveMA50=100.0%
- #7 Healthcare: score=7.98 5d=4.14% 20d=7.81% aboveMA50=66.67%
- #8 Investment Holding: score=7.85 5d=1.71% 20d=4.19% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- OIH.CA: BULLISH_WATCH score=97.85 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ORHD.CA: BULLISH_WATCH score=89.45 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ARCC.CA: BULLISH_WATCH score=88.82 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ICID.CA: BULLISH_WATCH score=84.39 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- APSW.CA: BULLISH_WATCH score=82.39 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended; sector is not leading
- TMGH.CA: BULLISH_WATCH score=81.45 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- SPIN.CA: BULLISH_WATCH score=81.35 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; close to resistance
- EALR.CA: BULLISH_WATCH score=80.39 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- GBCO.CA: BULLISH_WATCH score=78.92 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- EGAS.CA: BULLISH_WATCH score=78.29 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- OIH.CA: rank=29.88 outlook=BULLISH_WATCH outlook_score=97.85 sector_rank=8 price=1.47 support=1.35 resistance=1.43 liquidity=116495424.0
- SPIN.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=81.35 sector_rank=5 price=14.62 support=13.8 resistance=14.8 liquidity=49914887.23
- ARCC.CA: rank=28.9 outlook=BULLISH_WATCH outlook_score=88.82 sector_rank=11 price=57.6 support=53.0 resistance=56.7 liquidity=60718556.0
- APSW.CA: rank=27.24 outlook=BULLISH_WATCH outlook_score=82.39 sector_rank=12 price=9.19 support=8.0 resistance=8.84 liquidity=3838370.75
- EALR.CA: rank=27.0 outlook=BULLISH_WATCH outlook_score=80.39 sector_rank=12 price=379.21 support=332.0 resistance=425.0 liquidity=31035736.0
- GBCO.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=78.92 sector_rank=4 price=32.3 support=28.6 resistance=34.2 liquidity=14460383.0
- ICID.CA: rank=25.44 outlook=BULLISH_WATCH outlook_score=84.39 sector_rank=12 price=8.26 support=6.55 resistance=8.98 liquidity=12318708.28
- TMGH.CA: rank=25.4 outlook=BULLISH_WATCH outlook_score=81.45 sector_rank=3 price=100.5 support=92.1 resistance=103.5 liquidity=38051768.0
- ORHD.CA: rank=25.4 outlook=BULLISH_WATCH outlook_score=89.45 sector_rank=3 price=39.0 support=37.0 resistance=40.2 liquidity=19466866.0
- COMI.CA: rank=25.15 outlook=CONSTRUCTIVE outlook_score=67.88 sector_rank=17 price=134.67 support=126.21 resistance=137.98 liquidity=65296464.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=10.96 buy_ready=False sector_rank=12 price=244.13 support=243.0 resistance=253.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26735034.0 spike=1.78
- ABUK.CA: score=22.51 buy_ready=False sector_rank=15 price=74.36 support=66.66 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=71.65 liquidity=38692608.0 spike=0.24
- ACAMD.CA: score=22.4 buy_ready=False sector_rank=12 price=2.38 support=2.14 resistance=2.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=71.88 liquidity=62333656.0 spike=0.82
- ACGC.CA: score=17.36 buy_ready=True sector_rank=5 price=9.86 support=8.92 resistance=10.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=67.93 liquidity=2961713.5 spike=0.15
- ADCI.CA: score=18.16 buy_ready=True sector_rank=12 price=243.4 support=227.55 resistance=249.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=51.61 liquidity=3755178.0 spike=0.33
- ADIB.CA: score=18.15 buy_ready=False sector_rank=17 price=46.39 support=44.1 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=54.76 liquidity=19006642.0 spike=0.2
- ADPC.CA: score=15.36 buy_ready=False sector_rank=12 price=3.85 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=83.08 liquidity=3956518.75 spike=0.16
- AFDI.CA: score=14.92 buy_ready=False sector_rank=12 price=47.4 support=41.84 resistance=48.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=72.3 liquidity=515633.09 spike=0.04
- AFMC.CA: score=14.4 buy_ready=False sector_rank=12 price=109.26 support=99.0 resistance=109.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=59051152.0 spike=8.0
- AJWA.CA: score=15.77 buy_ready=False sector_rank=12 price=174.0 support=172.1 resistance=192.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=45.09 liquidity=3366523.75 spike=0.25
- ALCN.CA: score=18.88 buy_ready=False sector_rank=6 price=29.72 support=27.7 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=73.16 liquidity=4481734.0 spike=0.22
- ALUM.CA: score=18.33 buy_ready=False sector_rank=12 price=23.75 support=20.55 resistance=23.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=80.23 liquidity=6793698.0 spike=1.07
- AMER.CA: score=24.4 buy_ready=False sector_rank=3 price=4.09 support=2.28 resistance=4.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=97.98 liquidity=61228428.0 spike=0.62
- AMES.CA: score=21.4 buy_ready=False sector_rank=12 price=119.05 support=45.15 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=78.13 liquidity=16965460.0 spike=0.19
- AMIA.CA: score=11.54 buy_ready=False sector_rank=12 price=10.56 support=9.95 resistance=10.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20479930.0 spike=2.07
- AMOC.CA: score=23.4 buy_ready=False sector_rank=9 price=8.36 support=7.42 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=75.41 liquidity=22497802.0 spike=0.39
- APSW.CA: score=27.24 buy_ready=True sector_rank=12 price=9.19 support=8.0 resistance=8.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=62.8 liquidity=3838370.75 spike=3.6
- ARAB.CA: score=25.4 buy_ready=False sector_rank=3 price=0.25 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=74.07 liquidity=51278040.0 spike=0.44
- ARCC.CA: score=28.9 buy_ready=True sector_rank=11 price=57.6 support=53.0 resistance=56.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=55.7 liquidity=60718556.0 spike=3.25
- AREH.CA: score=18.81 buy_ready=False sector_rank=12 price=1.49 support=1.48 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=6412935.0 spike=0.17
- ARVA.CA: score=24.4 buy_ready=True sector_rank=12 price=10.99 support=10.5 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=43.88 liquidity=11529166.0 spike=0.69
- ASCM.CA: score=16.91 buy_ready=True sector_rank=12 price=61.35 support=56.29 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=67.49 liquidity=4505102.0 spike=0.06
- ASPI.CA: score=20.89 buy_ready=False sector_rank=12 price=0.35 support=0.3 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=73.81 liquidity=6487122.5 spike=0.26
- ATLC.CA: score=17.02 buy_ready=False sector_rank=10 price=5.17 support=4.92 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=4616559.0 spike=0.58
- ATQA.CA: score=22.21 buy_ready=True sector_rank=15 price=9.69 support=9.21 resistance=9.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=59.26 liquidity=6700915.5 spike=0.22
- AXPH.CA: score=11.77 buy_ready=False sector_rank=12 price=1225.18 support=1075.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=75.81 liquidity=371674.75 spike=0.1
- BINV.CA: score=17.72 buy_ready=True sector_rank=8 price=49.52 support=45.01 resistance=51.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=62.84 liquidity=1323451.13 spike=0.2
- BIOC.CA: score=25.64 buy_ready=False sector_rank=12 price=121.55 support=66.75 resistance=126.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=96.32 liquidity=36307804.0 spike=2.12
- BTFH.CA: score=26.4 buy_ready=False sector_rank=10 price=3.16 support=2.91 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=70.45 liquidity=48765716.0 spike=0.23
- CAED.CA: score=9.4 buy_ready=False sector_rank=12 price=123.66 support=121.01 resistance=131.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32283466.0 spike=0.75
- CANA.CA: score=9.54 buy_ready=False sector_rank=17 price=35.52 support=34.7 resistance=38.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=56.08 liquidity=2392906.5 spike=0.2
- CCAP.CA: score=23.4 buy_ready=False sector_rank=8 price=5.5 support=4.65 resistance=5.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=86.92 liquidity=138326096.0 spike=0.22
- CCRS.CA: score=21.83 buy_ready=False sector_rank=12 price=2.62 support=2.18 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=71.23 liquidity=5425465.5 spike=0.36
- CEFM.CA: score=14.4 buy_ready=False sector_rank=12 price=140.0 support=129.55 resistance=142.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46552512.0 spike=7.16
- CERA.CA: score=24.4 buy_ready=False sector_rank=12 price=1.35 support=1.19 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=70.27 liquidity=12366126.0 spike=0.45
- CFGH.CA: score=10.4 buy_ready=False sector_rank=12 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=64.29 liquidity=4285.32 spike=0.47
- CICH.CA: score=16.95 buy_ready=False sector_rank=10 price=12.19 support=11.52 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=52.73 liquidity=545308.56 spike=0.11
- CIEB.CA: score=11.96 buy_ready=False sector_rank=17 price=24.04 support=23.3 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=64.44 liquidity=807113.13 spike=0.11
- CIRA.CA: score=20.04 buy_ready=False sector_rank=16 price=31.28 support=27.17 resistance=33.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=70.18 liquidity=6692061.0 spike=0.18
- CLHO.CA: score=24.4 buy_ready=True sector_rank=7 price=16.97 support=15.5 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=62.55 liquidity=22172524.0 spike=0.48
- CNFN.CA: score=19.55 buy_ready=True sector_rank=10 price=4.9 support=4.54 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=69.81 liquidity=5154541.5 spike=0.1
- COMI.CA: score=25.15 buy_ready=True sector_rank=17 price=134.67 support=126.21 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=57.86 liquidity=65296464.0 spike=0.18
- COPR.CA: score=20.1 buy_ready=True sector_rank=12 price=0.38 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=62.96 liquidity=4701208.0 spike=0.23
- COSG.CA: score=23.4 buy_ready=False sector_rank=12 price=1.69 support=1.47 resistance=1.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=85.71 liquidity=27699808.0 spike=0.72
- CPCI.CA: score=12.66 buy_ready=False sector_rank=12 price=458.21 support=365.01 resistance=512.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=76.19 liquidity=1255104.0 spike=0.12
- CSAG.CA: score=17.87 buy_ready=False sector_rank=6 price=33.53 support=30.87 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=70.57 liquidity=3468587.75 spike=0.18
- DAPH.CA: score=16.79 buy_ready=True sector_rank=12 price=87.37 support=78.52 resistance=87.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=68.98 liquidity=2388112.25 spike=0.23
- DEIN.CA: score=-0.6 buy_ready=False sector_rank=12 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=12.79 buy_ready=False sector_rank=20 price=26.74 support=25.75 resistance=27.83 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=52.49 liquidity=2209900.54 spike=0.43
- DSCW.CA: score=23.4 buy_ready=False sector_rank=12 price=1.95 support=1.71 resistance=1.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=96.15 liquidity=19182096.0 spike=0.44
- DTPP.CA: score=21.4 buy_ready=False sector_rank=12 price=230.3 support=114.67 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=86.11 liquidity=20417288.0 spike=0.38
- EALR.CA: score=27.0 buy_ready=True sector_rank=12 price=379.21 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=65.29 liquidity=31035736.0 spike=2.3
- EASB.CA: score=13.65 buy_ready=False sector_rank=12 price=7.19 support=6.88 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=39.31 liquidity=1248955.63 spike=0.07
- EAST.CA: score=12.06 buy_ready=False sector_rank=20 price=37.21 support=36.11 resistance=39.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=35.99 liquidity=5482025.5 spike=0.11
- EBSC.CA: score=13.3 buy_ready=False sector_rank=12 price=1.89 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=58.11 liquidity=896245.75 spike=0.13
- ECAP.CA: score=16.22 buy_ready=True sector_rank=12 price=33.31 support=31.52 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=59.19 liquidity=1819326.25 spike=0.21
- EDFM.CA: score=27.33 buy_ready=False sector_rank=12 price=389.37 support=310.2 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=88.23 liquidity=9612625.0 spike=3.16
- EEII.CA: score=23.09 buy_ready=False sector_rank=12 price=2.8 support=2.35 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=8694439.0 spike=0.41
- EFIC.CA: score=12.8 buy_ready=False sector_rank=15 price=186.85 support=180.02 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=43.57 liquidity=3294477.75 spike=0.38
- EFID.CA: score=15.58 buy_ready=False sector_rank=20 price=27.6 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=66.34 liquidity=10049380.0 spike=0.25
- EFIH.CA: score=18.05 buy_ready=True sector_rank=14 price=22.1 support=20.0 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=64.06 liquidity=2306482.5 spike=0.06
- EGAL.CA: score=19.51 buy_ready=False sector_rank=15 price=307.0 support=272.28 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=78.21 liquidity=16664741.0 spike=0.36
- EGAS.CA: score=22.34 buy_ready=True sector_rank=9 price=51.58 support=46.51 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=59.9 liquidity=5944833.0 spike=0.53
- EGBE.CA: score=12.18 buy_ready=False sector_rank=17 price=0.46 support=-0.34 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:59 AM market time freshness=DELAYED_CURRENT RSI=96.79 liquidity=24430.1 spike=-1.58
- EGCH.CA: score=17.51 buy_ready=False sector_rank=15 price=13.24 support=12.13 resistance=13.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=78.87 liquidity=12893472.0 spike=0.25
- EGSA.CA: score=19.51 buy_ready=False sector_rank=1 price=9.01 support=8.67 resistance=9.21 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=77.08 liquidity=113201.64 spike=10.42
- EGTS.CA: score=17.81 buy_ready=False sector_rank=3 price=17.9 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=62.7 liquidity=7410927.0 spike=0.14
- EHDR.CA: score=23.78 buy_ready=False sector_rank=12 price=2.96 support=2.37 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=81.71 liquidity=40440160.0 spike=1.19
- EKHO.CA: score=8.4 buy_ready=False sector_rank=9 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=27.6 buy_ready=False sector_rank=2 price=2.25 support=2.04 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=70.73 liquidity=58680040.0 spike=1.1
- ELKA.CA: score=23.4 buy_ready=False sector_rank=12 price=2.07 support=1.19 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=92.79 liquidity=20196228.0 spike=0.31
- ELNA.CA: score=14.65 buy_ready=False sector_rank=12 price=38.99 support=35.55 resistance=40.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:01 AM market time freshness=DELAYED_CURRENT RSI=61.57 liquidity=771776.75 spike=1.24
- ELSH.CA: score=21.46 buy_ready=False sector_rank=12 price=14.21 support=11.1 resistance=15.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=73.32 liquidity=7055549.5 spike=0.05
- ELWA.CA: score=15.95 buy_ready=False sector_rank=12 price=1.99 support=1.87 resistance=2.14 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=47.22 liquidity=2526197.55 spike=2.01
- EMFD.CA: score=16.86 buy_ready=False sector_rank=3 price=11.66 support=11.24 resistance=12.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=57.94 liquidity=3459531.25 spike=0.04
- ENGC.CA: score=23.78 buy_ready=False sector_rank=12 price=42.9 support=33.91 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=72.32 liquidity=9380347.0 spike=0.39
- EOSB.CA: score=14.43 buy_ready=False sector_rank=12 price=1.48 support=1.48 resistance=1.55 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=26589.68 spike=0.48
- EPCO.CA: score=23.4 buy_ready=False sector_rank=12 price=11.12 support=8.5 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=84.49 liquidity=15827964.0 spike=0.72
- EPPK.CA: score=14.74 buy_ready=False sector_rank=12 price=14.59 support=12.31 resistance=15.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=69.54 liquidity=341898.06 spike=0.3
- ETEL.CA: score=25.61 buy_ready=False sector_rank=1 price=98.36 support=89.01 resistance=101.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=73.26 liquidity=6212832.0 spike=0.1
- ETRS.CA: score=16.41 buy_ready=True sector_rank=12 price=10.87 support=10.12 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=54.47 liquidity=2010244.13 spike=0.03
- EXPA.CA: score=17.63 buy_ready=False sector_rank=17 price=19.6 support=18.03 resistance=19.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=77.54 liquidity=5480876.0 spike=0.21
- FAIT.CA: score=13.71 buy_ready=False sector_rank=17 price=37.32 support=35.06 resistance=37.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=73.42 liquidity=553438.5 spike=0.2
- FAITA.CA: score=8.19 buy_ready=False sector_rank=17 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=49.25 liquidity=33267.21 spike=0.97
- FERC.CA: score=12.46 buy_ready=False sector_rank=15 price=76.53 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=64.63 liquidity=950364.31 spike=0.2
- FWRY.CA: score=21.13 buy_ready=False sector_rank=14 price=18.93 support=18.13 resistance=19.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=8379961.0 spike=0.06
- GBCO.CA: score=26.4 buy_ready=True sector_rank=4 price=32.3 support=28.6 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=59.68 liquidity=14460383.0 spike=0.2
- GDWA.CA: score=21.86 buy_ready=False sector_rank=12 price=0.86 support=0.76 resistance=0.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=78.95 liquidity=59164628.0 spike=1.73
- GGCC.CA: score=9.7 buy_ready=False sector_rank=12 price=0.91 support=0.87 resistance=0.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30983546.0 spike=1.15
- GIHD.CA: score=24.4 buy_ready=True sector_rank=12 price=51.94 support=40.66 resistance=55.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=68.76 liquidity=30414640.0 spike=0.92
- GMCI.CA: score=18.09 buy_ready=False sector_rank=12 price=2.11 support=1.66 resistance=2.26 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=71.25 liquidity=2167839.21 spike=1.76
- GRCA.CA: score=14.4 buy_ready=False sector_rank=12 price=64.84 support=63.01 resistance=68.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24431652.0 spike=3.96
- GSSC.CA: score=24.18 buy_ready=False sector_rank=12 price=273.93 support=240.0 resistance=288.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=90.3 liquidity=12094753.0 spike=1.39
- GTWL.CA: score=24.4 buy_ready=False sector_rank=12 price=98.91 support=47.85 resistance=117.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=70.68 liquidity=49137264.0 spike=0.4
- HDBK.CA: score=9.21 buy_ready=False sector_rank=17 price=77.31 support=75.3 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=50.76 liquidity=2053902.0 spike=0.05
- HELI.CA: score=24.4 buy_ready=False sector_rank=3 price=7.92 support=6.36 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=89.29 liquidity=46360076.0 spike=0.27
- HRHO.CA: score=24.4 buy_ready=True sector_rank=10 price=27.0 support=26.09 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=57.62 liquidity=55158012.0 spike=0.45
- ICID.CA: score=25.44 buy_ready=True sector_rank=12 price=8.26 support=6.55 resistance=8.98 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=57.06 liquidity=12318708.28 spike=1.52
- IDRE.CA: score=18.6 buy_ready=True sector_rank=12 price=45.68 support=41.1 resistance=47.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=2202246.75 spike=0.16
- IFAP.CA: score=10.14 buy_ready=False sector_rank=18 price=19.28 support=18.47 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=46.92 liquidity=1475730.75 spike=0.29
- INFI.CA: score=23.7 buy_ready=False sector_rank=12 price=107.12 support=88.51 resistance=106.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=77.65 liquidity=22921202.0 spike=2.15
- IRON.CA: score=8.96 buy_ready=False sector_rank=15 price=31.58 support=30.45 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=57.8 liquidity=1454245.63 spike=0.19
- ISMA.CA: score=23.61 buy_ready=True sector_rank=12 price=28.43 support=26.54 resistance=30.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=38.13 liquidity=9205995.0 spike=0.4
- ISMQ.CA: score=22.72 buy_ready=True sector_rank=15 price=9.27 support=8.06 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=54.17 liquidity=9210028.0 spike=0.07
- ISPH.CA: score=18.76 buy_ready=False sector_rank=7 price=11.54 support=11.2 resistance=12.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=56.52 liquidity=9358138.0 spike=0.17
- JUFO.CA: score=15.81 buy_ready=False sector_rank=20 price=29.15 support=28.5 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=46.64 liquidity=8228141.5 spike=0.41
- KABO.CA: score=23.78 buy_ready=False sector_rank=5 price=8.17 support=6.04 resistance=7.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=95.05 liquidity=42015400.0 spike=1.19
- KWIN.CA: score=12.32 buy_ready=False sector_rank=12 price=89.97 support=83.99 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=64627004.0 spike=2.46
- KZPC.CA: score=10.92 buy_ready=False sector_rank=12 price=8.59 support=8.26 resistance=9.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=61.0 liquidity=517926.09 spike=0.09
- LCSW.CA: score=21.4 buy_ready=False sector_rank=11 price=33.25 support=27.01 resistance=33.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=86.54 liquidity=15490564.0 spike=0.23
- LUTS.CA: score=18.0 buy_ready=False sector_rank=12 price=0.74 support=0.69 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=54.64 liquidity=5600274.5 spike=0.13
- MAAL.CA: score=13.87 buy_ready=False sector_rank=12 price=8.7 support=6.46 resistance=8.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=91.88 liquidity=2465250.0 spike=0.13
- MASR.CA: score=23.4 buy_ready=False sector_rank=12 price=8.3 support=6.71 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=89.47 liquidity=19261392.0 spike=0.22
- MBSC.CA: score=19.76 buy_ready=False sector_rank=11 price=245.5 support=222.66 resistance=253.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=65.09 liquidity=20781328.0 spike=1.18
- MCQE.CA: score=14.2 buy_ready=False sector_rank=11 price=189.68 support=179.13 resistance=191.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=43582292.0 spike=3.4
- MCRO.CA: score=23.02 buy_ready=False sector_rank=12 price=1.4 support=1.17 resistance=1.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=77.42 liquidity=132209520.0 spike=2.31
- MENA.CA: score=16.04 buy_ready=False sector_rank=3 price=7.18 support=6.59 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:01 AM market time freshness=DELAYED_CURRENT RSI=64.8 liquidity=637013.31 spike=0.09
- MEPA.CA: score=24.1 buy_ready=False sector_rank=12 price=1.77 support=1.52 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=85.29 liquidity=21463580.0 spike=1.35
- MFPC.CA: score=20.51 buy_ready=False sector_rank=15 price=38.23 support=34.22 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=74.64 liquidity=14239842.0 spike=0.15
- MFSC.CA: score=10.07 buy_ready=False sector_rank=12 price=46.23 support=44.22 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=38.42 liquidity=672297.31 spike=0.08
- MHOT.CA: score=5.41 buy_ready=False sector_rank=21 price=16.25 support=16.12 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=36.02 liquidity=1010489.5 spike=0.07
- MICH.CA: score=14.0 buy_ready=False sector_rank=12 price=38.23 support=34.0 resistance=39.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=72.48 liquidity=1598959.88 spike=0.12
- MILS.CA: score=14.4 buy_ready=False sector_rank=12 price=186.89 support=170.0 resistance=194.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=93785144.0 spike=4.64
- MIPH.CA: score=19.9 buy_ready=False sector_rank=7 price=762.73 support=630.13 resistance=780.0 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=87.74 liquidity=5422247.43 spike=1.54
- MOED.CA: score=13.0 buy_ready=False sector_rank=12 price=0.72 support=0.65 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=2597857.5 spike=0.2
- MOIL.CA: score=13.41 buy_ready=False sector_rank=9 price=0.55 support=0.46 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=80.45 liquidity=10606.41 spike=0.03
- MOIN.CA: score=10.48 buy_ready=False sector_rank=12 price=24.04 support=22.6 resistance=24.76 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=65.07 liquidity=76615.48 spike=0.1
- MOSC.CA: score=17.84 buy_ready=True sector_rank=12 price=289.48 support=250.0 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=66.69 liquidity=3444016.0 spike=0.27
- MPCI.CA: score=21.4 buy_ready=False sector_rank=12 price=253.5 support=221.5 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=76.59 liquidity=36316092.0 spike=0.37
- MPCO.CA: score=22.67 buy_ready=True sector_rank=18 price=1.89 support=1.7 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=26109090.0 spike=0.36
- MPRC.CA: score=15.8 buy_ready=False sector_rank=12 price=42.97 support=31.74 resistance=44.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=78.35 liquidity=4395821.0 spike=0.09
- MTIE.CA: score=21.07 buy_ready=True sector_rank=4 price=9.4 support=8.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=64.14 liquidity=4674752.0 spike=0.19
- NAHO.CA: score=8.41 buy_ready=False sector_rank=12 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:53 AM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=14065.58 spike=0.56
- NCCW.CA: score=23.19 buy_ready=False sector_rank=12 price=6.65 support=5.82 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=71.35 liquidity=6786154.5 spike=0.28
- NEDA.CA: score=14.82 buy_ready=False sector_rank=12 price=2.87 support=2.7 resistance=3.02 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=68.57 liquidity=415291.85 spike=0.71
- NHPS.CA: score=21.4 buy_ready=False sector_rank=12 price=87.13 support=61.55 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=82.33 liquidity=15083802.0 spike=0.23
- NINH.CA: score=23.4 buy_ready=False sector_rank=12 price=22.56 support=17.12 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=86.51 liquidity=29723632.0 spike=0.89
- NIPH.CA: score=23.4 buy_ready=False sector_rank=7 price=209.25 support=157.01 resistance=203.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=84.36 liquidity=70816584.0 spike=0.61
- OBRI.CA: score=21.4 buy_ready=False sector_rank=12 price=35.5 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=68.02 liquidity=11715298.0 spike=0.36
- OCDI.CA: score=15.11 buy_ready=False sector_rank=3 price=28.04 support=21.4 resistance=28.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=75.24 liquidity=2712705.5 spike=0.02
- OCPH.CA: score=16.39 buy_ready=False sector_rank=12 price=421.19 support=337.0 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=92.13 liquidity=4985341.0 spike=0.24
- ODIN.CA: score=14.0 buy_ready=False sector_rank=12 price=2.46 support=2.05 resistance=2.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=77.46 liquidity=2604814.5 spike=0.18
- OFH.CA: score=21.4 buy_ready=False sector_rank=12 price=0.71 support=0.57 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=87.92 liquidity=37943792.0 spike=0.78
- OIH.CA: score=29.88 buy_ready=True sector_rank=8 price=1.47 support=1.35 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=116495424.0 spike=1.74
- OLFI.CA: score=22.58 buy_ready=True sector_rank=20 price=22.85 support=21.0 resistance=23.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=69.09 liquidity=15846958.0 spike=0.5
- ORAS.CA: score=7.6 buy_ready=False sector_rank=19 price=716.01 support=713.01 resistance=719.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19834270.0 spike=1.0
- ORHD.CA: score=25.4 buy_ready=True sector_rank=3 price=39.0 support=37.0 resistance=40.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=53.98 liquidity=19466866.0 spike=0.13
- ORWE.CA: score=17.7 buy_ready=True sector_rank=5 price=23.14 support=21.95 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=67.47 liquidity=3301888.5 spike=0.16
- PHAR.CA: score=26.4 buy_ready=False sector_rank=7 price=90.61 support=83.6 resistance=92.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=72.01 liquidity=16188272.0 spike=0.53
- PHDC.CA: score=20.4 buy_ready=False sector_rank=3 price=14.72 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=51.31 liquidity=33039536.0 spike=0.13
- PHTV.CA: score=13.96 buy_ready=False sector_rank=12 price=310.02 support=216.31 resistance=317.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=81.98 liquidity=556731.63 spike=0.05
- POUL.CA: score=14.0 buy_ready=True sector_rank=20 price=39.07 support=35.28 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=56.59 liquidity=1415179.38 spike=0.03
- PRCL.CA: score=23.4 buy_ready=False sector_rank=11 price=36.34 support=26.05 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=78.18 liquidity=17947476.0 spike=0.34
- PRDC.CA: score=24.4 buy_ready=False sector_rank=3 price=9.7 support=6.67 resistance=10.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=81.07 liquidity=104520320.0 spike=0.86
- PRMH.CA: score=13.35 buy_ready=False sector_rank=12 price=2.74 support=2.34 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=77.05 liquidity=1946696.75 spike=0.09
- RACC.CA: score=19.82 buy_ready=True sector_rank=12 price=10.1 support=9.36 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=62.22 liquidity=3416314.25 spike=0.18
- RAKT.CA: score=10.96 buy_ready=False sector_rank=12 price=22.16 support=21.25 resistance=23.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=19 July 12:39 PM market time freshness=DELAYED_CURRENT RSI=46.82 liquidity=357558.81 spike=1.1
- RAYA.CA: score=24.2 buy_ready=True sector_rank=13 price=7.78 support=6.99 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=60.44 liquidity=28162740.0 spike=0.22
- RMDA.CA: score=12.57 buy_ready=False sector_rank=7 price=4.96 support=4.81 resistance=5.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=61.22 liquidity=3167799.5 spike=0.18
- ROTO.CA: score=15.35 buy_ready=False sector_rank=12 price=41.6 support=38.0 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=57.2 liquidity=2950811.75 spike=0.09
- RREI.CA: score=15.47 buy_ready=False sector_rank=12 price=3.83 support=3.34 resistance=4.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=78.57 liquidity=4073360.0 spike=0.14
- RTVC.CA: score=21.27 buy_ready=False sector_rank=12 price=4.02 support=3.55 resistance=3.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=73.77 liquidity=5893136.0 spike=1.49
- RUBX.CA: score=20.24 buy_ready=True sector_rank=12 price=13.53 support=9.96 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=65.89 liquidity=5837652.0 spike=0.08
- SAUD.CA: score=11.07 buy_ready=False sector_rank=17 price=21.54 support=19.99 resistance=22.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=71.51 liquidity=920986.94 spike=0.17
- SCEM.CA: score=14.4 buy_ready=False sector_rank=11 price=79.5 support=71.25 resistance=81.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=182178160.0 spike=6.12
- SCFM.CA: score=28.4 buy_ready=False sector_rank=12 price=314.08 support=226.5 resistance=308.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=88.04 liquidity=55732300.0 spike=4.78
- SCTS.CA: score=10.88 buy_ready=False sector_rank=16 price=603.4 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:01 AM market time freshness=DELAYED_CURRENT RSI=74.17 liquidity=532279.25 spike=0.1
- SDTI.CA: score=14.79 buy_ready=False sector_rank=12 price=47.29 support=45.55 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=63.45 liquidity=394876.69 spike=0.08
- SEIG.CA: score=15.97 buy_ready=False sector_rank=12 price=241.93 support=182.01 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=74.45 liquidity=1574008.88 spike=0.07
- SIPC.CA: score=23.32 buy_ready=False sector_rank=12 price=3.85 support=3.25 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=75.28 liquidity=9922464.0 spike=0.77
- SKPC.CA: score=17.59 buy_ready=False sector_rank=15 price=16.05 support=14.8 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=53.86 liquidity=8077014.5 spike=0.23
- SMFR.CA: score=18.95 buy_ready=False sector_rank=12 price=238.73 support=187.01 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=79.3 liquidity=7552799.5 spike=0.43
- SNFC.CA: score=10.96 buy_ready=False sector_rank=12 price=11.34 support=11.26 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=38.71 liquidity=1563075.0 spike=0.14
- SPIN.CA: score=29.4 buy_ready=True sector_rank=5 price=14.62 support=13.8 resistance=14.8 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=68.18 liquidity=49914887.23 spike=4.12
- SPMD.CA: score=18.83 buy_ready=False sector_rank=12 price=0.46 support=0.41 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=77.78 liquidity=7428170.5 spike=0.33
- SUGR.CA: score=9.53 buy_ready=False sector_rank=20 price=46.97 support=45.31 resistance=48.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=59.55 liquidity=951824.81 spike=0.18
- SVCE.CA: score=24.4 buy_ready=True sector_rank=12 price=9.5 support=8.76 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=60.38 liquidity=43551248.0 spike=0.68
- SWDY.CA: score=21.88 buy_ready=False sector_rank=2 price=92.67 support=84.3 resistance=93.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=76.82 liquidity=6476027.5 spike=0.39
- TALM.CA: score=12.19 buy_ready=False sector_rank=16 price=15.73 support=15.27 resistance=16.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=53.75 liquidity=1838197.63 spike=0.14
- TMGH.CA: score=25.4 buy_ready=True sector_rank=3 price=100.5 support=92.1 resistance=103.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=68.19 liquidity=38051768.0 spike=0.1
- TRTO.CA: score=10.4 buy_ready=False sector_rank=12 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=393.99 spike=0.98
- UEFM.CA: score=27.04 buy_ready=False sector_rank=12 price=551.97 support=460.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=77.82 liquidity=9999259.0 spike=2.82
- UEGC.CA: score=23.4 buy_ready=False sector_rank=12 price=2.38 support=1.33 resistance=2.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=96.26 liquidity=32690006.0 spike=0.86
- UNIP.CA: score=10.82 buy_ready=False sector_rank=12 price=0.39 support=0.37 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30208688.0 spike=1.71
- UNIT.CA: score=14.5 buy_ready=False sector_rank=3 price=19.11 support=12.0 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=78.53 liquidity=2098027.0 spike=0.08
- WCDF.CA: score=10.05 buy_ready=False sector_rank=12 price=598.48 support=582.11 resistance=633.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5649969.0 spike=4.75
- WKOL.CA: score=12.94 buy_ready=False sector_rank=12 price=329.43 support=321.02 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20047256.0 spike=2.77
- ZEOT.CA: score=15.87 buy_ready=False sector_rank=12 price=11.6 support=10.4 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=71.74 liquidity=3474454.0 spike=0.07
- ZMID.CA: score=24.4 buy_ready=False sector_rank=3 price=7.6 support=6.19 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=78.14 liquidity=112199720.0 spike=0.47

## Backtesting Lite
- OIH.CA: 180d return=30.28%, max drawdown=-14.56%, MA20>MA50 days last20=0, as_of=2026-07-18T21:00:00+00:00
- SPIN.CA: 180d return=39.64%, max drawdown=-9.64%, MA20>MA50 days last20=2, as_of=2026-07-18T21:00:00+00:00
- ARCC.CA: 180d return=42.22%, max drawdown=-12.39%, MA20>MA50 days last20=12, as_of=2026-07-18T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- OIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Investment Holding summary=Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- SPIN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Spinning and Weaving summary=Evidence rejected for SPIN.CA: source text did not clearly match SPIN.CA / Alexandria Spinning and Weaving.
- ARCC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=565 sources=3 expected=Arabian Cement Company summary=Arabian Cement to pay out EGP 2bn dividends for 2025; Arabian Cement’s EGM approves nearly EGP 8m capital cut; Arabian Cement’s consolidated profits near EGP 3.6bn in 2025
  - Arabian Cement to pay out EGP 2bn dividends for 2025: https://english.mubasher.info/news/4587912/Arabian-Cement-to-pay-out-EGP-2bn-dividends-for-2025/
  - Arabian Cement’s EGM approves nearly EGP 8m capital cut: https://english.mubasher.info/news/4583762/Arabian-Cement-s-EGM-approves-nearly-EGP-8m-capital-cut/
  - Arabian Cement’s consolidated profits near EGP 3.6bn in 2025: https://english.mubasher.info/news/4562679/Arabian-Cement-s-consolidated-profits-near-EGP-3-6bn-in-2025/
- SCFM.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=South Cairo and Giza Flour Mills and Bakeries Company summary=South Cairo and Giza Mills targets over EGP 412.5m revenues in FY26/27; South Cairo and Giza Mills turns profitable in 8M-25/26; South Cairo and Giza Mills sells asset for EGP 17m
  - South Cairo and Giza Mills targets over EGP 412.5m revenues in FY26/27: https://english.mubasher.info/news/4583387/South-Cairo-and-Giza-Mills-targets-over-EGP-412-5m-revenues-in-FY26-27/
  - South Cairo and Giza Mills turns profitable in 8M-25/26: https://english.mubasher.info/news/4583237/South-Cairo-and-Giza-Mills-turns-profitable-in-8M-25-26/
  - South Cairo and Giza Mills sells asset for EGP 17m: https://english.mubasher.info/news/4547145/South-Cairo-and-Giza-Mills-sells-asset-for-EGP-17m/
- ELEC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=565 sources=3 expected=Electro Cable Egypt summary=Electro Cable Egypt sees lower profits in 2025; revenues exceed EGP 10.8bn; Mashareq reduces equity in Electro Cable Egypt to 0.77%; Electro Cable Egypt stock is testing significant demand zone, will it succeed to rebound?
  - Electro Cable Egypt sees lower profits in 2025; revenues exceed EGP 10.8bn: https://english.mubasher.info/news/4580607/Electro-Cable-Egypt-sees-lower-profits-in-2025-revenues-exceed-EGP-10-8bn/
  - Mashareq reduces equity in Electro Cable Egypt to 0.77%: https://english.mubasher.info/news/4561520/Mashareq-reduces-equity-in-Electro-Cable-Egypt-to-0-77-/
  - Electro Cable Egypt stock is testing significant demand zone, will it succeed to rebound?: https://english.mubasher.info/news/4556412/Electro-Cable-Egypt-stock-is-testing-significant-demand-zone-will-it-succeed-to-rebound-/
- EDFM.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=East Delta Flour Mills summary=East Delta Flour Mills eyes EGP 68m profits in FY22/23; East Delta Flour Mills sees 5% higher profits in audited financials; East Delta Flour Mills logs EGP 130m profit in FY20/21
  - East Delta Flour Mills eyes EGP 68m profits in FY22/23: https://english.mubasher.info/news/3945288/East-Delta-Flour-Mills-eyes-EGP-68m-profits-in-FY22-23/
  - East Delta Flour Mills sees 5% higher profits in audited financials: https://english.mubasher.info/news/3849218/East-Delta-Flour-Mills-sees-5-higher-profits-in-audited-financials/
  - East Delta Flour Mills logs EGP 130m profit in FY20/21: https://english.mubasher.info/news/3835718/East-Delta-Flour-Mills-logs-EGP-130m-profit-in-FY20-21/
- APSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Unirab Polvara Spinning & Weaving Co. summary=Evidence rejected for APSW.CA: source text did not clearly match APSW.CA / Unirab Polvara Spinning & Weaving Co..
- UEFM.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Upper Egypt Mills Company J.S.C summary=Upper Egypt Mills’ consolidated net profits retreat to EGP 52m in Q1-25/26; Upper Egypt Mills sells previous headquarters in Sohag; Upper Egypt Mills targets EGP 896m revenues in FY22/23
  - Upper Egypt Mills’ consolidated net profits retreat to EGP 52m in Q1-25/26: https://english.mubasher.info/news/4530741/Upper-Egypt-Mills-consolidated-net-profits-retreat-to-EGP-52m-in-Q1-25-26/
  - Upper Egypt Mills sells previous headquarters in Sohag: https://english.mubasher.info/news/4007606/Upper-Egypt-Mills-sells-previous-headquarters-in-Sohag/
  - Upper Egypt Mills targets EGP 896m revenues in FY22/23: https://english.mubasher.info/news/3973984/Upper-Egypt-Mills-targets-EGP-896m-revenues-in-FY22-23/

## Warnings
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Gemini batch evidence failed: Server disconnected without sending a response.
- Evidence rejected for SPIN.CA: source text did not clearly match SPIN.CA / Alexandria Spinning and Weaving.
- Evidence for ARCC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for SCFM.CA matches the company but no source/report date was detected.
- Evidence for ELEC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for EDFM.CA matches the company but no source/report date was detected.
- Evidence rejected for APSW.CA: source text did not clearly match APSW.CA / Unirab Polvara Spinning & Weaving Co..
- Evidence for UEFM.CA matches the company but no source/report date was detected.
