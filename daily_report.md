# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-09-01T13:01:13.800765+00:00
Generated Cairo: 2026-09-01 16:01
Run timing: target 11:00 Cairo | generated Cairo 2026-09-01 16:01 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-09-01 15:58

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 170/189
- Top sector: Investment Holding

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, September 01
- Freshness: DELAYED
- EGX30 regime: CONSTRUCTIVE / above MA20 52.63% / above MA50 78.95%
- EGX70 regime: BEARISH / above MA20 41.67% / above MA50 72.22%
- Sector breadth: 14.29%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=910881920.0 spike=1.81 score=21.02
- CCAP.CA: liquidity=907655872.0 spike=1.49 score=24.38
- SVCE.CA: liquidity=746993600.0 spike=7.14 score=10.6
- AMES.CA: liquidity=362010688.0 spike=5.55 score=10.6
- EMFD.CA: liquidity=359552160.0 spike=3.02 score=23.96

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 is constructive while EGX70 is bearish, sector breadth is weak at 14.3%, and risk mode is DEFENSIVE_NO_NEW_BUY; the scanner flags accumulation spikes and bullish watch outlooks on several tickets but keeps them as HOLD due to the defensive regime and low confidence.
- Top tickets (PRDC.CA, EBSC.CA, CIEB.CA) show liquidity accumulation spikes (2‑4×) and BULLISH_WATCH outlooks, yet they sit near or above resistance with tight or negative resistance distances, limiting near‑term upside.
- Support distances range from ~5% to ~20% while resistance distances are often ≤0% or slightly positive, indicating price may stall or retreat in the next 1‑3 days despite short‑term buying interest.
- Only Investment Holding, Textiles, and Industrial Goods & Cables are leading sectors; most flagged tickets belong to non‑leading sectors, reducing sector‑based conviction.
- The EGX30 constructive trend versus EGX70 bearish trend shifts the market regime to defensive, prompting the scanner to maintain HOLD with low confidence amid mixed liquidity and technical signals.

