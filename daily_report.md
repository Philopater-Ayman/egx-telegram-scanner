# Telegram-First EGX Scanner Report

Scan phase: Evening tomorrow plan
Generated UTC: 2026-09-17T19:49:29.141369+00:00
Generated Cairo: 2026-09-17 22:49
Run timing: target 19:30 Cairo | generated Cairo 2026-09-17 22:49 | cron 30 16 * * 0-4
Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-09-17 22:46

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 179/189
- Top sector: Investment Holding

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, September 17
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 60.0% / above MA50 60.0%
- EGX70 regime: BEARISH / above MA20 44.74% / above MA50 60.53%
- Sector breadth: 19.05%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- ORAS.CA: liquidity=2276142080.0 spike=1.0 score=4.6
- COMI.CA: liquidity=1515599360.0 spike=2.75 score=14.29
- ETEL.CA: liquidity=793895936.0 spike=4.1 score=25.4
- CCAP.CA: liquidity=660376384.0 spike=0.75 score=23.4
- HELI.CA: liquidity=388945024.0 spike=2.49 score=25.0

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with only 19% of sectors above their 20‑day MA, triggering a DEFENSIVE_NO_NEW_BUY risk mode; the scanner prioritized tickets by high rank scores and liquidity‑spike signals, but their bullish‑watch outlooks are tempered by overheated RSI, sector misalignment, and tight support‑resistance zones, so only a HOLD stance is warranted.
- Top tickets (BINV.CA, WKOL.CA, GBCO.CA, ETEL.CA) exhibit strong accumulation‑spike liquidity and high rank scores, yet RSI >80 for BINV/ETEL/MFPC signals overextension.
- Sector rank puts BINV/OIH in the leading Investment Holding group, but overall sector breadth is low (19%) and EGX30/EGX70 remain bearish, limiting any follow‑through.
- Support/resistance distances are tight (e.g., WKOL ~6% above support, ETEL ~2.8% below resistance), indicating limited upside room over the next 1‑3 days.
- Defensive market regime shifts risk mode to DEFENSIVE_NO_NEW_BUY, so despite bullish‑watch outlooks, uncertainty stays high and only HOLD is advised.

