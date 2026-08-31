# Telegram-First EGX Scanner Report

Scan phase: Evening tomorrow plan
Generated UTC: 2026-08-31T21:35:11.423804+00:00
Generated Cairo: 2026-09-01 00:35
Run timing: target 19:30 Cairo | generated Cairo 2026-09-01 00:35 | cron 30 16 * * 0-4
Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-09-01 00:31

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 146/189
- Top sector: Building Materials

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, August 31
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 46.67% / above MA50 66.67%
- EGX70 regime: BEARISH / above MA20 38.24% / above MA50 73.53%
- Sector breadth: 33.33%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=1247469184.0 spike=2.12 score=8.31
- COMI.CA: liquidity=1202718848.0 spike=2.48 score=22.36
- TMGH.CA: liquidity=610589888.0 spike=2.56 score=18.76
- NIPH.CA: liquidity=580211648.0 spike=1.73 score=7.86
- MPCI.CA: liquidity=540980224.0 spike=3.21 score=9.98

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 is mixed while EGX70 remains bearish, sector breadth is weak at ~33%, and the risk mode is defensive (no new buys). The scanner therefore highlights a watchlist of stocks with bullish outlooks but limited buying pressure, noting liquidity conditions, sector strength, and proximity to support/resistance for the next 1‑3 days.
- FAIT.CA (Banking): liquidity accumulation spike, RSI overheated, trading near 20‑day resistance – watch for a short‑term pullback.
- MCQE.CA (Building Materials – leading sector): solid liquidity, extended momentum far above support, sector strength supports upside but buying remains cautious.
- KWIN.CA (General/EGX Expansion): very high liquidity spike, price far above 20‑day support, sector not leading – upside possible if momentum holds.
- CIEB.CA (Banking): price sits just below 20‑day resistance, limited evidence, watch for a break‑out or reversal.
- SWDY.CA (Industrial Goods & Cables): liquidity cooling, RSI overheated, well above support – near‑term upside capped by resistance.

