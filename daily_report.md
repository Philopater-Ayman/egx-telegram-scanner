# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-06-07T10:30:43.065313+00:00
Generated Cairo: 2026-06-07 13:30
Run timing: target 11:00 Cairo | generated Cairo 2026-06-07 13:30 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-06-07 13:25

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 79
- Data quality issues: 0
- Tradeable price/liquidity tickers: 183/190
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, June 07
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 35.0% / above MA50 75.0%
- EGX70 regime: CONSTRUCTIVE / above MA20 57.5% / above MA50 82.5%
- Sector breadth: 80.95%
- Risk mode: SELECTIVE_SMALL_MID_SWINGS

## Top Liquidity
- CCAP.CA: liquidity=753533440.0 spike=0.92 score=24.4
- EMFD.CA: liquidity=750723648.0 spike=3.98 score=33.4
- PHDC.CA: liquidity=185418112.0 spike=0.41 score=26.4
- FWRY.CA: liquidity=172265776.0 spike=0.63 score=17.58
- MPCO.CA: liquidity=163410096.0 spike=2.97 score=30.34

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner highlighted a handful of bullish‑watch candidates—EMFD.CA, UEGC.CA, NCCW.CA, COSG.CA, GGCC.CA and MPCO.CA—because they cleared liquidity, freshness and technical gates, showing strong accumulation spikes, price near short‑term resistance and RSI in the upper‑mid range. EGX30 remains bearish, limiting broad‑market upside, while EGX70 stays constructive, allowing selective small‑mid swing opportunities, especially in leading sectors like Real Estate and Tourism & Leisure. Expect modest upside over the next 1‑3 days, but beware of the bearish EGX30 backdrop and the proximity of many stocks to resistance.
- Liquidity spikes (≈4× avg) and buy‑ready signals flag EMFD, UEGC, NCCW, COSG, GGCC and MPCO as top picks.
- All are near 20‑day resistance with RSI 63‑68, indicating momentum but limited upside cushion.
- EGX30 bearish trend (only 35% above MA20) pushes risk mode to SELECTIVE_SMALL_MID_SWINGS; EGX70 constructive (57% above MA20) supports sector‑driven plays.
- Real Estate leads sector breadth (80.95%); tourism & leisure also strong, reinforcing focus on EMFD and similar stocks.
- Uncertainty remains from overall market weakness and potential pull‑back at resistance levels.

## Top Liquidity Spikes
- LUTS.CA: spike=14.18 liquidity=92147176.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- UNIP.CA: spike=4.56 liquidity=56115952.0 outlook=CONSTRUCTIVE score=63.01 buy_ready=False
- AREH.CA: spike=4.34 liquidity=93041024.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- UEGC.CA: spike=4.07 liquidity=81401896.0 outlook=BULLISH_WATCH score=82.01 buy_ready=True
- EMFD.CA: spike=3.98 liquidity=750723648.0 outlook=BULLISH_WATCH score=91 buy_ready=True

## Sector Leaderboard
- #1 Tourism & Leisure: score=11.69 5d=4.25% 20d=18.02% aboveMA50=100.0%
- #2 Real Estate: score=10.47 5d=2.83% 20d=18.03% aboveMA50=100.0%
- #3 Technology & Distribution: score=10.37 5d=0.94% 20d=18.9% aboveMA50=100.0%
- #4 Investment Holding: score=8.6 5d=4.69% 20d=10.97% aboveMA50=66.67%
- #5 Agriculture & Food Production: score=8.59 5d=6.74% 20d=2.37% aboveMA50=50.0%
- #6 Industrial Goods & Cables: score=7.64 5d=2.04% 20d=1.18% aboveMA50=100.0%
- #7 Textiles: score=7.53 5d=2.4% 20d=6.38% aboveMA50=75.0%
- #8 Healthcare: score=7.48 5d=3.52% 20d=4.36% aboveMA50=83.33%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ZMID.CA: BULLISH_WATCH score=96 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- EMFD.CA: BULLISH_WATCH score=91 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended; far above support; close to resistance
- ARAB.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- AMER.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- RAYA.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MPCO.CA: BULLISH_WATCH score=89.59 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- UNIT.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- GDWA.CA: BULLISH_WATCH score=85.01 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance; sector is not leading
- UEGC.CA: BULLISH_WATCH score=82.01 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- PHDC.CA: BULLISH_WATCH score=82 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended

## BUY-Ready Candidates
- EMFD.CA: rank=33.4 outlook=BULLISH_WATCH outlook_score=91 sector_rank=2 price=12.29 support=9.83 resistance=12.38 liquidity=750723648.0
- UEGC.CA: rank=31.4 outlook=BULLISH_WATCH outlook_score=82.01 sector_rank=11 price=1.5 support=1.3 resistance=1.46 liquidity=81401896.0
- NCCW.CA: rank=31.4 outlook=BULLISH_WATCH outlook_score=72.01 sector_rank=11 price=6.19 support=5.13 resistance=6.2 liquidity=65960180.0
- COSG.CA: rank=31.28 outlook=BULLISH_WATCH outlook_score=76.01 sector_rank=11 price=1.69 support=1.44 resistance=1.71 liquidity=125588992.0
- GGCC.CA: rank=30.4 outlook=BULLISH_WATCH outlook_score=77.01 sector_rank=11 price=0.44 support=0.39 resistance=0.44 liquidity=20420148.0
- MPCO.CA: rank=30.34 outlook=BULLISH_WATCH outlook_score=89.59 sector_rank=5 price=1.81 support=1.54 resistance=1.88 liquidity=163410096.0
- MPRC.CA: rank=28.76 outlook=BULLISH_WATCH outlook_score=78.01 sector_rank=11 price=34.25 support=30.1 resistance=33.7 liquidity=22311996.0
- GDWA.CA: rank=28.66 outlook=BULLISH_WATCH outlook_score=85.01 sector_rank=11 price=0.82 support=0.77 resistance=0.83 liquidity=17852864.0
- JUFO.CA: rank=28.4 outlook=BULLISH_WATCH outlook_score=73.06 sector_rank=10 price=29.43 support=26.51 resistance=29.98 liquidity=16339525.0
- ARAB.CA: rank=28.4 outlook=BULLISH_WATCH outlook_score=90 sector_rank=2 price=0.21 support=0.19 resistance=0.22 liquidity=34833792.0

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=18.28 buy_ready=True sector_rank=11 price=211.12 support=195.1 resistance=249.99 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=40.2 liquidity=3883552.31 spike=0.41
- ABUK.CA: score=18.17 buy_ready=False sector_rank=18 price=81.6 support=81.52 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=37.92 liquidity=43459144.0 spike=0.33
- ACAMD.CA: score=26.4 buy_ready=True sector_rank=11 price=2.37 support=1.94 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=63.64 liquidity=105707144.0 spike=0.95
- ACGC.CA: score=24.4 buy_ready=True sector_rank=7 price=10.09 support=8.3 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=67.34 liquidity=29359506.0 spike=0.55
- ADCI.CA: score=16.4 buy_ready=True sector_rank=11 price=217.53 support=198.0 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=47.01 liquidity=2003678.38 spike=0.27
- ADIB.CA: score=21.65 buy_ready=False sector_rank=17 price=47.07 support=44.45 resistance=50.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=44.38 liquidity=29719626.0 spike=0.17
- ADPC.CA: score=20.06 buy_ready=False sector_rank=11 price=3.73 support=3.54 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=44.35 liquidity=7657078.0 spike=0.32
- AFDI.CA: score=23.13 buy_ready=True sector_rank=11 price=45.51 support=36.82 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=58.02 liquidity=6727162.0 spike=0.36
- AFMC.CA: score=19.8 buy_ready=True sector_rank=11 price=73.85 support=69.33 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=38.17 liquidity=5398562.0 spike=0.37
- AJWA.CA: score=18.46 buy_ready=True sector_rank=11 price=135.92 support=130.01 resistance=139.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=44.23 liquidity=4057860.0 spike=0.37
- ALCN.CA: score=17.48 buy_ready=False sector_rank=15 price=29.19 support=28.4 resistance=30.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=45.19 liquidity=6605687.5 spike=0.24
- ALUM.CA: score=23.37 buy_ready=True sector_rank=11 price=25.59 support=22.35 resistance=26.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=46.39 liquidity=8967805.0 spike=0.4
- AMER.CA: score=26.4 buy_ready=True sector_rank=2 price=2.7 support=2.29 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=49.4 liquidity=17478844.0 spike=0.13
- AMES.CA: score=9.23 buy_ready=False sector_rank=11 price=50.88 support=48.0 resistance=59.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=21.16 liquidity=1827017.63 spike=0.15
- AMIA.CA: score=17.26 buy_ready=False sector_rank=11 price=8.97 support=8.16 resistance=10.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=31.86 liquidity=7860207.0 spike=0.23
- AMOC.CA: score=19.27 buy_ready=False sector_rank=13 price=8.23 support=8.12 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=43.38 liquidity=32961192.0 spike=0.38
- ANFI.CA: score=13.04 buy_ready=False sector_rank=11 price=14.05 support=13.5 resistance=15.55 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=24.73 liquidity=5638883.28 spike=0.28
- APSW.CA: score=14.78 buy_ready=False sector_rank=11 price=8.99 support=8.62 resistance=9.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=49.5 liquidity=384156.34 spike=0.31
- ARAB.CA: score=28.4 buy_ready=True sector_rank=2 price=0.21 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=51.72 liquidity=34833792.0 spike=0.46
- ARCC.CA: score=26.4 buy_ready=True sector_rank=9 price=59.0 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=56.59 liquidity=27295740.0 spike=0.61
- AREH.CA: score=14.4 buy_ready=False sector_rank=11 price=1.5 support=1.4 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=93041024.0 spike=4.34
- ARVA.CA: score=27.3 buy_ready=True sector_rank=11 price=10.91 support=7.71 resistance=10.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=36462908.0 spike=1.45
- ASCM.CA: score=24.72 buy_ready=True sector_rank=11 price=56.95 support=43.76 resistance=59.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=65.89 liquidity=71535040.0 spike=1.16
- ASPI.CA: score=12.1 buy_ready=False sector_rank=11 price=0.35 support=0.35 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=109735320.0 spike=2.35
- ATLC.CA: score=13.41 buy_ready=False sector_rank=16 price=5.01 support=4.71 resistance=5.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=32.53 liquidity=4566662.5 spike=0.57
- ATQA.CA: score=25.17 buy_ready=True sector_rank=18 price=9.95 support=9.41 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=49.67 liquidity=17835224.0 spike=0.36
- AXPH.CA: score=8.88 buy_ready=False sector_rank=11 price=1128.99 support=960.0 resistance=1239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=7.55 liquidity=1484514.38 spike=0.25
- BINV.CA: score=19.05 buy_ready=True sector_rank=4 price=46.0 support=40.5 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=67.08 liquidity=4651820.0 spike=0.35
- BIOC.CA: score=17.49 buy_ready=True sector_rank=11 price=73.79 support=70.0 resistance=79.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=41.46 liquidity=3094133.5 spike=0.39
- BTFH.CA: score=20.84 buy_ready=False sector_rank=16 price=3.09 support=3.03 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=36.17 liquidity=110209040.0 spike=0.45
- CAED.CA: score=8.52 buy_ready=False sector_rank=11 price=71.43 support=64.49 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=24.28 liquidity=1115810.0 spike=0.07
- CANA.CA: score=25.77 buy_ready=True sector_rank=17 price=37.01 support=33.15 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=44.06 liquidity=14680712.0 spike=1.06
- CCAP.CA: score=24.4 buy_ready=True sector_rank=4 price=5.57 support=4.47 resistance=5.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=753533440.0 spike=0.92
- CCRS.CA: score=22.4 buy_ready=True sector_rank=11 price=2.57 support=1.98 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=65.79 liquidity=24352766.0 spike=0.88
- CEFM.CA: score=10.0 buy_ready=False sector_rank=11 price=107.16 support=103.07 resistance=119.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=28.81 liquidity=2598063.0 spike=0.35
- CERA.CA: score=19.28 buy_ready=True sector_rank=11 price=1.19 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=5876811.0 spike=0.43
- CFGH.CA: score=4.61 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=6311.86 spike=1.6
- CICH.CA: score=7.68 buy_ready=False sector_rank=16 price=12.31 support=10.9 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=33.16 liquidity=839935.0 spike=0.19
- CIEB.CA: score=15.54 buy_ready=True sector_rank=17 price=23.69 support=23.31 resistance=24.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=43.48 liquidity=1884676.38 spike=0.15
- CIRA.CA: score=18.79 buy_ready=True sector_rank=14 price=26.99 support=19.5 resistance=28.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=40.77 liquidity=4876118.0 spike=0.17
- CLHO.CA: score=24.4 buy_ready=True sector_rank=8 price=15.89 support=14.58 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=48.56 liquidity=10090282.0 spike=0.26
- CNFN.CA: score=12.93 buy_ready=False sector_rank=16 price=4.57 support=4.41 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=30.26 liquidity=7087340.5 spike=0.44
- COMI.CA: score=21.65 buy_ready=False sector_rank=17 price=131.83 support=131.3 resistance=144.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=44.39 liquidity=86448312.0 spike=0.13
- COPR.CA: score=18.4 buy_ready=False sector_rank=11 price=0.36 support=0.3 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=77.27 liquidity=36506104.0 spike=0.98
- COSG.CA: score=31.28 buy_ready=True sector_rank=11 price=1.69 support=1.44 resistance=1.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=63.89 liquidity=125588992.0 spike=2.44
- CPCI.CA: score=12.89 buy_ready=False sector_rank=11 price=364.44 support=336.0 resistance=374.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=75.65 liquidity=1489201.25 spike=0.19
- CSAG.CA: score=22.96 buy_ready=True sector_rank=15 price=31.88 support=30.4 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=5080084.0 spike=0.25
- DAPH.CA: score=17.4 buy_ready=False sector_rank=11 price=81.36 support=79.25 resistance=96.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=17.24 liquidity=11392255.0 spike=0.36
- DEIN.CA: score=10.4 buy_ready=False sector_rank=11 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=8.1 buy_ready=False sector_rank=10 price=24.5 support=24.7 resistance=26.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=34.39 liquidity=3057583.25 spike=1.32
- DSCW.CA: score=22.4 buy_ready=False sector_rank=11 price=1.85 support=1.71 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=44.83 liquidity=28191822.0 spike=0.42
- DTPP.CA: score=8.86 buy_ready=False sector_rank=11 price=124.96 support=121.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=28.41 liquidity=1464816.0 spike=0.23
- EALR.CA: score=13.65 buy_ready=False sector_rank=11 price=360.42 support=346.01 resistance=429.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=35.9 liquidity=1253118.38 spike=0.07
- EASB.CA: score=16.88 buy_ready=True sector_rank=11 price=5.0 support=4.61 resistance=5.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=2058020.63 spike=1.21
- EAST.CA: score=24.4 buy_ready=True sector_rank=10 price=38.75 support=37.01 resistance=39.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=48.01 liquidity=16991674.0 spike=0.24
- EBSC.CA: score=18.38 buy_ready=True sector_rank=11 price=1.9 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=68.29 liquidity=1977818.88 spike=0.66
- ECAP.CA: score=16.7 buy_ready=True sector_rank=11 price=30.94 support=28.7 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=51.75 liquidity=2296087.75 spike=0.43
- EDFM.CA: score=13.02 buy_ready=False sector_rank=11 price=334.4 support=320.2 resistance=364.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=48.99 liquidity=622014.69 spike=0.54
- EEII.CA: score=20.2 buy_ready=True sector_rank=11 price=2.4 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=43.48 liquidity=5797623.0 spike=0.32
- EFIC.CA: score=3.8 buy_ready=False sector_rank=18 price=205.67 support=195.25 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=26.74 liquidity=626379.38 spike=0.14
- EFID.CA: score=24.4 buy_ready=False sector_rank=10 price=28.75 support=27.49 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=71.91 liquidity=13935224.0 spike=0.29
- EFIH.CA: score=19.47 buy_ready=False sector_rank=20 price=21.95 support=21.0 resistance=22.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=54.51 liquidity=8887413.0 spike=0.14
- EGAL.CA: score=23.17 buy_ready=True sector_rank=18 price=325.69 support=295.0 resistance=344.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=43.9 liquidity=16346569.0 spike=0.14
- EGAS.CA: score=22.17 buy_ready=True sector_rank=13 price=51.0 support=46.51 resistance=51.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=60.23 liquidity=5900004.5 spike=0.34
- EGBE.CA: score=11.67 buy_ready=False sector_rank=17 price=0.45 support=0.41 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=35.13 liquidity=18405.48 spike=0.12
- EGCH.CA: score=25.17 buy_ready=True sector_rank=18 price=14.6 support=11.77 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=55.27 liquidity=29937576.0 spike=0.25
- EGSA.CA: score=9.37 buy_ready=False sector_rank=12 price=9.02 support=8.24 resistance=9.19 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=89.86 liquidity=2291.08 spike=0.2
- EGTS.CA: score=26.4 buy_ready=False sector_rank=2 price=18.96 support=12.9 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=70.39 liquidity=29968534.0 spike=0.28
- EHDR.CA: score=23.4 buy_ready=False sector_rank=11 price=2.69 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=76.81 liquidity=47668868.0 spike=0.95
- EKHO.CA: score=14.27 buy_ready=False sector_rank=13 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=25.4 buy_ready=True sector_rank=6 price=2.19 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=14836405.0 spike=0.48
- ELKA.CA: score=26.02 buy_ready=True sector_rank=11 price=1.27 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=68.97 liquidity=51859180.0 spike=1.31
- ELNA.CA: score=7.71 buy_ready=False sector_rank=11 price=39.51 support=38.0 resistance=42.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=306592.84 spike=0.71
- ELSH.CA: score=23.4 buy_ready=False sector_rank=11 price=11.47 support=7.8 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=90.09 liquidity=73502168.0 spike=0.85
- ELWA.CA: score=14.05 buy_ready=False sector_rank=11 price=2.05 support=1.79 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=81.48 liquidity=2647374.75 spike=0.93
- EMFD.CA: score=33.4 buy_ready=True sector_rank=2 price=12.29 support=9.83 resistance=12.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=67.51 liquidity=750723648.0 spike=3.98
- ENGC.CA: score=17.31 buy_ready=False sector_rank=11 price=33.64 support=32.31 resistance=35.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=39.43 liquidity=4910400.5 spike=0.4
- EOSB.CA: score=12.5 buy_ready=False sector_rank=11 price=1.42 support=1.34 resistance=1.54 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=95148.52 spike=0.84
- EPCO.CA: score=23.03 buy_ready=True sector_rank=11 price=9.4 support=8.56 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=44.2 liquidity=8627640.0 spike=0.69
- EPPK.CA: score=5.32 buy_ready=False sector_rank=11 price=12.01 support=12.0 resistance=13.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=33.18 liquidity=922273.0 spike=0.82
- ETEL.CA: score=22.37 buy_ready=False sector_rank=12 price=95.66 support=93.01 resistance=101.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=51.34 liquidity=13109726.0 spike=0.12
- ETRS.CA: score=23.4 buy_ready=False sector_rank=11 price=9.37 support=7.37 resistance=9.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=77.78 liquidity=38231952.0 spike=0.76
- EXPA.CA: score=21.65 buy_ready=False sector_rank=17 price=18.64 support=18.34 resistance=19.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=35.67 liquidity=16077141.0 spike=0.38
- FAIT.CA: score=14.67 buy_ready=True sector_rank=17 price=37.5 support=33.5 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=61.11 liquidity=1020786.13 spike=0.14
- FAITA.CA: score=15.1 buy_ready=False sector_rank=17 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=91908.73 spike=1.68
- FERC.CA: score=4.97 buy_ready=False sector_rank=18 price=78.03 support=76.5 resistance=83.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=26.23 liquidity=1796779.0 spike=0.25
- FWRY.CA: score=17.58 buy_ready=False sector_rank=20 price=18.92 support=19.03 resistance=21.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=39.11 liquidity=172265776.0 spike=0.63
- GBCO.CA: score=12.45 buy_ready=False sector_rank=21 price=26.01 support=25.25 resistance=29.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=25.93 liquidity=26526426.0 spike=0.23
- GDWA.CA: score=28.66 buy_ready=True sector_rank=11 price=0.82 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=17852864.0 spike=1.63
- GGCC.CA: score=30.4 buy_ready=True sector_rank=11 price=0.44 support=0.39 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=20420148.0 spike=3.74
- GIHD.CA: score=17.69 buy_ready=True sector_rank=11 price=42.19 support=39.1 resistance=44.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=43.64 liquidity=1289273.5 spike=0.22
- GMCI.CA: score=18.4 buy_ready=False sector_rank=11 price=1.8 support=1.67 resistance=1.84 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=598390.18 spike=1.7
- GRCA.CA: score=5.01 buy_ready=False sector_rank=11 price=55.0 support=54.5 resistance=58.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5613053.5 spike=0.59
- GSSC.CA: score=6.55 buy_ready=False sector_rank=11 price=247.97 support=250.0 resistance=275.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=12.18 liquidity=2150056.25 spike=0.18
- GTWL.CA: score=8.38 buy_ready=False sector_rank=11 price=46.98 support=47.5 resistance=59.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=11.86 liquidity=3981882.5 spike=0.33
- HDBK.CA: score=15.0 buy_ready=False sector_rank=17 price=140.19 support=140.0 resistance=150.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=41.86 liquidity=6346654.5 spike=0.37
- HELI.CA: score=24.4 buy_ready=False sector_rank=2 price=6.47 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=53.96 liquidity=30801204.0 spike=0.16
- HRHO.CA: score=12.84 buy_ready=False sector_rank=16 price=26.51 support=26.16 resistance=30.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=34.27 liquidity=57878344.0 spike=0.28
- ICID.CA: score=23.4 buy_ready=False sector_rank=11 price=5.92 support=4.37 resistance=6.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=76.67 liquidity=10712035.0 spike=0.89
- IDRE.CA: score=22.67 buy_ready=True sector_rank=11 price=45.32 support=39.51 resistance=49.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=49.96 liquidity=8267518.0 spike=0.24
- IFAP.CA: score=9.62 buy_ready=False sector_rank=5 price=19.67 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=26.58 liquidity=5223151.0 spike=0.26
- INFI.CA: score=10.41 buy_ready=False sector_rank=11 price=101.16 support=100.05 resistance=112.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=34.14 liquidity=4005292.25 spike=0.22
- IRON.CA: score=11.43 buy_ready=False sector_rank=18 price=32.67 support=31.83 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=50.09 liquidity=2259099.5 spike=0.26
- ISMA.CA: score=9.4 buy_ready=False sector_rank=11 price=29.09 support=27.79 resistance=29.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35175184.0 spike=0.75
- ISMQ.CA: score=25.17 buy_ready=True sector_rank=18 price=7.74 support=7.27 resistance=8.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=51.72 liquidity=19497656.0 spike=0.35
- ISPH.CA: score=26.4 buy_ready=True sector_rank=8 price=12.56 support=10.87 resistance=12.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=66.24 liquidity=65320204.0 spike=0.47
- JUFO.CA: score=28.4 buy_ready=True sector_rank=10 price=29.43 support=26.51 resistance=29.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=54.56 liquidity=16339525.0 spike=0.33
- KABO.CA: score=24.4 buy_ready=True sector_rank=7 price=6.4 support=5.92 resistance=6.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=67.03 liquidity=14015966.0 spike=0.78
- KWIN.CA: score=17.91 buy_ready=True sector_rank=11 price=73.11 support=69.0 resistance=81.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=41.93 liquidity=3508994.75 spike=0.72
- KZPC.CA: score=14.04 buy_ready=False sector_rank=11 price=10.75 support=10.3 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=30.68 liquidity=4643738.5 spike=0.35
- LCSW.CA: score=16.61 buy_ready=False sector_rank=9 price=27.08 support=26.16 resistance=29.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=39.05 liquidity=4212933.0 spike=0.24
- LUTS.CA: score=14.4 buy_ready=False sector_rank=11 price=0.64 support=0.6 resistance=0.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=92147176.0 spike=14.18
- MAAL.CA: score=25.86 buy_ready=False sector_rank=11 price=6.01 support=4.44 resistance=5.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=93.43 liquidity=22644678.0 spike=2.23
- MASR.CA: score=21.38 buy_ready=False sector_rank=11 price=6.84 support=6.26 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=36.61 liquidity=8976788.0 spike=0.13
- MBSC.CA: score=22.4 buy_ready=False sector_rank=9 price=271.51 support=259.0 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=58.99 liquidity=19862626.0 spike=0.42
- MCQE.CA: score=17.4 buy_ready=True sector_rank=9 price=194.14 support=188.01 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=50.91 liquidity=3004530.0 spike=0.15
- MCRO.CA: score=25.4 buy_ready=True sector_rank=11 price=1.28 support=1.21 resistance=1.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=31387568.0 spike=0.3
- MENA.CA: score=19.92 buy_ready=True sector_rank=2 price=6.92 support=5.76 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=68.88 liquidity=3520766.75 spike=0.22
- MEPA.CA: score=24.4 buy_ready=True sector_rank=11 price=1.75 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=18447432.0 spike=0.68
- MFPC.CA: score=21.17 buy_ready=False sector_rank=18 price=42.61 support=42.55 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=40.03 liquidity=20992740.0 spike=0.19
- MFSC.CA: score=17.62 buy_ready=False sector_rank=11 price=47.89 support=33.0 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=55.64 liquidity=5217264.5 spike=0.36
- MHOT.CA: score=24.46 buy_ready=True sector_rank=1 price=31.31 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=64.7 liquidity=5058512.0 spike=0.26
- MICH.CA: score=22.63 buy_ready=True sector_rank=11 price=36.48 support=35.01 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=59.23 liquidity=6233631.5 spike=0.7
- MILS.CA: score=24.4 buy_ready=True sector_rank=11 price=145.81 support=126.02 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=48.48 liquidity=12216667.0 spike=0.43
- MIPH.CA: score=11.66 buy_ready=False sector_rank=8 price=674.84 support=640.0 resistance=729.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=33.89 liquidity=2257968.75 spike=0.46
- MOED.CA: score=5.95 buy_ready=False sector_rank=11 price=0.7 support=0.68 resistance=0.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=12.06 liquidity=2545193.25 spike=0.19
- MOIL.CA: score=16.34 buy_ready=False sector_rank=13 price=0.47 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=56.92 liquidity=69716.54 spike=0.35
- MOIN.CA: score=14.03 buy_ready=False sector_rank=11 price=25.35 support=23.13 resistance=26.4 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=69.6 liquidity=630606.61 spike=0.33
- MOSC.CA: score=9.48 buy_ready=False sector_rank=11 price=275.05 support=271.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=18.62 liquidity=2081901.75 spike=0.1
- MPCI.CA: score=26.4 buy_ready=True sector_rank=11 price=222.08 support=182.01 resistance=224.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=52.45 liquidity=59024624.0 spike=0.61
- MPCO.CA: score=30.34 buy_ready=True sector_rank=5 price=1.81 support=1.54 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=65.22 liquidity=163410096.0 spike=2.97
- MPRC.CA: score=28.76 buy_ready=True sector_rank=11 price=34.25 support=30.1 resistance=33.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=57.82 liquidity=22311996.0 spike=1.18
- MTIE.CA: score=14.87 buy_ready=False sector_rank=21 price=9.04 support=8.71 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=45.74 liquidity=4423716.0 spike=0.14
- NAHO.CA: score=5.42 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=17721.0 spike=0.47
- NCCW.CA: score=31.4 buy_ready=True sector_rank=11 price=6.19 support=5.13 resistance=6.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=66.49 liquidity=65960180.0 spike=3.9
- NEDA.CA: score=15.72 buy_ready=False sector_rank=11 price=2.83 support=2.65 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=998227.38 spike=1.16
- NHPS.CA: score=10.04 buy_ready=False sector_rank=11 price=69.32 support=67.56 resistance=76.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=34.42 liquidity=3642323.0 spike=0.3
- NINH.CA: score=14.62 buy_ready=False sector_rank=11 price=18.03 support=17.53 resistance=20.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=39.27 liquidity=2221496.5 spike=0.14
- NIPH.CA: score=9.82 buy_ready=False sector_rank=8 price=172.71 support=162.01 resistance=176.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=145571728.0 spike=1.21
- OBRI.CA: score=9.06 buy_ready=False sector_rank=11 price=34.57 support=34.53 resistance=39.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=22.56 liquidity=4660950.5 spike=0.33
- OCDI.CA: score=21.5 buy_ready=False sector_rank=2 price=21.26 support=20.19 resistance=23.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=39.21 liquidity=7096372.5 spike=0.16
- OCPH.CA: score=15.05 buy_ready=False sector_rank=11 price=363.3 support=350.0 resistance=409.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=8.63 liquidity=7646548.5 spike=0.46
- ODIN.CA: score=25.73 buy_ready=True sector_rank=11 price=2.1 support=1.89 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=7327378.0 spike=0.66
- OFH.CA: score=27.73 buy_ready=True sector_rank=11 price=0.65 support=0.6 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=57.55 liquidity=9331233.0 spike=0.4
- OIH.CA: score=14.4 buy_ready=False sector_rank=4 price=1.38 support=1.4 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=20.0 liquidity=48207028.0 spike=0.32
- OLFI.CA: score=20.54 buy_ready=False sector_rank=10 price=21.61 support=21.0 resistance=22.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=37.65 liquidity=8138793.5 spike=0.36
- ORAS.CA: score=7.6 buy_ready=False sector_rank=19 price=730.2 support=728.0 resistance=739.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=53879928.0 spike=1.0
- ORHD.CA: score=26.4 buy_ready=False sector_rank=2 price=37.5 support=30.56 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=72.05 liquidity=54760696.0 spike=0.26
- ORWE.CA: score=24.4 buy_ready=False sector_rank=7 price=23.83 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=70.18 liquidity=24662270.0 spike=0.51
- PHAR.CA: score=22.4 buy_ready=False sector_rank=8 price=86.6 support=83.96 resistance=92.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=35.03 liquidity=19632346.0 spike=0.53
- PHDC.CA: score=26.4 buy_ready=True sector_rank=2 price=14.85 support=12.7 resistance=16.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=63.76 liquidity=185418112.0 spike=0.41
- PHTV.CA: score=15.55 buy_ready=False sector_rank=11 price=206.29 support=201.5 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=47.65 liquidity=3148797.75 spike=0.2
- POUL.CA: score=21.34 buy_ready=True sector_rank=10 price=37.69 support=34.06 resistance=39.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=53.75 liquidity=6938466.5 spike=0.13
- PRCL.CA: score=23.33 buy_ready=True sector_rank=9 price=24.0 support=20.8 resistance=25.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=56.18 liquidity=8934957.0 spike=0.28
- PRDC.CA: score=27.66 buy_ready=True sector_rank=2 price=6.2 support=5.09 resistance=6.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=68.79 liquidity=9262797.0 spike=0.45
- PRMH.CA: score=23.46 buy_ready=False sector_rank=11 price=2.85 support=2.17 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=79.35 liquidity=14981372.0 spike=1.03
- RACC.CA: score=19.46 buy_ready=False sector_rank=11 price=9.94 support=9.56 resistance=12.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=46.45 liquidity=7060319.5 spike=0.2
- RAKT.CA: score=12.62 buy_ready=False sector_rank=11 price=23.79 support=22.1 resistance=25.49 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=43.32 liquidity=217131.34 spike=0.79
- RAYA.CA: score=25.4 buy_ready=True sector_rank=3 price=7.57 support=6.4 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=48.37 liquidity=17105544.0 spike=0.14
- RMDA.CA: score=24.4 buy_ready=True sector_rank=8 price=5.06 support=4.47 resistance=5.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=49.99 liquidity=16057943.0 spike=0.28
- ROTO.CA: score=25.2 buy_ready=True sector_rank=11 price=34.37 support=32.66 resistance=36.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=36.4 liquidity=18135122.0 spike=1.4
- RREI.CA: score=26.4 buy_ready=True sector_rank=11 price=3.6 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=49.44 liquidity=10975120.0 spike=0.47
- RTVC.CA: score=9.6 buy_ready=False sector_rank=11 price=3.88 support=3.75 resistance=4.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=30.43 liquidity=2196365.0 spike=0.35
- RUBX.CA: score=10.64 buy_ready=False sector_rank=11 price=10.25 support=9.8 resistance=11.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=30.2 liquidity=3243606.25 spike=0.19
- SAUD.CA: score=17.64 buy_ready=False sector_rank=17 price=22.44 support=21.8 resistance=25.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=42.77 liquidity=5986137.5 spike=0.38
- SCEM.CA: score=22.4 buy_ready=False sector_rank=9 price=64.46 support=61.92 resistance=72.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=39.81 liquidity=12122519.0 spike=0.27
- SCFM.CA: score=12.26 buy_ready=False sector_rank=11 price=265.0 support=260.0 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=16.54 liquidity=4859435.0 spike=0.16
- SCTS.CA: score=8.36 buy_ready=False sector_rank=14 price=622.47 support=590.01 resistance=709.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=13.63 liquidity=1447664.13 spike=0.12
- SDTI.CA: score=20.46 buy_ready=True sector_rank=11 price=46.13 support=43.4 resistance=46.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=54.99 liquidity=4059137.0 spike=0.2
- SEIG.CA: score=17.02 buy_ready=False sector_rank=11 price=188.84 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=57.08 liquidity=624893.0 spike=0.09
- SIPC.CA: score=27.14 buy_ready=True sector_rank=11 price=3.7 support=3.4 resistance=3.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=51.02 liquidity=20424224.0 spike=1.37
- SKPC.CA: score=17.17 buy_ready=False sector_rank=18 price=16.95 support=16.8 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=37.93 liquidity=10662586.0 spike=0.13
- SMFR.CA: score=15.94 buy_ready=True sector_rank=11 price=210.58 support=203.51 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=42.24 liquidity=1542444.5 spike=0.13
- SNFC.CA: score=20.4 buy_ready=False sector_rank=11 price=12.0 support=11.66 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=65.58 liquidity=14574267.0 spike=0.53
- SPIN.CA: score=10.79 buy_ready=False sector_rank=7 price=14.32 support=13.69 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=43.05 liquidity=1390103.0 spike=0.28
- SPMD.CA: score=22.5 buy_ready=True sector_rank=11 price=0.42 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=64.08 liquidity=6101183.0 spike=0.26
- SUGR.CA: score=22.85 buy_ready=True sector_rank=10 price=50.12 support=47.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=56.5 liquidity=6453237.0 spike=0.39
- SVCE.CA: score=24.4 buy_ready=True sector_rank=11 price=9.18 support=7.98 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=55.5 liquidity=12620792.0 spike=0.08
- SWDY.CA: score=24.4 buy_ready=True sector_rank=6 price=87.88 support=85.25 resistance=91.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=53.16 liquidity=11228835.0 spike=0.31
- TALM.CA: score=13.23 buy_ready=False sector_rank=14 price=15.95 support=15.12 resistance=17.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=40.94 liquidity=1312755.75 spike=0.1
- TMGH.CA: score=24.4 buy_ready=False sector_rank=2 price=94.23 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=55.39 liquidity=138846752.0 spike=0.25
- TRTO.CA: score=10.4 buy_ready=False sector_rank=11 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=4.4 buy_ready=False sector_rank=11 price=475.55 support=455.6 resistance=517.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=32.78 liquidity=997079.81 spike=0.54
- UEGC.CA: score=31.4 buy_ready=True sector_rank=11 price=1.5 support=1.3 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=65.22 liquidity=81401896.0 spike=4.07
- UNIP.CA: score=30.4 buy_ready=False sector_rank=11 price=0.32 support=0.28 resistance=0.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=72.0 liquidity=56115952.0 spike=4.56
- UNIT.CA: score=25.16 buy_ready=True sector_rank=2 price=14.28 support=10.83 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=56.81 liquidity=6760161.0 spike=0.69
- WCDF.CA: score=9.25 buy_ready=False sector_rank=11 price=540.42 support=535.0 resistance=561.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=12.24 liquidity=1051876.13 spike=1.4
- WKOL.CA: score=8.09 buy_ready=False sector_rank=11 price=294.99 support=290.0 resistance=349.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=28.64 liquidity=687343.19 spike=0.06
- ZEOT.CA: score=21.11 buy_ready=True sector_rank=11 price=9.31 support=8.43 resistance=9.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=47.24 liquidity=4706329.5 spike=0.52
- ZMID.CA: score=26.4 buy_ready=True sector_rank=2 price=6.05 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=40.52 liquidity=96317312.0 spike=0.49

