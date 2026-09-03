# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-09-03T10:07:24.549473+00:00
Generated Cairo: 2026-09-03 13:07
Run timing: target 08:45 Cairo | generated Cairo 2026-09-03 13:07 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-03 13:04

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 55
- Data quality issues: 1
- Tradeable price/liquidity tickers: 178/189
- Top sector: Transportation & Logistics

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, September 03
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 60.0% / above MA50 75.0%
- EGX70 regime: MIXED / above MA20 48.72% / above MA50 74.36%
- Sector breadth: 42.86%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- ORAS.CA: liquidity=342173856.0 spike=1.0 score=7.6
- EGCH.CA: liquidity=251305136.0 spike=1.83 score=29.06
- BIOC.CA: liquidity=234081424.0 spike=0.98 score=8.58
- SVCE.CA: liquidity=216275712.0 spike=1.25 score=23.08
- COMI.CA: liquidity=193734880.0 spike=0.37 score=24.4

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner fell back to HOLD as no ticket satisfied evidence, liquidity, freshness and technical filters despite EGX30 bullish bias and EGX70 mixed tone.
- EGX30 shows bullish breadth (60% above MA20, 75% above MA50) supporting normal selection, while EGX70 is mixed with weaker MA20 breadth (48.7%).
- Sector breadth is 42.86%; leading sectors are Transportation & Logistics, Building Materials, Basic Resources & Chemicals, but overall breadth is moderate.
- Top scanner rows (e.g., ALCN.CA, FERC.CA, EGCH.CA) display accumulation spikes and bullish watch outlooks, yet they failed evidence/freshness/technical gates, prompting the HOLD fallback.
- Risk mode is SELECTIVE_SWING_TRADES_ONLY with buy‑only selective, reflecting uncertainty from mixed EGX70 and cooling liquidity in several names.

## Top Liquidity Spikes
- EPPK.CA: spike=3.07 liquidity=3551063.0 outlook=WEAK_OR_RISKY score=20.96 buy_ready=False
- ALCN.CA: spike=2.91 liquidity=89543840.0 outlook=BULLISH_WATCH score=100 buy_ready=True
- MFSC.CA: spike=2.68 liquidity=30578358.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MOIN.CA: spike=2.44 liquidity=86137880.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RAYA.CA: spike=2.33 liquidity=143113408.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Transportation & Logistics: score=13.16 5d=6.87% 20d=10.35% aboveMA50=100.0%
- #2 Building Materials: score=10.69 5d=1.96% 20d=25.32% aboveMA50=83.33%
- #3 Basic Resources & Chemicals: score=10.52 5d=5.33% 20d=10.77% aboveMA50=80.0%
- #4 Investment Holding: score=9.89 5d=2.61% 20d=12.38% aboveMA50=100.0%
- #5 Textiles: score=9.37 5d=-0.54% 20d=16.59% aboveMA50=100.0%
- #6 Telecommunications: score=8.26 5d=1.12% 20d=2.71% aboveMA50=100.0%
- #7 Banking & Financials: score=6.67 5d=0.59% 20d=3.84% aboveMA50=100.0%
- #8 Energy & Petrochemicals: score=6.21 5d=2.81% 20d=0.48% aboveMA50=75.0%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ALCN.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- FERC.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- EGCH.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- ISMQ.CA: BULLISH_WATCH score=96 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- CSAG.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ARCC.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- MCQE.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- BINV.CA: BULLISH_WATCH score=85.89 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- KABO.CA: BULLISH_WATCH score=84.37 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- CANA.CA: BULLISH_WATCH score=81.67 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.

