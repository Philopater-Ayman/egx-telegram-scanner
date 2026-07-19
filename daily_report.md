# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-07-19T08:42:22.425690+00:00
Generated Cairo: 2026-07-19 11:42
Run timing: target 09:15 Cairo | generated Cairo 2026-07-19 11:42 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-07-19 11:31

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 70
- Data quality issues: 1
- Tradeable price/liquidity tickers: 173/189
- Top sector: Telecommunications

## Market Context
- Market trend: Unavailable
- Source: Market context unavailable
- As of: None
- Freshness: MISSING
- EGX30 regime: CONSTRUCTIVE / above MA20 70.0% / above MA50 50.0%
- EGX70 regime: BULLISH / above MA20 76.92% / above MA50 76.92%
- Sector breadth: 52.38%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- TMGH.CA: liquidity=796409189.91 spike=2.25 score=28.9
- CCAP.CA: liquidity=326208352.0 spike=0.5 score=24.4
- COMI.CA: liquidity=228553849.54 spike=0.7 score=25.41
- ELEC.CA: liquidity=145984624.0 spike=3.5 score=32.4
- AMER.CA: liquidity=122869384.0 spike=1.35 score=10.1

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 constructive, EGX70 bullish with sector breadth ~52%; scanner prioritized tickets showing accumulation spikes, bullish‑watch outlook, and proximity to resistance, but missing macro data keeps confidence low and risk mode selective.
- Top tickets (ELEC.CA, SWDY.CA, ETEL.CA) scored high on rank_score due to accumulation‑spike liquidity regimes and BULLISH_WATCH outlook, despite extended momentum notes.
- Support/resistance distances are tight (small negative or low positive resistance_distance_pct), indicating limited near‑term upside over the next 1‑3 days.
- Leading sectors Telecommunications and Industrial Goods & Cables show 100% above MA20/50 and elevated liquidity spikes, supporting sector‑driven strength.
- EGX30 constructive and EGX70 bullish breadth maintain risk mode at SELECTIVE_SWING_TRADES_ONLY; the absence of macro source adds uncertainty and keeps confidence LOW.

