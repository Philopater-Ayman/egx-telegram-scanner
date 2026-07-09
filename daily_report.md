# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-07-09T10:00:02.298446+00:00
Generated Cairo: 2026-07-09 13:00
Run timing: target 09:15 Cairo | generated Cairo 2026-07-09 13:00 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-07-09 12:55

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 75
- Data quality issues: 0
- Tradeable price/liquidity tickers: 179/190
- Top sector: Telecommunications

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, July 09
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 70.0% / above MA50 55.0%
- EGX70 regime: BULLISH / above MA20 79.49% / above MA50 71.79%
- Sector breadth: 57.14%
- Risk mode: BROAD_RISK_ON

## Top Liquidity
- HELI.CA: liquidity=348953376.0 spike=2.87 score=31.64
- CCAP.CA: liquidity=275018240.0 spike=0.4 score=27.9
- AMES.CA: liquidity=161755648.0 spike=6.3 score=15.5
- COMI.CA: liquidity=143608592.0 spike=0.31 score=27.12
- ZMID.CA: liquidity=128532056.0 spike=0.61 score=27.9

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b-20230311:free
- Summary: Scanner highlighted AFMC.CA, HELI.CA and ETEL.CA as BUY setups under a broad risk‑on regime, citing aligned price action, sufficient liquidity and a bullish‑watch outlook while flagging low confidence and sector‑specific cautions.
- AFMC.CA chosen for liquidity accumulation spike, price above MA20/MA50 and support near 66, though its sector is not leading, adding uncertainty.
- HELI.CA flagged due to strong liquidity spike and price above moving averages, but RSI shows extended momentum, suggesting caution for the next 1‑3 days.
- ETEL.CA selected for trade‑able liquidity and price above MA20/MA50 with clear support around 89, yet cooling liquidity tempers the short‑term outlook.

## Top Liquidity Spikes
- UNIT.CA: spike=9.4 liquidity=100560944.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- UEFM.CA: spike=7.65 liquidity=8446799.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GIHD.CA: spike=7.22 liquidity=67482664.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AFMC.CA: spike=6.73 liquidity=17078834.0 outlook=BULLISH_WATCH score=87.0 buy_ready=True
- AMES.CA: spike=6.3 liquidity=161755648.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=9.5 5d=3.06% 20d=2.85% aboveMA50=100.0%
- #2 Fintech & Payments: score=8.87 5d=7.64% 20d=4.37% aboveMA50=50.0%
- #3 Technology & Distribution: score=8.87 5d=1.56% 20d=4.56% aboveMA50=100.0%
- #4 Real Estate: score=7.63 5d=3.49% 20d=2.08% aboveMA50=92.31%
- #5 Textiles: score=6.74 5d=2.95% 20d=0.0% aboveMA50=100.0%
- #6 Investment Holding: score=6.73 5d=3.23% 20d=0.71% aboveMA50=66.67%
- #7 Automotive & Distribution: score=6.47 5d=-2.15% 20d=4.7% aboveMA50=100.0%
- #8 Food, Beverages & Tobacco: score=5.65 5d=1.74% 20d=1.04% aboveMA50=71.43%

## Today's Prioritized Action Tickets
- Priority #1: BUY AFMC.CA
  - Entry: 73.09 | Take profit: 78.93 | Stop loss: 70.17
  - Confidence: LOW | score=32.5 | outlook=BULLISH_WATCH 87.0
  - Reason: BUY SETUP: AFMC.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 49.04, support 66.0, resistance 74.79, and evidence sources. Macro trend is Bullish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY HELI.CA
  - Entry: 7.12 | Take profit: 7.68 | Stop loss: 6.84
  - Confidence: LOW | score=31.64 | outlook=BULLISH_WATCH 88.63
  - Reason: WATCH/BUY SETUP: HELI.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 66.93, support 6.28, resistance 6.91, and evidence sources. Macro trend is Bullish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY ETEL.CA
  - Entry: 96.86 | Take profit: 104.6 | Stop loss: 92.99
  - Confidence: LOW | score=30.9 | outlook=BULLISH_WATCH 89.5
  - Reason: BUY SETUP: ETEL.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 60.23, support 89.01, resistance 101.5, and evidence sources. Macro trend is Bullish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ETEL.CA: BULLISH_WATCH score=89.5 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- HELI.CA: BULLISH_WATCH score=88.63 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- ARAB.CA: BULLISH_WATCH score=88.63 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- AFMC.CA: BULLISH_WATCH score=87.0 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CEFM.CA: BULLISH_WATCH score=87.0 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- OBRI.CA: BULLISH_WATCH score=87.0 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ENGC.CA: BULLISH_WATCH score=87.0 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- EFIH.CA: BULLISH_WATCH score=86.87 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- MENA.CA: BULLISH_WATCH score=83.63 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- BIOC.CA: BULLISH_WATCH score=83.0 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- AFMC.CA: rank=32.5 outlook=BULLISH_WATCH outlook_score=87.0 sector_rank=11 price=73.09 support=66.0 resistance=74.79 liquidity=17078834.0
