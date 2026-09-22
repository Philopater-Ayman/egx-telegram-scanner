# Telegram-First EGX Scanner Report

Scan phase: Evening tomorrow plan
Generated UTC: 2026-09-22T19:50:39.813510+00:00
Generated Cairo: 2026-09-22 22:50
Run timing: target 19:30 Cairo | generated Cairo 2026-09-22 22:50 | cron 30 16 * * 0-4
Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-09-22 22:48

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 177/186
- Top sector: Investment Holding

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, September 22
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 21.05% / above MA50 57.89%
- EGX70 regime: BEARISH / above MA20 30.0% / above MA50 55.0%
- Sector breadth: 38.1%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=949324800.0 spike=1.53 score=12.46
- CCAP.CA: liquidity=732470400.0 spike=0.87 score=21.4
- ETEL.CA: liquidity=453855968.0 spike=1.79 score=23.98
- NIPH.CA: liquidity=419252896.0 spike=2.79 score=7.58
- ORHD.CA: liquidity=319671200.0 spike=2.35 score=19.64

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30/EGX70 stay bearish with a defensive risk mode, so the scanner highlights only watch‑list tickets based on relative strength, liquidity spikes and sector leadership despite no new‑buy signal.
- Top tickets (GBCO.CA, ETEL.CA) show accumulation spikes and bullish‑watch outlooks but sit near 20‑day resistance, limiting upside in the next 1‑3 days.
- Sector breadth is weak (38.1% above MA20); leading sectors like Investment Holding and Telecommunications give relative strength, yet most stocks are extended (RSI>60) and liquidity is cooling.
- Support/resistance gaps are modest (e.g., ETEL.CA ~23% above support, resistance slightly negative), suggesting price may test resistance before pulling back.
- EGX30/EGX70 bearish trend shifts risk mode to DEFENSIVE_NO_NEW_BUY, raising uncertainty and discouraging new entries until breadth improves.

