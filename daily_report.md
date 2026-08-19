# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-08-19T06:03:49.511745+00:00
Generated Cairo: 2026-08-19 09:03
Run timing: target 08:45 Cairo | generated Cairo 2026-08-19 09:03 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-08-19 09:00

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 45
- Data quality issues: 1
- Tradeable price/liquidity tickers: 162/189
- Top sector: Industrial Goods & Cables

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, August 18
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 65.0% / above MA50 70.0%
- EGX70 regime: BULLISH / above MA20 67.65% / above MA50 85.29%
- Sector breadth: 61.9%
- Risk mode: BROAD_RISK_ON

## Top Liquidity
- CCAP.CA: liquidity=1350049792.0 spike=2.4 score=28.7
- PHDC.CA: liquidity=564179840.0 spike=2.35 score=27.31
- COMI.CA: liquidity=377663776.0 spike=0.86 score=23.9
- COPR.CA: liquidity=370150720.0 spike=9.59 score=15.9
- SCEM.CA: liquidity=348278624.0 spike=1.81 score=29.28

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bullish with broad risk‑on mode; the scanner highlighted a few tickets showing accumulation spikes and bullish‑watch outlook, but many exhibit overheated RSI, weak evidence, or cooling liquidity, keeping conviction low and uncertainty elevated for the next 1‑3 days.
- SCTS.CA and CIEB.CA rank highest; both have accumulation spikes and bullish‑watch outlook, yet CIEB lacks clear evidence and shows extended momentum.
- SWDY.CA and SUGR.CA display strong liquidity spikes but RSI >80, placing them well above support and near resistance, signaling overheating.
- ETEL.CA, EHDR.CA and RACC.CA offer tradeable liquidity with constructive outlooks, though liquidity is cooling and momentum remains extended.
- Sector breadth at 61.9% is led by Industrial Goods & Cables, Tourism & Leisure and Education, providing a supportive backdrop for selective picks.
- Despite the bullish index regime and broad risk‑on setting, low confidence scores and mixed technical signals mean uncertainty remains high over the short term.

## Top Liquidity Spikes
- COPR.CA: spike=9.59 liquidity=370150720.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AMIA.CA: spike=6.29 liquidity=158928352.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MOED.CA: spike=6.11 liquidity=204489312.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- NAHO.CA: spike=5.64 liquidity=317487.69 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ICID.CA: spike=5.61 liquidity=90799568.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Industrial Goods & Cables: score=13.72 5d=7.3% 20d=14.16% aboveMA50=50.0%
- #2 Tourism & Leisure: score=12.6 5d=12.24% 20d=16.25% aboveMA50=0.0%
- #3 Education: score=12.25 5d=2.75% 20d=19.55% aboveMA50=100.0%
- #4 Banking & Financials: score=10.96 5d=4.07% 20d=11.78% aboveMA50=90.0%
- #5 Healthcare: score=10.63 5d=-1.1% 20d=23.98% aboveMA50=100.0%
- #6 Basic Resources & Chemicals: score=9.76 5d=4.04% 20d=4.71% aboveMA50=100.0%
- #7 Fintech & Payments: score=9.28 5d=2.88% 20d=7.46% aboveMA50=100.0%
- #8 Energy & Petrochemicals: score=8.79 5d=0.37% 20d=17.62% aboveMA50=75.0%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- SCTS.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- IRON.CA: BULLISH_WATCH score=97.76 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- CIEB.CA: BULLISH_WATCH score=97 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- RTVC.CA: BULLISH_WATCH score=94.13 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- SCFM.CA: BULLISH_WATCH score=94.13 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- EBSC.CA: BULLISH_WATCH score=94.13 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CIRA.CA: BULLISH_WATCH score=91 liquidity=TRADEABLE sector=LEADING risk=far above support
- CCAP.CA: BULLISH_WATCH score=88.58 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- PHTV.CA: BULLISH_WATCH score=88.13 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ISMQ.CA: BULLISH_WATCH score=85.76 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling

## BUY-Ready Candidates
- SCTS.CA: rank=33.9 outlook=BULLISH_WATCH outlook_score=100 sector_rank=3 price=617.0 support=602.01 resistance=685.0 liquidity=38916452.0
- CIEB.CA: rank=32.9 outlook=BULLISH_WATCH outlook_score=97 sector_rank=4 price=25.11 support=23.75 resistance=24.9 liquidity=43842300.0
- ETEL.CA: rank=29.9 outlook=CONSTRUCTIVE outlook_score=65.28 sector_rank=12 price=116.75 support=98.0 resistance=120.0 liquidity=100565680.0
- EHDR.CA: rank=29.9 outlook=CONSTRUCTIVE outlook_score=59.13 sector_rank=13 price=3.14 support=2.71 resistance=3.2 liquidity=30341226.0
- RACC.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=76.13 sector_rank=13 price=10.46 support=9.8 resistance=10.88 liquidity=15967555.0
- RTVC.CA: rank=29.46 outlook=BULLISH_WATCH outlook_score=94.13 sector_rank=13 price=3.97 support=3.73 resistance=4.2 liquidity=14976248.0
- SCEM.CA: rank=29.28 outlook=BULLISH_WATCH outlook_score=77.39 sector_rank=15 price=102.5 support=71.25 resistance=113.0 liquidity=348278624.0
- AJWA.CA: rank=29.24 outlook=BULLISH_WATCH outlook_score=76.13 sector_rank=13 price=198.05 support=161.0 resistance=210.0 liquidity=70922768.0
- AALR.CA: rank=28.98 outlook=BULLISH_WATCH outlook_score=76.13 sector_rank=13 price=340.01 support=234.05 resistance=375.0 liquidity=150326800.0
- GSSC.CA: rank=28.9 outlook=BULLISH_WATCH outlook_score=80.13 sector_rank=13 price=290.0 support=264.0 resistance=300.0 liquidity=84069776.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=28.98 buy_ready=True sector_rank=13 price=340.01 support=234.05 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=69.9 liquidity=150326800.0 spike=2.54
- ABUK.CA: score=24.9 buy_ready=False sector_rank=6 price=77.54 support=70.6 resistance=80.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=77.93 liquidity=77286240.0 spike=0.58
- ACAMD.CA: score=20.94 buy_ready=False sector_rank=13 price=2.16 support=2.21 resistance=2.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=44.17 liquidity=59849456.0 spike=1.02
- ACGC.CA: score=13.68 buy_ready=False sector_rank=9 price=14.66 support=14.01 resistance=14.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=87696832.0 spike=2.39
- ADCI.CA: score=26.16 buy_ready=True sector_rank=13 price=293.3 support=239.0 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=61.56 liquidity=8260972.5 spike=0.36
- ADIB.CA: score=24.9 buy_ready=False sector_rank=4 price=54.93 support=46.05 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=76.68 liquidity=45616856.0 spike=0.4
- ADPC.CA: score=11.56 buy_ready=False sector_rank=13 price=4.28 support=4.25 resistance=4.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=64104284.0 spike=1.33
- AFDI.CA: score=25.9 buy_ready=False sector_rank=13 price=62.85 support=46.57 resistance=69.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=70.43 liquidity=16768737.0 spike=0.68
- AFMC.CA: score=26.08 buy_ready=False sector_rank=13 price=253.4 support=97.0 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=73.3 liquidity=179135824.0 spike=1.09
- AJWA.CA: score=29.24 buy_ready=True sector_rank=13 price=198.05 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=64.2 liquidity=70922768.0 spike=1.67
- ALCN.CA: score=25.5 buy_ready=False sector_rank=17 price=30.63 support=28.8 resistance=32.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=73.08 liquidity=14409115.0 spike=0.59
- ALUM.CA: score=22.9 buy_ready=False sector_rank=13 price=28.5 support=22.72 resistance=30.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=79.87 liquidity=14046831.0 spike=0.72
- AMER.CA: score=10.61 buy_ready=False sector_rank=16 price=6.41 support=6.3 resistance=6.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40627904.0 spike=0.34
- AMES.CA: score=15.4 buy_ready=False sector_rank=13 price=129.48 support=121.0 resistance=141.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=201668576.0 spike=3.25
- AMIA.CA: score=15.9 buy_ready=False sector_rank=13 price=16.02 support=15.44 resistance=17.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=158928352.0 spike=6.29
- AMOC.CA: score=27.16 buy_ready=False sector_rank=8 price=11.89 support=8.16 resistance=11.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=87.17 liquidity=248612608.0 spike=2.13
- APSW.CA: score=18.29 buy_ready=False sector_rank=13 price=8.74 support=8.6 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:12 PM market time freshness=DELAYED_CURRENT RSI=56.14 liquidity=3571193.25 spike=1.91
- ARAB.CA: score=23.61 buy_ready=False sector_rank=16 price=0.24 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=44.12 liquidity=42107304.0 spike=0.41
- ARCC.CA: score=22.66 buy_ready=False sector_rank=15 price=73.63 support=55.26 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=83.43 liquidity=62527880.0 spike=0.65
- AREH.CA: score=23.16 buy_ready=False sector_rank=13 price=1.54 support=1.38 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=59.09 liquidity=40065016.0 spike=1.13
- ARVA.CA: score=10.9 buy_ready=False sector_rank=13 price=13.91 support=13.83 resistance=14.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17105482.0 spike=0.31
- ASCM.CA: score=23.9 buy_ready=False sector_rank=13 price=63.39 support=60.1 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=50.71 liquidity=29150142.0 spike=0.48
- ASPI.CA: score=27.9 buy_ready=False sector_rank=13 price=0.56 support=0.34 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=70.83 liquidity=15426251.0 spike=0.34
- ATLC.CA: score=27.37 buy_ready=True sector_rank=18 price=5.39 support=5.0 resistance=5.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=61.94 liquidity=20355936.0 spike=1.05
- ATQA.CA: score=30.12 buy_ready=False sector_rank=6 price=11.3 support=9.6 resistance=11.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=73.85 liquidity=129316304.0 spike=2.11
- AXPH.CA: score=19.73 buy_ready=True sector_rank=13 price=1348.1 support=1121.56 resistance=1460.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:11 PM market time freshness=DELAYED_CURRENT RSI=66.87 liquidity=1829587.75 spike=0.42
- BINV.CA: score=17.94 buy_ready=False sector_rank=10 price=47.97 support=46.01 resistance=50.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=60.09 liquidity=4044292.5 spike=0.56
- BIOC.CA: score=22.9 buy_ready=False sector_rank=13 price=495.01 support=106.61 resistance=563.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=81.17 liquidity=106570968.0 spike=0.45
- BTFH.CA: score=23.27 buy_ready=False sector_rank=18 price=3.09 support=3.05 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=51.22 liquidity=159683856.0 spike=0.7
- CAED.CA: score=12.68 buy_ready=False sector_rank=13 price=154.94 support=131.74 resistance=154.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=132956968.0 spike=1.89
- CANA.CA: score=25.9 buy_ready=False sector_rank=4 price=42.36 support=35.2 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=72.3 liquidity=10199598.0 spike=0.45
- CCAP.CA: score=28.7 buy_ready=True sector_rank=10 price=5.51 support=5.14 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=1350049792.0 spike=2.4
- CCRS.CA: score=23.9 buy_ready=False sector_rank=13 price=2.49 support=2.44 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=11803389.0 spike=0.64
- CEFM.CA: score=26.76 buy_ready=True sector_rank=13 price=140.96 support=121.4 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=61.65 liquidity=48353372.0 spike=1.43
- CERA.CA: score=26.88 buy_ready=False sector_rank=13 price=1.3 support=1.25 resistance=1.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=51041020.0 spike=2.49
- CFGH.CA: score=19.24 buy_ready=False sector_rank=13 price=0.11 support=0.1 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=68.42 liquidity=58951.25 spike=3.14
- CICH.CA: score=14.94 buy_ready=True sector_rank=18 price=12.65 support=11.8 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=66.26 liquidity=1667798.25 spike=0.22
- CIEB.CA: score=32.9 buy_ready=True sector_rank=4 price=25.11 support=23.75 resistance=24.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=68.56 liquidity=43842300.0 spike=3.65
- CIRA.CA: score=26.9 buy_ready=True sector_rank=3 price=38.0 support=30.91 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=57.3 liquidity=48964744.0 spike=0.83
- CLHO.CA: score=23.9 buy_ready=False sector_rank=5 price=17.2 support=16.0 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=57.47 liquidity=43968496.0 spike=0.8
- CNFN.CA: score=26.59 buy_ready=True sector_rank=18 price=4.92 support=4.68 resistance=5.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=32696544.0 spike=1.66
- COMI.CA: score=23.9 buy_ready=False sector_rank=4 price=138.43 support=133.81 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=36.27 liquidity=377663776.0 spike=0.86
- COPR.CA: score=15.9 buy_ready=False sector_rank=13 price=0.52 support=0.44 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=370150720.0 spike=9.59
- COSG.CA: score=27.94 buy_ready=True sector_rank=13 price=1.81 support=1.6 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=62.79 liquidity=47390360.0 spike=1.02
- CPCI.CA: score=18.58 buy_ready=False sector_rank=13 price=535.89 support=440.01 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:12 PM market time freshness=DELAYED_CURRENT RSI=72.45 liquidity=2681242.5 spike=0.21
- CSAG.CA: score=10.5 buy_ready=False sector_rank=17 price=39.34 support=39.12 resistance=41.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20758442.0 spike=0.82
- DAPH.CA: score=24.9 buy_ready=False sector_rank=13 price=126.28 support=85.7 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=84.02 liquidity=13450449.0 spike=0.33
- DEIN.CA: score=0.9 buy_ready=False sector_rank=13 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=23.3 buy_ready=True sector_rank=11 price=28.9 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=66.25 liquidity=7403666.5 spike=0.51
- DSCW.CA: score=23.9 buy_ready=False sector_rank=13 price=1.99 support=1.89 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=55.32 liquidity=73014040.0 spike=0.76
- DTPP.CA: score=25.9 buy_ready=True sector_rank=13 price=290.25 support=222.0 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=69.47 liquidity=21269354.0 spike=0.33
- EALR.CA: score=12.58 buy_ready=False sector_rank=13 price=417.82 support=411.51 resistance=456.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=81968264.0 spike=1.84
- EASB.CA: score=21.18 buy_ready=True sector_rank=13 price=7.42 support=6.71 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=40.87 liquidity=5282406.5 spike=0.51
- EAST.CA: score=21.9 buy_ready=False sector_rank=11 price=36.44 support=36.01 resistance=37.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=58.64 liquidity=27772774.0 spike=0.43
- EBSC.CA: score=25.18 buy_ready=True sector_rank=13 price=1.92 support=1.85 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=8277208.0 spike=1.5
- ECAP.CA: score=21.21 buy_ready=False sector_rank=13 price=38.59 support=32.12 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=70.83 liquidity=5308571.5 spike=0.44
- EDFM.CA: score=19.29 buy_ready=False sector_rank=13 price=415.23 support=352.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=80.45 liquidity=6209927.5 spike=1.09
- EEII.CA: score=12.1 buy_ready=False sector_rank=13 price=3.23 support=3.06 resistance=3.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32179088.0 spike=1.6
- EFIC.CA: score=28.46 buy_ready=False sector_rank=6 price=227.0 support=184.0 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=80.94 liquidity=112187416.0 spike=2.78
- EFID.CA: score=24.9 buy_ready=False sector_rank=11 price=33.02 support=26.64 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=91.7 liquidity=26690406.0 spike=0.3
- EFIH.CA: score=27.9 buy_ready=False sector_rank=7 price=24.56 support=22.04 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=72.76 liquidity=57691064.0 spike=0.52
- EGAL.CA: score=25.16 buy_ready=False sector_rank=6 price=346.09 support=292.0 resistance=359.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=83.45 liquidity=115792280.0 spike=1.13
- EGAS.CA: score=22.9 buy_ready=False sector_rank=8 price=59.57 support=50.0 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=76.57 liquidity=12033776.0 spike=0.49
- EGBE.CA: score=17.06 buy_ready=False sector_rank=4 price=0.52 support=0.46 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=65.7 liquidity=398400.72 spike=2.38
- EGCH.CA: score=25.9 buy_ready=False sector_rank=6 price=14.2 support=12.69 resistance=14.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=74.72 liquidity=65481024.0 spike=0.56
- EGSA.CA: score=5.91 buy_ready=False sector_rank=12 price=8.7 support=8.65 resistance=9.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 12:46 PM market time freshness=DELAYED_CURRENT RSI=23.81 liquidity=10214.45 spike=0.48
- EGTS.CA: score=27.61 buy_ready=True sector_rank=16 price=18.33 support=17.11 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=63.02 liquidity=26391860.0 spike=0.65
- EHDR.CA: score=29.9 buy_ready=True sector_rank=13 price=3.14 support=2.71 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=62.77 liquidity=30341226.0 spike=0.62
- EKHO.CA: score=11.9 buy_ready=False sector_rank=8 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=24.36 buy_ready=False sector_rank=1 price=2.15 support=2.12 resistance=2.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=128091864.0 spike=1.73
- ELKA.CA: score=18.9 buy_ready=False sector_rank=13 price=1.71 support=1.69 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=25987370.0 spike=0.33
- ELNA.CA: score=7.03 buy_ready=False sector_rank=13 price=37.67 support=36.5 resistance=39.49 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=22.03 liquidity=126081.48 spike=0.32
- ELSH.CA: score=23.9 buy_ready=False sector_rank=13 price=13.73 support=13.31 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=35.69 liquidity=20095520.0 spike=0.24
- ELWA.CA: score=9.06 buy_ready=False sector_rank=13 price=1.74 support=1.65 resistance=2.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=34.37 liquidity=1163395.25 spike=0.77
- EMFD.CA: score=21.53 buy_ready=False sector_rank=16 price=11.6 support=11.08 resistance=12.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=83843168.0 spike=1.46
- ENGC.CA: score=24.9 buy_ready=False sector_rank=13 price=49.64 support=40.11 resistance=54.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=75.11 liquidity=16673766.0 spike=0.59
- EOSB.CA: score=17.91 buy_ready=False sector_rank=13 price=1.55 support=1.52 resistance=1.62 source=Yahoo Finance as_of=2026-08-16T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=11325.85 spike=0.24
- EPCO.CA: score=27.92 buy_ready=True sector_rank=13 price=12.26 support=10.32 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=62.02 liquidity=29100336.0 spike=1.01
- EPPK.CA: score=8.68 buy_ready=False sector_rank=13 price=13.0 support=12.62 resistance=15.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=20.55 liquidity=1502683.75 spike=1.64
- ETEL.CA: score=29.9 buy_ready=True sector_rank=12 price=116.75 support=98.0 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=64.24 liquidity=100565680.0 spike=0.76
- ETRS.CA: score=25.52 buy_ready=False sector_rank=13 price=11.36 support=10.21 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=87.5 liquidity=37301804.0 spike=1.31
- EXPA.CA: score=22.9 buy_ready=False sector_rank=4 price=21.05 support=19.43 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=77.91 liquidity=20535562.0 spike=0.56
- FAIT.CA: score=20.19 buy_ready=False sector_rank=4 price=42.56 support=36.1 resistance=42.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=91.07 liquidity=4810883.0 spike=1.24
- FAITA.CA: score=25.08 buy_ready=False sector_rank=4 price=0.99 support=0.96 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:10 PM market time freshness=DELAYED_CURRENT RSI=63.53 liquidity=177889.0 spike=3.68
- FERC.CA: score=25.8 buy_ready=False sector_rank=6 price=77.5 support=75.01 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=56.86 liquidity=26378694.0 spike=1.45
- FWRY.CA: score=25.9 buy_ready=True sector_rank=7 price=19.12 support=18.69 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=52.8 liquidity=42721144.0 spike=0.33
- GBCO.CA: score=19.13 buy_ready=False sector_rank=19 price=30.25 support=29.53 resistance=33.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=49.75 liquidity=17543308.0 spike=0.28
- GDWA.CA: score=14.9 buy_ready=False sector_rank=13 price=0.8 support=0.8 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=25.3 liquidity=42298000.0 spike=0.38
- GGCC.CA: score=12.1 buy_ready=False sector_rank=13 price=0.93 support=0.91 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=80575528.0 spike=1.6
- GIHD.CA: score=25.9 buy_ready=True sector_rank=13 price=65.53 support=50.6 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=65.1 liquidity=14053742.0 spike=0.3
- GMCI.CA: score=9.28 buy_ready=False sector_rank=13 price=1.92 support=1.88 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:12 PM market time freshness=DELAYED_CURRENT RSI=31.71 liquidity=382641.44 spike=0.52
- GRCA.CA: score=23.9 buy_ready=False sector_rank=13 price=56.59 support=54.7 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=39.56 liquidity=12736142.0 spike=0.65
- GSSC.CA: score=28.9 buy_ready=True sector_rank=13 price=290.0 support=264.0 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=65.47 liquidity=84069776.0 spike=4.61
- GTWL.CA: score=26.54 buy_ready=False sector_rank=13 price=172.99 support=85.0 resistance=184.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=87.91 liquidity=267982848.0 spike=1.82
- HDBK.CA: score=20.9 buy_ready=False sector_rank=4 price=92.86 support=77.07 resistance=91.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=95.69 liquidity=31776024.0 spike=0.78
- HELI.CA: score=23.61 buy_ready=False sector_rank=16 price=7.52 support=7.56 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=35.06 liquidity=148486352.0 spike=0.85
- HRHO.CA: score=19.27 buy_ready=False sector_rank=18 price=26.51 support=25.95 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=50.16 liquidity=67542896.0 spike=0.68
- ICID.CA: score=15.9 buy_ready=False sector_rank=13 price=15.72 support=14.5 resistance=16.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=90799568.0 spike=5.61
- IDRE.CA: score=24.93 buy_ready=True sector_rank=13 price=55.52 support=44.91 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=69.56 liquidity=9031981.0 spike=0.32
- IFAP.CA: score=27.87 buy_ready=True sector_rank=14 price=20.78 support=18.96 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=63.19 liquidity=15472299.0 spike=0.64
- INFI.CA: score=22.9 buy_ready=False sector_rank=13 price=156.39 support=103.32 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=77.0 liquidity=36702184.0 spike=0.63
- IRON.CA: score=27.98 buy_ready=True sector_rank=6 price=32.9 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=53.39 liquidity=23434104.0 spike=2.54
- ISMA.CA: score=24.9 buy_ready=False sector_rank=13 price=35.8 support=27.27 resistance=36.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=75.51 liquidity=20589480.0 spike=0.73
- ISMQ.CA: score=25.9 buy_ready=True sector_rank=6 price=9.31 support=8.96 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=48.74 liquidity=47712500.0 spike=0.76
- ISPH.CA: score=25.9 buy_ready=True sector_rank=5 price=13.2 support=11.3 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=68.42 liquidity=77328768.0 spike=0.41
- JUFO.CA: score=19.9 buy_ready=False sector_rank=11 price=27.1 support=22.78 resistance=29.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=91.13 liquidity=23130602.0 spike=0.39
- KABO.CA: score=13.72 buy_ready=False sector_rank=9 price=9.1 support=9.1 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=93324728.0 spike=2.41
- KWIN.CA: score=18.9 buy_ready=False sector_rank=13 price=88.17 support=83.99 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=20.55 liquidity=43720788.0 spike=0.74
- KZPC.CA: score=27.0 buy_ready=False sector_rank=13 price=12.21 support=8.42 resistance=13.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=93.63 liquidity=29152192.0 spike=2.05
- LCSW.CA: score=23.66 buy_ready=False sector_rank=15 price=34.38 support=30.2 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=36.32 liquidity=46611688.0 spike=1.0
- LUTS.CA: score=27.92 buy_ready=False sector_rank=13 price=1.42 support=0.54 resistance=1.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=93.78 liquidity=231758560.0 spike=2.51
- MAAL.CA: score=17.59 buy_ready=False sector_rank=13 price=8.75 support=8.32 resistance=9.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=57.0 liquidity=3685408.25 spike=0.25
- MASR.CA: score=20.9 buy_ready=False sector_rank=13 price=7.6 support=7.45 resistance=8.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=38.97 liquidity=70263928.0 spike=0.94
- MBSC.CA: score=11.88 buy_ready=False sector_rank=15 price=363.86 support=361.02 resistance=408.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=115157984.0 spike=1.61
- MCQE.CA: score=10.96 buy_ready=False sector_rank=15 price=224.45 support=212.01 resistance=244.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=54066292.0 spike=1.15
- MCRO.CA: score=23.9 buy_ready=False sector_rank=13 price=1.51 support=1.36 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=48.78 liquidity=51218092.0 spike=0.29
- MENA.CA: score=22.25 buy_ready=True sector_rank=16 price=7.11 support=6.83 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=56.6 liquidity=4635510.0 spike=0.73
- MEPA.CA: score=23.9 buy_ready=False sector_rank=13 price=1.88 support=1.76 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=39956016.0 spike=0.63
- MFPC.CA: score=22.9 buy_ready=False sector_rank=6 price=39.49 support=35.37 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=78.18 liquidity=71694904.0 spike=0.88
- MFSC.CA: score=18.89 buy_ready=True sector_rank=13 price=49.49 support=46.0 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:10 PM market time freshness=DELAYED_CURRENT RSI=56.5 liquidity=2990892.75 spike=0.25
- MHOT.CA: score=25.9 buy_ready=False sector_rank=2 price=18.66 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=61.3 liquidity=16154453.0 spike=0.97
- MICH.CA: score=14.82 buy_ready=False sector_rank=13 price=50.18 support=48.0 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=99755168.0 spike=2.96
- MILS.CA: score=15.9 buy_ready=False sector_rank=13 price=229.62 support=192.22 resistance=229.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=296529024.0 spike=4.35
- MIPH.CA: score=16.47 buy_ready=False sector_rank=5 price=775.8 support=722.7 resistance=828.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:09 PM market time freshness=DELAYED_CURRENT RSI=60.28 liquidity=567147.69 spike=0.12
- MOED.CA: score=15.9 buy_ready=False sector_rank=13 price=0.73 support=0.69 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=204489312.0 spike=6.11
- MOIL.CA: score=16.11 buy_ready=False sector_rank=8 price=0.66 support=0.55 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=58.06 liquidity=212201.28 spike=0.34
- MOIN.CA: score=24.9 buy_ready=False sector_rank=13 price=36.51 support=23.11 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=82.64 liquidity=26890648.0 spike=0.97
- MOSC.CA: score=24.9 buy_ready=False sector_rank=13 price=331.52 support=282.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=90.23 liquidity=12289776.0 spike=0.81
- MPCI.CA: score=25.96 buy_ready=False sector_rank=13 price=377.0 support=248.25 resistance=460.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=71.04 liquidity=161899536.0 spike=1.03
- MPCO.CA: score=13.05 buy_ready=False sector_rank=14 price=2.25 support=2.11 resistance=2.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=209805920.0 spike=2.09
- MPRC.CA: score=24.16 buy_ready=False sector_rank=13 price=44.0 support=42.6 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=47.54 liquidity=29644448.0 spike=1.13
- MTIE.CA: score=21.47 buy_ready=False sector_rank=19 price=8.97 support=8.68 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=106221112.0 spike=2.17
- NAHO.CA: score=6.22 buy_ready=False sector_rank=13 price=0.15 support=0.14 resistance=0.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=317487.69 spike=5.64
- NCCW.CA: score=20.9 buy_ready=False sector_rank=13 price=6.05 support=5.67 resistance=7.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=52.4 liquidity=30216448.0 spike=0.9
- NEDA.CA: score=26.54 buy_ready=True sector_rank=13 price=2.95 support=2.7 resistance=2.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:10 PM market time freshness=DELAYED_CURRENT RSI=64.29 liquidity=3644100.25 spike=4.32
- NHPS.CA: score=25.9 buy_ready=True sector_rank=13 price=89.84 support=82.25 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=58.72 liquidity=25789828.0 spike=0.43
- NINH.CA: score=23.9 buy_ready=False sector_rank=13 price=21.64 support=21.12 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=47.68 liquidity=13527693.0 spike=0.24
- NIPH.CA: score=25.9 buy_ready=False sector_rank=5 price=368.55 support=203.5 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=73.38 liquidity=187507840.0 spike=0.62
- OBRI.CA: score=26.66 buy_ready=False sector_rank=13 price=34.07 support=31.61 resistance=36.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=44.46 liquidity=62501756.0 spike=1.88
- OCDI.CA: score=25.61 buy_ready=False sector_rank=16 price=33.94 support=26.6 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=72.64 liquidity=73090976.0 spike=0.53
- OCPH.CA: score=22.9 buy_ready=False sector_rank=13 price=263.61 support=225.0 resistance=496.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=52.34 liquidity=10920870.0 spike=0.31
- ODIN.CA: score=12.36 buy_ready=False sector_rank=13 price=3.54 support=3.34 resistance=3.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=63761920.0 spike=1.73
- OFH.CA: score=22.9 buy_ready=False sector_rank=13 price=0.91 support=0.69 resistance=0.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=76.76 liquidity=58629244.0 spike=0.61
- OIH.CA: score=22.9 buy_ready=False sector_rank=10 price=1.82 support=1.43 resistance=1.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=80.43 liquidity=110440744.0 spike=0.92
- OLFI.CA: score=27.9 buy_ready=True sector_rank=11 price=24.53 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=63.46 liquidity=13950515.0 spike=0.21
- ORAS.CA: score=9.1 buy_ready=False sector_rank=20 price=761.16 support=750.01 resistance=768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=116998264.0 spike=1.0
- ORHD.CA: score=26.29 buy_ready=False sector_rank=16 price=41.6 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=70.43 liquidity=220414288.0 spike=1.34
- ORWE.CA: score=25.9 buy_ready=False sector_rank=9 price=25.79 support=22.55 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=74.82 liquidity=25445636.0 spike=0.33
- PHAR.CA: score=25.9 buy_ready=True sector_rank=5 price=134.2 support=90.01 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=68.6 liquidity=256337168.0 spike=0.62
- PHDC.CA: score=27.31 buy_ready=False sector_rank=16 price=15.38 support=14.32 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=77.27 liquidity=564179840.0 spike=2.35
- PHTV.CA: score=27.65 buy_ready=True sector_rank=13 price=367.95 support=309.09 resistance=447.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=61.81 liquidity=6753714.5 spike=2.5
- POUL.CA: score=22.9 buy_ready=False sector_rank=11 price=37.59 support=36.5 resistance=40.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=19209168.0 spike=0.76
- PRCL.CA: score=23.66 buy_ready=False sector_rank=15 price=35.25 support=32.8 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=52.46 liquidity=16858762.0 spike=0.44
- PRDC.CA: score=23.61 buy_ready=False sector_rank=16 price=8.83 support=8.7 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=46.54 liquidity=19204358.0 spike=0.19
- PRMH.CA: score=18.73 buy_ready=False sector_rank=13 price=2.56 support=2.56 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=45.59 liquidity=7833417.5 spike=0.61
- RACC.CA: score=29.9 buy_ready=True sector_rank=13 price=10.46 support=9.8 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=63.83 liquidity=15967555.0 spike=0.82
- RAKT.CA: score=10.89 buy_ready=False sector_rank=13 price=22.23 support=21.66 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:08 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=369719.5 spike=1.31
- RAYA.CA: score=17.88 buy_ready=False sector_rank=21 price=7.15 support=6.97 resistance=7.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=39.76 liquidity=42506184.0 spike=0.44
- RMDA.CA: score=25.9 buy_ready=False sector_rank=5 price=6.22 support=4.95 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=73.88 liquidity=43686788.0 spike=0.37
- ROTO.CA: score=22.9 buy_ready=False sector_rank=13 price=51.22 support=40.99 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=77.76 liquidity=19511696.0 spike=0.81
- RREI.CA: score=11.2 buy_ready=False sector_rank=13 price=4.9 support=4.63 resistance=4.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=73124736.0 spike=1.15
- RTVC.CA: score=29.46 buy_ready=True sector_rank=13 price=3.97 support=3.73 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=48.21 liquidity=14976248.0 spike=2.78
- RUBX.CA: score=25.9 buy_ready=True sector_rank=13 price=12.9 support=12.02 resistance=14.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=53.61 liquidity=22391732.0 spike=0.86
- SAUD.CA: score=29.24 buy_ready=False sector_rank=4 price=23.72 support=21.4 resistance=23.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=70.1 liquidity=47191772.0 spike=2.67
- SCEM.CA: score=29.28 buy_ready=True sector_rank=15 price=102.5 support=71.25 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=69.2 liquidity=348278624.0 spike=1.81
- SCFM.CA: score=27.68 buy_ready=True sector_rank=13 price=295.12 support=270.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=54.37 liquidity=57365408.0 spike=1.89
- SCTS.CA: score=33.9 buy_ready=True sector_rank=3 price=617.0 support=602.01 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=56.73 liquidity=38916452.0 spike=4.55
- SDTI.CA: score=25.9 buy_ready=False sector_rank=13 price=70.82 support=47.01 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=73.84 liquidity=15419446.0 spike=0.53
- SEIG.CA: score=12.91 buy_ready=False sector_rank=13 price=271.73 support=237.0 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=77.23 liquidity=2013269.25 spike=0.16
- SIPC.CA: score=24.9 buy_ready=False sector_rank=13 price=5.05 support=3.76 resistance=5.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=75.23 liquidity=45047488.0 spike=0.7
- SKPC.CA: score=26.9 buy_ready=True sector_rank=6 price=16.88 support=15.61 resistance=17.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=68.64 liquidity=38093352.0 spike=0.77
- SMFR.CA: score=22.47 buy_ready=True sector_rank=13 price=261.94 support=225.0 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=66.95 liquidity=6573742.5 spike=0.18
- SNFC.CA: score=18.92 buy_ready=False sector_rank=13 price=10.94 support=10.6 resistance=11.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=44.54 liquidity=6016727.5 spike=0.48
- SPIN.CA: score=22.92 buy_ready=False sector_rank=9 price=20.2 support=14.75 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=86.46 liquidity=47186384.0 spike=1.01
- SPMD.CA: score=23.9 buy_ready=False sector_rank=13 price=0.47 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=57.47 liquidity=12237112.0 spike=0.36
- SUGR.CA: score=29.9 buy_ready=False sector_rank=11 price=52.0 support=46.47 resistance=51.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=80.34 liquidity=85620608.0 spike=5.5
- SVCE.CA: score=25.9 buy_ready=False sector_rank=13 price=10.82 support=9.06 resistance=12.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=74.85 liquidity=47301316.0 spike=0.47
- SWDY.CA: score=32.9 buy_ready=False sector_rank=1 price=128.15 support=91.01 resistance=125.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=80.65 liquidity=347445280.0 spike=4.9
- TALM.CA: score=25.9 buy_ready=False sector_rank=3 price=19.59 support=15.61 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=76.61 liquidity=27776514.0 spike=0.66
- TMGH.CA: score=20.61 buy_ready=False sector_rank=16 price=96.44 support=95.2 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=35.65 liquidity=164146768.0 spike=0.47
- TRTO.CA: score=24.94 buy_ready=False sector_rank=13 price=0.05 support=0.03 resistance=0.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37068.59 spike=5.05
- UEFM.CA: score=17.34 buy_ready=False sector_rank=13 price=544.63 support=530.0 resistance=594.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=50.38 liquidity=3441298.5 spike=0.5
- UEGC.CA: score=10.9 buy_ready=False sector_rank=13 price=2.25 support=2.23 resistance=2.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=38244216.0 spike=0.87
- UNIP.CA: score=25.92 buy_ready=False sector_rank=13 price=0.4 support=0.37 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=49.44 liquidity=64867924.0 spike=2.01
- UNIT.CA: score=19.46 buy_ready=True sector_rank=16 price=18.78 support=17.32 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=55.99 liquidity=1846570.25 spike=0.13
- WCDF.CA: score=16.39 buy_ready=False sector_rank=13 price=644.63 support=550.0 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=80.01 liquidity=3486075.5 spike=0.65
- WKOL.CA: score=12.7 buy_ready=False sector_rank=13 price=345.25 support=341.0 resistance=372.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=59240780.0 spike=1.9
- ZEOT.CA: score=24.9 buy_ready=False sector_rank=13 price=14.27 support=11.51 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=75.25 liquidity=21051106.0 spike=0.74
- ZMID.CA: score=25.61 buy_ready=True sector_rank=16 price=7.45 support=7.06 resistance=7.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=118194968.0 spike=0.51

