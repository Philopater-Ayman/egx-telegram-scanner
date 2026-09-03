# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-09-03T11:12:08.482502+00:00
Generated Cairo: 2026-09-03 14:12
Run timing: target 09:15 Cairo | generated Cairo 2026-09-03 14:12 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-09-03 14:08

## Control Center
- Action tickets: 1 prioritized signal(s)
- BUY-ready candidates: 57
- Data quality issues: 1
- Tradeable price/liquidity tickers: 176/189
- Top sector: Transportation & Logistics

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, September 03
- Freshness: DELAYED
- EGX30 regime: CONSTRUCTIVE / above MA20 57.89% / above MA50 78.95%
- EGX70 regime: CONSTRUCTIVE / above MA20 50.0% / above MA50 72.5%
- Sector breadth: 42.86%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- ORAS.CA: liquidity=408392192.0 spike=1.0 score=7.6
- EGCH.CA: liquidity=314145824.0 spike=2.29 score=29.98
- COMI.CA: liquidity=301651840.0 spike=0.57 score=24.29
- BIOC.CA: liquidity=272819936.0 spike=1.15 score=8.94
- CCAP.CA: liquidity=264094704.0 spike=0.41 score=24.4

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: The scanner prioritized ALCN.CA because its price sits above the MA20/MA50, shows a strong liquidity accumulation spike, and rests near identified support with modest upside to resistance, all within the leading Transportation & Logistics sector while the EGX30 and EGX70 indices remain in a constructive trend and the market is in SELECTIVE_SWING_TRADES_ONLY mode, which tempers aggressiveness and adds uncertainty.
- ALCN.CA: price > MA20/MA50, RSI ~56, liquidity accumulation spike 3.34×, support 30.03, resistance 32.8, outlook BULLISH_WATCH, sector leader.
- EGCH.CA & FERC.CA: accumulation spikes, prices approaching resistance, Basic Resources & Chemicals sector, watch for resistance break or pullback.
- MBSC.CA & ARCC.CA: Building Materials stocks, liquidity cooling, momentum extended, far above support, higher short‑term volatility, outlook BULLISH_WATCH but caution advised.
- Market regime: EGX30 & EGX70 both CONSTRUCTIVE, sector breadth 42.86%, risk mode SELECTIVE_SWING_TRADES_ONLY → only selective swing setups considered, confidence remains low and liquidity signals mixed, introducing uncer

## Top Liquidity Spikes
- EPPK.CA: spike=3.35 liquidity=3878994.25 outlook=WEAK_OR_RISKY score=21.1 buy_ready=False
- ALCN.CA: spike=3.34 liquidity=102775480.0 outlook=BULLISH_WATCH score=100 buy_ready=True
- MFSC.CA: spike=2.91 liquidity=33199518.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MOIN.CA: spike=2.77 liquidity=97458600.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RAYA.CA: spike=2.65 liquidity=163227312.0 outlook=CONSTRUCTIVE score=58.74 buy_ready=False

## Sector Leaderboard
- #1 Transportation & Logistics: score=13.58 5d=6.87% 20d=10.35% aboveMA50=100.0%
- #2 Building Materials: score=10.77 5d=1.96% 20d=25.32% aboveMA50=83.33%
- #3 Basic Resources & Chemicals: score=10.75 5d=5.33% 20d=10.77% aboveMA50=80.0%
- #4 Investment Holding: score=10.13 5d=2.61% 20d=12.38% aboveMA50=100.0%
- #5 Textiles: score=9.41 5d=-0.54% 20d=16.59% aboveMA50=100.0%
- #6 Telecommunications: score=8.45 5d=1.12% 20d=2.71% aboveMA50=100.0%
- #7 Tourism & Leisure: score=6.65 5d=1.58% 20d=10.59% aboveMA50=0.0%
- #8 Industrial Goods & Cables: score=5.81 5d=0.62% 20d=9.17% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- Priority #1: BUY ALCN.CA
  - Entry: 33.01 | Take profit: 35.65 | Stop loss: 31.69
  - Confidence: LOW | score=34.08 | outlook=BULLISH_WATCH 100
  - Reason: BUY SETUP: ALCN.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 56.44, support 30.03, resistance 32.8, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ALCN.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- EGCH.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=close to resistance
- FERC.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- ISMQ.CA: BULLISH_WATCH score=96 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- CSAG.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- EXPA.CA: BULLISH_WATCH score=87.72 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CANA.CA: BULLISH_WATCH score=87.72 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ARCC.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- MCQE.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- BINV.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling

## BUY-Ready Candidates
- ALCN.CA: rank=34.08 outlook=BULLISH_WATCH outlook_score=100 sector_rank=1 price=33.01 support=30.03 resistance=32.8 liquidity=102775480.0
- EGCH.CA: rank=29.98 outlook=BULLISH_WATCH outlook_score=100 sector_rank=3 price=14.59 support=13.3 resistance=14.79 liquidity=314145824.0
- FERC.CA: rank=29.74 outlook=BULLISH_WATCH outlook_score=100 sector_rank=3 price=82.24 support=76.7 resistance=87.3 liquidity=44342832.0
- MBSC.CA: rank=28.4 outlook=BULLISH_WATCH outlook_score=72 sector_rank=2 price=419.65 support=253.1 resistance=470.0 liquidity=30157476.0
- ARCC.CA: rank=28.4 outlook=BULLISH_WATCH outlook_score=86 sector_rank=2 price=76.85 support=58.25 resistance=91.72 liquidity=27561416.0
- ETRS.CA: rank=27.64 outlook=CONSTRUCTIVE outlook_score=69.1 sector_rank=15 price=11.31 support=10.43 resistance=11.66 liquidity=14169436.0
- MASR.CA: rank=27.48 outlook=BULLISH_WATCH outlook_score=80.1 sector_rank=15 price=7.97 support=7.45 resistance=8.05 liquidity=120259808.0
- ISMQ.CA: rank=27.4 outlook=BULLISH_WATCH outlook_score=96 sector_rank=3 price=9.33 support=9.0 resistance=9.97 liquidity=33744216.0
- MAAL.CA: rank=27.06 outlook=BULLISH_WATCH outlook_score=80.1 sector_rank=15 price=9.89 support=8.32 resistance=9.76 liquidity=23267710.0
- CSAG.CA: rank=26.9 outlook=BULLISH_WATCH outlook_score=90 sector_rank=1 price=41.52 support=36.07 resistance=44.45 liquidity=9500466.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=21.64 buy_ready=False sector_rank=15 price=302.51 support=288.0 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=50.7 liquidity=18221848.0 spike=0.4
- ABUK.CA: score=25.92 buy_ready=False sector_rank=3 price=91.95 support=73.2 resistance=94.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=85.09 liquidity=248546000.0 spike=1.76
- ACAMD.CA: score=13.64 buy_ready=False sector_rank=15 price=2.06 support=1.95 resistance=2.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=28.89 liquidity=33768568.0 spike=0.62
- ACGC.CA: score=20.54 buy_ready=False sector_rank=5 price=13.94 support=10.36 resistance=14.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=72.57 liquidity=8136450.5 spike=0.2
- ADCI.CA: score=18.71 buy_ready=True sector_rank=15 price=298.97 support=274.0 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=5069723.5 spike=0.24
- ADIB.CA: score=17.29 buy_ready=False sector_rank=10 price=52.2 support=51.81 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=47752352.0 spike=0.71
- ADPC.CA: score=16.64 buy_ready=False sector_rank=15 price=3.97 support=3.85 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=29.52 liquidity=10261527.0 spike=0.24
- AFDI.CA: score=16.64 buy_ready=False sector_rank=15 price=55.79 support=53.54 resistance=69.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=26.42 liquidity=10669827.0 spike=0.32
- AFMC.CA: score=16.64 buy_ready=False sector_rank=15 price=172.69 support=175.2 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=22.13 liquidity=40202216.0 spike=0.32
- AJWA.CA: score=13.64 buy_ready=False sector_rank=15 price=179.0 support=176.0 resistance=202.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=8.21 liquidity=20448528.0 spike=0.34
- ALCN.CA: score=34.08 buy_ready=True sector_rank=1 price=33.01 support=30.03 resistance=32.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=56.44 liquidity=102775480.0 spike=3.34
- ALUM.CA: score=20.1 buy_ready=True sector_rank=15 price=28.28 support=24.35 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=55.19 liquidity=6464166.0 spike=0.23
- AMER.CA: score=21.46 buy_ready=False sector_rank=16 price=5.53 support=5.3 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=35.04 liquidity=17492322.0 spike=0.18
- AMES.CA: score=10.5 buy_ready=False sector_rank=15 price=86.45 support=85.02 resistance=94.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=186027136.0 spike=1.93
- AMIA.CA: score=20.64 buy_ready=False sector_rank=15 price=19.53 support=10.6 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=80.43 liquidity=11155470.0 spike=0.17
- AMOC.CA: score=23.32 buy_ready=False sector_rank=9 price=13.51 support=9.01 resistance=14.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=81.25 liquidity=126197440.0 spike=0.71
- APSW.CA: score=8.03 buy_ready=False sector_rank=15 price=8.61 support=8.41 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=48.18 liquidity=385896.59 spike=0.26
- ARAB.CA: score=25.46 buy_ready=True sector_rank=16 price=0.26 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=60.34 liquidity=37676940.0 spike=0.4
- ARCC.CA: score=28.4 buy_ready=True sector_rank=2 price=76.85 support=58.25 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=57.02 liquidity=27561416.0 spike=0.25
- AREH.CA: score=18.64 buy_ready=False sector_rank=15 price=1.48 support=1.39 resistance=1.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=35.48 liquidity=18436474.0 spike=0.63
- ARVA.CA: score=8.64 buy_ready=False sector_rank=15 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=16.64 buy_ready=False sector_rank=15 price=62.82 support=62.01 resistance=69.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=30.6 liquidity=14005796.0 spike=0.34
- ASPI.CA: score=22.3 buy_ready=False sector_rank=15 price=0.43 support=0.43 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=36.58 liquidity=52995916.0 spike=1.33
- ATLC.CA: score=21.93 buy_ready=False sector_rank=18 price=7.2 support=5.15 resistance=8.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=83.45 liquidity=30816144.0 spike=0.97
- ATQA.CA: score=22.4 buy_ready=False sector_rank=3 price=12.04 support=10.09 resistance=12.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=77.61 liquidity=71889416.0 spike=0.72
- AXPH.CA: score=15.9 buy_ready=False sector_rank=15 price=1691.24 support=1260.0 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=92.42 liquidity=5257737.0 spike=0.4
- BINV.CA: score=24.36 buy_ready=True sector_rank=4 price=49.52 support=46.25 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=55.62 liquidity=7956262.5 spike=0.73
- BIOC.CA: score=8.94 buy_ready=False sector_rank=15 price=339.0 support=316.41 resistance=353.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=272819936.0 spike=1.15
- BTFH.CA: score=16.93 buy_ready=False sector_rank=18 price=3.04 support=2.94 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=43859784.0 spike=0.25
- CAED.CA: score=18.48 buy_ready=False sector_rank=15 price=140.31 support=118.01 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=59.8 liquidity=6844113.0 spike=0.19
- CANA.CA: score=25.43 buy_ready=True sector_rank=10 price=42.96 support=38.61 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=48.79 liquidity=26766504.0 spike=1.57
- CCAP.CA: score=24.4 buy_ready=False sector_rank=4 price=5.95 support=5.18 resistance=6.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=72.93 liquidity=264094704.0 spike=0.41
- CCRS.CA: score=23.64 buy_ready=False sector_rank=15 price=2.56 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=53.85 liquidity=13041740.0 spike=0.25
- CEFM.CA: score=17.66 buy_ready=False sector_rank=15 price=145.63 support=132.0 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=72.43 liquidity=6022558.5 spike=0.29
- CERA.CA: score=10.26 buy_ready=False sector_rank=15 price=1.48 support=1.38 resistance=1.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51938260.0 spike=1.81
- CFGH.CA: score=14.66 buy_ready=False sector_rank=15 price=0.12 support=0.1 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=85.19 liquidity=39131.62 spike=1.99
- CICH.CA: score=18.42 buy_ready=False sector_rank=18 price=12.3 support=12.0 resistance=13.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=38.46 liquidity=7253153.0 spike=1.12
- CIEB.CA: score=23.02 buy_ready=True sector_rank=10 price=25.28 support=24.0 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=59.58 liquidity=6733529.5 spike=0.46
- CIRA.CA: score=16.67 buy_ready=False sector_rank=13 price=35.0 support=32.1 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=31.51 liquidity=12133150.0 spike=0.35
- CLHO.CA: score=23.66 buy_ready=True sector_rank=14 price=17.6 support=16.95 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=65.42 liquidity=44182520.0 spike=0.57
- CNFN.CA: score=17.93 buy_ready=False sector_rank=18 price=4.78 support=4.73 resistance=5.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=13682617.0 spike=0.77
- COMI.CA: score=24.29 buy_ready=True sector_rank=10 price=140.31 support=135.35 resistance=142.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=49.07 liquidity=301651840.0 spike=0.57
- COPR.CA: score=21.64 buy_ready=False sector_rank=15 price=0.48 support=0.4 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=61.85 liquidity=33270056.0 spike=0.37
- COSG.CA: score=23.98 buy_ready=True sector_rank=15 price=1.91 support=1.69 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=51.35 liquidity=61693264.0 spike=1.17
- CPCI.CA: score=16.86 buy_ready=True sector_rank=15 price=543.98 support=483.0 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=60.35 liquidity=3220804.0 spike=0.37
- CSAG.CA: score=26.9 buy_ready=True sector_rank=1 price=41.52 support=36.07 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=50.19 liquidity=9500466.0 spike=0.35
- DAPH.CA: score=8.64 buy_ready=False sector_rank=15 price=129.24 support=127.4 resistance=140.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=49605192.0 spike=0.7
- DEIN.CA: score=11.64 buy_ready=False sector_rank=15 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance as_of=2026-09-01T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=8.67 buy_ready=False sector_rank=17 price=28.31 support=27.79 resistance=30.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=31.76 liquidity=2289033.5 spike=0.14
- DSCW.CA: score=16.64 buy_ready=False sector_rank=15 price=1.95 support=1.84 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=23.26 liquidity=26317294.0 spike=0.31
- DTPP.CA: score=23.64 buy_ready=True sector_rank=15 price=302.4 support=244.1 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=51.39 liquidity=15326733.0 spike=0.4
- EALR.CA: score=21.64 buy_ready=False sector_rank=15 price=384.56 support=376.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=50.26 liquidity=11317585.0 spike=0.28
- EASB.CA: score=17.07 buy_ready=True sector_rank=15 price=7.44 support=7.05 resistance=8.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=3426029.5 spike=0.44
- EAST.CA: score=19.38 buy_ready=False sector_rank=17 price=36.0 support=35.0 resistance=37.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=44.19 liquidity=23348496.0 spike=0.37
- EBSC.CA: score=23.24 buy_ready=True sector_rank=15 price=2.18 support=1.88 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=68.29 liquidity=9604144.0 spike=0.68
- ECAP.CA: score=9.3 buy_ready=False sector_rank=15 price=33.58 support=31.16 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=26.83 liquidity=5658330.5 spike=0.31
- EDFM.CA: score=17.3 buy_ready=True sector_rank=15 price=425.84 support=390.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=59.18 liquidity=2917394.75 spike=1.37
- EEII.CA: score=17.56 buy_ready=False sector_rank=15 price=2.36 support=2.4 resistance=2.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=9919978.0 spike=1.0
- EFIC.CA: score=14.4 buy_ready=False sector_rank=3 price=193.1 support=193.0 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=20.29 liquidity=11497743.0 spike=0.25
- EFID.CA: score=21.38 buy_ready=False sector_rank=17 price=30.18 support=29.71 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=37.61 liquidity=74911528.0 spike=0.87
- EFIH.CA: score=20.92 buy_ready=False sector_rank=19 price=23.24 support=22.16 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=36.52 liquidity=79431256.0 spike=0.69
- EGAL.CA: score=24.4 buy_ready=False sector_rank=3 price=373.89 support=296.25 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=78.04 liquidity=80733016.0 spike=0.5
- EGAS.CA: score=24.56 buy_ready=True sector_rank=9 price=59.68 support=55.21 resistance=63.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=49.67 liquidity=26083734.0 spike=1.12
- EGBE.CA: score=12.33 buy_ready=False sector_rank=10 price=0.53 support=0.5 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=40.48 liquidity=37455.24 spike=0.19
- EGCH.CA: score=29.98 buy_ready=True sector_rank=3 price=14.59 support=13.3 resistance=14.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=48.73 liquidity=314145824.0 spike=2.29
- EGSA.CA: score=14.51 buy_ready=False sector_rank=6 price=9.05 support=8.65 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=89.47 liquidity=14881.08 spike=1.55
- EGTS.CA: score=8.1 buy_ready=False sector_rank=16 price=16.73 support=16.17 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=26.76 liquidity=4648021.5 spike=0.14
- EHDR.CA: score=21.64 buy_ready=False sector_rank=15 price=2.88 support=2.8 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=11967295.0 spike=0.37
- EKHO.CA: score=10.32 buy_ready=False sector_rank=9 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-09-01T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=18.32 buy_ready=False sector_rank=8 price=2.1 support=2.04 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=40768452.0 spike=0.64
- ELKA.CA: score=25.64 buy_ready=True sector_rank=15 price=1.85 support=1.7 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=20562714.0 spike=0.3
- ELNA.CA: score=5.0 buy_ready=False sector_rank=15 price=36.8 support=36.1 resistance=38.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=30.42 liquidity=357972.44 spike=0.96
- ELSH.CA: score=18.64 buy_ready=False sector_rank=15 price=13.36 support=12.97 resistance=14.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=41.1 liquidity=19244898.0 spike=0.4
- ELWA.CA: score=13.57 buy_ready=False sector_rank=15 price=1.84 support=1.62 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=58.82 liquidity=934210.44 spike=0.39
- EMFD.CA: score=22.94 buy_ready=False sector_rank=16 price=14.3 support=11.51 resistance=13.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=91.87 liquidity=178503392.0 spike=1.24
- ENGC.CA: score=21.64 buy_ready=False sector_rank=15 price=43.46 support=41.8 resistance=54.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=37.05 liquidity=10507498.0 spike=0.38
- EOSB.CA: score=15.65 buy_ready=False sector_rank=15 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-09-01T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=5206.12 spike=0.11
- EPCO.CA: score=11.18 buy_ready=False sector_rank=15 price=11.12 support=10.8 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=34.15 liquidity=4536185.0 spike=0.26
- EPPK.CA: score=11.22 buy_ready=False sector_rank=15 price=10.57 support=10.84 resistance=15.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=26.32 liquidity=3878994.25 spike=3.35
- ETEL.CA: score=24.4 buy_ready=True sector_rank=6 price=115.05 support=107.0 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=53.03 liquidity=56718924.0 spike=0.4
- ETRS.CA: score=27.64 buy_ready=True sector_rank=15 price=11.31 support=10.43 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=63.59 liquidity=14169436.0 spike=0.51
- EXPA.CA: score=25.71 buy_ready=True sector_rank=10 price=21.49 support=19.8 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=47.06 liquidity=63140148.0 spike=1.71
- FAIT.CA: score=18.27 buy_ready=True sector_rank=10 price=43.5 support=37.01 resistance=45.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT RSI=62.7 liquidity=1978697.5 spike=0.25
- FAITA.CA: score=9.32 buy_ready=False sector_rank=10 price=0.98 support=0.97 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT RSI=54.84 liquidity=30537.02 spike=0.54
- FERC.CA: score=29.74 buy_ready=True sector_rank=3 price=82.24 support=76.7 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=49.91 liquidity=44342832.0 spike=2.17
- FWRY.CA: score=20.92 buy_ready=False sector_rank=19 price=19.01 support=18.66 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=47.73 liquidity=51208956.0 spike=0.32
- GBCO.CA: score=12.27 buy_ready=False sector_rank=21 price=29.3 support=27.51 resistance=32.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=30.97 liquidity=32739030.0 spike=0.63
- GDWA.CA: score=24.64 buy_ready=True sector_rank=15 price=0.83 support=0.77 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=58.9 liquidity=18595830.0 spike=0.37
- GGCC.CA: score=16.64 buy_ready=False sector_rank=15 price=0.87 support=0.83 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=25.08 liquidity=30719884.0 spike=0.57
- GIHD.CA: score=25.8 buy_ready=True sector_rank=15 price=72.0 support=58.01 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=59.84 liquidity=26911838.0 spike=1.08
- GMCI.CA: score=10.64 buy_ready=False sector_rank=15 price=1.85 support=1.83 resistance=2.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=880570.63 spike=1.56
- GRCA.CA: score=23.64 buy_ready=False sector_rank=15 price=79.56 support=54.7 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=70.97 liquidity=31586496.0 spike=0.5
- GSSC.CA: score=11.88 buy_ready=False sector_rank=15 price=305.0 support=281.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39628576.0 spike=2.62
- GTWL.CA: score=20.64 buy_ready=False sector_rank=15 price=233.11 support=98.01 resistance=247.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=78.58 liquidity=173830176.0 spike=0.59
- HDBK.CA: score=12.47 buy_ready=False sector_rank=10 price=122.09 support=114.01 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=112115720.0 spike=2.59
- HELI.CA: score=26.38 buy_ready=True sector_rank=16 price=8.15 support=7.34 resistance=8.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=56.61 liquidity=220775392.0 spike=1.46
- HRHO.CA: score=11.93 buy_ready=False sector_rank=18 price=25.99 support=25.33 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=32.22 liquidity=50650796.0 spike=0.4
- ICID.CA: score=20.64 buy_ready=False sector_rank=15 price=18.2 support=8.0 resistance=18.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=82.64 liquidity=20802782.0 spike=0.74
- IDRE.CA: score=20.82 buy_ready=False sector_rank=15 price=53.15 support=51.16 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=50.67 liquidity=9178272.0 spike=0.61
- IFAP.CA: score=22.01 buy_ready=True sector_rank=12 price=21.1 support=20.2 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=36.13 liquidity=8217643.0 spike=0.24
- INFI.CA: score=21.64 buy_ready=False sector_rank=15 price=148.74 support=125.0 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=43.91 liquidity=51886356.0 spike=0.73
- IRON.CA: score=17.85 buy_ready=False sector_rank=3 price=29.99 support=29.82 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=40.39 liquidity=8446989.0 spike=0.64
- ISMA.CA: score=21.64 buy_ready=False sector_rank=15 price=32.84 support=30.7 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=46.22 liquidity=21713114.0 spike=0.84
- ISMQ.CA: score=27.4 buy_ready=True sector_rank=3 price=9.33 support=9.0 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=52.59 liquidity=33744216.0 spike=0.77
- ISPH.CA: score=16.66 buy_ready=False sector_rank=14 price=13.15 support=12.75 resistance=16.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=25.41 liquidity=63147300.0 spike=0.32
- JUFO.CA: score=22.38 buy_ready=False sector_rank=17 price=27.32 support=26.07 resistance=28.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=47.84 liquidity=25031832.0 spike=0.47
- KABO.CA: score=24.4 buy_ready=True sector_rank=5 price=9.2 support=7.94 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=40623652.0 spike=0.91
- KWIN.CA: score=8.64 buy_ready=False sector_rank=15 price=105.5 support=103.04 resistance=115.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31953760.0 spike=0.47
- KZPC.CA: score=20.2 buy_ready=True sector_rank=15 price=12.85 support=8.86 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=66.48 liquidity=8563502.0 spike=0.16
- LCSW.CA: score=24.4 buy_ready=False sector_rank=2 price=34.17 support=32.12 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=57.66 liquidity=27978200.0 spike=0.84
- LUTS.CA: score=8.64 buy_ready=False sector_rank=15 price=0.85 support=0.84 resistance=0.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=124487672.0 spike=0.47
- MAAL.CA: score=27.06 buy_ready=True sector_rank=15 price=9.89 support=8.32 resistance=9.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=68.24 liquidity=23267710.0 spike=1.71
- MASR.CA: score=27.48 buy_ready=True sector_rank=15 price=7.97 support=7.45 resistance=8.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=54.37 liquidity=120259808.0 spike=1.92
- MBSC.CA: score=28.4 buy_ready=True sector_rank=2 price=419.65 support=253.1 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=64.1 liquidity=30157476.0 spike=0.31
- MCQE.CA: score=26.4 buy_ready=True sector_rank=2 price=245.5 support=190.5 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=46.59 liquidity=11186952.0 spike=0.18
- MCRO.CA: score=23.64 buy_ready=True sector_rank=15 price=1.52 support=1.44 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=110036104.0 spike=0.99
- MENA.CA: score=5.09 buy_ready=False sector_rank=16 price=6.99 support=6.59 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=20.27 liquidity=1638524.5 spike=0.28
- MEPA.CA: score=25.64 buy_ready=True sector_rank=15 price=1.87 support=1.8 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=10523331.0 spike=0.35
- MFPC.CA: score=25.8 buy_ready=False sector_rank=3 price=46.0 support=36.95 resistance=46.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=84.07 liquidity=199783728.0 spike=1.7
- MFSC.CA: score=12.46 buy_ready=False sector_rank=15 price=53.41 support=51.45 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33199518.0 spike=2.91
- MHOT.CA: score=22.4 buy_ready=False sector_rank=7 price=18.35 support=16.81 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=47.6 liquidity=11164932.0 spike=0.6
- MICH.CA: score=23.64 buy_ready=True sector_rank=15 price=50.51 support=46.3 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=68.45 liquidity=27168054.0 spike=0.64
- MILS.CA: score=21.64 buy_ready=False sector_rank=15 price=203.05 support=179.05 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=58.39 liquidity=17227932.0 spike=0.24
- MIPH.CA: score=19.67 buy_ready=True sector_rank=14 price=789.39 support=700.2 resistance=827.36 source=Yahoo Finance as_of=2026-09-01T21:00:00+00:00 freshness=FRESH RSI=56.04 liquidity=5007100.86 spike=1.5
- MOED.CA: score=23.64 buy_ready=False sector_rank=15 price=0.83 support=0.67 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=70.41 liquidity=48613828.0 spike=0.45
- MOIL.CA: score=12.41 buy_ready=False sector_rank=9 price=0.67 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=51.35 liquidity=98643.04 spike=0.38
- MOIN.CA: score=12.18 buy_ready=False sector_rank=15 price=37.09 support=32.8 resistance=38.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=97458600.0 spike=2.77
- MOSC.CA: score=23.64 buy_ready=True sector_rank=15 price=324.22 support=292.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=50.54 liquidity=10809247.0 spike=0.68
- MPCI.CA: score=23.72 buy_ready=False sector_rank=15 price=429.81 support=310.05 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=73.97 liquidity=204508528.0 spike=1.04
- MPCO.CA: score=21.79 buy_ready=False sector_rank=12 price=2.16 support=1.94 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=44.12 liquidity=44003168.0 spike=0.43
- MPRC.CA: score=18.72 buy_ready=False sector_rank=15 price=42.67 support=39.5 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=42.96 liquidity=39643348.0 spike=1.04
- MTIE.CA: score=12.27 buy_ready=False sector_rank=21 price=8.6 support=8.25 resistance=11.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=31.86 liquidity=35503040.0 spike=0.51
- NAHO.CA: score=8.67 buy_ready=False sector_rank=15 price=0.14 support=0.1 resistance=0.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=78.43 liquidity=31992.81 spike=0.31
- NCCW.CA: score=23.38 buy_ready=False sector_rank=15 price=6.06 support=5.59 resistance=7.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=60.14 liquidity=37640400.0 spike=1.37
- NEDA.CA: score=9.09 buy_ready=False sector_rank=15 price=2.74 support=2.7 resistance=2.97 source=Yahoo Finance as_of=2026-09-01T21:00:00+00:00 freshness=FRESH RSI=52.24 liquidity=453722.08 spike=0.63
- NHPS.CA: score=21.64 buy_ready=False sector_rank=15 price=86.85 support=84.0 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=47.99 liquidity=13525140.0 spike=0.42
- NINH.CA: score=23.64 buy_ready=True sector_rank=15 price=23.55 support=21.53 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=65.1 liquidity=16098319.0 spike=0.37
- NIPH.CA: score=21.66 buy_ready=False sector_rank=14 price=346.81 support=266.01 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=35.12 liquidity=241182176.0 spike=0.69
- OBRI.CA: score=21.47 buy_ready=False sector_rank=15 price=33.59 support=31.62 resistance=34.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=56.83 liquidity=9834440.0 spike=0.34
- OCDI.CA: score=23.78 buy_ready=True sector_rank=16 price=33.83 support=29.6 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=36.2 liquidity=149763376.0 spike=1.16
- OCPH.CA: score=11.82 buy_ready=False sector_rank=15 price=250.23 support=235.0 resistance=341.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=24.16 liquidity=7175904.5 spike=0.33
- ODIN.CA: score=16.64 buy_ready=False sector_rank=15 price=2.88 support=2.87 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=32.35 liquidity=28735826.0 spike=0.61
- OFH.CA: score=23.64 buy_ready=True sector_rank=15 price=1.04 support=0.79 resistance=1.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=68.71 liquidity=93987120.0 spike=0.85
- OIH.CA: score=26.4 buy_ready=True sector_rank=4 price=2.01 support=1.57 resistance=2.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=63.93 liquidity=61907016.0 spike=0.39
- OLFI.CA: score=13.38 buy_ready=False sector_rank=17 price=22.22 support=22.07 resistance=26.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=19.16 liquidity=29515240.0 spike=0.5
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=856.19 support=831.51 resistance=890.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=408392192.0 spike=1.0
- ORHD.CA: score=23.46 buy_ready=True sector_rank=16 price=42.58 support=40.28 resistance=43.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=41.29 liquidity=110170568.0 spike=0.75
- ORWE.CA: score=24.4 buy_ready=True sector_rank=5 price=26.72 support=24.5 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=56.01 liquidity=17724760.0 spike=0.21
- PHAR.CA: score=16.66 buy_ready=False sector_rank=14 price=128.83 support=124.5 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=25.67 liquidity=175743568.0 spike=0.39
- PHDC.CA: score=13.46 buy_ready=False sector_rank=16 price=14.51 support=14.4 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=31.06 liquidity=118908856.0 spike=0.49
- PHTV.CA: score=7.87 buy_ready=False sector_rank=15 price=351.35 support=311.27 resistance=447.99 source=Yahoo Finance as_of=2026-09-01T21:00:00+00:00 freshness=FRESH RSI=30.24 liquidity=1234292.57 spike=0.63
- POUL.CA: score=25.38 buy_ready=True sector_rank=17 price=39.39 support=36.97 resistance=40.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=48.24 liquidity=17578450.0 spike=0.72
- PRCL.CA: score=20.09 buy_ready=False sector_rank=2 price=31.61 support=30.9 resistance=36.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=46.03 liquidity=8690308.0 spike=0.36
- PRDC.CA: score=21.46 buy_ready=False sector_rank=16 price=8.91 support=8.7 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=54.73 liquidity=62066728.0 spike=0.84
- PRMH.CA: score=25.64 buy_ready=True sector_rank=15 price=2.82 support=2.28 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=53.54 liquidity=10018167.0 spike=0.64
- RACC.CA: score=13.64 buy_ready=False sector_rank=15 price=9.83 support=9.4 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=29.05 liquidity=12585739.0 spike=0.59
- RAKT.CA: score=2.7 buy_ready=False sector_rank=15 price=22.2 support=21.4 resistance=24.0 source=Yahoo Finance as_of=2026-09-01T21:00:00+00:00 freshness=FRESH RSI=34.53 liquidity=59607.0 spike=0.22
- RAYA.CA: score=26.2 buy_ready=False sector_rank=11 price=7.42 support=6.95 resistance=7.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=53.45 liquidity=163227312.0 spike=2.65
- RMDA.CA: score=16.66 buy_ready=False sector_rank=14 price=5.95 support=5.77 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=28.03 liquidity=27821138.0 spike=0.23
- ROTO.CA: score=13.45 buy_ready=False sector_rank=15 price=43.1 support=43.7 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=6.77 liquidity=9812926.0 spike=0.47
- RREI.CA: score=21.64 buy_ready=False sector_rank=15 price=4.37 support=4.24 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=50.34 liquidity=17136002.0 spike=0.47
- RTVC.CA: score=15.66 buy_ready=True sector_rank=15 price=4.04 support=3.76 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=69.61 liquidity=2018162.75 spike=0.25
- RUBX.CA: score=15.11 buy_ready=False sector_rank=15 price=12.57 support=12.2 resistance=13.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=55.62 liquidity=6469570.0 spike=0.36
- SAUD.CA: score=20.22 buy_ready=True sector_rank=10 price=23.52 support=22.13 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=53.23 liquidity=5929547.0 spike=0.28
- SCEM.CA: score=26.4 buy_ready=True sector_rank=2 price=98.62 support=78.3 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=55.33 liquidity=59228796.0 spike=0.26
- SCFM.CA: score=16.27 buy_ready=False sector_rank=15 price=279.18 support=276.05 resistance=305.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=50.64 liquidity=4634482.0 spike=0.31
- SCTS.CA: score=14.25 buy_ready=False sector_rank=13 price=617.65 support=606.01 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=50.06 liquidity=2585167.75 spike=0.29
- SDTI.CA: score=15.98 buy_ready=False sector_rank=15 price=69.52 support=66.66 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=39.42 liquidity=4336931.5 spike=0.17
- SEIG.CA: score=9.06 buy_ready=False sector_rank=15 price=265.52 support=256.01 resistance=293.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=31.18 liquidity=2415571.0 spike=0.46
- SIPC.CA: score=24.1 buy_ready=True sector_rank=15 price=5.24 support=4.1 resistance=5.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=60.54 liquidity=67947856.0 spike=1.23
- SKPC.CA: score=25.28 buy_ready=False sector_rank=3 price=18.8 support=16.29 resistance=19.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=83.95 liquidity=156020272.0 spike=1.44
- SMFR.CA: score=10.06 buy_ready=False sector_rank=15 price=253.39 support=245.0 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=12.2 liquidity=3417539.25 spike=0.13
- SNFC.CA: score=12.64 buy_ready=False sector_rank=15 price=10.5 support=10.26 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=27.66 liquidity=13100781.0 spike=0.88
- SPIN.CA: score=18.16 buy_ready=True sector_rank=5 price=19.32 support=15.32 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=64.88 liquidity=3756243.5 spike=0.09
- SPMD.CA: score=6.73 buy_ready=False sector_rank=15 price=0.44 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=3085075.25 spike=0.17
- SUGR.CA: score=24.16 buy_ready=True sector_rank=17 price=60.25 support=47.45 resistance=61.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=69.69 liquidity=85924376.0 spike=1.39
- SVCE.CA: score=23.42 buy_ready=False sector_rank=15 price=12.77 support=9.2 resistance=13.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=77.27 liquidity=240824768.0 spike=1.39
- SWDY.CA: score=26.32 buy_ready=False sector_rank=8 price=129.58 support=105.5 resistance=133.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=71.96 liquidity=36188484.0 spike=0.33
- TALM.CA: score=20.72 buy_ready=False sector_rank=13 price=18.18 support=17.11 resistance=20.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=39.69 liquidity=9047828.0 spike=0.28
- TMGH.CA: score=18.46 buy_ready=False sector_rank=16 price=96.49 support=94.9 resistance=99.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=41.89 liquidity=110747896.0 spike=0.44
- TRTO.CA: score=0.72 buy_ready=False sector_rank=15 price=0.08 support=0.07 resistance=0.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=43209.16 spike=2.02
- UEFM.CA: score=7.75 buy_ready=False sector_rank=15 price=539.55 support=531.0 resistance=589.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=28.12 liquidity=1113978.75 spike=0.3
- UEGC.CA: score=13.64 buy_ready=False sector_rank=15 price=1.68 support=1.69 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=15.32 liquidity=41236952.0 spike=0.86
- UNIP.CA: score=9.36 buy_ready=False sector_rank=15 price=0.37 support=0.35 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=33.67 liquidity=5723083.0 spike=0.19
- UNIT.CA: score=6.92 buy_ready=False sector_rank=16 price=18.47 support=17.8 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=31.17 liquidity=465591.16 spike=0.04
- WCDF.CA: score=17.05 buy_ready=False sector_rank=15 price=678.75 support=581.01 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT RSI=74.1 liquidity=3408944.0 spike=0.9
- WKOL.CA: score=23.64 buy_ready=True sector_rank=15 price=341.22 support=318.0 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=55.53 liquidity=10333124.0 spike=0.37
- ZEOT.CA: score=17.46 buy_ready=True sector_rank=15 price=14.14 support=12.2 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=57.78 liquidity=3823667.25 spike=0.19
- ZMID.CA: score=22.46 buy_ready=False sector_rank=16 price=9.59 support=7.18 resistance=9.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=78.83 liquidity=135710320.0 spike=0.53

