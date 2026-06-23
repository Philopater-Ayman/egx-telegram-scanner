# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-06-23T11:02:25.288639+00:00
Generated Cairo: 2026-06-23 14:02
Run timing: target 11:00 Cairo | generated Cairo 2026-06-23 14:02 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-06-23 13:58

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 170/190
- Top sector: Healthcare

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, June 23
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 35.0% / above MA50 45.0%
- EGX70 regime: BEARISH / above MA20 41.18% / above MA50 67.65%
- Sector breadth: 38.1%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=446369440.0 spike=0.57 score=18.42
- COMI.CA: liquidity=382037152.0 spike=0.65 score=21.57
- CNFN.CA: liquidity=360697184.0 spike=22.0 score=10.86
- ASCM.CA: liquidity=340481920.0 spike=5.1 score=10.66
- ORAS.CA: liquidity=268386560.0 spike=1.0 score=4.6

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The local scanner stays on HOLD because both EGX30 and EGX70 are in a bearish regime with weak breadth (38.1%). Defensive risk mode blocks new buys until market support improves. The top‑ranked tickets show bullish watch signals and solid liquidity spikes, but sector breadth is low and resistance levels are near, so they remain watch‑only for the next 1‑3 days.
- EGX30/EGX70 trends bearish; above‑MA20/MA50 percentages under 45% signal weak market support.
- Healthcare leads sector breadth, yet stocks like CLHO.CA and ISPH.CA sit near resistance with mixed liquidity.
- Real Estate (OCDI.CA, ORHD.CA) shows accumulation spikes but sector breadth remains low, limiting upside.
- Defensive risk mode (no new BUY) reflects uncertainty; monitor support levels and liquidity spikes for any regime shift.