## BUY-Ready Candidates
- ALCN.CA: rank=33.22 outlook=BULLISH_WATCH outlook_score=100 sector_rank=1 price=31.91 support=30.03 resistance=32.8 liquidity=89543840.0
- FERC.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=100 sector_rank=3 price=82.22 support=76.7 resistance=87.3 liquidity=40743676.0
- EGCH.CA: rank=29.06 outlook=BULLISH_WATCH outlook_score=100 sector_rank=3 price=14.43 support=13.3 resistance=14.79 liquidity=251305136.0
- MBSC.CA: rank=28.4 outlook=BULLISH_WATCH outlook_score=72 sector_rank=2 price=418.3 support=253.1 resistance=470.0 liquidity=22967222.0
- ARCC.CA: rank=28.4 outlook=BULLISH_WATCH outlook_score=86 sector_rank=2 price=76.44 support=58.25 resistance=91.72 liquidity=24286390.0
- CERA.CA: rank=27.58 outlook=BULLISH_WATCH outlook_score=75.96 sector_rank=13 price=1.41 support=1.22 resistance=1.45 liquidity=25120968.0
- ETRS.CA: rank=27.58 outlook=CONSTRUCTIVE outlook_score=68.96 sector_rank=13 price=11.25 support=10.43 resistance=11.66 liquidity=11719386.0
- ISMQ.CA: rank=27.4 outlook=BULLISH_WATCH outlook_score=96 sector_rank=3 price=9.3 support=9.0 resistance=9.97 liquidity=27395180.0
- MASR.CA: rank=26.78 outlook=BULLISH_WATCH outlook_score=79.96 sector_rank=13 price=7.92 support=7.45 resistance=8.05 liquidity=99957528.0
- OIH.CA: rank=26.4 outlook=CONSTRUCTIVE outlook_score=67.89 sector_rank=4 price=2.0 support=1.57 resistance=2.11 liquidity=39330832.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=21.58 buy_ready=False sector_rank=13 price=303.76 support=288.0 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=50.7 liquidity=12204638.0 spike=0.27
- ABUK.CA: score=25.02 buy_ready=False sector_rank=3 price=90.17 support=73.2 resistance=94.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=85.09 liquidity=185390112.0 spike=1.31
- ACAMD.CA: score=13.58 buy_ready=False sector_rank=13 price=2.06 support=1.95 resistance=2.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=28.89 liquidity=25202652.0 spike=0.46
- ACGC.CA: score=19.52 buy_ready=False sector_rank=5 price=13.75 support=10.36 resistance=14.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=72.57 liquidity=7117496.0 spike=0.17
- ADCI.CA: score=17.01 buy_ready=True sector_rank=13 price=297.79 support=274.0 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=3425116.0 spike=0.16
- ADIB.CA: score=17.4 buy_ready=False sector_rank=7 price=52.2 support=51.81 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=26762316.0 spike=0.4
- ADPC.CA: score=14.65 buy_ready=False sector_rank=13 price=3.97 support=3.85 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=29.52 liquidity=8061343.0 spike=0.19
- AFDI.CA: score=14.12 buy_ready=False sector_rank=13 price=55.25 support=53.54 resistance=69.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=26.42 liquidity=7535228.0 spike=0.22
- AFMC.CA: score=16.58 buy_ready=False sector_rank=13 price=173.0 support=175.2 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=22.13 liquidity=36126196.0 spike=0.29
- AJWA.CA: score=13.58 buy_ready=False sector_rank=13 price=179.08 support=176.0 resistance=202.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=8.21 liquidity=17628310.0 spike=0.29
- ALCN.CA: score=33.22 buy_ready=True sector_rank=1 price=31.91 support=30.03 resistance=32.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=56.44 liquidity=89543840.0 spike=2.91
- ALUM.CA: score=17.81 buy_ready=True sector_rank=13 price=28.52 support=24.35 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=55.19 liquidity=4228464.5 spike=0.15
- AMER.CA: score=21.36 buy_ready=False sector_rank=15 price=5.55 support=5.3 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=35.04 liquidity=14409130.0 spike=0.15
- AMES.CA: score=9.3 buy_ready=False sector_rank=13 price=86.87 support=85.02 resistance=94.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=131649016.0 spike=1.36
- AMIA.CA: score=17.51 buy_ready=False sector_rank=13 price=19.34 support=10.6 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=80.43 liquidity=6927923.0 spike=0.11
- AMOC.CA: score=23.4 buy_ready=False sector_rank=8 price=13.35 support=9.01 resistance=14.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=81.25 liquidity=99672856.0 spike=0.56
- APSW.CA: score=7.89 buy_ready=False sector_rank=13 price=8.62 support=8.41 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=48.18 liquidity=307594.31 spike=0.2
- ARAB.CA: score=25.36 buy_ready=True sector_rank=15 price=0.26 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=60.34 liquidity=30301016.0 spike=0.32
- ARCC.CA: score=28.4 buy_ready=True sector_rank=2 price=76.44 support=58.25 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=57.02 liquidity=24286390.0 spike=0.22
- AREH.CA: score=12.54 buy_ready=False sector_rank=13 price=1.41 support=1.39 resistance=1.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=35.48 liquidity=3957610.75 spike=0.14
- ARVA.CA: score=8.58 buy_ready=False sector_rank=13 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=15.53 buy_ready=False sector_rank=13 price=63.0 support=62.01 resistance=69.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=30.6 liquidity=8943483.0 spike=0.22
- ASPI.CA: score=21.96 buy_ready=False sector_rank=13 price=0.43 support=0.43 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=36.58 liquidity=47488888.0 spike=1.19
- ATLC.CA: score=21.41 buy_ready=False sector_rank=19 price=7.35 support=5.15 resistance=8.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=83.45 liquidity=27806128.0 spike=0.88
- ATQA.CA: score=22.4 buy_ready=False sector_rank=3 price=11.93 support=10.09 resistance=12.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=77.61 liquidity=57279488.0 spike=0.57
- AXPH.CA: score=14.3 buy_ready=False sector_rank=13 price=1684.74 support=1260.0 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=92.42 liquidity=3711215.75 spike=0.28
- BINV.CA: score=22.11 buy_ready=True sector_rank=4 price=50.53 support=46.25 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=55.62 liquidity=5705313.5 spike=0.53
- BIOC.CA: score=8.58 buy_ready=False sector_rank=13 price=333.09 support=316.41 resistance=353.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=234081424.0 spike=0.98
- BTFH.CA: score=16.41 buy_ready=False sector_rank=19 price=3.02 support=2.94 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=29708884.0 spike=0.17
- CAED.CA: score=17.45 buy_ready=False sector_rank=13 price=140.26 support=118.01 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=59.8 liquidity=5869772.0 spike=0.16
- CANA.CA: score=25.2 buy_ready=True sector_rank=7 price=43.0 support=38.61 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=48.79 liquidity=23920790.0 spike=1.4
- CCAP.CA: score=24.4 buy_ready=False sector_rank=4 price=5.89 support=5.18 resistance=6.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=72.93 liquidity=151102624.0 spike=0.24
- CCRS.CA: score=23.58 buy_ready=False sector_rank=13 price=2.55 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=53.85 liquidity=10366443.0 spike=0.2
- CEFM.CA: score=16.73 buy_ready=False sector_rank=13 price=145.5 support=132.0 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=72.43 liquidity=5149468.5 spike=0.25
- CERA.CA: score=27.58 buy_ready=True sector_rank=13 price=1.41 support=1.22 resistance=1.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=58.97 liquidity=25120968.0 spike=0.88
- CFGH.CA: score=14.12 buy_ready=False sector_rank=13 price=0.12 support=0.1 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=85.19 liquidity=34472.33 spike=1.75
- CICH.CA: score=9.45 buy_ready=False sector_rank=19 price=12.11 support=12.0 resistance=13.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=38.46 liquidity=2037597.63 spike=0.31
- CIEB.CA: score=21.95 buy_ready=True sector_rank=7 price=25.29 support=24.0 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=59.58 liquidity=5545456.5 spike=0.38
- CIRA.CA: score=12.24 buy_ready=False sector_rank=12 price=34.23 support=32.1 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=31.51 liquidity=5651583.5 spike=0.16
- CLHO.CA: score=23.64 buy_ready=True sector_rank=11 price=17.6 support=16.95 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=65.42 liquidity=41170620.0 spike=0.53
- CNFN.CA: score=16.51 buy_ready=False sector_rank=19 price=4.8 support=4.73 resistance=5.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=9101574.0 spike=0.51
- COMI.CA: score=24.4 buy_ready=True sector_rank=7 price=139.5 support=135.35 resistance=142.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=49.07 liquidity=193734880.0 spike=0.37
- COPR.CA: score=21.58 buy_ready=False sector_rank=13 price=0.48 support=0.4 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=61.85 liquidity=25341404.0 spike=0.28
- COSG.CA: score=23.58 buy_ready=True sector_rank=13 price=1.87 support=1.69 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=51.35 liquidity=16542029.0 spike=0.31
- CPCI.CA: score=16.1 buy_ready=True sector_rank=13 price=545.92 support=483.0 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=60.35 liquidity=2513045.25 spike=0.29
- CSAG.CA: score=23.42 buy_ready=True sector_rank=1 price=41.67 support=36.07 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=50.19 liquidity=6016002.0 spike=0.22
- DAPH.CA: score=8.58 buy_ready=False sector_rank=13 price=128.17 support=128.03 resistance=140.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37974144.0 spike=0.53
- DEIN.CA: score=11.58 buy_ready=False sector_rank=13 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance as_of=2026-09-01T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=8.24 buy_ready=False sector_rank=16 price=28.39 support=27.79 resistance=30.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=31.76 liquidity=1926803.75 spike=0.11
- DSCW.CA: score=16.58 buy_ready=False sector_rank=13 price=1.94 support=1.84 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=23.26 liquidity=22952906.0 spike=0.27
- DTPP.CA: score=23.58 buy_ready=True sector_rank=13 price=302.21 support=244.1 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=51.39 liquidity=11411861.0 spike=0.3
- EALR.CA: score=15.84 buy_ready=False sector_rank=13 price=388.46 support=376.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=50.26 liquidity=4255425.5 spike=0.11
- EASB.CA: score=10.78 buy_ready=False sector_rank=13 price=7.38 support=7.05 resistance=8.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=2197431.0 spike=0.28
- EAST.CA: score=19.32 buy_ready=False sector_rank=16 price=35.9 support=35.0 resistance=37.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=44.19 liquidity=14230285.0 spike=0.23
- EBSC.CA: score=21.74 buy_ready=True sector_rank=13 price=2.17 support=1.88 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=68.29 liquidity=8151359.0 spike=0.58
- ECAP.CA: score=8.27 buy_ready=False sector_rank=13 price=33.5 support=31.16 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=26.83 liquidity=4681544.0 spike=0.26
- EDFM.CA: score=16.29 buy_ready=True sector_rank=13 price=423.59 support=390.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=59.18 liquidity=2424649.75 spike=1.14
- EEII.CA: score=16.3 buy_ready=False sector_rank=13 price=2.35 support=2.4 resistance=2.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=8718168.0 spike=1.0
- EFIC.CA: score=12.62 buy_ready=False sector_rank=3 price=193.55 support=193.0 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=20.29 liquidity=8223378.0 spike=0.18
- EFID.CA: score=21.32 buy_ready=False sector_rank=16 price=30.0 support=29.71 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=37.61 liquidity=60796072.0 spike=0.71
- EFIH.CA: score=20.23 buy_ready=False sector_rank=20 price=23.22 support=22.16 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=36.52 liquidity=55140240.0 spike=0.48
- EGAL.CA: score=24.4 buy_ready=False sector_rank=3 price=374.98 support=296.25 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=78.04 liquidity=66968468.0 spike=0.42
- EGAS.CA: score=24.4 buy_ready=True sector_rank=8 price=60.03 support=55.21 resistance=63.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=49.67 liquidity=22282216.0 spike=0.96
- EGBE.CA: score=12.41 buy_ready=False sector_rank=7 price=0.53 support=0.5 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=40.48 liquidity=8393.9 spike=0.04
- EGCH.CA: score=29.06 buy_ready=True sector_rank=3 price=14.43 support=13.3 resistance=14.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=48.73 liquidity=251305136.0 spike=1.83
- EGSA.CA: score=14.23 buy_ready=False sector_rank=6 price=8.96 support=8.65 resistance=9.0 source=Yahoo Finance as_of=2026-09-01T21:00:00+00:00 freshness=FRESH RSI=89.47 liquidity=7598.08 spike=1.41
- EGTS.CA: score=6.89 buy_ready=False sector_rank=15 price=16.81 support=16.17 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=26.76 liquidity=3537867.75 spike=0.1
- EHDR.CA: score=20.92 buy_ready=False sector_rank=13 price=2.85 support=2.8 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=9331397.0 spike=0.29
- EKHO.CA: score=10.4 buy_ready=False sector_rank=8 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-09-01T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=18.23 buy_ready=False sector_rank=9 price=2.11 support=2.04 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=25652126.0 spike=0.4
- ELKA.CA: score=25.58 buy_ready=True sector_rank=13 price=1.83 support=1.7 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=17262046.0 spike=0.25
- ELNA.CA: score=4.89 buy_ready=False sector_rank=13 price=36.83 support=36.1 resistance=38.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=30.42 liquidity=302095.5 spike=0.81
- ELSH.CA: score=18.58 buy_ready=False sector_rank=13 price=13.46 support=12.97 resistance=14.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=41.1 liquidity=13049117.0 spike=0.27
- ELWA.CA: score=13.06 buy_ready=False sector_rank=13 price=1.85 support=1.62 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=58.82 liquidity=479005.34 spike=0.2
- EMFD.CA: score=22.42 buy_ready=False sector_rank=15 price=14.28 support=11.51 resistance=13.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=91.87 liquidity=147664048.0 spike=1.03
- ENGC.CA: score=18.58 buy_ready=False sector_rank=13 price=44.0 support=41.8 resistance=54.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=37.05 liquidity=6993641.0 spike=0.25
- EOSB.CA: score=15.59 buy_ready=False sector_rank=13 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-09-01T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=5206.12 spike=0.11
- EPCO.CA: score=9.17 buy_ready=False sector_rank=13 price=11.17 support=10.8 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=34.15 liquidity=2582029.75 spike=0.15
- EPPK.CA: score=10.28 buy_ready=False sector_rank=13 price=10.39 support=10.84 resistance=15.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=26.32 liquidity=3551063.0 spike=3.07
- ETEL.CA: score=24.4 buy_ready=True sector_rank=6 price=114.56 support=107.0 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=53.03 liquidity=40466168.0 spike=0.28
- ETRS.CA: score=27.58 buy_ready=True sector_rank=13 price=11.25 support=10.43 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=63.59 liquidity=11719386.0 spike=0.43
- EXPA.CA: score=24.4 buy_ready=True sector_rank=7 price=21.51 support=19.8 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=47.06 liquidity=16619501.0 spike=0.45
- FAIT.CA: score=17.91 buy_ready=True sector_rank=7 price=43.51 support=37.01 resistance=45.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=62.7 liquidity=1508446.5 spike=0.19
- FAITA.CA: score=12.41 buy_ready=False sector_rank=7 price=0.99 support=0.97 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=54.84 liquidity=8241.28 spike=0.15
- FERC.CA: score=29.4 buy_ready=True sector_rank=3 price=82.22 support=76.7 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=49.91 liquidity=40743676.0 spike=2.0
- FWRY.CA: score=17.23 buy_ready=False sector_rank=20 price=18.93 support=18.66 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=47.73 liquidity=32041216.0 spike=0.2
- GBCO.CA: score=12.12 buy_ready=False sector_rank=21 price=29.08 support=27.51 resistance=32.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=30.97 liquidity=14263802.0 spike=0.28
- GDWA.CA: score=24.58 buy_ready=True sector_rank=13 price=0.83 support=0.77 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=58.9 liquidity=14587684.0 spike=0.29
- GGCC.CA: score=16.58 buy_ready=False sector_rank=13 price=0.87 support=0.83 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=25.08 liquidity=27362074.0 spike=0.5
- GIHD.CA: score=25.58 buy_ready=True sector_rank=13 price=71.61 support=58.01 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=59.84 liquidity=24060766.0 spike=0.96
- GMCI.CA: score=10.25 buy_ready=False sector_rank=13 price=1.85 support=1.83 resistance=2.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=805269.19 spike=1.43
- GRCA.CA: score=23.58 buy_ready=False sector_rank=13 price=80.0 support=54.7 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=70.97 liquidity=17973634.0 spike=0.29
- GSSC.CA: score=10.2 buy_ready=False sector_rank=13 price=308.42 support=281.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27461632.0 spike=1.81
- GTWL.CA: score=20.58 buy_ready=False sector_rank=13 price=225.17 support=98.01 resistance=247.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=78.58 liquidity=72105824.0 spike=0.25
- HDBK.CA: score=23.0 buy_ready=False sector_rank=7 price=119.09 support=84.0 resistance=119.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=87.15 liquidity=77786712.0 spike=1.8
- HELI.CA: score=25.36 buy_ready=True sector_rank=15 price=7.97 support=7.34 resistance=8.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=56.61 liquidity=125787360.0 spike=0.83
- HRHO.CA: score=11.41 buy_ready=False sector_rank=19 price=25.89 support=25.33 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=32.22 liquidity=34026004.0 spike=0.27
- ICID.CA: score=20.58 buy_ready=False sector_rank=13 price=17.93 support=8.0 resistance=18.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=82.64 liquidity=13826631.0 spike=0.49
- IDRE.CA: score=18.99 buy_ready=False sector_rank=13 price=52.62 support=51.16 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=50.67 liquidity=7404689.0 spike=0.49
- IFAP.CA: score=19.9 buy_ready=True sector_rank=10 price=21.11 support=20.2 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=36.13 liquidity=6181034.0 spike=0.18
- INFI.CA: score=21.58 buy_ready=False sector_rank=13 price=145.97 support=125.0 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=43.91 liquidity=11038201.0 spike=0.16
- IRON.CA: score=14.89 buy_ready=False sector_rank=3 price=29.97 support=29.82 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=40.39 liquidity=5491700.5 spike=0.42
- ISMA.CA: score=21.58 buy_ready=False sector_rank=13 price=33.02 support=30.7 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=46.22 liquidity=19334644.0 spike=0.75
- ISMQ.CA: score=27.4 buy_ready=True sector_rank=3 price=9.3 support=9.0 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=52.59 liquidity=27395180.0 spike=0.62
- ISPH.CA: score=16.64 buy_ready=False sector_rank=11 price=13.15 support=12.75 resistance=16.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=25.41 liquidity=53280912.0 spike=0.27
- JUFO.CA: score=22.32 buy_ready=False sector_rank=16 price=27.13 support=26.07 resistance=28.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=47.84 liquidity=21242352.0 spike=0.4
- KABO.CA: score=24.4 buy_ready=True sector_rank=5 price=9.18 support=7.94 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=37544740.0 spike=0.84
- KWIN.CA: score=8.58 buy_ready=False sector_rank=13 price=105.09 support=103.04 resistance=115.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27132732.0 spike=0.4
- KZPC.CA: score=17.97 buy_ready=True sector_rank=13 price=12.97 support=8.86 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=66.48 liquidity=6387548.0 spike=0.12
- LCSW.CA: score=24.4 buy_ready=False sector_rank=2 price=33.8 support=32.12 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=57.66 liquidity=26434712.0 spike=0.79
- LUTS.CA: score=8.58 buy_ready=False sector_rank=13 price=0.86 support=0.86 resistance=0.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=101846320.0 spike=0.39
- MAAL.CA: score=25.58 buy_ready=True sector_rank=13 price=9.95 support=8.32 resistance=9.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=68.24 liquidity=13560533.0 spike=1.0
- MASR.CA: score=26.78 buy_ready=True sector_rank=13 price=7.92 support=7.45 resistance=8.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=54.37 liquidity=99957528.0 spike=1.6
- MBSC.CA: score=28.4 buy_ready=True sector_rank=2 price=418.3 support=253.1 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=64.1 liquidity=22967222.0 spike=0.24
- MCQE.CA: score=25.65 buy_ready=True sector_rank=2 price=242.35 support=190.5 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=46.59 liquidity=9248627.0 spike=0.15
- MCRO.CA: score=23.58 buy_ready=True sector_rank=13 price=1.53 support=1.44 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=103170680.0 spike=0.93
- MENA.CA: score=4.39 buy_ready=False sector_rank=15 price=6.81 support=6.59 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=20.27 liquidity=1038438.69 spike=0.18
- MEPA.CA: score=23.46 buy_ready=True sector_rank=13 price=1.87 support=1.8 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=7874271.5 spike=0.27
- MFPC.CA: score=25.12 buy_ready=False sector_rank=3 price=45.69 support=36.95 resistance=46.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=84.07 liquidity=159702160.0 spike=1.36
- MFSC.CA: score=11.94 buy_ready=False sector_rank=13 price=53.63 support=51.45 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30578358.0 spike=2.68
- MHOT.CA: score=13.83 buy_ready=False sector_rank=17 price=18.32 support=16.81 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=47.6 liquidity=4580202.5 spike=0.25
- MICH.CA: score=23.58 buy_ready=True sector_rank=13 price=50.0 support=46.3 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=68.45 liquidity=22261400.0 spike=0.52
- MILS.CA: score=21.58 buy_ready=False sector_rank=13 price=201.39 support=179.05 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=58.39 liquidity=13400571.0 spike=0.19
- MIPH.CA: score=19.65 buy_ready=True sector_rank=11 price=789.39 support=700.2 resistance=827.36 source=Yahoo Finance as_of=2026-09-01T21:00:00+00:00 freshness=FRESH RSI=56.04 liquidity=5007100.86 spike=1.5
- MOED.CA: score=23.58 buy_ready=False sector_rank=13 price=0.81 support=0.67 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=70.41 liquidity=39444644.0 spike=0.37
- MOIL.CA: score=14.42 buy_ready=False sector_rank=8 price=0.68 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=51.35 liquidity=24289.69 spike=0.09
- MOIN.CA: score=11.46 buy_ready=False sector_rank=13 price=37.61 support=32.8 resistance=38.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=86137880.0 spike=2.44
- MOSC.CA: score=13.41 buy_ready=False sector_rank=13 price=318.69 support=292.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=50.54 liquidity=1823920.25 spike=0.11
- MPCI.CA: score=23.58 buy_ready=False sector_rank=13 price=432.69 support=310.05 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=73.97 liquidity=145282784.0 spike=0.74
- MPCO.CA: score=21.72 buy_ready=False sector_rank=10 price=2.11 support=1.94 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=44.12 liquidity=26496018.0 spike=0.26
- MPRC.CA: score=18.58 buy_ready=False sector_rank=13 price=42.79 support=39.5 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=42.96 liquidity=16254087.0 spike=0.42
- MTIE.CA: score=12.12 buy_ready=False sector_rank=21 price=8.61 support=8.25 resistance=11.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=31.86 liquidity=25468736.0 spike=0.37
- NAHO.CA: score=8.6 buy_ready=False sector_rank=13 price=0.14 support=0.1 resistance=0.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=78.43 liquidity=20774.52 spike=0.2
- NCCW.CA: score=22.58 buy_ready=False sector_rank=13 price=6.06 support=5.59 resistance=7.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=60.14 liquidity=25374832.0 spike=0.92
- NEDA.CA: score=9.04 buy_ready=False sector_rank=13 price=2.74 support=2.7 resistance=2.97 source=Yahoo Finance as_of=2026-09-01T21:00:00+00:00 freshness=FRESH RSI=52.24 liquidity=453722.08 spike=0.63
- NHPS.CA: score=20.29 buy_ready=False sector_rank=13 price=87.41 support=84.0 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=47.99 liquidity=8710846.0 spike=0.27
- NINH.CA: score=23.58 buy_ready=True sector_rank=13 price=23.75 support=21.53 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=65.1 liquidity=12788961.0 spike=0.29
- NIPH.CA: score=21.64 buy_ready=False sector_rank=11 price=342.98 support=266.01 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=35.12 liquidity=184803328.0 spike=0.53
- OBRI.CA: score=18.99 buy_ready=False sector_rank=13 price=33.59 support=31.62 resistance=34.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=56.83 liquidity=7403893.0 spike=0.25
- OCDI.CA: score=23.48 buy_ready=True sector_rank=15 price=33.63 support=29.6 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=36.2 liquidity=137681456.0 spike=1.06
- OCPH.CA: score=10.71 buy_ready=False sector_rank=13 price=252.57 support=235.0 resistance=341.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=24.16 liquidity=6121721.0 spike=0.28
- ODIN.CA: score=16.58 buy_ready=False sector_rank=13 price=2.88 support=2.87 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=32.35 liquidity=22018614.0 spike=0.46
- OFH.CA: score=23.58 buy_ready=True sector_rank=13 price=1.03 support=0.79 resistance=1.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=68.71 liquidity=79017336.0 spike=0.71
- OIH.CA: score=26.4 buy_ready=True sector_rank=4 price=2.0 support=1.57 resistance=2.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=63.93 liquidity=39330832.0 spike=0.25
- OLFI.CA: score=13.32 buy_ready=False sector_rank=16 price=22.25 support=22.07 resistance=26.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=19.16 liquidity=23719644.0 spike=0.4
- ORAS.CA: score=7.6 buy_ready=False sector_rank=18 price=862.11 support=831.51 resistance=890.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=342173856.0 spike=1.0
- ORHD.CA: score=23.36 buy_ready=True sector_rank=15 price=42.6 support=40.28 resistance=43.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=41.29 liquidity=69606080.0 spike=0.48
- ORWE.CA: score=24.4 buy_ready=True sector_rank=5 price=26.48 support=24.5 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=56.01 liquidity=14984998.0 spike=0.18
- PHAR.CA: score=16.64 buy_ready=False sector_rank=11 price=129.26 support=124.5 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=25.67 liquidity=159766576.0 spike=0.36
- PHDC.CA: score=13.36 buy_ready=False sector_rank=15 price=14.55 support=14.4 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=31.06 liquidity=76632152.0 spike=0.32
- PHTV.CA: score=7.82 buy_ready=False sector_rank=13 price=351.35 support=311.27 resistance=447.99 source=Yahoo Finance as_of=2026-09-01T21:00:00+00:00 freshness=FRESH RSI=30.24 liquidity=1234292.57 spike=0.63
- POUL.CA: score=25.32 buy_ready=True sector_rank=16 price=39.06 support=36.97 resistance=40.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=48.24 liquidity=13543637.0 spike=0.56
- PRCL.CA: score=18.54 buy_ready=False sector_rank=2 price=31.5 support=30.9 resistance=36.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=46.03 liquidity=7139962.0 spike=0.3
- PRDC.CA: score=21.36 buy_ready=False sector_rank=15 price=8.89 support=8.7 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=54.73 liquidity=51489444.0 spike=0.7
- PRMH.CA: score=22.67 buy_ready=True sector_rank=13 price=2.79 support=2.28 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=53.54 liquidity=7084928.0 spike=0.46
- RACC.CA: score=13.58 buy_ready=False sector_rank=13 price=9.8 support=9.4 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=29.05 liquidity=10632041.0 spike=0.5
- RAKT.CA: score=2.64 buy_ready=False sector_rank=13 price=22.2 support=21.4 resistance=24.0 source=Yahoo Finance as_of=2026-09-01T21:00:00+00:00 freshness=FRESH RSI=34.53 liquidity=59607.0 spike=0.22
- RAYA.CA: score=11.06 buy_ready=False sector_rank=14 price=7.57 support=7.15 resistance=7.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=143113408.0 spike=2.33
- RMDA.CA: score=16.64 buy_ready=False sector_rank=11 price=5.95 support=5.77 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=28.03 liquidity=21411896.0 spike=0.18
- ROTO.CA: score=9.26 buy_ready=False sector_rank=13 price=43.83 support=43.7 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=6.77 liquidity=5675429.0 spike=0.27
- RREI.CA: score=21.58 buy_ready=False sector_rank=13 price=4.32 support=4.24 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=50.34 liquidity=14446169.0 spike=0.39
- RTVC.CA: score=14.26 buy_ready=False sector_rank=13 price=4.1 support=3.76 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=69.61 liquidity=676952.44 spike=0.08
- RUBX.CA: score=12.6 buy_ready=False sector_rank=13 price=12.68 support=12.2 resistance=13.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=55.62 liquidity=4016809.25 spike=0.22
- SAUD.CA: score=18.17 buy_ready=True sector_rank=7 price=23.51 support=22.13 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=53.23 liquidity=3772739.5 spike=0.18
- SCEM.CA: score=26.4 buy_ready=True sector_rank=2 price=99.1 support=78.3 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=55.33 liquidity=48424320.0 spike=0.21
- SCFM.CA: score=15.89 buy_ready=False sector_rank=13 price=279.43 support=276.05 resistance=305.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=50.64 liquidity=4309739.5 spike=0.29
- SCTS.CA: score=13.34 buy_ready=False sector_rank=12 price=616.03 support=606.01 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=50.06 liquidity=1744769.38 spike=0.19
- SDTI.CA: score=14.89 buy_ready=False sector_rank=13 price=69.61 support=66.66 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=39.42 liquidity=3307854.25 spike=0.13
- SEIG.CA: score=6.9 buy_ready=False sector_rank=13 price=258.42 support=256.01 resistance=293.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=31.18 liquidity=315306.38 spike=0.06
- SIPC.CA: score=23.62 buy_ready=True sector_rank=13 price=5.2 support=4.1 resistance=5.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=60.54 liquidity=56630028.0 spike=1.02
- SKPC.CA: score=24.98 buy_ready=False sector_rank=3 price=18.72 support=16.29 resistance=19.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=83.95 liquidity=139765648.0 spike=1.29
- SMFR.CA: score=9.51 buy_ready=False sector_rank=13 price=252.33 support=245.0 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=12.2 liquidity=2930609.75 spike=0.11
- SNFC.CA: score=7.95 buy_ready=False sector_rank=13 price=10.39 support=10.26 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=27.66 liquidity=5361708.0 spike=0.36
- SPIN.CA: score=16.78 buy_ready=True sector_rank=5 price=19.1 support=15.32 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=64.88 liquidity=2378138.25 spike=0.06
- SPMD.CA: score=5.36 buy_ready=False sector_rank=13 price=0.44 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=1775434.88 spike=0.1
- SUGR.CA: score=23.92 buy_ready=True sector_rank=16 price=60.63 support=47.45 resistance=61.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=69.69 liquidity=80527216.0 spike=1.3
- SVCE.CA: score=23.08 buy_ready=False sector_rank=13 price=12.75 support=9.2 resistance=13.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=77.27 liquidity=216275712.0 spike=1.25
- SWDY.CA: score=26.23 buy_ready=False sector_rank=9 price=130.0 support=105.5 resistance=133.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=71.96 liquidity=29008884.0 spike=0.26
- TALM.CA: score=14.69 buy_ready=False sector_rank=12 price=18.12 support=17.11 resistance=20.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=39.69 liquidity=3099147.0 spike=0.1
- TMGH.CA: score=18.36 buy_ready=False sector_rank=15 price=96.0 support=94.9 resistance=99.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=41.89 liquidity=69740400.0 spike=0.28
- TRTO.CA: score=18.58 buy_ready=False sector_rank=13 price=0.07 support=0.03 resistance=0.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=31526.19 spike=1.48
- UEFM.CA: score=7.47 buy_ready=False sector_rank=13 price=539.22 support=531.0 resistance=589.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=28.12 liquidity=886444.38 spike=0.24
- UEGC.CA: score=13.58 buy_ready=False sector_rank=13 price=1.67 support=1.69 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=15.32 liquidity=33142854.0 spike=0.69
- UNIP.CA: score=6.68 buy_ready=False sector_rank=13 price=0.37 support=0.35 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=33.67 liquidity=3091014.25 spike=0.1
- UNIT.CA: score=6.71 buy_ready=False sector_rank=15 price=18.53 support=17.8 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=31.17 liquidity=354463.44 spike=0.03
- WCDF.CA: score=16.23 buy_ready=False sector_rank=13 price=671.08 support=581.01 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=74.1 liquidity=2650611.25 spike=0.7
- WKOL.CA: score=18.83 buy_ready=True sector_rank=13 price=341.68 support=318.0 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=55.53 liquidity=5248581.0 spike=0.19
- ZEOT.CA: score=16.44 buy_ready=True sector_rank=13 price=14.15 support=12.2 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=57.78 liquidity=2851622.0 spike=0.14
- ZMID.CA: score=22.36 buy_ready=False sector_rank=15 price=9.37 support=7.18 resistance=9.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=78.83 liquidity=59568884.0 spike=0.23