- HELI.CA: rank=31.64 outlook=BULLISH_WATCH outlook_score=88.63 sector_rank=4 price=7.12 support=6.28 resistance=6.91 liquidity=348953376.0
- ETEL.CA: rank=30.9 outlook=BULLISH_WATCH outlook_score=89.5 sector_rank=1 price=96.86 support=89.01 resistance=101.5 liquidity=21316178.0
- NHPS.CA: rank=30.5 outlook=BULLISH_WATCH outlook_score=79.0 sector_rank=11 price=71.59 support=61.55 resistance=75.49 liquidity=68076864.0
- CEFM.CA: rank=30.24 outlook=BULLISH_WATCH outlook_score=87.0 sector_rank=11 price=105.67 support=95.75 resistance=109.0 liquidity=7743280.5
- EFIH.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=86.87 sector_rank=2 price=22.22 support=20.0 resistance=23.65 liquidity=20151696.0
- OBRI.CA: rank=29.86 outlook=BULLISH_WATCH outlook_score=87.0 sector_rank=11 price=36.18 support=31.5 resistance=39.27 liquidity=59350456.0
- CERA.CA: rank=29.54 outlook=BULLISH_WATCH outlook_score=81.0 sector_rank=11 price=1.32 support=1.15 resistance=1.3 liquidity=39458248.0
- RREI.CA: rank=29.52 outlook=BULLISH_WATCH outlook_score=77.0 sector_rank=11 price=3.8 support=3.34 resistance=3.93 liquidity=17604460.0
- ARAB.CA: rank=29.1 outlook=BULLISH_WATCH outlook_score=88.63 sector_rank=4 price=0.23 support=0.2 resistance=0.24 liquidity=118318568.0

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=27.5 buy_ready=True sector_rank=11 price=220.47 support=196.0 resistance=247.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=62.25 liquidity=11641331.0 spike=0.87
- ABUK.CA: score=21.84 buy_ready=False sector_rank=19 price=70.36 support=66.66 resistance=81.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=50.59 liquidity=84327872.0 spike=0.61
- ACAMD.CA: score=27.5 buy_ready=True sector_rank=11 price=2.32 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=50209328.0 spike=0.49
- ACGC.CA: score=18.7 buy_ready=True sector_rank=5 price=9.48 support=8.92 resistance=10.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=51.27 liquidity=2795658.75 spike=0.12
- ADCI.CA: score=16.22 buy_ready=False sector_rank=11 price=230.7 support=219.0 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=56.4 liquidity=2724897.25 spike=0.23
- ADIB.CA: score=27.32 buy_ready=True sector_rank=14 price=47.0 support=44.01 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=43.33 liquidity=97525368.0 spike=1.1
- ADPC.CA: score=23.28 buy_ready=False sector_rank=11 price=3.65 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=45.79 liquidity=18264750.0 spike=1.39
- AFDI.CA: score=21.98 buy_ready=True sector_rank=11 price=45.48 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=58.78 liquidity=4482454.0 spike=0.38
- AFMC.CA: score=32.5 buy_ready=True sector_rank=11 price=73.09 support=66.0 resistance=74.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=49.04 liquidity=17078834.0 spike=6.73
- AJWA.CA: score=13.89 buy_ready=False sector_rank=11 price=175.44 support=144.0 resistance=190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=34.21 liquidity=3393900.5 spike=0.13
- ALCN.CA: score=25.38 buy_ready=False sector_rank=9 price=28.96 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=50.15 liquidity=14499123.0 spike=1.31
- ALUM.CA: score=20.1 buy_ready=False sector_rank=11 price=22.78 support=20.55 resistance=25.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=49.4 liquidity=5595866.5 spike=0.69
- AMER.CA: score=26.4 buy_ready=True sector_rank=4 price=2.91 support=2.28 resistance=2.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=67.05 liquidity=84696040.0 spike=1.25
- AMES.CA: score=15.5 buy_ready=False sector_rank=11 price=79.5 support=70.78 resistance=84.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=161755648.0 spike=6.3
- AMIA.CA: score=16.6 buy_ready=True sector_rank=11 price=8.96 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=45.05 liquidity=1101778.25 spike=0.11
- AMOC.CA: score=24.96 buy_ready=False sector_rank=12 price=8.01 support=7.42 resistance=8.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=59.59 liquidity=67405920.0 spike=1.3
- ANFI.CA: score=11.83 buy_ready=False sector_rank=11 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=STALE RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=11.76 buy_ready=False sector_rank=11 price=8.49 support=8.0 resistance=8.98 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=48.41 liquidity=258860.09 spike=0.32
- ARAB.CA: score=29.1 buy_ready=True sector_rank=4 price=0.23 support=0.2 resistance=0.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=58.18 liquidity=118318568.0 spike=1.6
- ARCC.CA: score=15.88 buy_ready=False sector_rank=13 price=55.38 support=53.0 resistance=58.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=44.73 liquidity=5719168.5 spike=0.25
- AREH.CA: score=25.5 buy_ready=True sector_rank=11 price=1.6 support=1.42 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=17858814.0 spike=0.49
- ARVA.CA: score=15.56 buy_ready=False sector_rank=11 price=10.86 support=10.3 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=40.17 liquidity=2062655.25 spike=0.08
- ASCM.CA: score=23.5 buy_ready=False sector_rank=11 price=58.08 support=54.12 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=46.6 liquidity=11377038.0 spike=0.15
- ASPI.CA: score=20.06 buy_ready=False sector_rank=11 price=0.32 support=0.3 resistance=0.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=54.76 liquidity=6556660.0 spike=0.17
- ATLC.CA: score=15.95 buy_ready=True sector_rank=18 price=5.19 support=4.7 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=50.67 liquidity=1063049.75 spike=0.15
- ATQA.CA: score=17.38 buy_ready=False sector_rank=19 price=9.55 support=9.02 resistance=10.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=42.75 liquidity=4536513.5 spike=0.14
- AXPH.CA: score=17.13 buy_ready=True sector_rank=11 price=1180.71 support=1073.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=65.94 liquidity=1628581.88 spike=0.53
- BINV.CA: score=17.22 buy_ready=True sector_rank=6 price=48.37 support=44.02 resistance=51.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=53.46 liquidity=1320243.75 spike=0.19
- BIOC.CA: score=22.73 buy_ready=True sector_rank=11 price=74.34 support=66.75 resistance=76.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=54.48 liquidity=3228163.75 spike=0.98
- BTFH.CA: score=22.88 buy_ready=False sector_rank=18 price=3.05 support=2.91 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=54.9 liquidity=37196296.0 spike=0.19
- CAED.CA: score=21.98 buy_ready=True sector_rank=11 price=72.88 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=54.04 liquidity=4479019.5 spike=0.9
- CANA.CA: score=14.98 buy_ready=False sector_rank=14 price=36.32 support=34.5 resistance=38.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=39.38 liquidity=2860831.25 spike=0.25
- CCAP.CA: score=27.9 buy_ready=True sector_rank=6 price=5.19 support=4.65 resistance=5.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=54.9 liquidity=275018240.0 spike=0.4
- CCRS.CA: score=16.09 buy_ready=False sector_rank=11 price=2.37 support=2.18 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=32.2 liquidity=7594394.0 spike=0.61
- CEFM.CA: score=30.24 buy_ready=True sector_rank=11 price=105.67 support=95.75 resistance=109.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=45.41 liquidity=7743280.5 spike=4.28
- CERA.CA: score=29.54 buy_ready=True sector_rank=11 price=1.32 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=45.0 liquidity=39458248.0 spike=2.02
- CFGH.CA: score=6.5 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.1 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=1494.6 spike=0.32
- CICH.CA: score=14.49 buy_ready=False sector_rank=18 price=11.68 support=11.1 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=2604410.25 spike=0.76
- CIEB.CA: score=18.57 buy_ready=True sector_rank=14 price=24.1 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=50.86 liquidity=1452451.88 spike=0.21
- CIRA.CA: score=22.16 buy_ready=True sector_rank=16 price=28.9 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=68.69 liquidity=9201684.0 spike=0.48
- CLHO.CA: score=18.83 buy_ready=True sector_rank=10 price=16.31 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=59.22 liquidity=3186240.0 spike=0.09
- CNFN.CA: score=20.25 buy_ready=True sector_rank=18 price=4.82 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=63.64 liquidity=3367599.5 spike=0.07
- COMI.CA: score=27.12 buy_ready=True sector_rank=14 price=134.29 support=126.21 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=49.31 liquidity=143608592.0 spike=0.31
- COPR.CA: score=19.55 buy_ready=False sector_rank=11 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=37.29 liquidity=7045357.0 spike=0.3
- COSG.CA: score=27.5 buy_ready=True sector_rank=11 price=1.6 support=1.47 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=45.16 liquidity=12624565.0 spike=0.27
- CPCI.CA: score=12.9 buy_ready=False sector_rank=11 price=398.77 support=354.0 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=75.84 liquidity=400270.31 spike=0.14
- CSAG.CA: score=21.94 buy_ready=True sector_rank=9 price=32.27 support=30.08 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=61.35 liquidity=4182349.25 spike=0.24
- DAPH.CA: score=22.56 buy_ready=True sector_rank=11 price=82.93 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=49.3 liquidity=5062743.0 spike=0.56
- DEIN.CA: score=0.5 buy_ready=False sector_rank=11 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=16.83 buy_ready=False sector_rank=8 price=26.92 support=23.7 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=72.53 liquidity=1068881.38 spike=0.21
- DSCW.CA: score=16.94 buy_ready=False sector_rank=11 price=1.79 support=1.71 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=34.78 liquidity=8437961.0 spike=0.29
- DTPP.CA: score=24.5 buy_ready=False sector_rank=11 price=204.09 support=114.0 resistance=234.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=88.92 liquidity=17770472.0 spike=0.57
- EALR.CA: score=28.1 buy_ready=True sector_rank=11 price=360.49 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=53.5 liquidity=13160452.0 spike=1.3
- EASB.CA: score=23.6 buy_ready=False sector_rank=11 price=7.08 support=4.87 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=45.15 liquidity=16603444.0 spike=1.05
- EAST.CA: score=14.76 buy_ready=False sector_rank=8 price=36.98 support=36.63 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=31.59 liquidity=13987568.0 spike=0.31
- EBSC.CA: score=20.02 buy_ready=True sector_rank=11 price=1.92 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=51.95 liquidity=2523468.5 spike=0.51
- ECAP.CA: score=14.42 buy_ready=False sector_rank=11 price=32.43 support=30.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=49.25 liquidity=915076.63 spike=0.09
- EDFM.CA: score=22.84 buy_ready=True sector_rank=11 price=341.03 support=310.2 resistance=344.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=52.76 liquidity=2337524.0 spike=4.12
- EEII.CA: score=10.5 buy_ready=False sector_rank=11 price=2.89 support=2.73 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13796098.0 spike=0.63
- EFIC.CA: score=5.17 buy_ready=False sector_rank=19 price=180.55 support=180.02 resistance=208.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=15.88 liquidity=1321886.75 spike=0.51
- EFID.CA: score=27.76 buy_ready=True sector_rank=8 price=28.4 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=48.68 liquidity=43259080.0 spike=0.57
- EFIH.CA: score=29.9 buy_ready=True sector_rank=2 price=22.22 support=20.0 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=62.91 liquidity=20151696.0 spike=0.46
- EGAL.CA: score=21.84 buy_ready=False sector_rank=19 price=293.08 support=272.28 resistance=318.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=45.46 liquidity=11057204.0 spike=0.22
- EGAS.CA: score=15.75 buy_ready=False sector_rank=12 price=49.85 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=42.74 liquidity=2387565.0 spike=0.3
- EGBE.CA: score=17.14 buy_ready=False sector_rank=14 price=0.46 support=0.43 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=60.71 liquidity=24239.7 spike=0.37
- EGCH.CA: score=22.66 buy_ready=False sector_rank=19 price=13.1 support=12.13 resistance=14.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=38.61 liquidity=58800516.0 spike=1.41
- EGSA.CA: score=17.9 buy_ready=False sector_rank=1 price=9.11 support=8.62 resistance=8.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=20132.64 spike=1.99
- EGTS.CA: score=27.9 buy_ready=True sector_rank=4 price=18.69 support=15.1 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=54.5 liquidity=29800544.0 spike=0.46
- EHDR.CA: score=23.5 buy_ready=False sector_rank=11 price=2.61 support=2.37 resistance=2.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=40.58 liquidity=22198962.0 spike=0.51
- EKHO.CA: score=12.36 buy_ready=False sector_rank=12 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=12.0 buy_ready=False sector_rank=17 price=2.1 support=2.04 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=3111890.0 spike=0.2
- ELKA.CA: score=11.9 buy_ready=False sector_rank=11 price=1.54 support=1.42 resistance=1.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=74257496.0 spike=1.7
- ELNA.CA: score=14.02 buy_ready=False sector_rank=11 price=38.75 support=35.55 resistance=41.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=35.49 liquidity=524656.5 spike=1.0
- ELSH.CA: score=25.5 buy_ready=True sector_rank=11 price=13.62 support=11.1 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=47.58 liquidity=116985992.0 spike=0.66
- ELWA.CA: score=10.81 buy_ready=False sector_rank=11 price=1.89 support=1.89 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=37.84 liquidity=306994.44 spike=0.15
- EMFD.CA: score=25.9 buy_ready=True sector_rank=4 price=11.87 support=11.11 resistance=12.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=35.26 liquidity=25996010.0 spike=0.13
- ENGC.CA: score=28.74 buy_ready=True sector_rank=11 price=37.51 support=33.0 resistance=39.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=66.28 liquidity=24756772.0 spike=1.62
- EOSB.CA: score=15.51 buy_ready=False sector_rank=11 price=1.48 support=1.42 resistance=1.55 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=11715.68 spike=0.12
- EPCO.CA: score=11.28 buy_ready=False sector_rank=11 price=8.99 support=8.5 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=782370.81 spike=0.12
- EPPK.CA: score=17.72 buy_ready=False sector_rank=11 price=14.32 support=11.72 resistance=15.25 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=74.03 liquidity=1344834.13 spike=1.44
- ETEL.CA: score=30.9 buy_ready=True sector_rank=1 price=96.86 support=89.01 resistance=101.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=60.23 liquidity=21316178.0 spike=0.28
- ETRS.CA: score=25.5 buy_ready=True sector_rank=11 price=10.82 support=8.77 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=57.43 liquidity=29598150.0 spike=0.38
- EXPA.CA: score=20.12 buy_ready=False sector_rank=14 price=18.44 support=18.03 resistance=19.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=41.76 liquidity=11393246.0 spike=0.38
- FAIT.CA: score=21.87 buy_ready=True sector_rank=14 price=37.05 support=35.01 resistance=37.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=41.72 liquidity=4734710.5 spike=2.01
- FAITA.CA: score=10.61 buy_ready=False sector_rank=14 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=52.0 liquidity=36826.02 spike=1.23
- FERC.CA: score=18.9 buy_ready=False sector_rank=19 price=76.19 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=55.95 liquidity=5216510.5 spike=1.42
- FWRY.CA: score=26.9 buy_ready=False sector_rank=2 price=19.26 support=17.71 resistance=19.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=61.9 liquidity=28692000.0 spike=0.13
- GBCO.CA: score=25.9 buy_ready=True sector_rank=7 price=30.84 support=26.62 resistance=32.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=63.86 liquidity=11421000.0 spike=0.13
- GDWA.CA: score=7.02 buy_ready=False sector_rank=11 price=0.77 support=0.76 resistance=0.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=28.72 liquidity=2522586.25 spike=0.18
- GGCC.CA: score=24.5 buy_ready=False sector_rank=11 price=0.55 support=0.4 resistance=0.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=91.88 liquidity=13861141.0 spike=0.84
- GIHD.CA: score=15.5 buy_ready=False sector_rank=11 price=48.01 support=43.0 resistance=49.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=67482664.0 spike=7.22
- GMCI.CA: score=17.64 buy_ready=False sector_rank=11 price=2.09 support=1.66 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=85.45 liquidity=1584494.13 spike=1.78
- GRCA.CA: score=6.68 buy_ready=False sector_rank=11 price=50.29 support=48.75 resistance=58.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=14.64 liquidity=1179071.13 spike=0.35
- GSSC.CA: score=29.5 buy_ready=False sector_rank=11 price=256.39 support=240.0 resistance=263.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=60.77 liquidity=13778732.0 spike=3.63
- GTWL.CA: score=25.54 buy_ready=False sector_rank=11 price=104.94 support=46.0 resistance=108.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=90.08 liquidity=112187240.0 spike=1.52
- HDBK.CA: score=14.12 buy_ready=False sector_rank=14 price=79.86 support=75.3 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=20.35 liquidity=16050971.0 spike=0.41
- HELI.CA: score=31.64 buy_ready=True sector_rank=4 price=7.12 support=6.28 resistance=6.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=66.93 liquidity=348953376.0 spike=2.87
- HRHO.CA: score=20.88 buy_ready=False sector_rank=18 price=26.71 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=35.4 liquidity=23157880.0 spike=0.17
- ICID.CA: score=17.78 buy_ready=True sector_rank=11 price=7.75 support=6.36 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=56.3 liquidity=2283765.0 spike=0.21
- IDRE.CA: score=18.77 buy_ready=True sector_rank=11 price=43.69 support=41.1 resistance=46.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=42.22 liquidity=3273034.75 spike=0.32
- IFAP.CA: score=20.98 buy_ready=False sector_rank=15 price=19.65 support=18.47 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=47.09 liquidity=6400918.5 spike=1.31
- INFI.CA: score=28.5 buy_ready=False sector_rank=11 price=97.41 support=88.51 resistance=102.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=40.25 liquidity=27459860.0 spike=4.5
- IRON.CA: score=15.59 buy_ready=False sector_rank=19 price=32.15 support=30.51 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=44.92 liquidity=2744960.25 spike=0.35
- ISMA.CA: score=12.8 buy_ready=False sector_rank=11 price=26.97 support=26.82 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=3.11 liquidity=4295188.5 spike=0.13
- ISMQ.CA: score=21.84 buy_ready=False sector_rank=19 price=9.75 support=7.67 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=77.42 liquidity=44379424.0 spike=0.32
- ISPH.CA: score=20.64 buy_ready=False sector_rank=10 price=11.38 support=11.2 resistance=12.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=37.45 liquidity=21978772.0 spike=0.29
- JUFO.CA: score=21.89 buy_ready=True sector_rank=8 price=30.94 support=28.5 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=51.44 liquidity=6133524.0 spike=0.21
- KABO.CA: score=24.9 buy_ready=False sector_rank=5 price=7.44 support=5.96 resistance=7.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=87.66 liquidity=17214636.0 spike=0.63
- KWIN.CA: score=9.32 buy_ready=False sector_rank=11 price=67.38 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=30.79 liquidity=4822309.5 spike=0.37
- KZPC.CA: score=12.34 buy_ready=False sector_rank=11 price=8.38 support=8.26 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=35.83 liquidity=2843089.75 spike=0.43
- LCSW.CA: score=27.16 buy_ready=True sector_rank=13 price=31.22 support=26.0 resistance=31.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=68.46 liquidity=37466992.0 spike=0.71
- LUTS.CA: score=25.5 buy_ready=True sector_rank=11 price=0.74 support=0.62 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=49.66 liquidity=20244344.0 spike=0.36
- MAAL.CA: score=24.5 buy_ready=False sector_rank=11 price=8.29 support=5.52 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=99.42 liquidity=15839461.0 spike=0.95
- MASR.CA: score=27.5 buy_ready=True sector_rank=11 price=7.7 support=6.54 resistance=7.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=58.67 liquidity=47652832.0 spike=0.61
- MBSC.CA: score=22.16 buy_ready=False sector_rank=13 price=242.46 support=222.66 resistance=257.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=40.85 liquidity=14652805.0 spike=0.58
- MCQE.CA: score=18.99 buy_ready=False sector_rank=13 price=177.63 support=166.66 resistance=189.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=52.03 liquidity=4830250.5 spike=0.33
- MCRO.CA: score=23.5 buy_ready=True sector_rank=11 price=1.24 support=1.17 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=21183136.0 spike=0.69
- MENA.CA: score=19.86 buy_ready=True sector_rank=4 price=7.03 support=6.41 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=59.16 liquidity=1959638.5 spike=0.23
- MEPA.CA: score=24.5 buy_ready=False sector_rank=11 price=1.65 support=1.52 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=10049235.0 spike=0.91
- MFPC.CA: score=23.84 buy_ready=False sector_rank=19 price=37.1 support=34.22 resistance=42.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=51.97 liquidity=88909664.0 spike=0.92
- MFSC.CA: score=16.86 buy_ready=False sector_rank=11 price=46.9 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=58.57 liquidity=3364357.25 spike=0.46
- MHOT.CA: score=10.9 buy_ready=False sector_rank=21 price=16.81 support=16.12 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=24.36 liquidity=14907614.0 spike=0.98
- MICH.CA: score=23.82 buy_ready=True sector_rank=11 price=37.9 support=34.0 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=51.51 liquidity=8322043.0 spike=0.52
- MILS.CA: score=25.5 buy_ready=False sector_rank=11 price=135.46 support=126.31 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=29.41 liquidity=46001488.0 spike=5.08
- MIPH.CA: score=19.02 buy_ready=True sector_rank=10 price=690.6 support=630.13 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=59.58 liquidity=1373893.5 spike=0.61
- MOED.CA: score=15.67 buy_ready=False sector_rank=11 price=0.69 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=43.8 liquidity=4173792.5 spike=0.45
- MOIL.CA: score=15.46 buy_ready=False sector_rank=12 price=0.52 support=0.46 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:12 AM market time freshness=DELAYED_CURRENT RSI=72.63 liquidity=97587.49 spike=0.34
- MOIN.CA: score=16.32 buy_ready=False sector_rank=11 price=24.05 support=22.6 resistance=25.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=41.18 liquidity=1335433.0 spike=1.74
- MOSC.CA: score=11.22 buy_ready=False sector_rank=11 price=271.19 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=41.71 liquidity=719143.38 spike=0.08
- MPCI.CA: score=23.54 buy_ready=True sector_rank=11 price=238.56 support=213.0 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=61.06 liquidity=8038450.5 spike=0.08
- MPCO.CA: score=17.96 buy_ready=False sector_rank=15 price=1.83 support=1.66 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=11911612.0 spike=0.13
- MPRC.CA: score=10.94 buy_ready=False sector_rank=11 price=43.0 support=40.7 resistance=43.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=56519200.0 spike=1.22
- MTIE.CA: score=25.7 buy_ready=True sector_rank=7 price=9.36 support=8.65 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=7798448.0 spike=0.39
- NAHO.CA: score=11.52 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=24715.65 spike=0.98
- NCCW.CA: score=21.89 buy_ready=False sector_rank=11 price=6.16 support=5.82 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=42.55 liquidity=8388590.0 spike=0.3
- NEDA.CA: score=12.41 buy_ready=False sector_rank=11 price=2.74 support=2.7 resistance=2.83 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=31.58 liquidity=1905448.07 spike=5.71
- NHPS.CA: score=30.5 buy_ready=True sector_rank=11 price=71.59 support=61.55 resistance=75.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=65.33 liquidity=68076864.0 spike=4.58
- NINH.CA: score=17.13 buy_ready=False sector_rank=11 price=17.76 support=16.8 resistance=18.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=47.76 liquidity=4629784.5 spike=0.67
- NIPH.CA: score=27.64 buy_ready=True sector_rank=10 price=175.35 support=157.01 resistance=185.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=64.8 liquidity=28777182.0 spike=0.3
- OBRI.CA: score=29.86 buy_ready=True sector_rank=11 price=36.18 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=46.72 liquidity=59350456.0 spike=2.18
- OCDI.CA: score=22.9 buy_ready=False sector_rank=4 price=26.96 support=20.0 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=81.43 liquidity=32577804.0 spike=0.34
- OCPH.CA: score=16.41 buy_ready=False sector_rank=11 price=355.01 support=337.0 resistance=374.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=58.42 liquidity=1910985.0 spike=0.29
- ODIN.CA: score=21.15 buy_ready=True sector_rank=11 price=2.35 support=2.01 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=58.18 liquidity=3653636.25 spike=0.27
- OFH.CA: score=27.5 buy_ready=True sector_rank=11 price=0.64 support=0.57 resistance=0.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=58.14 liquidity=11105999.0 spike=0.55
- OIH.CA: score=22.9 buy_ready=False sector_rank=6 price=1.41 support=1.33 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=70.0 liquidity=15673302.0 spike=0.2
- OLFI.CA: score=27.26 buy_ready=True sector_rank=8 price=22.77 support=21.0 resistance=23.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=62.42 liquidity=9504902.0 spike=0.33
- ORAS.CA: score=9.1 buy_ready=False sector_rank=20 price=685.03 support=680.1 resistance=687.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=102909672.0 spike=1.0
- ORHD.CA: score=25.9 buy_ready=True sector_rank=4 price=39.2 support=35.01 resistance=39.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=57.63 liquidity=52378668.0 spike=0.31
- ORWE.CA: score=19.25 buy_ready=False sector_rank=5 price=22.8 support=21.95 resistance=23.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=42.11 liquidity=5352341.5 spike=0.25
- PHAR.CA: score=18.78 buy_ready=True sector_rank=10 price=86.64 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=58.51 liquidity=1134070.25 spike=0.05
- PHDC.CA: score=18.9 buy_ready=False sector_rank=4 price=14.78 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=21.98 liquidity=88421976.0 spike=0.27
- PHTV.CA: score=11.32 buy_ready=False sector_rank=11 price=293.94 support=273.5 resistance=297.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17961406.0 spike=1.41
- POUL.CA: score=23.86 buy_ready=True sector_rank=8 price=39.5 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=66.8 liquidity=8099619.5 spike=0.21
- PRCL.CA: score=24.16 buy_ready=False sector_rank=13 price=36.04 support=23.75 resistance=36.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=84.32 liquidity=12448120.0 spike=0.24
- PRDC.CA: score=27.9 buy_ready=True sector_rank=4 price=8.45 support=5.91 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=57.89 liquidity=10102888.0 spike=0.07
- PRMH.CA: score=11.04 buy_ready=False sector_rank=11 price=2.55 support=2.34 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=29.17 liquidity=2542542.5 spike=0.09
- RACC.CA: score=21.73 buy_ready=True sector_rank=11 price=10.01 support=9.36 resistance=10.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=57.74 liquidity=4232029.0 spike=0.41
- RAKT.CA: score=12.61 buy_ready=False sector_rank=11 price=22.35 support=21.4 resistance=23.79 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=41.67 liquidity=371568.76 spike=1.37
- RAYA.CA: score=28.9 buy_ready=True sector_rank=3 price=7.92 support=6.7 resistance=8.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=63.3 liquidity=93027576.0 spike=0.89
- RMDA.CA: score=18.04 buy_ready=False sector_rank=10 price=5.01 support=4.81 resistance=5.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=40.98 liquidity=4391019.5 spike=0.06
- ROTO.CA: score=25.5 buy_ready=True sector_rank=11 price=42.25 support=33.06 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=43.66 liquidity=12402833.0 spike=0.39
- RREI.CA: score=29.52 buy_ready=True sector_rank=11 price=3.8 support=3.34 resistance=3.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=58.46 liquidity=17604460.0 spike=1.01
- RTVC.CA: score=13.69 buy_ready=False sector_rank=11 price=3.76 support=3.55 resistance=4.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=45.21 liquidity=1192149.38 spike=0.24
- RUBX.CA: score=22.5 buy_ready=False sector_rank=11 price=13.14 support=9.8 resistance=14.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=78.82 liquidity=21209768.0 spike=0.41
- SAUD.CA: score=13.44 buy_ready=False sector_rank=14 price=21.31 support=19.99 resistance=22.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=40.61 liquidity=1324873.25 spike=0.19
- SCEM.CA: score=19.32 buy_ready=False sector_rank=13 price=62.51 support=59.3 resistance=67.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=49.89 liquidity=5155847.5 spike=0.3
- SCFM.CA: score=29.5 buy_ready=False sector_rank=11 price=253.09 support=226.5 resistance=262.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=41.95 liquidity=24693818.0 spike=6.13
- SCTS.CA: score=20.09 buy_ready=True sector_rank=16 price=614.68 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=57.13 liquidity=3134752.0 spike=0.61
- SDTI.CA: score=14.96 buy_ready=False sector_rank=11 price=46.2 support=45.55 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=44.19 liquidity=1457952.5 spike=0.19
- SEIG.CA: score=27.54 buy_ready=False sector_rank=11 price=252.55 support=180.0 resistance=272.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=96.63 liquidity=32580158.0 spike=2.52
- SIPC.CA: score=16.18 buy_ready=False sector_rank=11 price=3.48 support=3.25 resistance=3.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=47.44 liquidity=1675476.0 spike=0.17
- SKPC.CA: score=23.24 buy_ready=False sector_rank=19 price=16.43 support=15.58 resistance=17.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=52.23 liquidity=39224080.0 spike=1.2
- SMFR.CA: score=15.07 buy_ready=False sector_rank=11 price=203.33 support=187.01 resistance=209.99 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=49.19 liquidity=566070.73 spike=0.33
- SNFC.CA: score=6.61 buy_ready=False sector_rank=11 price=11.39 support=11.26 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=26.23 liquidity=1110867.38 spike=0.09
- SPIN.CA: score=17.37 buy_ready=False sector_rank=5 price=14.55 support=13.3 resistance=14.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=70.21 liquidity=1465829.63 spike=0.16
- SPMD.CA: score=25.5 buy_ready=True sector_rank=11 price=0.45 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=58.73 liquidity=11867656.0 spike=0.64
- SUGR.CA: score=6.42 buy_ready=False sector_rank=8 price=46.97 support=45.31 resistance=50.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=29.6 liquidity=1664336.0 spike=0.32
- SVCE.CA: score=27.5 buy_ready=True sector_rank=11 price=9.32 support=8.11 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=51.59 liquidity=16669356.0 spike=0.23
- SWDY.CA: score=20.37 buy_ready=True sector_rank=17 price=88.23 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=55.81 liquidity=3473050.75 spike=0.26
- TALM.CA: score=9.39 buy_ready=False sector_rank=16 price=15.44 support=15.27 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=23.53 liquidity=4435923.0 spike=0.4
- TMGH.CA: score=27.9 buy_ready=True sector_rank=4 price=97.03 support=92.1 resistance=99.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=57.6 liquidity=87197008.0 spike=0.24
- TRTO.CA: score=11.5 buy_ready=False sector_rank=11 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=13.95 buy_ready=False sector_rank=11 price=513.0 support=480.0 resistance=529.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8446799.0 spike=7.65
- UEGC.CA: score=24.5 buy_ready=False sector_rank=11 price=1.72 support=1.33 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=76.36 liquidity=13718546.0 spike=0.54
- UNIP.CA: score=19.28 buy_ready=True sector_rank=11 price=0.33 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=40.74 liquidity=3778018.5 spike=0.19
- UNIT.CA: score=15.9 buy_ready=False sector_rank=4 price=18.8 support=16.64 resistance=19.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=100560944.0 spike=9.4
- WCDF.CA: score=12.8 buy_ready=False sector_rank=11 price=523.65 support=450.0 resistance=544.99 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=37.43 liquidity=304240.66 spike=0.98
- WKOL.CA: score=22.0 buy_ready=True sector_rank=11 price=313.01 support=273.1 resistance=334.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:27 AM market time freshness=DELAYED_CURRENT RSI=63.41 liquidity=4495592.0 spike=0.68
- ZEOT.CA: score=21.48 buy_ready=True sector_rank=11 price=11.01 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=46.51 liquidity=5982128.5 spike=0.16
- ZMID.CA: score=27.9 buy_ready=True sector_rank=4 price=6.79 support=6.03 resistance=6.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=63.95 liquidity=128532056.0 spike=0.61