## Top Liquidity Spikes
- EGAS.CA: spike=7.95 liquidity=68421800.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- WKOL.CA: spike=7.56 liquidity=95828648.0 outlook=BULLISH_WATCH score=91.6 buy_ready=False
- BINV.CA: spike=6.81 liquidity=116610960.0 outlook=BULLISH_WATCH score=83 buy_ready=False
- IDRE.CA: spike=6.17 liquidity=63841476.0 outlook=BULLISH_WATCH score=83.6 buy_ready=False
- AALR.CA: spike=6.16 liquidity=154568592.0 outlook=BULLISH_WATCH score=81.6 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=17.78 5d=12.95% 20d=24.59% aboveMA50=100.0%
- #2 Telecommunications: score=12.27 5d=1.89% 20d=6.9% aboveMA50=100.0%
- #3 Agriculture & Food Production: score=11.6 5d=7.45% 20d=8.27% aboveMA50=100.0%
- #4 Education: score=7.18 5d=1.67% 20d=4.14% aboveMA50=66.67%
- #5 Industrial Goods & Cables: score=5.0 5d=-2.46% 20d=-1.1% aboveMA50=50.0%
- #6 Textiles: score=4.82 5d=-4.62% 20d=2.87% aboveMA50=100.0%
- #7 Basic Resources & Chemicals: score=4.81 5d=-3.16% 20d=3.23% aboveMA50=70.0%
- #8 Banking & Financials: score=4.47 5d=-1.77% 20d=-1.82% aboveMA50=70.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- IFAP.CA: BULLISH_WATCH score=96 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- WKOL.CA: BULLISH_WATCH score=91.6 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- FERC.CA: BULLISH_WATCH score=85.81 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- OIH.CA: BULLISH_WATCH score=85 liquidity=TRADEABLE sector=LEADING risk=momentum is extended; far above support
- IDRE.CA: BULLISH_WATCH score=83.6 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CERA.CA: BULLISH_WATCH score=83.6 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- BINV.CA: BULLISH_WATCH score=83 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support
- AALR.CA: BULLISH_WATCH score=81.6 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- SWDY.CA: BULLISH_WATCH score=81.0 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- KABO.CA: BULLISH_WATCH score=80.82 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=22.64 buy_ready=False sector_rank=17 price=314.35 support=295.0 resistance=351.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=69.61 liquidity=154568592.0 spike=6.16
- ABUK.CA: score=20.62 buy_ready=False sector_rank=7 price=92.22 support=75.01 resistance=94.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.23 liquidity=288439840.0 spike=1.85
- ACAMD.CA: score=16.64 buy_ready=False sector_rank=17 price=2.07 support=1.95 resistance=2.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=46188776.0 spike=0.8
- ACGC.CA: score=20.93 buy_ready=False sector_rank=6 price=14.38 support=12.04 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.61 liquidity=31696904.0 spike=0.76
- ADCI.CA: score=9.55 buy_ready=False sector_rank=17 price=280.67 support=267.66 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.6 liquidity=1910115.38 spike=0.31
- ADIB.CA: score=22.85 buy_ready=False sector_rank=8 price=53.63 support=50.51 resistance=55.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.56 liquidity=136888736.0 spike=2.03
- ADPC.CA: score=14.64 buy_ready=False sector_rank=17 price=3.87 support=3.81 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=45.28 liquidity=15193545.0 spike=0.67
- AFDI.CA: score=17.64 buy_ready=False sector_rank=17 price=55.34 support=51.6 resistance=68.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=49.6 liquidity=17630736.0 spike=0.7
- AFMC.CA: score=9.64 buy_ready=False sector_rank=17 price=160.67 support=157.0 resistance=264.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=21.86 liquidity=18027188.0 spike=0.32
- AJWA.CA: score=13.72 buy_ready=False sector_rank=17 price=180.0 support=175.15 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.59 liquidity=9082506.0 spike=0.18
- ALCN.CA: score=9.96 buy_ready=False sector_rank=15 price=33.91 support=30.7 resistance=34.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=117184896.0 spike=4.1
- ALUM.CA: score=12.64 buy_ready=False sector_rank=17 price=26.92 support=25.0 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=20.1 liquidity=11556235.0 spike=0.8
- AMER.CA: score=13.02 buy_ready=False sector_rank=14 price=5.49 support=4.8 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.45 liquidity=42314908.0 spike=0.68
- AMES.CA: score=8.64 buy_ready=False sector_rank=17 price=52.53 support=51.22 resistance=173.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=2.68 liquidity=72190920.0 spike=0.28
- AMIA.CA: score=17.64 buy_ready=False sector_rank=17 price=18.0 support=15.3 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=35.75 liquidity=17317654.0 spike=0.27
- AMOC.CA: score=18.63 buy_ready=False sector_rank=9 price=13.73 support=10.65 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.61 liquidity=165531776.0 spike=0.91
- APSW.CA: score=6.7 buy_ready=False sector_rank=17 price=8.65 support=8.37 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.94 liquidity=1063151.88 spike=0.93
- ARAB.CA: score=20.02 buy_ready=False sector_rank=14 price=0.26 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=32625736.0 spike=0.33
- ARCC.CA: score=17.17 buy_ready=False sector_rank=21 price=73.0 support=71.5 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.22 liquidity=19331988.0 spike=0.44
- AREH.CA: score=13.15 buy_ready=False sector_rank=17 price=1.45 support=1.39 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=8506488.0 spike=0.53
- ARVA.CA: score=4.64 buy_ready=False sector_rank=17 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=14.0 buy_ready=False sector_rank=17 price=61.5 support=60.15 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=36.59 liquidity=9362955.0 spike=0.48
- ASPI.CA: score=18.78 buy_ready=False sector_rank=17 price=0.46 support=0.41 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.27 liquidity=87714472.0 spike=1.57
- ATLC.CA: score=6.06 buy_ready=False sector_rank=20 price=7.39 support=6.96 resistance=7.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=53499816.0 spike=1.94
- ATQA.CA: score=18.92 buy_ready=False sector_rank=7 price=12.7 support=10.8 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.33 liquidity=26058190.0 spike=0.24
- AXPH.CA: score=20.96 buy_ready=False sector_rank=17 price=1687.64 support=1351.0 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.86 liquidity=9323388.0 spike=0.76
- BINV.CA: score=28.4 buy_ready=False sector_rank=1 price=61.06 support=46.25 resistance=62.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=83.0 liquidity=116610960.0 spike=6.81
- BIOC.CA: score=9.64 buy_ready=False sector_rank=17 price=280.8 support=272.01 resistance=515.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=14.21 liquidity=18340282.0 spike=0.16
- BTFH.CA: score=13.18 buy_ready=False sector_rank=20 price=2.95 support=2.87 resistance=3.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.93 liquidity=64721040.0 spike=0.67
- CAED.CA: score=11.0 buy_ready=False sector_rank=17 price=129.27 support=123.56 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=29.76 liquidity=8355581.0 spike=0.2
- CANA.CA: score=10.79 buy_ready=False sector_rank=8 price=44.15 support=41.7 resistance=44.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=54710980.0 spike=3.89
- CCAP.CA: score=23.4 buy_ready=False sector_rank=1 price=6.95 support=5.42 resistance=6.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=81.32 liquidity=660376384.0 spike=0.75
- CCRS.CA: score=19.98 buy_ready=False sector_rank=17 price=2.75 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.89 liquidity=60084420.0 spike=1.17
- CEFM.CA: score=9.63 buy_ready=False sector_rank=17 price=145.73 support=138.1 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=1985804.75 spike=0.14
- CERA.CA: score=20.96 buy_ready=False sector_rank=17 price=1.46 support=1.22 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.63 liquidity=162242208.0 spike=1.66
- CFGH.CA: score=5.64 buy_ready=False sector_rank=17 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=613.56 spike=0.03
- CICH.CA: score=13.02 buy_ready=False sector_rank=20 price=12.96 support=12.0 resistance=13.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.91 liquidity=3848948.75 spike=0.81
- CIEB.CA: score=20.79 buy_ready=False sector_rank=8 price=25.23 support=24.01 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.05 liquidity=13446936.0 spike=0.98
- CIRA.CA: score=21.64 buy_ready=False sector_rank=4 price=40.65 support=32.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=68.68 liquidity=42290652.0 spike=1.12
- CLHO.CA: score=10.06 buy_ready=False sector_rank=16 price=16.0 support=15.81 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.81 liquidity=92685224.0 spike=1.21
- CNFN.CA: score=10.98 buy_ready=False sector_rank=20 price=4.62 support=4.46 resistance=4.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.57 liquidity=7803417.5 spike=0.67
- COMI.CA: score=14.29 buy_ready=False sector_rank=8 price=133.11 support=131.11 resistance=142.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.43 liquidity=1515599360.0 spike=2.75
- COPR.CA: score=17.64 buy_ready=False sector_rank=17 price=0.51 support=0.46 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=37.33 liquidity=33570252.0 spike=0.38
- COSG.CA: score=17.64 buy_ready=False sector_rank=17 price=1.85 support=1.74 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.72 liquidity=11152233.0 spike=0.27
- CPCI.CA: score=10.41 buy_ready=False sector_rank=17 price=555.0 support=525.01 resistance=569.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=26.84 liquidity=5229713.5 spike=1.27
- CSAG.CA: score=18.94 buy_ready=False sector_rank=15 price=38.02 support=36.5 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=36.74 liquidity=24679616.0 spike=1.49
- DAPH.CA: score=17.64 buy_ready=False sector_rank=17 price=123.4 support=108.11 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.89 liquidity=31468804.0 spike=0.51
- DEIN.CA: score=7.64 buy_ready=False sector_rank=17 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=1.3 buy_ready=False sector_rank=19 price=27.05 support=26.51 resistance=29.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=27.87 liquidity=2075846.88 spike=0.36
- DSCW.CA: score=14.39 buy_ready=False sector_rank=17 price=1.85 support=1.8 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.93 liquidity=9749928.0 spike=0.25
- DTPP.CA: score=23.04 buy_ready=False sector_rank=17 price=342.41 support=292.5 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.98 liquidity=175804624.0 spike=2.7
- EALR.CA: score=14.64 buy_ready=False sector_rank=17 price=382.16 support=340.0 resistance=426.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=34.06 liquidity=78410992.0 spike=4.67
- EASB.CA: score=15.89 buy_ready=False sector_rank=17 price=8.28 support=7.16 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=56.2 liquidity=4247492.5 spike=0.25
- EAST.CA: score=8.22 buy_ready=False sector_rank=19 price=32.62 support=32.0 resistance=36.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=28.11 liquidity=51447296.0 spike=0.73
- EBSC.CA: score=12.97 buy_ready=False sector_rank=17 price=2.04 support=1.88 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.87 liquidity=5334634.5 spike=0.36
- ECAP.CA: score=8.55 buy_ready=False sector_rank=17 price=32.23 support=31.16 resistance=39.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.33 liquidity=3909435.25 spike=0.34
- EDFM.CA: score=8.62 buy_ready=False sector_rank=17 price=408.01 support=394.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=59.07 liquidity=984863.13 spike=0.6
- EEII.CA: score=2.08 buy_ready=False sector_rank=17 price=2.2 support=2.15 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=31.58 liquidity=3437659.75 spike=0.16
- EFIC.CA: score=14.92 buy_ready=False sector_rank=7 price=193.69 support=192.75 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=58397932.0 spike=0.65
- EFID.CA: score=20.34 buy_ready=False sector_rank=19 price=31.74 support=29.71 resistance=33.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.52 liquidity=87912272.0 spike=1.56
- EFIH.CA: score=20.18 buy_ready=False sector_rank=13 price=23.82 support=22.16 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.81 liquidity=60078152.0 spike=0.95
- EGAL.CA: score=20.92 buy_ready=False sector_rank=7 price=371.41 support=321.01 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.34 liquidity=89621912.0 spike=0.83
- EGAS.CA: score=10.63 buy_ready=False sector_rank=9 price=59.01 support=55.25 resistance=60.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=68421800.0 spike=7.95
- EGBE.CA: score=3.91 buy_ready=False sector_rank=8 price=0.51 support=0.49 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=29.63 liquidity=120787.49 spike=0.89
- EGCH.CA: score=20.92 buy_ready=False sector_rank=7 price=14.02 support=13.3 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.58 liquidity=75329176.0 spike=0.67
- EGSA.CA: score=11.25 buy_ready=False sector_rank=2 price=9.0 support=8.67 resistance=9.1 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=78.18 liquidity=10413.0 spike=1.42
- EGTS.CA: score=13.26 buy_ready=False sector_rank=14 price=17.16 support=16.17 resistance=18.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.62 liquidity=6235426.5 spike=0.26
- EHDR.CA: score=13.78 buy_ready=False sector_rank=17 price=2.74 support=2.73 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=9135745.0 spike=0.45
- EKHO.CA: score=6.63 buy_ready=False sector_rank=9 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=11.0 buy_ready=False sector_rank=5 price=2.04 support=1.92 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=289274944.0 spike=3.97
- ELKA.CA: score=14.64 buy_ready=False sector_rank=17 price=1.76 support=1.7 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.17 liquidity=10593287.0 spike=0.24
- ELNA.CA: score=-1.34 buy_ready=False sector_rank=17 price=35.74 support=33.96 resistance=38.99 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=22.51 liquidity=23302.48 spike=0.05
- ELSH.CA: score=14.64 buy_ready=False sector_rank=17 price=13.15 support=12.67 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.01 liquidity=16059503.0 spike=0.42
- ELWA.CA: score=5.04 buy_ready=False sector_rank=17 price=1.7 support=1.62 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=404491.91 spike=0.16
- EMFD.CA: score=20.02 buy_ready=False sector_rank=14 price=14.25 support=11.55 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.05 liquidity=102250688.0 spike=0.62
- ENGC.CA: score=10.06 buy_ready=False sector_rank=17 price=42.33 support=41.0 resistance=50.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.08 liquidity=14814437.0 spike=1.21
- EOSB.CA: score=9.88 buy_ready=False sector_rank=17 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=77512.47 spike=1.08
- EPCO.CA: score=12.15 buy_ready=False sector_rank=17 price=11.21 support=10.8 resistance=12.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=47.6 liquidity=4509983.5 spike=0.23
- EPPK.CA: score=-4.94 buy_ready=False sector_rank=17 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=25.4 buy_ready=False sector_rank=2 price=131.73 support=112.1 resistance=135.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=86.15 liquidity=793895936.0 spike=4.1
- ETRS.CA: score=19.64 buy_ready=False sector_rank=17 price=11.14 support=10.66 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.72 liquidity=10984788.0 spike=0.66
- EXPA.CA: score=20.79 buy_ready=False sector_rank=8 price=21.39 support=19.8 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=60.73 liquidity=13004101.0 spike=0.37
- FAIT.CA: score=16.12 buy_ready=False sector_rank=8 price=47.5 support=39.58 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=68.21 liquidity=5333939.5 spike=0.68
- FAITA.CA: score=1.27 buy_ready=False sector_rank=8 price=0.99 support=0.98 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=9.76 liquidity=58471.56 spike=1.21
- FERC.CA: score=21.12 buy_ready=False sector_rank=7 price=80.7 support=76.9 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.29 liquidity=20250720.0 spike=1.1
- FWRY.CA: score=15.5 buy_ready=False sector_rank=13 price=19.0 support=18.66 resistance=19.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.03 liquidity=152805120.0 spike=1.16
- GBCO.CA: score=26.26 buy_ready=False sector_rank=10 price=30.96 support=27.51 resistance=31.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=63.69 liquidity=97307536.0 spike=1.82
- GDWA.CA: score=13.64 buy_ready=False sector_rank=17 price=0.78 support=0.76 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.66 liquidity=36821348.0 spike=0.92
- GGCC.CA: score=14.64 buy_ready=False sector_rank=17 price=0.87 support=0.83 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.36 liquidity=15771758.0 spike=0.4
- GIHD.CA: score=14.17 buy_ready=False sector_rank=17 price=73.4 support=58.01 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=65.35 liquidity=6532016.5 spike=0.23
- GMCI.CA: score=-0.99 buy_ready=False sector_rank=17 price=1.73 support=1.69 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=23.33 liquidity=370287.75 spike=0.74
- GRCA.CA: score=8.64 buy_ready=False sector_rank=17 price=43.12 support=39.0 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.52 liquidity=27521380.0 spike=0.33
- GSSC.CA: score=5.28 buy_ready=False sector_rank=17 price=319.37 support=291.16 resistance=321.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16713437.0 spike=1.32
- GTWL.CA: score=19.64 buy_ready=False sector_rank=17 price=237.91 support=175.01 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.29 liquidity=82254408.0 spike=0.31
- HDBK.CA: score=22.21 buy_ready=False sector_rank=8 price=120.5 support=89.01 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.49 liquidity=98584608.0 spike=1.71
- HELI.CA: score=25.0 buy_ready=False sector_rank=14 price=8.45 support=7.34 resistance=8.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.15 liquidity=388945024.0 spike=2.49
- HRHO.CA: score=13.18 buy_ready=False sector_rank=20 price=25.46 support=25.04 resistance=26.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.38 liquidity=31604316.0 spike=0.32
- ICID.CA: score=14.64 buy_ready=False sector_rank=17 price=18.81 support=15.04 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.57 liquidity=4995603.0 spike=0.24
- IDRE.CA: score=24.64 buy_ready=False sector_rank=17 price=56.13 support=51.0 resistance=57.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=52.65 liquidity=63841476.0 spike=6.17
- IFAP.CA: score=22.4 buy_ready=False sector_rank=3 price=20.88 support=20.05 resistance=22.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.41 liquidity=14054880.0 spike=0.6
- INFI.CA: score=12.64 buy_ready=False sector_rank=17 price=134.87 support=130.15 resistance=174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=16.41 liquidity=23029966.0 spike=0.72
- IRON.CA: score=10.22 buy_ready=False sector_rank=7 price=28.57 support=26.3 resistance=33.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=2.57 liquidity=16986298.0 spike=1.15
- ISMA.CA: score=6.86 buy_ready=False sector_rank=17 price=31.24 support=28.05 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=13.72 liquidity=7221043.5 spike=0.27
- ISMQ.CA: score=15.92 buy_ready=False sector_rank=7 price=8.98 support=8.68 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.6 liquidity=12445743.0 spike=0.44
- ISPH.CA: score=12.74 buy_ready=False sector_rank=16 price=12.05 support=11.9 resistance=13.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.22 liquidity=164091664.0 spike=2.55
- JUFO.CA: score=15.68 buy_ready=False sector_rank=19 price=27.0 support=26.45 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.8 liquidity=24332472.0 spike=1.23
- KABO.CA: score=20.93 buy_ready=False sector_rank=6 price=9.38 support=8.82 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.0 liquidity=14103351.0 spike=0.27
- KWIN.CA: score=9.64 buy_ready=False sector_rank=17 price=89.31 support=84.5 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=32.99 liquidity=11756638.0 spike=0.18
- KZPC.CA: score=17.64 buy_ready=False sector_rank=17 price=14.4 support=12.16 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=72.6 liquidity=18792420.0 spike=0.31
- LCSW.CA: score=14.17 buy_ready=False sector_rank=21 price=33.4 support=32.42 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.38 liquidity=15381877.0 spike=0.55
- LUTS.CA: score=17.64 buy_ready=False sector_rank=17 price=0.95 support=0.79 resistance=1.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.09 liquidity=80283712.0 spike=0.3
- MAAL.CA: score=8.02 buy_ready=False sector_rank=17 price=8.75 support=8.18 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=34.64 liquidity=8377174.0 spike=0.82
- MASR.CA: score=14.64 buy_ready=False sector_rank=17 price=7.89 support=7.49 resistance=8.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.2 liquidity=76563296.0 spike=0.84
- MBSC.CA: score=17.17 buy_ready=False sector_rank=21 price=372.29 support=355.04 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.97 liquidity=14812688.0 spike=0.26
- MCQE.CA: score=17.17 buy_ready=False sector_rank=21 price=218.99 support=213.0 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.18 liquidity=17070674.0 spike=0.47
- MCRO.CA: score=16.64 buy_ready=False sector_rank=17 price=1.69 support=1.44 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.49 liquidity=74633160.0 spike=0.64
- MENA.CA: score=7.79 buy_ready=False sector_rank=14 price=6.81 support=6.58 resistance=7.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=2670203.5 spike=1.05
- MEPA.CA: score=17.64 buy_ready=False sector_rank=17 price=1.92 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=58.97 liquidity=10196926.0 spike=0.29
- MFPC.CA: score=23.84 buy_ready=False sector_rank=7 price=50.0 support=38.93 resistance=48.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=83.75 liquidity=384674720.0 spike=2.96
- MFSC.CA: score=10.2 buy_ready=False sector_rank=17 price=49.28 support=48.5 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=2559300.25 spike=0.53
- MHOT.CA: score=17.2 buy_ready=False sector_rank=12 price=18.11 support=17.62 resistance=19.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=35.64 liquidity=10038788.0 spike=0.94
- MICH.CA: score=15.84 buy_ready=False sector_rank=17 price=49.4 support=47.2 resistance=53.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.29 liquidity=8196205.0 spike=0.32
- MILS.CA: score=9.07 buy_ready=False sector_rank=17 price=203.45 support=198.0 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.51 liquidity=6426245.5 spike=0.12
- MIPH.CA: score=15.95 buy_ready=False sector_rank=16 price=848.52 support=700.2 resistance=820.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.61 liquidity=5486777.0 spike=1.41
- MOED.CA: score=16.64 buy_ready=False sector_rank=17 price=0.79 support=0.74 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.14 liquidity=22939222.0 spike=0.19
- MOIL.CA: score=10.68 buy_ready=False sector_rank=9 price=0.68 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=59.38 liquidity=56020.11 spike=0.27
- MOIN.CA: score=19.64 buy_ready=False sector_rank=17 price=37.56 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.46 liquidity=22831836.0 spike=0.79
- MOSC.CA: score=12.86 buy_ready=False sector_rank=17 price=311.76 support=302.0 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=29.45 liquidity=9763284.0 spike=1.23
- MPCI.CA: score=17.64 buy_ready=False sector_rank=17 price=409.98 support=345.0 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.87 liquidity=34777348.0 spike=0.22
- MPCO.CA: score=22.4 buy_ready=False sector_rank=3 price=2.71 support=2.07 resistance=2.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.61 liquidity=110954200.0 spike=0.69
- MPRC.CA: score=14.64 buy_ready=False sector_rank=17 price=39.77 support=38.31 resistance=46.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.32 liquidity=10926595.0 spike=0.28
- MTIE.CA: score=15.62 buy_ready=False sector_rank=10 price=8.47 support=8.1 resistance=8.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.86 liquidity=16092042.0 spike=0.38
- NAHO.CA: score=7.65 buy_ready=False sector_rank=17 price=0.14 support=0.13 resistance=0.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=8589.42 spike=0.11
- NCCW.CA: score=16.64 buy_ready=False sector_rank=17 price=8.16 support=5.59 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.87 liquidity=57424748.0 spike=0.93
- NEDA.CA: score=4.97 buy_ready=False sector_rank=17 price=2.72 support=2.7 resistance=2.95 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=40.62 liquidity=334641.6 spike=0.47
- NHPS.CA: score=6.05 buy_ready=False sector_rank=17 price=76.97 support=75.31 resistance=98.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=6.12 liquidity=6405024.0 spike=0.31
- NINH.CA: score=9.64 buy_ready=False sector_rank=17 price=20.68 support=20.5 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=21.7 liquidity=26126982.0 spike=0.86
- NIPH.CA: score=12.64 buy_ready=False sector_rank=16 price=319.01 support=301.0 resistance=414.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=17.14 liquidity=107217976.0 spike=0.55
- OBRI.CA: score=9.51 buy_ready=False sector_rank=17 price=31.15 support=30.1 resistance=34.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.87 liquidity=5865408.0 spike=0.3
- OCDI.CA: score=15.02 buy_ready=False sector_rank=14 price=30.5 support=29.25 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.58 liquidity=53030680.0 spike=0.65
- OCPH.CA: score=3.45 buy_ready=False sector_rank=17 price=243.11 support=210.0 resistance=277.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=30.76 liquidity=2807458.75 spike=0.34
- ODIN.CA: score=4.67 buy_ready=False sector_rank=17 price=2.75 support=2.55 resistance=3.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=13.51 liquidity=5030909.0 spike=0.19
- OFH.CA: score=19.64 buy_ready=False sector_rank=17 price=1.06 support=0.88 resistance=1.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.74 liquidity=58595856.0 spike=0.53
- OIH.CA: score=24.64 buy_ready=False sector_rank=1 price=2.19 support=1.82 resistance=2.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=66.0 liquidity=137696080.0 spike=1.12
- OLFI.CA: score=14.22 buy_ready=False sector_rank=19 price=22.93 support=22.07 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.47 liquidity=11455615.0 spike=0.71
- ORAS.CA: score=4.6 buy_ready=False sector_rank=18 price=867.84 support=831.0 resistance=879.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2276142080.0 spike=1.0
- ORHD.CA: score=21.06 buy_ready=False sector_rank=14 price=43.35 support=40.28 resistance=43.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.0 liquidity=210129792.0 spike=1.52
- ORWE.CA: score=21.73 buy_ready=False sector_rank=6 price=27.91 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.35 liquidity=69470664.0 spike=1.4
- PHAR.CA: score=12.64 buy_ready=False sector_rank=16 price=119.5 support=117.01 resistance=141.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.32 liquidity=59976708.0 spike=0.39
- PHDC.CA: score=10.02 buy_ready=False sector_rank=14 price=13.66 support=13.65 resistance=15.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.85 liquidity=86285568.0 spike=0.44
- PHTV.CA: score=14.04 buy_ready=False sector_rank=17 price=367.22 support=311.27 resistance=389.0 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=64.27 liquidity=2978521.43 spike=1.71
- POUL.CA: score=14.22 buy_ready=False sector_rank=19 price=38.56 support=36.97 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.07 liquidity=22882056.0 spike=0.97
- PRCL.CA: score=12.19 buy_ready=False sector_rank=21 price=31.95 support=30.9 resistance=35.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=45.39 liquidity=6021483.5 spike=0.32
- PRDC.CA: score=10.02 buy_ready=False sector_rank=14 price=7.85 support=7.68 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.25 liquidity=36850088.0 spike=0.58
- PRMH.CA: score=3.19 buy_ready=False sector_rank=17 price=2.7 support=2.53 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8545401.0 spike=0.79
- RACC.CA: score=16.64 buy_ready=False sector_rank=17 price=9.98 support=9.4 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=47.29 liquidity=14690564.0 spike=0.75
- RAKT.CA: score=10.7 buy_ready=False sector_rank=17 price=22.65 support=21.4 resistance=23.02 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=57.94 liquidity=55651.05 spike=0.22
- RAYA.CA: score=17.43 buy_ready=False sector_rank=11 price=7.25 support=6.95 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=40321860.0 spike=0.74
- RMDA.CA: score=19.64 buy_ready=False sector_rank=16 price=6.16 support=5.77 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=16089499.0 spike=0.29
- ROTO.CA: score=7.91 buy_ready=False sector_rank=17 price=41.11 support=35.02 resistance=51.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=17.65 liquidity=8269437.0 spike=0.77
- RREI.CA: score=19.64 buy_ready=False sector_rank=17 price=4.46 support=4.24 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=25631918.0 spike=0.94
- RTVC.CA: score=8.41 buy_ready=False sector_rank=17 price=3.98 support=3.85 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=28.33 liquidity=5772793.5 spike=0.8
- RUBX.CA: score=21.64 buy_ready=False sector_rank=17 price=13.56 support=12.36 resistance=14.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=67.33 liquidity=11040298.0 spike=0.56
- SAUD.CA: score=19.02 buy_ready=False sector_rank=8 price=23.77 support=22.7 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.96 liquidity=8229628.0 spike=0.57
- SCEM.CA: score=17.17 buy_ready=False sector_rank=21 price=94.98 support=94.0 resistance=105.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.18 liquidity=30719482.0 spike=0.22
- SCFM.CA: score=2.28 buy_ready=False sector_rank=17 price=275.0 support=265.51 resistance=297.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=25.49 liquidity=2635598.5 spike=0.28
- SCTS.CA: score=2.94 buy_ready=False sector_rank=4 price=603.71 support=566.66 resistance=640.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=28.73 liquidity=1542648.0 spike=0.31
- SDTI.CA: score=19.72 buy_ready=False sector_rank=17 price=77.01 support=67.0 resistance=76.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=65.18 liquidity=41225448.0 spike=2.04
- SEIG.CA: score=5.97 buy_ready=False sector_rank=17 price=242.86 support=228.13 resistance=274.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=43.16 liquidity=1334226.5 spike=0.74
- SIPC.CA: score=19.64 buy_ready=False sector_rank=17 price=5.89 support=4.1 resistance=6.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=65.96 liquidity=20330202.0 spike=0.35
- SKPC.CA: score=20.92 buy_ready=False sector_rank=7 price=18.48 support=16.82 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.27 liquidity=113514408.0 spike=0.8
- SMFR.CA: score=9.82 buy_ready=False sector_rank=17 price=240.92 support=236.0 resistance=276.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.28 liquidity=10411218.0 spike=1.09
- SNFC.CA: score=19.76 buy_ready=False sector_rank=17 price=11.19 support=10.26 resistance=11.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.24 liquidity=14222101.0 spike=1.06
- SPIN.CA: score=11.17 buy_ready=False sector_rank=6 price=17.58 support=17.01 resistance=20.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=28.41 liquidity=7243756.0 spike=0.37
- SPMD.CA: score=18.64 buy_ready=False sector_rank=17 price=0.46 support=0.43 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.1 liquidity=129784344.0 spike=2.0
- SUGR.CA: score=19.22 buy_ready=False sector_rank=19 price=60.0 support=50.0 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=58.65 liquidity=21484816.0 spike=0.31
- SVCE.CA: score=19.64 buy_ready=False sector_rank=17 price=11.78 support=10.28 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.13 liquidity=113709120.0 spike=0.69
- SWDY.CA: score=21.0 buy_ready=False sector_rank=5 price=126.86 support=115.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.64 liquidity=28660762.0 spike=0.31
- TALM.CA: score=19.22 buy_ready=False sector_rank=4 price=22.2 support=17.11 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=80.86 liquidity=85229544.0 spike=1.41
- TMGH.CA: score=15.02 buy_ready=False sector_rank=14 price=95.65 support=94.86 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.75 liquidity=249902608.0 spike=0.94
- TRTO.CA: score=7.66 buy_ready=False sector_rank=17 price=0.07 support=0.05 resistance=0.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.92 liquidity=17539.39 spike=0.63
- UEFM.CA: score=6.93 buy_ready=False sector_rank=17 price=516.66 support=440.66 resistance=557.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=48.61 liquidity=2292627.0 spike=0.84
- UEGC.CA: score=9.64 buy_ready=False sector_rank=17 price=1.78 support=1.66 resistance=2.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.16 liquidity=23792500.0 spike=0.49
- UNIP.CA: score=19.64 buy_ready=False sector_rank=17 price=0.39 support=0.35 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.13 liquidity=21231282.0 spike=0.62
- UNIT.CA: score=20.82 buy_ready=False sector_rank=14 price=18.99 support=18.11 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.35 liquidity=20116440.0 spike=1.4
- WCDF.CA: score=18.67 buy_ready=False sector_rank=17 price=750.12 support=630.06 resistance=765.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=90.91 liquidity=7530966.0 spike=2.25
- WKOL.CA: score=26.64 buy_ready=False sector_rank=17 price=352.55 support=332.56 resistance=369.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.22 liquidity=95828648.0 spike=7.56
- ZEOT.CA: score=6.85 buy_ready=False sector_rank=17 price=13.16 support=13.03 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=28.1 liquidity=4214043.5 spike=0.57
- ZMID.CA: score=20.02 buy_ready=False sector_rank=14 price=9.37 support=7.41 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.03 liquidity=246055120.0 spike=0.99

