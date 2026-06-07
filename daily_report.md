# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-06-07T14:28:50.480503+00:00
Generated Cairo: 2026-06-07 17:28
Run timing: target 15:30 Cairo | generated Cairo 2026-06-07 17:28 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-06-07 17:25

## Control Center
- Action tickets: 1 prioritized signal(s)
- BUY-ready candidates: 77
- Data quality issues: 0
- Tradeable price/liquidity tickers: 178/190
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, June 07
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 30.0% / above MA50 75.0%
- EGX70 regime: CONSTRUCTIVE / above MA20 56.41% / above MA50 82.05%
- Sector breadth: 76.19%
- Risk mode: SELECTIVE_SMALL_MID_SWINGS

## Top Liquidity
- CCAP.CA: liquidity=1307626624.0 spike=1.6 score=9.32
- EMFD.CA: liquidity=964109248.0 spike=5.11 score=31.4
- FWRY.CA: liquidity=375867104.0 spike=1.37 score=18.64
- PHDC.CA: liquidity=288366400.0 spike=0.64 score=24.4
- TMGH.CA: liquidity=225499808.0 spike=0.41 score=22.4

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner highlighted EMFD.CA as the top BUY‑watch candidate. It cleared liquidity thresholds, trades above its 20‑ and 50‑day MAs, and sits at a strong resistance level (12.38 EGP) with RSI 67.5, suggesting short‑term bullish pressure despite an overall bearish EGX30 and a constructive EGX70 backdrop. The market regime is in SELECTIVE_SMALL_MID_SWINGS, meaning risk is limited to selective setups; sector breadth is healthy (76%) but Real Estate is not a leading sector, adding uncertainty.
- EMFD.CA shows strong price momentum (above MA20/MA50, RSI 67.5) but is far from its 20‑day support (9.83 EGP).
- Liquidity spike (5.1×) and accumulation regime support a short‑term watch, yet sector lag and extended momentum raise risk.
- EGX30 remains bearish while EGX70 is constructive; this mixed regime pushes the risk mode to selective small‑mid swings.
- Next 1‑3 days outlook hinges on price breaking the 12.38 EGP resistance; failure may pull back toward support.
- Uncertainty remains high due to low confidence score and sector not leading the market.

## Top Liquidity Spikes
- LUTS.CA: spike=22.07 liquidity=143389760.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- UNIP.CA: spike=5.31 liquidity=65309568.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AREH.CA: spike=5.11 liquidity=109493552.0 outlook=BULLISH_WATCH score=90.08 buy_ready=True
- EMFD.CA: spike=5.11 liquidity=964109248.0 outlook=BULLISH_WATCH score=78.7 buy_ready=True
- NCCW.CA: spike=4.85 liquidity=81983472.0 outlook=BULLISH_WATCH score=72.08 buy_ready=True

## Sector Leaderboard
- #1 Tourism & Leisure: score=12.13 5d=4.25% 20d=18.02% aboveMA50=100.0%
- #2 Technology & Distribution: score=11.06 5d=0.94% 20d=18.9% aboveMA50=100.0%
- #3 Agriculture & Food Production: score=9.47 5d=6.74% 20d=2.37% aboveMA50=50.0%
- #4 Textiles: score=7.97 5d=2.4% 20d=6.38% aboveMA50=75.0%
- #5 Industrial Goods & Cables: score=7.88 5d=2.04% 20d=1.18% aboveMA50=100.0%
- #6 Telecommunications: score=7.86 5d=-0.81% 20d=7.59% aboveMA50=100.0%
- #7 Healthcare: score=7.51 5d=3.52% 20d=4.36% aboveMA50=83.33%
- #8 Building Materials: score=6.74 5d=0.82% 20d=5.21% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- Priority #1: BUY EMFD.CA
  - Entry: 12.38 | Take profit: 13.38 | Stop loss: 11.88
  - Confidence: LOW | score=31.4 | outlook=BULLISH_WATCH 78.7
  - Reason: WATCH/BUY SETUP: EMFD.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 67.51, support 9.83, resistance 12.38, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MPCO.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- AREH.CA: BULLISH_WATCH score=90.08 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- MPRC.CA: BULLISH_WATCH score=90.08 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- SIPC.CA: BULLISH_WATCH score=88.08 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- KABO.CA: BULLISH_WATCH score=86.97 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- GDWA.CA: BULLISH_WATCH score=85.08 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance; sector is not leading
- ODIN.CA: BULLISH_WATCH score=84.08 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- CLHO.CA: BULLISH_WATCH score=83.51 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- GGCC.CA: BULLISH_WATCH score=83.08 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- ELKA.CA: BULLISH_WATCH score=83.08 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading

## BUY-Ready Candidates
- AREH.CA: rank=33.4 outlook=BULLISH_WATCH outlook_score=90.08 sector_rank=11 price=1.47 support=1.27 resistance=1.43 liquidity=109493552.0
- COSG.CA: rank=32.68 outlook=BULLISH_WATCH outlook_score=82.08 sector_rank=11 price=1.65 support=1.44 resistance=1.71 liquidity=161625088.0
- MPCO.CA: rank=32.4 outlook=BULLISH_WATCH outlook_score=100 sector_rank=3 price=1.77 support=1.54 resistance=1.88 liquidity=221589648.0
- EMFD.CA: rank=31.4 outlook=BULLISH_WATCH outlook_score=78.7 sector_rank=9 price=12.38 support=9.83 resistance=12.38 liquidity=964109248.0
- UEGC.CA: rank=31.4 outlook=BULLISH_WATCH outlook_score=82.08 sector_rank=11 price=1.5 support=1.3 resistance=1.46 liquidity=96498128.0
- NCCW.CA: rank=31.4 outlook=BULLISH_WATCH outlook_score=72.08 sector_rank=11 price=6.19 support=5.13 resistance=6.2 liquidity=81983472.0
- GGCC.CA: rank=30.4 outlook=BULLISH_WATCH outlook_score=83.08 sector_rank=11 price=0.43 support=0.39 resistance=0.44 liquidity=24663022.0
- MPRC.CA: rank=30.2 outlook=BULLISH_WATCH outlook_score=90.08 sector_rank=11 price=34.0 support=30.1 resistance=33.7 liquidity=35967752.0
- GDWA.CA: rank=30.02 outlook=BULLISH_WATCH outlook_score=85.08 sector_rank=11 price=0.82 support=0.77 resistance=0.83 liquidity=25407232.0
- MHOT.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=82 sector_rank=1 price=30.83 support=26.3 resistance=34.3 liquidity=10836366.0

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=16.05 buy_ready=True sector_rank=11 price=211.7 support=195.1 resistance=249.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=40.2 liquidity=1645972.75 spike=0.08
- ABUK.CA: score=18.28 buy_ready=False sector_rank=17 price=81.45 support=81.52 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.92 liquidity=62821632.0 spike=0.48
- ACAMD.CA: score=27.2 buy_ready=True sector_rank=11 price=2.37 support=1.94 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=63.64 liquidity=155486864.0 spike=1.4
- ACGC.CA: score=24.4 buy_ready=True sector_rank=4 price=9.96 support=8.3 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.34 liquidity=44443548.0 spike=0.83
- ADCI.CA: score=16.91 buy_ready=True sector_rank=11 price=214.84 support=198.0 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.01 liquidity=2508676.5 spike=0.34
- ADIB.CA: score=21.51 buy_ready=False sector_rank=16 price=46.97 support=44.45 resistance=50.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.38 liquidity=48274260.0 spike=0.28
- ADPC.CA: score=22.4 buy_ready=False sector_rank=11 price=3.72 support=3.54 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.35 liquidity=11465918.0 spike=0.47
- AFDI.CA: score=26.4 buy_ready=True sector_rank=11 price=44.37 support=36.82 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.02 liquidity=10984151.0 spike=0.59
- AFMC.CA: score=18.72 buy_ready=False sector_rank=11 price=73.43 support=69.33 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.17 liquidity=6321443.5 spike=0.44
- AJWA.CA: score=20.58 buy_ready=True sector_rank=11 price=135.09 support=130.01 resistance=139.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.23 liquidity=6181386.0 spike=0.57
- ALCN.CA: score=20.76 buy_ready=False sector_rank=13 price=29.12 support=28.4 resistance=30.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=45.19 liquidity=9772990.0 spike=0.36
- ALUM.CA: score=24.4 buy_ready=True sector_rank=11 price=25.55 support=22.35 resistance=26.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.39 liquidity=10095958.0 spike=0.45
- AMER.CA: score=24.4 buy_ready=True sector_rank=9 price=2.68 support=2.29 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.4 liquidity=26348478.0 spike=0.2
- AMES.CA: score=9.59 buy_ready=False sector_rank=11 price=50.79 support=48.0 resistance=59.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=21.16 liquidity=2192341.25 spike=0.18
- AMIA.CA: score=19.4 buy_ready=False sector_rank=11 price=8.94 support=8.16 resistance=10.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.86 liquidity=12508616.0 spike=0.36
- AMOC.CA: score=19.34 buy_ready=False sector_rank=12 price=8.19 support=8.12 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.38 liquidity=54485620.0 spike=0.63
- ANFI.CA: score=13.04 buy_ready=False sector_rank=11 price=14.05 support=13.5 resistance=15.55 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=24.73 liquidity=5638883.28 spike=0.28
- APSW.CA: score=12.96 buy_ready=False sector_rank=11 price=8.91 support=8.62 resistance=9.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=49.5 liquidity=1361244.75 spike=1.1
- ARAB.CA: score=26.4 buy_ready=True sector_rank=9 price=0.21 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.72 liquidity=46812412.0 spike=0.61
- ARCC.CA: score=26.4 buy_ready=True sector_rank=8 price=59.07 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.59 liquidity=40844380.0 spike=0.92
- AREH.CA: score=33.4 buy_ready=True sector_rank=11 price=1.47 support=1.27 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=109493552.0 spike=5.11
- ARVA.CA: score=28.04 buy_ready=True sector_rank=11 price=11.09 support=7.71 resistance=10.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=45538488.0 spike=1.82
- ASCM.CA: score=25.14 buy_ready=True sector_rank=11 price=56.45 support=43.76 resistance=59.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=65.89 liquidity=84011128.0 spike=1.37
- ASPI.CA: score=13.64 buy_ready=False sector_rank=11 price=0.36 support=0.35 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=145819200.0 spike=3.12
- ATLC.CA: score=14.77 buy_ready=False sector_rank=14 price=5.0 support=4.71 resistance=5.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=32.53 liquidity=5792082.0 spike=0.72
- ATQA.CA: score=25.28 buy_ready=True sector_rank=17 price=9.92 support=9.41 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.67 liquidity=23882086.0 spike=0.49
- AXPH.CA: score=9.01 buy_ready=False sector_rank=11 price=1128.27 support=960.0 resistance=1239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=7.55 liquidity=1605974.88 spike=0.28
- BINV.CA: score=20.22 buy_ready=True sector_rank=18 price=46.35 support=40.5 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=67.08 liquidity=7103227.5 spike=0.53
- BIOC.CA: score=18.1 buy_ready=True sector_rank=11 price=74.36 support=70.0 resistance=79.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.46 liquidity=3696964.75 spike=0.47
- BTFH.CA: score=20.98 buy_ready=False sector_rank=14 price=3.07 support=3.03 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.17 liquidity=171629136.0 spike=0.7
- CAED.CA: score=9.78 buy_ready=False sector_rank=11 price=70.73 support=64.49 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.28 liquidity=2383241.25 spike=0.16
- CANA.CA: score=25.95 buy_ready=True sector_rank=16 price=37.0 support=33.15 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=44.06 liquidity=16823644.0 spike=1.22
- CCAP.CA: score=9.32 buy_ready=False sector_rank=18 price=5.72 support=5.26 resistance=5.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1307626624.0 spike=1.6
- CCRS.CA: score=22.58 buy_ready=True sector_rank=11 price=2.56 support=1.98 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.79 liquidity=29980338.0 spike=1.09
- CEFM.CA: score=10.25 buy_ready=False sector_rank=11 price=106.48 support=103.07 resistance=119.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=28.81 liquidity=2846049.0 spike=0.38
- CERA.CA: score=21.4 buy_ready=True sector_rank=11 price=1.18 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=8001599.0 spike=0.58
- CFGH.CA: score=4.61 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=6311.86 spike=1.6
- CICH.CA: score=8.22 buy_ready=False sector_rank=14 price=12.3 support=10.9 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.16 liquidity=1244898.75 spike=0.28
- CIEB.CA: score=16.41 buy_ready=False sector_rank=16 price=23.55 support=23.31 resistance=24.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.48 liquidity=4896029.5 spike=0.39
- CIRA.CA: score=20.74 buy_ready=True sector_rank=15 price=26.81 support=19.5 resistance=28.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.77 liquidity=6783402.0 spike=0.24
- CLHO.CA: score=24.4 buy_ready=True sector_rank=7 price=15.81 support=14.58 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.56 liquidity=13126311.0 spike=0.34
- CNFN.CA: score=15.98 buy_ready=False sector_rank=14 price=4.53 support=4.41 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.26 liquidity=10758919.0 spike=0.67
- COMI.CA: score=21.51 buy_ready=False sector_rank=16 price=131.8 support=131.3 resistance=144.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.39 liquidity=180260384.0 spike=0.28
- COPR.CA: score=19.12 buy_ready=False sector_rank=11 price=0.36 support=0.3 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.27 liquidity=50625912.0 spike=1.36
- COSG.CA: score=32.68 buy_ready=True sector_rank=11 price=1.65 support=1.44 resistance=1.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.89 liquidity=161625088.0 spike=3.14
- CPCI.CA: score=13.14 buy_ready=False sector_rank=11 price=363.02 support=336.0 resistance=374.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=75.65 liquidity=1741300.0 spike=0.23
- CSAG.CA: score=27.83 buy_ready=True sector_rank=13 price=31.8 support=30.4 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=9846907.0 spike=0.49
- DAPH.CA: score=17.4 buy_ready=False sector_rank=11 price=81.04 support=79.25 resistance=96.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=17.24 liquidity=17191020.0 spike=0.54
- DEIN.CA: score=10.4 buy_ready=False sector_rank=11 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=10.28 buy_ready=False sector_rank=10 price=24.51 support=24.7 resistance=26.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.39 liquidity=4239266.5 spike=1.82
- DSCW.CA: score=22.4 buy_ready=False sector_rank=11 price=1.84 support=1.71 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.83 liquidity=38543224.0 spike=0.58
- DTPP.CA: score=9.1 buy_ready=False sector_rank=11 price=124.68 support=121.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=28.41 liquidity=1698442.75 spike=0.27
- EALR.CA: score=14.12 buy_ready=False sector_rank=11 price=357.24 support=346.01 resistance=429.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.9 liquidity=1721883.0 spike=0.09
- EASB.CA: score=17.0 buy_ready=True sector_rank=11 price=5.0 support=4.61 resistance=5.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=2117370.0 spike=1.24
- EAST.CA: score=24.4 buy_ready=True sector_rank=10 price=38.87 support=37.01 resistance=39.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.01 liquidity=19641070.0 spike=0.28
- EBSC.CA: score=18.98 buy_ready=True sector_rank=11 price=1.89 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=68.29 liquidity=2581880.25 spike=0.86
- ECAP.CA: score=17.06 buy_ready=True sector_rank=11 price=31.05 support=28.7 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=51.75 liquidity=2658012.75 spike=0.5
- EDFM.CA: score=13.07 buy_ready=False sector_rank=11 price=333.99 support=320.2 resistance=364.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=48.99 liquidity=672200.88 spike=0.59
- EEII.CA: score=22.54 buy_ready=True sector_rank=11 price=2.38 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.48 liquidity=8141553.5 spike=0.44
- EFIC.CA: score=4.66 buy_ready=False sector_rank=17 price=204.66 support=195.25 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.74 liquidity=1383568.0 spike=0.31
- EFID.CA: score=24.4 buy_ready=False sector_rank=10 price=28.73 support=27.49 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=71.91 liquidity=20029866.0 spike=0.42
- EFIH.CA: score=20.9 buy_ready=False sector_rank=19 price=21.84 support=21.0 resistance=22.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.51 liquidity=28816540.0 spike=0.45
- EGAL.CA: score=23.28 buy_ready=True sector_rank=17 price=324.12 support=295.0 resistance=344.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.9 liquidity=25145726.0 spike=0.22
- EGAS.CA: score=25.13 buy_ready=True sector_rank=12 price=50.53 support=46.51 resistance=51.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=60.23 liquidity=8789030.0 spike=0.5
- EGBE.CA: score=11.55 buy_ready=False sector_rank=16 price=0.44 support=0.41 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=35.13 liquidity=35931.32 spike=0.24
- EGCH.CA: score=25.28 buy_ready=True sector_rank=17 price=14.5 support=11.77 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.27 liquidity=55194400.0 spike=0.45
- EGSA.CA: score=12.34 buy_ready=False sector_rank=6 price=8.97 support=8.24 resistance=9.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=89.86 liquidity=39240.12 spike=2.45
- EGTS.CA: score=9.4 buy_ready=False sector_rank=9 price=17.85 support=17.61 resistance=20.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=103422616.0 spike=0.96
- EHDR.CA: score=24.32 buy_ready=False sector_rank=11 price=2.66 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.81 liquidity=73619440.0 spike=1.46
- EKHO.CA: score=14.34 buy_ready=False sector_rank=12 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=25.4 buy_ready=True sector_rank=5 price=2.19 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=22464240.0 spike=0.73
- ELKA.CA: score=26.6 buy_ready=True sector_rank=11 price=1.27 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.97 liquidity=63230380.0 spike=1.6
- ELNA.CA: score=7.72 buy_ready=False sector_rank=11 price=39.54 support=38.0 resistance=42.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=322573.06 spike=0.74
- ELSH.CA: score=10.14 buy_ready=False sector_rank=11 price=11.32 support=11.25 resistance=12.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=117770504.0 spike=1.37
- ELWA.CA: score=15.37 buy_ready=False sector_rank=11 price=2.03 support=1.79 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=81.48 liquidity=3512981.25 spike=1.23
- EMFD.CA: score=31.4 buy_ready=True sector_rank=9 price=12.38 support=9.83 resistance=12.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.51 liquidity=964109248.0 spike=5.11
- ENGC.CA: score=23.77 buy_ready=True sector_rank=11 price=33.82 support=32.31 resistance=35.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.43 liquidity=9370943.0 spike=0.76
- EOSB.CA: score=12.5 buy_ready=False sector_rank=11 price=1.42 support=1.34 resistance=1.54 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=95148.52 spike=0.84
- EPCO.CA: score=24.4 buy_ready=True sector_rank=11 price=9.22 support=8.56 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=44.2 liquidity=11777543.0 spike=0.94
- EPPK.CA: score=6.05 buy_ready=False sector_rank=11 price=11.93 support=12.0 resistance=13.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=33.18 liquidity=1314155.25 spike=1.17
- ETEL.CA: score=22.4 buy_ready=False sector_rank=6 price=95.82 support=93.01 resistance=101.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=51.34 liquidity=49546600.0 spike=0.44
- ETRS.CA: score=23.4 buy_ready=False sector_rank=11 price=9.2 support=7.37 resistance=9.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.78 liquidity=46934448.0 spike=0.93
- EXPA.CA: score=10.47 buy_ready=False sector_rank=16 price=19.99 support=18.34 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=83785568.0 spike=1.98
- FAIT.CA: score=14.95 buy_ready=True sector_rank=16 price=37.48 support=33.5 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=61.11 liquidity=1434135.0 spike=0.19
- FAITA.CA: score=15.0 buy_ready=False sector_rank=16 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=92609.59 spike=1.7
- FERC.CA: score=6.13 buy_ready=False sector_rank=17 price=77.32 support=76.5 resistance=83.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.23 liquidity=2857775.5 spike=0.4
- FWRY.CA: score=18.64 buy_ready=False sector_rank=19 price=18.7 support=19.03 resistance=21.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.11 liquidity=375867104.0 spike=1.37
- GBCO.CA: score=11.56 buy_ready=False sector_rank=21 price=25.63 support=25.25 resistance=29.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=25.93 liquidity=58640820.0 spike=0.5
- GDWA.CA: score=30.02 buy_ready=True sector_rank=11 price=0.82 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=25407232.0 spike=2.31
- GGCC.CA: score=30.4 buy_ready=True sector_rank=11 price=0.43 support=0.39 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=24663022.0 spike=4.52
- GIHD.CA: score=18.47 buy_ready=True sector_rank=11 price=42.0 support=39.1 resistance=44.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.64 liquidity=2074181.0 spike=0.35
- GMCI.CA: score=16.72 buy_ready=False sector_rank=11 price=1.78 support=1.67 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=317571.88 spike=0.81
- GRCA.CA: score=17.66 buy_ready=False sector_rank=11 price=55.28 support=53.36 resistance=60.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.33 liquidity=8259327.0 spike=0.87
- GSSC.CA: score=7.38 buy_ready=False sector_rank=11 price=248.44 support=250.0 resistance=275.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=12.18 liquidity=2976408.75 spike=0.25
- GTWL.CA: score=9.49 buy_ready=False sector_rank=11 price=46.45 support=47.5 resistance=59.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=11.86 liquidity=5088305.0 spike=0.43
- HDBK.CA: score=18.51 buy_ready=False sector_rank=16 price=140.09 support=140.0 resistance=150.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.86 liquidity=10513954.0 spike=0.61
- HELI.CA: score=22.4 buy_ready=False sector_rank=9 price=6.45 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.96 liquidity=55449080.0 spike=0.29
- HRHO.CA: score=12.98 buy_ready=False sector_rank=14 price=26.51 support=26.16 resistance=30.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.27 liquidity=116876512.0 spike=0.56
- ICID.CA: score=23.72 buy_ready=False sector_rank=11 price=6.01 support=4.37 resistance=6.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.67 liquidity=13883286.0 spike=1.16
- IDRE.CA: score=24.4 buy_ready=True sector_rank=11 price=45.0 support=39.51 resistance=49.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=49.96 liquidity=13452404.0 spike=0.39
- IFAP.CA: score=12.64 buy_ready=False sector_rank=3 price=19.63 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.58 liquidity=7244345.0 spike=0.37
- INFI.CA: score=14.45 buy_ready=False sector_rank=11 price=100.34 support=100.05 resistance=112.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.14 liquidity=8045240.5 spike=0.44
- IRON.CA: score=13.61 buy_ready=False sector_rank=17 price=32.39 support=31.83 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.09 liquidity=4332446.5 spike=0.49
- ISMA.CA: score=9.4 buy_ready=False sector_rank=11 price=29.2 support=27.79 resistance=29.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=44192104.0 spike=0.94
- ISMQ.CA: score=25.28 buy_ready=True sector_rank=17 price=7.67 support=7.27 resistance=8.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.72 liquidity=30053200.0 spike=0.53
- ISPH.CA: score=26.4 buy_ready=True sector_rank=7 price=12.65 support=10.87 resistance=12.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.24 liquidity=116752640.0 spike=0.83
- JUFO.CA: score=28.4 buy_ready=True sector_rank=10 price=29.42 support=26.51 resistance=29.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.56 liquidity=23354796.0 spike=0.47
- KABO.CA: score=27.24 buy_ready=True sector_rank=4 price=6.37 support=5.92 resistance=6.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=67.03 liquidity=43140724.0 spike=2.42
- KWIN.CA: score=18.84 buy_ready=True sector_rank=11 price=72.99 support=69.0 resistance=81.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.93 liquidity=4441173.0 spike=0.91
- KZPC.CA: score=13.95 buy_ready=False sector_rank=11 price=10.69 support=10.3 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.68 liquidity=6549776.5 spike=0.49
- LCSW.CA: score=18.42 buy_ready=False sector_rank=8 price=27.03 support=26.16 resistance=29.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.05 liquidity=6018473.5 spike=0.34
- LUTS.CA: score=14.4 buy_ready=False sector_rank=11 price=0.66 support=0.6 resistance=0.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=143389760.0 spike=22.07
- MAAL.CA: score=27.2 buy_ready=False sector_rank=11 price=5.9 support=4.44 resistance=5.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=93.43 liquidity=29449250.0 spike=2.9
- MASR.CA: score=22.4 buy_ready=False sector_rank=11 price=6.75 support=6.26 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.61 liquidity=25552884.0 spike=0.38
- MBSC.CA: score=22.4 buy_ready=False sector_rank=8 price=270.7 support=259.0 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.99 liquidity=30768692.0 spike=0.66
- MCQE.CA: score=20.12 buy_ready=True sector_rank=8 price=194.02 support=188.01 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.91 liquidity=5721531.0 spike=0.28
- MCRO.CA: score=25.4 buy_ready=True sector_rank=11 price=1.27 support=1.21 resistance=1.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=40816684.0 spike=0.39
- MENA.CA: score=9.4 buy_ready=False sector_rank=9 price=6.7 support=6.5 resistance=7.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12192957.0 spike=0.76
- MEPA.CA: score=24.4 buy_ready=True sector_rank=11 price=1.74 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=23847984.0 spike=0.89
- MFPC.CA: score=21.28 buy_ready=False sector_rank=17 price=42.39 support=42.55 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.03 liquidity=34424468.0 spike=0.31
- MFSC.CA: score=18.41 buy_ready=False sector_rank=11 price=48.15 support=33.0 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.64 liquidity=6010955.0 spike=0.41
- MHOT.CA: score=29.4 buy_ready=True sector_rank=1 price=30.83 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.7 liquidity=10836366.0 spike=0.55
- MICH.CA: score=25.43 buy_ready=True sector_rank=11 price=36.95 support=35.01 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=59.23 liquidity=9010063.0 spike=1.01
- MILS.CA: score=24.4 buy_ready=True sector_rank=11 price=144.3 support=126.02 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.48 liquidity=17080582.0 spike=0.6
- MIPH.CA: score=13.94 buy_ready=False sector_rank=7 price=651.6 support=640.0 resistance=729.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=33.89 liquidity=6084604.0 spike=1.23
- MOED.CA: score=7.5 buy_ready=False sector_rank=11 price=0.7 support=0.68 resistance=0.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=12.06 liquidity=4096240.5 spike=0.3
- MOIL.CA: score=16.42 buy_ready=False sector_rank=12 price=0.47 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.92 liquidity=79872.22 spike=0.4
- MOIN.CA: score=13.71 buy_ready=False sector_rank=11 price=25.05 support=23.13 resistance=26.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=69.6 liquidity=306226.84 spike=0.1
- MOSC.CA: score=11.42 buy_ready=False sector_rank=11 price=268.65 support=271.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=18.62 liquidity=4023972.0 spike=0.19
- MPCI.CA: score=26.4 buy_ready=True sector_rank=11 price=221.16 support=182.01 resistance=224.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.45 liquidity=81572880.0 spike=0.84
- MPCO.CA: score=32.4 buy_ready=True sector_rank=3 price=1.77 support=1.54 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.22 liquidity=221589648.0 spike=4.03
- MPRC.CA: score=30.2 buy_ready=True sector_rank=11 price=34.0 support=30.1 resistance=33.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.82 liquidity=35967752.0 spike=1.9
- MTIE.CA: score=18.1 buy_ready=False sector_rank=21 price=9.02 support=8.71 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=45.74 liquidity=7536265.0 spike=0.24
- NAHO.CA: score=5.44 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=35265.36 spike=0.94
- NCCW.CA: score=31.4 buy_ready=True sector_rank=11 price=6.19 support=5.13 resistance=6.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.49 liquidity=81983472.0 spike=4.85
- NEDA.CA: score=17.03 buy_ready=True sector_rank=11 price=2.83 support=2.65 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=1387299.63 spike=1.62
- NHPS.CA: score=11.61 buy_ready=False sector_rank=11 price=68.58 support=67.56 resistance=76.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.42 liquidity=5205260.0 spike=0.43
- NINH.CA: score=14.91 buy_ready=False sector_rank=11 price=18.04 support=17.53 resistance=20.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.27 liquidity=2512808.75 spike=0.16
- NIPH.CA: score=10.82 buy_ready=False sector_rank=7 price=171.35 support=162.01 resistance=176.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=205059776.0 spike=1.71
- OBRI.CA: score=10.08 buy_ready=False sector_rank=11 price=34.51 support=34.53 resistance=39.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=22.56 liquidity=5679295.5 spike=0.4
- OCDI.CA: score=22.4 buy_ready=False sector_rank=9 price=21.28 support=20.19 resistance=23.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.21 liquidity=20810604.0 spike=0.46
- OCPH.CA: score=17.22 buy_ready=False sector_rank=11 price=359.96 support=350.0 resistance=409.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=8.63 liquidity=9821009.0 spike=0.59
- ODIN.CA: score=27.27 buy_ready=True sector_rank=11 price=2.08 support=1.89 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=8870722.0 spike=0.8
- OFH.CA: score=28.4 buy_ready=True sector_rank=11 price=0.64 support=0.6 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=57.55 liquidity=16620067.0 spike=0.71
- OIH.CA: score=13.12 buy_ready=False sector_rank=18 price=1.36 support=1.4 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=20.0 liquidity=60827004.0 spike=0.4
- OLFI.CA: score=22.29 buy_ready=False sector_rank=10 price=21.56 support=21.0 resistance=22.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.65 liquidity=9894863.0 spike=0.44
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=731.49 support=728.0 resistance=739.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=124062552.0 spike=1.0
- ORHD.CA: score=24.4 buy_ready=False sector_rank=9 price=36.9 support=30.56 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.05 liquidity=107722704.0 spike=0.51
- ORWE.CA: score=24.4 buy_ready=False sector_rank=4 price=23.7 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.18 liquidity=39326808.0 spike=0.82
- PHAR.CA: score=22.4 buy_ready=False sector_rank=7 price=86.6 support=83.96 resistance=92.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.03 liquidity=29802204.0 spike=0.81
- PHDC.CA: score=24.4 buy_ready=True sector_rank=9 price=14.82 support=12.7 resistance=16.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=63.76 liquidity=288366400.0 spike=0.64
- PHTV.CA: score=16.94 buy_ready=False sector_rank=11 price=207.15 support=201.5 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=47.65 liquidity=4538393.5 spike=0.29
- POUL.CA: score=24.4 buy_ready=True sector_rank=10 price=37.45 support=34.06 resistance=39.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.75 liquidity=10232237.0 spike=0.19
- PRCL.CA: score=24.4 buy_ready=True sector_rank=8 price=24.47 support=20.8 resistance=25.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.18 liquidity=23117896.0 spike=0.72
- PRDC.CA: score=26.4 buy_ready=True sector_rank=9 price=6.19 support=5.09 resistance=6.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=68.79 liquidity=12609026.0 spike=0.62
- PRMH.CA: score=24.24 buy_ready=False sector_rank=11 price=2.79 support=2.17 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.35 liquidity=20802628.0 spike=1.42
- RACC.CA: score=21.75 buy_ready=False sector_rank=11 price=9.92 support=9.56 resistance=12.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.45 liquidity=9354134.0 spike=0.26
- RAKT.CA: score=12.62 buy_ready=False sector_rank=11 price=23.79 support=22.1 resistance=25.49 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=43.32 liquidity=217131.34 spike=0.79
- RAYA.CA: score=26.4 buy_ready=True sector_rank=2 price=7.71 support=6.4 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=48.37 liquidity=71667696.0 spike=0.6
- RMDA.CA: score=24.4 buy_ready=True sector_rank=7 price=5.15 support=4.47 resistance=5.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.99 liquidity=39219812.0 spike=0.69
- ROTO.CA: score=25.56 buy_ready=True sector_rank=11 price=34.13 support=32.66 resistance=36.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=36.4 liquidity=20517060.0 spike=1.58
- RREI.CA: score=26.4 buy_ready=True sector_rank=11 price=3.59 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.44 liquidity=15702375.0 spike=0.67
- RTVC.CA: score=10.75 buy_ready=False sector_rank=11 price=3.8 support=3.75 resistance=4.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.43 liquidity=6334241.5 spike=1.01
- RUBX.CA: score=10.95 buy_ready=False sector_rank=11 price=10.19 support=9.8 resistance=11.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=30.2 liquidity=4548065.5 spike=0.27
- SAUD.CA: score=19.32 buy_ready=False sector_rank=16 price=22.41 support=21.8 resistance=25.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=42.77 liquidity=7803240.5 spike=0.49
- SCEM.CA: score=22.4 buy_ready=False sector_rank=8 price=64.31 support=61.92 resistance=72.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.81 liquidity=22117616.0 spike=0.5
- SCFM.CA: score=13.21 buy_ready=False sector_rank=11 price=263.46 support=260.0 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=16.54 liquidity=5811548.5 spike=0.2
- SCTS.CA: score=9.19 buy_ready=False sector_rank=15 price=617.12 support=590.01 resistance=709.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=13.63 liquidity=2230675.25 spike=0.19
- SDTI.CA: score=24.35 buy_ready=True sector_rank=11 price=45.67 support=43.4 resistance=46.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=54.99 liquidity=7945394.0 spike=0.39
- SEIG.CA: score=17.86 buy_ready=True sector_rank=11 price=187.86 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.08 liquidity=1461340.0 spike=0.21
- SIPC.CA: score=27.76 buy_ready=True sector_rank=11 price=3.68 support=3.4 resistance=3.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=51.02 liquidity=25011356.0 spike=1.68
- SKPC.CA: score=17.28 buy_ready=False sector_rank=17 price=16.86 support=16.8 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=37.93 liquidity=24143658.0 spike=0.29
- SMFR.CA: score=14.87 buy_ready=False sector_rank=11 price=207.93 support=203.51 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=42.24 liquidity=2473875.0 spike=0.2
- SNFC.CA: score=9.4 buy_ready=False sector_rank=11 price=11.77 support=11.68 resistance=12.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23759232.0 spike=0.86
- SPIN.CA: score=11.43 buy_ready=False sector_rank=4 price=14.08 support=13.69 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.05 liquidity=2033730.88 spike=0.41
- SPMD.CA: score=26.4 buy_ready=True sector_rank=11 price=0.42 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.08 liquidity=21461676.0 spike=0.91
- SUGR.CA: score=24.61 buy_ready=True sector_rank=10 price=49.95 support=47.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=56.5 liquidity=8210025.0 spike=0.49
- SVCE.CA: score=22.4 buy_ready=False sector_rank=11 price=9.05 support=7.98 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.5 liquidity=26683470.0 spike=0.16
- SWDY.CA: score=24.4 buy_ready=True sector_rank=5 price=88.06 support=85.25 resistance=91.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=53.16 liquidity=13839017.0 spike=0.38
- TALM.CA: score=14.3 buy_ready=False sector_rank=15 price=15.85 support=15.12 resistance=17.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.94 liquidity=2338833.75 spike=0.18
- TMGH.CA: score=22.4 buy_ready=False sector_rank=9 price=94.55 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.39 liquidity=225499808.0 spike=0.41
- TRTO.CA: score=10.4 buy_ready=False sector_rank=11 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=4.78 buy_ready=False sector_rank=11 price=475.42 support=455.6 resistance=517.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=32.78 liquidity=1384732.63 spike=0.75
- UEGC.CA: score=31.4 buy_ready=True sector_rank=11 price=1.5 support=1.3 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.22 liquidity=96498128.0 spike=4.82
- UNIP.CA: score=14.4 buy_ready=False sector_rank=11 price=0.33 support=0.31 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=65309568.0 spike=5.31
- UNIT.CA: score=24.35 buy_ready=True sector_rank=9 price=13.75 support=10.83 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.81 liquidity=7953455.0 spike=0.82
- WCDF.CA: score=9.27 buy_ready=False sector_rank=11 price=540.42 support=535.0 resistance=561.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=12.24 liquidity=1052416.13 spike=1.41
- WKOL.CA: score=8.23 buy_ready=False sector_rank=11 price=294.6 support=290.0 resistance=349.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=28.64 liquidity=831912.69 spike=0.07
- ZEOT.CA: score=22.14 buy_ready=True sector_rank=11 price=9.26 support=8.43 resistance=9.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=47.24 liquidity=5737478.0 spike=0.63
- ZMID.CA: score=24.4 buy_ready=True sector_rank=9 price=6.13 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.52 liquidity=161706704.0 spike=0.83

