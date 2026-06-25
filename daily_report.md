# Telegram-First EGX Scanner Report

Scan phase: Evening tomorrow plan
Generated UTC: 2026-06-25T18:32:56.443118+00:00
Generated Cairo: 2026-06-25 21:32
Run timing: target 19:30 Cairo | generated Cairo 2026-06-25 21:32 | cron 30 16 * * 0-4
Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-06-25 21:29

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 180/190
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, June 25
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 15.79% / above MA50 31.58%
- EGX70 regime: MIXED / above MA20 46.15% / above MA50 66.67%
- Sector breadth: 33.33%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=944073280.0 spike=1.35 score=16.06
- ORAS.CA: liquidity=581945536.0 spike=1.0 score=4.6
- HRHO.CA: liquidity=384892864.0 spike=1.0 score=15.4
- TMGH.CA: liquidity=362160416.0 spike=0.75 score=18.44
- COMI.CA: liquidity=302314720.0 spike=0.51 score=17.03

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The local scanner stays on HOLD as the EGX30 remains bearish and EGX70 shows mixed signals, with sector breadth only at 33.3%. Risk mode is DEFENSIVE_NO_NEW_BUY, meaning new long entries are blocked until breadth improves. Liquidity spikes are present in several stocks, but they sit near resistance or in non‑leading sectors, so short‑term upside is uncertain for the next 1‑3 days.
- EGX30 bearish, EGX70 mixed → overall market risk elevated
- Sector breadth weak (33%) → no new BUYs allowed
- Top tickets show bullish outlooks but sit close to resistance or in lagging sectors
- Liquidity spikes exist but do not outweigh defensive regime
- Outlook for 1‑3 days remains uncertain; monitor breadth and any shift in EGX30 trend