## Backtesting Lite
- ALCN.CA: 180d return=36.36%, max drawdown=-15.82%, MA20>MA50 days last20=20, as_of=2026-09-01T21:00:00+00:00
- FERC.CA: 180d return=1.06%, max drawdown=-15.91%, MA20>MA50 days last20=20, as_of=2026-09-01T21:00:00+00:00
- EGCH.CA: 180d return=22.01%, max drawdown=-20.07%, MA20>MA50 days last20=17, as_of=2026-09-01T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- FERC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=610 sources=3 expected=Ferchem Misr Fertilizers and Chemicals summary=Ferchem Misr’s board greenlights EGP 500m dividends for 2025; Ferchem Misr’s profits soar 4,238% in 2025; Ferchem Misr’s profit leaps 75% in 9M
  - Ferchem Misr’s board greenlights EGP 500m dividends for 2025: https://english.mubasher.info/news/4600298/Ferchem-Misr-s-board-greenlights-EGP-500m-dividends-for-2025/
  - Ferchem Misr’s profits soar 4,238% in 2025: https://english.mubasher.info/news/4564349/Ferchem-Misr-s-profits-soar-4-238-in-2025/
  - Ferchem Misr’s profit leaps 75% in 9M: https://english.mubasher.info/news/3560738/Ferchem-Misr-s-profit-leaps-75-in-9M/