## Backtesting Lite
- SCTS.CA: 180d return=89.9%, max drawdown=-21.39%, MA20>MA50 days last20=15, as_of=2026-08-16T21:00:00+00:00
- CIEB.CA: 180d return=30.08%, max drawdown=-19.11%, MA20>MA50 days last20=20, as_of=2026-08-16T21:00:00+00:00
- SWDY.CA: 180d return=62.35%, max drawdown=-14.67%, MA20>MA50 days last20=20, as_of=2026-08-16T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- SCTS.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Suez Canal Company for Technology Settling summary=Suez Canal Technology’s consolidated net profits cross EGP 1.5bn in H1-25/26; Suez Canal Technology’s shareholders greenlight EGP 11/shr dividends; Suez Canal Technology logs EGP 1.3bn consolidated profits in FY23/24
  - Suez Canal Technology’s consolidated net profits cross EGP 1.5bn in H1-25/26: https://english.mubasher.info/news/4600018/Suez-Canal-Technology-s-consolidated-net-profits-cross-EGP-1-5bn-in-H1-25-26/
  - Suez Canal Technology’s shareholders greenlight EGP 11/shr dividends: https://english.mubasher.info/news/4463096/Suez-Canal-Technology-s-shareholders-greenlight-EGP-11-shr-dividends/
  - Suez Canal Technology logs EGP 1.3bn consolidated profits in FY23/24: https://english.mubasher.info/news/4366060/Suez-Canal-Technology-logs-EGP-1-3bn-consolidated-profits-in-FY23-24/