## Top Liquidity Spikes
- LCSW.CA: spike=18.64 liquidity=190849232.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GTWL.CA: spike=15.56 liquidity=144073936.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- KWIN.CA: spike=9.79 liquidity=64301540.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DAPH.CA: spike=7.91 liquidity=61638568.0 outlook=BULLISH_WATCH score=87.55 buy_ready=False
- OCDI.CA: spike=5.5 liquidity=281622208.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Tourism & Leisure: score=16.61 5d=17.17% 20d=14.38% aboveMA50=100.0%
- #2 Technology & Distribution: score=8.97 5d=5.56% 20d=-1.07% aboveMA50=100.0%
- #3 Automotive & Distribution: score=8.93 5d=4.13% 20d=8.6% aboveMA50=100.0%
- #4 Non-bank Financial Services: score=6.04 5d=1.0% 20d=0.0% aboveMA50=60.0%
- #5 Healthcare: score=5.42 5d=1.61% 20d=3.32% aboveMA50=83.33%
- #6 Agriculture & Food Production: score=5.11 5d=-2.46% 20d=6.22% aboveMA50=50.0%
- #7 Education: score=4.9 5d=0.0% 20d=2.84% aboveMA50=66.67%
- #8 Transportation & Logistics: score=4.37 5d=-1.06% 20d=-2.45% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- RAYA.CA: BULLISH_WATCH score=94.97 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ATLC.CA: BULLISH_WATCH score=93.04 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- CNFN.CA: BULLISH_WATCH score=91.04 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- DAPH.CA: BULLISH_WATCH score=87.55 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance; sector is not leading
- CICH.CA: BULLISH_WATCH score=87.04 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- CIRA.CA: BULLISH_WATCH score=85.9 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended
- SVCE.CA: BULLISH_WATCH score=85.55 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- POUL.CA: BULLISH_WATCH score=82.29 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- GIHD.CA: BULLISH_WATCH score=81.55 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support; sector is not leading
- CERA.CA: BULLISH_WATCH score=80.55 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=12.13 buy_ready=False sector_rank=10 price=203.93 support=200.0 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.24 liquidity=3712024.75 spike=0.63
- ABUK.CA: score=8.87 buy_ready=False sector_rank=21 price=69.23 support=68.01 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=12.81 liquidity=96851712.0 spike=0.72
- ACAMD.CA: score=18.42 buy_ready=False sector_rank=10 price=2.24 support=2.17 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=61362860.0 spike=0.48
- ACGC.CA: score=17.58 buy_ready=False sector_rank=19 price=9.41 support=9.11 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.39 liquidity=27434200.0 spike=0.48
- ADCI.CA: score=15.64 buy_ready=False sector_rank=10 price=238.94 support=211.0 resistance=243.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=92.86 liquidity=6221249.0 spike=0.71
- ADIB.CA: score=15.03 buy_ready=False sector_rank=15 price=45.0 support=44.01 resistance=48.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.29 liquidity=74253840.0 spike=0.74
- ADPC.CA: score=18.4 buy_ready=False sector_rank=10 price=3.45 support=3.45 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.42 liquidity=44957680.0 spike=1.99
- AFDI.CA: score=5.52 buy_ready=False sector_rank=10 price=44.13 support=44.1 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15416862.0 spike=1.05
- AFMC.CA: score=5.85 buy_ready=False sector_rank=10 price=69.72 support=67.0 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.62 liquidity=434305.13 spike=0.14
- AJWA.CA: score=16.27 buy_ready=False sector_rank=10 price=176.53 support=131.5 resistance=188.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=83.33 liquidity=8852770.0 spike=0.33
- ALCN.CA: score=13.49 buy_ready=False sector_rank=8 price=27.97 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.28 liquidity=7745292.0 spike=0.59
- ALUM.CA: score=9.9 buy_ready=False sector_rank=10 price=21.62 support=22.35 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.36 liquidity=9481038.0 spike=0.93
- AMER.CA: score=10.44 buy_ready=False sector_rank=9 price=2.38 support=2.35 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.87 liquidity=20712446.0 spike=0.26
- AMES.CA: score=6.59 buy_ready=False sector_rank=10 price=48.2 support=48.0 resistance=53.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.42 liquidity=2170051.75 spike=0.67
- AMIA.CA: score=18.16 buy_ready=False sector_rank=10 price=8.67 support=8.55 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.84 liquidity=9742213.0 spike=0.71
- AMOC.CA: score=10.06 buy_ready=False sector_rank=14 price=7.6 support=7.58 resistance=8.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=20.72 liquidity=28235148.0 spike=0.54
- ANFI.CA: score=15.75 buy_ready=False sector_rank=10 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=0.9 buy_ready=False sector_rank=10 price=8.46 support=8.24 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=12.9 liquidity=1002241.13 spike=1.24
- ARAB.CA: score=14.44 buy_ready=False sector_rank=9 price=0.2 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.06 liquidity=48986428.0 spike=0.59
- ARCC.CA: score=12.92 buy_ready=False sector_rank=17 price=55.44 support=53.0 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=33.77 liquidity=16843096.0 spike=0.49
- AREH.CA: score=21.2 buy_ready=False sector_rank=10 price=1.58 support=1.32 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.09 liquidity=44787980.0 spike=1.39
- ARVA.CA: score=19.85 buy_ready=False sector_rank=10 price=11.44 support=8.08 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.07 liquidity=9426540.0 spike=0.29
- ASCM.CA: score=22.42 buy_ready=False sector_rank=10 price=60.44 support=47.49 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.76 liquidity=60634816.0 spike=0.68
- ASPI.CA: score=13.42 buy_ready=False sector_rank=10 price=0.31 support=0.26 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=30.0 liquidity=20196428.0 spike=0.29
- ATLC.CA: score=24.88 buy_ready=False sector_rank=4 price=5.22 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=56.08 liquidity=10235856.0 spike=1.74
- ATQA.CA: score=14.21 buy_ready=False sector_rank=21 price=9.47 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.0 liquidity=51891704.0 spike=1.67
- AXPH.CA: score=9.66 buy_ready=False sector_rank=10 price=1100.31 support=1073.0 resistance=1174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=44.06 liquidity=1236765.25 spike=0.79
- BINV.CA: score=13.72 buy_ready=False sector_rank=11 price=48.0 support=42.97 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=56.07 liquidity=3354498.5 spike=0.33
- BIOC.CA: score=11.89 buy_ready=False sector_rank=10 price=71.44 support=68.34 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.74 liquidity=2928015.25 spike=1.27
- BTFH.CA: score=16.12 buy_ready=False sector_rank=4 price=3.02 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.84 liquidity=260344176.0 spike=1.36
- CAED.CA: score=16.94 buy_ready=False sector_rank=10 price=70.16 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.44 liquidity=7582663.5 spike=1.47
- CANA.CA: score=15.33 buy_ready=False sector_rank=15 price=35.41 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.55 liquidity=16665985.0 spike=1.65
- CCAP.CA: score=16.06 buy_ready=False sector_rank=11 price=4.88 support=4.92 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.62 liquidity=944073280.0 spike=1.35
- CCRS.CA: score=18.42 buy_ready=False sector_rank=10 price=2.36 support=2.32 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=41.79 liquidity=15179766.0 spike=0.82
- CEFM.CA: score=1.51 buy_ready=False sector_rank=10 price=100.06 support=100.27 resistance=109.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=30.83 liquidity=1085584.0 spike=0.51
- CERA.CA: score=24.92 buy_ready=False sector_rank=10 price=1.25 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.54 liquidity=41555744.0 spike=2.75
- CFGH.CA: score=-0.58 buy_ready=False sector_rank=10 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=1858.4 spike=0.32
- CICH.CA: score=17.54 buy_ready=False sector_rank=4 price=12.12 support=11.1 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=44.19 liquidity=3804122.5 spike=1.17
- CIEB.CA: score=13.52 buy_ready=False sector_rank=15 price=23.93 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=56.49 liquidity=4491317.5 spike=0.69
- CIRA.CA: score=24.96 buy_ready=False sector_rank=7 price=28.03 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=63.7 liquidity=16001895.0 spike=0.89
- CLHO.CA: score=23.53 buy_ready=False sector_rank=5 price=16.59 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=65.46 liquidity=41927292.0 spike=1.18
- CNFN.CA: score=26.14 buy_ready=False sector_rank=4 price=4.83 support=4.36 resistance=5.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=88093176.0 spike=2.37
- COMI.CA: score=17.03 buy_ready=False sector_rank=15 price=132.52 support=129.8 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.01 liquidity=302314720.0 spike=0.51
- COPR.CA: score=17.42 buy_ready=False sector_rank=10 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=54.69 liquidity=14394442.0 spike=0.4
- COSG.CA: score=13.42 buy_ready=False sector_rank=10 price=1.53 support=1.53 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=29.73 liquidity=12555515.0 spike=0.22
- CPCI.CA: score=11.07 buy_ready=False sector_rank=10 price=377.33 support=347.11 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=72.1 liquidity=654673.25 spike=0.33
- CSAG.CA: score=23.65 buy_ready=False sector_rank=8 price=31.93 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.2 liquidity=27169838.0 spike=2.45
- DAPH.CA: score=29.42 buy_ready=False sector_rank=10 price=82.48 support=76.6 resistance=82.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.9 liquidity=61638568.0 spike=7.91
- DEIN.CA: score=6.42 buy_ready=False sector_rank=10 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=21.73 buy_ready=False sector_rank=12 price=26.91 support=23.7 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=73.9 liquidity=8478628.0 spike=2.47
- DSCW.CA: score=16.42 buy_ready=False sector_rank=10 price=1.77 support=1.74 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=38.24 liquidity=18922690.0 spike=0.38
- DTPP.CA: score=1.42 buy_ready=False sector_rank=10 price=116.0 support=114.0 resistance=130.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=18.44 liquidity=996619.69 spike=0.55
- EALR.CA: score=7.56 buy_ready=False sector_rank=10 price=351.42 support=350.2 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.9 liquidity=2136305.5 spike=0.67
- EASB.CA: score=22.42 buy_ready=False sector_rank=10 price=8.11 support=4.66 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=84.31 liquidity=32961296.0 spike=3.53
- EAST.CA: score=14.32 buy_ready=False sector_rank=12 price=38.02 support=37.01 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=52.58 liquidity=21387746.0 spike=0.48
- EBSC.CA: score=4.36 buy_ready=False sector_rank=10 price=1.79 support=1.66 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=941270.69 spike=0.35
- ECAP.CA: score=27.42 buy_ready=False sector_rank=10 price=33.57 support=29.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.01 liquidity=35162560.0 spike=5.32
- EDFM.CA: score=0.8 buy_ready=False sector_rank=10 price=330.59 support=322.11 resistance=355.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=19.32 liquidity=384906.38 spike=0.63
- EEII.CA: score=20.42 buy_ready=False sector_rank=10 price=2.42 support=2.3 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.79 liquidity=10442042.0 spike=0.74
- EFIC.CA: score=-0.65 buy_ready=False sector_rank=21 price=195.08 support=192.01 resistance=213.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=17.89 liquidity=1476023.5 spike=0.76
- EFID.CA: score=10.32 buy_ready=False sector_rank=12 price=26.78 support=27.06 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.55 liquidity=40505192.0 spike=0.56
- EFIH.CA: score=13.18 buy_ready=False sector_rank=20 price=20.78 support=20.82 resistance=20.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=12773960.0 spike=1.0
- EGAL.CA: score=8.87 buy_ready=False sector_rank=21 price=281.82 support=282.5 resistance=334.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=10.26 liquidity=37812624.0 spike=0.49
- EGAS.CA: score=5.08 buy_ready=False sector_rank=14 price=49.14 support=49.0 resistance=52.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10999741.0 spike=1.01
- EGBE.CA: score=11.92 buy_ready=False sector_rank=15 price=0.46 support=0.43 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=46.0 liquidity=171163.0 spike=1.86
- EGCH.CA: score=8.87 buy_ready=False sector_rank=21 price=12.9 support=12.69 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.6 liquidity=38880228.0 spike=0.66
- EGSA.CA: score=3.49 buy_ready=False sector_rank=16 price=8.75 support=8.55 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=30.0 liquidity=17518.58 spike=1.24
- EGTS.CA: score=18.44 buy_ready=False sector_rank=9 price=17.06 support=17.25 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.09 liquidity=32949298.0 spike=0.3
- EHDR.CA: score=18.42 buy_ready=False sector_rank=10 price=2.57 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.92 liquidity=16662125.0 spike=0.29
- EKHO.CA: score=10.06 buy_ready=False sector_rank=14 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=16.11 buy_ready=False sector_rank=13 price=2.1 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=12377751.0 spike=0.59
- ELKA.CA: score=17.42 buy_ready=False sector_rank=10 price=1.24 support=1.15 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=14203525.0 spike=0.35
- ELNA.CA: score=6.0 buy_ready=False sector_rank=10 price=36.1 support=37.11 resistance=41.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.24 liquidity=640160.75 spike=1.47
- ELSH.CA: score=14.42 buy_ready=False sector_rank=10 price=11.7 support=11.87 resistance=11.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=43248408.0 spike=1.0
- ELWA.CA: score=9.78 buy_ready=False sector_rank=10 price=2.04 support=2.0 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=47.92 liquidity=1357926.75 spike=0.42
- EMFD.CA: score=18.44 buy_ready=False sector_rank=9 price=11.8 support=10.5 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=42.9 liquidity=127098352.0 spike=0.45
- ENGC.CA: score=17.55 buy_ready=False sector_rank=10 price=35.61 support=32.81 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.75 liquidity=5134144.5 spike=0.38
- EOSB.CA: score=12.49 buy_ready=False sector_rank=10 price=1.48 support=1.35 resistance=1.55 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=67810.64 spike=0.53
- EPCO.CA: score=8.86 buy_ready=False sector_rank=10 price=8.9 support=8.9 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=3444086.0 spike=0.37
- EPPK.CA: score=14.45 buy_ready=False sector_rank=10 price=12.79 support=11.67 resistance=13.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.94 liquidity=1268583.75 spike=1.38
- ETEL.CA: score=14.99 buy_ready=False sector_rank=16 price=94.0 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.82 liquidity=35964872.0 spike=0.46
- ETRS.CA: score=8.74 buy_ready=False sector_rank=10 price=11.3 support=10.25 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=162525664.0 spike=2.66
- EXPA.CA: score=15.55 buy_ready=False sector_rank=15 price=18.2 support=18.2 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.78 liquidity=41279272.0 spike=1.26
- FAIT.CA: score=8.81 buy_ready=False sector_rank=15 price=36.15 support=35.01 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.99 liquidity=782735.0 spike=0.23
- FAITA.CA: score=8.07 buy_ready=False sector_rank=15 price=0.99 support=0.99 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=37.84 liquidity=34287.18 spike=0.97
- FERC.CA: score=2.92 buy_ready=False sector_rank=21 price=75.24 support=75.0 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=23.73 liquidity=3044952.5 spike=0.79
- FWRY.CA: score=16.18 buy_ready=False sector_rank=20 price=18.71 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.3 liquidity=105757520.0 spike=0.4
- GBCO.CA: score=21.4 buy_ready=False sector_rank=3 price=31.13 support=25.25 resistance=31.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=85.89 liquidity=70494528.0 spike=0.74
- GDWA.CA: score=12.26 buy_ready=False sector_rank=10 price=0.78 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.58 liquidity=7840849.0 spike=0.56
- GGCC.CA: score=23.1 buy_ready=False sector_rank=10 price=0.44 support=0.4 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=15023014.0 spike=1.84
- GIHD.CA: score=26.78 buy_ready=False sector_rank=10 price=43.47 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.56 liquidity=15752623.0 spike=2.18
- GMCI.CA: score=-0.39 buy_ready=False sector_rank=10 price=1.71 support=1.66 resistance=1.84 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=33.33 liquidity=187734.06 spike=0.6
- GRCA.CA: score=3.22 buy_ready=False sector_rank=10 price=53.16 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=32.12 liquidity=2800888.5 spike=0.57
- GSSC.CA: score=9.39 buy_ready=False sector_rank=10 price=245.91 support=228.1 resistance=257.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=36.64 liquidity=1967935.63 spike=0.58
- GTWL.CA: score=10.42 buy_ready=False sector_rank=10 price=62.44 support=60.5 resistance=68.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=144073936.0 spike=15.56
- HDBK.CA: score=19.03 buy_ready=False sector_rank=15 price=161.92 support=138.0 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=82.54 liquidity=24235390.0 spike=0.92
- HELI.CA: score=20.44 buy_ready=False sector_rank=9 price=6.52 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.3 liquidity=103208504.0 spike=0.75
- HRHO.CA: score=15.4 buy_ready=False sector_rank=4 price=26.88 support=26.89 resistance=26.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=384892864.0 spike=1.0
- ICID.CA: score=4.79 buy_ready=False sector_rank=10 price=8.05 support=7.4 resistance=8.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9367628.0 spike=0.58
- IDRE.CA: score=17.16 buy_ready=False sector_rank=10 price=43.93 support=42.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.92 liquidity=8740001.0 spike=0.53
- IFAP.CA: score=17.16 buy_ready=False sector_rank=6 price=19.38 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.17 liquidity=12739626.0 spike=2.06
- INFI.CA: score=1.65 buy_ready=False sector_rank=10 price=92.69 support=93.0 resistance=105.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=16.44 liquidity=2226925.75 spike=0.27
- IRON.CA: score=3.78 buy_ready=False sector_rank=21 price=31.31 support=30.95 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=5909177.0 spike=0.74
- ISMA.CA: score=17.89 buy_ready=False sector_rank=10 price=29.59 support=25.95 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.59 liquidity=9468467.0 spike=0.24
- ISMQ.CA: score=23.69 buy_ready=False sector_rank=21 price=8.63 support=7.38 resistance=8.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.66 liquidity=213642320.0 spike=2.41
- ISPH.CA: score=19.17 buy_ready=False sector_rank=5 price=11.98 support=11.3 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.17 liquidity=58719644.0 spike=0.48
- JUFO.CA: score=17.9 buy_ready=False sector_rank=12 price=30.46 support=28.09 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=56.88 liquidity=5588794.0 spike=0.14
- KABO.CA: score=9.04 buy_ready=False sector_rank=19 price=6.15 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.9 liquidity=4467396.5 spike=0.25
- KWIN.CA: score=10.42 buy_ready=False sector_rank=10 price=70.12 support=68.25 resistance=75.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=64301540.0 spike=9.79
- KZPC.CA: score=10.89 buy_ready=False sector_rank=10 price=8.63 support=8.8 resistance=8.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=6466397.0 spike=1.0
- LCSW.CA: score=9.92 buy_ready=False sector_rank=17 price=29.65 support=27.34 resistance=31.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=190849232.0 spike=18.64
- LUTS.CA: score=20.42 buy_ready=False sector_rank=10 price=0.72 support=0.55 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.88 liquidity=20051588.0 spike=0.47
- MAAL.CA: score=17.14 buy_ready=False sector_rank=10 price=6.99 support=5.16 resistance=7.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=79.41 liquidity=7716529.0 spike=0.48
- MASR.CA: score=18.42 buy_ready=False sector_rank=10 price=7.0 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.29 liquidity=45227748.0 spike=0.81
- MBSC.CA: score=9.92 buy_ready=False sector_rank=17 price=242.74 support=242.2 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=33.82 liquidity=10540226.0 spike=0.26
- MCQE.CA: score=9.92 buy_ready=False sector_rank=17 price=167.34 support=171.0 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.54 liquidity=11049402.0 spike=0.7
- MCRO.CA: score=9.42 buy_ready=False sector_rank=10 price=1.22 support=1.2 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=22982070.0 spike=0.59
- MENA.CA: score=4.27 buy_ready=False sector_rank=9 price=6.69 support=6.22 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=32.08 liquidity=830791.19 spike=0.05
- MEPA.CA: score=9.42 buy_ready=False sector_rank=10 price=1.59 support=1.6 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=20.83 liquidity=10056420.0 spike=0.79
- MFPC.CA: score=8.89 buy_ready=False sector_rank=21 price=35.5 support=35.15 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=8.6 liquidity=85814168.0 spike=1.01
- MFSC.CA: score=16.26 buy_ready=False sector_rank=10 price=49.96 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=54.35 liquidity=5839614.5 spike=0.58
- MHOT.CA: score=24.4 buy_ready=False sector_rank=1 price=34.89 support=28.83 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.91 liquidity=15333721.0 spike=0.58
- MICH.CA: score=17.72 buy_ready=False sector_rank=10 price=37.67 support=35.4 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=64.57 liquidity=5299697.5 spike=0.35
- MILS.CA: score=10.65 buy_ready=False sector_rank=10 price=132.08 support=130.11 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=42.36 liquidity=2234662.0 spike=0.18
- MIPH.CA: score=8.17 buy_ready=False sector_rank=5 price=641.55 support=651.0 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.49 liquidity=2005803.13 spike=0.93
- MOED.CA: score=8.87 buy_ready=False sector_rank=10 price=0.67 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.94 liquidity=2449290.25 spike=0.23
- MOIL.CA: score=12.62 buy_ready=False sector_rank=14 price=0.48 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=353725.06 spike=2.1
- MOIN.CA: score=-0.04 buy_ready=False sector_rank=10 price=23.03 support=23.02 resistance=25.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=1.06 liquidity=538376.44 spike=0.37
- MOSC.CA: score=7.91 buy_ready=False sector_rank=10 price=260.65 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=44.89 liquidity=2492627.0 spike=0.29
- MPCI.CA: score=20.66 buy_ready=False sector_rank=10 price=236.1 support=204.36 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.3 liquidity=105643704.0 spike=1.12
- MPCO.CA: score=23.04 buy_ready=False sector_rank=6 price=1.84 support=1.58 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.52 liquidity=43198324.0 spike=0.41
- MPRC.CA: score=24.62 buy_ready=False sector_rank=10 price=38.3 support=31.1 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=73.84 liquidity=73320392.0 spike=2.1
- MTIE.CA: score=20.4 buy_ready=False sector_rank=3 price=9.04 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.99 liquidity=10707896.0 spike=0.67
- NAHO.CA: score=6.44 buy_ready=False sector_rank=10 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=24011.35 spike=0.72
- NCCW.CA: score=20.42 buy_ready=False sector_rank=10 price=6.21 support=5.29 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.8 liquidity=20465114.0 spike=0.64
- NEDA.CA: score=5.74 buy_ready=False sector_rank=10 price=2.74 support=2.68 resistance=2.84 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=42.31 liquidity=318344.16 spike=0.89
- NHPS.CA: score=14.26 buy_ready=False sector_rank=10 price=64.09 support=63.19 resistance=63.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=3839665.0 spike=1.0
- NINH.CA: score=18.66 buy_ready=False sector_rank=10 price=17.99 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=48.53 liquidity=7337712.5 spike=1.45
- NIPH.CA: score=19.17 buy_ready=False sector_rank=5 price=161.89 support=157.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.35 liquidity=23986264.0 spike=0.33
- OBRI.CA: score=14.21 buy_ready=False sector_rank=10 price=33.81 support=33.63 resistance=37.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.38 liquidity=8793552.0 spike=0.66
- OCDI.CA: score=10.44 buy_ready=False sector_rank=9 price=25.47 support=24.3 resistance=25.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=281622208.0 spike=5.5
- OCPH.CA: score=11.39 buy_ready=False sector_rank=10 price=345.35 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.33 liquidity=5974579.0 spike=0.97
- ODIN.CA: score=17.8 buy_ready=False sector_rank=10 price=2.1 support=1.91 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=7378017.5 spike=0.69
- OFH.CA: score=9.42 buy_ready=False sector_rank=10 price=0.59 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=22.09 liquidity=14345247.0 spike=0.71
- OIH.CA: score=19.36 buy_ready=False sector_rank=11 price=1.41 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.48 liquidity=38801004.0 spike=0.44
- OLFI.CA: score=15.32 buy_ready=False sector_rank=12 price=21.67 support=21.39 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.79 liquidity=17378372.0 spike=0.87
- ORAS.CA: score=4.6 buy_ready=False sector_rank=18 price=734.06 support=733.52 resistance=795.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=581945536.0 spike=1.0
- ORHD.CA: score=20.44 buy_ready=False sector_rank=9 price=38.74 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.72 liquidity=73013048.0 spike=0.39
- ORWE.CA: score=17.58 buy_ready=False sector_rank=19 price=22.84 support=22.65 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=15361090.0 spike=0.41
- PHAR.CA: score=22.41 buy_ready=False sector_rank=5 price=88.08 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.04 liquidity=9246790.0 spike=0.26
- PHDC.CA: score=18.44 buy_ready=False sector_rank=9 price=15.13 support=14.43 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.64 liquidity=162855344.0 spike=0.4
- PHTV.CA: score=18.44 buy_ready=False sector_rank=10 price=249.99 support=201.55 resistance=256.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=87.78 liquidity=9016899.0 spike=0.44
- POUL.CA: score=24.32 buy_ready=False sector_rank=12 price=38.24 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=59.88 liquidity=14333330.0 spike=0.36
- PRCL.CA: score=21.82 buy_ready=False sector_rank=17 price=30.55 support=22.02 resistance=32.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.88 liquidity=70940784.0 spike=1.95
- PRDC.CA: score=22.44 buy_ready=False sector_rank=9 price=7.04 support=5.7 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=63.66 liquidity=74106240.0 spike=0.67
- PRMH.CA: score=18.42 buy_ready=False sector_rank=10 price=2.55 support=2.26 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.62 liquidity=15072637.0 spike=0.5
- RACC.CA: score=14.17 buy_ready=False sector_rank=10 price=9.8 support=9.38 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=41.58 liquidity=5752533.0 spike=0.6
- RAKT.CA: score=6.48 buy_ready=False sector_rank=10 price=23.11 support=22.0 resistance=24.1 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=37.86 liquidity=58537.63 spike=0.25
- RAYA.CA: score=23.4 buy_ready=False sector_rank=2 price=7.37 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.7 liquidity=55790076.0 spike=0.64
- RMDA.CA: score=19.17 buy_ready=False sector_rank=5 price=4.95 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.9 liquidity=22665308.0 spike=0.28
- ROTO.CA: score=19.72 buy_ready=False sector_rank=10 price=41.14 support=32.76 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=75.77 liquidity=58700816.0 spike=2.15
- RREI.CA: score=15.42 buy_ready=False sector_rank=10 price=3.45 support=3.35 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=39.47 liquidity=10902370.0 spike=0.56
- RTVC.CA: score=18.08 buy_ready=False sector_rank=10 price=3.63 support=3.76 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=49.35 liquidity=13377439.0 spike=2.83
- RUBX.CA: score=22.68 buy_ready=False sector_rank=10 price=10.51 support=9.8 resistance=10.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.8 liquidity=11067778.0 spike=1.13
- SAUD.CA: score=6.61 buy_ready=False sector_rank=15 price=21.1 support=20.82 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.48 liquidity=6573970.5 spike=0.74
- SCEM.CA: score=14.92 buy_ready=False sector_rank=17 price=62.56 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.9 liquidity=13898802.0 spike=0.73
- SCFM.CA: score=2.36 buy_ready=False sector_rank=10 price=236.72 support=226.5 resistance=276.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.61 liquidity=1942974.25 spike=0.3
- SCTS.CA: score=6.38 buy_ready=False sector_rank=7 price=575.73 support=577.41 resistance=577.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=1423683.75 spike=1.0
- SDTI.CA: score=14.51 buy_ready=False sector_rank=10 price=46.97 support=44.03 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.93 liquidity=4088686.25 spike=0.32
- SEIG.CA: score=13.02 buy_ready=False sector_rank=10 price=185.27 support=179.43 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.62 liquidity=2600965.0 spike=0.63
- SIPC.CA: score=5.22 buy_ready=False sector_rank=10 price=3.44 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=27.78 liquidity=4795499.0 spike=0.42
- SKPC.CA: score=7.87 buy_ready=False sector_rank=21 price=15.92 support=15.95 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.92 liquidity=30667554.0 spike=0.79
- SMFR.CA: score=1.69 buy_ready=False sector_rank=10 price=196.11 support=192.0 resistance=214.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.4 liquidity=1273338.75 spike=0.53
- SNFC.CA: score=20.6 buy_ready=False sector_rank=10 price=12.29 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=37.79 liquidity=22427338.0 spike=1.09
- SPIN.CA: score=11.7 buy_ready=False sector_rank=19 price=13.99 support=13.3 resistance=14.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.13 liquidity=13735460.0 spike=2.06
- SPMD.CA: score=18.83 buy_ready=False sector_rank=10 price=0.42 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=54.97 liquidity=8414671.0 spike=0.3
- SUGR.CA: score=3.74 buy_ready=False sector_rank=12 price=47.05 support=47.27 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.98 liquidity=4424587.0 spike=0.51
- SVCE.CA: score=24.0 buy_ready=False sector_rank=10 price=9.3 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.51 liquidity=131929832.0 spike=1.79
- SWDY.CA: score=18.11 buy_ready=False sector_rank=13 price=86.96 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.89 liquidity=12772878.0 spike=0.73
- TALM.CA: score=15.66 buy_ready=False sector_rank=7 price=15.89 support=15.5 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.56 liquidity=6697628.5 spike=0.83
- TMGH.CA: score=18.44 buy_ready=False sector_rank=9 price=95.67 support=92.91 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.8 liquidity=362160416.0 spike=0.75
- TRTO.CA: score=6.42 buy_ready=False sector_rank=10 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=10.53 buy_ready=False sector_rank=10 price=486.78 support=465.01 resistance=500.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=74.13 liquidity=1009277.81 spike=1.05
- UEGC.CA: score=13.48 buy_ready=False sector_rank=10 price=1.39 support=1.32 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.24 liquidity=5061957.5 spike=0.21
- UNIP.CA: score=15.49 buy_ready=False sector_rank=10 price=0.31 support=0.28 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.07 liquidity=7069036.5 spike=0.31
- UNIT.CA: score=4.54 buy_ready=False sector_rank=9 price=12.96 support=12.92 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.19 liquidity=1102969.63 spike=0.16
- WCDF.CA: score=5.64 buy_ready=False sector_rank=10 price=531.95 support=450.0 resistance=547.9 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=44.29 liquidity=223950.96 spike=0.89
- WKOL.CA: score=7.63 buy_ready=False sector_rank=10 price=284.62 support=287.2 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.6 liquidity=2213909.25 spike=0.77
- ZEOT.CA: score=5.46 buy_ready=False sector_rank=10 price=10.84 support=10.8 resistance=11.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24825224.0 spike=1.02
- ZMID.CA: score=22.44 buy_ready=False sector_rank=9 price=6.48 support=5.82 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.23 liquidity=176512416.0 spike=0.85