## Backtesting Lite
- ALCN.CA: 180d return=36.36%, max drawdown=-15.82%, MA20>MA50 days last20=20, as_of=2026-09-01T21:00:00+00:00
- EGCH.CA: 180d return=22.01%, max drawdown=-20.07%, MA20>MA50 days last20=17, as_of=2026-09-01T21:00:00+00:00
- FERC.CA: 180d return=1.06%, max drawdown=-15.91%, MA20>MA50 days last20=20, as_of=2026-09-01T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ALCN.CA: status=RECENT_ACCEPTED latest=2026-09-01 age_days=2 sources=3 expected=Alexandria Containers and Cargo Handling summary=Alexandria Containers and Cargo Handling (ALCN.CA) has had several significant developments in the last 12 months. The company reported its financial results for the first half of 2026 on August 17, 2026, and its second-quarter 2026 earnings on August 19, 2026, showing increased EPS, revenue, and net income. ALCN.CA was added to the EGX 30 Index on September 1, 2026. An annual dividend was announced, payable on May 14, 2026. The company also disclosed its financial statements for the transitional period from July 1, 2025, to December 31, 2025, on March 18, 2026. In late 2025, AD Ports proposed to acquire a majority stake, though Egypt later declined a bid to increase the stake.
  - Alexandria Containers and goods (ALCN.CA) Reports its Financial Results for the Period from 01/01/2026 to 30/06/2026 (August 17, 2026): https://fouda.lens.com/company/ALCN/disclosures/2026-08-17-financial-statements-8-1-mb
  - Alexandria Container&Cargo Handling Company(CASE:ALCN) added to EGX 30 Index (September 1, 2026): https://www.marketscreener.com/quote/stock/ALEXANDRIA-CONTAINER-CARGO-1000002/news/Alexandria-Container-Cargo-Handling-Company-CASE-ALCN-added-to-EGX-30-Index-44709292/
  - Alexandria Container&Cargo Handling Company announces Annual dividend, payable on May 14, 2026 (April 28, 2026): https://simplywall.st/stocks/eg/transportation/egx-alcn/alexandria-container-cargo-handling#latest-news