## Top Liquidity Spikes
- AJWA.CA: spike=10.75 liquidity=522743808.0 outlook=WEAK_OR_RISKY score=23.9 buy_ready=False
- EBSC.CA: spike=6.4 liquidity=59070732.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- HRHO.CA: spike=5.54 liquidity=538924864.0 outlook=WEAK_OR_RISKY score=20.11 buy_ready=False
- EAST.CA: spike=5.23 liquidity=351972320.0 outlook=WEAK_OR_RISKY score=21.74 buy_ready=False
- DAPH.CA: spike=5.0 liquidity=225695056.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Building Materials: score=11.45 5d=2.4% 20d=21.92% aboveMA50=83.33%
- #2 Textiles: score=10.55 5d=1.1% 20d=17.57% aboveMA50=100.0%
- #3 Industrial Goods & Cables: score=8.51 5d=3.47% 20d=15.32% aboveMA50=50.0%
- #4 Transportation & Logistics: score=8.33 5d=0.0% 20d=12.91% aboveMA50=100.0%
- #5 Banking & Financials: score=7.43 5d=0.59% 20d=3.58% aboveMA50=90.0%
- #6 Healthcare: score=7.26 5d=1.09% 20d=10.11% aboveMA50=83.33%
- #7 Tourism & Leisure: score=6.1 5d=-0.05% 20d=8.54% aboveMA50=0.0%
- #8 Telecommunications: score=5.19 5d=0.21% 20d=3.29% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ADIB.CA: BULLISH_WATCH score=94.43 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- MIPH.CA: BULLISH_WATCH score=94.26 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- ORWE.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- CIEB.CA: BULLISH_WATCH score=88.43 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance
- CLHO.CA: BULLISH_WATCH score=88.26 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- MCQE.CA: BULLISH_WATCH score=83 liquidity=TRADEABLE sector=LEADING risk=momentum is extended; far above support
- LCSW.CA: BULLISH_WATCH score=83 liquidity=TRADEABLE sector=LEADING risk=below MA20
- EXPA.CA: BULLISH_WATCH score=82.43 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- FAIT.CA: BULLISH_WATCH score=80.43 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=overheated RSI
- NINH.CA: BULLISH_WATCH score=79.9 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=18.56 buy_ready=False sector_rank=15 price=305.09 support=240.49 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=54.29 liquidity=10986714.0 spike=0.18
- ABUK.CA: score=6.97 buy_ready=False sector_rank=12 price=79.98 support=78.26 resistance=80.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=149807824.0 spike=1.54
- ACAMD.CA: score=10.56 buy_ready=False sector_rank=15 price=2.0 support=1.95 resistance=2.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=32.14 liquidity=33911248.0 spike=0.59
- ACGC.CA: score=22.4 buy_ready=False sector_rank=2 price=14.14 support=10.14 resistance=14.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=79.23 liquidity=11348686.0 spike=0.26
- ADCI.CA: score=21.3 buy_ready=False sector_rank=15 price=299.74 support=245.0 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=53.07 liquidity=28248640.0 spike=1.37
- ADIB.CA: score=22.42 buy_ready=False sector_rank=5 price=53.68 support=50.1 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=56.92 liquidity=120038944.0 spike=1.51
- ADPC.CA: score=15.56 buy_ready=False sector_rank=15 price=3.88 support=3.81 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=36.61 liquidity=15725827.0 spike=0.34
- AFDI.CA: score=23.56 buy_ready=False sector_rank=15 price=56.35 support=50.48 resistance=69.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=116631056.0 spike=4.02
- AFMC.CA: score=5.56 buy_ready=False sector_rank=15 price=187.11 support=175.2 resistance=217.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=65758052.0 spike=0.4
- AJWA.CA: score=20.56 buy_ready=False sector_rank=15 price=180.13 support=180.01 resistance=204.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=39.83 liquidity=522743808.0 spike=10.75
- ALCN.CA: score=19.4 buy_ready=False sector_rank=4 price=30.77 support=28.8 resistance=32.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=44.91 liquidity=25058728.0 spike=0.99
- ALUM.CA: score=19.56 buy_ready=False sector_rank=15 price=28.18 support=22.72 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=75.9 liquidity=14882982.0 spike=0.56
- AMER.CA: score=6.1 buy_ready=False sector_rank=13 price=5.73 support=5.5 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=117383296.0 spike=1.23
- AMES.CA: score=5.56 buy_ready=False sector_rank=15 price=130.73 support=128.0 resistance=140.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32591988.0 spike=0.46
- AMIA.CA: score=17.98 buy_ready=False sector_rank=15 price=19.34 support=10.6 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=83.62 liquidity=62366608.0 spike=1.21
- AMOC.CA: score=6.66 buy_ready=False sector_rank=17 price=12.15 support=11.49 resistance=12.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=241815248.0 spike=1.64
- APSW.CA: score=8.69 buy_ready=False sector_rank=15 price=8.68 support=8.41 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=37.88 liquidity=1131792.63 spike=0.71
- ARAB.CA: score=23.28 buy_ready=False sector_rank=13 price=0.26 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=70.21 liquidity=112197472.0 spike=1.32
- ARCC.CA: score=21.4 buy_ready=False sector_rank=1 price=76.69 support=55.4 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=78.66 liquidity=101095096.0 spike=1.0
- AREH.CA: score=10.56 buy_ready=False sector_rank=15 price=1.41 support=1.38 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=32.0 liquidity=10257188.0 spike=0.35
- ARVA.CA: score=5.56 buy_ready=False sector_rank=15 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=13.56 buy_ready=False sector_rank=15 price=63.74 support=61.0 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=21.86 liquidity=32823982.0 spike=0.63
- ASPI.CA: score=9.2 buy_ready=False sector_rank=15 price=0.45 support=0.45 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=110024344.0 spike=2.82
- ATLC.CA: score=20.3 buy_ready=False sector_rank=19 price=5.67 support=5.0 resistance=5.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=58.7 liquidity=20436392.0 spike=1.03
- ATQA.CA: score=20.03 buy_ready=False sector_rank=12 price=11.9 support=9.66 resistance=11.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=81.17 liquidity=92308808.0 spike=1.07
- AXPH.CA: score=20.98 buy_ready=False sector_rank=15 price=1702.93 support=1121.56 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=88.41 liquidity=18551800.0 spike=1.71
- BINV.CA: score=11.07 buy_ready=False sector_rank=9 price=52.0 support=51.33 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26822182.0 spike=4.55
- BIOC.CA: score=7.88 buy_ready=False sector_rank=15 price=340.72 support=330.42 resistance=453.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=527309088.0 spike=2.16
- BTFH.CA: score=9.24 buy_ready=False sector_rank=19 price=2.97 support=2.94 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=26.32 liquidity=78256032.0 spike=0.38
- CAED.CA: score=4.84 buy_ready=False sector_rank=15 price=140.97 support=140.12 resistance=148.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9278406.0 spike=0.18
- CANA.CA: score=19.4 buy_ready=False sector_rank=5 price=41.61 support=36.62 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=72.33 liquidity=12366760.0 spike=0.7
- CCAP.CA: score=8.31 buy_ready=False sector_rank=9 price=6.09 support=5.79 resistance=6.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1247469184.0 spike=2.12
- CCRS.CA: score=5.56 buy_ready=False sector_rank=15 price=2.6 support=2.59 resistance=2.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35331404.0 spike=0.77
- CEFM.CA: score=20.56 buy_ready=False sector_rank=15 price=143.86 support=131.03 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=62.19 liquidity=21083066.0 spike=0.68
- CERA.CA: score=15.56 buy_ready=False sector_rank=15 price=1.24 support=1.23 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=10375740.0 spike=0.71
- CFGH.CA: score=-0.29 buy_ready=False sector_rank=15 price=0.12 support=0.12 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51034.52 spike=3.05
- CICH.CA: score=5.5 buy_ready=False sector_rank=19 price=12.24 support=11.92 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:13 PM market time freshness=DELAYED_CURRENT RSI=33.86 liquidity=2258986.5 spike=0.32
- CIEB.CA: score=24.44 buy_ready=False sector_rank=5 price=25.45 support=23.75 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=57.78 liquidity=19957852.0 spike=1.52
- CIRA.CA: score=5.63 buy_ready=False sector_rank=14 price=32.57 support=32.1 resistance=34.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=38392348.0 spike=0.76
- CLHO.CA: score=21.74 buy_ready=False sector_rank=6 price=17.86 support=16.0 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=46.15 liquidity=72900568.0 spike=1.17
- CNFN.CA: score=13.24 buy_ready=False sector_rank=19 price=4.85 support=4.68 resistance=5.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:13 PM market time freshness=DELAYED_CURRENT RSI=31.03 liquidity=15835750.0 spike=0.78
- COMI.CA: score=22.36 buy_ready=False sector_rank=5 price=137.45 support=135.35 resistance=142.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=1202718848.0 spike=2.48
- COPR.CA: score=5.56 buy_ready=False sector_rank=15 price=0.51 support=0.5 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=56494820.0 spike=0.64
- COSG.CA: score=20.56 buy_ready=False sector_rank=15 price=1.84 support=1.6 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=35266260.0 spike=0.69
- CPCI.CA: score=15.04 buy_ready=False sector_rank=15 price=548.1 support=455.01 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=71.2 liquidity=6477872.5 spike=0.75
- CSAG.CA: score=21.4 buy_ready=False sector_rank=4 price=41.36 support=31.35 resistance=43.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=61.18 liquidity=16023695.0 spike=0.67
- DAPH.CA: score=10.56 buy_ready=False sector_rank=15 price=135.0 support=134.05 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=225695056.0 spike=5.0
- DEIN.CA: score=-4.44 buy_ready=False sector_rank=15 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=17.03 buy_ready=False sector_rank=11 price=28.41 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:13 PM market time freshness=DELAYED_CURRENT RSI=48.12 liquidity=8134152.5 spike=0.52
- DSCW.CA: score=10.56 buy_ready=False sector_rank=15 price=1.92 support=1.84 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=30.19 liquidity=44242060.0 spike=0.5
- DTPP.CA: score=18.68 buy_ready=False sector_rank=15 price=308.11 support=235.59 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=72.49 liquidity=46348284.0 spike=1.06
- EALR.CA: score=20.56 buy_ready=False sector_rank=15 price=395.05 support=364.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=57.44 liquidity=10635300.0 spike=0.22
- EASB.CA: score=23.74 buy_ready=False sector_rank=15 price=7.68 support=6.71 resistance=8.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=62.09 liquidity=12111264.0 spike=1.59
- EAST.CA: score=14.9 buy_ready=False sector_rank=11 price=36.0 support=35.0 resistance=37.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=26.87 liquidity=351972320.0 spike=5.23
- EBSC.CA: score=10.56 buy_ready=False sector_rank=15 price=2.17 support=1.97 resistance=2.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=59070732.0 spike=6.4
- ECAP.CA: score=16.84 buy_ready=False sector_rank=15 price=32.28 support=32.12 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=47.1 liquidity=23832734.0 spike=1.64
- EDFM.CA: score=11.4 buy_ready=False sector_rank=15 price=405.15 support=384.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=842269.5 spike=0.28
- EEII.CA: score=20.56 buy_ready=False sector_rank=15 price=3.02 support=2.54 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=59.12 liquidity=21520480.0 spike=0.83
- EFIC.CA: score=17.89 buy_ready=False sector_rank=12 price=199.08 support=188.01 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=45.04 liquidity=20141878.0 spike=0.41
- EFID.CA: score=5.94 buy_ready=False sector_rank=11 price=30.61 support=30.3 resistance=31.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=91508256.0 spike=1.02
- EFIH.CA: score=19.05 buy_ready=False sector_rank=10 price=22.9 support=22.15 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=55.71 liquidity=87049816.0 spike=0.79
- EGAL.CA: score=21.29 buy_ready=False sector_rank=12 price=360.01 support=292.0 resistance=373.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=84.6 liquidity=226757904.0 spike=1.7
- EGAS.CA: score=18.38 buy_ready=False sector_rank=17 price=58.26 support=51.5 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=39.67 liquidity=18712800.0 spike=0.8
- EGBE.CA: score=9.87 buy_ready=False sector_rank=5 price=0.53 support=0.47 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=45.99 liquidity=225720.69 spike=1.12
- EGCH.CA: score=18.89 buy_ready=False sector_rank=12 price=13.81 support=12.69 resistance=14.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=37.3 liquidity=50973056.0 spike=0.42
- EGSA.CA: score=1.08 buy_ready=False sector_rank=8 price=8.69 support=8.65 resistance=8.99 source=Yahoo Finance as_of=2026-08-26T21:00:00+00:00 freshness=FRESH RSI=28.0 liquidity=0.0 spike=0.0
- EGTS.CA: score=16.1 buy_ready=False sector_rank=13 price=17.16 support=16.17 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=37.69 liquidity=42772320.0 spike=1.23
- EHDR.CA: score=18.56 buy_ready=False sector_rank=15 price=2.83 support=2.71 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=51.16 liquidity=19377698.0 spike=0.51
- EKHO.CA: score=6.38 buy_ready=False sector_rank=17 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-26T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=11.4 buy_ready=False sector_rank=3 price=2.08 support=2.04 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=30.43 liquidity=47672384.0 spike=0.86
- ELKA.CA: score=20.98 buy_ready=False sector_rank=15 price=1.83 support=1.69 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=78620984.0 spike=1.21
- ELNA.CA: score=-4.18 buy_ready=False sector_rank=15 price=37.01 support=36.1 resistance=39.24 source=Yahoo Finance as_of=2026-08-25T21:00:00+00:00 freshness=STALE RSI=42.95 liquidity=263104.08 spike=0.73
- ELSH.CA: score=11.9 buy_ready=False sector_rank=15 price=13.52 support=12.97 resistance=14.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=29.44 liquidity=90565520.0 spike=1.67
- ELWA.CA: score=16.87 buy_ready=False sector_rank=15 price=1.87 support=1.62 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=64.29 liquidity=4792313.0 spike=2.26
- EMFD.CA: score=10.64 buy_ready=False sector_rank=13 price=13.0 support=12.76 resistance=13.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=327131552.0 spike=4.01
- ENGC.CA: score=18.56 buy_ready=False sector_rank=15 price=43.4 support=40.11 resistance=54.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=47.68 liquidity=13711687.0 spike=0.5
- EOSB.CA: score=6.02 buy_ready=False sector_rank=15 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-08-25T21:00:00+00:00 freshness=STALE RSI=50.0 liquidity=137492.75 spike=2.16
- EPCO.CA: score=15.59 buy_ready=False sector_rank=15 price=11.17 support=10.32 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=7028924.5 spike=0.38
- EPPK.CA: score=3.55 buy_ready=False sector_rank=15 price=12.01 support=12.01 resistance=12.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2989728.25 spike=3.97
- ETEL.CA: score=22.94 buy_ready=False sector_rank=8 price=114.44 support=102.75 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=63.91 liquidity=254786976.0 spike=1.93
- ETRS.CA: score=20.56 buy_ready=False sector_rank=15 price=11.06 support=10.36 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=59.9 liquidity=17509422.0 spike=0.58
- EXPA.CA: score=22.2 buy_ready=False sector_rank=5 price=20.96 support=19.75 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=40.71 liquidity=51790268.0 spike=1.4
- FAIT.CA: score=26.76 buy_ready=False sector_rank=5 price=43.0 support=36.1 resistance=45.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=71.18 liquidity=16810952.0 spike=2.68
- FAITA.CA: score=14.58 buy_ready=False sector_rank=5 price=0.99 support=0.97 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:13 PM market time freshness=DELAYED_CURRENT RSI=67.07 liquidity=121500.09 spike=2.53
- FERC.CA: score=14.99 buy_ready=False sector_rank=12 price=77.44 support=75.01 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=49.2 liquidity=7103282.5 spike=0.4
- FWRY.CA: score=21.05 buy_ready=False sector_rank=10 price=18.9 support=18.69 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=37.58 liquidity=495544128.0 spike=3.99
- GBCO.CA: score=8.28 buy_ready=False sector_rank=21 price=28.9 support=27.51 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=34.46 liquidity=26405124.0 spike=0.53
- GDWA.CA: score=11.56 buy_ready=False sector_rank=15 price=0.81 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=34.07 liquidity=31381106.0 spike=0.5
- GGCC.CA: score=6.82 buy_ready=False sector_rank=15 price=0.87 support=0.86 resistance=0.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=74006392.0 spike=1.63
- GIHD.CA: score=8.12 buy_ready=False sector_rank=15 price=69.09 support=64.31 resistance=74.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=59560976.0 spike=2.28
- GMCI.CA: score=-8.16 buy_ready=False sector_rank=15 price=1.91 support=1.83 resistance=2.06 source=Yahoo Finance as_of=2026-08-25T21:00:00+00:00 freshness=STALE RSI=18.18 liquidity=281497.71 spike=0.6
- GRCA.CA: score=6.08 buy_ready=False sector_rank=15 price=78.97 support=78.9 resistance=85.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=64135508.0 spike=1.26
- GSSC.CA: score=17.79 buy_ready=False sector_rank=15 price=282.02 support=274.0 resistance=301.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=57.55 liquidity=9229412.0 spike=0.48
- GTWL.CA: score=6.06 buy_ready=False sector_rank=15 price=234.0 support=230.27 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=310305472.0 spike=1.25
- HDBK.CA: score=10.46 buy_ready=False sector_rank=5 price=105.18 support=96.5 resistance=106.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=125821528.0 spike=3.03
- HELI.CA: score=13.64 buy_ready=False sector_rank=13 price=7.76 support=7.34 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=34.81 liquidity=149244064.0 spike=0.93
- HRHO.CA: score=14.24 buy_ready=False sector_rank=19 price=25.67 support=25.49 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=19.76 liquidity=538924864.0 spike=5.54
- ICID.CA: score=17.56 buy_ready=False sector_rank=15 price=16.67 support=7.85 resistance=18.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=93.01 liquidity=10676814.0 spike=0.39
- IDRE.CA: score=20.56 buy_ready=False sector_rank=15 price=53.5 support=46.04 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=48.09 liquidity=15646025.0 spike=0.86
- IFAP.CA: score=18.38 buy_ready=False sector_rank=16 price=20.51 support=19.0 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=48.21 liquidity=25575474.0 spike=0.87
- INFI.CA: score=20.56 buy_ready=False sector_rank=15 price=152.44 support=104.0 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=62.24 liquidity=29524316.0 spike=0.42
- IRON.CA: score=10.79 buy_ready=False sector_rank=12 price=30.02 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=33.23 liquidity=17212938.0 spike=1.45
- ISMA.CA: score=5.56 buy_ready=False sector_rank=15 price=34.71 support=34.51 resistance=38.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19862974.0 spike=0.73
- ISMQ.CA: score=15.89 buy_ready=False sector_rank=12 price=9.13 support=8.96 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=49.2 liquidity=24967174.0 spike=0.46
- ISPH.CA: score=14.4 buy_ready=False sector_rank=6 price=13.06 support=11.3 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=33.0 liquidity=69719064.0 spike=0.36
- JUFO.CA: score=18.9 buy_ready=False sector_rank=11 price=26.54 support=22.78 resistance=28.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=67.2 liquidity=41572732.0 spike=0.77
- KABO.CA: score=22.78 buy_ready=False sector_rank=2 price=9.44 support=7.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=72.29 liquidity=67677016.0 spike=1.69
- KWIN.CA: score=25.54 buy_ready=False sector_rank=15 price=111.43 support=84.08 resistance=118.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=69.71 liquidity=203852736.0 spike=3.49
- KZPC.CA: score=20.56 buy_ready=False sector_rank=15 price=13.0 support=8.44 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=74.34 liquidity=34347944.0 spike=0.69
- LCSW.CA: score=22.7 buy_ready=False sector_rank=1 price=34.11 support=32.12 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=36191700.0 spike=1.15
- LUTS.CA: score=5.78 buy_ready=False sector_rank=15 price=1.12 support=1.1 resistance=1.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=256544112.0 spike=1.11
- MAAL.CA: score=20.94 buy_ready=False sector_rank=15 price=9.01 support=8.32 resistance=9.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=68.6 liquidity=14437642.0 spike=1.19
- MASR.CA: score=10.74 buy_ready=False sector_rank=15 price=7.7 support=7.45 resistance=8.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=34.19 liquidity=73372088.0 spike=1.09
- MBSC.CA: score=21.4 buy_ready=False sector_rank=1 price=408.7 support=240.02 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=80.79 liquidity=36313820.0 spike=0.43
- MCQE.CA: score=26.72 buy_ready=False sector_rank=1 price=235.66 support=178.0 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=64.88 liquidity=65524096.0 spike=1.16
- MCRO.CA: score=18.56 buy_ready=False sector_rank=15 price=1.5 support=1.44 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=61801056.0 spike=0.46
- MENA.CA: score=9.72 buy_ready=False sector_rank=13 price=6.91 support=6.82 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=49.11 liquidity=4074243.0 spike=0.69
- MEPA.CA: score=5.74 buy_ready=False sector_rank=15 price=1.9 support=1.83 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35973468.0 spike=1.09
- MFPC.CA: score=7.01 buy_ready=False sector_rank=12 price=41.38 support=40.55 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=122302472.0 spike=1.56
- MFSC.CA: score=12.95 buy_ready=False sector_rank=15 price=49.85 support=46.02 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=37.16 liquidity=4390416.5 spike=0.39
- MHOT.CA: score=19.4 buy_ready=False sector_rank=7 price=18.51 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=59.58 liquidity=17368062.0 spike=0.94
- MICH.CA: score=20.56 buy_ready=False sector_rank=15 price=50.48 support=39.01 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=49.92 liquidity=14045744.0 spike=0.34
- MILS.CA: score=22.56 buy_ready=False sector_rank=15 price=206.28 support=175.0 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=60.58 liquidity=38209740.0 spike=0.45
- MIPH.CA: score=18.88 buy_ready=False sector_rank=6 price=800.08 support=733.07 resistance=828.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=54.19 liquidity=6400948.5 spike=1.54
- MOED.CA: score=7.36 buy_ready=False sector_rank=15 price=0.84 support=0.81 resistance=0.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=172524656.0 spike=1.9
- MOIL.CA: score=10.75 buy_ready=False sector_rank=17 price=0.69 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:09 PM market time freshness=DELAYED_CURRENT RSI=43.93 liquidity=378645.88 spike=0.78
- MOIN.CA: score=14.59 buy_ready=False sector_rank=15 price=33.75 support=23.11 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=40.03 liquidity=4029543.5 spike=0.12
- MOSC.CA: score=20.8 buy_ready=False sector_rank=15 price=313.26 support=283.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=74.56 liquidity=31401536.0 spike=2.12
- MPCI.CA: score=9.98 buy_ready=False sector_rank=15 price=442.07 support=409.0 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=540980224.0 spike=3.21
- MPCO.CA: score=5.38 buy_ready=False sector_rank=16 price=2.11 support=2.09 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=96402608.0 spike=0.76
- MPRC.CA: score=19.56 buy_ready=False sector_rank=15 price=43.51 support=39.5 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=42.3 liquidity=44682220.0 spike=1.5
- MTIE.CA: score=13.28 buy_ready=False sector_rank=21 price=8.49 support=8.25 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=38.33 liquidity=36139108.0 spike=0.55
- NAHO.CA: score=7.6 buy_ready=False sector_rank=15 price=0.14 support=0.1 resistance=0.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=83.93 liquidity=43915.09 spike=0.49
- NCCW.CA: score=10.56 buy_ready=False sector_rank=15 price=5.87 support=5.59 resistance=7.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=32.65 liquidity=11618699.0 spike=0.37
- NEDA.CA: score=8.31 buy_ready=False sector_rank=15 price=2.74 support=2.7 resistance=2.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=752033.88 spike=0.88
- NHPS.CA: score=20.56 buy_ready=False sector_rank=15 price=88.99 support=82.25 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=63.08 liquidity=20412724.0 spike=0.6
- NINH.CA: score=22.72 buy_ready=False sector_rank=15 price=23.52 support=21.22 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=60.4 liquidity=45991360.0 spike=1.08
- NIPH.CA: score=7.86 buy_ready=False sector_rank=6 price=347.43 support=330.0 resistance=401.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=580211648.0 spike=1.73
- OBRI.CA: score=19.02 buy_ready=False sector_rank=15 price=33.3 support=31.61 resistance=34.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=54.32 liquidity=36804668.0 spike=1.23
- OCDI.CA: score=18.64 buy_ready=False sector_rank=13 price=31.2 support=27.7 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=53.32 liquidity=76211280.0 spike=0.55
- OCPH.CA: score=16.86 buy_ready=False sector_rank=15 price=252.61 support=225.0 resistance=341.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=55.6 liquidity=26155608.0 spike=1.15
- ODIN.CA: score=5.56 buy_ready=False sector_rank=15 price=3.03 support=2.99 resistance=3.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37071416.0 spike=0.8
- OFH.CA: score=20.56 buy_ready=False sector_rank=15 price=1.05 support=0.69 resistance=1.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=92.88 liquidity=143432224.0 spike=1.5
- OIH.CA: score=20.53 buy_ready=False sector_rank=9 price=2.01 support=1.43 resistance=2.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=84.31 liquidity=173672112.0 spike=1.23
- OLFI.CA: score=15.9 buy_ready=False sector_rank=11 price=22.67 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=38.12 liquidity=36537724.0 spike=0.65
- ORAS.CA: score=4.6 buy_ready=False sector_rank=20 price=858.39 support=825.31 resistance=859.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=341813312.0 spike=1.0
- ORHD.CA: score=18.64 buy_ready=False sector_rank=13 price=41.29 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=54.6 liquidity=131782000.0 spike=0.93
- ORWE.CA: score=23.4 buy_ready=False sector_rank=2 price=26.06 support=22.55 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=44.57 liquidity=34124724.0 spike=0.43
- PHAR.CA: score=19.4 buy_ready=False sector_rank=6 price=129.74 support=95.75 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=50.89 liquidity=270716160.0 spike=0.57
- PHDC.CA: score=10.64 buy_ready=False sector_rank=13 price=14.62 support=14.32 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=32.26 liquidity=189878688.0 spike=0.82
- PHTV.CA: score=9.83 buy_ready=False sector_rank=15 price=339.88 support=312.0 resistance=447.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=51.82 liquidity=1271378.0 spike=0.47
- POUL.CA: score=20.9 buy_ready=False sector_rank=11 price=39.5 support=36.5 resistance=40.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=48.33 liquidity=25202392.0 spike=0.98
- PRCL.CA: score=9.92 buy_ready=False sector_rank=1 price=31.13 support=31.0 resistance=34.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31233014.0 spike=1.26
- PRDC.CA: score=23.6 buy_ready=False sector_rank=13 price=9.78 support=8.7 resistance=9.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=55.91 liquidity=149024336.0 spike=2.48
- PRMH.CA: score=7.58 buy_ready=False sector_rank=15 price=2.72 support=2.58 resistance=2.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28758642.0 spike=2.01
- RACC.CA: score=10.56 buy_ready=False sector_rank=15 price=9.5 support=9.7 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=33.62 liquidity=17515168.0 spike=0.91
- RAKT.CA: score=1.83 buy_ready=False sector_rank=15 price=22.11 support=21.4 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:03 PM market time freshness=DELAYED_CURRENT RSI=9.2 liquidity=572274.81 spike=1.85
- RAYA.CA: score=17.38 buy_ready=False sector_rank=18 price=7.1 support=6.95 resistance=7.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=48.76 liquidity=74232600.0 spike=1.04
- RMDA.CA: score=19.4 buy_ready=False sector_rank=6 price=6.03 support=5.08 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=44.65 liquidity=59854068.0 spike=0.49
- ROTO.CA: score=17.04 buy_ready=False sector_rank=15 price=44.11 support=41.85 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=42.26 liquidity=8480744.0 spike=0.39
- RREI.CA: score=18.56 buy_ready=False sector_rank=15 price=4.32 support=4.24 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=16879698.0 spike=0.24
- RTVC.CA: score=14.39 buy_ready=False sector_rank=15 price=4.2 support=3.73 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=65.56 liquidity=3832599.25 spike=0.48
- RUBX.CA: score=22.6 buy_ready=False sector_rank=15 price=12.8 support=12.02 resistance=13.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=56.46 liquidity=18305692.0 spike=1.02
- SAUD.CA: score=16.0 buy_ready=False sector_rank=5 price=22.92 support=21.4 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=58.06 liquidity=6603164.5 spike=0.32
- SCEM.CA: score=22.4 buy_ready=False sector_rank=1 price=97.06 support=76.75 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=66.83 liquidity=131261624.0 spike=0.61
- SCFM.CA: score=18.61 buy_ready=False sector_rank=15 price=283.05 support=273.1 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=57.99 liquidity=8048254.0 spike=0.38
- SCTS.CA: score=14.05 buy_ready=False sector_rank=14 price=617.43 support=603.13 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=67.15 liquidity=3421352.25 spike=0.38
- SDTI.CA: score=20.56 buy_ready=False sector_rank=15 price=69.01 support=57.05 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=57.07 liquidity=10820455.0 spike=0.33
- SEIG.CA: score=10.15 buy_ready=False sector_rank=15 price=260.25 support=242.1 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=38.79 liquidity=1585516.5 spike=0.18
- SIPC.CA: score=20.56 buy_ready=False sector_rank=15 price=4.87 support=3.82 resistance=5.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=56.57 liquidity=21335486.0 spike=0.34
- SKPC.CA: score=23.83 buy_ready=False sector_rank=12 price=17.74 support=15.61 resistance=18.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=61.93 liquidity=105120336.0 spike=1.47
- SMFR.CA: score=15.28 buy_ready=False sector_rank=15 price=259.76 support=228.88 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=27.06 liquidity=9719936.0 spike=0.37
- SNFC.CA: score=9.56 buy_ready=False sector_rank=15 price=10.39 support=10.3 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=30.77 liquidity=13253756.0 spike=0.92
- SPIN.CA: score=23.4 buy_ready=False sector_rank=2 price=19.48 support=15.3 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=67.57 liquidity=15272424.0 spike=0.37
- SPMD.CA: score=8.21 buy_ready=False sector_rank=15 price=0.45 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=31.58 liquidity=7646940.0 spike=0.27
- SUGR.CA: score=21.18 buy_ready=False sector_rank=11 price=56.92 support=46.47 resistance=61.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=74.09 liquidity=60691760.0 spike=1.14
- SVCE.CA: score=20.56 buy_ready=False sector_rank=15 price=10.91 support=9.1 resistance=12.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=72.82 liquidity=71251328.0 spike=0.7
- SWDY.CA: score=24.4 buy_ready=False sector_rank=3 price=125.95 support=91.8 resistance=133.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=71.92 liquidity=56944072.0 spike=0.55
- TALM.CA: score=19.05 buy_ready=False sector_rank=14 price=17.71 support=17.2 resistance=20.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=43.98 liquidity=56284512.0 spike=1.21
- TMGH.CA: score=18.76 buy_ready=False sector_rank=13 price=95.22 support=95.2 resistance=99.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=41.6 liquidity=610589888.0 spike=2.56
- TRTO.CA: score=5.56 buy_ready=False sector_rank=15 price=0.05 support=0.03 resistance=0.05 source=Yahoo Finance as_of=2026-08-25T21:00:00+00:00 freshness=STALE RSI=50.0 liquidity=3617.48 spike=0.32
- UEFM.CA: score=10.1 buy_ready=False sector_rank=15 price=540.83 support=531.0 resistance=589.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 12:56 PM market time freshness=DELAYED_CURRENT RSI=41.99 liquidity=1541355.5 spike=0.34
- UEGC.CA: score=7.92 buy_ready=False sector_rank=15 price=1.84 support=1.8 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=89180360.0 spike=2.18
- UNIP.CA: score=15.56 buy_ready=False sector_rank=15 price=0.37 support=0.35 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=38.68 liquidity=15564366.0 spike=0.46
- UNIT.CA: score=10.87 buy_ready=False sector_rank=13 price=18.7 support=17.32 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=54.98 liquidity=2221856.75 spike=0.18
- WCDF.CA: score=9.25 buy_ready=False sector_rank=15 price=648.98 support=571.0 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=78.7 liquidity=1686778.0 spike=0.38
- WKOL.CA: score=19.51 buy_ready=False sector_rank=15 price=344.63 support=311.0 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=60.05 liquidity=6954586.0 spike=0.2
- ZEOT.CA: score=15.16 buy_ready=False sector_rank=15 price=13.76 support=12.1 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=70.11 liquidity=6596365.5 spike=0.26
- ZMID.CA: score=20.04 buy_ready=False sector_rank=13 price=8.93 support=7.06 resistance=8.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=31 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=75.47 liquidity=301728608.0 spike=1.2

