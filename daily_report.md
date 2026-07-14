# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-07-14T09:57:09.067443+00:00
Generated Cairo: 2026-07-14 12:57
Run timing: target 11:00 Cairo | generated Cairo 2026-07-14 12:57 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-07-14 12:52

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 78
- Data quality issues: 1
- Tradeable price/liquidity tickers: 177/189
- Top sector: Technology & Distribution

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, July 14
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 60.0% / above MA50 45.0%
- EGX70 regime: BULLISH / above MA20 73.68% / above MA50 73.68%
- Sector breadth: 47.62%
- Risk mode: SELECTIVE_SMALL_MID_SWINGS

## Top Liquidity
- CCAP.CA: liquidity=770691136.0 spike=1.16 score=28.5
- ABUK.CA: liquidity=277911616.0 spike=1.91 score=24.59
- COMI.CA: liquidity=208266112.0 spike=0.48 score=25.76
- ZMID.CA: liquidity=164659024.0 spike=0.77 score=26.29
- AMES.CA: liquidity=157993632.0 spike=2.98 score=13.36

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner prioritized GDWA.CA, RAYA.CA and ADPC.CA as watch/buy setups under a selective small‑mid swing regime, with EGX30 showing mixed breadth and EGX70 bullish, overall sector breadth around 48% and risk mode set to selective.
- GDWA.CA: liquidity accumulation spike, price above MA20/MA50, RSI ~58, support 0.76/resistance 0.87, bullish watch outlook but sector not leading; macro bearish adds uncertainty.
- RAYA.CA: liquidity cooling, momentum extended, price above MAs, RSI ~64, support 6.8/resistance 8.49, bullish watch outlook; cooling liquidity raises short‑term uncertainty.
- ADPC.CA: liquidity accumulation spike, price above MAs, RSI ~42, support 3.32/resistance 3.94, bullish watch outlook; sector not leading adds uncertainty.
- Market regime: EGX30 mixed (below MA50 breadth weak, 5‑day return negative), EGX70 bullish (strong breadth, positive returns), resulting in SELECTIVE_SMALL_MID_SWINGS risk mode.

## Top Liquidity Spikes
- SMFR.CA: spike=42.01 liquidity=86454736.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EFIC.CA: spike=18.02 liquidity=49888864.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EPCO.CA: spike=13.68 liquidity=110277184.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- UEGC.CA: spike=4.66 liquidity=107124640.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ADPC.CA: spike=3.41 liquidity=61594684.0 outlook=BULLISH_WATCH score=83.09 buy_ready=True

## Sector Leaderboard
- #1 Technology & Distribution: score=10.03 5d=0.12% 20d=16.93% aboveMA50=100.0%
- #2 Industrial Goods & Cables: score=9.38 5d=1.52% 20d=2.4% aboveMA50=100.0%
- #3 Energy & Petrochemicals: score=9.25 5d=5.48% 20d=2.37% aboveMA50=75.0%
- #4 Automotive & Distribution: score=9.22 5d=1.87% 20d=9.76% aboveMA50=100.0%
- #5 Telecommunications: score=9.04 5d=1.46% 20d=4.79% aboveMA50=100.0%
- #6 Transportation & Logistics: score=8.29 5d=0.72% 20d=3.08% aboveMA50=100.0%
- #7 Textiles: score=7.44 5d=2.53% 20d=5.92% aboveMA50=75.0%
- #8 General / Verified EGX Expansion: score=7.09 5d=2.46% 20d=4.41% aboveMA50=72.82%

## Today's Prioritized Action Tickets
- Priority #1: BUY GDWA.CA
  - Entry: 0.84 | Take profit: 0.9 | Stop loss: 0.81
  - Confidence: LOW | score=31.96 | outlook=BULLISH_WATCH 92.09
  - Reason: WATCH/BUY SETUP: GDWA.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 58.39, support 0.76, resistance 0.87, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY RAYA.CA
  - Entry: 8.1 | Take profit: 8.74 | Stop loss: 7.78
  - Confidence: LOW | score=31.4 | outlook=BULLISH_WATCH 84
  - Reason: WATCH/BUY SETUP: RAYA.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 64.14, support 6.8, resistance 8.49, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY ADPC.CA
  - Entry: 3.8 | Take profit: 4.1 | Stop loss: 3.65
  - Confidence: LOW | score=31.22 | outlook=BULLISH_WATCH 83.09
  - Reason: WATCH/BUY SETUP: ADPC.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 42.45, support 3.32, resistance 3.94, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ELEC.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- EGAS.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=close to resistance
- AMOC.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- GDWA.CA: BULLISH_WATCH score=92.09 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- AREH.CA: BULLISH_WATCH score=91.09 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- SWDY.CA: BULLISH_WATCH score=89.38 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ACGC.CA: BULLISH_WATCH score=85.44 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- CSAG.CA: BULLISH_WATCH score=84.29 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- RAYA.CA: BULLISH_WATCH score=84 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- ALCN.CA: BULLISH_WATCH score=83.29 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended

## BUY-Ready Candidates
- AREH.CA: rank=32.46 outlook=BULLISH_WATCH outlook_score=91.09 sector_rank=8 price=1.72 support=1.51 resistance=1.76 liquidity=107658224.0
- ELEC.CA: rank=32.06 outlook=BULLISH_WATCH outlook_score=100 sector_rank=2 price=2.15 support=2.04 resistance=2.21 liquidity=57520408.0
- GDWA.CA: rank=31.96 outlook=BULLISH_WATCH outlook_score=92.09 sector_rank=8 price=0.84 support=0.76 resistance=0.87 liquidity=72567544.0
- EGAS.CA: rank=31.7 outlook=BULLISH_WATCH outlook_score=100 sector_rank=3 price=53.69 support=46.51 resistance=54.0 liquidity=23202130.0
- RAYA.CA: rank=31.4 outlook=BULLISH_WATCH outlook_score=84 sector_rank=1 price=8.1 support=6.8 resistance=8.49 liquidity=47799980.0
- ADPC.CA: rank=31.22 outlook=BULLISH_WATCH outlook_score=83.09 sector_rank=8 price=3.8 support=3.32 resistance=3.94 liquidity=61594684.0
- AMOC.CA: rank=29.86 outlook=BULLISH_WATCH outlook_score=100 sector_rank=3 price=8.3 support=7.42 resistance=8.16 liquidity=119031112.0
- COSG.CA: rank=28.84 outlook=BULLISH_WATCH outlook_score=79.09 sector_rank=8 price=1.68 support=1.47 resistance=1.68 liquidity=52306228.0
- MCRO.CA: rank=28.54 outlook=BULLISH_WATCH outlook_score=78.09 sector_rank=8 price=1.37 support=1.17 resistance=1.37 liquidity=108516416.0
- CCAP.CA: rank=28.5 outlook=CONSTRUCTIVE outlook_score=69.45 sector_rank=11 price=5.46 support=4.65 resistance=5.41 liquidity=770691136.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=18.63 buy_ready=True sector_rank=8 price=228.82 support=196.0 resistance=247.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=64.75 liquidity=2225564.0 spike=0.16
- ABUK.CA: score=24.59 buy_ready=False sector_rank=14 price=71.58 support=66.66 resistance=73.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=41.12 liquidity=277911616.0 spike=1.91
- ACAMD.CA: score=26.4 buy_ready=True sector_rank=8 price=2.33 support=2.14 resistance=2.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=46.34 liquidity=29885294.0 spike=0.31
- ACGC.CA: score=28.4 buy_ready=True sector_rank=7 price=9.86 support=8.92 resistance=10.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=11335907.0 spike=0.54
- ADCI.CA: score=18.0 buy_ready=True sector_rank=8 price=235.19 support=223.15 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=56.21 liquidity=3604753.75 spike=0.29
- ADIB.CA: score=20.76 buy_ready=False sector_rank=15 price=46.5 support=44.1 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=47.99 liquidity=45495696.0 spike=0.47
- ADPC.CA: score=31.22 buy_ready=True sector_rank=8 price=3.8 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=42.45 liquidity=61594684.0 spike=3.41
- AFDI.CA: score=24.42 buy_ready=True sector_rank=8 price=46.76 support=41.84 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=60.65 liquidity=6017038.5 spike=0.43
- AFMC.CA: score=21.61 buy_ready=True sector_rank=8 price=73.64 support=66.0 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=62.76 liquidity=3210823.0 spike=0.85
- AJWA.CA: score=27.38 buy_ready=True sector_rank=8 price=180.73 support=160.0 resistance=190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=62.53 liquidity=28040336.0 spike=1.49
- ALCN.CA: score=27.0 buy_ready=True sector_rank=6 price=29.63 support=27.7 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=66.22 liquidity=23533322.0 spike=1.3
- ALUM.CA: score=16.52 buy_ready=False sector_rank=8 price=22.78 support=20.55 resistance=24.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=44.03 liquidity=3116802.5 spike=0.49
- AMER.CA: score=23.29 buy_ready=False sector_rank=10 price=3.18 support=2.28 resistance=3.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=76.8 liquidity=50523784.0 spike=0.64
- AMES.CA: score=13.36 buy_ready=False sector_rank=8 price=114.99 support=102.31 resistance=118.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=157993632.0 spike=2.98
- AMIA.CA: score=13.47 buy_ready=False sector_rank=8 price=8.88 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=46.46 liquidity=1069192.88 spike=0.12
- AMOC.CA: score=29.86 buy_ready=True sector_rank=3 price=8.3 support=7.42 resistance=8.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=57.4 liquidity=119031112.0 spike=2.23
- APSW.CA: score=18.22 buy_ready=False sector_rank=8 price=8.51 support=8.0 resistance=8.79 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=46.03 liquidity=2223577.96 spike=2.8
- ARAB.CA: score=23.69 buy_ready=False sector_rank=10 price=0.25 support=0.2 resistance=0.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=79.1 liquidity=121470576.0 spike=1.2
- ARCC.CA: score=18.08 buy_ready=False sector_rank=19 price=54.88 support=53.0 resistance=57.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=45.43 liquidity=20898224.0 spike=1.04
- AREH.CA: score=32.46 buy_ready=True sector_rank=8 price=1.72 support=1.51 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 July 01:29 PM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=107658224.0 spike=3.03
- ARVA.CA: score=16.89 buy_ready=False sector_rank=8 price=10.61 support=10.5 resistance=12.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=43.38 liquidity=4493574.5 spike=0.22
- ASCM.CA: score=24.4 buy_ready=True sector_rank=8 price=61.67 support=56.29 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=57.24 liquidity=14971835.0 spike=0.18
- ASPI.CA: score=19.4 buy_ready=False sector_rank=8 price=0.31 support=0.3 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=37.31 liquidity=18539200.0 spike=0.78
- ATLC.CA: score=15.1 buy_ready=False sector_rank=16 price=5.21 support=4.84 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=45.65 liquidity=3431172.5 spike=0.5
- ATQA.CA: score=19.67 buy_ready=False sector_rank=14 price=9.5 support=9.21 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=52.34 liquidity=9904287.0 spike=0.31
- AXPH.CA: score=19.45 buy_ready=True sector_rank=8 price=1209.7 support=1073.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:26 AM market time freshness=DELAYED_CURRENT RSI=64.76 liquidity=3045664.25 spike=0.95
- BINV.CA: score=17.51 buy_ready=True sector_rank=11 price=48.59 support=45.01 resistance=51.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:26 AM market time freshness=DELAYED_CURRENT RSI=56.05 liquidity=1333654.38 spike=0.21
- BIOC.CA: score=19.28 buy_ready=False sector_rank=8 price=73.91 support=66.75 resistance=76.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=55.63 liquidity=881051.56 spike=0.26
- BTFH.CA: score=21.67 buy_ready=False sector_rank=16 price=3.05 support=2.91 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=41.86 liquidity=75052360.0 spike=0.39
- CAED.CA: score=14.0 buy_ready=False sector_rank=8 price=78.97 support=73.7 resistance=79.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21619600.0 spike=3.3
- CANA.CA: score=23.24 buy_ready=False sector_rank=15 price=35.92 support=34.7 resistance=38.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=38.84 liquidity=12753091.0 spike=1.24
- CCAP.CA: score=28.5 buy_ready=True sector_rank=11 price=5.46 support=4.65 resistance=5.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=63.39 liquidity=770691136.0 spike=1.16
- CCRS.CA: score=25.34 buy_ready=True sector_rank=8 price=2.5 support=2.18 resistance=2.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=59.15 liquidity=6938289.0 spike=0.53
- CEFM.CA: score=14.51 buy_ready=False sector_rank=8 price=103.91 support=95.75 resistance=110.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:26 AM market time freshness=DELAYED_CURRENT RSI=55.54 liquidity=1110252.25 spike=0.51
- CERA.CA: score=21.53 buy_ready=True sector_rank=8 price=1.3 support=1.17 resistance=1.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=5128022.5 spike=0.25
- CFGH.CA: score=14.64 buy_ready=False sector_rank=8 price=0.11 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:28 AM market time freshness=DELAYED_CURRENT RSI=88.89 liquidity=16099.22 spike=2.11
- CICH.CA: score=12.52 buy_ready=False sector_rank=16 price=11.96 support=11.45 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=1854108.13 spike=0.46
- CIEB.CA: score=24.37 buy_ready=True sector_rank=15 price=24.31 support=23.3 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=57.31 liquidity=8236520.5 spike=1.19
- CIRA.CA: score=24.02 buy_ready=True sector_rank=13 price=30.99 support=26.0 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=68.96 liquidity=12890379.0 spike=0.51
- CLHO.CA: score=21.34 buy_ready=False sector_rank=18 price=16.15 support=15.21 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=27601608.0 spike=0.75
- CNFN.CA: score=25.67 buy_ready=True sector_rank=16 price=4.97 support=4.4 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=55.17 liquidity=29708068.0 spike=0.65
- COMI.CA: score=25.76 buy_ready=True sector_rank=15 price=135.0 support=126.21 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=50.34 liquidity=208266112.0 spike=0.48
- COPR.CA: score=23.4 buy_ready=True sector_rank=8 price=0.38 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=43.08 liquidity=21701222.0 spike=0.91
- COSG.CA: score=28.84 buy_ready=True sector_rank=8 price=1.68 support=1.47 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=59.46 liquidity=52306228.0 spike=1.22
- CPCI.CA: score=26.08 buy_ready=False sector_rank=8 price=431.59 support=360.53 resistance=482.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=85.59 liquidity=12052604.0 spike=2.34
- CSAG.CA: score=25.5 buy_ready=True sector_rank=6 price=32.16 support=30.87 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=60.11 liquidity=9095034.0 spike=0.54
- DAPH.CA: score=19.26 buy_ready=True sector_rank=8 price=83.62 support=77.5 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=56.57 liquidity=2856735.5 spike=0.32
- DEIN.CA: score=-0.6 buy_ready=False sector_rank=8 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=14.28 buy_ready=False sector_rank=17 price=26.83 support=24.23 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=61.58 liquidity=832554.38 spike=0.16
- DSCW.CA: score=26.06 buy_ready=True sector_rank=8 price=1.86 support=1.71 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=40970476.0 spike=1.33
- DTPP.CA: score=21.14 buy_ready=False sector_rank=8 price=204.67 support=114.0 resistance=234.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=85.86 liquidity=9739354.0 spike=0.25
- EALR.CA: score=18.46 buy_ready=True sector_rank=8 price=366.49 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=55.59 liquidity=2058669.75 spike=0.17
- EASB.CA: score=17.85 buy_ready=False sector_rank=8 price=7.03 support=5.84 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=36.51 liquidity=5445394.0 spike=0.3
- EAST.CA: score=9.99 buy_ready=False sector_rank=17 price=36.7 support=36.47 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=28.75 liquidity=7542845.5 spike=0.16
- EBSC.CA: score=17.2 buy_ready=True sector_rank=8 price=1.91 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=51.28 liquidity=2802688.25 spike=0.46
- ECAP.CA: score=14.86 buy_ready=False sector_rank=8 price=32.6 support=31.3 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=38.47 liquidity=2458615.75 spike=0.28
- EDFM.CA: score=21.13 buy_ready=False sector_rank=8 price=359.99 support=310.2 resistance=363.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=74.59 liquidity=2011658.75 spike=2.36
- EEII.CA: score=23.41 buy_ready=True sector_rank=8 price=2.73 support=2.35 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=64.89 liquidity=7005314.5 spike=0.34
- EFIC.CA: score=13.77 buy_ready=False sector_rank=14 price=199.63 support=184.0 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=49888864.0 spike=18.02
- EFID.CA: score=20.44 buy_ready=False sector_rank=17 price=27.9 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=53.69 liquidity=30055932.0 spike=0.63
- EFIH.CA: score=26.12 buy_ready=True sector_rank=12 price=22.2 support=20.0 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=62.0 liquidity=17825860.0 spike=0.4
- EGAL.CA: score=22.77 buy_ready=False sector_rank=14 price=298.17 support=272.28 resistance=314.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=44.64 liquidity=41630372.0 spike=0.88
- EGAS.CA: score=31.7 buy_ready=True sector_rank=3 price=53.69 support=46.51 resistance=54.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=56.62 liquidity=23202130.0 spike=2.15
- EGBE.CA: score=12.76 buy_ready=False sector_rank=15 price=0.45 support=-0.34 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=96.19 liquidity=6941.68 spike=-0.15
- EGCH.CA: score=28.49 buy_ready=True sector_rank=14 price=13.61 support=12.13 resistance=13.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=41.8 liquidity=109957688.0 spike=2.36
- EGSA.CA: score=15.97 buy_ready=False sector_rank=5 price=8.97 support=8.67 resistance=9.13 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=70.21 liquidity=9562.02 spike=1.78
- EGTS.CA: score=23.94 buy_ready=True sector_rank=10 price=18.49 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=47.82 liquidity=9647791.0 spike=0.18
- EHDR.CA: score=26.4 buy_ready=True sector_rank=8 price=2.68 support=2.37 resistance=2.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=48.35 liquidity=18954054.0 spike=0.51
- EKHO.CA: score=9.4 buy_ready=False sector_rank=3 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=32.06 buy_ready=True sector_rank=2 price=2.15 support=2.04 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=57520408.0 spike=2.33
- ELKA.CA: score=11.34 buy_ready=False sector_rank=8 price=1.78 support=1.6 resistance=1.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=99713440.0 spike=1.97
- ELNA.CA: score=17.98 buy_ready=False sector_rank=8 price=39.47 support=35.55 resistance=40.65 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=49.58 liquidity=735839.23 spike=1.42
- ELSH.CA: score=26.4 buy_ready=True sector_rank=8 price=14.59 support=11.1 resistance=15.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=62.52 liquidity=82858920.0 spike=0.51
- ELWA.CA: score=14.9 buy_ready=False sector_rank=8 price=2.04 support=1.87 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:10 AM market time freshness=DELAYED_CURRENT RSI=45.24 liquidity=501309.56 spike=0.27
- EMFD.CA: score=22.29 buy_ready=False sector_rank=10 price=11.68 support=11.24 resistance=12.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=43.03 liquidity=14821719.0 spike=0.11
- ENGC.CA: score=24.4 buy_ready=True sector_rank=8 price=41.99 support=33.91 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=66.86 liquidity=10671173.0 spike=0.44
- EOSB.CA: score=14.43 buy_ready=False sector_rank=8 price=1.48 support=1.42 resistance=1.55 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=29345.44 spike=0.43
- EPCO.CA: score=14.4 buy_ready=False sector_rank=8 price=10.4 support=9.72 resistance=10.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=110277184.0 spike=13.68
- EPPK.CA: score=14.89 buy_ready=False sector_rank=8 price=14.11 support=11.75 resistance=15.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:11 AM market time freshness=DELAYED_CURRENT RSI=67.37 liquidity=493824.41 spike=0.49
- ETEL.CA: score=26.4 buy_ready=True sector_rank=5 price=97.26 support=89.01 resistance=101.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=59.2 liquidity=15409829.0 spike=0.21
- ETRS.CA: score=23.52 buy_ready=True sector_rank=8 price=10.84 support=9.82 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=49.36 liquidity=9116233.0 spike=0.12
- EXPA.CA: score=24.05 buy_ready=True sector_rank=15 price=18.71 support=18.03 resistance=18.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=55.07 liquidity=8297911.0 spike=0.33
- FAIT.CA: score=20.29 buy_ready=True sector_rank=15 price=37.26 support=35.06 resistance=37.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=49.4 liquidity=3630668.0 spike=1.45
- FAITA.CA: score=8.78 buy_ready=False sector_rank=15 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=44.83 liquidity=26477.47 spike=0.93
- FERC.CA: score=21.28 buy_ready=False sector_rank=14 price=77.0 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=49.54 liquidity=7670514.5 spike=1.92
- FWRY.CA: score=23.12 buy_ready=False sector_rank=12 price=18.91 support=18.13 resistance=19.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=59.17 liquidity=56765748.0 spike=0.32
- GBCO.CA: score=22.4 buy_ready=True sector_rank=4 price=31.48 support=27.77 resistance=32.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=67.24 liquidity=14956435.0 spike=0.19
- GDWA.CA: score=31.96 buy_ready=True sector_rank=8 price=0.84 support=0.76 resistance=0.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=58.39 liquidity=72567544.0 spike=3.28
- GGCC.CA: score=12.52 buy_ready=False sector_rank=8 price=0.63 support=0.59 resistance=0.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=44560284.0 spike=2.56
- GIHD.CA: score=24.4 buy_ready=True sector_rank=8 price=49.02 support=40.5 resistance=52.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=67.51 liquidity=21429736.0 spike=0.88
- GMCI.CA: score=14.86 buy_ready=False sector_rank=8 price=1.99 support=1.66 resistance=2.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=66.22 liquidity=457568.38 spike=0.41
- GRCA.CA: score=10.59 buy_ready=False sector_rank=8 price=52.05 support=48.0 resistance=58.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=39.59 liquidity=1188648.0 spike=0.33
- GSSC.CA: score=18.06 buy_ready=True sector_rank=8 price=259.91 support=240.0 resistance=263.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=68.43 liquidity=1662821.75 spike=0.37
- GTWL.CA: score=21.4 buy_ready=False sector_rank=8 price=110.7 support=46.0 resistance=117.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=89.57 liquidity=43306148.0 spike=0.44
- HDBK.CA: score=12.52 buy_ready=False sector_rank=15 price=77.28 support=75.3 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=7.89 liquidity=9765195.0 spike=0.24
- HELI.CA: score=24.29 buy_ready=False sector_rank=10 price=7.36 support=6.34 resistance=7.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=71.2 liquidity=90447888.0 spike=0.59
- HRHO.CA: score=17.67 buy_ready=False sector_rank=16 price=26.49 support=26.09 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=39.4 liquidity=40885672.0 spike=0.31
- ICID.CA: score=15.2 buy_ready=False sector_rank=8 price=8.12 support=6.55 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=59.47 liquidity=800492.5 spike=0.09
- IDRE.CA: score=26.4 buy_ready=True sector_rank=8 price=45.09 support=41.1 resistance=47.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=53.88 liquidity=11394529.0 spike=0.86
- IFAP.CA: score=16.55 buy_ready=False sector_rank=9 price=19.59 support=18.47 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=59.11 liquidity=1154567.0 spike=0.25
- INFI.CA: score=25.19 buy_ready=False sector_rank=8 price=101.0 support=88.51 resistance=106.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=72.43 liquidity=9774744.0 spike=1.01
- IRON.CA: score=15.68 buy_ready=False sector_rank=14 price=31.37 support=30.51 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=46.91 liquidity=5913097.5 spike=0.74
- ISMA.CA: score=16.0 buy_ready=False sector_rank=8 price=27.42 support=26.54 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=17.9 liquidity=8596156.0 spike=0.33
- ISMQ.CA: score=23.77 buy_ready=True sector_rank=14 price=9.35 support=8.06 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=68.94 liquidity=74460624.0 spike=0.51
- ISPH.CA: score=13.34 buy_ready=False sector_rank=18 price=11.49 support=11.2 resistance=12.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=26.94 liquidity=33900376.0 spike=0.57
- JUFO.CA: score=21.44 buy_ready=False sector_rank=17 price=30.02 support=29.1 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=39.91 liquidity=11554876.0 spike=0.51
- KABO.CA: score=18.94 buy_ready=False sector_rank=7 price=7.5 support=6.04 resistance=7.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=86.71 liquidity=7541172.0 spike=0.26
- KWIN.CA: score=15.89 buy_ready=False sector_rank=8 price=68.58 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=35.76 liquidity=6493785.0 spike=0.49
- KZPC.CA: score=17.74 buy_ready=False sector_rank=8 price=8.69 support=8.26 resistance=10.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=39.41 liquidity=7341970.5 spike=0.99
- LCSW.CA: score=25.0 buy_ready=True sector_rank=19 price=30.79 support=26.6 resistance=32.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=64.56 liquidity=26069434.0 spike=0.44
- LUTS.CA: score=22.4 buy_ready=False sector_rank=8 price=0.73 support=0.69 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=50.7 liquidity=20896324.0 spike=0.41
- MAAL.CA: score=22.39 buy_ready=False sector_rank=8 price=8.51 support=5.75 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=98.37 liquidity=8991275.0 spike=0.53
- MASR.CA: score=26.4 buy_ready=True sector_rank=8 price=8.14 support=6.71 resistance=8.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=66.53 liquidity=44887436.0 spike=0.5
- MBSC.CA: score=19.18 buy_ready=False sector_rank=19 price=236.78 support=222.66 resistance=256.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=39.17 liquidity=9171379.0 spike=0.42
- MCQE.CA: score=15.75 buy_ready=False sector_rank=19 price=176.59 support=166.66 resistance=182.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=47.89 liquidity=3749734.0 spike=0.26
- MCRO.CA: score=28.54 buy_ready=True sector_rank=8 price=1.37 support=1.17 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=67.74 liquidity=108516416.0 spike=2.57
- MENA.CA: score=15.12 buy_ready=False sector_rank=10 price=7.09 support=6.59 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=55.38 liquidity=828255.75 spike=0.1
- MEPA.CA: score=20.57 buy_ready=False sector_rank=8 price=1.67 support=1.52 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=44.74 liquidity=7169370.5 spike=0.64
- MFPC.CA: score=23.67 buy_ready=False sector_rank=14 price=37.97 support=34.22 resistance=38.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=49.35 liquidity=146416608.0 spike=1.45
- MFSC.CA: score=16.83 buy_ready=False sector_rank=8 price=47.1 support=44.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=51.48 liquidity=4426097.0 spike=0.57
- MHOT.CA: score=1.7 buy_ready=False sector_rank=21 price=16.32 support=16.12 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=3.54 liquidity=2297018.25 spike=0.16
- MICH.CA: score=24.8 buy_ready=True sector_rank=8 price=38.2 support=34.0 resistance=39.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=42.94 liquidity=19760612.0 spike=1.2
- MILS.CA: score=22.94 buy_ready=True sector_rank=8 price=135.5 support=126.31 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=49.07 liquidity=6542396.0 spike=0.57
- MIPH.CA: score=17.94 buy_ready=False sector_rank=18 price=710.32 support=630.13 resistance=725.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=54.08 liquidity=603707.69 spike=0.28
- MOED.CA: score=24.54 buy_ready=False sector_rank=8 price=0.72 support=0.65 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=58.48 liquidity=13719741.0 spike=1.07
- MOIL.CA: score=14.62 buy_ready=False sector_rank=3 price=0.54 support=0.46 resistance=0.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=76.42 liquidity=219887.83 spike=0.63
- MOIN.CA: score=15.37 buy_ready=False sector_rank=8 price=24.5 support=22.6 resistance=25.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=48.18 liquidity=1430422.5 spike=1.77
- MOSC.CA: score=26.4 buy_ready=True sector_rank=8 price=283.3 support=250.0 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=56.35 liquidity=13495421.0 spike=1.0
- MPCI.CA: score=24.4 buy_ready=True sector_rank=8 price=240.14 support=215.0 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=50.37 liquidity=27198794.0 spike=0.28
- MPCO.CA: score=24.4 buy_ready=True sector_rank=9 price=1.9 support=1.7 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=79113024.0 spike=0.97
- MPRC.CA: score=21.4 buy_ready=False sector_rank=8 price=41.82 support=31.72 resistance=43.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=88.74 liquidity=22833196.0 spike=0.47
- MTIE.CA: score=28.4 buy_ready=True sector_rank=4 price=9.56 support=8.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=62.44 liquidity=11731639.0 spike=0.51
- NAHO.CA: score=8.41 buy_ready=False sector_rank=8 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=14876.5 spike=0.58
- NCCW.CA: score=26.4 buy_ready=True sector_rank=8 price=6.54 support=5.82 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=56.91 liquidity=10575368.0 spike=0.46
- NEDA.CA: score=16.96 buy_ready=False sector_rank=8 price=2.8 support=2.7 resistance=2.83 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=57.14 liquidity=361328.79 spike=1.1
- NHPS.CA: score=26.4 buy_ready=False sector_rank=8 price=84.69 support=61.55 resistance=83.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=77.61 liquidity=99603752.0 spike=2.5
- NINH.CA: score=20.3 buy_ready=False sector_rank=8 price=17.77 support=17.03 resistance=18.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=58.37 liquidity=13180167.0 spike=1.45
- NIPH.CA: score=25.34 buy_ready=True sector_rank=18 price=178.98 support=157.01 resistance=185.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=60.75 liquidity=62374020.0 spike=0.72
- OBRI.CA: score=23.4 buy_ready=False sector_rank=8 price=35.84 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=11581505.0 spike=0.35
- OCDI.CA: score=21.29 buy_ready=False sector_rank=10 price=26.91 support=20.55 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=78.93 liquidity=17856050.0 spike=0.18
- OCPH.CA: score=27.5 buy_ready=False sector_rank=8 price=370.14 support=337.0 resistance=385.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=71.98 liquidity=13593396.0 spike=1.55
- ODIN.CA: score=19.95 buy_ready=True sector_rank=8 price=2.46 support=2.05 resistance=2.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=68.49 liquidity=3547455.0 spike=0.24
- OFH.CA: score=23.65 buy_ready=True sector_rank=8 price=0.63 support=0.57 resistance=0.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=59.0 liquidity=7254494.0 spike=0.35
- OIH.CA: score=21.18 buy_ready=False sector_rank=11 price=1.41 support=1.35 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=18434244.0 spike=0.26
- OLFI.CA: score=22.85 buy_ready=True sector_rank=17 price=22.86 support=21.0 resistance=23.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=58.36 liquidity=7405602.5 spike=0.21
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=683.55 support=681.5 resistance=685.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=63349720.0 spike=1.0
- ORHD.CA: score=24.29 buy_ready=True sector_rank=10 price=38.86 support=37.0 resistance=39.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=47.05 liquidity=45282308.0 spike=0.28
- ORWE.CA: score=19.4 buy_ready=False sector_rank=7 price=22.62 support=21.95 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=36.84 liquidity=10984566.0 spike=0.59
- PHAR.CA: score=12.39 buy_ready=False sector_rank=18 price=86.16 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=38.42 liquidity=4053679.75 spike=0.18
- PHDC.CA: score=17.29 buy_ready=False sector_rank=10 price=14.7 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=24.37 liquidity=52606908.0 spike=0.17
- PHTV.CA: score=11.86 buy_ready=False sector_rank=8 price=295.02 support=207.0 resistance=308.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=86.72 liquidity=459660.78 spike=0.03
- POUL.CA: score=23.44 buy_ready=True sector_rank=17 price=38.89 support=35.28 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=65.82 liquidity=35462512.0 spike=0.79
- PRCL.CA: score=23.0 buy_ready=False sector_rank=19 price=34.21 support=24.5 resistance=36.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=73.47 liquidity=30728536.0 spike=0.68
- PRDC.CA: score=9.29 buy_ready=False sector_rank=10 price=8.9 support=8.21 resistance=8.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=135199872.0 spike=0.92
- PRMH.CA: score=24.4 buy_ready=True sector_rank=8 price=2.76 support=2.34 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=44.79 liquidity=20237372.0 spike=0.64
- RACC.CA: score=28.4 buy_ready=True sector_rank=8 price=10.33 support=9.36 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=64.68 liquidity=15438676.0 spike=0.93
- RAKT.CA: score=13.85 buy_ready=False sector_rank=8 price=22.51 support=21.25 resistance=23.79 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=50.2 liquidity=628951.92 spike=2.41
- RAYA.CA: score=31.4 buy_ready=True sector_rank=1 price=8.1 support=6.8 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=64.14 liquidity=47799980.0 spike=0.4
- RMDA.CA: score=18.34 buy_ready=False sector_rank=18 price=4.96 support=4.81 resistance=5.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=40.91 liquidity=11096241.0 spike=0.54
- ROTO.CA: score=24.4 buy_ready=True sector_rank=8 price=42.0 support=33.99 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=49.68 liquidity=10323990.0 spike=0.31
- RREI.CA: score=28.4 buy_ready=True sector_rank=8 price=3.83 support=3.34 resistance=3.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=16969954.0 spike=0.86
- RTVC.CA: score=15.22 buy_ready=False sector_rank=8 price=3.83 support=3.55 resistance=3.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=1824340.5 spike=0.45
- RUBX.CA: score=24.6 buy_ready=False sector_rank=8 price=13.72 support=9.8 resistance=14.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=79.42 liquidity=145563728.0 spike=2.6
- SAUD.CA: score=15.4 buy_ready=False sector_rank=15 price=21.61 support=19.99 resistance=22.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=2642096.25 spike=0.4
- SCEM.CA: score=14.97 buy_ready=False sector_rank=19 price=61.64 support=60.14 resistance=67.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=51.24 liquidity=4966966.0 spike=0.28
- SCFM.CA: score=16.59 buy_ready=False sector_rank=8 price=253.06 support=226.5 resistance=269.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=55.4 liquidity=1189713.0 spike=0.23
- SCTS.CA: score=17.63 buy_ready=True sector_rank=13 price=614.4 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=60.17 liquidity=1605306.5 spike=0.31
- SDTI.CA: score=15.8 buy_ready=True sector_rank=8 price=47.0 support=45.55 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=44.6 liquidity=1402882.75 spike=0.2
- SEIG.CA: score=19.73 buy_ready=False sector_rank=8 price=252.69 support=181.01 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=85.19 liquidity=6334492.0 spike=0.31
- SIPC.CA: score=18.26 buy_ready=False sector_rank=8 price=3.46 support=3.25 resistance=3.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=48.1 liquidity=4856430.5 spike=0.64
- SKPC.CA: score=21.81 buy_ready=False sector_rank=14 price=16.5 support=15.58 resistance=16.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=49.12 liquidity=31988528.0 spike=1.02
- SMFR.CA: score=14.4 buy_ready=False sector_rank=8 price=247.59 support=206.41 resistance=247.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=86454736.0 spike=42.01
- SNFC.CA: score=13.59 buy_ready=False sector_rank=8 price=11.53 support=11.26 resistance=12.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=45.0 liquidity=4191863.25 spike=0.37
- SPIN.CA: score=17.58 buy_ready=False sector_rank=7 price=14.65 support=13.3 resistance=14.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=80.45 liquidity=4177937.25 spike=0.45
- SPMD.CA: score=26.4 buy_ready=True sector_rank=8 price=0.44 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=13329814.0 spike=0.78
- SUGR.CA: score=13.32 buy_ready=False sector_rank=17 price=47.0 support=45.31 resistance=49.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=39.2 liquidity=3878457.0 spike=0.78
- SVCE.CA: score=25.98 buy_ready=True sector_rank=8 price=9.34 support=8.56 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=52.6 liquidity=9579959.0 spike=0.14
- SWDY.CA: score=27.74 buy_ready=True sector_rank=2 price=88.02 support=84.3 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=54.73 liquidity=9335382.0 spike=0.73
- TALM.CA: score=12.02 buy_ready=False sector_rank=13 price=15.55 support=15.27 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=38.86 liquidity=3001750.75 spike=0.26
- TMGH.CA: score=26.29 buy_ready=True sector_rank=10 price=97.49 support=92.1 resistance=99.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=53.98 liquidity=68023752.0 spike=0.19
- TRTO.CA: score=10.4 buy_ready=False sector_rank=8 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=68.03 spike=0.32
- UEFM.CA: score=20.07 buy_ready=True sector_rank=8 price=519.02 support=460.0 resistance=529.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=58.73 liquidity=2491502.75 spike=1.59
- UEGC.CA: score=14.4 buy_ready=False sector_rank=8 price=2.15 support=1.88 resistance=2.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=107124640.0 spike=4.66
- UNIP.CA: score=25.91 buy_ready=True sector_rank=8 price=0.34 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=7514253.5 spike=0.43
- UNIT.CA: score=13.89 buy_ready=False sector_rank=10 price=20.04 support=19.01 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=70742160.0 spike=3.3
- WCDF.CA: score=14.12 buy_ready=False sector_rank=8 price=523.93 support=504.0 resistance=544.99 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=45.1 liquidity=399758.58 spike=1.16
- WKOL.CA: score=17.63 buy_ready=True sector_rank=8 price=311.6 support=273.1 resistance=334.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=64.53 liquidity=1225907.75 spike=0.17
- ZEOT.CA: score=24.4 buy_ready=True sector_rank=8 price=11.63 support=9.26 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=48.89 liquidity=21144432.0 spike=0.47
- ZMID.CA: score=26.29 buy_ready=False sector_rank=10 price=7.24 support=6.11 resistance=7.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=71.82 liquidity=164659024.0 spike=0.77