## Backtesting Lite
- EMFD.CA: 180d return=49.39%, max drawdown=-15.54%, MA20>MA50 days last20=20, as_of=2026-06-03T21:00:00+00:00
- UEGC.CA: 180d return=41.75%, max drawdown=-21.74%, MA20>MA50 days last20=19, as_of=2026-06-03T21:00:00+00:00
- NCCW.CA: 180d return=-19.69%, max drawdown=-44.78%, MA20>MA50 days last20=20, as_of=2026-06-03T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- EMFD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=522 sources=3 expected=Emaar Misr for Development summary=Emaar Misr posts higher revenues at EGP 19.8bn in 2025; Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25; Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea
  - Emaar Misr posts higher revenues at EGP 19.8bn in 2025: https://english.mubasher.info/news/4561643/Emaar-Misr-posts-higher-revenues-at-EGP-19-8bn-in-2025/
  - Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25: https://english.mubasher.info/news/4525192/Emaar-Misr-s-consolidated-net-profits-drop-to-EGP-4-2bn-in-9M-25/
  - Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea: https://english.mubasher.info/news/4495287/Emaar-Misr-Golden-Coast-to-establish-EGP-900bn-project-in-Red-Sea/
- UEGC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=522 sources=3 expected=El-Saeed Company for Contracting and Real Estate Investment "SCCD" (S.A.E.) summary=ElSaeed Contracting stock eyes break above EGP 1.44 amid uptrend; ElSaeed Contracting posts higher consolidated profits at EGP 93m in 2025; ElSaeed Contracting stock signals upside move towards EGP 1.50
  - ElSaeed Contracting stock eyes break above EGP 1.44 amid uptrend: https://english.mubasher.info/news/4595500/ElSaeed-Contracting-stock-eyes-break-above-EGP-1-44-amid-uptrend/
  - ElSaeed Contracting posts higher consolidated profits at EGP 93m in 2025: https://english.mubasher.info/news/4589666/ElSaeed-Contracting-posts-higher-consolidated-profits-at-EGP-93m-in-2025/
  - ElSaeed Contracting stock signals upside move towards EGP 1.50: https://english.mubasher.info/news/4564890/ElSaeed-Contracting-stock-signals-upside-move-towards-EGP-1-50/