## Backtesting Lite
- DAPH.CA: 180d return=5.24%, max drawdown=-30.86%, MA20>MA50 days last20=12, as_of=2026-06-23T21:00:00+00:00
- ECAP.CA: 180d return=6.16%, max drawdown=-28.16%, MA20>MA50 days last20=20, as_of=2026-06-23T21:00:00+00:00
- GIHD.CA: 180d return=3.91%, max drawdown=-35.06%, MA20>MA50 days last20=20, as_of=2026-06-23T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- DAPH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Development & Engineering Consultants summary=Evidence rejected for DAPH.CA: source text did not clearly match DAPH.CA / Development & Engineering Consultants.
- ECAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Al Ezz Ceramics & Porcelain Co. summary=Evidence rejected for ECAP.CA: source text did not clearly match ECAP.CA / Al Ezz Ceramics & Porcelain Co..
- GIHD.CA: status=OLD_ACCEPTED latest=2016-01-01 age_days=3828 sources=3 expected=Gharbia Islamic Housing Development Company summary=Gharbia Islamic Housing to discuss raising capital mid-December; Gharbia Islamic Housing to distribute EGP 0.2/shr; Gharbia Islamic Housing profits fall 46% in 2016
  - Gharbia Islamic Housing to discuss raising capital mid-December: https://english.mubasher.info/news/3147599/Gharbia-Islamic-Housing-to-discuss-raising-capital-mid-December/
  - Gharbia Islamic Housing to distribute EGP 0.2/shr: https://english.mubasher.info/news/3082262/Gharbia-Islamic-Housing-to-distribute-EGP-0-2-shr/
  - Gharbia Islamic Housing profits fall 46% in 2016: https://english.mubasher.info/news/3068305/Gharbia-Islamic-Housing-profits-fall-46-in-2016/
