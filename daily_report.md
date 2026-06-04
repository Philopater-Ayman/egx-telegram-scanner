# Telegram-First EGX Scanner Report

Scan phase: Evening tomorrow plan
Generated UTC: 2026-06-04T18:37:36.318459+00:00
Generated Cairo: 2026-06-04 21:37
Run timing: target 19:30 Cairo | generated Cairo 2026-06-04 21:37 | cron 30 16 * * 0-4
Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-06-04 21:33

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 73
- Data quality issues: 0
- Tradeable price/liquidity tickers: 179/190
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, June 04
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 35.0% / above MA50 85.0%
- EGX70 regime: BULLISH / above MA20 69.23% / above MA50 89.74%
- Sector breadth: 66.67%
- Risk mode: SELECTIVE_SMALL_MID_SWINGS

## Top Liquidity
- EMFD.CA: liquidity=845328000.0 spike=5.57 score=31.4
- FWRY.CA: liquidity=580160832.0 spike=2.22 score=24.54
- CCAP.CA: liquidity=402771840.0 spike=0.48 score=23.4
- ASPI.CA: liquidity=382521024.0 spike=13.9 score=14.4
- MPCO.CA: liquidity=365360224.0 spike=8.89 score=14.4

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner highlights ISPH.CA as the top watch‑buy candidate, followed by ARVA.CA and ACAMD.CA. All three show strong liquidity spikes, price above the 20‑ and 50‑day MAs, and clear support‑resistance zones. The EGX30 remains bearish while the broader EGX70 is bullish, placing the market in a SELECTIVE_SMALL_MID_SWINGS risk mode – favoring isolated, well‑supported moves rather than broad index‑wide rallies. Expect modest upside over the next 1‑3 days if price respects the identified support levels, but be aware of heightened uncertainty from the mixed index trends and low confidence scores.
- ISPH.CA: liquidity spike, price > MA20/MA50, support 10.8, resistance 12.25, RSI 54.6 – low‑confidence bullish watch.
- ARVA.CA & ACAMD.CA: solid liquidity, price above MAs, but RSI above 60 and sector not leading – monitor for over‑extension.
- EGX30 bearish, EGX70 bullish → risk mode SELECTIVE_SMALL_MID_SWINGS; focus on tight support‑resistance setups.
- Sector breadth 66.7% with Healthcare and Real Estate leading; tourism & tech showing strongest returns.
- Uncertainty remains high due to mixed macro trend and low confidence; verify price action on Thndr before acting.

## Top Liquidity Spikes
- ASPI.CA: spike=13.9 liquidity=382521024.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- NCCW.CA: spike=12.16 liquidity=134405584.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- UNIP.CA: spike=11.36 liquidity=91624008.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MPCO.CA: spike=8.89 liquidity=365360224.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EBSC.CA: spike=7.38 liquidity=17174218.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Tourism & Leisure: score=12.82 5d=5.1% 20d=17.07% aboveMA50=100.0%
- #2 Technology & Distribution: score=10.99 5d=-0.13% 20d=18.76% aboveMA50=100.0%
- #3 Investment Holding: score=10.0 5d=6.05% 20d=12.89% aboveMA50=66.67%
- #4 Real Estate: score=9.6 5d=3.3% 20d=9.86% aboveMA50=92.31%
- #5 Healthcare: score=8.65 5d=1.79% 20d=8.15% aboveMA50=100.0%
- #6 Industrial Goods & Cables: score=7.87 5d=1.07% 20d=0.28% aboveMA50=100.0%
- #7 Telecommunications: score=7.34 5d=-1.23% 20d=5.9% aboveMA50=100.0%
- #8 Building Materials: score=7.32 5d=0.92% 20d=4.33% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- Priority #1: BUY ISPH.CA
  - Entry: 12.54 | Take profit: 13.54 | Stop loss: 12.04
  - Confidence: LOW | score=31.34 | outlook=BULLISH_WATCH 97.65
  - Reason: WATCH/BUY SETUP: ISPH.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 54.59, support 10.8, resistance 12.25, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY ARVA.CA
  - Entry: 10.6 | Take profit: 11.44 | Stop loss: 10.18
  - Confidence: LOW | score=30.24 | outlook=BULLISH_WATCH 78.14
  - Reason: WATCH/BUY SETUP: ARVA.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 64.71, support 7.71, resistance 10.5, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY ACAMD.CA
  - Entry: 2.37 | Take profit: 2.55 | Stop loss: 2.28
  - Confidence: LOW | score=29.52 | outlook=BULLISH_WATCH 78.14
  - Reason: WATCH/BUY SETUP: ACAMD.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 67.31, support 1.94, resistance 2.46, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ISPH.CA: BULLISH_WATCH score=97.65 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- AJWA.CA: BULLISH_WATCH score=96.14 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- TALM.CA: BULLISH_WATCH score=94.15 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ARAB.CA: BULLISH_WATCH score=92.6 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ARCC.CA: BULLISH_WATCH score=91.32 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance; sector is not leading
