# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-09-17T10:28:12.187695+00:00
Generated Cairo: 2026-09-17 13:28
Run timing: target 08:45 Cairo | generated Cairo 2026-09-17 13:28 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-17 13:24

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 182/189
- Top sector: Investment Holding

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, September 17
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 40.0% / above MA50 60.0%
- EGX70 regime: BEARISH / above MA20 42.5% / above MA50 60.0%
- Sector breadth: 19.05%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=437137536.0 spike=0.79 score=10.03
- CCAP.CA: liquidity=377088480.0 spike=0.43 score=23.4
- ELEC.CA: liquidity=202402096.0 spike=2.78 score=9.18
- MFPC.CA: liquidity=197599824.0 spike=1.52 score=20.68
- ABUK.CA: liquidity=168835312.0 spike=1.08 score=18.8

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with weak breadth (~19% sector participation), putting the market in DEFENSIVE_NO_NEW_BUY mode; the scanner therefore holds all tickets despite some bullish watch signals.
- Tickets such as BINV.CA and WKOL.CA show accumulation spikes and bullish‑watch outlooks but sit far above 20‑day support with overheated RSI, limiting near‑term upside.
- Sector strength is confined to Investment Holding, Agriculture & Food Production and Telecommunications, yet overall sector breadth remains low (~19%), indicating narrow market participation.
- The bearish EGX30/EGX70 trend and low above‑MA20 percentages shift risk mode to DEFENSIVE_NO_NEW_BUY, raising uncertainty for any breakout in the next 1‑3 days.
- Liquidity spikes suggest short‑term interest, but cooling liquidity and extended momentum increase the chance of pull‑back or sideways movement over the short term.