## Backtesting Lite
- AREH.CA: 180d return=38.24%, max drawdown=-37.58%, MA20>MA50 days last20=20, as_of=2026-06-03T21:00:00+00:00
- COSG.CA: 180d return=23.53%, max drawdown=-18.87%, MA20>MA50 days last20=20, as_of=2026-06-03T21:00:00+00:00
- MPCO.CA: 180d return=13.5%, max drawdown=-53.57%, MA20>MA50 days last20=20, as_of=2026-06-03T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- AREH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Real Estate Egyptian Consortium S.A.E summary=Real Estate Egyptian Consortium’s net profits approach EGP 2m in 9M-25; Shareholder ups stake in Real Estate Egyptian; Target for Real Estate Investment cuts stake in Real Estate Egyptian Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Real Estate Egyptian Consortium’s net profits approach EGP 2m in 9M-25: https://english.mubasher.info/news/4528467/Real-Estate-Egyptian-Consortium-s-net-profits-approach-EGP-2m-in-9M-25/
  - Shareholder ups stake in Real Estate Egyptian: https://english.mubasher.info/news/4026301/Shareholder-ups-stake-in-Real-Estate-Egyptian/
  - Target for Real Estate Investment cuts stake in Real Estate Egyptian: https://english.mubasher.info/news/4010821/Target-for-Real-Estate-Investment-cuts-stake-in-Real-Estate-Egyptian/
