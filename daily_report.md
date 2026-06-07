# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-06-07T08:43:18.395227+00:00
Generated Cairo: 2026-06-07 11:43
Run timing: target 08:45 Cairo | generated Cairo 2026-06-07 11:43 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-06-07 11:39

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 79
- Data quality issues: 0
- Tradeable price/liquidity tickers: 184/190
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, June 07
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 35.0% / above MA50 75.0%
- EGX70 regime: BULLISH / above MA20 60.0% / above MA50 82.5%
- Sector breadth: 80.95%
- Risk mode: SELECTIVE_SMALL_MID_SWINGS

## Top Liquidity
- EMFD.CA: liquidity=381871232.0 spike=2.02 score=30.44
- CCAP.CA: liquidity=173585728.0 spike=0.21 score=24.4
- MPCO.CA: liquidity=131602696.0 spike=2.4 score=29.2
- NIPH.CA: liquidity=116308880.0 spike=0.97 score=9.4
- PHDC.CA: liquidity=101225456.0 spike=0.22 score=26.4

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner highlighted three BUY‑watch tickets (UEGC, NCCW, EMFD) that cleared liquidity, price‑above‑MA20/MA50 and RSI ~65‑68 filters. All sit on solid 20‑day support, face modest resistance, and show an accumulation‑spike liquidity regime. The broader market is in a mixed regime: EGX30 remains bearish with weak breadth, while EGX70 is bullish, allowing selective small‑mid swing opportunities. Sector breadth is high (≈81%), but the top picks are in non‑leading sectors, adding extra caution. Outlooks are bullish‑watch but confidence is low, so price action should be verified on the Thndr chart before treating these as swing entries.
- UEGC, NCCW, EMFD show strong support (1.3, 5.13, 9.83) and are near or just above resistance, with RSI 65‑68 indicating room for upside.
- Liquidity spikes (3‑3.3×) and price above MA20/MA50 suggest short‑term accumulation despite overall EGX30 bearishness.
- EGX70 bullish breadth supports selective small‑mid swing trades; risk mode remains SELECTIVE_SMALL_MID_SWINGS.
- Sector leadership is weak; momentum appears extended, so monitor price action and volatility over the next 1‑3 days.
- Uncertainty remains high – macro trend bearish, confidence low, and sector not leading; treat as watch‑only until confirmation.

## Top Liquidity Spikes
- LUTS.CA: spike=12.9 liquidity=83817496.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AREH.CA: spike=3.64 liquidity=77971960.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- UEGC.CA: spike=3.29 liquidity=65824660.0 outlook=BULLISH_WATCH score=81.85 buy_ready=True
- GGCC.CA: spike=3.27 liquidity=17860310.0 outlook=BULLISH_WATCH score=76.85 buy_ready=True
- NCCW.CA: spike=3.17 liquidity=53575508.0 outlook=BULLISH_WATCH score=77.85 buy_ready=True

## Sector Leaderboard
- #1 Tourism & Leisure: score=11.5 5d=4.25% 20d=18.02% aboveMA50=100.0%
- #2 Real Estate: score=10.29 5d=2.83% 20d=18.03% aboveMA50=100.0%
- #3 Technology & Distribution: score=10.29 5d=0.94% 20d=18.9% aboveMA50=100.0%
- #4 Investment Holding: score=8.36 5d=4.69% 20d=10.97% aboveMA50=66.67%
- #5 Agriculture & Food Production: score=8.11 5d=6.74% 20d=2.37% aboveMA50=50.0%
- #6 Industrial Goods & Cables: score=7.46 5d=2.04% 20d=1.18% aboveMA50=100.0%
- #7 Healthcare: score=7.21 5d=3.52% 20d=4.36% aboveMA50=83.33%
- #8 Textiles: score=7.21 5d=2.4% 20d=6.38% aboveMA50=75.0%

## Today's Prioritized Action Tickets
- Priority #1: BUY UEGC.CA
  - Entry: 1.53 | Take profit: 1.65 | Stop loss: 1.47
  - Confidence: LOW | score=30.92 | outlook=BULLISH_WATCH 81.85
  - Reason: WATCH/BUY SETUP: UEGC.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 65.22, support 1.3, resistance 1.46, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY NCCW.CA
  - Entry: 6.2 | Take profit: 6.7 | Stop loss: 5.95
  - Confidence: LOW | score=30.68 | outlook=BULLISH_WATCH 77.85
  - Reason: WATCH/BUY SETUP: NCCW.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 66.49, support 5.13, resistance 6.2, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY EMFD.CA
  - Entry: 12.46 | Take profit: 13.46 | Stop loss: 11.96
  - Confidence: LOW | score=30.44 | outlook=BULLISH_WATCH 97
  - Reason: WATCH/BUY SETUP: EMFD.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 67.51, support 9.83, resistance 12.38, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- EMFD.CA: BULLISH_WATCH score=97 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended; far above support
- ZMID.CA: BULLISH_WATCH score=96 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ARAB.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- AMER.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- RAYA.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- UNIT.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- CLHO.CA: BULLISH_WATCH score=83.21 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- PHDC.CA: BULLISH_WATCH score=82 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- UEGC.CA: BULLISH_WATCH score=81.85 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- PRDC.CA: BULLISH_WATCH score=80 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended; far above support

