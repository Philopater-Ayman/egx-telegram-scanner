# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-06-21T14:43:19.512337+00:00
Generated Cairo: 2026-06-21 17:43
Run timing: target 15:30 Cairo | generated Cairo 2026-06-21 17:43 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-06-21 17:38

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 56
- Data quality issues: 0
- Tradeable price/liquidity tickers: 162/190
- Top sector: Automotive & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, June 21
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 44.44% / above MA50 50.0%
- EGX70 regime: CONSTRUCTIVE / above MA20 54.55% / above MA50 81.82%
- Sector breadth: 71.43%
- Risk mode: SELECTIVE_SMALL_MID_SWINGS

## Top Liquidity
- TMGH.CA: liquidity=1017440896.0 spike=2.23 score=26.86
- PHDC.CA: liquidity=430468832.0 spike=1.04 score=24.48
- CCAP.CA: liquidity=343967008.0 spike=0.4 score=21.55
- ANFI.CA: liquidity=340087598.93 spike=4.21 score=27.99
- BTFH.CA: liquidity=277888032.0 spike=1.34 score=27.08

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner highlighted KWIN.CA, MASR.CA and MTIE.CA as top BUY‑watch candidates. All three show price above MA20/MA50, solid liquidity spikes and clear support‑resistance zones, but confidence is low because momentum is stretched and their sectors are not leading. EGX30 remains bearish while EGX70 is constructive, placing the market in a SELECTIVE_SMALL_MID_SWINGS risk mode – favoring careful, small‑to‑mid swing entries with tight risk controls. Expect modest upside if price respects the identified support levels (≈69 for KWIN, 6.5 for MASR, 8.6 for MTIE) over the next 1‑3 days, but be aware of sector weakness and possible pull‑backs.
- KWIN.CA: price 74.6, support 69, resistance 77, RSI 62 – momentum extended, sector lagging.
- MASR.CA: price 7.4, support 6.5, resistance 7.4, RSI 61 – liquidity strong, sector not leading.
- MTIE.CA: price 9.2, support 8.65, resistance 9.6, RSI 55 – liquidity cooling, sector strong.
- EGX30 bearish vs EGX70 constructive → risk mode SELECTIVE_SMALL_MID_SWINGS.
- Uncertainty: sector weakness and extended momentum could trigger short‑term reversals.

## Top Liquidity Spikes
- TRTO.CA: spike=271.16 liquidity=266831.58 outlook=NEUTRAL score=36.98 buy_ready=False
- EASB.CA: spike=15.17 liquidity=67428160.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ROTO.CA: spike=9.02 liquidity=121913584.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CIRA.CA: spike=7.44 liquidity=115696320.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- PHAR.CA: spike=6.2 liquidity=175066480.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=10.0 5d=3.65% 20d=7.93% aboveMA50=100.0%
- #2 Non-bank Financial Services: score=9.7 5d=0.67% 20d=0.0% aboveMA50=60.0%
- #3 Agriculture & Food Production: score=9.44 5d=8.27% 20d=12.06% aboveMA50=50.0%
- #4 Healthcare: score=7.15 5d=1.98% 20d=1.48% aboveMA50=83.33%
- #5 Real Estate: score=6.61 5d=0.9% 20d=5.18% aboveMA50=84.62%
- #6 Industrial Goods & Cables: score=6.25 5d=2.71% 20d=0.5% aboveMA50=50.0%
- #7 Energy & Petrochemicals: score=5.38 5d=0.54% 20d=2.33% aboveMA50=75.0%
- #8 Food, Beverages & Tobacco: score=5.23 5d=1.44% 20d=2.42% aboveMA50=57.14%

## Today's Prioritized Action Tickets
- Priority #1: BUY KWIN.CA
  - Entry: 74.61 | Take profit: 80.57 | Stop loss: 71.63
  - Confidence: LOW | score=30.99 | outlook=BULLISH_WATCH 78.98
  - Reason: WATCH/BUY SETUP: KWIN.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 62.26, support 69.0, resistance 77.0, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY MASR.CA
  - Entry: 7.4 | Take profit: 8.0 | Stop loss: 7.1
  - Confidence: LOW | score=29.75 | outlook=BULLISH_WATCH 88.98
  - Reason: WATCH/BUY SETUP: MASR.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 61.24, support 6.54, resistance 7.4, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY MTIE.CA
  - Entry: 9.18 | Take profit: 9.76 | Stop loss: 8.89
  - Confidence: LOW | score=29.4 | outlook=BULLISH_WATCH 98.0
  - Reason: WATCH/BUY SETUP: MTIE.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 55.48, support 8.65, resistance 9.6, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MTIE.CA: BULLISH_WATCH score=98.0 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- HRHO.CA: BULLISH_WATCH score=96.7 liquidity=TRADEABLE sector=LEADING risk=close to resistance