## Top Liquidity Spikes
- TRTO.CA: spike=42.76 liquidity=43650.6 outlook=WEAK_OR_RISKY score=32.52 buy_ready=False
- EGSA.CA: spike=21.05 liquidity=136145.16 outlook=NEUTRAL score=44 buy_ready=False
- WCDF.CA: spike=18.21 liquidity=7155193.5 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EDFM.CA: spike=15.51 liquidity=17679960.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- BIOC.CA: spike=13.46 liquidity=96938784.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=23.19 5d=-0.38% 20d=3.93% aboveMA50=100.0%
- #2 Industrial Goods & Cables: score=12.26 5d=3.73% 20d=4.46% aboveMA50=100.0%
- #3 Automotive & Distribution: score=9.76 5d=4.05% 20d=9.38% aboveMA50=100.0%
- #4 Transportation & Logistics: score=9.47 5d=3.74% 20d=6.01% aboveMA50=100.0%
- #5 Technology & Distribution: score=8.87 5d=-1.38% 20d=12.55% aboveMA50=100.0%
- #6 Textiles: score=8.71 5d=3.1% 20d=5.94% aboveMA50=100.0%
- #7 Investment Holding: score=8.41 5d=4.22% 20d=6.05% aboveMA50=66.67%
- #8 Real Estate: score=7.42 5d=2.11% 20d=6.44% aboveMA50=92.31%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: macro source is missing, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- SWDY.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- GBCO.CA: BULLISH_WATCH score=89.76 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MTIE.CA: BULLISH_WATCH score=89.76 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- TMGH.CA: BULLISH_WATCH score=89.42 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- ELEC.CA: BULLISH_WATCH score=88 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- ETEL.CA: BULLISH_WATCH score=87 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- BINV.CA: BULLISH_WATCH score=86.41 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- RAYA.CA: BULLISH_WATCH score=84.87 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- CICH.CA: BULLISH_WATCH score=83.96 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- APSW.CA: BULLISH_WATCH score=83.52 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- ELEC.CA: rank=32.4 outlook=BULLISH_WATCH outlook_score=88 sector_rank=2 price=2.29 support=2.04 resistance=2.26 liquidity=145984624.0
- SWDY.CA: rank=29.74 outlook=BULLISH_WATCH outlook_score=100 sector_rank=2 price=93.06 support=84.3 resistance=91.5 liquidity=25001212.0
- CCRS.CA: rank=29.6 outlook=BULLISH_WATCH outlook_score=82.52 sector_rank=11 price=2.55 support=2.18 resistance=2.61 liquidity=20171848.57
- ETEL.CA: rank=29.44 outlook=BULLISH_WATCH outlook_score=87 sector_rank=1 price=98.3 support=89.01 resistance=101.5 liquidity=56383702.15
- SCEM.CA: rank=29.34 outlook=BULLISH_WATCH outlook_score=80.99 sector_rank=16 price=67.0 support=60.14 resistance=67.55 liquidity=34631844.0
- MEPA.CA: rank=28.92 outlook=BULLISH_WATCH outlook_score=82.52 sector_rank=11 price=1.74 support=1.52 resistance=1.74 liquidity=30673456.0
- TMGH.CA: rank=28.9 outlook=BULLISH_WATCH outlook_score=89.42 sector_rank=8 price=101.15 support=92.1 resistance=103.5 liquidity=796409189.91
- NCCW.CA: rank=27.6 outlook=BULLISH_WATCH outlook_score=82.52 sector_rank=11 price=6.81 support=5.82 resistance=6.97 liquidity=35826740.0
- ICID.CA: rank=26.86 outlook=BULLISH_WATCH outlook_score=74.52 sector_rank=11 price=8.36 support=6.55 resistance=8.7 liquidity=10126495.0
- GBCO.CA: rank=26.76 outlook=BULLISH_WATCH outlook_score=89.76 sector_rank=3 price=32.53 support=28.33 resistance=34.2 liquidity=9362807.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=20.0 buy_ready=True sector_rank=11 price=231.94 support=196.0 resistance=247.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=65.64 liquidity=5603253.0 spike=0.38
- ABUK.CA: score=25.04 buy_ready=False sector_rank=14 price=74.5 support=66.66 resistance=73.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=64.47 liquidity=94162176.0 spike=0.57
- ACAMD.CA: score=22.4 buy_ready=True sector_rank=11 price=2.31 support=2.14 resistance=2.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=68.97 liquidity=25851372.0 spike=0.34
- ACGC.CA: score=18.55 buy_ready=True sector_rank=6 price=9.89 support=8.92 resistance=10.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=69.83 liquidity=2149266.25 spike=0.11
- ADCI.CA: score=16.37 buy_ready=True sector_rank=11 price=240.0 support=227.1 resistance=249.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=47.48 liquidity=1969265.5 spike=0.17
- ADIB.CA: score=20.41 buy_ready=False sector_rank=18 price=46.62 support=44.1 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=60.68 liquidity=17918116.0 spike=0.19
- ADPC.CA: score=16.78 buy_ready=False sector_rank=11 price=3.83 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=75.71 liquidity=5379363.0 spike=0.23
- AFDI.CA: score=18.46 buy_ready=True sector_rank=11 price=47.82 support=41.84 resistance=48.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=62.02 liquidity=2063994.25 spike=0.14
- AFMC.CA: score=14.4 buy_ready=False sector_rank=11 price=91.05 support=77.25 resistance=91.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=38689424.0 spike=7.98
- AJWA.CA: score=15.53 buy_ready=False sector_rank=11 price=176.41 support=172.1 resistance=192.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=50.7 liquidity=3127140.75 spike=0.19
- ALCN.CA: score=24.4 buy_ready=True sector_rank=4 price=30.02 support=27.7 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=68.27 liquidity=12651455.0 spike=0.63
- ALUM.CA: score=20.55 buy_ready=True sector_rank=11 price=23.45 support=20.55 resistance=23.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=63.41 liquidity=4148132.25 spike=0.68
- AMER.CA: score=10.1 buy_ready=False sector_rank=8 price=4.42 support=3.92 resistance=4.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=122869384.0 spike=1.35
- AMES.CA: score=21.4 buy_ready=False sector_rank=11 price=120.23 support=45.15 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=76.15 liquidity=45958848.0 spike=0.56
- AMIA.CA: score=18.23 buy_ready=True sector_rank=11 price=9.59 support=8.4 resistance=9.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=67.72 liquidity=1827031.38 spike=0.18
- AMOC.CA: score=24.4 buy_ready=True sector_rank=9 price=8.35 support=7.42 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=66.49 liquidity=35440620.0 spike=0.62
- APSW.CA: score=21.06 buy_ready=True sector_rank=11 price=8.84 support=8.0 resistance=8.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=48.41 liquidity=2484007.75 spike=2.59
- ARAB.CA: score=21.4 buy_ready=False sector_rank=8 price=0.25 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=81.33 liquidity=27858140.0 spike=0.26
- ARCC.CA: score=15.62 buy_ready=False sector_rank=16 price=55.28 support=53.0 resistance=56.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=50.35 liquidity=6620448.5 spike=0.35
- AREH.CA: score=22.4 buy_ready=False sector_rank=11 price=1.52 support=1.51 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=10927588.0 spike=0.29
- ARVA.CA: score=24.54 buy_ready=True sector_rank=11 price=10.96 support=10.5 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=38.71 liquidity=18365922.0 spike=1.07
- ASCM.CA: score=24.4 buy_ready=True sector_rank=11 price=62.51 support=56.29 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=57.2 liquidity=12350049.0 spike=0.17
- ASPI.CA: score=26.62 buy_ready=False sector_rank=11 price=0.34 support=0.3 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=71.26 liquidity=25891328.0 spike=1.11
- ATLC.CA: score=13.21 buy_ready=False sector_rank=12 price=5.2 support=4.92 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=47.71 liquidity=830702.63 spike=0.1
- ATQA.CA: score=26.04 buy_ready=True sector_rank=14 price=9.74 support=9.21 resistance=9.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=55.77 liquidity=11338027.0 spike=0.38
- AXPH.CA: score=17.21 buy_ready=False sector_rank=11 price=1227.88 support=1075.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=72.72 liquidity=814245.94 spike=0.22
- BINV.CA: score=20.75 buy_ready=True sector_rank=7 price=49.35 support=45.01 resistance=51.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=58.33 liquidity=2352623.5 spike=0.34
- BIOC.CA: score=14.4 buy_ready=False sector_rank=11 price=118.98 support=111.11 resistance=126.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=96938784.0 spike=13.46
- BTFH.CA: score=26.38 buy_ready=True sector_rank=12 price=3.11 support=2.91 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=57.89 liquidity=94485760.0 spike=0.47
- CAED.CA: score=23.4 buy_ready=False sector_rank=11 price=107.62 support=68.0 resistance=127.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=94.09 liquidity=29532666.0 spike=0.91
- CANA.CA: score=9.32 buy_ready=False sector_rank=18 price=35.82 support=34.7 resistance=38.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=56.08 liquidity=1911385.38 spike=0.17
- CCAP.CA: score=24.4 buy_ready=False sector_rank=7 price=5.53 support=4.65 resistance=5.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=74.34 liquidity=326208352.0 spike=0.5
- CCRS.CA: score=29.6 buy_ready=True sector_rank=11 price=2.55 support=2.18 resistance=2.61 source=Yahoo Finance as_of=2026-07-15T21:00:00+00:00 freshness=FRESH RSI=62.67 liquidity=20171848.57 spike=1.6
- CEFM.CA: score=14.4 buy_ready=False sector_rank=11 price=124.37 support=108.01 resistance=128.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=34855484.0 spike=13.23
- CERA.CA: score=23.4 buy_ready=False sector_rank=11 price=1.39 support=1.19 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=76.47 liquidity=17733842.0 spike=0.68
- CFGH.CA: score=15.44 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-15T21:00:00+00:00 freshness=FRESH RSI=60.0 liquidity=37322.69 spike=4.15
- CICH.CA: score=25.8 buy_ready=True sector_rank=12 price=12.25 support=11.52 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=55.98 liquidity=6554455.0 spike=1.43
- CIEB.CA: score=18.82 buy_ready=True sector_rank=18 price=24.1 support=23.3 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=54.42 liquidity=3407646.5 spike=0.49
- CIRA.CA: score=20.7 buy_ready=False sector_rank=15 price=31.6 support=26.3 resistance=33.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=73.6 liquidity=6690420.0 spike=0.19
- CLHO.CA: score=19.54 buy_ready=True sector_rank=10 price=16.62 support=15.5 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=49.24 liquidity=5142761.0 spike=0.11
- CNFN.CA: score=20.65 buy_ready=True sector_rank=12 price=4.88 support=4.4 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=55.22 liquidity=4268876.0 spike=0.09
- COMI.CA: score=25.41 buy_ready=True sector_rank=18 price=135.8 support=126.21 resistance=137.98 source=Yahoo Finance as_of=2026-07-15T21:00:00+00:00 freshness=FRESH RSI=56.01 liquidity=228553849.54 spike=0.7
- COPR.CA: score=18.02 buy_ready=True sector_rank=11 price=0.38 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=61.82 liquidity=2616501.75 spike=0.12
- COSG.CA: score=24.66 buy_ready=False sector_rank=11 price=1.66 support=1.47 resistance=1.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=71.88 liquidity=8260302.0 spike=0.21
- CPCI.CA: score=17.51 buy_ready=False sector_rank=11 price=460.53 support=362.52 resistance=512.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=72.7 liquidity=3114730.5 spike=0.3
- CSAG.CA: score=24.21 buy_ready=False sector_rank=4 price=33.68 support=30.87 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=74.77 liquidity=7807914.5 spike=0.4
- DAPH.CA: score=17.57 buy_ready=True sector_rank=11 price=85.49 support=78.52 resistance=87.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=58.08 liquidity=1166447.63 spike=0.11
- DEIN.CA: score=-0.6 buy_ready=False sector_rank=11 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=14.3 buy_ready=True sector_rank=19 price=27.07 support=24.47 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=51.97 liquidity=1062930.13 spike=0.21
- DSCW.CA: score=24.0 buy_ready=False sector_rank=11 price=1.95 support=1.71 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=79.31 liquidity=51067108.0 spike=1.3
- DTPP.CA: score=25.7 buy_ready=False sector_rank=11 price=252.59 support=114.67 resistance=242.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=87.55 liquidity=99290408.0 spike=2.15
- EALR.CA: score=18.63 buy_ready=True sector_rank=11 price=368.11 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=56.74 liquidity=2228621.5 spike=0.17
- EASB.CA: score=9.27 buy_ready=False sector_rank=11 price=7.17 support=6.88 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=26.0 liquidity=1870580.13 spike=0.1
- EAST.CA: score=6.53 buy_ready=False sector_rank=19 price=36.87 support=36.11 resistance=39.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=33.81 liquidity=4289581.5 spike=0.09
- EBSC.CA: score=13.54 buy_ready=False sector_rank=11 price=1.89 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=57.33 liquidity=1144820.88 spike=0.17
- ECAP.CA: score=13.66 buy_ready=False sector_rank=11 price=32.44 support=31.52 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=39.2 liquidity=1262314.13 spike=0.15
- EDFM.CA: score=14.4 buy_ready=False sector_rank=11 price=408.71 support=373.01 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17679960.0 spike=15.51
- EEII.CA: score=16.84 buy_ready=True sector_rank=11 price=2.77 support=2.35 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=69.57 liquidity=2439499.75 spike=0.12
- EFIC.CA: score=20.66 buy_ready=False sector_rank=14 price=192.77 support=180.02 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=41.27 liquidity=8097172.0 spike=1.26
- EFID.CA: score=19.76 buy_ready=False sector_rank=19 price=27.79 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=61.47 liquidity=9519455.0 spike=0.2
- EFIH.CA: score=26.14 buy_ready=True sector_rank=13 price=22.23 support=20.0 resistance=23.65 source=Yahoo Finance as_of=2026-07-15T21:00:00+00:00 freshness=FRESH RSI=61.6 liquidity=20902290.59 spike=0.57
- EGAL.CA: score=24.08 buy_ready=True sector_rank=14 price=311.29 support=272.28 resistance=306.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=68.21 liquidity=49383120.0 spike=1.02
- EGAS.CA: score=19.89 buy_ready=True sector_rank=9 price=53.55 support=46.51 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=63.0 liquidity=3485189.0 spike=0.31
- EGBE.CA: score=12.42 buy_ready=False sector_rank=18 price=0.45 support=-0.34 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:45 AM market time freshness=DELAYED_CURRENT RSI=96.8 liquidity=10145.86 spike=-0.42
- EGCH.CA: score=23.04 buy_ready=False sector_rank=14 price=13.4 support=12.13 resistance=13.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=58.4 liquidity=12721985.0 spike=0.25
- EGSA.CA: score=22.54 buy_ready=False sector_rank=1 price=8.97 support=8.67 resistance=9.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 July 12:04 PM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=136145.16 spike=21.05
- EGTS.CA: score=26.4 buy_ready=True sector_rank=8 price=18.2 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=62.7 liquidity=15661530.0 spike=0.32
- EHDR.CA: score=26.23 buy_ready=True sector_rank=11 price=2.71 support=2.37 resistance=2.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=59.21 liquidity=9833705.0 spike=0.32
- EKHO.CA: score=8.4 buy_ready=False sector_rank=9 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=32.4 buy_ready=True sector_rank=2 price=2.29 support=2.04 resistance=2.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=63.89 liquidity=145984624.0 spike=3.5
- ELKA.CA: score=9.4 buy_ready=False sector_rank=11 price=2.17 support=1.96 resistance=2.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51873468.0 spike=0.86
- ELNA.CA: score=9.04 buy_ready=False sector_rank=11 price=38.05 support=35.55 resistance=40.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=66.63 liquidity=579280.31 spike=1.03
- ELSH.CA: score=24.4 buy_ready=False sector_rank=11 price=14.3 support=11.1 resistance=15.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=72.28 liquidity=13848077.0 spike=0.1
- ELWA.CA: score=16.75 buy_ready=False sector_rank=11 price=2.02 support=1.87 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=353153.06 spike=0.24
- EMFD.CA: score=17.77 buy_ready=False sector_rank=8 price=11.79 support=11.24 resistance=12.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=49.09 liquidity=5373651.0 spike=0.05
- ENGC.CA: score=12.85 buy_ready=False sector_rank=11 price=41.39 support=33.91 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=75.34 liquidity=1451669.25 spike=0.06
- EOSB.CA: score=14.43 buy_ready=False sector_rank=11 price=1.48 support=1.48 resistance=1.55 source=Yahoo Finance as_of=2026-07-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=25535.92 spike=0.47
- EPCO.CA: score=19.71 buy_ready=False sector_rank=11 price=10.51 support=8.5 resistance=11.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=76.84 liquidity=8313773.5 spike=0.44
- EPPK.CA: score=16.96 buy_ready=False sector_rank=11 price=15.19 support=12.31 resistance=15.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=74.4 liquidity=557446.06 spike=0.51
- ETEL.CA: score=29.44 buy_ready=True sector_rank=1 price=98.3 support=89.01 resistance=101.5 source=Yahoo Finance as_of=2026-07-15T21:00:00+00:00 freshness=FRESH RSI=62.28 liquidity=56383702.15 spike=1.02
- ETRS.CA: score=17.55 buy_ready=True sector_rank=11 price=10.83 support=9.97 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=3154639.75 spike=0.05
- EXPA.CA: score=23.18 buy_ready=False sector_rank=18 price=19.52 support=18.03 resistance=19.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=72.54 liquidity=7774510.0 spike=0.3
- FAIT.CA: score=18.81 buy_ready=True sector_rank=18 price=37.51 support=35.06 resistance=37.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=62.06 liquidity=1401305.25 spike=0.52
- FAITA.CA: score=12.75 buy_ready=False sector_rank=18 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-07-15T21:00:00+00:00 freshness=FRESH RSI=42.25 liquidity=101280.48 spike=3.12
- FERC.CA: score=17.1 buy_ready=True sector_rank=14 price=76.94 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=53.78 liquidity=2055120.13 spike=0.46
- FWRY.CA: score=23.14 buy_ready=False sector_rank=13 price=18.9 support=18.13 resistance=19.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=55.35 liquidity=16454652.0 spike=0.1
- GBCO.CA: score=26.76 buy_ready=True sector_rank=3 price=32.53 support=28.33 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=58.96 liquidity=9362807.0 spike=0.12
- GDWA.CA: score=22.4 buy_ready=False sector_rank=11 price=0.85 support=0.76 resistance=0.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=76.09 liquidity=15352976.0 spike=0.48
- GGCC.CA: score=9.4 buy_ready=False sector_rank=11 price=0.79 support=0.73 resistance=0.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24073246.0 spike=0.99
- GIHD.CA: score=20.82 buy_ready=True sector_rank=11 price=50.0 support=40.66 resistance=55.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=63.56 liquidity=4415915.5 spike=0.14
- GMCI.CA: score=15.29 buy_ready=False sector_rank=11 price=2.02 support=1.66 resistance=2.26 source=Yahoo Finance as_of=2026-07-15T21:00:00+00:00 freshness=FRESH RSI=70.13 liquidity=888711.11 spike=0.79
- GRCA.CA: score=9.44 buy_ready=False sector_rank=11 price=58.7 support=55.0 resistance=59.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7876772.0 spike=2.08
- GSSC.CA: score=14.4 buy_ready=False sector_rank=11 price=283.14 support=264.0 resistance=288.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=50821708.0 spike=9.88
- GTWL.CA: score=24.4 buy_ready=False sector_rank=11 price=98.8 support=47.85 resistance=117.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=74.55 liquidity=37780308.0 spike=0.32
- HDBK.CA: score=7.38 buy_ready=False sector_rank=18 price=77.32 support=75.3 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=9.0 liquidity=4967484.0 spike=0.12
- HELI.CA: score=23.4 buy_ready=False sector_rank=8 price=7.77 support=6.36 resistance=7.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=82.72 liquidity=12520492.0 spike=0.07
- HRHO.CA: score=18.38 buy_ready=False sector_rank=12 price=26.74 support=26.09 resistance=27.66 source=Yahoo Finance as_of=2026-07-15T21:00:00+00:00 freshness=FRESH RSI=48.05 liquidity=89737861.57 spike=0.91
- ICID.CA: score=26.86 buy_ready=True sector_rank=11 price=8.36 support=6.55 resistance=8.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=55.93 liquidity=10126495.0 spike=1.23
- IDRE.CA: score=19.21 buy_ready=True sector_rank=11 price=44.8 support=41.1 resistance=47.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=53.78 liquidity=2813683.0 spike=0.2
- IFAP.CA: score=18.76 buy_ready=False sector_rank=17 price=19.5 support=18.47 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=48.29 liquidity=5618856.0 spike=1.23
- INFI.CA: score=23.1 buy_ready=True sector_rank=11 price=104.53 support=88.51 resistance=106.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=66.37 liquidity=8697405.0 spike=0.84
- IRON.CA: score=10.87 buy_ready=False sector_rank=14 price=31.62 support=30.45 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=52.81 liquidity=2830615.75 spike=0.38
- ISMA.CA: score=17.4 buy_ready=False sector_rank=11 price=27.9 support=26.54 resistance=30.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=25.06 liquidity=12508502.0 spike=0.56
- ISMQ.CA: score=24.04 buy_ready=True sector_rank=14 price=9.35 support=8.06 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=63.91 liquidity=14486866.0 spike=0.11
- ISPH.CA: score=19.4 buy_ready=False sector_rank=10 price=11.5 support=11.2 resistance=12.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=36.97 liquidity=27960392.0 spike=0.51
- JUFO.CA: score=17.98 buy_ready=False sector_rank=19 price=29.71 support=29.1 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=45.42 liquidity=6743683.5 spike=0.32
- KABO.CA: score=19.32 buy_ready=False sector_rank=6 price=7.63 support=6.04 resistance=7.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=93.14 liquidity=7921359.5 spike=0.24
- KWIN.CA: score=24.1 buy_ready=False sector_rank=11 price=84.71 support=65.0 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=76.93 liquidity=32359556.0 spike=1.35
- KZPC.CA: score=13.46 buy_ready=False sector_rank=11 price=8.72 support=8.26 resistance=9.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=50.83 liquidity=1057623.13 spike=0.19
- LCSW.CA: score=20.21 buy_ready=True sector_rank=16 price=32.0 support=27.01 resistance=33.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=63.04 liquidity=4214158.5 spike=0.06
- LUTS.CA: score=22.4 buy_ready=False sector_rank=11 price=0.74 support=0.69 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=63.26 liquidity=11870621.0 spike=0.26
- MAAL.CA: score=17.37 buy_ready=False sector_rank=11 price=8.63 support=6.25 resistance=8.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=92.96 liquidity=3968308.5 spike=0.22
- MASR.CA: score=23.4 buy_ready=False sector_rank=11 price=8.24 support=6.71 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=78.97 liquidity=22925590.0 spike=0.27
- MBSC.CA: score=11.42 buy_ready=False sector_rank=16 price=241.34 support=222.66 resistance=253.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=47.35 liquidity=2422131.5 spike=0.12
- MCQE.CA: score=21.0 buy_ready=False sector_rank=16 price=181.73 support=166.66 resistance=182.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=70.43 liquidity=11193914.0 spike=0.89
- MCRO.CA: score=23.4 buy_ready=True sector_rank=11 price=1.36 support=1.17 resistance=1.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=23557864.0 spike=0.43
- MENA.CA: score=17.16 buy_ready=True sector_rank=8 price=7.21 support=6.59 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=61.08 liquidity=2762415.75 spike=0.38
- MEPA.CA: score=28.92 buy_ready=True sector_rank=11 price=1.74 support=1.52 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=67.65 liquidity=30673456.0 spike=2.26
- MFPC.CA: score=23.04 buy_ready=False sector_rank=14 price=38.38 support=34.22 resistance=38.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=62.92 liquidity=30924934.0 spike=0.3
- MFSC.CA: score=10.21 buy_ready=False sector_rank=11 price=46.72 support=44.22 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=35.49 liquidity=805214.31 spike=0.1
- MHOT.CA: score=0.37 buy_ready=False sector_rank=21 price=16.39 support=16.12 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=5.18 liquidity=965600.56 spike=0.06
- MICH.CA: score=21.7 buy_ready=True sector_rank=11 price=38.5 support=34.0 resistance=39.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=54.09 liquidity=7298105.5 spike=0.58
- MILS.CA: score=14.4 buy_ready=False sector_rank=11 price=162.95 support=140.1 resistance=165.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=108741440.0 spike=9.42
- MIPH.CA: score=15.68 buy_ready=False sector_rank=10 price=771.92 support=630.13 resistance=762.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=87.68 liquidity=2283342.25 spike=0.67
- MOED.CA: score=16.65 buy_ready=True sector_rank=11 price=0.72 support=0.65 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=68.87 liquidity=6254905.0 spike=0.45
- MOIL.CA: score=16.43 buy_ready=False sector_rank=9 price=0.55 support=0.46 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:58 AM market time freshness=DELAYED_CURRENT RSI=73.1 liquidity=25044.43 spike=0.07
- MOIN.CA: score=10.54 buy_ready=False sector_rank=11 price=24.04 support=22.6 resistance=24.76 source=Yahoo Finance as_of=2026-07-15T21:00:00+00:00 freshness=FRESH RSI=65.07 liquidity=142220.65 spike=0.18
- MOSC.CA: score=18.85 buy_ready=True sector_rank=11 price=283.34 support=250.0 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=59.41 liquidity=2451895.0 spike=0.18
- MPCI.CA: score=24.4 buy_ready=True sector_rank=11 price=247.0 support=220.97 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=55.55 liquidity=25646790.0 spike=0.27
- MPCO.CA: score=23.68 buy_ready=True sector_rank=17 price=1.87 support=1.7 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=52.27 liquidity=10485652.0 spike=0.12
- MPRC.CA: score=15.7 buy_ready=False sector_rank=11 price=43.76 support=31.74 resistance=44.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=83.33 liquidity=2299161.5 spike=0.05
- MTIE.CA: score=22.87 buy_ready=True sector_rank=3 price=9.47 support=8.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=61.35 liquidity=5468457.5 spike=0.23
- NAHO.CA: score=8.67 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-15T21:00:00+00:00 freshness=FRESH RSI=42.86 liquidity=26850.76 spike=1.12
- NCCW.CA: score=27.6 buy_ready=True sector_rank=11 price=6.81 support=5.82 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=60.73 liquidity=35826740.0 spike=1.6
- NEDA.CA: score=20.4 buy_ready=False sector_rank=11 price=2.9 support=2.7 resistance=3.02 source=Yahoo Finance as_of=2026-07-15T21:00:00+00:00 freshness=FRESH RSI=75.0 liquidity=1757147.76 spike=3.12
- NHPS.CA: score=21.4 buy_ready=False sector_rank=11 price=88.58 support=61.55 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=83.27 liquidity=21596266.0 spike=0.35
- NINH.CA: score=23.82 buy_ready=False sector_rank=11 price=21.04 support=17.12 resistance=22.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=80.1 liquidity=32727802.0 spike=1.21
- NIPH.CA: score=23.4 buy_ready=False sector_rank=10 price=195.91 support=157.01 resistance=198.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=76.25 liquidity=36498068.0 spike=0.33
- OBRI.CA: score=25.49 buy_ready=True sector_rank=11 price=36.51 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=58.61 liquidity=9088616.0 spike=0.28
- OCDI.CA: score=21.21 buy_ready=False sector_rank=8 price=28.2 support=20.71 resistance=28.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=70.33 liquidity=4812767.5 spike=0.04
- OCPH.CA: score=21.3 buy_ready=False sector_rank=11 price=425.62 support=337.0 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=90.78 liquidity=7900005.0 spike=0.4
- ODIN.CA: score=15.36 buy_ready=False sector_rank=11 price=2.46 support=2.05 resistance=2.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=75.34 liquidity=3964908.25 spike=0.26
- OFH.CA: score=23.4 buy_ready=False sector_rank=11 price=0.7 support=0.57 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=84.52 liquidity=24521780.0 spike=0.54
- OIH.CA: score=24.31 buy_ready=False sector_rank=7 price=1.42 support=1.35 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=8910385.0 spike=0.14
- OLFI.CA: score=13.13 buy_ready=False sector_rank=19 price=22.93 support=21.0 resistance=23.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=76.49 liquidity=2896270.5 spike=0.09
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=714.99 support=703.98 resistance=715.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=41585520.0 spike=1.0
- ORHD.CA: score=24.4 buy_ready=True sector_rank=8 price=38.83 support=37.0 resistance=40.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=52.97 liquidity=18678512.0 spike=0.12
- ORWE.CA: score=25.09 buy_ready=True sector_rank=6 price=23.18 support=21.95 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=56.69 liquidity=8688867.0 spike=0.45
- PHAR.CA: score=26.4 buy_ready=True sector_rank=10 price=89.51 support=83.6 resistance=90.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=51.65 liquidity=22620020.0 spike=0.85
- PHDC.CA: score=22.4 buy_ready=False sector_rank=8 price=14.88 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=44.95 liquidity=42062856.0 spike=0.14
- PHTV.CA: score=11.94 buy_ready=False sector_rank=11 price=309.47 support=216.31 resistance=308.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=81.29 liquidity=540758.75 spike=0.04
- POUL.CA: score=14.92 buy_ready=True sector_rank=19 price=39.12 support=35.28 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=55.54 liquidity=1679479.13 spike=0.04
- PRCL.CA: score=19.0 buy_ready=False sector_rank=16 price=36.9 support=24.5 resistance=36.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=75.35 liquidity=34884188.0 spike=0.72
- PRDC.CA: score=21.4 buy_ready=False sector_rank=8 price=9.8 support=6.67 resistance=9.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=77.68 liquidity=50443860.0 spike=0.45
- PRMH.CA: score=19.69 buy_ready=True sector_rank=11 price=2.75 support=2.34 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=64.38 liquidity=3294193.75 spike=0.14
- RACC.CA: score=21.34 buy_ready=True sector_rank=11 price=10.11 support=9.36 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=58.09 liquidity=4938397.5 spike=0.26
- RAKT.CA: score=14.54 buy_ready=False sector_rank=11 price=22.0 support=21.25 resistance=23.79 source=Yahoo Finance as_of=2026-07-15T21:00:00+00:00 freshness=FRESH RSI=38.36 liquidity=759154.0 spike=2.69
- RAYA.CA: score=26.4 buy_ready=True sector_rank=5 price=7.73 support=6.99 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=58.72 liquidity=73939176.0 spike=0.61
- RMDA.CA: score=12.79 buy_ready=False sector_rank=10 price=4.96 support=4.81 resistance=5.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=3393730.75 spike=0.18
- ROTO.CA: score=16.49 buy_ready=False sector_rank=11 price=41.18 support=38.0 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=49.25 liquidity=4088188.0 spike=0.12
- RREI.CA: score=15.79 buy_ready=False sector_rank=11 price=3.89 support=3.34 resistance=4.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=88.71 liquidity=4390571.0 spike=0.16
- RTVC.CA: score=14.51 buy_ready=False sector_rank=11 price=3.94 support=3.55 resistance=3.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=79.31 liquidity=1111071.13 spike=0.28
- RUBX.CA: score=20.02 buy_ready=False sector_rank=11 price=13.78 support=9.96 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=77.09 liquidity=8621490.0 spike=0.12
- SAUD.CA: score=13.53 buy_ready=False sector_rank=18 price=21.43 support=19.99 resistance=22.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=56.51 liquidity=1124218.38 spike=0.21
- SCEM.CA: score=29.34 buy_ready=True sector_rank=16 price=67.0 support=60.14 resistance=67.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=64.9 liquidity=34631844.0 spike=1.67
- SCFM.CA: score=14.4 buy_ready=False sector_rank=11 price=292.84 support=258.0 resistance=308.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=59633784.0 spike=10.54
- SCTS.CA: score=15.05 buy_ready=False sector_rank=15 price=607.62 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=62.05 liquidity=2045080.0 spike=0.4
- SDTI.CA: score=17.01 buy_ready=True sector_rank=11 price=47.19 support=45.55 resistance=49.5 source=Yahoo Finance as_of=2026-07-15T21:00:00+00:00 freshness=FRESH RSI=51.75 liquidity=2610928.24 spike=0.53
- SEIG.CA: score=16.47 buy_ready=False sector_rank=11 price=245.14 support=182.01 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=73.33 liquidity=2065655.13 spike=0.09
- SIPC.CA: score=24.88 buy_ready=True sector_rank=11 price=3.78 support=3.25 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=68.37 liquidity=8475264.0 spike=0.69
- SKPC.CA: score=22.04 buy_ready=False sector_rank=14 price=16.3 support=14.8 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=52.84 liquidity=17632572.0 spike=0.53
- SMFR.CA: score=28.8 buy_ready=False sector_rank=11 price=246.87 support=187.01 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=72.78 liquidity=47217732.0 spike=3.2
- SNFC.CA: score=12.74 buy_ready=False sector_rank=11 price=11.34 support=11.26 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=35.0 liquidity=3341643.75 spike=0.3
- SPIN.CA: score=14.72 buy_ready=False sector_rank=6 price=14.7 support=13.8 resistance=14.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=78.45 liquidity=1324782.25 spike=0.14
- SPMD.CA: score=22.33 buy_ready=True sector_rank=11 price=0.45 support=0.41 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=68.85 liquidity=7929563.5 spike=0.43
- SUGR.CA: score=11.73 buy_ready=False sector_rank=19 price=46.93 support=45.31 resistance=48.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=48.35 liquidity=2492643.75 spike=0.51
- SVCE.CA: score=20.12 buy_ready=True sector_rank=11 price=9.34 support=8.76 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=52.03 liquidity=5723892.5 spike=0.08
- SWDY.CA: score=29.74 buy_ready=True sector_rank=2 price=93.06 support=84.3 resistance=91.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=66.59 liquidity=25001212.0 spike=1.67
- TALM.CA: score=11.44 buy_ready=False sector_rank=15 price=15.77 support=15.27 resistance=16.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=46.45 liquidity=2430357.5 spike=0.19
- TMGH.CA: score=28.9 buy_ready=True sector_rank=8 price=101.15 support=92.1 resistance=103.5 source=Yahoo Finance as_of=2026-07-15T21:00:00+00:00 freshness=FRESH RSI=65.72 liquidity=796409189.91 spike=2.25
- TRTO.CA: score=15.44 buy_ready=False sector_rank=11 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 July 10:45 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=43650.6 spike=42.76
- UEFM.CA: score=14.4 buy_ready=False sector_rank=11 price=561.08 support=520.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17509310.0 spike=9.73
- UEGC.CA: score=9.4 buy_ready=False sector_rank=11 price=2.28 support=2.17 resistance=2.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=34553772.0 spike=0.99
- UNIP.CA: score=17.83 buy_ready=False sector_rank=11 price=0.36 support=0.29 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=73.27 liquidity=3429777.0 spike=0.2
- UNIT.CA: score=14.34 buy_ready=False sector_rank=8 price=19.62 support=12.0 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=76.14 liquidity=2944795.0 spike=0.11
- WCDF.CA: score=11.56 buy_ready=False sector_rank=11 price=601.48 support=523.3 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7155193.5 spike=18.21
- WKOL.CA: score=17.93 buy_ready=True sector_rank=11 price=312.7 support=273.1 resistance=334.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=63.2 liquidity=1529727.13 spike=0.21
- ZEOT.CA: score=18.5 buy_ready=True sector_rank=11 price=11.6 support=10.4 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=62.07 liquidity=4104626.5 spike=0.08
- ZMID.CA: score=26.4 buy_ready=False sector_rank=8 price=7.48 support=6.17 resistance=7.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=28532116.0 spike=0.12

