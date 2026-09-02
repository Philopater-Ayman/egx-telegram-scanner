# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-09-02T09:57:57.640786+00:00
Generated Cairo: 2026-09-02 12:57
Run timing: target 08:45 Cairo | generated Cairo 2026-09-02 12:57 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-02 12:53

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 56
- Data quality issues: 1
- Tradeable price/liquidity tickers: 179/189
- Top sector: Transportation & Logistics

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, September 02
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 50.0% / above MA50 72.22%
- EGX70 regime: MIXED / above MA20 48.72% / above MA50 74.36%
- Sector breadth: 42.86%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- SVCE.CA: liquidity=459154016.0 spike=3.16 score=27.19
- CCAP.CA: liquidity=349269216.0 spike=0.55 score=26.4
- SKPC.CA: liquidity=342837312.0 spike=4.15 score=14.4
- MFPC.CA: liquidity=319369984.0 spike=3.24 score=13.88
- AMOC.CA: liquidity=261636576.0 spike=1.45 score=24.24

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner found no high‑conviction buys; top rows show liquidity spikes and bullish watch in Transportation & Logistics, Building Materials, etc., but mixed EGX30/EGX70 breadth keeps risk mode selective.
- CSAG.CA: liquidity cooling, momentum extended, far above support; bullish watch in leading Transportation & Logistics sector.
- NCCW.CA: strong accumulation spike with liquidity surge, sector not leading, watch for resistance near 7.11.
- LCSW.CA: accumulation spike, RSI moderate, close to resistance, no short‑term scanner flags in Building Materials.
- ARCC.CA: liquidity cooling, extended momentum, far above support; bullish watch but sector breadth weak.

## Top Liquidity Spikes
- DEIN.CA: spike=20.0 liquidity=683.1 outlook=WEAK_OR_RISKY score=14.68 buy_ready=False
- CERA.CA: spike=17.88 liquidity=240490096.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- TRTO.CA: spike=5.64 liquidity=93771.56 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SKPC.CA: spike=4.15 liquidity=342837312.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EOSB.CA: spike=3.49 liquidity=177614.11 outlook=CONSTRUCTIVE score=59.68 buy_ready=False