## BUY-Ready Candidates
- UEGC.CA: rank=30.92 outlook=BULLISH_WATCH outlook_score=81.85 sector_rank=11 price=1.53 support=1.3 resistance=1.46 liquidity=65824660.0
- NCCW.CA: rank=30.68 outlook=BULLISH_WATCH outlook_score=77.85 sector_rank=11 price=6.2 support=5.13 resistance=6.2 liquidity=53575508.0
- EMFD.CA: rank=30.44 outlook=BULLISH_WATCH outlook_score=97 sector_rank=2 price=12.46 support=9.83 resistance=12.38 liquidity=381871232.0
- GGCC.CA: rank=29.88 outlook=BULLISH_WATCH outlook_score=76.85 sector_rank=11 price=0.44 support=0.39 resistance=0.44 liquidity=17860310.0
- MPCO.CA: rank=29.2 outlook=BULLISH_WATCH outlook_score=79.11 sector_rank=5 price=1.87 support=1.54 resistance=1.88 liquidity=131602696.0
- COSG.CA: rank=28.76 outlook=CONSTRUCTIVE outlook_score=63.85 sector_rank=11 price=1.7 support=1.44 resistance=1.71 liquidity=62303708.0
- ARAB.CA: rank=28.4 outlook=BULLISH_WATCH outlook_score=90 sector_rank=2 price=0.21 support=0.19 resistance=0.22 liquidity=13485010.0
- GDWA.CA: rank=27.38 outlook=BULLISH_WATCH outlook_score=78.85 sector_rank=11 price=0.83 support=0.77 resistance=0.83 liquidity=11152637.0
- JUFO.CA: rank=27.33 outlook=BULLISH_WATCH outlook_score=72.84 sector_rank=12 price=29.55 support=26.51 resistance=29.98 liquidity=8997666.0
- ARVA.CA: rank=26.46 outlook=CONSTRUCTIVE outlook_score=65.85 sector_rank=11 price=10.91 support=7.71 resistance=10.68 liquidity=26524222.0

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=12.91 buy_ready=False sector_rank=11 price=206.66 support=195.1 resistance=249.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=40.2 liquidity=568289.69 spike=0.03
- ABUK.CA: score=18.13 buy_ready=False sector_rank=18 price=81.32 support=81.52 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=37.92 liquidity=24931342.0 spike=0.19
- ACAMD.CA: score=26.34 buy_ready=True sector_rank=11 price=2.38 support=1.94 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=63.64 liquidity=50609228.0 spike=0.46
- ACGC.CA: score=24.4 buy_ready=True sector_rank=8 price=10.18 support=8.3 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=67.34 liquidity=19602242.0 spike=0.37
- ADCI.CA: score=16.17 buy_ready=True sector_rank=11 price=217.86 support=198.0 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=47.01 liquidity=1828479.13 spike=0.25
- ADIB.CA: score=21.56 buy_ready=False sector_rank=17 price=46.76 support=44.45 resistance=50.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=44.38 liquidity=13326503.0 spike=0.08
- ADPC.CA: score=16.27 buy_ready=False sector_rank=11 price=3.75 support=3.54 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=44.35 liquidity=3932121.0 spike=0.16
- AFDI.CA: score=19.68 buy_ready=True sector_rank=11 price=45.0 support=36.82 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=58.02 liquidity=3344112.5 spike=0.18
- AFMC.CA: score=17.55 buy_ready=True sector_rank=11 price=74.58 support=69.33 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=38.17 liquidity=3208816.0 spike=0.22
- AJWA.CA: score=16.78 buy_ready=True sector_rank=11 price=135.0 support=130.01 resistance=139.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=44.23 liquidity=2440352.75 spike=0.22
- ALCN.CA: score=14.92 buy_ready=False sector_rank=15 price=29.16 support=28.4 resistance=30.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=45.19 liquidity=4093885.75 spike=0.15
- ALUM.CA: score=21.15 buy_ready=True sector_rank=11 price=25.73 support=22.35 resistance=26.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=46.39 liquidity=6810264.5 spike=0.3
- AMER.CA: score=26.4 buy_ready=True sector_rank=2 price=2.72 support=2.29 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=49.4 liquidity=10112659.0 spike=0.08
- AMES.CA: score=8.89 buy_ready=False sector_rank=11 price=50.95 support=48.0 resistance=59.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=21.16 liquidity=1546302.25 spike=0.13
- AMIA.CA: score=14.96 buy_ready=False sector_rank=11 price=9.06 support=8.16 resistance=10.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=31.86 liquidity=5616201.5 spike=0.16
- AMOC.CA: score=19.18 buy_ready=False sector_rank=13 price=8.25 support=8.12 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=43.38 liquidity=14985116.0 spike=0.17
- ANFI.CA: score=12.98 buy_ready=False sector_rank=11 price=14.05 support=13.5 resistance=15.55 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=24.73 liquidity=5638883.28 spike=0.28
- APSW.CA: score=14.83 buy_ready=False sector_rank=11 price=9.02 support=8.62 resistance=9.38 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=49.5 liquidity=491581.0 spike=0.56
- ARAB.CA: score=28.4 buy_ready=True sector_rank=2 price=0.21 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=51.72 liquidity=13485010.0 spike=0.18
- ARCC.CA: score=26.4 buy_ready=True sector_rank=9 price=59.0 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=56.59 liquidity=12556855.0 spike=0.28
- AREH.CA: score=14.34 buy_ready=False sector_rank=11 price=1.52 support=1.4 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=77971960.0 spike=3.64
- ARVA.CA: score=26.46 buy_ready=True sector_rank=11 price=10.91 support=7.71 resistance=10.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=26524222.0 spike=1.06
- ASCM.CA: score=24.34 buy_ready=True sector_rank=11 price=56.61 support=43.76 resistance=59.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=65.89 liquidity=42541248.0 spike=0.69
- ASPI.CA: score=11.06 buy_ready=False sector_rank=11 price=0.36 support=0.35 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=87096760.0 spike=1.86
- ATLC.CA: score=11.3 buy_ready=False sector_rank=16 price=4.99 support=4.71 resistance=5.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=32.53 liquidity=2587802.5 spike=0.32
- ATQA.CA: score=25.13 buy_ready=True sector_rank=18 price=10.02 support=9.41 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=49.67 liquidity=14177549.0 spike=0.29
- AXPH.CA: score=8.31 buy_ready=False sector_rank=11 price=1128.59 support=960.0 resistance=1239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=7.55 liquidity=974792.69 spike=0.17
- BINV.CA: score=16.96 buy_ready=True sector_rank=4 price=46.11 support=40.5 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=67.08 liquidity=2558643.0 spike=0.19
- BIOC.CA: score=16.66 buy_ready=True sector_rank=11 price=75.03 support=70.0 resistance=79.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=41.46 liquidity=2316030.25 spike=0.29
- BTFH.CA: score=20.71 buy_ready=False sector_rank=16 price=3.09 support=3.03 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=36.17 liquidity=88938704.0 spike=0.36
- CAED.CA: score=7.99 buy_ready=False sector_rank=11 price=71.68 support=64.49 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=24.28 liquidity=645689.63 spike=0.04
- CANA.CA: score=24.83 buy_ready=True sector_rank=17 price=36.91 support=33.15 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=44.06 liquidity=9276119.0 spike=0.67
- CCAP.CA: score=24.4 buy_ready=True sector_rank=4 price=5.39 support=4.47 resistance=5.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=173585728.0 spike=0.21
- CCRS.CA: score=22.34 buy_ready=True sector_rank=11 price=2.57 support=1.98 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=65.79 liquidity=15421644.0 spike=0.56
- CEFM.CA: score=11.3 buy_ready=False sector_rank=11 price=109.12 support=103.07 resistance=119.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=28.81 liquidity=1955793.25 spike=0.26
- CERA.CA: score=17.3 buy_ready=True sector_rank=11 price=1.2 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=3959625.0 spike=0.29
- CFGH.CA: score=4.55 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=6311.86 spike=1.6
- CICH.CA: score=7.29 buy_ready=False sector_rank=16 price=12.31 support=10.9 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=33.16 liquidity=581421.63 spike=0.13
- CIEB.CA: score=14.62 buy_ready=True sector_rank=17 price=23.7 support=23.31 resistance=24.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=43.48 liquidity=1064567.5 spike=0.09
- CIRA.CA: score=16.47 buy_ready=True sector_rank=14 price=26.75 support=19.5 resistance=28.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=40.77 liquidity=2592181.0 spike=0.09
- CLHO.CA: score=17.05 buy_ready=True sector_rank=7 price=15.8 support=14.58 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=48.56 liquidity=2647334.5 spike=0.07
- CNFN.CA: score=9.22 buy_ready=False sector_rank=16 price=4.55 support=4.41 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=30.26 liquidity=3507115.0 spike=0.22
- COMI.CA: score=21.56 buy_ready=False sector_rank=17 price=131.86 support=131.3 resistance=144.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=44.39 liquidity=55497592.0 spike=0.09
- COPR.CA: score=18.34 buy_ready=False sector_rank=11 price=0.37 support=0.3 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=77.27 liquidity=30402792.0 spike=0.82
- COSG.CA: score=28.76 buy_ready=True sector_rank=11 price=1.7 support=1.44 resistance=1.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=63.89 liquidity=62303708.0 spike=1.21
- CPCI.CA: score=11.91 buy_ready=False sector_rank=11 price=362.19 support=336.0 resistance=374.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=75.65 liquidity=566298.13 spike=0.07
- CSAG.CA: score=21.23 buy_ready=True sector_rank=15 price=31.93 support=30.4 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=3401764.75 spike=0.17
- DAPH.CA: score=9.08 buy_ready=False sector_rank=11 price=81.37 support=79.25 resistance=96.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=17.24 liquidity=1744612.25 spike=0.05
- DEIN.CA: score=10.34 buy_ready=False sector_rank=11 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=5.57 buy_ready=False sector_rank=12 price=24.58 support=24.7 resistance=26.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=34.39 liquidity=1238556.88 spike=0.53
- DSCW.CA: score=22.34 buy_ready=False sector_rank=11 price=1.86 support=1.71 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=44.83 liquidity=20996330.0 spike=0.31
- DTPP.CA: score=7.78 buy_ready=False sector_rank=11 price=125.92 support=121.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=28.41 liquidity=438339.5 spike=0.07
- EALR.CA: score=12.9 buy_ready=False sector_rank=11 price=360.22 support=346.01 resistance=429.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=35.9 liquidity=555109.0 spike=0.03
- EASB.CA: score=15.79 buy_ready=True sector_rank=11 price=5.04 support=4.61 resistance=5.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=1446995.25 spike=0.85
- EAST.CA: score=22.4 buy_ready=True sector_rank=12 price=38.85 support=37.01 resistance=39.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=48.01 liquidity=8065700.0 spike=0.12
- EBSC.CA: score=17.4 buy_ready=True sector_rank=11 price=1.9 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=68.29 liquidity=1055798.13 spike=0.35
- ECAP.CA: score=15.81 buy_ready=True sector_rank=11 price=31.46 support=28.7 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=51.75 liquidity=1466870.63 spike=0.28
- EDFM.CA: score=14.66 buy_ready=False sector_rank=11 price=338.32 support=320.2 resistance=364.87 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=48.99 liquidity=322757.29 spike=0.45
- EEII.CA: score=18.13 buy_ready=True sector_rank=11 price=2.41 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=43.48 liquidity=3791245.75 spike=0.21
- EFIC.CA: score=3.44 buy_ready=False sector_rank=18 price=205.3 support=195.25 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=26.74 liquidity=305091.41 spike=0.07
- EFID.CA: score=24.34 buy_ready=False sector_rank=12 price=28.93 support=27.49 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=71.91 liquidity=11077674.0 spike=0.23
- EFIH.CA: score=16.35 buy_ready=False sector_rank=20 price=21.97 support=21.0 resistance=22.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=54.51 liquidity=5889778.0 spike=0.09
- EGAL.CA: score=23.13 buy_ready=True sector_rank=18 price=324.65 support=295.0 resistance=344.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=43.9 liquidity=12339842.0 spike=0.11
- EGAS.CA: score=19.84 buy_ready=True sector_rank=13 price=51.0 support=46.51 resistance=51.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=60.23 liquidity=3660412.75 spike=0.21
- EGBE.CA: score=11.57 buy_ready=False sector_rank=17 price=0.45 support=0.41 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:48 AM market time freshness=DELAYED_CURRENT RSI=35.13 liquidity=16926.41 spike=0.11
- EGCH.CA: score=25.13 buy_ready=True sector_rank=18 price=14.59 support=11.77 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=55.27 liquidity=22212186.0 spike=0.18
- EGSA.CA: score=9.36 buy_ready=False sector_rank=10 price=9.02 support=8.24 resistance=9.19 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=89.86 liquidity=2291.08 spike=0.2
- EGTS.CA: score=26.4 buy_ready=False sector_rank=2 price=19.95 support=12.9 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=70.39 liquidity=13272514.0 spike=0.12
- EHDR.CA: score=23.34 buy_ready=False sector_rank=11 price=2.75 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=76.81 liquidity=29420874.0 spike=0.59
- EKHO.CA: score=14.18 buy_ready=False sector_rank=13 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=25.4 buy_ready=True sector_rank=6 price=2.18 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=10255433.0 spike=0.33
- ELKA.CA: score=25.34 buy_ready=True sector_rank=11 price=1.33 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=68.97 liquidity=18357890.0 spike=0.46
- ELNA.CA: score=5.04 buy_ready=False sector_rank=11 price=38.29 support=38.0 resistance=42.79 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=516072.63 spike=1.59
- ELSH.CA: score=23.34 buy_ready=False sector_rank=11 price=11.76 support=7.8 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=90.09 liquidity=43617280.0 spike=0.51
- ELWA.CA: score=12.85 buy_ready=False sector_rank=11 price=2.05 support=1.79 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=81.48 liquidity=1513428.75 spike=0.53
- EMFD.CA: score=30.44 buy_ready=True sector_rank=2 price=12.46 support=9.83 resistance=12.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=67.51 liquidity=381871232.0 spike=2.02
- ENGC.CA: score=17.3 buy_ready=True sector_rank=11 price=33.79 support=32.31 resistance=35.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=39.43 liquidity=2959625.0 spike=0.24
- EOSB.CA: score=12.44 buy_ready=False sector_rank=11 price=1.42 support=1.34 resistance=1.54 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=95148.52 spike=0.84
- EPCO.CA: score=20.73 buy_ready=True sector_rank=11 price=9.49 support=8.56 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=44.2 liquidity=6389574.5 spike=0.51
- EPPK.CA: score=4.89 buy_ready=False sector_rank=11 price=11.83 support=12.0 resistance=13.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=33.18 liquidity=547507.0 spike=0.49
- ETEL.CA: score=21.13 buy_ready=False sector_rank=10 price=95.71 support=93.01 resistance=101.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=51.34 liquidity=8766655.0 spike=0.08
- ETRS.CA: score=23.34 buy_ready=False sector_rank=11 price=9.38 support=7.37 resistance=9.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=77.78 liquidity=32853926.0 spike=0.65
- EXPA.CA: score=16.54 buy_ready=False sector_rank=17 price=18.35 support=18.34 resistance=19.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=35.67 liquidity=4987095.5 spike=0.12
- FAIT.CA: score=14.08 buy_ready=False sector_rank=17 price=37.61 support=33.5 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=61.11 liquidity=523661.91 spike=0.07
- FAITA.CA: score=13.56 buy_ready=False sector_rank=17 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=6787.42 spike=0.12
- FERC.CA: score=4.53 buy_ready=False sector_rank=18 price=78.27 support=76.5 resistance=83.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=26.23 liquidity=1394841.5 spike=0.19
- FWRY.CA: score=17.46 buy_ready=False sector_rank=20 price=19.17 support=19.03 resistance=21.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=39.11 liquidity=70602752.0 spike=0.26
- GBCO.CA: score=12.4 buy_ready=False sector_rank=21 price=26.04 support=25.25 resistance=29.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=25.93 liquidity=13657016.0 spike=0.12
- GDWA.CA: score=27.38 buy_ready=True sector_rank=11 price=0.83 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=11152637.0 spike=1.02
- GGCC.CA: score=29.88 buy_ready=True sector_rank=11 price=0.44 support=0.39 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=17860310.0 spike=3.27
- GIHD.CA: score=17.54 buy_ready=True sector_rank=11 price=42.28 support=39.1 resistance=44.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=43.64 liquidity=1201322.75 spike=0.2
- GMCI.CA: score=18.34 buy_ready=False sector_rank=11 price=1.8 support=1.67 resistance=1.84 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=598390.18 spike=1.7
- GRCA.CA: score=13.58 buy_ready=False sector_rank=11 price=57.51 support=53.36 resistance=60.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=36.33 liquidity=1239874.5 spike=0.13
- GSSC.CA: score=5.6 buy_ready=False sector_rank=11 price=248.27 support=250.0 resistance=275.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=12.18 liquidity=1256170.5 spike=0.1
- GTWL.CA: score=6.11 buy_ready=False sector_rank=11 price=47.47 support=47.5 resistance=59.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=11.86 liquidity=1768739.0 spike=0.15
- HDBK.CA: score=12.63 buy_ready=False sector_rank=17 price=140.31 support=140.0 resistance=150.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=41.86 liquidity=4078832.75 spike=0.24
- HELI.CA: score=24.4 buy_ready=False sector_rank=2 price=6.48 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=53.96 liquidity=17793624.0 spike=0.09
- HRHO.CA: score=12.71 buy_ready=False sector_rank=16 price=26.78 support=26.16 resistance=30.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=34.27 liquidity=16608129.0 spike=0.08
- ICID.CA: score=17.44 buy_ready=False sector_rank=11 price=5.93 support=4.37 resistance=6.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=76.67 liquidity=4098603.0 spike=0.34
- IDRE.CA: score=20.16 buy_ready=True sector_rank=11 price=45.89 support=39.51 resistance=49.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=49.96 liquidity=5822012.5 spike=0.17
- IFAP.CA: score=8.18 buy_ready=False sector_rank=5 price=19.82 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=26.58 liquidity=3780103.25 spike=0.19
- INFI.CA: score=7.81 buy_ready=False sector_rank=11 price=101.97 support=100.05 resistance=112.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=34.14 liquidity=1468589.25 spike=0.08
- IRON.CA: score=10.82 buy_ready=False sector_rank=18 price=32.71 support=31.83 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=50.09 liquidity=1692482.25 spike=0.19
- ISMA.CA: score=21.34 buy_ready=False sector_rank=11 price=28.51 support=19.52 resistance=27.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=98.76 liquidity=15902951.0 spike=0.34
- ISMQ.CA: score=25.13 buy_ready=True sector_rank=18 price=7.77 support=7.27 resistance=8.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=51.72 liquidity=12085986.0 spike=0.21
- ISPH.CA: score=26.4 buy_ready=True sector_rank=7 price=12.47 support=10.87 resistance=12.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=66.24 liquidity=45839352.0 spike=0.33
- JUFO.CA: score=27.33 buy_ready=True sector_rank=12 price=29.55 support=26.51 resistance=29.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=54.56 liquidity=8997666.0 spike=0.18
- KABO.CA: score=24.35 buy_ready=True sector_rank=8 price=6.5 support=5.92 resistance=6.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=67.03 liquidity=9952530.0 spike=0.56
- KWIN.CA: score=16.55 buy_ready=True sector_rank=11 price=73.22 support=69.0 resistance=81.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=41.93 liquidity=2211946.25 spike=0.45
- KZPC.CA: score=12.61 buy_ready=False sector_rank=11 price=10.77 support=10.3 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=30.68 liquidity=3269962.0 spike=0.25
- LCSW.CA: score=15.68 buy_ready=False sector_rank=9 price=27.11 support=26.16 resistance=29.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=39.05 liquidity=3281849.5 spike=0.19
- LUTS.CA: score=14.34 buy_ready=False sector_rank=11 price=0.64 support=0.6 resistance=0.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=83817496.0 spike=12.9
- MAAL.CA: score=10.56 buy_ready=False sector_rank=11 price=6.04 support=5.76 resistance=6.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16362566.0 spike=1.61
- MASR.CA: score=18.26 buy_ready=False sector_rank=11 price=6.89 support=6.26 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=36.61 liquidity=5916709.5 spike=0.09
- MBSC.CA: score=24.4 buy_ready=True sector_rank=9 price=271.92 support=259.0 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=58.99 liquidity=14179279.0 spike=0.3
- MCQE.CA: score=15.96 buy_ready=True sector_rank=9 price=194.44 support=188.01 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=50.91 liquidity=1558085.25 spike=0.08
- MCRO.CA: score=23.5 buy_ready=True sector_rank=11 price=1.28 support=1.21 resistance=1.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=8163180.0 spike=0.08
- MENA.CA: score=18.51 buy_ready=True sector_rank=2 price=7.01 support=5.76 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=68.88 liquidity=2111296.75 spike=0.13
- MEPA.CA: score=24.34 buy_ready=True sector_rank=11 price=1.76 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=14446924.0 spike=0.54
- MFPC.CA: score=21.13 buy_ready=False sector_rank=18 price=42.66 support=42.55 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=40.03 liquidity=13871768.0 spike=0.13
- MFSC.CA: score=16.18 buy_ready=False sector_rank=11 price=48.14 support=33.0 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=55.64 liquidity=3835961.25 spike=0.26
- MHOT.CA: score=21.95 buy_ready=True sector_rank=1 price=31.8 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=64.7 liquidity=2552414.0 spike=0.13
- MICH.CA: score=20.94 buy_ready=True sector_rank=11 price=36.35 support=35.01 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=59.23 liquidity=4596289.5 spike=0.52
- MILS.CA: score=22.81 buy_ready=True sector_rank=11 price=146.09 support=126.02 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=48.48 liquidity=8465114.0 spike=0.3
- MIPH.CA: score=11.2 buy_ready=False sector_rank=7 price=686.12 support=640.0 resistance=729.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=33.89 liquidity=1796215.13 spike=0.36
- MOED.CA: score=4.91 buy_ready=False sector_rank=11 price=0.7 support=0.68 resistance=0.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=12.06 liquidity=1573199.5 spike=0.12
- MOIL.CA: score=17.92 buy_ready=False sector_rank=13 price=0.48 support=0.44 resistance=0.49 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=56.92 liquidity=296198.27 spike=1.72
- MOIN.CA: score=13.97 buy_ready=False sector_rank=11 price=25.35 support=23.13 resistance=26.4 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=69.6 liquidity=630606.61 spike=0.33
- MOSC.CA: score=8.13 buy_ready=False sector_rank=11 price=278.45 support=271.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=18.62 liquidity=788527.63 spike=0.04
- MPCI.CA: score=26.34 buy_ready=True sector_rank=11 price=224.44 support=182.01 resistance=224.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=52.45 liquidity=31751260.0 spike=0.33
- MPCO.CA: score=29.2 buy_ready=True sector_rank=5 price=1.87 support=1.54 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=65.22 liquidity=131602696.0 spike=2.4
- MPRC.CA: score=19.76 buy_ready=True sector_rank=11 price=33.12 support=30.1 resistance=33.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=57.82 liquidity=1416247.25 spike=0.07
- MTIE.CA: score=13.58 buy_ready=False sector_rank=21 price=9.04 support=8.71 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=45.74 liquidity=3176109.0 spike=0.1
- NAHO.CA: score=5.36 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=17721.0 spike=0.47
- NCCW.CA: score=30.68 buy_ready=True sector_rank=11 price=6.2 support=5.13 resistance=6.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=66.49 liquidity=53575508.0 spike=3.17
- NEDA.CA: score=16.09 buy_ready=False sector_rank=11 price=2.78 support=2.65 resistance=2.87 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=40.0 liquidity=850502.07 spike=1.45
- NHPS.CA: score=7.62 buy_ready=False sector_rank=11 price=68.15 support=67.56 resistance=76.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=34.42 liquidity=1280603.0 spike=0.11
- NINH.CA: score=13.64 buy_ready=False sector_rank=11 price=18.04 support=17.53 resistance=20.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=39.27 liquidity=1304731.5 spike=0.08
- NIPH.CA: score=9.4 buy_ready=False sector_rank=7 price=174.47 support=162.01 resistance=176.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=116308880.0 spike=0.97
- OBRI.CA: score=7.13 buy_ready=False sector_rank=11 price=34.32 support=34.53 resistance=39.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=22.56 liquidity=2791889.75 spike=0.2
- OCDI.CA: score=17.67 buy_ready=False sector_rank=2 price=21.21 support=20.19 resistance=23.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=39.21 liquidity=3265914.25 spike=0.07
- OCPH.CA: score=13.97 buy_ready=False sector_rank=11 price=364.81 support=350.0 resistance=409.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=8.63 liquidity=6627129.0 spike=0.4
- ODIN.CA: score=22.81 buy_ready=True sector_rank=11 price=2.12 support=1.89 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=4470239.0 spike=0.4
- OFH.CA: score=22.3 buy_ready=True sector_rank=11 price=0.65 support=0.6 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=57.55 liquidity=3957723.25 spike=0.17
- OIH.CA: score=14.4 buy_ready=False sector_rank=4 price=1.4 support=1.4 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=20.0 liquidity=17041882.0 spike=0.11
- OLFI.CA: score=15.86 buy_ready=False sector_rank=12 price=21.5 support=21.0 resistance=22.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=37.65 liquidity=3521317.25 spike=0.16
- ORAS.CA: score=7.6 buy_ready=False sector_rank=19 price=734.9 support=728.0 resistance=739.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=34759524.0 spike=1.0
- ORHD.CA: score=26.4 buy_ready=False sector_rank=2 price=37.57 support=30.56 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=72.05 liquidity=34618084.0 spike=0.16
- ORWE.CA: score=24.32 buy_ready=False sector_rank=8 price=23.62 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=70.18 liquidity=9920306.0 spike=0.21
- PHAR.CA: score=21.29 buy_ready=False sector_rank=7 price=86.98 support=83.96 resistance=92.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=35.03 liquidity=8885796.0 spike=0.24
- PHDC.CA: score=26.4 buy_ready=True sector_rank=2 price=14.85 support=12.7 resistance=16.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=63.76 liquidity=101225456.0 spike=0.22
- PHTV.CA: score=14.06 buy_ready=False sector_rank=11 price=209.63 support=201.5 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=47.65 liquidity=1722942.13 spike=0.11
- POUL.CA: score=19.23 buy_ready=True sector_rank=12 price=37.59 support=34.06 resistance=39.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=53.75 liquidity=4889221.5 spike=0.09
- PRCL.CA: score=16.71 buy_ready=True sector_rank=9 price=23.61 support=20.8 resistance=25.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=56.18 liquidity=2307800.5 spike=0.07
- PRDC.CA: score=20.91 buy_ready=True sector_rank=2 price=6.2 support=5.09 resistance=6.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=68.79 liquidity=2507338.0 spike=0.12
- PRMH.CA: score=21.85 buy_ready=False sector_rank=11 price=2.81 support=2.17 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=79.35 liquidity=8514075.0 spike=0.58
- RACC.CA: score=17.36 buy_ready=False sector_rank=11 price=9.89 support=9.56 resistance=12.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=46.45 liquidity=5024799.5 spike=0.14
- RAKT.CA: score=12.56 buy_ready=False sector_rank=11 price=23.79 support=22.1 resistance=25.49 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=43.32 liquidity=217131.34 spike=0.79
- RAYA.CA: score=25.4 buy_ready=True sector_rank=3 price=7.52 support=6.4 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=48.37 liquidity=11174370.0 spike=0.09
- RMDA.CA: score=23.03 buy_ready=True sector_rank=7 price=5.09 support=4.47 resistance=5.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=49.99 liquidity=8627863.0 spike=0.15
- ROTO.CA: score=24.42 buy_ready=True sector_rank=11 price=35.13 support=32.66 resistance=36.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=36.4 liquidity=13538021.0 spike=1.04
- RREI.CA: score=21.14 buy_ready=True sector_rank=11 price=3.66 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=49.44 liquidity=4795158.0 spike=0.2
- RTVC.CA: score=5.77 buy_ready=False sector_rank=11 price=3.85 support=3.75 resistance=4.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=30.43 liquidity=1425610.75 spike=0.23
- RUBX.CA: score=9.51 buy_ready=False sector_rank=11 price=10.32 support=9.8 resistance=11.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=30.2 liquidity=2166264.25 spike=0.13
- SAUD.CA: score=14.44 buy_ready=False sector_rank=17 price=22.6 support=21.8 resistance=25.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=42.77 liquidity=2879707.75 spike=0.18
- SCEM.CA: score=19.89 buy_ready=False sector_rank=9 price=64.44 support=61.92 resistance=72.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=39.81 liquidity=7490964.0 spike=0.17
- SCFM.CA: score=10.83 buy_ready=False sector_rank=11 price=268.37 support=260.0 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=16.54 liquidity=3490723.5 spike=0.12
- SCTS.CA: score=7.61 buy_ready=False sector_rank=14 price=621.86 support=590.01 resistance=709.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=13.63 liquidity=727559.75 spike=0.06
- SDTI.CA: score=18.19 buy_ready=True sector_rank=11 price=45.95 support=43.4 resistance=46.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=54.99 liquidity=1851878.0 spike=0.09
- SEIG.CA: score=16.8 buy_ready=False sector_rank=11 price=189.14 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=57.08 liquidity=463231.28 spike=0.07
- SIPC.CA: score=26.34 buy_ready=True sector_rank=11 price=3.72 support=3.4 resistance=3.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=51.02 liquidity=14888070.0 spike=1.0
- SKPC.CA: score=13.69 buy_ready=False sector_rank=18 price=17.0 support=16.8 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=37.93 liquidity=6558737.0 spike=0.08
- SMFR.CA: score=15.78 buy_ready=True sector_rank=11 price=209.49 support=203.51 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=42.24 liquidity=1435451.63 spike=0.12
- SNFC.CA: score=13.49 buy_ready=False sector_rank=11 price=12.18 support=11.66 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=65.58 liquidity=3148776.25 spike=0.11
- SPIN.CA: score=10.68 buy_ready=False sector_rank=8 price=14.27 support=13.69 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=43.05 liquidity=1275865.0 spike=0.26
- SPMD.CA: score=20.25 buy_ready=True sector_rank=11 price=0.42 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=64.08 liquidity=3912508.75 spike=0.17
- SUGR.CA: score=20.6 buy_ready=True sector_rank=12 price=50.08 support=47.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=56.5 liquidity=4262769.5 spike=0.26
- SVCE.CA: score=21.34 buy_ready=True sector_rank=11 price=9.22 support=7.98 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=55.5 liquidity=7001069.0 spike=0.04
- SWDY.CA: score=22.22 buy_ready=True sector_rank=6 price=87.8 support=85.25 resistance=91.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=53.16 liquidity=7820719.0 spike=0.22
- TALM.CA: score=12.57 buy_ready=False sector_rank=14 price=15.94 support=15.12 resistance=17.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=40.94 liquidity=686761.44 spike=0.05
- TMGH.CA: score=24.4 buy_ready=False sector_rank=2 price=94.97 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=55.39 liquidity=95779768.0 spike=0.17
- TRTO.CA: score=10.34 buy_ready=False sector_rank=11 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=3.91 buy_ready=False sector_rank=11 price=476.81 support=455.6 resistance=517.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=32.78 liquidity=566620.75 spike=0.31
- UEGC.CA: score=30.92 buy_ready=True sector_rank=11 price=1.53 support=1.3 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=65.22 liquidity=65824660.0 spike=3.29
- UNIP.CA: score=28.82 buy_ready=False sector_rank=11 price=0.32 support=0.28 resistance=0.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=72.0 liquidity=33668400.0 spike=2.74
- UNIT.CA: score=19.97 buy_ready=True sector_rank=2 price=13.81 support=10.83 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=56.81 liquidity=1574713.13 spike=0.16
- WCDF.CA: score=9.08 buy_ready=False sector_rank=11 price=540.04 support=535.0 resistance=561.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=12.24 liquidity=1020307.25 spike=1.36
- WKOL.CA: score=7.74 buy_ready=False sector_rank=11 price=294.83 support=290.0 resistance=349.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=28.64 liquidity=398565.94 spike=0.03
- ZEOT.CA: score=20.29 buy_ready=True sector_rank=11 price=9.33 support=8.43 resistance=9.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=47.24 liquidity=3952735.25 spike=0.44
- ZMID.CA: score=26.4 buy_ready=True sector_rank=2 price=6.02 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=40.52 liquidity=67393808.0 spike=0.34