- EGCH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Chemical Industries Kima summary=Evidence rejected for EGCH.CA: source text did not clearly match EGCH.CA / Egyptian Chemical Industries Kima.
- FERC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=610 sources=3 expected=Ferchem Misr Fertilizers and Chemicals summary=Ferchem Misr’s board greenlights EGP 500m dividends for 2025; Ferchem Misr’s profits soar 4,238% in 2025; Ferchem Misr’s profit leaps 75% in 9M Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Ferchem Misr’s board greenlights EGP 500m dividends for 2025: https://english.mubasher.info/news/4600298/Ferchem-Misr-s-board-greenlights-EGP-500m-dividends-for-2025/
  - Ferchem Misr’s profits soar 4,238% in 2025: https://english.mubasher.info/news/4564349/Ferchem-Misr-s-profits-soar-4-238-in-2025/
  - Ferchem Misr’s profit leaps 75% in 9M: https://english.mubasher.info/news/3560738/Ferchem-Misr-s-profit-leaps-75-in-9M/
- MBSC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=610 sources=3 expected=Misr Beni Suef Cement summary=Misr Beni Suef’s consolidated net profits near EGP 4bn in 2025; Misr Beni Suef’s consolidated net profits hit EGP 953m in H1-25; Misr Beni Suef Cement’s consolidate profits fall to EGP 574m in Q1-25 Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Misr Beni Suef’s consolidated net profits near EGP 4bn in 2025: https://english.mubasher.info/news/4599415/Misr-Beni-Suef-s-consolidated-net-profits-near-EGP-4bn-in-2025/
  - Misr Beni Suef’s consolidated net profits hit EGP 953m in H1-25: https://english.mubasher.info/news/4488249/Misr-Beni-Suef-s-consolidated-net-profits-hit-EGP-953m-in-H1-25/
  - Misr Beni Suef Cement’s consolidate profits fall to EGP 574m in Q1-25: https://english.mubasher.info/news/4455784/Misr-Beni-Suef-Cement-s-consolidate-profits-fall-to-EGP-574m-in-Q1-25/