- RAYA.CA: BULLISH_WATCH score=91 liquidity=TRADEABLE sector=LEADING risk=far above support
- ZMID.CA: BULLISH_WATCH score=90.6 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- CLHO.CA: BULLISH_WATCH score=89.65 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ETEL.CA: BULLISH_WATCH score=88.34 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ODIN.CA: BULLISH_WATCH score=88.14 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- EMFD.CA: rank=31.4 outlook=BULLISH_WATCH outlook_score=80.6 sector_rank=4 price=12.25 support=9.83 resistance=12.3 liquidity=845328000.0
- ISPH.CA: rank=31.34 outlook=BULLISH_WATCH outlook_score=97.65 sector_rank=5 price=12.54 support=10.8 resistance=12.25 liquidity=324024800.0
- GGCC.CA: rank=30.4 outlook=BULLISH_WATCH outlook_score=83.14 sector_rank=15 price=0.43 support=0.39 resistance=0.43 liquidity=31156986.0
- ARVA.CA: rank=30.24 outlook=BULLISH_WATCH outlook_score=78.14 sector_rank=15 price=10.6 support=7.71 resistance=10.5 liquidity=44943404.0
- ARCC.CA: rank=29.52 outlook=BULLISH_WATCH outlook_score=91.32 sector_rank=8 price=58.81 support=52.6 resistance=59.7 liquidity=67163240.0
- ACAMD.CA: rank=29.52 outlook=BULLISH_WATCH outlook_score=78.14 sector_rank=15 price=2.37 support=1.94 resistance=2.46 liquidity=261323536.0
- MPRC.CA: rank=29.08 outlook=BULLISH_WATCH outlook_score=84.14 sector_rank=15 price=32.8 support=30.01 resistance=33.7 liquidity=24478056.0
- PRDC.CA: rank=28.88 outlook=BULLISH_WATCH outlook_score=82.6 sector_rank=4 price=6.28 support=5.08 resistance=6.21 liquidity=24540382.0
- ODIN.CA: rank=28.66 outlook=BULLISH_WATCH outlook_score=88.14 sector_rank=15 price=2.1 support=1.89 resistance=2.08 liquidity=22485632.0
- ARAB.CA: rank=28.4 outlook=BULLISH_WATCH outlook_score=92.6 sector_rank=4 price=0.21 support=0.19 resistance=0.22 liquidity=71245000.0

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=13.31 buy_ready=False sector_rank=15 price=211.12 support=195.1 resistance=249.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.51 liquidity=3912154.5 spike=0.15
- ABUK.CA: score=18.55 buy_ready=False sector_rank=19 price=81.87 support=78.0 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.04 liquidity=44636652.0 spike=0.32
- ACAMD.CA: score=29.52 buy_ready=True sector_rank=15 price=2.37 support=1.94 resistance=2.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.31 liquidity=261323536.0 spike=2.56
- ACGC.CA: score=28.3 buy_ready=True sector_rank=9 price=10.12 support=8.3 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=96112688.0 spike=1.95
- ADCI.CA: score=21.13 buy_ready=True sector_rank=15 price=216.0 support=190.0 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.73 liquidity=6730396.0 spike=0.94
- ADIB.CA: score=21.71 buy_ready=False sector_rank=18 price=47.3 support=44.45 resistance=50.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.49 liquidity=71755000.0 spike=0.42
- ADPC.CA: score=11.22 buy_ready=False sector_rank=15 price=3.77 support=3.61 resistance=3.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42686636.0 spike=1.91
- AFDI.CA: score=27.82 buy_ready=False sector_rank=15 price=44.89 support=36.55 resistance=46.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=70.77 liquidity=29893694.0 spike=1.71
- AFMC.CA: score=15.07 buy_ready=False sector_rank=15 price=73.2 support=68.2 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.73 liquidity=2668339.75 spike=0.18
- AJWA.CA: score=28.14 buy_ready=True sector_rank=15 price=134.98 support=130.01 resistance=139.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.2 liquidity=18918006.0 spike=1.87
- ALCN.CA: score=23.4 buy_ready=False sector_rank=12 price=29.64 support=28.4 resistance=30.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.36 liquidity=17856962.0 spike=0.63
- ALUM.CA: score=24.4 buy_ready=True sector_rank=15 price=25.14 support=20.95 resistance=26.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.5 liquidity=16309217.0 spike=0.74
- AMER.CA: score=26.4 buy_ready=True sector_rank=4 price=2.76 support=2.29 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.3 liquidity=82152928.0 spike=0.63
- AMES.CA: score=11.29 buy_ready=False sector_rank=15 price=50.45 support=48.0 resistance=62.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=32.0 liquidity=3887181.75 spike=0.25
- AMIA.CA: score=17.4 buy_ready=False sector_rank=15 price=8.8 support=8.05 resistance=10.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=27.69 liquidity=22971002.0 spike=0.67
- AMOC.CA: score=22.4 buy_ready=False sector_rank=13 price=8.32 support=8.12 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.7 liquidity=38735808.0 spike=0.4
- ANFI.CA: score=17.37 buy_ready=False sector_rank=15 price=14.02 support=13.5 resistance=15.55 source=Yahoo Finance as_of=2026-06-02T21:00:00+00:00 freshness=FRESH RSI=55.39 liquidity=4973791.44 spike=0.24
- APSW.CA: score=14.89 buy_ready=False sector_rank=15 price=9.02 support=8.62 resistance=9.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=57.29 liquidity=492939.66 spike=0.4
- ARAB.CA: score=28.4 buy_ready=True sector_rank=4 price=0.21 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=71245000.0 spike=0.95
- ARCC.CA: score=29.52 buy_ready=True sector_rank=8 price=58.81 support=52.6 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.33 liquidity=67163240.0 spike=1.56
- AREH.CA: score=26.5 buy_ready=True sector_rank=15 price=1.4 support=1.27 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.91 liquidity=41730576.0 spike=2.05
- ARVA.CA: score=30.24 buy_ready=True sector_rank=15 price=10.6 support=7.71 resistance=10.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=64.71 liquidity=44943404.0 spike=1.92
- ASCM.CA: score=28.4 buy_ready=False sector_rank=15 price=55.1 support=43.76 resistance=58.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.54 liquidity=194916464.0 spike=3.69
- ASPI.CA: score=14.4 buy_ready=False sector_rank=15 price=0.39 support=0.34 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=382521024.0 spike=13.9
- ATLC.CA: score=12.47 buy_ready=False sector_rank=17 price=4.92 support=4.71 resistance=5.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=31.76 liquidity=5623872.5 spike=0.67
- ATQA.CA: score=24.81 buy_ready=True sector_rank=19 price=10.03 support=9.41 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=77396016.0 spike=1.63
- AXPH.CA: score=8.34 buy_ready=False sector_rank=15 price=1119.17 support=910.0 resistance=1239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=4.95 liquidity=935200.88 spike=0.16
- BINV.CA: score=24.19 buy_ready=False sector_rank=3 price=46.5 support=40.29 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.97 liquidity=8789524.0 spike=0.67
- BIOC.CA: score=11.81 buy_ready=False sector_rank=15 price=74.23 support=69.0 resistance=79.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=30.48 liquidity=2407165.25 spike=0.3
- BTFH.CA: score=21.85 buy_ready=False sector_rank=17 price=3.12 support=3.02 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.27 liquidity=180052480.0 spike=0.74
- CAED.CA: score=9.52 buy_ready=False sector_rank=15 price=71.39 support=61.6 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.74 liquidity=2122714.5 spike=0.13
- CANA.CA: score=18.65 buy_ready=False sector_rank=18 price=36.1 support=33.13 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.89 liquidity=5933393.0 spike=0.37
- CCAP.CA: score=23.4 buy_ready=True sector_rank=3 price=5.36 support=4.47 resistance=5.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=67.53 liquidity=402771840.0 spike=0.48
- CCRS.CA: score=24.4 buy_ready=False sector_rank=15 price=2.53 support=1.96 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=70.24 liquidity=25487538.0 spike=0.94
- CEFM.CA: score=14.27 buy_ready=False sector_rank=15 price=105.56 support=97.1 resistance=119.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.8 liquidity=1872836.63 spike=0.25
- CERA.CA: score=23.5 buy_ready=True sector_rank=15 price=1.18 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=14206700.0 spike=1.05
- CFGH.CA: score=4.57 buy_ready=False sector_rank=15 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=6310.68 spike=1.58
- CICH.CA: score=10.07 buy_ready=False sector_rank=17 price=12.42 support=10.9 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=33.85 liquidity=1224475.0 spike=0.27
- CIEB.CA: score=16.29 buy_ready=False sector_rank=18 price=23.7 support=23.31 resistance=24.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=48.68 liquidity=4576629.5 spike=0.33
- CIRA.CA: score=21.32 buy_ready=True sector_rank=14 price=27.13 support=19.35 resistance=28.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=6916205.5 spike=0.24
- CLHO.CA: score=24.52 buy_ready=True sector_rank=5 price=15.89 support=14.58 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=58.7 liquidity=44332680.0 spike=1.06
- CNFN.CA: score=15.85 buy_ready=False sector_rank=17 price=4.6 support=4.4 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=32.91 liquidity=11884073.0 spike=0.75
- COMI.CA: score=21.71 buy_ready=False sector_rank=18 price=132.48 support=131.5 resistance=144.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.0 liquidity=362467168.0 spike=0.55
- COPR.CA: score=18.4 buy_ready=False sector_rank=15 price=0.36 support=0.29 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=75.76 liquidity=31690976.0 spike=0.86
- COSG.CA: score=14.4 buy_ready=False sector_rank=15 price=1.66 support=1.56 resistance=1.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=225115232.0 spike=5.41
- CPCI.CA: score=20.36 buy_ready=True sector_rank=15 price=361.13 support=315.1 resistance=383.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=40.06 liquidity=5955157.0 spike=0.78
- CSAG.CA: score=26.4 buy_ready=True sector_rank=12 price=32.2 support=30.05 resistance=32.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=54.4 liquidity=20323754.0 spike=1.0
- DAPH.CA: score=13.44 buy_ready=False sector_rank=15 price=81.0 support=79.25 resistance=96.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=13.69 liquidity=6037539.0 spike=0.19
- DEIN.CA: score=10.4 buy_ready=False sector_rank=15 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-02T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=8.91 buy_ready=False sector_rank=10 price=24.96 support=24.5 resistance=26.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=33.72 liquidity=1510897.38 spike=0.65
- DSCW.CA: score=15.4 buy_ready=False sector_rank=15 price=1.86 support=1.71 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.03 liquidity=73118880.0 spike=0.97
- DTPP.CA: score=9.05 buy_ready=False sector_rank=15 price=126.75 support=121.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.39 liquidity=1647382.13 spike=0.24
- EALR.CA: score=9.91 buy_ready=False sector_rank=15 price=361.48 support=346.01 resistance=429.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=32.24 liquidity=2508298.25 spike=0.11
- EASB.CA: score=8.68 buy_ready=False sector_rank=15 price=4.85 support=4.61 resistance=5.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=29.82 liquidity=1277724.25 spike=0.49
- EAST.CA: score=24.4 buy_ready=True sector_rank=10 price=38.65 support=36.6 resistance=39.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=43.35 liquidity=25653858.0 spike=0.36
- EBSC.CA: score=14.4 buy_ready=False sector_rank=15 price=1.94 support=1.8 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17174218.0 spike=7.38
- ECAP.CA: score=23.5 buy_ready=True sector_rank=15 price=31.08 support=28.7 resistance=31.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.11 liquidity=8156972.5 spike=1.47
- EDFM.CA: score=14.72 buy_ready=False sector_rank=15 price=338.32 support=320.2 resistance=378.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=52.06 liquidity=322636.19 spike=0.28
- EEII.CA: score=24.4 buy_ready=True sector_rank=15 price=2.37 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.94 liquidity=17166230.0 spike=0.92
- EFIC.CA: score=9.26 buy_ready=False sector_rank=19 price=206.08 support=195.25 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=35.8 liquidity=713649.31 spike=0.15
- EFID.CA: score=24.68 buy_ready=True sector_rank=10 price=29.01 support=27.49 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.55 liquidity=54608980.0 spike=1.14
- EFIH.CA: score=22.1 buy_ready=False sector_rank=16 price=22.04 support=20.35 resistance=22.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.74 liquidity=37485672.0 spike=0.57
- EGAL.CA: score=23.55 buy_ready=True sector_rank=19 price=326.01 support=295.0 resistance=344.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.52 liquidity=29168392.0 spike=0.24
- EGAS.CA: score=22.4 buy_ready=True sector_rank=13 price=50.58 support=46.51 resistance=51.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.61 liquidity=8001536.5 spike=0.39
- EGBE.CA: score=12.22 buy_ready=False sector_rank=18 price=0.45 support=0.41 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.56 liquidity=171463.81 spike=1.17
- EGCH.CA: score=22.55 buy_ready=False sector_rank=19 price=14.64 support=11.64 resistance=15.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.42 liquidity=76957920.0 spike=0.62
- EGSA.CA: score=9.4 buy_ready=False sector_rank=7 price=9.02 support=8.12 resistance=9.19 source=Yahoo Finance as_of=2026-06-02T21:00:00+00:00 freshness=FRESH RSI=82.14 liquidity=902.0 spike=0.07
- EGTS.CA: score=9.74 buy_ready=False sector_rank=4 price=19.92 support=19.66 resistance=21.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=120745632.0 spike=1.17
- EHDR.CA: score=31.4 buy_ready=False sector_rank=15 price=2.72 support=2.25 resistance=2.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.43 liquidity=234513760.0 spike=5.96
- EKHO.CA: score=14.4 buy_ready=False sector_rank=13 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-02T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=19.54 buy_ready=False sector_rank=6 price=2.17 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.82 liquidity=47692468.0 spike=1.57
- ELKA.CA: score=27.46 buy_ready=True sector_rank=15 price=1.32 support=1.12 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=74489424.0 spike=2.03
- ELNA.CA: score=4.36 buy_ready=False sector_rank=15 price=38.29 support=38.67 resistance=42.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=519159.03 spike=1.22
- ELSH.CA: score=28.4 buy_ready=False sector_rank=15 price=12.01 support=7.77 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=88.62 liquidity=270651872.0 spike=3.7
- ELWA.CA: score=12.14 buy_ready=False sector_rank=15 price=2.03 support=1.79 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=81.48 liquidity=738749.81 spike=0.25
- EMFD.CA: score=31.4 buy_ready=True sector_rank=4 price=12.25 support=9.83 resistance=12.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.59 liquidity=845328000.0 spike=5.57
- ENGC.CA: score=19.84 buy_ready=True sector_rank=15 price=33.74 support=32.31 resistance=35.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.24 liquidity=5438804.0 spike=0.4
- EOSB.CA: score=16.37 buy_ready=False sector_rank=15 price=1.42 support=1.34 resistance=1.54 source=Yahoo Finance as_of=2026-06-02T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=348168.37 spike=2.81
- EPCO.CA: score=26.44 buy_ready=True sector_rank=15 price=9.34 support=8.56 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.16 liquidity=24142972.0 spike=2.02
- EPPK.CA: score=12.78 buy_ready=False sector_rank=15 price=12.27 support=12.0 resistance=13.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.49 liquidity=1840410.88 spike=1.77
- ETEL.CA: score=24.4 buy_ready=True sector_rank=7 price=96.81 support=91.0 resistance=101.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.59 liquidity=90135176.0 spike=0.8
- ETRS.CA: score=27.18 buy_ready=False sector_rank=15 price=9.3 support=7.37 resistance=8.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=66897572.0 spike=1.39
- EXPA.CA: score=21.71 buy_ready=False sector_rank=18 price=18.41 support=18.13 resistance=19.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.63 liquidity=27859526.0 spike=0.66
- FAIT.CA: score=15.28 buy_ready=True sector_rank=18 price=37.96 support=33.46 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=64.56 liquidity=1571151.5 spike=0.2
- FAITA.CA: score=16.28 buy_ready=False sector_rank=18 price=1.0 support=0.97 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=39.39 liquidity=129552.12 spike=2.22
- FERC.CA: score=12.11 buy_ready=False sector_rank=19 price=77.74 support=76.5 resistance=83.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=14.44 liquidity=8266232.0 spike=1.15
- FWRY.CA: score=24.54 buy_ready=False sector_rank=16 price=19.54 support=19.03 resistance=21.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.89 liquidity=580160832.0 spike=2.22
- GBCO.CA: score=15.91 buy_ready=False sector_rank=20 price=26.31 support=25.25 resistance=29.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=26.42 liquidity=61562264.0 spike=0.53
- GDWA.CA: score=27.8 buy_ready=True sector_rank=15 price=0.81 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.63 liquidity=22706130.0 spike=2.2
- GGCC.CA: score=30.4 buy_ready=True sector_rank=15 price=0.43 support=0.39 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.14 liquidity=31156986.0 spike=7.07
- GIHD.CA: score=20.3 buy_ready=True sector_rank=15 price=42.21 support=39.1 resistance=44.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.51 liquidity=5861036.5 spike=1.02
- GMCI.CA: score=20.1 buy_ready=False sector_rank=15 price=1.8 support=1.67 resistance=1.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=597098.5 spike=1.55
- GRCA.CA: score=21.6 buy_ready=False sector_rank=15 price=57.93 support=53.36 resistance=60.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.74 liquidity=18543708.0 spike=2.1
- GSSC.CA: score=8.81 buy_ready=False sector_rank=15 price=251.47 support=250.0 resistance=275.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=12.4 liquidity=1406603.63 spike=0.11
- GTWL.CA: score=10.93 buy_ready=False sector_rank=15 price=47.83 support=47.5 resistance=59.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=23.62 liquidity=3526162.5 spike=0.29
- HDBK.CA: score=20.68 buy_ready=False sector_rank=18 price=141.19 support=140.0 resistance=150.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=42.1 liquidity=8965936.0 spike=0.49
- HELI.CA: score=24.4 buy_ready=True sector_rank=4 price=6.58 support=6.17 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.53 liquidity=55562896.0 spike=0.28
- HRHO.CA: score=13.85 buy_ready=False sector_rank=17 price=27.03 support=26.16 resistance=30.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.34 liquidity=67815640.0 spike=0.32
- ICID.CA: score=26.7 buy_ready=False sector_rank=15 price=5.9 support=4.3 resistance=5.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=77.73 liquidity=28309684.0 spike=2.65
- IDRE.CA: score=24.4 buy_ready=True sector_rank=15 price=45.7 support=38.55 resistance=49.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.43 liquidity=27011888.0 spike=0.8
- IFAP.CA: score=14.4 buy_ready=False sector_rank=11 price=19.79 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=28.77 liquidity=10241869.0 spike=0.46
- INFI.CA: score=12.93 buy_ready=False sector_rank=15 price=102.46 support=98.2 resistance=112.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.43 liquidity=6525707.5 spike=0.36
- IRON.CA: score=18.96 buy_ready=False sector_rank=19 price=32.95 support=31.83 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.72 liquidity=7416430.0 spike=0.81
- ISMA.CA: score=21.4 buy_ready=False sector_rank=15 price=27.58 support=19.05 resistance=27.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=98.69 liquidity=32760328.0 spike=0.67
- ISMQ.CA: score=25.55 buy_ready=True sector_rank=19 price=7.86 support=7.27 resistance=8.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.3 liquidity=50576760.0 spike=0.89
- ISPH.CA: score=31.34 buy_ready=True sector_rank=5 price=12.54 support=10.8 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.59 liquidity=324024800.0 spike=2.47
- JUFO.CA: score=26.96 buy_ready=True sector_rank=10 price=29.92 support=26.51 resistance=29.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=43.15 liquidity=63511268.0 spike=1.28
- KABO.CA: score=24.4 buy_ready=True sector_rank=9 price=6.41 support=5.92 resistance=6.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=67.03 liquidity=10227203.0 spike=0.58
- KWIN.CA: score=13.46 buy_ready=False sector_rank=15 price=72.98 support=69.0 resistance=82.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=20.98 liquidity=6063182.5 spike=0.93
- KZPC.CA: score=10.71 buy_ready=False sector_rank=15 price=10.62 support=10.3 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=28.12 liquidity=3307997.5 spike=0.24
- LCSW.CA: score=22.4 buy_ready=False sector_rank=8 price=27.12 support=26.11 resistance=29.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.0 liquidity=12486387.0 spike=0.72
- LUTS.CA: score=26.48 buy_ready=True sector_rank=15 price=0.58 support=0.54 resistance=0.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.76 liquidity=12591775.0 spike=2.04
- MAAL.CA: score=24.22 buy_ready=False sector_rank=15 price=5.75 support=4.44 resistance=5.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=92.04 liquidity=13705076.0 spike=1.41
- MASR.CA: score=24.4 buy_ready=True sector_rank=15 price=6.94 support=6.18 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.43 liquidity=23270414.0 spike=0.34
- MBSC.CA: score=24.4 buy_ready=True sector_rank=8 price=272.43 support=258.5 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.2 liquidity=34568452.0 spike=0.73
- MCQE.CA: score=20.04 buy_ready=True sector_rank=8 price=195.0 support=188.01 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.78 liquidity=5636474.5 spike=0.27
- MCRO.CA: score=25.4 buy_ready=True sector_rank=15 price=1.27 support=1.21 resistance=1.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.0 liquidity=30150396.0 spike=0.29
- MENA.CA: score=24.52 buy_ready=True sector_rank=4 price=7.09 support=5.75 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.73 liquidity=16441040.0 spike=1.06
- MEPA.CA: score=24.7 buy_ready=True sector_rank=15 price=1.74 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=30107532.0 spike=1.15
- MFPC.CA: score=21.55 buy_ready=False sector_rank=19 price=42.97 support=42.55 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=37.75 liquidity=44461516.0 spike=0.35
- MFSC.CA: score=24.4 buy_ready=True sector_rank=15 price=48.45 support=32.23 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.51 liquidity=11333278.0 spike=0.8
- MHOT.CA: score=27.4 buy_ready=True sector_rank=1 price=31.73 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.33 liquidity=17231084.0 spike=0.91
- MICH.CA: score=24.58 buy_ready=True sector_rank=15 price=36.53 support=34.96 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=64.27 liquidity=6183089.0 spike=0.68
- MILS.CA: score=24.4 buy_ready=True sector_rank=15 price=140.0 support=117.5 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.93 liquidity=11003417.0 spike=0.38
- MIPH.CA: score=10.82 buy_ready=False sector_rank=5 price=669.42 support=640.0 resistance=740.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=31.31 liquidity=3416342.75 spike=0.67
- MOED.CA: score=11.78 buy_ready=False sector_rank=15 price=0.7 support=0.68 resistance=0.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=10.14 liquidity=8382266.5 spike=0.61
- MOIL.CA: score=17.71 buy_ready=False sector_rank=13 price=0.48 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=294339.06 spike=1.51
- MOIN.CA: score=15.03 buy_ready=False sector_rank=15 price=25.35 support=23.13 resistance=26.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=59.52 liquidity=628427.69 spike=0.2
- MOSC.CA: score=15.64 buy_ready=False sector_rank=15 price=278.72 support=271.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=14.67 liquidity=8237223.5 spike=0.31
- MPCI.CA: score=24.4 buy_ready=True sector_rank=15 price=219.48 support=173.03 resistance=224.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=51.27 liquidity=87996936.0 spike=0.94
- MPCO.CA: score=14.4 buy_ready=False sector_rank=11 price=1.84 support=1.67 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=365360224.0 spike=8.89
- MPRC.CA: score=29.08 buy_ready=True sector_rank=15 price=32.8 support=30.01 resistance=33.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.63 liquidity=24478056.0 spike=1.34
- MTIE.CA: score=20.89 buy_ready=False sector_rank=20 price=9.1 support=8.71 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.53 liquidity=9985672.0 spike=0.31
- NAHO.CA: score=15.57 buy_ready=False sector_rank=15 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=168101.81 spike=4.56
- NCCW.CA: score=14.4 buy_ready=False sector_rank=15 price=6.12 support=5.3 resistance=6.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=134405584.0 spike=12.16
- NEDA.CA: score=15.24 buy_ready=False sector_rank=15 price=2.78 support=2.65 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=842732.31 spike=0.93
- NHPS.CA: score=10.31 buy_ready=False sector_rank=15 price=69.03 support=67.56 resistance=76.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.21 liquidity=3907082.25 spike=0.31
- NINH.CA: score=14.27 buy_ready=False sector_rank=15 price=18.11 support=17.53 resistance=20.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=36.74 liquidity=1874166.38 spike=0.1
- NIPH.CA: score=17.4 buy_ready=False sector_rank=5 price=163.0 support=146.21 resistance=186.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.81 liquidity=65706240.0 spike=0.55
- OBRI.CA: score=14.86 buy_ready=False sector_rank=15 price=34.71 support=34.53 resistance=39.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=23.2 liquidity=17096782.0 spike=1.23
- OCDI.CA: score=22.4 buy_ready=False sector_rank=4 price=21.55 support=20.19 resistance=23.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.3 liquidity=14129542.0 spike=0.3
- OCPH.CA: score=13.29 buy_ready=False sector_rank=15 price=355.0 support=350.0 resistance=416.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=7.85 liquidity=5886450.0 spike=0.31
- ODIN.CA: score=28.66 buy_ready=True sector_rank=15 price=2.1 support=1.89 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.83 liquidity=22485632.0 spike=2.13
- OFH.CA: score=26.38 buy_ready=True sector_rank=15 price=0.64 support=0.6 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.55 liquidity=43179172.0 spike=1.99
- OIH.CA: score=16.4 buy_ready=False sector_rank=3 price=1.41 support=1.44 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=229276448.0 spike=1.5
- OLFI.CA: score=21.79 buy_ready=False sector_rank=10 price=21.54 support=21.0 resistance=22.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.2 liquidity=9391397.0 spike=0.41
- ORAS.CA: score=7.6 buy_ready=False sector_rank=21 price=735.23 support=730.5 resistance=748.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=89853952.0 spike=1.0
- ORHD.CA: score=24.4 buy_ready=False sector_rank=4 price=38.06 support=30.15 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.72 liquidity=109328032.0 spike=0.5
- ORWE.CA: score=24.4 buy_ready=False sector_rank=9 price=23.49 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=74.9 liquidity=22273934.0 spike=0.45
- PHAR.CA: score=21.08 buy_ready=False sector_rank=5 price=87.32 support=83.96 resistance=92.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=28.74 liquidity=63926908.0 spike=1.84
- PHDC.CA: score=24.4 buy_ready=True sector_rank=4 price=15.12 support=12.23 resistance=16.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.3 liquidity=345124384.0 spike=0.74
- PHTV.CA: score=18.52 buy_ready=False sector_rank=15 price=207.12 support=201.5 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=52.3 liquidity=6116183.5 spike=0.31
- POUL.CA: score=24.4 buy_ready=True sector_rank=10 price=37.73 support=33.8 resistance=39.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=52.13 liquidity=19534588.0 spike=0.35
- PRCL.CA: score=24.4 buy_ready=True sector_rank=8 price=23.71 support=19.79 resistance=25.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.06 liquidity=21427264.0 spike=0.67
- PRDC.CA: score=28.88 buy_ready=True sector_rank=4 price=6.28 support=5.08 resistance=6.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=60.42 liquidity=24540382.0 spike=1.24
- PRMH.CA: score=14.4 buy_ready=False sector_rank=15 price=2.84 support=2.58 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=56690576.0 spike=4.39
- RACC.CA: score=19.06 buy_ready=False sector_rank=15 price=10.02 support=9.56 resistance=12.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.46 liquidity=6658539.0 spike=0.18
- RAKT.CA: score=9.67 buy_ready=False sector_rank=15 price=23.79 support=22.1 resistance=25.81 source=Yahoo Finance as_of=2026-06-02T21:00:00+00:00 freshness=FRESH RSI=43.32 liquidity=389513.68 spike=1.44
- RAYA.CA: score=26.4 buy_ready=True sector_rank=2 price=7.55 support=6.2 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.83 liquidity=102526352.0 spike=0.86
- RMDA.CA: score=24.4 buy_ready=True sector_rank=5 price=5.08 support=4.33 resistance=5.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.98 liquidity=15750339.0 spike=0.27
- ROTO.CA: score=24.4 buy_ready=True sector_rank=15 price=33.61 support=32.66 resistance=36.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=46.1 liquidity=11448348.0 spike=0.83
- RREI.CA: score=24.4 buy_ready=True sector_rank=15 price=3.7 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.89 liquidity=22874820.0 spike=0.97
- RTVC.CA: score=11.18 buy_ready=False sector_rank=15 price=3.83 support=3.75 resistance=4.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.21 liquidity=6783467.0 spike=0.93
- RUBX.CA: score=16.4 buy_ready=False sector_rank=15 price=10.17 support=9.8 resistance=11.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.98 liquidity=10397966.0 spike=0.55
- SAUD.CA: score=20.2 buy_ready=False sector_rank=18 price=22.91 support=21.8 resistance=25.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=37.3 liquidity=8491723.0 spike=0.53
- SCEM.CA: score=17.4 buy_ready=False sector_rank=8 price=65.1 support=61.8 resistance=72.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=32.27 liquidity=40357748.0 spike=0.93
- SCFM.CA: score=13.11 buy_ready=False sector_rank=15 price=261.45 support=242.02 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.82 liquidity=5708212.0 spike=0.19
- SCTS.CA: score=9.72 buy_ready=False sector_rank=14 price=620.61 support=590.01 resistance=709.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=20.02 liquidity=2323418.25 spike=0.19
- SDTI.CA: score=25.66 buy_ready=True sector_rank=15 price=46.56 support=43.15 resistance=46.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.11 liquidity=33881216.0 spike=1.63
- SEIG.CA: score=19.8 buy_ready=True sector_rank=15 price=187.53 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=54.06 liquidity=3398027.0 spike=0.46
- SIPC.CA: score=25.18 buy_ready=True sector_rank=15 price=3.66 support=3.4 resistance=3.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=20102322.0 spike=1.39
- SKPC.CA: score=17.55 buy_ready=False sector_rank=19 price=17.05 support=16.8 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.69 liquidity=49277680.0 spike=0.54
- SMFR.CA: score=12.77 buy_ready=False sector_rank=15 price=208.21 support=203.51 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.65 liquidity=5368903.0 spike=0.45
- SNFC.CA: score=24.4 buy_ready=True sector_rank=15 price=12.41 support=11.66 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=61.27 liquidity=25953510.0 spike=0.9
- SPIN.CA: score=10.36 buy_ready=False sector_rank=9 price=14.25 support=13.69 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.5 liquidity=963649.44 spike=0.2
- SPMD.CA: score=26.96 buy_ready=True sector_rank=15 price=0.42 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.0 liquidity=30596382.0 spike=1.28
- SUGR.CA: score=25.56 buy_ready=True sector_rank=10 price=50.11 support=47.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=62.42 liquidity=9161945.0 spike=0.55
- SVCE.CA: score=24.4 buy_ready=True sector_rank=15 price=9.19 support=7.98 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.67 liquidity=58105052.0 spike=0.34
- SWDY.CA: score=24.4 buy_ready=True sector_rank=6 price=88.54 support=84.27 resistance=91.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.56 liquidity=10292513.0 spike=0.27
- TALM.CA: score=26.26 buy_ready=True sector_rank=14 price=16.0 support=15.12 resistance=17.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=24158882.0 spike=1.93
- TMGH.CA: score=22.4 buy_ready=False sector_rank=4 price=96.5 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.83 liquidity=259913344.0 spike=0.45
- TRTO.CA: score=15.4 buy_ready=False sector_rank=15 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-02T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=3073.6 spike=4.72
- UEFM.CA: score=8.87 buy_ready=False sector_rank=15 price=478.14 support=455.6 resistance=530.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.93 liquidity=467820.72 spike=0.24
- UEGC.CA: score=14.4 buy_ready=False sector_rank=15 price=1.46 support=1.36 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=103985456.0 spike=6.88
- UNIP.CA: score=14.4 buy_ready=False sector_rank=15 price=0.31 support=0.29 resistance=0.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=91624008.0 spike=11.36
- UNIT.CA: score=24.08 buy_ready=True sector_rank=4 price=13.83 support=10.33 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=62.95 liquidity=7678393.5 spike=0.82
- WCDF.CA: score=7.61 buy_ready=False sector_rank=15 price=539.96 support=535.0 resistance=570.0 source=Yahoo Finance as_of=2026-06-02T21:00:00+00:00 freshness=FRESH RSI=11.92 liquidity=209504.49 spike=0.3
- WKOL.CA: score=9.86 buy_ready=False sector_rank=15 price=295.83 support=290.0 resistance=349.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=25.98 liquidity=2461777.25 spike=0.15
- ZEOT.CA: score=27.02 buy_ready=True sector_rank=15 price=9.21 support=8.43 resistance=9.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.17 liquidity=20170256.0 spike=2.31
- ZMID.CA: score=24.4 buy_ready=True sector_rank=4 price=6.02 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.97 liquidity=159614304.0 spike=0.82

