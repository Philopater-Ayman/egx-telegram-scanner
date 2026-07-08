# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-07-08T14:52:05.654906+00:00
Generated Cairo: 2026-07-08 17:52
Run timing: target 15:30 Cairo | generated Cairo 2026-07-08 17:52 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-07-08 17:45

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 52
- Data quality issues: 0
- Tradeable price/liquidity tickers: 181/190
- Top sector: Technology & Distribution

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, July 08
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 60.0% / above MA50 40.0%
- EGX70 regime: BULLISH / above MA20 75.0% / above MA50 72.5%
- Sector breadth: 66.67%
- Risk mode: SELECTIVE_SMALL_MID_SWINGS

## Top Liquidity
- CCAP.CA: liquidity=1081576576.0 spike=1.64 score=25.68
- COMI.CA: liquidity=465417952.0 spike=1.02 score=24.85
- TMGH.CA: liquidity=334318112.0 spike=0.93 score=29.4
- ABUK.CA: liquidity=300660672.0 spike=2.41 score=23.32
- HELI.CA: liquidity=282626848.0 spike=2.57 score=30.54

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b-20230311:free
- Summary: EGX30 bearish / EGX70 bullish, sector breadth 66.7%, risk mode selective small‑mid swings; scanner highlights several Real Estate and Tech names with accumulation spikes and near‑resistance levels, but evidence is thin and confidence remains low.
- Selected tickets show high rank scores, BULLISH_WATCH outlook, and ACCUMULATION_SPIKE liquidity, sitting within 1‑2% of their 20‑day resistance while staying ~10‑12% above support.
- Liquidity spikes suggest short‑term institutional interest; proximity to resistance offers upside if broken, yet also raises pullback risk; sector alignment with leading Real Estate, Technology & Distribution, and Fintec
- EGX30’s bearish bias drags overall market confidence, while EGX70’s bullish breadth shifts the risk mode to SELECTIVE_SMALL_MID_SWINGS, implying only limited, selective exposure is warranted.
- Uncertainty remains high: most tickers lack clear fundamental evidence, RSI readings approach overbought levels, and momentum flags are extended, so the outlook for the next 1‑3 days stays watchful with possible reversal

## Top Liquidity Spikes
- SEIG.CA: spike=35.87 liquidity=166478688.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AMES.CA: spike=8.46 liquidity=150824336.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- BIOC.CA: spike=5.97 liquidity=15817874.0 outlook=BULLISH_WATCH score=82.47 buy_ready=True
- MIPH.CA: spike=5.66 liquidity=10737573.0 outlook=BULLISH_WATCH score=83.93 buy_ready=True
- RREI.CA: spike=5.26 liquidity=77869232.0 outlook=BULLISH_WATCH score=84.47 buy_ready=True

## Sector Leaderboard
- #1 Technology & Distribution: score=13.31 5d=10.27% 20d=8.05% aboveMA50=100.0%
- #2 Fintech & Payments: score=12.38 5d=10.64% 20d=8.23% aboveMA50=50.0%
- #3 Real Estate: score=11.23 5d=6.47% 20d=8.54% aboveMA50=100.0%
- #4 Investment Holding: score=10.53 5d=7.61% 20d=0.71% aboveMA50=66.67%
- #5 Telecommunications: score=10.29 5d=5.4% 20d=2.71% aboveMA50=100.0%
- #6 Automotive & Distribution: score=9.75 5d=2.21% 20d=10.79% aboveMA50=100.0%
- #7 Textiles: score=8.64 5d=4.93% 20d=1.46% aboveMA50=100.0%
- #8 Food, Beverages & Tobacco: score=8.25 5d=4.82% 20d=5.65% aboveMA50=57.14%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- TMGH.CA: BULLISH_WATCH score=100 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- ARAB.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- MENA.CA: BULLISH_WATCH score=100 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- BINV.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- HELI.CA: BULLISH_WATCH score=99 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- CCAP.CA: BULLISH_WATCH score=97 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- SPMD.CA: BULLISH_WATCH score=94.47 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- PRDC.CA: BULLISH_WATCH score=94 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- ETEL.CA: BULLISH_WATCH score=91 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended
- EFIH.CA: BULLISH_WATCH score=91 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI

## BUY-Ready Candidates
- RREI.CA: rank=33.4 outlook=BULLISH_WATCH outlook_score=84.47 sector_rank=15 price=3.76 support=3.34 resistance=3.81 liquidity=77869232.0
- BIOC.CA: rank=31.4 outlook=BULLISH_WATCH outlook_score=82.47 sector_rank=15 price=73.24 support=66.75 resistance=74.2 liquidity=15817874.0
- MIPH.CA: rank=31.4 outlook=BULLISH_WATCH outlook_score=83.93 sector_rank=9 price=698.41 support=630.13 resistance=710.0 liquidity=10737573.0
- HELI.CA: rank=30.54 outlook=BULLISH_WATCH outlook_score=99 sector_rank=3 price=6.85 support=6.28 resistance=6.84 liquidity=282626848.0
- LCSW.CA: rank=29.7 outlook=BULLISH_WATCH outlook_score=73.1 sector_rank=11 price=31.27 support=26.0 resistance=31.33 liquidity=125802360.0
- PRDC.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=94 sector_rank=3 price=8.3 support=5.91 resistance=9.0 liquidity=70464344.0
- TMGH.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=100 sector_rank=3 price=97.0 support=92.1 resistance=99.43 liquidity=334318112.0
- ARAB.CA: rank=29.06 outlook=BULLISH_WATCH outlook_score=100 sector_rank=3 price=0.23 support=0.2 resistance=0.24 liquidity=129980032.0
- MASR.CA: rank=28.64 outlook=BULLISH_WATCH outlook_score=70.47 sector_rank=15 price=7.61 support=6.54 resistance=7.84 liquidity=83927136.0
- OLFI.CA: rank=28.5 outlook=BULLISH_WATCH outlook_score=84.25 sector_rank=8 price=22.9 support=21.0 resistance=23.2 liquidity=54585768.0

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=24.7 buy_ready=False sector_rank=15 price=219.73 support=196.0 resistance=247.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=77.59 liquidity=20794272.0 spike=1.65
- ABUK.CA: score=23.32 buy_ready=False sector_rank=19 price=71.1 support=66.66 resistance=82.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.97 liquidity=300660672.0 spike=2.41
- ACAMD.CA: score=26.4 buy_ready=True sector_rank=15 price=2.32 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=51.43 liquidity=90655384.0 spike=0.81
- ACGC.CA: score=24.4 buy_ready=True sector_rank=7 price=9.5 support=8.92 resistance=10.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=55.8 liquidity=12682199.0 spike=0.45
- ADCI.CA: score=19.41 buy_ready=False sector_rank=15 price=232.0 support=215.04 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=60.85 liquidity=7010081.5 spike=0.59
- ADIB.CA: score=21.75 buy_ready=False sector_rank=17 price=46.3 support=44.01 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.7 liquidity=126930256.0 spike=1.47
- ADPC.CA: score=18.53 buy_ready=False sector_rank=15 price=3.51 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.12 liquidity=9134391.0 spike=0.62
- AFDI.CA: score=19.49 buy_ready=True sector_rank=15 price=45.24 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=65.15 liquidity=5088466.0 spike=0.39
- AFMC.CA: score=19.14 buy_ready=False sector_rank=15 price=70.97 support=66.0 resistance=74.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=59.46 liquidity=3203056.75 spike=1.27
- AJWA.CA: score=21.31 buy_ready=True sector_rank=15 price=173.58 support=135.0 resistance=190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=39.45 liquidity=6914923.0 spike=0.25
- ALCN.CA: score=25.4 buy_ready=False sector_rank=10 price=28.96 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=58.48 liquidity=10652133.0 spike=0.93
- ALUM.CA: score=25.58 buy_ready=False sector_rank=15 price=23.0 support=20.55 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.5 liquidity=16907468.0 spike=2.09
- AMER.CA: score=29.36 buy_ready=False sector_rank=3 price=2.79 support=2.28 resistance=2.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.24 liquidity=129313864.0 spike=1.98
- AMES.CA: score=14.4 buy_ready=False sector_rank=15 price=70.78 support=58.32 resistance=70.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=150824336.0 spike=8.46
- AMIA.CA: score=22.86 buy_ready=False sector_rank=15 price=8.93 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=53.76 liquidity=8455704.0 spike=0.8
- AMOC.CA: score=28.36 buy_ready=False sector_rank=12 price=8.12 support=7.42 resistance=8.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.37 liquidity=159495984.0 spike=3.48
- ANFI.CA: score=10.73 buy_ready=False sector_rank=15 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=STALE RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=11.08 buy_ready=False sector_rank=15 price=8.49 support=8.0 resistance=9.0 source=Yahoo Finance as_of=2026-07-06T21:00:00+00:00 freshness=FRESH RSI=48.41 liquidity=677867.05 spike=0.84
- ARAB.CA: score=29.06 buy_ready=True sector_rank=3 price=0.23 support=0.2 resistance=0.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=58.18 liquidity=129980032.0 spike=1.83
- ARCC.CA: score=19.4 buy_ready=False sector_rank=11 price=55.26 support=53.0 resistance=58.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.07 liquidity=14135180.0 spike=0.56
- AREH.CA: score=22.4 buy_ready=False sector_rank=15 price=1.55 support=1.42 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=51.28 liquidity=15328040.0 spike=0.4
- ARVA.CA: score=20.94 buy_ready=False sector_rank=15 price=10.82 support=10.3 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.17 liquidity=8538088.0 spike=0.32
- ASCM.CA: score=22.4 buy_ready=False sector_rank=15 price=57.6 support=54.12 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.68 liquidity=21809696.0 spike=0.25
- ASPI.CA: score=22.4 buy_ready=False sector_rank=15 price=0.32 support=0.3 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.76 liquidity=17127938.0 spike=0.3
- ATLC.CA: score=19.74 buy_ready=True sector_rank=14 price=5.18 support=4.7 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=54.29 liquidity=3340838.0 spike=0.46
- ATQA.CA: score=19.5 buy_ready=False sector_rank=19 price=9.5 support=9.02 resistance=10.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.68 liquidity=32623174.0 spike=0.92
- AXPH.CA: score=21.6 buy_ready=True sector_rank=15 price=1179.56 support=1073.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=62.2 liquidity=4263517.5 spike=1.47
- BINV.CA: score=25.52 buy_ready=True sector_rank=4 price=48.0 support=44.02 resistance=51.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=56.15 liquidity=10848693.0 spike=1.56
- BIOC.CA: score=31.4 buy_ready=True sector_rank=15 price=73.24 support=66.75 resistance=74.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=50.68 liquidity=15817874.0 spike=5.97
- BTFH.CA: score=22.62 buy_ready=False sector_rank=14 price=3.04 support=2.91 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.87 liquidity=216989952.0 spike=1.11
- CAED.CA: score=20.64 buy_ready=True sector_rank=15 price=71.98 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.68 liquidity=4238705.0 spike=0.87
- CANA.CA: score=21.05 buy_ready=False sector_rank=17 price=36.12 support=34.5 resistance=39.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.5 liquidity=12573470.0 spike=1.12
- CCAP.CA: score=25.68 buy_ready=True sector_rank=4 price=5.21 support=4.65 resistance=5.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.08 liquidity=1081576576.0 spike=1.64
- CCRS.CA: score=13.1 buy_ready=False sector_rank=15 price=2.31 support=2.18 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.93 liquidity=5701342.0 spike=0.42
- CEFM.CA: score=15.03 buy_ready=False sector_rank=15 price=101.77 support=95.75 resistance=109.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.09 liquidity=2650679.0 spike=1.49
- CERA.CA: score=24.78 buy_ready=True sector_rank=15 price=1.26 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.89 liquidity=22721692.0 spike=1.19
- CFGH.CA: score=3.4 buy_ready=False sector_rank=15 price=0.1 support=0.1 resistance=0.1 source=Yahoo Finance as_of=2026-07-06T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=2151.8 spike=0.4
- CICH.CA: score=15.68 buy_ready=False sector_rank=14 price=11.89 support=11.1 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=2280177.75 spike=0.68
- CIEB.CA: score=21.7 buy_ready=True sector_rank=17 price=23.95 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=62.71 liquidity=3884827.75 spike=0.57
- CIRA.CA: score=24.4 buy_ready=False sector_rank=13 price=28.7 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=72.06 liquidity=18542782.0 spike=0.99
- CLHO.CA: score=25.28 buy_ready=True sector_rank=9 price=16.3 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=61.79 liquidity=52134672.0 spike=1.44
- CNFN.CA: score=26.4 buy_ready=True sector_rank=14 price=4.79 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=63.64 liquidity=29297688.0 spike=0.66
- COMI.CA: score=24.85 buy_ready=False sector_rank=17 price=133.49 support=126.21 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.68 liquidity=465417952.0 spike=1.02
- COPR.CA: score=21.4 buy_ready=False sector_rank=15 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=10222765.0 spike=0.42
- COSG.CA: score=26.4 buy_ready=True sector_rank=15 price=1.59 support=1.47 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=27250294.0 spike=0.48
- CPCI.CA: score=12.97 buy_ready=False sector_rank=15 price=397.08 support=354.0 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=76.2 liquidity=1570447.75 spike=0.52
- CSAG.CA: score=24.4 buy_ready=False sector_rank=10 price=32.15 support=30.08 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=72.99 liquidity=11405856.0 spike=0.65
- DAPH.CA: score=17.55 buy_ready=False sector_rank=15 price=81.06 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.74 liquidity=4151023.25 spike=0.45
- DEIN.CA: score=-0.6 buy_ready=False sector_rank=15 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=1.0
- DOMT.CA: score=15.79 buy_ready=False sector_rank=8 price=26.75 support=23.7 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=78.25 liquidity=4393663.5 spike=0.89
- DSCW.CA: score=17.4 buy_ready=False sector_rank=15 price=1.79 support=1.71 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.78 liquidity=25135006.0 spike=0.79
- DTPP.CA: score=14.4 buy_ready=False sector_rank=15 price=206.11 support=195.2 resistance=217.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=95506064.0 spike=3.57
- EALR.CA: score=12.4 buy_ready=False sector_rank=15 price=363.78 support=363.0 resistance=389.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22840906.0 spike=2.5
- EASB.CA: score=21.6 buy_ready=False sector_rank=15 price=6.98 support=4.87 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=47.52 liquidity=9204782.0 spike=0.6
- EAST.CA: score=18.4 buy_ready=False sector_rank=8 price=37.29 support=36.63 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.75 liquidity=30293178.0 spike=0.67
- EBSC.CA: score=27.52 buy_ready=True sector_rank=15 price=1.93 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.82 liquidity=9538485.0 spike=1.79
- ECAP.CA: score=18.81 buy_ready=False sector_rank=15 price=32.43 support=30.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=51.21 liquidity=6413086.0 spike=0.65
- EDFM.CA: score=11.95 buy_ready=False sector_rank=15 price=333.03 support=310.2 resistance=355.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=50.85 liquidity=547732.06 spike=0.98
- EEII.CA: score=23.4 buy_ready=False sector_rank=15 price=2.73 support=2.3 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=77.22 liquidity=21264912.0 spike=0.98
- EFIC.CA: score=4.91 buy_ready=False sector_rank=19 price=182.83 support=180.02 resistance=208.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=16.76 liquidity=2408555.75 spike=0.96
- EFID.CA: score=23.4 buy_ready=False sector_rank=8 price=28.27 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=53.54 liquidity=38303676.0 spike=0.5
- EFIH.CA: score=25.7 buy_ready=False sector_rank=2 price=22.15 support=20.0 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.71 liquidity=88840976.0 spike=2.15
- EGAL.CA: score=20.5 buy_ready=False sector_rank=19 price=294.04 support=272.28 resistance=323.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.99 liquidity=43583680.0 spike=0.88
- EGAS.CA: score=22.96 buy_ready=False sector_rank=12 price=49.88 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.39 liquidity=10116681.0 spike=1.28
- EGBE.CA: score=15.83 buy_ready=False sector_rank=17 price=0.45 support=0.43 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=22429.38 spike=0.31
- EGCH.CA: score=15.22 buy_ready=False sector_rank=19 price=13.03 support=12.13 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.47 liquidity=77381792.0 spike=1.86
- EGSA.CA: score=11.95 buy_ready=False sector_rank=5 price=8.87 support=8.55 resistance=8.93 source=Yahoo Finance as_of=2026-07-06T21:00:00+00:00 freshness=FRESH RSI=80.0 liquidity=7770.12 spike=1.27
- EGTS.CA: score=27.4 buy_ready=True sector_rank=3 price=18.44 support=15.1 resistance=20.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.05 liquidity=47071916.0 spike=0.69
- EHDR.CA: score=22.4 buy_ready=False sector_rank=15 price=2.58 support=2.37 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=45.9 liquidity=34515176.0 spike=0.64
- EKHO.CA: score=11.4 buy_ready=False sector_rank=12 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-06T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=18.11 buy_ready=False sector_rank=16 price=2.09 support=2.04 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=42.11 liquidity=9802404.0 spike=0.55
- ELKA.CA: score=25.4 buy_ready=True sector_rank=15 price=1.43 support=1.19 resistance=1.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.83 liquidity=28576414.0 spike=0.62
- ELNA.CA: score=16.73 buy_ready=False sector_rank=15 price=37.03 support=35.55 resistance=41.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=45.61 liquidity=1591115.0 spike=3.37
- ELSH.CA: score=24.4 buy_ready=True sector_rank=15 price=13.29 support=11.1 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.0 liquidity=105618608.0 spike=0.57
- ELWA.CA: score=4.72 buy_ready=False sector_rank=15 price=1.94 support=1.89 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=34.29 liquidity=324917.94 spike=0.16
- EMFD.CA: score=23.4 buy_ready=False sector_rank=3 price=11.52 support=11.11 resistance=12.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.73 liquidity=99153248.0 spike=0.41
- ENGC.CA: score=28.3 buy_ready=True sector_rank=15 price=38.63 support=33.0 resistance=38.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=66.0 liquidity=27660220.0 spike=1.95
- EOSB.CA: score=16.44 buy_ready=False sector_rank=15 price=1.48 support=1.42 resistance=1.55 source=Yahoo Finance as_of=2026-07-06T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=36612.24 spike=0.34
- EPCO.CA: score=15.66 buy_ready=False sector_rank=15 price=8.91 support=8.5 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=6261479.5 spike=0.83
- EPPK.CA: score=13.15 buy_ready=False sector_rank=15 price=14.32 support=11.72 resistance=15.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=90.24 liquidity=1347434.0 spike=1.2
- ETEL.CA: score=26.4 buy_ready=True sector_rank=5 price=96.16 support=89.01 resistance=101.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.95 liquidity=63836096.0 spike=0.84
- ETRS.CA: score=24.4 buy_ready=True sector_rank=15 price=10.7 support=8.77 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.61 liquidity=46998388.0 spike=0.59
- EXPA.CA: score=20.81 buy_ready=False sector_rank=17 price=18.36 support=18.03 resistance=19.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.24 liquidity=17432506.0 spike=0.57
- FAIT.CA: score=13.95 buy_ready=False sector_rank=17 price=36.38 support=35.01 resistance=37.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.17 liquidity=2142926.0 spike=0.92
- FAITA.CA: score=8.85 buy_ready=False sector_rank=17 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.46 liquidity=36628.69 spike=0.91
- FERC.CA: score=24.75 buy_ready=False sector_rank=19 price=76.32 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.41 liquidity=9804249.0 spike=2.72
- FWRY.CA: score=27.4 buy_ready=False sector_rank=2 price=19.19 support=17.71 resistance=19.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=63.41 liquidity=115575328.0 spike=0.48
- GBCO.CA: score=24.4 buy_ready=False sector_rank=6 price=30.37 support=26.62 resistance=32.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=72.53 liquidity=28854050.0 spike=0.32
- GDWA.CA: score=9.48 buy_ready=False sector_rank=15 price=0.77 support=0.76 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.4 liquidity=6075280.0 spike=0.4
- GGCC.CA: score=9.6 buy_ready=False sector_rank=15 price=0.55 support=0.51 resistance=0.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18683466.0 spike=1.1
- GIHD.CA: score=20.43 buy_ready=True sector_rank=15 price=43.39 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.42 liquidity=4028149.5 spike=0.43
- GMCI.CA: score=19.83 buy_ready=False sector_rank=15 price=2.18 support=1.66 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=82.22 liquidity=2405941.5 spike=3.01
- GRCA.CA: score=7.74 buy_ready=False sector_rank=15 price=49.63 support=50.14 resistance=58.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=16.28 liquidity=3337428.0 spike=0.81
- GSSC.CA: score=20.84 buy_ready=False sector_rank=15 price=253.0 support=240.0 resistance=263.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=63.43 liquidity=4795067.0 spike=1.32
- GTWL.CA: score=28.4 buy_ready=False sector_rank=15 price=101.0 support=46.0 resistance=102.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=89.98 liquidity=232960304.0 spike=3.73
- HDBK.CA: score=17.81 buy_ready=False sector_rank=17 price=81.68 support=82.52 resistance=82.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=36685712.0 spike=1.0
- HELI.CA: score=30.54 buy_ready=True sector_rank=3 price=6.85 support=6.28 resistance=6.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.48 liquidity=282626848.0 spike=2.57
- HRHO.CA: score=20.4 buy_ready=False sector_rank=14 price=26.69 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.44 liquidity=76676768.0 spike=0.57
- ICID.CA: score=16.61 buy_ready=True sector_rank=15 price=7.6 support=6.12 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=59.26 liquidity=2205272.75 spike=0.18
- IDRE.CA: score=18.46 buy_ready=False sector_rank=15 price=42.51 support=41.1 resistance=46.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.53 liquidity=9059495.0 spike=0.82
- IFAP.CA: score=14.67 buy_ready=False sector_rank=18 price=19.26 support=18.47 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=54.27 liquidity=4976260.5 spike=0.97
- INFI.CA: score=15.03 buy_ready=False sector_rank=15 price=94.71 support=88.51 resistance=103.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=43.08 liquidity=4627237.5 spike=0.75
- IRON.CA: score=14.84 buy_ready=False sector_rank=19 price=32.01 support=30.51 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=44.4 liquidity=5339601.0 spike=0.68
- ISMA.CA: score=17.4 buy_ready=False sector_rank=15 price=27.15 support=26.9 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=3.51 liquidity=14963846.0 spike=0.45
- ISMQ.CA: score=20.5 buy_ready=False sector_rank=19 price=9.84 support=7.67 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.67 liquidity=133763232.0 spike=0.98
- ISPH.CA: score=19.4 buy_ready=False sector_rank=9 price=11.34 support=11.2 resistance=12.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.19 liquidity=72543624.0 spike=0.82
- JUFO.CA: score=26.4 buy_ready=True sector_rank=8 price=31.0 support=28.5 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.14 liquidity=30133762.0 spike=0.98
- KABO.CA: score=25.26 buy_ready=False sector_rank=7 price=7.39 support=5.96 resistance=7.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=87.33 liquidity=48985280.0 spike=1.93
- KWIN.CA: score=12.35 buy_ready=False sector_rank=15 price=66.95 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.77 liquidity=8952470.0 spike=0.7
- KZPC.CA: score=13.03 buy_ready=False sector_rank=15 price=8.47 support=8.26 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=36.13 liquidity=4628935.0 spike=0.7
- LCSW.CA: score=29.7 buy_ready=True sector_rank=11 price=31.27 support=26.0 resistance=31.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=65.12 liquidity=125802360.0 spike=2.65
- LUTS.CA: score=24.4 buy_ready=True sector_rank=15 price=0.73 support=0.62 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=39491628.0 spike=0.72
- MAAL.CA: score=24.6 buy_ready=False sector_rank=15 price=7.95 support=5.52 resistance=7.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=99.4 liquidity=25748342.0 spike=1.6
- MASR.CA: score=28.64 buy_ready=True sector_rank=15 price=7.61 support=6.54 resistance=7.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.54 liquidity=83927136.0 spike=1.12
- MBSC.CA: score=21.4 buy_ready=False sector_rank=11 price=243.75 support=222.66 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.85 liquidity=12534053.0 spike=0.48
- MCQE.CA: score=24.28 buy_ready=False sector_rank=11 price=178.01 support=166.66 resistance=192.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.25 liquidity=20088926.0 spike=1.44
- MCRO.CA: score=20.4 buy_ready=False sector_rank=15 price=1.23 support=1.17 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=22399528.0 spike=0.72
- MENA.CA: score=27.92 buy_ready=True sector_rank=3 price=7.05 support=6.41 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.43 liquidity=10996481.0 spike=1.26
- MEPA.CA: score=20.4 buy_ready=False sector_rank=15 price=1.62 support=1.52 resistance=1.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=45.16 liquidity=10262942.0 spike=0.85
- MFPC.CA: score=26.32 buy_ready=False sector_rank=19 price=37.3 support=34.22 resistance=42.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.72 liquidity=249579440.0 spike=2.91
- MFSC.CA: score=17.96 buy_ready=True sector_rank=15 price=47.29 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.69 liquidity=3564719.5 spike=0.46
- MHOT.CA: score=16.6 buy_ready=False sector_rank=21 price=16.84 support=17.55 resistance=17.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=12369079.0 spike=1.0
- MICH.CA: score=27.26 buy_ready=True sector_rank=15 price=38.19 support=34.0 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=51.37 liquidity=35510604.0 spike=2.43
- MILS.CA: score=12.78 buy_ready=False sector_rank=15 price=130.0 support=126.31 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.05 liquidity=8382670.0 spike=0.91
- MIPH.CA: score=31.4 buy_ready=True sector_rank=9 price=698.41 support=630.13 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.65 liquidity=10737573.0 spike=5.66
- MOED.CA: score=20.74 buy_ready=False sector_rank=15 price=0.69 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.0 liquidity=10641044.0 spike=1.17
- MOIL.CA: score=15.95 buy_ready=False sector_rank=12 price=0.52 support=0.46 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=76.67 liquidity=549387.56 spike=2.0
- MOIN.CA: score=11.03 buy_ready=False sector_rank=15 price=23.71 support=22.6 resistance=25.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=43.49 liquidity=633888.69 spike=0.83
- MOSC.CA: score=11.31 buy_ready=False sector_rank=15 price=269.55 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=43.77 liquidity=1908385.0 spike=0.2
- MPCI.CA: score=24.4 buy_ready=True sector_rank=15 price=239.52 support=213.0 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=61.37 liquidity=70943552.0 spike=0.68
- MPCO.CA: score=16.69 buy_ready=False sector_rank=18 price=1.8 support=1.66 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.3 liquidity=30669346.0 spike=0.28
- MPRC.CA: score=23.4 buy_ready=False sector_rank=15 price=40.76 support=31.15 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=92.18 liquidity=45552264.0 spike=1.0
- MTIE.CA: score=26.4 buy_ready=True sector_rank=6 price=9.18 support=8.65 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=53.85 liquidity=12405041.0 spike=0.62
- NAHO.CA: score=12.59 buy_ready=False sector_rank=15 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=34542.41 spike=1.08
- NCCW.CA: score=22.4 buy_ready=False sector_rank=15 price=6.09 support=5.82 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=49.59 liquidity=16034025.0 spike=0.46
- NEDA.CA: score=16.32 buy_ready=False sector_rank=15 price=2.74 support=2.7 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=46.15 liquidity=1924092.0 spike=5.15
- NHPS.CA: score=26.74 buy_ready=True sector_rank=15 price=70.61 support=61.55 resistance=75.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=67.11 liquidity=16652799.0 spike=1.17
- NINH.CA: score=21.74 buy_ready=False sector_rank=15 price=17.6 support=16.8 resistance=18.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=53.04 liquidity=9438686.0 spike=1.45
- NIPH.CA: score=25.32 buy_ready=True sector_rank=9 price=175.23 support=157.01 resistance=185.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=65.34 liquidity=134965856.0 spike=1.46
- OBRI.CA: score=24.3 buy_ready=False sector_rank=15 price=35.45 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.47 liquidity=38108448.0 spike=1.45
- OCDI.CA: score=25.34 buy_ready=False sector_rank=3 price=26.6 support=20.0 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=87.6 liquidity=133966544.0 spike=1.47
- OCPH.CA: score=24.9 buy_ready=False sector_rank=15 price=352.58 support=337.0 resistance=374.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=60.85 liquidity=10957772.0 spike=1.75
- ODIN.CA: score=26.96 buy_ready=True sector_rank=15 price=2.3 support=2.01 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.57 liquidity=17872352.0 spike=1.28
- OFH.CA: score=24.02 buy_ready=True sector_rank=15 price=0.62 support=0.57 resistance=0.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=58.14 liquidity=27657104.0 spike=1.31
- OIH.CA: score=20.86 buy_ready=False sector_rank=4 price=1.41 support=1.33 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=77.78 liquidity=102509384.0 spike=1.23
- OLFI.CA: score=28.5 buy_ready=True sector_rank=8 price=22.9 support=21.0 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.91 liquidity=54585768.0 spike=2.05
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=681.36 support=680.0 resistance=706.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=259597920.0 spike=1.0
- ORHD.CA: score=25.4 buy_ready=True sector_rank=3 price=38.58 support=35.01 resistance=39.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.28 liquidity=99563056.0 spike=0.59
- ORWE.CA: score=22.4 buy_ready=False sector_rank=7 price=22.7 support=21.95 resistance=23.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.48 liquidity=17434488.0 spike=0.8
- PHAR.CA: score=25.32 buy_ready=True sector_rank=9 price=87.0 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=60.19 liquidity=8923885.0 spike=0.35
- PHDC.CA: score=18.4 buy_ready=False sector_rank=3 price=14.74 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.39 liquidity=149202176.0 spike=0.45
- PHTV.CA: score=22.7 buy_ready=False sector_rank=15 price=276.32 support=201.55 resistance=277.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=85.91 liquidity=19877936.0 spike=1.65
- POUL.CA: score=27.3 buy_ready=False sector_rank=8 price=39.5 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=72.22 liquidity=54527216.0 spike=1.45
- PRCL.CA: score=23.8 buy_ready=False sector_rank=11 price=35.95 support=23.75 resistance=35.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=84.04 liquidity=59600316.0 spike=1.2
- PRDC.CA: score=29.4 buy_ready=True sector_rank=3 price=8.3 support=5.91 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.97 liquidity=70464344.0 spike=0.51
- PRMH.CA: score=16.0 buy_ready=False sector_rank=15 price=2.55 support=2.34 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.82 liquidity=8600732.0 spike=0.28
- RACC.CA: score=28.26 buy_ready=False sector_rank=15 price=9.98 support=9.36 resistance=10.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=71.32 liquidity=18848786.0 spike=1.93
- RAKT.CA: score=11.35 buy_ready=False sector_rank=15 price=22.35 support=21.4 resistance=23.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=46.2 liquidity=372218.22 spike=1.29
- RAYA.CA: score=27.52 buy_ready=True sector_rank=1 price=7.8 support=6.7 resistance=8.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.12 liquidity=110342512.0 spike=1.06
- RMDA.CA: score=22.4 buy_ready=False sector_rank=9 price=4.98 support=4.81 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=23619560.0 spike=0.31
- ROTO.CA: score=24.4 buy_ready=False sector_rank=15 price=41.33 support=33.06 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=71.36 liquidity=11541498.0 spike=0.36
- RREI.CA: score=33.4 buy_ready=True sector_rank=15 price=3.76 support=3.34 resistance=3.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.81 liquidity=77869232.0 spike=5.26
- RTVC.CA: score=15.25 buy_ready=False sector_rank=15 price=3.76 support=3.55 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=3850226.25 spike=0.76
- RUBX.CA: score=22.46 buy_ready=False sector_rank=15 price=12.9 support=9.8 resistance=14.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=81.21 liquidity=74602608.0 spike=1.53
- SAUD.CA: score=16.06 buy_ready=False sector_rank=17 price=21.16 support=19.99 resistance=22.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=46.63 liquidity=5249126.5 spike=0.72
- SCEM.CA: score=22.94 buy_ready=False sector_rank=11 price=62.46 support=59.3 resistance=67.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.79 liquidity=9541369.0 spike=0.51
- SCFM.CA: score=14.8 buy_ready=False sector_rank=15 price=243.42 support=226.5 resistance=265.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=46.36 liquidity=3397685.75 spike=0.82
- SCTS.CA: score=17.13 buy_ready=False sector_rank=13 price=608.52 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=61.71 liquidity=3732714.5 spike=0.74
- SDTI.CA: score=15.43 buy_ready=False sector_rank=15 price=46.28 support=45.55 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.65 liquidity=3030326.75 spike=0.32
- SEIG.CA: score=14.4 buy_ready=False sector_rank=15 price=257.67 support=228.51 resistance=272.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=166478688.0 spike=35.87
- SIPC.CA: score=18.51 buy_ready=False sector_rank=15 price=3.42 support=3.25 resistance=3.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.41 liquidity=7114696.5 spike=0.68
- SKPC.CA: score=23.18 buy_ready=False sector_rank=19 price=16.38 support=15.58 resistance=17.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.39 liquidity=59286448.0 spike=1.84
- SMFR.CA: score=13.97 buy_ready=False sector_rank=15 price=203.33 support=187.01 resistance=209.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.4 liquidity=566530.31 spike=0.25
- SNFC.CA: score=12.13 buy_ready=False sector_rank=15 price=11.49 support=11.26 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.37 liquidity=7725183.5 spike=0.61
- SPIN.CA: score=20.54 buy_ready=True sector_rank=7 price=14.55 support=13.3 resistance=14.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.34 liquidity=6135504.0 spike=0.7
- SPMD.CA: score=27.48 buy_ready=True sector_rank=15 price=0.44 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.02 liquidity=45540188.0 spike=2.54
- SUGR.CA: score=7.15 buy_ready=False sector_rank=8 price=46.71 support=45.31 resistance=50.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=31.53 liquidity=3751598.25 spike=0.69
- SVCE.CA: score=26.4 buy_ready=True sector_rank=15 price=9.15 support=8.11 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.48 liquidity=34787108.0 spike=0.48
- SWDY.CA: score=26.31 buy_ready=True sector_rank=16 price=87.74 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=67.21 liquidity=12376119.0 spike=0.92
- TALM.CA: score=14.72 buy_ready=False sector_rank=13 price=15.43 support=15.38 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=28.35 liquidity=13459228.0 spike=1.16
- TMGH.CA: score=29.4 buy_ready=True sector_rank=3 price=97.0 support=92.1 resistance=99.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=59.88 liquidity=334318112.0 spike=0.93
- TRTO.CA: score=12.46 buy_ready=False sector_rank=15 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-07-06T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=1232.06 spike=2.03
- UEFM.CA: score=14.22 buy_ready=False sector_rank=15 price=480.28 support=460.0 resistance=505.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=59.39 liquidity=817663.81 spike=0.75
- UEGC.CA: score=9.66 buy_ready=False sector_rank=15 price=1.72 support=1.58 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32882226.0 spike=1.13
- UNIP.CA: score=16.62 buy_ready=False sector_rank=15 price=0.32 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.21 liquidity=4222416.5 spike=0.17
- UNIT.CA: score=26.72 buy_ready=False sector_rank=3 price=16.75 support=12.0 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=80.22 liquidity=21645296.0 spike=2.16
- WCDF.CA: score=4.7 buy_ready=False sector_rank=15 price=523.65 support=450.0 resistance=544.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=8.18 liquidity=304227.47 spike=0.8
- WKOL.CA: score=21.74 buy_ready=False sector_rank=15 price=308.42 support=273.1 resistance=334.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=75.27 liquidity=7858421.0 spike=1.24
- ZEOT.CA: score=24.4 buy_ready=True sector_rank=15 price=10.99 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.08 liquidity=15810068.0 spike=0.41
- ZMID.CA: score=27.4 buy_ready=False sector_rank=3 price=6.65 support=6.03 resistance=6.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.37 liquidity=116116240.0 spike=0.55

