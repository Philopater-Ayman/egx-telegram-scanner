# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-09-15T10:28:41.157617+00:00
Generated Cairo: 2026-09-15 13:28
Run timing: target 08:45 Cairo | generated Cairo 2026-09-15 13:28 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-15 13:24

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 177/189
- Top sector: Investment Holding

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, September 15
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 40.0% / above MA50 55.0%
- EGX70 regime: BEARISH / above MA20 29.73% / above MA50 54.05%
- Sector breadth: 19.05%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=557730240.0 spike=1.07 score=14.29
- CCAP.CA: liquidity=513029408.0 spike=0.6 score=23.4
- SPMD.CA: liquidity=459169472.0 spike=25.34 score=9.33
- TALM.CA: liquidity=266274352.0 spike=6.32 score=29.4
- ETEL.CA: liquidity=137211008.0 spike=0.71 score=20.4

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with only 19% sector breadth, putting the market in a defensive mode that blocks new buys; the scanner therefore highlights tickets with strong relative liquidity and sector leadership but flags them as HOLD due to extended momentum and resistance proximity.
- TALM.CA (Education) – liquidity spike and bullish watch, yet price far above 20‑day support and momentum extended → hold.
- CIRA.CA (Education) – solid liquidity and recent takeover news, but RSI high and above support → hold.
- MPCO.CA (Agriculture & Food) – liquidity cooling, price above support, sector not leading → hold.
- CCAP.CA (Investment Holding) – top liquidity but RSI overheated and near resistance → hold.
- KABO.CA (Textiles) – liquidity cooling, momentum extended → hold.

