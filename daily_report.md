# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-06-08T10:11:05.800484+00:00
Generated Cairo: 2026-06-08 13:11
Run timing: target 08:45 Cairo | generated Cairo 2026-06-08 13:11 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-06-08 13:07

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 70
- Data quality issues: 0
- Tradeable price/liquidity tickers: 187/190
- Top sector: Technology & Distribution

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, June 08
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 20.0% / above MA50 70.0%
- EGX70 regime: CONSTRUCTIVE / above MA20 53.85% / above MA50 82.05%
- Sector breadth: 61.9%
- Risk mode: SELECTIVE_SMALL_MID_SWINGS

## Top Liquidity
- RMDA.CA: liquidity=1028768320.0 spike=18.33 score=31.4
- CCAP.CA: liquidity=692521152.0 spike=0.81 score=30.4
- EFID.CA: liquidity=588865664.0 spike=12.26 score=26.36
- COMI.CA: liquidity=480670272.0 spike=0.74 score=18.65
- ZMID.CA: liquidity=309845344.0 spike=1.56 score=25.52

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The local scanner highlighted a handful of bullish‑watch candidates despite a bearish EGX30 backdrop and a constructive EGX70 environment. Selection was driven by strong rank scores, recent liquidity spikes or solid tradeable volume, proximity to support levels, and placement in leading sectors (Technology & Distribution, Investment Holding, Tourism & Leisure). Market regime shifts push risk mode to SELECTIVE_SMALL_MID_SWINGS, so only the most liquid, support‑near stocks are considered, but evidence gaps keep confidence low.
- Liquidity spikes (e.g., RMDA, NCCW) and tradeable volume signal short‑term accumulation despite overall market weakness.
- All top tickets sit near 20‑day support (10‑24% distance) with modest resistance gaps, offering limited upside in the next 1‑3 days.
- Sector breadth at 61.9% and leadership from Technology & Distribution and Investment Holding bolster the outlook for those stocks.
- EGX30’s bearish trend reduces broad market upside, while EGX70’s constructive trend supports selective mid‑cap swings.
- Evidence gaps keep confidence low; treat signals as watch‑list items, not trade triggers.

## Top Liquidity Spikes
- RMDA.CA: spike=18.33 liquidity=1028768320.0 outlook=BULLISH_WATCH score=95.75 buy_ready=True
- EFID.CA: spike=12.26 liquidity=588865664.0 outlook=CONSTRUCTIVE score=65.91 buy_ready=False
- LUTS.CA: spike=3.09 liquidity=41871056.0 outlook=BULLISH_WATCH score=73.9 buy_ready=False
- PRCL.CA: spike=2.89 liquidity=93146664.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ECAP.CA: spike=2.81 liquidity=13896899.0 outlook=BULLISH_WATCH score=87.9 buy_ready=True

## Sector Leaderboard
- #1 Technology & Distribution: score=11.4 5d=3.21% 20d=18.4% aboveMA50=100.0%
- #2 Investment Holding: score=10.3 5d=6.55% 20d=12.31% aboveMA50=66.67%
- #3 Tourism & Leisure: score=9.63 5d=0.75% 20d=14.57% aboveMA50=100.0%
- #4 Healthcare: score=8.75 5d=3.62% 20d=7.32% aboveMA50=100.0%
- #5 Real Estate: score=7.9 5d=1.26% 20d=11.28% aboveMA50=84.62%
- #6 Industrial Goods & Cables: score=7.04 5d=2.0% 20d=-0.8% aboveMA50=100.0%
- #7 Textiles: score=6.78 5d=1.5% 20d=6.29% aboveMA50=75.0%
- #8 Food, Beverages & Tobacco: score=5.91 5d=0.31% 20d=2.11% aboveMA50=85.71%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ZMID.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- RMDA.CA: BULLISH_WATCH score=95.75 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- RAYA.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- NEDA.CA: BULLISH_WATCH score=89.9 liquidity=TRADEABLE sector=IMPROVING risk=close to resistance; sector is not leading
- MHOT.CA: BULLISH_WATCH score=89.63 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ECAP.CA: BULLISH_WATCH score=87.9 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CCAP.CA: BULLISH_WATCH score=87 liquidity=TRADEABLE sector=LEADING risk=far above support; close to resistance
- NIPH.CA: BULLISH_WATCH score=84.75 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MPRC.CA: BULLISH_WATCH score=83.9 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- NCCW.CA: BULLISH_WATCH score=83.9 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support; sector is not leading

