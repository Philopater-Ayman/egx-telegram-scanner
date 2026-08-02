# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-08-02T09:56:27.269658+00:00
Generated Cairo: 2026-08-02 12:56
Run timing: target 11:00 Cairo | generated Cairo 2026-08-02 12:56 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-08-02 12:51

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 168/189
- Top sector: Agriculture & Food Production

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, August 02
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 57.89% / above MA50 42.11%
- EGX70 regime: MIXED / above MA20 64.86% / above MA50 75.68%
- Sector breadth: 9.52%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- PHAR.CA: liquidity=340623840.0 spike=4.06 score=11.4
- CCAP.CA: liquidity=295573408.0 spike=0.41 score=19.0
- BIOC.CA: liquidity=273203296.0 spike=3.46 score=11.32
- AFMC.CA: liquidity=215076176.0 spike=2.78 score=9.96
- AMOC.CA: liquidity=196820304.0 spike=2.51 score=8.42

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 bearish and EGX70 mixed with only 9.5% sector breadth keep the scanner in defensive mode, so it holds all tickets; the top‑ranked stocks show accumulation spikes but extended momentum and cooling liquidity, meaning only a watch stance for the next 1‑3 days.

## Top Liquidity Spikes
- CFGH.CA: spike=111.4 liquidity=1921395.08 outlook=BULLISH_WATCH score=70.09 buy_ready=False
- EOSB.CA: spike=7.81 liquidity=446389.14 outlook=CONSTRUCTIVE score=66.09 buy_ready=False
- EGAS.CA: spike=7.59 liquidity=103266352.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ADCI.CA: spike=6.28 liquidity=64052328.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CICH.CA: spike=5.85 liquidity=31981550.0 outlook=BULLISH_WATCH score=78.42 buy_ready=False