## Sector Leaderboard
- #1 Transportation & Logistics: score=11.63 5d=2.8% 20d=16.62% aboveMA50=100.0%
- #2 Investment Holding: score=10.83 5d=3.85% 20d=13.38% aboveMA50=100.0%
- #3 Textiles: score=10.59 5d=0.94% 20d=19.0% aboveMA50=100.0%
- #4 Building Materials: score=9.26 5d=4.15% 20d=14.55% aboveMA50=66.67%
- #5 Industrial Goods & Cables: score=8.15 5d=2.21% 20d=16.27% aboveMA50=50.0%
- #6 Banking & Financials: score=7.35 5d=1.43% 20d=7.24% aboveMA50=100.0%
- #7 Tourism & Leisure: score=6.51 5d=3.45% 20d=9.73% aboveMA50=0.0%
- #8 Basic Resources & Chemicals: score=6.18 5d=1.71% 20d=2.93% aboveMA50=60.0%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- BINV.CA: BULLISH_WATCH score=96 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ORWE.CA: BULLISH_WATCH score=92 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- LCSW.CA: BULLISH_WATCH score=90.26 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- ALCN.CA: BULLISH_WATCH score=89 liquidity=TRADEABLE sector=LEADING risk=close to resistance
- NCCW.CA: BULLISH_WATCH score=86.68 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- MEPA.CA: BULLISH_WATCH score=83.68 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- KABO.CA: BULLISH_WATCH score=82 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- CSAG.CA: BULLISH_WATCH score=80 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended; far above support
- SPIN.CA: BULLISH_WATCH score=78 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended; far above support
- CCRS.CA: BULLISH_WATCH score=75.68 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- CSAG.CA: rank=31.4 outlook=BULLISH_WATCH outlook_score=80 sector_rank=1 price=42.45 support=33.4 resistance=44.3 liquidity=15912875.0
- NCCW.CA: rank=29.89 outlook=BULLISH_WATCH outlook_score=86.68 sector_rank=12 price=6.39 support=5.59 resistance=7.11 liquidity=74437912.0
- LCSW.CA: rank=28.82 outlook=BULLISH_WATCH outlook_score=90.26 sector_rank=4 price=36.0 support=32.12 resistance=37.5 liquidity=67332688.0
- ARCC.CA: rank=28.4 outlook=BULLISH_WATCH outlook_score=75.26 sector_rank=4 price=77.95 support=55.77 resistance=91.72 liquidity=45048252.0
- MAAL.CA: rank=28.39 outlook=BULLISH_WATCH outlook_score=70.68 sector_rank=12 price=9.6 support=8.32 resistance=9.76 liquidity=16710272.0
- POUL.CA: rank=28.07 outlook=BULLISH_WATCH outlook_score=72.17 sector_rank=10 price=39.93 support=36.6 resistance=40.24 liquidity=13488577.0
- GIHD.CA: rank=27.87 outlook=BULLISH_WATCH outlook_score=73.68 sector_rank=12 price=70.39 support=58.01 resistance=76.5 liquidity=13031141.0
- PRDC.CA: rank=27.78 outlook=BULLISH_WATCH outlook_score=75.45 sector_rank=13 price=9.3 support=8.7 resistance=10.25 liquidity=52492784.0
- ORWE.CA: rank=27.4 outlook=BULLISH_WATCH outlook_score=92 sector_rank=3 price=26.74 support=23.07 resistance=27.41 liquidity=32934120.0
- ALCN.CA: rank=27.4 outlook=BULLISH_WATCH outlook_score=89 sector_rank=1 price=31.99 support=29.74 resistance=32.61 liquidity=27911172.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=21.87 buy_ready=False sector_rank=12 price=302.31 support=266.01 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=11144243.0 spike=0.23
- ABUK.CA: score=24.64 buy_ready=False sector_rank=8 price=89.55 support=72.9 resistance=88.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=83.1 liquidity=199288128.0 spike=1.62
- ACAMD.CA: score=13.87 buy_ready=False sector_rank=12 price=2.07 support=1.95 resistance=2.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=29967066.0 spike=0.54
- ACGC.CA: score=19.42 buy_ready=False sector_rank=3 price=14.08 support=10.36 resistance=14.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=81.83 liquidity=7021920.0 spike=0.17
- ADCI.CA: score=16.47 buy_ready=True sector_rank=12 price=305.47 support=274.0 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:28 AM market time freshness=DELAYED_CURRENT RSI=41.91 liquidity=2595093.25 spike=0.12
- ADIB.CA: score=22.4 buy_ready=False sector_rank=6 price=51.9 support=51.02 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=45.62 liquidity=66171448.0 spike=0.97
- ADPC.CA: score=16.87 buy_ready=False sector_rank=12 price=3.97 support=3.85 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=27.18 liquidity=17549162.0 spike=0.42
- AFDI.CA: score=15.92 buy_ready=False sector_rank=12 price=56.0 support=52.56 resistance=69.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=24.45 liquidity=9043565.0 spike=0.26
- AFMC.CA: score=16.87 buy_ready=False sector_rank=12 price=182.36 support=175.2 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=20.67 liquidity=22792534.0 spike=0.16
- AJWA.CA: score=17.41 buy_ready=False sector_rank=12 price=179.94 support=179.1 resistance=204.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=39.11 liquidity=8541376.0 spike=0.14
- ALCN.CA: score=27.4 buy_ready=True sector_rank=1 price=31.99 support=29.74 resistance=32.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=48.08 liquidity=27911172.0 spike=1.0
- ALUM.CA: score=23.87 buy_ready=True sector_rank=12 price=29.13 support=23.35 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=49.28 liquidity=10213683.0 spike=0.37
- AMER.CA: score=16.78 buy_ready=False sector_rank=13 price=5.7 support=5.06 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=30.52 liquidity=24145834.0 spike=0.25
- AMES.CA: score=10.71 buy_ready=False sector_rank=12 price=91.5 support=90.06 resistance=104.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=155385536.0 spike=1.92
- AMIA.CA: score=20.99 buy_ready=False sector_rank=12 price=19.61 support=10.6 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=85.44 liquidity=64447700.0 spike=1.06
- AMOC.CA: score=24.24 buy_ready=False sector_rank=9 price=13.19 support=8.93 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=83.36 liquidity=261636576.0 spike=1.45
- APSW.CA: score=8.46 buy_ready=False sector_rank=12 price=8.58 support=8.41 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=50.36 liquidity=584287.13 spike=0.39
- ARAB.CA: score=23.78 buy_ready=True sector_rank=13 price=0.26 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=67065136.0 spike=0.73
- ARCC.CA: score=28.4 buy_ready=True sector_rank=4 price=77.95 support=55.77 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=63.13 liquidity=45048252.0 spike=0.42
- AREH.CA: score=13.09 buy_ready=False sector_rank=12 price=1.44 support=1.4 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=4219073.5 spike=0.15
- ARVA.CA: score=8.87 buy_ready=False sector_rank=12 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=13.4 buy_ready=False sector_rank=12 price=63.55 support=62.01 resistance=69.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=28.37 liquidity=6525056.0 spike=0.15
- ASPI.CA: score=21.87 buy_ready=False sector_rank=12 price=0.43 support=0.43 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=37.94 liquidity=18006184.0 spike=0.45
- ATLC.CA: score=29.62 buy_ready=False sector_rank=16 price=6.7 support=5.15 resistance=6.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=73.57 liquidity=82966504.0 spike=3.31
- ATQA.CA: score=23.4 buy_ready=False sector_rank=8 price=12.35 support=9.8 resistance=12.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=82.21 liquidity=60986452.0 spike=0.62
- AXPH.CA: score=14.87 buy_ready=False sector_rank=12 price=1703.46 support=1250.1 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=86.93 liquidity=3993458.25 spike=0.31
- BINV.CA: score=22.36 buy_ready=True sector_rank=2 price=50.31 support=46.25 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=58.14 liquidity=3963313.0 spike=0.37
- BIOC.CA: score=16.87 buy_ready=False sector_rank=12 price=320.55 support=265.2 resistance=563.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=20.47 liquidity=57442636.0 spike=0.23
- BTFH.CA: score=17.0 buy_ready=False sector_rank=16 price=3.04 support=2.94 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=66833128.0 spike=0.37
- CAED.CA: score=23.87 buy_ready=True sector_rank=12 price=144.04 support=118.01 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=62.76 liquidity=16322365.0 spike=0.46
- CANA.CA: score=20.57 buy_ready=False sector_rank=6 price=42.93 support=38.0 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=70.55 liquidity=6173435.0 spike=0.35
- CCAP.CA: score=26.4 buy_ready=False sector_rank=2 price=5.97 support=5.18 resistance=6.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=74.83 liquidity=349269216.0 spike=0.55
- CCRS.CA: score=25.87 buy_ready=True sector_rank=12 price=2.64 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=57.04 liquidity=16838674.0 spike=0.33
- CEFM.CA: score=15.55 buy_ready=True sector_rank=12 price=145.12 support=131.03 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=65.19 liquidity=3676987.25 spike=0.16
- CERA.CA: score=13.87 buy_ready=False sector_rank=12 price=1.43 support=1.25 resistance=1.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=240490096.0 spike=17.88
- CFGH.CA: score=15.86 buy_ready=False sector_rank=12 price=0.12 support=0.1 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=79.17 liquidity=46892.25 spike=2.47
- CICH.CA: score=11.69 buy_ready=False sector_rank=16 price=12.33 support=12.0 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=48.19 liquidity=688847.75 spike=0.1
- CIEB.CA: score=22.85 buy_ready=True sector_rank=6 price=25.33 support=23.97 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=60.24 liquidity=6454448.0 spike=0.43
- CIRA.CA: score=14.92 buy_ready=False sector_rank=20 price=33.6 support=32.1 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=20.68 liquidity=33293788.0 spike=0.98
- CLHO.CA: score=25.04 buy_ready=True sector_rank=15 price=18.16 support=16.95 resistance=18.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=58.36 liquidity=44138724.0 spike=0.59
- CNFN.CA: score=14.09 buy_ready=False sector_rank=16 price=4.88 support=4.73 resistance=5.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=3089898.75 spike=0.17
- COMI.CA: score=22.4 buy_ready=False sector_rank=6 price=138.09 support=135.35 resistance=142.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=122217760.0 spike=0.23
- COPR.CA: score=23.87 buy_ready=True sector_rank=12 price=0.5 support=0.4 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=67.72 liquidity=18981730.0 spike=0.21
- COSG.CA: score=25.87 buy_ready=True sector_rank=12 price=1.88 support=1.67 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=68.09 liquidity=40612088.0 spike=0.78
- CPCI.CA: score=15.13 buy_ready=True sector_rank=12 price=547.87 support=483.0 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=47.63 liquidity=1257667.13 spike=0.14
- CSAG.CA: score=31.4 buy_ready=True sector_rank=1 price=42.45 support=33.4 resistance=44.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=63.49 liquidity=15912875.0 spike=0.58
- DAPH.CA: score=25.87 buy_ready=True sector_rank=12 price=132.84 support=99.02 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=54.67 liquidity=29539238.0 spike=0.42
- DEIN.CA: score=16.87 buy_ready=False sector_rank=12 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance as_of=2026-08-31T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=683.1 spike=20.0
- DOMT.CA: score=12.82 buy_ready=False sector_rank=10 price=28.26 support=27.79 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=50.11 liquidity=752094.88 spike=0.04
- DSCW.CA: score=13.87 buy_ready=False sector_rank=12 price=1.92 support=1.84 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=30.19 liquidity=11065137.0 spike=0.13
- DTPP.CA: score=23.87 buy_ready=True sector_rank=12 price=303.49 support=240.1 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=45.43 liquidity=11184578.0 spike=0.27
- EALR.CA: score=17.55 buy_ready=False sector_rank=12 price=392.42 support=364.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=51.72 liquidity=5673870.5 spike=0.12
- EASB.CA: score=18.83 buy_ready=False sector_rank=12 price=7.2 support=6.71 resistance=8.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=52.81 liquidity=7876537.0 spike=1.04
- EAST.CA: score=17.85 buy_ready=False sector_rank=10 price=36.22 support=35.0 resistance=37.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=49.63 liquidity=7779389.5 spike=0.12
- EBSC.CA: score=25.87 buy_ready=False sector_rank=12 price=2.23 support=1.88 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=71.79 liquidity=10714894.0 spike=0.8
- ECAP.CA: score=9.93 buy_ready=False sector_rank=12 price=33.75 support=32.06 resistance=34.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25477232.0 spike=1.53
- EDFM.CA: score=15.22 buy_ready=True sector_rank=12 price=418.47 support=390.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=60.15 liquidity=1351220.38 spike=0.56
- EEII.CA: score=21.87 buy_ready=False sector_rank=12 price=2.94 support=2.66 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=51.77 liquidity=13851962.0 spike=0.48
- EFIC.CA: score=18.4 buy_ready=False sector_rank=8 price=195.94 support=188.01 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=39.73 liquidity=11684656.0 spike=0.25
- EFID.CA: score=22.07 buy_ready=False sector_rank=10 price=30.5 support=27.52 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=40.91 liquidity=79871256.0 spike=0.95
- EFIH.CA: score=20.63 buy_ready=False sector_rank=17 price=22.82 support=22.84 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=43.28 liquidity=39449480.0 spike=0.35
- EGAL.CA: score=24.4 buy_ready=False sector_rank=8 price=378.19 support=292.0 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=72.28 liquidity=152789472.0 spike=1.0
- EGAS.CA: score=19.01 buy_ready=True sector_rank=9 price=59.06 support=52.5 resistance=63.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=44.48 liquidity=4665703.0 spike=0.2
- EGBE.CA: score=12.41 buy_ready=False sector_rank=6 price=0.53 support=0.48 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=38.81 liquidity=12308.18 spike=0.06
- EGCH.CA: score=22.58 buy_ready=False sector_rank=8 price=14.01 support=13.3 resistance=14.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=51.6 liquidity=138990368.0 spike=1.09
- EGSA.CA: score=10.72 buy_ready=False sector_rank=14 price=8.69 support=8.65 resistance=8.93 source=Yahoo Finance as_of=2026-08-31T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=4527.49 spike=0.71
- EGTS.CA: score=13.78 buy_ready=False sector_rank=13 price=17.02 support=16.17 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=24.5 liquidity=13489828.0 spike=0.39
- EHDR.CA: score=16.87 buy_ready=False sector_rank=12 price=2.89 support=2.73 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=33.8 liquidity=15863326.0 spike=0.47
- EKHO.CA: score=10.34 buy_ready=False sector_rank=9 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-31T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=18.4 buy_ready=False sector_rank=5 price=2.13 support=2.04 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=48.48 liquidity=54308384.0 spike=0.89
- ELKA.CA: score=25.87 buy_ready=False sector_rank=12 price=1.9 support=1.69 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=72.0 liquidity=21735236.0 spike=0.29
- ELNA.CA: score=4.99 buy_ready=False sector_rank=12 price=37.0 support=36.1 resistance=38.4 source=Yahoo Finance as_of=2026-08-31T21:00:00+00:00 freshness=FRESH RSI=33.21 liquidity=122618.0 spike=0.39
- ELSH.CA: score=18.87 buy_ready=False sector_rank=12 price=13.45 support=12.97 resistance=14.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=40.6 liquidity=13592313.0 spike=0.25
- ELWA.CA: score=14.41 buy_ready=False sector_rank=12 price=1.86 support=1.62 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=1536001.0 spike=0.68
- EMFD.CA: score=22.78 buy_ready=False sector_rank=13 price=13.7 support=11.42 resistance=13.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=85.71 liquidity=85182056.0 spike=0.63
- ENGC.CA: score=16.87 buy_ready=False sector_rank=12 price=44.5 support=41.8 resistance=54.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=28.58 liquidity=22763018.0 spike=0.84
- EOSB.CA: score=21.03 buy_ready=False sector_rank=12 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-08-31T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=177614.11 spike=3.49
- EPCO.CA: score=11.58 buy_ready=False sector_rank=12 price=11.16 support=10.8 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=26.09 liquidity=4704284.5 spike=0.27
- EPPK.CA: score=3.64 buy_ready=False sector_rank=12 price=10.84 support=11.41 resistance=15.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=32.51 liquidity=770366.25 spike=0.69
- ETEL.CA: score=23.71 buy_ready=True sector_rank=14 price=114.89 support=107.0 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=58.15 liquidity=80237808.0 spike=0.56
- ETRS.CA: score=21.91 buy_ready=True sector_rank=12 price=11.47 support=10.41 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=65.35 liquidity=27900778.0 spike=1.02
- EXPA.CA: score=21.12 buy_ready=True sector_rank=6 price=21.05 support=19.8 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=47.38 liquidity=6723353.0 spike=0.17
- FAIT.CA: score=16.48 buy_ready=True sector_rank=6 price=43.82 support=36.9 resistance=45.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=67.16 liquidity=2083666.0 spike=0.27
- FAITA.CA: score=14.62 buy_ready=False sector_rank=6 price=0.99 support=0.97 resistance=1.02 source=Yahoo Finance as_of=2026-08-31T21:00:00+00:00 freshness=FRESH RSI=56.7 liquidity=57238.83 spike=1.08
- FERC.CA: score=25.66 buy_ready=True sector_rank=8 price=82.39 support=76.2 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=30390456.0 spike=1.63
- FWRY.CA: score=18.23 buy_ready=False sector_rank=17 price=18.95 support=18.66 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=54.61 liquidity=196820080.0 spike=1.3
- GBCO.CA: score=11.5 buy_ready=False sector_rank=21 price=29.17 support=27.51 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=27.21 liquidity=33733336.0 spike=0.68
- GDWA.CA: score=26.87 buy_ready=True sector_rank=12 price=0.84 support=0.77 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=62.24 liquidity=26447578.0 spike=0.51
- GGCC.CA: score=16.87 buy_ready=False sector_rank=12 price=0.86 support=0.84 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=15.65 liquidity=27520286.0 spike=0.51
- GIHD.CA: score=27.87 buy_ready=True sector_rank=12 price=70.39 support=58.01 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=59.07 liquidity=13031141.0 spike=0.53
- GMCI.CA: score=5.56 buy_ready=False sector_rank=12 price=1.88 support=1.83 resistance=2.04 source=Yahoo Finance as_of=2026-08-31T21:00:00+00:00 freshness=FRESH RSI=21.43 liquidity=705088.36 spike=1.49
- GRCA.CA: score=23.87 buy_ready=False sector_rank=12 price=77.89 support=54.7 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=74.29 liquidity=14110054.0 spike=0.23
- GSSC.CA: score=13.24 buy_ready=False sector_rank=12 price=280.04 support=274.0 resistance=301.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=55.58 liquidity=1364239.0 spike=0.08
- GTWL.CA: score=20.87 buy_ready=False sector_rank=12 price=229.17 support=85.0 resistance=247.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=77.87 liquidity=103558872.0 spike=0.36
- HDBK.CA: score=23.4 buy_ready=False sector_rank=6 price=111.88 support=83.0 resistance=119.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=87.95 liquidity=37495440.0 spike=0.69
- HELI.CA: score=24.5 buy_ready=True sector_rank=13 price=7.95 support=7.34 resistance=8.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=35.78 liquidity=201449536.0 spike=1.36
- HRHO.CA: score=12.0 buy_ready=False sector_rank=16 price=25.89 support=25.33 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=28.71 liquidity=33996484.0 spike=0.27
- ICID.CA: score=17.69 buy_ready=False sector_rank=12 price=17.23 support=7.85 resistance=18.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=90.42 liquidity=4819435.5 spike=0.17
- IDRE.CA: score=24.35 buy_ready=True sector_rank=12 price=56.26 support=48.27 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=46.84 liquidity=18011904.0 spike=1.24
- IFAP.CA: score=18.99 buy_ready=False sector_rank=11 price=21.09 support=19.75 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=31.06 liquidity=19480314.0 spike=0.59
- INFI.CA: score=21.87 buy_ready=False sector_rank=12 price=149.0 support=114.05 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=35.89 liquidity=14285269.0 spike=0.2
- IRON.CA: score=14.39 buy_ready=False sector_rank=8 price=30.0 support=29.82 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=38.7 liquidity=5986794.5 spike=0.46
- ISMA.CA: score=21.87 buy_ready=False sector_rank=12 price=32.87 support=30.5 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=42.41 liquidity=15463207.0 spike=0.6
- ISMQ.CA: score=19.5 buy_ready=False sector_rank=8 price=9.45 support=9.0 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=48626252.0 spike=1.05
- ISPH.CA: score=16.04 buy_ready=False sector_rank=15 price=12.99 support=12.75 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=18.07 liquidity=20303590.0 spike=0.1
- JUFO.CA: score=20.07 buy_ready=False sector_rank=10 price=26.95 support=24.29 resistance=28.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=59.07 liquidity=8001103.5 spike=0.15
- KABO.CA: score=23.4 buy_ready=True sector_rank=3 price=9.15 support=7.94 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=65.73 liquidity=23311598.0 spike=0.53
- KWIN.CA: score=25.87 buy_ready=True sector_rank=12 price=112.36 support=84.08 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=63.53 liquidity=44259288.0 spike=0.66
- KZPC.CA: score=23.87 buy_ready=False sector_rank=12 price=13.14 support=8.69 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=72.36 liquidity=13001688.0 spike=0.24
- LCSW.CA: score=28.82 buy_ready=True sector_rank=4 price=36.0 support=32.12 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=55.59 liquidity=67332688.0 spike=2.21
- LUTS.CA: score=21.87 buy_ready=False sector_rank=12 price=0.99 support=0.65 resistance=1.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=50.84 liquidity=93002288.0 spike=0.36
- MAAL.CA: score=28.39 buy_ready=True sector_rank=12 price=9.6 support=8.32 resistance=9.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=60.24 liquidity=16710272.0 spike=1.26
- MASR.CA: score=20.87 buy_ready=False sector_rank=12 price=7.75 support=7.45 resistance=8.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=57.97 liquidity=26370948.0 spike=0.41
- MBSC.CA: score=9.4 buy_ready=False sector_rank=4 price=435.0 support=435.0 resistance=464.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27399052.0 spike=0.29
- MCQE.CA: score=24.4 buy_ready=True sector_rank=4 price=245.91 support=180.5 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=50.7 liquidity=39510856.0 spike=0.64
- MCRO.CA: score=16.87 buy_ready=False sector_rank=12 price=1.5 support=1.44 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=34.62 liquidity=27726812.0 spike=0.24
- MENA.CA: score=11.18 buy_ready=False sector_rank=13 price=6.84 support=6.59 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=38.74 liquidity=2401355.25 spike=0.41
- MEPA.CA: score=23.85 buy_ready=True sector_rank=12 price=1.91 support=1.8 resistance=2.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=53.06 liquidity=7980190.5 spike=0.26
- MFPC.CA: score=13.88 buy_ready=False sector_rank=8 price=45.0 support=42.81 resistance=45.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=319369984.0 spike=3.24
- MFSC.CA: score=14.69 buy_ready=False sector_rank=12 price=50.42 support=48.0 resistance=57.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=59.45 liquidity=818977.81 spike=0.07
- MHOT.CA: score=9.6 buy_ready=False sector_rank=7 price=18.65 support=16.81 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=24.21 liquidity=2204058.75 spike=0.12
- MICH.CA: score=23.87 buy_ready=True sector_rank=12 price=51.5 support=46.3 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=64.61 liquidity=23485796.0 spike=0.56
- MILS.CA: score=22.74 buy_ready=True sector_rank=12 price=211.4 support=175.0 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=56.35 liquidity=8870738.0 spike=0.12
- MIPH.CA: score=14.63 buy_ready=False sector_rank=15 price=778.33 support=700.2 resistance=827.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=55.49 liquidity=3594724.5 spike=0.71
- MOED.CA: score=22.87 buy_ready=False sector_rank=12 price=0.83 support=0.66 resistance=0.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=79.33 liquidity=53890016.0 spike=0.51
- MOIL.CA: score=14.45 buy_ready=False sector_rank=9 price=0.68 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=53.38 liquidity=110710.88 spike=0.37
- MOIN.CA: score=17.33 buy_ready=False sector_rank=12 price=33.17 support=25.12 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=43.54 liquidity=5462432.0 spike=0.16
- MOSC.CA: score=17.94 buy_ready=True sector_rank=12 price=323.85 support=290.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=54.52 liquidity=4067859.0 spike=0.25
- MPCI.CA: score=25.87 buy_ready=True sector_rank=12 price=448.54 support=302.0 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=63.6 liquidity=128173488.0 spike=0.66
- MPCO.CA: score=21.99 buy_ready=False sector_rank=11 price=2.11 support=1.91 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=40.54 liquidity=20337532.0 spike=0.19
- MPRC.CA: score=18.03 buy_ready=False sector_rank=12 price=43.51 support=39.5 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=25.32 liquidity=55567788.0 spike=1.58
- MTIE.CA: score=16.5 buy_ready=False sector_rank=21 price=8.83 support=8.25 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=41.99 liquidity=34059028.0 spike=0.5
- NAHO.CA: score=10.96 buy_ready=False sector_rank=12 price=0.14 support=0.1 resistance=0.16 source=Yahoo Finance as_of=2026-08-31T21:00:00+00:00 freshness=FRESH RSI=83.05 liquidity=89164.31 spike=0.89
- NCCW.CA: score=29.89 buy_ready=True sector_rank=12 price=6.39 support=5.59 resistance=7.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=58.45 liquidity=74437912.0 spike=3.01
- NEDA.CA: score=9.19 buy_ready=False sector_rank=12 price=2.73 support=2.7 resistance=2.97 source=Yahoo Finance as_of=2026-08-31T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=313316.64 spike=0.42
- NHPS.CA: score=23.87 buy_ready=True sector_rank=12 price=89.54 support=82.5 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=40.61 liquidity=10126523.0 spike=0.32
- NINH.CA: score=23.87 buy_ready=False sector_rank=12 price=22.5 support=21.53 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=54.78 liquidity=14327179.0 spike=0.33
- NIPH.CA: score=16.04 buy_ready=False sector_rank=15 price=336.94 support=260.0 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=32.45 liquidity=63290184.0 spike=0.18
- OBRI.CA: score=23.87 buy_ready=False sector_rank=12 price=33.7 support=31.62 resistance=34.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=61.15 liquidity=20104744.0 spike=0.67
- OCDI.CA: score=16.78 buy_ready=False sector_rank=13 price=31.73 support=28.82 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=33.46 liquidity=47929720.0 spike=0.38
- OCPH.CA: score=9.35 buy_ready=False sector_rank=12 price=248.69 support=235.0 resistance=341.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=20.17 liquidity=4478264.0 spike=0.2
- ODIN.CA: score=16.87 buy_ready=False sector_rank=12 price=2.96 support=2.87 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=27.85 liquidity=14053870.0 spike=0.29
- OFH.CA: score=23.87 buy_ready=True sector_rank=12 price=1.02 support=0.71 resistance=1.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=68.27 liquidity=31463690.0 spike=0.29
- OIH.CA: score=26.4 buy_ready=False sector_rank=2 price=1.98 support=1.5 resistance=2.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=66258856.0 spike=0.41
- OLFI.CA: score=19.06 buy_ready=False sector_rank=10 price=22.28 support=22.07 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=39.22 liquidity=9989661.0 spike=0.17
- ORAS.CA: score=7.6 buy_ready=False sector_rank=18 price=833.83 support=824.0 resistance=843.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=62286724.0 spike=1.0
- ORHD.CA: score=23.78 buy_ready=True sector_rank=13 price=42.28 support=40.28 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=43.22 liquidity=116585904.0 spike=0.79
- ORWE.CA: score=27.4 buy_ready=True sector_rank=3 price=26.74 support=23.07 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=56.53 liquidity=32934120.0 spike=0.39
- PHAR.CA: score=16.04 buy_ready=False sector_rank=15 price=126.01 support=126.85 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=20.94 liquidity=68058240.0 spike=0.15
- PHDC.CA: score=13.78 buy_ready=False sector_rank=13 price=14.59 support=14.5 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=34.41 liquidity=101774440.0 spike=0.43
- PHTV.CA: score=7.79 buy_ready=False sector_rank=12 price=353.15 support=311.27 resistance=447.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=22.39 liquidity=914198.19 spike=0.37
- POUL.CA: score=28.07 buy_ready=True sector_rank=10 price=39.93 support=36.6 resistance=40.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=50.4 liquidity=13488577.0 spike=0.55
- PRCL.CA: score=12.39 buy_ready=False sector_rank=4 price=32.19 support=30.9 resistance=37.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=40.78 liquidity=2991028.25 spike=0.12
- PRDC.CA: score=27.78 buy_ready=True sector_rank=13 price=9.3 support=8.7 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=63.36 liquidity=52492784.0 spike=0.73
- PRMH.CA: score=25.97 buy_ready=True sector_rank=12 price=2.79 support=2.28 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=41.9 liquidity=15914525.0 spike=1.05
- RACC.CA: score=13.87 buy_ready=False sector_rank=12 price=9.62 support=9.4 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=33.54 liquidity=11462899.0 spike=0.55
- RAKT.CA: score=3.52 buy_ready=False sector_rank=12 price=22.2 support=21.4 resistance=24.0 source=Yahoo Finance as_of=2026-08-31T21:00:00+00:00 freshness=FRESH RSI=26.97 liquidity=331934.41 spike=1.16
- RAYA.CA: score=19.38 buy_ready=False sector_rank=19 price=7.18 support=6.95 resistance=7.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=49.6 liquidity=21448944.0 spike=0.34
- RMDA.CA: score=16.04 buy_ready=False sector_rank=15 price=5.94 support=5.76 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=26.43 liquidity=12533623.0 spike=0.1
- ROTO.CA: score=8.86 buy_ready=False sector_rank=12 price=44.13 support=43.7 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=21.97 liquidity=4986065.5 spike=0.23
- RREI.CA: score=21.87 buy_ready=False sector_rank=12 price=4.41 support=4.24 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=42.6 liquidity=15049628.0 spike=0.33
- RTVC.CA: score=16.48 buy_ready=True sector_rank=12 price=4.1 support=3.73 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=66.35 liquidity=2611051.25 spike=0.31
- RUBX.CA: score=23.87 buy_ready=True sector_rank=12 price=12.8 support=12.2 resistance=13.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=54.31 liquidity=10028167.0 spike=0.56
- SAUD.CA: score=21.79 buy_ready=True sector_rank=6 price=23.79 support=21.61 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=63.88 liquidity=7391406.0 spike=0.35
- SCEM.CA: score=24.4 buy_ready=True sector_rank=4 price=101.28 support=78.0 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=53.85 liquidity=112541000.0 spike=0.5
- SCFM.CA: score=16.1 buy_ready=False sector_rank=12 price=279.3 support=273.1 resistance=305.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=45.96 liquidity=4228016.0 spike=0.26
- SCTS.CA: score=11.23 buy_ready=False sector_rank=20 price=616.06 support=603.13 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=49.08 liquidity=1310049.63 spike=0.15
- SDTI.CA: score=18.87 buy_ready=False sector_rank=12 price=69.92 support=60.6 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=33.86 liquidity=19706184.0 spike=0.76
- SEIG.CA: score=12.18 buy_ready=False sector_rank=12 price=259.47 support=256.01 resistance=293.0 source=Yahoo Finance as_of=2026-08-31T21:00:00+00:00 freshness=FRESH RSI=38.46 liquidity=306953.01 spike=0.1
- SIPC.CA: score=23.87 buy_ready=True sector_rank=12 price=5.05 support=4.1 resistance=5.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=52.41 liquidity=27200056.0 spike=0.5
- SKPC.CA: score=14.4 buy_ready=False sector_rank=8 price=18.76 support=17.91 resistance=18.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=342837312.0 spike=4.15
- SMFR.CA: score=12.09 buy_ready=False sector_rank=12 price=254.94 support=228.88 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=31.29 liquidity=5220794.5 spike=0.19
- SNFC.CA: score=12.21 buy_ready=False sector_rank=12 price=10.38 support=10.3 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=37.58 liquidity=4341031.5 spike=0.3
- SPIN.CA: score=19.18 buy_ready=True sector_rank=3 price=19.17 support=15.32 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=67.08 liquidity=3777426.75 spike=0.09
- SPMD.CA: score=7.21 buy_ready=False sector_rank=12 price=0.45 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=21.92 liquidity=3335483.0 spike=0.18
- SUGR.CA: score=24.47 buy_ready=True sector_rank=10 price=58.3 support=46.53 resistance=61.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=67.09 liquidity=70274728.0 spike=1.2
- SVCE.CA: score=27.19 buy_ready=False sector_rank=12 price=12.7 support=9.16 resistance=12.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=75.76 liquidity=459154016.0 spike=3.16
- SWDY.CA: score=24.4 buy_ready=True sector_rank=5 price=129.45 support=95.48 resistance=133.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=68.52 liquidity=49793392.0 spike=0.46
- TALM.CA: score=15.61 buy_ready=False sector_rank=20 price=18.04 support=17.11 resistance=20.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=43.25 liquidity=5687760.0 spike=0.16
- TMGH.CA: score=18.78 buy_ready=False sector_rank=13 price=96.2 support=94.9 resistance=99.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=46.1 liquidity=129091488.0 spike=0.5
- TRTO.CA: score=3.97 buy_ready=False sector_rank=12 price=0.07 support=0.06 resistance=0.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=93771.56 spike=5.64
- UEFM.CA: score=12.35 buy_ready=False sector_rank=12 price=537.15 support=531.0 resistance=589.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=42.2 liquidity=474734.91 spike=0.12
- UEGC.CA: score=13.87 buy_ready=False sector_rank=12 price=1.77 support=1.74 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=13.67 liquidity=39630572.0 spike=0.88
- UNIP.CA: score=8.69 buy_ready=False sector_rank=12 price=0.37 support=0.35 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=32.04 liquidity=4822410.5 spike=0.16
- UNIT.CA: score=8.22 buy_ready=False sector_rank=13 price=18.62 support=17.8 resistance=23.0 source=Yahoo Finance as_of=2026-08-31T21:00:00+00:00 freshness=FRESH RSI=24.49 liquidity=1442789.39 spike=0.14
- WCDF.CA: score=11.01 buy_ready=False sector_rank=12 price=690.72 support=643.0 resistance=696.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8859112.0 spike=2.64
- WKOL.CA: score=17.4 buy_ready=True sector_rank=12 price=346.45 support=315.0 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=54.9 liquidity=3531583.75 spike=0.1
- ZEOT.CA: score=23.87 buy_ready=True sector_rank=12 price=14.5 support=12.2 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=64.15 liquidity=12408602.0 spike=0.58
- ZMID.CA: score=22.78 buy_ready=False sector_rank=13 price=9.35 support=7.06 resistance=9.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=76.01 liquidity=196821648.0 spike=0.79