- CNFN.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=540 sources=3 expected=Contact Financial Holding summary=Contact’s consolidated profits approach EGP 471m in 2025; Contact logs lower consolidated net profits at EGP 291m in 9M-25; Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem
  - Contact’s consolidated profits approach EGP 471m in 2025: https://english.mubasher.info/news/4582855/Contact-s-consolidated-profits-approach-EGP-471m-in-2025/
  - Contact logs lower consolidated net profits at EGP 291m in 9M-25: https://english.mubasher.info/news/4526894/Contact-logs-lower-consolidated-net-profits-at-EGP-291m-in-9M-25/
  - Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem: https://english.mubasher.info/news/4509412/Contact-e-money-forge-partnership-to-boost-Egypt-s-financial-ecosystem/
- CIRA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Investment and Real Estate Development summary=CIRA Education take over 51% of L’École Française Hurghada; CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion; CIRA Education launches Middle East’s 1st initiative for care economy
  - CIRA Education take over 51% of L’École Française Hurghada: https://english.mubasher.info/news/4488666/CIRA-Education-take-over-51-of-L-%C3%89cole-Fran%C3%A7aise-Hurghada/
  - CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion: https://english.mubasher.info/news/4393636/CIRA-s-majority-shareholder-acquires-37-5-additional-equity-backs-regional-expansion/
  - CIRA Education launches Middle East’s 1st initiative for care economy: https://english.mubasher.info/news/4391766/CIRA-Education-launches-Middle-East-s-1st-initiative-for-care-economy/
- CERA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=The Arab Ceramic Co. summary=Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- ATLC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Al Tawfeek Leasing summary=Evidence rejected for ATLC.CA: source text did not clearly match ATLC.CA / Al Tawfeek Leasing.
- MPRC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Media Production City summary=Evidence rejected for MPRC.CA: source text did not clearly match MPRC.CA / Egyptian Media Production City.

## Warnings
- Evidence rejected for DAPH.CA: source text did not clearly match DAPH.CA / Development & Engineering Consultants.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for ECAP.CA: source text did not clearly match ECAP.CA / Al Ezz Ceramics & Porcelain Co..
- Evidence for GIHD.CA matches the company but appears old; latest detected date is 2016-01-01.
- Evidence for CNFN.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
- Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- Evidence rejected for ATLC.CA: source text did not clearly match ATLC.CA / Al Tawfeek Leasing.
- Evidence rejected for MPRC.CA: source text did not clearly match MPRC.CA / Egyptian Media Production City.
