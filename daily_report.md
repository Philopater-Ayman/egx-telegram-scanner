# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-06-25T10:41:06.158416+00:00
Generated Cairo: 2026-06-25 13:41
Run timing: target 11:00 Cairo | generated Cairo 2026-06-25 13:41 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-06-25 13:37

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 185/190
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, June 25
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 30.0% / above MA50 40.0%
- EGX70 regime: BEARISH / above MA20 38.46% / above MA50 69.23%
- Sector breadth: 38.1%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=601518208.0 spike=0.86 score=14.81
- ORAS.CA: liquidity=410625600.0 spike=1.0 score=4.6
- HRHO.CA: liquidity=363422432.0 spike=1.0 score=21.2
- BTFH.CA: liquidity=206293104.0 spike=1.08 score=15.36
- TMGH.CA: liquidity=205239024.0 spike=0.42 score=15.43

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The local EGX scanner stays on HOLD because both EGX30 and EGX70 are in a bearish regime with weak breadth (≈38%). Risk mode is DEFENSIVE_NO_NEW_BUY, meaning the market does not support initiating fresh long positions for the next 1‑3 days. The top‑ranked tickets show bullish watch signals and strong liquidity spikes, but they sit in non‑leading sectors and are far from key support levels, so they remain on hold until the broader market outlook improves.
- EGX30/EGX70 trends bearish; median 5‑day returns negative, breadth below MA20/MA50.
- Risk mode DEFENSIVE_NO_NEW_BUY – no new buys allowed despite individual bullish outlooks.
- Top tickets (DAPH, ECAP, OCDI, etc.) show accumulation spikes but are in sectors not leading the market.
- Support levels are distant; resistance near or above current price, adding uncertainty.
- Sector outlook: Tourism & Leisure leads with strong returns, but overall market weakness dominates short‑term risk.

## Top Liquidity Spikes
- LCSW.CA: spike=14.89 liquidity=152455504.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GTWL.CA: spike=13.55 liquidity=125489016.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- KWIN.CA: spike=8.92 liquidity=58612288.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DAPH.CA: spike=7.37 liquidity=57494156.0 outlook=BULLISH_WATCH score=93.45 buy_ready=False
- ECAP.CA: spike=4.75 liquidity=31356230.0 outlook=BULLISH_WATCH score=71.45 buy_ready=False