- EGCH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Chemical Industries Kima summary=Evidence rejected for EGCH.CA: source text did not clearly match EGCH.CA / Egyptian Chemical Industries Kima.
- MBSC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=610 sources=3 expected=Misr Beni Suef Cement summary=Misr Beni Suef’s consolidated net profits near EGP 4bn in 2025; Misr Beni Suef’s consolidated net profits hit EGP 953m in H1-25; Misr Beni Suef Cement’s consolidate profits fall to EGP 574m in Q1-25
  - Misr Beni Suef’s consolidated net profits near EGP 4bn in 2025: https://english.mubasher.info/news/4599415/Misr-Beni-Suef-s-consolidated-net-profits-near-EGP-4bn-in-2025/
  - Misr Beni Suef’s consolidated net profits hit EGP 953m in H1-25: https://english.mubasher.info/news/4488249/Misr-Beni-Suef-s-consolidated-net-profits-hit-EGP-953m-in-H1-25/
  - Misr Beni Suef Cement’s consolidate profits fall to EGP 574m in Q1-25: https://english.mubasher.info/news/4455784/Misr-Beni-Suef-Cement-s-consolidate-profits-fall-to-EGP-574m-in-Q1-25/
- ARCC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=610 sources=3 expected=Arabian Cement Company summary=Arabian Cement to pay out EGP 2bn dividends for 2025; Arabian Cement’s EGM approves nearly EGP 8m capital cut; Arabian Cement’s consolidated profits near EGP 3.6bn in 2025
  - Arabian Cement to pay out EGP 2bn dividends for 2025: https://english.mubasher.info/news/4587912/Arabian-Cement-to-pay-out-EGP-2bn-dividends-for-2025/
  - Arabian Cement’s EGM approves nearly EGP 8m capital cut: https://english.mubasher.info/news/4583762/Arabian-Cement-s-EGM-approves-nearly-EGP-8m-capital-cut/
  - Arabian Cement’s consolidated profits near EGP 3.6bn in 2025: https://english.mubasher.info/news/4562679/Arabian-Cement-s-consolidated-profits-near-EGP-3-6bn-in-2025/