## Top Liquidity Spikes
- SPMD.CA: spike=25.34 liquidity=459169472.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- TALM.CA: spike=6.32 liquidity=266274352.0 outlook=BULLISH_WATCH score=94.61 buy_ready=False
- UNIT.CA: spike=3.11 liquidity=34558008.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EOSB.CA: spike=2.76 liquidity=187291.59 outlook=NEUTRAL score=37.82 buy_ready=False
- WCDF.CA: spike=1.93 liquidity=5833351.5 outlook=CONSTRUCTIVE score=62.82 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=12.1 5d=5.42% 20d=16.94% aboveMA50=100.0%
- #2 Telecommunications: score=10.53 5d=3.5% 20d=7.55% aboveMA50=100.0%
- #3 Education: score=7.61 5d=3.72% 20d=2.9% aboveMA50=66.67%
- #4 Agriculture & Food Production: score=5.99 5d=3.26% 20d=4.87% aboveMA50=50.0%
- #5 Textiles: score=4.05 5d=-5.29% 20d=5.67% aboveMA50=100.0%
- #6 Basic Resources & Chemicals: score=3.49 5d=-3.13% 20d=1.58% aboveMA50=80.0%
- #7 Energy & Petrochemicals: score=2.65 5d=-2.0% 20d=-0.29% aboveMA50=75.0%
- #8 Industrial Goods & Cables: score=1.98 5d=-6.81% 20d=4.45% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- TALM.CA: BULLISH_WATCH score=94.61 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended; far above support
- CIRA.CA: BULLISH_WATCH score=88.61 liquidity=TRADEABLE sector=LEADING risk=momentum is extended; far above support
- BINV.CA: BULLISH_WATCH score=88 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- ORWE.CA: BULLISH_WATCH score=80.05 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- SKPC.CA: BULLISH_WATCH score=79.49 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- EGAL.CA: BULLISH_WATCH score=73.49 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- SWDY.CA: BULLISH_WATCH score=72.98 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- MPCO.CA: BULLISH_WATCH score=71.99 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; far above support
- MASR.CA: BULLISH_WATCH score=71.82 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- WKOL.CA: BULLISH_WATCH score=71.82 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=12.33 buy_ready=False sector_rank=11 price=312.02 support=295.0 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=32.56 liquidity=12473237.0 spike=0.37
- ABUK.CA: score=20.4 buy_ready=False sector_rank=6 price=88.57 support=75.01 resistance=94.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=65.89 liquidity=27231406.0 spike=0.16
- ACAMD.CA: score=18.33 buy_ready=False sector_rank=11 price=2.1 support=1.95 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=54.39 liquidity=30602556.0 spike=0.54
- ACGC.CA: score=18.62 buy_ready=False sector_rank=5 price=14.2 support=11.85 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=54.19 liquidity=18426932.0 spike=0.45
- ADCI.CA: score=4.2 buy_ready=False sector_rank=11 price=276.51 support=267.66 resistance=319.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=28.35 liquidity=1874789.75 spike=0.25
- ADIB.CA: score=12.15 buy_ready=False sector_rank=15 price=52.0 support=50.51 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=28446666.0 spike=0.41
- ADPC.CA: score=10.45 buy_ready=False sector_rank=11 price=3.84 support=3.82 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=38.71 liquidity=6117296.0 spike=0.23
- AFDI.CA: score=1.03 buy_ready=False sector_rank=11 price=52.37 support=51.6 resistance=68.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=19.16 liquidity=1698578.88 spike=0.07
- AFMC.CA: score=9.33 buy_ready=False sector_rank=11 price=159.94 support=157.0 resistance=267.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=19.7 liquidity=14217318.0 spike=0.23
- AJWA.CA: score=11.19 buy_ready=False sector_rank=11 price=180.0 support=175.15 resistance=202.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=44.32 liquidity=6861699.5 spike=0.13
- ALCN.CA: score=14.81 buy_ready=False sector_rank=17 price=31.01 support=30.03 resistance=34.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=48.33 liquidity=8047928.0 spike=0.27
- ALUM.CA: score=5.46 buy_ready=False sector_rank=11 price=25.86 support=25.34 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=23.58 liquidity=3131722.75 spike=0.19
- AMER.CA: score=5.69 buy_ready=False sector_rank=12 price=5.75 support=4.91 resistance=5.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=108652152.0 spike=1.72
- AMES.CA: score=8.33 buy_ready=False sector_rank=11 price=52.25 support=53.4 resistance=173.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=0.56 liquidity=125897152.0 spike=0.52
- AMIA.CA: score=8.15 buy_ready=False sector_rank=11 price=17.76 support=12.71 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=29.09 liquidity=5819934.5 spike=0.08
- AMOC.CA: score=20.06 buy_ready=False sector_rank=7 price=13.22 support=10.65 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=70.36 liquidity=40334180.0 spike=0.2
- APSW.CA: score=3.9 buy_ready=False sector_rank=11 price=8.41 support=8.41 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=39.78 liquidity=574066.88 spike=0.47
- ARAB.CA: score=14.25 buy_ready=False sector_rank=12 price=0.25 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=47.17 liquidity=37559512.0 spike=0.38
- ARCC.CA: score=17.23 buy_ready=False sector_rank=13 price=71.59 support=71.51 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=41.74 liquidity=15900392.0 spike=0.29
- AREH.CA: score=6.74 buy_ready=False sector_rank=11 price=1.43 support=1.39 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=40.62 liquidity=2413977.75 spike=0.14
- ARVA.CA: score=4.33 buy_ready=False sector_rank=11 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=11.62 buy_ready=False sector_rank=11 price=61.12 support=60.92 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=36.67 liquidity=7292664.5 spike=0.32
- ASPI.CA: score=9.33 buy_ready=False sector_rank=11 price=0.43 support=0.41 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=28.49 liquidity=33086698.0 spike=0.62
- ATLC.CA: score=3.3 buy_ready=False sector_rank=20 price=7.33 support=6.61 resistance=7.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13623476.0 spike=0.48
- ATQA.CA: score=20.4 buy_ready=False sector_rank=6 price=12.36 support=10.8 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=70.72 liquidity=38497984.0 spike=0.36
- AXPH.CA: score=10.45 buy_ready=False sector_rank=11 price=1683.19 support=1340.0 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=79.71 liquidity=6121103.0 spike=0.51
- BINV.CA: score=17.88 buy_ready=False sector_rank=1 price=51.72 support=46.25 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=64.94 liquidity=1477540.25 spike=0.13
- BIOC.CA: score=9.33 buy_ready=False sector_rank=11 price=277.75 support=281.06 resistance=555.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=9.58 liquidity=15915649.0 spike=0.12
- BTFH.CA: score=7.3 buy_ready=False sector_rank=20 price=2.89 support=2.88 resistance=3.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=34.48 liquidity=23511754.0 spike=0.23
- CAED.CA: score=12.33 buy_ready=False sector_rank=11 price=131.9 support=123.56 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=32.85 liquidity=30183406.0 spike=0.73
- CANA.CA: score=9.53 buy_ready=False sector_rank=15 price=41.64 support=41.0 resistance=44.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=51.64 liquidity=2380011.5 spike=0.14
- CCAP.CA: score=23.4 buy_ready=False sector_rank=1 price=6.79 support=5.32 resistance=6.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=82.76 liquidity=513029408.0 spike=0.6
- CCRS.CA: score=4.33 buy_ready=False sector_rank=11 price=2.58 support=2.45 resistance=2.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12778468.0 spike=0.25
- CEFM.CA: score=10.09 buy_ready=False sector_rank=11 price=146.05 support=135.0 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=39.85 liquidity=758770.38 spike=0.05
- CERA.CA: score=21.75 buy_ready=False sector_rank=11 price=1.41 support=1.22 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=54.05 liquidity=103278560.0 spike=1.21
- CFGH.CA: score=7.34 buy_ready=False sector_rank=11 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance as_of=2026-09-13T21:00:00+00:00 freshness=FRESH RSI=58.82 liquidity=8794.1 spike=0.35
- CICH.CA: score=9.76 buy_ready=False sector_rank=20 price=12.42 support=12.0 resistance=13.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=51.96 liquidity=1464043.88 spike=0.3
- CIEB.CA: score=10.45 buy_ready=False sector_rank=15 price=24.22 support=24.01 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=45.35 liquidity=6298287.5 spike=0.43
- CIRA.CA: score=26.46 buy_ready=False sector_rank=3 price=39.59 support=32.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=63.68 liquidity=40553652.0 spike=1.03
- CLHO.CA: score=8.57 buy_ready=False sector_rank=18 price=16.11 support=15.81 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=27.13 liquidity=20127902.0 spike=0.25
- CNFN.CA: score=-1.17 buy_ready=False sector_rank=20 price=4.56 support=4.53 resistance=4.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=27.54 liquidity=1534466.75 spike=0.11
- COMI.CA: score=14.29 buy_ready=False sector_rank=15 price=132.2 support=132.9 resistance=142.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=35.91 liquidity=557730240.0 spike=1.07
- COPR.CA: score=12.33 buy_ready=False sector_rank=11 price=0.48 support=0.44 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=30.07 liquidity=13621375.0 spike=0.14
- COSG.CA: score=16.35 buy_ready=False sector_rank=11 price=1.83 support=1.74 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=46.51 liquidity=9017438.0 spike=0.16
- CPCI.CA: score=3.18 buy_ready=False sector_rank=11 price=532.1 support=525.01 resistance=569.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=28.12 liquidity=850325.44 spike=0.18
- CSAG.CA: score=11.61 buy_ready=False sector_rank=17 price=38.2 support=38.13 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=37.58 liquidity=4850638.5 spike=0.27
- DAPH.CA: score=17.33 buy_ready=False sector_rank=11 price=122.3 support=108.11 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=53.01 liquidity=19778264.0 spike=0.32
- DEIN.CA: score=7.33 buy_ready=False sector_rank=11 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=9.12 buy_ready=False sector_rank=16 price=27.06 support=27.02 resistance=29.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=40.05 liquidity=5256429.0 spike=0.74
- DSCW.CA: score=11.21 buy_ready=False sector_rank=11 price=1.82 support=1.8 resistance=2.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=7886729.0 spike=0.18
- DTPP.CA: score=19.33 buy_ready=False sector_rank=11 price=333.75 support=290.1 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=65.01 liquidity=46753268.0 spike=0.91
- EALR.CA: score=5.68 buy_ready=False sector_rank=11 price=380.14 support=340.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=19.39 liquidity=6355006.5 spike=0.23
- EASB.CA: score=21.33 buy_ready=False sector_rank=11 price=8.61 support=7.16 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=64.66 liquidity=14282757.0 spike=0.87
- EAST.CA: score=7.87 buy_ready=False sector_rank=16 price=33.51 support=33.04 resistance=37.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=26.72 liquidity=26682920.0 spike=0.4
- EBSC.CA: score=8.7 buy_ready=False sector_rank=11 price=2.06 support=1.88 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=57.26 liquidity=1373537.75 spike=0.09
- ECAP.CA: score=1.09 buy_ready=False sector_rank=11 price=32.52 support=31.16 resistance=40.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=30.27 liquidity=1765387.38 spike=0.14
- EDFM.CA: score=9.83 buy_ready=False sector_rank=11 price=412.9 support=394.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=54.82 liquidity=504260.22 spike=0.3
- EEII.CA: score=2.34 buy_ready=False sector_rank=11 price=2.17 support=2.15 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=29.67 liquidity=4012941.0 spike=0.16
- EFIC.CA: score=17.4 buy_ready=False sector_rank=6 price=200.17 support=192.75 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=44.04 liquidity=40476044.0 spike=0.41
- EFID.CA: score=17.09 buy_ready=False sector_rank=16 price=30.9 support=29.71 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=36.72 liquidity=63460940.0 spike=1.11
- EFIH.CA: score=17.16 buy_ready=False sector_rank=14 price=23.35 support=22.16 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=37.24 liquidity=22374116.0 spike=0.3
- EGAL.CA: score=20.4 buy_ready=False sector_rank=6 price=361.1 support=321.01 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=59.48 liquidity=37864176.0 spike=0.32
- EGAS.CA: score=12.56 buy_ready=False sector_rank=7 price=56.12 support=55.21 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=38.73 liquidity=4504269.5 spike=0.47
- EGBE.CA: score=2.22 buy_ready=False sector_rank=15 price=0.51 support=0.49 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=12.7 liquidity=66099.93 spike=0.47
- EGCH.CA: score=18.4 buy_ready=False sector_rank=6 price=13.9 support=13.3 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=47.29 liquidity=60140540.0 spike=0.49
- EGSA.CA: score=11.31 buy_ready=False sector_rank=2 price=8.98 support=8.67 resistance=9.1 source=Yahoo Finance as_of=2026-09-13T21:00:00+00:00 freshness=FRESH RSI=77.36 liquidity=11198.06 spike=1.45
- EGTS.CA: score=8.57 buy_ready=False sector_rank=12 price=16.85 support=16.17 resistance=19.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=43.73 liquidity=2326560.5 spike=0.09
- EHDR.CA: score=14.33 buy_ready=False sector_rank=11 price=2.8 support=2.81 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=41.51 liquidity=10538794.0 spike=0.47
- EKHO.CA: score=6.06 buy_ready=False sector_rank=7 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-09-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=13.79 buy_ready=False sector_rank=8 price=2.0 support=1.98 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=42469452.0 spike=0.61
- ELKA.CA: score=14.33 buy_ready=False sector_rank=11 price=1.73 support=1.7 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=48.21 liquidity=13048947.0 spike=0.29
- ELNA.CA: score=-1.52 buy_ready=False sector_rank=11 price=35.74 support=35.17 resistance=38.99 source=Yahoo Finance as_of=2026-09-13T21:00:00+00:00 freshness=FRESH RSI=22.51 liquidity=147999.35 spike=0.32
- ELSH.CA: score=10.56 buy_ready=False sector_rank=11 price=12.97 support=12.76 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=43.55 liquidity=6234762.5 spike=0.16
- ELWA.CA: score=0.18 buy_ready=False sector_rank=11 price=1.72 support=1.62 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=34.92 liquidity=849549.06 spike=0.35
- EMFD.CA: score=16.25 buy_ready=False sector_rank=12 price=14.24 support=11.51 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=76.8 liquidity=20130688.0 spike=0.12
- ENGC.CA: score=6.3 buy_ready=False sector_rank=11 price=41.35 support=41.0 resistance=54.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=29.38 liquidity=6976237.0 spike=0.43
- EOSB.CA: score=13.04 buy_ready=False sector_rank=11 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-09-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=187291.59 spike=2.76
- EPCO.CA: score=11.88 buy_ready=False sector_rank=11 price=11.11 support=10.8 resistance=12.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=4556272.0 spike=0.21
- EPPK.CA: score=-5.25 buy_ready=False sector_rank=11 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=20.4 buy_ready=False sector_rank=2 price=129.02 support=112.1 resistance=131.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=82.89 liquidity=137211008.0 spike=0.71
- ETRS.CA: score=15.37 buy_ready=False sector_rank=11 price=10.81 support=10.7 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=44.68 liquidity=8045668.5 spike=0.35
- EXPA.CA: score=17.15 buy_ready=False sector_rank=15 price=20.78 support=19.8 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=59.51 liquidity=14795505.0 spike=0.41
- FAIT.CA: score=9.97 buy_ready=False sector_rank=15 price=46.09 support=39.58 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=69.14 liquidity=822751.63 spike=0.09
- FAITA.CA: score=4.16 buy_ready=False sector_rank=15 price=0.99 support=0.98 resistance=1.02 source=Yahoo Finance as_of=2026-09-13T21:00:00+00:00 freshness=FRESH RSI=41.03 liquidity=10856.67 spike=0.21
- FERC.CA: score=11.59 buy_ready=False sector_rank=6 price=78.01 support=76.7 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=50.3 liquidity=4197604.5 spike=0.21
- FWRY.CA: score=16.16 buy_ready=False sector_rank=14 price=18.97 support=18.66 resistance=19.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=45.68 liquidity=62914724.0 spike=0.46
- GBCO.CA: score=17.45 buy_ready=False sector_rank=19 price=30.26 support=27.51 resistance=31.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=44.6 liquidity=33842788.0 spike=0.67
- GDWA.CA: score=12.9 buy_ready=False sector_rank=11 price=0.77 support=0.77 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=46.71 liquidity=9574677.0 spike=0.23
- GGCC.CA: score=9.39 buy_ready=False sector_rank=11 price=0.85 support=0.83 resistance=1.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=42.15 liquidity=5057880.5 spike=0.11
- GIHD.CA: score=19.33 buy_ready=False sector_rank=11 price=73.54 support=58.01 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=67.75 liquidity=10403979.0 spike=0.35
- GMCI.CA: score=-1.34 buy_ready=False sector_rank=11 price=1.76 support=1.77 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=28.0 liquidity=333766.78 spike=0.66
- GRCA.CA: score=8.33 buy_ready=False sector_rank=11 price=40.12 support=41.41 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=22.51 liquidity=27001430.0 spike=0.34
- GSSC.CA: score=10.11 buy_ready=False sector_rank=11 price=284.99 support=278.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=46.79 liquidity=2785518.0 spike=0.22
- GTWL.CA: score=17.33 buy_ready=False sector_rank=11 price=237.08 support=161.03 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=66.07 liquidity=46074324.0 spike=0.15
- HDBK.CA: score=19.15 buy_ready=False sector_rank=15 price=110.83 support=88.85 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=69.38 liquidity=14539564.0 spike=0.25
- HELI.CA: score=21.25 buy_ready=False sector_rank=12 price=8.0 support=7.34 resistance=8.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=63.58 liquidity=56016952.0 spike=0.35
- HRHO.CA: score=12.3 buy_ready=False sector_rank=20 price=25.28 support=25.21 resistance=26.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=38.14 liquidity=42867236.0 spike=0.43
- ICID.CA: score=9.79 buy_ready=False sector_rank=11 price=18.26 support=13.4 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=60.95 liquidity=462967.75 spike=0.02
- IDRE.CA: score=11.16 buy_ready=False sector_rank=11 price=53.24 support=51.02 resistance=57.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=43.65 liquidity=3830603.75 spike=0.41
- IFAP.CA: score=15.07 buy_ready=False sector_rank=4 price=20.27 support=20.2 resistance=22.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=47.55 liquidity=8670888.0 spike=0.35
- INFI.CA: score=8.98 buy_ready=False sector_rank=11 price=132.8 support=131.01 resistance=174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=8.85 liquidity=6648365.5 spike=0.17
- IRON.CA: score=8.44 buy_ready=False sector_rank=6 price=27.3 support=27.83 resistance=33.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=7.1 liquidity=9045626.0 spike=0.64
- ISMA.CA: score=6.55 buy_ready=False sector_rank=11 price=29.05 support=29.0 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=34.04 liquidity=7220468.0 spike=0.27
- ISMQ.CA: score=15.4 buy_ready=False sector_rank=6 price=8.8 support=8.85 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=10638118.0 spike=0.35
- ISPH.CA: score=8.57 buy_ready=False sector_rank=18 price=12.39 support=12.21 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=24.48 liquidity=36418764.0 spike=0.52
- JUFO.CA: score=13.19 buy_ready=False sector_rank=16 price=26.76 support=26.45 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=45.94 liquidity=8324562.0 spike=0.34
- KABO.CA: score=22.62 buy_ready=False sector_rank=5 price=9.81 support=8.82 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=63.2 liquidity=23949108.0 spike=0.45
- KWIN.CA: score=11.15 buy_ready=False sector_rank=11 price=86.82 support=84.5 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=38.98 liquidity=6822202.0 spike=0.1
- KZPC.CA: score=19.33 buy_ready=False sector_rank=11 price=14.2 support=11.5 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=59.71 liquidity=10736209.0 spike=0.16
- LCSW.CA: score=12.68 buy_ready=False sector_rank=13 price=33.35 support=32.61 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=42.77 liquidity=8452542.0 spike=0.28
- LUTS.CA: score=4.33 buy_ready=False sector_rank=11 price=0.95 support=0.88 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=96439624.0 spike=0.35
- MAAL.CA: score=7.34 buy_ready=False sector_rank=11 price=8.8 support=8.18 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=47.28 liquidity=3012062.5 spike=0.28
- MASR.CA: score=21.33 buy_ready=False sector_rank=11 price=7.98 support=7.49 resistance=8.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=56.07 liquidity=63959252.0 spike=0.7
- MBSC.CA: score=17.23 buy_ready=False sector_rank=13 price=379.85 support=355.04 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=52.74 liquidity=26568414.0 spike=0.37
- MCQE.CA: score=17.23 buy_ready=False sector_rank=13 price=217.19 support=212.01 resistance=255.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=38.59 liquidity=15008298.0 spike=0.34
- MCRO.CA: score=18.43 buy_ready=False sector_rank=11 price=1.76 support=1.44 resistance=1.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=77.5 liquidity=115034512.0 spike=1.05
- MENA.CA: score=-0.15 buy_ready=False sector_rank=12 price=6.62 support=6.58 resistance=7.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=29.55 liquidity=597436.19 spike=0.19
- MEPA.CA: score=16.77 buy_ready=False sector_rank=11 price=1.96 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=57.5 liquidity=5446690.0 spike=0.15
- MFPC.CA: score=17.4 buy_ready=False sector_rank=6 price=46.85 support=38.93 resistance=48.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=79.61 liquidity=45399116.0 spike=0.34
- MFSC.CA: score=9.93 buy_ready=False sector_rank=11 price=49.1 support=48.88 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=50.82 liquidity=2601035.0 spike=0.52
- MHOT.CA: score=8.53 buy_ready=False sector_rank=10 price=17.93 support=17.72 resistance=19.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=2032910.13 spike=0.18
- MICH.CA: score=11.49 buy_ready=False sector_rank=11 price=49.18 support=47.11 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=44.67 liquidity=4165699.75 spike=0.16
- MILS.CA: score=6.48 buy_ready=False sector_rank=11 price=201.18 support=191.0 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=19.84 liquidity=4150947.0 spike=0.08
- MIPH.CA: score=8.65 buy_ready=False sector_rank=18 price=807.87 support=700.2 resistance=820.0 source=Yahoo Finance as_of=2026-09-13T21:00:00+00:00 freshness=FRESH RSI=67.27 liquidity=2077841.63 spike=0.52
- MOED.CA: score=19.33 buy_ready=False sector_rank=11 price=0.81 support=0.69 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=53.58 liquidity=39466992.0 spike=0.33
- MOIL.CA: score=8.24 buy_ready=False sector_rank=7 price=0.67 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=45.21 liquidity=179479.23 spike=0.83
- MOIN.CA: score=5.63 buy_ready=False sector_rank=11 price=36.77 support=35.5 resistance=39.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=47021152.0 spike=1.65
- MOSC.CA: score=2.87 buy_ready=False sector_rank=11 price=308.65 support=300.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=22.1 liquidity=539930.0 spike=0.05
- MPCI.CA: score=17.33 buy_ready=False sector_rank=11 price=410.38 support=345.0 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=51.77 liquidity=49921540.0 spike=0.3
- MPCO.CA: score=23.4 buy_ready=False sector_rank=4 price=2.61 support=2.07 resistance=2.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=61.16 liquidity=89825816.0 spike=0.6
- MPRC.CA: score=9.34 buy_ready=False sector_rank=11 price=38.49 support=38.31 resistance=46.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=35.11 liquidity=5012300.5 spike=0.12
- MTIE.CA: score=12.1 buy_ready=False sector_rank=19 price=8.38 support=8.1 resistance=9.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=35.17 liquidity=8652286.0 spike=0.19
- NAHO.CA: score=-5.14 buy_ready=False sector_rank=11 price=0.14 support=0.13 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=131077.7 spike=1.2
- NCCW.CA: score=5.51 buy_ready=False sector_rank=11 price=8.25 support=7.61 resistance=8.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=84917712.0 spike=1.59
- NEDA.CA: score=4.6 buy_ready=False sector_rank=11 price=2.73 support=2.7 resistance=2.97 source=Yahoo Finance as_of=2026-09-13T21:00:00+00:00 freshness=FRESH RSI=45.24 liquidity=272033.58 spike=0.29
- NHPS.CA: score=2.67 buy_ready=False sector_rank=11 price=76.68 support=75.82 resistance=98.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=14.58 liquidity=3337263.0 spike=0.13
- NINH.CA: score=12.73 buy_ready=False sector_rank=11 price=20.83 support=21.4 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=46.49 liquidity=8405761.0 spike=0.28
- NIPH.CA: score=11.57 buy_ready=False sector_rank=18 price=315.9 support=301.0 resistance=414.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=16.45 liquidity=74469728.0 spike=0.31
- OBRI.CA: score=7.87 buy_ready=False sector_rank=11 price=30.83 support=30.1 resistance=34.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=37.48 liquidity=4543829.0 spike=0.21
- OCDI.CA: score=9.25 buy_ready=False sector_rank=12 price=29.27 support=30.0 resistance=34.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=34.84 liquidity=48346444.0 spike=0.55
- OCPH.CA: score=1.54 buy_ready=False sector_rank=11 price=242.67 support=241.05 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=28.04 liquidity=1213155.38 spike=0.11
- ODIN.CA: score=5.37 buy_ready=False sector_rank=11 price=2.8 support=2.55 resistance=3.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=25.88 liquidity=6037350.5 spike=0.19
- OFH.CA: score=19.33 buy_ready=False sector_rank=11 price=1.06 support=0.86 resistance=1.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=63.59 liquidity=43753080.0 spike=0.4
- OIH.CA: score=22.4 buy_ready=False sector_rank=1 price=2.13 support=1.75 resistance=2.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=70.18 liquidity=46290784.0 spike=0.36
- OLFI.CA: score=10.38 buy_ready=False sector_rank=16 price=22.43 support=22.07 resistance=25.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=36.76 liquidity=6510088.0 spike=0.15
- ORAS.CA: score=4.6 buy_ready=False sector_rank=9 price=849.69 support=834.5 resistance=855.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48510620.0 spike=1.0
- ORHD.CA: score=19.25 buy_ready=False sector_rank=12 price=42.38 support=40.28 resistance=43.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=50.7 liquidity=43485424.0 spike=0.32
- ORWE.CA: score=20.62 buy_ready=False sector_rank=5 price=26.89 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=50.4 liquidity=13900226.0 spike=0.26
- PHAR.CA: score=11.57 buy_ready=False sector_rank=18 price=118.32 support=118.16 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=18.06 liquidity=43751744.0 spike=0.22
- PHDC.CA: score=14.25 buy_ready=False sector_rank=12 price=13.82 support=13.65 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=35.18 liquidity=40365776.0 spike=0.19
- PHTV.CA: score=9.07 buy_ready=False sector_rank=11 price=350.0 support=311.27 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=41.44 liquidity=1741308.13 spike=0.84
- POUL.CA: score=15.87 buy_ready=False sector_rank=16 price=38.28 support=36.97 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=57.38 liquidity=14708783.0 spike=0.63
- PRCL.CA: score=6.6 buy_ready=False sector_rank=13 price=32.13 support=30.9 resistance=36.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=41.06 liquidity=2368797.0 spike=0.11
- PRDC.CA: score=6.95 buy_ready=False sector_rank=12 price=7.81 support=7.77 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=25.16 liquidity=7698201.0 spike=0.11
- PRMH.CA: score=5.84 buy_ready=False sector_rank=11 price=2.54 support=2.28 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=65.48 liquidity=1514116.75 spike=0.13
- RACC.CA: score=7.45 buy_ready=False sector_rank=11 price=9.67 support=9.4 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=43.06 liquidity=3118209.0 spike=0.13
- RAKT.CA: score=5.39 buy_ready=False sector_rank=11 price=22.15 support=21.4 resistance=23.09 source=Yahoo Finance as_of=2026-09-13T21:00:00+00:00 freshness=FRESH RSI=47.52 liquidity=64722.3 spike=0.25
- RAYA.CA: score=11.53 buy_ready=False sector_rank=21 price=7.08 support=6.95 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=52.45 liquidity=8267034.0 spike=0.13
- RMDA.CA: score=16.57 buy_ready=False sector_rank=18 price=6.08 support=5.77 resistance=6.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=51.3 liquidity=23760722.0 spike=0.39
- ROTO.CA: score=2.94 buy_ready=False sector_rank=11 price=40.33 support=35.02 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=12.86 liquidity=3611370.25 spike=0.28
- RREI.CA: score=16.27 buy_ready=False sector_rank=11 price=4.34 support=4.24 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=41.46 liquidity=8941086.0 spike=0.3
- RTVC.CA: score=2.97 buy_ready=False sector_rank=11 price=3.97 support=3.78 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=32.73 liquidity=638889.0 spike=0.09
- RUBX.CA: score=16.33 buy_ready=False sector_rank=11 price=12.92 support=12.36 resistance=13.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=36.32 liquidity=10141709.0 spike=0.51
- SAUD.CA: score=9.36 buy_ready=False sector_rank=15 price=23.17 support=22.83 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=39.95 liquidity=2206803.75 spike=0.14
- SCEM.CA: score=17.23 buy_ready=False sector_rank=13 price=96.78 support=94.0 resistance=112.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=48.59 liquidity=13993727.0 spike=0.09
- SCFM.CA: score=0.37 buy_ready=False sector_rank=11 price=272.93 support=270.0 resistance=305.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=33.35 liquidity=1044118.5 spike=0.1
- SCTS.CA: score=3.55 buy_ready=False sector_rank=3 price=605.02 support=566.66 resistance=660.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=19.76 liquidity=1147059.63 spike=0.22
- SDTI.CA: score=14.13 buy_ready=False sector_rank=11 price=74.6 support=67.0 resistance=76.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=58.42 liquidity=4798143.0 spike=0.24
- SEIG.CA: score=-0.14 buy_ready=False sector_rank=11 price=245.56 support=247.24 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=32.91 liquidity=529705.63 spike=0.32
- SIPC.CA: score=21.33 buy_ready=False sector_rank=11 price=5.92 support=4.1 resistance=6.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=64.01 liquidity=24548098.0 spike=0.4
- SKPC.CA: score=20.4 buy_ready=False sector_rank=6 price=18.1 support=16.8 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=54.32 liquidity=59604512.0 spike=0.43
- SMFR.CA: score=1.73 buy_ready=False sector_rank=11 price=240.26 support=240.0 resistance=276.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=28.92 liquidity=2399403.75 spike=0.21
- SNFC.CA: score=16.04 buy_ready=False sector_rank=11 price=10.88 support=10.26 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=62.73 liquidity=5713311.0 spike=0.41
- SPIN.CA: score=16.83 buy_ready=False sector_rank=5 price=17.76 support=18.12 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=39.96 liquidity=8210227.0 spike=0.23
- SPMD.CA: score=9.33 buy_ready=False sector_rank=11 price=0.61 support=0.58 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=459169472.0 spike=25.34
- SUGR.CA: score=20.87 buy_ready=False sector_rank=16 price=61.83 support=50.0 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=49.23 liquidity=18492446.0 spike=0.26
- SVCE.CA: score=19.33 buy_ready=False sector_rank=11 price=11.84 support=10.28 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=60.29 liquidity=65152936.0 spike=0.39
- SWDY.CA: score=19.79 buy_ready=False sector_rank=8 price=127.34 support=115.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=49.59 liquidity=45654168.0 spike=0.48
- TALM.CA: score=29.4 buy_ready=False sector_rank=3 price=23.35 support=17.11 resistance=22.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=68.14 liquidity=266274352.0 spike=6.32
- TMGH.CA: score=16.25 buy_ready=False sector_rank=12 price=95.55 support=94.9 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=45.3 liquidity=86443296.0 spike=0.31
- TRTO.CA: score=9.33 buy_ready=False sector_rank=11 price=0.07 support=0.04 resistance=0.08 source=Yahoo Finance as_of=2026-09-13T21:00:00+00:00 freshness=FRESH RSI=67.92 liquidity=3150.42 spike=0.1
- UEFM.CA: score=11.34 buy_ready=False sector_rank=11 price=534.5 support=440.66 resistance=570.0 source=Yahoo Finance as_of=2026-09-13T21:00:00+00:00 freshness=FRESH RSI=45.76 liquidity=5750685.5 spike=1.63
- UEGC.CA: score=7.73 buy_ready=False sector_rank=11 price=1.68 support=1.66 resistance=2.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=20.59 liquidity=8400993.0 spike=0.18
- UNIP.CA: score=14.33 buy_ready=False sector_rank=11 price=0.37 support=0.35 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=49.44 liquidity=10831876.0 spike=0.3
- UNIT.CA: score=8.47 buy_ready=False sector_rank=12 price=20.01 support=19.98 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=34558008.0 spike=3.11
- WCDF.CA: score=16.02 buy_ready=False sector_rank=11 price=745.28 support=630.0 resistance=729.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=86.64 liquidity=5833351.5 spike=1.93
- WKOL.CA: score=18.97 buy_ready=False sector_rank=11 price=346.53 support=326.5 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=48.27 liquidity=9638638.0 spike=0.48
- ZEOT.CA: score=9.8 buy_ready=False sector_rank=11 price=13.42 support=13.1 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=40.36 liquidity=2474211.0 spike=0.19
- ZMID.CA: score=19.25 buy_ready=False sector_rank=12 price=9.23 support=7.39 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=71.16 liquidity=80616424.0 spike=0.33