## Sector Leaderboard
- #1 Agriculture & Food Production: score=8.53 5d=3.28% 20d=3.81% aboveMA50=100.0%
- #2 Building Materials: score=7.22 5d=-1.38% 20d=9.43% aboveMA50=83.33%
- #3 Textiles: score=7.12 5d=-2.65% 20d=12.23% aboveMA50=75.0%
- #4 Healthcare: score=6.46 5d=-1.33% 20d=3.33% aboveMA50=66.67%
- #5 General / Verified EGX Expansion: score=6.09 5d=-0.34% 20d=8.59% aboveMA50=69.9%
- #6 Industrial Goods & Cables: score=5.45 5d=-2.34% 20d=5.51% aboveMA50=100.0%
- #7 Fintech & Payments: score=5.15 5d=-2.96% 20d=6.82% aboveMA50=50.0%
- #8 Real Estate: score=5.07 5d=-2.7% 20d=9.63% aboveMA50=76.92%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MPCO.CA: BULLISH_WATCH score=94.53 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MCQE.CA: BULLISH_WATCH score=93.22 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- AXPH.CA: BULLISH_WATCH score=93.09 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- EALR.CA: BULLISH_WATCH score=89.09 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support
- IFAP.CA: BULLISH_WATCH score=88.53 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- PRCL.CA: BULLISH_WATCH score=87.22 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ARCC.CA: BULLISH_WATCH score=87.22 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ORWE.CA: BULLISH_WATCH score=87.12 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MOSC.CA: BULLISH_WATCH score=85.09 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- AJWA.CA: BULLISH_WATCH score=85.09 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=10.94 buy_ready=False sector_rank=5 price=305.74 support=279.0 resistance=317.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=96476096.0 spike=3.27
- ABUK.CA: score=19.6 buy_ready=False sector_rank=14 price=74.31 support=67.73 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=59.64 liquidity=73907352.0 spike=0.47
- ACAMD.CA: score=19.4 buy_ready=False sector_rank=5 price=2.33 support=2.21 resistance=2.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=14795565.0 spike=0.2
- ACGC.CA: score=18.75 buy_ready=False sector_rank=3 price=10.65 support=9.15 resistance=11.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=68.12 liquidity=6349411.5 spike=0.21
- ADCI.CA: score=11.4 buy_ready=False sector_rank=5 price=288.47 support=256.0 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=64052328.0 spike=6.28
- ADIB.CA: score=19.8 buy_ready=False sector_rank=10 price=53.11 support=46.0 resistance=52.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=79.01 liquidity=32137416.0 spike=0.23
- ADPC.CA: score=18.76 buy_ready=False sector_rank=5 price=3.86 support=3.45 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=53.45 liquidity=5355730.5 spike=0.15
- AFDI.CA: score=21.4 buy_ready=False sector_rank=5 price=53.0 support=43.77 resistance=52.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=71.27 liquidity=10347987.0 spike=0.58
- AFMC.CA: score=9.96 buy_ready=False sector_rank=5 price=215.0 support=184.78 resistance=221.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=215076176.0 spike=2.78
- AJWA.CA: score=26.2 buy_ready=False sector_rank=5 price=191.12 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=30 July 01:28 PM market time freshness=DELAYED_CURRENT RSI=63.35 liquidity=75489496.0 spike=2.4
- ALCN.CA: score=20.64 buy_ready=False sector_rank=13 price=30.0 support=28.2 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=60.92 liquidity=19598684.0 spike=0.87
- ALUM.CA: score=10.96 buy_ready=False sector_rank=5 price=23.22 support=21.1 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=49.17 liquidity=562320.0 spike=0.09
- AMER.CA: score=18.03 buy_ready=False sector_rank=8 price=4.52 support=2.4 resistance=4.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=82.38 liquidity=17454502.0 spike=0.15
- AMES.CA: score=21.4 buy_ready=False sector_rank=5 price=123.07 support=57.5 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=65.57 liquidity=15634503.0 spike=0.15
- AMIA.CA: score=11.1 buy_ready=False sector_rank=5 price=11.45 support=8.62 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=75.38 liquidity=2695055.75 spike=0.18
- AMOC.CA: score=8.42 buy_ready=False sector_rank=15 price=9.54 support=9.16 resistance=9.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=196820304.0 spike=2.51
- APSW.CA: score=8.21 buy_ready=False sector_rank=5 price=8.68 support=8.1 resistance=9.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=56.12 liquidity=811305.31 spike=0.53
- ARAB.CA: score=19.03 buy_ready=False sector_rank=8 price=0.24 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=55.95 liquidity=27771432.0 spike=0.2
- ARCC.CA: score=22.69 buy_ready=False sector_rank=2 price=56.27 support=54.2 resistance=58.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=50.72 liquidity=7292487.5 spike=0.26
- AREH.CA: score=5.22 buy_ready=False sector_rank=5 price=1.43 support=1.38 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=28.0 liquidity=3821081.0 spike=0.14
- ARVA.CA: score=8.4 buy_ready=False sector_rank=5 price=12.35 support=10.5 resistance=12.6 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=81.59 liquidity=0.0 spike=0.0
- ASCM.CA: score=19.4 buy_ready=False sector_rank=5 price=64.62 support=57.25 resistance=66.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=66.08 liquidity=20882920.0 spike=0.38
- ASPI.CA: score=18.4 buy_ready=False sector_rank=5 price=0.42 support=0.31 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=75.86 liquidity=16173995.0 spike=0.41
- ATLC.CA: score=25.77 buy_ready=False sector_rank=11 price=5.38 support=5.0 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=48.33 liquidity=36129492.0 spike=5.36
- ATQA.CA: score=22.6 buy_ready=False sector_rank=14 price=9.86 support=9.43 resistance=10.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=59.2 liquidity=11553681.0 spike=0.29
- AXPH.CA: score=18.71 buy_ready=False sector_rank=5 price=1246.2 support=1090.02 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=61.67 liquidity=6225311.0 spike=1.54
- BINV.CA: score=9.7 buy_ready=False sector_rank=9 price=47.55 support=45.97 resistance=51.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=46.06 liquidity=699956.44 spike=0.1
- BIOC.CA: score=11.32 buy_ready=False sector_rank=5 price=285.54 support=241.15 resistance=287.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=273203296.0 spike=3.46
- BTFH.CA: score=21.77 buy_ready=False sector_rank=11 price=3.08 support=2.91 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=68467280.0 spike=0.31
- CAED.CA: score=18.4 buy_ready=False sector_rank=5 price=128.02 support=71.0 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=75.25 liquidity=18133838.0 spike=0.26
- CANA.CA: score=16.37 buy_ready=False sector_rank=10 price=38.12 support=35.2 resistance=39.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=55.24 liquidity=3571609.5 spike=0.21
- CCAP.CA: score=19.0 buy_ready=False sector_rank=9 price=5.28 support=4.76 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=48.04 liquidity=295573408.0 spike=0.41
- CCRS.CA: score=17.82 buy_ready=False sector_rank=5 price=2.59 support=2.26 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=64.38 liquidity=6418936.0 spike=0.35
- CEFM.CA: score=6.62 buy_ready=False sector_rank=5 price=142.89 support=138.1 resistance=145.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28967056.0 spike=1.11
- CERA.CA: score=12.39 buy_ready=False sector_rank=5 price=1.29 support=1.21 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=2991782.0 spike=0.12
- CFGH.CA: score=14.32 buy_ready=False sector_rank=5 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=30 July 12:18 PM market time freshness=DELAYED_CURRENT RSI=52.63 liquidity=1921395.08 spike=111.4
- CICH.CA: score=27.77 buy_ready=False sector_rank=11 price=12.59 support=11.6 resistance=12.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=31981550.0 spike=5.85
- CIEB.CA: score=11.59 buy_ready=False sector_rank=10 price=24.12 support=23.55 resistance=24.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=38.99 liquidity=2794213.75 spike=0.3
- CIRA.CA: score=20.64 buy_ready=False sector_rank=12 price=36.5 support=28.04 resistance=36.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=74.85 liquidity=39473008.0 spike=0.71
- CLHO.CA: score=21.78 buy_ready=False sector_rank=4 price=17.38 support=15.98 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=54.66 liquidity=50831004.0 spike=1.19
- CNFN.CA: score=12.85 buy_ready=False sector_rank=11 price=4.79 support=4.68 resistance=5.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=44.0 liquidity=4085780.0 spike=0.2
- COMI.CA: score=20.8 buy_ready=False sector_rank=10 price=141.74 support=127.25 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=67.31 liquidity=66827272.0 spike=0.16
- COPR.CA: score=21.4 buy_ready=False sector_rank=5 price=0.42 support=0.35 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=70.19 liquidity=10963610.0 spike=0.36
- COSG.CA: score=19.21 buy_ready=False sector_rank=5 price=1.65 support=1.5 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=9809880.0 spike=0.22
- CPCI.CA: score=20.58 buy_ready=False sector_rank=5 price=482.08 support=393.0 resistance=512.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=70.5 liquidity=17763062.0 spike=1.59
- CSAG.CA: score=14.27 buy_ready=False sector_rank=13 price=32.28 support=31.35 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=41.21 liquidity=5629179.5 spike=0.4
- DAPH.CA: score=22.04 buy_ready=False sector_rank=5 price=99.03 support=81.0 resistance=99.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=72.04 liquidity=24890706.0 spike=1.32
- DEIN.CA: score=-3.6 buy_ready=False sector_rank=5 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=8.07 buy_ready=False sector_rank=19 price=26.4 support=26.35 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:28 AM market time freshness=DELAYED_CURRENT RSI=42.28 liquidity=698941.06 spike=0.22
- DSCW.CA: score=18.4 buy_ready=False sector_rank=5 price=1.97 support=1.71 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=77.42 liquidity=22026954.0 spike=0.39
- DTPP.CA: score=21.4 buy_ready=False sector_rank=5 price=248.21 support=183.0 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=66.53 liquidity=24143092.0 spike=0.3
- EALR.CA: score=26.48 buy_ready=False sector_rank=5 price=409.0 support=338.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=66.95 liquidity=68860576.0 spike=2.54
- EASB.CA: score=12.68 buy_ready=False sector_rank=5 price=7.16 support=6.88 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=53.1 liquidity=3283532.25 spike=0.25
- EAST.CA: score=13.37 buy_ready=False sector_rank=19 price=36.8 support=36.01 resistance=37.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=44.1 liquidity=18630512.0 spike=0.23
- EBSC.CA: score=10.49 buy_ready=False sector_rank=5 price=1.9 support=1.74 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=1089495.88 spike=0.13
- ECAP.CA: score=13.68 buy_ready=False sector_rank=5 price=33.35 support=32.12 resistance=34.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=54.95 liquidity=2279799.75 spike=0.39
- EDFM.CA: score=14.32 buy_ready=False sector_rank=5 price=389.18 support=310.2 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=72.34 liquidity=2915671.0 spike=0.56
- EEII.CA: score=6.05 buy_ready=False sector_rank=5 price=2.65 support=2.47 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=30.61 liquidity=1650527.13 spike=0.07
- EFIC.CA: score=14.41 buy_ready=False sector_rank=14 price=201.35 support=180.07 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=66.48 liquidity=4812908.0 spike=0.27
- EFID.CA: score=8.58 buy_ready=False sector_rank=19 price=27.14 support=26.64 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=34.41 liquidity=9208206.0 spike=0.2
- EFIH.CA: score=23.06 buy_ready=False sector_rank=7 price=22.71 support=20.3 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=55.13 liquidity=25953202.0 spike=0.4
- EGAL.CA: score=19.6 buy_ready=False sector_rank=14 price=300.63 support=283.03 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=54.07 liquidity=17229646.0 spike=0.41
- EGAS.CA: score=10.4 buy_ready=False sector_rank=15 price=59.61 support=52.8 resistance=62.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=103266352.0 spike=7.59
- EGBE.CA: score=7.82 buy_ready=False sector_rank=10 price=0.47 support=-0.34 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=96.7 liquidity=25613.68 spike=0.37
- EGCH.CA: score=19.12 buy_ready=False sector_rank=14 price=13.3 support=12.24 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=47.06 liquidity=110086832.0 spike=1.76
- EGSA.CA: score=-0.51 buy_ready=False sector_rank=18 price=8.81 support=8.67 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=27.66 liquidity=18708.99 spike=1.01
- EGTS.CA: score=9.29 buy_ready=False sector_rank=8 price=17.36 support=17.15 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=34.58 liquidity=8260011.0 spike=0.18
- EHDR.CA: score=18.72 buy_ready=False sector_rank=5 price=2.78 support=2.49 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=7322704.0 spike=0.17
- EKHO.CA: score=4.4 buy_ready=False sector_rank=15 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=18.18 buy_ready=False sector_rank=6 price=2.16 support=2.08 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=55.0 liquidity=11236411.0 spike=0.16
- ELKA.CA: score=19.4 buy_ready=False sector_rank=5 price=1.73 support=1.35 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=40518996.0 spike=0.52
- ELNA.CA: score=9.22 buy_ready=False sector_rank=5 price=37.54 support=37.0 resistance=40.5 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=38.76 liquidity=1457190.22 spike=2.18
- ELSH.CA: score=19.4 buy_ready=False sector_rank=5 price=13.7 support=11.53 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=42.8 liquidity=25407716.0 spike=0.17
- ELWA.CA: score=1.96 buy_ready=False sector_rank=5 price=1.77 support=1.74 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=26.19 liquidity=563982.06 spike=0.37
- EMFD.CA: score=11.03 buy_ready=False sector_rank=8 price=11.29 support=11.08 resistance=12.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=26.62 liquidity=24068686.0 spike=0.41
- ENGC.CA: score=21.4 buy_ready=False sector_rank=5 price=41.48 support=36.31 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=59.04 liquidity=13289218.0 spike=0.51
- EOSB.CA: score=20.85 buy_ready=False sector_rank=5 price=1.55 support=1.5 resistance=1.55 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=446389.14 spike=7.81
- EPCO.CA: score=20.56 buy_ready=False sector_rank=5 price=10.96 support=8.57 resistance=11.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=70.67 liquidity=9158374.0 spike=0.31
- EPPK.CA: score=11.7 buy_ready=False sector_rank=5 price=14.96 support=13.52 resistance=15.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=61.16 liquidity=300958.09 spike=0.29
- ETEL.CA: score=4.45 buy_ready=False sector_rank=18 price=109.01 support=104.05 resistance=109.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=55545912.0 spike=0.63
- ETRS.CA: score=21.4 buy_ready=False sector_rank=5 price=10.6 support=10.1 resistance=10.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=49.99 liquidity=21113252.0 spike=0.52
- EXPA.CA: score=19.8 buy_ready=False sector_rank=10 price=20.12 support=18.18 resistance=20.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=83.57 liquidity=16011308.0 spike=0.48
- FAIT.CA: score=8.1 buy_ready=False sector_rank=10 price=37.01 support=36.1 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=42.94 liquidity=2303585.75 spike=0.91
- FAITA.CA: score=0.81 buy_ready=False sector_rank=10 price=0.97 support=0.96 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=28.33 liquidity=13462.06 spike=0.32
- FERC.CA: score=13.79 buy_ready=False sector_rank=14 price=76.97 support=73.45 resistance=85.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=49.92 liquidity=4192750.25 spike=0.35
- FWRY.CA: score=18.06 buy_ready=False sector_rank=7 price=19.08 support=18.28 resistance=19.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=38.43 liquidity=28707548.0 spike=0.23
- GBCO.CA: score=17.83 buy_ready=False sector_rank=16 price=30.67 support=29.53 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=42.99 liquidity=9590071.0 spike=0.15
- GDWA.CA: score=18.4 buy_ready=False sector_rank=5 price=0.81 support=0.76 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=56.77 liquidity=21310240.0 spike=0.2
- GGCC.CA: score=11.08 buy_ready=False sector_rank=5 price=0.83 support=0.48 resistance=0.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=76.99 liquidity=2675648.25 spike=0.07
- GIHD.CA: score=23.4 buy_ready=False sector_rank=5 price=57.91 support=41.71 resistance=65.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=59.67 liquidity=12077734.0 spike=0.23
- GMCI.CA: score=9.74 buy_ready=False sector_rank=5 price=1.97 support=1.75 resistance=2.26 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=40.68 liquidity=336481.91 spike=0.27
- GRCA.CA: score=18.43 buy_ready=False sector_rank=5 price=60.19 support=48.0 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=70.56 liquidity=7027306.5 spike=0.42
- GSSC.CA: score=21.4 buy_ready=False sector_rank=5 price=285.36 support=241.32 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=71.0 liquidity=11556838.0 spike=0.81
- GTWL.CA: score=16.4 buy_ready=False sector_rank=5 price=101.83 support=82.2 resistance=118.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=33.45 liquidity=23388864.0 spike=0.18
- HDBK.CA: score=18.8 buy_ready=False sector_rank=10 price=84.2 support=76.9 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=63.36 liquidity=30521960.0 spike=0.7
- HELI.CA: score=21.03 buy_ready=False sector_rank=8 price=8.36 support=6.41 resistance=8.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=73.26 liquidity=46980548.0 spike=0.22
- HRHO.CA: score=14.77 buy_ready=False sector_rank=11 price=26.6 support=25.95 resistance=27.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=38.46 liquidity=25541200.0 spike=0.3
- ICID.CA: score=20.64 buy_ready=False sector_rank=5 price=8.0 support=6.55 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=54.31 liquidity=11828169.0 spike=1.62
- IDRE.CA: score=17.88 buy_ready=False sector_rank=5 price=48.01 support=42.22 resistance=52.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=53.68 liquidity=4484009.0 spike=0.16
- IFAP.CA: score=19.48 buy_ready=False sector_rank=1 price=19.6 support=18.96 resistance=20.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=47.59 liquidity=3083341.75 spike=0.31
- INFI.CA: score=8.32 buy_ready=False sector_rank=5 price=112.84 support=108.1 resistance=114.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35133992.0 spike=1.96
- IRON.CA: score=3.75 buy_ready=False sector_rank=14 price=30.53 support=30.14 resistance=32.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=2.83 liquidity=4145685.75 spike=0.66
- ISMA.CA: score=15.19 buy_ready=False sector_rank=5 price=30.57 support=26.54 resistance=32.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=69.1 liquidity=3792392.25 spike=0.15
- ISMQ.CA: score=18.6 buy_ready=False sector_rank=14 price=9.16 support=8.96 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=35.35 liquidity=19946770.0 spike=0.21
- ISPH.CA: score=18.42 buy_ready=False sector_rank=4 price=11.67 support=11.2 resistance=11.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=38.78 liquidity=49033032.0 spike=1.01
- JUFO.CA: score=9.03 buy_ready=False sector_rank=19 price=29.08 support=28.48 resistance=31.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=19.95 liquidity=9666158.0 spike=0.37
- KABO.CA: score=22.36 buy_ready=False sector_rank=3 price=8.02 support=6.26 resistance=8.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=64.41 liquidity=9960255.0 spike=0.2
- KWIN.CA: score=18.4 buy_ready=False sector_rank=5 price=98.67 support=66.1 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=83.46 liquidity=27048498.0 spike=0.51
- KZPC.CA: score=17.07 buy_ready=False sector_rank=5 price=8.7 support=8.26 resistance=8.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=54.41 liquidity=6987231.0 spike=1.34
- LCSW.CA: score=25.4 buy_ready=False sector_rank=2 price=35.01 support=28.38 resistance=37.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=61.64 liquidity=16568186.0 spike=0.25
- LUTS.CA: score=6.4 buy_ready=False sector_rank=5 price=0.58 support=0.55 resistance=0.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17917130.0 spike=0.57
- MAAL.CA: score=18.3 buy_ready=False sector_rank=5 price=8.94 support=7.13 resistance=8.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=74.47 liquidity=8898349.0 spike=0.54
- MASR.CA: score=19.4 buy_ready=False sector_rank=5 price=7.91 support=7.24 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=59.26 liquidity=27219080.0 spike=0.33
- MBSC.CA: score=17.09 buy_ready=False sector_rank=2 price=243.3 support=231.51 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=44.96 liquidity=4688242.5 spike=0.26
- MCQE.CA: score=23.59 buy_ready=False sector_rank=2 price=184.59 support=170.0 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=55.32 liquidity=8189587.0 spike=0.45
- MCRO.CA: score=18.4 buy_ready=False sector_rank=5 price=1.49 support=1.2 resistance=1.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=77.27 liquidity=95621168.0 spike=0.7
- MENA.CA: score=9.5 buy_ready=False sector_rank=8 price=6.93 support=6.74 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=38.67 liquidity=476321.38 spike=0.06
- MEPA.CA: score=23.4 buy_ready=False sector_rank=5 price=1.88 support=1.56 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=63.16 liquidity=27217606.0 spike=0.54
- MFPC.CA: score=19.6 buy_ready=False sector_rank=14 price=37.47 support=35.19 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=47.34 liquidity=65946404.0 spike=0.72
- MFSC.CA: score=7.65 buy_ready=False sector_rank=5 price=51.14 support=46.48 resistance=51.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9833467.0 spike=1.71
- MHOT.CA: score=9.22 buy_ready=False sector_rank=20 price=16.52 support=16.2 resistance=18.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=43.09 liquidity=4547463.5 spike=0.4
- MICH.CA: score=6.4 buy_ready=False sector_rank=5 price=42.25 support=40.5 resistance=42.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13247088.0 spike=0.79
- MILS.CA: score=6.4 buy_ready=False sector_rank=5 price=201.41 support=192.5 resistance=209.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=44157372.0 spike=0.88
- MIPH.CA: score=16.23 buy_ready=False sector_rank=4 price=765.3 support=650.0 resistance=780.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=64.9 liquidity=4330445.0 spike=1.25
- MOED.CA: score=15.4 buy_ready=False sector_rank=5 price=0.68 support=0.68 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=40.87 liquidity=23570142.0 spike=0.92
- MOIL.CA: score=9.5 buy_ready=False sector_rank=15 price=0.67 support=0.47 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=92.15 liquidity=105515.2 spike=0.14
- MOIN.CA: score=15.54 buy_ready=False sector_rank=5 price=24.58 support=23.03 resistance=24.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=51.08 liquidity=1496474.25 spike=2.82
- MOSC.CA: score=27.14 buy_ready=False sector_rank=5 price=299.24 support=260.01 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=62.23 liquidity=35048152.0 spike=2.87
- MPCI.CA: score=18.4 buy_ready=False sector_rank=5 price=294.07 support=237.12 resistance=298.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=84.45 liquidity=46883596.0 spike=0.48
- MPCO.CA: score=26.4 buy_ready=False sector_rank=1 price=1.95 support=1.77 resistance=2.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=53.66 liquidity=24382762.0 spike=0.29
- MPRC.CA: score=16.95 buy_ready=False sector_rank=5 price=44.75 support=37.51 resistance=47.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=62.11 liquidity=5545837.0 spike=0.18
- MTIE.CA: score=20.05 buy_ready=False sector_rank=16 price=9.57 support=9.09 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=9813983.0 spike=0.4
- NAHO.CA: score=5.41 buy_ready=False sector_rank=5 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=9132.01 spike=0.36
- NCCW.CA: score=21.4 buy_ready=False sector_rank=5 price=7.07 support=6.01 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=70.49 liquidity=11510733.0 spike=0.4
- NEDA.CA: score=6.72 buy_ready=False sector_rank=5 price=2.74 support=2.7 resistance=3.02 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=319884.04 spike=0.41
- NHPS.CA: score=21.4 buy_ready=False sector_rank=5 price=84.6 support=67.0 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=64.68 liquidity=13745312.0 spike=0.16
- NINH.CA: score=6.76 buy_ready=False sector_rank=5 price=23.02 support=21.65 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=50870612.0 spike=1.18
- NIPH.CA: score=18.4 buy_ready=False sector_rank=4 price=233.03 support=165.0 resistance=242.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=77.86 liquidity=97554760.0 spike=0.6
- OBRI.CA: score=10.4 buy_ready=False sector_rank=5 price=32.65 support=32.2 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=24.17 liquidity=18634378.0 spike=0.43
- OCDI.CA: score=21.45 buy_ready=False sector_rank=8 price=28.8 support=24.46 resistance=29.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=60.81 liquidity=120323344.0 spike=1.21
- OCPH.CA: score=18.4 buy_ready=False sector_rank=5 price=483.02 support=350.6 resistance=496.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=82.68 liquidity=18991332.0 spike=0.75
- ODIN.CA: score=8.92 buy_ready=False sector_rank=5 price=2.94 support=2.84 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=45132240.0 spike=2.26
- OFH.CA: score=21.4 buy_ready=False sector_rank=5 price=0.72 support=0.59 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=66.49 liquidity=21185046.0 spike=0.31
- OIH.CA: score=23.0 buy_ready=False sector_rank=9 price=1.48 support=1.4 resistance=1.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=28806660.0 spike=0.38
- OLFI.CA: score=19.37 buy_ready=False sector_rank=19 price=23.09 support=21.91 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=47.3 liquidity=14094548.0 spike=0.41
- ORAS.CA: score=4.6 buy_ready=False sector_rank=17 price=713.61 support=708.0 resistance=714.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39869464.0 spike=1.0
- ORHD.CA: score=21.03 buy_ready=False sector_rank=8 price=39.64 support=37.76 resistance=40.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=51.57 liquidity=22709996.0 spike=0.15
- ORWE.CA: score=19.4 buy_ready=False sector_rank=3 price=22.92 support=22.2 resistance=23.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=45.37 liquidity=14248040.0 spike=0.57
- PHAR.CA: score=11.4 buy_ready=False sector_rank=4 price=124.8 support=104.2 resistance=124.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=340623840.0 spike=4.06
- PHDC.CA: score=16.03 buy_ready=False sector_rank=8 price=14.45 support=14.32 resistance=15.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=41.03 liquidity=33272062.0 spike=0.14
- PHTV.CA: score=9.74 buy_ready=False sector_rank=5 price=317.89 support=260.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:28 AM market time freshness=DELAYED_CURRENT RSI=73.12 liquidity=337741.06 spike=0.07
- POUL.CA: score=4.34 buy_ready=False sector_rank=19 price=37.81 support=36.5 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=32.88 liquidity=4968614.0 spike=0.15
- PRCL.CA: score=23.4 buy_ready=False sector_rank=2 price=36.22 support=30.83 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=42.2 liquidity=11763851.0 spike=0.25
- PRDC.CA: score=21.03 buy_ready=False sector_rank=8 price=9.41 support=7.4 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=55.01 liquidity=36093508.0 spike=0.3
- PRMH.CA: score=12.32 buy_ready=False sector_rank=5 price=2.64 support=2.48 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=2916320.75 spike=0.17
- RACC.CA: score=19.4 buy_ready=False sector_rank=5 price=10.03 support=9.65 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=49.48 liquidity=12249065.0 spike=0.54
- RAKT.CA: score=12.63 buy_ready=False sector_rank=5 price=22.53 support=21.25 resistance=23.7 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=53.46 liquidity=693563.54 spike=2.27
- RAYA.CA: score=13.34 buy_ready=False sector_rank=21 price=7.5 support=7.3 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=37.37 liquidity=13369899.0 spike=0.1
- RMDA.CA: score=26.4 buy_ready=False sector_rank=4 price=5.47 support=4.91 resistance=5.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=71.64 liquidity=152482096.0 spike=5.03
- ROTO.CA: score=21.4 buy_ready=False sector_rank=5 price=44.03 support=40.5 resistance=45.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=51.49 liquidity=10192515.0 spike=0.52
- RREI.CA: score=21.4 buy_ready=False sector_rank=5 price=4.7 support=3.45 resistance=4.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=71.0 liquidity=28114646.0 spike=0.44
- RTVC.CA: score=8.57 buy_ready=False sector_rank=5 price=3.79 support=3.7 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=49.15 liquidity=2168756.25 spike=0.45
- RUBX.CA: score=16.01 buy_ready=False sector_rank=5 price=12.56 support=11.22 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=42.57 liquidity=6612900.0 spike=0.1
- SAUD.CA: score=18.48 buy_ready=False sector_rank=10 price=21.75 support=21.01 resistance=22.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=54.51 liquidity=13339527.0 spike=1.34
- SCEM.CA: score=20.4 buy_ready=False sector_rank=2 price=80.48 support=61.28 resistance=87.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=75.59 liquidity=77713560.0 spike=1.0
- SCFM.CA: score=23.4 buy_ready=False sector_rank=5 price=289.77 support=237.08 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=60.42 liquidity=17741372.0 spike=0.66
- SCTS.CA: score=10.22 buy_ready=False sector_rank=12 price=610.66 support=599.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=47.65 liquidity=1583041.88 spike=0.26
- SDTI.CA: score=14.27 buy_ready=False sector_rank=5 price=58.58 support=46.0 resistance=60.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=83.8 liquidity=5872182.5 spike=0.32
- SEIG.CA: score=20.37 buy_ready=False sector_rank=5 price=259.22 support=186.05 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=57.13 liquidity=8970938.0 spike=0.33
- SIPC.CA: score=11.4 buy_ready=False sector_rank=5 price=4.46 support=3.99 resistance=4.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=131937080.0 spike=5.19
- SKPC.CA: score=16.6 buy_ready=False sector_rank=14 price=15.9 support=14.8 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=43.31 liquidity=17470562.0 spike=0.46
- SMFR.CA: score=21.4 buy_ready=False sector_rank=5 price=240.21 support=193.0 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=66.77 liquidity=14957594.0 spike=0.69
- SNFC.CA: score=10.02 buy_ready=False sector_rank=5 price=11.0 support=11.01 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=12.03 liquidity=8616722.0 spike=0.76
- SPIN.CA: score=22.4 buy_ready=False sector_rank=3 price=15.95 support=14.0 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=68.35 liquidity=11167602.0 spike=0.43
- SPMD.CA: score=21.4 buy_ready=False sector_rank=5 price=0.47 support=0.43 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=52.11 liquidity=22467996.0 spike=0.81
- SUGR.CA: score=7.83 buy_ready=False sector_rank=19 price=46.63 support=46.47 resistance=47.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=42.02 liquidity=2464301.75 spike=0.46
- SVCE.CA: score=9.85 buy_ready=False sector_rank=5 price=9.18 support=8.96 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=28.05 liquidity=8452402.0 spike=0.16
- SWDY.CA: score=21.18 buy_ready=False sector_rank=6 price=94.3 support=86.1 resistance=97.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=65.15 liquidity=19343360.0 spike=0.89
- TALM.CA: score=6.72 buy_ready=False sector_rank=12 price=18.39 support=18.3 resistance=18.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=49569216.0 spike=1.54
- TMGH.CA: score=19.03 buy_ready=False sector_rank=8 price=97.48 support=94.1 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=50.6 liquidity=50702392.0 spike=0.14
- TRTO.CA: score=10.02 buy_ready=False sector_rank=5 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=2951.44 spike=2.31
- UEFM.CA: score=14.57 buy_ready=False sector_rank=5 price=544.44 support=473.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=58.21 liquidity=1174449.38 spike=0.22
- UEGC.CA: score=21.4 buy_ready=False sector_rank=5 price=2.32 support=1.41 resistance=2.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=70.87 liquidity=11060703.0 spike=0.2
- UNIP.CA: score=17.82 buy_ready=False sector_rank=5 price=0.38 support=0.32 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=64.0 liquidity=4422354.0 spike=0.16
- UNIT.CA: score=13.11 buy_ready=False sector_rank=8 price=18.22 support=12.8 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=21.87 liquidity=7085904.5 spike=0.24
- WCDF.CA: score=14.61 buy_ready=False sector_rank=5 price=585.06 support=504.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=67.79 liquidity=3210918.5 spike=0.98
- WKOL.CA: score=11.4 buy_ready=False sector_rank=5 price=354.1 support=332.5 resistance=363.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=63539456.0 spike=3.66
- ZEOT.CA: score=21.4 buy_ready=False sector_rank=5 price=12.6 support=10.81 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=72.13 liquidity=14961425.0 spike=0.48
- ZMID.CA: score=21.03 buy_ready=False sector_rank=8 price=7.25 support=6.47 resistance=7.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=57.92 liquidity=60706168.0 spike=0.23

