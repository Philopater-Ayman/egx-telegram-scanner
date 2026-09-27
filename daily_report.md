# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-09-27T10:46:02.717118+00:00
Generated Cairo: 2026-09-27 13:46
Run timing: target 08:45 Cairo | generated Cairo 2026-09-27 13:46 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-27 13:43

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 171/187
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, September 27
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 10.53% / above MA50 31.58%
- EGX70 regime: BEARISH / above MA20 17.14% / above MA50 25.71%
- Sector breadth: 9.52%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=414836224.0 spike=0.48 score=19.4
- TMGH.CA: liquidity=207460944.0 spike=0.71 score=6.91
- ZMID.CA: liquidity=162519248.0 spike=0.84 score=7.91
- POUL.CA: liquidity=151878896.0 spike=5.89 score=8.52
- SDTI.CA: liquidity=141663648.0 spike=5.74 score=8.15

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with weak breadth (sector breadth ~9.5%), putting the market in a DEFENSIVE_NO_NEW_BUY risk mode; the scanner therefore holds and highlights tickets that show relative strength in liquidity or sector leadership despite the overall downturn.
- MHOT.CA leads the rank due to a large liquidity spike (9.9×) and top Tourism & Leisure sector score, with a BULLISH_WATCH outlook but price near resistance, so only a watch is advised.
- Education stocks CIRA.CA and TALM.CA show constructive outlooks and liquidity cooling, yet they sit above support, limiting near‑term upside in a bearish market.
- Telecom (ETEL.CA) and Investment Holding (OIH.CA) display normal liquidity and extended RSI, indicating momentum may be stretched and caution is warranted.
- Because EGX30/EGX70 remain below their MA20/MA50 with negative median returns, the risk mode shifts to defensive, increasing uncertainty for any new buys over the next 1‑3 days.

## Top Liquidity Spikes
- EGSA.CA: spike=15.36 liquidity=100936.9 outlook=CONSTRUCTIVE score=66 buy_ready=False
- MHOT.CA: spike=9.91 liquidity=108740624.0 outlook=BULLISH_WATCH score=100 buy_ready=False
- POUL.CA: spike=5.89 liquidity=151878896.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SDTI.CA: spike=5.74 liquidity=141663648.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ROTO.CA: spike=3.3 liquidity=22636522.0 outlook=WEAK_OR_RISKY score=22 buy_ready=False