- NCCW.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Nasr Company for Civil Works summary=Nasr for Civil Works unveils EGP 150m capital increase; Arabia Investments, Nasr Company for Civil Works unveil capital hike; Nasr Company for Civil Works’ consortium signs EUR 46m agreement with Uganda
  - Nasr for Civil Works unveils EGP 150m capital increase: https://english.mubasher.info/news/4550493/Nasr-for-Civil-Works-unveils-EGP-150m-capital-increase/
  - Arabia Investments, Nasr Company for Civil Works unveil capital hike: https://english.mubasher.info/news/4284206/Arabia-Investments-Nasr-Company-for-Civil-Works-unveil-capital-hike/
  - Nasr Company for Civil Works’ consortium signs EUR 46m agreement with Uganda: https://english.mubasher.info/news/4249759/Nasr-Company-for-Civil-Works-consortium-signs-EUR-46m-agreement-with-Uganda/
- COSG.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Oil & Soap Company summary=Cairo Oils stock stabilizes above EGP 1.50 resistance level; EGX approves capital increase, reduction of several listed firms; Cairo oils incurs EGP 25m losses in H1-19
  - Cairo Oils stock stabilizes above EGP 1.50 resistance level: https://english.mubasher.info/news/4546423/Cairo-Oils-stock-stabilizes-above-EGP-1-50-resistance-level/
  - EGX approves capital increase, reduction of several listed firms: https://english.mubasher.info/news/3828111/EGX-approves-capital-increase-reduction-of-several-listed-firms/
  - Cairo oils incurs EGP 25m losses in H1-19: https://english.mubasher.info/news/3521392/Cairo-oils-incurs-EGP-25m-losses-in-H1-19/