## Backtesting Lite
- CICH.CA: 180d return=50.25%, max drawdown=-14.78%, MA20>MA50 days last20=0, as_of=2026-07-29T21:00:00+00:00
- MOSC.CA: 180d return=50.34%, max drawdown=-24.01%, MA20>MA50 days last20=3, as_of=2026-07-29T21:00:00+00:00
- EALR.CA: 180d return=20.65%, max drawdown=-26.75%, MA20>MA50 days last20=5, as_of=2026-07-29T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CICH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=CI Capital Holding summary=Evidence rejected for CICH.CA: source text did not clearly match CICH.CA / CI Capital Holding.
- MOSC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Oils & Soap summary=Misr Oils and Soap not to pay dividends for FY20/21; Misr Oils and Soap&#39;s profit plunges 78% in FY20/21; Misr Oils and Soap swings to loss in 10 months
  - Misr Oils and Soap not to pay dividends for FY20/21: https://english.mubasher.info/news/3856493/Misr-Oils-and-Soap-not-to-pay-dividends-for-FY20-21/
  - Misr Oils and Soap&#39;s profit plunges 78% in FY20/21: https://english.mubasher.info/news/3851183/Misr-Oils-and-Soap-s-profit-plunges-78-in-FY20-21/
  - Misr Oils and Soap swings to loss in 10 months: https://english.mubasher.info/news/3811105/Misr-Oils-and-Soap-swings-to-loss-in-10-months/
