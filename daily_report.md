# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-06-30T10:03:17.314926+00:00
Generated Cairo: 2026-06-30 13:03
Run timing: target 09:15 Cairo | generated Cairo 2026-06-30 13:03 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-06-30 12:58

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 181/190
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, June 30
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 15.0% / above MA50 20.0%
- EGX70 regime: BEARISH / above MA20 53.85% / above MA50 69.23%
- Sector breadth: 9.52%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=219883072.0 spike=0.37 score=14.4
- TMGH.CA: liquidity=170402736.0 spike=0.46 score=14.42
- RAYA.CA: liquidity=133355024.0 spike=1.59 score=23.58
- ORAS.CA: liquidity=129377864.0 spike=1.0 score=4.6
- ETRS.CA: liquidity=127184528.0 spike=1.72 score=5.86

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The EGX30 and EGX70 indices are both in a bearish regime, sector breadth is weak at 9.5%, and the scanner is in DEFENSIVE_NO_NEW_BUY mode, so no new BUY signals are issued. The top‑ranked tickets (CSAG, MHOT, RAYA, etc.) show bullish watch outlooks and solid liquidity spikes, but they sit near resistance and lack strong short‑term catalyst, keeping the scanner on HOLD.
- Bearish EGX30/EGX70 trends and low breadth push risk mode to defensive, blocking new buys.
- Top tickets have accumulation‑spike liquidity and are near 20‑day resistance; short‑term upside is limited.
- Sector leaders (Tourism, Automotive, Technology) show modest returns; overall market support is weak.
- Liquidity remains adequate, but momentum is mixed and could reverse if broader market sentiment improves.
- Uncertainty remains high – any shift in EGX30/EGX70 trend or sector breadth could change the risk stance.

## Top Liquidity Spikes
- AMES.CA: spike=29.17 liquidity=124909224.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DTPP.CA: spike=15.81 liquidity=31808928.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- NHPS.CA: spike=5.33 liquidity=18543706.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GTWL.CA: spike=5.04 liquidity=125889848.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GMCI.CA: spike=4.15 liquidity=1664243.25 outlook=BULLISH_WATCH score=77.06 buy_ready=False

