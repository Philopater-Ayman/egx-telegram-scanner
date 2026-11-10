# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-11-10T19:56:11.082542+00:00
Generated Cairo: 2026-11-10 21:56
Run timing: target 15:30 Cairo | generated Cairo 2026-11-10 21:56 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-11-10 21:53

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 5
- Tradeable price/liquidity tickers: 183/185
- Top sector: Industrial Goods & Cables

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, November 09
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 84.21% / above MA50 21.05%
- EGX70 regime: BEARISH / above MA20 77.5% / above MA50 17.5%
- Sector breadth: 23.81%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- AMES.CA: liquidity=730505088.0 spike=6.34 score=24.4
- BIOC.CA: liquidity=614217408.0 spike=5.04 score=28.4
- CCAP.CA: liquidity=359285824.0 spike=0.88 score=15.33
- COMI.CA: liquidity=339587520.0 spike=0.64 score=19.28
- NIPH.CA: liquidity=254049216.0 spike=1.73 score=28.86

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- AMES.CA: spike=6.34 liquidity=730505088.0 outlook=NEUTRAL score=39.45 buy_ready=False
- GSSC.CA: spike=6.12 liquidity=8395782.0 outlook=CONSTRUCTIVE score=58.45 buy_ready=False
- PRMH.CA: spike=5.79 liquidity=28723378.0 outlook=CONSTRUCTIVE score=67.45 buy_ready=False
- OCPH.CA: spike=5.4 liquidity=24879768.0 outlook=CONSTRUCTIVE score=59.45 buy_ready=False
- EEII.CA: spike=5.28 liquidity=47589260.0 outlook=CONSTRUCTIVE score=69.45 buy_ready=False