## BUY-Ready Candidates
- RMDA.CA: rank=31.4 outlook=BULLISH_WATCH outlook_score=95.75 sector_rank=4 price=5.29 support=4.78 resistance=5.19 liquidity=1028768320.0
- CCAP.CA: rank=30.4 outlook=BULLISH_WATCH outlook_score=87 sector_rank=2 price=5.67 support=4.55 resistance=5.72 liquidity=692521152.0
- ECAP.CA: rank=29.98 outlook=BULLISH_WATCH outlook_score=87.9 sector_rank=9 price=31.74 support=28.7 resistance=31.5 liquidity=13896899.0
- RAYA.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=90 sector_rank=1 price=7.55 support=6.6 resistance=8.0 liquidity=34644988.0
- MPRC.CA: rank=28.6 outlook=BULLISH_WATCH outlook_score=83.9 sector_rank=9 price=33.73 support=30.61 resistance=34.55 liquidity=22728000.0
- NCCW.CA: rank=27.94 outlook=BULLISH_WATCH outlook_score=83.9 sector_rank=9 price=6.18 support=5.13 resistance=6.5 liquidity=35800212.0
- AREH.CA: rank=27.7 outlook=BULLISH_WATCH outlook_score=81.9 sector_rank=9 price=1.5 support=1.27 resistance=1.57 liquidity=42260352.0
- GDWA.CA: rank=27.1 outlook=BULLISH_WATCH outlook_score=72.9 sector_rank=9 price=0.82 support=0.77 resistance=0.83 liquidity=9736797.0
- CANA.CA: rank=26.61 outlook=CONSTRUCTIVE outlook_score=60.12 sector_rank=15 price=38.05 support=33.15 resistance=38.0 liquidity=21050652.0
- MPCO.CA: rank=26.6 outlook=CONSTRUCTIVE outlook_score=67.86 sector_rank=10 price=1.79 support=1.54 resistance=1.93 liquidity=71945920.0

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=15.37 buy_ready=True sector_rank=9 price=211.82 support=195.1 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=48.5 liquidity=1011785.94 spike=0.07
- ABUK.CA: score=12.88 buy_ready=False sector_rank=17 price=82.94 support=81.2 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=26.31 liquidity=58653360.0 spike=0.45
- ACAMD.CA: score=26.36 buy_ready=True sector_rank=9 price=2.34 support=1.96 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=64.81 liquidity=86772056.0 spike=0.74
- ACGC.CA: score=24.4 buy_ready=True sector_rank=7 price=9.9 support=8.3 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=61.04 liquidity=18919634.0 spike=0.35
- ADCI.CA: score=15.41 buy_ready=True sector_rank=9 price=216.75 support=202.22 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=56.57 liquidity=1045950.31 spike=0.15
- ADIB.CA: score=21.65 buy_ready=False sector_rank=15 price=46.66 support=44.45 resistance=50.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=54.16 liquidity=43135380.0 spike=0.26
- ADPC.CA: score=17.08 buy_ready=False sector_rank=9 price=3.7 support=3.54 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=37.72 liquidity=4723874.0 spike=0.19
- AFDI.CA: score=18.35 buy_ready=True sector_rank=9 price=44.17 support=37.54 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=65.21 liquidity=3988385.5 spike=0.22
- AFMC.CA: score=14.79 buy_ready=False sector_rank=9 price=72.98 support=69.33 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=37.49 liquidity=2426553.25 spike=0.18
- AJWA.CA: score=25.28 buy_ready=True sector_rank=9 price=134.25 support=130.01 resistance=139.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=50.49 liquidity=14984004.0 spike=1.46
- ALCN.CA: score=11.91 buy_ready=False sector_rank=18 price=29.06 support=28.4 resistance=30.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=48.74 liquidity=4074382.25 spike=0.17
- ALUM.CA: score=22.68 buy_ready=True sector_rank=9 price=25.7 support=22.5 resistance=26.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=56.55 liquidity=4321468.5 spike=0.19
- AMER.CA: score=24.4 buy_ready=True sector_rank=5 price=2.72 support=2.3 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=51.9 liquidity=51193132.0 spike=0.39
- AMES.CA: score=8.57 buy_ready=False sector_rank=9 price=50.89 support=48.0 resistance=57.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=29.19 liquidity=1211886.25 spike=0.13
- AMIA.CA: score=16.91 buy_ready=True sector_rank=9 price=8.94 support=8.25 resistance=10.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=2551752.5 spike=0.08
- AMOC.CA: score=17.15 buy_ready=False sector_rank=11 price=8.4 support=8.12 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=21.05 liquidity=66751376.0 spike=0.78
- ANFI.CA: score=13.0 buy_ready=False sector_rank=9 price=14.05 support=13.5 resistance=15.55 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=24.73 liquidity=5638883.28 spike=0.28
- APSW.CA: score=13.75 buy_ready=False sector_rank=9 price=8.91 support=8.62 resistance=9.38 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=43.64 liquidity=1354649.65 spike=1.52
- ARAB.CA: score=20.4 buy_ready=False sector_rank=5 price=0.2 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=39492728.0 spike=0.51
- ARCC.CA: score=23.8 buy_ready=True sector_rank=14 price=58.3 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=68.08 liquidity=11663389.0 spike=0.26
- AREH.CA: score=27.7 buy_ready=True sector_rank=9 price=1.5 support=1.27 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=67.74 liquidity=42260352.0 spike=1.67
- ARVA.CA: score=23.36 buy_ready=False sector_rank=9 price=11.0 support=7.71 resistance=11.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=75.37 liquidity=19690328.0 spike=0.78
- ASCM.CA: score=24.36 buy_ready=False sector_rank=9 price=55.57 support=44.75 resistance=59.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=73.58 liquidity=26879278.0 spike=0.41
- ASPI.CA: score=26.36 buy_ready=True sector_rank=9 price=0.35 support=0.25 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=60.53 liquidity=52469044.0 spike=0.98
- ATLC.CA: score=15.22 buy_ready=True sector_rank=16 price=5.05 support=4.71 resistance=5.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=47.3 liquidity=2185102.25 spike=0.27
- ATQA.CA: score=23.88 buy_ready=True sector_rank=17 price=9.81 support=9.41 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=47.77 liquidity=10358535.0 spike=0.21
- AXPH.CA: score=11.85 buy_ready=False sector_rank=9 price=1142.94 support=985.0 resistance=1239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=20.12 liquidity=2494690.75 spike=0.43
- BINV.CA: score=25.05 buy_ready=True sector_rank=2 price=46.0 support=40.5 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=66.86 liquidity=8649347.0 spike=0.66
- BIOC.CA: score=17.96 buy_ready=True sector_rank=9 price=73.93 support=70.0 resistance=79.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=47.22 liquidity=3598438.5 spike=0.48
- BTFH.CA: score=15.04 buy_ready=False sector_rank=16 price=3.06 support=3.03 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=31.37 liquidity=74023888.0 spike=0.3
- CAED.CA: score=9.12 buy_ready=False sector_rank=9 price=70.57 support=66.56 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=26.71 liquidity=1759509.25 spike=0.12
- CANA.CA: score=26.61 buy_ready=True sector_rank=15 price=38.05 support=33.15 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=63.1 liquidity=21050652.0 spike=1.48
- CCAP.CA: score=30.4 buy_ready=True sector_rank=2 price=5.67 support=4.55 resistance=5.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=692521152.0 spike=0.81
- CCRS.CA: score=20.33 buy_ready=False sector_rank=9 price=2.55 support=2.0 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=70.73 liquidity=5974032.5 spike=0.22
- CEFM.CA: score=8.29 buy_ready=False sector_rank=9 price=106.98 support=103.07 resistance=119.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=25.15 liquidity=928814.81 spike=0.13
- CERA.CA: score=26.52 buy_ready=True sector_rank=9 price=1.2 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=35869968.0 spike=2.58
- CFGH.CA: score=3.36 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=2804.02 spike=0.7
- CICH.CA: score=12.25 buy_ready=False sector_rank=16 price=12.14 support=11.01 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=1213455.0 spike=0.27
- CIEB.CA: score=14.21 buy_ready=False sector_rank=15 price=23.57 support=23.31 resistance=24.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=2563635.25 spike=0.22
- CIRA.CA: score=19.64 buy_ready=True sector_rank=13 price=26.75 support=21.0 resistance=28.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=56.48 liquidity=5795476.0 spike=0.2
- CLHO.CA: score=22.4 buy_ready=False sector_rank=4 price=15.48 support=14.58 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=43.06 liquidity=17514568.0 spike=0.47
- CNFN.CA: score=22.2 buy_ready=False sector_rank=16 price=4.6 support=4.47 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=37.7 liquidity=33641352.0 spike=2.08
- COMI.CA: score=18.65 buy_ready=False sector_rank=15 price=131.03 support=131.3 resistance=144.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=48.15 liquidity=480670272.0 spike=0.74
- COPR.CA: score=20.54 buy_ready=True sector_rank=9 price=0.36 support=0.31 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=7181854.0 spike=0.18
- COSG.CA: score=26.36 buy_ready=True sector_rank=9 price=1.63 support=1.45 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=58.97 liquidity=38990576.0 spike=0.67
- CPCI.CA: score=15.71 buy_ready=False sector_rank=9 price=361.58 support=340.01 resistance=374.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=72.04 liquidity=1350454.0 spike=0.18
- CSAG.CA: score=21.48 buy_ready=False sector_rank=18 price=31.4 support=30.4 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=53.77 liquidity=8640651.0 spike=0.44
- DAPH.CA: score=8.68 buy_ready=False sector_rank=9 price=80.75 support=79.25 resistance=96.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=16.14 liquidity=4324739.5 spike=0.13
- DEIN.CA: score=10.36 buy_ready=False sector_rank=9 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=4.82 buy_ready=False sector_rank=8 price=24.38 support=24.45 resistance=26.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=22.14 liquidity=454545.5 spike=0.19
- DSCW.CA: score=20.36 buy_ready=False sector_rank=9 price=1.82 support=1.71 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=44.83 liquidity=15925200.0 spike=0.25
- DTPP.CA: score=7.94 buy_ready=False sector_rank=9 price=124.68 support=121.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=27.48 liquidity=575957.69 spike=0.1
- EALR.CA: score=13.37 buy_ready=False sector_rank=9 price=356.01 support=346.01 resistance=392.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=36.82 liquidity=1014942.25 spike=0.08
- EASB.CA: score=14.83 buy_ready=False sector_rank=9 price=5.06 support=4.61 resistance=5.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=55.71 liquidity=474299.97 spike=0.29
- EAST.CA: score=26.36 buy_ready=True sector_rank=8 price=39.2 support=37.01 resistance=39.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=53.99 liquidity=68140304.0 spike=0.98
- EBSC.CA: score=17.01 buy_ready=False sector_rank=9 price=1.87 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=63.64 liquidity=650325.94 spike=0.22
- ECAP.CA: score=29.98 buy_ready=True sector_rank=9 price=31.74 support=28.7 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=59.45 liquidity=13896899.0 spike=2.81
- EDFM.CA: score=13.37 buy_ready=False sector_rank=9 price=333.99 support=320.2 resistance=349.0 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=39.0 liquidity=667979.98 spike=1.17
- EEII.CA: score=25.88 buy_ready=True sector_rank=9 price=2.46 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=35.0 liquidity=31034526.0 spike=1.76
- EFIC.CA: score=4.1 buy_ready=False sector_rank=17 price=204.46 support=195.25 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=6.17 liquidity=2224253.75 spike=0.5
- EFID.CA: score=26.36 buy_ready=False sector_rank=8 price=28.6 support=27.49 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=76.47 liquidity=588865664.0 spike=12.26
- EFIH.CA: score=19.51 buy_ready=False sector_rank=21 price=21.53 support=21.3 resistance=22.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=49.84 liquidity=22567434.0 spike=0.35
- EGAL.CA: score=20.88 buy_ready=False sector_rank=17 price=323.42 support=303.05 resistance=344.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=54.23 liquidity=12183995.0 spike=0.11
- EGAS.CA: score=15.26 buy_ready=True sector_rank=11 price=50.0 support=46.51 resistance=51.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=68.15 liquidity=3106910.75 spike=0.21
- EGBE.CA: score=6.68 buy_ready=False sector_rank=15 price=0.44 support=0.41 resistance=0.47 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=23.54 liquidity=35671.17 spike=0.28
- EGCH.CA: score=24.88 buy_ready=True sector_rank=17 price=14.85 support=11.95 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=49.0 liquidity=37828648.0 spike=0.31
- EGSA.CA: score=8.9 buy_ready=False sector_rank=12 price=8.93 support=8.3 resistance=9.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:10 AM market time freshness=DELAYED_CURRENT RSI=84.34 liquidity=9104.59 spike=0.56
- EGTS.CA: score=24.4 buy_ready=True sector_rank=5 price=18.11 support=12.9 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=54.78 liquidity=37861028.0 spike=0.34
- EHDR.CA: score=21.36 buy_ready=False sector_rank=9 price=2.67 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=75.71 liquidity=37122352.0 spike=0.7
- EKHO.CA: score=14.15 buy_ready=False sector_rank=11 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=23.34 buy_ready=True sector_rank=6 price=2.16 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=7943845.0 spike=0.27
- ELKA.CA: score=25.36 buy_ready=True sector_rank=9 price=1.26 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=26762030.0 spike=0.64
- ELNA.CA: score=7.68 buy_ready=False sector_rank=9 price=39.54 support=37.11 resistance=42.79 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=31.33 liquidity=323002.27 spike=1.0
- ELSH.CA: score=11.68 buy_ready=False sector_rank=9 price=12.16 support=11.15 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=195028128.0 spike=2.16
- ELWA.CA: score=12.88 buy_ready=False sector_rank=9 price=2.07 support=1.79 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=84.62 liquidity=1522021.63 spike=0.52
- EMFD.CA: score=26.4 buy_ready=False sector_rank=5 price=12.2 support=9.83 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=71.51 liquidity=147645728.0 spike=0.65
- ENGC.CA: score=23.96 buy_ready=True sector_rank=9 price=34.02 support=32.31 resistance=35.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=42.02 liquidity=7599334.5 spike=0.63
- EOSB.CA: score=14.89 buy_ready=False sector_rank=9 price=1.42 support=1.34 resistance=1.54 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=253515.43 spike=2.14
- EPCO.CA: score=19.63 buy_ready=True sector_rank=9 price=9.2 support=8.56 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=46.78 liquidity=3269284.5 spike=0.26
- EPPK.CA: score=8.38 buy_ready=False sector_rank=9 price=12.51 support=11.67 resistance=13.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=32.88 liquidity=1483958.13 spike=1.27
- ETEL.CA: score=21.89 buy_ready=False sector_rank=12 price=94.6 support=93.01 resistance=101.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=50.71 liquidity=23470682.0 spike=0.21
- ETRS.CA: score=24.36 buy_ready=False sector_rank=9 price=8.89 support=7.37 resistance=9.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=73.88 liquidity=29999754.0 spike=0.6
- EXPA.CA: score=23.65 buy_ready=False sector_rank=15 price=19.29 support=18.34 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=72.8 liquidity=45414784.0 spike=1.0
- FAIT.CA: score=14.75 buy_ready=True sector_rank=15 price=37.41 support=33.57 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=46.42 liquidity=1102258.38 spike=0.15
- FAITA.CA: score=11.66 buy_ready=False sector_rank=15 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:27 AM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=9225.89 spike=0.17
- FERC.CA: score=3.52 buy_ready=False sector_rank=17 price=77.65 support=76.5 resistance=83.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=27.01 liquidity=643416.44 spike=0.09
- FWRY.CA: score=16.51 buy_ready=False sector_rank=21 price=18.54 support=18.6 resistance=21.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=244790528.0 spike=0.85
- GBCO.CA: score=12.05 buy_ready=False sector_rank=20 price=26.0 support=25.25 resistance=29.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=31.56 liquidity=33189956.0 spike=0.28
- GDWA.CA: score=27.1 buy_ready=True sector_rank=9 price=0.82 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=61.11 liquidity=9736797.0 spike=0.9
- GGCC.CA: score=21.3 buy_ready=False sector_rank=9 price=0.42 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=70.37 liquidity=5939372.0 spike=0.92
- GIHD.CA: score=17.55 buy_ready=True sector_rank=9 price=41.85 support=39.1 resistance=44.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=46.01 liquidity=1194482.75 spike=0.21
- GMCI.CA: score=16.68 buy_ready=False sector_rank=9 price=1.78 support=1.67 resistance=1.84 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=60.71 liquidity=317931.13 spike=0.89
- GRCA.CA: score=5.42 buy_ready=False sector_rank=9 price=55.0 support=53.36 resistance=60.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=30.73 liquidity=1059081.38 spike=0.11
- GSSC.CA: score=6.25 buy_ready=False sector_rank=9 price=250.86 support=228.1 resistance=272.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=4.44 liquidity=1889817.63 spike=0.19
- GTWL.CA: score=8.27 buy_ready=False sector_rank=9 price=46.23 support=46.3 resistance=59.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=10.97 liquidity=3907337.5 spike=0.35
- HDBK.CA: score=21.75 buy_ready=False sector_rank=15 price=143.07 support=140.0 resistance=150.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=43.81 liquidity=17211958.0 spike=1.05
- HELI.CA: score=22.4 buy_ready=False sector_rank=5 price=6.4 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=56.02 liquidity=36749220.0 spike=0.21
- HRHO.CA: score=17.04 buy_ready=False sector_rank=16 price=26.4 support=26.16 resistance=30.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=36.17 liquidity=86513368.0 spike=0.41
- ICID.CA: score=16.45 buy_ready=False sector_rank=9 price=6.03 support=4.4 resistance=6.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=78.54 liquidity=3089860.0 spike=0.25
- IDRE.CA: score=17.07 buy_ready=True sector_rank=9 price=44.68 support=39.72 resistance=49.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=47.94 liquidity=2710604.0 spike=0.08
- IFAP.CA: score=6.88 buy_ready=False sector_rank=10 price=19.45 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=31.0 liquidity=3536459.75 spike=0.21
- INFI.CA: score=15.2 buy_ready=False sector_rank=9 price=101.06 support=99.51 resistance=112.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=37.06 liquidity=3837540.75 spike=0.23
- IRON.CA: score=11.09 buy_ready=False sector_rank=17 price=32.51 support=31.83 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=51.17 liquidity=2217429.5 spike=0.26
- ISMA.CA: score=23.36 buy_ready=False sector_rank=9 price=28.75 support=19.8 resistance=29.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=98.97 liquidity=40833316.0 spike=0.85
- ISMQ.CA: score=24.88 buy_ready=True sector_rank=17 price=7.7 support=7.27 resistance=8.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=51.72 liquidity=11048784.0 spike=0.22
- ISPH.CA: score=27.18 buy_ready=False sector_rank=4 price=12.6 support=11.12 resistance=12.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=74.25 liquidity=198880224.0 spike=1.39
- JUFO.CA: score=26.36 buy_ready=True sector_rank=8 price=29.61 support=26.51 resistance=29.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=54.12 liquidity=19518522.0 spike=0.43
- KABO.CA: score=20.47 buy_ready=True sector_rank=7 price=6.34 support=5.92 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=64.89 liquidity=4067416.25 spike=0.21
- KWIN.CA: score=13.53 buy_ready=False sector_rank=9 price=72.08 support=69.0 resistance=81.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=43.56 liquidity=1166204.88 spike=0.28
- KZPC.CA: score=15.36 buy_ready=False sector_rank=9 price=10.55 support=10.3 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=42.66 liquidity=3000534.5 spike=0.25
- LCSW.CA: score=20.61 buy_ready=False sector_rank=14 price=27.52 support=26.16 resistance=29.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=36.2 liquidity=8810846.0 spike=0.51
- LUTS.CA: score=27.54 buy_ready=False sector_rank=9 price=0.64 support=0.54 resistance=0.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=78.81 liquidity=41871056.0 spike=3.09
- MAAL.CA: score=20.96 buy_ready=False sector_rank=9 price=5.96 support=4.44 resistance=6.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=97.28 liquidity=7599367.0 spike=0.67
- MASR.CA: score=22.36 buy_ready=False sector_rank=9 price=6.86 support=6.46 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=13203512.0 spike=0.21
- MBSC.CA: score=23.84 buy_ready=True sector_rank=14 price=275.49 support=259.63 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=55.46 liquidity=48453976.0 spike=1.02
- MCQE.CA: score=21.26 buy_ready=False sector_rank=14 price=191.87 support=188.01 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=58.89 liquidity=9459938.0 spike=0.49
- MCRO.CA: score=25.36 buy_ready=True sector_rank=9 price=1.28 support=1.21 resistance=1.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=51143264.0 spike=0.54
- MENA.CA: score=22.18 buy_ready=True sector_rank=5 price=6.77 support=5.76 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=61.37 liquidity=5784914.0 spike=0.35
- MEPA.CA: score=19.3 buy_ready=True sector_rank=9 price=1.72 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=43.33 liquidity=4935176.0 spike=0.21
- MFPC.CA: score=15.88 buy_ready=False sector_rank=17 price=42.87 support=42.3 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=21.93 liquidity=50051364.0 spike=0.48
- MFSC.CA: score=9.41 buy_ready=False sector_rank=9 price=47.64 support=33.0 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=30.21 liquidity=2051040.5 spike=0.14
- MHOT.CA: score=22.99 buy_ready=True sector_rank=3 price=30.65 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=60.77 liquidity=5586587.0 spike=0.28
- MICH.CA: score=20.79 buy_ready=True sector_rank=9 price=36.35 support=35.01 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=49.24 liquidity=4430938.5 spike=0.49
- MILS.CA: score=20.48 buy_ready=True sector_rank=9 price=143.0 support=127.01 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=52.36 liquidity=4115424.0 spike=0.15
- MIPH.CA: score=10.57 buy_ready=False sector_rank=4 price=675.58 support=640.0 resistance=729.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=27.24 liquidity=1165012.13 spike=0.26
- MOED.CA: score=5.38 buy_ready=False sector_rank=9 price=0.69 support=0.68 resistance=0.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=16.5 liquidity=2020220.12 spike=0.15
- MOIL.CA: score=16.2 buy_ready=False sector_rank=11 price=0.48 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=52.11 liquidity=44317.18 spike=0.22
- MOIN.CA: score=14.26 buy_ready=False sector_rank=9 price=24.96 support=23.13 resistance=26.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=53.71 liquidity=898858.44 spike=0.36
- MOSC.CA: score=9.43 buy_ready=False sector_rank=9 price=271.38 support=268.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=17.07 liquidity=2073034.38 spike=0.1
- MPCI.CA: score=26.36 buy_ready=True sector_rank=9 price=229.09 support=187.01 resistance=224.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=63.07 liquidity=61615668.0 spike=0.63
- MPCO.CA: score=26.6 buy_ready=True sector_rank=10 price=1.79 support=1.54 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=63.83 liquidity=71945920.0 spike=1.13
- MPRC.CA: score=28.6 buy_ready=True sector_rank=9 price=33.73 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=60.71 liquidity=22728000.0 spike=1.12
- MTIE.CA: score=15.32 buy_ready=False sector_rank=20 price=9.0 support=8.71 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=42.75 liquidity=5272055.0 spike=0.21
- NAHO.CA: score=3.38 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=18291.8 spike=0.49
- NCCW.CA: score=27.94 buy_ready=True sector_rank=9 price=6.18 support=5.13 resistance=6.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=67.37 liquidity=35800212.0 spike=1.79
- NEDA.CA: score=20.17 buy_ready=True sector_rank=9 price=2.83 support=2.65 resistance=2.87 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=55.56 liquidity=1393078.78 spike=2.21
- NHPS.CA: score=11.96 buy_ready=False sector_rank=9 price=68.56 support=67.53 resistance=73.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=38.38 liquidity=602957.31 spike=0.05
- NINH.CA: score=13.7 buy_ready=False sector_rank=9 price=18.01 support=17.53 resistance=20.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=47.16 liquidity=1344376.13 spike=0.1
- NIPH.CA: score=24.4 buy_ready=True sector_rank=4 price=171.85 support=155.1 resistance=186.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=59.65 liquidity=79941888.0 spike=0.64
- OBRI.CA: score=10.18 buy_ready=False sector_rank=9 price=34.35 support=34.2 resistance=39.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=26.33 liquidity=5816744.0 spike=0.48
- OCDI.CA: score=16.8 buy_ready=False sector_rank=5 price=21.15 support=20.19 resistance=23.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=44.4 liquidity=7401196.0 spike=0.17
- OCPH.CA: score=9.29 buy_ready=False sector_rank=9 price=361.21 support=350.0 resistance=409.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=20.34 liquidity=1926342.5 spike=0.14
- ODIN.CA: score=19.37 buy_ready=True sector_rank=9 price=2.08 support=1.89 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=65.62 liquidity=5005325.5 spike=0.5
- OFH.CA: score=21.19 buy_ready=True sector_rank=9 price=0.64 support=0.6 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=43.4 liquidity=4829082.0 spike=0.21
- OIH.CA: score=16.42 buy_ready=False sector_rank=2 price=1.41 support=1.35 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=12.5 liquidity=131973096.0 spike=1.01
- OLFI.CA: score=22.36 buy_ready=False sector_rank=8 price=21.63 support=21.0 resistance=22.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=43.78 liquidity=11310791.0 spike=0.51
- ORAS.CA: score=7.6 buy_ready=False sector_rank=19 price=728.66 support=722.99 resistance=730.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=90231224.0 spike=1.0
- ORHD.CA: score=22.4 buy_ready=True sector_rank=5 price=36.9 support=32.9 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=68.84 liquidity=51787052.0 spike=0.25
- ORWE.CA: score=21.4 buy_ready=False sector_rank=7 price=23.55 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=76.41 liquidity=19933112.0 spike=0.42
- PHAR.CA: score=15.86 buy_ready=False sector_rank=4 price=86.92 support=83.96 resistance=92.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=37.37 liquidity=3460465.75 spike=0.09
- PHDC.CA: score=24.4 buy_ready=True sector_rank=5 price=15.03 support=13.01 resistance=16.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=64.65 liquidity=199615696.0 spike=0.46
- PHTV.CA: score=14.28 buy_ready=False sector_rank=9 price=205.8 support=201.5 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=44.25 liquidity=1923032.25 spike=0.13
- POUL.CA: score=19.31 buy_ready=True sector_rank=8 price=37.35 support=34.06 resistance=39.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=60.39 liquidity=4950892.0 spike=0.1
- PRCL.CA: score=12.58 buy_ready=False sector_rank=14 price=26.42 support=24.26 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=93146664.0 spike=2.89
- PRDC.CA: score=16.14 buy_ready=True sector_rank=5 price=6.08 support=5.2 resistance=6.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=69.29 liquidity=1742179.63 spike=0.09
- PRMH.CA: score=21.36 buy_ready=False sector_rank=9 price=2.79 support=2.17 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=76.04 liquidity=14082240.0 spike=0.92
- RACC.CA: score=15.95 buy_ready=False sector_rank=9 price=9.87 support=9.56 resistance=12.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=57.05 liquidity=3586920.0 spike=0.11
- RAKT.CA: score=7.47 buy_ready=False sector_rank=9 price=23.79 support=22.1 resistance=25.0 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=34.57 liquidity=113287.98 spike=0.44
- RAYA.CA: score=29.4 buy_ready=True sector_rank=1 price=7.55 support=6.6 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=62.76 liquidity=34644988.0 spike=0.29
- RMDA.CA: score=31.4 buy_ready=True sector_rank=4 price=5.29 support=4.78 resistance=5.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=62.85 liquidity=1028768320.0 spike=18.33
- ROTO.CA: score=20.83 buy_ready=True sector_rank=9 price=33.86 support=32.66 resistance=36.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=43.85 liquidity=6469866.5 spike=0.5
- RREI.CA: score=26.36 buy_ready=True sector_rank=9 price=3.6 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=49.44 liquidity=13336343.0 spike=0.57
- RTVC.CA: score=5.97 buy_ready=False sector_rank=9 price=3.81 support=3.75 resistance=4.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=31.82 liquidity=1605523.5 spike=0.25
- RUBX.CA: score=6.34 buy_ready=False sector_rank=9 price=10.12 support=9.8 resistance=11.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=31.69 liquidity=2981073.5 spike=0.19
- SAUD.CA: score=16.88 buy_ready=False sector_rank=15 price=22.27 support=21.8 resistance=25.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=47.0 liquidity=5227851.0 spike=0.36
- SCEM.CA: score=17.17 buy_ready=False sector_rank=14 price=63.96 support=62.07 resistance=72.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=42.14 liquidity=5373418.5 spike=0.12
- SCFM.CA: score=8.92 buy_ready=False sector_rank=9 price=260.43 support=255.7 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=22.13 liquidity=1564136.0 spike=0.05
- SCTS.CA: score=8.51 buy_ready=False sector_rank=13 price=615.04 support=590.01 resistance=709.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=14.59 liquidity=1669090.0 spike=0.15
- SDTI.CA: score=17.37 buy_ready=True sector_rank=9 price=46.0 support=43.4 resistance=46.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=55.97 liquidity=3014567.25 spike=0.15
- SEIG.CA: score=17.11 buy_ready=False sector_rank=9 price=187.83 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=53.14 liquidity=752755.56 spike=0.12
- SIPC.CA: score=26.36 buy_ready=True sector_rank=9 price=3.63 support=3.4 resistance=3.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=53.06 liquidity=10217614.0 spike=0.66
- SKPC.CA: score=11.88 buy_ready=False sector_rank=17 price=17.32 support=16.8 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=27.72 liquidity=56279140.0 spike=0.76
- SMFR.CA: score=9.5 buy_ready=False sector_rank=9 price=205.95 support=203.51 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=29.94 liquidity=2143296.75 spike=0.18
- SNFC.CA: score=18.41 buy_ready=False sector_rank=9 price=11.89 support=11.66 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=6054568.0 spike=0.22
- SPIN.CA: score=9.89 buy_ready=False sector_rank=7 price=14.08 support=13.69 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=40.88 liquidity=494635.88 spike=0.1
- SPMD.CA: score=26.42 buy_ready=True sector_rank=9 price=0.43 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=66.96 liquidity=24586538.0 spike=1.03
- SUGR.CA: score=19.95 buy_ready=True sector_rank=8 price=49.5 support=48.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=36.46 liquidity=3590109.75 spike=0.22
- SVCE.CA: score=22.36 buy_ready=False sector_rank=9 price=8.87 support=7.98 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=42.27 liquidity=32877080.0 spike=0.23
- SWDY.CA: score=23.65 buy_ready=True sector_rank=6 price=87.99 support=85.25 resistance=91.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=55.17 liquidity=9253719.0 spike=0.26
- TALM.CA: score=13.17 buy_ready=False sector_rank=13 price=15.85 support=15.12 resistance=17.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=40.94 liquidity=1326128.5 spike=0.1
- TMGH.CA: score=22.4 buy_ready=False sector_rank=5 price=96.21 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=57.55 liquidity=177601408.0 spike=0.33
- TRTO.CA: score=10.36 buy_ready=False sector_rank=9 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=5.42 buy_ready=False sector_rank=9 price=475.42 support=455.6 resistance=508.0 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=30.99 liquidity=1382521.4 spike=1.34
- UEGC.CA: score=26.72 buy_ready=False sector_rank=9 price=1.46 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=28827416.0 spike=1.18
- UNIP.CA: score=21.67 buy_ready=False sector_rank=9 price=0.32 support=0.28 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=78.46 liquidity=9308928.0 spike=0.6
- UNIT.CA: score=20.4 buy_ready=True sector_rank=5 price=13.98 support=10.83 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=62.8 liquidity=3995815.5 spike=0.4
- WCDF.CA: score=7.72 buy_ready=False sector_rank=9 price=539.21 support=535.0 resistance=559.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=15.04 liquidity=364395.31 spike=0.48
- WKOL.CA: score=5.24 buy_ready=False sector_rank=9 price=292.48 support=290.0 resistance=339.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=30.88 liquidity=878158.25 spike=0.12
- ZEOT.CA: score=18.51 buy_ready=True sector_rank=9 price=9.21 support=8.43 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=55.41 liquidity=2146193.0 spike=0.25
- ZMID.CA: score=25.52 buy_ready=True sector_rank=5 price=6.25 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=309845344.0 spike=1.56