## Backtesting Lite
- AREH.CA: 180d return=42.5%, max drawdown=-37.58%, MA20>MA50 days last20=20, as_of=2026-07-12T21:00:00+00:00
- ELEC.CA: 180d return=-23.4%, max drawdown=-35.96%, MA20>MA50 days last20=0, as_of=2026-07-12T21:00:00+00:00
- GDWA.CA: 180d return=-28.9%, max drawdown=-39.84%, MA20>MA50 days last20=12, as_of=2026-07-12T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- AREH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Real Estate Egyptian Consortium S.A.E summary=Real Estate Egyptian Consortium’s net profits approach EGP 2m in 9M-25; Shareholder ups stake in Real Estate Egyptian; Target for Real Estate Investment cuts stake in Real Estate Egyptian Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Real Estate Egyptian Consortium’s net profits approach EGP 2m in 9M-25: https://english.mubasher.info/news/4528467/Real-Estate-Egyptian-Consortium-s-net-profits-approach-EGP-2m-in-9M-25/
  - Shareholder ups stake in Real Estate Egyptian: https://english.mubasher.info/news/4026301/Shareholder-ups-stake-in-Real-Estate-Egyptian/
  - Target for Real Estate Investment cuts stake in Real Estate Egyptian: https://english.mubasher.info/news/4010821/Target-for-Real-Estate-Investment-cuts-stake-in-Real-Estate-Egyptian/