## Backtesting Lite
- FAIT.CA: 180d return=41.2%, max drawdown=-8.36%, MA20>MA50 days last20=19, as_of=2026-08-25T21:00:00+00:00
- MCQE.CA: 180d return=87.38%, max drawdown=-17.56%, MA20>MA50 days last20=17, as_of=2026-08-25T21:00:00+00:00
- KWIN.CA: 180d return=62.43%, max drawdown=-34.04%, MA20>MA50 days last20=20, as_of=2026-08-25T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- FAIT.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=607 sources=3 expected=Faisal Islamic Bank of Egypt summary=Faisal Islamic Bank of Egypt unveils dividends for 2025; Faisal Islamic Bank of Egypt’s consolidated net profits drop to EGP 4.6bn in 2025; Faisal Islamic Bank of Egypt posts 63% lower standalone net profits in 2025
  - Faisal Islamic Bank of Egypt unveils dividends for 2025: https://english.mubasher.info/news/4585552/Faisal-Islamic-Bank-of-Egypt-unveils-dividends-for-2025/
  - Faisal Islamic Bank of Egypt’s consolidated net profits drop to EGP 4.6bn in 2025: https://english.mubasher.info/news/4582812/Faisal-Islamic-Bank-of-Egypt-s-consolidated-net-profits-drop-to-EGP-4-6bn-in-2025/
  - Faisal Islamic Bank of Egypt posts 63% lower standalone net profits in 2025: https://english.mubasher.info/news/4548875/Faisal-Islamic-Bank-of-Egypt-posts-63-lower-standalone-net-profits-in-2025/