## Top Liquidity Spikes
- CNFN.CA: spike=22.0 liquidity=360697184.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GIHD.CA: spike=17.8 liquidity=56344852.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DOMT.CA: spike=10.03 liquidity=21232356.0 outlook=BULLISH_WATCH score=87.61 buy_ready=False
- MPRC.CA: spike=6.21 liquidity=133214920.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ASCM.CA: spike=5.1 liquidity=340481920.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Healthcare: score=7.89 5d=3.13% 20d=3.89% aboveMA50=100.0%
- #2 Real Estate: score=6.24 5d=1.63% 20d=5.26% aboveMA50=84.62%
- #3 Industrial Goods & Cables: score=5.99 5d=1.46% 20d=1.89% aboveMA50=50.0%
- #4 Technology & Distribution: score=5.76 5d=6.14% 20d=-2.88% aboveMA50=100.0%
- #5 Agriculture & Food Production: score=5.35 5d=-1.64% 20d=8.88% aboveMA50=50.0%
- #6 Energy & Petrochemicals: score=4.96 5d=0.17% 20d=2.29% aboveMA50=75.0%
- #7 Education: score=4.76 5d=-0.06% 20d=5.23% aboveMA50=66.67%
- #8 Telecommunications: score=4.72 5d=0.24% 20d=-3.06% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- OCDI.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- CLHO.CA: BULLISH_WATCH score=98.89 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- NIPH.CA: BULLISH_WATCH score=98.89 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- ORHD.CA: BULLISH_WATCH score=94.24 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- PHDC.CA: BULLISH_WATCH score=92.24 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MICH.CA: BULLISH_WATCH score=92.14 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- CIRA.CA: BULLISH_WATCH score=91.76 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- ZMID.CA: BULLISH_WATCH score=91.24 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- PHAR.CA: BULLISH_WATCH score=89.89 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; close to resistance
- MASR.CA: BULLISH_WATCH score=88.14 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=12.1 buy_ready=False sector_rank=10 price=207.1 support=199.25 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=44.97 liquidity=1441827.63 spike=0.23
- ABUK.CA: score=9.26 buy_ready=False sector_rank=20 price=68.5 support=70.5 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=8.05 liquidity=90400000.0 spike=0.61
- ACAMD.CA: score=18.66 buy_ready=False sector_rank=10 price=2.26 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=55.74 liquidity=110360320.0 spike=0.88
- ACGC.CA: score=17.96 buy_ready=False sector_rank=16 price=9.4 support=9.11 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=43.27 liquidity=12041709.0 spike=0.21
- ADCI.CA: score=21.44 buy_ready=False sector_rank=10 price=241.52 support=211.0 resistance=238.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=79.84 liquidity=14723061.0 spike=1.89
- ADIB.CA: score=15.57 buy_ready=False sector_rank=11 price=45.5 support=44.01 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=46.17 liquidity=47776440.0 spike=0.44
- ADPC.CA: score=5.66 buy_ready=False sector_rank=10 price=3.69 support=3.68 resistance=3.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17696580.0 spike=0.66
- AFDI.CA: score=24.14 buy_ready=False sector_rank=10 price=46.07 support=40.15 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=53.44 liquidity=37300944.0 spike=2.74
- AFMC.CA: score=7.43 buy_ready=False sector_rank=10 price=70.05 support=67.0 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=39.0 liquidity=1777696.25 spike=0.37
- AJWA.CA: score=17.66 buy_ready=False sector_rank=10 price=177.89 support=130.01 resistance=188.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=84.42 liquidity=11554640.0 spike=0.44
- ALCN.CA: score=9.48 buy_ready=False sector_rank=17 price=28.08 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=36.64 liquidity=4639239.0 spike=0.32
- ALUM.CA: score=12.26 buy_ready=False sector_rank=10 price=22.86 support=23.02 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=46.4 liquidity=3601794.25 spike=0.32
- AMER.CA: score=13.4 buy_ready=False sector_rank=2 price=2.37 support=2.47 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=25.56 liquidity=49492616.0 spike=0.56
- AMES.CA: score=10.13 buy_ready=False sector_rank=10 price=49.03 support=48.0 resistance=53.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=35.12 liquidity=2472300.25 spike=0.7
- AMIA.CA: score=12.01 buy_ready=False sector_rank=10 price=8.69 support=8.54 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=54.63 liquidity=3358831.75 spike=0.23
- AMOC.CA: score=10.98 buy_ready=False sector_rank=6 price=7.63 support=7.71 resistance=8.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=17.2 liquidity=50710564.0 spike=0.72
- ANFI.CA: score=10.93 buy_ready=False sector_rank=10 price=33.12 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=76.32 liquidity=3274408.69 spike=0.04
- APSW.CA: score=0.08 buy_ready=False sector_rank=10 price=8.57 support=8.24 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=21.33 liquidity=425934.63 spike=0.46
- ARAB.CA: score=23.4 buy_ready=False sector_rank=2 price=0.21 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=52.78 liquidity=52154540.0 spike=0.61
- ARCC.CA: score=14.5 buy_ready=False sector_rank=19 price=54.87 support=54.31 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=38.83 liquidity=13615755.0 spike=0.38
- AREH.CA: score=19.66 buy_ready=False sector_rank=10 price=1.57 support=1.32 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=80.85 liquidity=22291744.0 spike=0.72
- ARVA.CA: score=20.66 buy_ready=False sector_rank=10 price=11.2 support=7.81 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=58.82 liquidity=16956574.0 spike=0.52
- ASCM.CA: score=10.66 buy_ready=False sector_rank=10 price=63.83 support=63.65 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=340481920.0 spike=5.1
- ASPI.CA: score=20.66 buy_ready=False sector_rank=10 price=0.32 support=0.26 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=60.96 liquidity=15758995.0 spike=0.22
- ATLC.CA: score=25.58 buy_ready=False sector_rank=9 price=5.24 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=68.29 liquidity=12648928.0 spike=2.36
- ATQA.CA: score=13.26 buy_ready=False sector_rank=20 price=9.28 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=45.49 liquidity=10521712.0 spike=0.31
- AXPH.CA: score=11.48 buy_ready=False sector_rank=10 price=1126.49 support=1073.0 resistance=1174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=47.39 liquidity=828150.44 spike=0.45
- BINV.CA: score=11.63 buy_ready=False sector_rank=13 price=47.52 support=42.9 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=43.93 liquidity=1208406.13 spike=0.11
- BIOC.CA: score=14.73 buy_ready=False sector_rank=10 price=73.86 support=68.34 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=46.54 liquidity=3472654.0 spike=1.3
- BTFH.CA: score=16.86 buy_ready=False sector_rank=9 price=3.06 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=124863912.0 spike=0.6
- CAED.CA: score=21.74 buy_ready=False sector_rank=10 price=72.13 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=56.39 liquidity=6660188.5 spike=1.21
- CANA.CA: score=18.76 buy_ready=False sector_rank=11 price=36.51 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=62.15 liquidity=6191863.0 spike=0.64
- CCAP.CA: score=18.42 buy_ready=False sector_rank=13 price=5.09 support=4.92 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=35.9 liquidity=446369440.0 spike=0.57
- CCRS.CA: score=17.1 buy_ready=False sector_rank=10 price=2.39 support=2.32 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=47.89 liquidity=8439180.0 spike=0.36
- CEFM.CA: score=1.83 buy_ready=False sector_rank=10 price=101.18 support=100.53 resistance=109.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=27.36 liquidity=1172410.13 spike=0.36
- CERA.CA: score=16.66 buy_ready=False sector_rank=10 price=1.23 support=1.14 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=68.0 liquidity=7006839.5 spike=0.44
- CFGH.CA: score=-0.34 buy_ready=False sector_rank=10 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=0.0 spike=0.0
- CICH.CA: score=11.98 buy_ready=False sector_rank=9 price=11.92 support=11.1 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=46.19 liquidity=3115446.75 spike=0.87
- CIEB.CA: score=23.23 buy_ready=False sector_rank=11 price=24.0 support=23.27 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=55.74 liquidity=8240388.0 spike=1.21
- CIRA.CA: score=22.12 buy_ready=False sector_rank=7 price=28.57 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=66.92 liquidity=29572672.0 spike=1.61
- CLHO.CA: score=29.4 buy_ready=False sector_rank=1 price=16.3 support=14.25 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=45.29 liquidity=108065296.0 spike=4.22
- CNFN.CA: score=10.86 buy_ready=False sector_rank=9 price=5.18 support=4.72 resistance=5.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=360697184.0 spike=22.0
- COMI.CA: score=21.57 buy_ready=False sector_rank=11 price=134.07 support=129.8 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=62.27 liquidity=382037152.0 spike=0.65
- COPR.CA: score=5.66 buy_ready=False sector_rank=10 price=0.36 support=0.36 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15714147.0 spike=0.36
- COSG.CA: score=18.66 buy_ready=False sector_rank=10 price=1.57 support=1.52 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=51.16 liquidity=18376602.0 spike=0.29
- CPCI.CA: score=12.22 buy_ready=False sector_rank=10 price=370.96 support=346.0 resistance=374.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=73.6 liquidity=1564266.88 spike=0.76
- CSAG.CA: score=16.72 buy_ready=False sector_rank=17 price=31.16 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=47.26 liquidity=8880615.0 spike=0.76
- DAPH.CA: score=13.72 buy_ready=False sector_rank=10 price=80.81 support=76.6 resistance=82.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=52.65 liquidity=2063073.38 spike=0.21
- DEIN.CA: score=6.66 buy_ready=False sector_rank=10 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=29.44 buy_ready=False sector_rank=12 price=27.18 support=23.7 resistance=26.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=61.63 liquidity=21232356.0 spike=10.03
- DSCW.CA: score=16.66 buy_ready=False sector_rank=10 price=1.8 support=1.74 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=20744004.0 spike=0.41
- DTPP.CA: score=1.13 buy_ready=False sector_rank=10 price=116.33 support=114.0 resistance=131.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=10.98 liquidity=470300.13 spike=0.26
- EALR.CA: score=11.81 buy_ready=False sector_rank=10 price=356.71 support=350.15 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=49.3 liquidity=1154004.75 spike=0.33
- EASB.CA: score=6.68 buy_ready=False sector_rank=10 price=7.51 support=7.31 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11083603.0 spike=1.51
- EAST.CA: score=14.44 buy_ready=False sector_rank=12 price=38.02 support=37.01 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=59.59 liquidity=26579030.0 spike=0.59
- EBSC.CA: score=14.25 buy_ready=False sector_rank=10 price=1.84 support=1.66 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=61.9 liquidity=1595021.38 spike=0.6
- ECAP.CA: score=16.62 buy_ready=False sector_rank=10 price=32.96 support=29.36 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=94.89 liquidity=6768625.0 spike=1.1
- EDFM.CA: score=8.66 buy_ready=False sector_rank=10 price=332.0 support=320.2 resistance=355.0 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=35.25 liquidity=0.0 spike=0.0
- EEII.CA: score=21.19 buy_ready=False sector_rank=10 price=2.4 support=2.29 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=6536370.5 spike=0.39
- EFIC.CA: score=-1.33 buy_ready=False sector_rank=20 price=199.35 support=192.01 resistance=213.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=23.61 liquidity=413633.06 spike=0.18
- EFID.CA: score=10.44 buy_ready=False sector_rank=12 price=27.59 support=27.06 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=33.77 liquidity=21694590.0 spike=0.29
- EFIH.CA: score=13.78 buy_ready=False sector_rank=21 price=20.94 support=20.2 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=37.27 liquidity=15459976.0 spike=0.3
- EGAL.CA: score=9.4 buy_ready=False sector_rank=20 price=286.49 support=294.99 resistance=334.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=13.55 liquidity=81023208.0 spike=1.07
- EGAS.CA: score=13.51 buy_ready=False sector_rank=6 price=51.12 support=47.5 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=60.41 liquidity=2527437.25 spike=0.2
- EGBE.CA: score=8.66 buy_ready=False sector_rank=11 price=0.44 support=0.43 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=38.0 liquidity=89104.0 spike=0.84
- EGCH.CA: score=4.26 buy_ready=False sector_rank=20 price=12.89 support=12.8 resistance=13.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24239064.0 spike=0.31
- EGSA.CA: score=3.89 buy_ready=False sector_rank=8 price=8.78 support=8.55 resistance=9.1 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=30.0 liquidity=0.0 spike=0.0
- EGTS.CA: score=16.4 buy_ready=False sector_rank=2 price=17.94 support=17.25 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=34.17 liquidity=25106012.0 spike=0.2
- EHDR.CA: score=20.66 buy_ready=False sector_rank=10 price=2.59 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=63.64 liquidity=27211416.0 spike=0.49
- EKHO.CA: score=10.98 buy_ready=False sector_rank=6 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=18.4 buy_ready=False sector_rank=3 price=2.11 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=12869278.0 spike=0.56
- ELKA.CA: score=5.66 buy_ready=False sector_rank=10 price=1.25 support=1.24 resistance=1.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27605758.0 spike=0.69
- ELNA.CA: score=7.04 buy_ready=False sector_rank=10 price=38.01 support=37.11 resistance=41.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=51.56 liquidity=721981.94 spike=1.83
- ELSH.CA: score=5.66 buy_ready=False sector_rank=10 price=12.09 support=11.99 resistance=12.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40562856.0 spike=0.22
- ELWA.CA: score=11.57 buy_ready=False sector_rank=10 price=2.08 support=1.87 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=58.54 liquidity=913203.19 spike=0.29
- EMFD.CA: score=21.4 buy_ready=False sector_rank=2 price=11.7 support=10.4 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=54.13 liquidity=69961752.0 spike=0.25
- ENGC.CA: score=17.25 buy_ready=False sector_rank=10 price=36.88 support=32.61 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=74.34 liquidity=4591179.0 spike=0.32
- EOSB.CA: score=12.66 buy_ready=False sector_rank=10 price=1.48 support=1.35 resistance=1.55 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- EPCO.CA: score=11.35 buy_ready=False sector_rank=10 price=9.12 support=8.9 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=52.91 liquidity=3698811.5 spike=0.38
- EPPK.CA: score=14.66 buy_ready=False sector_rank=10 price=12.68 support=11.67 resistance=13.12 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=57.63 liquidity=0.0 spike=0.0
- ETEL.CA: score=15.89 buy_ready=False sector_rank=8 price=95.52 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=30.46 liquidity=78656880.0 spike=0.99
- ETRS.CA: score=19.66 buy_ready=False sector_rank=10 price=10.39 support=7.65 resistance=11.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=76.67 liquidity=24529602.0 spike=0.39
- EXPA.CA: score=18.57 buy_ready=False sector_rank=11 price=18.4 support=18.21 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=46.63 liquidity=13324574.0 spike=0.39
- FAIT.CA: score=9.95 buy_ready=False sector_rank=11 price=36.49 support=35.01 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=42.28 liquidity=1376034.25 spike=0.29
- FAITA.CA: score=9.2 buy_ready=False sector_rank=11 price=0.99 support=0.99 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=52717.2 spike=1.29
- FERC.CA: score=12.24 buy_ready=False sector_rank=20 price=76.51 support=75.0 resistance=79.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=31.9 liquidity=11166559.0 spike=2.99
- FWRY.CA: score=8.78 buy_ready=False sector_rank=21 price=18.86 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=32.04 liquidity=131222424.0 spike=0.45
- GBCO.CA: score=5.0 buy_ready=False sector_rank=14 price=30.86 support=30.27 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=45640784.0 spike=0.43
- GDWA.CA: score=14.09 buy_ready=False sector_rank=10 price=0.79 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=58.54 liquidity=7434621.0 spike=0.53
- GGCC.CA: score=19.66 buy_ready=False sector_rank=10 price=0.42 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=56.18 liquidity=7960802.5 spike=1.02
- GIHD.CA: score=10.66 buy_ready=False sector_rank=10 price=43.97 support=42.79 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=56344852.0 spike=17.8
- GMCI.CA: score=7.25 buy_ready=False sector_rank=10 price=1.71 support=1.68 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=437354.47 spike=1.08
- GRCA.CA: score=6.25 buy_ready=False sector_rank=10 price=54.35 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=34.33 liquidity=5556731.5 spike=1.02
- GSSC.CA: score=4.01 buy_ready=False sector_rank=10 price=250.95 support=228.1 resistance=257.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=28.98 liquidity=3356805.0 spike=0.7
- GTWL.CA: score=12.7 buy_ready=False sector_rank=10 price=48.01 support=45.47 resistance=52.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=48.56 liquidity=3040983.25 spike=0.45
- HDBK.CA: score=24.57 buy_ready=False sector_rank=11 price=162.39 support=138.0 resistance=160.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=75.16 liquidity=81452640.0 spike=4.04
- HELI.CA: score=21.4 buy_ready=False sector_rank=2 price=6.4 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=42.95 liquidity=63937784.0 spike=0.45
- HRHO.CA: score=16.86 buy_ready=False sector_rank=9 price=26.93 support=25.8 resistance=27.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=51.97 liquidity=85255400.0 spike=0.58
- ICID.CA: score=12.63 buy_ready=False sector_rank=10 price=7.46 support=4.56 resistance=7.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=86.27 liquidity=2974754.25 spike=0.18
- IDRE.CA: score=20.84 buy_ready=False sector_rank=10 price=44.82 support=42.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=50.46 liquidity=19937456.0 spike=1.09
- IFAP.CA: score=3.0 buy_ready=False sector_rank=5 price=19.02 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=33.05 liquidity=2858382.25 spike=0.43
- INFI.CA: score=7.6 buy_ready=False sector_rank=10 price=94.15 support=93.0 resistance=105.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=12.22 liquidity=7945497.5 spike=0.88
- IRON.CA: score=13.38 buy_ready=False sector_rank=20 price=31.45 support=31.3 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=46.83 liquidity=8119442.5 spike=0.99
- ISMA.CA: score=15.11 buy_ready=False sector_rank=10 price=29.58 support=25.79 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=80.95 liquidity=9457122.0 spike=0.23
- ISMQ.CA: score=21.26 buy_ready=False sector_rank=20 price=8.18 support=7.31 resistance=8.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=58.1 liquidity=43862176.0 spike=0.59
- ISPH.CA: score=26.4 buy_ready=False sector_rank=1 price=12.24 support=11.3 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=60.23 liquidity=28901128.0 spike=0.22
- JUFO.CA: score=22.44 buy_ready=False sector_rank=12 price=30.9 support=27.6 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=69.51 liquidity=14422913.0 spike=0.35
- KABO.CA: score=7.21 buy_ready=False sector_rank=16 price=6.08 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=38.71 liquidity=3250144.25 spike=0.17
- KWIN.CA: score=7.36 buy_ready=False sector_rank=10 price=68.0 support=66.1 resistance=70.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11040459.0 spike=1.85
- KZPC.CA: score=15.49 buy_ready=False sector_rank=10 price=10.72 support=10.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=2838039.25 spike=0.37
- LCSW.CA: score=21.34 buy_ready=False sector_rank=19 price=27.59 support=26.0 resistance=28.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=53.08 liquidity=7838985.5 spike=0.78
- LUTS.CA: score=5.66 buy_ready=False sector_rank=10 price=0.74 support=0.73 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=34311208.0 spike=0.86
- MAAL.CA: score=14.96 buy_ready=False sector_rank=10 price=6.63 support=4.68 resistance=6.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=80.1 liquidity=5300215.0 spike=0.37
- MASR.CA: score=24.66 buy_ready=False sector_rank=10 price=7.14 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=57.93 liquidity=50150464.0 spike=0.89
- MBSC.CA: score=14.5 buy_ready=False sector_rank=19 price=244.05 support=247.43 resistance=260.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=49.73 liquidity=18738966.0 spike=0.43
- MCQE.CA: score=8.76 buy_ready=False sector_rank=19 price=171.82 support=174.0 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=22.19 liquidity=9263512.0 spike=0.58
- MCRO.CA: score=9.66 buy_ready=False sector_rank=10 price=1.22 support=1.2 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=15020089.0 spike=0.33
- MENA.CA: score=9.82 buy_ready=False sector_rank=2 price=6.8 support=6.22 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=29.06 liquidity=1423438.88 spike=0.08
- MEPA.CA: score=14.02 buy_ready=False sector_rank=10 price=1.63 support=1.66 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=8360744.0 spike=0.49
- MFPC.CA: score=9.26 buy_ready=False sector_rank=20 price=35.58 support=36.76 resistance=44.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=6.41 liquidity=86513920.0 spike=0.93
- MFSC.CA: score=10.38 buy_ready=False sector_rank=10 price=50.16 support=46.99 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40581352.0 spike=3.36
- MHOT.CA: score=6.21 buy_ready=False sector_rank=15 price=35.27 support=35.26 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=38704500.0 spike=1.62
- MICH.CA: score=23.84 buy_ready=False sector_rank=10 price=37.79 support=35.31 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=68.78 liquidity=25412910.0 spike=1.59
- MILS.CA: score=12.25 buy_ready=False sector_rank=10 price=136.22 support=131.58 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=48.27 liquidity=3595967.0 spike=0.21
- MIPH.CA: score=18.83 buy_ready=False sector_rank=1 price=661.57 support=648.25 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=64.54 liquidity=2333311.25 spike=1.05
- MOED.CA: score=11.8 buy_ready=False sector_rank=10 price=0.68 support=0.65 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=45.31 liquidity=5141844.0 spike=0.41
- MOIL.CA: score=13.13 buy_ready=False sector_rank=6 price=0.48 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=52.83 liquidity=142525.33 spike=0.89
- MOIN.CA: score=-0.34 buy_ready=False sector_rank=10 price=24.09 support=24.01 resistance=25.66 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=14.86 liquidity=0.0 spike=0.0
- MOSC.CA: score=11.5 buy_ready=False sector_rank=10 price=271.13 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=49.89 liquidity=2848334.0 spike=0.33
- MPCI.CA: score=26.02 buy_ready=False sector_rank=10 price=247.29 support=202.3 resistance=243.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=73.68 liquidity=217489312.0 spike=2.68
- MPCO.CA: score=21.56 buy_ready=False sector_rank=5 price=1.89 support=1.58 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=71.6 liquidity=119065928.0 spike=1.21
- MPRC.CA: score=10.66 buy_ready=False sector_rank=10 price=36.0 support=33.9 resistance=36.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=133214920.0 spike=6.21
- MTIE.CA: score=15.66 buy_ready=False sector_rank=14 price=9.05 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=48.87 liquidity=7659983.0 spike=0.44
- NAHO.CA: score=-0.34 buy_ready=False sector_rank=10 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=20.0 liquidity=0.0 spike=0.0
- NCCW.CA: score=24.14 buy_ready=False sector_rank=10 price=6.41 support=5.22 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=70.12 liquidity=77276032.0 spike=2.74
- NEDA.CA: score=6.04 buy_ready=False sector_rank=10 price=2.75 support=2.65 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=56.76 liquidity=382204.78 spike=0.87
- NHPS.CA: score=11.62 buy_ready=False sector_rank=10 price=67.82 support=65.03 resistance=71.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=53.83 liquidity=2963993.25 spike=0.67
- NINH.CA: score=18.66 buy_ready=False sector_rank=10 price=17.79 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=32.32 liquidity=21466418.0 spike=4.78
- NIPH.CA: score=24.4 buy_ready=False sector_rank=1 price=166.59 support=157.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=56.89 liquidity=71082424.0 spike=0.92
- OBRI.CA: score=16.36 buy_ready=False sector_rank=10 price=34.24 support=33.63 resistance=37.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=48.1 liquidity=8699270.0 spike=0.65
- OCDI.CA: score=32.36 buy_ready=False sector_rank=2 price=23.0 support=20.0 resistance=22.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=52.42 liquidity=129052624.0 spike=3.48
- OCPH.CA: score=20.66 buy_ready=False sector_rank=10 price=355.2 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=24.92 liquidity=23417750.0 spike=4.34
- ODIN.CA: score=17.83 buy_ready=False sector_rank=10 price=2.11 support=1.9 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=5171281.0 spike=0.47
- OFH.CA: score=15.66 buy_ready=False sector_rank=10 price=0.62 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=44.66 liquidity=14637877.0 spike=0.64
- OIH.CA: score=13.2 buy_ready=False sector_rank=13 price=1.41 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=32.35 liquidity=205329920.0 spike=2.39
- OLFI.CA: score=20.44 buy_ready=False sector_rank=12 price=21.95 support=21.39 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=66.95 liquidity=12261214.0 spike=0.61
- ORAS.CA: score=4.6 buy_ready=False sector_rank=18 price=792.28 support=787.25 resistance=812.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=268386560.0 spike=1.0
- ORHD.CA: score=25.4 buy_ready=False sector_rank=2 price=38.8 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=59.61 liquidity=123055904.0 spike=0.66
- ORWE.CA: score=17.96 buy_ready=False sector_rank=16 price=22.82 support=22.12 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=11732895.0 spike=0.28
- PHAR.CA: score=26.87 buy_ready=False sector_rank=1 price=87.76 support=83.02 resistance=89.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=60.2 liquidity=8472851.0 spike=0.23
- PHDC.CA: score=23.4 buy_ready=False sector_rank=2 price=15.5 support=14.32 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=54.6 liquidity=241529536.0 spike=0.57
- PHTV.CA: score=19.66 buy_ready=False sector_rank=10 price=236.55 support=201.55 resistance=238.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=75.76 liquidity=15085666.0 spike=0.82
- POUL.CA: score=6.7 buy_ready=False sector_rank=12 price=38.34 support=37.6 resistance=39.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=54811028.0 spike=1.63
- PRCL.CA: score=6.08 buy_ready=False sector_rank=19 price=31.77 support=28.66 resistance=31.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=55077788.0 spike=1.79
- PRDC.CA: score=8.4 buy_ready=False sector_rank=2 price=6.83 support=6.67 resistance=7.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=89854104.0 spike=0.89
- PRMH.CA: score=22.66 buy_ready=False sector_rank=10 price=2.71 support=2.23 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=60.55 liquidity=12984090.0 spike=0.46
- RACC.CA: score=23.8 buy_ready=False sector_rank=10 price=9.91 support=9.38 resistance=10.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=43.96 liquidity=25230992.0 spike=2.57
- RAKT.CA: score=5.39 buy_ready=False sector_rank=10 price=23.11 support=22.0 resistance=24.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=39.79 liquidity=391641.56 spike=1.17
- RAYA.CA: score=19.3 buy_ready=False sector_rank=4 price=7.12 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=48.55 liquidity=53700436.0 spike=0.59
- RMDA.CA: score=20.31 buy_ready=False sector_rank=1 price=5.03 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=47.52 liquidity=7911279.5 spike=0.09
- ROTO.CA: score=22.38 buy_ready=False sector_rank=10 price=42.42 support=32.66 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=84.24 liquidity=58711412.0 spike=2.36
- RREI.CA: score=13.88 buy_ready=False sector_rank=10 price=3.53 support=3.35 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=53.75 liquidity=6224103.5 spike=0.3
- RTVC.CA: score=10.52 buy_ready=False sector_rank=10 price=3.84 support=3.75 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=56.06 liquidity=2863146.0 spike=0.57
- RUBX.CA: score=14.69 buy_ready=False sector_rank=10 price=10.35 support=9.8 resistance=10.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=7033506.5 spike=0.64
- SAUD.CA: score=5.06 buy_ready=False sector_rank=11 price=21.4 support=20.82 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=32.06 liquidity=4488926.0 spike=0.43
- SCEM.CA: score=3.69 buy_ready=False sector_rank=19 price=61.55 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=27.42 liquidity=4189976.25 spike=0.21
- SCFM.CA: score=3.51 buy_ready=False sector_rank=10 price=240.73 support=248.1 resistance=276.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=23.66 liquidity=2854833.75 spike=0.26
- SCTS.CA: score=3.29 buy_ready=False sector_rank=7 price=592.12 support=565.25 resistance=648.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=28.59 liquidity=2387114.25 spike=0.48
- SDTI.CA: score=16.2 buy_ready=False sector_rank=10 price=47.08 support=43.6 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=71.18 liquidity=3542617.75 spike=0.25
- SEIG.CA: score=8.92 buy_ready=False sector_rank=10 price=186.25 support=178.0 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=25.67 liquidity=3266387.5 spike=0.72
- SIPC.CA: score=9.27 buy_ready=False sector_rank=10 price=3.46 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=38.78 liquidity=3617527.25 spike=0.29
- SKPC.CA: score=13.26 buy_ready=False sector_rank=20 price=16.09 support=16.13 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=35.95 liquidity=11897856.0 spike=0.23
- SMFR.CA: score=6.3 buy_ready=False sector_rank=10 price=199.43 support=192.0 resistance=214.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=41.88 liquidity=647944.56 spike=0.19
- SNFC.CA: score=12.7 buy_ready=False sector_rank=10 price=11.97 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=36.32 liquidity=4041453.75 spike=0.15
- SPIN.CA: score=1.86 buy_ready=False sector_rank=16 price=13.9 support=13.3 resistance=14.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=25.23 liquidity=1893202.63 spike=0.42
- SPMD.CA: score=5.8 buy_ready=False sector_rank=10 price=0.43 support=0.43 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28363880.0 spike=1.07
- SUGR.CA: score=4.47 buy_ready=False sector_rank=12 price=47.66 support=48.0 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=24.76 liquidity=5022765.5 spike=0.34
- SVCE.CA: score=20.66 buy_ready=False sector_rank=10 price=9.09 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=42.4 liquidity=37724056.0 spike=0.43
- SWDY.CA: score=24.7 buy_ready=False sector_rank=3 price=88.89 support=84.01 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=37.66 liquidity=38539408.0 spike=2.15
- TALM.CA: score=14.69 buy_ready=False sector_rank=7 price=15.82 support=15.32 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=64.15 liquidity=3782187.0 spike=0.49
- TMGH.CA: score=21.4 buy_ready=False sector_rank=2 price=95.01 support=92.91 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=50.74 liquidity=264187536.0 spike=0.54
- TRTO.CA: score=6.66 buy_ready=False sector_rank=10 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=9.03 buy_ready=False sector_rank=10 price=483.18 support=455.6 resistance=489.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=30.31 liquidity=1776181.25 spike=2.3
- UEGC.CA: score=18.66 buy_ready=False sector_rank=10 price=1.39 support=1.31 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=65.79 liquidity=10076383.0 spike=0.41
- UNIP.CA: score=19.66 buy_ready=False sector_rank=10 price=0.33 support=0.28 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=85.29 liquidity=21871752.0 spike=0.91
- UNIT.CA: score=6.89 buy_ready=False sector_rank=2 price=13.27 support=12.5 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=30.53 liquidity=489167.84 spike=0.07
- WCDF.CA: score=5.66 buy_ready=False sector_rank=10 price=531.95 support=450.0 resistance=547.9 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=44.29 liquidity=0.0 spike=0.0
- WKOL.CA: score=7.03 buy_ready=False sector_rank=10 price=289.98 support=287.66 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=35.88 liquidity=1373952.75 spike=0.44
- ZEOT.CA: score=20.6 buy_ready=False sector_rank=10 price=11.36 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=84.02 liquidity=30818672.0 spike=1.47
- ZMID.CA: score=23.5 buy_ready=False sector_rank=2 price=6.3 support=5.81 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=58.87 liquidity=215889904.0 spike=1.05

