# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-07-13T09:49:30.666068+00:00
Generated Cairo: 2026-07-13 12:49
Run timing: target 09:15 Cairo | generated Cairo 2026-07-13 12:49 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-07-13 12:45

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 80
- Data quality issues: 1
- Tradeable price/liquidity tickers: 180/189
- Top sector: Technology & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, July 13
- Freshness: DELAYED
- EGX30 regime: CONSTRUCTIVE / above MA20 60.0% / above MA50 50.0%
- EGX70 regime: BULLISH / above MA20 77.5% / above MA50 72.5%
- Sector breadth: 52.38%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- CCAP.CA: liquidity=724020736.0 spike=1.11 score=26.62
- COMI.CA: liquidity=206324032.0 spike=0.47 score=25.84
- ZMID.CA: liquidity=198496512.0 spike=0.91 score=27.4
- ARAB.CA: liquidity=153119664.0 spike=1.7 score=28.8
- RAYA.CA: liquidity=135891936.0 spike=1.19 score=29.78

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner highlights ELEC.CA as the top buy‑ready candidate, followed by MCRO.CA and COSG.CA. All three show price above MA20/MA50, modest RSI, and clear support‑resistance zones, with liquidity spikes indicating accumulation. EGX70 is in a bullish regime while EGX30 remains constructive, pushing the system into a SELECTIVE_SWING_TRADES_ONLY risk mode. Expect the next 1‑3 days to be driven by short‑term price action around the identified support (2.04 EGP for ELEC) and resistance (2.18 EGP), but low confidence and sector‑lead lag add uncertainty.
- ELEC.CA: price at resistance 2.18 EGP, support 2.04 EGP, RSI 51.9, liquidity spike 4.86×, sector Industrial Goods & Cables (2nd rank).
- MCRO.CA & COSG.CA: above MA20/MA50, RSI 65.5 / 54.6, support 1.17 EGP & 1.47 EGP, resistance at entry levels, but sectors not leading.
- EGX70 bullish, EGX30 constructive → risk mode SELECTIVE_SWING_TRADES_ONLY; focus on swing entries, verify on Thndr.
- Liquidity spikes suggest accumulation, yet confidence low; watch for price breaking resistance or falling back to support.
- Uncertainty remains from sector weakness and macro‑level earnings dips (e.g., ELEC loss report).

## Top Liquidity Spikes
- RACC.CA: spike=9.95 liquidity=104019848.0 outlook=BULLISH_WATCH score=77.64 buy_ready=True
- CPCI.CA: spike=8.23 liquidity=21636448.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MOSC.CA: spike=7.74 liquidity=70856736.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- OCPH.CA: spike=7.16 liquidity=44803972.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GDWA.CA: spike=5.5 liquidity=89456344.0 outlook=BULLISH_WATCH score=92.64 buy_ready=True

## Sector Leaderboard
- #1 Technology & Distribution: score=13.29 5d=4.42% 20d=18.68% aboveMA50=100.0%
- #2 Industrial Goods & Cables: score=11.66 5d=2.41% 20d=4.51% aboveMA50=100.0%
- #3 Real Estate: score=10.38 5d=3.68% 20d=14.76% aboveMA50=100.0%
- #4 Transportation & Logistics: score=10.25 5d=3.01% 20d=7.21% aboveMA50=100.0%
- #5 Telecommunications: score=10.13 5d=5.07% 20d=6.67% aboveMA50=100.0%
- #6 Automotive & Distribution: score=9.67 5d=-0.72% 20d=9.65% aboveMA50=100.0%
- #7 Fintech & Payments: score=8.61 5d=4.38% 20d=9.24% aboveMA50=50.0%
- #8 Textiles: score=8.31 5d=3.17% 20d=5.0% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- Priority #1: BUY ELEC.CA
  - Entry: 2.18 | Take profit: 2.36 | Stop loss: 2.09
  - Confidence: LOW | score=34.4 | outlook=BULLISH_WATCH 100
  - Reason: BUY SETUP: ELEC.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 51.85, support 2.04, resistance 2.18, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY MCRO.CA
  - Entry: 1.33 | Take profit: 1.43 | Stop loss: 1.28
  - Confidence: LOW | score=29.58 | outlook=BULLISH_WATCH 78.64
  - Reason: WATCH/BUY SETUP: MCRO.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 65.52, support 1.17, resistance 1.33, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY COSG.CA
  - Entry: 1.67 | Take profit: 1.81 | Stop loss: 1.6
  - Confidence: LOW | score=29.42 | outlook=BULLISH_WATCH 91.64
  - Reason: BUY SETUP: COSG.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 54.55, support 1.47, resistance 1.66, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ELEC.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- ALCN.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- MTIE.CA: BULLISH_WATCH score=96.67 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- GDWA.CA: BULLISH_WATCH score=92.64 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- AREH.CA: BULLISH_WATCH score=91.64 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- COSG.CA: BULLISH_WATCH score=91.64 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- TMGH.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- SWDY.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- NINH.CA: BULLISH_WATCH score=89.64 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ZMID.CA: BULLISH_WATCH score=89 liquidity=TRADEABLE sector=LEADING risk=momentum is extended