## Sector Leaderboard
- #1 Industrial Goods & Cables: score=12.18 5d=13.18% 20d=3.44% aboveMA50=50.0%
- #2 Healthcare: score=11.58 5d=12.78% 20d=-0.05% aboveMA50=33.33%
- #3 Technology & Distribution: score=11.08 5d=12.86% 20d=-2.49% aboveMA50=0.0%
- #4 Agriculture & Food Production: score=10.99 5d=16.99% 20d=-5.26% aboveMA50=0.0%
- #5 Education: score=10.77 5d=9.06% 20d=-2.77% aboveMA50=66.67%
- #6 Food, Beverages & Tobacco: score=9.92 5d=9.31% 20d=4.17% aboveMA50=28.57%
- #7 Building Materials: score=9.65 5d=10.19% 20d=0.2% aboveMA50=33.33%
- #8 Transportation & Logistics: score=9.2 5d=6.91% 20d=-1.48% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- NIPH.CA: BULLISH_WATCH score=99 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=far above support; high short-term volatility
- RMDA.CA: BULLISH_WATCH score=99 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=far above support; close to resistance
- CIRA.CA: BULLISH_WATCH score=93 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance
- SWDY.CA: BULLISH_WATCH score=91 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended; far above support; close to resistance
- TALM.CA: BULLISH_WATCH score=87 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support
- SMFR.CA: BULLISH_WATCH score=86.45 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- SNFC.CA: BULLISH_WATCH score=84.45 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance; sector is not leading
- KZPC.CA: BULLISH_WATCH score=82.45 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; close to resistance; sector is not leading
- ALCN.CA: BULLISH_WATCH score=81.2 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- PHAR.CA: BULLISH_WATCH score=81 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=below MA50; close to resistance

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- FERC.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=20.4 buy_ready=False sector_rank=11 price=245.95 support=171.02 resistance=258.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=56.28 liquidity=15631649.0 spike=0.89
- ABUK.CA: score=11.64 buy_ready=False sector_rank=19 price=74.19 support=73.6 resistance=95.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=22.88 liquidity=253824224.0 spike=2.29
- ACAMD.CA: score=19.4 buy_ready=False sector_rank=11 price=2.0 support=1.86 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=46.94 liquidity=41620856.0 spike=0.79
- ACGC.CA: score=19.57 buy_ready=False sector_rank=13 price=13.69 support=11.6 resistance=13.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=55.01 liquidity=7091608.0 spike=1.04
- ADCI.CA: score=25.4 buy_ready=False sector_rank=11 price=267.76 support=221.0 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:25 PM market time freshness=DELAYED_CURRENT RSI=55.12 liquidity=10061679.0 spike=4.26
- ADIB.CA: score=20.28 buy_ready=False sector_rank=15 price=48.4 support=43.16 resistance=50.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=58.31 liquidity=53210288.0 spike=0.65
- ADPC.CA: score=17.07 buy_ready=False sector_rank=11 price=3.08 support=2.53 resistance=3.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=48.48 liquidity=7669688.5 spike=0.98
- AFDI.CA: score=14.67 buy_ready=False sector_rank=11 price=45.55 support=34.8 resistance=51.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=45.88 liquidity=3688489.75 spike=1.29
- AFMC.CA: score=23.86 buy_ready=False sector_rank=11 price=144.55 support=94.6 resistance=148.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=59.92 liquidity=33548332.0 spike=1.73
- AJWA.CA: score=25.58 buy_ready=False sector_rank=11 price=262.78 support=190.2 resistance=263.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=68.42 liquidity=67385504.0 spike=2.09
- ALCN.CA: score=25.86 buy_ready=False sector_rank=8 price=32.87 support=27.11 resistance=34.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=54.1 liquidity=25640302.0 spike=2.23
- ALUM.CA: score=12.44 buy_ready=False sector_rank=11 price=20.85 support=16.02 resistance=22.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=52.95 liquidity=3041045.75 spike=0.97
- AMER.CA: score=21.62 buy_ready=False sector_rank=12 price=4.59 support=3.21 resistance=5.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=55.12 liquidity=96359544.0 spike=1.61
- AMES.CA: score=24.4 buy_ready=False sector_rank=11 price=48.58 support=28.0 resistance=53.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=72.9 liquidity=730505088.0 spike=6.34
- AMIA.CA: score=20.98 buy_ready=False sector_rank=11 price=17.97 support=14.0 resistance=19.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=47.27 liquidity=13989075.0 spike=1.29
- AMOC.CA: score=15.19 buy_ready=False sector_rank=18 price=13.22 support=12.55 resistance=15.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=44.04 liquidity=95181112.0 spike=0.68
- APSW.CA: score=10.66 buy_ready=False sector_rank=11 price=7.6 support=7.1 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=42.13 liquidity=618673.44 spike=1.32
- ARAB.CA: score=18.44 buy_ready=False sector_rank=12 price=0.25 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=46.4 liquidity=92212176.0 spike=1.02
- ARCC.CA: score=22.4 buy_ready=False sector_rank=7 price=69.0 support=58.01 resistance=70.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=53.83 liquidity=29510100.0 spike=0.83
- AREH.CA: score=20.3 buy_ready=False sector_rank=11 price=1.13 support=0.91 resistance=1.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=11176113.0 spike=1.45
- ASCM.CA: score=16.66 buy_ready=False sector_rank=11 price=47.83 support=38.2 resistance=53.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:25 PM market time freshness=DELAYED_CURRENT RSI=50.94 liquidity=7262814.5 spike=0.91
- ASPI.CA: score=20.92 buy_ready=False sector_rank=11 price=0.33 support=0.27 resistance=0.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=50.34 liquidity=35822372.0 spike=1.76
- ATLC.CA: score=21.02 buy_ready=False sector_rank=16 price=5.06 support=3.93 resistance=5.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:26 PM market time freshness=DELAYED_CURRENT RSI=48.0 liquidity=14030422.0 spike=1.69
- ATQA.CA: score=19.06 buy_ready=False sector_rank=19 price=10.16 support=8.25 resistance=12.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=43.07 liquidity=44781876.0 spike=0.93
- AXPH.CA: score=17.49 buy_ready=False sector_rank=11 price=1356.39 support=1135.0 resistance=1449.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=54.1 liquidity=6431836.5 spike=1.33
- BINV.CA: score=1.95 buy_ready=False sector_rank=17 price=53.64 support=50.62 resistance=62.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=33.43 liquidity=1625423.25 spike=0.19
- BIOC.CA: score=28.4 buy_ready=False sector_rank=11 price=388.81 support=212.05 resistance=415.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=68.1 liquidity=614217408.0 spike=5.04
- BTFH.CA: score=16.64 buy_ready=False sector_rank=16 price=2.41 support=2.05 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=36.79 liquidity=63574264.0 spike=0.53
- CAED.CA: score=21.82 buy_ready=False sector_rank=11 price=101.43 support=64.0 resistance=111.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=53.94 liquidity=29625206.0 spike=1.71
- CANA.CA: score=23.28 buy_ready=False sector_rank=15 price=48.74 support=38.1 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=67.9 liquidity=14259921.0 spike=0.77
- CCAP.CA: score=15.33 buy_ready=False sector_rank=17 price=5.96 support=5.55 resistance=6.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=38.78 liquidity=359285824.0 spike=0.88
- CCRS.CA: score=21.4 buy_ready=False sector_rank=11 price=2.1 support=1.3 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:25 PM market time freshness=DELAYED_CURRENT RSI=54.48 liquidity=14905524.0 spike=1.5
- CEFM.CA: score=15.12 buy_ready=False sector_rank=11 price=123.84 support=97.79 resistance=129.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=51.48 liquidity=2502737.0 spike=1.11
- CERA.CA: score=17.4 buy_ready=False sector_rank=11 price=1.11 support=0.93 resistance=1.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=38.0 liquidity=45052164.0 spike=0.54
- CFGH.CA: score=0.4 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-11-08T22:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=1542.9 spike=0.35
- CICH.CA: score=8.82 buy_ready=False sector_rank=16 price=10.51 support=9.63 resistance=11.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:26 PM market time freshness=DELAYED_CURRENT RSI=43.58 liquidity=2178434.0 spike=0.93
- CIEB.CA: score=14.89 buy_ready=False sector_rank=15 price=22.74 support=21.35 resistance=23.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:14 PM market time freshness=DELAYED_CURRENT RSI=51.45 liquidity=5609583.0 spike=0.68
- CIRA.CA: score=27.0 buy_ready=False sector_rank=5 price=38.4 support=32.01 resistance=38.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=58.69 liquidity=22903236.0 spike=1.8
- CLHO.CA: score=26.4 buy_ready=False sector_rank=2 price=14.38 support=12.51 resistance=14.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=54.88 liquidity=161459520.0 spike=3.64
- CNFN.CA: score=22.98 buy_ready=False sector_rank=16 price=4.19 support=3.25 resistance=4.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=52.72 liquidity=18469092.0 spike=2.17
- COMI.CA: score=19.28 buy_ready=False sector_rank=15 price=128.12 support=117.41 resistance=129.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=53.35 liquidity=339587520.0 spike=0.64
- COPR.CA: score=23.34 buy_ready=False sector_rank=11 price=0.43 support=0.33 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:14 PM market time freshness=DELAYED_CURRENT RSI=47.69 liquidity=40511280.0 spike=2.47
- COSG.CA: score=15.76 buy_ready=False sector_rank=11 price=1.36 support=1.11 resistance=1.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=46.77 liquidity=6359520.5 spike=0.68
- CPCI.CA: score=16.38 buy_ready=False sector_rank=11 price=594.39 support=502.25 resistance=620.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=54.15 liquidity=6418852.0 spike=1.28
- CSAG.CA: score=15.79 buy_ready=False sector_rank=8 price=35.06 support=30.1 resistance=37.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:25 PM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=5385617.0 spike=0.75
- DAPH.CA: score=21.7 buy_ready=False sector_rank=11 price=90.34 support=65.2 resistance=103.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=55.11 liquidity=39896084.0 spike=1.65
- DEIN.CA: score=9.4 buy_ready=False sector_rank=11 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=29 October 12:10 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=62.1 spike=0.02
- DOMT.CA: score=25.77 buy_ready=False sector_rank=6 price=25.14 support=20.27 resistance=25.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=62.99 liquidity=6705774.5 spike=3.33
- DSCW.CA: score=19.9 buy_ready=False sector_rank=11 price=1.54 support=1.23 resistance=1.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=49.23 liquidity=17772492.0 spike=1.25
- DTPP.CA: score=12.4 buy_ready=False sector_rank=11 price=49.15 support=36.0 resistance=71.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=33.25 liquidity=20971396.0 spike=0.68
- EALR.CA: score=14.97 buy_ready=False sector_rank=11 price=305.2 support=236.01 resistance=324.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:26 PM market time freshness=DELAYED_CURRENT RSI=51.19 liquidity=5566642.0 spike=0.93
- EASB.CA: score=25.4 buy_ready=False sector_rank=11 price=6.82 support=5.03 resistance=7.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=48.72 liquidity=26490548.0 spike=4.0
- EAST.CA: score=22.4 buy_ready=False sector_rank=6 price=33.12 support=27.01 resistance=33.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=69.86 liquidity=16051316.0 spike=0.44
- EBSC.CA: score=24.4 buy_ready=False sector_rank=11 price=1.58 support=1.2 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=52.44 liquidity=14733094.0 spike=3.83
- ECAP.CA: score=14.46 buy_ready=False sector_rank=11 price=28.73 support=24.8 resistance=30.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=53.34 liquidity=4023317.0 spike=1.52
- EDFM.CA: score=11.91 buy_ready=False sector_rank=11 price=365.19 support=312.92 resistance=370.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:07 PM market time freshness=DELAYED_CURRENT RSI=52.7 liquidity=1312555.13 spike=1.1
- EEII.CA: score=29.4 buy_ready=False sector_rank=11 price=2.12 support=1.42 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=62.75 liquidity=47589260.0 spike=5.28
- EFIC.CA: score=20.22 buy_ready=False sector_rank=19 price=169.17 support=121.0 resistance=174.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:14 PM market time freshness=DELAYED_CURRENT RSI=56.24 liquidity=30015898.0 spike=1.08
- EFID.CA: score=21.4 buy_ready=False sector_rank=6 price=19.69 support=16.01 resistance=19.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=55.99 liquidity=16368410.0 spike=0.44
- EFIH.CA: score=25.4 buy_ready=False sector_rank=9 price=24.7 support=20.3 resistance=24.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=53.05 liquidity=42508984.0 spike=0.74
- EGAL.CA: score=20.12 buy_ready=False sector_rank=19 price=314.03 support=275.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=58.83 liquidity=161038448.0 spike=1.53
- EGAS.CA: score=11.79 buy_ready=False sector_rank=18 price=49.39 support=43.0 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=43.71 liquidity=2603009.0 spike=0.67
- EGBE.CA: score=6.28 buy_ready=False sector_rank=15 price=0.49 support=0.47 resistance=0.54 source=Yahoo Finance as_of=2026-11-08T22:00:00+00:00 freshness=FRESH RSI=44.19 liquidity=602.7 spike=0.01
- EGCH.CA: score=16.06 buy_ready=False sector_rank=19 price=10.66 support=9.66 resistance=12.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=52210364.0 spike=0.94
- EGSA.CA: score=13.4 buy_ready=False sector_rank=10 price=9.0 support=8.7 resistance=9.09 source=Yahoo Finance as_of=2026-11-08T22:00:00+00:00 freshness=FRESH RSI=47.54 liquidity=3123.0 spike=0.43
- EGTS.CA: score=22.48 buy_ready=False sector_rank=12 price=13.42 support=10.19 resistance=15.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=52.65 liquidity=51054852.0 spike=2.54
- EHDR.CA: score=22.22 buy_ready=False sector_rank=11 price=2.18 support=1.8 resistance=2.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=47.22 liquidity=24134916.0 spike=2.41
- ELEC.CA: score=22.4 buy_ready=False sector_rank=1 price=1.72 support=1.34 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=46.59 liquidity=32427140.0 spike=0.61
- ELKA.CA: score=20.03 buy_ready=False sector_rank=11 price=1.54 support=1.21 resistance=1.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=53.52 liquidity=9626834.0 spike=0.74
- ELNA.CA: score=11.15 buy_ready=False sector_rank=11 price=42.96 support=33.46 resistance=42.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 01:15 PM market time freshness=DELAYED_CURRENT RSI=78.67 liquidity=732965.88 spike=1.01
- ELSH.CA: score=20.4 buy_ready=False sector_rank=11 price=11.23 support=8.57 resistance=11.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:25 PM market time freshness=DELAYED_CURRENT RSI=54.23 liquidity=11573560.0 spike=0.75
- ELWA.CA: score=0.7 buy_ready=False sector_rank=11 price=1.33 support=1.3 resistance=1.59 source=Yahoo Finance as_of=2026-11-08T22:00:00+00:00 freshness=FRESH RSI=10.0 liquidity=296297.41 spike=0.34
- EMFD.CA: score=20.4 buy_ready=False sector_rank=12 price=12.29 support=10.6 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=50.93 liquidity=19566624.0 spike=0.36
- ENGC.CA: score=23.94 buy_ready=False sector_rank=11 price=36.09 support=26.91 resistance=37.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=58.94 liquidity=22841682.0 spike=2.27
- EOSB.CA: score=11.42 buy_ready=False sector_rank=11 price=1.61 support=1.55 resistance=1.72 source=Yahoo Finance as_of=2026-11-08T22:00:00+00:00 freshness=FRESH RSI=70.0 liquidity=18743.62 spike=0.21
- EPCO.CA: score=18.86 buy_ready=False sector_rank=11 price=9.25 support=7.0 resistance=9.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=55.73 liquidity=6883186.5 spike=1.29
- EPPK.CA: score=-3.18 buy_ready=False sector_rank=11 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=23.4 buy_ready=False sector_rank=10 price=133.72 support=115.0 resistance=148.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=88820416.0 spike=0.37
- ETRS.CA: score=17.42 buy_ready=False sector_rank=11 price=10.9 support=9.51 resistance=11.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=53.87 liquidity=4022344.25 spike=0.31
- EXPA.CA: score=19.28 buy_ready=False sector_rank=15 price=14.5 support=12.0 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=52.18 liquidity=13198954.0 spike=0.55
- FAIT.CA: score=17.79 buy_ready=False sector_rank=15 price=44.86 support=40.0 resistance=46.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:25 PM market time freshness=DELAYED_CURRENT RSI=46.55 liquidity=3681095.0 spike=1.41
- FAITA.CA: score=7.82 buy_ready=False sector_rank=15 price=0.99 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:13 PM market time freshness=DELAYED_CURRENT RSI=54.46 liquidity=59850.36 spike=1.74
- FWRY.CA: score=19.4 buy_ready=False sector_rank=9 price=17.52 support=15.27 resistance=18.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=40.38 liquidity=68816952.0 spike=0.69
- GBCO.CA: score=8.71 buy_ready=False sector_rank=20 price=23.05 support=20.9 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=26.27 liquidity=103496592.0 spike=0.9
- GDWA.CA: score=19.4 buy_ready=False sector_rank=11 price=0.57 support=0.46 resistance=0.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=46.93 liquidity=10708713.0 spike=0.88
- GGCC.CA: score=17.5 buy_ready=False sector_rank=11 price=0.57 support=0.49 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=38.95 liquidity=22381208.0 spike=1.05
- GIHD.CA: score=20.4 buy_ready=False sector_rank=11 price=49.37 support=32.1 resistance=59.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=53.55 liquidity=13048178.0 spike=0.84
- GMCI.CA: score=12.11 buy_ready=False sector_rank=11 price=1.55 support=1.34 resistance=1.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 01:32 PM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=645809.81 spike=2.03
- GRCA.CA: score=16.01 buy_ready=False sector_rank=11 price=32.02 support=22.57 resistance=34.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=55.74 liquidity=6605336.0 spike=0.72
- GSSC.CA: score=23.8 buy_ready=False sector_rank=11 price=260.98 support=211.52 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:13 PM market time freshness=DELAYED_CURRENT RSI=48.3 liquidity=8395782.0 spike=6.12
- HDBK.CA: score=19.28 buy_ready=False sector_rank=15 price=99.46 support=83.01 resistance=105.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=54.07 liquidity=11173953.0 spike=0.47
- HELI.CA: score=20.4 buy_ready=False sector_rank=12 price=6.89 support=5.72 resistance=7.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=47.87 liquidity=44843768.0 spike=0.6
- HRHO.CA: score=16.64 buy_ready=False sector_rank=16 price=23.71 support=21.87 resistance=25.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=40.08 liquidity=35088540.0 spike=0.7
- ICID.CA: score=11.74 buy_ready=False sector_rank=11 price=17.18 support=14.26 resistance=18.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=49.86 liquidity=1335454.88 spike=0.27
- IDRE.CA: score=16.92 buy_ready=False sector_rank=11 price=40.39 support=29.11 resistance=45.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:14 PM market time freshness=DELAYED_CURRENT RSI=48.2 liquidity=7100648.0 spike=1.21
- IFAP.CA: score=14.34 buy_ready=False sector_rank=4 price=17.74 support=15.12 resistance=19.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:13 PM market time freshness=DELAYED_CURRENT RSI=46.85 liquidity=4937053.0 spike=0.72
- INFI.CA: score=20.4 buy_ready=False sector_rank=11 price=123.99 support=93.44 resistance=138.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:26 PM market time freshness=DELAYED_CURRENT RSI=46.66 liquidity=17263176.0 spike=0.81
- IRON.CA: score=7.33 buy_ready=False sector_rank=19 price=24.15 support=23.13 resistance=28.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:26 PM market time freshness=DELAYED_CURRENT RSI=34.17 liquidity=6273796.0 spike=0.72
- ISMA.CA: score=22.32 buy_ready=False sector_rank=11 price=21.56 support=14.11 resistance=24.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=49.74 liquidity=23506116.0 spike=2.46
- ISMQ.CA: score=16.56 buy_ready=False sector_rank=19 price=7.43 support=5.96 resistance=7.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=47.5 liquidity=8502020.0 spike=0.64
- ISPH.CA: score=22.56 buy_ready=False sector_rank=2 price=10.47 support=9.02 resistance=11.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=47.91 liquidity=95552512.0 spike=1.58
- JUFO.CA: score=21.98 buy_ready=False sector_rank=6 price=24.82 support=21.01 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=28644386.0 spike=1.29
- KABO.CA: score=20.76 buy_ready=False sector_rank=13 price=7.18 support=5.58 resistance=8.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=38.71 liquidity=22219550.0 spike=1.18
- KWIN.CA: score=15.14 buy_ready=False sector_rank=11 price=71.2 support=44.02 resistance=76.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=55.47 liquidity=5743790.0 spike=0.66
- KZPC.CA: score=29.54 buy_ready=False sector_rank=11 price=14.55 support=11.56 resistance=14.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=59.29 liquidity=29428594.0 spike=3.07
- LCSW.CA: score=21.4 buy_ready=False sector_rank=7 price=38.45 support=28.0 resistance=39.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=67.91 liquidity=21751914.0 spike=0.98
- LUTS.CA: score=20.4 buy_ready=False sector_rank=11 price=0.77 support=0.47 resistance=0.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=56.4 liquidity=53539080.0 spike=0.86
- MAAL.CA: score=23.4 buy_ready=False sector_rank=11 price=7.0 support=4.88 resistance=10.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=42.52 liquidity=49710132.0 spike=3.91
- MASR.CA: score=20.4 buy_ready=False sector_rank=11 price=6.87 support=5.6 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=46.94 liquidity=21324338.0 spike=0.52
- MBSC.CA: score=20.54 buy_ready=False sector_rank=7 price=336.27 support=262.0 resistance=400.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=49.79 liquidity=67980944.0 spike=1.07
- MCQE.CA: score=19.66 buy_ready=False sector_rank=7 price=178.28 support=144.0 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=54.64 liquidity=60435144.0 spike=1.13
- MCRO.CA: score=19.82 buy_ready=False sector_rank=11 price=1.34 support=1.07 resistance=1.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=48.65 liquidity=51781220.0 spike=1.21
- MENA.CA: score=10.77 buy_ready=False sector_rank=12 price=5.9 support=5.45 resistance=6.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:14 PM market time freshness=DELAYED_CURRENT RSI=46.56 liquidity=1368716.88 spike=0.36
- MEPA.CA: score=12.4 buy_ready=False sector_rank=11 price=1.37 support=1.14 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=34.37 liquidity=12972174.0 spike=0.8
- MFPC.CA: score=11.44 buy_ready=False sector_rank=19 price=37.62 support=37.23 resistance=47.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=28.34 liquidity=159315184.0 spike=2.19
- MFSC.CA: score=12.23 buy_ready=False sector_rank=11 price=36.22 support=28.55 resistance=42.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:14 PM market time freshness=DELAYED_CURRENT RSI=45.66 liquidity=2490475.75 spike=1.17
- MHOT.CA: score=10.5 buy_ready=False sector_rank=14 price=15.94 support=13.0 resistance=16.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=51.63 liquidity=1212640.88 spike=0.22
- MICH.CA: score=21.07 buy_ready=False sector_rank=11 price=43.8 support=35.5 resistance=44.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=55.46 liquidity=5672400.5 spike=0.87
- MILS.CA: score=18.33 buy_ready=False sector_rank=11 price=145.0 support=94.24 resistance=171.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=49.6 liquidity=7930947.5 spike=0.91
- MIPH.CA: score=13.16 buy_ready=False sector_rank=2 price=785.75 support=610.0 resistance=810.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:12 PM market time freshness=DELAYED_CURRENT RSI=57.32 liquidity=760148.5 spike=0.23
- MOED.CA: score=17.8 buy_ready=False sector_rank=11 price=0.51 support=0.39 resistance=0.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=40.45 liquidity=16704726.0 spike=1.2
- MOIL.CA: score=7.23 buy_ready=False sector_rank=18 price=0.64 support=0.6 resistance=0.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:11 PM market time freshness=DELAYED_CURRENT RSI=40.94 liquidity=39853.0 spike=0.26
- MOIN.CA: score=25.4 buy_ready=False sector_rank=11 price=31.52 support=25.7 resistance=34.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=38438056.0 spike=5.07
- MOSC.CA: score=13.34 buy_ready=False sector_rank=11 price=267.99 support=198.01 resistance=286.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:13 PM market time freshness=DELAYED_CURRENT RSI=52.26 liquidity=2937343.5 spike=0.66
- MPCI.CA: score=23.74 buy_ready=False sector_rank=11 price=339.74 support=238.6 resistance=347.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=59.12 liquidity=178209232.0 spike=1.67
- MPCO.CA: score=22.96 buy_ready=False sector_rank=4 price=2.07 support=1.55 resistance=2.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=49.02 liquidity=199180752.0 spike=2.28
- MPRC.CA: score=23.4 buy_ready=False sector_rank=11 price=37.79 support=27.0 resistance=39.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:25 PM market time freshness=DELAYED_CURRENT RSI=56.85 liquidity=15343726.0 spike=0.79
- MTIE.CA: score=15.71 buy_ready=False sector_rank=20 price=7.07 support=6.05 resistance=8.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=44.54 liquidity=18527156.0 spike=0.91
- NAHO.CA: score=6.4 buy_ready=False sector_rank=11 price=0.12 support=0.12 resistance=0.13 source=Yahoo Finance as_of=2026-11-08T22:00:00+00:00 freshness=FRESH RSI=35.29 liquidity=4062.5 spike=0.23
- NCCW.CA: score=19.88 buy_ready=False sector_rank=11 price=5.69 support=4.05 resistance=6.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=50.3 liquidity=20065064.0 spike=1.24
- NEDA.CA: score=1.11 buy_ready=False sector_rank=11 price=2.36 support=2.26 resistance=2.6 source=Yahoo Finance as_of=2026-11-08T22:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=210009.31 spike=1.25
- NHPS.CA: score=23.3 buy_ready=False sector_rank=11 price=64.46 support=50.0 resistance=69.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:25 PM market time freshness=DELAYED_CURRENT RSI=54.64 liquidity=22785682.0 spike=2.95
- NINH.CA: score=25.4 buy_ready=False sector_rank=11 price=17.01 support=12.36 resistance=18.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=59.27 liquidity=57837804.0 spike=5.09
- NIPH.CA: score=28.86 buy_ready=False sector_rank=2 price=304.67 support=205.0 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=254049216.0 spike=1.73
- OBRI.CA: score=18.45 buy_ready=False sector_rank=11 price=24.56 support=18.11 resistance=27.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=9053797.0 spike=0.96
- OCDI.CA: score=20.4 buy_ready=False sector_rank=12 price=25.38 support=21.0 resistance=26.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=44.19 liquidity=33064888.0 spike=1.0
- OCPH.CA: score=24.4 buy_ready=False sector_rank=11 price=202.16 support=147.96 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=55.25 liquidity=24879768.0 spike=5.4
- ODIN.CA: score=21.08 buy_ready=False sector_rank=11 price=2.19 support=1.7 resistance=2.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=48.65 liquidity=13762030.0 spike=1.84
- OFH.CA: score=20.68 buy_ready=False sector_rank=11 price=0.76 support=0.61 resistance=0.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=51.02 liquidity=24288658.0 spike=1.14
- OIH.CA: score=19.33 buy_ready=False sector_rank=17 price=1.77 support=1.5 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=49.35 liquidity=38156732.0 spike=0.84
- OLFI.CA: score=14.57 buy_ready=False sector_rank=6 price=20.18 support=17.86 resistance=20.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=52.18 liquidity=5169495.5 spike=0.66
- ORAS.CA: score=4.6 buy_ready=False sector_rank=21 price=793.79 support=790.0 resistance=808.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=135690128.0 spike=1.0
- ORHD.CA: score=19.4 buy_ready=False sector_rank=12 price=10.53 support=8.5 resistance=11.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=52.67 liquidity=50780680.0 spike=0.44
- ORWE.CA: score=18.72 buy_ready=False sector_rank=13 price=25.02 support=22.2 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=44.15 liquidity=40902432.0 spike=1.16
- PHAR.CA: score=27.14 buy_ready=False sector_rank=2 price=108.21 support=90.2 resistance=109.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=54.39 liquidity=141276192.0 spike=2.37
- PHDC.CA: score=17.4 buy_ready=False sector_rank=12 price=11.95 support=10.33 resistance=13.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=39.04 liquidity=82569288.0 spike=0.68
- PHTV.CA: score=10.93 buy_ready=False sector_rank=11 price=329.93 support=300.0 resistance=343.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:06 PM market time freshness=DELAYED_CURRENT RSI=49.96 liquidity=531390.31 spike=0.39
- POUL.CA: score=20.14 buy_ready=False sector_rank=6 price=9.98 support=8.81 resistance=10.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=48.78 liquidity=121512024.0 spike=1.37
- PRCL.CA: score=20.0 buy_ready=False sector_rank=7 price=22.0 support=16.65 resistance=24.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=52.53 liquidity=22040178.0 spike=1.3
- PRDC.CA: score=20.4 buy_ready=False sector_rank=12 price=6.5 support=5.08 resistance=6.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=56.69 liquidity=13779365.0 spike=0.72
- PRMH.CA: score=26.4 buy_ready=False sector_rank=11 price=2.24 support=1.7 resistance=2.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:25 PM market time freshness=DELAYED_CURRENT RSI=61.39 liquidity=28723378.0 spike=5.79
- RACC.CA: score=13.71 buy_ready=False sector_rank=11 price=8.0 support=6.1 resistance=9.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=40.13 liquidity=4307821.5 spike=0.69
- RAKT.CA: score=7.53 buy_ready=False sector_rank=11 price=22.35 support=20.4 resistance=23.16 source=Yahoo Finance as_of=2026-11-08T22:00:00+00:00 freshness=FRESH RSI=53.99 liquidity=128870.1 spike=0.49
- RAYA.CA: score=22.98 buy_ready=False sector_rank=3 price=5.88 support=5.02 resistance=6.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=50.21 liquidity=50280036.0 spike=2.29
- RMDA.CA: score=28.48 buy_ready=False sector_rank=2 price=5.61 support=4.5 resistance=5.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=59.9 liquidity=47712232.0 spike=1.54
- ROTO.CA: score=20.58 buy_ready=False sector_rank=11 price=34.25 support=25.0 resistance=39.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:14 PM market time freshness=DELAYED_CURRENT RSI=47.52 liquidity=15025342.0 spike=1.59
- RREI.CA: score=17.91 buy_ready=False sector_rank=11 price=2.99 support=1.96 resistance=3.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=42.52 liquidity=8506284.0 spike=0.77
- RTVC.CA: score=6.81 buy_ready=False sector_rank=11 price=2.86 support=2.66 resistance=3.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=29.13 liquidity=3589866.75 spike=1.41
- RUBX.CA: score=11.4 buy_ready=False sector_rank=11 price=13.34 support=10.51 resistance=18.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=27.74 liquidity=43917836.0 spike=0.69
- SAUD.CA: score=27.28 buy_ready=False sector_rank=15 price=22.0 support=19.3 resistance=23.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:25 PM market time freshness=DELAYED_CURRENT RSI=58.22 liquidity=59374552.0 spike=3.9
- SCEM.CA: score=25.4 buy_ready=False sector_rank=7 price=96.25 support=73.9 resistance=98.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:26 PM market time freshness=DELAYED_CURRENT RSI=63.65 liquidity=29307296.0 spike=0.64
- SCFM.CA: score=15.62 buy_ready=False sector_rank=11 price=220.8 support=153.02 resistance=244.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=48.75 liquidity=4564057.0 spike=1.83
- SCTS.CA: score=17.79 buy_ready=False sector_rank=5 price=502.38 support=410.0 resistance=555.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=54.96 liquidity=6992914.5 spike=1.2
- SDTI.CA: score=24.28 buy_ready=False sector_rank=11 price=87.0 support=75.01 resistance=89.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=58.98 liquidity=25438698.0 spike=1.44
- SEIG.CA: score=18.37 buy_ready=False sector_rank=11 price=226.61 support=142.0 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=56.09 liquidity=4974660.5 spike=0.55
- SIPC.CA: score=25.38 buy_ready=False sector_rank=11 price=5.57 support=3.73 resistance=6.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=50.68 liquidity=99442512.0 spike=1.99
- SKPC.CA: score=18.06 buy_ready=False sector_rank=19 price=15.0 support=14.01 resistance=15.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=40.85 liquidity=27274284.0 spike=0.63
- SMFR.CA: score=26.82 buy_ready=False sector_rank=11 price=221.53 support=165.0 resistance=264.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:25 PM market time freshness=DELAYED_CURRENT RSI=60.1 liquidity=16994160.0 spike=2.71
- SNFC.CA: score=24.7 buy_ready=False sector_rank=11 price=11.18 support=10.08 resistance=11.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:14 PM market time freshness=DELAYED_CURRENT RSI=49.55 liquidity=13976384.0 spike=1.65
- SPIN.CA: score=25.38 buy_ready=False sector_rank=13 price=15.48 support=12.0 resistance=15.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=56.75 liquidity=21250258.0 spike=3.49
- SPMD.CA: score=17.65 buy_ready=False sector_rank=11 price=0.36 support=0.3 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=44.16 liquidity=8252739.5 spike=0.48
- SUGR.CA: score=11.98 buy_ready=False sector_rank=6 price=47.24 support=44.62 resistance=54.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=32.39 liquidity=13928243.0 spike=1.29
- SVCE.CA: score=25.5 buy_ready=False sector_rank=11 price=9.53 support=7.01 resistance=9.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=52.88 liquidity=128327432.0 spike=2.55
- SWDY.CA: score=29.76 buy_ready=False sector_rank=1 price=119.68 support=97.0 resistance=121.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=62.81 liquidity=96075408.0 spike=1.68
- TALM.CA: score=25.8 buy_ready=False sector_rank=5 price=21.01 support=17.0 resistance=22.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=59.65 liquidity=45232248.0 spike=2.2
- TMGH.CA: score=19.4 buy_ready=False sector_rank=12 price=83.48 support=76.5 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=47.48 liquidity=137302240.0 spike=0.51
- TRTO.CA: score=1.4 buy_ready=False sector_rank=11 price=0.06 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-11-08T22:00:00+00:00 freshness=FRESH RSI=23.08 liquidity=3190.23 spike=0.68
- UEFM.CA: score=10.16 buy_ready=False sector_rank=11 price=486.84 support=422.0 resistance=520.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:14 PM market time freshness=DELAYED_CURRENT RSI=51.49 liquidity=762208.94 spike=0.48
- UEGC.CA: score=19.4 buy_ready=False sector_rank=11 price=1.52 support=1.21 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=48.75 liquidity=39773616.0 spike=0.81
- UNIP.CA: score=17.27 buy_ready=False sector_rank=11 price=0.31 support=0.25 resistance=0.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=49.17 liquidity=7750018.0 spike=1.06
- UNIT.CA: score=19.79 buy_ready=False sector_rank=12 price=18.78 support=15.06 resistance=18.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:14 PM market time freshness=DELAYED_CURRENT RSI=63.25 liquidity=3249007.5 spike=1.57
- WCDF.CA: score=11.81 buy_ready=False sector_rank=11 price=531.2 support=432.5 resistance=599.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:12 PM market time freshness=DELAYED_CURRENT RSI=63.54 liquidity=1413049.25 spike=0.87
- WKOL.CA: score=8.99 buy_ready=False sector_rank=11 price=176.55 support=145.33 resistance=309.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=22.96 liquidity=6590681.0 spike=0.58
- ZEOT.CA: score=17.53 buy_ready=False sector_rank=11 price=11.4 support=7.9 resistance=12.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=53.36 liquidity=7125290.0 spike=0.81
- ZMID.CA: score=21.82 buy_ready=False sector_rank=12 price=6.82 support=5.91 resistance=7.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=47.54 liquidity=134846944.0 spike=1.71