## Backtesting Lite
- UEGC.CA: 180d return=41.75%, max drawdown=-21.74%, MA20>MA50 days last20=19, as_of=2026-06-03T21:00:00+00:00
- NCCW.CA: 180d return=-19.69%, max drawdown=-44.78%, MA20>MA50 days last20=20, as_of=2026-06-03T21:00:00+00:00
- EMFD.CA: 180d return=49.39%, max drawdown=-15.54%, MA20>MA50 days last20=20, as_of=2026-06-03T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- UEGC.CA: status=RECENT_ACCEPTED latest=2026-06-06 age_days=1 sources=2 expected=El-Saeed Company for Contracting and Real Estate Investment "SCCD" (S.A.E.) summary=Recent evidence for El-Saeed Company for Contracting and Real Estate Investment "SCCD" (S.A.E.) (UEGC.CA) includes its current trading status on the EGX, its 52-week price range, and the release of its consolidated financial statements for the year ended December 31, 2025. The company is actively involved in general and private contract works in Egypt.
  - El Saeed Contracting & RE Inv (UEGC) Stock Price Today | EGX: UEGC Live (as of June 6, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyFw53nMdxaow85HsdzCFNU6jNGOWTPMF3tD60o2MuHY-Mg9zdi8XuPgBdUbK4Vy01cuBJJbi863YmTXv-YnUyd-cyxZQR0piUwBzaIOHCIzmXEDuPhCy9A67M4XvBJKYCiXoQCKbhVu04
  - El-Saeed Company for Contracting and Real Estate Investment "SCCD" (S.A.E.) Consolidated Financial Statements for the year ended 31 December 2025 (April 2, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoKK4jvlV_GBjoe60L49wrgrNz43sH54M-Ovk2okjlJKQQ4LgW7zvYRyOIJQp6ds0CcB8EYifsH5kqz5QM7XXCEdOcFRDQ1T9LHwQD2hYgtxaBYeBhJEoPMyj6PzC-GidpVdoXx-zPc5iGI6eXATrQ
- NCCW.CA: status=RECENT_ACCEPTED latest=2026-06-06 age_days=1 sources=3 expected=Nasr Company for Civil Works summary=Nasr Company for Civil Works (NCCW.CA) has recently reported its Q1 2026 financial results, held its Annual General Meeting (AGM), and received approval from the Financial Regulatory Authority (FRA) for a capital increase via bonus shares. The company's current stock price and TTM financial ratios are also available.
  - Nasr Company for Civil Works (NCCW.CA) - AGM Minutes (after Certification) (June 6, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGskwhFze3vUzZzeObuQYrGQwmhMLnN7C2ge3O08VxS1VMaKwr5XAEVIOEpjkwwLcHnBHsxwIWz-DV5p-0KK_DGrcWYZ1Of4Tdxck5FT8nhHy6kfHbK_ozL6X_Zj6a1eOdFFGq9pWPufThLkX1Uset_fg8rNgVh62L5RIiezZ-Hvn8yRQhr8nId12sarf4cRYcbXnjc7FSleXIDiWYmsaGdVG0jEr_msdu7yfjwLiWj8yVMb664jSKfkNkze9tdrcGGgDxcDOBkISYOToa08qM2rGcY2QYIlgMnUUPhf47TToRQjzN-FCT9aSn3HnVjTtjxaFEdbxfpMkOwkNMmTIb-Lc42oLZ82ktqQX1TR_rUXABFmBykJEMoRvfAx0P8tEkWEGr7gd5qbEQcmP4WdtWa6owGC2Qx5iSTfLpu0325V-dkUOvrcqp1qmzl2q_TX-7OmzT_AxBxWqLbylIn4GisviglRrnc40AwS_urD_Qq2Ov-zA_Ej4osK8TfbJRCu2ybGf1n9IA4Aq4N_qOfCVUa7D7uQm8Ues6mgg==
  - Nasr for Civil Works posts 35.9% lower profits in Q1 2026 (May 18, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJ0URiKhwGCW-2wyk4TzrgGFypuCgi4g2r1VeAbrXjO79AD9HirsaULwRQqRVzGZ4zVlrBhnQHgtgaOihbPflg-5Xcb-ET0q2P_5juRkExnb0g_X2EQmZQOTUST5-Gx2lqouP40A1mgYqcCT2z0NEt
  - Nasr Company for Civil Works (NCCW.CA) Reports 3 Months Results (May 25, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZ3jr0uUS1qBHCEd31U809T5ylJR8EQG06-_YoymAzR4zhgfiVrKh8UwNuEVJsws2lcYqjmD_10gw7KqKl2N3YhAsvS2DxEstGoP4rVMrUTkIH3P4kjnppFWF_8ow=
- EMFD.CA: status=RECENT_ACCEPTED latest=2026-09-02 age_days=0 sources=3 expected=Emaar Misr for Development summary=Emaar Misr for Development (EMFD.CA) has recently announced its Q1 2026 consolidated profits, the departure of its CEO, and plans for residential units in its Belle Vie project. The company also released its consolidated financial statements for the year ended December 31, 2025, and has an upcoming earnings report scheduled for September 2, 2026.
  - Release from Emaar Misr for Development (EMFD.CA) Concerning the Board of Directors & the Executive Managers (June 6, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGskwhFze3vUzZzeObuQYrGQwmhMLnN7C2ge3O08VxS1VMaKwr5XAEVIOEpjkwwLcHnBHsxwIWz-DV5p-0KK_DGrcWYZ1Of4Tdxck5FT8nhHy6kfHbK_ozL6X_Zj6a1eOdFFGq9pWPufThLkX1Uset_fg8rNgVh62L5RIiezZ-Hvn8yRQhr8nId12sarf4cRYcbXnjc7FSleXIDiWYmsaGdVG0jEr_msdu7yfjwLiWj8yVMb664jSKfkNkze9tdrcGGgDxcDOBkISYOToa08qM2rGcY2QYIlgMnUUPhf47TToRQjzN-FCT9aSn3HnVjTtjxaFEdbxfpMkOwkNMmTIb-Lc42oLZ82ktqQX1TR_rUXABFmBykJEMoRvfAx0P8tEkWEGr7gd5qbEQcmP4WdtWa6owGC2Qx5iSTfLpu0325V-dkUOvrcqp1qmzl2q_TX-7OmzT_AxBxWqLbylIn4GisviglRrnc40AwS_urD_Qq2Ov-zA_Ej4osK8TfbJRCu2ybGf1n9IA4Aq4N_qOfCVUa7D7uQm8Ues6mgg==
  - Emaar Misr says no CEO appointed, Mohamed Alabbar maintains operational oversight (June 2, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHSI6FghpcQc7QuVzVq38MWv1j9b2d7rJPKe9vEVv1_Cagi37yKVrfDQAiBuEfFcjyzy7t_Hf4SKF19iEVcnie6F7wDqJBdvqgJYvM-VMfhSQjkQPkuDKPPiHNt-drH7BmShs7QHMXZBkPIT4QzZt0
  - Emaar Misr records 133.5% YoY higher consolidated profits in Q1 2026 (June 1, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHSI6FghpcQc7QuVzVq38MWv1j9b2d7rJPKe9vEVv1_Cagi37yKVrfDQAiBuEfFcjyzy7t_Hf4SKF19iEVcnie6F7wDqJBdvqgJYvM-VMfhSQjkQPkuDKPPiHNt-drH7BmShs7QHMXZBkPIT4QzZt0
- GGCC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Giza General - Contracting and Real Estate Investment S.A.E summary=EGX approves listing EGP 144m capital increase for Giza Contracting; Giza Contracting tests key EGP 0.51 level; Giza Contracting’s consolidated net profits leap to EGP 140m in 9M-25 Gemini also reviewed web evidence but did not return ticker-specific citations.
  - EGX approves listing EGP 144m capital increase for Giza Contracting: https://english.mubasher.info/news/4588793/EGX-approves-listing-EGP-144m-capital-increase-for-Giza-Contracting/
  - Giza Contracting tests key EGP 0.51 level: https://english.mubasher.info/news/4563778/Giza-Contracting-tests-key-EGP-0-51-level/
  - Giza Contracting’s consolidated net profits leap to EGP 140m in 9M-25: https://english.mubasher.info/news/4530408/Giza-Contracting-s-consolidated-net-profits-leap-to-EGP-140m-in-9M-25/
- MPCO.CA: status=RECENT_ACCEPTED latest=2026-06-01 age_days=6 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry (MPCO.CA) has recently released its consolidated and standalone financial results for Q1 2026, along with minutes from its Board of Directors meeting. The company also reported lower profits in 2025.
  - Release from Mansourah Poultry (MPCO.CA) Concerning the Board of Directors & the Executive Managers (June 1, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEk8dSt6nA-lUiauOcn4p5aZJsLXMzRcikCEHb6volv7dFkMuO0Wdgg2CXF3iz2Qj43EqzRYVRkXUqj0MJB82vFtOoGEpr1FBOC714gIb1e5EdkmFjiPBa1CoXrQKAYbvRxiXw1klhPbPDnOBq-62HB-z6MfHUB8ctmHqTt7-n7HG2v9Q1bXKXyR91kLAoTLhHGSjS3A1hc_dIUw==
  - Mansourah Poultry (MPCO.CA) - Minutes of the BoD Meeting (June 1, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEk8dSt6nA-lUiauOcn4p5aZJsLXMzRcikCEHb6volv7dFkMuO0Wdgg2CXF3iz2Qj43EqzRYVRkXUqj0MJB82vFtOoGEpr1FBOC714gIb1e5EdkmFjiPBa1CoXrQKAYbvRxiXw1klhPbPDnOBq-62HB-z6MfHUB8ctmHqTt7-n7HG2v9Q1bXKXyR91kLAoTLhHGSjS3A1hc_dIUw==
  - Mansourah Poultry (MPCO.CA) Reports its Financial Results (Consolidated) for the Period from 01/01/2026 to 31/03/2026 (June 1, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEk8dSt6nA-lUiauOcn4p5aZJsLXMzRcikCEHb6volv7dFkMuO0Wdgg2CXF3iz2Qj43EqzRYVRkXUqj0MJB82vFtOoGEpr1FBOC714gIb1e5EdkmFjiPBa1CoXrQKAYbvRxiXw1klhPbPDnOBq-62HB-z6MfHUB8ctmHqTt7-n7HG2v9Q1bXKXyR91kLAoTLhHGSjS3A1hc_dIUw==
- UNIP.CA: status=RECENT_ACCEPTED latest=2026-06-04 age_days=3 sources=3 expected=Universal For Paper and Packaging Materials summary=Universal For Paper and Packaging Materials (UNIP.CA) has seen its capital increase approved by the EGX's listing committee in September 2025. The company also reported lower consolidated profits in H1 2025.
  - EGX's listing committee approves Unipack's capital increase (September 24, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-8T0b9xdfhwJuO7p8QF41s0k1DLqTxkz3NRnditbHPbOX3luYqsvnJXVDpTa1U3c3umrzk7Jce1sdD2XkW-2yzdABynkXLzwU8d4G-zdwrA5LOuoK-pH2qQt0Vf9qTGbUPHRNe5EkgxcclskihqXe
  - Unipack sees 63.1% lower consolidated profits in H1 2025 (August 18, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-8T0b9xdfhwJuO7p8QF41s0k1DLqTxkz3NRnditbHPbOX3luYqsvnJXVDpTa1U3c3umrzk7Jce1sdD2XkW-2yzdABynkXLzwU8d4G-zdwrA5LOuoK-pH2qQt0Vf9qTGbUPHRNe5EkgxcclskihqXe
  - Universal For Paper and Packaging Materials (Unipack) (June 4, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-m8F0ijZph4SMsxH6DZobXoTPKm6U2QDNeY3GTL65dbbRtm3dvy1V6vn7VpICnicZV7cWOWon6eDpe7tRdbrwp9bazubiEbKg84eDorwboWrphYpPDjePjKAjb3E-JHPMBJqzc8Ud9u6qzpIleT_H3huf6LuJeg==
- COSG.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Oil & Soap Company summary=Cairo Oils stock stabilizes above EGP 1.50 resistance level; EGX approves capital increase, reduction of several listed firms; Cairo oils incurs EGP 25m losses in H1-19 Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Cairo Oils stock stabilizes above EGP 1.50 resistance level: https://english.mubasher.info/news/4546423/Cairo-Oils-stock-stabilizes-above-EGP-1-50-resistance-level/
  - EGX approves capital increase, reduction of several listed firms: https://english.mubasher.info/news/3828111/EGX-approves-capital-increase-reduction-of-several-listed-firms/
  - Cairo oils incurs EGP 25m losses in H1-19: https://english.mubasher.info/news/3521392/Cairo-oils-incurs-EGP-25m-losses-in-H1-19/
- ARAB.CA: status=RECENT_ACCEPTED latest=2026-06-01 age_days=6 sources=3 expected=Arab Developers Holding summary=Arab Developers Holding (ARAB.CA) has recently held its Annual General Meeting (AGM) and announced a significant investment plan for 2025, aiming to inject EGP 3.25 billion into the Egyptian real estate sector. The company also reported its 2025 consolidated profits and set an opening price for subscription rights related to a capital increase.
  - ARAB Developers Holding (PORT.CA) - AGM Decisions (June 1, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEk8dSt6nA-lUiauOcn4p5aZJsLXMzRcikCEHb6volv7dFkMuO0Wdgg2CXF3iz2Qj43EqzRYVRkXUqj0MJB82vFtOoGEpr1FBOC714gIb1e5EdkmFjiPBa1CoXrQKAYbvRxiXw1klhPbPDnOBq-62HB-z6MfHUB8ctmHqTt7-n7HG2v9Q1bXKXyR91kLAoTLhHGSjS3A1hc_dIUw==
  - Arab Developers Holding's 2025 consolidated profits up 4.7% YoY (April 30, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYxlqqKpwrH_v4JTYEmZXOkrDuoDWvQYbyr0Gc1vHp14NABq4D6JocRKNoR-AtpPZrvYSjPsTgTBr1M7o2Iqa_qorBF36dDduhGjB65B65TKWhaS2VbiTYOelIrA08KHaUcAII0vNW48ugIZgGJvu3
  - Arab Developers Holding sets EGP 0.070 opening price for subscription rights (April 1, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYxlqqKpwrH_v4JTYEmZXOkrDuoDWvQYbyr0Gc1vHp14NABq4D6JocRKNoR-AtpPZrvYSjPsTgTBr1M7o2Iqa_qorBF36dDduhGjB65B65TKWhaS2VbiTYOelIrA08KHaUcAII0vNW48ugIZgGJvu3

## Warnings
- Evidence for GGCC.CA matches the company but no source/report date was detected.
- Evidence for COSG.CA matches the company but no source/report date was detected.
