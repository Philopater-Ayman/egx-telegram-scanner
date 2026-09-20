# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-09-20T10:08:01.208500+00:00
Generated Cairo: 2026-09-20 13:08
Run timing: target 08:45 Cairo | generated Cairo 2026-09-20 13:08 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-20 13:04

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 169/187
- Top sector: Investment Holding

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, September 20
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 55.56% / above MA50 61.11%
- EGX70 regime: BEARISH / above MA20 37.84% / above MA50 56.76%
- Sector breadth: 14.29%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=405748736.0 spike=0.49 score=23.4
- MPCO.CA: liquidity=206374816.0 spike=1.34 score=5.34
- ABUK.CA: liquidity=170717136.0 spike=1.09 score=5.64
- EGCH.CA: liquidity=156513536.0 spike=1.36 score=21.18
- BTFH.CA: liquidity=155784224.0 spike=1.66 score=17.27

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with low sector breadth (14.29%), triggering a defensive risk mode that blocks new buys; the scanner still highlights several tickets with high rank scores and bullish‑watch outlooks, but they show elevated RSI, liquidity spikes, and prices near resistance, suggesting limited upside in the next 1‑3 days.
- Selected tickets (BINV.CA, OIH.CA, GBCO.CA, etc.) rank high due to accumulation spikes and bullish‑watch scores, yet RSI >60 indicates overextension.
- Liquidity is spiking or cooling, support lies below current prices while resistance is tight or just above, and leading sectors (Investment Holding, Telecommunications, Education) show strong MA20/50 alignment.
- EGX30/EGX70 bearish trend and weak breadth shift risk mode to DEFENSIVE_NO_NEW_BUY, lowering confidence in any new long positions.
- Uncertainty remains: mixed signals from strong sector fundamentals versus technical overextension and negative medium‑term returns could reverse quickly.

