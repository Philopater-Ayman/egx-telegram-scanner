# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-07-27T09:01:18.843279+00:00
Generated Cairo: 2026-07-27 12:01
Run timing: target 08:45 Cairo | generated Cairo 2026-07-27 12:01 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-07-27 11:57

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 69
- Data quality issues: 1
- Tradeable price/liquidity tickers: 178/189
- Top sector: Textiles

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, July 27
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 70.0% / above MA50 55.0%
- EGX70 regime: MIXED / above MA20 82.05% / above MA50 82.05%
- Sector breadth: 52.38%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- CCAP.CA: liquidity=283424704.0 spike=0.41 score=26.4
- PHAR.CA: liquidity=214349872.0 spike=7.44 score=14.27
- COMI.CA: liquidity=174608400.0 spike=0.43 score=24.4
- ADIB.CA: liquidity=170918192.0 spike=1.47 score=27.34
- CAED.CA: liquidity=133844600.0 spike=2.54 score=12.48

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: The local scanner highlighted a handful of EGX tickets with strong rank scores and bullish/watch outlooks, but the mixed EGX30/EGX70 regime and low confidence forced a fallback HOLD on all positions.
- Tickets were prioritized by high rank_score, constructive or bullish_watch outlooks, and liquidity regimes indicating accumulation or tradeable conditions.
- Sector strength in Textiles, Building Materials, and Industrial Goods & Cables lifted those stocks, while most remain above their 20‑day support but show varying distances to resistance.
- EGX30 and EGX70 both show mixed trends (median 5‑day returns negative, 20‑day returns positive), prompting the risk mode to SELECTIVE_SWING_TRADES_ONLY and limiting aggressive entries.
- Uncertainty remains due to overheated RSI readings, cooling liquidity spikes, and the overall mixed market regime, which reduces confidence in any breakout.

## Top Liquidity Spikes
- PHAR.CA: spike=7.44 liquidity=214349872.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AJWA.CA: spike=3.39 liquidity=48836292.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CAED.CA: spike=2.54 liquidity=133844600.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ASPI.CA: spike=2.36 liquidity=64154188.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- BIOC.CA: spike=2.35 liquidity=75205984.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Textiles: score=10.19 5d=4.36% 20d=10.26% aboveMA50=100.0%
- #2 Building Materials: score=9.83 5d=3.41% 20d=13.39% aboveMA50=83.33%
- #3 Industrial Goods & Cables: score=9.19 5d=2.93% 20d=7.02% aboveMA50=100.0%
- #4 Agriculture & Food Production: score=7.97 5d=1.81% 20d=1.8% aboveMA50=100.0%
- #5 Telecommunications: score=7.77 5d=2.4% 20d=5.67% aboveMA50=100.0%
- #6 Banking & Financials: score=7.72 5d=3.15% 20d=3.71% aboveMA50=80.0%
- #7 General / Verified EGX Expansion: score=7.72 5d=1.32% 20d=9.15% aboveMA50=78.64%
- #8 Education: score=7.7 5d=-0.32% 20d=6.79% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- IFAP.CA: BULLISH_WATCH score=90.97 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ORWE.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ARCC.CA: BULLISH_WATCH score=89.83 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- WCDF.CA: BULLISH_WATCH score=86.72 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended
- PRCL.CA: BULLISH_WATCH score=85.83 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- ECAP.CA: BULLISH_WATCH score=85.72 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- IDRE.CA: BULLISH_WATCH score=84.72 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support
- EALR.CA: BULLISH_WATCH score=83.72 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MCQE.CA: BULLISH_WATCH score=81.83 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- ICID.CA: BULLISH_WATCH score=78.72 liquidity=TRADEABLE sector=IMPROVING risk=far above support