- COSG.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Oil & Soap Company summary=Cairo Oils stock stabilizes above EGP 1.50 resistance level; EGX approves capital increase, reduction of several listed firms; Cairo oils incurs EGP 25m losses in H1-19 Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Cairo Oils stock stabilizes above EGP 1.50 resistance level: https://english.mubasher.info/news/4546423/Cairo-Oils-stock-stabilizes-above-EGP-1-50-resistance-level/
  - EGX approves capital increase, reduction of several listed firms: https://english.mubasher.info/news/3828111/EGX-approves-capital-increase-reduction-of-several-listed-firms/
  - Cairo oils incurs EGP 25m losses in H1-19: https://english.mubasher.info/news/3521392/Cairo-oils-incurs-EGP-25m-losses-in-H1-19/
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=522 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- EMFD.CA: status=RECENT_ACCEPTED latest=2026-01-01 age_days=157 sources=3 expected=Emaar Misr for Development summary=Recent disclosures from Emaar Misr for Development (EMFD.CA) include financial results for Q1 2026 and updates regarding its Board of Directors and Executive Managers.
  - Release from Emaar Misr for Development (EMFD.CA) Concerning the Board of Directors & the Executive Managers. 03/06/2026: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9V5ZNwRD3IdkXr_saM2vAHoitQMJvdaixTlwyap8e9pPvuo2qI6wBCWgSSMTHjKBPjrJ8plgd_ZZPnrw6Cf1CtxKpjQ6u5hOa0ddn8n52oufL73K0RarrxqUKlCHUhn5jjQzd2wG7I-FZ4dYtxLNA9CUTXAxkFfeOhNk9HmNPYs7hrCj5rf0ZsvhalN_6YNJ1hEwActm3eeHAzlg=
  - Emaar Misr for Development (EMFD.CA) Reports its Financial Results (Consolidated) for the Period from 01/01/2026 to 31/03/2026 01/06/2026: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhTAUrvK6g1kAPMUG69aGnp3LvSQfpjW-n-US7JHea7EQX-ay-UdaUMkJ-Oo7tG_9pg1hykCPmb4Bw17FqfSSltpuA844L0xvU5iGvy6Ura2-draTsmvcoHwxe6uBjYMXhfRfRYhy_wuTGnoUjnT761Cg=
  - EGX 30 Index Constituents (EMFD.CA weight 0.72%) 04/06/2026: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhiAlwG7SzpJJR2q7YEOAVFj5xJ3b5X4O6vK8aCtJM9CzjJTFUCFztF4JHABbyAnVEPfjp4VaeQSGHtS5jHaLsVyFnAFwVFBl9pCtnDu3eUv5XxE2FnIJZPXuL7OwVMAQZI9PDK--iCGdQxO5GSuSjH90jMEGuSWH1Pf7nbyY=