## Top Liquidity Spikes
- IDRE.CA: spike=4.41 liquidity=45160868.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RUBX.CA: spike=3.74 liquidity=73134408.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- FAITA.CA: spike=3.28 liquidity=141508.62 outlook=WEAK_OR_RISKY score=6.32 buy_ready=False
- ENGC.CA: spike=3.05 liquidity=37061424.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ZEOT.CA: spike=2.8 liquidity=18408180.0 outlook=NEUTRAL score=49.98 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=17.11 5d=12.95% 20d=25.96% aboveMA50=100.0%
- #2 Telecommunications: score=9.74 5d=1.89% 20d=8.38% aboveMA50=100.0%
- #3 Education: score=6.08 5d=1.67% 20d=3.61% aboveMA50=66.67%
- #4 Energy & Petrochemicals: score=5.15 5d=-4.2% 20d=3.69% aboveMA50=100.0%
- #5 Automotive & Distribution: score=4.5 5d=-0.07% 20d=0.23% aboveMA50=50.0%
- #6 Textiles: score=3.81 5d=-4.62% 20d=4.21% aboveMA50=100.0%
- #7 Basic Resources & Chemicals: score=3.66 5d=-2.42% 20d=-0.13% aboveMA50=60.0%
- #8 Banking & Financials: score=3.32 5d=-1.77% 20d=-0.53% aboveMA50=70.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- OIH.CA: BULLISH_WATCH score=84 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- GBCO.CA: BULLISH_WATCH score=83.5 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- BINV.CA: BULLISH_WATCH score=83 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support
- EGAS.CA: BULLISH_WATCH score=81.15 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- WKOL.CA: BULLISH_WATCH score=80.98 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- KABO.CA: BULLISH_WATCH score=79.81 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- FERC.CA: BULLISH_WATCH score=79.66 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- EGCH.CA: BULLISH_WATCH score=78.66 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- MFSC.CA: BULLISH_WATCH score=77.98 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- EXPA.CA: BULLISH_WATCH score=74.32 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=17.79 buy_ready=False sector_rank=11 price=305.99 support=295.0 resistance=345.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=61.15 liquidity=17658212.0 spike=0.84
- ABUK.CA: score=5.64 buy_ready=False sector_rank=7 price=94.43 support=93.0 resistance=95.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=170717136.0 spike=1.09
- ACAMD.CA: score=18.79 buy_ready=False sector_rank=11 price=2.11 support=1.95 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=31076734.0 spike=0.52
- ACGC.CA: score=13.46 buy_ready=False sector_rank=6 price=14.05 support=12.56 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=47.61 liquidity=4936315.0 spike=0.13
- ADCI.CA: score=9.9 buy_ready=False sector_rank=11 price=285.74 support=267.66 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=38.15 liquidity=2105695.5 spike=0.36
- ADIB.CA: score=20.33 buy_ready=False sector_rank=8 price=52.97 support=50.51 resistance=55.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=38.56 liquidity=48825452.0 spike=0.68
- ADPC.CA: score=17.15 buy_ready=False sector_rank=11 price=3.96 support=3.81 resistance=4.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=45.28 liquidity=24092702.0 spike=1.18
- AFDI.CA: score=15.15 buy_ready=False sector_rank=11 price=55.53 support=51.6 resistance=68.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=49.6 liquidity=7354905.5 spike=0.3
- AFMC.CA: score=9.79 buy_ready=False sector_rank=11 price=164.72 support=153.0 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=28.35 liquidity=24249210.0 spike=0.37
- AJWA.CA: score=8.41 buy_ready=False sector_rank=11 price=180.02 support=175.15 resistance=199.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=44.93 liquidity=3621221.25 spike=0.08
- ALCN.CA: score=4.68 buy_ready=False sector_rank=16 price=33.47 support=33.16 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32908322.0 spike=1.13
- ALUM.CA: score=5.52 buy_ready=False sector_rank=11 price=26.97 support=25.0 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=22.55 liquidity=2729901.25 spike=0.19
- AMER.CA: score=12.51 buy_ready=False sector_rank=15 price=5.41 support=4.8 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=34.13 liquidity=14652968.0 spike=0.23
- AMES.CA: score=4.79 buy_ready=False sector_rank=11 price=51.23 support=51.2 resistance=53.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46488096.0 spike=0.17
- AMIA.CA: score=17.79 buy_ready=False sector_rank=11 price=18.12 support=15.3 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=36.22 liquidity=14790905.0 spike=0.25
- AMOC.CA: score=19.06 buy_ready=False sector_rank=4 price=14.11 support=10.65 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=74.24 liquidity=115948656.0 spike=0.66
- APSW.CA: score=4.28 buy_ready=False sector_rank=11 price=8.42 support=8.37 resistance=8.99 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=44.94 liquidity=487795.86 spike=0.52
- ARAB.CA: score=14.51 buy_ready=False sector_rank=15 price=0.25 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=27367062.0 spike=0.25
- ARCC.CA: score=17.2 buy_ready=False sector_rank=19 price=72.99 support=71.5 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=43.26 liquidity=10172798.0 spike=0.24
- AREH.CA: score=11.39 buy_ready=False sector_rank=11 price=1.45 support=1.39 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=6596947.5 spike=0.44
- ASCM.CA: score=7.51 buy_ready=False sector_rank=11 price=61.26 support=60.15 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=36.59 liquidity=2715026.5 spike=0.12
- ASPI.CA: score=17.79 buy_ready=False sector_rank=11 price=0.46 support=0.41 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=38.27 liquidity=56385440.0 spike=1.0
- ATLC.CA: score=13.83 buy_ready=False sector_rank=9 price=7.25 support=5.2 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=66.16 liquidity=5876754.5 spike=0.21
- ATQA.CA: score=20.46 buy_ready=False sector_rank=7 price=13.1 support=10.8 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=64.41 liquidity=68928840.0 spike=0.66
- AXPH.CA: score=14.26 buy_ready=False sector_rank=11 price=1688.98 support=1362.0 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=55.4 liquidity=2464302.0 spike=0.2
- BINV.CA: score=25.22 buy_ready=False sector_rank=1 price=62.63 support=47.07 resistance=62.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=83.0 liquidity=32899396.0 spike=1.91
- BIOC.CA: score=9.79 buy_ready=False sector_rank=11 price=276.05 support=272.01 resistance=506.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=14.21 liquidity=12846919.0 spike=0.11
- BTFH.CA: score=17.27 buy_ready=False sector_rank=9 price=3.03 support=2.87 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=37.93 liquidity=155784224.0 spike=1.66
- CAED.CA: score=12.02 buy_ready=False sector_rank=11 price=129.15 support=123.56 resistance=181.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=29.76 liquidity=9228328.0 spike=0.26
- CANA.CA: score=8.03 buy_ready=False sector_rank=8 price=46.44 support=44.0 resistance=46.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33660608.0 spike=2.35
- CCAP.CA: score=23.4 buy_ready=False sector_rank=1 price=7.04 support=5.42 resistance=6.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=79.08 liquidity=405748736.0 spike=0.49
- CCRS.CA: score=19.79 buy_ready=False sector_rank=11 price=2.66 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=40.91 liquidity=14330454.0 spike=0.27
- CEFM.CA: score=15.93 buy_ready=False sector_rank=11 price=147.34 support=143.0 resistance=167.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=53.61 liquidity=6139615.5 spike=0.39
- CERA.CA: score=19.79 buy_ready=False sector_rank=11 price=1.46 support=1.22 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=57.63 liquidity=39742460.0 spike=0.36
- CFGH.CA: score=7.8 buy_ready=False sector_rank=11 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=63.16 liquidity=8225.7 spike=0.42
- CICH.CA: score=12.78 buy_ready=False sector_rank=9 price=13.06 support=12.0 resistance=13.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=54.91 liquidity=2831284.25 spike=0.48
- CIEB.CA: score=14.6 buy_ready=False sector_rank=8 price=25.32 support=24.01 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=46.05 liquidity=4275625.0 spike=0.31
- CIRA.CA: score=22.4 buy_ready=False sector_rank=3 price=40.62 support=32.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=29914250.0 spike=0.82
- CLHO.CA: score=8.56 buy_ready=False sector_rank=21 price=16.01 support=15.81 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=33.81 liquidity=59517176.0 spike=0.77
- CNFN.CA: score=15.15 buy_ready=False sector_rank=9 price=4.75 support=4.46 resistance=4.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=39.47 liquidity=13336900.0 spike=1.1
- COMI.CA: score=10.33 buy_ready=False sector_rank=8 price=133.0 support=131.11 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=31.43 liquidity=109255616.0 spike=0.2
- COPR.CA: score=17.79 buy_ready=False sector_rank=11 price=0.51 support=0.46 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=38.82 liquidity=34853668.0 spike=0.48
- COSG.CA: score=19.79 buy_ready=False sector_rank=11 price=1.87 support=1.74 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=48.72 liquidity=21478528.0 spike=0.53
- CPCI.CA: score=1.94 buy_ready=False sector_rank=11 price=560.19 support=546.54 resistance=584.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6148364.0 spike=1.5
- CSAG.CA: score=-1.25 buy_ready=False sector_rank=16 price=38.39 support=38.25 resistance=39.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4337988.0 spike=0.26
- DAPH.CA: score=17.79 buy_ready=False sector_rank=11 price=123.14 support=108.11 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=52.89 liquidity=11898532.0 spike=0.19
- DEIN.CA: score=7.79 buy_ready=False sector_rank=11 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=0.66 buy_ready=False sector_rank=17 price=27.01 support=26.51 resistance=29.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=28.18 liquidity=1247213.75 spike=0.22
- DSCW.CA: score=13.79 buy_ready=False sector_rank=11 price=1.83 support=1.8 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=37.93 liquidity=22401684.0 spike=0.59
- DTPP.CA: score=19.79 buy_ready=False sector_rank=11 price=345.07 support=292.5 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=68.84 liquidity=64025732.0 spike=0.98
- EALR.CA: score=8.43 buy_ready=False sector_rank=11 price=380.12 support=340.0 resistance=415.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=3635634.0 spike=0.26
- EASB.CA: score=17.42 buy_ready=False sector_rank=11 price=8.1 support=7.16 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=56.2 liquidity=5626302.0 spike=0.33
- EAST.CA: score=8.41 buy_ready=False sector_rank=17 price=32.07 support=32.0 resistance=36.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=28.11 liquidity=24669924.0 spike=0.35
- EBSC.CA: score=10.04 buy_ready=False sector_rank=11 price=2.08 support=1.88 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=47.96 liquidity=2243243.0 spike=0.15
- ECAP.CA: score=5.76 buy_ready=False sector_rank=11 price=32.58 support=31.16 resistance=37.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=43.33 liquidity=967272.75 spike=0.08
- EDFM.CA: score=10.12 buy_ready=False sector_rank=11 price=413.39 support=399.0 resistance=465.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=58.7 liquidity=330902.25 spike=0.17
- EEII.CA: score=4.79 buy_ready=False sector_rank=11 price=2.32 support=2.23 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16143629.0 spike=0.76
- EFIC.CA: score=14.46 buy_ready=False sector_rank=7 price=193.97 support=192.75 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=33972916.0 spike=0.1
- EFID.CA: score=19.41 buy_ready=False sector_rank=17 price=31.59 support=29.71 resistance=33.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=39.83 liquidity=21338992.0 spike=0.35
- EFIH.CA: score=17.29 buy_ready=False sector_rank=18 price=23.41 support=22.16 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=41.65 liquidity=37933632.0 spike=0.61
- EGAL.CA: score=20.46 buy_ready=False sector_rank=7 price=370.06 support=321.01 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=49.36 liquidity=18949088.0 spike=0.18
- EGAS.CA: score=17.33 buy_ready=False sector_rank=4 price=58.56 support=55.0 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=43.63 liquidity=6268180.0 spike=0.73
- EGBE.CA: score=3.35 buy_ready=False sector_rank=8 price=0.51 support=0.49 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=29.63 liquidity=21122.99 spike=0.18
- EGCH.CA: score=21.18 buy_ready=False sector_rank=7 price=14.23 support=13.3 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=58.58 liquidity=156513536.0 spike=1.36
- EGSA.CA: score=11.39 buy_ready=False sector_rank=2 price=9.0 support=8.67 resistance=9.1 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=78.18 liquidity=10413.0 spike=1.49
- EGTS.CA: score=13.47 buy_ready=False sector_rank=15 price=16.81 support=16.17 resistance=17.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=47.02 liquidity=8958775.0 spike=0.36
- EHDR.CA: score=11.67 buy_ready=False sector_rank=11 price=2.79 support=2.73 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=6875314.0 spike=0.34
- ELEC.CA: score=8.54 buy_ready=False sector_rank=14 price=2.02 support=1.93 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=30.56 liquidity=62516808.0 spike=0.91
- ELKA.CA: score=14.79 buy_ready=False sector_rank=11 price=1.74 support=1.7 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=47.17 liquidity=10346352.0 spike=0.24
- ELNA.CA: score=-1.18 buy_ready=False sector_rank=11 price=35.74 support=33.96 resistance=38.99 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=28.76 liquidity=23302.48 spike=0.06
- ELSH.CA: score=14.79 buy_ready=False sector_rank=11 price=13.3 support=12.67 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=41.01 liquidity=10262271.0 spike=0.26
- ELWA.CA: score=6.39 buy_ready=False sector_rank=11 price=1.7 support=1.62 resistance=1.99 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=36.36 liquidity=1599076.14 spike=0.65
- EMFD.CA: score=17.51 buy_ready=False sector_rank=15 price=14.04 support=11.55 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=73.27 liquidity=38348376.0 spike=0.22
- ENGC.CA: score=8.89 buy_ready=False sector_rank=11 price=43.9 support=42.41 resistance=45.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37061424.0 spike=3.05
- EOSB.CA: score=10.01 buy_ready=False sector_rank=11 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=77512.47 spike=1.07
- EPCO.CA: score=14.71 buy_ready=False sector_rank=11 price=11.51 support=10.8 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=47.6 liquidity=4915922.0 spike=0.26
- EPPK.CA: score=-4.79 buy_ready=False sector_rank=11 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=20.4 buy_ready=False sector_rank=2 price=132.04 support=112.5 resistance=135.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=83.97 liquidity=52908012.0 spike=0.25
- ETRS.CA: score=18.31 buy_ready=False sector_rank=11 price=11.17 support=10.66 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=49.74 liquidity=8520294.0 spike=0.56
- EXPA.CA: score=20.33 buy_ready=False sector_rank=8 price=21.3 support=19.8 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=60.73 liquidity=25655290.0 spike=0.68
- FAIT.CA: score=9.44 buy_ready=False sector_rank=8 price=46.87 support=39.58 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=66.22 liquidity=1113277.38 spike=0.13
- FAITA.CA: score=5.03 buy_ready=False sector_rank=8 price=0.99 support=0.98 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=9.76 liquidity=141508.62 spike=3.28
- FERC.CA: score=18.84 buy_ready=False sector_rank=7 price=79.95 support=76.9 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=48.29 liquidity=8376735.5 spike=0.47
- FWRY.CA: score=14.29 buy_ready=False sector_rank=18 price=18.92 support=18.66 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=50.8 liquidity=24554440.0 spike=0.17
- GBCO.CA: score=24.22 buy_ready=False sector_rank=5 price=30.78 support=27.51 resistance=31.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=62.31 liquidity=98076304.0 spike=1.71
- GDWA.CA: score=13.79 buy_ready=False sector_rank=11 price=0.78 support=0.76 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=43.92 liquidity=17205930.0 spike=0.39
- GGCC.CA: score=9.31 buy_ready=False sector_rank=11 price=0.86 support=0.83 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=35.36 liquidity=4514016.5 spike=0.13
- GIHD.CA: score=15.15 buy_ready=False sector_rank=11 price=73.54 support=58.01 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=65.35 liquidity=7361330.0 spike=0.25
- GMCI.CA: score=1.35 buy_ready=False sector_rank=11 price=1.75 support=1.69 resistance=1.94 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=23.33 liquidity=841701.0 spike=1.86
- GRCA.CA: score=4.79 buy_ready=False sector_rank=11 price=41.42 support=41.21 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10248384.0 spike=0.12
- GSSC.CA: score=5.51 buy_ready=False sector_rank=11 price=318.6 support=315.01 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12547274.0 spike=1.36
- GTWL.CA: score=19.79 buy_ready=False sector_rank=11 price=233.87 support=181.52 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=62.29 liquidity=58639776.0 spike=0.23
- HDBK.CA: score=18.33 buy_ready=False sector_rank=8 price=119.52 support=89.01 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=66.08 liquidity=20559334.0 spike=0.36
- HELI.CA: score=21.51 buy_ready=False sector_rank=15 price=8.34 support=7.34 resistance=8.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=68.15 liquidity=110181624.0 spike=0.71
- HRHO.CA: score=13.95 buy_ready=False sector_rank=9 price=25.4 support=25.04 resistance=26.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=40.38 liquidity=52803604.0 spike=0.52
- ICID.CA: score=14.19 buy_ready=False sector_rank=11 price=17.98 support=15.25 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=60.06 liquidity=4393521.0 spike=0.27
- IDRE.CA: score=9.79 buy_ready=False sector_rank=11 price=57.93 support=55.7 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=45160868.0 spike=4.41
- IFAP.CA: score=12.97 buy_ready=False sector_rank=12 price=20.53 support=20.05 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=40.41 liquidity=5304204.5 spike=0.19
- INFI.CA: score=7.64 buy_ready=False sector_rank=11 price=135.0 support=130.15 resistance=174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=16.41 liquidity=4847509.5 spike=0.15
- IRON.CA: score=9.46 buy_ready=False sector_rank=7 price=28.44 support=26.3 resistance=32.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=2.57 liquidity=10788488.0 spike=0.75
- ISMA.CA: score=2.68 buy_ready=False sector_rank=11 price=30.99 support=28.05 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=18.03 liquidity=2892539.75 spike=0.11
- ISMQ.CA: score=15.74 buy_ready=False sector_rank=7 price=9.1 support=8.68 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=37.6 liquidity=30953042.0 spike=1.14
- ISPH.CA: score=8.56 buy_ready=False sector_rank=21 price=12.1 support=11.9 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=34.75 liquidity=37474088.0 spike=0.54
- JUFO.CA: score=9.08 buy_ready=False sector_rank=17 price=27.03 support=26.45 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=47.98 liquidity=3664410.5 spike=0.17
- KABO.CA: score=20.52 buy_ready=False sector_rank=6 price=9.38 support=8.82 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=53.97 liquidity=14427540.0 spike=0.29
- KWIN.CA: score=9.79 buy_ready=False sector_rank=11 price=91.63 support=84.5 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=32.99 liquidity=11437564.0 spike=0.17
- KZPC.CA: score=17.79 buy_ready=False sector_rank=11 price=14.42 support=12.6 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=72.6 liquidity=11341894.0 spike=0.18
- LCSW.CA: score=12.05 buy_ready=False sector_rank=19 price=33.5 support=32.42 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=45.62 liquidity=7846026.0 spike=0.3
- LUTS.CA: score=17.79 buy_ready=False sector_rank=11 price=0.95 support=0.79 resistance=1.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=51.07 liquidity=26090872.0 spike=0.1
- MAAL.CA: score=10.35 buy_ready=False sector_rank=11 price=8.9 support=8.18 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:27 AM market time freshness=DELAYED_CURRENT RSI=35.22 liquidity=2562754.0 spike=0.25
- MASR.CA: score=14.79 buy_ready=False sector_rank=11 price=7.77 support=7.49 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=56.91 liquidity=54692016.0 spike=0.58
- MBSC.CA: score=17.2 buy_ready=False sector_rank=19 price=363.61 support=363.0 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=46.6 liquidity=17327130.0 spike=0.33
- MCQE.CA: score=17.2 buy_ready=False sector_rank=19 price=219.89 support=213.0 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=41.55 liquidity=11239173.0 spike=0.32
- MCRO.CA: score=16.79 buy_ready=False sector_rank=11 price=1.69 support=1.44 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=79.49 liquidity=33426966.0 spike=0.26
- MENA.CA: score=4.88 buy_ready=False sector_rank=15 price=6.72 support=6.58 resistance=7.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=363191.44 spike=0.15
- MEPA.CA: score=19.79 buy_ready=False sector_rank=11 price=1.98 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=58.97 liquidity=26008192.0 spike=0.68
- MFPC.CA: score=19.54 buy_ready=False sector_rank=7 price=50.44 support=39.02 resistance=48.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=81.52 liquidity=147759968.0 spike=1.04
- MFSC.CA: score=15.37 buy_ready=False sector_rank=11 price=51.02 support=48.5 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=5421348.0 spike=1.08
- MHOT.CA: score=9.01 buy_ready=False sector_rank=10 price=18.07 support=17.62 resistance=19.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=35.64 liquidity=2104044.5 spike=0.21
- MICH.CA: score=14.39 buy_ready=False sector_rank=11 price=49.67 support=47.2 resistance=53.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=48.52 liquidity=6600124.5 spike=0.31
- MILS.CA: score=9.26 buy_ready=False sector_rank=11 price=203.99 support=198.0 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=32.69 liquidity=6463061.0 spike=0.14
- MIPH.CA: score=0.94 buy_ready=False sector_rank=21 price=852.57 support=811.03 resistance=878.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6191780.0 spike=1.59
- MOED.CA: score=16.79 buy_ready=False sector_rank=11 price=0.78 support=0.74 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=51.14 liquidity=10020437.0 spike=0.09
- MOIL.CA: score=9.24 buy_ready=False sector_rank=4 price=0.68 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=58.11 liquidity=179080.78 spike=0.86
- MOIN.CA: score=15.31 buy_ready=False sector_rank=11 price=36.91 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=53.32 liquidity=5522182.0 spike=0.18
- MOSC.CA: score=13.53 buy_ready=False sector_rank=11 price=314.63 support=302.0 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=30.09 liquidity=10312919.0 spike=1.37
- MPCI.CA: score=17.79 buy_ready=False sector_rank=11 price=405.17 support=345.0 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=53.38 liquidity=49115288.0 spike=0.31
- MPCO.CA: score=5.34 buy_ready=False sector_rank=12 price=2.92 support=2.72 resistance=2.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=206374816.0 spike=1.34
- MPRC.CA: score=8.76 buy_ready=False sector_rank=11 price=39.93 support=38.31 resistance=46.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=35.32 liquidity=3968331.0 spike=0.1
- MTIE.CA: score=15.74 buy_ready=False sector_rank=5 price=8.48 support=8.1 resistance=8.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=45.86 liquidity=9944102.0 spike=0.26
- NAHO.CA: score=7.8 buy_ready=False sector_rank=11 price=0.14 support=0.13 resistance=0.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=9539.91 spike=0.15
- NCCW.CA: score=16.79 buy_ready=False sector_rank=11 price=7.88 support=5.59 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=75.87 liquidity=39984904.0 spike=0.66
- NEDA.CA: score=10.27 buy_ready=False sector_rank=11 price=2.79 support=2.7 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=40.62 liquidity=477982.06 spike=0.67
- NHPS.CA: score=7.4 buy_ready=False sector_rank=11 price=77.55 support=75.31 resistance=98.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=6.12 liquidity=7604758.0 spike=0.38
- NINH.CA: score=10.45 buy_ready=False sector_rank=11 price=21.72 support=20.5 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=25.28 liquidity=40375420.0 spike=1.33
- NIPH.CA: score=11.56 buy_ready=False sector_rank=21 price=315.24 support=301.0 resistance=414.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=17.33 liquidity=30902480.0 spike=0.16
- OBRI.CA: score=10.21 buy_ready=False sector_rank=11 price=31.35 support=30.1 resistance=34.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=37.87 liquidity=6413312.5 spike=0.38
- OCDI.CA: score=14.51 buy_ready=False sector_rank=15 price=30.18 support=29.25 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=41.46 liquidity=46023156.0 spike=0.56
- OCPH.CA: score=3.26 buy_ready=False sector_rank=11 price=244.65 support=210.0 resistance=277.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=33.91 liquidity=2467912.75 spike=0.3
- ODIN.CA: score=9.79 buy_ready=False sector_rank=11 price=2.86 support=2.55 resistance=3.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=13.51 liquidity=24170356.0 spike=0.97
- OFH.CA: score=19.79 buy_ready=False sector_rank=11 price=1.09 support=0.88 resistance=1.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=100471656.0 spike=0.81
- OIH.CA: score=24.4 buy_ready=False sector_rank=1 price=2.17 support=1.83 resistance=2.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=66.0 liquidity=58948224.0 spike=0.47
- OLFI.CA: score=11.42 buy_ready=False sector_rank=17 price=22.9 support=22.07 resistance=24.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=41.47 liquidity=7006412.0 spike=0.43
- ORAS.CA: score=4.6 buy_ready=False sector_rank=13 price=855.47 support=850.4 resistance=875.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=100525416.0 spike=1.0
- ORHD.CA: score=19.51 buy_ready=False sector_rank=15 price=42.97 support=40.28 resistance=43.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=49.0 liquidity=86195968.0 spike=0.65
- ORWE.CA: score=20.52 buy_ready=False sector_rank=6 price=28.08 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=57.35 liquidity=37871932.0 spike=0.72
- PHAR.CA: score=8.56 buy_ready=False sector_rank=21 price=118.41 support=117.01 resistance=141.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=19.74 liquidity=27869232.0 spike=0.19
- PHDC.CA: score=9.51 buy_ready=False sector_rank=15 price=13.28 support=13.65 resistance=15.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=31.85 liquidity=99934792.0 spike=0.58
- PHTV.CA: score=11.26 buy_ready=False sector_rank=11 price=367.7 support=311.27 resistance=382.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=64.27 liquidity=1464315.13 spike=0.76
- POUL.CA: score=18.77 buy_ready=False sector_rank=17 price=38.91 support=37.03 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=47.07 liquidity=9357677.0 spike=0.39
- PRCL.CA: score=14.2 buy_ready=False sector_rank=19 price=32.15 support=30.9 resistance=35.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=45.64 liquidity=18943158.0 spike=1.0
- PRDC.CA: score=7.69 buy_ready=False sector_rank=15 price=7.82 support=7.68 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=23.25 liquidity=8173339.0 spike=0.12
- PRMH.CA: score=-1.8 buy_ready=False sector_rank=11 price=2.72 support=2.66 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3404934.25 spike=0.32
- RACC.CA: score=10.51 buy_ready=False sector_rank=11 price=9.84 support=9.4 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=47.29 liquidity=3719459.0 spike=0.19
- RAKT.CA: score=10.85 buy_ready=False sector_rank=11 price=22.65 support=21.4 resistance=23.02 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=57.94 liquidity=55651.05 spike=0.24
- RAYA.CA: score=14.18 buy_ready=False sector_rank=20 price=7.2 support=6.95 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=24474456.0 spike=0.44
- RMDA.CA: score=16.56 buy_ready=False sector_rank=21 price=6.12 support=5.77 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=11544826.0 spike=0.19
- ROTO.CA: score=2.39 buy_ready=False sector_rank=11 price=41.16 support=35.02 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=21.14 liquidity=2597582.25 spike=0.26
- RREI.CA: score=19.79 buy_ready=False sector_rank=11 price=4.44 support=4.24 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=55.07 liquidity=14395473.0 spike=0.57
- RTVC.CA: score=4.02 buy_ready=False sector_rank=11 price=3.98 support=3.85 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=28.33 liquidity=1225412.13 spike=0.19
- RUBX.CA: score=9.79 buy_ready=False sector_rank=11 price=16.27 support=12.9 resistance=16.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=73134408.0 spike=3.74
- SAUD.CA: score=12.97 buy_ready=False sector_rank=8 price=23.51 support=22.7 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=50.96 liquidity=4637750.0 spike=0.36
- SCEM.CA: score=17.2 buy_ready=False sector_rank=19 price=95.0 support=94.0 resistance=105.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=44.55 liquidity=90380392.0 spike=0.71
- SCFM.CA: score=1.71 buy_ready=False sector_rank=11 price=276.19 support=265.51 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=30.39 liquidity=1917604.0 spike=0.2
- SCTS.CA: score=3.01 buy_ready=False sector_rank=3 price=609.04 support=566.66 resistance=640.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=32.18 liquidity=613292.44 spike=0.19
- SDTI.CA: score=17.79 buy_ready=False sector_rank=11 price=77.76 support=67.0 resistance=76.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=65.18 liquidity=11375497.0 spike=0.55
- SEIG.CA: score=5.27 buy_ready=False sector_rank=11 price=242.86 support=228.13 resistance=274.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=43.16 liquidity=474534.59 spike=0.27
- SIPC.CA: score=19.79 buy_ready=False sector_rank=11 price=5.82 support=4.1 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=65.96 liquidity=12315532.0 spike=0.18
- SKPC.CA: score=20.46 buy_ready=False sector_rank=7 price=18.64 support=17.0 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=63.27 liquidity=76707800.0 spike=0.53
- SMFR.CA: score=1.5 buy_ready=False sector_rank=11 price=241.69 support=236.0 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=27.28 liquidity=1705325.0 spike=0.17
- SNFC.CA: score=20.15 buy_ready=False sector_rank=11 price=11.34 support=10.26 resistance=11.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=65.24 liquidity=17011376.0 spike=1.18
- SPIN.CA: score=4.55 buy_ready=False sector_rank=6 price=17.63 support=17.01 resistance=20.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=28.6 liquidity=1021179.0 spike=0.06
- SPMD.CA: score=4.79 buy_ready=False sector_rank=11 price=0.45 support=0.44 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30837946.0 spike=0.47
- SUGR.CA: score=15.43 buy_ready=False sector_rank=17 price=59.1 support=50.0 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=58.65 liquidity=6016892.0 spike=0.09
- SVCE.CA: score=19.79 buy_ready=False sector_rank=11 price=12.0 support=10.28 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=56.57 liquidity=58630344.0 spike=0.31
- SWDY.CA: score=19.54 buy_ready=False sector_rank=14 price=127.74 support=115.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=43.09 liquidity=16670077.0 spike=0.22
- TALM.CA: score=19.4 buy_ready=False sector_rank=3 price=21.55 support=17.11 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=80.86 liquidity=27317388.0 spike=0.46
- TMGH.CA: score=14.51 buy_ready=False sector_rank=15 price=94.5 support=94.86 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=40.75 liquidity=89098960.0 spike=0.32
- TRTO.CA: score=7.79 buy_ready=False sector_rank=11 price=0.07 support=0.05 resistance=0.08 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=66.1 liquidity=2023.0 spike=0.08
- UEFM.CA: score=5.56 buy_ready=False sector_rank=11 price=509.73 support=440.66 resistance=574.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=48.61 liquidity=768160.81 spike=0.25
- UEGC.CA: score=9.79 buy_ready=False sector_rank=11 price=1.79 support=1.66 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=32.88 liquidity=18318594.0 spike=0.37
- UNIP.CA: score=12.23 buy_ready=False sector_rank=11 price=0.38 support=0.35 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=52.13 liquidity=7434155.0 spike=0.23
- UNIT.CA: score=13.11 buy_ready=False sector_rank=15 price=18.9 support=18.11 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=56.35 liquidity=3600878.25 spike=0.25
- WCDF.CA: score=11.01 buy_ready=False sector_rank=11 price=745.86 support=630.06 resistance=796.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=81.23 liquidity=2213288.0 spike=0.49
- WKOL.CA: score=17.62 buy_ready=False sector_rank=11 price=346.33 support=332.56 resistance=369.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=55.88 liquidity=5823958.5 spike=0.51
- ZEOT.CA: score=21.39 buy_ready=False sector_rank=11 price=13.48 support=13.03 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=35.16 liquidity=18408180.0 spike=2.8
- ZMID.CA: score=19.51 buy_ready=False sector_rank=15 price=9.05 support=7.81 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=62.03 liquidity=83030584.0 spike=0.33

