# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-06-21T11:17:01.369840+00:00
Generated Cairo: 2026-06-21 14:17
Run timing: target 11:00 Cairo | generated Cairo 2026-06-21 14:17 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-06-21 14:12

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 61
- Data quality issues: 0
- Tradeable price/liquidity tickers: 164/190
- Top sector: Automotive & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, June 21
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 44.44% / above MA50 50.0%
- EGX70 regime: CONSTRUCTIVE / above MA20 57.58% / above MA50 81.82%
- Sector breadth: 71.43%
- Risk mode: SELECTIVE_SMALL_MID_SWINGS

## Top Liquidity
- TMGH.CA: liquidity=747906304.0 spike=1.64 score=25.68
- PHDC.CA: liquidity=355957600.0 spike=0.86 score=24.4
- ANFI.CA: liquidity=340087598.93 spike=4.21 score=28.04
- CCAP.CA: liquidity=285035616.0 spike=0.33 score=21.51
- BTFH.CA: liquidity=247416736.0 spike=1.19 score=25.78

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner highlights KWIN.CA as the top priority BUY watch, followed by MASR.CA and MTIE.CA. All three show price above MA20/MA50, solid liquidity spikes, and RSI in the 55‑62 range, indicating modest bullish momentum. Support levels sit 6‑7% below current prices, while resistance is 4‑5% above, suggesting limited upside in the next 1‑3 days. EGX30 remains bearish, limiting broad‑market risk, whereas EGX70 is constructive, allowing selective small‑mid swing opportunities. Sector breadth is healthy (71%), but KWIN’s sector isn’t leading, adding uncertainty.
- KWIN.CA: price 74.04, support 69.0, resistance 77.0, RSI 62, liquidity spike 4.7× – low confidence, sector lagging
- MASR.CA: price 7.43, support 6.54, resistance 7.4, RSI 61, liquidity spike 1.6× – low confidence, sector not leading
- MTIE.CA: price 9.19, support 8.65, resistance 9.6, RSI 55, liquidity spike modest – low confidence, liquidity cooling
- EGX30 bearish, EGX70 constructive → risk mode SELECTIVE_SMALL_MID_SWINGS, focus on tight setups
- Uncertainty: extended momentum, sector weakness, and short‑term market breadth could reverse quickly

## Top Liquidity Spikes
- TRTO.CA: spike=271.16 liquidity=266831.58 outlook=NEUTRAL score=37.11 buy_ready=False
- EASB.CA: spike=14.45 liquidity=64222636.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ROTO.CA: spike=8.6 liquidity=116186104.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CIRA.CA: spike=6.95 liquidity=108162504.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ZEOT.CA: spike=5.54 liquidity=91798864.0 outlook=CONSTRUCTIVE score=63.11 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=9.87 5d=3.65% 20d=7.93% aboveMA50=100.0%
- #2 Agriculture & Food Production: score=9.31 5d=8.27% 20d=12.06% aboveMA50=50.0%
- #3 Non-bank Financial Services: score=9.06 5d=0.67% 20d=0.0% aboveMA50=60.0%
- #4 Healthcare: score=6.96 5d=1.98% 20d=1.48% aboveMA50=83.33%
- #5 Real Estate: score=6.52 5d=0.9% 20d=5.18% aboveMA50=84.62%
- #6 Industrial Goods & Cables: score=6.16 5d=2.71% 20d=0.5% aboveMA50=50.0%
- #7 Energy & Petrochemicals: score=5.35 5d=0.54% 20d=2.33% aboveMA50=75.0%
- #8 General / Verified EGX Expansion: score=5.11 5d=1.1% 20d=0.92% aboveMA50=64.42%

## Today's Prioritized Action Tickets
- Priority #1: BUY KWIN.CA
  - Entry: 74.04 | Take profit: 79.96 | Stop loss: 71.08
  - Confidence: LOW | score=31.04 | outlook=BULLISH_WATCH 79.11
  - Reason: WATCH/BUY SETUP: KWIN.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 62.26, support 69.0, resistance 77.0, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY MASR.CA
  - Entry: 7.43 | Take profit: 8.03 | Stop loss: 7.13
  - Confidence: LOW | score=29.34 | outlook=BULLISH_WATCH 89.11
  - Reason: WATCH/BUY SETUP: MASR.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 61.24, support 6.54, resistance 7.4, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY MTIE.CA
  - Entry: 9.19 | Take profit: 9.79 | Stop loss: 8.89
  - Confidence: LOW | score=28.75 | outlook=BULLISH_WATCH 97.87
  - Reason: WATCH/BUY SETUP: MTIE.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 55.48, support 8.65, resistance 9.6, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MTIE.CA: BULLISH_WATCH score=97.87 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- BTFH.CA: BULLISH_WATCH score=94.06 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- TMGH.CA: BULLISH_WATCH score=93.52 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- ATLC.CA: BULLISH_WATCH score=92.06 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- HRHO.CA: BULLISH_WATCH score=91.06 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; close to resistance
- MASR.CA: BULLISH_WATCH score=89.11 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- NIPH.CA: BULLISH_WATCH score=87.96 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- MPRC.CA: BULLISH_WATCH score=87.11 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- NHPS.CA: BULLISH_WATCH score=87.11 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CLHO.CA: BULLISH_WATCH score=82.96 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling

## BUY-Ready Candidates
- ATLC.CA: rank=32.4 outlook=BULLISH_WATCH outlook_score=92.06 sector_rank=3 price=5.3 support=4.7 resistance=5.27 liquidity=19248800.0
- KWIN.CA: rank=31.04 outlook=BULLISH_WATCH outlook_score=79.11 sector_rank=8 price=74.04 support=69.0 resistance=77.0 liquidity=23064406.0
- HRHO.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=91.06 sector_rank=3 price=27.6 support=25.8 resistance=27.9 liquidity=117089944.0
- MASR.CA: rank=29.34 outlook=BULLISH_WATCH outlook_score=89.11 sector_rank=8 price=7.43 support=6.54 resistance=7.4 liquidity=94161352.0
- MTIE.CA: rank=28.75 outlook=BULLISH_WATCH outlook_score=97.87 sector_rank=1 price=9.19 support=8.65 resistance=9.6 liquidity=9350850.0
- LCSW.CA: rank=28.25 outlook=BULLISH_WATCH outlook_score=79.13 sector_rank=15 price=28.11 support=26.0 resistance=28.3 liquidity=31362712.0
- MPRC.CA: rank=27.62 outlook=BULLISH_WATCH outlook_score=87.11 sector_rank=8 price=33.54 support=30.61 resistance=34.55 liquidity=55994224.0
- CAED.CA: rank=27.52 outlook=BULLISH_WATCH outlook_score=71.11 sector_rank=8 price=74.21 support=67.21 resistance=79.87 liquidity=15381252.0
- GBCO.CA: rank=27.4 outlook=BULLISH_WATCH outlook_score=75.87 sector_rank=1 price=29.22 support=25.25 resistance=28.81 liquidity=63071048.0
- ADCI.CA: rank=27.04 outlook=BULLISH_WATCH outlook_score=73.11 sector_rank=8 price=232.0 support=206.51 resistance=230.9 liquidity=24329876.0

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=15.24 buy_ready=True sector_rank=8 price=206.97 support=195.1 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=54.01 liquidity=1191811.25 spike=0.18
- ABUK.CA: score=13.76 buy_ready=False sector_rank=21 price=71.91 support=71.06 resistance=86.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=4.08 liquidity=228010480.0 spike=1.64
- ACAMD.CA: score=24.04 buy_ready=True sector_rank=8 price=2.34 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=61.97 liquidity=82715816.0 spike=0.66
- ACGC.CA: score=21.5 buy_ready=False sector_rank=14 price=9.69 support=9.11 resistance=10.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=37.43 liquidity=20795662.0 spike=0.36
- ADCI.CA: score=27.04 buy_ready=True sector_rank=8 price=232.0 support=206.51 resistance=230.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=68.7 liquidity=24329876.0 spike=3.57
- ADIB.CA: score=23.93 buy_ready=False sector_rank=11 price=46.41 support=44.01 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=50.93 liquidity=65079624.0 spike=0.58
- ADPC.CA: score=9.58 buy_ready=False sector_rank=8 price=3.9 support=3.65 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32632226.0 spike=1.27
- AFDI.CA: score=24.04 buy_ready=True sector_rank=8 price=44.05 support=40.15 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=54.73 liquidity=10941921.0 spike=0.67
- AFMC.CA: score=13.36 buy_ready=False sector_rank=8 price=70.66 support=67.0 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=46.63 liquidity=1319969.38 spike=0.24
- AJWA.CA: score=23.08 buy_ready=False sector_rank=8 price=175.02 support=130.01 resistance=188.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=93.13 liquidity=26526404.0 spike=1.02
- ALCN.CA: score=16.26 buy_ready=False sector_rank=10 price=28.59 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=38.58 liquidity=7261040.0 spike=0.49
- ALUM.CA: score=15.28 buy_ready=False sector_rank=8 price=23.49 support=23.02 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=49.34 liquidity=3231005.5 spike=0.2
- AMER.CA: score=22.4 buy_ready=False sector_rank=5 price=2.49 support=2.47 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=36.79 liquidity=29577232.0 spike=0.29
- AMES.CA: score=8.99 buy_ready=False sector_rank=8 price=49.83 support=48.0 resistance=54.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=30.05 liquidity=2943803.0 spike=0.73
- AMIA.CA: score=16.18 buy_ready=True sector_rank=8 price=9.09 support=8.54 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=4132858.0 spike=0.26
- AMOC.CA: score=14.14 buy_ready=False sector_rank=7 price=7.76 support=7.71 resistance=8.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=31.86 liquidity=54524812.0 spike=0.74
- ANFI.CA: score=28.04 buy_ready=False sector_rank=8 price=41.4 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-16T21:00:00+00:00 freshness=FRESH RSI=98.86 liquidity=340087598.93 spike=4.21
- APSW.CA: score=3.39 buy_ready=False sector_rank=8 price=8.62 support=8.24 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=28.92 liquidity=343415.31 spike=0.35
- ARAB.CA: score=22.4 buy_ready=False sector_rank=5 price=0.21 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=67.57 liquidity=29921284.0 spike=0.35
- ARCC.CA: score=21.25 buy_ready=False sector_rank=15 price=56.16 support=53.6 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=50.97 liquidity=11879477.0 spike=0.33
- AREH.CA: score=14.04 buy_ready=False sector_rank=8 price=1.67 support=1.63 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=99359048.0 spike=3.57
- ARVA.CA: score=25.7 buy_ready=False sector_rank=8 price=10.99 support=7.71 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=72.75 liquidity=55032344.0 spike=1.83
- ASCM.CA: score=24.04 buy_ready=False sector_rank=8 price=59.5 support=47.3 resistance=64.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=73.67 liquidity=24931012.0 spike=0.36
- ASPI.CA: score=24.04 buy_ready=True sector_rank=8 price=0.32 support=0.25 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=60.09 liquidity=37204516.0 spike=0.54
- ATLC.CA: score=32.4 buy_ready=True sector_rank=3 price=5.3 support=4.7 resistance=5.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=19248800.0 spike=4.39
- ATQA.CA: score=16.48 buy_ready=False sector_rank=21 price=9.55 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=55.16 liquidity=16146416.0 spike=0.47
- AXPH.CA: score=7.89 buy_ready=False sector_rank=8 price=1117.89 support=1073.0 resistance=1174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=28.66 liquidity=843715.13 spike=0.45
- BINV.CA: score=15.82 buy_ready=True sector_rank=13 price=47.46 support=41.0 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=63.48 liquidity=2307927.25 spike=0.21
- BIOC.CA: score=15.93 buy_ready=True sector_rank=8 price=72.4 support=68.34 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=48.88 liquidity=1886065.5 spike=0.68
- BTFH.CA: score=25.78 buy_ready=True sector_rank=3 price=3.1 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=43.66 liquidity=247416736.0 spike=1.19
- CAED.CA: score=27.52 buy_ready=True sector_rank=8 price=74.21 support=67.21 resistance=79.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=39.03 liquidity=15381252.0 spike=2.74
- CANA.CA: score=22.29 buy_ready=True sector_rank=11 price=37.54 support=34.11 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=58.62 liquidity=6360586.0 spike=0.61
- CCAP.CA: score=21.51 buy_ready=False sector_rank=13 price=5.08 support=4.92 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=285035616.0 spike=0.33
- CCRS.CA: score=21.95 buy_ready=False sector_rank=8 price=2.44 support=2.32 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=58.21 liquidity=9904677.0 spike=0.42
- CEFM.CA: score=10.6 buy_ready=False sector_rank=8 price=102.15 support=100.53 resistance=111.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=41.26 liquidity=1556572.38 spike=0.44
- CERA.CA: score=22.5 buy_ready=False sector_rank=8 price=1.25 support=1.13 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=79.17 liquidity=20639190.0 spike=1.23
- CFGH.CA: score=3.04 buy_ready=False sector_rank=8 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=0.0 spike=0.0
- CICH.CA: score=15.32 buy_ready=False sector_rank=3 price=12.22 support=12.14 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11024051.0 spike=3.46
- CIEB.CA: score=18.14 buy_ready=False sector_rank=11 price=23.91 support=23.27 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=60.1 liquidity=3210693.25 spike=0.46
- CIRA.CA: score=13.89 buy_ready=False sector_rank=12 price=28.57 support=27.17 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=108162504.0 spike=6.95
- CLHO.CA: score=19.58 buy_ready=True sector_rank=4 price=15.9 support=14.25 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=56.73 liquidity=5176447.5 spike=0.18
- CNFN.CA: score=15.4 buy_ready=False sector_rank=3 price=4.77 support=4.54 resistance=4.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=63326272.0 spike=4.21
- COMI.CA: score=25.93 buy_ready=True sector_rank=11 price=136.35 support=129.8 resistance=136.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=51.28 liquidity=86014728.0 spike=0.14
- COPR.CA: score=23.04 buy_ready=True sector_rank=8 price=0.38 support=0.35 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=65.85 liquidity=40458412.0 spike=0.97
- COSG.CA: score=22.04 buy_ready=False sector_rank=8 price=1.59 support=1.49 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=59.57 liquidity=31348982.0 spike=0.45
- CPCI.CA: score=13.38 buy_ready=False sector_rank=8 price=369.82 support=345.01 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=71.29 liquidity=1334031.38 spike=0.61
- CSAG.CA: score=18.3 buy_ready=True sector_rank=10 price=31.58 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=50.66 liquidity=4297105.0 spike=0.33
- DAPH.CA: score=18.96 buy_ready=True sector_rank=8 price=81.38 support=76.6 resistance=83.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=56.52 liquidity=2917508.75 spike=0.26
- DEIN.CA: score=10.04 buy_ready=False sector_rank=8 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=9.01 buy_ready=False sector_rank=9 price=26.12 support=25.75 resistance=26.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5889475.5 spike=3.05
- DSCW.CA: score=24.04 buy_ready=False sector_rank=8 price=1.84 support=1.71 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=26877786.0 spike=0.51
- DTPP.CA: score=4.78 buy_ready=False sector_rank=8 price=117.33 support=114.0 resistance=132.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=16.62 liquidity=734289.81 spike=0.38
- EALR.CA: score=15.6 buy_ready=True sector_rank=8 price=358.67 support=346.01 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=54.36 liquidity=1560904.13 spike=0.42
- EASB.CA: score=14.04 buy_ready=False sector_rank=8 price=8.07 support=7.84 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=64222636.0 spike=14.45
- EAST.CA: score=26.02 buy_ready=True sector_rank=9 price=38.84 support=37.01 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=56.27 liquidity=14117310.0 spike=0.21
- EBSC.CA: score=15.78 buy_ready=False sector_rank=8 price=1.91 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=70.91 liquidity=1735377.75 spike=0.64
- ECAP.CA: score=14.04 buy_ready=False sector_rank=8 price=34.21 support=33.72 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22452196.0 spike=4.33
- EDFM.CA: score=12.58 buy_ready=False sector_rank=8 price=332.38 support=320.2 resistance=355.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=52.43 liquidity=536854.94 spike=0.81
- EEII.CA: score=24.04 buy_ready=True sector_rank=8 price=2.5 support=2.27 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=61.54 liquidity=15754038.0 spike=0.87
- EFIC.CA: score=1.86 buy_ready=False sector_rank=21 price=201.97 support=192.01 resistance=215.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=23.12 liquidity=379364.66 spike=0.15
- EFID.CA: score=19.02 buy_ready=False sector_rank=9 price=27.93 support=27.06 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=43.58 liquidity=27542690.0 spike=0.37
- EFIH.CA: score=17.75 buy_ready=False sector_rank=19 price=21.0 support=20.2 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=35.74 liquidity=30253036.0 spike=0.57
- EGAL.CA: score=12.48 buy_ready=False sector_rank=21 price=295.86 support=297.1 resistance=334.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=24.21 liquidity=57277828.0 spike=0.72
- EGAS.CA: score=20.25 buy_ready=True sector_rank=7 price=51.67 support=47.5 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=69.09 liquidity=8105887.5 spike=0.65
- EGBE.CA: score=11.94 buy_ready=False sector_rank=11 price=0.44 support=0.43 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=44.02 liquidity=12082.38 spike=0.11
- EGCH.CA: score=20.48 buy_ready=False sector_rank=21 price=13.69 support=12.9 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=13955667.0 spike=0.15
- EGSA.CA: score=5.96 buy_ready=False sector_rank=17 price=8.78 support=8.55 resistance=9.19 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=26.47 liquidity=0.0 spike=0.0
- EGTS.CA: score=22.4 buy_ready=False sector_rank=5 price=18.52 support=17.25 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=41.85 liquidity=85291192.0 spike=0.68
- EHDR.CA: score=24.04 buy_ready=True sector_rank=8 price=2.72 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=68.97 liquidity=13025657.0 spike=0.22
- EKHO.CA: score=14.14 buy_ready=False sector_rank=7 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=18.26 buy_ready=False sector_rank=6 price=2.14 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=54.84 liquidity=5856316.0 spike=0.22
- ELKA.CA: score=25.04 buy_ready=True sector_rank=8 price=1.32 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=69.77 liquidity=31186170.0 spike=0.76
- ELNA.CA: score=14.43 buy_ready=False sector_rank=8 price=39.56 support=37.11 resistance=41.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=50.98 liquidity=383269.63 spike=0.94
- ELSH.CA: score=9.04 buy_ready=False sector_rank=8 price=12.8 support=12.71 resistance=13.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=67964648.0 spike=0.37
- ELWA.CA: score=15.93 buy_ready=True sector_rank=8 price=2.09 support=1.84 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=1887109.5 spike=0.6
- EMFD.CA: score=26.4 buy_ready=False sector_rank=5 price=12.3 support=10.02 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=71.01 liquidity=86062832.0 spike=0.31
- ENGC.CA: score=9.04 buy_ready=False sector_rank=8 price=38.17 support=37.0 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11096027.0 spike=0.8
- EOSB.CA: score=18.04 buy_ready=False sector_rank=8 price=1.48 support=1.34 resistance=1.55 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- EPCO.CA: score=22.41 buy_ready=True sector_rank=8 price=9.16 support=8.63 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=62.42 liquidity=4362603.0 spike=0.4
- EPPK.CA: score=16.37 buy_ready=False sector_rank=8 price=12.69 support=11.67 resistance=12.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=47.1 liquidity=324173.66 spike=0.29
- ETEL.CA: score=12.96 buy_ready=False sector_rank=17 price=93.59 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=32.31 liquidity=37483792.0 spike=0.46
- ETRS.CA: score=10.5 buy_ready=False sector_rank=8 price=10.75 support=10.31 resistance=11.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=106104320.0 spike=1.73
- EXPA.CA: score=21.93 buy_ready=False sector_rank=11 price=18.34 support=18.31 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=20198232.0 spike=0.58
- FAIT.CA: score=15.66 buy_ready=True sector_rank=11 price=37.34 support=35.01 resistance=38.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=49.14 liquidity=1733181.38 spike=0.36
- FAITA.CA: score=11.94 buy_ready=False sector_rank=11 price=0.99 support=0.99 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=47.73 liquidity=15752.32 spike=0.34
- FERC.CA: score=4.29 buy_ready=False sector_rank=21 price=75.61 support=75.0 resistance=79.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=24.38 liquidity=2805324.0 spike=0.69
- FWRY.CA: score=12.75 buy_ready=False sector_rank=19 price=18.8 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=32.35 liquidity=53439380.0 spike=0.18
- GBCO.CA: score=27.4 buy_ready=True sector_rank=1 price=29.22 support=25.25 resistance=28.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=66.73 liquidity=63071048.0 spike=0.58
- GDWA.CA: score=23.81 buy_ready=True sector_rank=8 price=0.81 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=61.94 liquidity=8762751.0 spike=0.62
- GGCC.CA: score=18.21 buy_ready=True sector_rank=8 price=0.42 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=59.38 liquidity=5169175.0 spike=0.67
- GIHD.CA: score=16.85 buy_ready=True sector_rank=8 price=41.85 support=35.15 resistance=43.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=59.11 liquidity=2809626.0 spike=0.8
- GMCI.CA: score=16.04 buy_ready=False sector_rank=8 price=1.79 support=1.68 resistance=1.84 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=54.05 liquidity=0.0 spike=0.0
- GRCA.CA: score=5.44 buy_ready=False sector_rank=8 price=53.27 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=30.47 liquidity=1399598.25 spike=0.23
- GSSC.CA: score=8.84 buy_ready=False sector_rank=8 price=249.76 support=228.1 resistance=263.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=21.11 liquidity=4796541.5 spike=0.98
- GTWL.CA: score=18.17 buy_ready=True sector_rank=8 price=48.94 support=45.47 resistance=52.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=50.92 liquidity=2130504.5 spike=0.28
- HDBK.CA: score=13.93 buy_ready=False sector_rank=11 price=157.42 support=146.25 resistance=157.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=73266640.0 spike=4.53
- HELI.CA: score=24.4 buy_ready=True sector_rank=5 price=6.6 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=50.83 liquidity=68526832.0 spike=0.46
- HRHO.CA: score=29.4 buy_ready=True sector_rank=3 price=27.6 support=25.8 resistance=27.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=61.13 liquidity=117089944.0 spike=0.78
- ICID.CA: score=9.04 buy_ready=False sector_rank=8 price=7.6 support=7.4 resistance=7.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10679782.0 spike=0.65
- IDRE.CA: score=24.04 buy_ready=True sector_rank=8 price=44.97 support=41.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=45.41 liquidity=13565503.0 spike=0.6
- IFAP.CA: score=13.94 buy_ready=False sector_rank=2 price=19.17 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=35.91 liquidity=3541535.25 spike=0.47
- INFI.CA: score=9.4 buy_ready=False sector_rank=8 price=93.0 support=93.0 resistance=97.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11707524.0 spike=1.18
- IRON.CA: score=21.6 buy_ready=False sector_rank=21 price=32.82 support=31.3 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=50.32 liquidity=12404634.0 spike=1.56
- ISMA.CA: score=19.04 buy_ready=False sector_rank=8 price=30.24 support=24.05 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=80.54 liquidity=21155752.0 spike=0.5
- ISMQ.CA: score=25.18 buy_ready=True sector_rank=21 price=8.35 support=7.27 resistance=8.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=64.52 liquidity=95465568.0 spike=1.35
- ISPH.CA: score=24.4 buy_ready=True sector_rank=4 price=12.59 support=11.12 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=59.28 liquidity=120059968.0 spike=0.94
- JUFO.CA: score=25.42 buy_ready=True sector_rank=9 price=31.92 support=26.8 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=69.55 liquidity=66233012.0 spike=1.7
- KABO.CA: score=19.0 buy_ready=False sector_rank=14 price=6.24 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=49.49 liquidity=7501902.5 spike=0.38
- KWIN.CA: score=31.04 buy_ready=True sector_rank=8 price=74.04 support=69.0 resistance=77.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=62.26 liquidity=23064406.0 spike=4.74
- KZPC.CA: score=19.42 buy_ready=True sector_rank=8 price=10.71 support=10.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=57.42 liquidity=5376069.5 spike=0.62
- LCSW.CA: score=28.25 buy_ready=True sector_rank=15 price=28.11 support=26.0 resistance=28.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=42.74 liquidity=31362712.0 spike=3.58
- LUTS.CA: score=23.9 buy_ready=False sector_rank=8 price=0.76 support=0.54 resistance=0.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=83.88 liquidity=84364776.0 spike=2.43
- MAAL.CA: score=9.04 buy_ready=False sector_rank=8 price=6.7 support=6.46 resistance=6.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10185372.0 spike=0.73
- MASR.CA: score=29.34 buy_ready=True sector_rank=8 price=7.43 support=6.54 resistance=7.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=61.24 liquidity=94161352.0 spike=1.65
- MBSC.CA: score=21.25 buy_ready=False sector_rank=15 price=251.12 support=247.43 resistance=273.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=48.2 liquidity=14650847.0 spike=0.33
- MCQE.CA: score=11.82 buy_ready=False sector_rank=15 price=178.35 support=174.0 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=25.31 liquidity=8571928.0 spike=0.53
- MCRO.CA: score=21.04 buy_ready=False sector_rank=8 price=1.24 support=1.2 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=19798044.0 spike=0.41
- MENA.CA: score=19.0 buy_ready=True sector_rank=5 price=6.81 support=6.15 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=58.21 liquidity=4604186.5 spike=0.27
- MEPA.CA: score=24.04 buy_ready=True sector_rank=8 price=1.71 support=1.63 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=16723100.0 spike=0.97
- MFPC.CA: score=13.74 buy_ready=False sector_rank=21 price=37.21 support=36.9 resistance=45.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=4.77 liquidity=142657616.0 spike=1.63
- MFSC.CA: score=9.36 buy_ready=False sector_rank=8 price=45.22 support=43.0 resistance=55.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=21.46 liquidity=2319299.0 spike=0.19
- MHOT.CA: score=9.94 buy_ready=False sector_rank=16 price=32.32 support=31.72 resistance=34.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=41538556.0 spike=1.9
- MICH.CA: score=27.3 buy_ready=False sector_rank=8 price=38.99 support=35.05 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=70.19 liquidity=23955490.0 spike=1.63
- MILS.CA: score=17.93 buy_ready=False sector_rank=8 price=138.31 support=130.4 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=62.27 liquidity=5889131.5 spike=0.3
- MIPH.CA: score=17.43 buy_ready=True sector_rank=4 price=694.61 support=647.0 resistance=690.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=56.6 liquidity=2653926.0 spike=1.19
- MOED.CA: score=18.95 buy_ready=False sector_rank=8 price=0.7 support=0.65 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=46.03 liquidity=8906810.0 spike=0.71
- MOIL.CA: score=14.23 buy_ready=False sector_rank=7 price=0.48 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=93952.06 spike=0.58
- MOIN.CA: score=3.83 buy_ready=False sector_rank=8 price=24.09 support=24.12 resistance=25.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=21.12 liquidity=784779.31 spike=0.46
- MOSC.CA: score=16.82 buy_ready=True sector_rank=8 price=281.41 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=53.26 liquidity=2778690.75 spike=0.3
- MPCI.CA: score=11.06 buy_ready=False sector_rank=8 price=238.68 support=221.5 resistance=243.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=158823424.0 spike=2.01
- MPCO.CA: score=26.4 buy_ready=False sector_rank=2 price=1.95 support=1.54 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=71.08 liquidity=32011338.0 spike=0.32
- MPRC.CA: score=27.62 buy_ready=True sector_rank=8 price=33.54 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=60.66 liquidity=55994224.0 spike=2.79
- MTIE.CA: score=28.75 buy_ready=True sector_rank=1 price=9.19 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=55.48 liquidity=9350850.0 spike=0.52
- NAHO.CA: score=8.04 buy_ready=False sector_rank=8 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- NCCW.CA: score=24.04 buy_ready=True sector_rank=8 price=6.31 support=5.13 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=69.02 liquidity=11443815.0 spike=0.41
- NEDA.CA: score=14.04 buy_ready=False sector_rank=8 price=2.81 support=2.65 resistance=2.84 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=61.76 liquidity=0.0 spike=0.0
- NHPS.CA: score=23.34 buy_ready=True sector_rank=8 price=70.41 support=65.03 resistance=71.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=45.56 liquidity=7798098.5 spike=1.75
- NINH.CA: score=9.63 buy_ready=False sector_rank=8 price=17.49 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=43.3 liquidity=588599.88 spike=0.12
- NIPH.CA: score=24.4 buy_ready=True sector_rank=4 price=166.8 support=155.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=72651528.0 spike=0.89
- OBRI.CA: score=21.37 buy_ready=False sector_rank=8 price=35.43 support=33.63 resistance=37.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=56.68 liquidity=8326564.5 spike=0.61
- OCDI.CA: score=14.36 buy_ready=False sector_rank=5 price=22.3 support=21.4 resistance=22.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=118380936.0 spike=3.48
- OCPH.CA: score=9.88 buy_ready=False sector_rank=8 price=338.95 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=26.79 liquidity=5833384.5 spike=1.0
- ODIN.CA: score=26.36 buy_ready=False sector_rank=8 price=2.21 support=1.89 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=71.43 liquidity=12607283.0 spike=1.16
- OFH.CA: score=19.04 buy_ready=False sector_rank=8 price=0.61 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=54.78 liquidity=10620169.0 spike=0.46
- OIH.CA: score=13.51 buy_ready=False sector_rank=13 price=1.36 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=34.29 liquidity=34625484.0 spike=0.39
- OLFI.CA: score=26.94 buy_ready=True sector_rank=9 price=22.41 support=21.0 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=61.21 liquidity=28989132.0 spike=1.46
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=793.04 support=786.0 resistance=797.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=86686632.0 spike=1.0
- ORHD.CA: score=9.86 buy_ready=False sector_rank=5 price=39.42 support=38.36 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=224307760.0 spike=1.23
- ORWE.CA: score=23.5 buy_ready=True sector_rank=14 price=23.28 support=21.65 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=56.81 liquidity=19276158.0 spike=0.46
- PHAR.CA: score=11.94 buy_ready=False sector_rank=4 price=88.97 support=84.51 resistance=88.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=64184004.0 spike=2.27
- PHDC.CA: score=24.4 buy_ready=True sector_rank=5 price=15.91 support=13.4 resistance=16.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=56.98 liquidity=355957600.0 spike=0.86
- PHTV.CA: score=11.36 buy_ready=False sector_rank=8 price=235.0 support=216.31 resistance=238.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36285108.0 spike=2.16
- POUL.CA: score=22.02 buy_ready=False sector_rank=9 price=35.82 support=34.99 resistance=38.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=37.3 liquidity=23909998.0 spike=0.66
- PRCL.CA: score=9.25 buy_ready=False sector_rank=15 price=27.26 support=26.05 resistance=27.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=41799364.0 spike=1.5
- PRDC.CA: score=23.44 buy_ready=False sector_rank=5 price=8.0 support=5.32 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=90.46 liquidity=99929448.0 spike=1.02
- PRMH.CA: score=25.04 buy_ready=False sector_rank=8 price=2.85 support=2.21 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=70.63 liquidity=39542780.0 spike=1.5
- RACC.CA: score=12.55 buy_ready=False sector_rank=8 price=9.87 support=9.38 resistance=10.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=26.88 liquidity=5509471.0 spike=0.54
- RAKT.CA: score=8.04 buy_ready=False sector_rank=8 price=23.03 support=22.0 resistance=24.48 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=48.94 liquidity=0.0 spike=0.0
- RAYA.CA: score=8.28 buy_ready=False sector_rank=18 price=7.5 support=7.3 resistance=7.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=119318480.0 spike=1.26
- RMDA.CA: score=22.4 buy_ready=False sector_rank=4 price=5.09 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=52.66 liquidity=10560489.0 spike=0.12
- ROTO.CA: score=14.04 buy_ready=False sector_rank=8 price=43.71 support=43.22 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=116186104.0 spike=8.6
- RREI.CA: score=26.04 buy_ready=True sector_rank=8 price=3.65 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=62.63 liquidity=11138251.0 spike=0.52
- RTVC.CA: score=17.21 buy_ready=True sector_rank=8 price=3.94 support=3.75 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=55.38 liquidity=3165807.25 spike=0.56
- RUBX.CA: score=10.39 buy_ready=False sector_rank=8 price=9.98 support=9.8 resistance=10.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=44.32 liquidity=2347830.25 spike=0.21
- SAUD.CA: score=12.34 buy_ready=False sector_rank=11 price=21.8 support=20.82 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=36.8 liquidity=3411215.5 spike=0.31
- SCEM.CA: score=18.25 buy_ready=False sector_rank=15 price=61.77 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=38.76 liquidity=11052065.0 spike=0.51
- SCFM.CA: score=6.08 buy_ready=False sector_rank=8 price=249.91 support=248.1 resistance=276.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=34.55 liquidity=2033353.0 spike=0.17
- SCTS.CA: score=8.45 buy_ready=False sector_rank=12 price=598.12 support=565.25 resistance=660.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=28.2 liquidity=1561557.5 spike=0.29
- SDTI.CA: score=26.04 buy_ready=True sector_rank=8 price=48.18 support=43.4 resistance=47.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=62.01 liquidity=10425294.0 spike=0.71
- SEIG.CA: score=14.93 buy_ready=False sector_rank=8 price=186.01 support=174.0 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=54.17 liquidity=881507.31 spike=0.19
- SIPC.CA: score=18.67 buy_ready=False sector_rank=8 price=3.54 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=6626000.0 spike=0.52
- SKPC.CA: score=11.48 buy_ready=False sector_rank=21 price=16.35 support=16.16 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=33.46 liquidity=39204540.0 spike=0.75
- SMFR.CA: score=11.13 buy_ready=False sector_rank=8 price=204.38 support=192.0 resistance=214.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=42.73 liquidity=2082859.25 spike=0.5
- SNFC.CA: score=21.38 buy_ready=False sector_rank=8 price=11.95 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=47.98 liquidity=9336244.0 spike=0.36
- SPIN.CA: score=5.92 buy_ready=False sector_rank=14 price=13.82 support=13.3 resistance=14.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=31.53 liquidity=2423330.5 spike=0.53
- SPMD.CA: score=13.82 buy_ready=False sector_rank=8 price=0.45 support=0.45 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=80062992.0 spike=3.39
- SUGR.CA: score=11.61 buy_ready=False sector_rank=9 price=48.5 support=48.0 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=50.74 liquidity=3590863.75 spike=0.24
- SVCE.CA: score=24.04 buy_ready=True sector_rank=8 price=9.23 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=76615384.0 spike=0.84
- SWDY.CA: score=22.75 buy_ready=True sector_rank=6 price=87.24 support=84.01 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=42.95 liquidity=8350162.5 spike=0.42
- TALM.CA: score=22.35 buy_ready=False sector_rank=12 price=16.25 support=15.12 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=77.6 liquidity=9158163.0 spike=1.15
- TMGH.CA: score=25.68 buy_ready=True sector_rank=5 price=98.0 support=92.91 resistance=100.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=48.52 liquidity=747906304.0 spike=1.64
- TRTO.CA: score=15.31 buy_ready=False sector_rank=8 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 June 11:57 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=266831.58 spike=271.16
- UEFM.CA: score=10.63 buy_ready=False sector_rank=8 price=473.11 support=455.6 resistance=489.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=48.69 liquidity=587998.06 spike=0.73
- UEGC.CA: score=23.36 buy_ready=True sector_rank=8 price=1.46 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=7315543.5 spike=0.29
- UNIP.CA: score=23.04 buy_ready=False sector_rank=8 price=0.34 support=0.28 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=85.92 liquidity=10130957.0 spike=0.43
- UNIT.CA: score=14.98 buy_ready=False sector_rank=5 price=13.71 support=12.5 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=58.26 liquidity=577206.94 spike=0.07
- WCDF.CA: score=11.04 buy_ready=False sector_rank=8 price=537.53 support=450.0 resistance=549.95 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=45.74 liquidity=0.0 spike=0.0
- WKOL.CA: score=9.57 buy_ready=False sector_rank=8 price=288.93 support=289.0 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=44.38 liquidity=528117.56 spike=0.16
- ZEOT.CA: score=28.04 buy_ready=False sector_rank=8 price=11.61 support=8.41 resistance=11.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=83.5 liquidity=91798864.0 spike=5.54
- ZMID.CA: score=24.4 buy_ready=True sector_rank=5 price=6.3 support=5.77 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=62.77 liquidity=103616168.0 spike=0.49

