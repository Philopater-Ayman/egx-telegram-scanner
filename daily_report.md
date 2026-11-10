# Telegram-First EGX Scanner Report

Scan phase: Evening tomorrow plan
Generated UTC: 2026-11-10T00:23:53.180979+00:00
Generated Cairo: 2026-11-10 02:23
Run timing: target 19:30 Cairo | generated Cairo 2026-11-10 02:23 | cron 30 16 * * 0-4
Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-11-10 02:20

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 169/187
- Top sector: Telecommunications

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, November 09
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 77.78% / above MA50 16.67%
- EGX70 regime: BEARISH / above MA20 74.29% / above MA50 20.0%
- Sector breadth: 19.05%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- AMES.CA: liquidity=730505088.0 spike=8.82 score=10.93
- BIOC.CA: liquidity=614217408.0 spike=6.23 score=27.93
- GTWL.CA: liquidity=438486784.0 spike=2.19 score=8.31
- CCAP.CA: liquidity=359285824.0 spike=0.86 score=14.63
- COMI.CA: liquidity=339587520.0 spike=0.63 score=18.63

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- AMES.CA: spike=8.82 liquidity=730505088.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GSSC.CA: spike=8.4 liquidity=8395782.0 outlook=CONSTRUCTIVE score=60.83 buy_ready=False
- EGSA.CA: spike=7.93 liquidity=56394.0 outlook=CONSTRUCTIVE score=58 buy_ready=False
- PRMH.CA: spike=7.89 liquidity=28723378.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EEII.CA: spike=7.03 liquidity=47589260.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=13.77 5d=6.12% 20d=-4.54% aboveMA50=100.0%
- #2 Industrial Goods & Cables: score=9.59 5d=9.05% 20d=-1.51% aboveMA50=50.0%
- #3 Education: score=9.21 5d=4.41% 20d=-1.47% aboveMA50=66.67%
- #4 Building Materials: score=7.91 5d=8.17% 20d=-2.08% aboveMA50=33.33%
- #5 Transportation & Logistics: score=7.61 5d=4.11% 20d=-3.65% aboveMA50=50.0%
- #6 Food, Beverages & Tobacco: score=7.54 5d=5.2% 20d=0.13% aboveMA50=28.57%
- #7 Healthcare: score=6.32 5d=4.25% 20d=-5.08% aboveMA50=16.67%
- #8 Tourism & Leisure: score=5.42 5d=6.27% 20d=-1.87% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- TALM.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=far above support
- CIRA.CA: BULLISH_WATCH score=94.21 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=close to resistance
- SWDY.CA: BULLISH_WATCH score=90.59 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended; far above support; close to resistance
- DOMT.CA: BULLISH_WATCH score=87.54 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support
- SNFC.CA: BULLISH_WATCH score=86.83 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- RMDA.CA: BULLISH_WATCH score=85.32 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; close to resistance
- KZPC.CA: BULLISH_WATCH score=84.83 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- ALCN.CA: BULLISH_WATCH score=84.61 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support
- SMFR.CA: BULLISH_WATCH score=82.83 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support; sector is not leading
- SIPC.CA: BULLISH_WATCH score=76.83 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading; high short-term volatility

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=19.93 buy_ready=False sector_rank=11 price=245.95 support=171.02 resistance=259.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=58.49 liquidity=15631649.0 spike=0.91
- ABUK.CA: score=11.83 buy_ready=False sector_rank=15 price=74.19 support=76.12 resistance=95.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=34.96 liquidity=253824224.0 spike=2.52
- ACAMD.CA: score=18.93 buy_ready=False sector_rank=11 price=2.0 support=1.86 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=46.0 liquidity=41620856.0 spike=0.79
- ACGC.CA: score=16.17 buy_ready=False sector_rank=14 price=13.69 support=11.6 resistance=13.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=54.82 liquidity=7091608.0 spike=1.01
- ADCI.CA: score=24.93 buy_ready=False sector_rank=11 price=267.76 support=221.0 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:25 PM market time freshness=DELAYED_CURRENT RSI=50.89 liquidity=10061679.0 spike=5.15
- ADIB.CA: score=19.63 buy_ready=False sector_rank=12 price=48.4 support=43.16 resistance=50.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=61.37 liquidity=53210288.0 spike=0.64
- ADPC.CA: score=16.6 buy_ready=False sector_rank=11 price=3.08 support=2.53 resistance=3.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=47.69 liquidity=7669688.5 spike=0.91
- AFDI.CA: score=14.2 buy_ready=False sector_rank=11 price=45.55 support=34.8 resistance=53.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=44.32 liquidity=3688489.75 spike=1.29
- AFMC.CA: score=21.61 buy_ready=False sector_rank=11 price=144.55 support=94.6 resistance=147.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=58.23 liquidity=33548332.0 spike=1.84
- AJWA.CA: score=24.93 buy_ready=False sector_rank=11 price=262.78 support=190.2 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=67.78 liquidity=67385504.0 spike=2.0
- ALCN.CA: score=25.78 buy_ready=False sector_rank=5 price=32.87 support=27.11 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=52.65 liquidity=25640302.0 spike=2.19
- ALUM.CA: score=11.97 buy_ready=False sector_rank=11 price=20.85 support=16.02 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=53.71 liquidity=3041045.75 spike=0.96
- AMER.CA: score=21.3 buy_ready=False sector_rank=9 price=4.59 support=3.21 resistance=5.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=58.7 liquidity=96359544.0 spike=1.64
- AMES.CA: score=10.93 buy_ready=False sector_rank=11 price=48.58 support=47.21 resistance=53.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=730505088.0 spike=8.82
- AMIA.CA: score=20.31 buy_ready=False sector_rank=11 price=17.97 support=14.0 resistance=19.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=51.96 liquidity=13989075.0 spike=1.19
- AMOC.CA: score=14.51 buy_ready=False sector_rank=19 price=13.22 support=12.55 resistance=15.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=52.47 liquidity=95181112.0 spike=0.68
- APSW.CA: score=8.21 buy_ready=False sector_rank=11 price=7.6 support=7.1 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=35.9 liquidity=618673.44 spike=1.33
- ARAB.CA: score=18.02 buy_ready=False sector_rank=9 price=0.25 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=44.63 liquidity=92212176.0 spike=0.97
- ARCC.CA: score=20.4 buy_ready=False sector_rank=4 price=69.0 support=58.01 resistance=70.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=55.06 liquidity=29510100.0 spike=0.84
- AREH.CA: score=19.85 buy_ready=False sector_rank=11 price=1.13 support=0.91 resistance=1.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=11176113.0 spike=1.46
- ASCM.CA: score=16.19 buy_ready=False sector_rank=11 price=47.83 support=38.2 resistance=56.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:25 PM market time freshness=DELAYED_CURRENT RSI=50.87 liquidity=7262814.5 spike=0.88
- ASPI.CA: score=20.61 buy_ready=False sector_rank=11 price=0.33 support=0.27 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=51.33 liquidity=35822372.0 spike=1.84
- ATLC.CA: score=19.8 buy_ready=False sector_rank=20 price=5.06 support=3.93 resistance=6.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:26 PM market time freshness=DELAYED_CURRENT RSI=47.23 liquidity=14030422.0 spike=1.76
- ATQA.CA: score=18.79 buy_ready=False sector_rank=15 price=10.16 support=8.25 resistance=12.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=41.34 liquidity=44781876.0 spike=0.92
- AXPH.CA: score=17.1 buy_ready=False sector_rank=11 price=1356.39 support=1135.0 resistance=1499.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=53.83 liquidity=6431836.5 spike=1.37
- BINV.CA: score=1.25 buy_ready=False sector_rank=16 price=53.64 support=50.62 resistance=62.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=31.73 liquidity=1625423.25 spike=0.16
- BIOC.CA: score=27.93 buy_ready=False sector_rank=11 price=388.81 support=212.05 resistance=379.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=65.32 liquidity=614217408.0 spike=6.23
- BTFH.CA: score=15.28 buy_ready=False sector_rank=20 price=2.41 support=2.05 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=35.85 liquidity=63574264.0 spike=0.52
- CAED.CA: score=21.59 buy_ready=False sector_rank=11 price=101.43 support=64.0 resistance=112.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=52.45 liquidity=29625206.0 spike=1.83
- CANA.CA: score=20.63 buy_ready=False sector_rank=12 price=48.74 support=38.1 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=66.88 liquidity=14259921.0 spike=0.72
- CCAP.CA: score=14.63 buy_ready=False sector_rank=16 price=5.96 support=5.55 resistance=6.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=40.59 liquidity=359285824.0 spike=0.86
- CCRS.CA: score=21.03 buy_ready=False sector_rank=11 price=2.1 support=1.3 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:25 PM market time freshness=DELAYED_CURRENT RSI=58.33 liquidity=14905524.0 spike=1.55
- CEFM.CA: score=12.73 buy_ready=False sector_rank=11 price=123.84 support=97.79 resistance=130.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=48.44 liquidity=2502737.0 spike=1.15
- CERA.CA: score=16.93 buy_ready=False sector_rank=11 price=1.11 support=0.93 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=38.0 liquidity=45052164.0 spike=0.52
- CFGH.CA: score=1.93 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-11-07T22:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=0.0 spike=0.0
- CICH.CA: score=7.46 buy_ready=False sector_rank=20 price=10.51 support=9.63 resistance=11.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:26 PM market time freshness=DELAYED_CURRENT RSI=45.9 liquidity=2178434.0 spike=0.93
- CIEB.CA: score=14.24 buy_ready=False sector_rank=12 price=22.74 support=21.35 resistance=23.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:14 PM market time freshness=DELAYED_CURRENT RSI=53.87 liquidity=5609583.0 spike=0.65
- CIRA.CA: score=26.06 buy_ready=False sector_rank=3 price=38.4 support=32.01 resistance=38.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=59.0 liquidity=22903236.0 spike=1.83
- CLHO.CA: score=24.4 buy_ready=False sector_rank=7 price=14.38 support=12.51 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=47.44 liquidity=161459520.0 spike=4.31
- CNFN.CA: score=6.7 buy_ready=False sector_rank=20 price=4.19 support=3.91 resistance=4.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18469092.0 spike=2.21
- COMI.CA: score=18.63 buy_ready=False sector_rank=12 price=128.12 support=117.41 resistance=129.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=53.63 liquidity=339587520.0 spike=0.63
- COPR.CA: score=23.17 buy_ready=False sector_rank=11 price=0.43 support=0.33 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:14 PM market time freshness=DELAYED_CURRENT RSI=43.72 liquidity=40511280.0 spike=2.62
- COSG.CA: score=15.29 buy_ready=False sector_rank=11 price=1.36 support=1.11 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=46.77 liquidity=6359520.5 spike=0.66
- CPCI.CA: score=16.03 buy_ready=False sector_rank=11 price=594.39 support=502.25 resistance=620.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=62.12 liquidity=6418852.0 spike=1.34
- CSAG.CA: score=15.79 buy_ready=False sector_rank=5 price=35.06 support=30.1 resistance=37.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:25 PM market time freshness=DELAYED_CURRENT RSI=54.88 liquidity=5385617.0 spike=0.74
- DAPH.CA: score=21.23 buy_ready=False sector_rank=11 price=90.34 support=65.2 resistance=103.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=52.09 liquidity=39896084.0 spike=1.65
- DEIN.CA: score=8.93 buy_ready=False sector_rank=11 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=29 October 12:10 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=62.1 spike=0.02
- DOMT.CA: score=26.11 buy_ready=False sector_rank=6 price=25.14 support=20.27 resistance=24.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=56.69 liquidity=6705774.5 spike=3.61
- DSCW.CA: score=19.49 buy_ready=False sector_rank=11 price=1.54 support=1.23 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=50.75 liquidity=17772492.0 spike=1.28
- DTPP.CA: score=11.93 buy_ready=False sector_rank=11 price=49.15 support=36.0 resistance=291.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=33.08 liquidity=20971396.0 spike=0.67
- EALR.CA: score=14.5 buy_ready=False sector_rank=11 price=305.2 support=236.01 resistance=334.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:26 PM market time freshness=DELAYED_CURRENT RSI=53.06 liquidity=5566642.0 spike=0.96
- EASB.CA: score=24.93 buy_ready=False sector_rank=11 price=6.82 support=5.03 resistance=7.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=54.63 liquidity=26490548.0 spike=4.74
- EAST.CA: score=20.4 buy_ready=False sector_rank=6 price=33.12 support=27.01 resistance=33.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=67.29 liquidity=16051316.0 spike=0.43
- EBSC.CA: score=23.93 buy_ready=False sector_rank=11 price=1.58 support=1.2 resistance=1.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=50.63 liquidity=14733094.0 spike=4.64
- ECAP.CA: score=14.06 buy_ready=False sector_rank=11 price=28.73 support=24.8 resistance=30.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=54.96 liquidity=4023317.0 spike=1.55
- EDFM.CA: score=11.5 buy_ready=False sector_rank=11 price=365.19 support=312.92 resistance=373.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:07 PM market time freshness=DELAYED_CURRENT RSI=53.24 liquidity=1312555.13 spike=1.13
- EEII.CA: score=10.93 buy_ready=False sector_rank=11 price=2.12 support=1.79 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=47589260.0 spike=7.03
- EFIC.CA: score=17.99 buy_ready=False sector_rank=15 price=169.17 support=121.0 resistance=174.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:14 PM market time freshness=DELAYED_CURRENT RSI=57.39 liquidity=30015898.0 spike=1.1
- EFID.CA: score=21.4 buy_ready=False sector_rank=6 price=19.69 support=16.01 resistance=19.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=58.06 liquidity=16368410.0 spike=0.43
- EFIH.CA: score=4.57 buy_ready=False sector_rank=18 price=24.7 support=23.4 resistance=24.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42508984.0 spike=0.74
- EGAL.CA: score=20.03 buy_ready=False sector_rank=15 price=314.03 support=275.0 resistance=335.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=64.07 liquidity=161038448.0 spike=1.62
- EGAS.CA: score=11.11 buy_ready=False sector_rank=19 price=49.39 support=43.0 resistance=56.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=44.55 liquidity=2603009.0 spike=0.65
- EGBE.CA: score=5.63 buy_ready=False sector_rank=12 price=0.49 support=0.47 resistance=0.54 source=Yahoo Finance as_of=2026-11-07T22:00:00+00:00 freshness=FRESH RSI=41.3 liquidity=1739.5 spike=0.03
- EGCH.CA: score=15.79 buy_ready=False sector_rank=15 price=10.66 support=9.66 resistance=13.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=35.13 liquidity=52210364.0 spike=0.96
- EGSA.CA: score=19.46 buy_ready=False sector_rank=1 price=9.0 support=8.7 resistance=9.09 source=Yahoo Finance as_of=2026-11-07T22:00:00+00:00 freshness=FRESH RSI=63.64 liquidity=56394.0 spike=7.93
- EGTS.CA: score=22.38 buy_ready=False sector_rank=9 price=13.42 support=10.19 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=48.5 liquidity=51054852.0 spike=2.68
- EHDR.CA: score=22.17 buy_ready=False sector_rank=11 price=2.18 support=1.8 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=43.0 liquidity=24134916.0 spike=2.62
- ELEC.CA: score=21.4 buy_ready=False sector_rank=2 price=1.72 support=1.34 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=51.55 liquidity=32427140.0 spike=0.61
- ELKA.CA: score=19.56 buy_ready=False sector_rank=11 price=1.54 support=1.21 resistance=1.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=9626834.0 spike=0.73
- ELNA.CA: score=10.76 buy_ready=False sector_rank=11 price=42.96 support=33.46 resistance=41.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 01:15 PM market time freshness=DELAYED_CURRENT RSI=75.66 liquidity=732965.88 spike=1.05
- ELSH.CA: score=19.93 buy_ready=False sector_rank=11 price=11.23 support=8.57 resistance=11.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:25 PM market time freshness=DELAYED_CURRENT RSI=57.88 liquidity=11573560.0 spike=0.71
- ELWA.CA: score=5.97 buy_ready=False sector_rank=11 price=1.33 support=1.3 resistance=1.63 source=Yahoo Finance as_of=2026-11-07T22:00:00+00:00 freshness=FRESH RSI=10.0 liquidity=2435207.47 spike=2.8
- EMFD.CA: score=20.02 buy_ready=False sector_rank=9 price=12.29 support=10.6 resistance=12.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=60.08 liquidity=19566624.0 spike=0.35
- ENGC.CA: score=21.85 buy_ready=False sector_rank=11 price=36.09 support=26.91 resistance=37.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=61.02 liquidity=22841682.0 spike=2.46
- EOSB.CA: score=11.02 buy_ready=False sector_rank=11 price=1.61 support=1.55 resistance=1.72 source=Yahoo Finance as_of=2026-11-07T22:00:00+00:00 freshness=FRESH RSI=70.0 liquidity=91307.93 spike=1.0
- EPCO.CA: score=16.48 buy_ready=False sector_rank=11 price=9.25 support=7.0 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=57.25 liquidity=6883186.5 spike=1.33
- EPPK.CA: score=-3.65 buy_ready=False sector_rank=11 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=24.4 buy_ready=False sector_rank=1 price=133.72 support=115.0 resistance=148.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=39.99 liquidity=88820416.0 spike=0.37
- ETRS.CA: score=16.95 buy_ready=False sector_rank=11 price=10.9 support=9.51 resistance=11.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=61.77 liquidity=4022344.25 spike=0.28
- EXPA.CA: score=18.63 buy_ready=False sector_rank=12 price=14.5 support=12.0 resistance=15.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=54.29 liquidity=13198954.0 spike=0.54
- FAIT.CA: score=19.15 buy_ready=False sector_rank=12 price=44.86 support=40.0 resistance=46.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:25 PM market time freshness=DELAYED_CURRENT RSI=59.1 liquidity=3681095.0 spike=1.42
- FAITA.CA: score=7.21 buy_ready=False sector_rank=12 price=0.99 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:13 PM market time freshness=DELAYED_CURRENT RSI=49.45 liquidity=59850.36 spike=1.76
- FERC.CA: score=19.83 buy_ready=False sector_rank=15 price=70.96 support=53.57 resistance=77.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=54.82 liquidity=14864431.0 spike=2.02
- FWRY.CA: score=15.57 buy_ready=False sector_rank=18 price=17.52 support=15.27 resistance=18.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=40.38 liquidity=68816952.0 spike=0.67
- GBCO.CA: score=7.75 buy_ready=False sector_rank=21 price=23.05 support=20.9 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=20.6 liquidity=103496592.0 spike=0.93
- GDWA.CA: score=18.93 buy_ready=False sector_rank=11 price=0.57 support=0.46 resistance=0.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=48.05 liquidity=10708713.0 spike=0.88
- GGCC.CA: score=17.13 buy_ready=False sector_rank=11 price=0.57 support=0.49 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=36.03 liquidity=22381208.0 spike=1.1
- GIHD.CA: score=19.93 buy_ready=False sector_rank=11 price=49.37 support=32.1 resistance=60.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=50.16 liquidity=13048178.0 spike=0.84
- GMCI.CA: score=11.92 buy_ready=False sector_rank=11 price=1.55 support=1.34 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 01:32 PM market time freshness=DELAYED_CURRENT RSI=42.11 liquidity=645809.81 spike=2.17
- GRCA.CA: score=15.54 buy_ready=False sector_rank=11 price=32.02 support=22.57 resistance=36.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=57.98 liquidity=6605336.0 spike=0.73
- GSSC.CA: score=23.33 buy_ready=False sector_rank=11 price=260.98 support=211.52 resistance=279.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:13 PM market time freshness=DELAYED_CURRENT RSI=47.97 liquidity=8395782.0 spike=8.4
- GTWL.CA: score=8.31 buy_ready=False sector_rank=11 price=144.01 support=123.0 resistance=144.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=438486784.0 spike=2.19
- HDBK.CA: score=18.63 buy_ready=False sector_rank=12 price=99.46 support=83.01 resistance=107.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=56.58 liquidity=11173953.0 spike=0.46
- HELI.CA: score=20.02 buy_ready=False sector_rank=9 price=6.89 support=5.72 resistance=7.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=50.84 liquidity=44843768.0 spike=0.59
- HRHO.CA: score=13.28 buy_ready=False sector_rank=20 price=23.71 support=21.87 resistance=26.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=35088540.0 spike=0.68
- ICID.CA: score=11.27 buy_ready=False sector_rank=11 price=17.18 support=14.26 resistance=18.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=49.73 liquidity=1335454.88 spike=0.25
- IDRE.CA: score=16.45 buy_ready=False sector_rank=11 price=40.39 support=29.11 resistance=48.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:14 PM market time freshness=DELAYED_CURRENT RSI=50.92 liquidity=7100648.0 spike=1.21
- IFAP.CA: score=13.9 buy_ready=False sector_rank=10 price=17.74 support=15.12 resistance=19.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:13 PM market time freshness=DELAYED_CURRENT RSI=49.5 liquidity=4937053.0 spike=0.71
- INFI.CA: score=19.93 buy_ready=False sector_rank=11 price=123.99 support=93.44 resistance=138.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:26 PM market time freshness=DELAYED_CURRENT RSI=46.7 liquidity=17263176.0 spike=0.83
- IRON.CA: score=5.06 buy_ready=False sector_rank=15 price=24.15 support=23.13 resistance=29.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:26 PM market time freshness=DELAYED_CURRENT RSI=34.42 liquidity=6273796.0 spike=0.69
- ISMA.CA: score=9.35 buy_ready=False sector_rank=11 price=21.56 support=20.53 resistance=22.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23506116.0 spike=2.71
- ISMQ.CA: score=16.29 buy_ready=False sector_rank=15 price=7.43 support=5.96 resistance=8.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=52.27 liquidity=8502020.0 spike=0.62
- ISPH.CA: score=20.74 buy_ready=False sector_rank=7 price=10.47 support=9.02 resistance=11.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=47.47 liquidity=95552512.0 spike=1.67
- JUFO.CA: score=20.08 buy_ready=False sector_rank=6 price=24.82 support=21.01 resistance=25.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=53.64 liquidity=28644386.0 spike=1.34
- KABO.CA: score=19.22 buy_ready=False sector_rank=14 price=7.18 support=5.58 resistance=8.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=49.67 liquidity=22219550.0 spike=1.08
- KWIN.CA: score=14.68 buy_ready=False sector_rank=11 price=71.2 support=44.02 resistance=76.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=57.99 liquidity=5743790.0 spike=0.67
- KZPC.CA: score=29.93 buy_ready=False sector_rank=11 price=14.55 support=11.56 resistance=14.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=59.79 liquidity=29428594.0 spike=3.55
- LCSW.CA: score=23.4 buy_ready=False sector_rank=4 price=38.45 support=28.0 resistance=39.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=73.22 liquidity=21751914.0 spike=1.0
- LUTS.CA: score=19.93 buy_ready=False sector_rank=11 price=0.77 support=0.47 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=56.73 liquidity=53539080.0 spike=0.86
- MAAL.CA: score=22.93 buy_ready=False sector_rank=11 price=7.0 support=4.88 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=39.96 liquidity=49710132.0 spike=4.62
- MASR.CA: score=19.93 buy_ready=False sector_rank=11 price=6.87 support=5.6 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=46.2 liquidity=21324338.0 spike=0.5
- MBSC.CA: score=6.56 buy_ready=False sector_rank=4 price=336.27 support=324.0 resistance=347.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=67980944.0 spike=1.08
- MCQE.CA: score=19.66 buy_ready=False sector_rank=4 price=178.28 support=144.0 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=56.71 liquidity=60435144.0 spike=1.13
- MCRO.CA: score=19.43 buy_ready=False sector_rank=11 price=1.34 support=1.07 resistance=1.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=49.33 liquidity=51781220.0 spike=1.25
- MENA.CA: score=10.38 buy_ready=False sector_rank=9 price=5.9 support=5.45 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:14 PM market time freshness=DELAYED_CURRENT RSI=48.15 liquidity=1368716.88 spike=0.32
- MEPA.CA: score=16.93 buy_ready=False sector_rank=11 price=1.37 support=1.14 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=35.38 liquidity=12972174.0 spike=0.81
- MFPC.CA: score=16.61 buy_ready=False sector_rank=15 price=37.62 support=38.42 resistance=47.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=37.6 liquidity=159315184.0 spike=2.41
- MFSC.CA: score=11.78 buy_ready=False sector_rank=11 price=36.22 support=28.55 resistance=42.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:14 PM market time freshness=DELAYED_CURRENT RSI=47.55 liquidity=2490475.75 spike=1.18
- MHOT.CA: score=10.38 buy_ready=False sector_rank=8 price=15.94 support=13.0 resistance=16.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=52.44 liquidity=1212640.88 spike=0.19
- MICH.CA: score=18.6 buy_ready=False sector_rank=11 price=43.8 support=35.5 resistance=44.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=59.23 liquidity=5672400.5 spike=0.86
- MILS.CA: score=17.86 buy_ready=False sector_rank=11 price=145.0 support=94.24 resistance=176.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=48.4 liquidity=7930947.5 spike=0.93
- MIPH.CA: score=11.16 buy_ready=False sector_rank=7 price=785.75 support=610.0 resistance=810.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:12 PM market time freshness=DELAYED_CURRENT RSI=54.57 liquidity=760148.5 spike=0.23
- MOED.CA: score=17.35 buy_ready=False sector_rank=11 price=0.51 support=0.39 resistance=0.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=42.28 liquidity=16704726.0 spike=1.21
- MOIL.CA: score=4.55 buy_ready=False sector_rank=19 price=0.64 support=0.6 resistance=0.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:11 PM market time freshness=DELAYED_CURRENT RSI=40.13 liquidity=39853.0 spike=0.25
- MOIN.CA: score=10.93 buy_ready=False sector_rank=11 price=31.52 support=29.0 resistance=33.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=38438056.0 spike=6.46
- MOSC.CA: score=12.87 buy_ready=False sector_rank=11 price=267.99 support=198.01 resistance=286.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:13 PM market time freshness=DELAYED_CURRENT RSI=57.61 liquidity=2937343.5 spike=0.67
- MPCI.CA: score=21.33 buy_ready=False sector_rank=11 price=339.74 support=238.6 resistance=335.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=55.68 liquidity=178209232.0 spike=1.7
- MPCO.CA: score=8.86 buy_ready=False sector_rank=10 price=2.07 support=1.9 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=199180752.0 spike=2.45
- MPRC.CA: score=22.93 buy_ready=False sector_rank=11 price=37.79 support=27.0 resistance=39.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:25 PM market time freshness=DELAYED_CURRENT RSI=58.46 liquidity=15343726.0 spike=0.81
- MTIE.CA: score=14.75 buy_ready=False sector_rank=21 price=7.07 support=6.05 resistance=8.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=46.77 liquidity=18527156.0 spike=0.92
- NAHO.CA: score=5.93 buy_ready=False sector_rank=11 price=0.12 support=0.12 resistance=0.13 source=Yahoo Finance as_of=2026-11-07T22:00:00+00:00 freshness=FRESH RSI=35.29 liquidity=823.75 spike=0.05
- NCCW.CA: score=6.37 buy_ready=False sector_rank=11 price=5.69 support=5.41 resistance=5.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20065064.0 spike=1.22
- NEDA.CA: score=0.75 buy_ready=False sector_rank=11 price=2.36 support=2.26 resistance=2.62 source=Yahoo Finance as_of=2026-11-07T22:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=215444.39 spike=1.3
- NHPS.CA: score=23.57 buy_ready=False sector_rank=11 price=64.46 support=50.0 resistance=71.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:25 PM market time freshness=DELAYED_CURRENT RSI=50.55 liquidity=22785682.0 spike=3.32
- NINH.CA: score=10.93 buy_ready=False sector_rank=11 price=17.01 support=16.65 resistance=18.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=57837804.0 spike=6.36
- NIPH.CA: score=8.08 buy_ready=False sector_rank=7 price=304.67 support=290.07 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=254049216.0 spike=1.84
- OBRI.CA: score=17.99 buy_ready=False sector_rank=11 price=24.56 support=18.11 resistance=28.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=9053797.0 spike=0.95
- OCDI.CA: score=20.04 buy_ready=False sector_rank=9 price=25.38 support=21.0 resistance=26.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=51.07 liquidity=33064888.0 spike=1.01
- OCPH.CA: score=10.93 buy_ready=False sector_rank=11 price=202.16 support=189.95 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24879768.0 spike=6.95
- ODIN.CA: score=20.79 buy_ready=False sector_rank=11 price=2.19 support=1.7 resistance=2.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=46.73 liquidity=13762030.0 spike=1.93
- OFH.CA: score=20.19 buy_ready=False sector_rank=11 price=0.76 support=0.61 resistance=0.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=55.06 liquidity=24288658.0 spike=1.13
- OIH.CA: score=18.63 buy_ready=False sector_rank=16 price=1.77 support=1.5 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=50.65 liquidity=38156732.0 spike=0.83
- OLFI.CA: score=14.57 buy_ready=False sector_rank=6 price=20.18 support=17.86 resistance=21.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=51.44 liquidity=5169495.5 spike=0.63
- ORAS.CA: score=4.6 buy_ready=False sector_rank=17 price=793.79 support=790.0 resistance=808.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=135690128.0 spike=1.0
- ORHD.CA: score=19.02 buy_ready=False sector_rank=9 price=10.53 support=8.5 resistance=11.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=55.19 liquidity=50780680.0 spike=0.43
- ORWE.CA: score=17.4 buy_ready=False sector_rank=14 price=25.02 support=22.2 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=42.33 liquidity=40902432.0 spike=1.17
- PHAR.CA: score=23.56 buy_ready=False sector_rank=7 price=108.21 support=90.2 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=49.46 liquidity=141276192.0 spike=2.58
- PHDC.CA: score=17.02 buy_ready=False sector_rank=9 price=11.95 support=10.33 resistance=13.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=47.46 liquidity=82569288.0 spike=0.69
- PHTV.CA: score=10.46 buy_ready=False sector_rank=11 price=329.93 support=300.0 resistance=345.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:06 PM market time freshness=DELAYED_CURRENT RSI=44.74 liquidity=531390.31 spike=0.39
- POUL.CA: score=20.3 buy_ready=False sector_rank=6 price=9.98 support=8.81 resistance=10.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=121512024.0 spike=1.45
- PRCL.CA: score=20.12 buy_ready=False sector_rank=4 price=22.0 support=16.65 resistance=25.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:27 PM market time freshness=DELAYED_CURRENT RSI=56.9 liquidity=22040178.0 spike=1.36
- PRDC.CA: score=20.02 buy_ready=False sector_rank=9 price=6.5 support=5.08 resistance=7.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=56.69 liquidity=13779365.0 spike=0.7
- PRMH.CA: score=10.93 buy_ready=False sector_rank=11 price=2.24 support=2.01 resistance=2.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28723378.0 spike=7.89
- RACC.CA: score=13.24 buy_ready=False sector_rank=11 price=8.0 support=6.1 resistance=9.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=48.59 liquidity=4307821.5 spike=0.69
- RAKT.CA: score=5.02 buy_ready=False sector_rank=11 price=22.35 support=20.4 resistance=23.85 source=Yahoo Finance as_of=2026-11-07T22:00:00+00:00 freshness=FRESH RSI=53.99 liquidity=91299.75 spike=0.34
- RAYA.CA: score=8.45 buy_ready=False sector_rank=13 price=5.88 support=5.59 resistance=5.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=50280036.0 spike=2.48
- RMDA.CA: score=26.66 buy_ready=False sector_rank=7 price=5.61 support=4.5 resistance=5.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=61.79 liquidity=47712232.0 spike=1.63
- ROTO.CA: score=20.25 buy_ready=False sector_rank=11 price=34.25 support=25.0 resistance=41.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:14 PM market time freshness=DELAYED_CURRENT RSI=50.6 liquidity=15025342.0 spike=1.66
- RREI.CA: score=17.44 buy_ready=False sector_rank=11 price=2.99 support=1.96 resistance=3.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=40.58 liquidity=8506284.0 spike=0.77
- RTVC.CA: score=4.34 buy_ready=False sector_rank=11 price=2.86 support=2.66 resistance=3.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=28.43 liquidity=3589866.75 spike=1.41
- RUBX.CA: score=15.93 buy_ready=False sector_rank=11 price=13.34 support=10.51 resistance=18.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=35.14 liquidity=43917836.0 spike=0.67
- SAUD.CA: score=24.63 buy_ready=False sector_rank=12 price=22.0 support=19.3 resistance=23.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:25 PM market time freshness=DELAYED_CURRENT RSI=60.23 liquidity=59374552.0 spike=4.64
- SCEM.CA: score=23.4 buy_ready=False sector_rank=4 price=96.25 support=73.9 resistance=96.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:26 PM market time freshness=DELAYED_CURRENT RSI=62.26 liquidity=29307296.0 spike=0.63
- SCFM.CA: score=15.48 buy_ready=False sector_rank=11 price=220.8 support=153.02 resistance=246.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=50.31 liquidity=4564057.0 spike=1.99
- SCTS.CA: score=18.91 buy_ready=False sector_rank=3 price=502.38 support=410.0 resistance=555.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=57.05 liquidity=6992914.5 spike=1.26
- SDTI.CA: score=23.83 buy_ready=False sector_rank=11 price=87.0 support=75.01 resistance=89.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=60.44 liquidity=25438698.0 spike=1.45
- SEIG.CA: score=17.91 buy_ready=False sector_rank=11 price=226.61 support=142.0 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=56.84 liquidity=4974660.5 spike=0.57
- SIPC.CA: score=25.05 buy_ready=False sector_rank=11 price=5.57 support=3.73 resistance=6.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=49.86 liquidity=99442512.0 spike=2.06
- SKPC.CA: score=17.79 buy_ready=False sector_rank=15 price=15.0 support=14.01 resistance=15.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=49.55 liquidity=27274284.0 spike=0.61
- SMFR.CA: score=27.05 buy_ready=False sector_rank=11 price=221.53 support=165.0 resistance=264.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:25 PM market time freshness=DELAYED_CURRENT RSI=67.81 liquidity=16994160.0 spike=3.06
- SNFC.CA: score=24.35 buy_ready=False sector_rank=11 price=11.18 support=10.08 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:14 PM market time freshness=DELAYED_CURRENT RSI=46.32 liquidity=13976384.0 spike=1.71
- SPIN.CA: score=10.06 buy_ready=False sector_rank=14 price=15.48 support=14.0 resistance=15.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21250258.0 spike=4.17
- SPMD.CA: score=17.18 buy_ready=False sector_rank=11 price=0.36 support=0.3 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=39.87 liquidity=8252739.5 spike=0.47
- SUGR.CA: score=17.1 buy_ready=False sector_rank=6 price=47.24 support=44.62 resistance=54.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=40.7 liquidity=13928243.0 spike=1.35
- SVCE.CA: score=23.47 buy_ready=False sector_rank=11 price=9.53 support=7.01 resistance=10.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=53.08 liquidity=128327432.0 spike=2.77
- SWDY.CA: score=28.9 buy_ready=False sector_rank=2 price=119.68 support=97.0 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=62.13 liquidity=96075408.0 spike=1.75
- TALM.CA: score=26.54 buy_ready=False sector_rank=3 price=21.01 support=17.0 resistance=22.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=50.94 liquidity=45232248.0 spike=2.07
- TMGH.CA: score=19.02 buy_ready=False sector_rank=9 price=83.48 support=76.5 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=52.72 liquidity=137302240.0 spike=0.5
- TRTO.CA: score=1.52 buy_ready=False sector_rank=11 price=0.06 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-11-07T22:00:00+00:00 freshness=FRESH RSI=23.08 liquidity=6190.86 spike=1.29
- UEFM.CA: score=9.69 buy_ready=False sector_rank=11 price=486.84 support=422.0 resistance=520.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:14 PM market time freshness=DELAYED_CURRENT RSI=52.02 liquidity=762208.94 spike=0.46
- UEGC.CA: score=18.93 buy_ready=False sector_rank=11 price=1.52 support=1.21 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=44.0 liquidity=39773616.0 spike=0.83
- UNIP.CA: score=16.8 buy_ready=False sector_rank=11 price=0.31 support=0.25 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=48.74 liquidity=7750018.0 spike=1.06
- UNIT.CA: score=17.55 buy_ready=False sector_rank=9 price=18.78 support=15.06 resistance=18.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:14 PM market time freshness=DELAYED_CURRENT RSI=62.65 liquidity=3249007.5 spike=1.64
- WCDF.CA: score=9.35 buy_ready=False sector_rank=11 price=531.2 support=432.5 resistance=620.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:12 PM market time freshness=DELAYED_CURRENT RSI=66.37 liquidity=1413049.25 spike=0.81
- WKOL.CA: score=6.52 buy_ready=False sector_rank=11 price=176.55 support=145.33 resistance=309.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=29.72 liquidity=6590681.0 spike=0.57
- ZEOT.CA: score=17.06 buy_ready=False sector_rank=11 price=11.4 support=7.9 resistance=12.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:28 PM market time freshness=DELAYED_CURRENT RSI=58.28 liquidity=7125290.0 spike=0.81
- ZMID.CA: score=21.66 buy_ready=False sector_rank=9 price=6.82 support=5.91 resistance=7.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 November 02:29 PM market time freshness=DELAYED_CURRENT RSI=52.33 liquidity=134846944.0 spike=1.82