## Backtesting Lite
- RMDA.CA: 180d return=26.65%, max drawdown=-31.33%, MA20>MA50 days last20=20, as_of=2026-06-06T21:00:00+00:00
- CCAP.CA: 180d return=120.08%, max drawdown=-25.0%, MA20>MA50 days last20=20, as_of=2026-06-06T21:00:00+00:00
- ECAP.CA: 180d return=7.11%, max drawdown=-28.16%, MA20>MA50 days last20=20, as_of=2026-06-06T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- RMDA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tenth of Ramadan Pharmaceutical Industries summary=Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- ECAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Al Ezz Ceramics & Porcelain Co. summary=Evidence rejected for ECAP.CA: source text did not clearly match ECAP.CA / Al Ezz Ceramics & Porcelain Co..
- RAYA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=523 sources=3 expected=Raya Holding summary=Raya stock maintains bullish momentum above EGP 9; Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt; Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn
  - Raya stock maintains bullish momentum above EGP 9: https://english.mubasher.info/news/4601857/Raya-stock-maintains-bullish-momentum-above-EGP-9/
  - Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt: https://english.mubasher.info/news/4577815/Aman-Holding-MSMEDA-partner-to-inject-EGP-300m-into-SMEs-across-Egypt/
  - Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn: https://english.mubasher.info/news/4564195/Raya-Holding-s-consolidated-profits-surge-in-2025-revenues-hit-EGP-63-8bn/