## Sector Leaderboard
- #1 Tourism & Leisure: score=8.83 5d=4.84% 20d=1.71% aboveMA50=100.0%
- #2 Automotive & Distribution: score=7.79 5d=2.47% 20d=7.28% aboveMA50=100.0%
- #3 Technology & Distribution: score=7.15 5d=-1.75% 20d=-2.67% aboveMA50=100.0%
- #4 Transportation & Logistics: score=5.74 5d=-0.26% 20d=-2.71% aboveMA50=50.0%
- #5 Textiles: score=2.21 5d=-2.61% 20d=-4.21% aboveMA50=75.0%
- #6 Healthcare: score=2.04 5d=-4.29% 20d=-1.1% aboveMA50=83.33%
- #7 Food, Beverages & Tobacco: score=2.02 5d=-3.15% 20d=-0.4% aboveMA50=57.14%
- #8 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CSAG.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- RAYA.CA: BULLISH_WATCH score=98.15 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- CAED.CA: BULLISH_WATCH score=89.06 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- FAIT.CA: BULLISH_WATCH score=83.0 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- MHOT.CA: BULLISH_WATCH score=80.83 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- POUL.CA: BULLISH_WATCH score=78.02 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MASR.CA: BULLISH_WATCH score=77.06 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- AFDI.CA: BULLISH_WATCH score=77.06 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- GMCI.CA: BULLISH_WATCH score=77.06 liquidity=TRADEABLE sector=IMPROVING risk=close to resistance; sector is not leading
- PHAR.CA: BULLISH_WATCH score=77.04 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=0.97 buy_ready=False sector_rank=10 price=202.61 support=196.0 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=29.49 liquidity=1548519.88 spike=0.25
- ABUK.CA: score=8.14 buy_ready=False sector_rank=20 price=67.66 support=66.66 resistance=84.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=9.05 liquidity=32504488.0 spike=0.24
- ACAMD.CA: score=12.42 buy_ready=False sector_rank=10 price=2.22 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=34.78 liquidity=43345780.0 spike=0.35
- ACGC.CA: score=12.4 buy_ready=False sector_rank=5 price=9.25 support=8.92 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=32.99 liquidity=9517895.0 spike=0.25
- ADCI.CA: score=13.32 buy_ready=False sector_rank=10 price=242.16 support=211.0 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=84.3 liquidity=4900353.5 spike=0.48
- ADIB.CA: score=14.4 buy_ready=False sector_rank=12 price=45.39 support=44.01 resistance=48.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=20875886.0 spike=0.23
- ADPC.CA: score=7.37 buy_ready=False sector_rank=10 price=3.45 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=35.4 liquidity=3950291.5 spike=0.19
- AFDI.CA: score=19.78 buy_ready=False sector_rank=10 price=44.3 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=45.35 liquidity=17419228.0 spike=1.18
- AFMC.CA: score=-0.22 buy_ready=False sector_rank=10 price=68.77 support=66.0 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=28.48 liquidity=359116.09 spike=0.16
- AJWA.CA: score=14.1 buy_ready=False sector_rank=10 price=175.0 support=132.0 resistance=188.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=74.49 liquidity=4677263.0 spike=0.17
- ALCN.CA: score=13.32 buy_ready=False sector_rank=4 price=28.63 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=32.53 liquidity=12322711.0 spike=1.01
- ALUM.CA: score=2.99 buy_ready=False sector_rank=10 price=21.24 support=20.55 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=11.73 liquidity=3565197.25 spike=0.37
- AMER.CA: score=9.42 buy_ready=False sector_rank=11 price=2.43 support=2.28 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=19.28 liquidity=60928988.0 spike=0.86
- AMES.CA: score=9.42 buy_ready=False sector_rank=10 price=66.26 support=57.23 resistance=66.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=124909224.0 spike=29.17
- AMIA.CA: score=1.7 buy_ready=False sector_rank=10 price=8.53 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=28.97 liquidity=2279304.75 spike=0.17
- AMOC.CA: score=9.02 buy_ready=False sector_rank=16 price=7.59 support=7.42 resistance=8.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=17.54 liquidity=16018638.0 spike=0.33
- ANFI.CA: score=5.76 buy_ready=False sector_rank=10 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=STALE RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=-1.0 buy_ready=False sector_rank=10 price=8.34 support=8.0 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=7.62 liquidity=578371.69 spike=0.65
- ARAB.CA: score=14.42 buy_ready=False sector_rank=11 price=0.21 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=55.88 liquidity=17059898.0 spike=0.2
- ARCC.CA: score=7.93 buy_ready=False sector_rank=15 price=55.01 support=53.0 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=27.87 liquidity=8909773.0 spike=0.26
- AREH.CA: score=19.42 buy_ready=False sector_rank=10 price=1.58 support=1.34 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=16687139.0 spike=0.49
- ARVA.CA: score=14.49 buy_ready=False sector_rank=10 price=10.9 support=9.43 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=46.86 liquidity=7070269.0 spike=0.22
- ASCM.CA: score=19.42 buy_ready=False sector_rank=10 price=59.68 support=47.7 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=54.53 liquidity=30636734.0 spike=0.33
- ASPI.CA: score=11.73 buy_ready=False sector_rank=10 price=0.31 support=0.27 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=29.06 liquidity=9301052.0 spike=0.13
- ATLC.CA: score=10.06 buy_ready=False sector_rank=13 price=5.09 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=48.0 liquidity=800427.5 spike=0.13
- ATQA.CA: score=12.14 buy_ready=False sector_rank=20 price=9.55 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=36.19 liquidity=12862378.0 spike=0.39
- AXPH.CA: score=9.76 buy_ready=False sector_rank=10 price=1118.12 support=1073.0 resistance=1174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:27 AM market time freshness=DELAYED_CURRENT RSI=42.94 liquidity=337693.38 spike=0.23
- BINV.CA: score=8.56 buy_ready=False sector_rank=17 price=46.01 support=44.02 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=39.7 liquidity=1759151.75 spike=0.17
- BIOC.CA: score=4.79 buy_ready=False sector_rank=10 price=68.67 support=66.75 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=35.71 liquidity=368389.03 spike=0.15
- BTFH.CA: score=13.26 buy_ready=False sector_rank=13 price=2.99 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=37.7 liquidity=94111536.0 spike=0.52
- CAED.CA: score=23.3 buy_ready=False sector_rank=10 price=73.35 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=44.96 liquidity=12196791.0 spike=2.94
- CANA.CA: score=14.96 buy_ready=False sector_rank=12 price=35.5 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=37.78 liquidity=8559795.0 spike=0.79
- CCAP.CA: score=8.8 buy_ready=False sector_rank=17 price=4.78 support=4.65 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=18.55 liquidity=120541656.0 spike=0.18
- CCRS.CA: score=1.29 buy_ready=False sector_rank=10 price=2.24 support=2.22 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=1863278.0 spike=0.11
- CEFM.CA: score=0.83 buy_ready=False sector_rank=10 price=100.1 support=95.75 resistance=109.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=20.18 liquidity=1402412.0 spike=0.78
- CERA.CA: score=9.43 buy_ready=False sector_rank=10 price=1.21 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=3009095.75 spike=0.18
- CFGH.CA: score=-1.57 buy_ready=False sector_rank=10 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=4880.0 spike=0.79
- CICH.CA: score=8.18 buy_ready=False sector_rank=13 price=11.76 support=11.1 resistance=12.8 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=48.77 liquidity=1919655.4 spike=0.74
- CIEB.CA: score=5.96 buy_ready=False sector_rank=12 price=23.54 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=51.06 liquidity=1560019.0 spike=0.23
- CIRA.CA: score=15.93 buy_ready=False sector_rank=9 price=28.45 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=61.39 liquidity=6486479.5 spike=0.38
- CLHO.CA: score=19.82 buy_ready=False sector_rank=6 price=16.29 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=66.94 liquidity=14773577.0 spike=0.4
- CNFN.CA: score=21.26 buy_ready=False sector_rank=13 price=4.73 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=53.55 liquidity=11037808.0 spike=0.27
- COMI.CA: score=14.4 buy_ready=False sector_rank=12 price=129.64 support=126.21 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=35.45 liquidity=219883072.0 spike=0.37
- COPR.CA: score=11.3 buy_ready=False sector_rank=10 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=43.55 liquidity=4871562.0 spike=0.17
- COSG.CA: score=8.71 buy_ready=False sector_rank=10 price=1.53 support=1.47 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=27.78 liquidity=9282329.0 spike=0.17
- CPCI.CA: score=17.22 buy_ready=False sector_rank=10 price=399.38 support=350.04 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=71.98 liquidity=4237128.5 spike=1.78
- CSAG.CA: score=26.3 buy_ready=False sector_rank=4 price=32.88 support=30.08 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=61.3 liquidity=24927126.0 spike=1.5
- DAPH.CA: score=10.26 buy_ready=False sector_rank=10 price=81.33 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=48.28 liquidity=1840640.38 spike=0.18
- DEIN.CA: score=5.42 buy_ready=False sector_rank=10 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=11.4 buy_ready=False sector_rank=7 price=26.91 support=23.7 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=70.34 liquidity=1591717.25 spike=0.4
- DSCW.CA: score=13.42 buy_ready=False sector_rank=10 price=1.73 support=1.71 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=36.11 liquidity=11140353.0 spike=0.32
- DTPP.CA: score=9.42 buy_ready=False sector_rank=10 price=166.05 support=153.55 resistance=166.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31808928.0 spike=15.81
- EALR.CA: score=-0.19 buy_ready=False sector_rank=10 price=342.52 support=332.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=25.74 liquidity=386455.5 spike=0.12
- EASB.CA: score=11.07 buy_ready=False sector_rank=10 price=7.5 support=4.66 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=75.15 liquidity=4647521.5 spike=0.36
- EAST.CA: score=7.81 buy_ready=False sector_rank=7 price=36.93 support=36.86 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=31.93 liquidity=9006689.0 spike=0.24
- EBSC.CA: score=4.84 buy_ready=False sector_rank=10 price=1.75 support=1.69 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:28 AM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=412844.09 spike=0.15
- ECAP.CA: score=11.43 buy_ready=False sector_rank=10 price=32.13 support=29.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:28 AM market time freshness=DELAYED_CURRENT RSI=54.65 liquidity=2001709.0 spike=0.22
- EDFM.CA: score=-0.32 buy_ready=False sector_rank=10 price=330.59 support=320.29 resistance=355.0 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=30.71 liquidity=253893.12 spike=0.52
- EEII.CA: score=11.87 buy_ready=False sector_rank=10 price=2.41 support=2.3 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=4449620.0 spike=0.34
- EFIC.CA: score=-1.93 buy_ready=False sector_rank=20 price=189.46 support=189.01 resistance=212.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=6.38 liquidity=937360.75 spike=0.48
- EFID.CA: score=14.17 buy_ready=False sector_rank=7 price=27.17 support=25.5 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=41.64 liquidity=9362520.0 spike=0.12
- EFIH.CA: score=8.49 buy_ready=False sector_rank=21 price=20.63 support=20.0 resistance=22.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=36.37 liquidity=5701988.0 spike=0.13
- EGAL.CA: score=8.14 buy_ready=False sector_rank=20 price=285.04 support=272.28 resistance=334.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=10.71 liquidity=27729212.0 spike=0.44
- EGAS.CA: score=9.13 buy_ready=False sector_rank=16 price=49.44 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=44.48 liquidity=2116177.25 spike=0.23
- EGBE.CA: score=9.43 buy_ready=False sector_rank=12 price=0.45 support=0.43 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=28574.37 spike=0.33
- EGCH.CA: score=8.14 buy_ready=False sector_rank=20 price=12.22 support=12.13 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=19.35 liquidity=15818323.0 spike=0.3
- EGSA.CA: score=7.19 buy_ready=False sector_rank=14 price=8.75 support=8.55 resistance=9.1 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=42.86 liquidity=5801.25 spike=0.62
- EGTS.CA: score=12.42 buy_ready=False sector_rank=11 price=17.33 support=15.1 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=29.08 liquidity=15965005.0 spike=0.18
- EHDR.CA: score=12.42 buy_ready=False sector_rank=10 price=2.5 support=2.32 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=26.74 liquidity=12707455.0 spike=0.22
- EKHO.CA: score=6.02 buy_ready=False sector_rank=16 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=7.55 buy_ready=False sector_rank=19 price=2.08 support=2.05 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=32.14 liquidity=14918477.0 spike=0.78
- ELKA.CA: score=5.26 buy_ready=False sector_rank=10 price=1.34 support=1.21 resistance=1.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=57580000.0 spike=1.42
- ELNA.CA: score=-1.03 buy_ready=False sector_rank=10 price=37.81 support=35.55 resistance=41.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:26 AM market time freshness=DELAYED_CURRENT RSI=33.43 liquidity=469579.34 spike=1.04
- ELSH.CA: score=17.42 buy_ready=False sector_rank=10 price=11.77 support=9.33 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=38.89 liquidity=51277272.0 spike=0.27
- ELWA.CA: score=3.22 buy_ready=False sector_rank=10 price=2.0 support=1.95 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=31.91 liquidity=791203.19 spike=0.26
- EMFD.CA: score=17.42 buy_ready=False sector_rank=11 price=11.55 support=11.11 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=41.0 liquidity=45967616.0 spike=0.16
- ENGC.CA: score=16.28 buy_ready=False sector_rank=10 price=36.88 support=33.0 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=56.36 liquidity=4854907.0 spike=0.33
- EOSB.CA: score=11.46 buy_ready=False sector_rank=10 price=1.48 support=1.39 resistance=1.55 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=36743.96 spike=0.28
- EPCO.CA: score=0.46 buy_ready=False sector_rank=10 price=8.76 support=8.5 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=28.31 liquidity=1039957.5 spike=0.12
- EPPK.CA: score=17.98 buy_ready=False sector_rank=10 price=13.67 support=11.67 resistance=13.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=70.53 liquidity=3771574.25 spike=3.39
- ETEL.CA: score=14.18 buy_ready=False sector_rank=14 price=93.11 support=89.01 resistance=97.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=35.42 liquidity=38895624.0 spike=0.55
- ETRS.CA: score=5.86 buy_ready=False sector_rank=10 price=10.89 support=10.75 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=127184528.0 spike=1.72
- EXPA.CA: score=3.57 buy_ready=False sector_rank=12 price=18.29 support=18.03 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=27.33 liquidity=4165453.5 spike=0.13
- FAIT.CA: score=19.36 buy_ready=False sector_rank=12 price=37.02 support=35.01 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=43.7 liquidity=7042636.5 spike=2.46
- FAITA.CA: score=4.41 buy_ready=False sector_rank=12 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT RSI=38.71 liquidity=12373.96 spike=0.31
- FERC.CA: score=0.16 buy_ready=False sector_rank=20 price=73.0 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=12.94 liquidity=3027602.5 spike=0.79
- FWRY.CA: score=12.79 buy_ready=False sector_rank=21 price=18.57 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=42.96 liquidity=101600336.0 spike=0.41
- GBCO.CA: score=20.4 buy_ready=False sector_rank=2 price=31.96 support=25.25 resistance=32.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=83.43 liquidity=70355648.0 spike=0.77
- GDWA.CA: score=8.42 buy_ready=False sector_rank=10 price=0.76 support=0.76 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=10349176.0 spike=0.74
- GGCC.CA: score=21.58 buy_ready=False sector_rank=10 price=0.48 support=0.4 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=67.68 liquidity=17983878.0 spike=1.58
- GIHD.CA: score=20.08 buy_ready=False sector_rank=10 price=42.5 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=46.44 liquidity=10891390.0 spike=1.33
- GMCI.CA: score=16.09 buy_ready=False sector_rank=10 price=1.81 support=1.66 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:11 AM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=1664243.25 spike=4.15
- GRCA.CA: score=4.74 buy_ready=False sector_rank=10 price=51.91 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=42.98 liquidity=313790.56 spike=0.07
- GSSC.CA: score=0.46 buy_ready=False sector_rank=10 price=243.83 support=228.1 resistance=257.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=23.83 liquidity=1039300.0 spike=0.35
- GTWL.CA: score=9.42 buy_ready=False sector_rank=10 price=88.2 support=76.25 resistance=88.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=125889848.0 spike=5.04
- HDBK.CA: score=19.6 buy_ready=False sector_rank=12 price=159.66 support=138.0 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=66.54 liquidity=31293366.0 spike=1.1
- HELI.CA: score=17.42 buy_ready=False sector_rank=11 price=6.46 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=30435052.0 spike=0.26
- HRHO.CA: score=13.26 buy_ready=False sector_rank=13 price=26.6 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=27484138.0 spike=0.2
- ICID.CA: score=20.01 buy_ready=False sector_rank=10 price=7.89 support=5.24 resistance=8.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=61.75 liquidity=8586736.0 spike=0.51
- IDRE.CA: score=4.65 buy_ready=False sector_rank=10 price=42.5 support=41.1 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=33.22 liquidity=2227440.75 spike=0.17
- IFAP.CA: score=3.49 buy_ready=False sector_rank=18 price=19.09 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=40.08 liquidity=697855.0 spike=0.1
- INFI.CA: score=-0.15 buy_ready=False sector_rank=10 price=90.54 support=88.51 resistance=105.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=9.75 liquidity=1430522.25 spike=0.23
- IRON.CA: score=11.42 buy_ready=False sector_rank=20 price=33.03 support=30.51 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=48.72 liquidity=7280265.0 spike=0.95
- ISMA.CA: score=7.96 buy_ready=False sector_rank=10 price=28.69 support=25.99 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=33.55 liquidity=5533742.0 spike=0.15
- ISMQ.CA: score=20.14 buy_ready=False sector_rank=20 price=9.24 support=7.56 resistance=9.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=68.24 liquidity=51395024.0 spike=0.45
- ISPH.CA: score=17.82 buy_ready=False sector_rank=6 price=11.66 support=11.2 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=36.75 liquidity=25716830.0 spike=0.23
- JUFO.CA: score=14.99 buy_ready=False sector_rank=7 price=29.96 support=28.5 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=39.34 liquidity=7186423.0 spike=0.23
- KABO.CA: score=16.08 buy_ready=False sector_rank=5 price=6.3 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=42.25 liquidity=6191727.5 spike=0.38
- KWIN.CA: score=8.9 buy_ready=False sector_rank=10 price=67.84 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=5476791.5 spike=0.47
- KZPC.CA: score=-0.03 buy_ready=False sector_rank=10 price=8.5 support=8.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=12.29 liquidity=1549119.25 spike=0.25
- LCSW.CA: score=21.02 buy_ready=False sector_rank=15 price=27.86 support=26.0 resistance=31.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=53.11 liquidity=22862224.0 spike=0.79
- LUTS.CA: score=19.42 buy_ready=False sector_rank=10 price=0.74 support=0.56 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=64.74 liquidity=18519866.0 spike=0.4
- MAAL.CA: score=15.75 buy_ready=False sector_rank=10 price=7.2 support=5.25 resistance=7.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=77.89 liquidity=7326743.5 spike=0.41
- MASR.CA: score=21.38 buy_ready=False sector_rank=10 price=7.38 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=55.61 liquidity=113792672.0 spike=1.98
- MBSC.CA: score=9.02 buy_ready=False sector_rank=15 price=240.5 support=222.66 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=14.67 liquidity=13132062.0 spike=0.39
- MCQE.CA: score=7.66 buy_ready=False sector_rank=15 price=172.24 support=166.66 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=24.62 liquidity=8647491.0 spike=0.61
- MCRO.CA: score=8.42 buy_ready=False sector_rank=10 price=1.21 support=1.17 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=23247358.0 spike=0.67
- MENA.CA: score=10.6 buy_ready=False sector_rank=11 price=6.79 support=6.32 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=52.69 liquidity=1182176.5 spike=0.09
- MEPA.CA: score=2.77 buy_ready=False sector_rank=10 price=1.57 support=1.52 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=17.24 liquidity=4350899.0 spike=0.38
- MFPC.CA: score=8.14 buy_ready=False sector_rank=20 price=35.2 support=34.22 resistance=43.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=9.0 liquidity=25002374.0 spike=0.29
- MFSC.CA: score=9.31 buy_ready=False sector_rank=10 price=46.93 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=51.33 liquidity=1884112.0 spike=0.22
- MHOT.CA: score=24.02 buy_ready=False sector_rank=1 price=33.95 support=28.83 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=63.86 liquidity=7624904.0 spike=0.37
- MICH.CA: score=9.89 buy_ready=False sector_rank=10 price=36.59 support=34.0 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=45.35 liquidity=2462061.5 spike=0.16
- MILS.CA: score=2.6 buy_ready=False sector_rank=10 price=129.69 support=126.5 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=29.31 liquidity=3171940.0 spike=0.34
- MIPH.CA: score=6.19 buy_ready=False sector_rank=6 price=651.64 support=630.13 resistance=710.0 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=46.04 liquidity=1373657.15 spike=0.84
- MOED.CA: score=2.09 buy_ready=False sector_rank=10 price=0.68 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=34.35 liquidity=3663691.25 spike=0.4
- MOIL.CA: score=7.06 buy_ready=False sector_rank=16 price=0.47 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=36.21 liquidity=45818.15 spike=0.23
- MOIN.CA: score=3.52 buy_ready=False sector_rank=10 price=23.96 support=22.6 resistance=25.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=2058514.25 spike=2.52
- MOSC.CA: score=11.26 buy_ready=False sector_rank=10 price=279.18 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=56.3 liquidity=1836989.88 spike=0.2
- MPCI.CA: score=19.42 buy_ready=False sector_rank=10 price=238.17 support=204.36 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=54.8 liquidity=23309918.0 spike=0.24
- MPCO.CA: score=16.79 buy_ready=False sector_rank=18 price=1.8 support=1.6 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=44.78 liquidity=35712504.0 spike=0.34
- MPRC.CA: score=14.82 buy_ready=False sector_rank=10 price=38.73 support=31.15 resistance=40.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=77.97 liquidity=8399519.0 spike=0.19
- MTIE.CA: score=17.19 buy_ready=False sector_rank=2 price=9.03 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=42.65 liquidity=5787068.0 spike=0.36
- NAHO.CA: score=5.44 buy_ready=False sector_rank=10 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=15889.68 spike=0.44
- NCCW.CA: score=8.51 buy_ready=False sector_rank=10 price=6.13 support=5.29 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=28.48 liquidity=6085248.0 spike=0.18
- NEDA.CA: score=-0.48 buy_ready=False sector_rank=10 price=2.74 support=2.68 resistance=2.84 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=33.33 liquidity=92390.06 spike=0.25
- NHPS.CA: score=9.42 buy_ready=False sector_rank=10 price=68.14 support=62.1 resistance=71.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18543706.0 spike=5.33
- NINH.CA: score=23.42 buy_ready=False sector_rank=10 price=17.97 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=50.18 liquidity=17319666.0 spike=4.13
- NIPH.CA: score=17.82 buy_ready=False sector_rank=6 price=162.14 support=157.01 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=42.84 liquidity=14078030.0 spike=0.2
- OBRI.CA: score=9.56 buy_ready=False sector_rank=10 price=32.82 support=31.5 resistance=37.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=30.98 liquidity=15115558.0 spike=1.07
- OCDI.CA: score=19.42 buy_ready=False sector_rank=11 price=24.52 support=20.0 resistance=25.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=66.71 liquidity=13746561.0 spike=0.18
- OCPH.CA: score=13.13 buy_ready=False sector_rank=10 price=356.45 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=41.47 liquidity=3701182.0 spike=0.59
- ODIN.CA: score=11.49 buy_ready=False sector_rank=10 price=2.1 support=1.94 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=38.3 liquidity=4064089.75 spike=0.37
- OFH.CA: score=3.78 buy_ready=False sector_rank=10 price=0.59 support=0.57 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=22.09 liquidity=5352123.0 spike=0.28
- OIH.CA: score=17.8 buy_ready=False sector_rank=17 price=1.41 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=24522470.0 spike=0.32
- OLFI.CA: score=19.81 buy_ready=False sector_rank=7 price=22.2 support=21.0 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=53.18 liquidity=19034866.0 spike=0.92
- ORAS.CA: score=4.6 buy_ready=False sector_rank=8 price=725.08 support=704.52 resistance=728.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=129377864.0 spike=1.0
- ORHD.CA: score=19.42 buy_ready=False sector_rank=11 price=38.09 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=53.68 liquidity=95024568.0 spike=0.56
- ORWE.CA: score=7.01 buy_ready=False sector_rank=5 price=22.39 support=21.95 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=19.64 liquidity=7128711.0 spike=0.2
- PHAR.CA: score=20.24 buy_ready=False sector_rank=6 price=87.53 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=43.72 liquidity=41190516.0 spike=1.21
- PHDC.CA: score=17.42 buy_ready=False sector_rank=11 price=14.66 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=44.1 liquidity=108622912.0 spike=0.27
- PHTV.CA: score=9.76 buy_ready=False sector_rank=10 price=269.83 support=201.55 resistance=275.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=90.82 liquidity=1336075.25 spike=0.09
- POUL.CA: score=17.27 buy_ready=False sector_rank=7 price=37.67 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=52.46 liquidity=5460417.5 spike=0.15
- PRCL.CA: score=19.02 buy_ready=False sector_rank=15 price=30.91 support=22.86 resistance=32.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=68.92 liquidity=32416810.0 spike=0.8
- PRDC.CA: score=17.42 buy_ready=False sector_rank=11 price=7.41 support=5.86 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=65.55 liquidity=24990182.0 spike=0.21
- PRMH.CA: score=12.35 buy_ready=False sector_rank=10 price=2.49 support=2.28 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=38.26 liquidity=4921409.0 spike=0.16
- RACC.CA: score=6.94 buy_ready=False sector_rank=10 price=9.68 support=9.36 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=36.84 liquidity=2519181.0 spike=0.27
- RAKT.CA: score=-0.99 buy_ready=False sector_rank=10 price=21.8 support=21.96 resistance=24.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=30.46 liquidity=322886.81 spike=1.13
- RAYA.CA: score=23.58 buy_ready=False sector_rank=3 price=7.62 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=46.49 liquidity=133355024.0 spike=1.59
- RMDA.CA: score=9.03 buy_ready=False sector_rank=6 price=4.98 support=4.81 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=30.3 liquidity=6211092.0 spike=0.08
- ROTO.CA: score=19.42 buy_ready=False sector_rank=10 price=41.01 support=33.0 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=66.01 liquidity=13853046.0 spike=0.48
- RREI.CA: score=9.86 buy_ready=False sector_rank=10 price=3.49 support=3.34 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=41.1 liquidity=5437409.0 spike=0.32
- RTVC.CA: score=4.64 buy_ready=False sector_rank=10 price=3.8 support=3.55 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=21.43 liquidity=5198169.5 spike=1.01
- RUBX.CA: score=21.42 buy_ready=False sector_rank=10 price=11.07 support=9.8 resistance=12.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=61.35 liquidity=16589948.0 spike=0.92
- SAUD.CA: score=2.56 buy_ready=False sector_rank=12 price=20.86 support=19.99 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=27.42 liquidity=3160226.5 spike=0.38
- SCEM.CA: score=9.56 buy_ready=False sector_rank=15 price=62.58 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=38.22 liquidity=5541834.5 spike=0.32
- SCFM.CA: score=0.71 buy_ready=False sector_rank=10 price=242.98 support=226.5 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=27.28 liquidity=1285874.0 spike=0.28
- SCTS.CA: score=0.59 buy_ready=False sector_rank=9 price=556.0 support=540.0 resistance=630.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=3.24 liquidity=1146004.0 spike=0.37
- SDTI.CA: score=9.5 buy_ready=False sector_rank=10 price=45.88 support=44.17 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=38.33 liquidity=2078710.5 spike=0.18
- SEIG.CA: score=9.99 buy_ready=False sector_rank=10 price=187.9 support=180.0 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=36.97 liquidity=564789.25 spike=0.14
- SIPC.CA: score=3.9 buy_ready=False sector_rank=10 price=3.32 support=3.25 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=23.88 liquidity=4480798.5 spike=0.39
- SKPC.CA: score=4.42 buy_ready=False sector_rank=20 price=15.99 support=15.58 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=24.44 liquidity=7285262.5 spike=0.21
- SMFR.CA: score=-0.09 buy_ready=False sector_rank=10 price=190.82 support=187.01 resistance=214.0 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=27.39 liquidity=486591.02 spike=0.27
- SNFC.CA: score=7.52 buy_ready=False sector_rank=10 price=11.9 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=46.46 liquidity=3096114.5 spike=0.18
- SPIN.CA: score=13.18 buy_ready=False sector_rank=5 price=14.25 support=13.3 resistance=14.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=53.9 liquidity=1297653.13 spike=0.21
- SPMD.CA: score=12.58 buy_ready=False sector_rank=10 price=0.42 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=5151738.0 spike=0.21
- SUGR.CA: score=3.82 buy_ready=False sector_rank=7 price=46.72 support=45.31 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=15.05 liquidity=5008015.5 spike=0.68
- SVCE.CA: score=15.35 buy_ready=False sector_rank=10 price=9.04 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=53.31 liquidity=5929876.5 spike=0.09
- SWDY.CA: score=10.85 buy_ready=False sector_rank=19 price=85.97 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=38.97 liquidity=7302935.5 spike=0.42
- TALM.CA: score=1.01 buy_ready=False sector_rank=9 price=15.66 support=15.38 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=28.89 liquidity=1572958.63 spike=0.22
- TMGH.CA: score=14.42 buy_ready=False sector_rank=11 price=94.05 support=92.1 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=37.8 liquidity=170402736.0 spike=0.46
- TRTO.CA: score=5.42 buy_ready=False sector_rank=10 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=235.59 spike=0.33
- UEFM.CA: score=7.55 buy_ready=False sector_rank=10 price=470.0 support=460.0 resistance=505.0 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=47.13 liquidity=1309420.0 spike=1.41
- UEGC.CA: score=16.03 buy_ready=False sector_rank=10 price=1.4 support=1.33 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=8605563.0 spike=0.36
- UNIP.CA: score=9.77 buy_ready=False sector_rank=10 price=0.32 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=49.41 liquidity=2345885.25 spike=0.1
- UNIT.CA: score=0.1 buy_ready=False sector_rank=11 price=13.14 support=12.66 resistance=13.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5681162.5 spike=0.91
- WCDF.CA: score=5.54 buy_ready=False sector_rank=10 price=518.05 support=450.0 resistance=547.9 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=38.07 liquidity=396308.24 spike=1.36
- WKOL.CA: score=-0.16 buy_ready=False sector_rank=10 price=279.09 support=273.1 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=17.3 liquidity=418548.22 spike=0.15
- ZEOT.CA: score=19.42 buy_ready=False sector_rank=10 price=10.95 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=66.72 liquidity=16888380.0 spike=0.55
- ZMID.CA: score=19.42 buy_ready=False sector_rank=11 price=6.32 support=5.96 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=42.03 liquidity=41971204.0 spike=0.2