## Backtesting Lite
- BINV.CA: 180d return=70.75%, max drawdown=-17.77%, MA20>MA50 days last20=20, as_of=2026-09-15T21:00:00+00:00
- OIH.CA: 180d return=86.21%, max drawdown=-14.56%, MA20>MA50 days last20=20, as_of=2026-09-15T21:00:00+00:00
- GBCO.CA: 180d return=19.04%, max drawdown=-24.35%, MA20>MA50 days last20=1, as_of=2026-09-15T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- OIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Investment Holding summary=Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- CIRA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Investment and Real Estate Development summary=CIRA Education take over 51% of L’École Française Hurghada; CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion; CIRA Education launches Middle East’s 1st initiative for care economy
  - CIRA Education take over 51% of L’École Française Hurghada: https://english.mubasher.info/news/4488666/CIRA-Education-take-over-51-of-L-%C3%89cole-Fran%C3%A7aise-Hurghada/
  - CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion: https://english.mubasher.info/news/4393636/CIRA-s-majority-shareholder-acquires-37-5-additional-equity-backs-regional-expansion/
  - CIRA Education launches Middle East’s 1st initiative for care economy: https://english.mubasher.info/news/4391766/CIRA-Education-launches-Middle-East-s-1st-initiative-for-care-economy/