- MPRC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Media Production City summary=Evidence rejected for MPRC.CA: source text did not clearly match MPRC.CA / Egyptian Media Production City.
- NCCW.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Nasr Company for Civil Works summary=Nasr for Civil Works unveils EGP 150m capital increase; Arabia Investments, Nasr Company for Civil Works unveil capital hike; Nasr Company for Civil Works’ consortium signs EUR 46m agreement with Uganda
  - Nasr for Civil Works unveils EGP 150m capital increase: https://english.mubasher.info/news/4550493/Nasr-for-Civil-Works-unveils-EGP-150m-capital-increase/
  - Arabia Investments, Nasr Company for Civil Works unveil capital hike: https://english.mubasher.info/news/4284206/Arabia-Investments-Nasr-Company-for-Civil-Works-unveil-capital-hike/
  - Nasr Company for Civil Works’ consortium signs EUR 46m agreement with Uganda: https://english.mubasher.info/news/4249759/Nasr-Company-for-Civil-Works-consortium-signs-EUR-46m-agreement-with-Uganda/
- AREH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Real Estate Egyptian Consortium S.A.E summary=Real Estate Egyptian Consortium’s net profits approach EGP 2m in 9M-25; Shareholder ups stake in Real Estate Egyptian; Target for Real Estate Investment cuts stake in Real Estate Egyptian
  - Real Estate Egyptian Consortium’s net profits approach EGP 2m in 9M-25: https://english.mubasher.info/news/4528467/Real-Estate-Egyptian-Consortium-s-net-profits-approach-EGP-2m-in-9M-25/
  - Shareholder ups stake in Real Estate Egyptian: https://english.mubasher.info/news/4026301/Shareholder-ups-stake-in-Real-Estate-Egyptian/
  - Target for Real Estate Investment cuts stake in Real Estate Egyptian: https://english.mubasher.info/news/4010821/Target-for-Real-Estate-Investment-cuts-stake-in-Real-Estate-Egyptian/
- LUTS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lotus Agri Capital summary=Evidence rejected for LUTS.CA: source text did not clearly match LUTS.CA / Lotus Agri Capital.

## Warnings
- Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence rejected for ECAP.CA: source text did not clearly match ECAP.CA / Al Ezz Ceramics & Porcelain Co..
- Evidence for RAYA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for MPRC.CA: source text did not clearly match MPRC.CA / Egyptian Media Production City.
- Evidence for NCCW.CA matches the company but no source/report date was detected.
- Evidence for AREH.CA matches the company but no source/report date was detected.
- Mubasher stock page returned no evidence titles for LUTS.CA.
- No Yahoo or Mubasher evidence found for LUTS.CA.
- Evidence rejected for LUTS.CA: source text did not clearly match LUTS.CA / Lotus Agri Capital.