## Backtesting Lite
- KZPC.CA: 180d return=36.08%, max drawdown=-27.57%, MA20>MA50 days last20=8, as_of=2026-11-07T22:00:00+00:00
- SWDY.CA: 180d return=52.16%, max drawdown=-25.52%, MA20>MA50 days last20=0, as_of=2026-11-07T22:00:00+00:00
- BIOC.CA: 180d return=471.13%, max drawdown=-58.13%, MA20>MA50 days last20=0, as_of=2026-11-07T22:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- KZPC.CA: status=OLD_ACCEPTED latest=2024-01-01 age_days=1044 sources=3 expected=Kafr El Zayat For Pesticides & Chemicals Co.(S.A.E) summary=Kafr El Zayat to set up fund with EGP 5m capital; Kafr El Zayat Pesticides targets EGP 1.73bn sales in 2024; Kafr El Zayat Pesticides’ EGM approves stock split, capital hike
  - Kafr El Zayat to set up fund with EGP 5m capital: https://english.mubasher.info/news/4201137/Kafr-El-Zayat-to-set-up-fund-with-EGP-5m-capital/
  - Kafr El Zayat Pesticides targets EGP 1.73bn sales in 2024: https://english.mubasher.info/news/4200526/Kafr-El-Zayat-Pesticides-targets-EGP-1-73bn-sales-in-2024/
  - Kafr El Zayat Pesticides’ EGM approves stock split, capital hike: https://english.mubasher.info/news/4052937/Kafr-El-Zayat-Pesticides-EGM-approves-stock-split-capital-hike/