## Sector Leaderboard
- #1 Tourism & Leisure: score=16.43 5d=17.17% 20d=14.38% aboveMA50=100.0%
- #2 Automotive & Distribution: score=8.69 5d=4.13% 20d=8.6% aboveMA50=100.0%
- #3 Healthcare: score=5.76 5d=1.61% 20d=3.32% aboveMA50=100.0%
- #4 Technology & Distribution: score=5.73 5d=5.56% 20d=-1.07% aboveMA50=100.0%
- #5 Education: score=5.65 5d=0.0% 20d=2.84% aboveMA50=66.67%
- #6 Non-bank Financial Services: score=5.5 5d=1.0% 20d=0.0% aboveMA50=80.0%
- #7 Agriculture & Food Production: score=4.84 5d=-2.46% 20d=6.22% aboveMA50=50.0%
- #8 Industrial Goods & Cables: score=3.86 5d=0.48% 20d=0.42% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- DAPH.CA: BULLISH_WATCH score=93.45 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CNFN.CA: BULLISH_WATCH score=90.5 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- PHAR.CA: BULLISH_WATCH score=85.76 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- CLHO.CA: BULLISH_WATCH score=84.76 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- POUL.CA: BULLISH_WATCH score=82.05 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- CIRA.CA: BULLISH_WATCH score=81.65 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended
- GIHD.CA: BULLISH_WATCH score=81.45 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support; sector is not leading
- CERA.CA: BULLISH_WATCH score=80.45 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- SVCE.CA: BULLISH_WATCH score=79.45 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- MHOT.CA: BULLISH_WATCH score=78 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended; far above support

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=10.02 buy_ready=False sector_rank=12 price=205.2 support=200.0 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=44.24 liquidity=1636910.88 spike=0.28
- ABUK.CA: score=8.74 buy_ready=False sector_rank=21 price=68.66 support=68.01 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=12.81 liquidity=51491904.0 spike=0.38
- ACAMD.CA: score=18.38 buy_ready=False sector_rank=12 price=2.2 support=2.17 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=33613216.0 spike=0.26
- ACGC.CA: score=17.78 buy_ready=False sector_rank=18 price=9.46 support=9.11 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=38.39 liquidity=18486316.0 spike=0.32
- ADCI.CA: score=14.55 buy_ready=False sector_rank=12 price=238.01 support=211.0 resistance=243.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=92.86 liquidity=5167359.5 spike=0.59
- ADIB.CA: score=15.2 buy_ready=False sector_rank=14 price=44.88 support=44.01 resistance=48.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=40.29 liquidity=49829060.0 spike=0.5
- ADPC.CA: score=18.26 buy_ready=False sector_rank=12 price=3.5 support=3.45 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=42.42 liquidity=32482614.0 spike=1.44
- AFDI.CA: score=20.55 buy_ready=False sector_rank=12 price=45.49 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=57.85 liquidity=6173806.5 spike=0.42
- AFMC.CA: score=6.42 buy_ready=False sector_rank=12 price=70.56 support=67.0 resistance=74.69 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=37.62 liquidity=1042453.4 spike=0.62
- AJWA.CA: score=14.66 buy_ready=False sector_rank=12 price=174.74 support=131.5 resistance=188.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=83.33 liquidity=7281982.0 spike=0.27
- ALCN.CA: score=11.59 buy_ready=False sector_rank=9 price=27.82 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=35.28 liquidity=6044962.5 spike=0.46
- ALUM.CA: score=7.6 buy_ready=False sector_rank=12 price=21.56 support=22.35 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=27.36 liquidity=7219383.5 spike=0.71
- AMER.CA: score=10.43 buy_ready=False sector_rank=11 price=2.38 support=2.35 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=31.87 liquidity=15443846.0 spike=0.19
- AMES.CA: score=6.39 buy_ready=False sector_rank=12 price=48.3 support=48.0 resistance=53.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=36.42 liquidity=2008344.25 spike=0.62
- AMIA.CA: score=14.58 buy_ready=False sector_rank=12 price=8.68 support=8.55 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=41.84 liquidity=6197261.0 spike=0.45
- AMOC.CA: score=10.47 buy_ready=False sector_rank=10 price=7.6 support=7.58 resistance=8.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=20.72 liquidity=20349610.0 spike=0.39
- ANFI.CA: score=15.71 buy_ready=False sector_rank=12 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=0.44 buy_ready=False sector_rank=12 price=8.48 support=8.24 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=12.9 liquidity=882156.31 spike=1.09
- ARAB.CA: score=14.43 buy_ready=False sector_rank=11 price=0.2 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=47.06 liquidity=27597170.0 spike=0.33
- ARCC.CA: score=13.01 buy_ready=False sector_rank=15 price=55.48 support=53.0 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=33.77 liquidity=12086416.0 spike=0.35
- AREH.CA: score=20.52 buy_ready=False sector_rank=12 price=1.6 support=1.32 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=69.09 liquidity=34528328.0 spike=1.07
- ARVA.CA: score=13.86 buy_ready=False sector_rank=12 price=11.2 support=8.08 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=56.07 liquidity=3482633.5 spike=0.11
- ASCM.CA: score=22.38 buy_ready=False sector_rank=12 price=60.81 support=47.49 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=61.76 liquidity=45703300.0 spike=0.51
- ASPI.CA: score=13.38 buy_ready=False sector_rank=12 price=0.32 support=0.26 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=30.0 liquidity=14578622.0 spike=0.21
- ATLC.CA: score=16.37 buy_ready=False sector_rank=6 price=5.02 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=56.08 liquidity=5170954.0 spike=0.88
- ATQA.CA: score=13.58 buy_ready=False sector_rank=21 price=9.54 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=36.0 liquidity=44309320.0 spike=1.42
- AXPH.CA: score=9.52 buy_ready=False sector_rank=12 price=1100.36 support=1073.0 resistance=1174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=44.06 liquidity=1139950.13 spike=0.73
- BINV.CA: score=10.5 buy_ready=False sector_rank=17 price=47.22 support=42.97 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=56.07 liquidity=696786.19 spike=0.07
- BIOC.CA: score=11.9 buy_ready=False sector_rank=12 price=72.87 support=68.34 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=37.74 liquidity=1519894.0 spike=0.66
- BTFH.CA: score=15.36 buy_ready=False sector_rank=6 price=3.0 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=43.84 liquidity=206293104.0 spike=1.08
- CAED.CA: score=16.17 buy_ready=False sector_rank=12 price=70.1 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=47.44 liquidity=7053250.0 spike=1.37
- CANA.CA: score=17.56 buy_ready=False sector_rank=14 price=35.96 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=50.55 liquidity=11885924.0 spike=1.18
- CCAP.CA: score=14.81 buy_ready=False sector_rank=17 price=4.89 support=4.92 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=38.62 liquidity=601518208.0 spike=0.86
- CCRS.CA: score=18.38 buy_ready=False sector_rank=12 price=2.38 support=2.32 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=41.79 liquidity=13520485.0 spike=0.73
- CEFM.CA: score=1.14 buy_ready=False sector_rank=12 price=101.44 support=100.27 resistance=109.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=30.83 liquidity=762392.69 spike=0.36
- CERA.CA: score=24.02 buy_ready=False sector_rank=12 price=1.25 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=61.54 liquidity=35034272.0 spike=2.32
- CFGH.CA: score=-0.62 buy_ready=False sector_rank=12 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=1858.4 spike=0.32
- CICH.CA: score=13.21 buy_ready=False sector_rank=6 price=11.99 support=11.1 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=44.19 liquidity=2008095.13 spike=0.62
- CIEB.CA: score=15.6 buy_ready=False sector_rank=14 price=23.95 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=56.49 liquidity=3396942.25 spike=0.52
- CIRA.CA: score=25.26 buy_ready=False sector_rank=5 price=28.22 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=63.7 liquidity=12996083.0 spike=0.72
- CLHO.CA: score=24.3 buy_ready=False sector_rank=3 price=16.61 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=65.46 liquidity=32515712.0 spike=0.91
- CNFN.CA: score=24.92 buy_ready=False sector_rank=6 price=4.85 support=4.36 resistance=5.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=69151992.0 spike=1.86
- COMI.CA: score=17.2 buy_ready=False sector_rank=14 price=132.19 support=129.8 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=49.01 liquidity=126194816.0 spike=0.21
- COPR.CA: score=17.38 buy_ready=False sector_rank=12 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=54.69 liquidity=11343294.0 spike=0.32
- COSG.CA: score=10.8 buy_ready=False sector_rank=12 price=1.53 support=1.53 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=29.73 liquidity=7423253.0 spike=0.13
- CPCI.CA: score=10.95 buy_ready=False sector_rank=12 price=377.4 support=347.11 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=72.1 liquidity=565112.0 spike=0.28
- CSAG.CA: score=22.36 buy_ready=False sector_rank=9 price=31.83 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=39.2 liquidity=21166638.0 spike=1.91
- DAPH.CA: score=29.38 buy_ready=False sector_rank=12 price=83.1 support=76.6 resistance=82.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=53.9 liquidity=57494156.0 spike=7.37
- DEIN.CA: score=6.38 buy_ready=False sector_rank=12 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=19.52 buy_ready=False sector_rank=13 price=27.0 support=23.7 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=73.9 liquidity=7143592.0 spike=2.08
- DSCW.CA: score=16.38 buy_ready=False sector_rank=12 price=1.76 support=1.74 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=38.24 liquidity=14733575.0 spike=0.3
- DTPP.CA: score=1.56 buy_ready=False sector_rank=12 price=117.3 support=114.0 resistance=130.89 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=18.44 liquidity=1122912.93 spike=1.03
- EALR.CA: score=7.21 buy_ready=False sector_rank=12 price=351.53 support=350.2 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=43.9 liquidity=1828037.13 spike=0.57
- EASB.CA: score=21.52 buy_ready=False sector_rank=12 price=8.23 support=4.66 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=84.31 liquidity=28653510.0 spike=3.07
- EAST.CA: score=14.22 buy_ready=False sector_rank=13 price=37.91 support=37.01 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=52.58 liquidity=10221503.0 spike=0.23
- EBSC.CA: score=4.0 buy_ready=False sector_rank=12 price=1.8 support=1.66 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=615824.38 spike=0.23
- ECAP.CA: score=27.38 buy_ready=False sector_rank=12 price=33.69 support=29.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=63.01 liquidity=31356230.0 spike=4.75
- EDFM.CA: score=0.69 buy_ready=False sector_rank=12 price=330.43 support=322.11 resistance=355.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=19.32 liquidity=313262.34 spike=0.52
- EEII.CA: score=18.31 buy_ready=False sector_rank=12 price=2.42 support=2.3 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=51.79 liquidity=7926475.5 spike=0.57
- EFIC.CA: score=-0.86 buy_ready=False sector_rank=21 price=194.94 support=192.01 resistance=213.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=17.89 liquidity=1392113.0 spike=0.71
- EFID.CA: score=10.22 buy_ready=False sector_rank=13 price=26.88 support=27.06 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=31.55 liquidity=31352658.0 spike=0.44
- EFIH.CA: score=11.65 buy_ready=False sector_rank=20 price=20.77 support=20.82 resistance=20.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=8509019.0 spike=1.0
- EGAL.CA: score=8.74 buy_ready=False sector_rank=21 price=281.57 support=282.5 resistance=334.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=10.26 liquidity=23465842.0 spike=0.31
- EGAS.CA: score=13.85 buy_ready=False sector_rank=10 price=49.99 support=48.2 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=64.85 liquidity=5373725.5 spike=0.5
- EGBE.CA: score=11.68 buy_ready=False sector_rank=14 price=0.46 support=0.43 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=46.0 liquidity=152881.92 spike=1.66
- EGCH.CA: score=8.74 buy_ready=False sector_rank=21 price=12.98 support=12.69 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=29.6 liquidity=28828290.0 spike=0.49
- EGSA.CA: score=3.04 buy_ready=False sector_rank=16 price=8.76 support=8.55 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=30.0 liquidity=15045.0 spike=1.07
- EGTS.CA: score=18.43 buy_ready=False sector_rank=11 price=17.38 support=17.25 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=37.09 liquidity=20581098.0 spike=0.19
- EHDR.CA: score=18.38 buy_ready=False sector_rank=12 price=2.54 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=45.92 liquidity=12024579.0 spike=0.21
- EKHO.CA: score=10.47 buy_ready=False sector_rank=10 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=14.13 buy_ready=False sector_rank=8 price=2.11 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=7584312.5 spike=0.36
- ELKA.CA: score=16.85 buy_ready=False sector_rank=12 price=1.24 support=1.15 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=9465923.0 spike=0.23
- ELNA.CA: score=5.5 buy_ready=False sector_rank=12 price=36.01 support=37.11 resistance=41.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=47.24 liquidity=557339.75 spike=1.28
- ELSH.CA: score=14.38 buy_ready=False sector_rank=12 price=11.8 support=11.87 resistance=11.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=34403840.0 spike=1.0
- ELWA.CA: score=9.38 buy_ready=False sector_rank=12 price=2.05 support=2.0 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=47.92 liquidity=1002281.69 spike=0.31
- EMFD.CA: score=18.43 buy_ready=False sector_rank=11 price=11.7 support=10.5 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=42.9 liquidity=83538216.0 spike=0.3
- ENGC.CA: score=16.2 buy_ready=False sector_rank=12 price=35.91 support=32.81 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=64.75 liquidity=3815555.25 spike=0.28
- EOSB.CA: score=12.45 buy_ready=False sector_rank=12 price=1.48 support=1.35 resistance=1.55 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=67810.64 spike=0.53
- EPCO.CA: score=7.43 buy_ready=False sector_rank=12 price=8.94 support=8.9 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=2048620.25 spike=0.22
- EPPK.CA: score=9.79 buy_ready=False sector_rank=12 price=12.48 support=11.67 resistance=13.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=54.94 liquidity=409486.53 spike=0.45
- ETEL.CA: score=14.89 buy_ready=False sector_rank=16 price=93.67 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=44.82 liquidity=23144410.0 spike=0.29
- ETRS.CA: score=5.42 buy_ready=False sector_rank=12 price=10.91 support=10.25 resistance=11.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=62232580.0 spike=1.02
- EXPA.CA: score=18.2 buy_ready=False sector_rank=14 price=18.45 support=18.2 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=45.78 liquidity=22488364.0 spike=0.69
- FAIT.CA: score=8.72 buy_ready=False sector_rank=14 price=36.18 support=35.01 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=35.99 liquidity=515453.47 spike=0.15
- FAITA.CA: score=8.23 buy_ready=False sector_rank=14 price=0.99 support=0.99 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:13 AM market time freshness=DELAYED_CURRENT RSI=37.84 liquidity=26425.41 spike=0.74
- FERC.CA: score=2.18 buy_ready=False sector_rank=21 price=75.36 support=75.0 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=23.73 liquidity=2433650.75 spike=0.63
- FWRY.CA: score=16.14 buy_ready=False sector_rank=20 price=18.77 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=43.3 liquidity=66252336.0 spike=0.25
- GBCO.CA: score=22.4 buy_ready=False sector_rank=2 price=31.08 support=25.25 resistance=31.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=85.89 liquidity=49928400.0 spike=0.52
- GDWA.CA: score=7.99 buy_ready=False sector_rank=12 price=0.78 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=38.58 liquidity=3609564.0 spike=0.26
- GGCC.CA: score=22.2 buy_ready=False sector_rank=12 price=0.43 support=0.4 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=11489821.0 spike=1.41
- GIHD.CA: score=26.12 buy_ready=False sector_rank=12 price=43.95 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=63.56 liquidity=13530424.0 spike=1.87
- GMCI.CA: score=-0.43 buy_ready=False sector_rank=12 price=1.71 support=1.66 resistance=1.84 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=33.33 liquidity=187734.06 spike=0.6
- GRCA.CA: score=1.63 buy_ready=False sector_rank=12 price=52.94 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=32.12 liquidity=1247976.25 spike=0.25
- GSSC.CA: score=8.98 buy_ready=False sector_rank=12 price=245.8 support=228.1 resistance=257.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=36.64 liquidity=1603105.13 spike=0.48
- GTWL.CA: score=10.38 buy_ready=False sector_rank=12 price=64.99 support=60.5 resistance=68.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=125489016.0 spike=13.55
- HDBK.CA: score=19.2 buy_ready=False sector_rank=14 price=162.45 support=138.0 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=82.54 liquidity=13632281.0 spike=0.52
- HELI.CA: score=18.43 buy_ready=False sector_rank=11 price=6.48 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=50.3 liquidity=85920152.0 spike=0.63
- HRHO.CA: score=21.2 buy_ready=False sector_rank=6 price=26.91 support=26.89 resistance=26.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=363422432.0 spike=1.0
- ICID.CA: score=11.5 buy_ready=False sector_rank=12 price=7.48 support=5.0 resistance=7.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=78.35 liquidity=2120921.75 spike=0.13
- IDRE.CA: score=14.49 buy_ready=False sector_rank=12 price=44.11 support=42.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=42.92 liquidity=6108063.0 spike=0.37
- IFAP.CA: score=16.76 buy_ready=False sector_rank=7 price=19.37 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=40.17 liquidity=11811527.0 spike=1.91
- INFI.CA: score=0.68 buy_ready=False sector_rank=12 price=93.42 support=93.0 resistance=105.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=16.44 liquidity=1300223.5 spike=0.16
- IRON.CA: score=2.38 buy_ready=False sector_rank=21 price=31.5 support=30.95 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=4638091.5 spike=0.58
- ISMA.CA: score=13.5 buy_ready=False sector_rank=12 price=29.47 support=25.95 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=71.59 liquidity=5119948.0 spike=0.13
- ISMQ.CA: score=22.86 buy_ready=False sector_rank=21 price=8.7 support=7.38 resistance=8.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=68.66 liquidity=182936752.0 spike=2.06
- ISPH.CA: score=20.3 buy_ready=False sector_rank=3 price=11.91 support=11.3 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=45.17 liquidity=48124896.0 spike=0.39
- JUFO.CA: score=16.68 buy_ready=False sector_rank=13 price=30.36 support=28.09 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=56.88 liquidity=4459614.5 spike=0.12
- KABO.CA: score=9.73 buy_ready=False sector_rank=18 price=6.16 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=35.9 liquidity=1950037.0 spike=0.11
- KWIN.CA: score=10.38 buy_ready=False sector_rank=12 price=71.25 support=68.25 resistance=75.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=58612288.0 spike=8.92
- KZPC.CA: score=9.67 buy_ready=False sector_rank=12 price=8.65 support=8.8 resistance=8.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=5292990.5 spike=1.0
- LCSW.CA: score=10.01 buy_ready=False sector_rank=15 price=30.24 support=27.34 resistance=31.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=152455504.0 spike=14.89
- LUTS.CA: score=19.9 buy_ready=False sector_rank=12 price=0.73 support=0.55 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=71.88 liquidity=9520970.0 spike=0.22
- MAAL.CA: score=12.6 buy_ready=False sector_rank=12 price=6.79 support=5.16 resistance=7.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=79.41 liquidity=3224376.75 spike=0.2
- MASR.CA: score=18.38 buy_ready=False sector_rank=12 price=6.95 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=54.29 liquidity=22267950.0 spike=0.4
- MBSC.CA: score=6.92 buy_ready=False sector_rank=15 price=242.95 support=242.2 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=33.82 liquidity=6910489.5 spike=0.17
- MCQE.CA: score=7.4 buy_ready=False sector_rank=15 price=168.4 support=171.0 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=19.54 liquidity=7390850.5 spike=0.47
- MCRO.CA: score=9.38 buy_ready=False sector_rank=12 price=1.21 support=1.2 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=15918072.0 spike=0.41
- MENA.CA: score=4.03 buy_ready=False sector_rank=11 price=6.71 support=6.22 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=32.08 liquidity=601830.5 spike=0.04
- MEPA.CA: score=7.43 buy_ready=False sector_rank=12 price=1.6 support=1.6 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=20.83 liquidity=8051665.5 spike=0.64
- MFPC.CA: score=8.74 buy_ready=False sector_rank=21 price=35.7 support=35.15 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=8.6 liquidity=35793640.0 spike=0.42
- MFSC.CA: score=14.37 buy_ready=False sector_rank=12 price=50.0 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=54.35 liquidity=3990590.5 spike=0.4
- MHOT.CA: score=24.4 buy_ready=False sector_rank=1 price=34.79 support=28.83 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=65.91 liquidity=12101648.0 spike=0.46
- MICH.CA: score=16.88 buy_ready=False sector_rank=12 price=37.74 support=35.4 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=64.57 liquidity=4496268.5 spike=0.3
- MILS.CA: score=9.81 buy_ready=False sector_rank=12 price=131.83 support=130.11 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=42.36 liquidity=1432834.13 spike=0.12
- MIPH.CA: score=11.42 buy_ready=False sector_rank=3 price=652.93 support=651.0 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=47.49 liquidity=1118651.0 spike=0.52
- MOED.CA: score=7.86 buy_ready=False sector_rank=12 price=0.68 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=41.94 liquidity=1484645.12 spike=0.14
- MOIL.CA: score=11.68 buy_ready=False sector_rank=10 price=0.48 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=249871.75 spike=1.48
- MOIN.CA: score=-0.14 buy_ready=False sector_rank=12 price=23.14 support=23.02 resistance=25.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=1.06 liquidity=482190.34 spike=0.33
- MOSC.CA: score=6.56 buy_ready=False sector_rank=12 price=261.93 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=44.89 liquidity=1181474.63 spike=0.14
- MPCI.CA: score=20.38 buy_ready=False sector_rank=12 price=237.01 support=204.36 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=66.3 liquidity=46046824.0 spike=0.49
- MPCO.CA: score=22.94 buy_ready=False sector_rank=7 price=1.84 support=1.58 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=51.52 liquidity=20358570.0 spike=0.2
- MPRC.CA: score=22.46 buy_ready=False sector_rank=12 price=37.0 support=31.1 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=73.84 liquidity=36371416.0 spike=1.04
- MTIE.CA: score=20.32 buy_ready=False sector_rank=2 price=9.02 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=45.99 liquidity=8921026.0 spike=0.56
- NAHO.CA: score=6.39 buy_ready=False sector_rank=12 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=12432.87 spike=0.37
- NCCW.CA: score=20.38 buy_ready=False sector_rank=12 price=6.14 support=5.29 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=56.8 liquidity=15243618.0 spike=0.48
- NEDA.CA: score=5.7 buy_ready=False sector_rank=12 price=2.74 support=2.68 resistance=2.84 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=42.31 liquidity=318344.16 spike=0.89
- NHPS.CA: score=13.75 buy_ready=False sector_rank=12 price=64.31 support=63.19 resistance=63.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=3369394.0 spike=1.0
- NINH.CA: score=10.14 buy_ready=False sector_rank=12 price=17.86 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=48.53 liquidity=2756363.25 spike=0.54
- NIPH.CA: score=20.3 buy_ready=False sector_rank=3 price=162.78 support=157.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=57.35 liquidity=15004416.0 spike=0.21
- OBRI.CA: score=11.14 buy_ready=False sector_rank=12 price=34.19 support=33.63 resistance=37.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=48.38 liquidity=5755596.0 spike=0.43
- OCDI.CA: score=27.05 buy_ready=False sector_rank=11 price=25.14 support=20.0 resistance=24.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=67.7 liquidity=169358544.0 spike=3.31
- OCPH.CA: score=10.53 buy_ready=False sector_rank=12 price=345.49 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=38.33 liquidity=5146959.5 spike=0.84
- ODIN.CA: score=15.23 buy_ready=False sector_rank=12 price=2.11 support=1.91 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=4851311.0 spike=0.45
- OFH.CA: score=9.38 buy_ready=False sector_rank=12 price=0.59 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=22.09 liquidity=10808451.0 spike=0.53
- OIH.CA: score=16.81 buy_ready=False sector_rank=17 price=1.4 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=48.48 liquidity=15431640.0 spike=0.18
- OLFI.CA: score=15.22 buy_ready=False sector_rank=13 price=21.69 support=21.39 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=54.79 liquidity=14040636.0 spike=0.7
- ORAS.CA: score=4.6 buy_ready=False sector_rank=19 price=748.6 support=741.01 resistance=795.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=410625600.0 spike=1.0
- ORHD.CA: score=20.43 buy_ready=False sector_rank=11 price=38.73 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=56.72 liquidity=38485880.0 spike=0.2
- ORWE.CA: score=17.58 buy_ready=False sector_rank=18 price=22.72 support=22.65 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=9793486.0 spike=0.26
- PHAR.CA: score=19.11 buy_ready=False sector_rank=3 price=87.03 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=52.04 liquidity=4801760.0 spike=0.13
- PHDC.CA: score=18.43 buy_ready=False sector_rank=11 price=15.17 support=14.43 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=53.64 liquidity=110532968.0 spike=0.27
- PHTV.CA: score=14.38 buy_ready=False sector_rank=12 price=250.39 support=201.55 resistance=256.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=87.78 liquidity=4999552.5 spike=0.25
- POUL.CA: score=23.49 buy_ready=False sector_rank=13 price=38.61 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=59.88 liquidity=9266476.0 spike=0.23
- PRCL.CA: score=21.11 buy_ready=False sector_rank=15 price=30.33 support=22.02 resistance=32.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=68.88 liquidity=56179720.0 spike=1.55
- PRDC.CA: score=22.43 buy_ready=False sector_rank=11 price=7.15 support=5.7 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=63.66 liquidity=51403888.0 spike=0.46
- PRMH.CA: score=18.38 buy_ready=False sector_rank=12 price=2.52 support=2.26 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=37.62 liquidity=11942218.0 spike=0.4
- RACC.CA: score=12.11 buy_ready=False sector_rank=12 price=9.83 support=9.38 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=41.58 liquidity=3726050.5 spike=0.39
- RAKT.CA: score=6.44 buy_ready=False sector_rank=12 price=23.11 support=22.0 resistance=24.1 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=37.86 liquidity=58537.63 spike=0.25
- RAYA.CA: score=19.29 buy_ready=False sector_rank=4 price=7.29 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=46.7 liquidity=42329268.0 spike=0.48
- RMDA.CA: score=20.3 buy_ready=False sector_rank=3 price=5.01 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=44.9 liquidity=12323977.0 spike=0.15
- ROTO.CA: score=18.96 buy_ready=False sector_rank=12 price=41.8 support=32.76 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=75.77 liquidity=48888792.0 spike=1.79
- RREI.CA: score=12.96 buy_ready=False sector_rank=12 price=3.47 support=3.35 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=39.47 liquidity=7584485.0 spike=0.39
- RTVC.CA: score=9.8 buy_ready=False sector_rank=12 price=3.7 support=3.76 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=49.35 liquidity=5220813.0 spike=1.1
- RUBX.CA: score=17.25 buy_ready=False sector_rank=12 price=10.43 support=9.8 resistance=10.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=53.8 liquidity=7873716.0 spike=0.8
- SAUD.CA: score=4.33 buy_ready=False sector_rank=14 price=21.0 support=20.82 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=19.48 liquidity=4130061.5 spike=0.46
- SCEM.CA: score=18.01 buy_ready=False sector_rank=15 price=62.85 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=39.9 liquidity=11241531.0 spike=0.59
- SCFM.CA: score=1.52 buy_ready=False sector_rank=12 price=240.85 support=226.5 resistance=276.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=28.61 liquidity=1142794.25 spike=0.18
- SCTS.CA: score=6.27 buy_ready=False sector_rank=5 price=576.93 support=577.41 resistance=577.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=1014318.25 spike=1.0
- SDTI.CA: score=12.38 buy_ready=False sector_rank=12 price=46.4 support=44.03 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=50.93 liquidity=2001363.0 spike=0.16
- SEIG.CA: score=12.44 buy_ready=False sector_rank=12 price=189.21 support=179.43 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=40.62 liquidity=2063997.38 spike=0.5
- SIPC.CA: score=2.97 buy_ready=False sector_rank=12 price=3.45 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=27.78 liquidity=2585873.25 spike=0.22
- SKPC.CA: score=7.74 buy_ready=False sector_rank=21 price=15.96 support=15.95 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=31.92 liquidity=21419450.0 spike=0.55
- SMFR.CA: score=1.08 buy_ready=False sector_rank=12 price=197.58 support=192.0 resistance=214.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=34.4 liquidity=696097.38 spike=0.29
- SNFC.CA: score=18.38 buy_ready=False sector_rank=12 price=12.07 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=37.79 liquidity=14556034.0 spike=0.71
- SPIN.CA: score=11.46 buy_ready=False sector_rank=18 price=13.95 support=13.3 resistance=14.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=29.13 liquidity=12234783.0 spike=1.84
- SPMD.CA: score=16.94 buy_ready=False sector_rank=12 price=0.43 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=54.97 liquidity=4564507.5 spike=0.16
- SUGR.CA: score=2.28 buy_ready=False sector_rank=13 price=47.15 support=47.27 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=23.98 liquidity=3055938.75 spike=0.35
- SVCE.CA: score=23.46 buy_ready=False sector_rank=12 price=9.43 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=53.51 liquidity=113195072.0 spike=1.54
- SWDY.CA: score=17.82 buy_ready=False sector_rank=8 price=87.61 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=43.89 liquidity=7277238.5 spike=0.41
- TALM.CA: score=16.57 buy_ready=False sector_rank=5 price=16.02 support=15.5 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=47.56 liquidity=5313324.5 spike=0.66
- TMGH.CA: score=15.43 buy_ready=False sector_rank=11 price=94.5 support=92.91 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=45.8 liquidity=205239024.0 spike=0.42
- TRTO.CA: score=6.38 buy_ready=False sector_rank=12 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=10.27 buy_ready=False sector_rank=12 price=488.83 support=465.01 resistance=500.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=74.13 liquidity=894224.44 spike=0.93
- UEGC.CA: score=11.69 buy_ready=False sector_rank=12 price=1.39 support=1.32 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=38.24 liquidity=3310453.25 spike=0.14
- UNIP.CA: score=13.05 buy_ready=False sector_rank=12 price=0.32 support=0.28 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=55.07 liquidity=4672918.0 spike=0.2
- UNIT.CA: score=4.52 buy_ready=False sector_rank=11 price=12.97 support=12.92 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=34.19 liquidity=1083175.38 spike=0.15
- WCDF.CA: score=5.6 buy_ready=False sector_rank=12 price=531.95 support=450.0 resistance=547.9 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=44.29 liquidity=223950.96 spike=0.89
- WKOL.CA: score=7.31 buy_ready=False sector_rank=12 price=285.13 support=287.2 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=36.6 liquidity=1925928.25 spike=0.67
- ZEOT.CA: score=17.38 buy_ready=False sector_rank=12 price=10.91 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=76.79 liquidity=19262924.0 spike=0.79
- ZMID.CA: score=22.43 buy_ready=False sector_rank=11 price=6.49 support=5.82 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=69.23 liquidity=127287304.0 spike=0.61