## Backtesting Lite
- ATLC.CA: 180d return=46.12%, max drawdown=-16.0%, MA20>MA50 days last20=20, as_of=2026-06-17T21:00:00+00:00
- KWIN.CA: 180d return=2.96%, max drawdown=-34.04%, MA20>MA50 days last20=20, as_of=2026-06-17T21:00:00+00:00
- HRHO.CA: 180d return=4.85%, max drawdown=-18.92%, MA20>MA50 days last20=12, as_of=2026-06-17T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ATLC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Al Tawfeek Leasing summary=Evidence rejected for ATLC.CA: source text did not clearly match ATLC.CA / Al Tawfeek Leasing.
- KWIN.CA: status=RECENT_ACCEPTED latest=2026-05-19 age_days=33 sources=3 expected=El Kahera El Watania Investment summary=Recent evidence for El Kahera El Watania Investment (KWIN.CA) includes board decisions, AGM minutes, and financial results for Q1 2026, indicating ongoing corporate activities and financial reporting.
  - El Kahera El Watania Investment (KWIN.CA) - Decisions of the Board of Directors' Meeting (May 18, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQw8KaZJTi5fGxzlVQintG73hJlTeu4krPdqgALJUHLB6DEGQ9mg1UG4CKb3bumRPUtATg1TMZYDkff9h7zvFtob-sNvGh8WNddlCcTOI1KDPTkFz73ILq2iWyyQj3WbXt2rCMU9g4XpuE6UgEufE
  - El Kahera El Watania Investment (KWIN.CA) Reports Its Financial Results (Consolidated) for The Period From 01/01/2026 to 31/03/2026 (May 19, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE50p2_7GLHQPzc3AoUQrEtBV5ba2M8YFZkTgtf_DlsydhhfSaVAxheMEmSvOeS34AHvQx7gnXg4Tk-Z5DchwIUsqk2VOA3MzcE8YghEdhIPu2Wd9o7g1EqGWsfXAnVVaDDH3mEXS2SkfFJIDbF4OiLy50xo-Gmy-zZzIC_EenR-UXA698pqQ
  - El Kahera El Watania Investment (KWIN.CA) - AGM Minutes (Notarized) (April 19, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQw8KaZJTi5fGxzlVQintG73hJlTeu4krPdqgALJUHLB6DEGQ9mg1UG4CKb3bumRPUtATg1TMZYDkff9h7zvFtob-sNvGh8WNddlCcTOI1KDPTkFz73ILq2iWyyQj3WbXt2rCMU9g4XpuE6UgEufE
- HRHO.CA: status=RECENT_ACCEPTED latest=2026-06-11 age_days=10 sources=3 expected=EFG Holding summary=EFG Holding (HRHO.CA) has recently announced a dividend, released Q1 2026 earnings, and made board appointments, reflecting active corporate governance and financial performance.
  - EFG Holding CompanyE (CASE:HRHO) Stock Price - Simply Wall St: Declared Dividend (June 11, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgv34DMixtBXHPPYleNyDqfsek-5y6Pv5e2OwJ3EUdyLo3yIchJz3Ih1GGAzBG0xYDvUkE7dFXFEOeqBrOq1NEuFVXpXpZewaUgP5PJT2-Vhd3XFXImQJAE__F00xS
  - EFG Holding CompanyE (CASE:HRHO) Stock Price - Simply Wall St: Reported Q1 2026 Earnings (May 21, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgv34DMixtBXHPPYleNyDqfsek-5y6Pv5e2OwJ3EUdyLo3yIchJz3Ih1GGAzBG0xYDvUkE7dFXFEOeqBrOq1NEuFVXpXpZewaUgP5PJT2-Vhd3XFXImQJAE__F00xS
  - EFG Holding CompanyE (CASE:HRHO) Stock Price - Simply Wall St: Board Appointments (May 6, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgv34DMixtBXHPPYleNyDqfsek-5y6Pv5e2OwJ3EUdyLo3yIchJz3Ih1GGAzBG0xYDvUkE7dFXFEOeqBrOq1NEuFVXpXpZewaUgP5PJT2-Vhd3XFXImQJAE__F00xS
- MASR.CA: status=RECENT_ACCEPTED latest=2026-06-21 age_days=0 sources=3 expected=Madinet Masr For Housing and Development summary=Madinet Masr For Housing and Development (MASR.CA) has reported strong financial performance for 2025 and Q1 2026, with significant revenue and earnings growth, and analysts maintaining a 'Strong Buy' rating.
  - Madinet Masr For Housing and Development (EGX:MASR) Stock Price & Overview: 2025 Financial Performance (June 21, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGARa6aD6PR_Qu-Q9Gl-73p2XRvbbDwvLzCU5er8am_dJZTILqAE0n5m_FQqWZHavi5vVCUd1svMAjUR0o5S96ayVKVIuMLeVNx0ottfoo9uBsTcVlUDQ_dacoJcx-AeyrM2A==
  - EGX:MASR Financials | Madinet Nasr for Housing and Development SAE - Investing.com: Latest Earnings Release (May 24, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdkM3vvB5kCO3kfQnAiUz7T8iRROeo3MZXp8HvvEbYxpVRh4UWHprZzVbnrpb00SS9qt1WgSv2DucKUw-xKOscof_QZCESb3eXVsNMbiwO4A2WJpA02728Jy4BwE4nMIYiQEzrrGvK5xHVgWudz6KY4Nnkc3xr1ckSQ7MX
  - Madinet Masr for Housing & Development Income Statement – EGX:MASR - TradingView: Q1 2026 Net Income and Revenue (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZAglFUJi1Fd9lLnic7fPH3njm-X2orKc244qiYAtu15nrZaesMyF2b16H_Tp3UYvBaM8PFVHyLHjplfhPBj6iEfpzf6xR4FLtGt1AQbDMRr9GaIoMQzxH6oIyVo4lCejMapx4oVo_F-XqursF1ztNAV6R9CcFYG6rfwIyMaNrmCI6
- MTIE.CA: status=RECENT_ACCEPTED latest=2026-05-21 age_days=31 sources=3 expected=MM Group For Industry and International Trade summary=MM Group For Industry and International Trade (MTIE.CA) has reported Q1 2026 earnings, announced changes in executive management, and seen an increase in its price target, with its next earnings report expected in September 2026.
  - Release from MM Group For Industry And International Trade (MTIE.CA) Concerning the BoD and the Executive Management (March 26, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfYKA4H1qa40Z_CM-ma8rOpwf-TrD-WfuEksVsG2J3TYzsdAGrTEveiOYvDCMfqNpuAQxtjw_Qb0wIm2pPqNfscHS6wbKowi4_rWjx_X3m9cc_ksWQudiZ8-PEz4QwarVXFhWZMYqdKCZTxPGQ7mqUVA==
  - MM Group for Industry and International TradeE (CASE:MTIE) - Stock Analysis: Q1 2026 Earnings Released (May 21, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6mEkhe8GtTo0u0dp1SfmxIaO_KcQPhDY_koeVAUiTf_LC748fxGyWD4ePo-RCjnqYL2BNH37IcwW3C6u5S0C-Z5CymdbJ44dpozOWzVybYdJtE6pppDbkMpUdRBu8NXb_8jpx5UdGcZE4c5BtdAUUb9vvjMu6ou_oktHFHo1ldPTzUgwJrAyPCqJycGLk7nsuvGQz47gMk8BbJRI4Mhk=
  - MM Group For Industry And International Trade (MTIE) - Mubasher Info: AGM and EGM Minutes (before Certification) (May 19, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1l_zNyDaeskAEqdyQCzqTvKOKkhlK48GXXcG5yO5UaD37JvH9tKkfT7JKUCaYWHENMCapZl9gfgDdxGGAR9UP_z9LK1mo_-epLk_FhXqYg7eh7g-rzgF6fGqtxVFTQVwmDyhboCvOwMSxqq_BCQ==
- LCSW.CA: status=RECENT_ACCEPTED latest=2026-04-29 age_days=53 sources=3 expected=Lecico Egypt summary=Lecico Egypt (LCSW.CA) has been active with recent AGM and EGM minutes, financial disclosures, and reported Q1 2026 earnings, alongside its consolidated financial results for the period ending December 2025.
  - Lecico Egypt (LCSW.CA) - AGM Minutes (Notarized) (April 29, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2hG3NieTz-awQ2nUy2A1yfJZQnJ8CpZM_eVO244NjGk6KpP2aImoACiQmz3IvrG9AKyHtogzWIey0U-xZXMbQJOsGzRpwy-MBY_L1CKjgTERKG8H-VTHC9bBuTzwfUUFu6M5SZY_G0JKEO8ctnbQ=
  - Lecico Egypt (LCSW.CA) - Disclosure Form for the BoD & the Shareholders' Structure (April 9, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2hG3NieTz-awQ2nUy2A1yfJZQnJ8CpZM_eVO244NjGk6KpP2aImoACiQmz3IvrG9AKyHtogzWIey0U-xZXMbQJOsGzRpwy-MBY_L1CKjgTERKG8H-VTHC9bBuTzwfUUFu6M5SZY_G0JKEO8ctnbQ=
  - Lecico Egypt (LCSW.CA) Reports Its Financial Results (Consolidated) for The Period ending 31/12/2025 (March 1, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2hG3NieTz-awQ2nUy2A1yfJZQnJ8CpZM_eVO244NjGk6KpP2aImoACiQmz3IvrG9AKyHtogzWIey0U-xZXMbQJOsGzRpwy-MBY_L1CKjgTERKG8H-VTHC9bBuTzwfUUFu6M5SZY_G0JKEO8ctnbQ=
- ANFI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tycoon Holding Company For Financial Investments summary=Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- ZEOT.CA: status=RECENT_ACCEPTED latest=2026-06-07 age_days=14 sources=3 expected=Extracted Oil & Derivatives Co. summary=Extracted Oil & Derivatives Co. (ZEOT.CA) has released recent financial statements and auditor reports, along with Q1 2026 financial results, demonstrating ongoing financial transparency and operational updates.
  - Announcements - Extracted Oils (ZEOT) - Mubasher Info: Release from Extracted Oils (ZEOT.CA) Concerning the Financial Statements (June 7, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdQfr2gFCF42dZyKafO-DVoi1KEP1N_ip6rQguvpsmPpZxmb6bCaxj2Dc0gtU5otqRe7uvogUF8H6ZnUEEQfeWp4E59z9zU3tr7DUlB1V0uwYraZed_4zjxnaJn_wDnNB_uopWuk8mWHU9JuYOoPqFJQ6uxbsgq8PorR-u
  - Announcements - Extracted Oils (ZEOT) - Mubasher Info: The External Auditor's Report (June 7, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdQfr2gFCF42dZyKafO-DVoi1KEP1N_ip6rQguvpsmPpZxmb6bCaxj2Dc0gtU5otqRe7uvogUF8H6ZnUEEQfeWb0L9nTao07cukrf14imuyZiEId96v89qkSPwquNOmkQg-nE3opcTOPT3UIh3trPk_vZeA
  - Announcements - Extracted Oils (ZEOT) - Mubasher Info: Reports its Financial Results for the Period from 01/07/2025 to 31/03/2026 (June 3, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdQfr2gFCF42dZyKafO-DVoi1KEP1N_ip6rQguvpsmPpZxmb6bCaxj2Dc0gtU5otqRe7uvogUF8H6ZnUEEQfeWp4E59z9zU3tr7DUlB1V0uwYraZed_4zjxnaJn_wDnNB_uopWuk8mWHU9JuYOoPqFJQ6uxbsgq8PorR-u

## Warnings
- Evidence rejected for ATLC.CA: source text did not clearly match ATLC.CA / Al Tawfeek Leasing.
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