## Top Liquidity Spikes
- SVCE.CA: spike=7.14 liquidity=746993600.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- TRTO.CA: spike=6.79 liquidity=83294.68 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AMES.CA: spike=5.55 liquidity=362010688.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ATLC.CA: spike=4.41 liquidity=90492984.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- PRDC.CA: spike=4.29 liquidity=278562816.0 outlook=BULLISH_WATCH score=88.8 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=12.82 5d=7.45% 20d=12.66% aboveMA50=100.0%
- #2 Textiles: score=12.5 5d=3.0% 20d=22.2% aboveMA50=100.0%
- #3 Industrial Goods & Cables: score=11.73 5d=1.62% 20d=14.11% aboveMA50=100.0%
- #4 Banking & Financials: score=7.17 5d=0.0% 20d=4.52% aboveMA50=90.0%
- #5 Tourism & Leisure: score=6.48 5d=1.31% 20d=11.57% aboveMA50=0.0%
- #6 Basic Resources & Chemicals: score=6.1 5d=-0.34% 20d=1.15% aboveMA50=70.0%
- #7 Food, Beverages & Tobacco: score=5.15 5d=-1.41% 20d=5.42% aboveMA50=57.14%
- #8 Real Estate: score=4.8 5d=-0.82% 20d=3.66% aboveMA50=69.23%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CIEB.CA: BULLISH_WATCH score=96.17 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance
- EBSC.CA: BULLISH_WATCH score=93.99 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- BINV.CA: BULLISH_WATCH score=93 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- CLHO.CA: BULLISH_WATCH score=92.76 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- PRDC.CA: BULLISH_WATCH score=88.8 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ISMQ.CA: BULLISH_WATCH score=87.1 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ORWE.CA: BULLISH_WATCH score=83 liquidity=TRADEABLE sector=LEADING risk=close to resistance
- SAUD.CA: BULLISH_WATCH score=82.17 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- FERC.CA: BULLISH_WATCH score=82.1 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ELEC.CA: BULLISH_WATCH score=82 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=weak RSI

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=18.6 buy_ready=False sector_rank=12 price=303.6 support=266.01 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=54.3 liquidity=10987385.0 spike=0.21
- ABUK.CA: score=27.98 buy_ready=False sector_rank=6 price=84.31 support=72.0 resistance=80.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.74 liquidity=349758368.0 spike=3.29
- ACAMD.CA: score=10.6 buy_ready=False sector_rank=12 price=2.01 support=1.95 resistance=2.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=15.38 liquidity=33933924.0 spike=0.6
- ACGC.CA: score=23.4 buy_ready=False sector_rank=2 price=14.13 support=10.36 resistance=14.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=72.69 liquidity=19056874.0 spike=0.46
- ADCI.CA: score=17.81 buy_ready=False sector_rank=12 price=305.01 support=274.0 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.21 liquidity=7218151.0 spike=0.34
- ADIB.CA: score=21.18 buy_ready=False sector_rank=4 price=53.3 support=51.02 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.1 liquidity=126825584.0 spike=1.89
- ADPC.CA: score=15.6 buy_ready=False sector_rank=12 price=3.9 support=3.85 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.02 liquidity=16400429.0 spike=0.38
- AFDI.CA: score=18.86 buy_ready=False sector_rank=12 price=56.39 support=52.56 resistance=69.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.26 liquidity=38028032.0 spike=1.13
- AFMC.CA: score=13.6 buy_ready=False sector_rank=12 price=183.69 support=174.84 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.64 liquidity=36234640.0 spike=0.24
- AJWA.CA: score=15.6 buy_ready=False sector_rank=12 price=180.08 support=179.1 resistance=204.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=37.98 liquidity=33373158.0 spike=0.52
- ALCN.CA: score=20.62 buy_ready=False sector_rank=10 price=30.89 support=29.74 resistance=32.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.54 liquidity=50219188.0 spike=1.95
- ALUM.CA: score=15.37 buy_ready=False sector_rank=12 price=28.65 support=23.0 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=68.4 liquidity=4773889.0 spike=0.17
- AMER.CA: score=19.46 buy_ready=False sector_rank=8 price=5.58 support=4.86 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.25 liquidity=123134944.0 spike=1.27
- AMES.CA: score=10.6 buy_ready=False sector_rank=12 price=104.59 support=104.59 resistance=126.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=362010688.0 spike=5.55
- AMIA.CA: score=8.58 buy_ready=False sector_rank=12 price=20.4 support=19.01 resistance=21.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=137094864.0 spike=2.49
- AMOC.CA: score=6.9 buy_ready=False sector_rank=16 price=13.35 support=12.25 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=320970400.0 spike=1.94
- APSW.CA: score=8.76 buy_ready=False sector_rank=12 price=8.7 support=8.41 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=44.97 liquidity=1168345.5 spike=0.79
- ARAB.CA: score=23.18 buy_ready=False sector_rank=8 price=0.26 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.71 liquidity=101513992.0 spike=1.13
- ARCC.CA: score=19.39 buy_ready=False sector_rank=14 price=80.84 support=55.77 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.62 liquidity=89476688.0 spike=0.86
- AREH.CA: score=9.62 buy_ready=False sector_rank=12 price=1.45 support=1.4 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=9025584.0 spike=0.31
- ARVA.CA: score=5.6 buy_ready=False sector_rank=12 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=13.6 buy_ready=False sector_rank=12 price=62.98 support=62.01 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.38 liquidity=17271140.0 spike=0.38
- ASPI.CA: score=20.22 buy_ready=False sector_rank=12 price=0.43 support=0.43 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.95 liquidity=68922968.0 spike=1.81
- ATLC.CA: score=9.63 buy_ready=False sector_rank=18 price=6.8 support=5.76 resistance=6.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=90492984.0 spike=4.41
- ATQA.CA: score=9.7 buy_ready=False sector_rank=6 price=12.63 support=11.82 resistance=12.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=243125136.0 spike=2.65
- AXPH.CA: score=17.6 buy_ready=False sector_rank=12 price=1703.35 support=1246.92 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=88.66 liquidity=11749191.0 spike=0.94
- BINV.CA: score=25.53 buy_ready=False sector_rank=1 price=50.28 support=46.25 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=64.95 liquidity=9125809.0 spike=0.87
- BIOC.CA: score=5.6 buy_ready=False sector_rank=12 price=320.04 support=320.0 resistance=347.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=133416696.0 spike=0.52
- BTFH.CA: score=8.63 buy_ready=False sector_rank=18 price=3.0 support=2.94 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=127658216.0 spike=0.71
- CAED.CA: score=19.42 buy_ready=False sector_rank=12 price=142.38 support=118.01 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.01 liquidity=8823214.0 spike=0.23
- CANA.CA: score=19.4 buy_ready=False sector_rank=4 price=43.14 support=37.9 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.26 liquidity=13675320.0 spike=0.78
- CCAP.CA: score=24.38 buy_ready=False sector_rank=1 price=5.92 support=5.18 resistance=6.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.92 liquidity=907655872.0 spike=1.49
- CCRS.CA: score=22.6 buy_ready=False sector_rank=12 price=2.73 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=55.73 liquidity=44742104.0 spike=0.91
- CEFM.CA: score=13.75 buy_ready=False sector_rank=12 price=144.25 support=131.03 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.34 liquidity=3157051.0 spike=0.11
- CERA.CA: score=10.6 buy_ready=False sector_rank=12 price=1.25 support=1.23 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.77 liquidity=13653166.0 spike=0.98
- CFGH.CA: score=9.61 buy_ready=False sector_rank=12 price=0.12 support=0.1 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=79.17 liquidity=16422.59 spike=0.89
- CICH.CA: score=5.87 buy_ready=False sector_rank=18 price=12.31 support=12.0 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.27 liquidity=3240541.5 spike=0.48
- CIEB.CA: score=29.08 buy_ready=False sector_rank=4 price=25.12 support=23.95 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=61.39 liquidity=38055472.0 spike=2.84
- CIRA.CA: score=12.08 buy_ready=False sector_rank=21 price=33.99 support=32.1 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=30.91 liquidity=29018584.0 spike=0.79
- CLHO.CA: score=25.9 buy_ready=False sector_rank=9 price=18.26 support=16.95 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.38 liquidity=231508912.0 spike=3.61
- CNFN.CA: score=17.63 buy_ready=False sector_rank=18 price=4.88 support=4.73 resistance=5.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=16930664.0 spike=0.9
- COMI.CA: score=21.02 buy_ready=False sector_rank=4 price=138.96 support=135.35 resistance=142.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=37.83 liquidity=910881920.0 spike=1.81
- COPR.CA: score=20.6 buy_ready=False sector_rank=12 price=0.51 support=0.4 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.36 liquidity=31930852.0 spike=0.36
- COSG.CA: score=18.6 buy_ready=False sector_rank=12 price=1.87 support=1.67 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.12 liquidity=45831412.0 spike=0.91
- CPCI.CA: score=12.19 buy_ready=False sector_rank=12 price=548.97 support=483.0 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=71.99 liquidity=3593138.0 spike=0.41
- CSAG.CA: score=10.06 buy_ready=False sector_rank=10 price=44.0 support=41.4 resistance=44.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=75681744.0 spike=3.17
- DAPH.CA: score=25.12 buy_ready=False sector_rank=12 price=138.43 support=99.02 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.95 liquidity=146039744.0 spike=2.26
- DEIN.CA: score=8.6 buy_ready=False sector_rank=12 price=10.35 support=10.35 resistance=10.35 source=Yahoo Finance as_of=2026-08-30T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=19.2 buy_ready=False sector_rank=7 price=28.01 support=26.6 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=44.49 liquidity=17303186.0 spike=1.07
- DSCW.CA: score=10.6 buy_ready=False sector_rank=12 price=1.92 support=1.84 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=33.93 liquidity=34404744.0 spike=0.39
- DTPP.CA: score=15.6 buy_ready=False sector_rank=12 price=305.54 support=240.1 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=75.01 liquidity=20311698.0 spike=0.49
- EALR.CA: score=16.24 buy_ready=False sector_rank=12 price=390.57 support=364.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.89 liquidity=7640068.5 spike=0.16
- EASB.CA: score=19.3 buy_ready=False sector_rank=12 price=7.34 support=6.71 resistance=8.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.18 liquidity=13526892.0 spike=1.85
- EAST.CA: score=17.06 buy_ready=False sector_rank=7 price=36.17 support=35.0 resistance=37.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.18 liquidity=43064152.0 spike=0.53
- EBSC.CA: score=29.6 buy_ready=False sector_rank=12 price=2.24 support=1.88 resistance=2.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.84 liquidity=44336136.0 spike=3.92
- ECAP.CA: score=16.36 buy_ready=False sector_rank=12 price=32.0 support=32.05 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.49 liquidity=21595952.0 spike=1.38
- EDFM.CA: score=12.27 buy_ready=False sector_rank=12 price=409.6 support=390.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=59.15 liquidity=1669217.88 spike=0.59
- EEII.CA: score=20.6 buy_ready=False sector_rank=12 price=3.0 support=2.64 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.48 liquidity=12484560.0 spike=0.43
- EFIC.CA: score=15.4 buy_ready=False sector_rank=6 price=197.07 support=188.01 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.49 liquidity=16078896.0 spike=0.31
- EFID.CA: score=19.06 buy_ready=False sector_rank=7 price=30.01 support=27.1 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.37 liquidity=69596928.0 spike=0.8
- EFIH.CA: score=17.83 buy_ready=False sector_rank=17 price=22.98 support=22.9 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.53 liquidity=64005500.0 spike=0.57
- EGAL.CA: score=18.4 buy_ready=False sector_rank=6 price=362.01 support=292.0 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.24 liquidity=109345688.0 spike=0.74
- EGAS.CA: score=15.68 buy_ready=False sector_rank=16 price=58.71 support=52.5 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.23 liquidity=7666675.0 spike=0.33
- EGBE.CA: score=9.44 buy_ready=False sector_rank=4 price=0.53 support=0.47 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=44.22 liquidity=37162.34 spike=0.18
- EGCH.CA: score=21.74 buy_ready=False sector_rank=6 price=14.16 support=13.3 resistance=14.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.22 liquidity=142171728.0 spike=1.17
- EGSA.CA: score=7.63 buy_ready=False sector_rank=11 price=8.69 support=8.65 resistance=8.93 source=Yahoo Finance as_of=2026-08-30T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=3684.56 spike=0.55
- EGTS.CA: score=15.92 buy_ready=False sector_rank=8 price=16.96 support=16.17 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=40.82 liquidity=12459479.0 spike=0.36
- EHDR.CA: score=18.6 buy_ready=False sector_rank=12 price=2.86 support=2.73 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=19206826.0 spike=0.56
- EKHO.CA: score=6.02 buy_ready=False sector_rank=16 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-30T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=19.48 buy_ready=False sector_rank=3 price=2.15 support=2.04 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=142069664.0 spike=2.54
- ELKA.CA: score=8.74 buy_ready=False sector_rank=12 price=1.95 support=1.86 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=174838720.0 spike=2.57
- ELNA.CA: score=4.78 buy_ready=False sector_rank=12 price=37.0 support=36.1 resistance=38.44 source=Yahoo Finance as_of=2026-08-30T21:00:00+00:00 freshness=FRESH RSI=42.81 liquidity=187923.0 spike=0.58
- ELSH.CA: score=15.6 buy_ready=False sector_rank=12 price=13.44 support=12.97 resistance=14.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.05 liquidity=54836544.0 spike=0.99
- ELWA.CA: score=10.92 buy_ready=False sector_rank=12 price=1.84 support=1.62 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=1319248.13 spike=0.54
- EMFD.CA: score=23.96 buy_ready=False sector_rank=8 price=13.63 support=11.41 resistance=13.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=80.33 liquidity=359552160.0 spike=3.02
- ENGC.CA: score=15.6 buy_ready=False sector_rank=12 price=42.63 support=41.99 resistance=54.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.78 liquidity=24379362.0 spike=0.92
- EOSB.CA: score=15.0 buy_ready=False sector_rank=12 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-08-30T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=103337.4 spike=2.15
- EPCO.CA: score=13.55 buy_ready=False sector_rank=12 price=11.17 support=10.8 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.69 liquidity=4956229.0 spike=0.27
- EPPK.CA: score=0.86 buy_ready=False sector_rank=12 price=11.41 support=12.01 resistance=15.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=32.02 liquidity=1145004.88 spike=1.06
- ETEL.CA: score=21.42 buy_ready=False sector_rank=11 price=114.71 support=107.0 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=63.73 liquidity=192839920.0 spike=1.4
- ETRS.CA: score=21.32 buy_ready=False sector_rank=12 price=11.4 support=10.41 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.74 liquidity=37106640.0 spike=1.36
- EXPA.CA: score=21.64 buy_ready=False sector_rank=4 price=21.22 support=19.8 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.08 liquidity=43823788.0 spike=1.12
- FAIT.CA: score=22.06 buy_ready=False sector_rank=4 price=43.11 support=36.9 resistance=45.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=67.71 liquidity=9920716.0 spike=1.37
- FAITA.CA: score=11.5 buy_ready=False sector_rank=4 price=0.99 support=0.97 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=49.11 liquidity=56733.41 spike=1.02
- FERC.CA: score=20.76 buy_ready=False sector_rank=6 price=78.66 support=76.16 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.31 liquidity=20979344.0 spike=1.18
- FWRY.CA: score=17.83 buy_ready=False sector_rank=17 price=19.0 support=18.66 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.46 liquidity=104405984.0 spike=0.71
- GBCO.CA: score=15.26 buy_ready=False sector_rank=20 price=28.68 support=27.51 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=42.3 liquidity=76668472.0 spike=1.57
- GDWA.CA: score=23.78 buy_ready=False sector_rank=12 price=0.85 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=171646432.0 spike=3.09
- GGCC.CA: score=14.0 buy_ready=False sector_rank=12 price=0.85 support=0.85 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.64 liquidity=62039348.0 spike=1.2
- GIHD.CA: score=20.74 buy_ready=False sector_rank=12 price=72.0 support=57.82 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=65.41 liquidity=27490852.0 spike=1.07
- GMCI.CA: score=1.84 buy_ready=False sector_rank=12 price=1.88 support=1.83 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=13.33 liquidity=702819.0 spike=1.27
- GRCA.CA: score=20.6 buy_ready=False sector_rank=12 price=79.69 support=54.7 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=71.85 liquidity=59041788.0 spike=0.99
- GSSC.CA: score=14.88 buy_ready=False sector_rank=12 price=279.37 support=274.0 resistance=301.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=52.13 liquidity=6288079.0 spike=0.33
- GTWL.CA: score=17.6 buy_ready=False sector_rank=12 price=224.76 support=85.0 resistance=247.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:30 PM market time freshness=DELAYED_CURRENT RSI=80.72 liquidity=142482432.0 spike=0.5
- HDBK.CA: score=11.28 buy_ready=False sector_rank=4 price=115.18 support=102.5 resistance=119.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=162832032.0 spike=3.44
- HELI.CA: score=18.92 buy_ready=False sector_rank=8 price=7.78 support=7.34 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.5 liquidity=79866456.0 spike=0.5
- HRHO.CA: score=8.79 buy_ready=False sector_rank=18 price=25.89 support=25.33 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=17.61 liquidity=131601144.0 spike=1.08
- ICID.CA: score=5.6 buy_ready=False sector_rank=12 price=17.75 support=16.65 resistance=18.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24999374.0 spike=0.89
- IDRE.CA: score=20.78 buy_ready=False sector_rank=12 price=55.33 support=48.27 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=51.02 liquidity=15841989.0 spike=1.09
- IFAP.CA: score=18.16 buy_ready=False sector_rank=15 price=20.77 support=19.71 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.08 liquidity=30888874.0 spike=0.97
- INFI.CA: score=20.6 buy_ready=False sector_rank=12 price=151.12 support=114.05 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.09 liquidity=26852362.0 spike=0.38
- IRON.CA: score=10.4 buy_ready=False sector_rank=6 price=30.04 support=29.82 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.84 liquidity=12105939.0 spike=0.95
- ISMA.CA: score=21.28 buy_ready=False sector_rank=12 price=33.12 support=30.2 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.17 liquidity=34236036.0 spike=1.34
- ISMQ.CA: score=21.84 buy_ready=False sector_rank=6 price=9.37 support=9.0 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.92 liquidity=58848276.0 spike=1.22
- ISPH.CA: score=13.9 buy_ready=False sector_rank=9 price=12.94 support=11.83 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=47180344.0 spike=0.24
- JUFO.CA: score=20.06 buy_ready=False sector_rank=7 price=27.26 support=23.44 resistance=36.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.1 liquidity=24712724.0 spike=0.46
- KABO.CA: score=18.4 buy_ready=False sector_rank=2 price=9.3 support=7.86 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=75.7 liquidity=30062546.0 spike=0.69
- KWIN.CA: score=20.92 buy_ready=False sector_rank=12 price=109.55 support=84.08 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.97 liquidity=76290528.0 spike=1.16
- KZPC.CA: score=20.6 buy_ready=False sector_rank=12 price=13.08 support=8.69 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.46 liquidity=33509428.0 spike=0.64
- LCSW.CA: score=20.39 buy_ready=False sector_rank=14 price=36.0 support=32.12 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=54.58 liquidity=28789266.0 spike=0.94
- LUTS.CA: score=5.6 buy_ready=False sector_rank=12 price=1.05 support=1.02 resistance=1.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=235016928.0 spike=0.94
- MAAL.CA: score=7.26 buy_ready=False sector_rank=12 price=9.5 support=9.07 resistance=9.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23136426.0 spike=1.83
- MASR.CA: score=15.6 buy_ready=False sector_rank=12 price=7.71 support=7.45 resistance=8.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.34 liquidity=46504764.0 spike=0.72
- MBSC.CA: score=7.69 buy_ready=False sector_rank=14 price=454.47 support=405.0 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=183510560.0 spike=2.15
- MCQE.CA: score=5.45 buy_ready=False sector_rank=14 price=247.07 support=234.1 resistance=253.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=61357096.0 spike=1.03
- MCRO.CA: score=18.6 buy_ready=False sector_rank=12 price=1.5 support=1.44 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=52.78 liquidity=76025352.0 spike=0.61
- MENA.CA: score=7.0 buy_ready=False sector_rank=8 price=6.85 support=6.59 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.59 liquidity=1076633.13 spike=0.18
- MEPA.CA: score=20.64 buy_ready=False sector_rank=12 price=1.94 support=1.8 resistance=2.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=53.06 liquidity=31702528.0 spike=1.02
- MFPC.CA: score=23.36 buy_ready=False sector_rank=6 price=42.58 support=36.81 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.68 liquidity=220441840.0 spike=2.48
- MFSC.CA: score=12.72 buy_ready=False sector_rank=12 price=50.14 support=47.47 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=42.27 liquidity=2127080.75 spike=0.18
- MHOT.CA: score=17.58 buy_ready=False sector_rank=5 price=18.6 support=16.81 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=60.66 liquidity=8180836.0 spike=0.43
- MICH.CA: score=22.6 buy_ready=False sector_rank=12 price=50.13 support=42.15 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.95 liquidity=18195298.0 spike=0.44
- MILS.CA: score=18.6 buy_ready=False sector_rank=12 price=205.02 support=175.0 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=54.88 liquidity=16627966.0 spike=0.2
- MIPH.CA: score=19.04 buy_ready=False sector_rank=9 price=798.21 support=745.0 resistance=828.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=57.28 liquidity=7153067.0 spike=1.49
- MOED.CA: score=19.8 buy_ready=False sector_rank=12 price=0.87 support=0.66 resistance=0.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=78.47 liquidity=111497192.0 spike=1.1
- MOIL.CA: score=10.04 buy_ready=False sector_rank=16 price=0.69 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=54.41 liquidity=23148.26 spike=0.06
- MOIN.CA: score=18.6 buy_ready=False sector_rank=12 price=33.18 support=24.0 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=11939273.0 spike=0.35
- MOSC.CA: score=15.22 buy_ready=False sector_rank=12 price=315.29 support=290.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=59.86 liquidity=6622706.5 spike=0.41
- MPCI.CA: score=19.64 buy_ready=False sector_rank=12 price=442.08 support=293.06 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.21 liquidity=193132160.0 spike=1.02
- MPCO.CA: score=18.16 buy_ready=False sector_rank=15 price=2.08 support=1.91 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.7 liquidity=65540716.0 spike=0.52
- MPRC.CA: score=18.72 buy_ready=False sector_rank=12 price=42.92 support=39.5 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=45.79 liquidity=36801132.0 spike=1.06
- MTIE.CA: score=9.12 buy_ready=False sector_rank=20 price=8.85 support=8.01 resistance=11.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.65 liquidity=61336664.0 spike=0.91
- NAHO.CA: score=7.69 buy_ready=False sector_rank=12 price=0.14 support=0.1 resistance=0.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=84.48 liquidity=89165.22 spike=0.91
- NCCW.CA: score=12.86 buy_ready=False sector_rank=12 price=6.15 support=5.59 resistance=7.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.16 liquidity=28237680.0 spike=1.13
- NEDA.CA: score=5.91 buy_ready=False sector_rank=12 price=2.73 support=2.7 resistance=2.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=52.86 liquidity=313190.88 spike=0.37
- NHPS.CA: score=20.6 buy_ready=False sector_rank=12 price=88.89 support=82.5 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.81 liquidity=16346012.0 spike=0.51
- NINH.CA: score=22.6 buy_ready=False sector_rank=12 price=23.42 support=21.53 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.78 liquidity=18001312.0 spike=0.42
- NIPH.CA: score=13.9 buy_ready=False sector_rank=9 price=340.48 support=237.15 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.34 liquidity=94948344.0 spike=0.26
- OBRI.CA: score=24.12 buy_ready=False sector_rank=12 price=34.58 support=31.61 resistance=34.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.17 liquidity=51619548.0 spike=1.76
- OCDI.CA: score=18.92 buy_ready=False sector_rank=8 price=31.01 support=28.82 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.16 liquidity=52769268.0 spike=0.39
- OCPH.CA: score=10.08 buy_ready=False sector_rank=12 price=251.7 support=235.0 resistance=500.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.12 liquidity=3487701.25 spike=0.15
- ODIN.CA: score=18.6 buy_ready=False sector_rank=12 price=2.98 support=2.87 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.84 liquidity=26039346.0 spike=0.53
- OFH.CA: score=17.6 buy_ready=False sector_rank=12 price=1.03 support=0.71 resistance=1.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=76.94 liquidity=76952136.0 spike=0.72
- OIH.CA: score=21.4 buy_ready=False sector_rank=1 price=2.05 support=1.48 resistance=2.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.06 liquidity=115189728.0 spike=0.74
- OLFI.CA: score=16.06 buy_ready=False sector_rank=7 price=22.19 support=22.53 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.74 liquidity=49719880.0 spike=0.88
- ORAS.CA: score=4.6 buy_ready=False sector_rank=19 price=827.56 support=822.5 resistance=859.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=203159776.0 spike=1.0
- ORHD.CA: score=19.06 buy_ready=False sector_rank=8 price=41.53 support=39.7 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.97 liquidity=153135440.0 spike=1.07
- ORWE.CA: score=24.06 buy_ready=False sector_rank=2 price=26.9 support=22.86 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.61 liquidity=106219544.0 spike=1.33
- PHAR.CA: score=18.9 buy_ready=False sector_rank=9 price=127.39 support=127.27 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.77 liquidity=127764328.0 spike=0.27
- PHDC.CA: score=15.92 buy_ready=False sector_rank=8 price=14.8 support=14.5 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.63 liquidity=227813744.0 spike=0.97
- PHTV.CA: score=9.95 buy_ready=False sector_rank=12 price=347.98 support=311.27 resistance=447.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=49.78 liquidity=1353954.75 spike=0.52
- POUL.CA: score=23.58 buy_ready=False sector_rank=7 price=39.95 support=36.6 resistance=40.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=56.07 liquidity=30215636.0 spike=1.26
- PRCL.CA: score=16.91 buy_ready=False sector_rank=14 price=32.2 support=31.0 resistance=37.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.81 liquidity=40333344.0 spike=1.76
- PRDC.CA: score=29.92 buy_ready=False sector_rank=8 price=9.89 support=8.7 resistance=9.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.13 liquidity=278562816.0 spike=4.29
- PRMH.CA: score=18.78 buy_ready=False sector_rank=12 price=2.68 support=2.28 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=44.55 liquidity=8186273.0 spike=0.55
- RACC.CA: score=10.86 buy_ready=False sector_rank=12 price=9.62 support=9.4 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=28.08 liquidity=22950336.0 spike=1.13
- RAKT.CA: score=-0.07 buy_ready=False sector_rank=12 price=22.2 support=21.4 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=25.71 liquidity=332124.13 spike=0.96
- RAYA.CA: score=19.5 buy_ready=False sector_rank=13 price=7.26 support=6.95 resistance=7.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.66 liquidity=25657338.0 spike=0.39
- RMDA.CA: score=19.46 buy_ready=False sector_rank=9 price=5.94 support=5.6 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.04 liquidity=150770000.0 spike=1.28
- ROTO.CA: score=15.6 buy_ready=False sector_rank=12 price=44.17 support=43.7 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.23 liquidity=10286105.0 spike=0.48
- RREI.CA: score=18.6 buy_ready=False sector_rank=12 price=4.42 support=4.24 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.93 liquidity=11081549.0 spike=0.2
- RTVC.CA: score=17.43 buy_ready=False sector_rank=12 price=4.14 support=3.73 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=66.99 liquidity=6836232.5 spike=0.81
- RUBX.CA: score=20.6 buy_ready=False sector_rank=12 price=12.61 support=12.2 resistance=13.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.01 liquidity=11110229.0 spike=0.62
- SAUD.CA: score=22.18 buy_ready=False sector_rank=4 price=24.01 support=21.61 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=56.27 liquidity=28022934.0 spike=1.39
- SCEM.CA: score=5.39 buy_ready=False sector_rank=14 price=101.99 support=97.22 resistance=102.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=182450832.0 spike=0.83
- SCFM.CA: score=11.97 buy_ready=False sector_rank=12 price=282.11 support=273.1 resistance=305.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.88 liquidity=3372048.75 spike=0.17
- SCTS.CA: score=11.82 buy_ready=False sector_rank=21 price=616.43 support=603.13 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=61.28 liquidity=2743009.25 spike=0.31
- SDTI.CA: score=18.38 buy_ready=False sector_rank=12 price=68.68 support=59.5 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.64 liquidity=9788333.0 spike=0.33
- SEIG.CA: score=8.9 buy_ready=False sector_rank=12 price=259.47 support=252.0 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=44.21 liquidity=307090.88 spike=0.04
- SIPC.CA: score=20.6 buy_ready=False sector_rank=12 price=4.93 support=4.1 resistance=5.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.05 liquidity=20701194.0 spike=0.38
- SKPC.CA: score=25.44 buy_ready=False sector_rank=6 price=17.8 support=15.71 resistance=18.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.93 liquidity=152997168.0 spike=2.02
- SMFR.CA: score=8.31 buy_ready=False sector_rank=12 price=257.31 support=228.88 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=27.65 liquidity=4710172.0 spike=0.18
- SNFC.CA: score=8.03 buy_ready=False sector_rank=12 price=10.4 support=10.3 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.16 liquidity=8433977.0 spike=0.58
- SPIN.CA: score=23.4 buy_ready=False sector_rank=2 price=19.2 support=15.32 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=70.14 liquidity=11764133.0 spike=0.29
- SPMD.CA: score=10.6 buy_ready=False sector_rank=12 price=0.44 support=0.45 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.27 liquidity=11896656.0 spike=0.59
- SUGR.CA: score=21.06 buy_ready=False sector_rank=7 price=56.14 support=46.53 resistance=61.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.97 liquidity=30114252.0 spike=0.53
- SVCE.CA: score=10.6 buy_ready=False sector_rank=12 price=12.29 support=10.51 resistance=12.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=746993600.0 spike=7.14
- SWDY.CA: score=22.4 buy_ready=False sector_rank=3 price=127.51 support=95.48 resistance=133.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.98 liquidity=51568908.0 spike=0.48
- TALM.CA: score=17.08 buy_ready=False sector_rank=21 price=17.86 support=17.11 resistance=20.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.52 liquidity=15763284.0 spike=0.34
- TMGH.CA: score=15.92 buy_ready=False sector_rank=8 price=96.84 support=94.9 resistance=99.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.62 liquidity=235085712.0 spike=0.9
- TRTO.CA: score=0.68 buy_ready=False sector_rank=12 price=0.06 support=0.05 resistance=0.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=83294.68 spike=6.79
- UEFM.CA: score=9.54 buy_ready=False sector_rank=12 price=536.73 support=531.0 resistance=589.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.27 liquidity=944679.13 spike=0.2
- UEGC.CA: score=13.52 buy_ready=False sector_rank=12 price=1.75 support=1.8 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.76 liquidity=106437752.0 spike=2.46
- UNIP.CA: score=18.6 buy_ready=False sector_rank=12 price=0.38 support=0.35 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.6 liquidity=16214216.0 spike=0.49
- UNIT.CA: score=10.36 buy_ready=False sector_rank=8 price=18.62 support=17.8 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.19 liquidity=1439238.75 spike=0.12
- WCDF.CA: score=7.22 buy_ready=False sector_rank=12 price=640.74 support=580.05 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=78.05 liquidity=1627181.75 spike=0.41
- WKOL.CA: score=19.75 buy_ready=False sector_rank=12 price=340.78 support=315.0 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=58.19 liquidity=7156769.0 spike=0.21
- ZEOT.CA: score=14.03 buy_ready=False sector_rank=12 price=14.0 support=12.2 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=65.9 liquidity=5432285.5 spike=0.24
- ZMID.CA: score=19.92 buy_ready=False sector_rank=8 price=9.05 support=7.06 resistance=9.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=78.11 liquidity=235829424.0 spike=0.93