## Backtesting Lite
- SWDY.CA: 180d return=56.66%, max drawdown=-25.52%, MA20>MA50 days last20=0, as_of=2026-11-08T22:00:00+00:00
- KZPC.CA: 180d return=43.21%, max drawdown=-27.57%, MA20>MA50 days last20=7, as_of=2026-11-08T22:00:00+00:00
- EEII.CA: 180d return=6.0%, max drawdown=-53.23%, MA20>MA50 days last20=0, as_of=2026-11-08T22:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- SWDY.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Elsewedy Electric summary=Elsewedy-Sinohydro JV signs contract for Rabigh 2 IPP expansion project; Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26; Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations
  - Elsewedy-Sinohydro JV signs contract for Rabigh 2 IPP expansion project: https://english.mubasher.info/news/4684693/Elsewedy-Sinohydro-JV-signs-contract-for-Rabigh-2-IPP-expansion-project/
  - Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26: https://english.mubasher.info/news/4614341/Elsewedy-Electric-s-consolidated-revenues-total-EGP-75-2bn-in-Q1-26/
  - Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations: https://english.mubasher.info/news/4593166/Elsewedy-Electric-accelerates-power-transformation-project-in-KSA-with-6-high-voltage-substations/
- KZPC.CA: status=OLD_ACCEPTED latest=2024-01-01 age_days=1044 sources=3 expected=Kafr El Zayat For Pesticides & Chemicals Co.(S.A.E) summary=Kafr El Zayat to set up fund with EGP 5m capital; Kafr El Zayat Pesticides targets EGP 1.73bn sales in 2024; Kafr El Zayat Pesticides’ EGM approves stock split, capital hike
  - Kafr El Zayat to set up fund with EGP 5m capital: https://english.mubasher.info/news/4201137/Kafr-El-Zayat-to-set-up-fund-with-EGP-5m-capital/
  - Kafr El Zayat Pesticides targets EGP 1.73bn sales in 2024: https://english.mubasher.info/news/4200526/Kafr-El-Zayat-Pesticides-targets-EGP-1-73bn-sales-in-2024/
  - Kafr El Zayat Pesticides’ EGM approves stock split, capital hike: https://english.mubasher.info/news/4052937/Kafr-El-Zayat-Pesticides-EGM-approves-stock-split-capital-hike/