## Backtesting Lite
- DAPH.CA: 180d return=5.24%, max drawdown=-30.86%, MA20>MA50 days last20=12, as_of=2026-06-23T21:00:00+00:00
- ECAP.CA: 180d return=6.16%, max drawdown=-28.16%, MA20>MA50 days last20=20, as_of=2026-06-23T21:00:00+00:00
- OCDI.CA: 180d return=48.65%, max drawdown=-18.11%, MA20>MA50 days last20=10, as_of=2026-06-23T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- DAPH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Development & Engineering Consultants summary=Evidence rejected for DAPH.CA: source text did not clearly match DAPH.CA / Development & Engineering Consultants.
- ECAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Al Ezz Ceramics & Porcelain Co. summary=Evidence rejected for ECAP.CA: source text did not clearly match ECAP.CA / Al Ezz Ceramics & Porcelain Co..
- OCDI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Sixth of October Development and Investment summary=Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- GIHD.CA: status=OLD_ACCEPTED latest=2016-01-01 age_days=3828 sources=3 expected=Gharbia Islamic Housing Development Company summary=Gharbia Islamic Housing to discuss raising capital mid-December; Gharbia Islamic Housing to distribute EGP 0.2/shr; Gharbia Islamic Housing profits fall 46% in 2016
  - Gharbia Islamic Housing to discuss raising capital mid-December: https://english.mubasher.info/news/3147599/Gharbia-Islamic-Housing-to-discuss-raising-capital-mid-December/
  - Gharbia Islamic Housing to distribute EGP 0.2/shr: https://english.mubasher.info/news/3082262/Gharbia-Islamic-Housing-to-distribute-EGP-0-2-shr/
  - Gharbia Islamic Housing profits fall 46% in 2016: https://english.mubasher.info/news/3068305/Gharbia-Islamic-Housing-profits-fall-46-in-2016/
