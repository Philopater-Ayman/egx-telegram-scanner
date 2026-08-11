# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-08-11T07:36:42.137416+00:00
Generated Cairo: 2026-08-11 10:36
Run timing: target 09:15 Cairo | generated Cairo 2026-08-11 10:36 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-08-11 10:32

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 30
- Data quality issues: 1
- Tradeable price/liquidity tickers: 129/189
- Top sector: Automotive & Distribution

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, August 11
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 75.0% / above MA50 70.0%
- EGX70 regime: BULLISH / above MA20 71.43% / above MA50 89.29%
- Sector breadth: 47.62%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- PHAR.CA: liquidity=165082000.0 spike=0.61 score=8.02
- ISPH.CA: liquidity=126096232.0 spike=0.83 score=8.02
- RMDA.CA: liquidity=53427236.0 spike=0.56 score=8.02
- BIOC.CA: liquidity=41988060.0 spike=0.25 score=8.01
- NIPH.CA: liquidity=40915136.0 spike=0.19 score=8.02

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner prioritized EFIH.CA, AMOC.CA, and COMI.CA as watch/buy setups because each trades above its MA20/MA50, shows RSI in the bullish zone, has liquidity above the threshold, and offers clear support/resistance bands for the next 1‑3 days, despite cooling liquidity and extended momentum; EGX30 and EGX70 remain bullish but the risk mode is SELECTIVE_SWING_TRADES_ONLY, introducing uncertainty.
- EFIH.CA: price 23.7 > MA20/MA50, RSI 62.6, support 21.87 / resistance 25.0, outlook BULLISH_WATCH (73.9), liquidity cooling.
- AMOC.CA: price 9.35 > MA20/MA50, RSI 65.3, support 7.95 / resistance 9.77, outlook CONSTRUCTIVE (63.7), liquidity cooling.

## Top Liquidity Spikes
- ECAP.CA: spike=3.8 liquidity=23084678.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- FAITA.CA: spike=2.52 liquidity=105498.45 outlook=NEUTRAL score=42.56 buy_ready=False
- DAPH.CA: spike=1.53 liquidity=38765604.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EGBE.CA: spike=1.44 liquidity=166615.3 outlook=WEAK_OR_RISKY score=14.56 buy_ready=False
- EGSA.CA: spike=1.38 liquidity=29978.24 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=10.83 5d=7.65% 20d=8.35% aboveMA50=100.0%
- #2 Industrial Goods & Cables: score=9.61 5d=6.27% 20d=11.77% aboveMA50=100.0%
- #3 Textiles: score=7.91 5d=2.73% 20d=11.29% aboveMA50=75.0%
- #4 Energy & Petrochemicals: score=7.7 5d=-0.93% 20d=17.59% aboveMA50=75.0%
- #5 Food, Beverages & Tobacco: score=7.67 5d=7.42% 20d=1.79% aboveMA50=71.43%
- #6 Banking & Financials: score=6.56 5d=1.48% 20d=3.92% aboveMA50=80.0%
- #7 Fintech & Payments: score=5.94 5d=1.88% 20d=2.62% aboveMA50=100.0%
- #8 Non-bank Financial Services: score=5.92 5d=2.46% 20d=3.59% aboveMA50=80.0%

## Today's Prioritized Action Tickets
- Priority #1: BUY EFIH.CA
  - Entry: 23.7 | Take profit: 25.6 | Stop loss: 22.75
  - Confidence: LOW | score=26.38 | outlook=BULLISH_WATCH 73.94
  - Reason: WATCH/BUY SETUP: EFIH.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 62.61, support 21.87, resistance 25.0, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY AMOC.CA
  - Entry: 9.35 | Take profit: 10.09 | Stop loss: 8.98
  - Confidence: LOW | score=24.4 | outlook=CONSTRUCTIVE 63.7
  - Reason: WATCH/BUY SETUP: AMOC.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 65.29, support 7.95, resistance 9.77, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY COMI.CA
  - Entry: 139.57 | Take profit: 147.17 | Stop loss: 135.77
  - Confidence: LOW | score=22.4 | outlook=CONSTRUCTIVE 68.56
  - Reason: WATCH/BUY SETUP: COMI.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 69.99, support 132.81, resistance 142.88, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- POUL.CA: BULLISH_WATCH score=77.67 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- EGTS.CA: BULLISH_WATCH score=75.27 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- GBCO.CA: BULLISH_WATCH score=74 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; overheated RSI
- EFIH.CA: BULLISH_WATCH score=73.94 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended
- CERA.CA: BULLISH_WATCH score=73.52 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- SUGR.CA: BULLISH_WATCH score=71.67 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; close to resistance
- OLFI.CA: CONSTRUCTIVE score=69.67 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; overheated RSI
- ARAB.CA: CONSTRUCTIVE score=69.27 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- ISMQ.CA: CONSTRUCTIVE score=68.72 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- COMI.CA: CONSTRUCTIVE score=68.56 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended

## BUY-Ready Candidates
- EFIH.CA: rank=26.38 outlook=BULLISH_WATCH outlook_score=73.94 sector_rank=7 price=23.7 support=21.87 resistance=25.0 liquidity=13387287.0
- AMOC.CA: rank=24.4 outlook=CONSTRUCTIVE outlook_score=63.7 sector_rank=4 price=9.35 support=7.95 resistance=9.77 liquidity=12639141.0
- COMI.CA: rank=22.4 outlook=CONSTRUCTIVE outlook_score=68.56 sector_rank=6 price=139.57 support=132.81 resistance=142.88 liquidity=37353504.0
- PHDC.CA: rank=21.1 outlook=CONSTRUCTIVE outlook_score=55.27 sector_rank=11 price=15.48 support=14.32 resistance=15.73 liquidity=7391906.5
- EGCH.CA: rank=20.01 outlook=CONSTRUCTIVE outlook_score=60.72 sector_rank=15 price=14.19 support=12.69 resistance=14.62 liquidity=4524680.0
- SUGR.CA: rank=19.25 outlook=BULLISH_WATCH outlook_score=71.67 sector_rank=5 price=49.14 support=46.47 resistance=49.25 liquidity=2853928.5
- GBCO.CA: rank=19.12 outlook=BULLISH_WATCH outlook_score=74 sector_rank=1 price=31.82 support=29.53 resistance=34.2 liquidity=1719252.25
- ARAB.CA: rank=19.11 outlook=CONSTRUCTIVE outlook_score=69.27 sector_rank=11 price=0.25 support=0.23 resistance=0.26 liquidity=5402483.5
- SPMD.CA: rank=19.02 outlook=CONSTRUCTIVE outlook_score=61.52 sector_rank=18 price=0.5 support=0.44 resistance=0.5 liquidity=4009601.5
- CLHO.CA: rank=18.59 outlook=CONSTRUCTIVE outlook_score=67.56 sector_rank=17 price=17.9 support=15.98 resistance=19.72 liquidity=3562377.5

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=15.55 buy_ready=True sector_rank=18 price=290.08 support=223.25 resistance=317.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=69.22 liquidity=2537800.5 spike=0.07
- ABUK.CA: score=22.49 buy_ready=False sector_rank=15 price=73.59 support=69.01 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=48.32 liquidity=11737138.0 spike=0.08
- ACAMD.CA: score=10.9 buy_ready=False sector_rank=18 price=2.27 support=2.28 resistance=2.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=3895388.25 spike=1.0
- ACGC.CA: score=16.41 buy_ready=False sector_rank=3 price=11.2 support=9.55 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=78.1 liquidity=2010104.5 spike=0.06
- ADCI.CA: score=8.01 buy_ready=False sector_rank=18 price=375.31 support=331.5 resistance=387.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:08 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11179983.0 spike=0.59
- ADIB.CA: score=15.18 buy_ready=False sector_rank=6 price=53.68 support=46.02 resistance=53.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=83.57 liquidity=3780541.5 spike=0.03
- ADPC.CA: score=0.74 buy_ready=False sector_rank=18 price=4.53 support=4.46 resistance=4.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2736487.25 spike=0.06
- AFDI.CA: score=-1.34 buy_ready=False sector_rank=18 price=64.49 support=64.2 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=647921.5 spike=0.03
- AFMC.CA: score=16.23 buy_ready=False sector_rank=18 price=218.04 support=72.0 resistance=250.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=75.31 liquidity=6217637.0 spike=0.04
- AJWA.CA: score=13.01 buy_ready=False sector_rank=18 price=188.12 support=161.0 resistance=210.0 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=63.87 liquidity=0.0 spike=0.0
- ALCN.CA: score=17.93 buy_ready=True sector_rank=12 price=31.11 support=28.8 resistance=31.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=62.2 liquidity=2243000.5 spike=0.08
- ALUM.CA: score=0.87 buy_ready=False sector_rank=18 price=25.69 support=25.5 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2858795.75 spike=0.39
- AMER.CA: score=8.71 buy_ready=False sector_rank=11 price=7.14 support=6.49 resistance=7.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:10 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21140316.0 spike=0.18
- AMES.CA: score=8.01 buy_ready=False sector_rank=18 price=128.96 support=121.34 resistance=129.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11982148.0 spike=0.12
- AMIA.CA: score=10.37 buy_ready=False sector_rank=18 price=12.72 support=8.74 resistance=13.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=78.49 liquidity=361995.38 spike=0.02
- AMOC.CA: score=24.4 buy_ready=True sector_rank=4 price=9.35 support=7.95 resistance=9.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=65.29 liquidity=12639141.0 spike=0.13
- APSW.CA: score=12.01 buy_ready=False sector_rank=18 price=8.83 support=8.1 resistance=9.34 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=49.76 liquidity=0.0 spike=0.0
- ARAB.CA: score=19.11 buy_ready=True sector_rank=11 price=0.25 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=5402483.5 spike=0.04
- ARCC.CA: score=3.95 buy_ready=False sector_rank=19 price=64.99 support=63.7 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6267027.0 spike=0.18
- AREH.CA: score=12.07 buy_ready=False sector_rank=18 price=1.53 support=1.38 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=54.9 liquidity=2058483.38 spike=0.05
- ARVA.CA: score=4.01 buy_ready=False sector_rank=18 price=12.35 support=12.35 resistance=12.35 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=88.83 liquidity=0.0 spike=0.0
- ASCM.CA: score=20.26 buy_ready=False sector_rank=18 price=68.04 support=58.16 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=70.12 liquidity=7255617.0 spike=0.11
- ASPI.CA: score=0.13 buy_ready=False sector_rank=18 price=0.5 support=0.49 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2121163.75 spike=0.05
- ATLC.CA: score=2.41 buy_ready=False sector_rank=8 price=5.53 support=5.49 resistance=5.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3039039.0 spike=0.21
- ATQA.CA: score=8.49 buy_ready=False sector_rank=15 price=10.97 support=10.8 resistance=10.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32123872.0 spike=0.82
- AXPH.CA: score=1.05 buy_ready=False sector_rank=18 price=1403.02 support=1325.0 resistance=1419.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3046227.5 spike=0.75
- BINV.CA: score=16.34 buy_ready=False sector_rank=9 price=49.5 support=46.01 resistance=50.9 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=52.9 liquidity=0.0 spike=0.0
- BIOC.CA: score=8.01 buy_ready=False sector_rank=18 price=572.03 support=525.0 resistance=572.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:05 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=41988060.0 spike=0.25
- BTFH.CA: score=20.3 buy_ready=False sector_rank=8 price=3.1 support=3.03 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=48.84 liquidity=5929635.0 spike=0.03
- CAED.CA: score=14.1 buy_ready=True sector_rank=18 price=120.59 support=73.25 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=39.52 liquidity=1090242.5 spike=0.02
- CANA.CA: score=15.92 buy_ready=False sector_rank=6 price=40.16 support=35.2 resistance=39.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=74.85 liquidity=1524230.13 spike=0.08
- CCAP.CA: score=19.34 buy_ready=False sector_rank=9 price=5.19 support=5.14 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=38.46 liquidity=15438269.0 spike=0.02
- CCRS.CA: score=3.01 buy_ready=False sector_rank=18 price=2.45 support=2.35 resistance=2.76 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=34.69 liquidity=0.0 spike=0.0
- CEFM.CA: score=15.61 buy_ready=False sector_rank=18 price=133.1 support=101.57 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=55.81 liquidity=598972.0 spike=0.02
- CERA.CA: score=17.34 buy_ready=True sector_rank=18 price=1.35 support=1.25 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=43.48 liquidity=4334945.5 spike=0.19
- CFGH.CA: score=7.01 buy_ready=False sector_rank=18 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- CICH.CA: score=11.37 buy_ready=False sector_rank=8 price=12.91 support=11.61 resistance=13.25 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=78.91 liquidity=0.0 spike=0.0
- CIEB.CA: score=18.4 buy_ready=False sector_rank=6 price=24.5 support=23.75 resistance=24.7 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=59.64 liquidity=0.0 spike=0.0
- CIRA.CA: score=-0.57 buy_ready=False sector_rank=16 price=39.0 support=38.7 resistance=39.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:09 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1323532.13 spike=0.02
- CLHO.CA: score=18.59 buy_ready=True sector_rank=17 price=17.9 support=15.98 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=60.09 liquidity=3562377.5 spike=0.07
- CNFN.CA: score=18.37 buy_ready=False sector_rank=8 price=5.0 support=4.68 resistance=5.05 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=61.7 liquidity=0.0 spike=0.0
- COMI.CA: score=22.4 buy_ready=True sector_rank=6 price=139.57 support=132.81 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=69.99 liquidity=37353504.0 spike=0.09
- COPR.CA: score=14.31 buy_ready=True sector_rank=18 price=0.41 support=0.36 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=62.86 liquidity=1305926.75 spike=0.04
- COSG.CA: score=17.44 buy_ready=True sector_rank=18 price=1.72 support=1.6 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=51.52 liquidity=4431346.0 spike=0.11
- CPCI.CA: score=8.01 buy_ready=False sector_rank=18 price=639.35 support=570.0 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:08 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10626972.0 spike=0.79
- CSAG.CA: score=3.93 buy_ready=False sector_rank=12 price=40.0 support=39.8 resistance=40.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5243080.5 spike=0.25
- DAPH.CA: score=9.07 buy_ready=False sector_rank=18 price=137.02 support=135.0 resistance=142.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=38765604.0 spike=1.53
- DEIN.CA: score=-1.99 buy_ready=False sector_rank=18 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=14.4 buy_ready=False sector_rank=5 price=28.95 support=26.01 resistance=32.0 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=70.35 liquidity=0.0 spike=0.0
- DSCW.CA: score=17.16 buy_ready=False sector_rank=18 price=2.13 support=1.77 resistance=2.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=2156920.75 spike=0.03
- DTPP.CA: score=8.01 buy_ready=False sector_rank=18 price=318.18 support=300.0 resistance=318.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:05 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30773396.0 spike=0.52
- EALR.CA: score=15.88 buy_ready=False sector_rank=18 price=379.81 support=360.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=55.73 liquidity=872890.13 spike=0.03
- EASB.CA: score=11.01 buy_ready=False sector_rank=18 price=7.15 support=6.71 resistance=8.52 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=48.88 liquidity=0.0 spike=0.0
- EAST.CA: score=10.98 buy_ready=False sector_rank=5 price=36.48 support=36.01 resistance=37.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=48.86 liquidity=580435.88 spike=0.01
- EBSC.CA: score=13.63 buy_ready=False sector_rank=18 price=1.91 support=1.85 resistance=2.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:09 AM market time freshness=DELAYED_CURRENT RSI=72.0 liquidity=623329.75 spike=0.1
- ECAP.CA: score=13.01 buy_ready=False sector_rank=18 price=41.68 support=38.11 resistance=41.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:09 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23084678.0 spike=3.8
- EDFM.CA: score=13.01 buy_ready=False sector_rank=18 price=395.38 support=337.96 resistance=430.0 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=48.98 liquidity=0.0 spike=0.0
- EEII.CA: score=5.24 buy_ready=False sector_rank=18 price=3.05 support=3.03 resistance=3.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7236032.5 spike=0.51
- EFIC.CA: score=16.23 buy_ready=False sector_rank=15 price=211.43 support=181.69 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=69.15 liquidity=740926.19 spike=0.03
- EFID.CA: score=16.76 buy_ready=False sector_rank=5 price=31.2 support=26.64 resistance=32.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=83.88 liquidity=3364343.25 spike=0.04
- EFIH.CA: score=26.38 buy_ready=True sector_rank=7 price=23.7 support=21.87 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=62.61 liquidity=13387287.0 spike=0.15
- EGAL.CA: score=15.88 buy_ready=False sector_rank=15 price=304.87 support=290.0 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=31.1 liquidity=5395823.0 spike=0.13
- EGAS.CA: score=13.51 buy_ready=False sector_rank=4 price=59.98 support=48.95 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:10 AM market time freshness=DELAYED_CURRENT RSI=75.45 liquidity=2109779.5 spike=0.08
- EGBE.CA: score=12.45 buy_ready=False sector_rank=6 price=0.56 support=-0.34 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 August 01:07 PM market time freshness=DELAYED_CURRENT RSI=81.06 liquidity=166615.3 spike=1.44
- EGCH.CA: score=20.01 buy_ready=True sector_rank=15 price=14.19 support=12.69 resistance=14.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=63.0 liquidity=4524680.0 spike=0.04
- EGSA.CA: score=4.45 buy_ready=False sector_rank=13 price=8.69 support=8.8 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 August 01:13 PM market time freshness=DELAYED_CURRENT RSI=31.58 liquidity=29978.24 spike=1.38
- EGTS.CA: score=17.21 buy_ready=True sector_rank=11 price=18.46 support=17.11 resistance=19.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=54.09 liquidity=1497163.38 spike=0.04
- EHDR.CA: score=3.34 buy_ready=False sector_rank=18 price=2.99 support=2.94 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5327982.0 spike=0.13
- EKHO.CA: score=8.4 buy_ready=False sector_rank=4 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=15.48 buy_ready=False sector_rank=2 price=2.18 support=2.1 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=26.32 liquidity=7080263.5 spike=0.09
- ELKA.CA: score=11.07 buy_ready=False sector_rank=18 price=1.71 support=1.59 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=15.87 liquidity=5061413.5 spike=0.06
- ELNA.CA: score=7.01 buy_ready=False sector_rank=18 price=37.44 support=36.5 resistance=40.5 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=41.89 liquidity=0.0 spike=0.0
- ELSH.CA: score=12.48 buy_ready=False sector_rank=18 price=14.05 support=13.31 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=48.8 liquidity=1468131.5 spike=0.01
- ELWA.CA: score=3.01 buy_ready=False sector_rank=18 price=1.69 support=1.65 resistance=2.14 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=8.33 liquidity=0.0 spike=0.0
- EMFD.CA: score=15.03 buy_ready=False sector_rank=11 price=11.73 support=11.08 resistance=12.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:10 AM market time freshness=DELAYED_CURRENT RSI=55.15 liquidity=2317562.5 spike=0.04
- ENGC.CA: score=14.0 buy_ready=False sector_rank=18 price=46.29 support=38.15 resistance=47.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=65.31 liquidity=994863.06 spike=0.03
- EOSB.CA: score=17.01 buy_ready=False sector_rank=18 price=1.55 support=1.52 resistance=1.62 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- EPCO.CA: score=0.89 buy_ready=False sector_rank=18 price=12.85 support=12.7 resistance=12.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2878471.0 spike=0.09
- EPPK.CA: score=11.01 buy_ready=False sector_rank=18 price=13.93 support=13.87 resistance=15.93 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=35.9 liquidity=0.0 spike=0.0
- ETEL.CA: score=16.53 buy_ready=True sector_rank=13 price=108.45 support=96.0 resistance=114.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=65.27 liquidity=2874327.5 spike=0.03
- ETRS.CA: score=13.79 buy_ready=False sector_rank=18 price=10.72 support=10.21 resistance=10.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=54.26 liquidity=786755.75 spike=0.03
- EXPA.CA: score=14.74 buy_ready=False sector_rank=6 price=20.51 support=18.61 resistance=20.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=73.74 liquidity=339296.75 spike=0.01
- FAIT.CA: score=18.4 buy_ready=False sector_rank=6 price=38.36 support=36.1 resistance=38.37 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=62.76 liquidity=0.0 spike=0.0
- FAITA.CA: score=16.55 buy_ready=False sector_rank=6 price=0.98 support=0.96 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=105498.45 spike=2.52
- FERC.CA: score=4.02 buy_ready=False sector_rank=15 price=87.0 support=84.72 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5536683.0 spike=0.39
- FWRY.CA: score=21.11 buy_ready=False sector_rank=7 price=19.09 support=18.43 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=56.89 liquidity=6729125.5 spike=0.06
- GBCO.CA: score=19.12 buy_ready=True sector_rank=1 price=31.82 support=29.53 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=38.48 liquidity=1719252.25 spike=0.03
- GDWA.CA: score=8.58 buy_ready=False sector_rank=18 price=0.81 support=0.78 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=41.27 liquidity=1568068.5 spike=0.01
- GGCC.CA: score=3.1 buy_ready=False sector_rank=18 price=1.22 support=1.17 resistance=1.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5096574.0 spike=0.11
- GIHD.CA: score=6.22 buy_ready=False sector_rank=18 price=68.89 support=68.4 resistance=70.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8213357.0 spike=0.15
- GMCI.CA: score=11.01 buy_ready=False sector_rank=18 price=1.98 support=1.91 resistance=2.2 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=37.25 liquidity=0.0 spike=0.0
- GRCA.CA: score=13.97 buy_ready=False sector_rank=18 price=58.72 support=48.0 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=40.29 liquidity=963401.63 spike=0.05
- GSSC.CA: score=15.72 buy_ready=False sector_rank=18 price=276.13 support=257.0 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=53.41 liquidity=715625.94 spike=0.04
- GTWL.CA: score=8.01 buy_ready=False sector_rank=18 price=125.36 support=125.03 resistance=132.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22810482.0 spike=0.23
- HDBK.CA: score=9.98 buy_ready=False sector_rank=6 price=85.28 support=76.9 resistance=85.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:10 AM market time freshness=DELAYED_CURRENT RSI=80.83 liquidity=575889.44 spike=0.02
- HELI.CA: score=14.67 buy_ready=False sector_rank=11 price=8.44 support=7.24 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=58.78 liquidity=966228.38 spike=0.0
- HRHO.CA: score=17.32 buy_ready=False sector_rank=8 price=27.29 support=25.95 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=60.26 liquidity=954119.63 spike=0.01
- ICID.CA: score=-1.39 buy_ready=False sector_rank=18 price=9.08 support=9.0 resistance=9.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=601583.25 spike=0.08
- IDRE.CA: score=-0.32 buy_ready=False sector_rank=18 price=56.05 support=55.9 resistance=57.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1676780.63 spike=0.05
- IFAP.CA: score=13.1 buy_ready=False sector_rank=10 price=21.63 support=18.96 resistance=21.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=76.22 liquidity=2094024.13 spike=0.11
- INFI.CA: score=8.01 buy_ready=False sector_rank=18 price=167.81 support=167.0 resistance=178.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19303392.0 spike=0.45
- IRON.CA: score=10.74 buy_ready=False sector_rank=15 price=31.4 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=61.84 liquidity=1253364.0 spike=0.16
- ISMA.CA: score=4.17 buy_ready=False sector_rank=18 price=33.13 support=33.0 resistance=33.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6160688.0 spike=0.26
- ISMQ.CA: score=17.34 buy_ready=True sector_rank=15 price=9.49 support=8.96 resistance=9.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=46.27 liquidity=3855583.5 spike=0.06
- ISPH.CA: score=8.02 buy_ready=False sector_rank=17 price=15.7 support=14.62 resistance=15.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=126096232.0 spike=0.83
- JUFO.CA: score=13.12 buy_ready=False sector_rank=5 price=26.59 support=22.78 resistance=36.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=44.64 liquidity=2720380.5 spike=0.05
- KABO.CA: score=1.62 buy_ready=False sector_rank=3 price=8.56 support=8.47 resistance=8.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1224969.75 spike=0.03
- KWIN.CA: score=-0.11 buy_ready=False sector_rank=18 price=94.15 support=93.7 resistance=95.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1884339.88 spike=0.03
- KZPC.CA: score=9.01 buy_ready=False sector_rank=18 price=8.91 support=8.4 resistance=9.1 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=65.98 liquidity=0.0 spike=0.0
- LCSW.CA: score=14.58 buy_ready=True sector_rank=19 price=34.14 support=30.2 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=45.37 liquidity=1893113.63 spike=0.04
- LUTS.CA: score=4.24 buy_ready=False sector_rank=18 price=0.83 support=0.82 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6227702.5 spike=0.14
- MAAL.CA: score=15.61 buy_ready=True sector_rank=18 price=8.71 support=8.1 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=59.52 liquidity=2597433.25 spike=0.18
- MASR.CA: score=16.01 buy_ready=False sector_rank=18 price=7.64 support=7.7 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=28.4 liquidity=11770970.0 spike=0.16
- MBSC.CA: score=7.68 buy_ready=False sector_rank=19 price=271.99 support=265.51 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10439055.0 spike=0.5
- MCQE.CA: score=7.68 buy_ready=False sector_rank=19 price=212.69 support=201.0 resistance=214.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19544324.0 spike=0.97
- MCRO.CA: score=8.01 buy_ready=False sector_rank=18 price=1.65 support=1.63 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18790812.0 spike=0.11
- MENA.CA: score=11.71 buy_ready=False sector_rank=11 price=6.92 support=6.83 resistance=7.28 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=36.0 liquidity=0.0 spike=0.0
- MEPA.CA: score=8.01 buy_ready=False sector_rank=18 price=1.99 support=1.97 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11058129.0 spike=0.18
- MFPC.CA: score=11.17 buy_ready=False sector_rank=15 price=37.01 support=35.37 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=34.32 liquidity=5679368.0 spike=0.07
- MFSC.CA: score=15.47 buy_ready=False sector_rank=18 price=49.38 support=45.05 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=61.81 liquidity=465649.38 spike=0.04
- MHOT.CA: score=12.72 buy_ready=False sector_rank=14 price=17.46 support=16.2 resistance=17.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=60.21 liquidity=1171373.88 spike=0.13
- MICH.CA: score=11.21 buy_ready=False sector_rank=18 price=48.88 support=37.46 resistance=53.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=83.87 liquidity=1197378.75 spike=0.04
- MILS.CA: score=16.37 buy_ready=True sector_rank=18 price=186.59 support=134.03 resistance=211.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=59.54 liquidity=1363031.5 spike=0.02
- MIPH.CA: score=15.95 buy_ready=False sector_rank=17 price=803.69 support=690.01 resistance=831.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=55.67 liquidity=928725.44 spike=0.19
- MOED.CA: score=3.42 buy_ready=False sector_rank=18 price=0.68 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=19.44 liquidity=1416158.5 spike=0.05
- MOIL.CA: score=11.4 buy_ready=False sector_rank=4 price=0.68 support=0.51 resistance=0.69 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=92.52 liquidity=0.0 spike=0.0
- MOIN.CA: score=13.93 buy_ready=False sector_rank=18 price=36.23 support=23.03 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=97.0 liquidity=1918960.38 spike=0.09
- MOSC.CA: score=-0.56 buy_ready=False sector_rank=18 price=312.9 support=308.0 resistance=314.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1430839.5 spike=0.09
- MPCI.CA: score=8.01 buy_ready=False sector_rank=18 price=457.35 support=410.0 resistance=460.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29225642.0 spike=0.24
- MPCO.CA: score=9.0 buy_ready=False sector_rank=10 price=2.11 support=2.1 resistance=2.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11847054.0 spike=0.13
- MPRC.CA: score=14.09 buy_ready=True sector_rank=18 price=46.86 support=41.0 resistance=47.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=61.5 liquidity=1086670.0 spike=0.04
- MTIE.CA: score=20.12 buy_ready=False sector_rank=1 price=11.31 support=9.3 resistance=11.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=86.45 liquidity=3720581.75 spike=0.1
- NAHO.CA: score=9.01 buy_ready=False sector_rank=18 price=0.1 support=0.1 resistance=0.1 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=0.0 spike=0.0
- NCCW.CA: score=0.37 buy_ready=False sector_rank=18 price=5.97 support=5.96 resistance=6.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2358233.75 spike=0.07
- NEDA.CA: score=3.01 buy_ready=False sector_rank=18 price=2.7 support=2.7 resistance=3.02 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=13.04 liquidity=0.0 spike=0.0
- NHPS.CA: score=8.01 buy_ready=False sector_rank=18 price=97.6 support=97.01 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15342395.0 spike=0.19
- NINH.CA: score=17.15 buy_ready=True sector_rank=18 price=23.53 support=17.52 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=50.84 liquidity=2145386.75 spike=0.04
- NIPH.CA: score=8.02 buy_ready=False sector_rank=17 price=489.86 support=430.8 resistance=516.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40915136.0 spike=0.19
- OBRI.CA: score=2.27 buy_ready=False sector_rank=18 price=33.63 support=33.61 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4258168.0 spike=0.12
- OCDI.CA: score=25.14 buy_ready=False sector_rank=11 price=31.59 support=26.2 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=71.17 liquidity=9432550.0 spike=0.09
- OCPH.CA: score=8.01 buy_ready=False sector_rank=18 price=331.9 support=301.02 resistance=339.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12973179.0 spike=0.43
- ODIN.CA: score=8.01 buy_ready=False sector_rank=18 price=3.66 support=3.3 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16351734.0 spike=0.75
- OFH.CA: score=14.72 buy_ready=False sector_rank=18 price=0.87 support=0.62 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=76.65 liquidity=2715706.5 spike=0.03
- OIH.CA: score=14.15 buy_ready=False sector_rank=9 price=1.63 support=1.41 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=84.85 liquidity=814074.62 spike=0.01
- OLFI.CA: score=15.08 buy_ready=False sector_rank=5 price=24.42 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=78.84 liquidity=1675044.75 spike=0.04
- ORAS.CA: score=6.62 buy_ready=False sector_rank=20 price=717.38 support=716.5 resistance=723.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9023469.0 spike=1.0
- ORHD.CA: score=21.21 buy_ready=False sector_rank=11 price=42.64 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=74.79 liquidity=5503940.0 spike=0.03
- ORWE.CA: score=15.37 buy_ready=False sector_rank=3 price=26.14 support=22.42 resistance=27.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=78.06 liquidity=2974297.0 spike=0.05
- PHAR.CA: score=8.02 buy_ready=False sector_rank=17 price=176.53 support=165.27 resistance=176.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:06 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=165082000.0 spike=0.61
- PHDC.CA: score=21.1 buy_ready=True sector_rank=11 price=15.48 support=14.32 resistance=15.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=67.45 liquidity=7391906.5 spike=0.03
- PHTV.CA: score=0.27 buy_ready=False sector_rank=18 price=429.08 support=382.49 resistance=447.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:10 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2262216.0 spike=0.58
- POUL.CA: score=17.57 buy_ready=True sector_rank=5 price=39.8 support=36.5 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=45.76 liquidity=3173491.25 spike=0.1
- PRCL.CA: score=11.51 buy_ready=False sector_rank=19 price=35.01 support=32.76 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=38.12 liquidity=824604.31 spike=0.02
- PRDC.CA: score=12.58 buy_ready=False sector_rank=11 price=9.3 support=8.2 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=35.13 liquidity=868786.69 spike=0.01
- PRMH.CA: score=15.37 buy_ready=False sector_rank=18 price=2.78 support=2.56 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:10 AM market time freshness=DELAYED_CURRENT RSI=53.19 liquidity=358921.75 spike=0.02
- RACC.CA: score=11.49 buy_ready=False sector_rank=18 price=10.12 support=9.8 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=50.88 liquidity=480067.56 spike=0.02
- RAKT.CA: score=9.01 buy_ready=False sector_rank=18 price=22.96 support=21.25 resistance=23.5 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=89.22 liquidity=0.0 spike=0.0
- RAYA.CA: score=11.74 buy_ready=False sector_rank=21 price=7.32 support=7.3 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=39.37 liquidity=5541751.0 spike=0.05
- RMDA.CA: score=8.02 buy_ready=False sector_rank=17 price=7.24 support=6.94 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=53427236.0 spike=0.56
- ROTO.CA: score=0.41 buy_ready=False sector_rank=18 price=49.08 support=49.01 resistance=49.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2403941.5 spike=0.11
- RREI.CA: score=5.53 buy_ready=False sector_rank=18 price=4.85 support=4.82 resistance=4.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7521965.5 spike=0.12
- RTVC.CA: score=8.01 buy_ready=False sector_rank=18 price=3.85 support=3.73 resistance=4.2 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=46.15 liquidity=0.0 spike=0.0
- RUBX.CA: score=6.76 buy_ready=False sector_rank=18 price=12.29 support=12.02 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=30.96 liquidity=754901.88 spike=0.02
- SAUD.CA: score=17.46 buy_ready=True sector_rank=6 price=22.35 support=21.25 resistance=22.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=62.72 liquidity=1060996.5 spike=0.08
- SCEM.CA: score=7.68 buy_ready=False sector_rank=19 price=83.09 support=82.34 resistance=83.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10445672.0 spike=0.1
- SCFM.CA: score=13.01 buy_ready=False sector_rank=18 price=279.58 support=250.12 resistance=325.0 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=39.78 liquidity=0.0 spike=0.0
- SCTS.CA: score=11.1 buy_ready=False sector_rank=16 price=609.02 support=602.0 resistance=685.0 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=53.82 liquidity=0.0 spike=0.0
- SDTI.CA: score=-0.96 buy_ready=False sector_rank=18 price=73.4 support=72.8 resistance=74.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:10 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1027022.56 spike=0.04
- SEIG.CA: score=10.01 buy_ready=False sector_rank=18 price=266.93 support=237.0 resistance=295.0 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=75.66 liquidity=0.0 spike=0.0
- SIPC.CA: score=8.01 buy_ready=False sector_rank=18 price=5.25 support=5.09 resistance=5.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19153988.0 spike=0.37
- SKPC.CA: score=17.72 buy_ready=True sector_rank=15 price=16.5 support=14.8 resistance=16.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:10 AM market time freshness=DELAYED_CURRENT RSI=67.37 liquidity=3229915.25 spike=0.07
- SMFR.CA: score=8.01 buy_ready=False sector_rank=18 price=287.61 support=272.0 resistance=289.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:04 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14784576.0 spike=0.42
- SNFC.CA: score=4.21 buy_ready=False sector_rank=18 price=10.89 support=10.7 resistance=12.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=34.91 liquidity=1197903.5 spike=0.1
- SPIN.CA: score=15.78 buy_ready=False sector_rank=3 price=15.72 support=14.55 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:10 AM market time freshness=DELAYED_CURRENT RSI=66.76 liquidity=377354.41 spike=0.01
- SPMD.CA: score=19.02 buy_ready=True sector_rank=18 price=0.5 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=61.47 liquidity=4009601.5 spike=0.12
- SUGR.CA: score=19.25 buy_ready=True sector_rank=5 price=49.14 support=46.47 resistance=49.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=59.9 liquidity=2853928.5 spike=0.32
- SVCE.CA: score=16.25 buy_ready=True sector_rank=18 price=9.41 support=9.06 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=48.62 liquidity=3240994.0 spike=0.09
- SWDY.CA: score=26.4 buy_ready=False sector_rank=2 price=110.46 support=87.41 resistance=114.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=73.84 liquidity=13704442.0 spike=0.24
- TALM.CA: score=14.19 buy_ready=True sector_rank=16 price=18.66 support=15.4 resistance=19.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=69.57 liquidity=1090663.75 spike=0.03
- TMGH.CA: score=21.71 buy_ready=False sector_rank=11 price=98.91 support=95.2 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=46.72 liquidity=21226294.0 spike=0.06
- TRTO.CA: score=9.01 buy_ready=False sector_rank=18 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=14.04 buy_ready=True sector_rank=18 price=550.0 support=491.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:08 AM market time freshness=DELAYED_CURRENT RSI=42.89 liquidity=1030897.13 spike=0.19
- UEGC.CA: score=-0.31 buy_ready=False sector_rank=18 price=2.87 support=2.8 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1682017.75 spike=0.03
- UNIP.CA: score=13.89 buy_ready=False sector_rank=18 price=0.42 support=0.34 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=59.15 liquidity=879339.94 spike=0.03
- UNIT.CA: score=7.03 buy_ready=False sector_rank=11 price=17.96 support=17.32 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=29.77 liquidity=324369.34 spike=0.01
- WCDF.CA: score=10.68 buy_ready=False sector_rank=18 price=596.09 support=508.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=25.6 liquidity=676155.63 spike=0.17
- WKOL.CA: score=13.36 buy_ready=False sector_rank=18 price=324.83 support=307.0 resistance=363.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=54.89 liquidity=349535.22 spike=0.02
- ZEOT.CA: score=8.01 buy_ready=False sector_rank=18 price=13.52 support=13.4 resistance=13.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12154175.0 spike=0.41
- ZMID.CA: score=8.71 buy_ready=False sector_rank=11 price=7.69 support=7.65 resistance=7.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27425328.0 spike=0.1