## Backtesting Lite
- CSAG.CA: 180d return=13.61%, max drawdown=-28.0%, MA20>MA50 days last20=20, as_of=2026-06-28T21:00:00+00:00
- MHOT.CA: 180d return=39.65%, max drawdown=-15.7%, MA20>MA50 days last20=20, as_of=2026-06-28T21:00:00+00:00
- RAYA.CA: 180d return=153.47%, max drawdown=-12.86%, MA20>MA50 days last20=20, as_of=2026-06-28T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CSAG.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Canal Shipping Agencies summary=Canal Shipping Agencies targets EGP 970m net profits in FY26/27; Canal Shipping Agencies’ stock rebounds; Canal Shipping Agencies mulls EGP 100m capital raise
  - Canal Shipping Agencies targets EGP 970m net profits in FY26/27: https://english.mubasher.info/news/4582423/Canal-Shipping-Agencies-targets-EGP-970m-net-profits-in-FY26-27/
  - Canal Shipping Agencies’ stock rebounds: https://english.mubasher.info/news/4564447/Canal-Shipping-Agencies-stock-rebounds/
  - Canal Shipping Agencies mulls EGP 100m capital raise: https://english.mubasher.info/news/4191441/Canal-Shipping-Agencies-mulls-EGP-100m-capital-raise/