## Backtesting Lite
- AFMC.CA: 180d return=-4.97%, max drawdown=-29.5%, MA20>MA50 days last20=13, as_of=2026-07-07T21:00:00+00:00
- HELI.CA: 180d return=128.56%, max drawdown=-14.36%, MA20>MA50 days last20=20, as_of=2026-07-07T21:00:00+00:00
- ETEL.CA: 180d return=93.86%, max drawdown=-30.44%, MA20>MA50 days last20=9, as_of=2026-07-07T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- AFMC.CA: status=RECENT_ACCEPTED latest=2026-06-29 age_days=10 sources=3 expected=Alexandria Flour Mills summary=Alexandria Flour Mills (AFMC.CA) has shown positive financial performance in the last 12 months. The company reported revenue of EGP 392.46 million and profits of 53.96 million. Its stock price increased by over 138% in the last 52 weeks. Recent quarterly results (May 2026) indicate a net income of EGP 11.16 million and revenue of EGP 94.26 million. The company also announced an annual dividend of EGP 0.75 per share with an ex-dividend date of November 10, 2025.
  - Alexandria Flour Mills (EGX:AFMC) Statistics & Valuation Metrics - Stock Analysis (June 29, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGl1Rtmc3l9FfgOV8LQQueiszGhOx9SyZiF8b8ongu2qbrTEC6G_unikLKHVMAM5_Fmv2Bb3fv17XmmIF9wH3xwXUwE-WsjxTnNvq3TljABjtWMEgBxJIE2GO6vtK8o0ECwIDZtTMT1uuZmQPZ18w==
  - Alexandria Flour Mills - EGX:AFMC Financials - Investing.com (Latest Release: May 04, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP9OD_aVMQETza-yNGxpBLGDs9mbnepkJ9UILqiY1V66wUo31-9REXtylhYzzyt8q34dPikEGWTxvvDeLSS6_fx-3UJLxusb3k8o38FHOkmnj2axcEaI2HeYqSOuIVpzJp5p_4fY4jwKN48G5crh7gxU4VkufG5nxq
  - Alexandria Flour Mills (EGX:AFMC) Dividend History, Dates & Yield - Stock Analysis (November 10, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHE5zE_Ro91bSFv-Y83REmS5I6VFXmO8SE4CkgeaElYWOIc-McBf5B98lRZKHuDebvONVaN-8hDXt3-HwD14ueRTwm6P1iuApfKqpwxtqkfribtVRbs8qNwpPARAj_JJsTpwlUL5Lu8G2-xlDg==
- HELI.CA: status=RECENT_ACCEPTED latest=2026-09-07 age_days=0 sources=2 expected=Heliopolis Housing summary=Heliopolis Housing (HELI.CA) reported significant growth in 2025, with revenue reaching EGP 3.14 billion, a 197.18% increase year-over-year, and earnings of EGP 2.71 billion, up 5.68%. The company's ex-dividend date was May 18, 2026, and its next earnings date is scheduled for September 7, 2026.
  - Heliopolis Co. for Housing & Development (EGX:HELI) Stock Price & Overview (June 25, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIsKpP1L9oBJSjnPXy0RsRSg2G2NUvO66DhL1miRIqG4aSbviXzzdcONTjIZ2_VTVRRPE026amrkhpiG6hnG4OUY1uHfpCVcKPKGL58TgZIhlxVLpEvYN9pTtcCsuATO49Jvw=
  - Heliopolis Co. for Housing & Development Stock (HELI) - Quote Egyptian Exchange: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdfYpqEjcdElh_4leDyJbZkJSLeDQ-rtR4OifBESd-H69oLMsfmGfc7uDP-5Vu0ULaNKFqdvr6msyGR5u3vIxX8242Y8JHRnEBonVoVYOiBASOOE5NACmP0VzOhs3SwF8HPfrQKeF0l0-7HC0s7Xsrcp5pyaB4e6b12JoZxBmbNi3P1X0DWAc=
- ETEL.CA: status=RECENT_ACCEPTED latest=2026-07-07 age_days=2 sources=3 expected=Telecom Egypt summary=Telecom Egypt (ETEL.CA) demonstrated strong financial performance in the last 12 months, with revenue of EGP 110.17 billion and profits of EGP 19.30 billion, resulting in an EPS of 11.30. The stock price has increased by over 152% in the last 52 weeks. For the latest quarter, the company reported revenue of EGP 28.21 billion and a net income of EGP 3.57 billion.
  - Telecom Egypt Company (EGX:ETEL) Statistics & Valuation Metrics - Stock Analysis (July 07, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEB8xviI3S_vHLoAa7OBTWaf7pXa2Mj1-CTu9C7WMCh5B1sqhnEF1fm0lAc5llN8lPJ20VqyHpl_Sbxt1zjBRFJ_w77-n8XrfuX8kIXLNiObWGvmKgsUJveHRD1KTyMlgUKyBieKEK7Y3_84fQGpQ==
  - Telecom Egypt - EGX:ETEL Financials - Investing.com: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHY4iDbCh-wpcW_rY5-0v4V6teB00jBrf0mpoTvzrKttWnkvlthbMnvLGYrAOtFkvCU246DrnXVUJs14N3_v7PmpCoxNwQlxxSnB4yGTfJDJ9-TDWTKTVC5RLg1Ljoao3FVDo7GD3nxW22RcYwamAJRdawWleobpvUE-qq4
  - Telecom Egypt Income Statement - Investing.com: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNU8wpIvdWZzmwcy0T7C7SvXz5WQ_41Q0WVyG0sCEphmxa3lrFmOc3np_MT_ms6BBTWVdefuTKXdpxq6CDN2U-3ZVtEzeZb3HyDtIaDUW1X-DtM5yE9aHxO3sju8QxXtI0A4EOmW4f-lp5Gkal3gVG_dN0F-jcIhLbiUM=
- NHPS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=National Company for Housing Professional Syndicates SAE summary=Evidence rejected for NHPS.CA: source text did not clearly match NHPS.CA / National Company for Housing Professional Syndicates SAE.
- CEFM.CA: status=RECENT_ACCEPTED latest=2026-07-06 age_days=3 sources=3 expected=Middle Egypt Flour Mills summary=Middle Egypt Flour Mills (CEFM.CA) reported fiscal year 2025 revenue of EGP 871.63 million, a 25.21% increase, and earnings of EGP 140.11 million, up 8.76%. The latest quarterly results show revenue of EGP 214.16 million and net income of EGP 27.32 million. The company's Board of Directors held meetings in June and April 2026, and an external auditor's report was released in June 2026. Shareholders approved an EGP 3.25 per share cash dividend.
  - Middle Egypt Flour Mills (EGX:CEFM) Stock Price & Overview (July 3, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGj6VEI8vDRS5gqPXkONEhseIrMw1XaQj7j3tuF5fu_hlN9s_D5kEEKzekBbFF2kg_pTGm_I_OMEZcJ-Vr1KrUTkZVdJ-ZlkFIxX7PtERkXSodFxsoB8Jco7SozgPOxpN6oJwE=
  - Middle Egypt Flour Mills (CEFM) - Mubasher Info (Last Update: July 06, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFd3CPqIwexJB7zn0_Pszi9oQWK3M27iEBoRgXN-yr9Lt74v4k6UrDWC8R6J8Wk-EwA8ntq496npc3oHZZmAYCBKITY4bi-kVPFPlGL9P8EVaHaBbh3UlHT3YwlA1g6MoK5iL6osLq6yDXLvq9GZXXT
  - EGX:CEFM Financials | Middle Egypt Flour Mills - Investing.com: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNsFRKxiCo7tESdW6r6QlExUxH7cxEu5NtsuimzB6gqUrbr5LPVn-AqWsjSj1iR_XYuDvh6f7Uu65atFOiItvP0k0x_oq-TPmcd_PQKcuJDXrTe5i1PxPxYM6WCrXbAfiSOcnqjbqruVwDjFaWarr06v-sNZwh5nl8sNcOcw==
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- OBRI.CA: status=RECENT_ACCEPTED latest=2026-07-07 age_days=2 sources=3 expected=El-Ebour Co. for Real Estate Investment S.A.E. summary=El-Ebour Co. for Real Estate Investment S.A.E. (OBRI.CA) reported strong financial results in the last 12 months, with revenue of EGP 1.57 billion and profits of EGP 62.28 million. The stock price surged by over 265% in the last 52 weeks. First-quarter 2026 earnings showed an EPS of EGP 0.46, revenue of EGP 465.6 million (up 148%), and net income of EGP 18.4 million (up 237%). The company held its Annual General Meeting on May 11, 2026, and approved establishing a real estate investment company in the UAE in January 2026. A semi-annual disclosure form regarding capital increase proceeds was released on May 13, 2026.
  - El-Ebour Co. for Real Estate Investment S.A.E. (EGX:OBRI) Statistics & Valuation Metrics (July 07, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEV_hzPjR45Fjnw6Dk-UcW9qW84t3Je--H-DZxnYb5DTswPumtHOt73O6ZSLemcZYu9pnNBKsILPsn9Ev8m_ui0D8cnb1zSpaaJcZLSQGRjj9gb1gzuZ1-1oxkJc13UC1re_mtHc3RkT4Mh46qOPA==
  - El-Ebour for Real Estate InvestmentE (CASE:OBRI) - Stock Analysis - Simply Wall St (July 04, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdkcM25dUlVD_-An8qgcOvTQNN21j7m9JgwOhIIL-tT94Eku-DSZ2v6LJAHWgg8jyh6W-Cy1c4xOypKX_zWnatc3WxnXi2k_LR2fJbBL_zNKCGlKZFzP9qtd9cxxmyHqB7-ydq5WinucV3-LGmH_wZm-Wq4VfGYjTkPtKb_ctsf1CBRNvUV-nnPKQcczUp5UmB19uiBgceIVbp6a0kwy6oPoHmrDxCMVbjojFupQkKhneYt7_lG_A==
  - El-Ebour Co. for Real Estate Investment S.A.E. Stock (OBRI) - Quote Egyptian Exchange (June 15, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYQEg3Gvs7d7_E0KZqkqXrpoKTHThZZXHMb4s9uhB8EBCBKD52KikY-cfgFC-wdEpqdA51IG3GEFPWEAGb_koyaRUA0L0sF9ILGzBWSpBJpTBJ6sXXLvJuLaC4oz-UPj_56Ks7qOzMmFFNJJ6nLzpK0RkoD9ezdmCnBaFXY0mk2rULasK9Nvos
- CERA.CA: status=RECENT_ACCEPTED latest=2026-08-10 age_days=0 sources=3 expected=The Arab Ceramic Co. summary=The Arab Ceramic Co. (CERA.CA) reported 2025 revenue of EGP 2.29 billion, an increase of 21.30% from the previous year, and earnings of EGP 37.57 million. The latest quarterly results (Q1 2026) show revenue of EGP 565.00 million and a net income of EGP 5.70 million. The next earnings date is scheduled for August 10, 2026.
  - The Arab Ceramic Co. (EGX:CERA) Stock Price & Overview (July 3, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4QzhwcdCIpxYDDpbKgfba4gYNW72KJzz0gZEp-vSFzGo8_XNxZffeIvGQd-2P9ILLZGZMOUgOh9x0Q6e4rr5Yd45wM8kNNxeQxbeAeo12mtIVrbHgwggIcYu5ZNUCHpW9sGQ=
  - Arab Ceramic Co. - Ceramica Remas Income Statement – EGX:CERA - TradingView: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkag_Nv2HQzr5Ich0hwDoRf1E7qEUHrpmDJJJCRBrcSeAEOGnEf2iSypRi14XVvu8aOQb6d9IsuQrHwUxlukkvtGzs6wUh1Ym7jnr17mFhT_ZuLBuRrvx9mxMmaClE9SDR1Pd_PK3-eBs3Zgf0kSCbCMMEQlf4hmDUkX3Qp4zRkdtu2A==
  - The Arab Ceramic Co. (EGX:CERA) Financial Ratios - Stock Analysis (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-xg1O0xdk-tqP3O-I62T4Dlr208Nq3IpqJSFhrTteEIU2-1UseOxqEzJOuq4ohjJF8ahBntEeRcoiPILx_IUzFsdad1X6Ou2XniSxn9So4hipSxMz-C_mtUpr5Kiph9_EIt_Laf6I13h0dLiHiIxgGtyKI88=

## Warnings
- Evidence rejected for NHPS.CA: source text did not clearly match NHPS.CA / National Company for Housing Professional Syndicates SAE.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