## Backtesting Lite
- RREI.CA: 180d return=55.6%, max drawdown=-27.36%, MA20>MA50 days last20=4, as_of=2026-07-06T21:00:00+00:00
- BIOC.CA: 180d return=2.34%, max drawdown=-19.91%, MA20>MA50 days last20=17, as_of=2026-07-06T21:00:00+00:00
- MIPH.CA: 180d return=113.77%, max drawdown=-11.96%, MA20>MA50 days last20=19, as_of=2026-07-06T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- RREI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Arab Real Estate Investment Co. summary=Evidence rejected for RREI.CA: source text did not clearly match RREI.CA / Arab Real Estate Investment Co..
- BIOC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GlaxoSmithKline S.A.E summary=Evidence rejected for BIOC.CA: source text did not clearly match BIOC.CA / GlaxoSmithKline S.A.E.
- MIPH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Minapharm Pharmaceuticals summary=Minapharm’ consolidated net profits retreat to EGP 62m in 9M-25; Minapharm posts EGP 66.5m standalone net profits in 9M-25; sales hit EGP 2.8bn; Investor buys EGP 1.3bn stake in Minapharm Pharmaceuticals Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Minapharm’ consolidated net profits retreat to EGP 62m in 9M-25: https://english.mubasher.info/news/4531893/Minapharm-consolidated-net-profits-retreat-to-EGP-62m-in-9M-25/
  - Minapharm posts EGP 66.5m standalone net profits in 9M-25; sales hit EGP 2.8bn: https://english.mubasher.info/news/4528557/Minapharm-posts-EGP-66-5m-standalone-net-profits-in-9M-25-sales-hit-EGP-2-8bn/
  - Investor buys EGP 1.3bn stake in Minapharm Pharmaceuticals: https://english.mubasher.info/news/4295954/Investor-buys-EGP-1-3bn-stake-in-Minapharm-Pharmaceuticals/