## Backtesting Lite
- CSAG.CA: 180d return=30.8%, max drawdown=-28.0%, MA20>MA50 days last20=20, as_of=2026-08-31T21:00:00+00:00
- NCCW.CA: 180d return=-0.49%, max drawdown=-30.87%, MA20>MA50 days last20=8, as_of=2026-08-31T21:00:00+00:00
- ATLC.CA: 180d return=74.64%, max drawdown=-16.0%, MA20>MA50 days last20=20, as_of=2026-08-31T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CSAG.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Canal Shipping Agencies summary=Canal Shipping Agencies targets EGP 970m net profits in FY26/27; Canal Shipping Agencies’ stock rebounds; Canal Shipping Agencies mulls EGP 100m capital raise
  - Canal Shipping Agencies targets EGP 970m net profits in FY26/27: https://english.mubasher.info/news/4582423/Canal-Shipping-Agencies-targets-EGP-970m-net-profits-in-FY26-27/
  - Canal Shipping Agencies’ stock rebounds: https://english.mubasher.info/news/4564447/Canal-Shipping-Agencies-stock-rebounds/
  - Canal Shipping Agencies mulls EGP 100m capital raise: https://english.mubasher.info/news/4191441/Canal-Shipping-Agencies-mulls-EGP-100m-capital-raise/
