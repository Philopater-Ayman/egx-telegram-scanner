# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-08-31T19:14:43.324162+00:00
Generated Cairo: 2026-08-31 22:14
Run timing: target 15:30 Cairo | generated Cairo 2026-08-31 22:14 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-08-31 22:10

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 38
- Data quality issues: 1
- Tradeable price/liquidity tickers: 154/189
- Top sector: Textiles

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, August 31
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 47.06% / above MA50 70.59%
- EGX70 regime: BEARISH / above MA20 38.89% / above MA50 72.22%
- Sector breadth: 42.86%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- CCAP.CA: liquidity=1247469184.0 spike=2.19 score=12.78
- COMI.CA: liquidity=1202718848.0 spike=2.52 score=25.44
- TMGH.CA: liquidity=610589888.0 spike=2.56 score=21.92
- NIPH.CA: liquidity=580211648.0 spike=1.7 score=10.8
- MPCI.CA: liquidity=540980224.0 spike=3.21 score=13.08

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner prioritized SPIN.CA, ORWE.CA and SKPC.CA as watch/buy setups under a SELECTIVE_SWING_TRADES_ONLY regime, noting price above MA20/MA50, moderate RSI and sector‑specific cues, while EGX30 shows mixed breadth and EGX70 remains bearish, keeping risk mode selective.
- Liquidity is cooling for SPIN.CA and ORWE.CA with momentum extended; prices sit far above support and near resistance, suggesting a watch for a potential pullback or breakout in the next 1‑3 days.
- ORWE.CA carries the highest outlook score (90) within the leading Textiles sector, which shows full MA20/MA50 coverage, giving a modest upside bias if the stock holds above its moving averages.

## Top Liquidity Spikes
- AJWA.CA: spike=10.75 liquidity=522743808.0 outlook=WEAK_OR_RISKY score=24.15 buy_ready=False
- EBSC.CA: spike=6.4 liquidity=59070732.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- HRHO.CA: spike=5.41 liquidity=538924864.0 outlook=WEAK_OR_RISKY score=19.75 buy_ready=False
- EAST.CA: spike=5.23 liquidity=351972320.0 outlook=WEAK_OR_RISKY score=23.25 buy_ready=False
- DAPH.CA: spike=5.0 liquidity=225695056.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Textiles: score=13.14 5d=5.72% 20d=21.24% aboveMA50=100.0%
- #2 Building Materials: score=12.61 5d=3.25% 20d=25.98% aboveMA50=83.33%
- #3 Investment Holding: score=12.19 5d=6.95% 20d=10.62% aboveMA50=66.67%
- #4 Industrial Goods & Cables: score=8.67 5d=3.66% 20d=15.73% aboveMA50=50.0%
- #5 Banking & Financials: score=7.75 5d=0.9% 20d=3.53% aboveMA50=90.0%
- #6 Tourism & Leisure: score=7.7 5d=1.65% 20d=13.29% aboveMA50=0.0%
- #7 Transportation & Logistics: score=7.42 5d=-3.2% 20d=14.79% aboveMA50=100.0%
- #8 Healthcare: score=6.9 5d=-0.11% 20d=10.56% aboveMA50=83.33%

## Today's Prioritized Action Tickets
- Priority #1: BUY SPIN.CA
  - Entry: 19.48 | Take profit: 21.77 | Stop loss: 18.7
  - Confidence: LOW | score=27.4 | outlook=BULLISH_WATCH 78
  - Reason: WATCH/BUY SETUP: SPIN.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 69.28, support 15.32, resistance 21.88, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY ORWE.CA
  - Entry: 26.06 | Take profit: 27.98 | Stop loss: 25.1
  - Confidence: LOW | score=27.4 | outlook=BULLISH_WATCH 90
  - Reason: WATCH/BUY SETUP: ORWE.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 53.95, support 22.72, resistance 27.41, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY SKPC.CA
  - Entry: 17.74 | Take profit: 19.16 | Stop loss: 17.03
  - Confidence: LOW | score=27.23 | outlook=CONSTRUCTIVE 69.73
  - Reason: WATCH/BUY SETUP: SKPC.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 61.93, support 15.61, resistance 18.15, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- BINV.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- ADIB.CA: BULLISH_WATCH score=94.75 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- ORWE.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- CIEB.CA: BULLISH_WATCH score=88.75 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance
- MCQE.CA: BULLISH_WATCH score=83 liquidity=TRADEABLE sector=LEADING risk=momentum is extended; far above support
- LCSW.CA: BULLISH_WATCH score=83 liquidity=TRADEABLE sector=LEADING risk=below MA20
- CLHO.CA: BULLISH_WATCH score=82.9 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- EXPA.CA: BULLISH_WATCH score=82.75 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- FAIT.CA: BULLISH_WATCH score=80.75 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=overheated RSI
- NINH.CA: BULLISH_WATCH score=80.15 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- BINV.CA: rank=31.12 outlook=BULLISH_WATCH outlook_score=100 sector_rank=3 price=52.0 support=46.25 resistance=53.65 liquidity=26822182.0
- CIEB.CA: rank=27.44 outlook=BULLISH_WATCH outlook_score=88.75 sector_rank=5 price=25.45 support=23.75 resistance=25.6 liquidity=19957852.0
- SPIN.CA: rank=27.4 outlook=BULLISH_WATCH outlook_score=78 sector_rank=1 price=19.48 support=15.32 resistance=21.88 liquidity=15272424.0
- ORWE.CA: rank=27.4 outlook=BULLISH_WATCH outlook_score=90 sector_rank=1 price=26.06 support=22.72 resistance=27.41 liquidity=34124724.0
- SKPC.CA: rank=27.23 outlook=CONSTRUCTIVE outlook_score=69.73 sector_rank=11 price=17.74 support=15.61 resistance=18.15 liquidity=105120336.0
- PRDC.CA: rank=26.86 outlook=BULLISH_WATCH outlook_score=74.5 sector_rank=14 price=9.78 support=8.7 resistance=9.88 liquidity=149024336.0
- EASB.CA: rank=26.84 outlook=BULLISH_WATCH outlook_score=78.15 sector_rank=15 price=7.68 support=6.71 resistance=8.2 liquidity=12111264.0
- MCQE.CA: rank=26.72 outlook=BULLISH_WATCH outlook_score=83 sector_rank=2 price=235.66 support=180.5 resistance=292.32 liquidity=65524096.0
- ETEL.CA: rank=26.12 outlook=BULLISH_WATCH outlook_score=79.66 sector_rank=12 price=114.44 support=102.75 resistance=120.0 liquidity=254786976.0
- MAAL.CA: rank=26.0 outlook=BULLISH_WATCH outlook_score=72.15 sector_rank=15 price=9.01 support=8.32 resistance=9.76 liquidity=14437642.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=21.66 buy_ready=False sector_rank=15 price=305.09 support=240.49 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=54.29 liquidity=10986714.0 spike=0.18
- ABUK.CA: score=27.21 buy_ready=False sector_rank=11 price=79.98 support=72.0 resistance=80.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.59 liquidity=149807824.0 spike=1.46
- ACAMD.CA: score=13.66 buy_ready=False sector_rank=15 price=2.0 support=1.95 resistance=2.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=32.14 liquidity=33911248.0 spike=0.59
- ACGC.CA: score=26.4 buy_ready=False sector_rank=1 price=14.14 support=10.14 resistance=14.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=79.23 liquidity=11348686.0 spike=0.26
- ADCI.CA: score=24.5 buy_ready=True sector_rank=15 price=299.74 support=256.0 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=52.95 liquidity=28248640.0 spike=1.42
- ADIB.CA: score=25.98 buy_ready=True sector_rank=5 price=53.68 support=51.02 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.29 liquidity=120038944.0 spike=1.79
- ADPC.CA: score=18.66 buy_ready=False sector_rank=15 price=3.88 support=3.84 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.32 liquidity=15725827.0 spike=0.36
- AFDI.CA: score=13.66 buy_ready=False sector_rank=15 price=56.35 support=53.65 resistance=61.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=116631056.0 spike=4.01
- AFMC.CA: score=8.66 buy_ready=False sector_rank=15 price=187.11 support=175.2 resistance=217.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=65758052.0 spike=0.4
- AJWA.CA: score=23.66 buy_ready=False sector_rank=15 price=180.13 support=180.01 resistance=204.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.83 liquidity=522743808.0 spike=10.75
- ALCN.CA: score=22.4 buy_ready=False sector_rank=7 price=30.77 support=29.0 resistance=32.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.92 liquidity=25058728.0 spike=0.98
- ALUM.CA: score=23.66 buy_ready=False sector_rank=15 price=28.18 support=22.72 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=71.55 liquidity=14882982.0 spike=0.55
- AMER.CA: score=9.26 buy_ready=False sector_rank=14 price=5.73 support=5.5 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=117383296.0 spike=1.23
- AMES.CA: score=8.66 buy_ready=False sector_rank=15 price=130.73 support=128.0 resistance=140.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32591988.0 spike=0.46
- AMIA.CA: score=21.0 buy_ready=False sector_rank=15 price=19.34 support=10.6 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=83.8 liquidity=62366608.0 spike=1.17
- AMOC.CA: score=9.86 buy_ready=False sector_rank=17 price=12.15 support=11.49 resistance=12.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=241815248.0 spike=1.64
- APSW.CA: score=11.79 buy_ready=False sector_rank=15 price=8.68 support=8.41 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.88 liquidity=1131792.63 spike=0.71
- ARAB.CA: score=26.44 buy_ready=False sector_rank=14 price=0.26 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.21 liquidity=112197472.0 spike=1.32
- ARCC.CA: score=23.4 buy_ready=False sector_rank=2 price=76.69 support=55.77 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.19 liquidity=101095096.0 spike=1.0
- AREH.CA: score=13.66 buy_ready=False sector_rank=15 price=1.41 support=1.38 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.0 liquidity=10257188.0 spike=0.35
- ARVA.CA: score=8.66 buy_ready=False sector_rank=15 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=16.66 buy_ready=False sector_rank=15 price=63.74 support=61.0 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=21.86 liquidity=32823982.0 spike=0.63
- ASPI.CA: score=12.3 buy_ready=False sector_rank=15 price=0.45 support=0.45 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=110024344.0 spike=2.82
- ATLC.CA: score=23.16 buy_ready=True sector_rank=19 price=5.67 support=5.12 resistance=5.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.45 liquidity=20436392.0 spike=1.03
- ATQA.CA: score=23.43 buy_ready=False sector_rank=11 price=11.9 support=9.66 resistance=11.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=81.17 liquidity=92308808.0 spike=1.07
- AXPH.CA: score=24.08 buy_ready=False sector_rank=15 price=1702.93 support=1121.56 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=88.41 liquidity=18551800.0 spike=1.71
- BINV.CA: score=31.12 buy_ready=True sector_rank=3 price=52.0 support=46.25 resistance=53.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=69.08 liquidity=26822182.0 spike=2.86
- BIOC.CA: score=10.98 buy_ready=False sector_rank=15 price=340.72 support=330.42 resistance=453.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=527309088.0 spike=2.16
- BTFH.CA: score=12.1 buy_ready=False sector_rank=19 price=2.97 support=2.94 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.32 liquidity=78256032.0 spike=0.38
- CAED.CA: score=7.94 buy_ready=False sector_rank=15 price=140.97 support=140.12 resistance=148.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9278406.0 spike=0.18
- CANA.CA: score=22.4 buy_ready=False sector_rank=5 price=41.61 support=36.62 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.33 liquidity=12366760.0 spike=0.7
- CCAP.CA: score=12.78 buy_ready=False sector_rank=3 price=6.09 support=5.79 resistance=6.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1247469184.0 spike=2.19
- CCRS.CA: score=8.66 buy_ready=False sector_rank=15 price=2.6 support=2.59 resistance=2.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35331404.0 spike=0.77
- CEFM.CA: score=23.66 buy_ready=True sector_rank=15 price=143.86 support=131.03 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=61.21 liquidity=21083066.0 spike=0.72
- CERA.CA: score=18.66 buy_ready=False sector_rank=15 price=1.24 support=1.23 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=10375740.0 spike=0.75
- CFGH.CA: score=2.81 buy_ready=False sector_rank=15 price=0.12 support=0.12 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51034.52 spike=3.05
- CICH.CA: score=8.36 buy_ready=False sector_rank=19 price=12.24 support=11.92 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=33.86 liquidity=2258986.5 spike=0.32
- CIEB.CA: score=27.44 buy_ready=True sector_rank=5 price=25.45 support=23.75 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=57.78 liquidity=19957852.0 spike=1.52
- CIRA.CA: score=8.65 buy_ready=False sector_rank=16 price=32.57 support=32.1 resistance=34.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=38392348.0 spike=0.76
- CLHO.CA: score=24.78 buy_ready=True sector_rank=8 price=17.86 support=16.65 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.05 liquidity=72900568.0 spike=1.19
- CNFN.CA: score=13.1 buy_ready=False sector_rank=19 price=4.85 support=4.72 resistance=5.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=30.0 liquidity=15835750.0 spike=0.81
- COMI.CA: score=25.44 buy_ready=False sector_rank=5 price=137.45 support=135.35 resistance=142.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.71 liquidity=1202718848.0 spike=2.52
- COPR.CA: score=8.66 buy_ready=False sector_rank=15 price=0.51 support=0.5 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=56494820.0 spike=0.64
- COSG.CA: score=23.66 buy_ready=True sector_rank=15 price=1.84 support=1.62 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=63.41 liquidity=35266260.0 spike=0.7
- CPCI.CA: score=18.14 buy_ready=False sector_rank=15 price=548.1 support=462.0 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=71.63 liquidity=6477872.5 spike=0.76
- CSAG.CA: score=24.4 buy_ready=True sector_rank=7 price=41.36 support=31.64 resistance=43.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=61.29 liquidity=16023695.0 spike=0.68
- DAPH.CA: score=13.66 buy_ready=False sector_rank=15 price=135.0 support=134.05 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=225695056.0 spike=5.0
- DEIN.CA: score=-1.34 buy_ready=False sector_rank=15 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=20.53 buy_ready=False sector_rank=9 price=28.41 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=44.38 liquidity=8134152.5 spike=0.51
- DSCW.CA: score=13.66 buy_ready=False sector_rank=15 price=1.92 support=1.84 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.19 liquidity=44242060.0 spike=0.5
- DTPP.CA: score=21.78 buy_ready=False sector_rank=15 price=308.11 support=235.59 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=72.49 liquidity=46348284.0 spike=1.06
- EALR.CA: score=21.66 buy_ready=False sector_rank=15 price=395.05 support=364.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.67 liquidity=10635300.0 spike=0.22
- EASB.CA: score=26.84 buy_ready=True sector_rank=15 price=7.68 support=6.71 resistance=8.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.09 liquidity=12111264.0 spike=1.59
- EAST.CA: score=18.4 buy_ready=False sector_rank=9 price=36.0 support=35.0 resistance=37.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.87 liquidity=351972320.0 spike=5.23
- EBSC.CA: score=13.66 buy_ready=False sector_rank=15 price=2.17 support=1.97 resistance=2.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=59070732.0 spike=6.4
- ECAP.CA: score=19.94 buy_ready=False sector_rank=15 price=32.28 support=32.12 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.1 liquidity=23832734.0 spike=1.64
- EDFM.CA: score=14.5 buy_ready=False sector_rank=15 price=405.15 support=386.16 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.24 liquidity=842269.5 spike=0.29
- EEII.CA: score=23.66 buy_ready=True sector_rank=15 price=3.02 support=2.54 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=59.12 liquidity=21520480.0 spike=0.83
- EFIC.CA: score=21.29 buy_ready=False sector_rank=11 price=199.08 support=188.01 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.2 liquidity=20141878.0 spike=0.4
- EFID.CA: score=22.46 buy_ready=False sector_rank=9 price=30.61 support=27.0 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.68 liquidity=91508256.0 spike=1.03
- EFIH.CA: score=22.09 buy_ready=False sector_rank=13 price=22.9 support=22.15 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.71 liquidity=87049816.0 spike=0.79
- EGAL.CA: score=24.69 buy_ready=False sector_rank=11 price=360.01 support=292.0 resistance=373.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=84.6 liquidity=226757904.0 spike=1.7
- EGAS.CA: score=21.58 buy_ready=False sector_rank=17 price=58.26 support=52.5 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.95 liquidity=18712800.0 spike=0.8
- EGBE.CA: score=12.87 buy_ready=False sector_rank=5 price=0.53 support=0.47 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.99 liquidity=225720.69 spike=1.12
- EGCH.CA: score=22.29 buy_ready=False sector_rank=11 price=13.81 support=12.69 resistance=14.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.3 liquidity=50973056.0 spike=0.42
- EGSA.CA: score=6.27 buy_ready=False sector_rank=12 price=8.69 support=8.65 resistance=8.93 source=Yahoo Finance as_of=2026-08-29T21:00:00+00:00 freshness=FRESH RSI=28.0 liquidity=4006.09 spike=0.54
- EGTS.CA: score=19.26 buy_ready=False sector_rank=14 price=17.16 support=16.17 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.05 liquidity=42772320.0 spike=1.23
- EHDR.CA: score=21.66 buy_ready=False sector_rank=15 price=2.83 support=2.71 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=51.16 liquidity=19377698.0 spike=0.51
- EKHO.CA: score=9.58 buy_ready=False sector_rank=17 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=13.4 buy_ready=False sector_rank=4 price=2.08 support=2.04 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.43 liquidity=47672384.0 spike=0.86
- ELKA.CA: score=24.02 buy_ready=False sector_rank=15 price=1.83 support=1.69 resistance=1.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.27 liquidity=78620984.0 spike=1.18
- ELNA.CA: score=11.11 buy_ready=False sector_rank=15 price=37.0 support=36.1 resistance=38.5 source=Yahoo Finance as_of=2026-08-29T21:00:00+00:00 freshness=FRESH RSI=42.81 liquidity=765308.0 spike=2.34
- ELSH.CA: score=15.0 buy_ready=False sector_rank=15 price=13.52 support=12.97 resistance=14.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=29.44 liquidity=90565520.0 spike=1.67
- ELWA.CA: score=19.39 buy_ready=False sector_rank=15 price=1.87 support=1.62 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=69.23 liquidity=4792313.0 spike=1.97
- EMFD.CA: score=13.8 buy_ready=False sector_rank=14 price=13.0 support=12.76 resistance=13.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=327131552.0 spike=4.01
- ENGC.CA: score=21.66 buy_ready=False sector_rank=15 price=43.4 support=40.11 resistance=54.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.68 liquidity=13711687.0 spike=0.5
- EOSB.CA: score=16.58 buy_ready=False sector_rank=15 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-08-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=63526.91 spike=1.43
- EPCO.CA: score=18.69 buy_ready=False sector_rank=15 price=11.17 support=10.32 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=7028924.5 spike=0.38
- EPPK.CA: score=6.65 buy_ready=False sector_rank=15 price=12.01 support=12.01 resistance=12.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2989728.25 spike=3.97
- ETEL.CA: score=26.12 buy_ready=True sector_rank=12 price=114.44 support=102.75 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.91 liquidity=254786976.0 spike=1.93
- ETRS.CA: score=23.66 buy_ready=True sector_rank=15 price=11.06 support=10.36 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=59.9 liquidity=17509422.0 spike=0.58
- EXPA.CA: score=25.14 buy_ready=True sector_rank=5 price=20.96 support=19.8 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.61 liquidity=51790268.0 spike=1.37
- FAIT.CA: score=29.58 buy_ready=False sector_rank=5 price=43.0 support=36.2 resistance=45.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=71.65 liquidity=16810952.0 spike=2.59
- FAITA.CA: score=17.58 buy_ready=False sector_rank=5 price=0.99 support=0.97 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=67.07 liquidity=121500.09 spike=2.53
- FERC.CA: score=18.4 buy_ready=False sector_rank=11 price=77.44 support=75.01 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=49.2 liquidity=7103282.5 spike=0.4
- FWRY.CA: score=24.09 buy_ready=False sector_rank=13 price=18.9 support=18.66 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=42.69 liquidity=495544128.0 spike=3.95
- GBCO.CA: score=11.26 buy_ready=False sector_rank=21 price=28.9 support=27.51 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.46 liquidity=26405124.0 spike=0.53
- GDWA.CA: score=14.66 buy_ready=False sector_rank=15 price=0.81 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.07 liquidity=31381106.0 spike=0.5
- GGCC.CA: score=9.92 buy_ready=False sector_rank=15 price=0.87 support=0.86 resistance=0.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=74006392.0 spike=1.63
- GIHD.CA: score=11.22 buy_ready=False sector_rank=15 price=69.09 support=64.31 resistance=74.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=59560976.0 spike=2.28
- GMCI.CA: score=6.16 buy_ready=False sector_rank=15 price=1.87 support=1.83 resistance=2.06 source=Yahoo Finance as_of=2026-08-29T21:00:00+00:00 freshness=FRESH RSI=13.33 liquidity=897616.83 spike=1.8
- GRCA.CA: score=22.88 buy_ready=False sector_rank=15 price=78.97 support=54.7 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.54 liquidity=64135508.0 spike=1.11
- GSSC.CA: score=20.89 buy_ready=False sector_rank=15 price=282.02 support=274.0 resistance=301.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.55 liquidity=9229412.0 spike=0.48
- GTWL.CA: score=22.96 buy_ready=False sector_rank=15 price=234.0 support=85.0 resistance=247.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=85.71 liquidity=310305472.0 spike=1.15
- HDBK.CA: score=13.4 buy_ready=False sector_rank=5 price=105.18 support=96.5 resistance=106.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=125821528.0 spike=3.0
- HELI.CA: score=21.8 buy_ready=False sector_rank=14 price=7.76 support=7.34 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.0 liquidity=149244064.0 spike=0.91
- HRHO.CA: score=17.1 buy_ready=False sector_rank=19 price=25.67 support=25.49 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.25 liquidity=538924864.0 spike=5.41
- ICID.CA: score=20.66 buy_ready=False sector_rank=15 price=16.67 support=7.85 resistance=18.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=93.01 liquidity=10676814.0 spike=0.39
- IDRE.CA: score=23.78 buy_ready=True sector_rank=15 price=53.5 support=47.01 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.18 liquidity=15646025.0 spike=1.06
- IFAP.CA: score=22.34 buy_ready=False sector_rank=10 price=20.51 support=19.0 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.21 liquidity=25575474.0 spike=0.87
- INFI.CA: score=23.66 buy_ready=True sector_rank=15 price=152.44 support=108.1 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.96 liquidity=29524316.0 spike=0.42
- IRON.CA: score=14.19 buy_ready=False sector_rank=11 price=30.02 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=33.23 liquidity=17212938.0 spike=1.45
- ISMA.CA: score=8.66 buy_ready=False sector_rank=15 price=34.71 support=34.51 resistance=38.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19862974.0 spike=0.73
- ISMQ.CA: score=19.29 buy_ready=False sector_rank=11 price=9.13 support=9.0 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.94 liquidity=24967174.0 spike=0.48
- ISPH.CA: score=17.4 buy_ready=False sector_rank=8 price=13.06 support=11.3 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=33.0 liquidity=69719064.0 spike=0.36
- JUFO.CA: score=22.4 buy_ready=False sector_rank=9 price=26.54 support=22.78 resistance=28.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=67.2 liquidity=41572732.0 spike=0.77
- KABO.CA: score=26.78 buy_ready=False sector_rank=1 price=9.44 support=7.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=72.29 liquidity=67677016.0 spike=1.69
- KWIN.CA: score=12.96 buy_ready=False sector_rank=15 price=111.43 support=110.0 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=203852736.0 spike=3.15
- KZPC.CA: score=23.66 buy_ready=False sector_rank=15 price=13.0 support=8.53 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=73.7 liquidity=34347944.0 spike=0.67
- LCSW.CA: score=24.84 buy_ready=False sector_rank=2 price=34.11 support=32.12 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=55.08 liquidity=36191700.0 spike=1.22
- LUTS.CA: score=8.88 buy_ready=False sector_rank=15 price=1.12 support=1.1 resistance=1.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=256544112.0 spike=1.11
- MAAL.CA: score=26.0 buy_ready=True sector_rank=15 price=9.01 support=8.32 resistance=9.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.77 liquidity=14437642.0 spike=1.17
- MASR.CA: score=18.96 buy_ready=False sector_rank=15 price=7.7 support=7.45 resistance=8.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=73372088.0 spike=1.15
- MBSC.CA: score=25.4 buy_ready=False sector_rank=2 price=408.7 support=242.01 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=81.64 liquidity=36313820.0 spike=0.43
- MCQE.CA: score=26.72 buy_ready=True sector_rank=2 price=235.66 support=180.5 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=64.42 liquidity=65524096.0 spike=1.16
- MCRO.CA: score=21.66 buy_ready=False sector_rank=15 price=1.5 support=1.44 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.43 liquidity=61801056.0 spike=0.48
- MENA.CA: score=12.87 buy_ready=False sector_rank=14 price=6.91 support=6.59 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.01 liquidity=4074243.0 spike=0.7
- MEPA.CA: score=8.84 buy_ready=False sector_rank=15 price=1.9 support=1.83 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35973468.0 spike=1.09
- MFPC.CA: score=10.41 buy_ready=False sector_rank=11 price=41.38 support=40.55 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=122302472.0 spike=1.56
- MFSC.CA: score=16.05 buy_ready=False sector_rank=15 price=49.85 support=46.02 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.16 liquidity=4390416.5 spike=0.39
- MHOT.CA: score=22.4 buy_ready=False sector_rank=6 price=18.51 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=60.61 liquidity=17368062.0 spike=0.92
- MICH.CA: score=23.66 buy_ready=True sector_rank=15 price=50.48 support=39.01 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.92 liquidity=14045744.0 spike=0.34
- MILS.CA: score=23.66 buy_ready=True sector_rank=15 price=206.28 support=175.0 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.75 liquidity=38209740.0 spike=0.46
- MIPH.CA: score=21.64 buy_ready=True sector_rank=8 price=800.08 support=738.1 resistance=828.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.32 liquidity=6400948.5 spike=1.42
- MOED.CA: score=10.46 buy_ready=False sector_rank=15 price=0.84 support=0.81 resistance=0.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=172524656.0 spike=1.9
- MOIL.CA: score=15.95 buy_ready=False sector_rank=17 price=0.69 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=55.22 liquidity=378645.88 spike=0.9
- MOIN.CA: score=15.69 buy_ready=False sector_rank=15 price=33.75 support=23.44 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.55 liquidity=4029543.5 spike=0.12
- MOSC.CA: score=23.82 buy_ready=False sector_rank=15 price=313.26 support=290.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=63.42 liquidity=31401536.0 spike=2.08
- MPCI.CA: score=13.08 buy_ready=False sector_rank=15 price=442.07 support=409.0 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=540980224.0 spike=3.21
- MPCO.CA: score=22.34 buy_ready=False sector_rank=10 price=2.11 support=1.91 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.8 liquidity=96402608.0 spike=0.75
- MPRC.CA: score=22.66 buy_ready=False sector_rank=15 price=43.51 support=39.5 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.3 liquidity=44682220.0 spike=1.5
- MTIE.CA: score=16.26 buy_ready=False sector_rank=21 price=8.49 support=8.01 resistance=11.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.88 liquidity=36139108.0 spike=0.54
- NAHO.CA: score=10.7 buy_ready=False sector_rank=15 price=0.14 support=0.1 resistance=0.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=83.93 liquidity=43915.09 spike=0.49
- NCCW.CA: score=13.66 buy_ready=False sector_rank=15 price=5.87 support=5.59 resistance=7.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=31.17 liquidity=11618699.0 spike=0.39
- NEDA.CA: score=11.41 buy_ready=False sector_rank=15 price=2.74 support=2.7 resistance=2.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=752033.88 spike=0.88
- NHPS.CA: score=23.66 buy_ready=True sector_rank=15 price=88.99 support=82.25 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.08 liquidity=20412724.0 spike=0.6
- NINH.CA: score=25.9 buy_ready=True sector_rank=15 price=23.52 support=21.53 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.33 liquidity=45991360.0 spike=1.12
- NIPH.CA: score=10.8 buy_ready=False sector_rank=8 price=347.43 support=330.0 resistance=401.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=580211648.0 spike=1.7
- OBRI.CA: score=22.2 buy_ready=False sector_rank=15 price=33.3 support=31.61 resistance=34.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.6 liquidity=36804668.0 spike=1.27
- OCDI.CA: score=21.8 buy_ready=False sector_rank=14 price=31.2 support=28.21 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.32 liquidity=76211280.0 spike=0.55
- OCPH.CA: score=19.96 buy_ready=False sector_rank=15 price=252.61 support=225.0 resistance=341.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.6 liquidity=26155608.0 spike=1.15
- ODIN.CA: score=8.66 buy_ready=False sector_rank=15 price=3.03 support=2.99 resistance=3.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37071416.0 spike=0.8
- OFH.CA: score=23.66 buy_ready=False sector_rank=15 price=1.05 support=0.69 resistance=1.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=92.88 liquidity=143432224.0 spike=1.5
- OIH.CA: score=24.86 buy_ready=False sector_rank=3 price=2.01 support=1.43 resistance=2.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=84.31 liquidity=173672112.0 spike=1.23
- OLFI.CA: score=19.4 buy_ready=False sector_rank=9 price=22.67 support=22.76 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.06 liquidity=36537724.0 spike=0.66
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=858.39 support=825.31 resistance=859.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=341813312.0 spike=1.0
- ORHD.CA: score=21.8 buy_ready=False sector_rank=14 price=41.29 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.6 liquidity=131782000.0 spike=0.93
- ORWE.CA: score=27.4 buy_ready=True sector_rank=1 price=26.06 support=22.72 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=53.95 liquidity=34124724.0 spike=0.43
- PHAR.CA: score=22.4 buy_ready=False sector_rank=8 price=129.74 support=104.2 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.9 liquidity=270716160.0 spike=0.58
- PHDC.CA: score=13.8 buy_ready=False sector_rank=14 price=14.62 support=14.32 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.26 liquidity=189878688.0 spike=0.82
- PHTV.CA: score=12.93 buy_ready=False sector_rank=15 price=339.88 support=312.0 resistance=447.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=51.82 liquidity=1271378.0 spike=0.47
- POUL.CA: score=24.4 buy_ready=True sector_rank=9 price=39.5 support=36.5 resistance=40.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.33 liquidity=25202392.0 spike=0.98
- PRCL.CA: score=11.92 buy_ready=False sector_rank=2 price=31.13 support=31.0 resistance=34.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31233014.0 spike=1.26
- PRDC.CA: score=26.86 buy_ready=True sector_rank=14 price=9.78 support=8.7 resistance=9.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.83 liquidity=149024336.0 spike=2.53
- PRMH.CA: score=10.68 buy_ready=False sector_rank=15 price=2.72 support=2.58 resistance=2.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28758642.0 spike=2.01
- RACC.CA: score=13.66 buy_ready=False sector_rank=15 price=9.5 support=9.4 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.08 liquidity=17515168.0 spike=0.84
- RAKT.CA: score=4.93 buy_ready=False sector_rank=15 price=22.11 support=21.4 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=9.2 liquidity=572274.81 spike=1.85
- RAYA.CA: score=20.38 buy_ready=False sector_rank=18 price=7.1 support=6.95 resistance=7.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.76 liquidity=74232600.0 spike=1.04
- RMDA.CA: score=22.4 buy_ready=False sector_rank=8 price=6.03 support=5.08 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=44.65 liquidity=59854068.0 spike=0.49
- ROTO.CA: score=17.14 buy_ready=False sector_rank=15 price=44.11 support=42.6 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.2 liquidity=8480744.0 spike=0.39
- RREI.CA: score=21.66 buy_ready=False sector_rank=15 price=4.32 support=4.24 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=16879698.0 spike=0.24
- RTVC.CA: score=19.49 buy_ready=True sector_rank=15 price=4.2 support=3.73 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=69.0 liquidity=3832599.25 spike=0.44
- RUBX.CA: score=25.72 buy_ready=True sector_rank=15 price=12.8 support=12.02 resistance=13.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=55.73 liquidity=18305692.0 spike=1.03
- SAUD.CA: score=19.0 buy_ready=False sector_rank=5 price=22.92 support=21.4 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=58.06 liquidity=6603164.5 spike=0.32
- SCEM.CA: score=24.4 buy_ready=True sector_rank=2 price=97.06 support=76.75 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=67.93 liquidity=131261624.0 spike=0.59
- SCFM.CA: score=21.71 buy_ready=True sector_rank=15 price=283.05 support=273.1 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.99 liquidity=8048254.0 spike=0.38
- SCTS.CA: score=19.07 buy_ready=True sector_rank=16 price=617.43 support=603.13 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=63.19 liquidity=3421352.25 spike=0.38
- SDTI.CA: score=23.66 buy_ready=True sector_rank=15 price=69.01 support=57.05 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.07 liquidity=10820455.0 spike=0.33
- SEIG.CA: score=13.25 buy_ready=False sector_rank=15 price=260.25 support=252.0 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=54.39 liquidity=1585516.5 spike=0.18
- SIPC.CA: score=23.66 buy_ready=True sector_rank=15 price=4.87 support=3.82 resistance=5.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=56.57 liquidity=21335486.0 spike=0.34
- SKPC.CA: score=27.23 buy_ready=True sector_rank=11 price=17.74 support=15.61 resistance=18.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.93 liquidity=105120336.0 spike=1.47
- SMFR.CA: score=18.38 buy_ready=False sector_rank=15 price=259.76 support=228.88 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.06 liquidity=9719936.0 spike=0.37
- SNFC.CA: score=12.66 buy_ready=False sector_rank=15 price=10.39 support=10.3 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.77 liquidity=13253756.0 spike=0.92
- SPIN.CA: score=27.4 buy_ready=True sector_rank=1 price=19.48 support=15.32 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.28 liquidity=15272424.0 spike=0.37
- SPMD.CA: score=11.31 buy_ready=False sector_rank=15 price=0.45 support=0.45 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.51 liquidity=7646940.0 spike=0.27
- SUGR.CA: score=24.68 buy_ready=False sector_rank=9 price=56.92 support=46.47 resistance=61.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.09 liquidity=60691760.0 spike=1.14
- SVCE.CA: score=23.66 buy_ready=False sector_rank=15 price=10.91 support=9.1 resistance=12.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.82 liquidity=71251328.0 spike=0.7
- SWDY.CA: score=24.4 buy_ready=True sector_rank=4 price=125.95 support=92.5 resistance=133.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.23 liquidity=56944072.0 spike=0.55
- TALM.CA: score=22.05 buy_ready=False sector_rank=16 price=17.71 support=17.36 resistance=20.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=42.77 liquidity=56284512.0 spike=1.2
- TMGH.CA: score=21.92 buy_ready=False sector_rank=14 price=95.22 support=95.2 resistance=99.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.6 liquidity=610589888.0 spike=2.56
- TRTO.CA: score=17.66 buy_ready=False sector_rank=15 price=0.05 support=0.03 resistance=0.05 source=Yahoo Finance as_of=2026-08-25T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=3617.48 spike=0.32
- UEFM.CA: score=13.2 buy_ready=False sector_rank=15 price=540.83 support=531.0 resistance=589.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=41.99 liquidity=1541355.5 spike=0.34
- UEGC.CA: score=11.02 buy_ready=False sector_rank=15 price=1.84 support=1.8 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=89180360.0 spike=2.18
- UNIP.CA: score=18.66 buy_ready=False sector_rank=15 price=0.37 support=0.35 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.37 liquidity=15564366.0 spike=0.47
- UNIT.CA: score=14.02 buy_ready=False sector_rank=14 price=18.7 support=17.51 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=2221856.75 spike=0.19
- WCDF.CA: score=12.35 buy_ready=False sector_rank=15 price=648.98 support=571.0 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=78.7 liquidity=1686778.0 spike=0.38
- WKOL.CA: score=22.61 buy_ready=True sector_rank=15 price=344.63 support=315.0 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=61.28 liquidity=6954586.0 spike=0.2
- ZEOT.CA: score=18.26 buy_ready=True sector_rank=15 price=13.76 support=12.2 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=65.36 liquidity=6596365.5 spike=0.26
- ZMID.CA: score=23.22 buy_ready=False sector_rank=14 price=8.93 support=7.06 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.97 liquidity=301728608.0 spike=1.21