- HELI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Heliopolis Housing summary=Evidence rejected for HELI.CA: source text did not clearly match HELI.CA / Heliopolis Housing.
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- PRDC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Pioneers Properties For Urban Development summary=Evidence rejected for PRDC.CA: source text did not clearly match PRDC.CA / Pioneers Properties For Urban Development.
- TMGH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talaat Moustafa Group Holding summary=Evidence rejected for TMGH.CA: source text did not clearly match TMGH.CA / Talaat Moustafa Group Holding.
- AMER.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=553 sources=3 expected=Amer Group Holding summary=Amer Group stock holds above EGP 1.95 as bulls target higher levels; Amer Group’s consolidated profits hit EGP 196m in 2025; Amer Group stock’s technical outlook on profit-taking, holding above main support – Analysis Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Amer Group stock holds above EGP 1.95 as bulls target higher levels: https://english.mubasher.info/news/4583812/Amer-Group-stock-holds-above-EGP-1-95-as-bulls-target-higher-levels/
  - Amer Group’s consolidated profits hit EGP 196m in 2025: https://english.mubasher.info/news/4563160/Amer-Group-s-consolidated-profits-hit-EGP-196m-in-2025/
  - Amer Group stock’s technical outlook on profit-taking, holding above main support – Analysis: https://english.mubasher.info/news/4546813/Amer-Group-stock-s-technical-outlook-on-profit-taking-holding-above-main-support-Analysis/

## Warnings
- Evidence rejected for RREI.CA: source text did not clearly match RREI.CA / Arab Real Estate Investment Co..
- Evidence rejected for BIOC.CA: source text did not clearly match BIOC.CA / GlaxoSmithKline S.A.E.
- Evidence for MIPH.CA matches the company but no source/report date was detected.
- Evidence rejected for HELI.CA: source text did not clearly match HELI.CA / Heliopolis Housing.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence rejected for PRDC.CA: source text did not clearly match PRDC.CA / Pioneers Properties For Urban Development.
- Evidence rejected for TMGH.CA: source text did not clearly match TMGH.CA / Talaat Moustafa Group Holding.
- Evidence for AMER.CA matches the company but appears old; latest detected date is 2025-01-01.