- ELEC.CA: status=OLD_ACCEPTED latest=2025-03-31 age_days=470 sources=3 expected=Electro Cable Egypt summary=Recent disclosures and financial reports for Electro Cable Egypt (ELEC.CA) indicate standalone results for the year ended December 31, 2024, and investor relations information. The company reported sales of 2,094.080 million EGP and a net loss of 241.612 million EGP for the latest quarter.
  - Electro Cable Egypt (ELEC.CA) Reports Year Ended 31/12/2024 Standalone Results - The Egyptian Exchange (Report Date: 2025-03-31): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5ZmAYSsB1l8gAkBX4KjKMnOSK8j-Cxrtabq4mH09qleauL5SXDogBpzeBNYazBcC3GMzNqpkX87HWQfC-VIK6CLvP6uVxdDQRFvDKYQhVYA-lQSZS5GcykmB1XIdM13ZcUcyWcaTIZG3mt-WA2A==
  - EGX:ELEC Financials | Electro Cable - Investing.com (Latest Quarter Earnings): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGY2r2zcCZpCgcySMs7xpwYn5yHaOz3ANrM0gZSkKQcSEc6ytqGhq9QjLhukE67_tScPhF-RahrP6wsmb-0UpfYE0L8_UbN8ntWxVDkIt2sKIbzsACBvbBHhJE5nliam2PZ8QdjHcPEH8ku5yF47xZ45EVBifNA52huaaf1
  - Investor Relations - Electro Cable Egypt: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWp2YLKGjlFearb7A0UZsiezE9Y6lkRP2Zp5rRx8ptsdEji5KVLbjqDbrubIr_PCt9CmEd9BXhOAi9HYy-2b_cRTr2YlQfkaWCzzb7rMVCxYliX0pUGaey0NFn7ya-pZsOEGuFVTrX