## BUY-Ready Candidates
- IDRE.CA: rank=29.44 outlook=BULLISH_WATCH outlook_score=84.72 sector_rank=7 price=51.12 support=41.1 resistance=52.68 liquidity=34291256.0
- ELSH.CA: rank=28.4 outlook=CONSTRUCTIVE outlook_score=67.72 sector_rank=7 price=15.15 support=11.1 resistance=15.59 liquidity=34131240.0
- RMDA.CA: rank=28.35 outlook=BULLISH_WATCH outlook_score=77.68 sector_rank=14 price=5.16 support=4.81 resistance=5.17 liquidity=21285192.0
- ADIB.CA: rank=27.34 outlook=CONSTRUCTIVE outlook_score=68.72 sector_rank=6 price=51.15 support=44.1 resistance=49.87 liquidity=170918192.0
- ARCC.CA: rank=26.97 outlook=BULLISH_WATCH outlook_score=89.83 sector_rank=2 price=56.6 support=53.5 resistance=58.5 liquidity=8573137.0
- CANA.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=71.72 sector_rank=6 price=38.01 support=34.7 resistance=38.65 liquidity=11215051.0
- TMGH.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=72.28 sector_rank=10 price=99.81 support=92.1 resistance=103.87 liquidity=40845260.0
- PRCL.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=85.83 sector_rank=2 price=36.13 support=29.15 resistance=38.25 liquidity=22493718.0
- PRDC.CA: rank=26.4 outlook=CONSTRUCTIVE outlook_score=60.28 sector_rank=10 price=9.47 support=6.8 resistance=10.4 liquidity=11087577.0
- DTPP.CA: rank=26.4 outlook=CONSTRUCTIVE outlook_score=67.72 sector_rank=7 price=246.66 support=114.67 resistance=273.0 liquidity=29146038.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=26.4 buy_ready=False sector_rank=7 price=249.99 support=196.0 resistance=253.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=70.31 liquidity=13504546.0 spike=0.71
- ABUK.CA: score=22.07 buy_ready=False sector_rank=17 price=71.44 support=66.66 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=53.74 liquidity=29950776.0 spike=0.19
- ACAMD.CA: score=24.4 buy_ready=True sector_rank=7 price=2.41 support=2.14 resistance=2.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=18226510.0 spike=0.24
- ACGC.CA: score=25.67 buy_ready=False sector_rank=1 price=10.7 support=8.92 resistance=11.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=74.82 liquidity=8265016.5 spike=0.29
- ADCI.CA: score=25.22 buy_ready=True sector_rank=7 price=264.55 support=230.0 resistance=266.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=68.4 liquidity=15118312.0 spike=1.41
- ADIB.CA: score=27.34 buy_ready=True sector_rank=6 price=51.15 support=44.1 resistance=49.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=63.07 liquidity=170918192.0 spike=1.47
- ADPC.CA: score=18.84 buy_ready=False sector_rank=7 price=4.0 support=3.32 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=77.17 liquidity=7439739.0 spike=0.24
- AFDI.CA: score=24.58 buy_ready=True sector_rank=7 price=49.12 support=41.84 resistance=49.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=69.03 liquidity=15695600.0 spike=1.09
- AFMC.CA: score=11.44 buy_ready=False sector_rank=7 price=112.99 support=102.11 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=54175488.0 spike=2.02
- AJWA.CA: score=14.18 buy_ready=False sector_rank=7 price=198.49 support=182.0 resistance=198.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48836292.0 spike=3.39
- ALCN.CA: score=16.35 buy_ready=True sector_rank=13 price=29.68 support=27.7 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=69.59 liquidity=1949578.25 spike=0.09
- ALUM.CA: score=16.62 buy_ready=True sector_rank=7 price=23.73 support=20.55 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=67.09 liquidity=2219529.5 spike=0.33
- AMER.CA: score=23.4 buy_ready=False sector_rank=10 price=4.34 support=2.28 resistance=4.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=89.73 liquidity=36754528.0 spike=0.36
- AMES.CA: score=9.92 buy_ready=False sector_rank=7 price=131.89 support=118.25 resistance=136.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=124133264.0 spike=1.26
- AMIA.CA: score=16.54 buy_ready=False sector_rank=7 price=10.4 support=8.4 resistance=10.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=72.62 liquidity=2138213.5 spike=0.16
- AMOC.CA: score=24.4 buy_ready=True sector_rank=12 price=8.31 support=7.42 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=65.27 liquidity=19308112.0 spike=0.33
- APSW.CA: score=18.21 buy_ready=True sector_rank=7 price=9.06 support=8.0 resistance=9.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=55.83 liquidity=1648408.63 spike=1.08
- ARAB.CA: score=22.4 buy_ready=True sector_rank=10 price=0.25 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=52410804.0 spike=0.4
- ARCC.CA: score=26.97 buy_ready=True sector_rank=2 price=56.6 support=53.5 resistance=58.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=53.22 liquidity=8573137.0 spike=0.34
- AREH.CA: score=15.68 buy_ready=False sector_rank=7 price=1.49 support=1.44 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=41.82 liquidity=6280039.0 spike=0.19
- ARVA.CA: score=23.46 buy_ready=False sector_rank=7 price=12.31 support=10.5 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=76.51 liquidity=24637012.0 spike=1.03
- ASCM.CA: score=24.4 buy_ready=True sector_rank=7 price=61.89 support=56.29 resistance=64.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=55.41 liquidity=13019369.0 spike=0.26
- ASPI.CA: score=12.12 buy_ready=False sector_rank=7 price=0.44 support=0.39 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=64154188.0 spike=2.36
- ATLC.CA: score=12.94 buy_ready=False sector_rank=15 price=5.2 support=4.92 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=45.07 liquidity=719608.06 spike=0.1
- ATQA.CA: score=25.07 buy_ready=True sector_rank=17 price=9.91 support=9.35 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=66.09 liquidity=14455106.0 spike=0.43
- AXPH.CA: score=16.99 buy_ready=False sector_rank=7 price=1223.1 support=1075.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=55.62 liquidity=587594.31 spike=0.15
- BINV.CA: score=13.13 buy_ready=False sector_rank=9 price=47.49 support=44.98 resistance=51.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=50.94 liquidity=727369.38 spike=0.1
- BIOC.CA: score=12.1 buy_ready=False sector_rank=7 price=142.8 support=119.32 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=75205984.0 spike=2.35
- BTFH.CA: score=26.22 buy_ready=True sector_rank=15 price=3.1 support=2.91 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=57.78 liquidity=119658008.0 spike=0.58
- CAED.CA: score=12.48 buy_ready=False sector_rank=7 price=139.34 support=120.02 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=133844600.0 spike=2.54
- CANA.CA: score=26.4 buy_ready=True sector_rank=6 price=38.01 support=34.7 resistance=38.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=66.3 liquidity=11215051.0 spike=0.71
- CCAP.CA: score=26.4 buy_ready=False sector_rank=9 price=5.43 support=4.65 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=72.22 liquidity=283424704.0 spike=0.41
- CCRS.CA: score=20.28 buy_ready=True sector_rank=7 price=2.69 support=2.18 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=69.01 liquidity=5876898.0 spike=0.34
- CEFM.CA: score=25.3 buy_ready=True sector_rank=7 price=126.87 support=95.75 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=65.03 liquidity=20887622.0 spike=1.45
- CERA.CA: score=21.2 buy_ready=True sector_rank=7 price=1.37 support=1.19 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=65.79 liquidity=6799347.0 spike=0.27
- CFGH.CA: score=-0.59 buy_ready=False sector_rank=7 price=0.11 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10261.81 spike=0.7
- CICH.CA: score=18.74 buy_ready=True sector_rank=15 price=12.22 support=11.52 resistance=12.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=54.58 liquidity=2523662.75 spike=0.48
- CIEB.CA: score=16.4 buy_ready=True sector_rank=6 price=24.17 support=23.3 resistance=24.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=43.55 liquidity=1995697.88 spike=0.25
- CIRA.CA: score=24.4 buy_ready=False sector_rank=8 price=32.98 support=27.45 resistance=33.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=73.7 liquidity=23292520.0 spike=0.66
- CLHO.CA: score=24.27 buy_ready=True sector_rank=14 price=17.01 support=15.9 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=56.49 liquidity=29572858.0 spike=0.68
- CNFN.CA: score=17.43 buy_ready=True sector_rank=15 price=4.87 support=4.61 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=3207514.5 spike=0.14
- COMI.CA: score=24.4 buy_ready=True sector_rank=6 price=140.73 support=126.21 resistance=140.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=66.21 liquidity=174608400.0 spike=0.43
- COPR.CA: score=22.48 buy_ready=False sector_rank=7 price=0.42 support=0.35 resistance=0.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=83.91 liquidity=28081260.0 spike=1.04
- COSG.CA: score=19.98 buy_ready=False sector_rank=7 price=1.72 support=1.47 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=80.77 liquidity=8581643.0 spike=0.2
- CPCI.CA: score=16.52 buy_ready=False sector_rank=7 price=468.58 support=370.01 resistance=512.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=72.77 liquidity=2122129.5 spike=0.19
- CSAG.CA: score=17.58 buy_ready=True sector_rank=13 price=33.17 support=31.3 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=53.28 liquidity=1176557.0 spike=0.06
- DAPH.CA: score=23.4 buy_ready=False sector_rank=7 price=95.93 support=78.52 resistance=98.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=75.22 liquidity=13489959.0 spike=0.75
- DEIN.CA: score=-0.6 buy_ready=False sector_rank=7 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=13.69 buy_ready=False sector_rank=18 price=26.99 support=26.06 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=46.55 liquidity=623471.25 spike=0.17
- DSCW.CA: score=21.4 buy_ready=False sector_rank=7 price=1.94 support=1.71 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=87.1 liquidity=27930552.0 spike=0.55
- DTPP.CA: score=26.4 buy_ready=True sector_rank=7 price=246.66 support=114.67 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=68.78 liquidity=29146038.0 spike=0.42
- EALR.CA: score=26.4 buy_ready=True sector_rank=7 price=371.08 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=61.04 liquidity=12930020.0 spike=0.75
- EASB.CA: score=22.15 buy_ready=True sector_rank=7 price=8.0 support=6.88 resistance=8.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=61.65 liquidity=7745986.0 spike=0.5
- EAST.CA: score=19.07 buy_ready=False sector_rank=18 price=36.64 support=36.11 resistance=38.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=45.39 liquidity=17163864.0 spike=0.29
- EBSC.CA: score=12.58 buy_ready=False sector_rank=7 price=1.91 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=21.87 liquidity=3181468.5 spike=0.46
- ECAP.CA: score=19.95 buy_ready=True sector_rank=7 price=33.65 support=31.52 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=60.1 liquidity=1552224.75 spike=0.2
- EDFM.CA: score=11.88 buy_ready=False sector_rank=7 price=388.43 support=310.2 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=82.59 liquidity=481629.13 spike=0.12
- EEII.CA: score=24.4 buy_ready=True sector_rank=7 price=2.79 support=2.35 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=49.12 liquidity=14060129.0 spike=0.64
- EFIC.CA: score=10.25 buy_ready=False sector_rank=17 price=186.27 support=180.02 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=53.18 liquidity=1179020.88 spike=0.11
- EFID.CA: score=17.31 buy_ready=False sector_rank=18 price=27.61 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=42.11 liquidity=9245807.0 spike=0.23
- EFIH.CA: score=24.4 buy_ready=True sector_rank=11 price=22.97 support=20.0 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=66.05 liquidity=30065724.0 spike=0.54
- EGAL.CA: score=22.07 buy_ready=False sector_rank=17 price=300.76 support=272.28 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=56.59 liquidity=18955384.0 spike=0.44
- EGAS.CA: score=21.65 buy_ready=True sector_rank=12 price=53.87 support=46.51 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=67.8 liquidity=7254168.5 spike=0.58
- EGBE.CA: score=13.41 buy_ready=False sector_rank=6 price=0.49 support=-0.34 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=97.71 liquidity=14719.4 spike=0.57
- EGCH.CA: score=22.07 buy_ready=False sector_rank=17 price=12.9 support=12.13 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=55.68 liquidity=15672692.0 spike=0.27
- EGSA.CA: score=10.92 buy_ready=False sector_rank=5 price=8.9 support=8.67 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:03 AM market time freshness=DELAYED_CURRENT RSI=65.71 liquidity=20530.79 spike=1.25
- EGTS.CA: score=9.05 buy_ready=False sector_rank=10 price=17.62 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=31.59 liquidity=4650186.0 spike=0.1
- EHDR.CA: score=26.9 buy_ready=False sector_rank=7 price=2.99 support=2.37 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=70.33 liquidity=46346848.0 spike=1.25
- EKHO.CA: score=8.4 buy_ready=False sector_rank=12 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=24.4 buy_ready=True sector_rank=3 price=2.21 support=2.04 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=12475253.0 spike=0.19
- ELKA.CA: score=21.4 buy_ready=False sector_rank=7 price=2.04 support=1.19 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=79.21 liquidity=13831566.0 spike=0.2
- ELNA.CA: score=13.16 buy_ready=False sector_rank=7 price=38.58 support=35.55 resistance=40.5 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=54.53 liquidity=659486.55 spike=1.05
- ELSH.CA: score=28.4 buy_ready=True sector_rank=7 price=15.15 support=11.1 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=63.2 liquidity=34131240.0 spike=0.25
- ELWA.CA: score=10.5 buy_ready=False sector_rank=7 price=1.91 support=1.87 resistance=2.14 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=40.0 liquidity=1103044.08 spike=0.93
- EMFD.CA: score=24.4 buy_ready=True sector_rank=10 price=11.75 support=11.24 resistance=12.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=47.71 liquidity=12450825.0 spike=0.19
- ENGC.CA: score=16.34 buy_ready=False sector_rank=7 price=41.93 support=35.1 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=70.98 liquidity=1939916.0 spike=0.08
- EOSB.CA: score=14.41 buy_ready=False sector_rank=7 price=1.48 support=1.5 resistance=1.55 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=6979.68 spike=0.16
- EPCO.CA: score=22.26 buy_ready=False sector_rank=7 price=11.37 support=8.5 resistance=11.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=86.46 liquidity=8858782.0 spike=0.32
- EPPK.CA: score=19.13 buy_ready=False sector_rank=7 price=15.25 support=12.37 resistance=15.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=62.06 liquidity=725801.38 spike=0.54
- ETEL.CA: score=21.4 buy_ready=False sector_rank=5 price=104.19 support=89.01 resistance=106.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=77.8 liquidity=24235126.0 spike=0.32
- ETRS.CA: score=18.46 buy_ready=False sector_rank=7 price=10.78 support=10.25 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=6057769.0 spike=0.1
- EXPA.CA: score=24.4 buy_ready=False sector_rank=6 price=19.91 support=18.03 resistance=20.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=74.78 liquidity=16591431.0 spike=0.55
- FAIT.CA: score=18.42 buy_ready=True sector_rank=6 price=37.33 support=35.06 resistance=38.0 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=59.26 liquidity=2017313.3 spike=0.7
- FAITA.CA: score=10.47 buy_ready=False sector_rank=6 price=0.96 support=0.96 resistance=0.99 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=36.76 liquidity=93572.78 spike=1.99
- FERC.CA: score=24.21 buy_ready=True sector_rank=17 price=77.87 support=72.75 resistance=85.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=57.31 liquidity=11805998.0 spike=1.07
- FWRY.CA: score=23.4 buy_ready=False sector_rank=11 price=19.11 support=18.13 resistance=19.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=57.94 liquidity=22773210.0 spike=0.17
- GBCO.CA: score=18.77 buy_ready=False sector_rank=16 price=30.81 support=29.5 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=48.14 liquidity=7390084.5 spike=0.1
- GDWA.CA: score=20.4 buy_ready=False sector_rank=7 price=0.87 support=0.76 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=81.53 liquidity=80074544.0 spike=0.99
- GGCC.CA: score=23.4 buy_ready=False sector_rank=7 price=0.91 support=0.42 resistance=0.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=89.37 liquidity=27260242.0 spike=0.73
- GIHD.CA: score=23.4 buy_ready=False sector_rank=7 price=59.9 support=40.66 resistance=65.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=76.45 liquidity=13751837.0 spike=0.29
- GMCI.CA: score=15.07 buy_ready=False sector_rank=7 price=2.0 support=1.66 resistance=2.26 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=53.33 liquidity=672628.0 spike=0.5
- GRCA.CA: score=24.4 buy_ready=True sector_rank=7 price=61.21 support=48.0 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=66.01 liquidity=13905503.0 spike=0.96
- GSSC.CA: score=15.6 buy_ready=True sector_rank=7 price=266.85 support=240.0 resistance=288.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=68.87 liquidity=1199984.75 spike=0.12
- GTWL.CA: score=24.4 buy_ready=True sector_rank=7 price=102.6 support=60.0 resistance=118.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=60.62 liquidity=22936788.0 spike=0.16
- HDBK.CA: score=20.4 buy_ready=False sector_rank=6 price=82.39 support=75.3 resistance=163.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=42.05 liquidity=13997935.0 spike=0.44
- HELI.CA: score=21.4 buy_ready=False sector_rank=10 price=8.28 support=6.36 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=89.9 liquidity=39765464.0 spike=0.22
- HRHO.CA: score=24.19 buy_ready=True sector_rank=15 price=26.9 support=26.09 resistance=27.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=49.81 liquidity=8968340.0 spike=0.09
- ICID.CA: score=22.98 buy_ready=True sector_rank=7 price=8.1 support=6.55 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=52.87 liquidity=8364340.5 spike=1.11
- IDRE.CA: score=29.44 buy_ready=True sector_rank=7 price=51.12 support=41.1 resistance=52.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=63.02 liquidity=34291256.0 spike=1.52
- IFAP.CA: score=26.23 buy_ready=True sector_rank=4 price=19.82 support=18.47 resistance=20.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=57.38 liquidity=7827741.5 spike=0.88
- INFI.CA: score=23.46 buy_ready=False sector_rank=7 price=108.06 support=88.51 resistance=111.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=74.8 liquidity=9062979.0 spike=0.63
- IRON.CA: score=7.25 buy_ready=False sector_rank=17 price=31.07 support=30.45 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=29.61 liquidity=5178761.0 spike=0.78
- ISMA.CA: score=28.4 buy_ready=False sector_rank=7 price=32.35 support=26.54 resistance=31.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=70.84 liquidity=44496528.0 spike=2.0
- ISMQ.CA: score=16.07 buy_ready=False sector_rank=17 price=9.31 support=8.6 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=30.41 liquidity=16299345.0 spike=0.15
- ISPH.CA: score=23.27 buy_ready=False sector_rank=14 price=11.69 support=11.2 resistance=12.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=51.54 liquidity=14145082.0 spike=0.26
- JUFO.CA: score=18.11 buy_ready=False sector_rank=18 price=29.3 support=28.5 resistance=31.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=44.46 liquidity=23340680.0 spike=1.02
- KABO.CA: score=17.91 buy_ready=False sector_rank=1 price=8.62 support=6.04 resistance=8.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=89.21 liquidity=3508722.0 spike=0.08
- KWIN.CA: score=23.4 buy_ready=False sector_rank=7 price=99.81 support=65.0 resistance=109.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=93.14 liquidity=13633637.0 spike=0.3
- KZPC.CA: score=13.39 buy_ready=False sector_rank=7 price=8.61 support=8.26 resistance=9.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=51.69 liquidity=985827.0 spike=0.19
- LCSW.CA: score=21.0 buy_ready=False sector_rank=2 price=34.72 support=27.01 resistance=37.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=77.83 liquidity=5596058.0 spike=0.07
- LUTS.CA: score=24.4 buy_ready=True sector_rank=7 price=0.6 support=0.59 resistance=0.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=19910618.0 spike=1.0
- MAAL.CA: score=15.96 buy_ready=False sector_rank=7 price=8.92 support=6.78 resistance=8.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=83.78 liquidity=4558189.0 spike=0.25
- MASR.CA: score=24.4 buy_ready=False sector_rank=7 price=8.15 support=6.71 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=74.65 liquidity=33671932.0 spike=0.4
- MBSC.CA: score=18.4 buy_ready=False sector_rank=2 price=245.8 support=222.66 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=51.57 liquidity=2996703.25 spike=0.16
- MCQE.CA: score=19.9 buy_ready=True sector_rank=2 price=186.31 support=166.66 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=66.84 liquidity=3503414.0 spike=0.19
- MCRO.CA: score=22.4 buy_ready=False sector_rank=7 price=1.49 support=1.17 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=83.72 liquidity=88571432.0 spike=0.83
- MENA.CA: score=15.55 buy_ready=True sector_rank=10 price=7.08 support=6.59 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=52.69 liquidity=1147646.38 spike=0.15
- MEPA.CA: score=24.4 buy_ready=False sector_rank=7 price=1.93 support=1.52 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=34913812.0 spike=0.81
- MFPC.CA: score=20.07 buy_ready=False sector_rank=17 price=36.5 support=34.22 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=52.84 liquidity=24141006.0 spike=0.26
- MFSC.CA: score=5.3 buy_ready=False sector_rank=7 price=46.8 support=45.05 resistance=53.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=30.28 liquidity=899396.31 spike=0.14
- MHOT.CA: score=3.28 buy_ready=False sector_rank=21 price=16.54 support=16.12 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=31.72 liquidity=1882839.88 spike=0.16
- MICH.CA: score=18.55 buy_ready=False sector_rank=7 price=41.35 support=34.0 resistance=43.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=83.28 liquidity=5149694.0 spike=0.33
- MILS.CA: score=9.4 buy_ready=False sector_rank=7 price=177.02 support=167.02 resistance=180.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27506474.0 spike=0.81
- MIPH.CA: score=14.72 buy_ready=False sector_rank=14 price=744.86 support=630.13 resistance=780.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=72.06 liquidity=449782.75 spike=0.13
- MOED.CA: score=22.4 buy_ready=True sector_rank=7 price=0.71 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=61.24 liquidity=10189524.0 spike=0.52
- MOIL.CA: score=14.32 buy_ready=False sector_rank=12 price=0.61 support=0.46 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=86.93 liquidity=620364.19 spike=1.15
- MOIN.CA: score=10.87 buy_ready=False sector_rank=7 price=23.6 support=22.6 resistance=24.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 July 01:14 PM market time freshness=DELAYED_CURRENT RSI=46.84 liquidity=465703.44 spike=0.59
- MOSC.CA: score=17.3 buy_ready=False sector_rank=7 price=288.17 support=250.0 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=63.16 liquidity=897314.63 spike=0.07
- MPCI.CA: score=23.4 buy_ready=False sector_rank=7 price=285.0 support=222.55 resistance=289.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=78.68 liquidity=16165043.0 spike=0.17
- MPCO.CA: score=24.4 buy_ready=True sector_rank=4 price=1.88 support=1.7 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=56.41 liquidity=16341128.0 spike=0.3
- MPRC.CA: score=11.12 buy_ready=False sector_rank=7 price=43.99 support=36.7 resistance=45.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=75.27 liquidity=1715361.38 spike=0.05
- MTIE.CA: score=15.98 buy_ready=True sector_rank=16 price=9.36 support=8.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=44.06 liquidity=2598673.0 spike=0.12
- NAHO.CA: score=3.41 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=6073.21 spike=0.18
- NCCW.CA: score=25.81 buy_ready=True sector_rank=7 price=6.68 support=5.82 resistance=6.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=62.33 liquidity=9410095.0 spike=0.44
- NEDA.CA: score=9.92 buy_ready=False sector_rank=7 price=2.75 support=2.7 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=518695.09 spike=0.77
- NHPS.CA: score=19.65 buy_ready=False sector_rank=7 price=89.34 support=61.55 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=79.33 liquidity=8254127.5 spike=0.1
- NINH.CA: score=24.74 buy_ready=False sector_rank=7 price=22.53 support=17.4 resistance=23.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=72.36 liquidity=47276168.0 spike=1.17
- NIPH.CA: score=21.27 buy_ready=False sector_rank=14 price=230.01 support=157.01 resistance=242.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=89.55 liquidity=40277052.0 spike=0.28
- OBRI.CA: score=14.4 buy_ready=False sector_rank=7 price=34.5 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=29.55 liquidity=11620420.0 spike=0.3
- OCDI.CA: score=24.4 buy_ready=True sector_rank=10 price=27.55 support=23.75 resistance=28.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=61.06 liquidity=62672716.0 spike=0.62
- OCPH.CA: score=21.4 buy_ready=False sector_rank=7 price=472.77 support=341.4 resistance=496.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=90.9 liquidity=17100930.0 spike=0.73
- ODIN.CA: score=21.95 buy_ready=False sector_rank=7 price=2.69 support=2.05 resistance=2.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=76.81 liquidity=8551363.0 spike=0.53
- OFH.CA: score=19.56 buy_ready=False sector_rank=7 price=0.72 support=0.57 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=8160480.0 spike=0.14
- OIH.CA: score=27.22 buy_ready=False sector_rank=9 price=1.5 support=1.4 resistance=1.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=92897424.0 spike=1.41
- OLFI.CA: score=16.41 buy_ready=True sector_rank=18 price=23.41 support=21.0 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=66.26 liquidity=3342524.25 spike=0.09
- ORAS.CA: score=7.6 buy_ready=False sector_rank=19 price=707.24 support=705.0 resistance=709.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18318440.0 spike=1.0
- ORHD.CA: score=24.4 buy_ready=True sector_rank=10 price=40.08 support=37.0 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=61.59 liquidity=18163658.0 spike=0.12
- ORWE.CA: score=25.06 buy_ready=True sector_rank=1 price=22.99 support=21.95 resistance=23.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=56.03 liquidity=5663464.5 spike=0.24
- PHAR.CA: score=14.27 buy_ready=False sector_rank=14 price=95.52 support=92.1 resistance=97.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=214349872.0 spike=7.44
- PHDC.CA: score=21.4 buy_ready=False sector_rank=10 price=14.83 support=14.26 resistance=15.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=50.59 liquidity=81369184.0 spike=0.34
- PHTV.CA: score=13.14 buy_ready=False sector_rank=7 price=311.36 support=246.51 resistance=319.0 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=79.62 liquidity=1743615.92 spike=0.28
- POUL.CA: score=21.07 buy_ready=False sector_rank=18 price=38.74 support=36.52 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=53.32 liquidity=20741214.0 spike=0.63
- PRCL.CA: score=26.4 buy_ready=True sector_rank=2 price=36.13 support=29.15 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=61.78 liquidity=22493718.0 spike=0.45
- PRDC.CA: score=26.4 buy_ready=True sector_rank=10 price=9.47 support=6.8 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=63.96 liquidity=11087577.0 spike=0.09
- PRMH.CA: score=18.2 buy_ready=True sector_rank=7 price=2.7 support=2.34 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=56.86 liquidity=3796593.75 spike=0.22
- RACC.CA: score=14.67 buy_ready=False sector_rank=7 price=10.03 support=9.36 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=52.51 liquidity=2270033.5 spike=0.11
- RAKT.CA: score=12.56 buy_ready=False sector_rank=7 price=22.64 support=21.25 resistance=23.79 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=62.22 liquidity=156465.04 spike=0.54
- RAYA.CA: score=16.75 buy_ready=False sector_rank=20 price=7.5 support=7.01 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=44.07 liquidity=34511100.0 spike=0.26
- RMDA.CA: score=28.35 buy_ready=True sector_rank=14 price=5.16 support=4.81 resistance=5.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=21285192.0 spike=1.04
- ROTO.CA: score=17.63 buy_ready=True sector_rank=7 price=44.1 support=38.0 resistance=46.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=54.73 liquidity=3231323.5 spike=0.14
- RREI.CA: score=22.48 buy_ready=False sector_rank=7 price=3.96 support=3.34 resistance=4.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=70.59 liquidity=30092600.0 spike=1.04
- RTVC.CA: score=17.34 buy_ready=False sector_rank=7 price=4.0 support=3.55 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=56.96 liquidity=940396.63 spike=0.21
- RUBX.CA: score=17.66 buy_ready=True sector_rank=7 price=13.37 support=10.38 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=51.3 liquidity=3262945.5 spike=0.04
- SAUD.CA: score=22.21 buy_ready=True sector_rank=6 price=22.56 support=19.99 resistance=22.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=68.81 liquidity=5806277.0 spike=0.66
- SCEM.CA: score=23.4 buy_ready=False sector_rank=2 price=81.17 support=60.14 resistance=85.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=80.14 liquidity=11454785.0 spike=0.2
- SCFM.CA: score=26.4 buy_ready=True sector_rank=7 price=283.47 support=230.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=61.36 liquidity=12442912.0 spike=0.64
- SCTS.CA: score=16.53 buy_ready=True sector_rank=8 price=619.52 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=2125576.75 spike=0.31
- SDTI.CA: score=17.7 buy_ready=False sector_rank=7 price=52.64 support=45.55 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=80.99 liquidity=4300741.0 spike=0.57
- SEIG.CA: score=13.42 buy_ready=False sector_rank=7 price=246.99 support=182.01 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=71.54 liquidity=1017686.94 spike=0.04
- SIPC.CA: score=17.78 buy_ready=False sector_rank=7 price=3.81 support=3.25 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=79.17 liquidity=4380779.0 spike=0.3
- SKPC.CA: score=19.07 buy_ready=False sector_rank=17 price=16.0 support=14.8 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=47.96 liquidity=13968581.0 spike=0.39
- SMFR.CA: score=16.71 buy_ready=False sector_rank=7 price=232.35 support=187.01 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=71.36 liquidity=2312534.25 spike=0.11
- SNFC.CA: score=12.8 buy_ready=False sector_rank=7 price=11.25 support=11.2 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=38.97 liquidity=3401590.25 spike=0.3
- SPIN.CA: score=26.4 buy_ready=False sector_rank=1 price=15.28 support=13.8 resistance=15.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=81.4 liquidity=13130262.0 spike=0.85
- SPMD.CA: score=16.67 buy_ready=True sector_rank=7 price=0.45 support=0.41 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=65.31 liquidity=4274986.0 spike=0.24
- SUGR.CA: score=13.01 buy_ready=False sector_rank=18 price=47.19 support=45.31 resistance=47.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=48.13 liquidity=1946885.25 spike=0.36
- SVCE.CA: score=17.99 buy_ready=False sector_rank=7 price=9.32 support=8.76 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=36.48 liquidity=5590541.5 spike=0.09
- SWDY.CA: score=24.4 buy_ready=False sector_rank=3 price=95.25 support=84.3 resistance=97.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=78.81 liquidity=12839799.0 spike=0.63
- TALM.CA: score=18.33 buy_ready=True sector_rank=8 price=15.85 support=15.27 resistance=16.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=42.69 liquidity=1926252.25 spike=0.14
- TMGH.CA: score=26.4 buy_ready=True sector_rank=10 price=99.81 support=92.1 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=58.65 liquidity=40845260.0 spike=0.11
- TRTO.CA: score=12.06 buy_ready=False sector_rank=7 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=2036.5 spike=1.83
- UEFM.CA: score=15.21 buy_ready=False sector_rank=7 price=542.21 support=460.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=67.95 liquidity=811302.25 spike=0.19
- UEGC.CA: score=23.4 buy_ready=False sector_rank=7 price=2.65 support=1.33 resistance=2.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=90.91 liquidity=44316024.0 spike=0.98
- UNIP.CA: score=21.4 buy_ready=False sector_rank=7 price=0.41 support=0.3 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=80.45 liquidity=10043341.0 spike=0.43
- UNIT.CA: score=14.48 buy_ready=True sector_rank=10 price=18.25 support=12.0 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=69.19 liquidity=2084431.13 spike=0.07
- WCDF.CA: score=21.08 buy_ready=True sector_rank=7 price=594.1 support=504.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=64.42 liquidity=3203689.0 spike=1.74
- WKOL.CA: score=21.52 buy_ready=True sector_rank=7 price=322.01 support=273.1 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=66.08 liquidity=7119875.5 spike=0.75
- ZEOT.CA: score=17.48 buy_ready=True sector_rank=7 price=11.74 support=10.4 resistance=12.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=64.13 liquidity=3083123.25 spike=0.1
- ZMID.CA: score=24.4 buy_ready=False sector_rank=10 price=7.62 support=6.19 resistance=7.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=70.27 liquidity=129066264.0 spike=0.54