## Top Liquidity Spikes
- WKOL.CA: spike=6.52 liquidity=82656600.0 outlook=BULLISH_WATCH score=91.08 buy_ready=False
- BINV.CA: spike=5.54 liquidity=94845112.0 outlook=BULLISH_WATCH score=83 buy_ready=False
- IDRE.CA: spike=4.62 liquidity=47784728.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AALR.CA: spike=4.39 liquidity=110243688.0 outlook=BULLISH_WATCH score=81.08 buy_ready=False
- EALR.CA: spike=4.04 liquidity=67792840.0 outlook=NEUTRAL score=45.08 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=16.74 5d=12.95% 20d=24.59% aboveMA50=100.0%
- #2 Agriculture & Food Production: score=11.08 5d=7.45% 20d=8.27% aboveMA50=100.0%
- #3 Telecommunications: score=9.44 5d=1.89% 20d=6.9% aboveMA50=100.0%
- #4 Education: score=5.83 5d=1.67% 20d=4.14% aboveMA50=66.67%
- #5 Energy & Petrochemicals: score=4.23 5d=-2.32% 20d=1.37% aboveMA50=75.0%
- #6 Basic Resources & Chemicals: score=4.11 5d=-3.16% 20d=3.23% aboveMA50=70.0%
- #7 Industrial Goods & Cables: score=4.04 5d=-2.46% 20d=-1.1% aboveMA50=50.0%
- #8 Textiles: score=3.62 5d=-4.62% 20d=2.87% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- IFAP.CA: BULLISH_WATCH score=96 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- WKOL.CA: BULLISH_WATCH score=91.08 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- EGAS.CA: BULLISH_WATCH score=85.23 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- OIH.CA: BULLISH_WATCH score=84 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- BINV.CA: BULLISH_WATCH score=83 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support
- AALR.CA: BULLISH_WATCH score=81.08 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- EGCH.CA: BULLISH_WATCH score=80.11 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- FERC.CA: BULLISH_WATCH score=80.11 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- SWDY.CA: BULLISH_WATCH score=80.04 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MPCO.CA: BULLISH_WATCH score=78 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended; far above support

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=22.43 buy_ready=False sector_rank=14 price=323.85 support=295.0 resistance=351.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=69.61 liquidity=110243688.0 spike=4.39
- ABUK.CA: score=18.8 buy_ready=False sector_rank=6 price=93.04 support=75.01 resistance=94.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=67.23 liquidity=168835312.0 spike=1.08
- ACAMD.CA: score=18.43 buy_ready=False sector_rank=14 price=2.11 support=1.95 resistance=2.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=24398328.0 spike=0.42
- ACGC.CA: score=18.45 buy_ready=False sector_rank=8 price=13.99 support=12.04 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=47.61 liquidity=16465502.0 spike=0.4
- ADCI.CA: score=8.84 buy_ready=False sector_rank=14 price=279.91 support=267.66 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=37.6 liquidity=1409710.38 spike=0.23
- ADIB.CA: score=18.03 buy_ready=False sector_rank=9 price=52.2 support=50.51 resistance=55.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=38.56 liquidity=14182559.0 spike=0.21
- ADPC.CA: score=11.61 buy_ready=False sector_rank=14 price=3.89 support=3.81 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=45.28 liquidity=7175494.0 spike=0.32
- AFDI.CA: score=15.12 buy_ready=False sector_rank=14 price=55.95 support=51.6 resistance=68.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=49.6 liquidity=7687660.0 spike=0.31
- AFMC.CA: score=9.43 buy_ready=False sector_rank=14 price=160.63 support=157.0 resistance=264.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=21.86 liquidity=10653114.0 spike=0.19
- AJWA.CA: score=10.22 buy_ready=False sector_rank=14 price=180.16 support=175.15 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:00 AM market time freshness=DELAYED_CURRENT RSI=43.59 liquidity=5788332.5 spike=0.12
- ALCN.CA: score=16.32 buy_ready=False sector_rank=15 price=31.7 support=30.03 resistance=34.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=54.87 liquidity=6902275.0 spike=0.24
- ALUM.CA: score=4.62 buy_ready=False sector_rank=14 price=26.06 support=25.0 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:00 AM market time freshness=DELAYED_CURRENT RSI=20.1 liquidity=2187284.75 spike=0.15
- AMER.CA: score=12.9 buy_ready=False sector_rank=10 price=5.43 support=4.8 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=32.45 liquidity=20726056.0 spike=0.33
- AMES.CA: score=8.43 buy_ready=False sector_rank=14 price=52.63 support=51.22 resistance=173.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=2.68 liquidity=39589536.0 spike=0.15
- AMIA.CA: score=8.63 buy_ready=False sector_rank=14 price=17.29 support=15.3 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=35.75 liquidity=1201389.0 spike=0.02
- AMOC.CA: score=18.69 buy_ready=False sector_rank=5 price=13.69 support=10.65 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=74.61 liquidity=63918604.0 spike=0.35
- APSW.CA: score=3.92 buy_ready=False sector_rank=14 price=8.42 support=8.37 resistance=9.1 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=44.94 liquidity=487795.86 spike=0.51
- ARAB.CA: score=19.9 buy_ready=False sector_rank=10 price=0.26 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=15227108.0 spike=0.15
- ARCC.CA: score=17.02 buy_ready=False sector_rank=19 price=72.73 support=71.5 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=42.22 liquidity=10503185.0 spike=0.24
- AREH.CA: score=7.52 buy_ready=False sector_rank=14 price=1.43 support=1.39 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=3087476.25 spike=0.19
- ARVA.CA: score=4.43 buy_ready=False sector_rank=14 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=10.19 buy_ready=False sector_rank=14 price=60.6 support=60.15 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=36.59 liquidity=5753281.5 spike=0.29
- ASPI.CA: score=17.43 buy_ready=False sector_rank=14 price=0.45 support=0.41 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=38.27 liquidity=50554076.0 spike=0.9
- ATLC.CA: score=14.29 buy_ready=False sector_rank=16 price=7.24 support=5.2 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=66.16 liquidity=4899741.5 spike=0.18
- ATQA.CA: score=18.64 buy_ready=False sector_rank=6 price=12.53 support=10.8 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=66.33 liquidity=15813653.0 spike=0.15
- AXPH.CA: score=16.47 buy_ready=False sector_rank=14 price=1699.05 support=1351.0 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:56 AM market time freshness=DELAYED_CURRENT RSI=56.86 liquidity=5038987.0 spike=0.41
- BINV.CA: score=28.4 buy_ready=False sector_rank=1 price=63.62 support=46.25 resistance=62.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=83.0 liquidity=94845112.0 spike=5.54
- BIOC.CA: score=9.28 buy_ready=False sector_rank=14 price=280.27 support=272.01 resistance=515.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=14.21 liquidity=9846366.0 spike=0.08
- BTFH.CA: score=13.39 buy_ready=False sector_rank=16 price=2.95 support=2.87 resistance=3.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=37.93 liquidity=30254394.0 spike=0.31
- CAED.CA: score=6.53 buy_ready=False sector_rank=14 price=127.18 support=123.56 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=29.76 liquidity=4094250.25 spike=0.1
- CANA.CA: score=20.91 buy_ready=False sector_rank=9 price=42.55 support=41.0 resistance=44.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:57 AM market time freshness=DELAYED_CURRENT RSI=48.65 liquidity=20298070.0 spike=1.44
- CCAP.CA: score=23.4 buy_ready=False sector_rank=1 price=6.98 support=5.42 resistance=6.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=81.32 liquidity=377088480.0 spike=0.43
- CCRS.CA: score=19.43 buy_ready=False sector_rank=14 price=2.71 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=38.89 liquidity=50439496.0 spike=0.98
- CEFM.CA: score=10.3 buy_ready=False sector_rank=14 price=147.16 support=138.1 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=865138.94 spike=0.06
- CERA.CA: score=19.43 buy_ready=False sector_rank=14 price=1.47 support=1.22 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=57.63 liquidity=81913424.0 spike=0.84
- CFGH.CA: score=5.43 buy_ready=False sector_rank=14 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=613.56 spike=0.03
- CICH.CA: score=10.45 buy_ready=False sector_rank=16 price=12.75 support=12.0 resistance=13.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=54.91 liquidity=1064320.0 spike=0.22
- CIEB.CA: score=10.6 buy_ready=False sector_rank=9 price=24.86 support=24.01 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:00 AM market time freshness=DELAYED_CURRENT RSI=46.05 liquidity=2563816.5 spike=0.19
- CIRA.CA: score=19.61 buy_ready=False sector_rank=4 price=39.55 support=32.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=68.68 liquidity=8276318.0 spike=0.22
- CLHO.CA: score=9.28 buy_ready=False sector_rank=17 price=16.0 support=15.81 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=33.81 liquidity=38370760.0 spike=0.5
- CNFN.CA: score=7.25 buy_ready=False sector_rank=16 price=4.56 support=4.46 resistance=4.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:55 AM market time freshness=DELAYED_CURRENT RSI=38.57 liquidity=3860805.0 spike=0.33
- COMI.CA: score=10.03 buy_ready=False sector_rank=9 price=132.93 support=131.11 resistance=142.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:00 AM market time freshness=DELAYED_CURRENT RSI=31.43 liquidity=437137536.0 spike=0.79
- COPR.CA: score=17.43 buy_ready=False sector_rank=14 price=0.5 support=0.46 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=37.33 liquidity=14301029.0 spike=0.16
- COSG.CA: score=10.01 buy_ready=False sector_rank=14 price=1.82 support=1.74 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=48.72 liquidity=2582353.75 spike=0.06
- CPCI.CA: score=6.62 buy_ready=False sector_rank=14 price=544.76 support=525.01 resistance=569.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=26.84 liquidity=2192118.5 spike=0.53
- CSAG.CA: score=17.42 buy_ready=False sector_rank=15 price=37.76 support=36.5 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=36.74 liquidity=12863788.0 spike=0.78
- DAPH.CA: score=17.43 buy_ready=False sector_rank=14 price=122.67 support=108.11 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=52.89 liquidity=14948552.0 spike=0.24
- DEIN.CA: score=7.43 buy_ready=False sector_rank=14 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=0.01 buy_ready=False sector_rank=21 price=26.88 support=26.51 resistance=29.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:00 AM market time freshness=DELAYED_CURRENT RSI=27.87 liquidity=1261040.13 spike=0.22
- DSCW.CA: score=8.99 buy_ready=False sector_rank=14 price=1.84 support=1.8 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=37.93 liquidity=4562789.0 spike=0.12
- DTPP.CA: score=19.57 buy_ready=False sector_rank=14 price=339.99 support=292.5 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=68.98 liquidity=69980648.0 spike=1.07
- EALR.CA: score=17.43 buy_ready=False sector_rank=14 price=385.47 support=340.0 resistance=426.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=34.06 liquidity=67792840.0 spike=4.04
- EASB.CA: score=12.77 buy_ready=False sector_rank=14 price=8.22 support=7.16 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=56.2 liquidity=1338698.13 spike=0.08
- EAST.CA: score=6.15 buy_ready=False sector_rank=21 price=32.84 support=32.0 resistance=36.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=28.11 liquidity=8409675.0 spike=0.12
- EBSC.CA: score=8.78 buy_ready=False sector_rank=14 price=2.04 support=1.88 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:00 AM market time freshness=DELAYED_CURRENT RSI=47.87 liquidity=1346405.38 spike=0.09
- ECAP.CA: score=5.33 buy_ready=False sector_rank=14 price=32.51 support=31.16 resistance=39.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:59 AM market time freshness=DELAYED_CURRENT RSI=43.33 liquidity=899932.13 spike=0.08
- EDFM.CA: score=9.79 buy_ready=False sector_rank=14 price=411.84 support=394.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=59.07 liquidity=354870.88 spike=0.22
- EEII.CA: score=0.12 buy_ready=False sector_rank=14 price=2.19 support=2.15 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=31.58 liquidity=1683685.5 spike=0.08
- EFIC.CA: score=14.64 buy_ready=False sector_rank=6 price=195.86 support=192.75 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=31333382.0 spike=0.35
- EFID.CA: score=16.74 buy_ready=False sector_rank=21 price=31.11 support=29.71 resistance=33.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=39.52 liquidity=26457372.0 spike=0.47
- EFIH.CA: score=17.06 buy_ready=False sector_rank=18 price=23.42 support=22.16 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:00 AM market time freshness=DELAYED_CURRENT RSI=40.81 liquidity=19195108.0 spike=0.3
- EGAL.CA: score=20.64 buy_ready=False sector_rank=6 price=370.03 support=321.01 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=49.34 liquidity=29824656.0 spike=0.28
- EGAS.CA: score=21.45 buy_ready=False sector_rank=5 price=58.54 support=55.0 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=43.63 liquidity=11863616.0 spike=1.38
- EGBE.CA: score=3.11 buy_ready=False sector_rank=9 price=0.5 support=0.49 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=29.63 liquidity=74339.8 spike=0.55
- EGCH.CA: score=20.64 buy_ready=False sector_rank=6 price=14.01 support=13.3 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=58.58 liquidity=39472944.0 spike=0.35
- EGSA.CA: score=9.79 buy_ready=False sector_rank=3 price=9.0 support=8.67 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 September 01:08 PM market time freshness=DELAYED_CURRENT RSI=78.18 liquidity=10410.0 spike=1.19
- EGTS.CA: score=10.65 buy_ready=False sector_rank=10 price=17.26 support=16.17 resistance=18.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:58 AM market time freshness=DELAYED_CURRENT RSI=46.62 liquidity=3750254.75 spike=0.15
- EHDR.CA: score=7.48 buy_ready=False sector_rank=14 price=2.77 support=2.73 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=3051818.0 spike=0.15
- EKHO.CA: score=6.69 buy_ready=False sector_rank=5 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=9.18 buy_ready=False sector_rank=7 price=2.05 support=1.92 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=202402096.0 spike=2.78
- ELKA.CA: score=8.05 buy_ready=False sector_rank=14 price=1.75 support=1.7 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:59 AM market time freshness=DELAYED_CURRENT RSI=47.17 liquidity=3616929.75 spike=0.08
- ELNA.CA: score=-1.54 buy_ready=False sector_rank=14 price=35.74 support=33.96 resistance=38.99 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=22.51 liquidity=23302.48 spike=0.05
- ELSH.CA: score=9.17 buy_ready=False sector_rank=14 price=12.91 support=12.67 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=41.01 liquidity=4741233.5 spike=0.12
- ELWA.CA: score=6.03 buy_ready=False sector_rank=14 price=1.7 support=1.62 resistance=1.99 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=36.36 liquidity=1599076.14 spike=0.65
- EMFD.CA: score=19.9 buy_ready=False sector_rank=10 price=14.09 support=11.55 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=74.05 liquidity=22700680.0 spike=0.14
- ENGC.CA: score=1.36 buy_ready=False sector_rank=14 price=41.76 support=41.0 resistance=50.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:56 AM market time freshness=DELAYED_CURRENT RSI=34.08 liquidity=1928314.5 spike=0.16
- EOSB.CA: score=9.67 buy_ready=False sector_rank=14 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=77512.47 spike=1.08
- EPCO.CA: score=11.26 buy_ready=False sector_rank=14 price=11.27 support=10.8 resistance=12.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:58 AM market time freshness=DELAYED_CURRENT RSI=47.6 liquidity=1830156.63 spike=0.09
- EPPK.CA: score=-5.15 buy_ready=False sector_rank=14 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=19.4 buy_ready=False sector_rank=3 price=128.99 support=112.1 resistance=135.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=86.15 liquidity=105967080.0 spike=0.55
- ETRS.CA: score=9.97 buy_ready=False sector_rank=14 price=10.98 support=10.66 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=49.72 liquidity=2538597.75 spike=0.15
- EXPA.CA: score=13.88 buy_ready=False sector_rank=9 price=21.2 support=19.8 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=60.73 liquidity=3846447.0 spike=0.11
- FAIT.CA: score=12.42 buy_ready=False sector_rank=9 price=47.34 support=39.58 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=68.21 liquidity=2392000.5 spike=0.3
- FAITA.CA: score=0.04 buy_ready=False sector_rank=9 price=0.99 support=0.98 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=9.76 liquidity=10103.3 spike=0.21
- FERC.CA: score=20.35 buy_ready=False sector_rank=6 price=79.46 support=76.9 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=48.29 liquidity=9708463.0 spike=0.53
- FWRY.CA: score=14.06 buy_ready=False sector_rank=18 price=18.88 support=18.66 resistance=19.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=51.03 liquidity=12271207.0 spike=0.09
- GBCO.CA: score=14.36 buy_ready=False sector_rank=13 price=30.43 support=27.51 resistance=31.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:59 AM market time freshness=DELAYED_CURRENT RSI=63.69 liquidity=3914810.25 spike=0.07
- GDWA.CA: score=13.43 buy_ready=False sector_rank=14 price=0.78 support=0.76 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=43.66 liquidity=22410926.0 spike=0.56
- GGCC.CA: score=11.23 buy_ready=False sector_rank=14 price=0.87 support=0.83 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:58 AM market time freshness=DELAYED_CURRENT RSI=35.36 liquidity=6793202.0 spike=0.17
- GIHD.CA: score=10.4 buy_ready=False sector_rank=14 price=74.18 support=58.01 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:55 AM market time freshness=DELAYED_CURRENT RSI=65.35 liquidity=2966642.75 spike=0.1
- GMCI.CA: score=0.75 buy_ready=False sector_rank=14 price=1.75 support=1.69 resistance=1.95 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=23.33 liquidity=841701.0 spike=1.74
- GRCA.CA: score=8.43 buy_ready=False sector_rank=14 price=43.39 support=39.0 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=27.52 liquidity=18376906.0 spike=0.22
- GSSC.CA: score=4.43 buy_ready=False sector_rank=14 price=312.91 support=291.16 resistance=321.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10984359.0 spike=0.87
- GTWL.CA: score=19.43 buy_ready=False sector_rank=14 price=237.11 support=175.01 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=62.29 liquidity=53082020.0 spike=0.2
- HDBK.CA: score=17.95 buy_ready=False sector_rank=9 price=114.32 support=89.01 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=71.49 liquidity=7921581.5 spike=0.14
- HELI.CA: score=21.9 buy_ready=False sector_rank=10 price=8.29 support=7.34 resistance=8.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=68.15 liquidity=123199520.0 spike=0.79
- HRHO.CA: score=11.86 buy_ready=False sector_rank=16 price=25.49 support=25.04 resistance=26.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=40.38 liquidity=8469161.0 spike=0.09
- ICID.CA: score=10.18 buy_ready=False sector_rank=14 price=18.11 support=15.04 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=62.57 liquidity=750931.0 spike=0.04
- IDRE.CA: score=9.43 buy_ready=False sector_rank=14 price=56.92 support=53.8 resistance=59.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=47784728.0 spike=4.62
- IFAP.CA: score=21.27 buy_ready=False sector_rank=2 price=20.93 support=20.05 resistance=22.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=40.41 liquidity=7869895.0 spike=0.34
- INFI.CA: score=12.43 buy_ready=False sector_rank=14 price=137.79 support=130.15 resistance=174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=16.41 liquidity=16806832.0 spike=0.53
- IRON.CA: score=4.05 buy_ready=False sector_rank=6 price=27.79 support=26.3 resistance=33.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=2.57 liquidity=4406505.5 spike=0.3
- ISMA.CA: score=1.78 buy_ready=False sector_rank=14 price=29.74 support=28.05 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:00 AM market time freshness=DELAYED_CURRENT RSI=13.72 liquidity=2343860.0 spike=0.09
- ISMQ.CA: score=8.49 buy_ready=False sector_rank=6 price=8.82 support=8.68 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=37.6 liquidity=2849812.75 spike=0.1
- ISPH.CA: score=9.28 buy_ready=False sector_rank=17 price=12.07 support=11.9 resistance=13.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=30.22 liquidity=41315652.0 spike=0.64
- JUFO.CA: score=7.72 buy_ready=False sector_rank=21 price=27.01 support=26.45 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=47.8 liquidity=2980933.0 spike=0.15
- KABO.CA: score=15.66 buy_ready=False sector_rank=8 price=9.41 support=8.82 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=54.0 liquidity=5211398.0 spike=0.1
- KWIN.CA: score=7.09 buy_ready=False sector_rank=14 price=89.74 support=84.5 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=32.99 liquidity=7661428.5 spike=0.11
- KZPC.CA: score=17.43 buy_ready=False sector_rank=14 price=14.5 support=12.16 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=72.6 liquidity=10084268.0 spike=0.17
- LCSW.CA: score=12.36 buy_ready=False sector_rank=19 price=33.51 support=32.42 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=45.38 liquidity=8333399.0 spike=0.3
- LUTS.CA: score=17.43 buy_ready=False sector_rank=14 price=1.0 support=0.79 resistance=1.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=51.09 liquidity=42921488.0 spike=0.16
- MAAL.CA: score=1.03 buy_ready=False sector_rank=14 price=8.79 support=8.18 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=34.64 liquidity=1599482.5 spike=0.16
- MASR.CA: score=14.43 buy_ready=False sector_rank=14 price=7.88 support=7.49 resistance=8.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=57.2 liquidity=28788940.0 spike=0.32
- MBSC.CA: score=13.36 buy_ready=False sector_rank=19 price=377.13 support=355.04 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=45.97 liquidity=6331683.5 spike=0.11
- MCQE.CA: score=12.95 buy_ready=False sector_rank=19 price=221.52 support=213.0 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=40.18 liquidity=5921637.0 spike=0.16
- MCRO.CA: score=16.43 buy_ready=False sector_rank=14 price=1.7 support=1.44 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=79.49 liquidity=24989182.0 spike=0.21
- MENA.CA: score=6.46 buy_ready=False sector_rank=10 price=6.7 support=6.58 resistance=7.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=1559169.5 spike=0.61
- MEPA.CA: score=13.21 buy_ready=False sector_rank=14 price=1.95 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=58.97 liquidity=3773270.25 spike=0.11
- MFPC.CA: score=20.68 buy_ready=False sector_rank=6 price=50.34 support=38.93 resistance=48.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=83.75 liquidity=197599824.0 spike=1.52
- MFSC.CA: score=5.01 buy_ready=False sector_rank=14 price=49.02 support=48.5 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=579425.13 spike=0.12
- MHOT.CA: score=8.32 buy_ready=False sector_rank=11 price=17.97 support=17.62 resistance=19.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:55 AM market time freshness=DELAYED_CURRENT RSI=35.64 liquidity=1591973.0 spike=0.15
- MICH.CA: score=11.43 buy_ready=False sector_rank=14 price=49.48 support=47.2 resistance=53.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=48.29 liquidity=4000793.75 spike=0.16
- MILS.CA: score=5.26 buy_ready=False sector_rank=14 price=202.0 support=198.0 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=26.51 liquidity=2828189.75 spike=0.05
- MIPH.CA: score=10.69 buy_ready=False sector_rank=17 price=819.42 support=700.2 resistance=820.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=62.61 liquidity=1410014.63 spike=0.36
- MOED.CA: score=16.43 buy_ready=False sector_rank=14 price=0.79 support=0.74 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=51.14 liquidity=10805458.0 spike=0.09
- MOIL.CA: score=10.72 buy_ready=False sector_rank=5 price=0.68 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:00 AM market time freshness=DELAYED_CURRENT RSI=59.38 liquidity=32317.24 spike=0.16
- MOIN.CA: score=19.43 buy_ready=False sector_rank=14 price=37.82 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=53.46 liquidity=15148968.0 spike=0.53
- MOSC.CA: score=11.78 buy_ready=False sector_rank=14 price=314.83 support=302.0 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=29.45 liquidity=9064134.0 spike=1.14
- MPCI.CA: score=17.43 buy_ready=False sector_rank=14 price=410.03 support=345.0 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=53.87 liquidity=11255359.0 spike=0.07
- MPCO.CA: score=23.4 buy_ready=False sector_rank=2 price=2.72 support=2.07 resistance=2.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=65.61 liquidity=41541456.0 spike=0.26
- MPRC.CA: score=7.96 buy_ready=False sector_rank=14 price=39.45 support=38.31 resistance=46.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=35.32 liquidity=3527141.75 spike=0.09
- MTIE.CA: score=13.72 buy_ready=False sector_rank=13 price=8.48 support=8.1 resistance=8.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=45.86 liquidity=9268054.0 spike=0.22
- NAHO.CA: score=7.47 buy_ready=False sector_rank=14 price=0.14 support=0.13 resistance=0.15 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=41.67 liquidity=33459.51 spike=0.53
- NCCW.CA: score=16.43 buy_ready=False sector_rank=14 price=8.15 support=5.59 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=75.87 liquidity=32795260.0 spike=0.53
- NEDA.CA: score=4.77 buy_ready=False sector_rank=14 price=2.72 support=2.7 resistance=2.95 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=40.62 liquidity=334641.6 spike=0.47
- NHPS.CA: score=3.32 buy_ready=False sector_rank=14 price=76.92 support=75.31 resistance=98.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=6.12 liquidity=3888121.0 spike=0.19
- NINH.CA: score=9.43 buy_ready=False sector_rank=14 price=20.71 support=20.5 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=21.7 liquidity=18846448.0 spike=0.62
- NIPH.CA: score=12.28 buy_ready=False sector_rank=17 price=317.08 support=301.0 resistance=414.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=17.14 liquidity=32432798.0 spike=0.17
- OBRI.CA: score=5.18 buy_ready=False sector_rank=14 price=30.65 support=30.1 resistance=34.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=37.87 liquidity=1749869.13 spike=0.09
- OCDI.CA: score=14.9 buy_ready=False sector_rank=10 price=30.25 support=29.25 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=39.58 liquidity=27117240.0 spike=0.33
- OCPH.CA: score=2.13 buy_ready=False sector_rank=14 price=240.61 support=210.0 resistance=277.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=30.76 liquidity=1696534.13 spike=0.21
- ODIN.CA: score=1.04 buy_ready=False sector_rank=14 price=2.71 support=2.55 resistance=3.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=13.51 liquidity=1604856.38 spike=0.06
- OFH.CA: score=19.43 buy_ready=False sector_rank=14 price=1.06 support=0.88 resistance=1.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=40.74 liquidity=18154788.0 spike=0.16
- OIH.CA: score=24.4 buy_ready=False sector_rank=1 price=2.18 support=1.82 resistance=2.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=66.0 liquidity=50798928.0 spike=0.41
- OLFI.CA: score=10.88 buy_ready=False sector_rank=21 price=22.99 support=22.07 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=41.47 liquidity=7138659.0 spike=0.44
- ORAS.CA: score=4.6 buy_ready=False sector_rank=12 price=842.05 support=831.0 resistance=844.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=86298792.0 spike=1.0
- ORHD.CA: score=19.9 buy_ready=False sector_rank=10 price=42.8 support=40.28 resistance=43.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=49.0 liquidity=70242968.0 spike=0.51
- ORWE.CA: score=20.45 buy_ready=False sector_rank=8 price=27.27 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=57.35 liquidity=22189110.0 spike=0.45
- PHAR.CA: score=12.28 buy_ready=False sector_rank=17 price=118.4 support=117.01 resistance=141.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=19.32 liquidity=17380908.0 spike=0.11
- PHDC.CA: score=9.9 buy_ready=False sector_rank=10 price=13.7 support=13.65 resistance=15.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=31.85 liquidity=25337458.0 spike=0.13
- PHTV.CA: score=13.83 buy_ready=False sector_rank=14 price=367.22 support=311.27 resistance=389.0 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=64.27 liquidity=2978521.43 spike=1.71
- POUL.CA: score=10.18 buy_ready=False sector_rank=21 price=37.83 support=36.97 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:00 AM market time freshness=DELAYED_CURRENT RSI=47.07 liquidity=6438609.5 spike=0.27
- PRCL.CA: score=7.23 buy_ready=False sector_rank=19 price=31.93 support=30.9 resistance=35.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:59 AM market time freshness=DELAYED_CURRENT RSI=45.39 liquidity=1210930.25 spike=0.06
- PRDC.CA: score=9.9 buy_ready=False sector_rank=10 price=7.85 support=7.68 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=23.25 liquidity=18783054.0 spike=0.3
- PRMH.CA: score=6.55 buy_ready=False sector_rank=14 price=2.59 support=2.28 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=2119361.5 spike=0.2
- RACC.CA: score=7.86 buy_ready=False sector_rank=14 price=9.72 support=9.4 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=47.29 liquidity=3427797.75 spike=0.18
- RAKT.CA: score=10.49 buy_ready=False sector_rank=14 price=22.65 support=21.4 resistance=23.02 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=57.94 liquidity=55651.05 spike=0.22
- RAYA.CA: score=10.96 buy_ready=False sector_rank=20 price=7.09 support=6.95 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=7091266.5 spike=0.13
- RMDA.CA: score=14.4 buy_ready=False sector_rank=17 price=6.2 support=5.77 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=5128186.0 spike=0.09
- ROTO.CA: score=2.62 buy_ready=False sector_rank=14 price=40.8 support=35.02 resistance=51.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT RSI=17.65 liquidity=3187477.0 spike=0.3
- RREI.CA: score=19.43 buy_ready=False sector_rank=14 price=4.43 support=4.24 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=15475290.0 spike=0.57
- RTVC.CA: score=0.04 buy_ready=False sector_rank=14 price=3.93 support=3.85 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=28.33 liquidity=603951.06 spike=0.08
- RUBX.CA: score=16.69 buy_ready=False sector_rank=14 price=13.69 support=12.36 resistance=14.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=67.33 liquidity=5262075.5 spike=0.26
- SAUD.CA: score=9.86 buy_ready=False sector_rank=9 price=23.24 support=22.7 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:00 AM market time freshness=DELAYED_CURRENT RSI=50.96 liquidity=1824667.13 spike=0.13
- SCEM.CA: score=17.02 buy_ready=False sector_rank=19 price=95.16 support=94.0 resistance=105.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=43.18 liquidity=16469035.0 spike=0.12
- SCFM.CA: score=3.83 buy_ready=False sector_rank=14 price=278.02 support=265.51 resistance=297.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:00 AM market time freshness=DELAYED_CURRENT RSI=25.49 liquidity=1402775.88 spike=0.15
- SCTS.CA: score=1.85 buy_ready=False sector_rank=4 price=607.71 support=566.66 resistance=640.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=28.73 liquidity=513577.0 spike=0.1
- SDTI.CA: score=17.43 buy_ready=False sector_rank=14 price=74.0 support=67.0 resistance=76.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=65.18 liquidity=10886781.0 spike=0.54
- SEIG.CA: score=5.33 buy_ready=False sector_rank=14 price=246.29 support=228.13 resistance=274.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=43.16 liquidity=893164.13 spike=0.49
- SIPC.CA: score=19.43 buy_ready=False sector_rank=14 price=5.89 support=4.1 resistance=6.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=65.96 liquidity=11682701.0 spike=0.2
- SKPC.CA: score=20.64 buy_ready=False sector_rank=6 price=18.49 support=16.82 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=63.27 liquidity=50964184.0 spike=0.36
- SMFR.CA: score=8.4 buy_ready=False sector_rank=14 price=241.98 support=236.0 resistance=276.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=27.28 liquidity=8972890.0 spike=0.94
- SNFC.CA: score=18.79 buy_ready=False sector_rank=14 price=11.19 support=10.26 resistance=11.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=65.24 liquidity=9361630.0 spike=0.69
- SPIN.CA: score=5.88 buy_ready=False sector_rank=8 price=17.58 support=17.01 resistance=20.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:59 AM market time freshness=DELAYED_CURRENT RSI=28.41 liquidity=2433571.0 spike=0.12
- SPMD.CA: score=5.19 buy_ready=False sector_rank=14 price=0.45 support=0.44 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:06 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=89820848.0 spike=1.38
- SUGR.CA: score=14.98 buy_ready=False sector_rank=21 price=60.72 support=50.0 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=58.65 liquidity=6239075.5 spike=0.09
- SVCE.CA: score=19.43 buy_ready=False sector_rank=14 price=11.91 support=10.28 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=58.13 liquidity=72378304.0 spike=0.44
- SWDY.CA: score=20.62 buy_ready=False sector_rank=7 price=127.19 support=115.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=42.64 liquidity=19145334.0 spike=0.21
- TALM.CA: score=18.33 buy_ready=False sector_rank=4 price=21.78 support=17.11 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=80.86 liquidity=40506396.0 spike=0.67
- TMGH.CA: score=14.9 buy_ready=False sector_rank=10 price=95.28 support=94.86 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=40.75 liquidity=63960852.0 spike=0.24
- TRTO.CA: score=7.44 buy_ready=False sector_rank=14 price=0.07 support=0.05 resistance=0.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=67.92 liquidity=8015.92 spike=0.29
- UEFM.CA: score=5.89 buy_ready=False sector_rank=14 price=517.31 support=440.66 resistance=557.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=48.61 liquidity=1458221.88 spike=0.53
- UEGC.CA: score=9.43 buy_ready=False sector_rank=14 price=1.78 support=1.66 resistance=2.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=30.16 liquidity=12730171.0 spike=0.26
- UNIP.CA: score=11.81 buy_ready=False sector_rank=14 price=0.38 support=0.35 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:59 AM market time freshness=DELAYED_CURRENT RSI=52.13 liquidity=7377303.5 spike=0.22
- UNIT.CA: score=21.66 buy_ready=False sector_rank=10 price=19.51 support=18.11 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:58 AM market time freshness=DELAYED_CURRENT RSI=56.35 liquidity=9757378.0 spike=0.68
- WCDF.CA: score=12.24 buy_ready=False sector_rank=14 price=759.61 support=630.06 resistance=765.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=90.91 liquidity=3628373.5 spike=1.09
- WKOL.CA: score=26.43 buy_ready=False sector_rank=14 price=358.31 support=332.56 resistance=369.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=57.22 liquidity=82656600.0 spike=6.52
- ZEOT.CA: score=3.64 buy_ready=False sector_rank=14 price=13.11 support=13.03 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=28.1 liquidity=1203848.38 spike=0.16
- ZMID.CA: score=19.9 buy_ready=False sector_rank=10 price=9.59 support=7.41 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=62.03 liquidity=150835504.0 spike=0.61