## Backtesting Lite
- SWDY.CA: 180d return=43.67%, max drawdown=-14.67%, MA20>MA50 days last20=19, as_of=2026-08-08T21:00:00+00:00
- EFIH.CA: 180d return=51.07%, max drawdown=-22.68%, MA20>MA50 days last20=14, as_of=2026-08-08T21:00:00+00:00
- OCDI.CA: 180d return=70.0%, max drawdown=-16.75%, MA20>MA50 days last20=20, as_of=2026-08-08T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- SWDY.CA: status=RECENT_ACCEPTED latest=2026-07-19 age_days=23 sources=3 expected=Elsewedy Electric summary=Elsewedy Electric (SWDY.CA) has recently announced a significant project award for a subsidiary and has several recent disclosures on the Egyptian Exchange. The company's Shariah compliance status was updated in July 2026, and recent financial performance data is available.
  - Release from El sewedy Electric (SWDY.CA) Concerning a Subsidiary Company (2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlNXip9fGqQwtSxHPoZEfVLOqjHLPMJWL6Y0eAecKtIdblxbfcxwaGqoEoY5lKDpa6qPyeN08bfu1It2YTsxlBnNa-muIYuh9f0LqVvWKTHkx2Mr3XyAE8BsVpnK78lLTYYtQ9FiX_-dBndY4a
  - ELSWEDY ELECTRIC (SWDY.CA) - EGM Minutes (Notarized) (July 19, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGu9wPn1eHrt2WKCOwM1891kXIb-Y6zLt1l0NXfXUgCWKyBtc5pKWpGOUBTej4P6gXws58uyexTdg4k6dAvHMjk5R5wUEVqtX-WHgBzVqK6EaZQg6R4lucrxJqaCH6xIA2QGjC8AhKA7Z0S3vAjyPFttvepcmJQUPByjyQDXQ==
  - ELSWEDY ELECTRIC (SWDY.CA) - Disclosure Form for the BoD & the Shareholders' Structure (June 25, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGu9wPn1eHrt2WKCOwM1891kXIb-Y6zLt1l0NXfXUgCWKyBtc5pKWpGOUBTej4P6gXws58uyexTdg4k6dAvHMjk5R5wUEVqtX-WHgBzVqK6EaZQg6R4lucrxJqaCH6xIA2QGjC8AhKA7Z0S3vAjyPFttvepcmJQUPByjyQDXQ==
- EFIH.CA: status=RECENT_ACCEPTED latest=2026-07-22 age_days=20 sources=3 expected=E-Finance For Digital and Financial Investments summary=E-Finance For Digital and Financial Investments (EFIH.CA) has several recent disclosures on the Egyptian Exchange, including periodic disclosure to shareholders and updates on its Board of Directors and shareholder structure. The company's last trading date information and coupon payment date are also available.
  - E-Finance For Digital and Financial Investements SAE (EFIH.CA) - Disclosure Form for the BoD & the Shareholders' Structure (April 17, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnm9c64NcDQOQ19b_P8wVRPPAnteH4ZcfSUtQITsIVLRX_jwXfS42s4TwpqoAJViZ8Hz2IwtrjzikP1q2q0Q_oQSadheGnRs_n1-7RlNtJUc2BXTgC3dSmDxtvokjJ31Vn_3Q6iMGC2gNg_eJ8
  - E-Finance For Digital and Financial Investements SAE (EFIH.CA) - Release Concerning the Periodic Disclosure to Shareholders (July 22, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF93LpYO_d5pIM92vV3K7m89UH2T-dc-TroeTg3kJR289p0Osa7-Z3KzgoF6bMy-_qEKMtxUtJqqazU8zKRvL04zGGrfZri2Rqz6l9oViu-mDyimWLGpirwTDwGpMETG5bKxGBpPmMS1IL2zIThbvA
  - E-finance For Digital and Financial Investments (EFIH.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 20, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF93LpYO_d5pIM92vV3K7m89UH2T-dc-TroeTg3kJR289p0Osa7-Z3KzgoF6bMy-_qEKMtxUtJqqazU8zKRvL04zGGrfZri2Rqz6l9oViu-mDyimWLGpirwTDwGpMETG5bKxGBpPmMS1IL2zIThbvA
- OCDI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Sixth of October Development and Investment summary=Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- AMOC.CA: status=RECENT_ACCEPTED latest=2026-07-26 age_days=16 sources=3 expected=Alexandria Mineral Oils summary=Alexandria Mineral Oils (AMOC.CA) has provided several recent disclosures on the Egyptian Exchange regarding its Board of Directors, shareholder structure, and periodic disclosures to shareholders. Recent income statement data is also available.
  - Alexandria Mineral Oils Company (AMOC.CA) - Disclosure Form for the BoD & the Shareholders' Structure (April 14, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWQoKz4kLcWbBlDVdeQhuDKn0gZNEr5vMes24ZIy33UtqgHom01Ki1l9VmexUOBehnc6N36xKzDDfOUm11yZ3di4WJ8zMRKerorAeTCBDR0Zm9nJaN25IolmV4ykoz7myZQl3Xr9bEsYU_1CiGNPuRIQ==
  - Alexandria Mineral Oils Company (AMOC.CA) - Release Concerning Periodic Disclosure to Shareholders (July 26, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKqCW4NJgDoB39MI2vSUy1-qE9RZJ8B635Inzwzs_Vjm5JkdT87TrnF9OvhDEzkvRctfRMDVcbLaJ6mTfeGSmQisx0dGWB3I14fewJVxGFBZA85_j3RKf2xAXC2o3LuYSimDyNr15KiNcRlEwE3NAaCA==
  - Correction from Alexandria Mineral Oils Company (AMOC.CA) Concerning the BoD & the Shareholders' Structure (July 14, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxQJIbmQbvwchWGlsYKAo30tWsRdhH7CK07IcfNxn-WROkSFTPzryBZr_m9RkyV5Azm85XztdH7qEPTRRQ3vR8lqxRW_RGNNBb0yuODkDDX7sj6ysxazJ2sXWgwfQHas3roGnVaiiTrMCQUVR0zg==
- ABUK.CA: status=RECENT_ACCEPTED latest=2026-07-30 age_days=12 sources=3 expected=Abu Qir Fertilizers summary=Abu Qir Fertilizers (ABUK.CA) has released recent Board of Directors' decisions and unaudited financial indicators. The company's fiscal year 2025 revenue and earnings have been reported, and there are announcements regarding strategic agreements and stake acquisitions.
  - Abou Kir Fertilizers (ABUK.CA) - Decisions of the BoD Meeting (July 30, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-mUNmanhxmi-xtfqYpSwXz0C-u4d6FYH41D1RSJgAGiF0kh47VzxlYt6ryaVnu3RPeAsfytgQTtoYtE6vHukt7QenPczZwQ230IvHb0nP0twmHyaI7GL9OxdacbHXxHtZnIF6-6b3fk4wcygNrwLuvw==
  - Abou Kir Fertilizers (ABUK.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 13, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEk0-bgUl-lxvf0IeQYe8Oy5iK2FnovPPQ3aCiA_ysWXLGCNR6HP6p3wAWddfhHm6k80N5U5Vy-fLzyfFBzpqcqKL8fA46Do_Ccdq9s65Mn3CUeknAgqG1jIeDthUtQr5QNM6jyr8F7tfI2YJbtlfDUarB3kdhy9SYhr1nMfg==
  - Abu Qir Fertilizers & Chemical Industries Company (SAE) (EGX:ABUK) - Stock Analysis (Fiscal Year 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6vxWNfJWE7LkJncTfFOx1YhN37irmmsj6UDXZ3Ve3YHV35I1F7s1PAc0NMuQQYh3wWHxJFDp--mOELHaS2-e4Avd3dM6_CovRAnJTgH8GiyK-RjddmSTxe92cunae4Npy6w==
- COMI.CA: status=RECENT_ACCEPTED latest=2026-07-14 age_days=28 sources=3 expected=Commercial International Bank Egypt summary=Commercial International Bank Egypt (COMI.CA) has been active with recent news, including celebrating 30 years of GDRs, starting due diligence on HSBC's retail banking portfolio, and receiving an award for sustainable finance. The bank has also released recent business results and financial disclosures.
  - CIB Celebrates with the Egyptian Exchange 30 Years of launching Egypt's first Global Depositary Receipts program (July 14, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmvFw7kJtO544tHvKVdhfif45uGsXMhKPmBNM44vmvM8GmVa0CHQgkJWRXR_Zy0aKMZXhBNvdhSK5cau6QLYxLmLR-EGGEdMZzwzorMhMm8jbDGPGs7nzxJ5jEFCgbv_57e_BS
  - CIB starts the due diligence process on HSBC's retail banking portfolio (February 24, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmvFw7kJtO544tHvKVdhfif45uGsXMhKPmBNM44vmvM8GmVa0CHQgkJWRXR_Zy0aKMZXhBNvdhSK5cau6QLYxLmLR-EGGEdMZzwzorMhMm8jbDGPGs7nzxJ5jEFCgbv_57e_BS
  - CIB Has Been Honored at the Stock Exchange for Winning the Best Bank in Sustainable Finance Award in Africa for 2025 (February 19, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmvFw7kJtO544tHvKVdhfif45uGsXMhKPmBNM44vmvM8GmVa0CHQgkJWRXR_Zy0aKMZXhBNvdhSK5cau6QLYxLmLR-EGGEdMZzwzorMhMm8jbDGPGs7nzxJ5jEFCgbv_57e_BS
- TMGH.CA: status=RECENT_ACCEPTED latest=2026-07-16 age_days=26 sources=3 expected=Talaat Moustafa Group Holding summary=Talaat Moustafa Group Holding (TMGH.CA) has provided recent disclosures on the EGX, including updates on its Board of Directors and shareholder structure, company sales, projects, and the signing of an MOU. The company also announced a recent dividend payment and its Shariah compliance status was updated in August 2026.
  - T M G Holding (TMGH.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 16, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF025gcyHcmRIMGQ534AIM84ZCP9BrOMkC_OBy8ZRlKrFK4zVVDPF-aK8Z7Qn52OBzVJbm7sBt53vOC2xMM4qRACLo3lSepOVPN70Er94Dbm7__XgKV2URB5aRDHk3-YXDhooRZreXj6_teNSoILk4=
  - Release from T M G Holding (TMGH.CA) Concerning the Company's Sales (July 5, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF025gcyHcmRIMGQ534AIM84ZCP9BrOMkC_OBy8ZRlKrFK4zVVDPF-aK8Z7Qn52OBzVJbm7sBt53vOC2xMM4qRACLo3lSepOVPN70Er94Dbm7__XgKV2URB5aRDHk3-YXDhooRZreXj6_teNSoILk4=
  - Release from TMG Holding (TMGH.CA) Concerning Company's Projects (June 25, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF025gcyHcmRIMGQ534AIM84ZCP9BrOMkC_OBy8ZRlKrFK4zVVDPF-aK8Z7Qn52OBzVJbm7sBt53vOC2xMM4qRACLo3lSepOVPN70Er94Dbm7__XgKV2URB5aRDHk3-YXDhooRZreXj6_teNSoILk4=
- ORHD.CA: status=RECENT_ACCEPTED latest=2026-07-17 age_days=25 sources=3 expected=Orascom Development Egypt summary=Orascom Development Egypt (ORHD.CA) has recently secured a significant syndicated loan to accelerate development of one of its subsidiaries. The company has also provided recent disclosures on its Board of Directors and shareholder structure, and reported its financial results for Q1-2026.
  - Orascom Development Egypt (ORHD.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 08, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEziGT43M0rN57kcJElXUfxGbJQr_lpxuoe-TfKUpgX_mC4zP4C4XXXQiinneGkaJoNkeV8_W_gEJ9BjQzms25-nQ79LP3eB45KTjOIn2EJINSxj5jGCE9ce4Uh9KVfmB_KapI-7bS0XWMmXHRKeePMDA==
  - Release from Orascom Development Egypt (ORHD.CA) Concerning One of its Subsidiaries (July 17, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmBMl0vJWj8RwbQmRZkBns6jwCC-VCaT--rSPB-R6rm8RMn9lvUw0thDgmJgWNlH5_dqt3DHzxUDSnxBjDriUuB0XfajDS29_8l0g_oxjDB_Hw5WWwd_q2av8Hpj3hm1BobBBsBrBxK_ij_qn3uOaAhA==
  - Orascom Development logs EGP 5.3bn net profits in 2025 Financial Results (Recent): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYUWmOZ0wJYrrUPGzJaVbV96457262sL0ptTx5bAIaom5iIioZ69WJ6F8KwFPeqqumJuTn4Az5_-dqcb7DMcww6CFosYA1TSen0T5i00U9ttVRcSx-Tz6_zigDoikZEasPnt_nP9WDW_1ew_tZTTc=

## Warnings
- Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