- ARCC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=610 sources=3 expected=Arabian Cement Company summary=Arabian Cement to pay out EGP 2bn dividends for 2025; Arabian Cement’s EGM approves nearly EGP 8m capital cut; Arabian Cement’s consolidated profits near EGP 3.6bn in 2025 Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Arabian Cement to pay out EGP 2bn dividends for 2025: https://english.mubasher.info/news/4587912/Arabian-Cement-to-pay-out-EGP-2bn-dividends-for-2025/
  - Arabian Cement’s EGM approves nearly EGP 8m capital cut: https://english.mubasher.info/news/4583762/Arabian-Cement-s-EGM-approves-nearly-EGP-8m-capital-cut/
  - Arabian Cement’s consolidated profits near EGP 3.6bn in 2025: https://english.mubasher.info/news/4562679/Arabian-Cement-s-consolidated-profits-near-EGP-3-6bn-in-2025/
- ETRS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Transport and Commercial Services Company S.A.E. summary=Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- MASR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=610 sources=3 expected=Madinet Masr For Housing and Development summary=Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval; Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended; Madinet Masr to distribute treasury stocks in first-ever move Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval: https://english.mubasher.info/news/4601386/Madinet-Masr-to-pay-out-EGP-0-15-shr-for-2025-upon-equityholders-approval/
  - Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended: https://english.mubasher.info/news/4578449/Madinet-Masr-logs-24-higher-consolidated-profits-in-2025-dividends-recommended/
  - Madinet Masr to distribute treasury stocks in first-ever move: https://english.mubasher.info/news/4577724/Madinet-Masr-to-distribute-treasury-stocks-in-first-ever-move/