## Backtesting Lite
- BINV.CA: 180d return=40.09%, max drawdown=-17.77%, MA20>MA50 days last20=20, as_of=2026-08-29T21:00:00+00:00
- FAIT.CA: 180d return=41.85%, max drawdown=-8.36%, MA20>MA50 days last20=20, as_of=2026-08-29T21:00:00+00:00
- CIEB.CA: 180d return=24.16%, max drawdown=-19.11%, MA20>MA50 days last20=20, as_of=2026-08-29T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- FAIT.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=607 sources=3 expected=Faisal Islamic Bank of Egypt summary=Faisal Islamic Bank of Egypt unveils dividends for 2025; Faisal Islamic Bank of Egypt’s consolidated net profits drop to EGP 4.6bn in 2025; Faisal Islamic Bank of Egypt posts 63% lower standalone net profits in 2025 Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Faisal Islamic Bank of Egypt unveils dividends for 2025: https://english.mubasher.info/news/4585552/Faisal-Islamic-Bank-of-Egypt-unveils-dividends-for-2025/
  - Faisal Islamic Bank of Egypt’s consolidated net profits drop to EGP 4.6bn in 2025: https://english.mubasher.info/news/4582812/Faisal-Islamic-Bank-of-Egypt-s-consolidated-net-profits-drop-to-EGP-4-6bn-in-2025/
  - Faisal Islamic Bank of Egypt posts 63% lower standalone net profits in 2025: https://english.mubasher.info/news/4548875/Faisal-Islamic-Bank-of-Egypt-posts-63-lower-standalone-net-profits-in-2025/