## Backtesting Lite
- IDRE.CA: 180d return=22.95%, max drawdown=-24.62%, MA20>MA50 days last20=20, as_of=2026-07-25T21:00:00+00:00
- ELSH.CA: 180d return=87.8%, max drawdown=-27.17%, MA20>MA50 days last20=20, as_of=2026-07-25T21:00:00+00:00
- ISMA.CA: 180d return=139.38%, max drawdown=-18.8%, MA20>MA50 days last20=20, as_of=2026-07-25T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- IDRE.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Ismailia Development and Real Estate Co summary=Evidence rejected for IDRE.CA: source text did not clearly match IDRE.CA / Ismailia Development and Real Estate Co.
- ELSH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Al Shams Housing and Urbanization SAE summary=Al Shams Housing’s stock tests key support amid selling pressure; FRA approves Al Shams Housing’s capital increase; Al Shams Housing awards part of NAC project to Olive Tree
  - Al Shams Housing’s stock tests key support amid selling pressure: https://english.mubasher.info/news/4553488/Al-Shams-Housing-s-stock-tests-key-support-amid-selling-pressure/
  - FRA approves Al Shams Housing’s capital increase: https://english.mubasher.info/news/3899254/FRA-approves-Al-Shams-Housing-s-capital-increase/
  - Al Shams Housing awards part of NAC project to Olive Tree: https://english.mubasher.info/news/3896693/Al-Shams-Housing-awards-part-of-NAC-project-to-Olive-Tree/