- MCQE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=607 sources=3 expected=Misr Cement Qena summary=Misr Cement to distribute EGP 10/shr dividends for 2025; Misr Cement stock is testing technical level ahead of historical peak – Analysis; Misr Cement witnesses 3,254% remarkable jump in 9M-25 consolidated net profits
  - Misr Cement to distribute EGP 10/shr dividends for 2025: https://english.mubasher.info/news/4586191/Misr-Cement-to-distribute-EGP-10-shr-dividends-for-2025/
  - Misr Cement stock is testing technical level ahead of historical peak – Analysis: https://english.mubasher.info/news/4560306/Misr-Cement-stock-is-testing-technical-level-ahead-of-historical-peak-Analysis/
  - Misr Cement witnesses 3,254% remarkable jump in 9M-25 consolidated net profits: https://english.mubasher.info/news/4524754/Misr-Cement-witnesses-3-254-remarkable-jump-in-9M-25-consolidated-net-profits/
- KWIN.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Kahera El Watania Investment summary=ADIB Egypt&#39;s Cairo National unveils equity reduction transaction worth over EGP 3m; El Kahera El Watania to buy stake in Assiut for Agricultural Development; Tycoon Holding acquires 85% of Alexandria National Investment
  - ADIB Egypt&#39;s Cairo National unveils equity reduction transaction worth over EGP 3m: https://english.mubasher.info/news/4546852/ADIB-Egypt-s-Cairo-National-unveils-equity-reduction-transaction-worth-over-EGP-3m/
  - El Kahera El Watania to buy stake in Assiut for Agricultural Development: https://english.mubasher.info/news/4009433/El-Kahera-El-Watania-to-buy-stake-in-Assiut-for-Agricultural-Development/
  - Tycoon Holding acquires 85% of Alexandria National Investment: https://english.mubasher.info/news/3844623/Tycoon-Holding-acquires-85-of-Alexandria-National-Investment/
