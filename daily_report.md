# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-10-18T09:56:38.084647+00:00
Generated Cairo: 2026-10-18 12:56
Run timing: target 08:45 Cairo | generated Cairo 2026-10-18 12:56 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-10-18 12:52

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 176/187
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, October 18
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 16.67% / above MA50 22.22%
- EGX70 regime: BEARISH / above MA20 7.89% / above MA50 13.16%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=540116992.0 spike=0.92 score=7.76
- ETEL.CA: liquidity=191787136.0 spike=0.72 score=24.02
- EGAL.CA: liquidity=159825312.0 spike=2.54 score=5.79
- ORHD.CA: liquidity=131938008.0 spike=0.88 score=6.51
- UEGC.CA: liquidity=119798944.0 spike=2.84 score=20.08

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with weak breadth, triggering defensive risk mode; the scanner flags a few tickets with relatively strong outlook scores and liquidity spikes despite overall weakness, but notes cooling liquidity and sector constraints.
- EFIH.CA and ETEL.CA show BULLISH_WATCH outlook (>80) and TRADEABLE liquidity, yet both sit near resistance (≈6% and ≈10% away) with cooling liquidity spikes, limiting near‑term upside.
- ORWE.CA and UEGC.CA display ACCUMULATION_SPIKE liquidity and modest support distances (≈6% and ≈23%), but sector rankings are weak and confidence remains LOW.
- Sector breadth is 0%; leading sectors (Telecom, Fintech, Transport) have mixed MA‑above percentages, reinforcing the defensive stance and adding uncertainty to any short‑term bounce.
- Overall EGX30/EGX70 bearish regime shifts risk mode to DEFENSIVE_NO_NEW_BUY, so even tickets with positive outlook are treated as watch‑list only for the next 1‑3 days.