- ISMQ.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Iron and Steel for Mines and Quarries summary=Iron and Steel for Mines and Quarries stock stabilizes above key support after correction; Will Iron and Steel for Mines and Quarries stock hit new historical peaks?; Iron and Steel for Mines and Quarries expects EGP 448m net profit in FY24/25 Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Iron and Steel for Mines and Quarries stock stabilizes above key support after correction: https://english.mubasher.info/news/4578786/Iron-and-Steel-for-Mines-and-Quarries-stock-stabilizes-above-key-support-after-correction/
  - Will Iron and Steel for Mines and Quarries stock hit new historical peaks?: https://english.mubasher.info/news/4556956/Will-Iron-and-Steel-for-Mines-and-Quarries-stock-hit-new-historical-peaks-/
  - Iron and Steel for Mines and Quarries expects EGP 448m net profit in FY24/25: https://english.mubasher.info/news/4249734/Iron-and-Steel-for-Mines-and-Quarries-expects-EGP-448m-net-profit-in-FY24-25/

## Warnings
- Evidence rejected for EGCH.CA: source text did not clearly match EGCH.CA / Egyptian Chemical Industries Kima.
- Evidence for FERC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for MBSC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ARCC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- Evidence for MASR.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ISMQ.CA matches the company but no source/report date was detected.