- CIEB.CA: status=RECENT_ACCEPTED latest=2026-07-29 age_days=33 sources=3 expected=Credit Agricole Egypt summary=Recent evidence for Credit Agricole Egypt (CIEB.CA) includes market announcements and financial results from the Egyptian Exchange and financial news outlets, covering Q1 2026 and 2025 performance.
  - Release from Credit Agricole Egypt (CIEB.CA) Regarding the Board of Directors & the Executive Managers (July 29, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6Q_-R60uz2fqJULBv6815vLB2x1cdWBVqD9Iz4l00BOvBZsUS9lijTKc37JzT5dHAbMu-S59xCUr_-Cj8iLKNBSSPMHCcPpG1nx9g4NNqjDOxxgMDjMoxgxIlyeiibkbG9lzuMQmGJ8z9Jk-1WLc=
  - Release from Credit Agricole Egypt (CIEB.CA) Regarding the Financial Results (July 29, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6Q_-R60uz2fqJULBv6815vLB2x1cdWBVqD9Iz4l00BOvBZsUS9lijTKc37JzT5dHAbMu-S59xCUr_-Cj8iLKNBSSPMHCcPpG1nx9g4NNqjDOxxgMDjMoxgxIlyeiibkbG9lzuMQmGJ8z9Jk-1WLc=
  - Credit Agricole Egypt (CIEB.CA) - Decisions of the BoD Meeting (July 29, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6Q_-R60uz2fqJULBv6815vLB2x1cdWBVqD9Iz4l00BOvBZsUS9lijTKc37JzT5dHAbMu-S59xCUr_-Cj8iLKNBSSPMHCcPpG1nx9g4NNqjDOxxgMDjMoxgxIlyeiibkbG9lzuMQmGJ8z9Jk-1WLc=
- SPIN.CA: status=RECENT_ACCEPTED latest=2026-08-30 age_days=1 sources=3 expected=Alexandria Spinning and Weaving summary=Alexandria Spinning and Weaving (SPIN.CA) has released recent financial results for various periods up to March 2026, showing both profits and losses, along with board decisions and capital changes.
  - Alexandria Spinning & Weaving (SPINALEX) (SPIN.CA) Reports its Financial Results for the Period from 01/07/2025 to 31/03/2026 (August 30, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIOF48ENb-soddC55mliIJpFbgsLvlqhMk6bbhzMXNPv2uYuMshKOEAw8BkfprSJXu7c0DHCO01YuwFw7FbXhazVbWXKcfqJ-FI4bhcuuiRhrOEgAVsat8nS9Og58aDOnv9QtdbYTejHI_6FkunKcPUw==
  - Alexandria Spinning & Weaving Co. Reports Earnings Results for the Third Quarter and Nine Months Ended March 31, 2026 (August 26, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7b2jsiZ3LznWmdJwngxSHDKcK7dVWAVcLnDHM60MngI9phSr2gZ5Sv9IFmANWIeBAzGfAnKCFdsfZzEaJT7RH6vkeIWLhYIcG0URyPOGVQGCi1bIsStHPqghelaIJzpARJYBKTA8dkmXnCzfD7n3QCUiHSBcb444pTPnLESM2itv0wNFwC7abfZbOMP0GxFXFrQfYQ8r9ygwZ3L7dmWdti7g4IsBFPoKu_bQiVQMHUTX2qo3WVrR-DHD4vnFeYHesKhsI4qhdD9MbjsgpxgMB
  - Alexandria Spinning & Weaving (SPINALEX) (SPIN.CA) Reports Its Financial Results for the Period From 01/07/2025 to 31/12/2025 (August 04, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0UbmnLLAnn7A_gaJ29cNrsGPvYzPGCh5R1jlPr5Ofae6SD7K8E_VIqBmDOfvh6fIhuLpDmTJfA5mLAmB6Gk6Aok9fhXac7BUQInn8PDilfWRoIX-GdFFmf-eyoGDgoRkYJCJqF5zfWBI8m6Ler00ZkiB7IPcpvtpa0Ds2Wb1wQS48sMBKcqh16APrVs7J3w==
- ORWE.CA: status=RECENT_ACCEPTED latest=2026-08-11 age_days=20 sources=3 expected=Oriental Weavers summary=Oriental Weavers (ORWE.CA) has released its Q1 and Q2 2026 earnings, along with a 2025 cash dividend. The company also provides investor relations reports and disclosures.
  - Oriental Weavers 2Q 2026 Earnings Release (August 11, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-ihogHkxC_RrTFrodnyvPF1aAxNYxV2aGrX4fDCZwGQpt8ZEGJlusEa3qf_m5ePJnCDjWK6zS1HUapbtC3ozQJKuhknfmCBBK_-zUbx2NDwHOyqYf2tuthJJUEw7akGyLgDSgVJYP9A==
  - Oriental Weavers 1Q 2026 Earnings Release (May 20, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-ihogHkxC_RrTFrodnyvPF1aAxNYxV2aGrX4fDCZwGQpt8ZEGJlusEa3qf_m5ePJnCDjWK6zS1HUapbtC3ozQJKuhknfmCBBK_-zUbx2NDwHOyqYf2tuthJJUEw7akGyLgDSgVJYP9A==
  - 2025 Cash Dividend Value: EGP 1.5, Payment Date: May 20, 2026: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-ihogHkxC_RrTFrodnyvPF1aAxNYxV2aGrX4fDCZwGQpt8ZEGJlusEa3qf_m5ePJnCDjWK6zS1HUapbtC3ozQJKuhknfmCBBK_-zUbx2NDwHOyqYf2tuthJJUEw7akGyLgDSgVJYP9A==
- SKPC.CA: status=RECENT_ACCEPTED latest=2026-08-13 age_days=18 sources=3 expected=Sidi Kerir Petrochemicals summary=Sidi Kerir Petrochemicals (SKPC.CA) has reported financial results for the first half of 2026 and 2025, along with board decisions and news regarding a private placement.
  - Sidi Kerir Petrochemicals - SIDPEC (SKPC.CA) Reports Its Financial Results for the Period From 01/01/2026 to 30/06/2026 (August 13, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9ZNk5nFDro-6dYfexPx_dGJdkYDFjwZFvD1wZ03sIJjgM3vjNIeta-feEcpH09hdZCP1aEkmgxOLjAFAEqkH91VOGPJvb032QuSV368afKaQAvxBk5ZxMQba00_DBq93VVtrpfDwvDI9z0PQnfnSZqNg=
  - Sidi Kerir Petrochemicals - SIDPEC (SKPC.CA) - Decisions of the BoD Meeting (July 30, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9ZNk5nFDro-6dYfexPx_dGJdkYDFjwZFvD1wZ03sIJjgM3vjNIeta-feEcpH09hdZCP1aEkmgxOLjAFAEqkH91VOGPJvb032QuSV368afKaQAvxBk5ZxMQba00_DBq93VVtrpfDwvDI9z0PQnfnSZqNg==
  - Sidi Kerir Petrochemicals Co. announced private placement on October 20, 2025: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHk5iA5Qk2FQwT_mLUc9sePtbgsG3dMERgBybEMZc9tdffwhmNr2hPyuaf2DHEwkYXS0dQI-EpfUa58IkRGLLhJ-30Its_o__ddhdJEv1xVwDmNbvzbxX9KoYDXMYanylRIfLUJ7yTAj9qLnMON2Ir5u70P0ckFcfLFBzFpPzJm1qkKgfrYksB6k6gJmf0
- ABUK.CA: status=RECENT_ACCEPTED latest=2026-08-31 age_days=0 sources=3 expected=Abu Qir Fertilizers summary=Abu Qir Fertilizers (ABUK.CA) has upcoming earnings, recent dividend information, and material events related to operations and strategic initiatives, including a license for a solar power station and news on green hydrogen adoption.
  - Abou Kir Fertilizers & Chemical Industries Co. next earnings report on Aug 31, 2026: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2P2uenY4DH-FAyakhysYec-ja3NmgfrijjH2h8qg5uGEBHUA396nnpP9gTrkNkNu0e33fvR4nEWH2FqlqmpoEpX6k0jlr_ptiNk1vfGZkjcSu55Tno6ZxpyC-ZXF7jyLWaHSA0OI=
  - Abu Qir Fertilizers dividend yield was 12.00% in 2025: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2P2uenY4DH-FAyakhysYec-ja3NmgfrijjH2h8qg5uGEBHUA396nnpP9gTrkNkNu0e33fvR4nEWH2FqlqmpoEpX6k0jlr_ptiNk1vfGZkjcSu55Tno6ZxpyC-ZXF7jyLWaHSA0OI=
  - Grant the company a license to operate electricity generation activity from the solar power station (Dec 23, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPTKiqWyTLavzXNhIBJpKKi8UQWiPYDLv0JmUWvjgz5vNMT2-wH8MkCzyFpMvYF8awdbsdT-CiZO56tQXJcsXVCczHCjsPU9EoDMM-rGwqHbVUir9vQfbTfcPTW3mux6NbaKaY_CYMBIO-1kJdc-c=
- PRDC.CA: status=RECENT_ACCEPTED latest=2026-08-23 age_days=8 sources=3 expected=Pioneers Properties For Urban Development summary=Pioneers Properties For Urban Development (PRDC.CA) has reported strong financial results for H1 2026, Q1 2026, and the full years 2025 and 2024, with significant profit growth and increasing investor sentiment.
  - Pioneers Properties For Urban Development - PRE Group (PRDC.CA) Reports its Financial Results (Consolidated) for the Period from 01/01/2026 to 30/06/2026 (August 23, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHirHf2IAb5FZaXGV1omwuFiGgNCK9gcZtcht67OMiboI7hl5iKVqRCOrP84HwbXkwaO8EJ7WqtEIDg71QYqf_JnY9CqNbFngzWTWigrfnw25iyWQmL5G6MYMTDC8zwuWUlkqCPpfkLjPvxbjgc5DA=
  - First quarter 2026 earnings released: EPS: EGP 0.31 (vs EGP 0.073 in 1Q 2025), Revenue: EGP 1.90b (up 25% from 1Q 2025), Net income: EGP 323.7m (up 338% from 1Q 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL42EeyBE5fBi7pjobEnnxsdTohVT4lFZT3BKnaleNh8Mit7zNZnJ0teG4YMl-HiZgONPVJcsu856SsBMOXiftCoe3xYZpzLYgFcf2L71WOp8iH40iTIyQGzy_eUzt_RJ1xrbDKLUNhZGh8yXjUL7jYr2H5Ufo5t3OTSWPKm7xjxCw2KKbO6XuATfgN-uRyPxSyAAI9GjQd9Z0TdraF0MVR6qKjo_tKxFYi1u9wsQhstieCgI=
  - Investor sentiment improves as stock rises 20% (July 15, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL42EeyBE5fBi7pjobEnnxsdTohVT4lFZT3BKnaleNh8Mit7zNZnJ0teG4YMl-HiZgONPVJcsu856SsBMOXiftCoe3xYZpzLYgFcf2L71WOp8iH40iTIyQGzy_eUzt_RJ1xrbDKLUNhZGh8yXjUL7jYr2H5Ufo5t3OTSWPKm7xjxCw2KKbO6XuATfgN-uRyPxSyAAI9GjQd9Z0TdraF0MVR6qGjo_tKxFYi1u9wsQhstieCgI=

## Warnings
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Evidence for FAIT.CA matches the company but appears old; latest detected date is 2025-01-01.