## Backtesting Lite
- TALM.CA: 180d return=45.38%, max drawdown=-12.27%, MA20>MA50 days last20=20, as_of=2026-09-13T21:00:00+00:00
- CIRA.CA: 180d return=124.03%, max drawdown=-16.44%, MA20>MA50 days last20=20, as_of=2026-09-13T21:00:00+00:00
- MPCO.CA: 180d return=47.09%, max drawdown=-16.86%, MA20>MA50 days last20=20, as_of=2026-09-13T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- CIRA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Investment and Real Estate Development summary=CIRA Education take over 51% of L’École Française Hurghada; CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion; CIRA Education launches Middle East’s 1st initiative for care economy
  - CIRA Education take over 51% of L’École Française Hurghada: https://english.mubasher.info/news/4488666/CIRA-Education-take-over-51-of-L-%C3%89cole-Fran%C3%A7aise-Hurghada/
  - CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion: https://english.mubasher.info/news/4393636/CIRA-s-majority-shareholder-acquires-37-5-additional-equity-backs-regional-expansion/
  - CIRA Education launches Middle East’s 1st initiative for care economy: https://english.mubasher.info/news/4391766/CIRA-Education-launches-Middle-East-s-1st-initiative-for-care-economy/
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=622 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- KABO.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Nasr Clothing and Textiles summary=KABO posts EGP 17m in Q1-25/26 unaudited consolidated net profits; KABO sells over 1.9m shares in Spinalex for EGP 20m; KABO unveils international agreements, expansion plan including export lines
  - KABO posts EGP 17m in Q1-25/26 unaudited consolidated net profits: https://english.mubasher.info/news/4600162/KABO-posts-EGP-17m-in-Q1-25-26-unaudited-consolidated-net-profits/
  - KABO sells over 1.9m shares in Spinalex for EGP 20m: https://english.mubasher.info/news/4543747/KABO-sells-over-1-9m-shares-in-Spinalex-for-EGP-20m/
  - KABO unveils international agreements, expansion plan including export lines: https://english.mubasher.info/news/4533185/KABO-unveils-international-agreements-expansion-plan-including-export-lines/
- OIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Investment Holding summary=Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- CERA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=The Arab Ceramic Co. summary=Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- MASR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=622 sources=3 expected=Madinet Masr For Housing and Development summary=Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval; Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended; Madinet Masr to distribute treasury stocks in first-ever move
  - Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval: https://english.mubasher.info/news/4601386/Madinet-Masr-to-pay-out-EGP-0-15-shr-for-2025-upon-equityholders-approval/
  - Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended: https://english.mubasher.info/news/4578449/Madinet-Masr-logs-24-higher-consolidated-profits-in-2025-dividends-recommended/
  - Madinet Masr to distribute treasury stocks in first-ever move: https://english.mubasher.info/news/4577724/Madinet-Masr-to-distribute-treasury-stocks-in-first-ever-move/

## Warnings
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for KABO.CA matches the company but no source/report date was detected.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- Evidence for MASR.CA matches the company but appears old; latest detected date is 2025-01-01.