## Backtesting Lite
- PRDC.CA: 180d return=133.17%, max drawdown=-14.02%, MA20>MA50 days last20=20, as_of=2026-08-30T21:00:00+00:00
- EBSC.CA: 180d return=30.72%, max drawdown=-23.41%, MA20>MA50 days last20=20, as_of=2026-08-30T21:00:00+00:00
- CIEB.CA: 180d return=27.54%, max drawdown=-19.11%, MA20>MA50 days last20=20, as_of=2026-08-30T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- PRDC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Pioneers Properties For Urban Development summary=Evidence rejected for PRDC.CA: source text did not clearly match PRDC.CA / Pioneers Properties For Urban Development.
- EBSC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Osool ESB Securities Brokerage summary=Evidence rejected for EBSC.CA: source text did not clearly match EBSC.CA / Osool ESB Securities Brokerage.
- CIEB.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Credit Agricole Egypt summary=Evidence rejected for CIEB.CA: source text did not clearly match CIEB.CA / Credit Agricole Egypt.
- ABUK.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Qir Fertilizers summary=Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results; Abu Qir Fertilizers&#39; board approves $5.6m coated urea project; Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26
  - Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results: https://english.mubasher.info/news/4604919/Abu-Qir-Fertilizers-generates-EGP-5-6bn-net-profits-in-Q1-26-unaudited-results/
  - Abu Qir Fertilizers&#39; board approves $5.6m coated urea project: https://english.mubasher.info/news/4585599/Abu-Qir-Fertilizers-board-approves-5-6m-coated-urea-project/
  - Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26: https://english.mubasher.info/news/4554415/Abu-Qir-Fertilizers-profits-exceed-EGP-5-1bn-in-H1-25-26/