## Top Liquidity Spikes
- SEIG.CA: spike=3.28 liquidity=5632000.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- INFI.CA: spike=2.9 liquidity=46072424.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- UEGC.CA: spike=2.84 liquidity=119798944.0 outlook=CONSTRUCTIVE score=56 buy_ready=False
- EGAL.CA: spike=2.54 liquidity=159825312.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ORWE.CA: spike=2.26 liquidity=93554616.0 outlook=BULLISH_WATCH score=82 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=5.06 5d=-1.22% 20d=4.32% aboveMA50=50.0%
- #2 Fintech & Payments: score=2.86 5d=-2.47% 20d=2.06% aboveMA50=50.0%
- #3 Transportation & Logistics: score=2.43 5d=-0.55% 20d=4.02% aboveMA50=50.0%
- #4 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #5 Energy & Petrochemicals: score=-0.87 5d=-5.72% 20d=0.22% aboveMA50=33.33%
- #6 Automotive & Distribution: score=-1.15 5d=-2.48% 20d=-4.41% aboveMA50=0.0%
- #7 Food, Beverages & Tobacco: score=-1.19 5d=-1.1% 20d=-9.98% aboveMA50=14.29%
- #8 Non-bank Financial Services: score=-1.24 5d=-2.94% 20d=-5.82% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ETEL.CA: BULLISH_WATCH score=91.06 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- EFIH.CA: BULLISH_WATCH score=82.86 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ORWE.CA: BULLISH_WATCH score=82 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=sector is not leading
- SUGR.CA: BULLISH_WATCH score=76 liquidity=TRADEABLE sector=NEUTRAL risk=liquidity is cooling
- AMIA.CA: BULLISH_WATCH score=71 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- ALCN.CA: BULLISH_WATCH score=70.43 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20
- ACAMD.CA: CONSTRUCTIVE score=59 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; momentum is extended; sector is not leading
- AMOC.CA: CONSTRUCTIVE score=58 liquidity=TRADEABLE sector=NEUTRAL risk=liquidity is cooling; below MA20
- SDTI.CA: CONSTRUCTIVE score=57 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; momentum is extended; sector is not leading
- UEGC.CA: CONSTRUCTIVE score=56 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=below MA50; far above support; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=7.88 buy_ready=False sector_rank=19 price=234.96 support=225.0 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=25.33 liquidity=22023586.0 spike=1.24
- ABUK.CA: score=15.71 buy_ready=False sector_rank=15 price=85.5 support=83.0 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=44.33 liquidity=42916664.0 spike=0.46
- ACAMD.CA: score=19.4 buy_ready=False sector_rank=19 price=2.11 support=1.87 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=67.86 liquidity=32952428.0 spike=0.71
- ACGC.CA: score=5.59 buy_ready=False sector_rank=13 price=13.2 support=12.81 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=40.2 liquidity=2690958.5 spike=0.21
- ADCI.CA: score=-2.18 buy_ready=False sector_rank=19 price=258.96 support=250.06 resistance=288.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=33.73 liquidity=421393.22 spike=0.21
- ADIB.CA: score=8.28 buy_ready=False sector_rank=11 price=45.75 support=43.5 resistance=54.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=34.23 liquidity=22101970.0 spike=0.28
- ADPC.CA: score=-0.16 buy_ready=False sector_rank=19 price=3.15 support=3.01 resistance=4.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=27.83 liquidity=3439462.25 spike=0.23
- AFDI.CA: score=3.97 buy_ready=False sector_rank=19 price=49.46 support=46.12 resistance=56.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=42.22 liquidity=1574640.13 spike=0.26
- AFMC.CA: score=4.28 buy_ready=False sector_rank=19 price=130.11 support=122.0 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=36.2 liquidity=1877087.13 spike=0.09
- AJWA.CA: score=16.29 buy_ready=False sector_rank=19 price=223.99 support=176.0 resistance=227.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=89.12 liquidity=9893098.0 spike=0.33
- ALCN.CA: score=14.57 buy_ready=False sector_rank=3 price=32.81 support=30.7 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=51.2 liquidity=5593625.5 spike=0.16
- ALUM.CA: score=-1.94 buy_ready=False sector_rank=19 price=20.83 support=20.52 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=29.94 liquidity=1664084.88 spike=0.36
- AMER.CA: score=14.51 buy_ready=False sector_rank=17 price=4.4 support=4.05 resistance=5.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=38.46 liquidity=18714102.0 spike=0.38
- AMES.CA: score=8.4 buy_ready=False sector_rank=19 price=37.34 support=38.02 resistance=54.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=31.32 liquidity=24369270.0 spike=0.3
- AMIA.CA: score=10.96 buy_ready=False sector_rank=19 price=18.72 support=17.2 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=52.51 liquidity=3557270.25 spike=0.19
- AMOC.CA: score=16.65 buy_ready=False sector_rank=5 price=13.36 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=51.0 liquidity=31721308.0 spike=0.25
- APSW.CA: score=1.72 buy_ready=False sector_rank=19 price=8.11 support=7.81 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=44.57 liquidity=319057.28 spike=0.49
- ARAB.CA: score=17.53 buy_ready=False sector_rank=17 price=0.26 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=72.55 liquidity=100389608.0 spike=1.01
- ARCC.CA: score=13.16 buy_ready=False sector_rank=12 price=66.14 support=60.01 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=49.86 liquidity=18220084.0 spike=0.59
- AREH.CA: score=1.07 buy_ready=False sector_rank=19 price=1.16 support=1.11 resistance=1.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=32.69 liquidity=4671736.0 spike=0.56
- ASCM.CA: score=0.4 buy_ready=False sector_rank=19 price=49.08 support=48.0 resistance=61.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=30.97 liquidity=3995756.0 spike=0.47
- ASPI.CA: score=11.4 buy_ready=False sector_rank=19 price=0.33 support=0.31 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=35.23 liquidity=15597678.0 spike=0.51
- ATLC.CA: score=-1.0 buy_ready=False sector_rank=8 price=5.19 support=5.05 resistance=5.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5496782.5 spike=0.57
- ATQA.CA: score=12.71 buy_ready=False sector_rank=15 price=11.47 support=10.61 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=39.34 liquidity=22443002.0 spike=0.31
- AXPH.CA: score=-0.33 buy_ready=False sector_rank=19 price=1353.37 support=1300.0 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=23.63 liquidity=2274697.5 spike=0.34
- BINV.CA: score=7.18 buy_ready=False sector_rank=14 price=58.02 support=52.11 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=57.37 liquidity=1416379.13 spike=0.07
- BIOC.CA: score=14.4 buy_ready=False sector_rank=19 price=288.7 support=225.21 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=59.79 liquidity=26567988.0 spike=0.26
- BTFH.CA: score=12.5 buy_ready=False sector_rank=8 price=2.69 support=2.55 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=44.78 liquidity=50291284.0 spike=0.48
- CAED.CA: score=5.98 buy_ready=False sector_rank=19 price=100.32 support=95.0 resistance=136.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=38.94 liquidity=3576004.5 spike=0.44
- CANA.CA: score=8.28 buy_ready=False sector_rank=11 price=42.82 support=41.7 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=32.48 liquidity=10654320.0 spike=0.43
- CCAP.CA: score=7.76 buy_ready=False sector_rank=14 price=6.06 support=6.04 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=22.75 liquidity=540116992.0 spike=0.92
- CCRS.CA: score=0.45 buy_ready=False sector_rank=19 price=1.96 support=1.87 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=18.42 liquidity=4052651.25 spike=0.35
- CEFM.CA: score=2.83 buy_ready=False sector_rank=19 price=125.47 support=113.0 resistance=152.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=38.49 liquidity=429673.97 spike=0.16
- CERA.CA: score=12.4 buy_ready=False sector_rank=19 price=1.25 support=1.18 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=48.05 liquidity=40391744.0 spike=0.33
- CFGH.CA: score=-3.51 buy_ready=False sector_rank=19 price=0.11 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=9.09 liquidity=6303.18 spike=1.04
- CICH.CA: score=-2.0 buy_ready=False sector_rank=8 price=10.6 support=10.6 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=491897.59 spike=0.14
- CIEB.CA: score=4.84 buy_ready=False sector_rank=11 price=22.88 support=22.56 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=36.01 liquidity=2564514.0 spike=0.26
- CIRA.CA: score=6.1 buy_ready=False sector_rank=10 price=36.62 support=35.51 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=42.63 liquidity=2758536.25 spike=0.12
- CLHO.CA: score=6.41 buy_ready=False sector_rank=18 price=13.72 support=13.51 resistance=16.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=30.5 liquidity=12612077.0 spike=0.29
- CNFN.CA: score=7.51 buy_ready=False sector_rank=8 price=4.08 support=3.8 resistance=4.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=45.57 liquidity=3010781.75 spike=0.33
- COMI.CA: score=12.28 buy_ready=False sector_rank=11 price=123.59 support=120.0 resistance=134.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=39.38 liquidity=102121320.0 spike=0.19
- COPR.CA: score=5.84 buy_ready=False sector_rank=19 price=0.46 support=0.44 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=45.65 liquidity=3440066.0 spike=0.16
- COSG.CA: score=6.52 buy_ready=False sector_rank=19 price=1.46 support=1.34 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=35.0 liquidity=5121881.0 spike=0.34
- CPCI.CA: score=8.39 buy_ready=False sector_rank=19 price=596.01 support=532.24 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=77.64 liquidity=1988110.25 spike=0.48
- CSAG.CA: score=8.22 buy_ready=False sector_rank=3 price=35.56 support=34.06 resistance=39.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=2250666.0 spike=0.31
- DAPH.CA: score=12.4 buy_ready=False sector_rank=19 price=91.63 support=89.1 resistance=129.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=39.16 liquidity=10090010.0 spike=0.24
- DEIN.CA: score=5.4 buy_ready=False sector_rank=19 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 09:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37.26 spike=0.01
- DOMT.CA: score=-2.02 buy_ready=False sector_rank=7 price=23.28 support=22.85 resistance=27.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=31.95 liquidity=455726.19 spike=0.1
- DSCW.CA: score=3.19 buy_ready=False sector_rank=19 price=1.59 support=1.55 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=6791001.5 spike=0.39
- DTPP.CA: score=12.4 buy_ready=False sector_rank=19 price=257.18 support=225.0 resistance=360.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=36.01 liquidity=18579178.0 spike=0.3
- EALR.CA: score=-1.15 buy_ready=False sector_rank=19 price=307.01 support=290.17 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=30.09 liquidity=2447432.75 spike=0.32
- EASB.CA: score=4.14 buy_ready=False sector_rank=19 price=6.69 support=6.04 resistance=8.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=39.67 liquidity=1742492.25 spike=0.34
- EAST.CA: score=12.44 buy_ready=False sector_rank=7 price=28.95 support=27.01 resistance=33.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=35.52 liquidity=7918592.5 spike=0.18
- EBSC.CA: score=-2.57 buy_ready=False sector_rank=19 price=1.59 support=1.5 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:13 AM market time freshness=DELAYED_CURRENT RSI=31.65 liquidity=1028771.44 spike=0.44
- ECAP.CA: score=-2.09 buy_ready=False sector_rank=19 price=28.01 support=27.5 resistance=32.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=26.3 liquidity=1506684.0 spike=0.36
- EDFM.CA: score=2.89 buy_ready=False sector_rank=19 price=388.92 support=335.2 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=48.78 liquidity=485593.22 spike=0.41
- EEII.CA: score=-1.32 buy_ready=False sector_rank=19 price=1.88 support=1.83 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=20.31 liquidity=2276834.5 spike=0.25
- EFIC.CA: score=4.63 buy_ready=False sector_rank=15 price=150.42 support=147.0 resistance=199.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=30.02 liquidity=7919556.0 spike=0.24
- EFID.CA: score=14.52 buy_ready=False sector_rank=7 price=18.51 support=18.07 resistance=31.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=40.89 liquidity=16127381.0 spike=0.34
- EFIH.CA: score=24.14 buy_ready=False sector_rank=2 price=23.9 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=59.32 liquidity=23254336.0 spike=0.35
- EGAL.CA: score=5.79 buy_ready=False sector_rank=15 price=288.95 support=284.95 resistance=305.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=159825312.0 spike=2.54
- EGAS.CA: score=6.9 buy_ready=False sector_rank=5 price=51.37 support=48.08 resistance=60.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=42.53 liquidity=3244364.75 spike=0.29
- EGBE.CA: score=3.33 buy_ready=False sector_rank=11 price=0.5 support=0.5 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:28 AM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=45246.61 spike=0.33
- EGCH.CA: score=6.71 buy_ready=False sector_rank=15 price=11.74 support=11.86 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=16.09 liquidity=20119948.0 spike=0.25
- EGSA.CA: score=5.09 buy_ready=False sector_rank=1 price=8.81 support=8.8 resistance=9.09 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=25.64 liquidity=7488.5 spike=1.53
- EGTS.CA: score=6.26 buy_ready=False sector_rank=17 price=13.65 support=13.56 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=19.18 liquidity=8755026.0 spike=0.25
- EHDR.CA: score=0.39 buy_ready=False sector_rank=19 price=2.22 support=2.1 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=32.43 liquidity=3990214.5 spike=0.38
- ELEC.CA: score=6.64 buy_ready=False sector_rank=16 price=1.68 support=1.65 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=30.77 liquidity=17123802.0 spike=0.34
- ELKA.CA: score=14.62 buy_ready=False sector_rank=19 price=1.54 support=1.38 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=14321986.0 spike=1.11
- ELNA.CA: score=5.04 buy_ready=False sector_rank=19 price=35.22 support=33.46 resistance=36.4 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=281266.93 spike=1.68
- ELSH.CA: score=7.71 buy_ready=False sector_rank=19 price=10.84 support=10.76 resistance=13.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=37.11 liquidity=5314913.0 spike=0.25
- ELWA.CA: score=6.51 buy_ready=False sector_rank=19 price=1.65 support=1.43 resistance=1.74 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=54.05 liquidity=110069.85 spike=0.24
- EMFD.CA: score=11.98 buy_ready=False sector_rank=17 price=11.89 support=11.7 resistance=14.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=35.01 liquidity=9473661.0 spike=0.15
- ENGC.CA: score=-1.24 buy_ready=False sector_rank=19 price=33.33 support=32.37 resistance=45.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=28.04 liquidity=2355128.0 spike=0.13
- EOSB.CA: score=7.4 buy_ready=False sector_rank=19 price=1.57 support=1.64 resistance=1.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=15 October 12:37 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=401.8 spike=0.01
- EPCO.CA: score=-2.7 buy_ready=False sector_rank=19 price=8.65 support=8.0 resistance=11.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=26.76 liquidity=899189.69 spike=0.18
- EPPK.CA: score=-7.18 buy_ready=False sector_rank=19 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=24.02 buy_ready=False sector_rank=1 price=141.63 support=128.52 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=61.77 liquidity=191787136.0 spike=0.72
- ETRS.CA: score=4.17 buy_ready=False sector_rank=19 price=10.33 support=9.82 resistance=11.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=52.1 liquidity=1769566.13 spike=0.17
- EXPA.CA: score=7.28 buy_ready=False sector_rank=11 price=14.27 support=14.0 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=10.28 liquidity=23878294.0 spike=0.63
- FAIT.CA: score=4.19 buy_ready=False sector_rank=11 price=43.68 support=38.48 resistance=47.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=37.34 liquidity=911204.31 spike=0.3
- FAITA.CA: score=10.3 buy_ready=False sector_rank=11 price=1.0 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=58.75 liquidity=21944.14 spike=0.54
- FERC.CA: score=-2.49 buy_ready=False sector_rank=15 price=68.54 support=66.72 resistance=82.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=26.04 liquidity=793144.75 spike=0.15
- FWRY.CA: score=18.14 buy_ready=False sector_rank=2 price=18.39 support=17.5 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=50.59 liquidity=26338844.0 spike=0.23
- GBCO.CA: score=3.54 buy_ready=False sector_rank=6 price=29.2 support=29.11 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=57336992.0 spike=0.54
- GDWA.CA: score=1.43 buy_ready=False sector_rank=19 price=0.61 support=0.6 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=30.29 liquidity=5032010.5 spike=0.25
- GGCC.CA: score=3.94 buy_ready=False sector_rank=19 price=0.66 support=0.66 resistance=0.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26887192.0 spike=1.77
- GIHD.CA: score=0.49 buy_ready=False sector_rank=19 price=52.54 support=53.02 resistance=78.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=15.03 liquidity=3090927.75 spike=0.16
- GMCI.CA: score=3.77 buy_ready=False sector_rank=19 price=1.54 support=1.49 resistance=1.78 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=36.21 liquidity=371782.17 spike=0.95
- GRCA.CA: score=0.22 buy_ready=False sector_rank=19 price=31.85 support=30.51 resistance=45.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=31.16 liquidity=1823799.0 spike=0.21
- GSSC.CA: score=3.53 buy_ready=False sector_rank=19 price=265.97 support=246.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=40.19 liquidity=1126650.0 spike=0.37
- GTWL.CA: score=7.4 buy_ready=False sector_rank=19 price=124.85 support=116.16 resistance=241.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=20.94 liquidity=41486936.0 spike=0.26
- HDBK.CA: score=4.56 buy_ready=False sector_rank=11 price=99.53 support=98.01 resistance=121.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=33.86 liquidity=7284584.0 spike=0.3
- HELI.CA: score=12.51 buy_ready=False sector_rank=17 price=7.16 support=6.92 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=30075770.0 spike=0.31
- HRHO.CA: score=16.5 buy_ready=False sector_rank=8 price=25.2 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=62.0 liquidity=33696876.0 spike=0.25
- ICID.CA: score=6.53 buy_ready=False sector_rank=19 price=17.51 support=16.52 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=53.35 liquidity=1125035.0 spike=0.14
- IDRE.CA: score=2.56 buy_ready=False sector_rank=19 price=42.53 support=40.05 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=35.33 liquidity=1157350.38 spike=0.09
- IFAP.CA: score=-0.93 buy_ready=False sector_rank=20 price=18.29 support=17.17 resistance=21.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=27.7 liquidity=2667773.0 spike=0.38
- INFI.CA: score=6.2 buy_ready=False sector_rank=19 price=135.91 support=124.25 resistance=137.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46072424.0 spike=2.9
- IRON.CA: score=7.28 buy_ready=False sector_rank=15 price=26.09 support=25.01 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=43.3 liquidity=5564253.5 spike=0.53
- ISMA.CA: score=-1.46 buy_ready=False sector_rank=19 price=21.23 support=18.91 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=31.44 liquidity=2142818.5 spike=0.29
- ISMQ.CA: score=0.95 buy_ready=False sector_rank=15 price=7.52 support=7.14 resistance=9.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=32.5 liquidity=4237813.0 spike=0.22
- ISPH.CA: score=10.73 buy_ready=False sector_rank=18 price=11.02 support=10.03 resistance=12.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=43.8 liquidity=9320885.0 spike=0.17
- JUFO.CA: score=12.52 buy_ready=False sector_rank=7 price=23.53 support=23.5 resistance=27.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=35.62 liquidity=14554442.0 spike=0.85
- KABO.CA: score=3.95 buy_ready=False sector_rank=13 price=7.41 support=7.3 resistance=9.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=34.27 liquidity=6049392.5 spike=0.26
- KWIN.CA: score=-2.44 buy_ready=False sector_rank=19 price=64.87 support=60.0 resistance=93.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:26 AM market time freshness=DELAYED_CURRENT RSI=19.54 liquidity=1161657.63 spike=0.13
- KZPC.CA: score=7.66 buy_ready=False sector_rank=19 price=13.15 support=12.15 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=44.59 liquidity=2255295.75 spike=0.25
- LCSW.CA: score=9.77 buy_ready=False sector_rank=12 price=33.27 support=28.86 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=61.67 liquidity=2610363.75 spike=0.13
- LUTS.CA: score=12.4 buy_ready=False sector_rank=19 price=0.71 support=0.65 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=37.88 liquidity=22293868.0 spike=0.4
- MAAL.CA: score=7.4 buy_ready=False sector_rank=19 price=8.3 support=8.45 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=29.39 liquidity=12374044.0 spike=0.49
- MASR.CA: score=12.4 buy_ready=False sector_rank=19 price=7.21 support=6.82 resistance=7.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=50.19 liquidity=15707002.0 spike=0.28
- MBSC.CA: score=17.16 buy_ready=False sector_rank=12 price=347.05 support=288.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=49931228.0 spike=0.58
- MCQE.CA: score=12.16 buy_ready=False sector_rank=12 price=173.0 support=170.0 resistance=224.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=36.32 liquidity=45374732.0 spike=0.82
- MCRO.CA: score=7.4 buy_ready=False sector_rank=19 price=1.39 support=1.25 resistance=1.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=32.08 liquidity=39373552.0 spike=0.72
- MENA.CA: score=5.16 buy_ready=False sector_rank=17 price=5.88 support=5.57 resistance=7.05 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=35.53 liquidity=2148034.6 spike=1.25
- MEPA.CA: score=4.07 buy_ready=False sector_rank=19 price=1.59 support=1.53 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=40.28 liquidity=2669355.75 spike=0.28
- MFPC.CA: score=15.71 buy_ready=False sector_rank=15 price=43.84 support=42.0 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=37.35 liquidity=27992600.0 spike=0.33
- MFSC.CA: score=-3.27 buy_ready=False sector_rank=19 price=38.27 support=36.25 resistance=49.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=18.42 liquidity=329002.0 spike=0.14
- MHOT.CA: score=3.92 buy_ready=False sector_rank=9 price=15.82 support=15.08 resistance=19.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=30.38 liquidity=6533511.5 spike=0.37
- MICH.CA: score=5.96 buy_ready=False sector_rank=19 price=41.07 support=38.91 resistance=47.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=39.22 liquidity=3559204.25 spike=0.41
- MILS.CA: score=-0.46 buy_ready=False sector_rank=19 price=153.92 support=147.06 resistance=207.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=28.06 liquidity=2142855.5 spike=0.27
- MIPH.CA: score=4.49 buy_ready=False sector_rank=18 price=700.0 support=686.2 resistance=798.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17199902.0 spike=2.04
- MOED.CA: score=2.66 buy_ready=False sector_rank=19 price=0.59 support=0.57 resistance=0.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=32.55 liquidity=6255107.0 spike=0.38
- MOIL.CA: score=-1.31 buy_ready=False sector_rank=5 price=0.67 support=0.63 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=31.08 liquidity=40713.14 spike=0.14
- MOIN.CA: score=-2.35 buy_ready=False sector_rank=19 price=30.32 support=29.7 resistance=31.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5250533.0 spike=0.5
- MOSC.CA: score=3.32 buy_ready=False sector_rank=19 price=259.91 support=231.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=40.15 liquidity=920580.69 spike=0.24
- MPCI.CA: score=7.4 buy_ready=False sector_rank=19 price=314.25 support=294.2 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=28.71 liquidity=71774384.0 spike=0.71
- MPCO.CA: score=7.4 buy_ready=False sector_rank=20 price=2.0 support=2.0 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=20.24 liquidity=31734390.0 spike=0.25
- MPRC.CA: score=12.56 buy_ready=False sector_rank=19 price=36.09 support=34.53 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=35.94 liquidity=16972172.0 spike=1.08
- MTIE.CA: score=10.37 buy_ready=False sector_rank=6 price=7.47 support=7.27 resistance=8.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=37.85 liquidity=7831862.5 spike=0.43
- NAHO.CA: score=2.42 buy_ready=False sector_rank=19 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=22601.64 spike=0.78
- NCCW.CA: score=4.13 buy_ready=False sector_rank=19 price=5.7 support=5.3 resistance=8.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=29.69 liquidity=7727668.0 spike=0.19
- NEDA.CA: score=-2.54 buy_ready=False sector_rank=19 price=2.6 support=2.47 resistance=2.8 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=32.14 liquidity=59974.2 spike=0.09
- NHPS.CA: score=-0.55 buy_ready=False sector_rank=19 price=63.99 support=63.02 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=29.36 liquidity=3045079.5 spike=0.21
- NINH.CA: score=4.44 buy_ready=False sector_rank=19 price=16.0 support=16.02 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=21.16 liquidity=8043182.5 spike=0.56
- NIPH.CA: score=7.41 buy_ready=False sector_rank=18 price=269.4 support=241.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=29.65 liquidity=34258228.0 spike=0.28
- OBRI.CA: score=7.88 buy_ready=False sector_rank=19 price=25.98 support=22.8 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=45.97 liquidity=4482047.5 spike=0.31
- OCDI.CA: score=12.51 buy_ready=False sector_rank=17 price=25.62 support=24.2 resistance=30.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=38.69 liquidity=22684724.0 spike=0.53
- OCPH.CA: score=-2.83 buy_ready=False sector_rank=19 price=197.83 support=190.0 resistance=247.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=34.95 liquidity=771987.19 spike=0.23
- ODIN.CA: score=-1.89 buy_ready=False sector_rank=19 price=2.22 support=2.11 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=30.39 liquidity=1710706.0 spike=0.2
- OFH.CA: score=2.77 buy_ready=False sector_rank=19 price=0.79 support=0.76 resistance=1.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=29.55 liquidity=5369520.0 spike=0.06
- OIH.CA: score=7.76 buy_ready=False sector_rank=14 price=1.77 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=12928110.0 spike=0.15
- OLFI.CA: score=-0.76 buy_ready=False sector_rank=7 price=20.54 support=19.8 resistance=23.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=24.92 liquidity=1716585.13 spike=0.1
- ORAS.CA: score=4.6 buy_ready=False sector_rank=4 price=871.98 support=871.5 resistance=893.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=62477400.0 spike=1.0
- ORHD.CA: score=6.51 buy_ready=False sector_rank=17 price=10.48 support=10.01 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=2.79 liquidity=131938008.0 spike=0.88
- ORWE.CA: score=20.42 buy_ready=False sector_rank=13 price=27.61 support=26.01 resistance=28.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=58.11 liquidity=93554616.0 spike=2.26
- PHAR.CA: score=12.41 buy_ready=False sector_rank=18 price=105.38 support=102.0 resistance=122.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=45.41 liquidity=15716973.0 spike=0.24
- PHDC.CA: score=14.51 buy_ready=False sector_rank=17 price=12.59 support=12.35 resistance=13.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=35.62 liquidity=18879932.0 spike=0.2
- PHTV.CA: score=2.87 buy_ready=False sector_rank=19 price=338.3 support=315.0 resistance=377.96 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=41.91 liquidity=474634.88 spike=0.55
- POUL.CA: score=5.65 buy_ready=False sector_rank=7 price=9.92 support=9.12 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=3.27 liquidity=8121996.0 spike=0.26
- PRCL.CA: score=-0.75 buy_ready=False sector_rank=12 price=21.52 support=21.0 resistance=32.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=27.19 liquidity=2081112.88 spike=0.19
- PRDC.CA: score=12.51 buy_ready=False sector_rank=17 price=6.2 support=6.07 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=40.44 liquidity=10153357.0 spike=0.28
- PRMH.CA: score=-2.75 buy_ready=False sector_rank=19 price=2.0 support=1.8 resistance=2.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=845293.06 spike=0.21
- RACC.CA: score=3.49 buy_ready=False sector_rank=19 price=8.85 support=8.51 resistance=10.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=42.67 liquidity=2087136.38 spike=0.32
- RAKT.CA: score=1.71 buy_ready=False sector_rank=19 price=22.06 support=20.26 resistance=25.08 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=49.81 liquidity=308795.87 spike=0.87
- RAYA.CA: score=3.93 buy_ready=False sector_rank=21 price=5.91 support=5.7 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=31.66 liquidity=7532934.5 spike=0.21
- RMDA.CA: score=7.41 buy_ready=False sector_rank=18 price=5.05 support=4.83 resistance=6.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=27.97 liquidity=15681504.0 spike=0.6
- ROTO.CA: score=3.41 buy_ready=False sector_rank=19 price=36.26 support=35.56 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=42.3 liquidity=2005179.88 spike=0.24
- RREI.CA: score=3.37 buy_ready=False sector_rank=19 price=3.45 support=3.29 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=36.54 liquidity=1973683.13 spike=0.21
- RTVC.CA: score=-2.47 buy_ready=False sector_rank=19 price=3.36 support=3.31 resistance=4.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=34.37 liquidity=1128977.13 spike=0.41
- RUBX.CA: score=17.4 buy_ready=False sector_rank=19 price=16.99 support=12.9 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=44.48 liquidity=43229684.0 spike=0.42
- SAUD.CA: score=13.28 buy_ready=False sector_rank=11 price=21.89 support=20.2 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=39.87 liquidity=16066852.0 spike=0.76
- SCEM.CA: score=17.16 buy_ready=False sector_rank=12 price=88.7 support=74.55 resistance=95.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=57.0 liquidity=40363572.0 spike=0.63
- SCFM.CA: score=-3.26 buy_ready=False sector_rank=19 price=232.59 support=220.35 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=33.98 liquidity=340260.0 spike=0.19
- SCTS.CA: score=-1.34 buy_ready=False sector_rank=10 price=483.03 support=463.13 resistance=615.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=24.24 liquidity=320127.72 spike=0.32
- SDTI.CA: score=11.92 buy_ready=False sector_rank=19 price=86.01 support=73.3 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=63.73 liquidity=4522467.0 spike=0.13
- SEIG.CA: score=2.59 buy_ready=False sector_rank=19 price=215.74 support=193.0 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5632000.0 spike=3.28
- SIPC.CA: score=19.4 buy_ready=False sector_rank=19 price=5.56 support=4.22 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=54.87 liquidity=24742588.0 spike=0.47
- SKPC.CA: score=6.71 buy_ready=False sector_rank=15 price=15.12 support=14.98 resistance=18.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=24.66 liquidity=11901841.0 spike=0.15
- SMFR.CA: score=2.6 buy_ready=False sector_rank=19 price=203.62 support=181.6 resistance=255.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=38.5 liquidity=1198928.25 spike=0.33
- SNFC.CA: score=3.92 buy_ready=False sector_rank=19 price=11.06 support=10.81 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=41.25 liquidity=1520033.38 spike=0.14
- SPIN.CA: score=-1.18 buy_ready=False sector_rank=13 price=14.43 support=14.8 resistance=18.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=28.97 liquidity=1913836.25 spike=0.36
- SPMD.CA: score=5.99 buy_ready=False sector_rank=19 price=0.36 support=0.34 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=31.82 liquidity=9585650.0 spike=0.45
- SUGR.CA: score=17.67 buy_ready=False sector_rank=7 price=56.25 support=50.5 resistance=61.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=53.51 liquidity=7141478.5 spike=0.69
- SVCE.CA: score=7.4 buy_ready=False sector_rank=19 price=9.33 support=8.81 resistance=12.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=31.55 liquidity=36946400.0 spike=0.45
- SWDY.CA: score=12.64 buy_ready=False sector_rank=16 price=109.88 support=102.31 resistance=128.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=43.46 liquidity=27134356.0 spike=0.45
- TALM.CA: score=14.73 buy_ready=False sector_rank=10 price=20.77 support=18.71 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=55.34 liquidity=8393052.0 spike=0.22
- TMGH.CA: score=6.51 buy_ready=False sector_rank=17 price=83.36 support=81.22 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=21.82 liquidity=46775568.0 spike=0.21
- TRTO.CA: score=9.59 buy_ready=False sector_rank=19 price=0.07 support=0.05 resistance=0.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=10701.08 spike=1.09
- UEFM.CA: score=4.25 buy_ready=False sector_rank=19 price=479.55 support=407.57 resistance=550.0 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=54.34 liquidity=850242.13 spike=0.27
- UEGC.CA: score=20.08 buy_ready=False sector_rank=19 price=1.65 support=1.34 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=56.79 liquidity=119798944.0 spike=2.84
- UNIP.CA: score=4.05 buy_ready=False sector_rank=19 price=0.32 support=0.31 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=38.89 liquidity=2647049.75 spike=0.28
- UNIT.CA: score=2.9 buy_ready=False sector_rank=17 price=16.82 support=16.15 resistance=20.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=41.61 liquidity=394350.09 spike=0.07
- WCDF.CA: score=-1.39 buy_ready=False sector_rank=19 price=522.09 support=515.0 resistance=719.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=21.81 liquidity=1213834.75 spike=0.38
- WKOL.CA: score=4.15 buy_ready=False sector_rank=19 price=275.76 support=266.18 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=27.55 liquidity=7750777.5 spike=0.76
- ZEOT.CA: score=-2.87 buy_ready=False sector_rank=19 price=10.71 support=10.6 resistance=11.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4729206.0 spike=0.59
- ZMID.CA: score=7.51 buy_ready=False sector_rank=17 price=7.11 support=6.83 resistance=9.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=24.07 liquidity=98377656.0 spike=0.98