- UEGC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=522 sources=3 expected=El-Saeed Company for Contracting and Real Estate Investment "SCCD" (S.A.E.) summary=ElSaeed Contracting stock eyes break above EGP 1.44 amid uptrend; ElSaeed Contracting posts higher consolidated profits at EGP 93m in 2025; ElSaeed Contracting stock signals upside move towards EGP 1.50 Gemini also reviewed web evidence but did not return ticker-specific citations.
  - ElSaeed Contracting stock eyes break above EGP 1.44 amid uptrend: https://english.mubasher.info/news/4595500/ElSaeed-Contracting-stock-eyes-break-above-EGP-1-44-amid-uptrend/
  - ElSaeed Contracting posts higher consolidated profits at EGP 93m in 2025: https://english.mubasher.info/news/4589666/ElSaeed-Contracting-posts-higher-consolidated-profits-at-EGP-93m-in-2025/
  - ElSaeed Contracting stock signals upside move towards EGP 1.50: https://english.mubasher.info/news/4564890/ElSaeed-Contracting-stock-signals-upside-move-towards-EGP-1-50/
- NCCW.CA: status=RECENT_ACCEPTED latest=2026-01-01 age_days=157 sources=3 expected=Nasr Company for Civil Works summary=Nasr Company for Civil Works (NCCW.CA) has recently published AGM minutes, announced an EGM invitation, and disclosed being awarded new construction works.
  - Nasr Company for Civil Works (NCCW.CA) - AGM Minutes (after Certification). 03/06/2026: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9V5ZNwRD3IdkXr_saM2vAHoitQMJvdaixTlwyap8e9pPvuo2qI6wBCWgSSMTHjKBPjrJ8plgd_ZZPnrw6Cf1CtxKpjQ6u5hOa0ddn8n52oufL73K0RarrxqUKlCHUhn5jjQzd2wG7I-FZ4dYtxLNA9CUTXAxkFfeOhNk9HmNPYs7hrCj5rf0ZsvhalN_6YNJ1hEwActm3eeHAzlg=
  - Release from Nasr Company for Civil Works (NCCW.CA) 03/09/2025: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFn6dHWLOKE-pRrBv8MM2LsVNq8mb-Sj3vBCZS2TISmV2C_YExtkKpxWU_gLMOZ03c8G049fTBvKgsYFUJMCxL698l8FRp8ZzdPXBCTAXMiL9wNtn4f_w3Fg2DE4zOpkOpAFCGtfzGX_Rpzy85xfw=
  - Release from Nasr Company for Civil Works (NCCW.CA) Concerning the EGM Invitation 29/04/2026: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECck-cnPja3BPo-KjphStgdeQb_6uso2QYam2RJiQ5l-NZ2FbN1hm7Rvl9d0ml6irHl_WbrS6c01SX0tZZijJ1OHzk14yd2Lp6TAPWe7Ag1iL5bN3kH7et-wUaiwqW5jRnL_xS-VP6yx6j868d9sowq1Y=
