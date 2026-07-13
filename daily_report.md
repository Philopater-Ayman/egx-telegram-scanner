# Telegram-First EGX Scanner Report

Scan phase: Evening tomorrow plan
Generated UTC: 2026-07-13T18:21:04.763332+00:00
Generated Cairo: 2026-07-13 21:21
Run timing: target 19:30 Cairo | generated Cairo 2026-07-13 21:21 | cron 30 16 * * 0-4
Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-07-13 21:15

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 85
- Data quality issues: 1
- Tradeable price/liquidity tickers: 178/189
- Top sector: Technology & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, July 13
- Freshness: DELAYED
- EGX30 regime: CONSTRUCTIVE / above MA20 55.0% / above MA50 50.0%
- EGX70 regime: BULLISH / above MA20 77.5% / above MA50 70.0%
- Sector breadth: 52.38%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- CCAP.CA: liquidity=910191104.0 spike=1.4 score=27.2
- ZMID.CA: liquidity=342790528.0 spike=1.57 score=27.54
- COMI.CA: liquidity=331090944.0 spike=0.76 score=25.75
- TMGH.CA: liquidity=248257136.0 spike=0.7 score=26.4
- ARAB.CA: liquidity=246783680.0 spike=2.73 score=29.86

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner highlighted GDWA.CA as the top BUY candidate, followed by ALCN.CA and COSG.CA. All three show price above MA20/MA50, solid liquidity spikes, and bullish outlook scores above 90. EGX70 is in a bullish regime while EGX30 remains constructive, pushing the system into SELECTIVE_SWING_TRADES_ONLY risk mode. This favors swing‑type entries on stocks with clear support‑resistance structures, but sector breadth is modest (≈52%) and the leading sectors are Technology, Industrial Goods & Cables, and Transportation, adding uncertainty to non‑leading sectors.
- GDWA.CA: price 0.84, support 0.76, resistance 0.82, RSI 51.8 – near resistance, sector not leading.
- ALCN.CA: strong momentum (RSI 66), support 27.7, resistance 33.2 – extended upside, transport sector in top‑3.
- COSG.CA: price at resistance 1.66, support 1.47, RSI 54.5 – bullish watch, sector not leading.
- EGX70 bullish, EGX30 constructive → selective swing trades only; watch for regime shift.
- Uncertainty: sector breadth modest, low confidence scores, and macro outlook may change in 1‑3 days.

## Top Liquidity Spikes
- CPCI.CA: spike=20.1 liquidity=52834264.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RACC.CA: spike=12.16 liquidity=127170648.0 outlook=BULLISH_WATCH score=84.3 buy_ready=True
- MOSC.CA: spike=10.03 liquidity=91840776.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- OCPH.CA: spike=9.25 liquidity=57890988.0 outlook=BULLISH_WATCH score=82.3 buy_ready=True
- GDWA.CA: spike=7.87 liquidity=127888456.0 outlook=BULLISH_WATCH score=93.3 buy_ready=True

## Sector Leaderboard
- #1 Technology & Distribution: score=13.71 5d=4.42% 20d=18.68% aboveMA50=100.0%
- #2 Industrial Goods & Cables: score=13.29 5d=2.41% 20d=4.51% aboveMA50=100.0%
- #3 Transportation & Logistics: score=11.08 5d=3.01% 20d=7.21% aboveMA50=100.0%
- #4 Real Estate: score=10.95 5d=3.68% 20d=14.76% aboveMA50=100.0%
- #5 Telecommunications: score=10.77 5d=5.07% 20d=6.67% aboveMA50=100.0%
- #6 Automotive & Distribution: score=10.69 5d=-0.72% 20d=9.65% aboveMA50=100.0%
- #7 Fintech & Payments: score=8.96 5d=4.38% 20d=9.24% aboveMA50=50.0%
- #8 General / Verified EGX Expansion: score=8.3 5d=2.64% 20d=5.32% aboveMA50=73.79%

## Today's Prioritized Action Tickets
- Priority #1: BUY GDWA.CA
  - Entry: 0.84 | Take profit: 0.9 | Stop loss: 0.81
  - Confidence: LOW | score=32.4 | outlook=BULLISH_WATCH 93.3
  - Reason: BUY SETUP: GDWA.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 51.8, support 0.76, resistance 0.82, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY ALCN.CA
  - Entry: 29.95 | Take profit: 33.03 | Stop loss: 28.75
  - Confidence: LOW | score=31.1 | outlook=BULLISH_WATCH 100
  - Reason: WATCH/BUY SETUP: ALCN.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 66.15, support 27.7, resistance 33.2, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY COSG.CA
  - Entry: 1.66 | Take profit: 1.8 | Stop loss: 1.59
  - Confidence: LOW | score=30.9 | outlook=BULLISH_WATCH 92.3
  - Reason: BUY SETUP: COSG.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 54.55, support 1.47, resistance 1.66, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ELEC.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=close to resistance
- ALCN.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- MTIE.CA: BULLISH_WATCH score=97 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- GDWA.CA: BULLISH_WATCH score=93.3 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- AREH.CA: BULLISH_WATCH score=92.3 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- COSG.CA: BULLISH_WATCH score=92.3 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CAED.CA: BULLISH_WATCH score=92.3 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- ACGC.CA: BULLISH_WATCH score=92.05 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ZMID.CA: BULLISH_WATCH score=91 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- SWDY.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling

## BUY-Ready Candidates
- ELEC.CA: rank=34.4 outlook=BULLISH_WATCH outlook_score=100 sector_rank=2 price=2.16 support=2.04 resistance=2.18 liquidity=129780192.0
- AREH.CA: rank=32.46 outlook=BULLISH_WATCH outlook_score=92.3 sector_rank=8 price=1.72 support=1.51 resistance=1.76 liquidity=107658224.0
- GDWA.CA: rank=32.4 outlook=BULLISH_WATCH outlook_score=93.3 sector_rank=8 price=0.84 support=0.76 resistance=0.82 liquidity=127888456.0
- EPCO.CA: rank=31.4 outlook=BULLISH_WATCH outlook_score=78.3 sector_rank=8 price=9.64 support=8.5 resistance=9.8 liquidity=39881408.0
- RACC.CA: rank=31.4 outlook=BULLISH_WATCH outlook_score=84.3 sector_rank=8 price=10.48 support=9.36 resistance=10.57 liquidity=127170648.0
- ALCN.CA: rank=31.1 outlook=BULLISH_WATCH outlook_score=100 sector_rank=3 price=29.95 support=27.7 resistance=33.2 liquidity=47196152.0
- COSG.CA: rank=30.9 outlook=BULLISH_WATCH outlook_score=92.3 sector_rank=8 price=1.66 support=1.47 resistance=1.66 liquidity=90478136.0
- ADPC.CA: rank=30.66 outlook=CONSTRUCTIVE outlook_score=68.3 sector_rank=8 price=3.75 support=3.32 resistance=3.94 liquidity=49888068.0
- MCRO.CA: rank=30.4 outlook=BULLISH_WATCH outlook_score=79.3 sector_rank=8 price=1.35 support=1.17 resistance=1.33 liquidity=183460880.0
- RAYA.CA: rank=30.34 outlook=BULLISH_WATCH outlook_score=77 sector_rank=1 price=8.29 support=6.8 resistance=8.29 liquidity=168170464.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=26.4 buy_ready=False sector_rank=8 price=232.11 support=196.0 resistance=247.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=70.14 liquidity=14101022.0 spike=0.95
- ABUK.CA: score=20.12 buy_ready=False sector_rank=19 price=69.05 support=66.66 resistance=77.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.84 liquidity=112001016.0 spike=0.79
- ACAMD.CA: score=26.4 buy_ready=True sector_rank=8 price=2.35 support=2.14 resistance=2.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.0 liquidity=47800900.0 spike=0.5
- ACGC.CA: score=29.44 buy_ready=True sector_rank=9 price=10.01 support=8.92 resistance=9.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=54.07 liquidity=33348348.0 spike=1.52
- ADCI.CA: score=24.94 buy_ready=True sector_rank=8 price=236.44 support=223.0 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=51.65 liquidity=15179475.0 spike=1.27
- ADIB.CA: score=20.99 buy_ready=False sector_rank=17 price=46.55 support=44.1 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.79 liquidity=105729776.0 spike=1.12
- ADPC.CA: score=30.66 buy_ready=True sector_rank=8 price=3.75 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.0 liquidity=49888068.0 spike=3.13
- AFDI.CA: score=29.34 buy_ready=True sector_rank=8 price=46.81 support=40.8 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=59.42 liquidity=20047208.0 spike=1.47
- AFMC.CA: score=28.68 buy_ready=True sector_rank=8 price=74.15 support=66.0 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.13 liquidity=8983277.0 spike=2.65
- AJWA.CA: score=19.92 buy_ready=True sector_rank=8 price=183.97 support=150.51 resistance=190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.66 liquidity=5523553.0 spike=0.21
- ALCN.CA: score=31.1 buy_ready=True sector_rank=3 price=29.95 support=27.7 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=66.15 liquidity=47196152.0 spike=2.85
- ALUM.CA: score=15.97 buy_ready=False sector_rank=8 price=22.81 support=20.55 resistance=24.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.37 liquidity=2570795.5 spike=0.33
- AMER.CA: score=23.4 buy_ready=False sector_rank=4 price=3.15 support=2.28 resistance=3.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.8 liquidity=65159096.0 spike=0.8
- AMES.CA: score=14.4 buy_ready=False sector_rank=8 price=100.66 support=83.13 resistance=100.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=230643136.0 spike=5.63
- AMIA.CA: score=16.43 buy_ready=False sector_rank=8 price=8.9 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.46 liquidity=4032729.0 spike=0.42
- AMOC.CA: score=23.02 buy_ready=False sector_rank=15 price=8.04 support=7.42 resistance=8.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.63 liquidity=56101496.0 spike=1.08
- APSW.CA: score=17.59 buy_ready=False sector_rank=8 price=8.51 support=8.0 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.6 liquidity=2194979.75 spike=2.5
- ARAB.CA: score=29.86 buy_ready=False sector_rank=4 price=0.25 support=0.2 resistance=0.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=246783680.0 spike=2.73
- ARCC.CA: score=17.96 buy_ready=False sector_rank=18 price=55.17 support=53.0 resistance=57.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=46.04 liquidity=9356927.0 spike=0.45
- AREH.CA: score=32.46 buy_ready=True sector_rank=8 price=1.72 support=1.51 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 July 01:29 PM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=107658224.0 spike=3.03
- ARVA.CA: score=22.4 buy_ready=False sector_rank=8 price=10.78 support=10.5 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.12 liquidity=12018983.0 spike=0.57
- ASCM.CA: score=24.4 buy_ready=True sector_rank=8 price=62.1 support=56.29 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.49 liquidity=63347404.0 spike=0.77
- ASPI.CA: score=19.4 buy_ready=False sector_rank=8 price=0.31 support=0.3 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.06 liquidity=21950474.0 spike=0.77
- ATLC.CA: score=17.06 buy_ready=True sector_rank=14 price=5.24 support=4.77 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.85 liquidity=2945649.75 spike=0.43
- ATQA.CA: score=21.12 buy_ready=False sector_rank=19 price=9.6 support=9.21 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.34 liquidity=16366150.0 spike=0.5
- AXPH.CA: score=29.67 buy_ready=True sector_rank=8 price=1205.55 support=1073.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=63.99 liquidity=9114504.0 spike=3.08
- BINV.CA: score=16.82 buy_ready=True sector_rank=10 price=48.79 support=45.01 resistance=51.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.5 liquidity=2419274.5 spike=0.38
- BIOC.CA: score=23.89 buy_ready=True sector_rank=8 price=73.43 support=66.75 resistance=76.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=52.12 liquidity=4627362.0 spike=1.43
- BTFH.CA: score=22.12 buy_ready=False sector_rank=14 price=3.05 support=2.91 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.9 liquidity=170250464.0 spike=0.88
- CAED.CA: score=27.01 buy_ready=True sector_rank=8 price=74.42 support=68.0 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.31 liquidity=8108676.5 spike=1.25
- CANA.CA: score=18.02 buy_ready=False sector_rank=17 price=36.13 support=34.7 resistance=38.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=41.44 liquidity=5271913.0 spike=0.51
- CCAP.CA: score=27.2 buy_ready=True sector_rank=10 price=5.35 support=4.65 resistance=5.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.41 liquidity=910191104.0 spike=1.4
- CCRS.CA: score=14.4 buy_ready=False sector_rank=8 price=2.53 support=2.42 resistance=2.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51452248.0 spike=4.58
- CEFM.CA: score=14.61 buy_ready=False sector_rank=8 price=104.46 support=95.75 resistance=110.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=55.4 liquidity=1214445.63 spike=0.56
- CERA.CA: score=26.4 buy_ready=True sector_rank=8 price=1.32 support=1.17 resistance=1.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=11369921.0 spike=0.53
- CFGH.CA: score=4.43 buy_ready=False sector_rank=8 price=0.11 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29879.51 spike=4.7
- CICH.CA: score=18.53 buy_ready=False sector_rank=14 price=12.0 support=11.36 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=34.72 liquidity=9452032.0 spike=2.48
- CIEB.CA: score=19.64 buy_ready=True sector_rank=17 price=24.31 support=23.3 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.42 liquidity=3889204.0 spike=0.56
- CIRA.CA: score=28.88 buy_ready=False sector_rank=12 price=31.37 support=26.0 resistance=31.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.57 liquidity=52113216.0 spike=2.24
- CLHO.CA: score=22.18 buy_ready=False sector_rank=16 price=16.07 support=14.85 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=55.59 liquidity=41643112.0 spike=1.17
- CNFN.CA: score=26.6 buy_ready=True sector_rank=14 price=4.9 support=4.4 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=54216052.0 spike=1.24
- COMI.CA: score=25.75 buy_ready=True sector_rank=17 price=136.75 support=126.21 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.96 liquidity=331090944.0 spike=0.76
- COPR.CA: score=23.2 buy_ready=False sector_rank=8 price=0.37 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=32.73 liquidity=71535144.0 spike=3.4
- COSG.CA: score=30.9 buy_ready=True sector_rank=8 price=1.66 support=1.47 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=90478136.0 spike=2.25
- CPCI.CA: score=14.4 buy_ready=False sector_rank=8 price=449.86 support=400.03 resistance=482.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=52834264.0 spike=20.1
- CSAG.CA: score=24.18 buy_ready=True sector_rank=3 price=32.35 support=30.85 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=64.2 liquidity=6780592.0 spike=0.4
- DAPH.CA: score=25.8 buy_ready=True sector_rank=8 price=83.87 support=77.12 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=59.99 liquidity=7402982.0 spike=0.83
- DEIN.CA: score=-0.6 buy_ready=False sector_rank=8 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=18.01 buy_ready=True sector_rank=13 price=27.04 support=24.21 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.17 liquidity=1612265.25 spike=0.31
- DSCW.CA: score=29.36 buy_ready=True sector_rank=8 price=1.84 support=1.71 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.91 liquidity=82324176.0 spike=2.98
- DTPP.CA: score=23.4 buy_ready=False sector_rank=8 price=207.73 support=114.0 resistance=234.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=89.03 liquidity=22140058.0 spike=0.59
- EALR.CA: score=27.06 buy_ready=True sector_rank=8 price=369.95 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.03 liquidity=15706855.0 spike=1.33
- EASB.CA: score=22.4 buy_ready=False sector_rank=8 price=7.17 support=5.06 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.74 liquidity=16991016.0 spike=0.98
- EAST.CA: score=13.4 buy_ready=False sector_rank=13 price=36.57 support=36.6 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=29.64 liquidity=43879168.0 spike=0.99
- EBSC.CA: score=23.91 buy_ready=True sector_rank=8 price=1.92 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.95 liquidity=7050336.0 spike=1.23
- ECAP.CA: score=15.24 buy_ready=False sector_rank=8 price=32.68 support=31.15 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.35 liquidity=2841642.25 spike=0.31
- EDFM.CA: score=26.45 buy_ready=True sector_rank=8 price=354.39 support=310.2 resistance=349.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=66.15 liquidity=5050800.5 spike=6.77
- EEII.CA: score=21.44 buy_ready=True sector_rank=8 price=2.78 support=2.35 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=67.03 liquidity=7043841.0 spike=0.33
- EFIC.CA: score=12.49 buy_ready=False sector_rank=19 price=186.17 support=180.02 resistance=207.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.85 liquidity=6988626.0 spike=2.69
- EFID.CA: score=26.4 buy_ready=True sector_rank=13 price=28.38 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.8 liquidity=16319430.0 spike=0.34
- EFIH.CA: score=26.4 buy_ready=True sector_rank=7 price=22.34 support=20.0 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.96 liquidity=36375028.0 spike=0.82
- EGAL.CA: score=20.12 buy_ready=False sector_rank=19 price=291.4 support=272.28 resistance=314.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.96 liquidity=23548080.0 spike=0.48
- EGAS.CA: score=13.86 buy_ready=False sector_rank=15 price=52.83 support=50.01 resistance=53.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=54402784.0 spike=6.67
- EGBE.CA: score=7.85 buy_ready=False sector_rank=17 price=0.45 support=0.45 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=97807.36 spike=1.0
- EGCH.CA: score=23.4 buy_ready=False sector_rank=19 price=13.2 support=12.13 resistance=14.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=40.88 liquidity=73195400.0 spike=1.64
- EGSA.CA: score=13.47 buy_ready=False sector_rank=5 price=8.97 support=8.67 resistance=9.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=91.67 liquidity=9586.75 spike=1.03
- EGTS.CA: score=26.4 buy_ready=True sector_rank=4 price=18.11 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.79 liquidity=17222554.0 spike=0.27
- EHDR.CA: score=26.4 buy_ready=True sector_rank=8 price=2.69 support=2.37 resistance=2.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.76 liquidity=23749066.0 spike=0.57
- EKHO.CA: score=7.86 buy_ready=False sector_rank=15 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=34.4 buy_ready=True sector_rank=2 price=2.16 support=2.04 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=129780192.0 spike=6.85
- ELKA.CA: score=25.4 buy_ready=False sector_rank=8 price=1.64 support=1.19 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=72.22 liquidity=36926364.0 spike=0.73
- ELNA.CA: score=17.49 buy_ready=False sector_rank=8 price=39.47 support=35.55 resistance=40.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.25 liquidity=734476.63 spike=1.18
- ELSH.CA: score=28.4 buy_ready=True sector_rank=8 price=14.55 support=11.1 resistance=15.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.31 liquidity=92369056.0 spike=0.53
- ELWA.CA: score=17.14 buy_ready=True sector_rank=8 price=2.05 support=1.87 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.9 liquidity=2224132.0 spike=1.26
- EMFD.CA: score=22.4 buy_ready=False sector_rank=4 price=11.72 support=11.24 resistance=12.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.69 liquidity=77999288.0 spike=0.54
- ENGC.CA: score=28.36 buy_ready=False sector_rank=8 price=41.54 support=33.91 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=73.42 liquidity=46933304.0 spike=1.98
- EOSB.CA: score=14.44 buy_ready=False sector_rank=8 price=1.48 support=1.42 resistance=1.55 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=35839.68 spike=0.47
- EPCO.CA: score=31.4 buy_ready=True sector_rank=8 price=9.64 support=8.5 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=39881408.0 spike=5.92
- EPPK.CA: score=14.98 buy_ready=False sector_rank=8 price=14.17 support=11.72 resistance=15.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=69.3 liquidity=580490.81 spike=0.58
- ETEL.CA: score=28.4 buy_ready=True sector_rank=5 price=97.48 support=89.01 resistance=101.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=64.17 liquidity=61752488.0 spike=0.85
- ETRS.CA: score=24.4 buy_ready=True sector_rank=8 price=10.8 support=9.15 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.55 liquidity=17759826.0 spike=0.22
- EXPA.CA: score=27.49 buy_ready=True sector_rank=17 price=18.7 support=18.03 resistance=18.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=56.44 liquidity=9741383.0 spike=0.37
- FAIT.CA: score=16.95 buy_ready=True sector_rank=17 price=37.04 support=35.06 resistance=37.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=50.44 liquidity=1204939.63 spike=0.47
- FAITA.CA: score=8.77 buy_ready=False sector_rank=17 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=44.83 liquidity=26479.25 spike=0.85
- FERC.CA: score=13.56 buy_ready=False sector_rank=19 price=75.56 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.71 liquidity=2436679.75 spike=0.62
- FWRY.CA: score=23.4 buy_ready=False sector_rank=7 price=19.27 support=18.13 resistance=19.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.28 liquidity=59204904.0 spike=0.32
- GBCO.CA: score=24.72 buy_ready=True sector_rank=6 price=31.86 support=27.77 resistance=32.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=64.63 liquidity=98352368.0 spike=1.16
- GDWA.CA: score=32.4 buy_ready=True sector_rank=8 price=0.84 support=0.76 resistance=0.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.8 liquidity=127888456.0 spike=7.87
- GGCC.CA: score=23.4 buy_ready=False sector_rank=8 price=0.59 support=0.41 resistance=0.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=92.74 liquidity=15026198.0 spike=0.87
- GIHD.CA: score=27.36 buy_ready=True sector_rank=8 price=49.61 support=40.0 resistance=52.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=69.42 liquidity=53899940.0 spike=2.48
- GMCI.CA: score=15.41 buy_ready=True sector_rank=8 price=2.01 support=1.66 resistance=2.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=65.28 liquidity=1006822.13 spike=0.92
- GRCA.CA: score=14.4 buy_ready=False sector_rank=8 price=51.49 support=48.74 resistance=54.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13502287.0 spike=4.4
- GSSC.CA: score=21.49 buy_ready=True sector_rank=8 price=261.44 support=240.0 resistance=263.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.51 liquidity=4887512.5 spike=1.1
- GTWL.CA: score=21.6 buy_ready=False sector_rank=8 price=112.2 support=46.0 resistance=117.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=89.45 liquidity=104335176.0 spike=1.1
- HDBK.CA: score=12.75 buy_ready=False sector_rank=17 price=78.03 support=75.3 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=10.6 liquidity=17938980.0 spike=0.45
- HELI.CA: score=23.4 buy_ready=False sector_rank=4 price=7.35 support=6.34 resistance=7.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=75.72 liquidity=116687768.0 spike=0.74
- HRHO.CA: score=18.12 buy_ready=False sector_rank=14 price=26.62 support=26.09 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.62 liquidity=99726008.0 spike=0.77
- ICID.CA: score=22.42 buy_ready=True sector_rank=8 price=8.26 support=6.55 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=59.95 liquidity=8024932.0 spike=0.74
- IDRE.CA: score=28.58 buy_ready=True sector_rank=8 price=46.0 support=41.1 resistance=47.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.98 liquidity=14256326.0 spike=1.09
- IFAP.CA: score=16.75 buy_ready=False sector_rank=11 price=19.51 support=18.47 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=57.21 liquidity=3353929.5 spike=0.7
- INFI.CA: score=27.12 buy_ready=False sector_rank=8 price=103.64 support=88.51 resistance=106.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.89 liquidity=13262709.0 spike=1.36
- IRON.CA: score=15.5 buy_ready=False sector_rank=19 price=32.04 support=30.51 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.19 liquidity=6375268.5 spike=0.81
- ISMA.CA: score=15.0 buy_ready=False sector_rank=8 price=27.33 support=26.54 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=16.02 liquidity=7602784.5 spike=0.26
- ISMQ.CA: score=23.12 buy_ready=False sector_rank=19 price=9.51 support=8.06 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.31 liquidity=81307568.0 spike=0.56
- ISPH.CA: score=13.84 buy_ready=False sector_rank=16 price=11.45 support=11.2 resistance=12.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.27 liquidity=48203716.0 spike=0.79
- JUFO.CA: score=21.97 buy_ready=False sector_rank=13 price=30.56 support=29.1 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.22 liquidity=9571113.0 spike=0.38
- KABO.CA: score=23.4 buy_ready=False sector_rank=9 price=7.51 support=6.04 resistance=7.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=88.76 liquidity=23743142.0 spike=0.82
- KWIN.CA: score=14.44 buy_ready=False sector_rank=8 price=68.86 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=33.96 liquidity=13617967.0 spike=1.02
- KZPC.CA: score=19.08 buy_ready=False sector_rank=8 price=8.64 support=8.26 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=29.44 liquidity=18828980.0 spike=2.84
- LCSW.CA: score=25.6 buy_ready=True sector_rank=18 price=31.5 support=26.41 resistance=32.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=67.42 liquidity=18093550.0 spike=0.31
- LUTS.CA: score=22.4 buy_ready=False sector_rank=8 price=0.74 support=0.69 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=42.08 liquidity=33157148.0 spike=0.67
- MAAL.CA: score=23.0 buy_ready=False sector_rank=8 price=8.46 support=5.72 resistance=8.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=98.01 liquidity=29525868.0 spike=1.8
- MASR.CA: score=28.98 buy_ready=True sector_rank=8 price=8.13 support=6.71 resistance=7.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.67 liquidity=109816720.0 spike=1.29
- MBSC.CA: score=20.6 buy_ready=False sector_rank=18 price=240.04 support=222.66 resistance=256.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.92 liquidity=13697517.0 spike=0.59
- MCQE.CA: score=23.12 buy_ready=False sector_rank=18 price=177.0 support=166.66 resistance=182.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.1 liquidity=18816168.0 spike=1.26
- MCRO.CA: score=30.4 buy_ready=True sector_rank=8 price=1.35 support=1.17 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.52 liquidity=183460880.0 spike=5.4
- MENA.CA: score=21.28 buy_ready=True sector_rank=4 price=7.01 support=6.41 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.06 liquidity=4878350.0 spike=0.61
- MEPA.CA: score=25.7 buy_ready=False sector_rank=8 price=1.66 support=1.52 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=44.74 liquidity=23354608.0 spike=2.15
- MFPC.CA: score=22.12 buy_ready=False sector_rank=19 price=37.1 support=34.22 resistance=40.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.84 liquidity=54281392.0 spike=0.54
- MFSC.CA: score=14.39 buy_ready=False sector_rank=8 price=45.71 support=44.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=51.37 liquidity=4985197.5 spike=0.65
- MHOT.CA: score=4.86 buy_ready=False sector_rank=21 price=16.44 support=16.12 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=15.69 liquidity=5458066.0 spike=0.35
- MICH.CA: score=22.48 buy_ready=True sector_rank=8 price=38.0 support=34.0 resistance=39.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.69 liquidity=8084610.0 spike=0.5
- MILS.CA: score=24.92 buy_ready=True sector_rank=8 price=137.71 support=126.31 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=48.18 liquidity=14081340.0 spike=1.26
- MIPH.CA: score=19.73 buy_ready=True sector_rank=16 price=707.19 support=630.13 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=51.34 liquidity=3009290.25 spike=1.44
- MOED.CA: score=29.4 buy_ready=True sector_rank=8 price=0.73 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.62 liquidity=50895712.0 spike=4.76
- MOIL.CA: score=5.07 buy_ready=False sector_rank=15 price=0.55 support=0.52 resistance=0.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1206726.38 spike=4.12
- MOIN.CA: score=12.82 buy_ready=False sector_rank=8 price=23.95 support=22.6 resistance=25.25 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=48.18 liquidity=418933.41 spike=0.55
- MOSC.CA: score=14.4 buy_ready=False sector_rank=8 price=296.11 support=275.0 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=91840776.0 spike=10.03
- MPCI.CA: score=24.4 buy_ready=True sector_rank=8 price=240.47 support=215.0 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.77 liquidity=75240928.0 spike=0.77
- MPCO.CA: score=24.4 buy_ready=True sector_rank=11 price=1.88 support=1.7 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=71151168.0 spike=0.85
- MPRC.CA: score=23.4 buy_ready=False sector_rank=8 price=42.16 support=31.72 resistance=43.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=89.47 liquidity=41312804.0 spike=0.87
- MTIE.CA: score=30.2 buy_ready=True sector_rank=6 price=9.74 support=8.75 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.23 liquidity=59465200.0 spike=2.9
- NAHO.CA: score=12.61 buy_ready=False sector_rank=8 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=55.56 liquidity=48426.17 spike=2.08
- NCCW.CA: score=27.08 buy_ready=True sector_rank=8 price=6.64 support=5.82 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.79 liquidity=58119052.0 spike=2.34
- NEDA.CA: score=16.76 buy_ready=False sector_rank=8 price=2.8 support=2.7 resistance=2.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=361265.84 spike=0.99
- NHPS.CA: score=28.4 buy_ready=False sector_rank=8 price=83.02 support=61.55 resistance=83.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.67 liquidity=163333920.0 spike=5.14
- NINH.CA: score=26.4 buy_ready=False sector_rank=8 price=17.99 support=16.82 resistance=18.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.8 liquidity=37232956.0 spike=5.08
- NIPH.CA: score=25.84 buy_ready=True sector_rank=16 price=176.36 support=157.01 resistance=185.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.61 liquidity=83625952.0 spike=0.96
- OBRI.CA: score=26.4 buy_ready=True sector_rank=8 price=36.34 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.18 liquidity=19868374.0 spike=0.59
- OCDI.CA: score=21.4 buy_ready=False sector_rank=4 price=27.01 support=20.24 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=78.6 liquidity=52471212.0 spike=0.53
- OCPH.CA: score=29.4 buy_ready=True sector_rank=8 price=366.34 support=337.0 resistance=374.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=65.84 liquidity=57890988.0 spike=9.25
- ODIN.CA: score=11.04 buy_ready=False sector_rank=8 price=2.48 support=2.36 resistance=2.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25829254.0 spike=1.82
- OFH.CA: score=26.4 buy_ready=True sector_rank=8 price=0.63 support=0.57 resistance=0.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.46 liquidity=16244299.0 spike=0.77
- OIH.CA: score=21.4 buy_ready=False sector_rank=10 price=1.41 support=1.35 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=41345112.0 spike=0.6
- OLFI.CA: score=27.42 buy_ready=True sector_rank=13 price=23.0 support=21.0 resistance=23.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.56 liquidity=49759204.0 spike=1.51
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=682.55 support=681.14 resistance=691.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=100233048.0 spike=1.0
- ORHD.CA: score=24.4 buy_ready=True sector_rank=4 price=39.19 support=36.92 resistance=39.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.12 liquidity=107874992.0 spike=0.66
- ORWE.CA: score=19.4 buy_ready=False sector_rank=9 price=22.62 support=21.95 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.21 liquidity=17230034.0 spike=0.89
- PHAR.CA: score=18.84 buy_ready=False sector_rank=16 price=85.54 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=39.19 liquidity=17631736.0 spike=0.81
- PHDC.CA: score=17.4 buy_ready=False sector_rank=4 price=14.74 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=222625632.0 spike=0.69
- PHTV.CA: score=16.31 buy_ready=False sector_rank=8 price=298.84 support=204.03 resistance=304.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=89.79 liquidity=2911046.0 spike=0.21
- POUL.CA: score=24.6 buy_ready=True sector_rank=13 price=39.57 support=34.99 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=69.01 liquidity=47237300.0 spike=1.1
- PRCL.CA: score=20.6 buy_ready=False sector_rank=18 price=34.55 support=24.14 resistance=36.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.45 liquidity=11170020.0 spike=0.23
- PRDC.CA: score=26.4 buy_ready=True sector_rank=4 price=8.2 support=6.2 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=59.52 liquidity=54539664.0 spike=0.38
- PRMH.CA: score=24.4 buy_ready=True sector_rank=8 price=2.74 support=2.34 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.24 liquidity=22743272.0 spike=0.73
- RACC.CA: score=31.4 buy_ready=True sector_rank=8 price=10.48 support=9.36 resistance=10.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.48 liquidity=127170648.0 spike=12.16
- RAKT.CA: score=13.25 buy_ready=False sector_rank=8 price=22.51 support=21.25 resistance=23.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=57.11 liquidity=629096.06 spike=2.11
- RAYA.CA: score=30.34 buy_ready=True sector_rank=1 price=8.29 support=6.8 resistance=8.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.79 liquidity=168170464.0 spike=1.47
- RMDA.CA: score=18.84 buy_ready=False sector_rank=16 price=4.97 support=4.81 resistance=5.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=20118886.0 spike=0.92
- ROTO.CA: score=26.4 buy_ready=True sector_rank=8 price=43.07 support=33.7 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=54.28 liquidity=17313924.0 spike=0.53
- RREI.CA: score=28.54 buy_ready=True sector_rank=8 price=3.81 support=3.34 resistance=3.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=60.87 liquidity=20973786.0 spike=1.07
- RTVC.CA: score=16.25 buy_ready=False sector_rank=8 price=3.86 support=3.55 resistance=3.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=2852747.75 spike=0.66
- RUBX.CA: score=21.4 buy_ready=False sector_rank=8 price=13.21 support=9.8 resistance=14.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=80.15 liquidity=47242696.0 spike=0.86
- SAUD.CA: score=14.84 buy_ready=False sector_rank=17 price=21.54 support=19.99 resistance=22.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.15 liquidity=2088836.0 spike=0.31
- SCEM.CA: score=21.02 buy_ready=False sector_rank=18 price=61.92 support=60.14 resistance=67.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=52.02 liquidity=20318116.0 spike=1.21
- SCFM.CA: score=21.59 buy_ready=False sector_rank=8 price=256.69 support=226.5 resistance=269.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.22 liquidity=5967157.0 spike=1.11
- SCTS.CA: score=18.4 buy_ready=True sector_rank=12 price=616.15 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.37 liquidity=1999763.25 spike=0.37
- SDTI.CA: score=17.66 buy_ready=True sector_rank=8 price=47.05 support=45.55 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.44 liquidity=3261766.25 spike=0.41
- SEIG.CA: score=23.68 buy_ready=False sector_rank=8 price=259.07 support=180.6 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=85.04 liquidity=22023340.0 spike=1.14
- SIPC.CA: score=19.35 buy_ready=True sector_rank=8 price=3.52 support=3.25 resistance=3.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.75 liquidity=5954790.5 spike=0.72
- SKPC.CA: score=21.12 buy_ready=False sector_rank=19 price=16.37 support=15.58 resistance=16.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.21 liquidity=21826382.0 spike=0.69
- SMFR.CA: score=27.3 buy_ready=True sector_rank=8 price=206.33 support=187.01 resistance=209.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.46 liquidity=6180407.0 spike=3.36
- SNFC.CA: score=15.35 buy_ready=False sector_rank=8 price=11.8 support=11.26 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.55 liquidity=5948770.5 spike=0.52
- SPIN.CA: score=17.54 buy_ready=False sector_rank=9 price=14.63 support=13.3 resistance=14.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=6136914.5 spike=0.67
- SPMD.CA: score=23.96 buy_ready=True sector_rank=8 price=0.45 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=7558135.5 spike=0.43
- SUGR.CA: score=13.1 buy_ready=False sector_rank=13 price=47.26 support=45.31 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=8284334.5 spike=1.71
- SVCE.CA: score=26.4 buy_ready=True sector_rank=8 price=9.36 support=8.35 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.6 liquidity=24692126.0 spike=0.35
- SWDY.CA: score=23.31 buy_ready=True sector_rank=2 price=88.47 support=84.3 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=56.06 liquidity=4909208.5 spike=0.38
- TALM.CA: score=15.0 buy_ready=False sector_rank=12 price=15.71 support=15.27 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=30.07 liquidity=14967729.0 spike=1.3
- TMGH.CA: score=26.4 buy_ready=True sector_rank=4 price=97.93 support=92.1 resistance=99.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.25 liquidity=248257136.0 spike=0.7
- TRTO.CA: score=13.36 buy_ready=False sector_rank=8 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=751.23 spike=2.48
- UEFM.CA: score=17.12 buy_ready=False sector_rank=8 price=500.78 support=460.0 resistance=529.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=60.58 liquidity=722057.38 spike=0.46
- UEGC.CA: score=24.22 buy_ready=False sector_rank=8 price=1.9 support=1.33 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=80.3 liquidity=32123606.0 spike=1.41
- UNIP.CA: score=28.13 buy_ready=True sector_rank=8 price=0.34 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=9726915.0 spike=0.55
- UNIT.CA: score=21.4 buy_ready=False sector_rank=4 price=19.06 support=12.0 resistance=20.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.24 liquidity=11561665.0 spike=0.54
- WCDF.CA: score=11.8 buy_ready=False sector_rank=8 price=523.93 support=450.0 resistance=544.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=39.17 liquidity=399774.84 spike=1.0
- WKOL.CA: score=24.32 buy_ready=True sector_rank=8 price=315.0 support=273.1 resistance=334.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=7795098.5 spike=1.06
- ZEOT.CA: score=28.76 buy_ready=True sector_rank=8 price=11.72 support=9.05 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.32 liquidity=124801560.0 spike=3.18
- ZMID.CA: score=27.54 buy_ready=True sector_rank=4 price=7.27 support=6.11 resistance=7.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.84 liquidity=342790528.0 spike=1.57