## Backtesting Lite
- EFIH.CA: 180d return=22.76%, max drawdown=-22.68%, MA20>MA50 days last20=5, as_of=2026-10-14T21:00:00+00:00
- ETEL.CA: 180d return=117.39%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-10-14T21:00:00+00:00
- ORWE.CA: 180d return=34.87%, max drawdown=-9.36%, MA20>MA50 days last20=20, as_of=2026-10-14T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- ORWE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=655 sources=3 expected=Oriental Weavers summary=Oriental Weavers to disburse EGP 1.5/shr dividends for 2025; Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025; Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25
  - Oriental Weavers to disburse EGP 1.5/shr dividends for 2025: https://english.mubasher.info/news/4590236/Oriental-Weavers-to-disburse-EGP-1-5-shr-dividends-for-2025/
  - Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025: https://english.mubasher.info/news/4562972/Oriental-Weavers-consolidated-profits-cross-EGP-2-2bn-in-2025/
  - Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25: https://english.mubasher.info/news/4487417/Oriental-Weavers-generates-EGP-12-5bn-consolidated-sales-in-H1-25/
- UEGC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=655 sources=3 expected=El-Saeed Company for Contracting and Real Estate Investment "SCCD" (S.A.E.) summary=ElSaeed Contracting stock eyes break above EGP 1.44 amid uptrend; ElSaeed Contracting posts higher consolidated profits at EGP 93m in 2025; ElSaeed Contracting stock signals upside move towards EGP 1.50
  - ElSaeed Contracting stock eyes break above EGP 1.44 amid uptrend: https://english.mubasher.info/news/4595500/ElSaeed-Contracting-stock-eyes-break-above-EGP-1-44-amid-uptrend/
  - ElSaeed Contracting posts higher consolidated profits at EGP 93m in 2025: https://english.mubasher.info/news/4589666/ElSaeed-Contracting-posts-higher-consolidated-profits-at-EGP-93m-in-2025/
  - ElSaeed Contracting stock signals upside move towards EGP 1.50: https://english.mubasher.info/news/4564890/ElSaeed-Contracting-stock-signals-upside-move-towards-EGP-1-50/