- GDWA.CA: status=RECENT_ACCEPTED latest=2026-07-09 age_days=5 sources=3 expected=Gadwa for Industrial Development summary=Gadwa for Industrial Development (GDWA.CA) reported consolidated financial results for Q1 2026, showing a net loss of 381,799,191 EGP. The company's revenue for the last 12 months was EGP 13.72 billion with losses of 359.94 million EGP. Gadwa holds diversified industrial interests, including stakes in Electro Cables and Arab Dairy.
  - Gadwa For Industrial Development (GDWA.CA) Reports its Financial Results (Consolidated) for the Period from 01/01/2026 to 31/03/2026 - The Egyptian Exchange (Report Date: 2026-06-30): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElvjwUETuFJyvgfMKJe6biizM9P7B4LKUUZeSxpm2_I_CXm44OSAsqUbEDOrfa7quZjsTWEeH1HhduK_kS9Oh3gDT1ZFJ9Hx-2vDNH9euD5UuOcE0gfrY6LnwyJkN1d8lqVm27eJXPdBf2HPoGYWmxTZ8=
  - Gadwa for Industrial Development (EGX:GDWA) Statistics & Valuation Metrics (As of 2026-07-09): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmrBjqVrcLInurZHn3211u5q0KahHChG1CriFt8ariRss8nK8QWXAepl2vsQJgJhzRiKTnmwLbs8iYrD-DJdAM6Zodc6phJjMLIYGDEbIkWVVvZOkHw0J9jTqGkkKOAUj_ML8ac5LSwcnO1ksHcA==
  - Gadwa for Industrial Development Stock Price Today | EGX: GDWA Live - Investing.com: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc1SYNsF0tiBoUlO6MsHNAsCyAA_BmSlZNdPuFxzqbtiPYCKqVBB-wR_ThgpY7YCca3HFF0s-GtBz81wm7DaVhNExXhzSzXerjNJOo3K_Qi3nzv2vmMWR88CER8R5OfVJ3XIBfNZ7U--sRwxx6eaeRhBfbgqVRLj4DHuUEjg==