- CLHO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=608 sources=3 expected=Cleopatra Hospital Group summary=Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025; Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn; Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo
  - Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025: https://english.mubasher.info/news/4594702/Cleopatra-Hospitals-unveils-EGP-84m-dividends-to-employee-for-2025/
  - Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn: https://english.mubasher.info/news/4579844/Cleopatra-Hospitals-posts-higher-consolidated-profits-in-2025-revenues-cross-EGP-7-2bn/
  - Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo: https://english.mubasher.info/news/4553462/Cleopatra-Hospitals-launches-EGP-3-5bn-Sky-hospital-in-East-Cairo/
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- SKPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Sidi Kerir Petrochemicals summary=Evidence rejected for SKPC.CA: source text did not clearly match SKPC.CA / Sidi Kerir Petrochemicals.
- DAPH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Development & Engineering Consultants summary=Evidence rejected for DAPH.CA: source text did not clearly match DAPH.CA / Development & Engineering Consultants.

## Warnings
- Evidence rejected for PRDC.CA: source text did not clearly match PRDC.CA / Pioneers Properties For Urban Development.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for EBSC.CA: source text did not clearly match EBSC.CA / Osool ESB Securities Brokerage.
- Evidence rejected for CIEB.CA: source text did not clearly match CIEB.CA / Credit Agricole Egypt.
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Evidence for CLHO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Evidence rejected for SKPC.CA: source text did not clearly match SKPC.CA / Sidi Kerir Petrochemicals.
- Evidence rejected for DAPH.CA: source text did not clearly match DAPH.CA / Development & Engineering Consultants.