## Backtesting Lite
- BINV.CA: 180d return=68.35%, max drawdown=-17.77%, MA20>MA50 days last20=20, as_of=2026-09-15T21:00:00+00:00
- WKOL.CA: 180d return=13.4%, max drawdown=-25.83%, MA20>MA50 days last20=20, as_of=2026-09-15T21:00:00+00:00
- OIH.CA: 180d return=83.05%, max drawdown=-14.56%, MA20>MA50 days last20=20, as_of=2026-09-15T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- WKOL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Wadi Kom Ombo For Land Reclamation Co. summary=Wadi Kom Ombo amends estimated budget for FY26/27; Wadi Kom Ombo eyes EGP 257.77m in FY26/27 net profits; Wadi Kom Ombo records lower net profits at nearly EGP 2m in Q1-25/26
  - Wadi Kom Ombo amends estimated budget for FY26/27: https://english.mubasher.info/news/4600336/Wadi-Kom-Ombo-amends-estimated-budget-for-FY26-27/
  - Wadi Kom Ombo eyes EGP 257.77m in FY26/27 net profits: https://english.mubasher.info/news/4585452/Wadi-Kom-Ombo-eyes-EGP-257-77m-in-FY26-27-net-profits/
  - Wadi Kom Ombo records lower net profits at nearly EGP 2m in Q1-25/26: https://english.mubasher.info/news/4531526/Wadi-Kom-Ombo-records-lower-net-profits-at-nearly-EGP-2m-in-Q1-25-26/
- OIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Investment Holding summary=Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=624 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- AALR.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=General Company For Land Reclamation, Development & Reconstruction summary=General Land Reclamation expects over EGP 8.6m net profits in FY26/27 estimated budget; General Land Reclamation incurs EGP 29.5m loss in FY18/19; General Land Reclamation turns to losses in 9M
  - General Land Reclamation expects over EGP 8.6m net profits in FY26/27 estimated budget: https://english.mubasher.info/news/4600324/General-Land-Reclamation-expects-over-EGP-8-6m-net-profits-in-FY26-27-estimated-budget/
  - General Land Reclamation incurs EGP 29.5m loss in FY18/19: https://english.mubasher.info/news/3525030/General-Land-Reclamation-incurs-EGP-29-5m-loss-in-FY18-19/
  - General Land Reclamation turns to losses in 9M: https://english.mubasher.info/news/3465326/General-Land-Reclamation-turns-to-losses-in-9M/
- HELI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Heliopolis Housing summary=Evidence rejected for HELI.CA: source text did not clearly match HELI.CA / Heliopolis Housing.
- UNIT.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=624 sources=3 expected=United Housing and Development summary=United Housing’s shareholders pass EGP 0.12/shr dividends for 2025; United Housing unveils EGP 5.9bn mixed-use project in Alexandria; United Housing’s consolidated net profits exceed EGP 174.5m in 9M-25
  - United Housing’s shareholders pass EGP 0.12/shr dividends for 2025: https://english.mubasher.info/news/4591202/United-Housing-s-shareholders-pass-EGP-0-12-shr-dividends-for-2025/
  - United Housing unveils EGP 5.9bn mixed-use project in Alexandria: https://english.mubasher.info/news/4540667/United-Housing-unveils-EGP-5-9bn-mixed-use-project-in-Alexandria/
  - United Housing’s consolidated net profits exceed EGP 174.5m in 9M-25: https://english.mubasher.info/news/4530945/United-Housing-s-consolidated-net-profits-exceed-EGP-174-5m-in-9M-25/

## Warnings
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for WKOL.CA matches the company but no source/report date was detected.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for AALR.CA matches the company but no source/report date was detected.
- Evidence rejected for HELI.CA: source text did not clearly match HELI.CA / Heliopolis Housing.
- Evidence for UNIT.CA matches the company but appears old; latest detected date is 2025-01-01.