- ACAMD.CA: status=OLD_ACCEPTED latest=2020-01-01 age_days=2482 sources=3 expected=Arab Co.,for asset management and development summary=Arab Company for Asset Management shifts to EGP 7m net profits in 9M-25; Arab Co. for Asset Management approves offer to sell land in El-Minya; Arab Co. Asset Management swings to loss in 2020
  - Arab Company for Asset Management shifts to EGP 7m net profits in 9M-25: https://english.mubasher.info/news/4543171/Arab-Company-for-Asset-Management-shifts-to-EGP-7m-net-profits-in-9M-25/
  - Arab Co. for Asset Management approves offer to sell land in El-Minya: https://english.mubasher.info/news/3777445/Arab-Co-for-Asset-Management-approves-offer-to-sell-land-in-El-Minya/
  - Arab Co. Asset Management swings to loss in 2020: https://english.mubasher.info/news/3767136/Arab-Co-Asset-Management-swings-to-loss-in-2020/
- SIPC.CA: status=OLD_ACCEPTED latest=2020-01-01 age_days=2482 sources=3 expected=Sabaa International Company for Pharmaceutical and Chemical Industry summary=Sabaa Pharmaceutical&#39;s shareholders approve capital raise via bonus issue; FRA approves Sabaa Pharmaceutical&#39;s capital raise; Sabaa Pharmaceutical&#39;s profit leaps 76% in 2020 initial results
  - Sabaa Pharmaceutical&#39;s shareholders approve capital raise via bonus issue: https://english.mubasher.info/news/3809286/Sabaa-Pharmaceutical-s-shareholders-approve-capital-raise-via-bonus-issue/
  - FRA approves Sabaa Pharmaceutical&#39;s capital raise: https://english.mubasher.info/news/3789753/FRA-approves-Sabaa-Pharmaceutical-s-capital-raise/
  - Sabaa Pharmaceutical&#39;s profit leaps 76% in 2020 initial results: https://english.mubasher.info/news/3779465/Sabaa-Pharmaceutical-s-profit-leaps-76-in-2020-initial-results/
- FWRY.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Fawry For Banking Technology and Electronic Payments summary=Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- SUGR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=655 sources=3 expected=Delta Sugar summary=Delta Sugar’s net profits fall 74% in Q1-26; Delta Sugar stock tests key resistance near EGP 50 amid downtrend; Delta Sugar turns to EGP 346m net losses in 2025
  - Delta Sugar’s net profits fall 74% in Q1-26: https://english.mubasher.info/news/4604921/Delta-Sugar-s-net-profits-fall-74-in-Q1-26/
  - Delta Sugar stock tests key resistance near EGP 50 amid downtrend: https://english.mubasher.info/news/4584932/Delta-Sugar-stock-tests-key-resistance-near-EGP-50-amid-downtrend/
  - Delta Sugar turns to EGP 346m net losses in 2025: https://english.mubasher.info/news/4557875/Delta-Sugar-turns-to-EGP-346m-net-losses-in-2025/

## Warnings
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for ORWE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for UEGC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ACAMD.CA matches the company but appears old; latest detected date is 2020-01-01.
- Evidence for SIPC.CA matches the company but appears old; latest detected date is 2020-01-01.
- Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- Evidence for SUGR.CA matches the company but appears old; latest detected date is 2025-01-01.