- MHOT.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Hotels summary=Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26; Shareholder buys EGP 3.39m worth of shares in Misr Hotels; Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits
  - Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26: https://english.mubasher.info/news/4602482/Misr-Hotels-net-profits-cross-EGP-1-1bn-in-9M-25-26/
  - Shareholder buys EGP 3.39m worth of shares in Misr Hotels: https://english.mubasher.info/news/4013808/Shareholder-buys-EGP-3-39m-worth-of-shares-in-Misr-Hotels/
  - Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits: https://english.mubasher.info/news/3975543/Misr-Hotels-repays-EGP-383m-of-NBE-s-loan-unveils-estimated-profits/
- RAYA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=545 sources=3 expected=Raya Holding summary=Raya stock maintains bullish momentum above EGP 9; Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt; Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn
  - Raya stock maintains bullish momentum above EGP 9: https://english.mubasher.info/news/4601857/Raya-stock-maintains-bullish-momentum-above-EGP-9/
  - Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt: https://english.mubasher.info/news/4577815/Aman-Holding-MSMEDA-partner-to-inject-EGP-300m-into-SMEs-across-Egypt/
  - Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn: https://english.mubasher.info/news/4564195/Raya-Holding-s-consolidated-profits-surge-in-2025-revenues-hit-EGP-63-8bn/