- CIEB.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Credit Agricole Egypt summary=Evidence rejected for CIEB.CA: source text did not clearly match CIEB.CA / Credit Agricole Egypt.
- SWDY.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Elsewedy Electric summary=Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26; Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations; Elsewedy Electric’s subsidiary leads expansion of SAL project at Riyadh airport
  - Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26: https://english.mubasher.info/news/4614341/Elsewedy-Electric-s-consolidated-revenues-total-EGP-75-2bn-in-Q1-26/
  - Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations: https://english.mubasher.info/news/4593166/Elsewedy-Electric-accelerates-power-transformation-project-in-KSA-with-6-high-voltage-substations/
  - Elsewedy Electric’s subsidiary leads expansion of SAL project at Riyadh airport: https://english.mubasher.info/news/4580464/Elsewedy-Electric-s-subsidiary-leads-expansion-of-SAL-project-at-Riyadh-airport/
- SKPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Sidi Kerir Petrochemicals summary=Evidence rejected for SKPC.CA: source text did not clearly match SKPC.CA / Sidi Kerir Petrochemicals.
- EASB.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Arabian Company (Themar) for securities Brokerage EAC summary=Evidence rejected for EASB.CA: source text did not clearly match EASB.CA / Egyptian Arabian Company (Themar) for securities Brokerage EAC.
- PRDC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Pioneers Properties For Urban Development summary=Evidence rejected for PRDC.CA: source text did not clearly match PRDC.CA / Pioneers Properties For Urban Development.

## Warnings
- Evidence for FAIT.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for MCQE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for KWIN.CA matches the company but no source/report date was detected.
- Evidence rejected for CIEB.CA: source text did not clearly match CIEB.CA / Credit Agricole Egypt.
- Evidence for SWDY.CA matches the company but no source/report date was detected.
- Evidence rejected for SKPC.CA: source text did not clearly match SKPC.CA / Sidi Kerir Petrochemicals.
- Evidence rejected for EASB.CA: source text did not clearly match EASB.CA / Egyptian Arabian Company (Themar) for securities Brokerage EAC.
- Evidence rejected for PRDC.CA: source text did not clearly match PRDC.CA / Pioneers Properties For Urban Development.