## Backtesting Lite
- EMFD.CA: 180d return=43.56%, max drawdown=-15.54%, MA20>MA50 days last20=20, as_of=2026-06-02T21:00:00+00:00
- EHDR.CA: 180d return=654.6%, max drawdown=-21.74%, MA20>MA50 days last20=20, as_of=2026-06-02T21:00:00+00:00
- ISPH.CA: 180d return=21.6%, max drawdown=-23.92%, MA20>MA50 days last20=20, as_of=2026-06-02T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- EMFD.CA: status=RECENT_ACCEPTED latest=2026-06-01 age_days=3 sources=3 expected=Emaar Misr for Development summary=Emaar Misr for Development (EMFD.CA) has reported its Q1 2026 financial results, showing significant profit increases. The company also announced a change in its CEO role and released its full-year 2025 earnings.
  - Emaar Misr for Development (EMFD.CA) Reports its Financial Results (Consolidated) for the Period from 01/01/2026 to 31/03/2026 (June 01, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVr0j7BAEJFgmlmw4bjinccmfLxx4KvMbM7fXVHve5x-nLW5lG1_37m_FQTNcsApEhOQvJbNoPmrpVrqubd7bS7ago76iT-89Gyvekf08bGkEkrsYDlhTFeE1chg_5ZhIBnNzjevgLM52CdJoNknHYwcM=
  - Emaar Misr for Development (EMFD.CA) Reports its Financial Results (Standalone) for the Period from 01/01/2026 to 31/03/2026 (June 01, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUK4edRoV_fIB69SpMgziqGUmzVCXUuPms_C69fYvEa54qvOimQL3LVkLa9OFmVF--btzNQbwBby3Fe5fcF-abuEiOP5LGA1FcPdaR4c3vnw-VyaL_u8Hv-OF_JhhCO6x9XG39rXEk7gktuPI8u5JROhQ=
  - Emaar Misr for Development Company (S.A.E.) Reports Earnings Results for the Full Year Ended December 31, 2025 (February 23, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnjfO4-pKxrzBOWbRH0x61VjNJ_4b2t45ArJMSHTG5Xe0ex6vDsfzXHmD2LgenkFz2aEa5W9px33TQ9zUeoyWGWiUqpY1cJOUr-i3Dhnk6IS-aze5H1TiMQzHB5jYJgwPe0TmJoywl3AbD1RQT8w9ej8i9Wgg2YFfvuTCsPewK1KYFENGJ866K
- EHDR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=519 sources=3 expected=Egyptians for Housing & Development Co. summary=Egyptians for Housing to disburse EGP 0.01/shr for 2025; EGX-listed companies, banks propose cash dividends for 2025; Egyptians for Housing stock witnesses selling pressures amid key levels to observe – Analysis Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Egyptians for Housing to disburse EGP 0.01/shr for 2025: https://english.mubasher.info/news/4584569/Egyptians-for-Housing-to-disburse-EGP-0-01-shr-for-2025/
  - EGX-listed companies, banks propose cash dividends for 2025: https://english.mubasher.info/news/4560139/EGX-listed-companies-banks-propose-cash-dividends-for-2025/
  - Egyptians for Housing stock witnesses selling pressures amid key levels to observe – Analysis: https://english.mubasher.info/news/4547337/Egyptians-for-Housing-stock-witnesses-selling-pressures-amid-key-levels-to-observe-Analysis/
- ISPH.CA: status=RECENT_ACCEPTED latest=2026-05-18 age_days=17 sources=3 expected=Ibn Sina Pharma summary=Ibn Sina Pharma (ISPH.CA) has released its Q1 2026 and full-year 2025 financial results, declared cash dividends, and secured significant financing from the EBRD for green transformation initiatives.
  - Ibnsina Pharma (ISPH.CA) Reports Its Financial Results (Standalone) for The Period From 01/01/2026 to 31/03/2026 (May 17, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-1NlB-r_SnrX8u6JO_OfJHHpppuuwCVDi9xa7qfwjhxfAzHFKtEhpWWRUaEWSXGeLEk5EjYtWM_wsnUyrgg61eQAZdZDev4Tl5jyey_0Z4LIpn5ZFPZBrFLNHemYJd4o8fYZXsH_NtVC75aAR9A==
  - Release from Ibnsina Pharma (ISPH.CA) Concerning the Consolidated Financial Results (May 18, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgKD8Xfu1WbC1qb5J0CIjD2I-RvqT8g5kvifWbUAbV8SZXbWwViLwFocrqwZNZLwJaCphdhyIXhkr0oeLd3g2xsFqD3ZQtzMYydNTjf9tr-C18aw1SF15lBPsXC3HU7B92ZIyWs_ve-44ogPWw4BA==
  - Ibnsina Pharma Releases Audited FY25 Results (March 02, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWz7c-BfIUqsSW99z8DkD_cEUJ8GNQ9OvMD96L_Ik6EEz1JIv3j0yVzAzPg-gdO74K4r9Cl7NC4wns9BxPAOikUvkkhQD1xuk3_Cumf_vlFK5eFQ6KoZx2
- GGCC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=519 sources=3 expected=Giza General - Contracting and Real Estate Investment S.A.E summary=Giza General - Contracting and Real Estate Investment S.A.E (GGCC.CA) has reported its Q1 2025 financial results and 9M 2025 consolidated net profits. The company has also been awarded several new projects.
  - Giza General Contracting (GGCC.CA) Reports Its Financial Results (Standalone) for the Period from 01/01/2025 to 31/03/2025 (Date not specified, but within 12 months of current date): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMq0JPG_FfvvGjdD1rWQx3MUoUAbq-5OZk6Xj-71thXZ_tEAqV8rJvWsXyYu8wdAOkghYkPCnpZhOzERTUq86VfjoJkFcguZkF6SSIIaAqLOtBRqUdL1WCcrqhlVZjrXUJvsKTtnRh3W3siXfRPQ==
  - Giza General Contracting and Real Estate Investment Company consolidated net profits after tax reached EGP 140.07 million in 9M 2025 (Date not specified, but within 12 months of current date): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVGS_r1jH1zxLD-4g_t1LxSkNmoZa1T1VcCo7aHfdS7YU52J7iYrOe7yOQb1TTaKBwpc9n6FgMQ6d9qW_V_7PK7Bc6HCopm4Orzx-ZbosWX7-lbpR0hE1D_vHL2I1TeU2YmedYfVaRnIoB6Y1pJdYVXgJcMsU=
  - Giza General Contracting and Real Estate Investment Company awarded a project contract valued at EGP 539.11 million (Date not specified, but within 12 months of current date): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVGS_r1jH1zxLD-4g_t1LxSkNmoZa1T1VcCo7aHfdS7YU52J7iYrOe7yOQb1TTaKBwpc9n6FgMQ6d9qW_V_7PK7Bc6HCopm4Orzx-ZbosWX7-lbpR0hE1D_vHL2I1TeU2YmedYfVaRnIoB6Y1pJdYVXgJcMsU=
- ARVA.CA: status=RECENT_ACCEPTED latest=2026-05-25 age_days=10 sources=3 expected=Arab Valves Company summary=Arab Valves Company (ARVA.CA) experienced a suspension of trading in late 2025 and has released its Q4 2025 financial performance. A disclosure form was also released in May 2026.
  - Suspension of Trading on Arab Valves Company (ARVA.CA) (November 30, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHIzlDalywYuRIgWsbz4A9ZACJKgz74vrl03wBH4TjdCjbfztBpnIhlBfWQPyjl8N4kW6ChZN6wUa1o1baouCXzrKF5DOA3J2pPEic0ABcOx3j5rqevZUbtMa7L4HtOpo6kIs11feBaK-jdtx5itG2rL6ezV2kq0_qoZ0K0FAHNsLVsazfa2lhdMBLy47hF9JH
  - EGX:ARVA Financials | Arab Valves Co - Investing.com (Q4 2025 financial data, accessed May 25, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIsFYmqYHxCNzmA--7rllmO-s_AefnPaXv5JxSFvEcofYbn9KlFz-iDi6ePC52WXChcdCPisS3Rs_F6JuDo5EGUO6KNeswhvhBVaSCboyn3kzw9GW0AvB7AckwPYH8I8vprDAv_0AdB-kc6MWcIRjx-oEl2Jr2EsVBHWbUKdXolywi
  - Arab Valves Company (EGX:ARVA) Stock Price & Overview - 2025 Financial Performance (Accessed May 25, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoeSBgbT224hAnyDWf2oeKEFUhJssAdBeS5NnZy-qQk7bPq2_7Hf86GFG1qiwExK5JYbmtFFXO78e1F0TvlbthMbComkj4p0vObQojD6upW64hyenp6CLleGh3NToWb8SjzHQ=
- ARCC.CA: status=RECENT_ACCEPTED latest=2026-06-04 age_days=0 sources=3 expected=Arabian Cement Company summary=Arabian Cement Company (ARCC.CA) has reported its Q1 2026 financial results and announced dividend details for April 2026. The company also saw significant growth in revenue and earnings in 2025.
  - Arabian Cement Company (ARCC.CA) Reports its Financial Results (Standalone) for the Period from 01/01/2026 to 31/03/2026 (June 01, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4uccIP7tzC_e6LMuXd0VhbDa1symcAL6Ti8QT_UyZU_SWeMe_RDaVLBJZFYFCSfuzOL37YvHfYcOqz5POzQm-WMr7brxqJl97a36jzTrSaSYVf6DtEdyASweOnH3cBu_qIYgXIcqatgXWujw_5lVuUK5x8M-nyRQiW9c15l1fn4eYSLnEuCO1UghzQ=
  - Arabian Cement Company (ARCC.CA) - Listing Committee Decision and EGM Minutes (before Certification) (April 26, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTk2O59jzcUr0LPR2syDZU5kScZPPmAZYFCBmulB3iP5KYlb1XwCCj6J7jocZVmaMEZ6DwFkHiY8oxjy9IJyIOw2puR9smYBPmvNFLMhW35zcNc4Uei1l3PvrNxqyPbXbnaW--V8HS41p7sFNGtuE=
  - Arabian Cement Co SAE Stock Price Today | EGX: ARCC Live - Ex-Dividend Date: Apr 14, 2026, Payment Date: Apr 16, 2026 (Accessed June 04, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqFkfsM3xB8Z8ygwZRC-v030a7dN_lVa6PwyXjH9zQABd9muFGTQXODcvSalnUnolRLnKvc-nYPzLMsPp9UwGqzs6JEknyLNB7-c8QXegB2C4ZmJ8sYLmpaJqswxmWWJ8cvDNgouY6A__3bvQslSt60ow=
- ACAMD.CA: status=RECENT_ACCEPTED latest=2026-06-04 age_days=0 sources=3 expected=Arab Co.,for asset management and development summary=Arab Co.,for asset management and development (ACAMD.CA) has reported its 9M 2025 net profits and Q4 2025 EPS. The company has also been involved in discussions regarding land sales and treasury stock purchases, with a Listing Committee Decision in May 2026.
  - Arab Co. for Asset Management And Development (ACAMD) - Arab Company for Asset Management shifts to EGP 7m net profits in 9M-25 (Date not specified, but within 12 months of current date): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHluWUFP70tGXFyN0_6bbNtKsZAb_wwA6NHCodqlfxp1iH92cqNBs2_qgXLSsr9NDeD68gYU_guSzc1iCnyW5N_-gDdDk6ZzZXFNYH0-1AzAvr4jswP0EFtXO-8445fManee977yJKtsU0HKVA56RwSXg==
  - Arab Co. for Asset Management And Development (ACAMD) - EPS -0.03 Egyptian Pound Based on: Fourth Quarter 2025 (Accessed June 04, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHluWUFP70tGXFyN0_6bbNtKsZAb_wwA6NHCodqlfxp1iH92cqNBs2_qgXLSsr9NDeD68gYU_guSzc1iCnyW5N_-gDdDk6ZzZXFNYH0-1AzAvr4jswP0EFtXO-8445fManee977yJKtsU0HKVA56RwSXg==
  - Release from Arab Co.,for asset management and development (ACAMD.CA) concerning an offer to purchase a plot of land (Date not specified, but within 12 months of current date): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJHEx5PbCD8qhMjFOjBUYF4l61z6XB_O0d8Qq7YXlz0fHd_sy_lvDBN1_2uFK7yAT4_jeZDH9DpnXQVcHiqLE0Rhf4PmwPwXXL2xRJUTDQjnwixWxnvnYbUj8hCsf-kBVgsgJ9sjeZx_6QPR8ZQg==
- MPRC.CA: status=RECENT_ACCEPTED latest=2026-05-25 age_days=10 sources=1 expected=Egyptian Media Production City summary=Egyptian Media Production City (MPRC.CA) has reported its Q1 2026 financial results, showing increases in revenue, net income, and EPS.
  - EGX:MPRC Financials | Egyptian Media Production City - Investing.com (Q1 2026 financial data, accessed May 25, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwfpGb_6aue3X8_mQPlI8vFebDVPxVtssNmmMGClWvXFy91hlbkNVV43yH-0EVG9BMF0dHo0u9t7_XR8fbFT3UyIfHXtdaisnJzK6pCi3b2-CgNalA_QfuF0P-dlmMPk57ieHv94y9qtVtjtqjmw1RsgYXK9SuawqsaTaUmA==

## Warnings
- Evidence for EHDR.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for GGCC.CA matches the company but appears old; latest detected date is 2025-01-01.