## Top Liquidity Spikes
- NEDA.CA: spike=11.88 liquidity=7372879.0 outlook=NEUTRAL score=42.62 buy_ready=False
- EGTS.CA: spike=5.08 liquidity=114232544.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- NIPH.CA: spike=2.79 liquidity=419252896.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SEIG.CA: spike=2.44 liquidity=4200065.0 outlook=WEAK_OR_RISKY score=28.62 buy_ready=False
- GBCO.CA: spike=2.4 liquidity=167279536.0 outlook=BULLISH_WATCH score=78.71 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=13.25 5d=4.09% 20d=21.55% aboveMA50=100.0%
- #2 Telecommunications: score=10.86 5d=2.98% 20d=9.42% aboveMA50=100.0%
- #3 Agriculture & Food Production: score=9.85 5d=5.68% 20d=12.05% aboveMA50=100.0%
- #4 Transportation & Logistics: score=7.88 5d=5.21% 20d=1.09% aboveMA50=100.0%
- #5 Energy & Petrochemicals: score=7.25 5d=4.48% 20d=3.4% aboveMA50=66.67%
- #6 Banking & Financials: score=6.75 5d=2.82% 20d=4.7% aboveMA50=80.0%
- #7 Automotive & Distribution: score=5.71 5d=2.42% 20d=-1.41% aboveMA50=50.0%
- #8 Basic Resources & Chemicals: score=4.63 5d=1.92% 20d=2.73% aboveMA50=60.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ETEL.CA: BULLISH_WATCH score=83 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support
- DTPP.CA: BULLISH_WATCH score=82.62 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- OIH.CA: BULLISH_WATCH score=82 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- GBCO.CA: BULLISH_WATCH score=78.71 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- CPCI.CA: BULLISH_WATCH score=78.62 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- IFAP.CA: BULLISH_WATCH score=77.85 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20
- SAUD.CA: BULLISH_WATCH score=75.75 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended
- EXPA.CA: BULLISH_WATCH score=73.75 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended
- AMOC.CA: BULLISH_WATCH score=73.25 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; far above support
- BINV.CA: BULLISH_WATCH score=73 liquidity=TRADEABLE sector=LEADING risk=overheated RSI

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- CICH.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=14.25 buy_ready=False sector_rank=16 price=290.0 support=288.01 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.82 liquidity=14690579.0 spike=0.58
- ABUK.CA: score=22.85 buy_ready=False sector_rank=8 price=93.73 support=75.01 resistance=96.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=59.62 liquidity=97974136.0 spike=0.54
- ACAMD.CA: score=16.25 buy_ready=False sector_rank=16 price=2.03 support=1.99 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=24396366.0 spike=0.43
- ACGC.CA: score=14.67 buy_ready=False sector_rank=11 price=14.09 support=13.55 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=48.89 liquidity=6644566.0 spike=0.19
- ADCI.CA: score=5.33 buy_ready=False sector_rank=16 price=283.19 support=267.66 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=20.86 liquidity=3082339.25 spike=0.63
- ADIB.CA: score=19.4 buy_ready=False sector_rank=6 price=52.48 support=50.51 resistance=55.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.3 liquidity=45185816.0 spike=0.58
- ADPC.CA: score=17.75 buy_ready=False sector_rank=16 price=3.98 support=3.81 resistance=4.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.28 liquidity=31544312.0 spike=1.75
- AFDI.CA: score=4.7 buy_ready=False sector_rank=16 price=52.77 support=51.6 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.99 liquidity=5448802.0 spike=0.22
- AFMC.CA: score=11.37 buy_ready=False sector_rank=16 price=159.58 support=153.0 resistance=239.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.79 liquidity=7125847.0 spike=0.12
- AJWA.CA: score=9.88 buy_ready=False sector_rank=16 price=180.0 support=175.15 resistance=199.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=47.21 liquidity=5636622.0 spike=0.13
- ALCN.CA: score=23.82 buy_ready=False sector_rank=4 price=34.08 support=30.03 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.47 liquidity=42444224.0 spike=1.21
- ALUM.CA: score=2.24 buy_ready=False sector_rank=16 price=25.5 support=25.0 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=30.52 liquidity=2992195.0 spike=0.21
- AMER.CA: score=13.94 buy_ready=False sector_rank=19 price=5.24 support=4.8 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.37 liquidity=41784748.0 spike=0.76
- AMES.CA: score=8.25 buy_ready=False sector_rank=16 price=51.09 support=48.45 resistance=158.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=9.27 liquidity=80112064.0 spike=0.3
- AMIA.CA: score=12.25 buy_ready=False sector_rank=16 price=18.49 support=17.12 resistance=21.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=33.83 liquidity=23665816.0 spike=0.48
- AMOC.CA: score=21.4 buy_ready=False sector_rank=5 price=13.44 support=10.65 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.3 liquidity=59774252.0 spike=0.34
- APSW.CA: score=-1.3 buy_ready=False sector_rank=16 price=8.22 support=8.2 resistance=8.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=34.38 liquidity=452155.53 spike=0.48
- ARAB.CA: score=8.94 buy_ready=False sector_rank=19 price=0.24 support=0.24 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.61 liquidity=46025868.0 spike=0.45
- ARCC.CA: score=11.5 buy_ready=False sector_rank=21 price=70.52 support=69.0 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=20.43 liquidity=11184824.0 spike=0.28
- AREH.CA: score=7.73 buy_ready=False sector_rank=16 price=1.41 support=1.39 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=3479798.0 spike=0.24
- ASCM.CA: score=4.88 buy_ready=False sector_rank=16 price=59.02 support=58.16 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=31.4 liquidity=5635812.5 spike=0.29
- ASPI.CA: score=14.25 buy_ready=False sector_rank=16 price=0.43 support=0.41 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.41 liquidity=38545796.0 spike=0.62
- ATLC.CA: score=14.46 buy_ready=False sector_rank=10 price=7.01 support=5.35 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=52.63 liquidity=4335959.5 spike=0.15
- ATQA.CA: score=24.85 buy_ready=False sector_rank=8 price=13.11 support=11.0 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.31 liquidity=81928168.0 spike=0.74
- AXPH.CA: score=19.45 buy_ready=False sector_rank=16 price=1691.79 support=1501.0 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.72 liquidity=10144296.0 spike=1.1
- BINV.CA: score=21.4 buy_ready=False sector_rank=1 price=57.27 support=48.04 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=75.89 liquidity=21564676.0 spike=0.89
- BIOC.CA: score=9.25 buy_ready=False sector_rank=16 price=271.12 support=247.03 resistance=488.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.38 liquidity=55589272.0 spike=0.58
- BTFH.CA: score=16.13 buy_ready=False sector_rank=10 price=2.92 support=2.87 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.34 liquidity=74613048.0 spike=0.92
- CAED.CA: score=3.88 buy_ready=False sector_rank=16 price=124.46 support=122.6 resistance=173.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=32.49 liquidity=4632860.5 spike=0.2
- CANA.CA: score=21.19 buy_ready=False sector_rank=6 price=47.51 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=70.58 liquidity=7789217.5 spike=0.34
- CCAP.CA: score=21.4 buy_ready=False sector_rank=1 price=7.2 support=5.72 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=732470400.0 spike=0.87
- CCRS.CA: score=14.04 buy_ready=False sector_rank=16 price=2.57 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=48.74 liquidity=7790675.5 spike=0.14
- CEFM.CA: score=8.21 buy_ready=False sector_rank=16 price=143.19 support=135.0 resistance=167.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.55 liquidity=966143.06 spike=0.09
- CERA.CA: score=17.25 buy_ready=False sector_rank=16 price=1.39 support=1.22 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.92 liquidity=77030056.0 spike=0.62
- CFGH.CA: score=7.26 buy_ready=False sector_rank=16 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=7714.89 spike=0.44
- CIEB.CA: score=15.75 buy_ready=False sector_rank=6 price=24.79 support=24.01 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.7 liquidity=6350786.5 spike=0.46
- CIRA.CA: score=19.82 buy_ready=False sector_rank=9 price=40.31 support=32.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=75.87 liquidity=16872534.0 spike=0.42
- CLHO.CA: score=9.0 buy_ready=False sector_rank=18 price=15.83 support=15.4 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=12.13 liquidity=24010150.0 spike=0.33
- CNFN.CA: score=6.17 buy_ready=False sector_rank=10 price=4.51 support=4.46 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.59 liquidity=7042272.0 spike=0.6
- COMI.CA: score=12.46 buy_ready=False sector_rank=6 price=131.85 support=131.11 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.85 liquidity=949324800.0 spike=1.53
- COPR.CA: score=17.25 buy_ready=False sector_rank=16 price=0.49 support=0.46 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.4 liquidity=10940717.0 spike=0.23
- COSG.CA: score=14.25 buy_ready=False sector_rank=16 price=1.78 support=1.78 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=13513451.0 spike=0.4
- CPCI.CA: score=14.0 buy_ready=False sector_rank=16 price=564.43 support=530.0 resistance=584.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=60.45 liquidity=2754758.0 spike=0.83
- CSAG.CA: score=8.01 buy_ready=False sector_rank=4 price=38.39 support=36.5 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=27.53 liquidity=3607392.75 spike=0.23
- DAPH.CA: score=9.25 buy_ready=False sector_rank=16 price=110.54 support=108.11 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.49 liquidity=17855296.0 spike=0.3
- DEIN.CA: score=7.25 buy_ready=False sector_rank=16 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=1.7 buy_ready=False sector_rank=15 price=26.47 support=25.56 resistance=29.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.65 liquidity=2384506.5 spike=0.45
- DSCW.CA: score=8.25 buy_ready=False sector_rank=16 price=1.79 support=1.77 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.35 liquidity=10194767.0 spike=0.33
- DTPP.CA: score=20.87 buy_ready=False sector_rank=16 price=336.13 support=294.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.6 liquidity=135517216.0 spike=1.81
- EALR.CA: score=6.88 buy_ready=False sector_rank=16 price=369.73 support=340.0 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=33.51 liquidity=7632856.0 spike=0.53
- EASB.CA: score=10.61 buy_ready=False sector_rank=16 price=7.66 support=7.2 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.61 liquidity=3366091.0 spike=0.2
- EAST.CA: score=8.32 buy_ready=False sector_rank=15 price=31.86 support=31.31 resistance=36.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=11.07 liquidity=17769114.0 spike=0.23
- EBSC.CA: score=4.38 buy_ready=False sector_rank=16 price=2.0 support=1.91 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.26 liquidity=2133379.25 spike=0.14
- ECAP.CA: score=14.29 buy_ready=False sector_rank=16 price=31.89 support=31.16 resistance=36.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=46.37 liquidity=11379295.0 spike=1.02
- EDFM.CA: score=4.92 buy_ready=False sector_rank=16 price=400.02 support=390.0 resistance=465.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=43.16 liquidity=674084.5 spike=0.37
- EEII.CA: score=4.38 buy_ready=False sector_rank=16 price=2.25 support=2.15 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=33.9 liquidity=6135427.0 spike=0.4
- EFIC.CA: score=14.85 buy_ready=False sector_rank=8 price=184.91 support=183.0 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=43.33 liquidity=22343572.0 spike=0.06
- EFID.CA: score=17.32 buy_ready=False sector_rank=15 price=30.63 support=29.71 resistance=32.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.36 liquidity=26420912.0 spike=0.4
- EFIH.CA: score=14.29 buy_ready=False sector_rank=17 price=22.93 support=22.16 resistance=24.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.2 liquidity=62728492.0 spike=1.06
- EGAL.CA: score=18.85 buy_ready=False sector_rank=8 price=366.14 support=345.0 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.02 liquidity=28880188.0 spike=0.28
- EGAS.CA: score=12.58 buy_ready=False sector_rank=5 price=56.55 support=55.0 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.42 liquidity=6183258.5 spike=0.52
- EGBE.CA: score=4.48 buy_ready=False sector_rank=6 price=0.52 support=0.49 resistance=0.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=78808.98 spike=0.96
- EGCH.CA: score=18.85 buy_ready=False sector_rank=8 price=13.91 support=13.3 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=52099404.0 spike=0.43
- EGSA.CA: score=10.4 buy_ready=False sector_rank=2 price=9.0 support=8.68 resistance=9.1 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=78.18 liquidity=3654.0 spike=0.59
- EGTS.CA: score=8.94 buy_ready=False sector_rank=19 price=18.71 support=16.85 resistance=18.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=114232544.0 spike=5.08
- EHDR.CA: score=6.78 buy_ready=False sector_rank=16 price=2.65 support=2.65 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.43 liquidity=7534952.0 spike=0.41
- ELEC.CA: score=8.46 buy_ready=False sector_rank=14 price=1.96 support=1.92 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=42682268.0 spike=0.55
- ELKA.CA: score=5.55 buy_ready=False sector_rank=16 price=1.67 support=1.64 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=13.16 liquidity=6300295.5 spike=0.17
- ELNA.CA: score=-1.6 buy_ready=False sector_rank=16 price=35.22 support=33.96 resistance=38.99 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=24.57 liquidity=154827.13 spike=0.42
- ELSH.CA: score=13.35 buy_ready=False sector_rank=16 price=12.71 support=12.55 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.74 liquidity=9102761.0 spike=0.24
- ELWA.CA: score=0.06 buy_ready=False sector_rank=16 price=1.69 support=1.66 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.95 liquidity=814831.5 spike=0.38
- EMFD.CA: score=16.94 buy_ready=False sector_rank=19 price=13.48 support=12.1 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.19 liquidity=40342688.0 spike=0.24
- ENGC.CA: score=14.99 buy_ready=False sector_rank=16 price=41.47 support=41.0 resistance=47.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=49.72 liquidity=22052972.0 spike=1.37
- EOSB.CA: score=9.72 buy_ready=False sector_rank=16 price=1.57 support=1.53 resistance=1.64 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=76532.79 spike=1.2
- EPCO.CA: score=9.89 buy_ready=False sector_rank=16 price=10.77 support=10.6 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=44.78 liquidity=5646107.0 spike=0.35
- EPPK.CA: score=-5.33 buy_ready=False sector_rank=16 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=23.98 buy_ready=False sector_rank=2 price=138.53 support=112.5 resistance=136.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=85.57 liquidity=453855968.0 spike=1.79
- ETRS.CA: score=10.17 buy_ready=False sector_rank=16 price=10.87 support=10.66 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.51 liquidity=2924377.75 spike=0.21
- EXPA.CA: score=23.4 buy_ready=False sector_rank=6 price=21.95 support=19.96 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=64.72 liquidity=35958924.0 spike=0.97
- FAIT.CA: score=10.88 buy_ready=False sector_rank=6 price=47.08 support=41.52 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=67.5 liquidity=1475498.0 spike=0.18
- FAITA.CA: score=6.42 buy_ready=False sector_rank=6 price=0.99 support=0.98 resistance=1.02 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=41.18 liquidity=16085.14 spike=0.33
- FERC.CA: score=11.34 buy_ready=False sector_rank=8 price=78.22 support=77.3 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=4483994.0 spike=0.3
- FWRY.CA: score=14.17 buy_ready=False sector_rank=17 price=18.93 support=18.66 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.24 liquidity=50574564.0 spike=0.37
- GBCO.CA: score=26.08 buy_ready=False sector_rank=7 price=31.12 support=27.51 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.86 liquidity=167279536.0 spike=2.4
- GDWA.CA: score=8.25 buy_ready=False sector_rank=16 price=0.75 support=0.75 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=13.22 liquidity=17119108.0 spike=0.39
- GGCC.CA: score=14.25 buy_ready=False sector_rank=16 price=0.81 support=0.83 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=19831758.0 spike=0.6
- GIHD.CA: score=13.72 buy_ready=False sector_rank=16 price=72.44 support=61.61 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.29 liquidity=4475831.0 spike=0.16
- GMCI.CA: score=-1.53 buy_ready=False sector_rank=16 price=1.76 support=1.69 resistance=1.94 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=30.0 liquidity=224906.88 spike=0.47
- GRCA.CA: score=3.87 buy_ready=False sector_rank=16 price=39.53 support=38.7 resistance=85.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=20.93 liquidity=5619615.5 spike=0.09
- GSSC.CA: score=14.48 buy_ready=False sector_rank=16 price=304.9 support=278.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=61.87 liquidity=3227560.0 spike=0.35
- GTWL.CA: score=19.25 buy_ready=False sector_rank=16 price=237.45 support=201.3 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.63 liquidity=92998984.0 spike=0.47
- HDBK.CA: score=23.4 buy_ready=False sector_rank=6 price=118.35 support=90.51 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.79 liquidity=10401468.0 spike=0.17
- HELI.CA: score=20.94 buy_ready=False sector_rank=19 price=8.15 support=7.34 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.92 liquidity=101920952.0 spike=0.6
- HRHO.CA: score=9.99 buy_ready=False sector_rank=10 price=24.58 support=24.83 resistance=26.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.67 liquidity=143108352.0 spike=1.43
- ICID.CA: score=10.02 buy_ready=False sector_rank=16 price=17.1 support=16.2 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.78 liquidity=2770278.25 spike=0.23
- IDRE.CA: score=15.27 buy_ready=False sector_rank=16 price=54.24 support=51.0 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.86 liquidity=6022855.0 spike=0.36
- IFAP.CA: score=16.26 buy_ready=False sector_rank=3 price=20.59 support=19.05 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.05 liquidity=5856322.5 spike=0.26
- INFI.CA: score=6.15 buy_ready=False sector_rank=16 price=126.94 support=123.0 resistance=168.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.11 liquidity=6903748.5 spike=0.25
- IRON.CA: score=2.88 buy_ready=False sector_rank=8 price=27.17 support=26.3 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=24.29 liquidity=3025771.25 spike=0.21
- ISMA.CA: score=9.53 buy_ready=False sector_rank=16 price=29.46 support=28.05 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.67 liquidity=5286347.0 spike=0.23
- ISMQ.CA: score=10.85 buy_ready=False sector_rank=8 price=8.77 support=8.68 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.39 liquidity=11112172.0 spike=0.43
- ISPH.CA: score=9.0 buy_ready=False sector_rank=18 price=12.19 support=11.9 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.5 liquidity=29451656.0 spike=0.41
- JUFO.CA: score=20.32 buy_ready=False sector_rank=15 price=27.18 support=26.45 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.83 liquidity=14811150.0 spike=0.7
- KABO.CA: score=18.02 buy_ready=False sector_rank=11 price=9.27 support=8.9 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.27 liquidity=19158640.0 spike=0.45
- KWIN.CA: score=3.19 buy_ready=False sector_rank=16 price=86.14 support=82.5 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=18.91 liquidity=3937810.25 spike=0.07
- KZPC.CA: score=12.51 buy_ready=False sector_rank=16 price=13.69 support=12.6 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.9 liquidity=3260169.0 spike=0.09
- LCSW.CA: score=8.5 buy_ready=False sector_rank=21 price=33.33 support=31.61 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=25.24 liquidity=20129022.0 spike=0.83
- LUTS.CA: score=17.25 buy_ready=False sector_rank=16 price=0.89 support=0.83 resistance=1.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.2 liquidity=33935596.0 spike=0.18
- MAAL.CA: score=5.69 buy_ready=False sector_rank=16 price=9.14 support=8.7 resistance=9.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20197958.0 spike=1.72
- MASR.CA: score=14.25 buy_ready=False sector_rank=16 price=7.69 support=7.49 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=45.56 liquidity=41131384.0 spike=0.41
- MBSC.CA: score=11.5 buy_ready=False sector_rank=21 price=338.63 support=340.66 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=20.64 liquidity=21191946.0 spike=0.43
- MCQE.CA: score=8.5 buy_ready=False sector_rank=21 price=206.96 support=207.1 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.89 liquidity=24126828.0 spike=0.78
- MCRO.CA: score=19.45 buy_ready=False sector_rank=16 price=1.67 support=1.48 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=134441600.0 spike=1.1
- MENA.CA: score=4.51 buy_ready=False sector_rank=19 price=6.72 support=6.58 resistance=7.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.32 liquidity=568390.13 spike=0.31
- MEPA.CA: score=16.67 buy_ready=False sector_rank=16 price=1.91 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=46.91 liquidity=9419672.0 spike=0.24
- MFPC.CA: score=17.85 buy_ready=False sector_rank=8 price=48.82 support=39.02 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=76.27 liquidity=70304912.0 spike=0.39
- MFSC.CA: score=8.25 buy_ready=False sector_rank=16 price=49.64 support=48.5 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.06 liquidity=1004363.63 spike=0.2
- MHOT.CA: score=10.12 buy_ready=False sector_rank=12 price=17.9 support=16.61 resistance=19.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.1 liquidity=8107030.0 spike=0.84
- MICH.CA: score=17.25 buy_ready=False sector_rank=16 price=47.53 support=47.51 resistance=53.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=10163868.0 spike=0.63
- MILS.CA: score=11.53 buy_ready=False sector_rank=16 price=191.26 support=180.01 resistance=232.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=35.45 liquidity=7278509.5 spike=0.27
- MIPH.CA: score=6.68 buy_ready=False sector_rank=18 price=879.95 support=861.0 resistance=941.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19000672.0 spike=2.34
- MOED.CA: score=8.25 buy_ready=False sector_rank=16 price=0.72 support=0.7 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.78 liquidity=19846444.0 spike=0.26
- MOIL.CA: score=14.3 buy_ready=False sector_rank=5 price=0.7 support=0.66 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=58.57 liquidity=284956.12 spike=1.31
- MOIN.CA: score=14.27 buy_ready=False sector_rank=16 price=35.69 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=54.45 liquidity=7017362.5 spike=0.23
- MOSC.CA: score=0.31 buy_ready=False sector_rank=16 price=299.38 support=290.0 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.83 liquidity=1061057.63 spike=0.15
- MPCI.CA: score=12.61 buy_ready=False sector_rank=16 price=393.07 support=371.11 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=16.95 liquidity=169804656.0 spike=1.18
- MPCO.CA: score=22.4 buy_ready=False sector_rank=3 price=2.79 support=2.07 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=72.25 liquidity=107334672.0 spike=0.63
- MPRC.CA: score=6.03 buy_ready=False sector_rank=16 price=38.29 support=37.65 resistance=46.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.87 liquidity=6780998.5 spike=0.17
- MTIE.CA: score=9.67 buy_ready=False sector_rank=7 price=8.19 support=8.02 resistance=8.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=21.74 liquidity=9381374.0 spike=0.29
- NAHO.CA: score=-4.32 buy_ready=False sector_rank=16 price=0.13 support=0.13 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=94326.53 spike=1.67
- NCCW.CA: score=21.25 buy_ready=False sector_rank=16 price=7.21 support=5.77 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.95 liquidity=54960636.0 spike=0.83
- NEDA.CA: score=16.62 buy_ready=False sector_rank=16 price=2.75 support=2.7 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=7372879.0 spike=11.88
- NHPS.CA: score=2.03 buy_ready=False sector_rank=16 price=73.25 support=72.52 resistance=98.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=9.18 liquidity=2784468.25 spike=0.16
- NINH.CA: score=6.99 buy_ready=False sector_rank=16 price=20.41 support=20.3 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=32.64 liquidity=7742415.5 spike=0.25
- NIPH.CA: score=7.58 buy_ready=False sector_rank=18 price=340.87 support=310.01 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419252896.0 spike=2.79
- OBRI.CA: score=4.97 buy_ready=False sector_rank=16 price=30.1 support=29.51 resistance=34.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=16.11 liquidity=6719481.5 spike=0.43
- OCDI.CA: score=13.94 buy_ready=False sector_rank=19 price=29.19 support=29.25 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=42.29 liquidity=39033084.0 spike=0.48
- OCPH.CA: score=6.12 buy_ready=False sector_rank=16 price=240.64 support=210.0 resistance=277.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.17 liquidity=5870982.5 spike=0.88
- ODIN.CA: score=9.45 buy_ready=False sector_rank=16 price=2.82 support=2.55 resistance=3.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=33.8 liquidity=24352384.0 spike=1.1
- OFH.CA: score=6.27 buy_ready=False sector_rank=16 price=1.09 support=1.04 resistance=1.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=251175008.0 spike=2.01
- OIH.CA: score=22.4 buy_ready=False sector_rank=1 price=2.13 support=1.91 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.97 liquidity=61610988.0 spike=0.52
- OLFI.CA: score=11.25 buy_ready=False sector_rank=15 price=22.71 support=22.07 resistance=23.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=54.22 liquidity=6938384.5 spike=0.39
- ORAS.CA: score=4.6 buy_ready=False sector_rank=13 price=841.52 support=836.12 resistance=848.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=100363736.0 spike=1.0
- ORHD.CA: score=19.64 buy_ready=False sector_rank=19 price=42.02 support=40.85 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.18 liquidity=319671200.0 spike=2.35
- ORWE.CA: score=20.02 buy_ready=False sector_rank=11 price=27.78 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.06 liquidity=31413674.0 spike=0.55
- PHAR.CA: score=9.0 buy_ready=False sector_rank=18 price=115.68 support=111.55 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=26.6 liquidity=98950600.0 spike=0.91
- PHDC.CA: score=8.94 buy_ready=False sector_rank=19 price=13.36 support=12.91 resistance=15.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.14 liquidity=89470696.0 spike=0.53
- PHTV.CA: score=5.11 buy_ready=False sector_rank=16 price=335.17 support=311.27 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=49.26 liquidity=862860.56 spike=0.51
- POUL.CA: score=16.88 buy_ready=False sector_rank=15 price=38.55 support=37.15 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=21 September 01:28 PM market time freshness=DELAYED_CURRENT RSI=38.94 liquidity=58845364.0 spike=2.28
- PRCL.CA: score=9.16 buy_ready=False sector_rank=21 price=30.95 support=30.61 resistance=34.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.88 liquidity=5663177.5 spike=0.31
- PRDC.CA: score=8.94 buy_ready=False sector_rank=19 price=7.56 support=7.51 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=9.33 liquidity=15394223.0 spike=0.26
- PRMH.CA: score=7.81 buy_ready=False sector_rank=16 price=2.59 support=2.32 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=3565456.0 spike=0.34
- RACC.CA: score=5.85 buy_ready=False sector_rank=16 price=9.69 support=9.4 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.44 liquidity=1600803.38 spike=0.09
- RAKT.CA: score=3.33 buy_ready=False sector_rank=16 price=22.08 support=21.4 resistance=23.02 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=47.17 liquidity=81607.68 spike=0.37
- RAYA.CA: score=13.81 buy_ready=False sector_rank=20 price=7.0 support=6.8 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=15193913.0 spike=0.28
- RMDA.CA: score=17.0 buy_ready=False sector_rank=18 price=6.06 support=5.77 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=14941217.0 spike=0.25
- ROTO.CA: score=5.87 buy_ready=False sector_rank=16 price=40.7 support=35.02 resistance=47.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.67 liquidity=6623861.0 spike=0.77
- RREI.CA: score=8.53 buy_ready=False sector_rank=16 price=4.21 support=4.2 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=40.62 liquidity=4278076.5 spike=0.24
- RTVC.CA: score=0.3 buy_ready=False sector_rank=16 price=3.86 support=3.79 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.69 liquidity=1052960.25 spike=0.24
- RUBX.CA: score=6.97 buy_ready=False sector_rank=16 price=14.12 support=14.07 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=90356304.0 spike=2.36
- SAUD.CA: score=23.4 buy_ready=False sector_rank=6 price=25.6 support=22.7 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=65.55 liquidity=17688072.0 spike=0.97
- SCEM.CA: score=8.5 buy_ready=False sector_rank=21 price=85.93 support=87.02 resistance=105.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=21.91 liquidity=43603660.0 spike=0.39
- SCFM.CA: score=0.29 buy_ready=False sector_rank=16 price=270.3 support=250.2 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=34.9 liquidity=1046218.06 spike=0.14
- SCTS.CA: score=2.12 buy_ready=False sector_rank=9 price=581.8 support=566.66 resistance=640.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=22.63 liquidity=1304219.0 spike=0.45
- SDTI.CA: score=16.89 buy_ready=False sector_rank=16 price=78.84 support=67.0 resistance=79.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=75.63 liquidity=34145612.0 spike=1.32
- SEIG.CA: score=6.33 buy_ready=False sector_rank=16 price=239.4 support=228.13 resistance=274.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=29.74 liquidity=4200065.0 spike=2.44
- SIPC.CA: score=17.25 buy_ready=False sector_rank=16 price=5.47 support=4.1 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.94 liquidity=31809460.0 spike=0.46
- SKPC.CA: score=18.85 buy_ready=False sector_rank=8 price=17.92 support=17.0 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.39 liquidity=56677848.0 spike=0.43
- SMFR.CA: score=0.95 buy_ready=False sector_rank=16 price=232.05 support=226.1 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=26.93 liquidity=1703453.5 spike=0.21
- SNFC.CA: score=18.25 buy_ready=False sector_rank=16 price=11.54 support=10.26 resistance=11.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=79.25 liquidity=13676199.0 spike=0.87
- SPIN.CA: score=6.93 buy_ready=False sector_rank=11 price=17.3 support=16.1 resistance=20.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=24.6 liquidity=3905470.25 spike=0.28
- SPMD.CA: score=14.25 buy_ready=False sector_rank=16 price=0.41 support=0.41 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.24 liquidity=15425748.0 spike=0.21
- SUGR.CA: score=14.76 buy_ready=False sector_rank=15 price=59.42 support=55.06 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.46 liquidity=7440432.0 spike=0.12
- SVCE.CA: score=17.25 buy_ready=False sector_rank=16 price=11.3 support=9.6 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.71 liquidity=68136240.0 spike=0.34
- SWDY.CA: score=17.46 buy_ready=False sector_rank=14 price=125.55 support=122.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.17 liquidity=10585356.0 spike=0.15
- TALM.CA: score=20.82 buy_ready=False sector_rank=9 price=20.86 support=17.11 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.79 liquidity=33252740.0 spike=0.5
- TMGH.CA: score=13.94 buy_ready=False sector_rank=19 price=94.18 support=93.08 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.73 liquidity=157738368.0 spike=0.55
- TRTO.CA: score=7.78 buy_ready=False sector_rank=16 price=0.06 support=0.05 resistance=0.08 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=48.39 liquidity=35016.92 spike=1.25
- UEFM.CA: score=0.82 buy_ready=False sector_rank=16 price=480.2 support=440.66 resistance=574.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=32.59 liquidity=2570455.75 spike=0.85
- UEGC.CA: score=16.97 buy_ready=False sector_rank=16 price=1.7 support=1.66 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.06 liquidity=68917624.0 spike=1.36
- UNIP.CA: score=12.15 buy_ready=False sector_rank=16 price=0.37 support=0.37 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=7900772.5 spike=0.34
- UNIT.CA: score=5.93 buy_ready=False sector_rank=19 price=18.13 support=17.12 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.79 liquidity=1987302.25 spike=0.14
- WCDF.CA: score=11.3 buy_ready=False sector_rank=16 price=706.22 support=636.31 resistance=796.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=67.72 liquidity=2051701.75 spike=0.4
- WKOL.CA: score=11.17 buy_ready=False sector_rank=16 price=334.07 support=325.0 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.17 liquidity=3923445.25 spike=0.27
- ZEOT.CA: score=9.33 buy_ready=False sector_rank=16 price=13.2 support=13.03 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.68 liquidity=2084812.25 spike=0.32
- ZMID.CA: score=16.94 buy_ready=False sector_rank=19 price=8.39 support=7.9 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.56 liquidity=93281472.0 spike=0.44