## BUY-Ready Candidates
- ELEC.CA: rank=34.4 outlook=BULLISH_WATCH outlook_score=100 sector_rank=2 price=2.18 support=2.04 resistance=2.18 liquidity=92052784.0
- AREH.CA: rank=32.46 outlook=BULLISH_WATCH outlook_score=91.64 sector_rank=9 price=1.72 support=1.51 resistance=1.76 liquidity=107658224.0
- GDWA.CA: rank=32.4 outlook=BULLISH_WATCH outlook_score=92.64 sector_rank=9 price=0.84 support=0.76 resistance=0.82 liquidity=89456344.0
- RACC.CA: rank=31.4 outlook=BULLISH_WATCH outlook_score=77.64 sector_rank=9 price=10.5 support=9.36 resistance=10.57 liquidity=104019848.0
- RAYA.CA: rank=29.78 outlook=BULLISH_WATCH outlook_score=77 sector_rank=1 price=8.39 support=6.8 resistance=8.29 liquidity=135891936.0
- MCRO.CA: rank=29.58 outlook=BULLISH_WATCH outlook_score=78.64 sector_rank=9 price=1.33 support=1.17 resistance=1.33 liquidity=105018768.0
- COSG.CA: rank=29.42 outlook=BULLISH_WATCH outlook_score=91.64 sector_rank=9 price=1.67 support=1.47 resistance=1.66 liquidity=60865264.0
- MOED.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=86.64 sector_rank=9 price=0.73 support=0.65 resistance=0.72 liquidity=41770468.0
- ADPC.CA: rank=29.02 outlook=CONSTRUCTIVE outlook_score=61.64 sector_rank=9 price=3.77 support=3.32 resistance=3.94 liquidity=36785324.0
- ACGC.CA: rank=28.78 outlook=BULLISH_WATCH outlook_score=86.31 sector_rank=8 price=9.99 support=8.92 resistance=9.88 liquidity=25994730.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=25.45 buy_ready=False sector_rank=9 price=233.56 support=196.0 resistance=247.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=70.14 liquidity=9045695.0 spike=0.61
- ABUK.CA: score=19.94 buy_ready=False sector_rank=19 price=69.68 support=66.66 resistance=77.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=42.84 liquidity=51074852.0 spike=0.36
- ACAMD.CA: score=26.4 buy_ready=True sector_rank=9 price=2.34 support=2.14 resistance=2.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:26 AM market time freshness=DELAYED_CURRENT RSI=45.0 liquidity=26379492.0 spike=0.28
- ACGC.CA: score=28.78 buy_ready=True sector_rank=8 price=9.99 support=8.92 resistance=9.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=54.07 liquidity=25994730.0 spike=1.19
- ADCI.CA: score=24.4 buy_ready=True sector_rank=9 price=239.28 support=223.0 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=51.65 liquidity=10631186.0 spike=0.89
- ADIB.CA: score=20.84 buy_ready=False sector_rank=16 price=46.6 support=44.1 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=49.79 liquidity=49248844.0 spike=0.52
- ADPC.CA: score=29.02 buy_ready=True sector_rank=9 price=3.77 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=39.0 liquidity=36785324.0 spike=2.31
- AFDI.CA: score=28.4 buy_ready=True sector_rank=9 price=47.43 support=40.8 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=59.42 liquidity=11254165.0 spike=0.83
- AFMC.CA: score=26.49 buy_ready=True sector_rank=9 price=74.43 support=66.0 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=57.13 liquidity=7614602.0 spike=2.24
- AJWA.CA: score=17.05 buy_ready=True sector_rank=9 price=182.01 support=150.51 resistance=190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=57.66 liquidity=2649864.0 spike=0.1
- ALCN.CA: score=28.36 buy_ready=True sector_rank=4 price=30.25 support=27.7 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=66.15 liquidity=32800974.0 spike=1.98
- ALUM.CA: score=15.33 buy_ready=False sector_rank=9 price=22.81 support=20.55 resistance=24.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=44.37 liquidity=1932350.63 spike=0.25
- AMER.CA: score=24.4 buy_ready=False sector_rank=3 price=3.16 support=2.28 resistance=3.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=76.8 liquidity=45650556.0 spike=0.56
- AMES.CA: score=12.02 buy_ready=False sector_rank=9 price=91.06 support=83.13 resistance=94.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=94735344.0 spike=2.31
- AMIA.CA: score=16.33 buy_ready=True sector_rank=9 price=8.97 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=46.46 liquidity=1927242.63 spike=0.2
- AMOC.CA: score=22.88 buy_ready=False sector_rank=15 price=8.06 support=7.42 resistance=8.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=56.63 liquidity=37226864.0 spike=0.72
- APSW.CA: score=15.98 buy_ready=False sector_rank=9 price=8.52 support=8.0 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:28 AM market time freshness=DELAYED_CURRENT RSI=45.6 liquidity=1704799.5 spike=1.94
- ARAB.CA: score=28.8 buy_ready=False sector_rank=3 price=0.25 support=0.2 resistance=0.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=153119664.0 spike=1.7
- ARCC.CA: score=13.9 buy_ready=False sector_rank=18 price=55.34 support=53.0 resistance=57.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=46.04 liquidity=5478534.0 spike=0.27
- AREH.CA: score=32.46 buy_ready=True sector_rank=9 price=1.72 support=1.51 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 July 01:29 PM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=107658224.0 spike=3.03
- ARVA.CA: score=17.74 buy_ready=False sector_rank=9 price=10.8 support=10.5 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=46.12 liquidity=5340717.5 spike=0.25
- ASCM.CA: score=24.4 buy_ready=True sector_rank=9 price=62.91 support=56.29 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=57.49 liquidity=40947672.0 spike=0.5
- ASPI.CA: score=19.4 buy_ready=False sector_rank=9 price=0.31 support=0.3 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=39.06 liquidity=12856652.0 spike=0.45
- ATLC.CA: score=15.64 buy_ready=True sector_rank=17 price=5.23 support=4.77 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=44.85 liquidity=2028665.5 spike=0.29
- ATQA.CA: score=19.02 buy_ready=False sector_rank=19 price=9.59 support=9.21 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=52.34 liquidity=8077371.0 spike=0.25
- AXPH.CA: score=24.24 buy_ready=True sector_rank=9 price=1207.72 support=1073.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=63.99 liquidity=5875599.5 spike=1.98
- BINV.CA: score=15.08 buy_ready=False sector_rank=11 price=48.6 support=45.01 resistance=51.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT RSI=54.5 liquidity=684304.25 spike=0.11
- BIOC.CA: score=20.56 buy_ready=True sector_rank=9 price=74.61 support=66.75 resistance=76.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=52.12 liquidity=2162720.75 spike=0.67
- BTFH.CA: score=21.62 buy_ready=False sector_rank=17 price=3.06 support=2.91 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=43.9 liquidity=92331904.0 spike=0.48
- CAED.CA: score=22.96 buy_ready=True sector_rank=9 price=74.65 support=68.0 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=51.31 liquidity=4561313.0 spike=0.7
- CANA.CA: score=14.35 buy_ready=False sector_rank=16 price=36.37 support=34.7 resistance=38.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=41.44 liquidity=1510906.5 spike=0.15
- CCAP.CA: score=26.62 buy_ready=True sector_rank=11 price=5.37 support=4.65 resistance=5.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=59.41 liquidity=724020736.0 spike=1.11
- CCRS.CA: score=14.4 buy_ready=False sector_rank=9 price=2.53 support=2.42 resistance=2.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39857344.0 spike=3.54
- CEFM.CA: score=14.05 buy_ready=False sector_rank=9 price=105.27 support=95.75 resistance=110.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=55.4 liquidity=653456.44 spike=0.3
- CERA.CA: score=22.26 buy_ready=True sector_rank=9 price=1.32 support=1.17 resistance=1.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=5855949.5 spike=0.27
- CFGH.CA: score=8.43 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 July 01:25 PM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=9605.83 spike=1.51
- CICH.CA: score=14.03 buy_ready=False sector_rank=17 price=11.85 support=11.36 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=34.72 liquidity=8138942.0 spike=2.14
- CIEB.CA: score=17.3 buy_ready=True sector_rank=16 price=24.37 support=23.3 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=53.42 liquidity=1458369.0 spike=0.21
- CIRA.CA: score=26.54 buy_ready=False sector_rank=12 price=30.61 support=26.0 resistance=31.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=70.57 liquidity=28479756.0 spike=1.22
- CLHO.CA: score=24.0 buy_ready=True sector_rank=14 price=16.3 support=14.85 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=55.59 liquidity=24587470.0 spike=0.69
- CNFN.CA: score=24.69 buy_ready=True sector_rank=17 price=4.85 support=4.4 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=9075831.0 spike=0.21
- COMI.CA: score=25.84 buy_ready=True sector_rank=16 price=136.7 support=126.21 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=45.96 liquidity=206324032.0 spike=0.47
- COPR.CA: score=21.58 buy_ready=False sector_rank=9 price=0.37 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=32.73 liquidity=54454580.0 spike=2.59
- COSG.CA: score=29.42 buy_ready=True sector_rank=9 price=1.67 support=1.47 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=60865264.0 spike=1.51
- CPCI.CA: score=14.4 buy_ready=False sector_rank=9 price=476.41 support=400.03 resistance=482.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21636448.0 spike=8.23
- CSAG.CA: score=19.15 buy_ready=True sector_rank=4 price=32.51 support=30.85 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=64.2 liquidity=2753230.0 spike=0.16
- DAPH.CA: score=24.01 buy_ready=True sector_rank=9 price=84.2 support=77.12 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=59.99 liquidity=5607632.0 spike=0.63
- DEIN.CA: score=-0.6 buy_ready=False sector_rank=9 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=16.79 buy_ready=False sector_rank=13 price=27.07 support=24.21 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:11 AM market time freshness=DELAYED_CURRENT RSI=60.17 liquidity=746375.88 spike=0.14
- DSCW.CA: score=27.8 buy_ready=True sector_rank=9 price=1.85 support=1.71 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=40.91 liquidity=60815040.0 spike=2.2
- DTPP.CA: score=23.4 buy_ready=False sector_rank=9 price=209.83 support=114.0 resistance=234.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=89.03 liquidity=11465215.0 spike=0.31
- EALR.CA: score=26.54 buy_ready=True sector_rank=9 price=369.34 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=57.03 liquidity=12560392.0 spike=1.07
- EASB.CA: score=22.4 buy_ready=False sector_rank=9 price=7.3 support=5.06 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=36.74 liquidity=12498997.0 spike=0.72
- EAST.CA: score=13.04 buy_ready=False sector_rank=13 price=36.64 support=36.6 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=29.64 liquidity=16525291.0 spike=0.37
- EBSC.CA: score=19.63 buy_ready=True sector_rank=9 price=1.95 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:28 AM market time freshness=DELAYED_CURRENT RSI=51.95 liquidity=3233247.0 spike=0.56
- ECAP.CA: score=14.21 buy_ready=False sector_rank=9 price=32.68 support=31.15 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=35.35 liquidity=1806806.88 spike=0.2
- EDFM.CA: score=20.8 buy_ready=True sector_rank=9 price=345.03 support=310.2 resistance=349.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=66.15 liquidity=1741951.13 spike=2.33
- EEII.CA: score=18.9 buy_ready=True sector_rank=9 price=2.79 support=2.35 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=67.03 liquidity=4502749.5 spike=0.21
- EFIC.CA: score=4.1 buy_ready=False sector_rank=19 price=187.57 support=180.02 resistance=207.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=19.85 liquidity=2156295.5 spike=0.83
- EFID.CA: score=25.95 buy_ready=True sector_rank=13 price=28.34 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=52.8 liquidity=9907618.0 spike=0.2
- EFIH.CA: score=26.4 buy_ready=True sector_rank=7 price=22.44 support=20.0 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=60.96 liquidity=21793332.0 spike=0.49
- EGAL.CA: score=19.94 buy_ready=False sector_rank=19 price=292.11 support=272.28 resistance=314.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=45.96 liquidity=17913974.0 spike=0.37
- EGAS.CA: score=13.88 buy_ready=False sector_rank=15 price=53.68 support=50.01 resistance=53.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=43866388.0 spike=5.38
- EGBE.CA: score=13.91 buy_ready=False sector_rank=16 price=0.45 support=0.43 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=64182.34 spike=1.0
- EGCH.CA: score=22.02 buy_ready=False sector_rank=19 price=13.21 support=12.13 resistance=14.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=40.88 liquidity=46431724.0 spike=1.04
- EGSA.CA: score=13.4 buy_ready=False sector_rank=5 price=9.08 support=8.67 resistance=9.13 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=91.67 liquidity=1979.44 spike=0.39
- EGTS.CA: score=24.68 buy_ready=True sector_rank=3 price=18.38 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=48.79 liquidity=7282175.0 spike=0.12
- EHDR.CA: score=26.4 buy_ready=True sector_rank=9 price=2.72 support=2.37 resistance=2.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=51.76 liquidity=15315679.0 spike=0.37
- EKHO.CA: score=7.88 buy_ready=False sector_rank=15 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=34.4 buy_ready=True sector_rank=2 price=2.18 support=2.04 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=92052784.0 spike=4.86
- ELKA.CA: score=26.4 buy_ready=False sector_rank=9 price=1.65 support=1.19 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=72.22 liquidity=14649013.0 spike=0.29
- ELNA.CA: score=17.15 buy_ready=False sector_rank=9 price=39.58 support=35.55 resistance=40.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=46.25 liquidity=651846.94 spike=1.05
- ELSH.CA: score=28.4 buy_ready=True sector_rank=9 price=14.8 support=11.1 resistance=15.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=64.31 liquidity=54248260.0 spike=0.31
- ELWA.CA: score=16.68 buy_ready=True sector_rank=9 price=2.06 support=1.87 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=43.9 liquidity=2004525.63 spike=1.14
- EMFD.CA: score=23.4 buy_ready=False sector_rank=3 price=11.8 support=11.24 resistance=12.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=43.69 liquidity=56445612.0 spike=0.39
- ENGC.CA: score=27.04 buy_ready=False sector_rank=9 price=41.4 support=33.91 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=73.42 liquidity=31220522.0 spike=1.32
- EOSB.CA: score=14.44 buy_ready=False sector_rank=9 price=1.48 support=1.42 resistance=1.55 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=35839.68 spike=0.47
- EPCO.CA: score=19.12 buy_ready=True sector_rank=9 price=9.22 support=8.5 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:28 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=2715097.75 spike=0.4
- EPPK.CA: score=14.86 buy_ready=False sector_rank=9 price=14.29 support=11.72 resistance=15.25 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=69.3 liquidity=455879.58 spike=0.48
- ETEL.CA: score=28.4 buy_ready=True sector_rank=5 price=98.28 support=89.01 resistance=101.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=64.17 liquidity=45816380.0 spike=0.63
- ETRS.CA: score=19.97 buy_ready=True sector_rank=9 price=10.87 support=9.15 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=50.55 liquidity=5566179.0 spike=0.07
- EXPA.CA: score=22.41 buy_ready=True sector_rank=16 price=18.72 support=18.03 resistance=18.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=56.44 liquidity=4570019.0 spike=0.17
- FAIT.CA: score=16.63 buy_ready=False sector_rank=16 price=37.09 support=35.06 resistance=37.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=50.44 liquidity=790172.19 spike=0.31
- FAITA.CA: score=8.85 buy_ready=False sector_rank=16 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=44.83 liquidity=9466.08 spike=0.32
- FERC.CA: score=12.58 buy_ready=False sector_rank=19 price=75.5 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=48.71 liquidity=1633032.88 spike=0.41
- FWRY.CA: score=23.4 buy_ready=False sector_rank=7 price=19.28 support=18.13 resistance=19.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=60.28 liquidity=34434624.0 spike=0.19
- GBCO.CA: score=24.4 buy_ready=True sector_rank=6 price=31.95 support=27.77 resistance=32.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:27 AM market time freshness=DELAYED_CURRENT RSI=64.63 liquidity=68322896.0 spike=0.8
- GDWA.CA: score=32.4 buy_ready=True sector_rank=9 price=0.84 support=0.76 resistance=0.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=51.8 liquidity=89456344.0 spike=5.5
- GGCC.CA: score=17.31 buy_ready=False sector_rank=9 price=0.57 support=0.41 resistance=0.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=92.74 liquidity=3914949.0 spike=0.23
- GIHD.CA: score=26.42 buy_ready=True sector_rank=9 price=50.52 support=40.0 resistance=52.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=69.42 liquidity=43762300.0 spike=2.01
- GMCI.CA: score=15.21 buy_ready=False sector_rank=9 price=2.01 support=1.66 resistance=2.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:26 AM market time freshness=DELAYED_CURRENT RSI=65.28 liquidity=806397.13 spike=0.74
- GRCA.CA: score=19.4 buy_ready=False sector_rank=9 price=51.33 support=48.0 resistance=58.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:28 AM market time freshness=DELAYED_CURRENT RSI=13.23 liquidity=11257564.0 spike=3.67
- GSSC.CA: score=18.63 buy_ready=True sector_rank=9 price=260.67 support=240.0 resistance=263.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:28 AM market time freshness=DELAYED_CURRENT RSI=65.51 liquidity=2234345.75 spike=0.5
- GTWL.CA: score=21.4 buy_ready=False sector_rank=9 price=109.62 support=46.0 resistance=117.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=89.45 liquidity=64636812.0 spike=0.68
- HDBK.CA: score=12.84 buy_ready=False sector_rank=16 price=78.15 support=75.3 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=10.6 liquidity=11600589.0 spike=0.29
- HELI.CA: score=24.4 buy_ready=False sector_rank=3 price=7.4 support=6.34 resistance=7.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=75.72 liquidity=68365656.0 spike=0.43
- HRHO.CA: score=17.62 buy_ready=False sector_rank=17 price=26.61 support=26.09 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=36.62 liquidity=57327512.0 spike=0.45
- ICID.CA: score=20.97 buy_ready=True sector_rank=9 price=8.3 support=6.55 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=59.95 liquidity=6569612.5 spike=0.61
- IDRE.CA: score=27.09 buy_ready=True sector_rank=9 price=46.3 support=41.1 resistance=47.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=57.98 liquidity=8688451.0 spike=0.67
- IFAP.CA: score=14.84 buy_ready=False sector_rank=10 price=19.5 support=18.47 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=57.21 liquidity=1444737.5 spike=0.3
- INFI.CA: score=26.3 buy_ready=False sector_rank=9 price=104.52 support=88.51 resistance=106.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=71.89 liquidity=9877560.0 spike=1.01
- IRON.CA: score=12.37 buy_ready=False sector_rank=19 price=32.1 support=30.51 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:26 AM market time freshness=DELAYED_CURRENT RSI=49.19 liquidity=3424752.0 spike=0.43
- ISMA.CA: score=11.05 buy_ready=False sector_rank=9 price=27.25 support=26.54 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=16.02 liquidity=3653419.0 spike=0.13
- ISMQ.CA: score=22.94 buy_ready=False sector_rank=19 price=9.65 support=8.06 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=72.31 liquidity=41196108.0 spike=0.28
- ISPH.CA: score=14.0 buy_ready=False sector_rank=14 price=11.5 support=11.2 resistance=12.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=27.27 liquidity=28621180.0 spike=0.47
- JUFO.CA: score=16.34 buy_ready=False sector_rank=13 price=30.63 support=29.1 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=40.22 liquidity=4304078.0 spike=0.17
- KABO.CA: score=23.4 buy_ready=False sector_rank=8 price=7.51 support=6.04 resistance=7.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=88.76 liquidity=17467416.0 spike=0.6
- KWIN.CA: score=14.4 buy_ready=False sector_rank=9 price=69.0 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=33.96 liquidity=11495387.0 spike=0.86
- KZPC.CA: score=18.1 buy_ready=False sector_rank=9 price=8.7 support=8.26 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=29.44 liquidity=15608580.0 spike=2.35
- LCSW.CA: score=25.42 buy_ready=True sector_rank=18 price=31.61 support=26.41 resistance=32.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=67.42 liquidity=10647100.0 spike=0.18
- LUTS.CA: score=22.4 buy_ready=False sector_rank=9 price=0.74 support=0.69 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=42.08 liquidity=13392056.0 spike=0.27
- MAAL.CA: score=21.92 buy_ready=False sector_rank=9 price=8.11 support=5.72 resistance=8.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=98.01 liquidity=20640848.0 spike=1.26
- MASR.CA: score=28.4 buy_ready=True sector_rank=9 price=8.14 support=6.71 resistance=7.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=62.67 liquidity=61472672.0 spike=0.72
- MBSC.CA: score=18.16 buy_ready=False sector_rank=18 price=240.9 support=222.66 resistance=256.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:28 AM market time freshness=DELAYED_CURRENT RSI=39.92 liquidity=7744706.5 spike=0.33
- MCQE.CA: score=15.04 buy_ready=False sector_rank=18 price=177.0 support=166.66 resistance=182.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=46.1 liquidity=2622565.5 spike=0.18
- MCRO.CA: score=29.58 buy_ready=True sector_rank=9 price=1.33 support=1.17 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=65.52 liquidity=105018768.0 spike=3.09
- MENA.CA: score=17.99 buy_ready=False sector_rank=3 price=7.07 support=6.41 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=58.06 liquidity=593185.25 spike=0.07
- MEPA.CA: score=24.78 buy_ready=False sector_rank=9 price=1.67 support=1.52 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=44.74 liquidity=18319116.0 spike=1.69
- MFPC.CA: score=21.94 buy_ready=False sector_rank=19 price=37.3 support=34.22 resistance=40.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=49.84 liquidity=25824808.0 spike=0.26
- MFSC.CA: score=12.62 buy_ready=False sector_rank=9 price=45.75 support=44.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=51.37 liquidity=3219517.0 spike=0.42
- MHOT.CA: score=2.37 buy_ready=False sector_rank=21 price=16.48 support=16.12 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=15.69 liquidity=2973294.5 spike=0.19
- MICH.CA: score=14.16 buy_ready=False sector_rank=9 price=37.56 support=34.0 resistance=39.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=38.69 liquidity=1759719.75 spike=0.11
- MILS.CA: score=24.4 buy_ready=True sector_rank=9 price=137.12 support=126.31 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=48.18 liquidity=10408233.0 spike=0.93
- MIPH.CA: score=18.55 buy_ready=True sector_rank=14 price=704.4 support=630.13 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:27 AM market time freshness=DELAYED_CURRENT RSI=51.34 liquidity=2325978.75 spike=1.11
- MOED.CA: score=29.4 buy_ready=True sector_rank=9 price=0.73 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=55.62 liquidity=41770468.0 spike=3.91
- MOIL.CA: score=16.09 buy_ready=False sector_rank=15 price=0.54 support=0.46 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=69.47 liquidity=538252.81 spike=1.84
- MOIN.CA: score=12.82 buy_ready=False sector_rank=9 price=23.95 support=22.6 resistance=25.25 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=48.18 liquidity=418933.41 spike=0.55
- MOSC.CA: score=14.4 buy_ready=False sector_rank=9 price=301.32 support=275.0 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=70856736.0 spike=7.74
- MPCI.CA: score=24.4 buy_ready=True sector_rank=9 price=242.31 support=215.0 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=49.77 liquidity=14035808.0 spike=0.14
- MPCO.CA: score=24.4 buy_ready=True sector_rank=10 price=1.89 support=1.7 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=50913256.0 spike=0.61
- MPRC.CA: score=23.4 buy_ready=False sector_rank=9 price=42.28 support=31.72 resistance=43.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=89.47 liquidity=16380264.0 spike=0.35
- MTIE.CA: score=28.2 buy_ready=True sector_rank=6 price=9.74 support=8.75 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=55.23 liquidity=38927104.0 spike=1.9
- NAHO.CA: score=12.61 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=55.56 liquidity=48426.17 spike=2.08
- NCCW.CA: score=24.92 buy_ready=True sector_rank=9 price=6.56 support=5.82 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=51.79 liquidity=31154032.0 spike=1.26
- NEDA.CA: score=17.23 buy_ready=False sector_rank=9 price=2.8 support=2.7 resistance=2.83 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=57.14 liquidity=386822.79 spike=1.22
- NHPS.CA: score=27.42 buy_ready=False sector_rank=9 price=79.96 support=61.55 resistance=83.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=75.67 liquidity=95547368.0 spike=3.01
- NINH.CA: score=26.12 buy_ready=True sector_rank=9 price=18.33 support=16.82 resistance=18.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=51.8 liquidity=24624464.0 spike=3.36
- NIPH.CA: score=26.0 buy_ready=True sector_rank=14 price=178.02 support=157.01 resistance=185.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=60.61 liquidity=52476272.0 spike=0.6
- OBRI.CA: score=26.4 buy_ready=True sector_rank=9 price=36.7 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=55.18 liquidity=10973751.0 spike=0.33
- OCDI.CA: score=22.4 buy_ready=False sector_rank=3 price=26.87 support=20.24 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:27 AM market time freshness=DELAYED_CURRENT RSI=78.6 liquidity=18225588.0 spike=0.18
- OCPH.CA: score=14.4 buy_ready=False sector_rank=9 price=375.0 support=352.5 resistance=385.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=44803972.0 spike=7.16
- ODIN.CA: score=10.12 buy_ready=False sector_rank=9 price=2.47 support=2.36 resistance=2.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19319576.0 spike=1.36
- OFH.CA: score=24.89 buy_ready=True sector_rank=9 price=0.63 support=0.57 resistance=0.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=61.46 liquidity=8489159.0 spike=0.4
- OIH.CA: score=21.4 buy_ready=False sector_rank=11 price=1.42 support=1.35 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=14935171.0 spike=0.22
- OLFI.CA: score=26.04 buy_ready=True sector_rank=13 price=22.99 support=21.0 resistance=23.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=58.56 liquidity=26310950.0 spike=0.8
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=684.52 support=681.14 resistance=691.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=34762304.0 spike=1.0
- ORHD.CA: score=25.4 buy_ready=True sector_rank=3 price=39.0 support=36.92 resistance=39.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=47.12 liquidity=39828456.0 spike=0.24
- ORWE.CA: score=21.3 buy_ready=False sector_rank=8 price=22.69 support=21.95 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=37.21 liquidity=8901872.0 spike=0.46
- PHAR.CA: score=16.97 buy_ready=False sector_rank=14 price=86.36 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=39.19 liquidity=7971340.0 spike=0.37
- PHDC.CA: score=18.4 buy_ready=False sector_rank=3 price=14.84 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=94072264.0 spike=0.29
- PHTV.CA: score=14.78 buy_ready=False sector_rank=9 price=301.01 support=204.03 resistance=304.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=89.79 liquidity=1379763.25 spike=0.1
- POUL.CA: score=24.04 buy_ready=True sector_rank=13 price=39.98 support=34.99 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=69.01 liquidity=27879020.0 spike=0.65
- PRCL.CA: score=16.09 buy_ready=False sector_rank=18 price=34.81 support=24.14 resistance=36.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=75.45 liquidity=5669225.0 spike=0.12
- PRDC.CA: score=27.4 buy_ready=True sector_rank=3 price=8.49 support=6.2 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=59.52 liquidity=19364008.0 spike=0.13
- PRMH.CA: score=24.4 buy_ready=True sector_rank=9 price=2.71 support=2.34 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=46.24 liquidity=16298179.0 spike=0.52
- RACC.CA: score=31.4 buy_ready=True sector_rank=9 price=10.5 support=9.36 resistance=10.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=58.48 liquidity=104019848.0 spike=9.95
- RAKT.CA: score=10.95 buy_ready=False sector_rank=9 price=22.57 support=21.25 resistance=23.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:06 AM market time freshness=DELAYED_CURRENT RSI=57.11 liquidity=329449.63 spike=1.11
- RAYA.CA: score=29.78 buy_ready=True sector_rank=1 price=8.39 support=6.8 resistance=8.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=63.79 liquidity=135891936.0 spike=1.19
- RMDA.CA: score=21.09 buy_ready=False sector_rank=14 price=5.0 support=4.81 resistance=5.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=9087892.0 spike=0.41
- ROTO.CA: score=25.29 buy_ready=True sector_rank=9 price=44.35 support=33.7 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=54.28 liquidity=8886149.0 spike=0.27
- RREI.CA: score=28.4 buy_ready=True sector_rank=9 price=3.84 support=3.34 resistance=3.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=60.87 liquidity=10139123.0 spike=0.52
- RTVC.CA: score=15.11 buy_ready=False sector_rank=9 price=3.87 support=3.55 resistance=3.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:27 AM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=1707499.75 spike=0.4
- RUBX.CA: score=21.4 buy_ready=False sector_rank=9 price=13.28 support=9.8 resistance=14.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=80.15 liquidity=20085548.0 spike=0.37
- SAUD.CA: score=13.84 buy_ready=False sector_rank=16 price=21.58 support=19.99 resistance=22.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:26 AM market time freshness=DELAYED_CURRENT RSI=49.15 liquidity=994807.63 spike=0.15
- SCEM.CA: score=17.19 buy_ready=False sector_rank=18 price=61.96 support=60.14 resistance=67.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=52.02 liquidity=6765021.0 spike=0.4
- SCFM.CA: score=20.11 buy_ready=False sector_rank=9 price=255.53 support=226.5 resistance=269.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=54.22 liquidity=4711845.5 spike=0.87
- SCTS.CA: score=17.42 buy_ready=True sector_rank=12 price=617.58 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=59.37 liquidity=1319768.63 spike=0.24
- SDTI.CA: score=15.8 buy_ready=True sector_rank=9 price=47.49 support=45.55 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=49.44 liquidity=1397549.38 spike=0.17
- SEIG.CA: score=23.4 buy_ready=False sector_rank=9 price=260.34 support=180.6 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=85.04 liquidity=16028640.0 spike=0.83
- SIPC.CA: score=19.24 buy_ready=True sector_rank=9 price=3.53 support=3.25 resistance=3.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=46.75 liquidity=2835038.75 spike=0.34
- SKPC.CA: score=20.76 buy_ready=False sector_rank=19 price=16.4 support=15.58 resistance=16.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=48.21 liquidity=9811087.0 spike=0.31
- SMFR.CA: score=14.22 buy_ready=False sector_rank=9 price=203.97 support=187.01 resistance=209.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=51.46 liquidity=824779.19 spike=0.45
- SNFC.CA: score=10.79 buy_ready=False sector_rank=9 price=11.79 support=11.26 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:28 AM market time freshness=DELAYED_CURRENT RSI=46.55 liquidity=1388336.25 spike=0.12
- SPIN.CA: score=14.84 buy_ready=False sector_rank=8 price=14.61 support=13.3 resistance=14.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=3442577.25 spike=0.38
- SPMD.CA: score=20.3 buy_ready=True sector_rank=9 price=0.45 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=3902078.25 spike=0.22
- SUGR.CA: score=8.23 buy_ready=False sector_rank=13 price=47.19 support=45.31 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=5091252.0 spike=1.05
- SVCE.CA: score=26.4 buy_ready=True sector_rank=9 price=9.41 support=8.35 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=52.6 liquidity=16200067.0 spike=0.23
- SWDY.CA: score=20.98 buy_ready=True sector_rank=2 price=88.42 support=84.3 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=56.06 liquidity=2576342.75 spike=0.2
- TALM.CA: score=12.75 buy_ready=False sector_rank=12 price=15.52 support=15.27 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:26 AM market time freshness=DELAYED_CURRENT RSI=30.07 liquidity=8653908.0 spike=0.75
- TMGH.CA: score=27.4 buy_ready=True sector_rank=3 price=97.42 support=92.1 resistance=99.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=48.25 liquidity=90224712.0 spike=0.25
- TRTO.CA: score=13.36 buy_ready=False sector_rank=9 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=751.23 spike=2.48
- UEFM.CA: score=16.89 buy_ready=False sector_rank=9 price=500.35 support=460.0 resistance=529.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=60.58 liquidity=494713.38 spike=0.32
- UEGC.CA: score=23.4 buy_ready=False sector_rank=9 price=1.9 support=1.33 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=80.3 liquidity=18109372.0 spike=0.79
- UNIP.CA: score=25.14 buy_ready=True sector_rank=9 price=0.34 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=6742862.5 spike=0.38
- UNIT.CA: score=18.31 buy_ready=False sector_rank=3 price=19.16 support=12.0 resistance=20.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=76.24 liquidity=5913773.0 spike=0.28
- WCDF.CA: score=12.57 buy_ready=False sector_rank=9 price=515.94 support=450.0 resistance=544.99 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=39.17 liquidity=767718.72 spike=2.2
- WKOL.CA: score=22.56 buy_ready=True sector_rank=9 price=317.86 support=273.1 resistance=334.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=6157073.5 spike=0.84
- ZEOT.CA: score=28.08 buy_ready=True sector_rank=9 price=11.79 support=9.05 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=42.32 liquidity=111490400.0 spike=2.84
- ZMID.CA: score=27.4 buy_ready=True sector_rank=3 price=7.2 support=6.11 resistance=7.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=68.84 liquidity=198496512.0 spike=0.91