## Backtesting Lite
- ELEC.CA: 180d return=-21.99%, max drawdown=-35.96%, MA20>MA50 days last20=0, as_of=2026-07-15T21:00:00+00:00
- SWDY.CA: 180d return=22.99%, max drawdown=-20.2%, MA20>MA50 days last20=15, as_of=2026-07-15T21:00:00+00:00
- CCRS.CA: 180d return=63.46%, max drawdown=-34.85%, MA20>MA50 days last20=20, as_of=2026-07-15T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ELEC.CA: status=RECENT_ACCEPTED latest=2026-07-05 age_days=14 sources=3 expected=Electro Cable Egypt summary=Electro Cable Egypt (ELEC.CA) has reported consolidated losses in Q1 2026 and a significant decrease in consolidated profits for 2025. Recent market activities include block-trading deals and changes in major shareholder stakes. The company's financial statements for Q1 2026 were released in June 2026.
  - Alhsn for Consulting cuts stake in Electro Cable Egypt to 19.8% (July 5, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVF9mffyOJH1FU1AzD9clsNMn20qhzhpR9wwZ33wfiwTBC5L4WWAI5WkbWvsJCBX5OlCs4o6-u-ndJ8FSU-F-hnJdyHUiTm1JX-HWwdiKBifWOxTUSFLOvDm8ntFIOUIFgeOJoDyo36qiubHb3I9O6
  - Electro Cable incurs consolidated losses in Q1 2026 (June 30, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVF9mffyOJH1FU1AzD9clsNMn20qhzhpR9wwZ33wfiwTBC5L4WWAI5WkbWvsJCBX5OlCs4o6-u-ndJ8FSU-F-hnJdyHUiTm1JX-HWwdiKBifWOxTUSFLOvDm8ntFIOUIFgeOJoDyo36qiubHb3I9O6
  - Electro Cable Egypt sees EGP 87.3M block-trading deal on April 16th (April 16, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVF9mffyOJH1FU1AzD9clsNMn20qhzhpR9wwZ33wfiwTBC5L4WWAI5WkbWvsJCBX5OlCs4o6-u-ndJ8FSU-F-hnJdyHUiTm1JX-HWwdiKBifWOxTUSFLOvDm8ntFIOUIFgeOJoDyo36qiubHb3I9O6
- SWDY.CA: status=RECENT_ACCEPTED latest=2026-07-13 age_days=6 sources=3 expected=Elsewedy Electric summary=Elsewedy Electric (SWDY.CA) has been active with corporate disclosures, including changes in its Board of Directors and shareholder structure. The company reported strong Q1 2026 consolidated revenues and significant consolidated profits for 2025. Recent project developments include power transformation in KSA and a new contract for a compound in New Cairo. An acquisition of a significant stake by Electra Investment Holding was completed in July 2024, with related news extending into the last 12 months.
  - ELSWEDY ELECTRIC (SWDY.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 13, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4kpooaQKzsRSQpFOCt_ycGkkJvZ-QlCw4By2o376uwViwDhGPyfcdhXNBG83FUhxPSnmh93GPP_AW_UmkRujXzpNHlVipfhneY_pJ3Wy79WWByzK6h_9RnlS1qutyyzLRL4zy1kGSnLHkcP5wy78
  - Release from El sewedy Electric (SWDY.CA) Concerning Company's Projects (June 25, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4kpooaQKzsRSQpFOCt_ycGkkJvZ-QlCw4By2o376uwViwDhGPyfcdhXNBG83FUhxPSnmh93GPP_AW_UmkRujXzpNHlVipfhneY_pJ3Wy79WWByzK6h_9RnlS1qutyyzLRL4zy1kGSnLHkcP5wy78
  - Elsewedy Electric's consolidated revenues total EGP 75.2bn in Q1-26 (Financial Results): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4kpooaQKzsRSQpFOCt_ycGkkJvZ-QlCw4By2o376uwViwDhGPyfcdhXNBG83FUhxPSnmh93GPP_AW_UmkRujXzpNHlVipfhneY_pJ3Wy79WWByzK6h_9RnlS1qutyyzLRL4zy1kGSnLHkcP5wy78
- CCRS.CA: status=RECENT_ACCEPTED latest=2026-06-02 age_days=47 sources=3 expected=Gulf Canadian Company for Arab Real Estate Investment summary=Gulf Canadian Company for Arab Real Estate Investment (CCRS.CA) has held its Annual General Meeting in April 2026 and made recent disclosures regarding its Board of Directors. The company reported positive net income for the last quarter and has seen significant stock price increases over the past year.
  - Release from Gulf Canadian Real Estate Investment Co. (CCRS.CA) Regarding a Disclosure Form (June 2, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFaQ7xrgZgbVfpSil-IXbIplcHuZq7JQQGi0bnAUXfh5Bfj3CBk4LE_64zmB-XG0k00QJKu7DKSYCz3RYqGMxyqEaRlNiYNBgWVR12YRBDaqpE7THR0VSN6qizOppKqhD7QMjHcoTxcDsfMPf7W080
  - Gulf Canadian Real Estate Investment Co. (CCRS.CA) - Board of Directors' Decisions (June 1, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFaQ7xrgZgbVfpSil-IXbIplcHuZq7JQQGi0bnAUXfh5Bfj3CBk4LE_64zmB-XG0k00QJKu7DKSYCz3RYqGMxyqEaRlNiYNBgWVR12YRBDaqpE7THR0VSN6qizOppKqhD7QMjHcoTxcDsfMPf7W080
  - Gulf Canadian Company for Arab Real Estate Investment, Annual General Meeting (April 26, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRtnS6XkQt31bKNwYgdhmDy1ew24p5aqkJCGN2qnYMgm6queU_Xoa65v8CAeHrUbf4zH88IwC5SBscLDICAsWyFPUwlfsHDscbiEgON271VG3-VRdNetFmywONM0T2
- ETEL.CA: status=RECENT_ACCEPTED latest=2026-07-16 age_days=3 sources=3 expected=Telecom Egypt summary=Telecom Egypt (ETEL.CA) reported strong underlying business performance in Q1 2026 and delivered growth ahead of expectations for FY 2025. The company announced it would not proceed with a proposed RDH transaction and has declared cash dividends. Recent news also highlights agreements for network expansion and 5G rollout, and plans to raise funds for debt restructuring.
  - Q1 2026 Results: Telecom Egypt Reports Strong Underlying Business Performance (May 21, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmlBUx1SHoVo9siCQsx6sgOgWKysvGuFjUd5MXG2w5RYE3PtEDqATFZuSaapFcW2wZEBww3clXAP917_KBtcZk6E0cMuo7YQztzw
  - Telecom Egypt Announces It Will Not Proceed with the Proposed RDH Transaction with Helios Investments (July 16, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmlBUx1SHoVo9siCQsx6sgOgWKysvGuFjUd5MXG2w5RYE3PtEDqATFZuSaapFcW2wZEBww3clXAP917_KBtcZk6E0cMuo7YQztzw
  - FY 2025 Results: Telecom Egypt Delivers Growth Ahead of Expectations (December 31, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQES3EPpmAV3K63dCDG-rzdbcCtbhnIQy_fQX2mAPVI2pGPGPiz3sIUaTOuQzt2LuheHPSKUDbh7f0LDlg7qqRnHVcXNDjnkCaVHNoufohvWh4SXu-m30mOMdmLgLASaviafq-Rf2PZxtA
- SCEM.CA: status=RECENT_ACCEPTED latest=2026-05-14 age_days=66 sources=3 expected=Sinai Cement summary=Sinai Cement (SCEM.CA) has released its consolidated financial results for FY 2025 and Q1 2026, reporting a fall in consolidated profits for 2025 but positive net profit in Q1 2026. The company has also announced changes in its Board of Directors and held its AGM & EGM in April 2026.
  - Release from Sinai Cement (SCEM.CA) Concerning the Amendments in the Board of Directors (May 14, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZC9F1IKfvDO1z5nAQWpoFfuweuTUr7kyehngT5W8HI6w6ctRo-GUVQEOnugQyIGhBGLlrxA2cT90t16yE8EnyqX8elLt4DMUx8NuYxmyf5hQM_yM5l8djVG1oRWXGRG32f44P2p5yD-1tvgxtpMA
  - Sinai Cement (SCEM.CA) - AGM & EGM Resolutions (April 8, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZC9F1IKfvDO1z5nAQWpoFfuweuTUr7kyehngT5W8HI6w6ctRo-GUVQEOnugQyIGhBGLlrxA2cT90t16yE8EnyqX8elLt4DMUx8NuYxmyf5hQM_yM5l8djVG1oRWXGRG32f44P2p5yD-1tvgxtpMA
  - Sinai Cement (SCEM.CA) Reports Its Financial Results (Consolidated) for The Period ending 31/12/2025 (March 10, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZC9F1IKfvDO1z5nAQWpoFfuweuTUr7kyehngT5W8HI6w6ctRo-GUVQEOnugQyIGhBGLlrxA2cT90t16yE8EnyqX8elLt4DMUx8NuYxmyf5hQM_yM5l8djVG1oRWXGRG32f44P2p5yD-1tvgxtpMA
- MEPA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Medical Packaging Company summary=Medical Packaging stock close to break above EGP 1.7; Medical Packaging announces EGP 62m capital hike; Medical Packaging&#39;s profit jumps 54% in Q1-21 Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Medical Packaging stock close to break above EGP 1.7: https://english.mubasher.info/news/4598700/Medical-Packaging-stock-close-to-break-above-EGP-1-7/
  - Medical Packaging announces EGP 62m capital hike: https://english.mubasher.info/news/3936298/Medical-Packaging-announces-EGP-62m-capital-hike/
  - Medical Packaging&#39;s profit jumps 54% in Q1-21: https://english.mubasher.info/news/3815448/Medical-Packaging-s-profit-jumps-54-in-Q1-21/
- TMGH.CA: status=RECENT_ACCEPTED latest=2026-07-05 age_days=14 sources=3 expected=Talaat Moustafa Group Holding summary=Talaat Moustafa Group Holding (TMGH.CA) has reported strong financial performance for FY 2025 with significant revenue growth and positive Q1 2026 results. The company is actively involved in new project launches and regional expansion, including 'The Spine' in East Cairo and projects in KSA and Oman. TMGH also announced dividend payouts for 2025.
  - Release from T M G Holding (TMGH.CA) Concerning the Company's Sales (July 5, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwqCwECFyAvqHkQvPRvfFq-UOBwTxmlVCgghR2uGA4LTRY4qm6f-bie6OvOjzUnvr_ZxhJrdocyH6Od72SI8x2ZhbePGXAaFt-ku3Zs8JchbbeoRiqyH55Yl8i2HfsbQ6Dsxgm3kL3xCkbjcIslw8
  - Release from TMG Holding (TMGH.CA) Concerning Company's Projects (June 25, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwqCwECFyAvqHkQvPRvfFq-UOBwTxmlVCgghR2uGA4LTRY4qm6f-bie6OvOjzUnvr_ZxhJrdocyH6Od72SI8x2ZhbePGXAaFt-ku3Zs8JchbbeoRiqyH55Yl8i2HfsbQ6Dsxgm3kL3xCkbjcIslw8
  - TMG Holding logs 39% higher revenues in Q1-26; contracted sales hit EGP 49.1bn (Mubasher Info): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwqCwECFyAvqHkQvPRvfFq-UOBwTxmlVCgghR2uGA4LTRY4qm6f-bie6OvOjzUnvr_ZxhJrdocyH6Od72SI8x2ZhbePGXAaFt-ku3Zs8JchbbeoRiqyH55Yl8i2HfsbQ6Dsxgm3kL3xCkbjcIslw8
- SMFR.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Samad Misr EGYFERT.S.A.E summary=Evidence rejected for SMFR.CA: source text did not clearly match SMFR.CA / Samad Misr EGYFERT.S.A.E.

## Warnings
- Evidence for MEPA.CA matches the company but no source/report date was detected.
- Evidence rejected for SMFR.CA: source text did not clearly match SMFR.CA / Samad Misr EGYFERT.S.A.E.