- CERA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=The Arab Ceramic Co. summary=Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- ETRS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Transport and Commercial Services Company S.A.E. summary=Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- ISMQ.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Iron and Steel for Mines and Quarries summary=Iron and Steel for Mines and Quarries stock stabilizes above key support after correction; Will Iron and Steel for Mines and Quarries stock hit new historical peaks?; Iron and Steel for Mines and Quarries expects EGP 448m net profit in FY24/25
  - Iron and Steel for Mines and Quarries stock stabilizes above key support after correction: https://english.mubasher.info/news/4578786/Iron-and-Steel-for-Mines-and-Quarries-stock-stabilizes-above-key-support-after-correction/
  - Will Iron and Steel for Mines and Quarries stock hit new historical peaks?: https://english.mubasher.info/news/4556956/Will-Iron-and-Steel-for-Mines-and-Quarries-stock-hit-new-historical-peaks-/
  - Iron and Steel for Mines and Quarries expects EGP 448m net profit in FY24/25: https://english.mubasher.info/news/4249734/Iron-and-Steel-for-Mines-and-Quarries-expects-EGP-448m-net-profit-in-FY24-25/

## Warnings
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence for FERC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for EGCH.CA: source text did not clearly match EGCH.CA / Egyptian Chemical Industries Kima.
- Evidence for MBSC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ARCC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- Evidence for ISMQ.CA matches the company but no source/report date was detected.