- EEII.CA: status=OLD_ACCEPTED latest=2019-01-01 age_days=2870 sources=3 expected=Arab Engineering Industries summary=Shareholder cuts stake in Arab Engineering Industries to 9%; Arab Moltaqa cuts stake in Arab Engineering Industries; Lower sales weigh on Arab Engineering Industries’ profit in 2019
  - Shareholder cuts stake in Arab Engineering Industries to 9%: https://english.mubasher.info/news/4009461/Shareholder-cuts-stake-in-Arab-Engineering-Industries-to-9-/
  - Arab Moltaqa cuts stake in Arab Engineering Industries: https://english.mubasher.info/news/3707590/Arab-Moltaqa-cuts-stake-in-Arab-Engineering-Industries/
  - Lower sales weigh on Arab Engineering Industries’ profit in 2019: https://english.mubasher.info/news/3586813/Lower-sales-weigh-on-Arab-Engineering-Industries-profit-in-2019/
- NIPH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Nile Pharmaceuticals summary=El-Nile for Pharmaceuticals logs 155% leap in H1-25/26 net profits; Nile Pharma announces FY21/22 dividends; Nile Pharma logs EGP 90.3m profit in FY21/22
  - El-Nile for Pharmaceuticals logs 155% leap in H1-25/26 net profits: https://english.mubasher.info/news/4554358/El-Nile-for-Pharmaceuticals-logs-155-leap-in-H1-25-26-net-profits/
  - Nile Pharma announces FY21/22 dividends: https://english.mubasher.info/news/4024745/Nile-Pharma-announces-FY21-22-dividends/
  - Nile Pharma logs EGP 90.3m profit in FY21/22: https://english.mubasher.info/news/3993739/Nile-Pharma-logs-EGP-90-3m-profit-in-FY21-22/