- NCCW.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Nasr Company for Civil Works summary=Nasr for Civil Works unveils EGP 150m capital increase; Arabia Investments, Nasr Company for Civil Works unveil capital hike; Nasr Company for Civil Works’ consortium signs EUR 46m agreement with Uganda
  - Nasr for Civil Works unveils EGP 150m capital increase: https://english.mubasher.info/news/4550493/Nasr-for-Civil-Works-unveils-EGP-150m-capital-increase/
  - Arabia Investments, Nasr Company for Civil Works unveil capital hike: https://english.mubasher.info/news/4284206/Arabia-Investments-Nasr-Company-for-Civil-Works-unveil-capital-hike/
  - Nasr Company for Civil Works’ consortium signs EUR 46m agreement with Uganda: https://english.mubasher.info/news/4249759/Nasr-Company-for-Civil-Works-consortium-signs-EUR-46m-agreement-with-Uganda/
- ATLC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Al Tawfeek Leasing summary=Evidence rejected for ATLC.CA: source text did not clearly match ATLC.CA / Al Tawfeek Leasing.
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- ARCC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=609 sources=3 expected=Arabian Cement Company summary=Arabian Cement to pay out EGP 2bn dividends for 2025; Arabian Cement’s EGM approves nearly EGP 8m capital cut; Arabian Cement’s consolidated profits near EGP 3.6bn in 2025
  - Arabian Cement to pay out EGP 2bn dividends for 2025: https://english.mubasher.info/news/4587912/Arabian-Cement-to-pay-out-EGP-2bn-dividends-for-2025/
  - Arabian Cement’s EGM approves nearly EGP 8m capital cut: https://english.mubasher.info/news/4583762/Arabian-Cement-s-EGM-approves-nearly-EGP-8m-capital-cut/
  - Arabian Cement’s consolidated profits near EGP 3.6bn in 2025: https://english.mubasher.info/news/4562679/Arabian-Cement-s-consolidated-profits-near-EGP-3-6bn-in-2025/