- CIRA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Investment and Real Estate Development summary=CIRA Education take over 51% of L’École Française Hurghada; CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion; CIRA Education launches Middle East’s 1st initiative for care economy
  - CIRA Education take over 51% of L’École Française Hurghada: https://english.mubasher.info/news/4488666/CIRA-Education-take-over-51-of-L-%C3%89cole-Fran%C3%A7aise-Hurghada/
  - CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion: https://english.mubasher.info/news/4393636/CIRA-s-majority-shareholder-acquires-37-5-additional-equity-backs-regional-expansion/
  - CIRA Education launches Middle East’s 1st initiative for care economy: https://english.mubasher.info/news/4391766/CIRA-Education-launches-Middle-East-s-1st-initiative-for-care-economy/
- CNFN.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=540 sources=3 expected=Contact Financial Holding summary=Contact’s consolidated profits approach EGP 471m in 2025; Contact logs lower consolidated net profits at EGP 291m in 9M-25; Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem
  - Contact’s consolidated profits approach EGP 471m in 2025: https://english.mubasher.info/news/4582855/Contact-s-consolidated-profits-approach-EGP-471m-in-2025/
  - Contact logs lower consolidated net profits at EGP 291m in 9M-25: https://english.mubasher.info/news/4526894/Contact-logs-lower-consolidated-net-profits-at-EGP-291m-in-9M-25/
  - Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem: https://english.mubasher.info/news/4509412/Contact-e-money-forge-partnership-to-boost-Egypt-s-financial-ecosystem/
