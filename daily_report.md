# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-07-06T11:03:18.584176+00:00
Generated Cairo: 2026-07-06 14:03
Run timing: target 09:15 Cairo | generated Cairo 2026-07-06 14:03 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-07-06 13:58

## Control Center
- Action tickets: 1 prioritized signal(s)
- BUY-ready candidates: 77
- Data quality issues: 0
- Tradeable price/liquidity tickers: 178/190
- Top sector: Technology & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, July 06
- Freshness: DELAYED
- EGX30 regime: CONSTRUCTIVE / above MA20 63.16% / above MA50 52.63%
- EGX70 regime: BULLISH / above MA20 75.0% / above MA50 72.22%
- Sector breadth: 52.38%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- COMI.CA: liquidity=584917568.0 spike=1.31 score=21.99
- TMGH.CA: liquidity=533494624.0 spike=1.58 score=25.56
- ARAB.CA: liquidity=483670176.0 spike=6.21 score=31.4
- FWRY.CA: liquidity=408356032.0 spike=1.83 score=22.48
- CCAP.CA: liquidity=338548384.0 spike=0.51 score=21.9

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner highlighted RAYA.CA as the top BUY‑ready ticket. It shows strong liquidity (≈2.5 × 10⁸ EGP, 2.95× spike), price well above the 20‑day MA20/MA50, RSI 68.5 and a bullish outlook score of 97. Support sits at 6.7 EGP (≈21% below current price) and resistance at 7.93 EGP (≈2% above). Momentum is extended, so the move may face short‑term pressure. EGX30 is in a constructive phase while EGX70 remains bullish, keeping the overall market risk mode at SELECTIVE_SWING_TRADES_ONLY, which favors careful swing entries and adds uncertainty over the next 1‑3 days.
- RAYA.CA selected for high liquidity, price above MA20/MA50 and strong bullish outlook
- Support at 6.7 EGP, resistance near 7.9 EGP; RSI 68.5 suggests upward bias but momentum may be stretched
- EGX30 constructive / EGX70 bullish regime keeps risk mode selective, implying cautious swing positioning
- Sector leadership from Technology & Distribution supports RAYA, but short‑term price action needs confirmation
- Uncertainty remains due to extended momentum and potential resistance test in the next 1‑3 days

## Top Liquidity Spikes
- KABO.CA: spike=9.19 liquidity=130157608.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- NHPS.CA: spike=6.97 liquidity=69758296.0 outlook=BULLISH_WATCH score=87.37 buy_ready=True
- UNIT.CA: spike=6.22 liquidity=39943616.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ARAB.CA: spike=6.21 liquidity=483670176.0 outlook=BULLISH_WATCH score=87.36 buy_ready=True
- RUBX.CA: spike=4.63 liquidity=169863520.0 outlook=CONSTRUCTIVE score=69.37 buy_ready=False

## Sector Leaderboard
- #1 Technology & Distribution: score=14.14 5d=6.89% 20d=4.77% aboveMA50=100.0%
- #2 Automotive & Distribution: score=10.56 5d=2.29% 20d=11.66% aboveMA50=100.0%
- #3 Tourism & Leisure: score=8.55 5d=-0.29% 20d=9.06% aboveMA50=100.0%
- #4 Non-bank Financial Services: score=7.11 5d=-0.99% 20d=0.17% aboveMA50=60.0%
- #5 Real Estate: score=6.36 5d=0.47% 20d=0.0% aboveMA50=84.62%
- #6 Healthcare: score=6.19 5d=0.92% 20d=-0.08% aboveMA50=83.33%
- #7 Education: score=6.11 5d=0.61% 20d=2.37% aboveMA50=66.67%
- #8 Food, Beverages & Tobacco: score=6.04 5d=0.85% 20d=0.23% aboveMA50=71.43%

## Today's Prioritized Action Tickets
- Priority #1: BUY RAYA.CA
  - Entry: 8.1 | Take profit: 8.74 | Stop loss: 7.78
  - Confidence: LOW | score=33.3 | outlook=BULLISH_WATCH 97
  - Reason: WATCH/BUY SETUP: RAYA.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 68.47, support 6.7, resistance 7.93, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CICH.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- RAYA.CA: BULLISH_WATCH score=97 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended; far above support