- RMDA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tenth of Ramadan Pharmaceutical Industries summary=Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- BIOC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GlaxoSmithKline S.A.E summary=Evidence rejected for BIOC.CA: source text did not clearly match BIOC.CA / GlaxoSmithKline S.A.E.
- SAUD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=678 sources=3 expected=Al Baraka Bank Egypt summary=Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26; Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE; Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025
  - Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26: https://english.mubasher.info/news/4611927/Al-Baraka-Bank-Egypt-records-EGP-2-2bn-operating-income-in-Q1-26/
  - Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE: https://english.mubasher.info/news/4583822/Al-Baraka-Bank-Egypt-files-MTO-to-acquire-majority-stake-in-A-T-LEASE/
  - Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025: https://english.mubasher.info/news/4583458/Al-Baraka-Bank-Egypt-to-pay-EGP-1-1-share-dividends-for-2025/
- PHAR.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian International Pharmaceutical Industries summary=Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.

## Warnings
- OpenRouter API error: 404
- Evidence for SWDY.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for KZPC.CA matches the company but appears old; latest detected date is 2024-01-01.
- Evidence for EEII.CA matches the company but appears old; latest detected date is 2019-01-01.
- Evidence for NIPH.CA matches the company but no source/report date was detected.
- Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- Evidence rejected for BIOC.CA: source text did not clearly match BIOC.CA / GlaxoSmithKline S.A.E.
- Evidence for SAUD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