- MHOT.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Hotels summary=Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26; Shareholder buys EGP 3.39m worth of shares in Misr Hotels; Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits
  - Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26: https://english.mubasher.info/news/4602482/Misr-Hotels-net-profits-cross-EGP-1-1bn-in-9M-25-26/
  - Shareholder buys EGP 3.39m worth of shares in Misr Hotels: https://english.mubasher.info/news/4013808/Shareholder-buys-EGP-3-39m-worth-of-shares-in-Misr-Hotels/
  - Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits: https://english.mubasher.info/news/3975543/Misr-Hotels-repays-EGP-383m-of-NBE-s-loan-unveils-estimated-profits/
- CLHO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=540 sources=3 expected=Cleopatra Hospital Group summary=Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025; Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn; Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo
  - Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025: https://english.mubasher.info/news/4594702/Cleopatra-Hospitals-unveils-EGP-84m-dividends-to-employee-for-2025/
  - Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn: https://english.mubasher.info/news/4579844/Cleopatra-Hospitals-posts-higher-consolidated-profits-in-2025-revenues-cross-EGP-7-2bn/
  - Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo: https://english.mubasher.info/news/4553462/Cleopatra-Hospitals-launches-EGP-3-5bn-Sky-hospital-in-East-Cairo/

## Warnings
- Evidence rejected for DAPH.CA: source text did not clearly match DAPH.CA / Development & Engineering Consultants.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for ECAP.CA: source text did not clearly match ECAP.CA / Al Ezz Ceramics & Porcelain Co..
- Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- Evidence for GIHD.CA matches the company but appears old; latest detected date is 2016-01-01.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
- Evidence for CNFN.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for MHOT.CA matches the company but no source/report date was detected.
- Evidence for CLHO.CA matches the company but appears old; latest detected date is 2025-01-01.