- EGAS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Natural Gas and Mining Project summary=Evidence rejected for EGAS.CA: source text did not clearly match EGAS.CA / Natural Gas and Mining Project.
- RAYA.CA: status=RECENT_ACCEPTED latest=2026-07-12 age_days=2 sources=3 expected=Raya Holding summary=Raya Holding (RAYA.CA) reported strong financial performance, with group consolidated turnover of EGP 45.1 billion and net income before minority of EGP 1.7 billion for FY24 (reported April 14, 2025). The company's stock price increased by +142.42% in the last 52 weeks (as of July 12, 2026). Raya Holding is listed on the EGX since 2005 and operates a diversified investment portfolio across various sectors.
  - Raya Holding Delivers Record-Breaking Profit Growth and Broad-Based Revenue Expansion (Report Date: 2025-04-14): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHw6x6EHIQeXDFVh7c7uHBrFrfqpFDLj_hOmiQ4RhxQogCL9dwGPdDQtbL4f2P__fRk5oaDwJ05OcFZj98HkqpEXh-M4pUAeEAmFNDGh9L5JYUWQhk0cciaga6-hklG5WEJJQFS91Bp1U8r0uPl2fMrIQ==
  - Raya Holding Company for Financial Investments (S.A.E) (EGX:RAYA) Statistics & Valuation Metrics - Stock Analysis (As of 2026-07-12): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtxte-bu9S2JHQGt-IeFjagOOMxMykefRiE3ZXSi-z2wMt3hoJxQIMekSueXIvTkg6OmUZU6RDu0fEDGNmEiWLdsK1evyLbwumYbBzTsR0NThYsFgDygRVHrdr_d-f5BDvk3Y9X4qgqU4e_rJD7Q==
  - EGX:RAYA Financials | Raya Hld - Investing.com (Latest Release: 2026-05-28): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeb8MPXXdbq81E7QJmfwFxn-Ks36E5j9nu9efd9cgnW72I2ANJSMQdY-WTsGtG4DApbrw1-zGNAtRfaVYnD3kYfHeL5NLCaarrChUaEHYg1Br5GHJ30Eerk1NJdr_H9RMA5ROGAxDjPWf4FoICiDNMJBkraEsSo7bRMsXgGw==