## Backtesting Lite
- GBCO.CA: 180d return=17.08%, max drawdown=-24.35%, MA20>MA50 days last20=0, as_of=2026-09-20T21:00:00+00:00
- ATQA.CA: 180d return=33.43%, max drawdown=-21.44%, MA20>MA50 days last20=20, as_of=2026-09-20T21:00:00+00:00
- ETEL.CA: 180d return=109.1%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-09-20T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- ATQA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr National Steel Ataqa summary=Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- HDBK.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Housing and Development Bank Egypt summary=Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- SAUD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=629 sources=3 expected=Al Baraka Bank Egypt summary=Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26; Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE; Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025
  - Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26: https://english.mubasher.info/news/4611927/Al-Baraka-Bank-Egypt-records-EGP-2-2bn-operating-income-in-Q1-26/
  - Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE: https://english.mubasher.info/news/4583822/Al-Baraka-Bank-Egypt-files-MTO-to-acquire-majority-stake-in-A-T-LEASE/
  - Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025: https://english.mubasher.info/news/4583458/Al-Baraka-Bank-Egypt-to-pay-EGP-1-1-share-dividends-for-2025/
- EXPA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Export Development Bank of Egypt summary=Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- ABUK.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Qir Fertilizers summary=Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results; Abu Qir Fertilizers&#39; board approves $5.6m coated urea project; Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26
  - Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results: https://english.mubasher.info/news/4604919/Abu-Qir-Fertilizers-generates-EGP-5-6bn-net-profits-in-Q1-26-unaudited-results/
  - Abu Qir Fertilizers&#39; board approves $5.6m coated urea project: https://english.mubasher.info/news/4585599/Abu-Qir-Fertilizers-board-approves-5-6m-coated-urea-project/
  - Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26: https://english.mubasher.info/news/4554415/Abu-Qir-Fertilizers-profits-exceed-EGP-5-1bn-in-H1-25-26/

## Warnings
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- Evidence for SAUD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- Evidence for ABUK.CA matches the company but no source/report date was detected.