## Backtesting Lite
- BINV.CA: 180d return=68.35%, max drawdown=-17.77%, MA20>MA50 days last20=20, as_of=2026-09-15T21:00:00+00:00
- WKOL.CA: 180d return=13.4%, max drawdown=-25.83%, MA20>MA50 days last20=20, as_of=2026-09-15T21:00:00+00:00
- GBCO.CA: 180d return=14.63%, max drawdown=-24.35%, MA20>MA50 days last20=2, as_of=2026-09-15T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- WKOL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Wadi Kom Ombo For Land Reclamation Co. summary=Wadi Kom Ombo amends estimated budget for FY26/27; Wadi Kom Ombo eyes EGP 257.77m in FY26/27 net profits; Wadi Kom Ombo records lower net profits at nearly EGP 2m in Q1-25/26
  - Wadi Kom Ombo amends estimated budget for FY26/27: https://english.mubasher.info/news/4600336/Wadi-Kom-Ombo-amends-estimated-budget-for-FY26-27/
  - Wadi Kom Ombo eyes EGP 257.77m in FY26/27 net profits: https://english.mubasher.info/news/4585452/Wadi-Kom-Ombo-eyes-EGP-257-77m-in-FY26-27-net-profits/
  - Wadi Kom Ombo records lower net profits at nearly EGP 2m in Q1-25/26: https://english.mubasher.info/news/4531526/Wadi-Kom-Ombo-records-lower-net-profits-at-nearly-EGP-2m-in-Q1-25-26/
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- HELI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Heliopolis Housing summary=Evidence rejected for HELI.CA: source text did not clearly match HELI.CA / Heliopolis Housing.
- OIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Investment Holding summary=Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- IDRE.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Ismailia Development and Real Estate Co summary=Evidence rejected for IDRE.CA: source text did not clearly match IDRE.CA / Ismailia Development and Real Estate Co.
- MFPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr Fertilizers Production summary=Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.

## Warnings
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for WKOL.CA matches the company but no source/report date was detected.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence rejected for HELI.CA: source text did not clearly match HELI.CA / Heliopolis Housing.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence rejected for IDRE.CA: source text did not clearly match IDRE.CA / Ismailia Development and Real Estate Co.
- Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