- ADPC.CA: status=RECENT_ACCEPTED latest=2026-07-05 age_days=9 sources=3 expected=The Arab Dairy Products Co. summary=The Arab Dairy Products Co. (ADPC.CA) has recent disclosure forms released on the Egyptian Exchange on July 5, 2026, and June 28, 2026. The company, listed on EGX since 2001, operates in the food and beverage sector, focusing on packaged foods and meats. Gadwa for Industrial Development holds a 36.22% ownership stake.
  - The Arab Dairy Products Co. Arab Dairy - Panda (ADPC.CA) - Release Regarding a Disclosure Form - The Egyptian Exchange (Report Date: 2026-07-05): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUxvrUMpW57U9-hdAvYlBMC3WSt3O90D6QDKiqdnkuGCcB8RadKuVPh6M8UMiYMt6a0saNFcXSXwAvTork-drzcSUyXkyGm5RaZvplS6TwLc-M59fLN-Cg3mgChyZVddppaazAix1rbaMCyvOdwDI=
  - The Arab Dairy Products Co. Arab Dairy - Panda (ADPC.CA) - Release Regarding a Disclosure Form - The Egyptian Exchange (Report Date: 2026-06-28): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUxvrUMpW57U9-hdAvYlBMC3WSt3O90D6QDKiqdnkuGCcB8RadKuVPh6M8UMiYMt6a0saNFcXSXwAvTork-drzcSUyXkyGm5RaZvplS6TwLc-M59fLN-Cg3mgChyZVddppaazAix1rbaMCyvOdwDI=
  - Investor Relations - Arab Dairy: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-U4SBC7-jJxUZraJ1xW7nbNuPH7QntZos0VZalFxz2Ag4I8U8p4VPt0SGYGJbPnDsMyGQwMjcFx_eWzcR0GohTQGRCtw9QTFLGInVKJZqVe8j5sdSenefeu-ZF2nAxzuAcw==