- NINH.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=545 sources=3 expected=Nozha International Hospital summary=Nozha International Hospital’s net profits cross EGP 174m in 2025; Nozha International Hospital unveils EGP 58m capital increase, new asset details; Nozha International Hospital registers EGP 11.3m block trading
  - Nozha International Hospital’s net profits cross EGP 174m in 2025: https://english.mubasher.info/news/4558517/Nozha-International-Hospital-s-net-profits-cross-EGP-174m-in-2025/
  - Nozha International Hospital unveils EGP 58m capital increase, new asset details: https://english.mubasher.info/news/4558456/Nozha-International-Hospital-unveils-EGP-58m-capital-increase-new-asset-details/
  - Nozha International Hospital registers EGP 11.3m block trading: https://english.mubasher.info/news/4056645/Nozha-International-Hospital-registers-EGP-11-3m-block-trading/
- CAED.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Educational Services SAE summary=Cairo Educational Services&#39; OGM approves EGP 1/shr coupon distribution; Cairo Educational Services’ board proposes 80 piastres per-share dividends; Cairo Educational Services’ profit declines in FY18/19
  - Cairo Educational Services&#39; OGM approves EGP 1/shr coupon distribution: https://english.mubasher.info/news/3884789/Cairo-Educational-Services-OGM-approves-EGP-1-shr-coupon-distribution/
  - Cairo Educational Services’ board proposes 80 piastres per-share dividends: https://english.mubasher.info/news/3556129/Cairo-Educational-Services-board-proposes-80-piastres-per-share-dividends/
  - Cairo Educational Services’ profit declines in FY18/19: https://english.mubasher.info/news/3556119/Cairo-Educational-Services-profit-declines-in-FY18-19/