- MTIE.CA: BULLISH_WATCH score=89 liquidity=TRADEABLE sector=LEADING risk=momentum is extended; close to resistance
- NHPS.CA: BULLISH_WATCH score=87.37 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- OFH.CA: BULLISH_WATCH score=87.37 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ARAB.CA: BULLISH_WATCH score=87.36 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- HELI.CA: BULLISH_WATCH score=87.36 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance
- TMGH.CA: BULLISH_WATCH score=87.36 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance
- MIPH.CA: BULLISH_WATCH score=87.19 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- BINV.CA: BULLISH_WATCH score=86.76 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- RAYA.CA: rank=33.3 outlook=BULLISH_WATCH outlook_score=97 sector_rank=1 price=8.1 support=6.7 resistance=7.93 liquidity=254635312.0
- ARAB.CA: rank=31.4 outlook=BULLISH_WATCH outlook_score=87.36 sector_rank=5 price=0.23 support=0.2 resistance=0.22 liquidity=483670176.0
- CICH.CA: rank=31.4 outlook=BULLISH_WATCH outlook_score=100 sector_rank=4 price=12.16 support=11.1 resistance=12.8 liquidity=11425418.0
- EBSC.CA: rank=31.15 outlook=CONSTRUCTIVE outlook_score=69.37 sector_rank=12 price=2.07 support=1.71 resistance=2.12 liquidity=20757928.0
- NHPS.CA: rank=31.15 outlook=BULLISH_WATCH outlook_score=87.37 sector_rank=12 price=70.42 support=61.55 resistance=75.49 liquidity=69758296.0
- ODIN.CA: rank=31.15 outlook=BULLISH_WATCH outlook_score=81.37 sector_rank=12 price=2.37 support=2.01 resistance=2.3 liquidity=43263924.0
- RACC.CA: rank=29.21 outlook=BULLISH_WATCH outlook_score=81.37 sector_rank=12 price=10.3 support=9.36 resistance=10.38 liquidity=19991472.0
- OBRI.CA: rank=28.45 outlook=BULLISH_WATCH outlook_score=83.37 sector_rank=12 price=37.1 support=31.5 resistance=39.27 liquidity=28773692.0
- MTIE.CA: rank=28.4 outlook=BULLISH_WATCH outlook_score=89 sector_rank=2 price=9.53 support=8.65 resistance=9.65 liquidity=18639244.0
- ATLC.CA: rank=28.22 outlook=BULLISH_WATCH outlook_score=82.11 sector_rank=4 price=5.32 support=4.7 resistance=5.38 liquidity=13087826.0

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=13.23 buy_ready=False sector_rank=12 price=222.0 support=206.0 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18659848.0 spike=3.04
- ABUK.CA: score=19.41 buy_ready=False sector_rank=21 price=69.43 support=66.66 resistance=83.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=37.09 liquidity=73504104.0 spike=0.59
- ACAMD.CA: score=24.15 buy_ready=True sector_rank=12 price=2.36 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=48.65 liquidity=79295856.0 spike=0.63
- ACGC.CA: score=24.39 buy_ready=True sector_rank=13 price=9.55 support=8.92 resistance=10.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=50.62 liquidity=35335612.0 spike=1.21
- ADCI.CA: score=20.92 buy_ready=True sector_rank=12 price=237.82 support=212.14 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=65.92 liquidity=8768692.0 spike=0.77
- ADIB.CA: score=26.37 buy_ready=True sector_rank=9 price=47.31 support=44.01 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=54.13 liquidity=64540812.0 spike=0.9
- ADPC.CA: score=19.15 buy_ready=False sector_rank=12 price=3.55 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=46.6 liquidity=16000300.0 spike=0.99
- AFDI.CA: score=20.47 buy_ready=True sector_rank=12 price=44.87 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=55.52 liquidity=6318258.0 spike=0.41
- AFMC.CA: score=16.77 buy_ready=True sector_rank=12 price=71.98 support=66.0 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=50.72 liquidity=2382772.0 spike=1.12
- AJWA.CA: score=15.99 buy_ready=False sector_rank=12 price=179.0 support=132.15 resistance=190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=74.97 liquidity=3845865.25 spike=0.14
- ALCN.CA: score=18.24 buy_ready=False sector_rank=10 price=28.72 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=33.46 liquidity=9921601.0 spike=0.86
- ALUM.CA: score=10.59 buy_ready=False sector_rank=12 price=22.56 support=20.55 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=34.36 liquidity=6440920.0 spike=0.7
- AMER.CA: score=22.4 buy_ready=False sector_rank=5 price=2.51 support=2.28 resistance=2.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=21607034.0 spike=0.33
- AMES.CA: score=24.15 buy_ready=True sector_rank=12 price=59.65 support=45.15 resistance=69.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=66.95 liquidity=14202545.0 spike=0.86
- AMIA.CA: score=21.61 buy_ready=True sector_rank=12 price=8.95 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=35.62 liquidity=7457299.5 spike=0.66
- AMOC.CA: score=20.49 buy_ready=False sector_rank=17 price=7.75 support=7.42 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=47.75 liquidity=35340360.0 spike=0.78
- ANFI.CA: score=10.48 buy_ready=False sector_rank=12 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=STALE RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=8.88 buy_ready=False sector_rank=12 price=8.5 support=8.0 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=47.66 liquidity=731871.69 spike=0.81
- ARAB.CA: score=31.4 buy_ready=True sector_rank=5 price=0.23 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=48.48 liquidity=483670176.0 spike=6.21
- ARCC.CA: score=23.92 buy_ready=True sector_rank=14 price=56.2 support=53.0 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=48.94 liquidity=11253656.0 spike=0.37
- AREH.CA: score=24.15 buy_ready=True sector_rank=12 price=1.59 support=1.4 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=55.1 liquidity=18179250.0 spike=0.49
- ARVA.CA: score=10.8 buy_ready=False sector_rank=12 price=10.92 support=10.3 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=19.49 liquidity=3656401.25 spike=0.13
- ASCM.CA: score=24.15 buy_ready=True sector_rank=12 price=59.49 support=54.07 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=48.14 liquidity=25354592.0 spike=0.26
- ASPI.CA: score=18.26 buy_ready=False sector_rank=12 price=0.32 support=0.3 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=49.44 liquidity=6110766.5 spike=0.09
- ATLC.CA: score=28.22 buy_ready=True sector_rank=4 price=5.32 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=60.76 liquidity=13087826.0 spike=1.91
- ATQA.CA: score=19.03 buy_ready=False sector_rank=21 price=9.65 support=9.02 resistance=10.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=54.4 liquidity=46083668.0 spike=1.31
- AXPH.CA: score=20.53 buy_ready=True sector_rank=12 price=1182.14 support=1073.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=65.18 liquidity=4757119.0 spike=1.81
- BINV.CA: score=27.82 buy_ready=True sector_rank=15 price=48.93 support=44.02 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=48.94 liquidity=24272516.0 spike=2.96
- BIOC.CA: score=15.96 buy_ready=True sector_rank=12 price=72.13 support=66.75 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=46.42 liquidity=1813673.38 spike=0.69
- BTFH.CA: score=20.86 buy_ready=False sector_rank=4 price=3.05 support=2.91 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=43.18 liquidity=231259504.0 spike=1.23
- CAED.CA: score=16.26 buy_ready=True sector_rank=12 price=72.15 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=57.35 liquidity=2115705.0 spike=0.45
- CANA.CA: score=17.18 buy_ready=True sector_rank=9 price=36.57 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=50.22 liquidity=2808073.25 spike=0.24
- CCAP.CA: score=21.9 buy_ready=False sector_rank=15 price=5.09 support=4.65 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=338548384.0 spike=0.51
- CCRS.CA: score=22.15 buy_ready=False sector_rank=12 price=2.4 support=2.18 resistance=2.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=49.21 liquidity=10478923.0 spike=0.72
- CEFM.CA: score=4.82 buy_ready=False sector_rank=12 price=100.79 support=95.75 resistance=109.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=30.31 liquidity=676031.25 spike=0.43
- CERA.CA: score=25.09 buy_ready=True sector_rank=12 price=1.26 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=26265516.0 spike=1.47
- CFGH.CA: score=3.15 buy_ready=False sector_rank=12 price=0.1 support=0.1 resistance=0.1 source=Yahoo Finance as_of=2026-07-04T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=0.0 spike=0.0
- CICH.CA: score=31.4 buy_ready=True sector_rank=4 price=12.16 support=11.1 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=11425418.0 spike=4.01
- CIEB.CA: score=22.94 buy_ready=True sector_rank=9 price=24.38 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=62.8 liquidity=4569319.0 spike=0.67
- CIRA.CA: score=24.58 buy_ready=True sector_rank=7 price=29.0 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=61.29 liquidity=19544808.0 spike=1.09
- CLHO.CA: score=25.06 buy_ready=True sector_rank=6 price=16.95 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=65.74 liquidity=52856372.0 spike=1.33
- CNFN.CA: score=26.4 buy_ready=True sector_rank=4 price=4.87 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=61.94 liquidity=22370354.0 spike=0.52
- COMI.CA: score=21.99 buy_ready=False sector_rank=9 price=133.94 support=126.21 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=36.34 liquidity=584917568.0 spike=1.31
- COPR.CA: score=21.15 buy_ready=False sector_rank=12 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=52.31 liquidity=16006842.0 spike=0.66
- COSG.CA: score=24.25 buy_ready=True sector_rank=12 price=1.6 support=1.47 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=57521436.0 spike=1.05
- CPCI.CA: score=12.49 buy_ready=False sector_rank=12 price=396.92 support=354.0 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=80.82 liquidity=1339089.13 spike=0.45
- CSAG.CA: score=19.17 buy_ready=False sector_rank=10 price=32.63 support=30.08 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=78.34 liquidity=7852705.5 spike=0.45
- DAPH.CA: score=21.03 buy_ready=True sector_rank=12 price=83.39 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=62.96 liquidity=2877953.75 spike=0.3
- DEIN.CA: score=10.15 buy_ready=False sector_rank=12 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=25.2 buy_ready=False sector_rank=8 price=27.59 support=23.7 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=81.58 liquidity=12275323.0 spike=2.9
- DSCW.CA: score=18.15 buy_ready=False sector_rank=12 price=1.76 support=1.71 resistance=1.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=42.31 liquidity=25941042.0 spike=0.8
- DTPP.CA: score=27.49 buy_ready=False sector_rank=12 price=203.93 support=114.0 resistance=234.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=92.85 liquidity=67481952.0 spike=3.17
- EALR.CA: score=14.15 buy_ready=False sector_rank=12 price=359.51 support=341.12 resistance=364.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11012137.0 spike=4.03
- EASB.CA: score=20.56 buy_ready=True sector_rank=12 price=7.34 support=4.81 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=64.19 liquidity=6407531.5 spike=0.44
- EAST.CA: score=20.18 buy_ready=False sector_rank=8 price=37.5 support=36.63 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=42.23 liquidity=59824640.0 spike=1.89
- EBSC.CA: score=31.15 buy_ready=True sector_rank=12 price=2.07 support=1.71 resistance=2.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=63.79 liquidity=20757928.0 spike=4.35
- ECAP.CA: score=20.33 buy_ready=True sector_rank=12 price=33.28 support=30.0 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=56.09 liquidity=6184188.5 spike=0.66
- EDFM.CA: score=4.54 buy_ready=False sector_rank=12 price=326.02 support=310.2 resistance=355.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=2.14 liquidity=394088.56 spike=0.71
- EEII.CA: score=26.47 buy_ready=False sector_rank=12 price=2.69 support=2.3 resistance=2.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=74.29 liquidity=22307040.0 spike=1.16
- EFIC.CA: score=2.54 buy_ready=False sector_rank=21 price=185.8 support=180.02 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=18.2 liquidity=1133020.63 spike=0.49
- EFID.CA: score=24.4 buy_ready=True sector_rank=8 price=28.66 support=25.5 resistance=29.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=47.06 liquidity=34988248.0 spike=0.45
- EFIH.CA: score=13.62 buy_ready=False sector_rank=16 price=23.09 support=21.56 resistance=23.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=120572656.0 spike=3.4
- EGAL.CA: score=12.41 buy_ready=False sector_rank=21 price=296.7 support=272.28 resistance=327.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=33.81 liquidity=41757536.0 spike=0.77
- EGAS.CA: score=16.58 buy_ready=False sector_rank=17 price=49.86 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=37.58 liquidity=5091436.5 spike=0.6
- EGBE.CA: score=16.42 buy_ready=False sector_rank=9 price=0.46 support=0.43 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=63.33 liquidity=51676.74 spike=0.72
- EGCH.CA: score=17.41 buy_ready=False sector_rank=21 price=12.69 support=12.13 resistance=14.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=41.02 liquidity=31225754.0 spike=0.62
- EGSA.CA: score=12.66 buy_ready=False sector_rank=11 price=8.75 support=8.55 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=11619.02 spike=1.23
- EGTS.CA: score=24.4 buy_ready=True sector_rank=5 price=18.89 support=15.1 resistance=20.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=55.88 liquidity=36094168.0 spike=0.48
- EHDR.CA: score=19.15 buy_ready=False sector_rank=12 price=2.65 support=2.37 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=35441688.0 spike=0.6
- EKHO.CA: score=10.49 buy_ready=False sector_rank=17 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-04T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=17.6 buy_ready=False sector_rank=18 price=2.11 support=2.04 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=18575844.0 spike=1.08
- ELKA.CA: score=25.29 buy_ready=True sector_rank=12 price=1.49 support=1.19 resistance=1.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=69.77 liquidity=54676596.0 spike=1.07
- ELNA.CA: score=8.21 buy_ready=False sector_rank=12 price=37.81 support=35.55 resistance=41.51 source=Yahoo Finance as_of=2026-07-04T21:00:00+00:00 freshness=FRESH RSI=50.49 liquidity=60609.43 spike=0.15
- ELSH.CA: score=24.39 buy_ready=True sector_rank=12 price=13.7 support=11.1 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=55.21 liquidity=229368496.0 spike=1.12
- ELWA.CA: score=7.84 buy_ready=False sector_rank=12 price=2.0 support=1.94 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=29.27 liquidity=691567.38 spike=0.33
- EMFD.CA: score=22.4 buy_ready=False sector_rank=5 price=11.9 support=11.11 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=67505960.0 spike=0.25
- ENGC.CA: score=24.4 buy_ready=True sector_rank=12 price=37.0 support=33.0 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=63.02 liquidity=8250055.0 spike=0.58
- EOSB.CA: score=16.25 buy_ready=False sector_rank=12 price=1.48 support=1.42 resistance=1.55 source=Yahoo Finance as_of=2026-07-04T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=106451.96 spike=0.9
- EPCO.CA: score=11.59 buy_ready=False sector_rank=12 price=8.9 support=8.5 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=39.72 liquidity=2437975.5 spike=0.32
- EPPK.CA: score=20.99 buy_ready=False sector_rank=12 price=15.06 support=11.67 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=94.35 liquidity=3498280.0 spike=3.17
- ETEL.CA: score=24.56 buy_ready=True sector_rank=11 price=95.87 support=89.01 resistance=96.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=58.12 liquidity=77765816.0 spike=1.19
- ETRS.CA: score=25.35 buy_ready=True sector_rank=12 price=11.0 support=8.75 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=60.52 liquidity=125007168.0 spike=1.6
- EXPA.CA: score=24.37 buy_ready=True sector_rank=9 price=18.82 support=18.03 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=55.19 liquidity=13375140.0 spike=0.45
- FAIT.CA: score=13.22 buy_ready=False sector_rank=9 price=36.65 support=35.01 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=51.54 liquidity=845115.5 spike=0.32
- FAITA.CA: score=4.41 buy_ready=False sector_rank=9 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=25.64 liquidity=35101.41 spike=0.9
- FERC.CA: score=4.4 buy_ready=False sector_rank=21 price=74.69 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=33.16 liquidity=2988406.75 spike=0.78
- FWRY.CA: score=22.48 buy_ready=False sector_rank=16 price=19.2 support=17.71 resistance=19.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=50.33 liquidity=408356032.0 spike=1.83
- GBCO.CA: score=26.4 buy_ready=False sector_rank=2 price=31.3 support=25.25 resistance=32.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=70.76 liquidity=73588856.0 spike=0.8
- GDWA.CA: score=18.15 buy_ready=False sector_rank=12 price=0.78 support=0.76 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=36.56 liquidity=12402111.0 spike=0.85
- GGCC.CA: score=24.47 buy_ready=False sector_rank=12 price=0.53 support=0.4 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=98.25 liquidity=25209252.0 spike=1.66
- GIHD.CA: score=27.47 buy_ready=True sector_rank=12 price=44.96 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=64.72 liquidity=14542574.0 spike=1.66
- GMCI.CA: score=19.78 buy_ready=False sector_rank=12 price=1.95 support=1.66 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=80.49 liquidity=2053135.75 spike=3.29
- GRCA.CA: score=6.57 buy_ready=False sector_rank=12 price=52.0 support=50.2 resistance=58.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=31.7 liquidity=2420077.75 spike=0.6
- GSSC.CA: score=15.76 buy_ready=False sector_rank=12 price=250.41 support=228.1 resistance=255.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=48.77 liquidity=2608927.25 spike=0.94
- GTWL.CA: score=23.15 buy_ready=False sector_rank=12 price=87.3 support=45.47 resistance=102.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=93.48 liquidity=30684756.0 spike=0.63
- HDBK.CA: score=23.37 buy_ready=False sector_rank=9 price=165.39 support=138.0 resistance=173.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=78.75 liquidity=30091630.0 spike=0.89
- HELI.CA: score=27.8 buy_ready=True sector_rank=5 price=6.78 support=6.28 resistance=6.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=52.63 liquidity=274328480.0 spike=2.7
- HRHO.CA: score=22.96 buy_ready=False sector_rank=4 price=27.1 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=55.45 liquidity=223149856.0 spike=1.78
- ICID.CA: score=22.15 buy_ready=True sector_rank=12 price=7.78 support=5.8 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=66.96 liquidity=10638281.0 spike=0.77
- IDRE.CA: score=19.01 buy_ready=True sector_rank=12 price=44.41 support=41.1 resistance=46.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=61.69 liquidity=4859100.0 spike=0.38
- IFAP.CA: score=15.64 buy_ready=False sector_rank=19 price=19.53 support=18.47 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=48.75 liquidity=3262473.5 spike=0.51
- INFI.CA: score=12.01 buy_ready=False sector_rank=12 price=94.45 support=88.51 resistance=103.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=37.1 liquidity=3864843.75 spike=0.66
- IRON.CA: score=13.83 buy_ready=False sector_rank=21 price=32.08 support=30.51 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=47.85 liquidity=5419835.0 spike=0.68
- ISMA.CA: score=17.15 buy_ready=False sector_rank=12 price=27.77 support=27.79 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=3.51 liquidity=13742774.0 spike=0.41
- ISMQ.CA: score=24.41 buy_ready=False sector_rank=21 price=9.85 support=7.56 resistance=10.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=74.92 liquidity=125899920.0 spike=0.94
- ISPH.CA: score=19.4 buy_ready=False sector_rank=6 price=11.65 support=11.2 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=41.83 liquidity=28233510.0 spike=0.26
- JUFO.CA: score=24.4 buy_ready=True sector_rank=8 price=30.9 support=28.5 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=44.81 liquidity=18468734.0 spike=0.6
- KABO.CA: score=13.97 buy_ready=False sector_rank=13 price=7.0 support=6.57 resistance=7.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=130157608.0 spike=9.19
- KWIN.CA: score=17.62 buy_ready=False sector_rank=12 price=68.74 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=40.77 liquidity=8471545.0 spike=0.71
- KZPC.CA: score=6.11 buy_ready=False sector_rank=12 price=8.52 support=8.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=10.85 liquidity=2964799.0 spike=0.48
- LCSW.CA: score=13.92 buy_ready=False sector_rank=14 price=30.14 support=28.6 resistance=30.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=163899120.0 spike=4.52
- LUTS.CA: score=24.15 buy_ready=True sector_rank=12 price=0.73 support=0.6 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=50.18 liquidity=19567166.0 spike=0.39
- MAAL.CA: score=24.13 buy_ready=False sector_rank=12 price=7.7 support=5.52 resistance=7.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=99.44 liquidity=24434074.0 spike=1.49
- MASR.CA: score=26.45 buy_ready=True sector_rank=12 price=7.69 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=65.62 liquidity=78914296.0 spike=1.15
- MBSC.CA: score=15.54 buy_ready=False sector_rank=14 price=245.0 support=222.66 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=37.67 liquidity=6619933.5 spike=0.24
- MCQE.CA: score=16.66 buy_ready=False sector_rank=14 price=177.6 support=166.66 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=30.73 liquidity=18712430.0 spike=1.37
- MCRO.CA: score=23.75 buy_ready=True sector_rank=12 price=1.25 support=1.17 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=39884584.0 spike=1.3
- MENA.CA: score=24.84 buy_ready=True sector_rank=5 price=7.05 support=6.41 resistance=7.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=63.51 liquidity=15784658.0 spike=1.22
- MEPA.CA: score=7.52 buy_ready=False sector_rank=12 price=1.62 support=1.52 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=32.14 liquidity=4367972.0 spike=0.38
- MFPC.CA: score=17.57 buy_ready=False sector_rank=21 price=35.72 support=34.22 resistance=43.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=35.28 liquidity=87685008.0 spike=1.08
- MFSC.CA: score=20.71 buy_ready=True sector_rank=12 price=48.95 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=62.88 liquidity=4557789.5 spike=0.6
- MHOT.CA: score=20.89 buy_ready=False sector_rank=3 price=34.6 support=28.83 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=76.14 liquidity=8486294.0 spike=0.57
- MICH.CA: score=18.57 buy_ready=True sector_rank=12 price=37.82 support=34.0 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=55.02 liquidity=4419465.5 spike=0.28
- MILS.CA: score=7.66 buy_ready=False sector_rank=12 price=130.23 support=126.31 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=21.37 liquidity=3511518.5 spike=0.39
- MIPH.CA: score=15.82 buy_ready=True sector_rank=6 price=669.5 support=630.13 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=51.41 liquidity=1422530.5 spike=0.82
- MOED.CA: score=19.83 buy_ready=False sector_rank=12 price=0.7 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=49.59 liquidity=7682560.0 spike=0.86
- MOIL.CA: score=15.6 buy_ready=False sector_rank=17 price=0.51 support=0.46 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=69.23 liquidity=108163.7 spike=0.39
- MOIN.CA: score=3.7 buy_ready=False sector_rank=12 price=23.72 support=22.6 resistance=25.3 source=Yahoo Finance as_of=2026-07-04T21:00:00+00:00 freshness=FRESH RSI=33.51 liquidity=552059.26 spike=0.8
- MOSC.CA: score=10.86 buy_ready=False sector_rank=12 price=270.66 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=37.35 liquidity=1709574.5 spike=0.18
- MPCI.CA: score=26.15 buy_ready=True sector_rank=12 price=244.58 support=213.0 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=64.95 liquidity=41813536.0 spike=0.41
- MPCO.CA: score=21.38 buy_ready=False sector_rank=19 price=1.8 support=1.66 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=54.24 liquidity=45514692.0 spike=0.42
- MPRC.CA: score=21.15 buy_ready=False sector_rank=12 price=38.7 support=31.15 resistance=40.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=86.35 liquidity=11632170.0 spike=0.26
- MTIE.CA: score=28.4 buy_ready=True sector_rank=2 price=9.53 support=8.65 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=69.23 liquidity=18639244.0 spike=0.95
- NAHO.CA: score=-0.82 buy_ready=False sector_rank=12 price=0.11 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27341.81 spike=0.87
- NCCW.CA: score=24.15 buy_ready=True sector_rank=12 price=6.35 support=5.82 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=40.14 liquidity=11622990.0 spike=0.34
- NEDA.CA: score=9.27 buy_ready=False sector_rank=12 price=2.75 support=2.7 resistance=2.84 source=Yahoo Finance as_of=2026-07-04T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=120406.0 spike=0.42
- NHPS.CA: score=31.15 buy_ready=True sector_rank=12 price=70.42 support=61.55 resistance=75.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=60.46 liquidity=69758296.0 spike=6.97
- NINH.CA: score=22.06 buy_ready=False sector_rank=12 price=18.17 support=16.8 resistance=18.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=70.93 liquidity=9747208.0 spike=1.58
- NIPH.CA: score=26.88 buy_ready=True sector_rank=6 price=177.15 support=157.01 resistance=185.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=60.19 liquidity=105739800.0 spike=1.24
- OBRI.CA: score=28.45 buy_ready=True sector_rank=12 price=37.1 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=57.4 liquidity=28773692.0 spike=1.15
- OCDI.CA: score=23.6 buy_ready=False sector_rank=5 price=26.69 support=20.0 resistance=25.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=84.94 liquidity=90857824.0 spike=1.1
- OCPH.CA: score=19.51 buy_ready=True sector_rank=12 price=356.2 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=62.3 liquidity=3362105.5 spike=0.51
- ODIN.CA: score=31.15 buy_ready=True sector_rank=12 price=2.37 support=2.01 resistance=2.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=43263924.0 spike=3.62
- OFH.CA: score=26.97 buy_ready=True sector_rank=12 price=0.63 support=0.57 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=57.32 liquidity=50886744.0 spike=2.41
- OIH.CA: score=23.14 buy_ready=False sector_rank=15 price=1.41 support=1.33 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=8238405.0 spike=0.11
- OLFI.CA: score=27.36 buy_ready=True sector_rank=8 price=22.76 support=21.0 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=49.36 liquidity=32476652.0 spike=1.48
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=706.99 support=703.25 resistance=726.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=196045792.0 spike=1.0
- ORHD.CA: score=24.78 buy_ready=True sector_rank=5 price=38.94 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=51.07 liquidity=193690608.0 spike=1.19
- ORWE.CA: score=21.97 buy_ready=False sector_rank=13 price=22.91 support=21.95 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=36.96 liquidity=23436622.0 spike=0.77
- PHAR.CA: score=24.63 buy_ready=True sector_rank=6 price=87.55 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=63.45 liquidity=8231858.5 spike=0.3
- PHDC.CA: score=17.4 buy_ready=False sector_rank=5 price=14.85 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=25.12 liquidity=329985984.0 spike=0.97
- PHTV.CA: score=15.12 buy_ready=False sector_rank=12 price=267.0 support=201.55 resistance=277.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=92.07 liquidity=3969686.0 spike=0.3
- POUL.CA: score=24.4 buy_ready=True sector_rank=8 price=38.59 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=65.5 liquidity=28998222.0 spike=0.91
- PRCL.CA: score=22.92 buy_ready=False sector_rank=14 price=33.83 support=23.5 resistance=34.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=82.14 liquidity=27854284.0 spike=0.6
- PRDC.CA: score=9.96 buy_ready=False sector_rank=5 price=8.51 support=7.7 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=162842736.0 spike=1.28
- PRMH.CA: score=16.92 buy_ready=False sector_rank=12 price=2.62 support=2.34 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=31.76 liquidity=9774960.0 spike=0.3
- RACC.CA: score=29.21 buy_ready=True sector_rank=12 price=10.3 support=9.36 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=61.47 liquidity=19991472.0 spike=2.53
- RAKT.CA: score=3.68 buy_ready=False sector_rank=12 price=22.75 support=21.4 resistance=23.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=31.64 liquidity=328416.0 spike=1.1
- RAYA.CA: score=33.3 buy_ready=True sector_rank=1 price=8.1 support=6.7 resistance=7.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=68.47 liquidity=254635312.0 spike=2.95
- RMDA.CA: score=19.4 buy_ready=False sector_rank=6 price=5.08 support=4.81 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=30.19 liquidity=15775124.0 spike=0.21
- ROTO.CA: score=17.24 buy_ready=False sector_rank=12 price=42.75 support=33.06 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=75.98 liquidity=6096919.5 spike=0.19
- RREI.CA: score=20.2 buy_ready=True sector_rank=12 price=3.59 support=3.34 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=51.61 liquidity=9052674.0 spike=0.54
- RTVC.CA: score=15.74 buy_ready=False sector_rank=12 price=3.84 support=3.55 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=50.72 liquidity=2589290.5 spike=0.49
- RUBX.CA: score=28.15 buy_ready=False sector_rank=12 price=13.5 support=9.8 resistance=14.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=84.11 liquidity=169863520.0 spike=4.63
- SAUD.CA: score=17.69 buy_ready=False sector_rank=9 price=21.69 support=19.99 resistance=22.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=47.8 liquidity=6317634.0 spike=0.83
- SCEM.CA: score=21.76 buy_ready=True sector_rank=14 price=64.88 support=59.3 resistance=67.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=65.99 liquidity=7840554.0 spike=0.45
- SCFM.CA: score=11.47 buy_ready=False sector_rank=12 price=243.62 support=226.5 resistance=269.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=40.04 liquidity=2325694.5 spike=0.61
- SCTS.CA: score=20.06 buy_ready=True sector_rank=7 price=619.29 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=58.67 liquidity=3658554.0 spike=0.77
- SDTI.CA: score=19.16 buy_ready=True sector_rank=12 price=47.01 support=45.45 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=40.57 liquidity=5012489.0 spike=0.49
- SEIG.CA: score=11.56 buy_ready=False sector_rank=12 price=190.92 support=180.0 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=82.05 liquidity=407917.19 spike=0.1
- SIPC.CA: score=11.54 buy_ready=False sector_rank=12 price=3.44 support=3.25 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=45.76 liquidity=2393417.25 spike=0.21
- SKPC.CA: score=18.41 buy_ready=False sector_rank=21 price=16.17 support=15.58 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=40.8 liquidity=14181584.0 spike=0.44
- SMFR.CA: score=5.98 buy_ready=False sector_rank=12 price=205.31 support=195.1 resistance=209.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4309400.5 spike=2.26
- SNFC.CA: score=14.49 buy_ready=False sector_rank=12 price=11.57 support=11.68 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=32.88 liquidity=17568828.0 spike=1.17
- SPIN.CA: score=24.47 buy_ready=True sector_rank=13 price=14.6 support=13.3 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=69.67 liquidity=8399490.0 spike=1.05
- SPMD.CA: score=20.58 buy_ready=True sector_rank=12 price=0.43 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT RSI=58.96 liquidity=6434168.5 spike=0.33
- SUGR.CA: score=6.66 buy_ready=False sector_rank=8 price=47.31 support=45.31 resistance=50.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=3262637.75 spike=0.46
- SVCE.CA: score=27.37 buy_ready=False sector_rank=12 price=9.75 support=8.11 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=70.36 liquidity=114164920.0 spike=1.61
- SWDY.CA: score=21.04 buy_ready=True sector_rank=18 price=88.05 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=57.04 liquidity=7600994.5 spike=0.51
- TALM.CA: score=16.27 buy_ready=False sector_rank=7 price=15.72 support=15.38 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=42.99 liquidity=6874019.0 spike=0.93
- TMGH.CA: score=25.56 buy_ready=True sector_rank=5 price=98.19 support=92.1 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=50.91 liquidity=533494624.0 spike=1.58
- TRTO.CA: score=10.89 buy_ready=False sector_rank=12 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-07-04T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=759.29 spike=1.37
- UEFM.CA: score=19.7 buy_ready=True sector_rank=12 price=499.32 support=460.0 resistance=505.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=56.71 liquidity=1834311.0 spike=1.86
- UEGC.CA: score=27.07 buy_ready=True sector_rank=12 price=1.6 support=1.33 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=67.5 liquidity=37963428.0 spike=1.46
- UNIP.CA: score=22.53 buy_ready=True sector_rank=12 price=0.33 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=8378812.5 spike=0.35
- UNIT.CA: score=14.4 buy_ready=False sector_rank=5 price=16.09 support=13.45 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39943616.0 spike=6.22
- WCDF.CA: score=9.43 buy_ready=False sector_rank=12 price=506.06 support=450.0 resistance=545.99 source=Yahoo Finance as_of=2026-07-04T21:00:00+00:00 freshness=FRESH RSI=48.87 liquidity=277826.94 spike=0.8
- WKOL.CA: score=10.08 buy_ready=False sector_rank=12 price=299.33 support=280.05 resistance=299.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7212828.5 spike=2.86
- ZEOT.CA: score=22.15 buy_ready=True sector_rank=12 price=11.17 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=68.22 liquidity=22828048.0 spike=0.64
- ZMID.CA: score=26.4 buy_ready=True sector_rank=5 price=6.78 support=5.96 resistance=6.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=68.67 liquidity=129066816.0 spike=0.58