- AMOC.CA: status=RECENT_ACCEPTED latest=2026-06-29 age_days=15 sources=3 expected=Alexandria Mineral Oils summary=Alexandria Mineral Oils (AMOC.CA) reported a revised operating budget for FY 2026, projecting a net profit after tax of approximately EGP 2.099 billion (approved June 29, 2026). The company also reported Q1 2026 consolidated net profit of EGP 635.12 million, a 37% increase year-over-year. Financial results for Q1 2026 (standalone) were reported on May 17, 2026. For fiscal year 2025, revenue increased by 11.42% to 37.62 billion EGP, and earnings increased by 18.09% to 1.49 billion EGP.
  - AMOC's Revises FY 2026 Budget Forecsts, Doubles Profit to EGP 2.1 Bn | Egypt Oil & Gas (Report Date: 2026-06-29): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGk4zRE5gXC68P7iz3evY5fIdy1n53_ddCpg_5yw4VInN5QMDgkMS8iMmeimCgzXTX27R7vLz19weW-NmeR7Vc9A3meNq5rmt-wKZ1iGDzHxleg6F8VU5HP6cXtkH5Dv5GGzV4yHbHWY8jdzfz58IBkTBolrnvpKtOaahzZf8C4z4vxbX3cpKL13JQI69PhPzok2wM-LwHcgWqCQ==
  - Alexandria Mineral Oils Company (AMOC.CA) Reports Its Financial Results (Standalone) for The Period From 01/01/2026 to 31/03/2026 - The Egyptian Exchange (Report Date: 2026-05-17): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGESNV2-2eyyDAUa9K-ueJeJImiVp7chdpezfBOXFCNQvSV2kxhkioL6ORTsXSJKCchqwt8Q7UcafT0Eo7pTVjfZprcyM99NnLu0uHMoFqRna9IGiyiDe3O_8wXyWK_pwugqMjgRoPSdfOED1KV3Ds=
  - Alexandria Mineral Oils - EGX:AMOC Financials - Investing.com (Latest Release: 2026-04-22): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXNOTEwTjZu2T8cyXR5b0lkcPDiH_xdQlNCSnT3VJW6nUapeBYlh3X1v9eOfwTgQhtdTpESobEPi9pVrJ8XkTb8Ln77-bXuBPixwYGkUM0QZHx_HzhwtSvg0zOLzOV8_nKWUvRQlWEk6umd5B4wXI_8tkd-Q50Yyva_pQMTg==
- COSG.CA: status=RECENT_ACCEPTED latest=2026-07-07 age_days=7 sources=3 expected=Cairo Oil & Soap Company summary=Cairo Oil & Soap Company (COSG.CA) has recent market announcements from July 2026, including disclosure forms and board meeting minutes. The company reported sales of 283.633 million EGP and a net income of 6.735 million EGP for the latest quarter (released May 11, 2026). For the last 12 months, revenue was EGP 802.09 million with losses of 60.34 million EGP. The company is listed on the EGX since 1999 and specializes in edible oil, butter, and soap manufacturing.
  - Cairo Oils and Soap (COSG) - Mubasher Info (Market Announcements: 2026-07-07, 2026-07-05, 2026-04-26): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH60Scyd6lvGhJ4r4jm2hSfx0Lklpc4fdvp2u_aq2nrw4lxSuVHpioIH2lyEtkSFINSFA71aEMHejTp17k1QTAR-b2EzL9OZNvlKLJhsiy681ikaCOlmSiMgdHoVJAuKSf325EMeiDGpEjr-mYrgriE
  - Cairo Oils & Soap - EGX:COSG Financials - Investing.com (Latest Release: 2026-05-11): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpbaeQz63kN2WRbJNu5VYukA7SsURnjN3Km-YMjMlsC26nYBs6xx3BLhA3K0wCj0BbDTJ-flFU3S2HM3gyUwg5-97OmUsXT__viQ18wYltUND1prWBV4oFp9erl8fnA6CwnHtNCMu2MwfCX3e7PTIqiDr1QSGg64yFL37TPw==
  - Cairo Oil & Soap Company (EGX:COSG) Statistics & Valuation Metrics - Stock Analysis (As of 2026-07-01): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWWAeL73s4oXXpRRWQllU4KjLg_KiamRjJu5LQV9rNR2ADCh7Lh4NuMTrjAnEFLGQvULg_bhOR1CVxAQFCouMnSGHkoSiwBzcua69C9htGXB0j8by9bAlxuUnjxU2sH2kfPifFre-FuCu53ts9Nw==

## Warnings
- Evidence for AREH.CA matches the company but no source/report date was detected.
- Evidence for ELEC.CA matches the company but appears old; latest detected date is 2025-03-31.
- Evidence rejected for EGAS.CA: source text did not clearly match EGAS.CA / Natural Gas and Mining Project.