## Backtesting Lite
- ELEC.CA: 180d return=-25.35%, max drawdown=-35.96%, MA20>MA50 days last20=0, as_of=2026-07-11T21:00:00+00:00
- AREH.CA: 180d return=48.7%, max drawdown=-37.58%, MA20>MA50 days last20=20, as_of=2026-07-11T21:00:00+00:00
- GDWA.CA: 180d return=-30.17%, max drawdown=-39.84%, MA20>MA50 days last20=13, as_of=2026-07-11T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ELEC.CA: status=RECENT_ACCEPTED latest=2026-07-06 age_days=7 sources=3 expected=Electro Cable Egypt summary=Electro Cable Egypt (ELEC.CA) has seen recent activity including a reduction in stake by Alhsn for Consulting and Q1 2026 consolidated net losses. The company also had several disclosures and board decisions in the first half of 2026.
  - Alhsn for Consulting cuts stake in Electro Cable Egypt to 19.8% (July 06, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgeuSOoyKjxDf_NegMi5M1b7gIp_i16FV49hKv01ayenduWGF7L9c_hJfdqiUu7BFSK6OAe1maA2dPDI04aP3B2aXPob4CWbBwDjXrdlv7AWVc5Z5S5mi8C2GycDx1J8pNUqpGM5wWcdWIAOC5URvjskIRr-CVNhvRrHXAG70u_cKX6ASo6OKLAzApuUU31kEiYXcgFbMLRIvZLvarovxuaGM4jc9-JyxBQlOfRNA=
  - Electro Cable Egypt (ELEC.CA) - Release Regarding a Disclosure Form (July 05, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHObIr4hGNUmzFAP0S2yfZEo9Z54ZHzKZwUWMLwS76CC_fIIbMW4ubCUdp7XxvJKZBgmbXUyO_49xMj_M_auEh4-Db2hhdvzznSV9LzjWJLBXtn7hvh06Wt8F-ZjQE5H_7tq6D1_rvOtbQY8FZpWizh_bEme9pKg_t_3vQUXTuyEQYusogdvygeor6vLUiwk0jvNJQHwsYWJ_c9khx1BdeenoTDVCXJcQcLig==
  - Electro Cable Egypt (ELEC.CA) - Board of Directors' Decisions (June 30, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjlesdy_O6cXvI-cwU-kT2-p886F_-Qia8grWPgiYxI0jRgIs4zQW1jBASKBxZ4-eoPvLM8-_aYz5c32ip12r4PVfJHw-HwhDNIWu5FOjYJKAK0oEfw_HJymGJaQIpDJPCoGfAnqBbeP8bSe6FHjycUOtndp_T_K7jsolM-MU=
- AREH.CA: status=OLD_ACCEPTED latest=2024-05-16 age_days=788 sources=1 expected=Real Estate Egyptian Consortium S.A.E summary=Recent information for Real Estate Egyptian Consortium S.A.E (AREH.CA) is limited within the last 12 months. The most recent relevant disclosure found is from May 2024.
  - Egyptian Real Estate Group (AREH.CA) - Release Regarding a Disclosure Form (May 16, 2024): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6oFruP_zfsqqK1MZa7WCyDeFFSovNm8GwHvQrH0qqVhHmHNrYsTv9ypZfLdTmrhOiSwjpPDanfQpmW1GgpvN-233G9zjARhTiX_JU2fY2kfLgfBzUOGZzqF0hUSC2iQ8044VOaHKSgVi-0OQiIle6CY_uR0PwTw==
- GDWA.CA: status=RECENT_ACCEPTED latest=2026-06-30 age_days=13 sources=3 expected=Gadwa for Industrial Development summary=Gadwa for Industrial Development (GDWA.CA) reported its Q1 2026 consolidated financial results in June 2026, showing revenues of approximately EGP 3.26 billion and a net loss. The company also had several board and general assembly meetings with related disclosures.
  - GADWA for Industrial Development Announces its Consolidated Results for the period ended on the 31st of March, 2026 (June 30, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFopAsu0_76puKD4jNlB76ErIgEhG_E3SK7myrNBOhEfjaBzSrGEdljA7vNX8hCFOfSaGHn7QD5OmTntA8LP6Ol_Skg-DGwWeqcyJ914KWh9sosAApZwTYE50BxC68WCokuleiC-z5tVpmzC50K
  - Gadwa For Industrial Development (GDWA.CA) Reports its Financial Results (Consolidated) for the Period from 01/01/2026 to 31/03/2026 (June 30, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFj77yXsQ5jh5eAkeY4T8PE1wUZcZ6YArgOg_FZraz5Hq0qUFP_OsmEb7dxKu46MNL0bbT62mL_dlE-_7JSN419FtgvfAy9Ha6_UN6A4ONaglxhhiWeKCxDvrtitoIz-Okpo-f3jczZQtTR6DdBp6jWKbw=
  - Gadwa For Industrial Development (GDWA.CA) - Decisions of the Board of Directors' Meeting (June 30, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqtuXWBREyAty8WBszjNiRNyoBreZzHgWbZWOd_9DB8bvypuKrj2kieCeUD8fgDE1tOGzigflzB3PL-hx9EXP-Fvsh83EFAlU91fBh3Se_Duk_Az1bGrDzl6OjYjgP6G4igegc_iA3VME9VafH0hbQ
- EPCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egypt for Poultry summary=Evidence rejected for EPCO.CA: source text did not clearly match EPCO.CA / Egypt for Poultry.
- RACC.CA: status=RECENT_ACCEPTED latest=2026-05-11 age_days=63 sources=3 expected=Raya Customer Experience summary=Raya Customer Experience (RACC.CA) reported strong Q1 2026 results with significant increases in revenues, gross profit, EBITDA, and net profit. The company also provided its 2025 financial performance and details on its business operations.
  - Raya Customer Experience Reports Q1 2026 Results (May 11, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKiIxtn4AuE__dwNYmQAYc-kc21xzp8CB01qru0cKlPVb_rMXHw9xwxjtwFaXExsruv89IjX4s0BKJQEJMvsTN_O_C5sPrGUlRq2UhESJgozFMgsEVNAFI3lJwMuzDpqNf0LdOrQwjPDNhAzI3
  - Raya Customer Experience (EGX:RACC) Stock Price & Overview (2025 Financial Performance): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSUN7kWfdkfjmAC37ekskeOlIEhU6qB5_Zm5FxBDW1S2-eUf-h8Fvq3uGH91Sr5hhQhA5fXepw1DYv-Tg6B8vv37RR9fg9yUKky7XWM2d_8P1TA8trfZKQu4pPQ00873qarKs=
  - Raya Contact Center Co Stock Price Today | EGX: RACC Live - Investing.com (Company Profile and Latest Quarter Earnings): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwK0duKfEIKZO2RSXTtYqgUJQld83IoRQ-KUmBqT-43CL7BTUbqG76kiuBsezllcZuIStK43lx2clEL17Sj3mZ05TOcQk7cH7EPYGefUhuftQvaHGH_ORqTsk9Vo7-9eNfQEOYgRERlY5YG4Jl34p2
- ALCN.CA: status=RECENT_ACCEPTED latest=2026-05-14 age_days=60 sources=3 expected=Alexandria Containers and Cargo Handling summary=Alexandria Containers and Cargo Handling (ALCN.CA) has been active with dividend announcements, earnings reports, and significant corporate actions including a proposed acquisition by Abu Dhabi Ports Company PJSC and share purchases by Holding Company for Maritime and Land Transport.
  - Alexandria Container&Cargo Handling Company announces Annual dividend, payable on May 14, 2026 (April 26, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFe3OOzvn_m4REOjmKYot-brMZeY5WoOI4i15KC8vc6EmfeIyGxS1WGNek1G6WTyEaNHtmCLVU3FEhkPmRqr7q6GfgOxCttY9_AF7KmO47lOr-VPBgl6Nst4qVkjbyasrM5IGXsiaxRIZHFT_neomp3B320petRt3iwpVz5xEDtzDmGPJcH18IhXl3Kw==
  - Alexandria Container and Cargo Handling Co interim dividend egp 0.99/share (April 27, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFe3OOzvn_m4REOjmKYot-brMZeY5WoOI4i15KC8vc6EmfeIyGxS1WGNek1G6WTyEaNHtmCLVU3FEhkPmRqr7q6GfgOxCttY9_AF7KmO47lOr-VPBgl6Nst4qVkjbyasrM5IGXsiaxRIZHFT_neomp3B320petRt3iwpVz5xEDtzDmGPJcH18IhXl3Kw==
  - Holding Company for Maritime and Land Transport buys 27.3 mln shares in ALCN for EGP 880.9 mln - EGX (April 09, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFe3OOzvn_m4REOjmKYot-brMZeY5WoOI4i15KC8vc6EmfeIyGxS1WGNek1G6WTyEaNHtmCLVU3FEhkPmRqr7q6GfgOxCttY9_AF7KmO47lOr-VPBgl6Nst4qVkjbyasrM5IGXsiaxRIZHFT_neomp3B320petRt3iwpVz5xEDtzDmGPJcH18IhXl3Kw==
- COSG.CA: status=RECENT_ACCEPTED latest=2026-07-07 age_days=6 sources=3 expected=Cairo Oil & Soap Company summary=Cairo Oil & Soap Company (COSG.CA) has released several disclosure forms and board meeting minutes in 2026. The company also reported its latest quarterly financials showing an increase in revenue and net income.
  - Cairo Oils & Soap (COSG.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 07, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFu1B-el7vIbbhBQBNzaVLJR-dEFp8Csab4Z2k-uId0AojdxlgAswAt9tJDsdptNMJ2UDNy98Ff7inBEEcHeRR6cHeFkVBTC3ZwH0Onz7aheMMi3XKg0ChNAZpV7v9p9sJ63-TcaPuEqjiWh2nbccnb
  - Cairo Oils & Soap (COSG.CA) - Minutes of the BoD Meeting (July 05, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFu1B-el7vIbbhBQBNzaVLJR-dEFp8Csab4Z2k-uId0AojdxlgAswAt9tJDsdptNMJ2UDNy98Ff7inBEEcHeRR6cHeFkVBTC3ZwH0Onz7aheMMi3XKg0ChNAZpV7v9p9sJ63-TcaPuEqjiWh2nbccnb
  - Cairo Oils & Soap (COSG.CA) - Decisions of the Board of Directors' Meeting (April 26, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFu1B-el7vIbbhBQBNzaVLJR-dEFp8Csab4Z2k-uId0AojdxlgAswAt9tJDsdptNMJ2UDNy98Ff7inBEEcHeRR6cHeFkVBTC3ZwH0Onz7aheMMi3XKg0ChNAZpV7v9p9sJ63-TcaPuEqjiWh2nbccnb
- ADPC.CA: status=RECENT_ACCEPTED latest=2026-07-01 age_days=12 sources=3 expected=The Arab Dairy Products Co. summary=The Arab Dairy Products Co. (ADPC.CA) has seen recent block trading transactions and reported deepening consolidated losses in Q1 2026. The company's investor relations page provides general information and its ownership structure, including Gadwa for Industrial Development as a major shareholder.
  - Panda records EGP 40.2M block trading transaction (July 01, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6Nm2N913dS2IINz4R56KECShaiEAdBVnKtTI6aisiNh3I6cjs0D3fYwfhDzKF1_k9FQuYfC4HDNspNrUFcSYjrYP6J8rXIe9l9OgjZrEDgMgJkczNnNc_-U9Xab6mHiZaK9QGSAjxhzD0A9KSgq5rYw==
  - Panda's consolidated losses deepen 260.2% YoY in Q1 2026 (June 23, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6Nm2N913dS2IINz4R56KECShaiEAdBVnKtTI6aisiNh3I6cjs0D3fYwfhDzKF1_k9FQuYfC4HDNspNrUFcSYjrYP6J8rXIe9l9OgjZrEDgMgJkczNnNc_-U9Xab6mHiZaK9QGSAjxhzD0A9KSgq5rYw==
  - Panda records EGP 25M block trading transaction (January 21, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6Nm2N913dS2IINz4R56KECShaiEAdBVnKtTI6aisiNh3I6cjs0D3fYwfhDzKF1_k9FQuYfC4HDNspNrUFcSYjrYP6J8rXIe9l9OgjZrEDgMgJkczNnNc_-U9Xab6mHiZaK9QGSAjxhzD0A9KSgq5rYw==

## Warnings
- Evidence for AREH.CA matches the company but appears old; latest detected date is 2024-05-16.
- Evidence rejected for EPCO.CA: source text did not clearly match EPCO.CA / Egypt for Poultry.