## Backtesting Lite
- RAYA.CA: 180d return=171.82%, max drawdown=-12.86%, MA20>MA50 days last20=20, as_of=2026-07-04T21:00:00+00:00
- ARAB.CA: 180d return=16.76%, max drawdown=-38.02%, MA20>MA50 days last20=20, as_of=2026-07-04T21:00:00+00:00
- CICH.CA: 180d return=51.65%, max drawdown=-14.78%, MA20>MA50 days last20=16, as_of=2026-07-04T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- RAYA.CA: status=RECENT_ACCEPTED latest=2026-06-29 age_days=7 sources=3 expected=Raya Holding summary=Raya Holding for Financial Investments (RAYA.CA) has demonstrated recent activity on the EGX, including an employee incentive share transfer in June 2026. The company released its Q1 2026 financial results in May 2026, showing continued financial performance. Raya Holding reported significant consolidated profit and revenue growth in 2025, with revenues reaching EGP 63.8 billion, and strong performance in the first nine months of 2024, driven by its diversified investment portfolio across various sectors.
  - Raya Holding executes EGP 23.9M employee incentive share transfer (June 29, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpnu9Ffxccc34XE3S9uxAXi-Ywm-j8QtSdWrwHc861fB58JN4RS3yKjwC8mWqOYynV3Tm0gxx8xqjR8W9pIR1Kq0znHeS5XxlunRm7Ijmf0N-fUWKIo8on_g4GNwbtRlmO93wf223y3XO2qWa2Q5Jan-oTUPawlm90G1gFQWL3hkGXAH1Ppker6mOnaOA3L-_wS-PoZ5X51D1c3eUzbv0d
  - Raya Quarterly Financials Report Q1 2026 (May 14, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVPBa5gF1a4gQemJ2jS0jEjM7GLOWh1CYoa5X4Fv0Jn0CyoSbjWia0xq-v-z-gT9RzVzN-V3pD7034R4BO6rKu3Xmdtn-IADdP-F1GPEfNRF-vnNkI1lDWjGYu
  - Release from Raya Holding For Financial Investments (RAYA.CA) Concerning the Financial Results (May 14, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfHHjzRRcfCMq2YtcvVkxhLTdh-wbgCgzVZ6q4Yk2gbA7C94hrO76iYD11L8idYiXLCN78cgqVjHoDca4KyjJaoOSGSG8QekOWnrzkv2no-p5_42fRlgWkC9vmGl5QVWM-J1tey6GZx0BLizjL5Cqi
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- CICH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=CI Capital Holding summary=Evidence rejected for CICH.CA: source text did not clearly match CICH.CA / CI Capital Holding.
- EBSC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Osool ESB Securities Brokerage summary=Evidence rejected for EBSC.CA: source text did not clearly match EBSC.CA / Osool ESB Securities Brokerage.
- NHPS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=National Company for Housing Professional Syndicates SAE summary=Evidence rejected for NHPS.CA: source text did not clearly match NHPS.CA / National Company for Housing Professional Syndicates SAE.
- ODIN.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=551 sources=3 expected=ODIN Investments (S.A.E) summary=Odin Investments to distribute EGP 45m dividends for 2025; EGX-listed companies, banks propose cash dividends for 2025; Odin Investments to launch EGP 5m fund for investments in metals Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Odin Investments to distribute EGP 45m dividends for 2025: https://english.mubasher.info/news/4586642/Odin-Investments-to-distribute-EGP-45m-dividends-for-2025/
  - EGX-listed companies, banks propose cash dividends for 2025: https://english.mubasher.info/news/4560139/EGX-listed-companies-banks-propose-cash-dividends-for-2025/
  - Odin Investments to launch EGP 5m fund for investments in metals: https://english.mubasher.info/news/4550653/Odin-Investments-to-launch-EGP-5m-fund-for-investments-in-metals/
- RACC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Raya Customer Experience summary=Evidence rejected for RACC.CA: source text did not clearly match RACC.CA / Raya Customer Experience.
- OBRI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El-Ebour Co. for Real Estate Investment S.A.E. summary=El Obour for Real Estate advances UAE expansion via new subsidiary; El Obour for Real Estate registers EGP 39m consolidated net profits in 9M-25; El Ebour for Real Estate expands business in UAE Gemini also reviewed web evidence but did not return ticker-specific citations.
  - El Obour for Real Estate advances UAE expansion via new subsidiary: https://english.mubasher.info/news/4547120/El-Obour-for-Real-Estate-advances-UAE-expansion-via-new-subsidiary/
  - El Obour for Real Estate registers EGP 39m consolidated net profits in 9M-25: https://english.mubasher.info/news/4527519/El-Obour-for-Real-Estate-registers-EGP-39m-consolidated-net-profits-in-9M-25/
  - El Ebour for Real Estate expands business in UAE: https://english.mubasher.info/news/4469178/El-Ebour-for-Real-Estate-expands-business-in-UAE/

## Warnings
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence rejected for CICH.CA: source text did not clearly match CICH.CA / CI Capital Holding.
- Evidence rejected for EBSC.CA: source text did not clearly match EBSC.CA / Osool ESB Securities Brokerage.
- Evidence rejected for NHPS.CA: source text did not clearly match NHPS.CA / National Company for Housing Professional Syndicates SAE.
- Evidence for ODIN.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for RACC.CA: source text did not clearly match RACC.CA / Raya Customer Experience.
- Evidence for OBRI.CA matches the company but no source/report date was detected.