- GGCC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Giza General - Contracting and Real Estate Investment S.A.E summary=EGX approves listing EGP 144m capital increase for Giza Contracting; Giza Contracting tests key EGP 0.51 level; Giza Contracting’s consolidated net profits leap to EGP 140m in 9M-25
  - EGX approves listing EGP 144m capital increase for Giza Contracting: https://english.mubasher.info/news/4588793/EGX-approves-listing-EGP-144m-capital-increase-for-Giza-Contracting/
  - Giza Contracting tests key EGP 0.51 level: https://english.mubasher.info/news/4563778/Giza-Contracting-tests-key-EGP-0-51-level/
  - Giza Contracting’s consolidated net profits leap to EGP 140m in 9M-25: https://english.mubasher.info/news/4530408/Giza-Contracting-s-consolidated-net-profits-leap-to-EGP-140m-in-9M-25/
- RUBX.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Rubex International for Plastic and Acrylic Manufacturing summary=Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- MASR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=545 sources=3 expected=Madinet Masr For Housing and Development summary=Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval; Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended; Madinet Masr to distribute treasury stocks in first-ever move
  - Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval: https://english.mubasher.info/news/4601386/Madinet-Masr-to-pay-out-EGP-0-15-shr-for-2025-upon-equityholders-approval/
  - Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended: https://english.mubasher.info/news/4578449/Madinet-Masr-logs-24-higher-consolidated-profits-in-2025-dividends-recommended/
  - Madinet Masr to distribute treasury stocks in first-ever move: https://english.mubasher.info/news/4577724/Madinet-Masr-to-distribute-treasury-stocks-in-first-ever-move/

## Warnings
- Evidence for CSAG.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for MHOT.CA matches the company but no source/report date was detected.
- Evidence for RAYA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for NINH.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CAED.CA matches the company but no source/report date was detected.
- Evidence for GGCC.CA matches the company but no source/report date was detected.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Evidence for MASR.CA matches the company but appears old; latest detected date is 2025-01-01.