- MAAL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Marseille Almasreia Alkhalegeya For Holding Investment SAE summary=Evidence rejected for MAAL.CA: source text did not clearly match MAAL.CA / Marseille Almasreia Alkhalegeya For Holding Investment SAE.
- POUL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Poultry summary=Cairo Poultry stock approaching historic peak – Analysis; Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA; Cairo Poultry sees EGP 871m block-trading deal
  - Cairo Poultry stock approaching historic peak – Analysis: https://english.mubasher.info/news/4539104/Cairo-Poultry-stock-approaching-historic-peak-Analysis/
  - Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA: https://english.mubasher.info/news/3962334/Cairo-Poultry-cancels-commercial-license-in-Dubai-s-JAFZA/
  - Cairo Poultry sees EGP 871m block-trading deal: https://english.mubasher.info/news/3862165/Cairo-Poultry-sees-EGP-871m-block-trading-deal/
- GIHD.CA: status=OLD_ACCEPTED latest=2016-01-01 age_days=3897 sources=3 expected=Gharbia Islamic Housing Development Company summary=Gharbia Islamic Housing to discuss raising capital mid-December; Gharbia Islamic Housing to distribute EGP 0.2/shr; Gharbia Islamic Housing profits fall 46% in 2016
  - Gharbia Islamic Housing to discuss raising capital mid-December: https://english.mubasher.info/news/3147599/Gharbia-Islamic-Housing-to-discuss-raising-capital-mid-December/
  - Gharbia Islamic Housing to distribute EGP 0.2/shr: https://english.mubasher.info/news/3082262/Gharbia-Islamic-Housing-to-distribute-EGP-0-2-shr/
  - Gharbia Islamic Housing profits fall 46% in 2016: https://english.mubasher.info/news/3068305/Gharbia-Islamic-Housing-profits-fall-46-in-2016/

## Warnings
- Evidence for CSAG.CA matches the company but no source/report date was detected.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence for NCCW.CA matches the company but no source/report date was detected.
- Evidence rejected for ATLC.CA: source text did not clearly match ATLC.CA / Al Tawfeek Leasing.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence for ARCC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for MAAL.CA: source text did not clearly match MAAL.CA / Marseille Almasreia Alkhalegeya For Holding Investment SAE.
- Evidence for POUL.CA matches the company but no source/report date was detected.
- Evidence for GIHD.CA matches the company but appears old; latest detected date is 2016-01-01.