- HELI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Heliopolis Housing summary=Evidence rejected for HELI.CA: source text did not clearly match HELI.CA / Heliopolis Housing.
- ZEOT.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Extracted Oil & Derivatives Co. summary=Extracted Oils stock nears record high on strong momentum; Extracted Oils stock witnesses increasing buying power amid current resistance – Analysis; Extracted Oils swings to nearly EGP 14.5m net profits in Q1-25/26
  - Extracted Oils stock nears record high on strong momentum: https://english.mubasher.info/news/4599376/Extracted-Oils-stock-nears-record-high-on-strong-momentum/
  - Extracted Oils stock witnesses increasing buying power amid current resistance – Analysis: https://english.mubasher.info/news/4555925/Extracted-Oils-stock-witnesses-increasing-buying-power-amid-current-resistance-Analysis/
  - Extracted Oils swings to nearly EGP 14.5m net profits in Q1-25/26: https://english.mubasher.info/news/4537956/Extracted-Oils-swings-to-nearly-EGP-14-5m-net-profits-in-Q1-25-26/
- EGCH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Chemical Industries Kima summary=Evidence rejected for EGCH.CA: source text did not clearly match EGCH.CA / Egyptian Chemical Industries Kima.

## Warnings
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
- Evidence rejected for HELI.CA: source text did not clearly match HELI.CA / Heliopolis Housing.
- Evidence for ZEOT.CA matches the company but no source/report date was detected.
- Evidence rejected for EGCH.CA: source text did not clearly match EGCH.CA / Egyptian Chemical Industries Kima.