- SWDY.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Elsewedy Electric summary=Elsewedy-Sinohydro JV signs contract for Rabigh 2 IPP expansion project; Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26; Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations
  - Elsewedy-Sinohydro JV signs contract for Rabigh 2 IPP expansion project: https://english.mubasher.info/news/4684693/Elsewedy-Sinohydro-JV-signs-contract-for-Rabigh-2-IPP-expansion-project/
  - Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26: https://english.mubasher.info/news/4614341/Elsewedy-Electric-s-consolidated-revenues-total-EGP-75-2bn-in-Q1-26/
  - Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations: https://english.mubasher.info/news/4593166/Elsewedy-Electric-accelerates-power-transformation-project-in-KSA-with-6-high-voltage-substations/
- BIOC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GlaxoSmithKline S.A.E summary=Evidence rejected for BIOC.CA: source text did not clearly match BIOC.CA / GlaxoSmithKline S.A.E.
- SMFR.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Samad Misr EGYFERT.S.A.E summary=Evidence rejected for SMFR.CA: source text did not clearly match SMFR.CA / Samad Misr EGYFERT.S.A.E.
- RMDA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tenth of Ramadan Pharmaceutical Industries summary=Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- DOMT.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=678 sources=3 expected=Arabian Food Industries Domty summary=Domty posts lower consolidated net profits at EGP 161m in 2025; net sales exceed EGP 9.3bn; Selling pressure pushes Domty’s stock toward EGP 23.50–22.85; Domty unveils demerger, establishes Dairy Products Euro Arabian
  - Domty posts lower consolidated net profits at EGP 161m in 2025; net sales exceed EGP 9.3bn: https://english.mubasher.info/news/4593671/Domty-posts-lower-consolidated-net-profits-at-EGP-161m-in-2025-net-sales-exceed-EGP-9-3bn/
  - Selling pressure pushes Domty’s stock toward EGP 23.50–22.85: https://english.mubasher.info/news/4562323/Selling-pressure-pushes-Domty-s-stock-toward-EGP-23-50-22-85/
  - Domty unveils demerger, establishes Dairy Products Euro Arabian: https://english.mubasher.info/news/4543153/Domty-unveils-demerger-establishes-Dairy-Products-Euro-Arabian/
- CIRA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Investment and Real Estate Development summary=CIRA Education take over 51% of L’École Française Hurghada; CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion; CIRA Education launches Middle East’s 1st initiative for care economy
  - CIRA Education take over 51% of L’École Française Hurghada: https://english.mubasher.info/news/4488666/CIRA-Education-take-over-51-of-L-%C3%89cole-Fran%C3%A7aise-Hurghada/
  - CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion: https://english.mubasher.info/news/4393636/CIRA-s-majority-shareholder-acquires-37-5-additional-equity-backs-regional-expansion/
  - CIRA Education launches Middle East’s 1st initiative for care economy: https://english.mubasher.info/news/4391766/CIRA-Education-launches-Middle-East-s-1st-initiative-for-care-economy/

## Warnings
- OpenRouter API error: 404
- Evidence for KZPC.CA matches the company but appears old; latest detected date is 2024-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for SWDY.CA matches the company but no source/report date was detected.
- Evidence rejected for BIOC.CA: source text did not clearly match BIOC.CA / GlaxoSmithKline S.A.E.
- Evidence rejected for SMFR.CA: source text did not clearly match SMFR.CA / Samad Misr EGYFERT.S.A.E.
- Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence for DOMT.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