## Backtesting Lite
- OCDI.CA: 180d return=42.4%, max drawdown=-18.11%, MA20>MA50 days last20=12, as_of=2026-06-21T21:00:00+00:00
- DOMT.CA: 180d return=22.78%, max drawdown=-13.36%, MA20>MA50 days last20=16, as_of=2026-06-21T21:00:00+00:00
- CLHO.CA: 180d return=42.86%, max drawdown=-14.16%, MA20>MA50 days last20=20, as_of=2026-06-21T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- OCDI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Sixth of October Development and Investment summary=Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- DOMT.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=538 sources=3 expected=Arabian Food Industries Domty summary=Domty posts lower consolidated net profits at EGP 161m in 2025; net sales exceed EGP 9.3bn; Selling pressure pushes Domty’s stock toward EGP 23.50–22.85; Domty unveils demerger, establishes Dairy Products Euro Arabian
  - Domty posts lower consolidated net profits at EGP 161m in 2025; net sales exceed EGP 9.3bn: https://english.mubasher.info/news/4593671/Domty-posts-lower-consolidated-net-profits-at-EGP-161m-in-2025-net-sales-exceed-EGP-9-3bn/
  - Selling pressure pushes Domty’s stock toward EGP 23.50–22.85: https://english.mubasher.info/news/4562323/Selling-pressure-pushes-Domty-s-stock-toward-EGP-23-50-22-85/
  - Domty unveils demerger, establishes Dairy Products Euro Arabian: https://english.mubasher.info/news/4543153/Domty-unveils-demerger-establishes-Dairy-Products-Euro-Arabian/