## Sector Leaderboard
- #1 Tourism & Leisure: score=23.46 5d=4.89% 20d=3.22% aboveMA50=100.0%
- #2 Telecommunications: score=20.19 5d=1.12% 20d=10.4% aboveMA50=100.0%
- #3 Investment Holding: score=7.46 5d=-2.76% 20d=16.46% aboveMA50=100.0%
- #4 Education: score=5.11 5d=-5.09% 20d=13.91% aboveMA50=66.67%
- #5 Energy & Petrochemicals: score=4.6 5d=0.0% 20d=6.33% aboveMA50=66.67%
- #6 Transportation & Logistics: score=3.33 5d=-1.36% 20d=2.51% aboveMA50=50.0%
- #7 Agriculture & Food Production: score=2.68 5d=-5.24% 20d=5.69% aboveMA50=50.0%
- #8 Technology & Distribution: score=2.37 5d=0.0% 20d=0.0% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MHOT.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- BINV.CA: BULLISH_WATCH score=79.46 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- ALCN.CA: BULLISH_WATCH score=79.33 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- EGCH.CA: BULLISH_WATCH score=72.34 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- CANA.CA: BULLISH_WATCH score=71.41 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended; sector is not leading
- TALM.CA: BULLISH_WATCH score=71.11 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; far above support
- DTPP.CA: BULLISH_WATCH score=71 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- KZPC.CA: BULLISH_WATCH score=71 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- MPCO.CA: CONSTRUCTIVE score=68.68 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; far above support
- EGTS.CA: CONSTRUCTIVE score=68 liquidity=TRADEABLE sector=LAGGING risk=momentum is extended; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=8.36 buy_ready=False sector_rank=17 price=277.62 support=277.0 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=39.64 liquidity=5214678.5 spike=0.21
- ABUK.CA: score=17.54 buy_ready=False sector_rank=11 price=88.97 support=76.01 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=55.49 liquidity=27373336.0 spike=0.15
- ACAMD.CA: score=8.65 buy_ready=False sector_rank=17 price=1.97 support=1.94 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=12.82 liquidity=60910964.0 spike=1.25
- ACGC.CA: score=14.11 buy_ready=False sector_rank=12 price=13.95 support=13.65 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=39.67 liquidity=7068564.0 spike=0.28
- ADCI.CA: score=4.59 buy_ready=False sector_rank=17 price=276.09 support=267.66 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=36.46 liquidity=1439162.63 spike=0.32
- ADIB.CA: score=14.56 buy_ready=False sector_rank=10 price=51.22 support=49.0 resistance=55.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=41.07 liquidity=23066102.0 spike=0.27
- ADPC.CA: score=7.15 buy_ready=False sector_rank=17 price=3.65 support=3.75 resistance=4.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=27.78 liquidity=12278765.0 spike=0.65
- AFDI.CA: score=4.96 buy_ready=False sector_rank=17 price=51.82 support=51.5 resistance=61.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=39.42 liquidity=1816792.38 spike=0.1
- AFMC.CA: score=7.13 buy_ready=False sector_rank=17 price=151.3 support=151.1 resistance=221.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=47.13 liquidity=3984178.0 spike=0.07
- AJWA.CA: score=17.15 buy_ready=False sector_rank=17 price=181.95 support=175.15 resistance=199.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=63.11 liquidity=13823182.0 spike=0.31
- ALCN.CA: score=22.33 buy_ready=False sector_rank=6 price=32.6 support=30.05 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=53.19 liquidity=11568852.0 spike=0.3
- ALUM.CA: score=0.93 buy_ready=False sector_rank=17 price=23.93 support=23.6 resistance=30.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=22.0 liquidity=2779991.5 spike=0.37
- AMER.CA: score=12.91 buy_ready=False sector_rank=18 price=4.96 support=4.8 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=40.09 liquidity=13546532.0 spike=0.26
- AMES.CA: score=7.15 buy_ready=False sector_rank=17 price=46.93 support=47.55 resistance=150.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=14.66 liquidity=35018292.0 spike=0.13
- AMIA.CA: score=16.15 buy_ready=False sector_rank=17 price=18.66 support=17.12 resistance=21.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=44.26 liquidity=20014528.0 spike=0.57
- AMOC.CA: score=18.84 buy_ready=False sector_rank=5 price=13.12 support=11.0 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=48.22 liquidity=36780128.0 spike=0.22
- APSW.CA: score=2.66 buy_ready=False sector_rank=17 price=8.19 support=8.16 resistance=8.79 source=Yahoo Finance as_of=2026-09-23T21:00:00+00:00 freshness=FRESH RSI=35.61 liquidity=512538.36 spike=0.62
- ARAB.CA: score=6.91 buy_ready=False sector_rank=18 price=0.22 support=0.22 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=20.34 liquidity=33008028.0 spike=0.38
- ARCC.CA: score=7.7 buy_ready=False sector_rank=21 price=64.26 support=66.12 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=18.63 liquidity=35833256.0 spike=1.15
- AREH.CA: score=0.94 buy_ready=False sector_rank=17 price=1.32 support=1.35 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=23.08 liquidity=3791971.0 spike=0.28
- ASCM.CA: score=4.15 buy_ready=False sector_rank=17 price=58.06 support=57.36 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=26.49 liquidity=5999844.5 spike=0.32
- ASPI.CA: score=3.15 buy_ready=False sector_rank=17 price=0.37 support=0.37 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18038220.0 spike=0.28
- ATLC.CA: score=-0.47 buy_ready=False sector_rank=16 price=6.02 support=5.95 resistance=6.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6158698.5 spike=0.21
- ATQA.CA: score=17.54 buy_ready=False sector_rank=11 price=12.56 support=11.56 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=52.85 liquidity=58381060.0 spike=0.56
- AXPH.CA: score=11.24 buy_ready=False sector_rank=17 price=1617.66 support=1580.0 resistance=1750.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=44.43 liquidity=5091260.5 spike=0.69
- BINV.CA: score=15.84 buy_ready=False sector_rank=3 price=57.07 support=48.04 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=65.76 liquidity=3438687.75 spike=0.13
- BIOC.CA: score=7.12 buy_ready=False sector_rank=17 price=251.45 support=247.03 resistance=453.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=19.0 liquidity=8976089.0 spike=0.1
- BTFH.CA: score=7.38 buy_ready=False sector_rank=16 price=2.77 support=2.79 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=28.85 liquidity=49737928.0 spike=0.57
- CAED.CA: score=-0.11 buy_ready=False sector_rank=17 price=117.09 support=112.01 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=24.95 liquidity=1743418.88 spike=0.09
- CANA.CA: score=22.18 buy_ready=False sector_rank=10 price=46.67 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=65.91 liquidity=30854988.0 spike=1.31
- CCAP.CA: score=19.4 buy_ready=False sector_rank=3 price=6.91 support=5.74 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=75.61 liquidity=414836224.0 spike=0.48
- CCRS.CA: score=6.7 buy_ready=False sector_rank=17 price=2.46 support=2.4 resistance=2.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=46.9 liquidity=3548519.5 spike=0.15
- CEFM.CA: score=7.03 buy_ready=False sector_rank=17 price=140.84 support=135.0 resistance=167.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=36.31 liquidity=878384.63 spike=0.1
- CERA.CA: score=8.15 buy_ready=False sector_rank=17 price=1.24 support=1.22 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=17.95 liquidity=92798392.0 spike=0.67
- CFGH.CA: score=1.15 buy_ready=False sector_rank=17 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance as_of=2026-09-23T21:00:00+00:00 freshness=FRESH RSI=23.08 liquidity=1710.51 spike=0.1
- CICH.CA: score=8.14 buy_ready=False sector_rank=16 price=12.05 support=11.51 resistance=13.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=39.08 liquidity=1766062.25 spike=0.3
- CIEB.CA: score=4.65 buy_ready=False sector_rank=10 price=24.04 support=23.9 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=28.51 liquidity=5085310.5 spike=0.36
- CIRA.CA: score=23.04 buy_ready=False sector_rank=4 price=39.89 support=32.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=54.94 liquidity=11581450.0 spike=0.29
- CLHO.CA: score=7.7 buy_ready=False sector_rank=20 price=15.53 support=15.35 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=14.8 liquidity=10964298.0 spike=0.16
- CNFN.CA: score=2.5 buy_ready=False sector_rank=16 price=4.17 support=4.24 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=26.26 liquidity=5128941.5 spike=0.46
- COMI.CA: score=9.56 buy_ready=False sector_rank=10 price=128.59 support=126.81 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=14.02 liquidity=104935176.0 spike=0.17
- COPR.CA: score=16.11 buy_ready=False sector_rank=17 price=0.48 support=0.46 resistance=0.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=40.94 liquidity=9962727.0 spike=0.29
- COSG.CA: score=5.62 buy_ready=False sector_rank=17 price=1.64 support=1.63 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=19.57 liquidity=7473206.0 spike=0.26
- CPCI.CA: score=11.01 buy_ready=False sector_rank=17 price=560.43 support=530.0 resistance=584.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=71.71 liquidity=2863529.75 spike=0.94
- CSAG.CA: score=3.27 buy_ready=False sector_rank=6 price=37.24 support=36.5 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=30.89 liquidity=2936943.25 spike=0.2
- DAPH.CA: score=8.15 buy_ready=False sector_rank=17 price=103.75 support=101.55 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=22.93 liquidity=25283318.0 spike=0.48
- DEIN.CA: score=6.15 buy_ready=False sector_rank=17 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=2.45 buy_ready=False sector_rank=15 price=24.93 support=25.56 resistance=29.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=25.45 liquidity=4929788.0 spike=0.94
- DSCW.CA: score=7.15 buy_ready=False sector_rank=17 price=1.75 support=1.71 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=15.63 liquidity=12522097.0 spike=0.54
- DTPP.CA: score=18.15 buy_ready=False sector_rank=17 price=323.47 support=296.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=57.15 liquidity=25378116.0 spike=0.3
- EALR.CA: score=0.21 buy_ready=False sector_rank=17 price=352.33 support=340.0 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=32.72 liquidity=3061501.25 spike=0.23
- EASB.CA: score=5.9 buy_ready=False sector_rank=17 price=7.4 support=7.13 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=51.44 liquidity=2753091.75 spike=0.17
- EAST.CA: score=3.22 buy_ready=False sector_rank=15 price=31.21 support=30.59 resistance=36.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=4.1 liquidity=5701409.5 spike=0.1
- EBSC.CA: score=4.57 buy_ready=False sector_rank=17 price=1.93 support=1.9 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=36.49 liquidity=1419472.38 spike=0.13
- ECAP.CA: score=0.05 buy_ready=False sector_rank=17 price=31.09 support=31.0 resistance=34.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=18.79 liquidity=1906689.5 spike=0.21
- EDFM.CA: score=-1.32 buy_ready=False sector_rank=17 price=387.66 support=382.35 resistance=465.0 source=Yahoo Finance as_of=2026-09-23T21:00:00+00:00 freshness=FRESH RSI=30.78 liquidity=534583.15 spike=0.3
- EEII.CA: score=10.99 buy_ready=False sector_rank=17 price=2.28 support=2.15 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=49.33 liquidity=6841302.0 spike=0.46
- EFIC.CA: score=4.54 buy_ready=False sector_rank=11 price=166.01 support=165.01 resistance=179.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42366644.0 spike=0.12
- EFID.CA: score=13.52 buy_ready=False sector_rank=15 price=29.53 support=28.56 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=43.21 liquidity=37610212.0 spike=0.54
- EFIH.CA: score=13.56 buy_ready=False sector_rank=14 price=23.0 support=22.16 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=43.39 liquidity=19763438.0 spike=0.33
- EGAL.CA: score=17.54 buy_ready=False sector_rank=11 price=355.46 support=340.0 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=38.49 liquidity=10994850.0 spike=0.15
- EGAS.CA: score=9.36 buy_ready=False sector_rank=5 price=58.8 support=55.7 resistance=60.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33504626.0 spike=2.76
- EGBE.CA: score=7.57 buy_ready=False sector_rank=10 price=0.52 support=0.49 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=45.65 liquidity=8491.41 spike=0.08
- EGCH.CA: score=19.54 buy_ready=False sector_rank=11 price=14.07 support=13.53 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=49.25 liquidity=89775928.0 spike=0.69
- EGSA.CA: score=18.5 buy_ready=False sector_rank=2 price=9.0 support=8.8 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=24 September 12:29 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=100936.9 spike=15.36
- EGTS.CA: score=20.09 buy_ready=False sector_rank=18 price=18.38 support=16.51 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=62.03 liquidity=37572488.0 spike=1.09
- EHDR.CA: score=8.59 buy_ready=False sector_rank=17 price=2.59 support=2.44 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=14.75 liquidity=20859134.0 spike=1.22
- ELEC.CA: score=6.77 buy_ready=False sector_rank=19 price=1.92 support=1.91 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=25.64 liquidity=34263148.0 spike=0.44
- ELKA.CA: score=4.15 buy_ready=False sector_rank=17 price=1.56 support=1.54 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=10.53 liquidity=5998540.5 spike=0.18
- ELNA.CA: score=-2.73 buy_ready=False sector_rank=17 price=35.22 support=33.96 resistance=38.99 source=Yahoo Finance as_of=2026-09-23T21:00:00+00:00 freshness=FRESH RSI=27.7 liquidity=126897.66 spike=0.33
- ELSH.CA: score=8.15 buy_ready=False sector_rank=17 price=12.13 support=12.06 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=26.62 liquidity=29623692.0 spike=0.82
- ELWA.CA: score=-1.47 buy_ready=False sector_rank=17 price=1.64 support=1.61 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=28.13 liquidity=378783.0 spike=0.23
- EMFD.CA: score=10.91 buy_ready=False sector_rank=18 price=13.04 support=12.2 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=26.82 liquidity=29277380.0 spike=0.19
- ENGC.CA: score=9.92 buy_ready=False sector_rank=17 price=40.58 support=39.11 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=36.82 liquidity=6769151.5 spike=0.38
- EOSB.CA: score=12.63 buy_ready=False sector_rank=17 price=1.57 support=1.53 resistance=1.64 source=Yahoo Finance as_of=2026-09-23T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=218437.25 spike=3.13
- EPCO.CA: score=13.15 buy_ready=False sector_rank=17 price=10.36 support=10.3 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=39.83 liquidity=10441532.0 spike=0.7
- EPPK.CA: score=-6.43 buy_ready=False sector_rank=17 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=20.4 buy_ready=False sector_rank=2 price=133.98 support=112.5 resistance=140.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=79.88 liquidity=53939064.0 spike=0.19
- ETRS.CA: score=2.63 buy_ready=False sector_rank=17 price=10.46 support=10.42 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=31.19 liquidity=4486134.5 spike=0.35
- EXPA.CA: score=21.56 buy_ready=False sector_rank=10 price=21.47 support=19.96 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=45.42 liquidity=23509888.0 spike=0.66
- FAIT.CA: score=9.5 buy_ready=False sector_rank=10 price=44.89 support=38.48 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=51.75 liquidity=1938764.13 spike=0.31
- FAITA.CA: score=3.58 buy_ready=False sector_rank=10 price=0.98 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=11099.2 spike=0.26
- FERC.CA: score=6.64 buy_ready=False sector_rank=11 price=75.41 support=76.1 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=37.24 liquidity=3103314.75 spike=0.22
- FWRY.CA: score=8.56 buy_ready=False sector_rank=14 price=18.77 support=17.5 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=25.35 liquidity=29477114.0 spike=0.23
- GBCO.CA: score=15.9 buy_ready=False sector_rank=13 price=30.0 support=27.0 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=54.78 liquidity=32612764.0 spike=0.45
- GDWA.CA: score=7.15 buy_ready=False sector_rank=17 price=0.68 support=0.69 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=11.85 liquidity=18523702.0 spike=0.42
- GGCC.CA: score=1.4 buy_ready=False sector_rank=17 price=0.73 support=0.7 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=27.02 liquidity=3247430.25 spike=0.11
- GIHD.CA: score=18.15 buy_ready=False sector_rank=17 price=74.0 support=63.1 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=61.07 liquidity=22602958.0 spike=0.74
- GMCI.CA: score=-2.54 buy_ready=False sector_rank=17 price=1.7 support=1.65 resistance=1.94 source=Yahoo Finance as_of=2026-09-23T21:00:00+00:00 freshness=FRESH RSI=21.43 liquidity=311315.91 spike=0.63
- GRCA.CA: score=2.25 buy_ready=False sector_rank=17 price=37.78 support=38.7 resistance=85.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=15.09 liquidity=5100920.5 spike=0.12
- GSSC.CA: score=6.57 buy_ready=False sector_rank=17 price=291.88 support=278.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=44.16 liquidity=426984.81 spike=0.05
- GTWL.CA: score=11.15 buy_ready=False sector_rank=17 price=216.43 support=210.0 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=34.17 liquidity=57977976.0 spike=0.38
- HDBK.CA: score=16.56 buy_ready=False sector_rank=10 price=109.45 support=95.51 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=40.67 liquidity=10992902.0 spike=0.18
- HELI.CA: score=12.91 buy_ready=False sector_rank=18 price=7.82 support=7.59 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=40.78 liquidity=49030884.0 spike=0.29
- HRHO.CA: score=7.38 buy_ready=False sector_rank=16 price=23.99 support=23.91 resistance=26.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=10.53 liquidity=52082736.0 spike=0.52
- ICID.CA: score=11.91 buy_ready=False sector_rank=17 price=17.34 support=16.2 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=48.55 liquidity=5764175.0 spike=0.59
- IDRE.CA: score=8.93 buy_ready=False sector_rank=17 price=49.54 support=51.0 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=42.04 liquidity=5779072.5 spike=0.34
- IFAP.CA: score=8.27 buy_ready=False sector_rank=7 price=20.03 support=19.05 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=36.87 liquidity=3199635.75 spike=0.15
- INFI.CA: score=4.13 buy_ready=False sector_rank=17 price=125.15 support=122.0 resistance=161.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=28.79 liquidity=5983419.0 spike=0.32
- IRON.CA: score=10.91 buy_ready=False sector_rank=11 price=27.48 support=26.3 resistance=31.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=35.47 liquidity=5372373.0 spike=0.39
- ISMA.CA: score=4.37 buy_ready=False sector_rank=17 price=28.0 support=27.7 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=31.75 liquidity=6217139.0 spike=0.34
- ISMQ.CA: score=9.54 buy_ready=False sector_rank=11 price=8.38 support=8.35 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=24.36 liquidity=10079373.0 spike=0.41
- ISPH.CA: score=7.7 buy_ready=False sector_rank=20 price=11.76 support=11.5 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=22.94 liquidity=28708630.0 spike=0.42
- JUFO.CA: score=7.52 buy_ready=False sector_rank=15 price=25.74 support=25.5 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=32.1 liquidity=12070220.0 spike=0.56
- KABO.CA: score=10.85 buy_ready=False sector_rank=12 price=8.82 support=8.78 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=46.72 liquidity=6810693.0 spike=0.17
- KWIN.CA: score=2.74 buy_ready=False sector_rank=17 price=86.24 support=82.5 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=29.43 liquidity=4595893.5 spike=0.12
- KZPC.CA: score=16.41 buy_ready=False sector_rank=17 price=13.8 support=12.6 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=61.15 liquidity=8257076.0 spike=0.26
- LCSW.CA: score=4.89 buy_ready=False sector_rank=21 price=31.51 support=31.0 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=19.46 liquidity=7485440.0 spike=0.32
- LUTS.CA: score=13.15 buy_ready=False sector_rank=17 price=0.83 support=0.82 resistance=1.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=40.45 liquidity=17153184.0 spike=0.14
- MAAL.CA: score=7.09 buy_ready=False sector_rank=17 price=11.26 support=10.63 resistance=12.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=54437932.0 spike=2.97
- MASR.CA: score=8.15 buy_ready=False sector_rank=17 price=7.25 support=7.26 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=16.58 liquidity=30338020.0 spike=0.32
- MBSC.CA: score=7.4 buy_ready=False sector_rank=21 price=328.0 support=325.0 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=25.55 liquidity=25586512.0 spike=0.58
- MCQE.CA: score=7.4 buy_ready=False sector_rank=21 price=200.21 support=197.51 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=21.89 liquidity=11931155.0 spike=0.48
- MCRO.CA: score=3.15 buy_ready=False sector_rank=17 price=1.5 support=1.5 resistance=1.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26505732.0 spike=0.21
- MENA.CA: score=-1.74 buy_ready=False sector_rank=18 price=6.6 support=6.45 resistance=7.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=29.57 liquidity=344149.81 spike=0.21
- MEPA.CA: score=4.67 buy_ready=False sector_rank=17 price=1.77 support=1.76 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=14.29 liquidity=6522848.5 spike=0.16
- MFPC.CA: score=19.54 buy_ready=False sector_rank=11 price=46.9 support=39.71 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=54.36 liquidity=19676296.0 spike=0.11
- MFSC.CA: score=7.29 buy_ready=False sector_rank=17 price=48.06 support=48.5 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=38.93 liquidity=4140978.0 spike=0.87
- MHOT.CA: score=32.4 buy_ready=False sector_rank=1 price=19.7 support=16.61 resistance=19.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=56.49 liquidity=108740624.0 spike=9.91
- MICH.CA: score=11.86 buy_ready=False sector_rank=17 price=46.8 support=45.77 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=40.58 liquidity=8714678.0 spike=0.64
- MILS.CA: score=10.64 buy_ready=False sector_rank=17 price=183.45 support=180.01 resistance=232.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=36.42 liquidity=7495788.0 spike=0.37
- MIPH.CA: score=9.88 buy_ready=False sector_rank=20 price=790.92 support=700.2 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=50.76 liquidity=5183524.0 spike=0.55
- MOED.CA: score=6.85 buy_ready=False sector_rank=17 price=0.69 support=0.69 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=11.94 liquidity=9697814.0 spike=0.15
- MOIL.CA: score=12.86 buy_ready=False sector_rank=5 price=0.7 support=0.67 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=73.02 liquidity=24454.85 spike=0.09
- MOIN.CA: score=11.15 buy_ready=False sector_rank=17 price=35.58 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=26.15 liquidity=23656826.0 spike=0.82
- MOSC.CA: score=-1.28 buy_ready=False sector_rank=17 price=291.1 support=281.0 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=17.29 liquidity=567328.63 spike=0.1
- MPCI.CA: score=11.15 buy_ready=False sector_rank=17 price=371.28 support=363.63 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=26.37 liquidity=121259184.0 spike=0.88
- MPCO.CA: score=20.07 buy_ready=False sector_rank=7 price=2.59 support=2.07 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=125576488.0 spike=0.7
- MPRC.CA: score=10.14 buy_ready=False sector_rank=17 price=38.76 support=37.65 resistance=46.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=6987494.5 spike=0.19
- MTIE.CA: score=5.12 buy_ready=False sector_rank=13 price=8.18 support=8.02 resistance=8.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=25.23 liquidity=7222961.0 spike=0.29
- NAHO.CA: score=6.16 buy_ready=False sector_rank=17 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=47.06 liquidity=9235.8 spike=0.16
- NCCW.CA: score=18.15 buy_ready=False sector_rank=17 price=7.19 support=5.77 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=60.26 liquidity=18253276.0 spike=0.24
- NEDA.CA: score=3.62 buy_ready=False sector_rank=17 price=2.7 support=2.68 resistance=2.89 source=Yahoo Finance as_of=2026-09-23T21:00:00+00:00 freshness=FRESH RSI=43.24 liquidity=474824.71 spike=0.5
- NHPS.CA: score=5.68 buy_ready=False sector_rank=17 price=74.5 support=72.52 resistance=92.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=33.28 liquidity=7532833.5 spike=0.47
- NINH.CA: score=7.85 buy_ready=False sector_rank=17 price=19.92 support=19.55 resistance=24.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=23.3 liquidity=9697003.0 spike=0.51
- NIPH.CA: score=12.7 buy_ready=False sector_rank=20 price=319.43 support=290.0 resistance=401.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=42.61 liquidity=41664328.0 spike=0.28
- OBRI.CA: score=1.84 buy_ready=False sector_rank=17 price=28.18 support=28.12 resistance=34.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=14.56 liquidity=4687482.0 spike=0.32
- OCDI.CA: score=7.91 buy_ready=False sector_rank=18 price=27.99 support=27.4 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=16.97 liquidity=19167650.0 spike=0.27
- OCPH.CA: score=0.82 buy_ready=False sector_rank=17 price=222.53 support=210.0 resistance=277.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=29.63 liquidity=1669290.13 spike=0.27
- ODIN.CA: score=3.0 buy_ready=False sector_rank=17 price=2.6 support=2.54 resistance=3.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=32.14 liquidity=4854661.5 spike=0.28
- OFH.CA: score=3.15 buy_ready=False sector_rank=17 price=0.93 support=0.92 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=117317112.0 spike=0.84
- OIH.CA: score=20.4 buy_ready=False sector_rank=3 price=2.08 support=1.98 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=63.33 liquidity=21802376.0 spike=0.18
- OLFI.CA: score=2.91 buy_ready=False sector_rank=15 price=22.38 support=22.07 resistance=23.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=34.04 liquidity=2391766.25 spike=0.13
- ORAS.CA: score=4.6 buy_ready=False sector_rank=9 price=813.98 support=813.0 resistance=835.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24905186.0 spike=1.0
- ORHD.CA: score=12.91 buy_ready=False sector_rank=18 price=40.07 support=39.1 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=36.11 liquidity=93735616.0 spike=0.56
- ORWE.CA: score=12.04 buy_ready=False sector_rank=12 price=27.25 support=25.6 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=34.78 liquidity=28712150.0 spike=0.51
- PHAR.CA: score=7.7 buy_ready=False sector_rank=20 price=111.49 support=108.1 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=18.99 liquidity=67643760.0 spike=0.73
- PHDC.CA: score=2.91 buy_ready=False sector_rank=18 price=12.81 support=12.8 resistance=13.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=84093608.0 spike=0.57
- PHTV.CA: score=9.11 buy_ready=False sector_rank=17 price=354.91 support=311.27 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=44.14 liquidity=960640.5 spike=0.58
- POUL.CA: score=8.52 buy_ready=False sector_rank=15 price=10.23 support=10.2 resistance=12.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=151878896.0 spike=5.89
- PRCL.CA: score=2.4 buy_ready=False sector_rank=21 price=29.08 support=28.68 resistance=31.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12394130.0 spike=0.71
- PRDC.CA: score=6.42 buy_ready=False sector_rank=18 price=7.15 support=7.14 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=12.44 liquidity=8512914.0 spike=0.15
- PRMH.CA: score=-0.65 buy_ready=False sector_rank=17 price=2.4 support=2.43 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=32.94 liquidity=1197480.13 spike=0.16
- RACC.CA: score=0.74 buy_ready=False sector_rank=17 price=9.33 support=9.2 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=24.04 liquidity=2594994.5 spike=0.16
- RAKT.CA: score=2.2 buy_ready=False sector_rank=17 price=22.08 support=21.2 resistance=23.02 source=Yahoo Finance as_of=2026-09-23T21:00:00+00:00 freshness=FRESH RSI=47.17 liquidity=48377.28 spike=0.22
- RAYA.CA: score=6.11 buy_ready=False sector_rank=8 price=6.44 support=6.4 resistance=7.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=81165512.0 spike=1.58
- RMDA.CA: score=12.7 buy_ready=False sector_rank=20 price=5.66 support=5.61 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=37.78 liquidity=20820756.0 spike=0.35
- ROTO.CA: score=12.75 buy_ready=False sector_rank=17 price=40.75 support=35.02 resistance=45.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=22.95 liquidity=22636522.0 spike=3.3
- RREI.CA: score=0.37 buy_ready=False sector_rank=17 price=4.03 support=3.86 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=32.08 liquidity=2222233.5 spike=0.14
- RTVC.CA: score=0.33 buy_ready=False sector_rank=17 price=3.68 support=3.67 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=3184100.5 spike=0.9
- RUBX.CA: score=3.15 buy_ready=False sector_rank=17 price=16.64 support=16.6 resistance=17.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=53760788.0 spike=0.89
- SAUD.CA: score=16.56 buy_ready=False sector_rank=10 price=22.7 support=22.7 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=44.31 liquidity=13298006.0 spike=0.66
- SCEM.CA: score=7.4 buy_ready=False sector_rank=21 price=81.99 support=83.05 resistance=105.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=21.7 liquidity=86788880.0 spike=0.98
- SCFM.CA: score=3.42 buy_ready=False sector_rank=17 price=250.01 support=250.2 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=35.83 liquidity=1267011.13 spike=0.19
- SCTS.CA: score=1.55 buy_ready=False sector_rank=4 price=572.42 support=566.66 resistance=639.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=24.5 liquidity=503442.53 spike=0.21
- SDTI.CA: score=8.15 buy_ready=False sector_rank=17 price=85.04 support=79.0 resistance=91.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=141663648.0 spike=5.74
- SEIG.CA: score=-0.6 buy_ready=False sector_rank=17 price=228.74 support=222.1 resistance=274.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=30.53 liquidity=1254606.25 spike=0.67
- SIPC.CA: score=10.62 buy_ready=False sector_rank=17 price=5.0 support=4.77 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=27.13 liquidity=9474267.0 spike=0.13
- SKPC.CA: score=8.54 buy_ready=False sector_rank=11 price=16.74 support=16.8 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=28.33 liquidity=47585672.0 spike=0.35
- SMFR.CA: score=-0.94 buy_ready=False sector_rank=17 price=218.66 support=217.0 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=26.08 liquidity=914663.0 spike=0.12
- SNFC.CA: score=13.69 buy_ready=False sector_rank=17 price=11.51 support=10.26 resistance=11.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=77.78 liquidity=6545294.5 spike=0.46
- SPIN.CA: score=3.48 buy_ready=False sector_rank=12 price=16.39 support=16.1 resistance=20.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=16.89 liquidity=4438378.0 spike=0.46
- SPMD.CA: score=11.62 buy_ready=False sector_rank=17 price=0.4 support=0.4 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=42.28 liquidity=9467703.0 spike=0.12
- SUGR.CA: score=8.84 buy_ready=False sector_rank=15 price=56.23 support=55.06 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=41.74 liquidity=2325783.0 spike=0.07
- SVCE.CA: score=3.15 buy_ready=False sector_rank=17 price=10.34 support=10.32 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24159962.0 spike=0.12
- SWDY.CA: score=7.77 buy_ready=False sector_rank=19 price=115.11 support=116.5 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=15.54 liquidity=40103648.0 spike=0.63
- TALM.CA: score=21.04 buy_ready=False sector_rank=4 price=20.69 support=17.11 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=58.26 liquidity=15868733.0 spike=0.24
- TMGH.CA: score=6.91 buy_ready=False sector_rank=18 price=89.09 support=90.0 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=17.46 liquidity=207460944.0 spike=0.71
- TRTO.CA: score=-1.84 buy_ready=False sector_rank=17 price=0.05 support=0.05 resistance=0.08 source=Yahoo Finance as_of=2026-09-23T21:00:00+00:00 freshness=FRESH RSI=26.47 liquidity=10509.86 spike=0.36
- UEFM.CA: score=-2.27 buy_ready=False sector_rank=17 price=462.21 support=440.66 resistance=574.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=32.27 liquidity=580049.94 spike=0.19
- UEGC.CA: score=7.15 buy_ready=False sector_rank=17 price=1.5 support=1.51 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=31.48 liquidity=20549450.0 spike=0.42
- UNIP.CA: score=2.82 buy_ready=False sector_rank=17 price=0.36 support=0.35 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=27.27 liquidity=4674542.0 spike=0.22
- UNIT.CA: score=4.24 buy_ready=False sector_rank=18 price=17.41 support=16.66 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=45.51 liquidity=1324321.13 spike=0.09
- WCDF.CA: score=9.03 buy_ready=False sector_rank=17 price=666.73 support=640.0 resistance=796.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=2878121.0 spike=0.55
- WKOL.CA: score=7.11 buy_ready=False sector_rank=17 price=312.12 support=320.05 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=39.71 liquidity=3962439.0 spike=0.29
- ZEOT.CA: score=-0.23 buy_ready=False sector_rank=17 price=12.28 support=12.25 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=26.7 liquidity=1626257.88 spike=0.26
- ZMID.CA: score=7.91 buy_ready=False sector_rank=18 price=8.0 support=7.92 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=18.57 liquidity=162519248.0 spike=0.84