- BTFH.CA: BULLISH_WATCH score=94.7 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- TMGH.CA: BULLISH_WATCH score=93.61 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- ATLC.CA: BULLISH_WATCH score=92.7 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- MASR.CA: BULLISH_WATCH score=88.98 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- NIPH.CA: BULLISH_WATCH score=88.15 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- OLFI.CA: BULLISH_WATCH score=87.23 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- MPRC.CA: BULLISH_WATCH score=86.98 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- NHPS.CA: BULLISH_WATCH score=86.98 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- ATLC.CA: rank=33.4 outlook=BULLISH_WATCH outlook_score=92.7 sector_rank=2 price=5.3 support=4.7 resistance=5.27 liquidity=21927126.0
- KWIN.CA: rank=30.99 outlook=BULLISH_WATCH outlook_score=78.98 sector_rank=10 price=74.61 support=69.0 resistance=77.0 liquidity=26228008.0
- HRHO.CA: rank=30.4 outlook=BULLISH_WATCH outlook_score=96.7 sector_rank=2 price=27.52 support=25.8 resistance=27.9 liquidity=134065200.0
- MASR.CA: rank=29.75 outlook=BULLISH_WATCH outlook_score=88.98 sector_rank=10 price=7.4 support=6.54 resistance=7.4 liquidity=106722912.0
- MTIE.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=98.0 sector_rank=1 price=9.18 support=8.65 resistance=9.6 liquidity=10863253.0
- LCSW.CA: rank=28.28 outlook=BULLISH_WATCH outlook_score=79.19 sector_rank=15 price=28.2 support=26.0 resistance=28.3 liquidity=33082138.0
- MPRC.CA: rank=27.87 outlook=BULLISH_WATCH outlook_score=86.98 sector_rank=10 price=33.68 support=30.61 resistance=34.55 liquidity=59002016.0
- GBCO.CA: rank=27.4 outlook=BULLISH_WATCH outlook_score=76.0 sector_rank=1 price=29.07 support=25.25 resistance=28.81 liquidity=71818392.0
- OLFI.CA: rank=27.35 outlook=BULLISH_WATCH outlook_score=87.23 sector_rank=8 price=22.49 support=21.0 resistance=23.08 liquidity=32375112.0
- BTFH.CA: rank=27.08 outlook=BULLISH_WATCH outlook_score=94.7 sector_rank=2 price=3.1 support=2.96 resistance=3.23 liquidity=277888032.0

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=15.74 buy_ready=True sector_rank=10 price=207.04 support=195.1 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.01 liquidity=1745335.5 spike=0.26
- ABUK.CA: score=13.93 buy_ready=False sector_rank=21 price=71.3 support=71.06 resistance=86.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=4.08 liquidity=245013264.0 spike=1.76
- ACAMD.CA: score=23.99 buy_ready=True sector_rank=10 price=2.37 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.97 liquidity=101252640.0 spike=0.81
- ACGC.CA: score=21.54 buy_ready=False sector_rank=14 price=9.69 support=9.11 resistance=10.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=37.43 liquidity=21717816.0 spike=0.38
- ADCI.CA: score=26.99 buy_ready=True sector_rank=10 price=231.71 support=206.51 resistance=230.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=68.7 liquidity=24623434.0 spike=3.61
- ADIB.CA: score=23.87 buy_ready=False sector_rank=12 price=46.81 support=44.01 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.93 liquidity=73478696.0 spike=0.66
- ADPC.CA: score=9.87 buy_ready=False sector_rank=10 price=3.91 support=3.65 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36907228.0 spike=1.44
- AFDI.CA: score=23.99 buy_ready=True sector_rank=10 price=43.97 support=40.15 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.73 liquidity=12052749.0 spike=0.73
- AFMC.CA: score=13.39 buy_ready=False sector_rank=10 price=70.78 support=67.0 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=46.63 liquidity=1402446.0 spike=0.25
- AJWA.CA: score=23.37 buy_ready=False sector_rank=10 price=176.0 support=130.01 resistance=188.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=93.13 liquidity=30992802.0 spike=1.19
- ALCN.CA: score=17.95 buy_ready=False sector_rank=9 price=28.45 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.58 liquidity=8896609.0 spike=0.6
- ALUM.CA: score=15.71 buy_ready=False sector_rank=10 price=23.57 support=23.02 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.34 liquidity=3719176.25 spike=0.23
- AMER.CA: score=22.4 buy_ready=False sector_rank=5 price=2.49 support=2.47 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.79 liquidity=33319964.0 spike=0.33
- AMES.CA: score=9.01 buy_ready=False sector_rank=10 price=49.76 support=48.0 resistance=54.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=30.05 liquidity=3013320.75 spike=0.75
- AMIA.CA: score=17.18 buy_ready=True sector_rank=10 price=9.02 support=8.54 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=5186976.0 spike=0.33
- AMOC.CA: score=14.15 buy_ready=False sector_rank=7 price=7.79 support=7.71 resistance=8.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.86 liquidity=61739552.0 spike=0.84
- ANFI.CA: score=27.99 buy_ready=False sector_rank=10 price=41.4 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-16T21:00:00+00:00 freshness=FRESH RSI=98.86 liquidity=340087598.93 spike=4.21
- APSW.CA: score=3.38 buy_ready=False sector_rank=10 price=8.61 support=8.24 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=28.92 liquidity=386217.44 spike=0.4
- ARAB.CA: score=22.4 buy_ready=False sector_rank=5 price=0.21 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.57 liquidity=38724536.0 spike=0.45
- ARCC.CA: score=21.28 buy_ready=False sector_rank=15 price=56.12 support=53.6 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.97 liquidity=14587450.0 spike=0.4
- AREH.CA: score=13.99 buy_ready=False sector_rank=10 price=1.66 support=1.63 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=110516320.0 spike=3.97
- ARVA.CA: score=25.75 buy_ready=False sector_rank=10 price=11.0 support=7.71 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.75 liquidity=56568052.0 spike=1.88
- ASCM.CA: score=23.99 buy_ready=False sector_rank=10 price=59.34 support=47.3 resistance=64.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=73.67 liquidity=29035682.0 spike=0.42
- ASPI.CA: score=8.99 buy_ready=False sector_rank=10 price=0.33 support=0.31 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=52672628.0 spike=0.77
- ATLC.CA: score=33.4 buy_ready=True sector_rank=2 price=5.3 support=4.7 resistance=5.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=21927126.0 spike=5.0
- ATQA.CA: score=16.41 buy_ready=False sector_rank=21 price=9.51 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.16 liquidity=22418932.0 spike=0.65
- AXPH.CA: score=7.99 buy_ready=False sector_rank=10 price=1118.16 support=1073.0 resistance=1174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=28.66 liquidity=996995.63 spike=0.53
- BINV.CA: score=15.93 buy_ready=True sector_rank=13 price=47.4 support=41.0 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=63.48 liquidity=2376978.5 spike=0.22
- BIOC.CA: score=16.21 buy_ready=True sector_rank=10 price=72.46 support=68.34 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.88 liquidity=2216946.0 spike=0.8
- BTFH.CA: score=27.08 buy_ready=True sector_rank=2 price=3.1 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.66 liquidity=277888032.0 spike=1.34
- CAED.CA: score=12.67 buy_ready=False sector_rank=10 price=74.42 support=73.65 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15928609.0 spike=2.84
- CANA.CA: score=22.3 buy_ready=True sector_rank=12 price=37.55 support=34.11 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.62 liquidity=6428709.0 spike=0.61
- CCAP.CA: score=21.55 buy_ready=False sector_rank=13 price=5.06 support=4.92 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=343967008.0 spike=0.4
- CCRS.CA: score=21.99 buy_ready=False sector_rank=10 price=2.41 support=2.32 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=58.21 liquidity=13146628.0 spike=0.55
- CEFM.CA: score=10.78 buy_ready=False sector_rank=10 price=102.04 support=100.53 resistance=111.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.26 liquidity=1785191.13 spike=0.5
- CERA.CA: score=22.75 buy_ready=False sector_rank=10 price=1.26 support=1.13 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=79.17 liquidity=23235070.0 spike=1.38
- CFGH.CA: score=2.99 buy_ready=False sector_rank=10 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=0.0 spike=0.0
- CICH.CA: score=16.4 buy_ready=False sector_rank=2 price=12.21 support=12.14 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12413366.0 spike=3.89
- CIEB.CA: score=19.29 buy_ready=False sector_rank=12 price=23.91 support=23.27 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=60.1 liquidity=4423287.5 spike=0.63
- CIRA.CA: score=13.96 buy_ready=False sector_rank=11 price=28.61 support=27.17 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=115696320.0 spike=7.44
- CLHO.CA: score=22.72 buy_ready=True sector_rank=4 price=15.9 support=14.25 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=56.73 liquidity=8321664.5 spike=0.29
- CNFN.CA: score=16.4 buy_ready=False sector_rank=2 price=4.76 support=4.54 resistance=4.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=68450816.0 spike=4.55
- COMI.CA: score=25.87 buy_ready=True sector_rank=12 price=137.0 support=129.8 resistance=136.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.28 liquidity=130737232.0 spike=0.21
- COPR.CA: score=23.25 buy_ready=True sector_rank=10 price=0.38 support=0.35 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.85 liquidity=47210644.0 spike=1.13
- COSG.CA: score=21.99 buy_ready=False sector_rank=10 price=1.59 support=1.49 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.57 liquidity=36644648.0 spike=0.53
- CPCI.CA: score=13.85 buy_ready=False sector_rank=10 price=370.0 support=345.01 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=71.29 liquidity=1860174.25 spike=0.86
- CSAG.CA: score=19.42 buy_ready=True sector_rank=9 price=31.56 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.66 liquidity=5359055.0 spike=0.41
- DAPH.CA: score=16.64 buy_ready=False sector_rank=10 price=81.14 support=76.6 resistance=83.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=56.52 liquidity=3646629.5 spike=0.32
- DEIN.CA: score=9.99 buy_ready=False sector_rank=10 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=10.01 buy_ready=False sector_rank=8 price=26.19 support=25.75 resistance=26.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6336502.5 spike=3.29
- DSCW.CA: score=23.99 buy_ready=False sector_rank=10 price=1.83 support=1.71 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=31453560.0 spike=0.59
- DTPP.CA: score=4.73 buy_ready=False sector_rank=10 price=117.33 support=114.0 resistance=132.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=16.62 liquidity=740139.81 spike=0.39
- EALR.CA: score=15.56 buy_ready=True sector_rank=10 price=358.66 support=346.01 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=54.36 liquidity=1568420.13 spike=0.42
- EASB.CA: score=13.99 buy_ready=False sector_rank=10 price=8.02 support=7.84 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=67428160.0 spike=15.17
- EAST.CA: score=26.09 buy_ready=True sector_rank=8 price=38.88 support=37.01 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=56.27 liquidity=16923656.0 spike=0.25
- EBSC.CA: score=15.87 buy_ready=False sector_rank=10 price=1.9 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=70.91 liquidity=1879631.13 spike=0.69
- ECAP.CA: score=13.99 buy_ready=False sector_rank=10 price=34.21 support=33.72 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23590120.0 spike=4.55
- EDFM.CA: score=12.81 buy_ready=False sector_rank=10 price=332.0 support=320.2 resistance=355.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=52.43 liquidity=702791.31 spike=1.06
- EEII.CA: score=23.99 buy_ready=True sector_rank=10 price=2.48 support=2.27 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.54 liquidity=17714400.0 spike=0.98
- EFIC.CA: score=1.8 buy_ready=False sector_rank=21 price=202.08 support=192.01 resistance=215.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=23.12 liquidity=384231.78 spike=0.15
- EFID.CA: score=19.09 buy_ready=False sector_rank=8 price=27.82 support=27.06 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.58 liquidity=34341076.0 spike=0.46
- EFIH.CA: score=17.81 buy_ready=False sector_rank=19 price=21.23 support=20.2 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.74 liquidity=36937748.0 spike=0.7
- EGAL.CA: score=12.41 buy_ready=False sector_rank=21 price=297.1 support=297.1 resistance=334.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.21 liquidity=60510244.0 spike=0.76
- EGAS.CA: score=20.46 buy_ready=True sector_rank=7 price=51.67 support=47.5 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.09 liquidity=8306751.5 spike=0.67
- EGBE.CA: score=11.88 buy_ready=False sector_rank=12 price=0.44 support=0.43 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=44.02 liquidity=13658.18 spike=0.12
- EGCH.CA: score=20.41 buy_ready=False sector_rank=21 price=13.66 support=12.9 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=19018578.0 spike=0.2
- EGSA.CA: score=5.99 buy_ready=False sector_rank=17 price=8.78 support=8.55 resistance=9.19 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=26.47 liquidity=0.0 spike=0.0
- EGTS.CA: score=22.4 buy_ready=False sector_rank=5 price=18.51 support=17.25 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.85 liquidity=89922704.0 spike=0.72
- EHDR.CA: score=23.99 buy_ready=True sector_rank=10 price=2.7 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.97 liquidity=16793120.0 spike=0.29
- EKHO.CA: score=14.15 buy_ready=False sector_rank=7 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=19.17 buy_ready=False sector_rank=6 price=2.14 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=54.84 liquidity=6768522.0 spike=0.26
- ELKA.CA: score=24.99 buy_ready=True sector_rank=10 price=1.31 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=69.77 liquidity=36823696.0 spike=0.9
- ELNA.CA: score=14.38 buy_ready=False sector_rank=10 price=39.56 support=37.11 resistance=41.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=50.98 liquidity=383269.63 spike=0.94
- ELSH.CA: score=8.99 buy_ready=False sector_rank=10 price=12.82 support=12.71 resistance=13.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=80260776.0 spike=0.43
- ELWA.CA: score=15.96 buy_ready=True sector_rank=10 price=2.09 support=1.84 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=1971511.13 spike=0.63
- EMFD.CA: score=26.4 buy_ready=False sector_rank=5 price=12.12 support=10.02 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.01 liquidity=127941640.0 spike=0.46
- ENGC.CA: score=24.25 buy_ready=False sector_rank=10 price=37.47 support=32.31 resistance=36.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=70.73 liquidity=15662899.0 spike=1.13
- EOSB.CA: score=17.99 buy_ready=False sector_rank=10 price=1.48 support=1.34 resistance=1.55 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- EPCO.CA: score=23.76 buy_ready=True sector_rank=10 price=9.16 support=8.63 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=62.42 liquidity=5769405.5 spike=0.53
- EPPK.CA: score=16.34 buy_ready=False sector_rank=10 price=12.68 support=11.67 resistance=12.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=47.1 liquidity=346160.66 spike=0.31
- ETEL.CA: score=12.99 buy_ready=False sector_rank=17 price=93.0 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=32.31 liquidity=45681076.0 spike=0.56
- ETRS.CA: score=10.63 buy_ready=False sector_rank=10 price=10.75 support=10.31 resistance=11.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=111409480.0 spike=1.82
- EXPA.CA: score=21.87 buy_ready=False sector_rank=12 price=18.41 support=18.31 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=25131554.0 spike=0.72
- FAIT.CA: score=13.87 buy_ready=False sector_rank=12 price=37.11 support=35.01 resistance=38.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=49.14 liquidity=2002256.5 spike=0.41
- FAITA.CA: score=11.88 buy_ready=False sector_rank=12 price=0.99 support=0.99 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=47.73 liquidity=16124.4 spike=0.35
- FERC.CA: score=4.43 buy_ready=False sector_rank=21 price=75.64 support=75.0 resistance=79.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=24.38 liquidity=3017309.75 spike=0.74
- FWRY.CA: score=12.81 buy_ready=False sector_rank=19 price=18.87 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.35 liquidity=68064960.0 spike=0.23
- GBCO.CA: score=27.4 buy_ready=True sector_rank=1 price=29.07 support=25.25 resistance=28.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.73 liquidity=71818392.0 spike=0.67
- GDWA.CA: score=24.99 buy_ready=True sector_rank=10 price=0.81 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.94 liquidity=12207213.0 spike=0.87
- GGCC.CA: score=19.29 buy_ready=True sector_rank=10 price=0.42 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=59.38 liquidity=6293467.5 spike=0.81
- GIHD.CA: score=16.84 buy_ready=True sector_rank=10 price=41.85 support=35.15 resistance=43.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=59.11 liquidity=2843164.75 spike=0.81
- GMCI.CA: score=15.99 buy_ready=False sector_rank=10 price=1.79 support=1.68 resistance=1.84 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=54.05 liquidity=0.0 spike=0.0
- GRCA.CA: score=5.46 buy_ready=False sector_rank=10 price=53.23 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=30.47 liquidity=1465289.75 spike=0.24
- GSSC.CA: score=9.09 buy_ready=False sector_rank=10 price=249.83 support=228.1 resistance=263.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=21.11 liquidity=5040142.0 spike=1.03
- GTWL.CA: score=15.53 buy_ready=False sector_rank=10 price=48.69 support=45.47 resistance=52.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.92 liquidity=2536819.5 spike=0.33
- HDBK.CA: score=13.87 buy_ready=False sector_rank=12 price=158.82 support=146.25 resistance=160.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=91285784.0 spike=5.64
- HELI.CA: score=24.4 buy_ready=True sector_rank=5 price=6.56 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.83 liquidity=78955512.0 spike=0.53
- HRHO.CA: score=30.4 buy_ready=True sector_rank=2 price=27.52 support=25.8 resistance=27.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.13 liquidity=134065200.0 spike=0.89
- ICID.CA: score=8.99 buy_ready=False sector_rank=10 price=7.55 support=7.4 resistance=7.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11299372.0 spike=0.69
- IDRE.CA: score=23.99 buy_ready=True sector_rank=10 price=44.92 support=41.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.41 liquidity=16078195.0 spike=0.71
- IFAP.CA: score=13.5 buy_ready=False sector_rank=3 price=19.18 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.91 liquidity=4096850.25 spike=0.54
- INFI.CA: score=9.61 buy_ready=False sector_rank=10 price=93.23 support=93.0 resistance=97.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12923619.0 spike=1.31
- IRON.CA: score=19.63 buy_ready=False sector_rank=21 price=32.44 support=31.3 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.32 liquidity=12840981.0 spike=1.61
- ISMA.CA: score=18.99 buy_ready=False sector_rank=10 price=30.19 support=24.05 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=80.54 liquidity=26949708.0 spike=0.63
- ISMQ.CA: score=25.49 buy_ready=True sector_rank=21 price=8.31 support=7.27 resistance=8.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.52 liquidity=109170256.0 spike=1.54
- ISPH.CA: score=24.62 buy_ready=True sector_rank=4 price=12.6 support=11.12 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.28 liquidity=142325008.0 spike=1.11
- JUFO.CA: score=25.85 buy_ready=True sector_rank=8 price=32.0 support=26.8 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.55 liquidity=73277144.0 spike=1.88
- KABO.CA: score=19.9 buy_ready=False sector_rank=14 price=6.24 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=49.49 liquidity=8359404.5 spike=0.43
- KWIN.CA: score=30.99 buy_ready=True sector_rank=10 price=74.61 support=69.0 resistance=77.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=62.26 liquidity=26228008.0 spike=5.39
- KZPC.CA: score=20.53 buy_ready=True sector_rank=10 price=10.71 support=10.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.42 liquidity=6538211.5 spike=0.75
- LCSW.CA: score=28.28 buy_ready=True sector_rank=15 price=28.2 support=26.0 resistance=28.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=42.74 liquidity=33082138.0 spike=3.78
- LUTS.CA: score=13.35 buy_ready=False sector_rank=10 price=0.79 support=0.72 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=110310168.0 spike=3.18
- MAAL.CA: score=8.99 buy_ready=False sector_rank=10 price=6.68 support=6.46 resistance=6.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10717641.0 spike=0.77
- MASR.CA: score=29.75 buy_ready=True sector_rank=10 price=7.4 support=6.54 resistance=7.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=61.24 liquidity=106722912.0 spike=1.88
- MBSC.CA: score=21.28 buy_ready=False sector_rank=15 price=251.0 support=247.43 resistance=273.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.2 liquidity=16347407.0 spike=0.37
- MCQE.CA: score=12.74 buy_ready=False sector_rank=15 price=178.42 support=174.0 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.31 liquidity=9467755.0 spike=0.58
- MCRO.CA: score=20.99 buy_ready=False sector_rank=10 price=1.24 support=1.2 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=21847604.0 spike=0.45
- MENA.CA: score=19.49 buy_ready=True sector_rank=5 price=6.8 support=6.15 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=58.21 liquidity=5088800.0 spike=0.3
- MEPA.CA: score=22.19 buy_ready=False sector_rank=10 price=1.7 support=1.63 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=18890750.0 spike=1.1
- MFPC.CA: score=14.05 buy_ready=False sector_rank=21 price=37.03 support=36.9 resistance=45.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=4.77 liquidity=159615328.0 spike=1.82
- MFSC.CA: score=9.51 buy_ready=False sector_rank=10 price=45.21 support=43.0 resistance=55.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=21.46 liquidity=2514892.75 spike=0.2
- MHOT.CA: score=10.2 buy_ready=False sector_rank=16 price=32.4 support=31.72 resistance=34.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=43605316.0 spike=2.0
- MICH.CA: score=28.01 buy_ready=False sector_rank=10 price=39.0 support=35.05 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=70.19 liquidity=29458660.0 spike=2.01
- MILS.CA: score=18.15 buy_ready=False sector_rank=10 price=138.32 support=130.4 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.27 liquidity=6158030.5 spike=0.31
- MIPH.CA: score=17.48 buy_ready=True sector_rank=4 price=694.0 support=647.0 resistance=690.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.6 liquidity=2676551.0 spike=1.2
- MOED.CA: score=19.53 buy_ready=False sector_rank=10 price=0.7 support=0.65 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=46.03 liquidity=9537684.0 spike=0.76
- MOIL.CA: score=14.25 buy_ready=False sector_rank=7 price=0.48 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=95802.59 spike=0.59
- MOIN.CA: score=3.78 buy_ready=False sector_rank=10 price=24.09 support=24.12 resistance=25.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=21.12 liquidity=785771.06 spike=0.46
- MOSC.CA: score=16.97 buy_ready=True sector_rank=10 price=281.68 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.26 liquidity=2978991.75 spike=0.32
- MPCI.CA: score=11.21 buy_ready=False sector_rank=10 price=237.85 support=221.5 resistance=243.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=166580848.0 spike=2.11
- MPCO.CA: score=25.4 buy_ready=False sector_rank=3 price=1.95 support=1.54 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.08 liquidity=41398036.0 spike=0.42
- MPRC.CA: score=27.87 buy_ready=True sector_rank=10 price=33.68 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=60.66 liquidity=59002016.0 spike=2.94
- MTIE.CA: score=29.4 buy_ready=True sector_rank=1 price=9.18 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.48 liquidity=10863253.0 spike=0.6
- NAHO.CA: score=8.0 buy_ready=False sector_rank=10 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=6642.38 spike=0.19
- NCCW.CA: score=23.99 buy_ready=True sector_rank=10 price=6.28 support=5.13 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=69.02 liquidity=12712085.0 spike=0.45
- NEDA.CA: score=13.99 buy_ready=False sector_rank=10 price=2.81 support=2.65 resistance=2.84 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=61.76 liquidity=0.0 spike=0.0
- NHPS.CA: score=24.22 buy_ready=True sector_rank=10 price=70.5 support=65.03 resistance=71.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.56 liquidity=8429214.0 spike=1.9
- NINH.CA: score=12.89 buy_ready=False sector_rank=10 price=17.56 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=43.3 liquidity=899672.31 spike=0.18
- NIPH.CA: score=24.4 buy_ready=True sector_rank=4 price=166.0 support=155.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=80636544.0 spike=0.98
- OBRI.CA: score=20.82 buy_ready=False sector_rank=10 price=35.31 support=33.63 resistance=37.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.68 liquidity=9825666.0 spike=0.72
- OCDI.CA: score=14.4 buy_ready=False sector_rank=5 price=22.4 support=21.4 resistance=22.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=130160744.0 spike=3.83
- OCPH.CA: score=10.31 buy_ready=False sector_rank=10 price=338.62 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=26.79 liquidity=6195695.0 spike=1.06
- ODIN.CA: score=26.39 buy_ready=False sector_rank=10 price=2.21 support=1.89 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=71.43 liquidity=13009640.0 spike=1.2
- OFH.CA: score=18.99 buy_ready=False sector_rank=10 price=0.61 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.78 liquidity=11788273.0 spike=0.51
- OIH.CA: score=13.55 buy_ready=False sector_rank=13 price=1.35 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.29 liquidity=48870492.0 spike=0.55
- OLFI.CA: score=27.35 buy_ready=True sector_rank=8 price=22.49 support=21.0 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.21 liquidity=32375112.0 spike=1.63
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=792.73 support=786.0 resistance=797.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=110564376.0 spike=1.0
- ORHD.CA: score=10.34 buy_ready=False sector_rank=5 price=39.5 support=38.36 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=268779328.0 spike=1.47
- ORWE.CA: score=23.54 buy_ready=True sector_rank=14 price=23.45 support=21.65 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=56.81 liquidity=22071974.0 spike=0.53
- PHAR.CA: score=14.4 buy_ready=False sector_rank=4 price=89.07 support=84.51 resistance=89.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=175066480.0 spike=6.2
- PHDC.CA: score=24.48 buy_ready=True sector_rank=5 price=15.9 support=13.4 resistance=16.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.98 liquidity=430468832.0 spike=1.04
- PHTV.CA: score=11.73 buy_ready=False sector_rank=10 price=234.13 support=216.31 resistance=238.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39822856.0 spike=2.37
- POUL.CA: score=22.09 buy_ready=False sector_rank=8 price=35.94 support=34.99 resistance=38.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.3 liquidity=28149664.0 spike=0.78
- PRCL.CA: score=10.78 buy_ready=False sector_rank=15 price=27.57 support=26.05 resistance=27.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=62908420.0 spike=2.25
- PRDC.CA: score=23.54 buy_ready=False sector_rank=5 price=7.96 support=5.32 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=90.46 liquidity=105020104.0 spike=1.07
- PRMH.CA: score=25.25 buy_ready=False sector_rank=10 price=2.82 support=2.21 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.63 liquidity=43094952.0 spike=1.63
- RACC.CA: score=13.2 buy_ready=False sector_rank=10 price=9.86 support=9.38 resistance=10.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.88 liquidity=6207707.0 spike=0.61
- RAKT.CA: score=9.14 buy_ready=False sector_rank=10 price=22.49 support=22.0 resistance=24.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=48.94 liquidity=451035.47 spike=1.35
- RAYA.CA: score=8.51 buy_ready=False sector_rank=18 price=7.46 support=7.3 resistance=7.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=127883624.0 spike=1.35
- RMDA.CA: score=22.4 buy_ready=False sector_rank=4 price=5.09 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.66 liquidity=11959009.0 spike=0.14
- ROTO.CA: score=13.99 buy_ready=False sector_rank=10 price=43.38 support=43.16 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=121913584.0 spike=9.02
- RREI.CA: score=25.99 buy_ready=True sector_rank=10 price=3.66 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.63 liquidity=12127632.0 spike=0.57
- RTVC.CA: score=17.28 buy_ready=True sector_rank=10 price=3.92 support=3.75 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=55.38 liquidity=3283448.25 spike=0.59
- RUBX.CA: score=10.86 buy_ready=False sector_rank=10 price=9.97 support=9.8 resistance=10.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.32 liquidity=2870771.75 spike=0.25
- SAUD.CA: score=13.39 buy_ready=False sector_rank=12 price=21.75 support=20.82 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=36.8 liquidity=4517480.0 spike=0.41
- SCEM.CA: score=18.28 buy_ready=False sector_rank=15 price=61.97 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=38.76 liquidity=11655689.0 spike=0.54
- SCFM.CA: score=6.12 buy_ready=False sector_rank=10 price=249.73 support=248.1 resistance=276.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.55 liquidity=2132397.75 spike=0.18
- SCTS.CA: score=8.6 buy_ready=False sector_rank=11 price=598.15 support=565.25 resistance=660.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.2 liquidity=1641722.75 spike=0.31
- SDTI.CA: score=26.41 buy_ready=True sector_rank=10 price=47.8 support=43.4 resistance=47.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=62.01 liquidity=17699058.0 spike=1.21
- SEIG.CA: score=14.96 buy_ready=False sector_rank=10 price=185.76 support=174.0 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=54.17 liquidity=964279.31 spike=0.2
- SIPC.CA: score=20.98 buy_ready=True sector_rank=10 price=3.55 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=6988385.5 spike=0.55
- SKPC.CA: score=11.41 buy_ready=False sector_rank=21 price=16.4 support=16.16 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.46 liquidity=45523884.0 spike=0.87
- SMFR.CA: score=11.11 buy_ready=False sector_rank=10 price=203.48 support=192.0 resistance=214.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=42.73 liquidity=2119239.25 spike=0.5
- SNFC.CA: score=21.99 buy_ready=False sector_rank=10 price=12.1 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.98 liquidity=11625641.0 spike=0.44
- SPIN.CA: score=5.96 buy_ready=False sector_rank=14 price=13.82 support=13.3 resistance=14.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=31.53 liquidity=2423330.5 spike=0.53
- SPMD.CA: score=13.99 buy_ready=False sector_rank=10 price=0.46 support=0.45 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=86113280.0 spike=3.65
- SUGR.CA: score=13.56 buy_ready=False sector_rank=8 price=48.39 support=48.0 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.74 liquidity=5465087.5 spike=0.36
- SVCE.CA: score=23.99 buy_ready=True sector_rank=10 price=9.21 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=82398856.0 spike=0.9
- SWDY.CA: score=24.27 buy_ready=True sector_rank=6 price=87.27 support=84.01 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=42.95 liquidity=9865673.0 spike=0.49
- TALM.CA: score=23.5 buy_ready=False sector_rank=11 price=16.11 support=15.12 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=77.6 liquidity=10092448.0 spike=1.27
- TMGH.CA: score=26.86 buy_ready=True sector_rank=5 price=97.0 support=92.91 resistance=100.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=48.52 liquidity=1017440896.0 spike=2.23
- TRTO.CA: score=15.26 buy_ready=False sector_rank=10 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 June 11:57 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=266831.58 spike=271.16
- UEFM.CA: score=10.58 buy_ready=False sector_rank=10 price=473.11 support=455.6 resistance=489.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=48.69 liquidity=587998.06 spike=0.73
- UEGC.CA: score=24.37 buy_ready=True sector_rank=10 price=1.46 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=8381462.5 spike=0.33
- UNIP.CA: score=22.99 buy_ready=False sector_rank=10 price=0.33 support=0.28 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=85.92 liquidity=11318830.0 spike=0.48
- UNIT.CA: score=15.17 buy_ready=False sector_rank=5 price=13.7 support=12.5 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.26 liquidity=771617.63 spike=0.1
- WCDF.CA: score=10.99 buy_ready=False sector_rank=10 price=537.53 support=450.0 resistance=549.95 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=45.74 liquidity=0.0 spike=0.0
- WKOL.CA: score=9.52 buy_ready=False sector_rank=10 price=288.93 support=289.0 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=44.38 liquidity=528117.56 spike=0.16
- ZEOT.CA: score=27.99 buy_ready=False sector_rank=10 price=11.7 support=8.41 resistance=11.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=83.5 liquidity=97557456.0 spike=5.89
- ZMID.CA: score=24.4 buy_ready=True sector_rank=5 price=6.3 support=5.77 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.77 liquidity=115376904.0 spike=0.55