- ISMA.CA: status=OLD_ACCEPTED latest=2020-01-01 age_days=2399 sources=3 expected=Ismailia / Misr Poultry Company S.A.E summary=Ismailia Misr Poultry stock gains momentum near breakout level; Ismailia Misr Poultry stock tests EGP 14.1 resistance; Ismailia Misr Poultry targets EGP 11.5m profit in 2020
  - Ismailia Misr Poultry stock gains momentum near breakout level: https://english.mubasher.info/news/4592166/Ismailia-Misr-Poultry-stock-gains-momentum-near-breakout-level/
  - Ismailia Misr Poultry stock tests EGP 14.1 resistance: https://english.mubasher.info/news/4582822/Ismailia-Misr-Poultry-stock-tests-EGP-14-1-resistance/
  - Ismailia Misr Poultry targets EGP 11.5m profit in 2020: https://english.mubasher.info/news/3582076/Ismailia-Misr-Poultry-targets-EGP-11-5m-profit-in-2020/
- RMDA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tenth of Ramadan Pharmaceutical Industries summary=Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- ADIB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Dhabi Islamic Bank Egypt summary=ADIB Egypt’s consolidated profits leap to EGP 3.6bn in Q1-26; ADIB Egypt stock approaches breakout above EGP 41; ADIB Egypt’s stock holds uptrend despite corrections
  - ADIB Egypt’s consolidated profits leap to EGP 3.6bn in Q1-26: https://english.mubasher.info/news/4607278/ADIB-Egypt-s-consolidated-profits-leap-to-EGP-3-6bn-in-Q1-26/
  - ADIB Egypt stock approaches breakout above EGP 41: https://english.mubasher.info/news/4591391/ADIB-Egypt-stock-approaches-breakout-above-EGP-41/
  - ADIB Egypt’s stock holds uptrend despite corrections: https://english.mubasher.info/news/4562331/ADIB-Egypt-s-stock-holds-uptrend-despite-corrections/
- OIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Investment Holding summary=Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- ARCC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=572 sources=3 expected=Arabian Cement Company summary=Arabian Cement to pay out EGP 2bn dividends for 2025; Arabian Cement’s EGM approves nearly EGP 8m capital cut; Arabian Cement’s consolidated profits near EGP 3.6bn in 2025
  - Arabian Cement to pay out EGP 2bn dividends for 2025: https://english.mubasher.info/news/4587912/Arabian-Cement-to-pay-out-EGP-2bn-dividends-for-2025/
  - Arabian Cement’s EGM approves nearly EGP 8m capital cut: https://english.mubasher.info/news/4583762/Arabian-Cement-s-EGM-approves-nearly-EGP-8m-capital-cut/
  - Arabian Cement’s consolidated profits near EGP 3.6bn in 2025: https://english.mubasher.info/news/4562679/Arabian-Cement-s-consolidated-profits-near-EGP-3-6bn-in-2025/
- EHDR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=572 sources=3 expected=Egyptians for Housing & Development Co. summary=Egyptians for Housing to disburse EGP 0.01/shr for 2025; EGX-listed companies, banks propose cash dividends for 2025; Egyptians for Housing stock witnesses selling pressures amid key levels to observe – Analysis
  - Egyptians for Housing to disburse EGP 0.01/shr for 2025: https://english.mubasher.info/news/4584569/Egyptians-for-Housing-to-disburse-EGP-0-01-shr-for-2025/
  - EGX-listed companies, banks propose cash dividends for 2025: https://english.mubasher.info/news/4560139/EGX-listed-companies-banks-propose-cash-dividends-for-2025/
  - Egyptians for Housing stock witnesses selling pressures amid key levels to observe – Analysis: https://english.mubasher.info/news/4547337/Egyptians-for-Housing-stock-witnesses-selling-pressures-amid-key-levels-to-observe-Analysis/

## Warnings
- Evidence rejected for IDRE.CA: source text did not clearly match IDRE.CA / Ismailia Development and Real Estate Co.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence for ELSH.CA matches the company but no source/report date was detected.
- Evidence for ISMA.CA matches the company but appears old; latest detected date is 2020-01-01.
- Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- Evidence for ADIB.CA matches the company but no source/report date was detected.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence for ARCC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for EHDR.CA matches the company but appears old; latest detected date is 2025-01-01.