## Backtesting Lite
- MHOT.CA: 180d return=-25.13%, max drawdown=-54.07%, MA20>MA50 days last20=16, as_of=2026-09-23T21:00:00+00:00
- CIRA.CA: 180d return=124.28%, max drawdown=-16.44%, MA20>MA50 days last20=20, as_of=2026-09-23T21:00:00+00:00
- ALCN.CA: 180d return=50.57%, max drawdown=-15.82%, MA20>MA50 days last20=20, as_of=2026-09-23T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- MHOT.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Hotels summary=Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26; Shareholder buys EGP 3.39m worth of shares in Misr Hotels; Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits
  - Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26: https://english.mubasher.info/news/4602482/Misr-Hotels-net-profits-cross-EGP-1-1bn-in-9M-25-26/
  - Shareholder buys EGP 3.39m worth of shares in Misr Hotels: https://english.mubasher.info/news/4013808/Shareholder-buys-EGP-3-39m-worth-of-shares-in-Misr-Hotels/
  - Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits: https://english.mubasher.info/news/3975543/Misr-Hotels-repays-EGP-383m-of-NBE-s-loan-unveils-estimated-profits/
- CIRA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Investment and Real Estate Development summary=CIRA Education take over 51% of L’École Française Hurghada; CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion; CIRA Education launches Middle East’s 1st initiative for care economy
  - CIRA Education take over 51% of L’École Française Hurghada: https://english.mubasher.info/news/4488666/CIRA-Education-take-over-51-of-L-%C3%89cole-Fran%C3%A7aise-Hurghada/
  - CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion: https://english.mubasher.info/news/4393636/CIRA-s-majority-shareholder-acquires-37-5-additional-equity-backs-regional-expansion/
  - CIRA Education launches Middle East’s 1st initiative for care economy: https://english.mubasher.info/news/4391766/CIRA-Education-launches-Middle-East-s-1st-initiative-for-care-economy/
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- CANA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=634 sources=3 expected=Suez Canal Bank summary=Suez Canal Bank delivers EGP 1.6bn profits in Q1-26; Suez Canal Bank unveils details for previous dividends payout; Suez Canal Bank to distribute EGP 5bn bonus shares for 2025
  - Suez Canal Bank delivers EGP 1.6bn profits in Q1-26: https://english.mubasher.info/news/4611255/Suez-Canal-Bank-delivers-EGP-1-6bn-profits-in-Q1-26/
  - Suez Canal Bank unveils details for previous dividends payout: https://english.mubasher.info/news/4586807/Suez-Canal-Bank-unveils-details-for-previous-dividends-payout/
  - Suez Canal Bank to distribute EGP 5bn bonus shares for 2025: https://english.mubasher.info/news/4581661/Suez-Canal-Bank-to-distribute-EGP-5bn-bonus-shares-for-2025/
- EXPA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Export Development Bank of Egypt summary=Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- OIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Investment Holding summary=Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.

## Warnings
- Evidence for MHOT.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