- GGCC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Giza General - Contracting and Real Estate Investment S.A.E summary=EGX approves listing EGP 144m capital increase for Giza Contracting; Giza Contracting tests key EGP 0.51 level; Giza Contracting’s consolidated net profits leap to EGP 140m in 9M-25
  - EGX approves listing EGP 144m capital increase for Giza Contracting: https://english.mubasher.info/news/4588793/EGX-approves-listing-EGP-144m-capital-increase-for-Giza-Contracting/
  - Giza Contracting tests key EGP 0.51 level: https://english.mubasher.info/news/4563778/Giza-Contracting-tests-key-EGP-0-51-level/
  - Giza Contracting’s consolidated net profits leap to EGP 140m in 9M-25: https://english.mubasher.info/news/4530408/Giza-Contracting-s-consolidated-net-profits-leap-to-EGP-140m-in-9M-25/
- UNIP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Universal For Paper and Packaging Materials summary=Evidence rejected for UNIP.CA: source text did not clearly match UNIP.CA / Universal For Paper and Packaging Materials.
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=522 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- MPRC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Media Production City summary=Evidence rejected for MPRC.CA: source text did not clearly match MPRC.CA / Egyptian Media Production City.

## Warnings
- Evidence for EMFD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence for UEGC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for NCCW.CA matches the company but no source/report date was detected.
- Evidence for COSG.CA matches the company but no source/report date was detected.
- Evidence for GGCC.CA matches the company but no source/report date was detected.
- Evidence rejected for UNIP.CA: source text did not clearly match UNIP.CA / Universal For Paper and Packaging Materials.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for MPRC.CA: source text did not clearly match MPRC.CA / Egyptian Media Production City.
