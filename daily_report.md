# Telegram-First EGX Scanner Report

Scan phase: Evening tomorrow plan
Generated UTC: 2026-08-18T17:13:14.430380+00:00
Generated Cairo: 2026-08-18 20:13
Run timing: target 19:30 Cairo | generated Cairo 2026-08-18 20:13 | cron 30 16 * * 0-4
Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-08-18 19:55

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 52
- Data quality issues: 1
- Tradeable price/liquidity tickers: 171/189
- Top sector: Industrial Goods & Cables

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, August 18
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 65.0% / above MA50 70.0%
- EGX70 regime: BULLISH / above MA20 68.57% / above MA50 85.71%
- Sector breadth: 66.67%
- Risk mode: BROAD_RISK_ON

## Top Liquidity
- CCAP.CA: liquidity=1350049792.0 spike=2.4 score=28.7
- PHDC.CA: liquidity=564179840.0 spike=2.35 score=27.31
- BIOC.CA: liquidity=379465164.0 spike=1.72 score=24.34
- COMI.CA: liquidity=377663776.0 spike=0.86 score=23.9
- SCEM.CA: liquidity=348278624.0 spike=1.95 score=29.7

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner flagged SCTS.CA, CIEB.CA and ETEL.CA as watch/buy setups based on aligned price action, adequate liquidity, and technical support/resistance, while the broader EGX30/EGX70 bullish breadth keeps risk mode in BROAD_RISK_ON despite a bearish macro trend.
- SCTS.CA shows liquidity accumulation spike, price above MA20/MA50, RSI 56.7, support near 602 and resistance 685; bullish watch outlook but low confidence due to bearish macro trend.
- CIEB.CA has strong liquidity spike, price above MAs, RSI 68.6 (extended), support 23.75/resistance 24.9; bullish watch with momentum‑extended uncertainty.
- ETEL.CA exhibits cooling liquidity, price above MAs, RSI 64.2, support 97.5/resistance 120; constructive outlook tempered by sector not leading and extended momentum.
- EGX30 and EGX70 are both bullish with ~66% sector breadth, maintaining BROAD_RISK_ON risk mode that supports buys, yet macro bearishness adds overall uncertainty for the next 1‑3 days.

## Top Liquidity Spikes
- AMIA.CA: spike=7.77 liquidity=156226761.65 outlook=CONSTRUCTIVE score=65.67 buy_ready=False
- MOED.CA: spike=6.11 liquidity=204489312.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- NAHO.CA: spike=5.64 liquidity=317487.69 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ICID.CA: spike=5.61 liquidity=90799568.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EALR.CA: spike=5.24 liquidity=222588061.98 outlook=CONSTRUCTIVE score=65.67 buy_ready=False

## Sector Leaderboard
- #1 Industrial Goods & Cables: score=14.63 5d=7.3% 20d=14.16% aboveMA50=100.0%
- #2 Tourism & Leisure: score=12.6 5d=12.24% 20d=16.25% aboveMA50=0.0%
- #3 Education: score=11.61 5d=2.75% 20d=16.56% aboveMA50=100.0%
- #4 Banking & Financials: score=10.96 5d=4.07% 20d=11.78% aboveMA50=90.0%
- #5 Agriculture & Food Production: score=10.88 5d=3.42% 20d=12.88% aboveMA50=100.0%
- #6 Healthcare: score=10.55 5d=-1.1% 20d=23.61% aboveMA50=100.0%
- #7 Basic Resources & Chemicals: score=9.76 5d=4.04% 20d=4.71% aboveMA50=100.0%
- #8 Fintech & Payments: score=9.28 5d=2.88% 20d=7.46% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- Priority #1: BUY SCTS.CA
  - Entry: 617.0 | Take profit: 681.58 | Stop loss: 600.08
  - Confidence: LOW | score=33.9 | outlook=BULLISH_WATCH 100
  - Reason: WATCH/BUY SETUP: SCTS.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 56.73, support 602.01, resistance 685.0, and evidence sources. Macro trend is Bearish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY CIEB.CA
  - Entry: 25.11 | Take profit: 27.11 | Stop loss: 24.11
  - Confidence: LOW | score=32.9 | outlook=BULLISH_WATCH 97
  - Reason: WATCH/BUY SETUP: CIEB.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 68.56, support 23.75, resistance 24.9, and evidence sources. Macro trend is Bearish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY ETEL.CA
  - Entry: 116.75 | Take profit: 126.09 | Stop loss: 112.08
  - Confidence: LOW | score=29.9 | outlook=CONSTRUCTIVE 65.35
  - Reason: WATCH/BUY SETUP: ETEL.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 64.24, support 97.54, resistance 120.0, and evidence sources. Macro trend is Bearish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- SCTS.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- IRON.CA: BULLISH_WATCH score=97.76 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- CIEB.CA: BULLISH_WATCH score=97 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- RTVC.CA: BULLISH_WATCH score=95.67 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- EASB.CA: BULLISH_WATCH score=95.67 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- COPR.CA: BULLISH_WATCH score=91.67 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CIRA.CA: BULLISH_WATCH score=91 liquidity=TRADEABLE sector=LEADING risk=far above support
- SCFM.CA: BULLISH_WATCH score=89.67 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CCAP.CA: BULLISH_WATCH score=88.5 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ISMQ.CA: BULLISH_WATCH score=85.76 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling

## BUY-Ready Candidates
- SCTS.CA: rank=33.9 outlook=BULLISH_WATCH outlook_score=100 sector_rank=3 price=617.0 support=602.01 resistance=685.0 liquidity=38916452.0
- CIEB.CA: rank=32.9 outlook=BULLISH_WATCH outlook_score=97 sector_rank=4 price=25.11 support=23.75 resistance=24.9 liquidity=43842300.0
- COPR.CA: rank=31.64 outlook=BULLISH_WATCH outlook_score=91.67 sector_rank=10 price=0.44 support=0.37 resistance=0.46 liquidity=66959596.79
- ETEL.CA: rank=29.9 outlook=CONSTRUCTIVE outlook_score=65.35 sector_rank=14 price=116.75 support=97.54 resistance=120.0 liquidity=100565680.0
- EHDR.CA: rank=29.9 outlook=CONSTRUCTIVE outlook_score=60.67 sector_rank=10 price=3.14 support=2.71 resistance=3.2 liquidity=30341226.0
- RACC.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=77.67 sector_rank=10 price=10.46 support=9.8 resistance=10.88 liquidity=15967555.0
- SCEM.CA: rank=29.7 outlook=BULLISH_WATCH outlook_score=77.76 sector_rank=15 price=102.5 support=66.75 resistance=113.0 liquidity=348278624.0
- RTVC.CA: rank=29.46 outlook=BULLISH_WATCH outlook_score=95.67 sector_rank=10 price=3.97 support=3.73 resistance=4.2 liquidity=14976248.0
- AJWA.CA: rank=29.38 outlook=BULLISH_WATCH outlook_score=77.67 sector_rank=10 price=197.36 support=161.0 resistance=210.0 liquidity=68044202.13
- GSSC.CA: rank=28.9 outlook=BULLISH_WATCH outlook_score=81.67 sector_rank=10 price=290.0 support=264.0 resistance=300.0 liquidity=84069776.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=29.9 buy_ready=False sector_rank=10 price=366.0 support=234.05 resistance=366.0 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=78.03 liquidity=183449448.0 spike=3.74
- ABUK.CA: score=24.9 buy_ready=False sector_rank=7 price=77.54 support=70.6 resistance=80.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.93 liquidity=77286240.0 spike=0.58
- ACAMD.CA: score=20.9 buy_ready=False sector_rank=10 price=2.23 support=2.21 resistance=2.41 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=44.17 liquidity=25595195.4 spike=0.51
- ACGC.CA: score=13.68 buy_ready=False sector_rank=11 price=14.66 support=14.01 resistance=14.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=87696832.0 spike=2.39
- ADCI.CA: score=27.9 buy_ready=True sector_rank=10 price=299.14 support=235.45 resistance=389.99 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=61.56 liquidity=15707842.17 spike=0.79
- ADIB.CA: score=24.9 buy_ready=False sector_rank=4 price=54.93 support=46.05 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=76.68 liquidity=45616856.0 spike=0.4
- ADPC.CA: score=27.9 buy_ready=True sector_rank=10 price=4.51 support=3.78 resistance=4.61 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=69.03 liquidity=33361080.54 spike=0.75
- AFDI.CA: score=25.9 buy_ready=False sector_rank=10 price=62.5 support=46.57 resistance=69.89 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=70.43 liquidity=20964375.0 spike=0.93
- AFMC.CA: score=25.9 buy_ready=False sector_rank=10 price=247.89 support=97.0 resistance=300.0 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=73.3 liquidity=82084807.06 spike=0.51
- AJWA.CA: score=29.38 buy_ready=True sector_rank=10 price=197.36 support=161.0 resistance=210.0 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=64.2 liquidity=68044202.13 spike=1.74
- ALCN.CA: score=25.5 buy_ready=False sector_rank=17 price=30.63 support=28.8 resistance=32.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=73.08 liquidity=14409115.0 spike=0.59
- ALUM.CA: score=23.02 buy_ready=False sector_rank=10 price=28.42 support=22.72 resistance=30.6 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=79.87 liquidity=19634241.25 spike=1.06
- AMER.CA: score=10.61 buy_ready=False sector_rank=16 price=6.41 support=6.3 resistance=6.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40627904.0 spike=0.34
- AMES.CA: score=25.9 buy_ready=True sector_rank=10 price=120.37 support=106.59 resistance=136.99 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=42.22 liquidity=11199225.06 spike=0.3
- AMIA.CA: score=29.9 buy_ready=False sector_rank=10 price=15.24 support=9.41 resistance=15.24 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=92.81 liquidity=156226761.65 spike=7.77
- AMOC.CA: score=27.16 buy_ready=False sector_rank=9 price=11.89 support=8.16 resistance=11.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=87.17 liquidity=248612608.0 spike=2.13
- APSW.CA: score=20.09 buy_ready=True sector_rank=10 price=9.12 support=8.5 resistance=9.39 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=56.14 liquidity=1794578.86 spike=1.2
- ARAB.CA: score=23.61 buy_ready=False sector_rank=16 price=0.24 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.12 liquidity=42107304.0 spike=0.41
- ARCC.CA: score=22.8 buy_ready=False sector_rank=15 price=73.63 support=55.26 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=83.43 liquidity=62527880.0 spike=0.65
- AREH.CA: score=23.54 buy_ready=False sector_rank=10 price=1.53 support=1.38 resistance=1.68 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=59.09 liquidity=37594521.29 spike=1.32
- ARVA.CA: score=11.9 buy_ready=False sector_rank=10 price=12.35 support=10.75 resistance=12.6 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ASCM.CA: score=23.9 buy_ready=False sector_rank=10 price=63.95 support=60.1 resistance=69.95 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=50.71 liquidity=38727097.26 spike=0.72
- ASPI.CA: score=27.9 buy_ready=False sector_rank=10 price=0.55 support=0.34 resistance=0.56 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=70.83 liquidity=33859362.53 spike=0.9
- ATLC.CA: score=27.38 buy_ready=True sector_rank=18 price=5.39 support=5.0 resistance=5.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.94 liquidity=20355936.0 spike=1.05
- ATQA.CA: score=30.14 buy_ready=False sector_rank=7 price=11.3 support=9.56 resistance=11.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=73.85 liquidity=129316304.0 spike=2.12
- AXPH.CA: score=20.76 buy_ready=True sector_rank=10 price=1344.57 support=1121.56 resistance=1460.0 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=66.87 liquidity=2862589.42 spike=0.76
- BINV.CA: score=17.94 buy_ready=False sector_rank=12 price=47.97 support=46.01 resistance=50.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=60.09 liquidity=4044292.5 spike=0.58
- BIOC.CA: score=24.34 buy_ready=False sector_rank=10 price=507.0 support=106.61 resistance=563.99 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=81.17 liquidity=379465164.0 spike=1.72
- BTFH.CA: score=23.28 buy_ready=False sector_rank=18 price=3.09 support=3.05 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.22 liquidity=159683856.0 spike=0.7
- CAED.CA: score=25.9 buy_ready=True sector_rank=10 price=129.15 support=114.01 resistance=143.0 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=50.79 liquidity=17029459.9 spike=0.45
- CANA.CA: score=25.9 buy_ready=False sector_rank=4 price=42.36 support=35.2 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=72.3 liquidity=10199598.0 spike=0.45
- CCAP.CA: score=28.7 buy_ready=True sector_rank=12 price=5.51 support=5.14 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=1350049792.0 spike=2.4
- CCRS.CA: score=25.14 buy_ready=False sector_rank=10 price=2.5 support=2.44 resistance=2.76 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=42.86 liquidity=24720460.0 spike=1.62
- CEFM.CA: score=19.9 buy_ready=True sector_rank=10 price=135.08 support=108.01 resistance=147.0 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=61.65 liquidity=3996612.01 spike=0.14
- CERA.CA: score=23.9 buy_ready=False sector_rank=10 price=1.31 support=1.25 resistance=1.39 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=42.86 liquidity=11050336.84 spike=0.87
- CFGH.CA: score=19.97 buy_ready=False sector_rank=10 price=0.11 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=68.42 liquidity=68292.5 spike=4.57
- CICH.CA: score=14.94 buy_ready=True sector_rank=18 price=12.65 support=11.8 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=66.26 liquidity=1667798.25 spike=0.22
- CIEB.CA: score=32.9 buy_ready=True sector_rank=4 price=25.11 support=23.75 resistance=24.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.56 liquidity=43842300.0 spike=3.63
- CIRA.CA: score=26.9 buy_ready=True sector_rank=3 price=38.0 support=31.0 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.3 liquidity=48964744.0 spike=0.8
- CLHO.CA: score=23.9 buy_ready=False sector_rank=6 price=17.2 support=16.0 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.47 liquidity=43968496.0 spike=0.8
- CNFN.CA: score=26.6 buy_ready=True sector_rank=18 price=4.92 support=4.68 resistance=5.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=32696544.0 spike=1.66
- COMI.CA: score=23.9 buy_ready=False sector_rank=4 price=138.43 support=133.81 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.27 liquidity=377663776.0 spike=0.86
- COPR.CA: score=31.64 buy_ready=True sector_rank=10 price=0.44 support=0.37 resistance=0.46 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=61.63 liquidity=66959596.79 spike=1.87
- COSG.CA: score=27.94 buy_ready=True sector_rank=10 price=1.8 support=1.6 resistance=1.93 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=62.79 liquidity=42888271.26 spike=1.02
- CPCI.CA: score=21.37 buy_ready=False sector_rank=10 price=538.84 support=440.01 resistance=644.0 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=72.45 liquidity=5467070.91 spike=0.74
- CSAG.CA: score=10.5 buy_ready=False sector_rank=17 price=39.34 support=39.12 resistance=41.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20758442.0 spike=0.82
- DAPH.CA: score=24.9 buy_ready=False sector_rank=10 price=130.4 support=84.31 resistance=147.0 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=84.02 liquidity=22890675.73 spike=0.6
- DEIN.CA: score=13.9 buy_ready=False sector_rank=10 price=10.35 support=10.35 resistance=10.35 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=23.3 buy_ready=True sector_rank=13 price=28.9 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=66.25 liquidity=7403666.5 spike=0.51
- DSCW.CA: score=23.94 buy_ready=False sector_rank=10 price=2.03 support=1.89 resistance=2.21 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=55.32 liquidity=81803122.0 spike=1.02
- DTPP.CA: score=25.9 buy_ready=True sector_rank=10 price=294.66 support=222.0 resistance=340.0 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=69.47 liquidity=33709988.4 spike=0.67
- EALR.CA: score=29.9 buy_ready=False sector_rank=10 price=456.01 support=360.0 resistance=471.18 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=77.21 liquidity=222588061.98 spike=5.24
- EASB.CA: score=27.26 buy_ready=True sector_rank=10 price=7.47 support=6.71 resistance=8.52 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=40.87 liquidity=13884989.1 spike=1.68
- EAST.CA: score=21.9 buy_ready=False sector_rank=13 price=36.44 support=36.01 resistance=37.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=58.64 liquidity=27772774.0 spike=0.42
- EBSC.CA: score=18.41 buy_ready=True sector_rank=10 price=1.93 support=1.85 resistance=2.06 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=53.57 liquidity=2510358.65 spike=0.53
- ECAP.CA: score=26.44 buy_ready=False sector_rank=10 price=39.3 support=32.12 resistance=43.5 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=70.83 liquidity=14469984.62 spike=1.27
- EDFM.CA: score=14.14 buy_ready=False sector_rank=10 price=411.42 support=352.0 resistance=430.0 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=80.45 liquidity=1237551.4 spike=0.26
- EEII.CA: score=25.9 buy_ready=True sector_rank=10 price=3.05 support=2.54 resistance=3.23 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=66.34 liquidity=13595097.24 spike=0.77
- EFIC.CA: score=28.46 buy_ready=False sector_rank=7 price=227.0 support=184.0 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=80.94 liquidity=112187416.0 spike=2.78
- EFID.CA: score=24.9 buy_ready=False sector_rank=13 price=33.02 support=26.64 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=91.7 liquidity=26690406.0 spike=0.29
- EFIH.CA: score=27.9 buy_ready=False sector_rank=8 price=24.56 support=22.04 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=72.76 liquidity=57691064.0 spike=0.52
- EGAL.CA: score=25.16 buy_ready=False sector_rank=7 price=346.09 support=292.0 resistance=359.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=83.45 liquidity=115792280.0 spike=1.13
- EGAS.CA: score=22.9 buy_ready=False sector_rank=9 price=59.58 support=50.0 resistance=67.7 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=76.57 liquidity=10933466.56 spike=0.47
- EGBE.CA: score=17.06 buy_ready=False sector_rank=4 price=0.52 support=0.46 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=65.7 liquidity=398400.72 spike=2.38
- EGCH.CA: score=25.9 buy_ready=False sector_rank=7 price=14.2 support=12.69 resistance=14.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.72 liquidity=65481024.0 spike=0.56
- EGSA.CA: score=5.91 buy_ready=False sector_rank=14 price=8.7 support=8.65 resistance=9.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=23.81 liquidity=10214.45 spike=0.48
- EGTS.CA: score=27.61 buy_ready=True sector_rank=16 price=18.33 support=17.11 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.02 liquidity=26391860.0 spike=0.65
- EHDR.CA: score=29.9 buy_ready=True sector_rank=10 price=3.14 support=2.71 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.77 liquidity=30341226.0 spike=0.62
- EKHO.CA: score=11.9 buy_ready=False sector_rank=9 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=25.9 buy_ready=False sector_rank=1 price=2.18 support=2.12 resistance=2.28 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=43.75 liquidity=43164151.74 spike=0.94
- ELKA.CA: score=18.9 buy_ready=False sector_rank=10 price=1.74 support=1.69 resistance=2.25 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=31.25 liquidity=31838344.43 spike=0.49
- ELNA.CA: score=7.03 buy_ready=False sector_rank=10 price=37.67 support=36.5 resistance=39.49 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=22.03 liquidity=126081.48 spike=0.31
- ELSH.CA: score=23.9 buy_ready=False sector_rank=10 price=13.74 support=13.31 resistance=15.59 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=35.69 liquidity=27847558.28 spike=0.39
- ELWA.CA: score=8.41 buy_ready=False sector_rank=10 price=1.73 support=1.65 resistance=2.03 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=34.37 liquidity=505573.48 spike=0.41
- EMFD.CA: score=21.53 buy_ready=False sector_rank=16 price=11.6 support=11.08 resistance=12.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=83843168.0 spike=1.46
- ENGC.CA: score=29.18 buy_ready=False sector_rank=10 price=51.2 support=40.11 resistance=54.79 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=75.11 liquidity=82158337.22 spike=3.14
- EOSB.CA: score=17.91 buy_ready=False sector_rank=10 price=1.55 support=1.53 resistance=1.62 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=11325.85 spike=0.25
- EPCO.CA: score=27.9 buy_ready=True sector_rank=10 price=11.95 support=10.32 resistance=13.05 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=62.02 liquidity=20228684.83 spike=0.94
- EPPK.CA: score=8.68 buy_ready=False sector_rank=10 price=13.0 support=12.62 resistance=15.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=20.55 liquidity=1502683.75 spike=1.64
- ETEL.CA: score=29.9 buy_ready=True sector_rank=14 price=116.75 support=97.54 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.24 liquidity=100565680.0 spike=0.77
- ETRS.CA: score=25.46 buy_ready=False sector_rank=10 price=11.36 support=10.21 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=87.5 liquidity=37301804.0 spike=1.28
- EXPA.CA: score=22.9 buy_ready=False sector_rank=4 price=21.05 support=19.43 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.91 liquidity=20535562.0 spike=0.56
- FAIT.CA: score=20.19 buy_ready=False sector_rank=4 price=42.56 support=36.1 resistance=42.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=91.07 liquidity=4810883.0 spike=1.24
- FAITA.CA: score=25.08 buy_ready=False sector_rank=4 price=0.99 support=0.96 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=63.53 liquidity=177889.0 spike=3.68
- FERC.CA: score=26.42 buy_ready=False sector_rank=7 price=77.5 support=75.01 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.86 liquidity=26378694.0 spike=1.76
- FWRY.CA: score=25.9 buy_ready=True sector_rank=8 price=19.12 support=18.69 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.8 liquidity=42721144.0 spike=0.33
- GBCO.CA: score=19.07 buy_ready=False sector_rank=20 price=30.25 support=29.53 resistance=33.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.75 liquidity=17543308.0 spike=0.29
- GDWA.CA: score=14.9 buy_ready=False sector_rank=10 price=0.8 support=0.8 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.3 liquidity=42298000.0 spike=0.38
- GGCC.CA: score=12.1 buy_ready=False sector_rank=10 price=0.93 support=0.91 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=80575528.0 spike=1.6
- GIHD.CA: score=25.9 buy_ready=True sector_rank=10 price=65.53 support=49.32 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=65.1 liquidity=14053742.0 spike=0.31
- GMCI.CA: score=9.28 buy_ready=False sector_rank=10 price=1.92 support=1.88 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=31.71 liquidity=382641.44 spike=0.52
- GRCA.CA: score=23.9 buy_ready=False sector_rank=10 price=56.59 support=54.7 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.56 liquidity=12736142.0 spike=0.65
- GSSC.CA: score=28.9 buy_ready=True sector_rank=10 price=290.0 support=264.0 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=65.47 liquidity=84069776.0 spike=4.61
- GTWL.CA: score=27.4 buy_ready=False sector_rank=10 price=172.99 support=85.0 resistance=184.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=88.45 liquidity=267982848.0 spike=2.25
- HDBK.CA: score=20.9 buy_ready=False sector_rank=4 price=92.86 support=77.03 resistance=91.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=95.69 liquidity=31776024.0 spike=0.8
- HELI.CA: score=23.61 buy_ready=False sector_rank=16 price=7.52 support=7.56 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.06 liquidity=148486352.0 spike=0.86
- HRHO.CA: score=19.28 buy_ready=False sector_rank=18 price=26.51 support=25.95 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.16 liquidity=67542896.0 spike=0.71
- ICID.CA: score=15.9 buy_ready=False sector_rank=10 price=15.72 support=14.5 resistance=16.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=90799568.0 spike=5.61
- IDRE.CA: score=24.93 buy_ready=True sector_rank=10 price=55.52 support=44.52 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=69.56 liquidity=9031981.0 spike=0.31
- IFAP.CA: score=27.9 buy_ready=True sector_rank=5 price=20.78 support=18.96 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=63.19 liquidity=15472299.0 spike=0.64
- INFI.CA: score=22.9 buy_ready=False sector_rank=10 price=156.39 support=103.32 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.0 liquidity=36702184.0 spike=0.63
- IRON.CA: score=27.98 buy_ready=True sector_rank=7 price=32.9 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=53.39 liquidity=23434104.0 spike=2.54
- ISMA.CA: score=24.9 buy_ready=False sector_rank=10 price=35.8 support=27.27 resistance=36.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=75.51 liquidity=20589480.0 spike=0.75
- ISMQ.CA: score=25.9 buy_ready=True sector_rank=7 price=9.43 support=8.96 resistance=9.97 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=48.74 liquidity=32013794.88 spike=0.62
- ISPH.CA: score=25.9 buy_ready=True sector_rank=6 price=13.2 support=11.3 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=68.42 liquidity=77328768.0 spike=0.41
- JUFO.CA: score=19.9 buy_ready=False sector_rank=13 price=27.1 support=22.78 resistance=29.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=91.13 liquidity=23130602.0 spike=0.39
- KABO.CA: score=13.72 buy_ready=False sector_rank=11 price=9.1 support=9.1 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=93324728.0 spike=2.41
- KWIN.CA: score=18.9 buy_ready=False sector_rank=10 price=88.17 support=83.99 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=20.55 liquidity=43720788.0 spike=0.74
- KZPC.CA: score=27.0 buy_ready=False sector_rank=10 price=12.21 support=8.42 resistance=13.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=93.63 liquidity=29152192.0 spike=2.05
- LCSW.CA: score=24.1 buy_ready=False sector_rank=15 price=34.38 support=30.2 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=36.32 liquidity=46611688.0 spike=1.15
- LUTS.CA: score=14.74 buy_ready=False sector_rank=10 price=1.42 support=1.2 resistance=1.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=231758560.0 spike=2.92
- MAAL.CA: score=17.59 buy_ready=False sector_rank=10 price=8.75 support=8.32 resistance=9.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.0 liquidity=3685408.25 spike=0.25
- MASR.CA: score=20.9 buy_ready=False sector_rank=10 price=7.6 support=7.45 resistance=8.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.97 liquidity=70263928.0 spike=0.94
- MBSC.CA: score=12.1 buy_ready=False sector_rank=15 price=363.86 support=361.02 resistance=408.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=115157984.0 spike=1.65
- MCQE.CA: score=11.3 buy_ready=False sector_rank=15 price=224.45 support=212.01 resistance=244.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=54066292.0 spike=1.25
- MCRO.CA: score=25.9 buy_ready=True sector_rank=10 price=1.51 support=1.32 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.78 liquidity=51218092.0 spike=0.29
- MENA.CA: score=22.25 buy_ready=True sector_rank=16 price=7.11 support=6.83 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=56.6 liquidity=4635510.0 spike=0.73
- MEPA.CA: score=23.9 buy_ready=False sector_rank=10 price=1.88 support=1.76 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=39956016.0 spike=0.63
- MFPC.CA: score=22.9 buy_ready=False sector_rank=7 price=39.49 support=35.37 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=78.18 liquidity=71694904.0 spike=0.88
- MFSC.CA: score=18.89 buy_ready=True sector_rank=10 price=49.49 support=46.0 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=56.5 liquidity=2990892.75 spike=0.25
- MHOT.CA: score=25.9 buy_ready=False sector_rank=2 price=18.66 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.3 liquidity=16154453.0 spike=0.97
- MICH.CA: score=14.82 buy_ready=False sector_rank=10 price=50.18 support=48.0 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=99755168.0 spike=2.96
- MILS.CA: score=15.9 buy_ready=False sector_rank=10 price=229.62 support=192.22 resistance=229.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=296529024.0 spike=4.97
- MIPH.CA: score=16.47 buy_ready=False sector_rank=6 price=775.8 support=722.7 resistance=828.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=60.28 liquidity=567147.69 spike=0.12
- MOED.CA: score=15.9 buy_ready=False sector_rank=10 price=0.73 support=0.69 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=204489312.0 spike=6.11
- MOIL.CA: score=16.11 buy_ready=False sector_rank=9 price=0.66 support=0.55 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.06 liquidity=212201.28 spike=0.35
- MOIN.CA: score=24.9 buy_ready=False sector_rank=10 price=36.51 support=23.11 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=82.64 liquidity=26890648.0 spike=0.97
- MOSC.CA: score=24.9 buy_ready=False sector_rank=10 price=331.52 support=282.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=90.23 liquidity=12289776.0 spike=0.81
- MPCI.CA: score=25.96 buy_ready=False sector_rank=10 price=377.0 support=248.25 resistance=460.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.04 liquidity=161899536.0 spike=1.03
- MPCO.CA: score=25.9 buy_ready=True sector_rank=5 price=2.12 support=1.82 resistance=2.3 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=67.27 liquidity=55293478.74 spike=0.61
- MPRC.CA: score=24.1 buy_ready=False sector_rank=10 price=44.0 support=43.02 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.54 liquidity=29644448.0 spike=1.1
- MTIE.CA: score=23.37 buy_ready=False sector_rank=20 price=8.97 support=8.01 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=106221112.0 spike=2.15
- NAHO.CA: score=6.22 buy_ready=False sector_rank=10 price=0.15 support=0.14 resistance=0.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=317487.69 spike=5.64
- NCCW.CA: score=20.9 buy_ready=False sector_rank=10 price=6.05 support=5.67 resistance=7.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.35 liquidity=30216448.0 spike=0.9
- NEDA.CA: score=26.54 buy_ready=True sector_rank=10 price=2.95 support=2.7 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=64.29 liquidity=3644100.25 spike=4.42
- NHPS.CA: score=25.9 buy_ready=True sector_rank=10 price=89.84 support=82.25 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.72 liquidity=25789828.0 spike=0.43
- NINH.CA: score=23.9 buy_ready=False sector_rank=10 price=21.64 support=20.85 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.68 liquidity=13527693.0 spike=0.25
- NIPH.CA: score=25.9 buy_ready=False sector_rank=6 price=368.55 support=194.0 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=73.38 liquidity=187507840.0 spike=0.63
- OBRI.CA: score=26.66 buy_ready=False sector_rank=10 price=34.07 support=31.61 resistance=36.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.46 liquidity=62501756.0 spike=1.88
- OCDI.CA: score=25.61 buy_ready=False sector_rank=16 price=33.94 support=26.6 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=72.64 liquidity=73090976.0 spike=0.53
- OCPH.CA: score=20.9 buy_ready=False sector_rank=10 price=263.61 support=225.0 resistance=500.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.25 liquidity=10920870.0 spike=0.31
- ODIN.CA: score=12.36 buy_ready=False sector_rank=10 price=3.54 support=3.34 resistance=3.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=63761920.0 spike=1.73
- OFH.CA: score=22.9 buy_ready=False sector_rank=10 price=0.91 support=0.69 resistance=0.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.76 liquidity=58629244.0 spike=0.62
- OIH.CA: score=22.9 buy_ready=False sector_rank=12 price=1.82 support=1.41 resistance=1.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=80.43 liquidity=110440744.0 spike=0.98
- OLFI.CA: score=27.9 buy_ready=True sector_rank=13 price=25.0 support=22.25 resistance=26.52 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=63.46 liquidity=20920150.0 spike=0.35
- ORAS.CA: score=9.1 buy_ready=False sector_rank=19 price=761.16 support=750.01 resistance=768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=116998264.0 spike=1.0
- ORHD.CA: score=26.29 buy_ready=False sector_rank=16 price=41.6 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=70.43 liquidity=220414288.0 spike=1.34
- ORWE.CA: score=25.9 buy_ready=False sector_rank=11 price=25.79 support=22.55 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.82 liquidity=25445636.0 spike=0.33
- PHAR.CA: score=25.9 buy_ready=True sector_rank=6 price=134.2 support=89.1 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.6 liquidity=256337168.0 spike=0.62
- PHDC.CA: score=27.31 buy_ready=False sector_rank=16 price=15.38 support=14.32 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=77.27 liquidity=564179840.0 spike=2.35
- PHTV.CA: score=27.71 buy_ready=True sector_rank=10 price=367.95 support=296.96 resistance=447.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=61.81 liquidity=6753714.5 spike=2.53
- POUL.CA: score=22.9 buy_ready=False sector_rank=13 price=37.59 support=36.5 resistance=40.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=19209168.0 spike=0.69
- PRCL.CA: score=23.8 buy_ready=False sector_rank=15 price=35.25 support=32.8 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.46 liquidity=16858762.0 spike=0.44
- PRDC.CA: score=23.61 buy_ready=False sector_rank=16 price=8.83 support=8.7 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.54 liquidity=19204358.0 spike=0.19
- PRMH.CA: score=18.73 buy_ready=False sector_rank=10 price=2.56 support=2.56 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.59 liquidity=7833417.5 spike=0.61
- RACC.CA: score=29.9 buy_ready=True sector_rank=10 price=10.46 support=9.8 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.83 liquidity=15967555.0 spike=0.82
- RAKT.CA: score=10.89 buy_ready=False sector_rank=10 price=22.23 support=21.66 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=369719.5 spike=1.31
- RAYA.CA: score=17.88 buy_ready=False sector_rank=21 price=7.15 support=6.97 resistance=7.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.76 liquidity=42506184.0 spike=0.44
- RMDA.CA: score=25.9 buy_ready=False sector_rank=6 price=6.22 support=4.95 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=73.88 liquidity=43686788.0 spike=0.37
- ROTO.CA: score=22.9 buy_ready=False sector_rank=10 price=51.22 support=40.99 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.76 liquidity=19511696.0 spike=0.81
- RREI.CA: score=11.2 buy_ready=False sector_rank=10 price=4.9 support=4.63 resistance=4.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=73124736.0 spike=1.15
- RTVC.CA: score=29.46 buy_ready=True sector_rank=10 price=3.97 support=3.73 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.21 liquidity=14976248.0 spike=2.78
- RUBX.CA: score=25.9 buy_ready=True sector_rank=10 price=12.9 support=12.02 resistance=14.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=53.61 liquidity=22391732.0 spike=0.65
- SAUD.CA: score=29.24 buy_ready=False sector_rank=4 price=23.72 support=21.4 resistance=23.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=70.1 liquidity=47191772.0 spike=2.67
- SCEM.CA: score=29.7 buy_ready=True sector_rank=15 price=102.5 support=66.75 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.2 liquidity=348278624.0 spike=1.95
- SCFM.CA: score=28.4 buy_ready=True sector_rank=10 price=295.12 support=258.0 resistance=319.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.37 liquidity=57365408.0 spike=2.25
- SCTS.CA: score=33.9 buy_ready=True sector_rank=3 price=617.0 support=602.01 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=56.73 liquidity=38916452.0 spike=4.55
- SDTI.CA: score=25.9 buy_ready=False sector_rank=10 price=70.82 support=46.6 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=73.84 liquidity=15419446.0 spike=0.54
- SEIG.CA: score=12.91 buy_ready=False sector_rank=10 price=271.73 support=237.0 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=77.23 liquidity=2013269.25 spike=0.16
- SIPC.CA: score=24.9 buy_ready=False sector_rank=10 price=5.05 support=3.76 resistance=5.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.23 liquidity=45047488.0 spike=0.7
- SKPC.CA: score=26.9 buy_ready=True sector_rank=7 price=16.88 support=15.61 resistance=17.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.64 liquidity=38093352.0 spike=0.77
- SMFR.CA: score=22.47 buy_ready=True sector_rank=10 price=261.94 support=225.0 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.95 liquidity=6573742.5 spike=0.16
- SNFC.CA: score=18.92 buy_ready=False sector_rank=10 price=10.94 support=10.6 resistance=11.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.54 liquidity=6016727.5 spike=0.48
- SPIN.CA: score=25.28 buy_ready=False sector_rank=11 price=20.2 support=14.57 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=83.28 liquidity=47186384.0 spike=1.19
- SPMD.CA: score=23.9 buy_ready=False sector_rank=10 price=0.47 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.47 liquidity=12237112.0 spike=0.36
- SUGR.CA: score=28.12 buy_ready=False sector_rank=13 price=51.06 support=46.47 resistance=51.98 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=80.34 liquidity=37993798.08 spike=2.61
- SVCE.CA: score=25.9 buy_ready=False sector_rank=10 price=10.82 support=9.06 resistance=12.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.85 liquidity=47301316.0 spike=0.49
- SWDY.CA: score=32.9 buy_ready=False sector_rank=1 price=128.15 support=91.01 resistance=125.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=80.65 liquidity=347445280.0 spike=4.9
- TALM.CA: score=25.9 buy_ready=False sector_rank=3 price=19.59 support=15.65 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=76.61 liquidity=27776514.0 spike=0.65
- TMGH.CA: score=20.61 buy_ready=False sector_rank=16 price=96.44 support=95.2 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.65 liquidity=164146768.0 spike=0.47
- TRTO.CA: score=24.94 buy_ready=False sector_rank=10 price=0.05 support=0.03 resistance=0.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37068.59 spike=5.05
- UEFM.CA: score=17.34 buy_ready=False sector_rank=10 price=544.63 support=520.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.38 liquidity=3441298.5 spike=0.54
- UEGC.CA: score=10.9 buy_ready=False sector_rank=10 price=2.25 support=2.23 resistance=2.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=38244216.0 spike=0.87
- UNIP.CA: score=25.92 buy_ready=False sector_rank=10 price=0.4 support=0.37 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.44 liquidity=64867924.0 spike=2.01
- UNIT.CA: score=19.46 buy_ready=True sector_rank=16 price=18.78 support=17.32 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=55.99 liquidity=1846570.25 spike=0.13
- WCDF.CA: score=16.39 buy_ready=False sector_rank=10 price=644.63 support=523.3 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=80.01 liquidity=3486075.5 spike=0.71
- WKOL.CA: score=12.86 buy_ready=False sector_rank=10 price=345.25 support=341.0 resistance=372.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=59240780.0 spike=1.98
- ZEOT.CA: score=24.9 buy_ready=False sector_rank=10 price=14.27 support=11.51 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=75.25 liquidity=21051106.0 spike=0.72
- ZMID.CA: score=25.61 buy_ready=True sector_rank=16 price=7.45 support=7.06 resistance=7.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=118194968.0 spike=0.51