- CIEB.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Credit Agricole Egypt summary=Evidence rejected for CIEB.CA: source text did not clearly match CIEB.CA / Credit Agricole Egypt.
- SWDY.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Elsewedy Electric summary=Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26; Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations; Elsewedy Electric’s subsidiary leads expansion of SAL project at Riyadh airport
  - Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26: https://english.mubasher.info/news/4614341/Elsewedy-Electric-s-consolidated-revenues-total-EGP-75-2bn-in-Q1-26/
  - Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations: https://english.mubasher.info/news/4593166/Elsewedy-Electric-accelerates-power-transformation-project-in-KSA-with-6-high-voltage-substations/
  - Elsewedy Electric’s subsidiary leads expansion of SAL project at Riyadh airport: https://english.mubasher.info/news/4580464/Elsewedy-Electric-s-subsidiary-leads-expansion-of-SAL-project-at-Riyadh-airport/
- ATQA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr National Steel Ataqa summary=Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- EHDR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=595 sources=3 expected=Egyptians for Housing & Development Co. summary=Egyptians for Housing to disburse EGP 0.01/shr for 2025; EGX-listed companies, banks propose cash dividends for 2025; Egyptians for Housing stock witnesses selling pressures amid key levels to observe – Analysis
  - Egyptians for Housing to disburse EGP 0.01/shr for 2025: https://english.mubasher.info/news/4584569/Egyptians-for-Housing-to-disburse-EGP-0-01-shr-for-2025/
  - EGX-listed companies, banks propose cash dividends for 2025: https://english.mubasher.info/news/4560139/EGX-listed-companies-banks-propose-cash-dividends-for-2025/
  - Egyptians for Housing stock witnesses selling pressures amid key levels to observe – Analysis: https://english.mubasher.info/news/4547337/Egyptians-for-Housing-stock-witnesses-selling-pressures-amid-key-levels-to-observe-Analysis/