- EALR.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Company For Land Reclamation summary=El Arabia for Land Reclamation targets EGP 2.5m profits in FY22/23; El Arabia for Land Reclamation starts work on Bahariya Oasis project; El Arabia for Land Reclamation H1 losses down 16%
  - El Arabia for Land Reclamation targets EGP 2.5m profits in FY22/23: https://english.mubasher.info/news/3938373/El-Arabia-for-Land-Reclamation-targets-EGP-2-5m-profits-in-FY22-23/
  - El Arabia for Land Reclamation starts work on Bahariya Oasis project: https://english.mubasher.info/news/3493569/El-Arabia-for-Land-Reclamation-starts-work-on-Bahariya-Oasis-project/
  - El Arabia for Land Reclamation H1 losses down 16%: https://english.mubasher.info/news/3058199/El-Arabia-for-Land-Reclamation-H1-losses-down-16-/
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=578 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- RMDA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tenth of Ramadan Pharmaceutical Industries summary=Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- AJWA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=AJWA For Food Industries Co. Egypt summary=Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture; AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3; Ajwa Egypt turns to losses in 9M
  - Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture: https://english.mubasher.info/news/4532004/Ajwa-Egypt-s-board-approves-capital-increase-to-EGP-500m-joins-new-food-venture/
  - AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3: https://english.mubasher.info/news/4527545/AJWA-Egypt-s-standalone-net-profits-retreat-to-EGP-14m-in-9M-25-amid-shift-to-profitability-in-Q3/
  - Ajwa Egypt turns to losses in 9M: https://english.mubasher.info/news/3883210/Ajwa-Egypt-turns-to-losses-in-9M/
- ATLC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Al Tawfeek Leasing summary=Evidence rejected for ATLC.CA: source text did not clearly match ATLC.CA / Al Tawfeek Leasing.
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.

## Warnings
- Evidence rejected for CICH.CA: source text did not clearly match CICH.CA / CI Capital Holding.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for MOSC.CA matches the company but no source/report date was detected.
- Evidence for EALR.CA matches the company but no source/report date was detected.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- Evidence for AJWA.CA matches the company but no source/report date was detected.
- Evidence rejected for ATLC.CA: source text did not clearly match ATLC.CA / Al Tawfeek Leasing.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