## Backtesting Lite
- SCTS.CA: 180d return=89.9%, max drawdown=-21.39%, MA20>MA50 days last20=15, as_of=2026-08-16T21:00:00+00:00
- CIEB.CA: 180d return=30.08%, max drawdown=-19.11%, MA20>MA50 days last20=20, as_of=2026-08-16T21:00:00+00:00
- SWDY.CA: 180d return=62.35%, max drawdown=-14.67%, MA20>MA50 days last20=20, as_of=2026-08-16T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- SCTS.CA: status=RECENT_ACCEPTED latest=2026-07-14 age_days=35 sources=3 expected=Suez Canal Company for Technology Settling summary=Suez Canal Company for Technology Settling (SCTS.CA) has released its Q3 2026 earnings, showing increased net income and profit margin. The company also announced cash dividends and several board and general assembly decisions in the past year. Investor sentiment has improved, with the stock rising 15% in early July 2026.
  - Third Quarter 2026 Earnings Released (July 14, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE14jddN-myiJJDDuHxz4qvgCAoImGP9aKiLRG8yrLyUgd5nW_Tf9d8lAE8VrSo1BjcOkGFdrP1PZ0_piiYVvaEQB8EdvorblYkePb5paSHM6_SWy8uTk8W11wyGUfH
  - Investor Sentiment Improves as Stock Rises 15% (July 04, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE14jddN-myiJJDDuHxz4qvgCAoImGP9aKiLRG8yrLyUgd5nW_Tf9d8lAE8VrSo1BjcOkGFdrP1PZ0_piiYVvaEQB8EdvorblYkePb5paSHM6_SWy8uTk8W11wyGUfH
  - Consolidated Financial Statements for Fiscal Period Ending 31/05/2026 (Announced July 12, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUfh9mbXPEuqGy8--EbSr3tDE_54B-rdmwCX9MG4ucVCs8J33nRZzQAbKMEG58Nv6H-ZJ23bpiFvzL5sQLAC2M9NA-DJH_oG-uO6u5gIEnwZMEKO57YaKkvV-reMDctH17zShzcP3m4Oj6PpzXK2yhmw8dykbaX8e9Gnw6Rg==
- CIEB.CA: status=RECENT_ACCEPTED latest=2026-07-30 age_days=19 sources=3 expected=Credit Agricole Egypt summary=Credit Agricole Egypt (CIEB.CA) has been active with several board and financial announcements in mid-2026. The bank reported its Q1 2026 consolidated profits exceeding EGP 1.7bn and plans to disburse EGP 4.1bn in dividends for 2025. However, its 2025 financial performance showed a decrease in revenue and earnings.
  - Release Regarding Board of Directors & Executive Managers (Announced July 30, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy-H1c9lenasY3Iw9sD3pZVZQUcDM8sZV1i_8URnobqqNOGd6UWimPULDSsG7sP9mr0nIvSOvUW0tIXCBZZpHG_OQ-eGKO1i8o3-6j4Zirw1ZhJUOYmYz9jitUgqH-JVrjj21xBSGXO-OXU3HorYWE5A==
  - Release Regarding Financial Results (Announced July 29, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUSOCrLpsfOY9ONoW5twZTPQPihYDsvwZ3xAKldLtx18aWUnG-GvueHO9KkQR0NmZnR2gxnhlUYjubyMCnJnbK2XFTf0GhA69jkXK3jehD5Y_UpuYzYz97HM6zJeUBV5iGWfzaJXvyl8dInwsfWcM=
  - Decisions of the Board of Directors' Meeting (Announced July 29, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUSOCrLpsfOY9ONoW5twZTPQPihYDsvwZ3xAKldLtx18aWUnG-GvueHO9KkQR0NmZnR2gxnhlUYjubyMCnJnbK2XFTf0GhA69jkXK3jehD5Y_UpuYzYz97HM6zJeUBV5iGWfzaJXvyl8dInwsfWcM=
- SWDY.CA: status=RECENT_ACCEPTED latest=2026-06-04 age_days=75 sources=3 expected=Elsewedy Electric summary=Elsewedy Electric (SWDY.CA) has seen significant financial growth in FY 2024, with revenues surging by 52.4% and net profit rising by 72.6%. The company also announced a substantial project award for its subsidiary in Qatar and declared dividends payable in June 2026. Various quarterly and annual financial reports from 2025 and 2024 are available.
  - El Sewedy Cable Qatar Subsidiary Receives Provisional Letter of Award for Project Exceeding USD 328 Million (Recent EGX announcement): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFZiSQH1wpHyNh1COE30Edd48c7V5pAi1YWqv4vg2tAQCxmV_8NbL098mJqn5PidTZHuJIKU8sDL8noZrZ4AMZMYywFtthM7KQ0geglT4PgUCkgqSwGf8pu99GMbVA-X5V9zQJ_QqsmtbDPMpj
  - FY 2024 Financial Highlights: Revenue Up 52.4%, Net Profit Up 72.6% (Reported early 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQ98hryEOyKhB3kPkQ0HH9jqjt6xQqAt2vkfqQ9bATYaXYLSs6WuY411-6qLW_9KdP9LojT_5NnL-FsFs8q_rbLR2PrdXM1ml0zlNksECqQDASjpWYtsZ6jhxM5xy9rxV4TJgn6aLWMt2ZdueprtARBwWswmi1sZYW91k
  - Dividend Declared: EGP 1.85, Ex-Dividend Date June 02, 2026, Payment Date June 04, 2026: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzjcT2msVWtB24UcpvaQexqZeFpycVbNp9IPRm1hYmDkH9zD71UHXEr55OBtTssiq1jCpdlFf0Qk84q7Bh3xQ9iRMEutZzazJ-WpMUOx1bnVDgoNJ8T8DSCWXOZYvMWmhYhVRfVrKVd6G1
- COPR.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Copper for Commercial Investment & Real Estate Development summary=Copper for Commercial Investment swings to EGP 7m net losses in 9M-25; NRPD’s EGM approves capital cut, increase; Two shareholders sell entire stakes in NRPD Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Copper for Commercial Investment swings to EGP 7m net losses in 9M-25: https://english.mubasher.info/news/4530417/Copper-for-Commercial-Investment-swings-to-EGP-7m-net-losses-in-9M-25/
  - NRPD’s EGM approves capital cut, increase: https://english.mubasher.info/news/4042300/NRPD-s-EGM-approves-capital-cut-increase/
  - Two shareholders sell entire stakes in NRPD: https://english.mubasher.info/news/4006432/Two-shareholders-sell-entire-stakes-in-NRPD/
- ATQA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr National Steel Ataqa summary=Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- ETEL.CA: status=RECENT_ACCEPTED latest=2026-08-13 age_days=5 sources=3 expected=Telecom Egypt summary=Telecom Egypt (ETEL.CA) has been actively reporting financial results and corporate decisions. The company announced improved profitability in H1 2026 and decided not to proceed with a proposed transaction for its Regional Data Center Hub. They also provided 2026 financial guidance and announced dividend payments.
  - Q2 2026 Results: Telecom Egypt Reports Improved Profitability and Efficiency in H1 2026 (Announced August 13, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkgP8joccsAG-04ee4L5J0zCJP2xVzjTdH4O3x-Yt3YFFaz0m7n74obaMbAwGPeYoLgsSnmbEu_JAGAEu5eVshtUiEhHqjdHapEQ==
  - Telecom Egypt Announces It Will Not Proceed with Proposed RDH Transaction with Helios Investments (Announced July 16, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkgP8joccsAG-04ee4L5J0zCJP2xVzjTdH4O3x-Yt3YFFaz0m7n74obaMbAwGPeYoLgsSnmbEu_JAGAEu5eVshtUiEhHqjdHapEQ==
  - Telecom Egypt Company to Report Q2, 2026 Results on Aug 13, 2026 (Announced July 30, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1t9cHi8LPjV9xyVyPRfaEhmH-oKcloESn1HHK3shGAUNFCIQ8snWabD4FdwA0NWuzSsS-tTEUbzCsVJiJ_rNshelAYRowurv3AC_HtB-FBhJFm5G8AUwLSJWwOR8E
- EHDR.CA: status=RECENT_ACCEPTED latest=2026-07-30 age_days=19 sources=3 expected=Egyptians for Housing & Development Co. summary=Egyptians for Housing & Development Co. (EHDR.CA) has released several disclosure forms and board decisions in mid-2026. The company's 2025 financial performance showed increases in both revenue and earnings, and it plans to disburse dividends for 2025.
  - Release Concerning Semi-Annual Disclosure Form for Capital Increase Proceeds (Recent EGX announcement): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6Ss_L6YXyIbjqbcCEFBfpO5T-zRglPP1E3gOaAN63R5tLKVUNeWLmJyqaMcWmGgKMhEGJpP016NLUsqZzaZ6owzQD7cdSI6lRW4ppQUKAKb2aOMi7y-RvwTEbGqi53DqCY482P6k01xSgUrOqXmH8kA==
  - Release Regarding a Disclosure Form (Announced July 30, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKipEDtL7TFxeSbrGDlsCfOFTvcTV4OnflT-9pYEhtf94UuFwTXb4Kwzai_ZTavX_tPjVOGvXhNqxu5RmLXJ6ncqrL34_s4YssA1Maix62Riz0--qokmI8I65LzB94rDSFL4wDgpK6Ngqh32cGfXY=
  - Disclosure Form for the Board of Directors & Shareholders' Structure (Announced July 16, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKipEDtL7TFxeSbrGDlsCfOFTvcTV4OnflT-9pYEhtf94UuFwTXb4Kwzai_ZTavX_tPjVOGvXhNqxu5R5mLXJ6ncqrL34_s4YssA1Maix62Riz0--qokmI8I65LzB94rDSFL4wDgpK6Ngqh32cGfXY=
- AALR.CA: status=RECENT_ACCEPTED latest=2026-03-31 age_days=140 sources=3 expected=General Company For Land Reclamation, Development & Reconstruction summary=General Company For Land Reclamation, Development & Reconstruction (AALR.CA) has provided its response to the Central Auditing Organization's report for the period ending September 2025. The company also submitted its disclosure form for the Board of Directors and shareholders' structure for Q2 2026 and has recent cash flow statements and 12-month financial performance data available.
  - Company's Response to Central Auditing Organization's Report on Financial Period Ending 30/09/2025 (Announced February 22, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8gHJks9WO02qIRMnejp2HNX2Ktct8vITM4ydS_m-o8308eAnvGW27puc1YayngwbV4oWb_6LL2jFrSyqF03mGeDIlM_gkxDbBQh0pqYTLb3GCQFSSDgQrs_9EYwI67zPbSbcK9yFj0wo_XPgEUKegig==
  - Disclosure Form for Board of Directors & Shareholders' Structure for Period on 30/06/2026 (Recent EGX announcement): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEUGD7Re0bAlISFc-SKe62alJ1eSseHJXdUsaFxQQ3eAJa852gfkRnka9soJiE_7N2g1Nc7C_yJSHNjOSiNOjEjVrjU_M2qmmE06nclM2swa3n0eZVSoqSirDeo3PTs6EEZ3B8hcfTaSPfyb5KQKUGdg==
  - Detailed Annual and Quarterly Cash Flow Statements (As of March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6fLctHnEp1K7NR4h7hc_6cjRn7deQrn7LY3lJxtWOAUyjUscmmY88ARRWwnlhquT9eCQguZg8y5o1ayJX8FvpNXVbFyox46BciH6wpwVFVeMnfri6HwZw-uLvE-Ku_ywY8O92KJ0vyJl4H5d4ymP47JWiSE5O6C4wat9WssBDfw8==

## Warnings
- Evidence for COPR.CA matches the company but no source/report date was detected.
- Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