## Backtesting Lite
- ATLC.CA: 180d return=46.12%, max drawdown=-16.0%, MA20>MA50 days last20=20, as_of=2026-06-17T21:00:00+00:00
- KWIN.CA: 180d return=2.96%, max drawdown=-34.04%, MA20>MA50 days last20=20, as_of=2026-06-17T21:00:00+00:00
- HRHO.CA: 180d return=4.85%, max drawdown=-18.92%, MA20>MA50 days last20=12, as_of=2026-06-17T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ATLC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Al Tawfeek Leasing summary=Evidence rejected for ATLC.CA: source text did not clearly match ATLC.CA / Al Tawfeek Leasing.
- KWIN.CA: status=RECENT_ACCEPTED latest=2026-05-18 age_days=34 sources=3 expected=El Kahera El Watania Investment summary=Recent financial results and board meeting decisions for El Kahera El Watania Investment (KWIN.CA) have been reported by the Egyptian Exchange and financial news outlets.
  - El Kahera El Watania Investment Reports Earnings Results for the First Quarter Ended March 31, 2026 (May 18, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7ZAoIAa776csjOmD1k0S__cwtouQ0E15xHZdczwY6E3y2wd4Thw7XhwwXn0zINA5qgl2sT2GTR6n2XX_g6_KHG5WJNwho-SDLUTb_IifPi93XGv0vrE3LPwPJd6tb5ETLmfJCLCVJ1hBDyTdFGxcE_75-lB34fPUE1MiL4O3Oqa2sgO3-HKvI
  - El Kahera El Watania Investment (KWIN.CA) - Decisions of the Board of Directors' Meeting (May 18, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUq4AxK5hCgjh42rik3PbkmAlucpTlFlrtFypJsX5gyGKMahGPQHLtrRtyxT1Sv6opqOOoDjr4Skga3mhv1dAvjpO9dzu-Wqb6HJcqRrQxurEXyRk38OKdIxc8dIKshttlT_bY7wyfz5B0ShOqqMfaZOmDXa_xFGsUFLB-ocJHjlWL6AjaYsnA9UMuPuyfPSA0imZ4
  - El Kahera El Watania Investment (KWIN.CA) تعلن نتائج أعمالها المجمعة عن الفترة من 01/01/2026 إلى 31/03/2026 (May 18, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUq4AxK5hCgjh42rik3PbkmAlucpTlFlrtFypJsX5gyGKMahGPQHLtrRtyxT1Sv6opqOOoDjr4Skga3mhv1dAvjpO9dzu-Wqb6HJcqRrQxurEXyRk38OKdIxc8dIKshttlT_bY7wyfz5B0ShOqqMfaZOmDXa_xFGsUFLB-ocJHjlWL6AjaYsnA9UMuPuyfPSA0imZ4
- HRHO.CA: status=RECENT_ACCEPTED latest=2026-01-01 age_days=171 sources=3 expected=EFG Holding summary=EFG Holding (HRHO.CA) has released its 2025 financial performance and recent balance sheet data, with analyst ratings indicating a 'Strong Buy'.
  - EFG Holding Company S.A.E (EGX:HRHO) Stock Price & Overview - Financial Performance in 2025 (June 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFr8Ek4FiFmsz9szemgsPZhuRic4180GWFyRDzt4F3u9v5Z5ctMruopmmqyaM-AgFhLTt7Xj8F9GcoWJaCNBhpV9Iz5uW1hE8UD6pJNbyWZzlhhxHaeh07PqyqPxV0OtOHk6ts=
  - EFG Holding S.A.E. Balance Sheet – EGX:HRHO - Q4 2025 (June 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2WO9y515O1yzIJVz4MxOuiX3nNrgTbpWGW1rNIhBAmKi1TitxNXgw6CCKaTwV7Ej9yr20ueIVkaPPfYIdd6h1kzIdt8b2X4Ljphim-fmE3RNBaL3io23tU-URk4kGaq4ACE00M3scmkX4t80qlYhAokNk_rv0hscouBrsiVbifw==
  - Financial Statements - EFG Holding (HRHO) - Mubasher Info (Latest available): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKcdkeNRKQrqzbhYbHY-d_eA9MRF33lK6oZt_mLmo3kVoB220bQIAxYrzfWNGQbaBNB0yJPqjJUwKTQ45JXdhjPaA7lMFufnqQbrnKEXUu-o6eYYa9EK0RCDDXImpXSH6Kyj_n9cAZUBYWunUIIKF4Wlfls18xNDFJJih70tjrtkHtgTIa
- MASR.CA: status=RECENT_ACCEPTED latest=2026-05-24 age_days=28 sources=3 expected=Madinet Masr For Housing and Development summary=Madinet Masr For Housing and Development (MASR.CA) has reported strong financial performance for 2025 and Q1 2026, including revenue growth and a recent dividend announcement.
  - Madinet Masr For Housing and Development (EGX:MASR) Stock Price & Overview - Financial Performance in 2025 (June 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlfGygb0ciEJskU_cxGB1YuO1g4ltnBRCn3Fi6WPR95JkDtgo1iNBgdebhM5fli6aGwaCX349rQvASUFxLisoZHZSkvB-Hrg1kXzDbu-ldKZWgF4Kpz8GEe_xohy6AH3Iwj5U=
  - Madinet Masr For Housing and Development (EGX:MASR) Financials & Income Statement (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFy89xz5jlbyhObclgdU-x9gZUJTIAvxwB2Tqm37A_-yhIhe27MZh7qQp3ioJC7AgWAwgm0r2HlZ-UDLWS9PhLphvI1bFHx_bJrw-TStMRkBTfdc1PsAv2TwwaPXs4IbuOdfH9toYFy1JcFIPWjUQ==
  - Madinet Nasr for Housing and Development SAE (MASR) Latest Earnings Release (May 24, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0T4NwRU43s2KcUT-m0XHAYGxPROIXXuZB95JxaAlutUbh4a80H2AMfQYPUM7qiAWQyhQXy9WtKGpLSeobe-5MfVFcbLB0RJR4zLBX-N5dGaqVeYNActuKQVJ6H3p66Zxl9CyQ0cy2Md0Iq0FMWR7W-0jjJaz0lYdlo75UaA==
- MTIE.CA: status=RECENT_ACCEPTED latest=2026-06-17 age_days=4 sources=3 expected=MM Group For Industry and International Trade summary=MM Group For Industry and International Trade (MTIE.CA) has reported recent financial results for Q1 2026 and its 2025 fiscal year, showing revenue and net income figures.
  - EGX:MTIE Financials | MM Group for Industry - Latest Quarter Performance (June 17, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpOd0g0w7yhMgQyoMsO9boOJSKdH7oEFGJ6LoiAPHW4XomtrIov2GodaehIa8lYanmwaeGKEKDIDjDdLItgcWAU7uZCxpMGJBSBvhCQMF24TXCLbzucXHZ-y9UR3XDNCo7PeygdJnr1pRzpTcmzVqx3XsI3-epctds1YUwuXQDEqmpWU4
  - MM Group for Industry and International Trade S.A.E. (EGX:MTIE) Balance Sheet (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHA2Dp6Y3S-pVWODqfVGxNfZRTZsWheoQ_Xu5fSUwM5nyFFDzPgzByPIzlsKLQB7crIoxL-_Agl6EvplBJFSyLj-s7i2Wuql6Tv_jufqQM6Fm3_zJACd6hOFHwQaXLjZzbhjLaiBDRHRDZXA-X-CcCVb0mXx8wnkkNx7tn7q
  - MM Group For Industry And International Trade (MTIE.CA) Reports its Financial Results (Consolidated) for the Period from 01/01/2026 to 31/03/2026 (June 12, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZWrUn1Dy9lEXqm1yw27pDtWFq822INvBN7eODlNA_S6YmeDw6Tbdk5JEWCO_FjBs7fypSV_jdcuJO2Xe54zFCrf6OwticRY6sPShAjiBlA_PUDMAFvhrv7lc3MbZWGttYfFiL47sDJB8do8zRz-IB7FJ8OmgBikXA
- LCSW.CA: status=RECENT_ACCEPTED latest=2026-06-14 age_days=7 sources=3 expected=Lecico Egypt summary=Lecico Egypt (LCSW.CA) has released its Q1 2026 financial results and 2025 annual report, detailing revenue, profits, and operational performance.
  - Lecico Egypt (S.A.E.) (EGX:LCSW) Statistics & Valuation Metrics - Last 12 months revenue (June 14, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZ2-77mmgix3UWGxHqQWJ1TC4m04IpsZ4hr9UjBY54T7A2xKzx3UPtE_RJOdndwyg3EAp64OGefwpIMrxmMGp2QFtSLnSbK_uC1Zyu4c17RYjah5hlT6I_tueacCqpqn7SxvykmL64Q79pV09X_g==
  - Lecico Egypt (LCSW.CA) Reports Its Financial Results (Consolidated) for The Period From 01/01/2026 to 31/03/2026 (May 25, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-EqqXQsV4XQPy499--pOdCbhtBz3iwZh4Es23qVDfgkp2fRl2UbVeTcvYk-sW9t83BOpelhM4TEd3J_UHcxfMgSiggw75NL2VEKNSOXb-4OUfUeEdiCbZpMV6w4Bhwcr_oy6G1KMfCMaVGiFqr5y7sy3W
  - Lecico Egypt (LCSW.CA) Reports Its Financial Results (Consolidated) for The Period ending 31/12/2025 (March 1, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQFIWMUO8iIy-UpEVD9usWP4nVb4OC1Yc_hjy5czPVHbvD7UT4BkwV9WMNKpAKOS7Oo3UaiJqrSN60e7_91Lsw2dX2_dOo1b4IL6gplvM29ACsvQ4jNB7HaWCJS6ZuztKAZJN0TeTfEHbcRZYSa5Q1
- MICH.CA: status=RECENT_ACCEPTED latest=2026-02-26 age_days=115 sources=3 expected=Misr Chemical Industries Co. summary=Misr Chemical Industries Co. (MICH.CA) has reported its fiscal year 2025 financial performance and recent quarterly results.
  - Misr Chemical Industries Co. (EGX:MICH) Stock Price & Overview - Financial Performance in fiscal year 2025 (June 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnsHDGRHe8hTRysdqbuWfjjDoxNM6F1EPyZijLxkG_rQ-VEmTDiUqMlC-9qqGNxlBJqdgl7zzvWO8tla_hFS2JfsrLTF7zyquNiDwQBTeBC-O8gc5Ba1d7Ne0V8FJfvMHmegM=
  - EGX:MICH Financials - Latest Release (February 26, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEM2QYF-XcUqRy_zXf7YKX90rt20XbVjFws9S3-7YEVeiiymM8BlFONIiRK4v9684hby5e2b0OseosrxMG2a1TPfBnOrkQEv2F7vJBmKgeMb9puHeb_vrLIbeLBF-ZQPs_XbQuvTsEmFgCHda5W0lL3aKYQW3lFc9eFpJMj
  - Financial Statments & Reports - Misr Chemical Industries Co. (Latest available): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoXQ0fUmsLKN1s2hXezWcatpDa4BGykgHwxILrKnWPPqfA7I6zdYSwGwzVraRHlAumwHm6Y6WWbnOpDgPcDS675DmOihSELkiAUHONIiMQ3l-pQ2JL_Fi1dy3hAQ==
- ANFI.CA: status=RECENT_ACCEPTED latest=2026-06-01 age_days=20 sources=3 expected=Tycoon Holding Company For Financial Investments summary=Tycoon Holding Company For Financial Investments (ANFI.CA) has reported its 2025 financial performance and recent Q1 2026 results, showing significant revenue and net income growth.
  - Tycoon Holding Company For Financial Investments (EGX:ANFI) - Financial Performance in 2025 (June 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-Fk6psj52PwWHxiImiREjs37oHcAwquD3nUnE0zxaIwXiK2pUtWgfBfhU7EHxJJ97J0GwPB-AYX_BBp-dAGRXbYCrvBxDlOTErGVkr6pPpnBKowqVkJ3Crz2yTzPKSmXxDLw=
  - Tycoon Holding Company For Financial Investments (EGX:ANFI) Revenue - Annual and Quarterly Revenue (December 31, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXBOLcz2GTZjx0BlH5jsYSjsVh9Y8TlAiSktP_hb98UadKKdg3_2ZIVi0LCvrZ4nyY1FLxIyF0CwqgKOLEHNL_ONaru2n0t1L-sTzOoRf7rBfLvjWTn051Q0w1seQ2q832v0c0gTIxLC1i-g==
  - Tycoon Holding Company For Financial Investments (TYCN.CA) Reports Its Financial Results for The Period From 01/01/2026 to 31/03/2026 (June 1, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNcN63e_KnTVw83d8FTJ2-umULx-M8jRgaRPBDcDUY6geDM1nB19JKP8fFQ6ezbSJvRudeaBTY6kN2F2MP2xhVfW8NNy6cV2vyHrS3NQEisAuamYTJikgGJ2CR8KnWh0Kg4rHl-SOMQu86LYe9CmJEI8I=

## Warnings
- Evidence rejected for ATLC.CA: source text did not clearly match ATLC.CA / Al Tawfeek Leasing.