- GGCC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Giza General - Contracting and Real Estate Investment S.A.E summary=EGX approves listing EGP 144m capital increase for Giza Contracting; Giza Contracting tests key EGP 0.51 level; Giza Contracting’s consolidated net profits leap to EGP 140m in 9M-25 Gemini also reviewed web evidence but did not return ticker-specific citations.
  - EGX approves listing EGP 144m capital increase for Giza Contracting: https://english.mubasher.info/news/4588793/EGX-approves-listing-EGP-144m-capital-increase-for-Giza-Contracting/
  - Giza Contracting tests key EGP 0.51 level: https://english.mubasher.info/news/4563778/Giza-Contracting-tests-key-EGP-0-51-level/
  - Giza Contracting’s consolidated net profits leap to EGP 140m in 9M-25: https://english.mubasher.info/news/4530408/Giza-Contracting-s-consolidated-net-profits-leap-to-EGP-140m-in-9M-25/
- MPRC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Media Production City summary=Evidence rejected for MPRC.CA: source text did not clearly match MPRC.CA / Egyptian Media Production City.

## Warnings
- Evidence for AREH.CA matches the company but no source/report date was detected.
- Evidence for COSG.CA matches the company but no source/report date was detected.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for UEGC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for GGCC.CA matches the company but no source/report date was detected.
- Evidence rejected for MPRC.CA: source text did not clearly match MPRC.CA / Egyptian Media Production City.