## Backtesting Lite
- ELEC.CA: 180d return=-25.35%, max drawdown=-35.96%, MA20>MA50 days last20=0, as_of=2026-07-11T21:00:00+00:00
- AREH.CA: 180d return=48.7%, max drawdown=-37.58%, MA20>MA50 days last20=20, as_of=2026-07-11T21:00:00+00:00
- GDWA.CA: 180d return=-30.17%, max drawdown=-39.84%, MA20>MA50 days last20=13, as_of=2026-07-11T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ELEC.CA: status=RECENT_ACCEPTED latest=2026-06-30 age_days=13 sources=3 expected=Electro Cable Egypt summary=Electro Cable Egypt (ELEC.CA) has reported recent financial results indicating a decline in profitability. In Q1 2026, the company incurred consolidated net losses of EGP 241.612 million, a significant drop from net profits in the same period of the previous year. Full-year 2025 results also showed lower profits and decreased revenue compared to 2024. The company's investor relations page provides access to financial statements.
  - Egypt: Electro Cable incurs consolidated losses in Q1 2026 (June 30, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_ECtN4ybwA0CPQIizlXD9fmqOy4bGLZGom_naXk25UDcQtzpDNwTIhg7k3iimXK10UJ1Xy0wLjQTy-KsepocEVRtj2A32YzKByNpoGRpb6SlMDgRuGqpQOV54zs75Nni_Imi1pfHXcU9X7gBGHzeiEr5JtQ-8hTTCs2tyhZ_TKFe_1IWCESq09a7BIa-Q1LurqfBP8TVRsNlvybD3L7adamqIucniwW0PB7OkKuY=
  - Electro Cable Egypt sees lower profits in 2025; revenues exceed EGP 10.8bn (March 19, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGx8rCmDZ0Hde3xmsFniYaxqFK4EkGJWEwlLiFZmfy9NeMW0t6m4l33XfseMYOmpulw8VWj1kTNF-p6RXLPskIO5CaWL5Dhej8evVgQk7osXxuZmGhxydzPR2DTay7Mss1N_hDs3C4srAkONaKF4k291uyicJM=
  - Electro Cable Egypt (EGX:ELEC) Financials & Income Statement (December 31, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaxBbBBDO8o4lVam0mNzz1xO-7I_74AiO2FcS-10xWxJH2EWXvUjDlSY84rEQxsUFCKJuMAwWJ5Wnuk6YPB34NI4QkUfaEigVO0w8TzoOvoMEIL2q0OWskYWXU5G4C7vSCpF0gmT4BGKTZ4Bk1dw==
- AREH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Real Estate Egyptian Consortium S.A.E summary=Real Estate Egyptian Consortium’s net profits approach EGP 2m in 9M-25; Shareholder ups stake in Real Estate Egyptian; Target for Real Estate Investment cuts stake in Real Estate Egyptian Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Real Estate Egyptian Consortium’s net profits approach EGP 2m in 9M-25: https://english.mubasher.info/news/4528467/Real-Estate-Egyptian-Consortium-s-net-profits-approach-EGP-2m-in-9M-25/
  - Shareholder ups stake in Real Estate Egyptian: https://english.mubasher.info/news/4026301/Shareholder-ups-stake-in-Real-Estate-Egyptian/
  - Target for Real Estate Investment cuts stake in Real Estate Egyptian: https://english.mubasher.info/news/4010821/Target-for-Real-Estate-Investment-cuts-stake-in-Real-Estate-Egyptian/
- GDWA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Gadwa for Industrial Development summary=Evidence rejected for GDWA.CA: source text did not clearly match GDWA.CA / Gadwa for Industrial Development.
- RACC.CA: status=RECENT_ACCEPTED latest=2026-05-11 age_days=63 sources=3 expected=Raya Customer Experience summary=Raya Customer Experience (RACC.CA) has demonstrated strong financial performance in Q1 2026, with significant year-over-year increases in revenue, gross profit, EBITDA, and net profit. The company's annual revenue for 2025 also showed growth. Investor relations information and earning releases are available on their official website.
  - Raya Customer Experience Reports Q1 2026 Results (May 11, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmhG6sPAmF4YRy3QoV8gEyEvpw459V1lgELF3OGGI-F949oE91aeRWxbrK53CN0c5hCqoQzvv8lJ5bSAO3rPB32tMM7F6tlXXCLXJWACjFdrXd7tEz2bXib_0n28EPHvuL6O_CUn8vZzIEy-P6
  - Raya Customer Experience (EGX:RACC) Revenue (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIalWCWAb2YPNoXQMo2_ZFfXRrC7E5DlKyBN7K5cAwDbVJeNhD5i9JeDPlDoKqw3BFWHka2zOSNZ4IL-B4Fq_HezeFqK2C-XqK8V-Hqvirx3FONUPXOGa0DaaumOedzVCri7yJecPLzF3ljw==
  - Raya Customer Experience Reports Earnings Results for the Full Year Ended December 31, 2025 (March 5, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoNR6pmaq4QYDnFMUtVI8EBHTvW4b1seXdmROltC-zCmft2l3CfoLvOXCdF1LE-BkoU1clX-KzxFC83kGS1ob34j3I-J2OMs_dA10c2RIl5yBFvik55Dlv1qzqWFw3OdtHvHf-nPvI1npG37TsDOV5yU3yKWFfX7WZXwqkLVG7iwP_TJWcyyI=
- RAYA.CA: status=OLD_ACCEPTED latest=2005-01-01 age_days=7863 sources=2 expected=Raya Holding summary=Raya Holding (RAYA.CA) is an investment conglomerate listed on the EGX since 2005 and is the parent company of Raya Customer Experience (RACC.CA). While no specific recent financial reports for Raya Holding itself were found within the last 12 months, its subsidiary RACC.CA has reported strong recent performance.
  - Stock Overview - Raya Corp: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFVg0r5P1aTX_K5dbl0JT4MMAW0ubVg3Vox28etjW7_yfXDSa73hyba6lCC9Gv80ydYA5fak3SnnW6d_Yyj4KhtQE4DLvz4hSaSFc_HXgLG18xg5Vf12yXtKTgL6ye
  - Raya Contact Center Co Stock Price Today | EGX: RACC Live - Investing.com (Mentions Raya Holding as parent company): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3FOIn4n-mEnetlhTsOFo8brVNBQG32BDQIbTxnGHeogU8AcRqfRRigvFG9sFdvxHgIJhoU2ijNhu8iv3ns8f2OJPoMJqy-MYrTnvdIcwNtx6YZDCbBXVP2sLqLBb5Z0hVgmpUtaLJCalVqSkdfYeZ
- MCRO.CA: status=RECENT_ACCEPTED latest=2026-05-17 age_days=57 sources=3 expected=Macro Group Pharmaceuticals (Macro Capital) S.A.E summary=Macro Group Pharmaceuticals (Macro Capital) S.A.E (MCRO.CA) reported strong operational and financial performance in Q1 2026, with significant increases in revenue, gross profit, EBITDA, and net profit. The company also turned to profitability in 2025 and approved an Employee Stock Ownership Plan in April 2026. Financial statements are available on their investor relations page.
  - Macro Group Pharmaceuticals Delivers Strong Growth Momentum, Reinforcing Market Leadership in 2026 (May 17, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtPGCZDcHKhN2L2I8mGekRiKxAuul6ijEOQwRr8Y0CFNxn1vZ6TS-SLOkUK0_N4x59kJwogyGFS1hRNcjzWFQidSZK6tg9C40vJK_F1uOUtheXtZbqjM2aSLMsbTA8rfKgYpC-Q3ghS8D7roglWZ2oiw==
  - Macro Capital Q1 consolidated profit surges 48.8% YoY (May 17, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKhstgeLxuzRPfqdMOjyiR0mH-WiuzscroNjqflNsqdd17sPMiOTGrIgyHBn5lu0bQzyrnWh8kG_12HRJjHlZuIQpyP682zbhHS6_iGO0scT5w7UeS5QGomycBGjOuBY5GTx-8XKLsY48jHs8PofztQA==
  - Macro Capital shifts to profits in 2025 (February 19, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKhstgeLxuzRPfqdMOjyiR0mH-WiuzscroNjqflNsqdd17sPMiOTGrIgyHBn5lu0bQzyrnWh8kG_12HRJjHlZuIQpyP682zbhHS6_iGO0scT5w7UeS5QGomycBGjOuBY5GTx-8XKLsY48jHs8PofztQA==
- COSG.CA: status=RECENT_ACCEPTED latest=2026-05-12 age_days=62 sources=3 expected=Cairo Oil & Soap Company summary=Cairo Oil & Soap Company (COSG.CA) reported a net profit of EGP 6.7 million in Q1 2026, a positive shift from a net loss in the previous quarter. The company's revenue also increased in the latest quarter. Full-year 2025 earnings were also reported.
  - Cairo Oil & Soap Company Reports Earnings Results for the First Quarter Ended March 31, 2026 (May 12, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMEt7Dm_5ZJMYsxWUc7B8iqzKQS_ivvpo-yMfZx3doULKz__lf_1gshmKo3N_KeiGpnLJbY80PT8JcTIezt-upeWXLPXFxL0VW6koWoMaT-wo8PiBP-xygwJrfUd73yPo4-VttIuuIJd2UU4hXZPDAQWEGJRl76znKP6NBNQbWooZfJrOU
  - Cairo Oils & Soap - EGX:COSG Financials (Latest Quarter): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2wKxp1TXhZWG3KSKeKl2g4PwLqGvvxLUFUMpOwmUiTXXDOg3TE0db9rYaDwAL-_KxBr-8lLnCOFDrEnFEjPxS5D8-ZbOZ6oi7S8_QAu8We-7JlXMNNwGutGBg85E7O-qvhbAXkzdlvv6uH3nPujKouLzvekeAaNCLHJbGyQ==
  - Cairo Oil & Soap Company Reports Earnings Results for the Full Year Ended December 31, 2025 (March 31, 2026): https://vertexaisearch.google.com/grounding-api-redirect/AUZIYQFMEt7Dm_5ZJMYsxWUc7B8iqzKQS_ivvpo-yMfZx3doULKz__lf_1gshmKo3N_KeiGpnLJbY80PT8JcTIezt-upeWXLPXFxL0VW6koWoMaT-wo8PiBP-xygwJrfUd73yPo4-VttIuuIJd2UU4hXZPDAQWEGJRl76znKP6NBNQbWooZfJrOU
- MOED.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=The Egyptian Modern Education Systems, S.A.E. summary=Egyptian Modern Education swings to over EGP 1.5m net profits in Q1-25/26; Egyptian Modern Education shifts to over EGP 1.5m net profits in Q1-25/26; Egyptian Modern Education&#39;s net profits near EGP 5m in FY24/25 Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Egyptian Modern Education swings to over EGP 1.5m net profits in Q1-25/26: https://english.mubasher.info/news/4542751/Egyptian-Modern-Education-swings-to-over-EGP-1-5m-net-profits-in-Q1-25-26/
  - Egyptian Modern Education shifts to over EGP 1.5m net profits in Q1-25/26: https://english.mubasher.info/news/4540647/Egyptian-Modern-Education-shifts-to-over-EGP-1-5m-net-profits-in-Q1-25-26/
  - Egyptian Modern Education&#39;s net profits near EGP 5m in FY24/25: https://english.mubasher.info/news/4534544/Egyptian-Modern-Education-s-net-profits-near-EGP-5m-in-FY24-25/

## Warnings
- Evidence for AREH.CA matches the company but no source/report date was detected.
- Evidence rejected for GDWA.CA: source text did not clearly match GDWA.CA / Gadwa for Industrial Development.
- Evidence for RAYA.CA matches the company but appears old; latest detected date is 2005-01-01.
- Evidence for MOED.CA matches the company but no source/report date was detected.