- SUGR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=595 sources=3 expected=Delta Sugar summary=Delta Sugar’s net profits fall 74% in Q1-26; Delta Sugar stock tests key resistance near EGP 50 amid downtrend; Delta Sugar turns to EGP 346m net losses in 2025
  - Delta Sugar’s net profits fall 74% in Q1-26: https://english.mubasher.info/news/4604921/Delta-Sugar-s-net-profits-fall-74-in-Q1-26/
  - Delta Sugar stock tests key resistance near EGP 50 amid downtrend: https://english.mubasher.info/news/4584932/Delta-Sugar-stock-tests-key-resistance-near-EGP-50-amid-downtrend/
  - Delta Sugar turns to EGP 346m net losses in 2025: https://english.mubasher.info/news/4557875/Delta-Sugar-turns-to-EGP-346m-net-losses-in-2025/
- RACC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Raya Customer Experience summary=Evidence rejected for RACC.CA: source text did not clearly match RACC.CA / Raya Customer Experience.

## Warnings
- Evidence for SCTS.CA matches the company but no source/report date was detected.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence rejected for CIEB.CA: source text did not clearly match CIEB.CA / Credit Agricole Egypt.
- Evidence for SWDY.CA matches the company but no source/report date was detected.
- Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for EHDR.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for SUGR.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for RACC.CA: source text did not clearly match RACC.CA / Raya Customer Experience.