- CLHO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=538 sources=3 expected=Cleopatra Hospital Group summary=Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025; Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn; Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo
  - Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025: https://english.mubasher.info/news/4594702/Cleopatra-Hospitals-unveils-EGP-84m-dividends-to-employee-for-2025/
  - Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn: https://english.mubasher.info/news/4579844/Cleopatra-Hospitals-posts-higher-consolidated-profits-in-2025-revenues-cross-EGP-7-2bn/
  - Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo: https://english.mubasher.info/news/4553462/Cleopatra-Hospitals-launches-EGP-3-5bn-Sky-hospital-in-East-Cairo/
- PHAR.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian International Pharmaceutical Industries summary=Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
- ISPH.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=538 sources=3 expected=Ibn Sina Pharma summary=Ibnsina Pharma’s consolidated profits jump to EGP 952m in 2025; EBRD grants EGP 1.3bn loan to Ibnsina Pharma for new warehouse; Ibnsina Pharma pens import, distribution deal with OMRON Healthcare
  - Ibnsina Pharma’s consolidated profits jump to EGP 952m in 2025: https://english.mubasher.info/news/4563237/Ibnsina-Pharma-s-consolidated-profits-jump-to-EGP-952m-in-2025/
  - EBRD grants EGP 1.3bn loan to Ibnsina Pharma for new warehouse: https://english.mubasher.info/news/4552027/EBRD-grants-EGP-1-3bn-loan-to-Ibnsina-Pharma-for-new-warehouse/
  - Ibnsina Pharma pens import, distribution deal with OMRON Healthcare: https://english.mubasher.info/news/4028068/Ibnsina-Pharma-pens-import-distribution-deal-with-OMRON-Healthcare/
- MPCI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Memphis Pharmaceuticals & Chemical Industries summary=Evidence rejected for MPCI.CA: source text did not clearly match MPCI.CA / Memphis Pharmaceuticals & Chemical Industries.
- ATLC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Al Tawfeek Leasing summary=Evidence rejected for ATLC.CA: source text did not clearly match ATLC.CA / Al Tawfeek Leasing.
- ORHD.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Development Egypt summary=Evidence rejected for ORHD.CA: source text did not clearly match ORHD.CA / Orascom Development Egypt.

## Warnings
- Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for DOMT.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CLHO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
- Evidence for ISPH.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for MPCI.CA: source text did not clearly match MPCI.CA / Memphis Pharmaceuticals & Chemical Industries.
- Evidence rejected for ATLC.CA: source text did not clearly match ATLC.CA / Al Tawfeek Leasing.
- Evidence rejected for ORHD.CA: source text did not clearly match ORHD.CA / Orascom Development Egypt.
