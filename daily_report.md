# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-06-30T15:09:11.498806+00:00
Generated Cairo: 2026-06-30 18:09
Run timing: target 15:30 Cairo | generated Cairo 2026-06-30 18:09 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-06-30 18:06

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 174/190
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, June 30
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 20.0% / above MA50 25.0%
- EGX70 regime: BEARISH / above MA20 43.24% / above MA50 62.16%
- Sector breadth: 9.52%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=533109888.0 spike=0.91 score=14.96
- TMGH.CA: liquidity=403056288.0 spike=1.08 score=14.56
- CCAP.CA: liquidity=277849280.0 spike=0.41 score=8.94
- PHDC.CA: liquidity=227825936.0 spike=0.56 score=17.4
- ZMID.CA: liquidity=217092816.0 spike=1.04 score=4.48

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner stays on HOLD because both EGX30 and EGX70 are in a bearish regime with weak breadth (≈9.5%). Market risk mode is DEFENSIVE_NO_NEW_BUY, so new long entries are blocked despite a few stocks showing bullish watch signals.
- Liquidity spikes in CSAG.CA and NINH.CA indicate short‑term accumulation, but sector breadth is low and market trend is down.
- MHOT.CA leads the Tourism & Leisure sector, which is the top‑performing sector, yet its support is 17% away and momentum is stretched.
- Resistance levels for most watch‑list stocks sit 4‑8% above current price, limiting upside in the next 1‑3 days.
- Bearish EGX30/EGX70 trends and negative median 5‑day returns keep overall risk high; any move higher is uncertain.

## Top Liquidity Spikes
- AMES.CA: spike=36.57 liquidity=156619984.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DTPP.CA: spike=16.14 liquidity=32460508.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- NHPS.CA: spike=6.99 liquidity=24310658.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SCTS.CA: spike=6.49 liquidity=20202018.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- NINH.CA: spike=6.27 liquidity=26266350.0 outlook=BULLISH_WATCH score=83.61 buy_ready=False

## Sector Leaderboard
- #1 Tourism & Leisure: score=9.01 5d=4.84% 20d=1.71% aboveMA50=100.0%
- #2 Automotive & Distribution: score=8.63 5d=2.47% 20d=7.28% aboveMA50=100.0%
- #3 Transportation & Logistics: score=4.65 5d=-0.26% 20d=-2.71% aboveMA50=50.0%
- #4 Technology & Distribution: score=3.39 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #5 Healthcare: score=2.94 5d=-4.29% 20d=-1.1% aboveMA50=83.33%
- #6 Food, Beverages & Tobacco: score=2.74 5d=-3.15% 20d=-0.4% aboveMA50=57.14%
- #7 Banking & Financials: score=2.41 5d=-3.15% 20d=-1.85% aboveMA50=50.0%
- #8 Textiles: score=2.39 5d=-2.61% 20d=-4.21% aboveMA50=75.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CSAG.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- PHAR.CA: BULLISH_WATCH score=89.94 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- CAED.CA: BULLISH_WATCH score=89.61 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- MASR.CA: BULLISH_WATCH score=89.61 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- FAIT.CA: BULLISH_WATCH score=89.41 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- NIPH.CA: BULLISH_WATCH score=83.94 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- NINH.CA: BULLISH_WATCH score=83.61 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- GIHD.CA: BULLISH_WATCH score=83.61 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- GMCI.CA: BULLISH_WATCH score=83.61 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- MTIE.CA: BULLISH_WATCH score=81.63 liquidity=TRADEABLE sector=LEADING risk=below MA20

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=3.07 buy_ready=False sector_rank=10 price=202.01 support=196.0 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.49 liquidity=3427405.0 spike=0.56
- ABUK.CA: score=8.27 buy_ready=False sector_rank=20 price=67.58 support=66.66 resistance=84.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=9.05 liquidity=54637912.0 spike=0.4
- ACAMD.CA: score=12.64 buy_ready=False sector_rank=10 price=2.24 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.78 liquidity=76394744.0 spike=0.62
- ACGC.CA: score=12.96 buy_ready=False sector_rank=8 price=9.21 support=8.92 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.99 liquidity=13787804.0 spike=0.36
- ADCI.CA: score=16.72 buy_ready=False sector_rank=10 price=240.47 support=211.0 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=84.3 liquidity=8079118.5 spike=0.79
- ADIB.CA: score=19.96 buy_ready=False sector_rank=7 price=46.49 support=44.01 resistance=48.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=80194120.0 spike=0.87
- ADPC.CA: score=10.41 buy_ready=False sector_rank=10 price=3.43 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=35.4 liquidity=6764691.5 spike=0.32
- AFDI.CA: score=20.4 buy_ready=False sector_rank=10 price=44.06 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.35 liquidity=20315368.0 spike=1.38
- AFMC.CA: score=1.79 buy_ready=False sector_rank=10 price=69.61 support=66.0 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=28.48 liquidity=2147074.75 spike=0.93
- AJWA.CA: score=18.3 buy_ready=False sector_rank=10 price=176.0 support=132.0 resistance=188.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.49 liquidity=8651353.0 spike=0.31
- ALCN.CA: score=12.22 buy_ready=False sector_rank=3 price=28.55 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.53 liquidity=14345603.0 spike=1.18
- ALUM.CA: score=4.82 buy_ready=False sector_rank=10 price=21.14 support=20.55 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=11.73 liquidity=5175541.5 spike=0.54
- AMER.CA: score=9.72 buy_ready=False sector_rank=13 price=2.43 support=2.28 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=19.28 liquidity=82251896.0 spike=1.16
- AMES.CA: score=9.64 buy_ready=False sector_rank=10 price=66.03 support=57.23 resistance=66.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=156619984.0 spike=36.57
- AMIA.CA: score=9.18 buy_ready=False sector_rank=10 price=8.78 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=28.97 liquidity=6533987.5 spike=0.48
- AMOC.CA: score=9.05 buy_ready=False sector_rank=16 price=7.7 support=7.42 resistance=8.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.54 liquidity=33609424.0 spike=0.7
- ANFI.CA: score=5.98 buy_ready=False sector_rank=10 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=STALE RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=-0.06 buy_ready=False sector_rank=10 price=8.34 support=8.0 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=7.62 liquidity=1013003.19 spike=1.14
- ARAB.CA: score=14.4 buy_ready=False sector_rank=13 price=0.21 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=55.88 liquidity=27731398.0 spike=0.32
- ARCC.CA: score=9.29 buy_ready=False sector_rank=15 price=55.09 support=53.0 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.87 liquidity=28603048.0 spike=0.84
- AREH.CA: score=19.64 buy_ready=False sector_rank=10 price=1.55 support=1.34 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=30293136.0 spike=0.88
- ARVA.CA: score=17.64 buy_ready=False sector_rank=10 price=10.7 support=9.43 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.86 liquidity=14057777.0 spike=0.44
- ASCM.CA: score=19.64 buy_ready=False sector_rank=10 price=59.2 support=47.7 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.53 liquidity=44833916.0 spike=0.48
- ASPI.CA: score=4.64 buy_ready=False sector_rank=10 price=0.32 support=0.31 resistance=0.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22102312.0 spike=0.31
- ATLC.CA: score=6.14 buy_ready=False sector_rank=12 price=5.3 support=4.97 resistance=5.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11277198.0 spike=1.83
- ATQA.CA: score=12.27 buy_ready=False sector_rank=20 price=9.45 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.19 liquidity=20470916.0 spike=0.62
- AXPH.CA: score=10.35 buy_ready=False sector_rank=10 price=1119.09 support=1073.0 resistance=1174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.94 liquidity=701340.44 spike=0.47
- BINV.CA: score=11.97 buy_ready=False sector_rank=17 price=46.5 support=44.02 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.7 liquidity=5032455.0 spike=0.5
- BIOC.CA: score=5.61 buy_ready=False sector_rank=10 price=69.22 support=66.75 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=35.71 liquidity=968940.56 spike=0.38
- BTFH.CA: score=13.84 buy_ready=False sector_rank=12 price=2.97 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.7 liquidity=214517184.0 spike=1.18
- CAED.CA: score=24.64 buy_ready=False sector_rank=10 price=71.96 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.96 liquidity=14602618.0 spike=3.52
- CANA.CA: score=19.9 buy_ready=False sector_rank=7 price=35.69 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=37.78 liquidity=26673762.0 spike=2.47
- CCAP.CA: score=8.94 buy_ready=False sector_rank=17 price=4.77 support=4.65 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=18.55 liquidity=277849280.0 spike=0.41
- CCRS.CA: score=7.4 buy_ready=False sector_rank=10 price=2.25 support=2.22 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=7753412.0 spike=0.45
- CEFM.CA: score=1.19 buy_ready=False sector_rank=10 price=100.16 support=95.75 resistance=109.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=20.18 liquidity=1544183.38 spike=0.86
- CERA.CA: score=14.27 buy_ready=False sector_rank=10 price=1.22 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=7625687.5 spike=0.46
- CFGH.CA: score=-1.35 buy_ready=False sector_rank=10 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=4880.0 spike=0.79
- CICH.CA: score=12.61 buy_ready=False sector_rank=12 price=11.99 support=11.1 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.77 liquidity=1123823.0 spike=0.34
- CIEB.CA: score=7.56 buy_ready=False sector_rank=7 price=23.66 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.06 liquidity=2592196.5 spike=0.39
- CIRA.CA: score=19.75 buy_ready=False sector_rank=9 price=28.16 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.39 liquidity=12354372.0 spike=0.73
- CLHO.CA: score=20.28 buy_ready=False sector_rank=5 price=16.75 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=66.94 liquidity=38441680.0 spike=1.05
- CNFN.CA: score=21.48 buy_ready=False sector_rank=12 price=4.72 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.55 liquidity=17017968.0 spike=0.41
- COMI.CA: score=14.96 buy_ready=False sector_rank=7 price=128.85 support=126.21 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.45 liquidity=533109888.0 spike=0.91
- COPR.CA: score=16.54 buy_ready=False sector_rank=10 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.55 liquidity=9895580.0 spike=0.35
- COSG.CA: score=9.64 buy_ready=False sector_rank=10 price=1.52 support=1.47 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=27.78 liquidity=14427278.0 spike=0.27
- CPCI.CA: score=19.78 buy_ready=False sector_rank=10 price=394.62 support=350.04 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=71.98 liquidity=5497673.5 spike=2.32
- CSAG.CA: score=27.62 buy_ready=False sector_rank=3 price=32.51 support=30.08 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.3 liquidity=31102658.0 spike=1.88
- DAPH.CA: score=13.47 buy_ready=False sector_rank=10 price=81.05 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=48.28 liquidity=4823981.5 spike=0.47
- DEIN.CA: score=5.64 buy_ready=False sector_rank=10 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=12.16 buy_ready=False sector_rank=6 price=26.95 support=23.7 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=70.34 liquidity=2068552.88 spike=0.52
- DSCW.CA: score=13.64 buy_ready=False sector_rank=10 price=1.74 support=1.71 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.11 liquidity=16415256.0 spike=0.47
- DTPP.CA: score=9.64 buy_ready=False sector_rank=10 price=166.05 support=153.55 resistance=166.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32460508.0 spike=16.14
- EALR.CA: score=0.87 buy_ready=False sector_rank=10 price=340.01 support=332.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=25.74 liquidity=1225294.5 spike=0.39
- EASB.CA: score=15.6 buy_ready=False sector_rank=10 price=7.34 support=4.66 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=75.15 liquidity=8952549.0 spike=0.69
- EAST.CA: score=9.1 buy_ready=False sector_rank=6 price=36.92 support=36.86 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.93 liquidity=27242458.0 spike=0.72
- EBSC.CA: score=5.15 buy_ready=False sector_rank=10 price=1.75 support=1.69 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=507534.66 spike=0.19
- ECAP.CA: score=14.67 buy_ready=False sector_rank=10 price=32.81 support=29.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.65 liquidity=5026036.5 spike=0.56
- EDFM.CA: score=-0.1 buy_ready=False sector_rank=10 price=330.59 support=320.29 resistance=355.0 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=30.71 liquidity=253893.12 spike=0.52
- EEII.CA: score=20.16 buy_ready=False sector_rank=10 price=2.46 support=2.3 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=16545014.0 spike=1.26
- EFIC.CA: score=1.56 buy_ready=False sector_rank=20 price=181.31 support=189.01 resistance=212.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=6.38 liquidity=3111983.75 spike=1.59
- EFID.CA: score=15.1 buy_ready=False sector_rank=6 price=27.4 support=25.5 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.64 liquidity=64346480.0 spike=0.84
- EFIH.CA: score=12.9 buy_ready=False sector_rank=21 price=20.29 support=20.0 resistance=22.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=36.37 liquidity=15478787.0 spike=0.35
- EGAL.CA: score=8.27 buy_ready=False sector_rank=20 price=286.18 support=272.28 resistance=334.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=10.71 liquidity=37530812.0 spike=0.59
- EGAS.CA: score=9.59 buy_ready=False sector_rank=16 price=49.58 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=44.48 liquidity=2536294.75 spike=0.27
- EGBE.CA: score=10.74 buy_ready=False sector_rank=7 price=0.45 support=0.43 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=113958.7 spike=1.33
- EGCH.CA: score=8.27 buy_ready=False sector_rank=20 price=12.2 support=12.13 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.35 liquidity=33307602.0 spike=0.63
- EGSA.CA: score=7.34 buy_ready=False sector_rank=14 price=8.75 support=8.55 resistance=9.1 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=42.86 liquidity=5801.25 spike=0.62
- EGTS.CA: score=12.4 buy_ready=False sector_rank=13 price=17.37 support=15.1 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.08 liquidity=35991000.0 spike=0.4
- EHDR.CA: score=12.64 buy_ready=False sector_rank=10 price=2.49 support=2.32 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.74 liquidity=22201680.0 spike=0.38
- EKHO.CA: score=6.05 buy_ready=False sector_rank=16 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=7.67 buy_ready=False sector_rank=19 price=2.08 support=2.05 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.14 liquidity=18397760.0 spike=0.96
- ELKA.CA: score=6.48 buy_ready=False sector_rank=10 price=1.33 support=1.21 resistance=1.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=77491032.0 spike=1.92
- ELNA.CA: score=-0.71 buy_ready=False sector_rank=10 price=37.81 support=35.55 resistance=41.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=33.43 liquidity=485619.25 spike=1.08
- ELSH.CA: score=17.64 buy_ready=False sector_rank=10 price=11.71 support=9.33 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.89 liquidity=62238348.0 spike=0.33
- ELWA.CA: score=3.78 buy_ready=False sector_rank=10 price=1.97 support=1.95 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=31.91 liquidity=1140425.0 spike=0.37
- EMFD.CA: score=17.4 buy_ready=False sector_rank=13 price=11.6 support=11.11 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.0 liquidity=85065784.0 spike=0.3
- ENGC.CA: score=21.53 buy_ready=False sector_rank=10 price=37.0 support=33.0 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=56.36 liquidity=9881519.0 spike=0.68
- EOSB.CA: score=-5.36 buy_ready=False sector_rank=10 price=1.48 support=1.48 resistance=1.48 source=StockAnalysis EGX public list (quote-only fallback) as_of=2026-06-30 freshness=QUOTE_ONLY RSI=50.0 liquidity=0.0 spike=0.0
- EPCO.CA: score=2.27 buy_ready=False sector_rank=10 price=8.7 support=8.5 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=28.31 liquidity=2630541.5 spike=0.31
- EPPK.CA: score=18.39 buy_ready=False sector_rank=10 price=13.67 support=11.67 resistance=13.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=70.53 liquidity=3841711.75 spike=3.45
- ETEL.CA: score=14.44 buy_ready=False sector_rank=14 price=92.87 support=89.01 resistance=97.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.42 liquidity=73944808.0 spike=1.05
- ETRS.CA: score=24.18 buy_ready=False sector_rank=10 price=10.77 support=8.5 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=167725488.0 spike=2.27
- EXPA.CA: score=8.54 buy_ready=False sector_rank=7 price=18.21 support=18.03 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.33 liquidity=8580202.0 spike=0.27
- FAIT.CA: score=21.88 buy_ready=False sector_rank=7 price=36.95 support=35.01 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.7 liquidity=8194786.5 spike=2.86
- FAITA.CA: score=4.98 buy_ready=False sector_rank=7 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=38.71 liquidity=14188.94 spike=0.35
- FERC.CA: score=1.7 buy_ready=False sector_rank=20 price=73.6 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=12.94 liquidity=4212608.5 spike=1.11
- FWRY.CA: score=12.9 buy_ready=False sector_rank=21 price=18.4 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.96 liquidity=134578128.0 spike=0.55
- GBCO.CA: score=21.1 buy_ready=False sector_rank=2 price=31.99 support=25.25 resistance=32.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=83.43 liquidity=123252440.0 spike=1.35
- GDWA.CA: score=8.64 buy_ready=False sector_rank=10 price=0.77 support=0.76 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=13923696.0 spike=0.99
- GGCC.CA: score=23.02 buy_ready=False sector_rank=10 price=0.48 support=0.4 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.68 liquidity=24904146.0 spike=2.19
- GIHD.CA: score=21.0 buy_ready=False sector_rank=10 price=42.13 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.44 liquidity=13802600.0 spike=1.68
- GMCI.CA: score=16.72 buy_ready=False sector_rank=10 price=1.78 support=1.66 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=2078454.0 spike=5.18
- GRCA.CA: score=6.23 buy_ready=False sector_rank=10 price=52.77 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.98 liquidity=1584342.75 spike=0.35
- GSSC.CA: score=1.6 buy_ready=False sector_rank=10 price=244.16 support=228.1 resistance=257.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=23.83 liquidity=1960335.88 spike=0.66
- GTWL.CA: score=9.64 buy_ready=False sector_rank=10 price=88.2 support=76.25 resistance=88.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=154179648.0 spike=6.17
- HDBK.CA: score=20.96 buy_ready=False sector_rank=7 price=158.96 support=138.0 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=66.54 liquidity=42756720.0 spike=1.5
- HELI.CA: score=17.4 buy_ready=False sector_rank=13 price=6.42 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=66623808.0 spike=0.58
- HRHO.CA: score=13.48 buy_ready=False sector_rank=12 price=26.7 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=61219340.0 spike=0.45
- ICID.CA: score=5.1 buy_ready=False sector_rank=10 price=8.39 support=7.57 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20543484.0 spike=1.23
- IDRE.CA: score=7.7 buy_ready=False sector_rank=10 price=42.33 support=41.1 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.22 liquidity=5056600.5 spike=0.38
- IFAP.CA: score=4.85 buy_ready=False sector_rank=18 price=19.2 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.08 liquidity=1942317.25 spike=0.29
- INFI.CA: score=1.01 buy_ready=False sector_rank=10 price=90.46 support=88.51 resistance=105.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=9.75 liquidity=2367974.75 spike=0.39
- IRON.CA: score=12.27 buy_ready=False sector_rank=20 price=32.72 support=30.51 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=48.72 liquidity=7938829.0 spike=1.03
- ISMA.CA: score=12.64 buy_ready=False sector_rank=10 price=28.59 support=25.99 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.55 liquidity=16863706.0 spike=0.46
- ISMQ.CA: score=20.27 buy_ready=False sector_rank=20 price=9.09 support=7.56 resistance=9.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.24 liquidity=106424912.0 spike=0.92
- ISPH.CA: score=15.18 buy_ready=False sector_rank=5 price=11.6 support=11.2 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.75 liquidity=37330124.0 spike=0.33
- JUFO.CA: score=18.1 buy_ready=False sector_rank=6 price=29.72 support=28.5 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=39.34 liquidity=12561703.0 spike=0.4
- KABO.CA: score=20.46 buy_ready=False sector_rank=8 price=6.37 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=42.25 liquidity=20222272.0 spike=1.25
- KWIN.CA: score=11.95 buy_ready=False sector_rank=10 price=67.68 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=8301524.0 spike=0.72
- KZPC.CA: score=2.08 buy_ready=False sector_rank=10 price=8.4 support=8.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=12.29 liquidity=3440788.75 spike=0.55
- LCSW.CA: score=21.97 buy_ready=False sector_rank=15 price=27.89 support=26.0 resistance=31.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.11 liquidity=38967744.0 spike=1.34
- LUTS.CA: score=4.78 buy_ready=False sector_rank=10 price=0.76 support=0.72 resistance=0.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48923928.0 spike=1.07
- MAAL.CA: score=18.64 buy_ready=False sector_rank=10 price=7.21 support=5.25 resistance=7.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=77.89 liquidity=11645760.0 spike=0.65
- MASR.CA: score=23.1 buy_ready=False sector_rank=10 price=7.32 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.61 liquidity=156703840.0 spike=2.73
- MBSC.CA: score=9.29 buy_ready=False sector_rank=15 price=237.5 support=222.66 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=14.67 liquidity=17386110.0 spike=0.51
- MCQE.CA: score=9.29 buy_ready=False sector_rank=15 price=170.64 support=166.66 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=24.62 liquidity=11746079.0 spike=0.82
- MCRO.CA: score=8.64 buy_ready=False sector_rank=10 price=1.2 support=1.17 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=29225090.0 spike=0.85
- MENA.CA: score=12.01 buy_ready=False sector_rank=13 price=6.83 support=6.32 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=52.69 liquidity=2609871.25 spike=0.2
- MEPA.CA: score=4.71 buy_ready=False sector_rank=10 price=1.56 support=1.52 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=17.24 liquidity=6070680.5 spike=0.54
- MFPC.CA: score=8.27 buy_ready=False sector_rank=20 price=35.17 support=34.22 resistance=43.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=9.0 liquidity=40326448.0 spike=0.47
- MFSC.CA: score=10.69 buy_ready=False sector_rank=10 price=46.96 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.33 liquidity=3042406.5 spike=0.35
- MHOT.CA: score=26.4 buy_ready=False sector_rank=1 price=33.77 support=28.83 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=63.86 liquidity=10149331.0 spike=0.49
- MICH.CA: score=18.16 buy_ready=False sector_rank=10 price=38.0 support=34.0 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.35 liquidity=8515557.0 spike=0.56
- MILS.CA: score=4.41 buy_ready=False sector_rank=10 price=128.91 support=126.5 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.31 liquidity=4762604.5 spike=0.5
- MIPH.CA: score=8.55 buy_ready=False sector_rank=5 price=656.35 support=630.13 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.04 liquidity=374939.31 spike=0.19
- MOED.CA: score=3.4 buy_ready=False sector_rank=10 price=0.68 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=34.35 liquidity=4752036.0 spike=0.51
- MOIL.CA: score=7.11 buy_ready=False sector_rank=16 price=0.47 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.21 liquidity=61454.88 spike=0.31
- MOIN.CA: score=4.7 buy_ready=False sector_rank=10 price=24.32 support=22.66 resistance=24.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5052587.5 spike=6.18
- MOSC.CA: score=12.04 buy_ready=False sector_rank=10 price=271.83 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=56.3 liquidity=4394625.5 spike=0.47
- MPCI.CA: score=20.34 buy_ready=False sector_rank=10 price=238.17 support=204.36 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=54.8 liquidity=128291184.0 spike=1.35
- MPCO.CA: score=16.91 buy_ready=False sector_rank=18 price=1.82 support=1.6 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.78 liquidity=57840328.0 spike=0.54
- MPRC.CA: score=16.64 buy_ready=False sector_rank=10 price=38.42 support=31.15 resistance=40.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=77.97 liquidity=15433790.0 spike=0.36
- MTIE.CA: score=21.4 buy_ready=False sector_rank=2 price=8.96 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.65 liquidity=14588864.0 spike=0.9
- NAHO.CA: score=8.47 buy_ready=False sector_rank=10 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=84917.81 spike=2.37
- NCCW.CA: score=12.64 buy_ready=False sector_rank=10 price=6.15 support=5.29 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=28.48 liquidity=12551172.0 spike=0.38
- NEDA.CA: score=-0.26 buy_ready=False sector_rank=10 price=2.74 support=2.68 resistance=2.84 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=33.33 liquidity=92390.06 spike=0.25
- NHPS.CA: score=9.64 buy_ready=False sector_rank=10 price=67.94 support=62.1 resistance=71.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24310658.0 spike=6.99
- NINH.CA: score=26.64 buy_ready=False sector_rank=10 price=18.16 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.18 liquidity=26266350.0 spike=6.27
- NIPH.CA: score=20.18 buy_ready=False sector_rank=5 price=163.19 support=157.01 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.84 liquidity=57979532.0 spike=0.84
- OBRI.CA: score=10.32 buy_ready=False sector_rank=10 price=32.84 support=31.5 resistance=37.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=30.98 liquidity=18960768.0 spike=1.34
- OCDI.CA: score=19.4 buy_ready=False sector_rank=13 price=24.69 support=20.0 resistance=25.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=66.71 liquidity=35830136.0 spike=0.47
- OCPH.CA: score=14.95 buy_ready=False sector_rank=10 price=352.54 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.47 liquidity=5309168.0 spike=0.85
- ODIN.CA: score=15.25 buy_ready=False sector_rank=10 price=2.11 support=1.94 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.3 liquidity=7609341.5 spike=0.69
- OFH.CA: score=8.64 buy_ready=False sector_rank=10 price=0.59 support=0.57 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=22.09 liquidity=12744279.0 spike=0.67
- OIH.CA: score=17.94 buy_ready=False sector_rank=17 price=1.41 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=30548004.0 spike=0.4
- OLFI.CA: score=20.62 buy_ready=False sector_rank=6 price=22.41 support=21.0 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.18 liquidity=26060128.0 spike=1.26
- ORAS.CA: score=4.6 buy_ready=False sector_rank=11 price=718.19 support=704.52 resistance=728.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=209002032.0 spike=1.0
- ORHD.CA: score=17.72 buy_ready=False sector_rank=13 price=37.68 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=53.68 liquidity=197574800.0 spike=1.16
- ORWE.CA: score=12.96 buy_ready=False sector_rank=8 price=22.44 support=21.95 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.64 liquidity=12032923.0 spike=0.34
- PHAR.CA: score=21.26 buy_ready=False sector_rank=5 price=87.39 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.72 liquidity=52380952.0 spike=1.54
- PHDC.CA: score=17.4 buy_ready=False sector_rank=13 price=14.6 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.1 liquidity=227825936.0 spike=0.56
- PHTV.CA: score=11.26 buy_ready=False sector_rank=10 price=271.6 support=201.55 resistance=275.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=90.82 liquidity=2613817.0 spike=0.18
- POUL.CA: score=21.88 buy_ready=False sector_rank=6 price=37.34 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=52.46 liquidity=9787203.0 spike=0.27
- PRCL.CA: score=19.41 buy_ready=False sector_rank=15 price=30.82 support=22.86 resistance=32.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.92 liquidity=42686000.0 spike=1.06
- PRDC.CA: score=17.4 buy_ready=False sector_rank=13 price=7.41 support=5.86 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.55 liquidity=64426372.0 spike=0.54
- PRMH.CA: score=16.34 buy_ready=False sector_rank=10 price=2.49 support=2.28 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.26 liquidity=8699348.0 spike=0.28
- RACC.CA: score=8.39 buy_ready=False sector_rank=10 price=9.7 support=9.36 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.84 liquidity=3746823.25 spike=0.4
- RAKT.CA: score=0.32 buy_ready=False sector_rank=10 price=21.67 support=21.96 resistance=24.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.46 liquidity=459327.47 spike=1.61
- RAYA.CA: score=7.88 buy_ready=False sector_rank=4 price=7.68 support=7.12 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=189392016.0 spike=2.26
- RMDA.CA: score=13.18 buy_ready=False sector_rank=5 price=4.95 support=4.81 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=30.3 liquidity=11750210.0 spike=0.15
- ROTO.CA: score=19.64 buy_ready=False sector_rank=10 price=41.39 support=33.0 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=66.01 liquidity=26997068.0 spike=0.93
- RREI.CA: score=12.67 buy_ready=False sector_rank=10 price=3.49 support=3.34 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.1 liquidity=8029510.5 spike=0.48
- RTVC.CA: score=5.91 buy_ready=False sector_rank=10 price=3.8 support=3.55 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.43 liquidity=5942854.0 spike=1.16
- RUBX.CA: score=22.52 buy_ready=False sector_rank=10 price=11.12 support=9.8 resistance=12.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.35 liquidity=25882804.0 spike=1.44
- SAUD.CA: score=6.73 buy_ready=False sector_rank=7 price=21.07 support=19.99 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=27.42 liquidity=6761773.5 spike=0.8
- SCEM.CA: score=15.81 buy_ready=False sector_rank=15 price=62.42 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.22 liquidity=30613420.0 spike=1.76
- SCFM.CA: score=2.18 buy_ready=False sector_rank=10 price=237.08 support=226.5 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.28 liquidity=2531842.5 spike=0.56
- SCTS.CA: score=9.75 buy_ready=False sector_rank=9 price=620.01 support=543.01 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20202018.0 spike=6.49
- SDTI.CA: score=10.8 buy_ready=False sector_rank=10 price=46.12 support=44.17 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.33 liquidity=3158336.25 spike=0.27
- SEIG.CA: score=11.15 buy_ready=False sector_rank=10 price=186.43 support=180.0 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=36.97 liquidity=1508273.75 spike=0.36
- SIPC.CA: score=5.5 buy_ready=False sector_rank=10 price=3.33 support=3.25 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=23.88 liquidity=5857327.0 spike=0.51
- SKPC.CA: score=7.27 buy_ready=False sector_rank=20 price=15.86 support=15.58 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.44 liquidity=22123138.0 spike=0.64
- SMFR.CA: score=0.12 buy_ready=False sector_rank=10 price=193.51 support=187.01 resistance=214.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=27.39 liquidity=474546.84 spike=0.22
- SNFC.CA: score=19.1 buy_ready=False sector_rank=10 price=12.22 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.46 liquidity=9452185.0 spike=0.55
- SPIN.CA: score=10.82 buy_ready=False sector_rank=8 price=14.16 support=13.3 resistance=14.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=53.9 liquidity=1861274.25 spike=0.31
- SPMD.CA: score=17.64 buy_ready=False sector_rank=10 price=0.42 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=11511867.0 spike=0.48
- SUGR.CA: score=6.92 buy_ready=False sector_rank=6 price=46.25 support=45.31 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=15.05 liquidity=7727452.5 spike=1.05
- SVCE.CA: score=17.64 buy_ready=False sector_rank=10 price=8.91 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=53.31 liquidity=13041635.0 spike=0.21
- SWDY.CA: score=13.67 buy_ready=False sector_rank=19 price=86.01 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.97 liquidity=11035011.0 spike=0.64
- TALM.CA: score=2.47 buy_ready=False sector_rank=9 price=15.71 support=15.38 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=28.89 liquidity=2721637.5 spike=0.37
- TMGH.CA: score=14.56 buy_ready=False sector_rank=13 price=94.32 support=92.1 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.8 liquidity=403056288.0 spike=1.08
- TRTO.CA: score=5.64 buy_ready=False sector_rank=10 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=235.59 spike=0.33
- UEFM.CA: score=7.77 buy_ready=False sector_rank=10 price=470.0 support=460.0 resistance=505.0 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=47.13 liquidity=1309420.0 spike=1.41
- UEGC.CA: score=17.64 buy_ready=False sector_rank=10 price=1.41 support=1.33 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=13096932.0 spike=0.55
- UNIP.CA: score=13.69 buy_ready=False sector_rank=10 price=0.33 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=49.41 liquidity=4049774.75 spike=0.17
- UNIT.CA: score=9.92 buy_ready=False sector_rank=13 price=12.86 support=12.0 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=16.59 liquidity=7225826.5 spike=1.15
- WCDF.CA: score=5.76 buy_ready=False sector_rank=10 price=518.05 support=450.0 resistance=547.9 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=38.07 liquidity=396308.24 spike=1.36
- WKOL.CA: score=0.26 buy_ready=False sector_rank=10 price=279.5 support=273.1 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=17.3 liquidity=612964.44 spike=0.22
- ZEOT.CA: score=19.64 buy_ready=False sector_rank=10 price=10.87 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.72 liquidity=27164106.0 spike=0.88
- ZMID.CA: score=4.48 buy_ready=False sector_rank=13 price=6.53 support=6.23 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=217092816.0 spike=1.04

## Backtesting Lite
- CSAG.CA: 180d return=13.61%, max drawdown=-28.0%, MA20>MA50 days last20=20, as_of=2026-06-28T21:00:00+00:00
- NINH.CA: 180d return=95.4%, max drawdown=-30.93%, MA20>MA50 days last20=15, as_of=2026-06-28T21:00:00+00:00
- MHOT.CA: 180d return=39.65%, max drawdown=-15.7%, MA20>MA50 days last20=20, as_of=2026-06-28T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CSAG.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Canal Shipping Agencies summary=Canal Shipping Agencies targets EGP 970m net profits in FY26/27; Canal Shipping Agencies’ stock rebounds; Canal Shipping Agencies mulls EGP 100m capital raise
  - Canal Shipping Agencies targets EGP 970m net profits in FY26/27: https://english.mubasher.info/news/4582423/Canal-Shipping-Agencies-targets-EGP-970m-net-profits-in-FY26-27/
  - Canal Shipping Agencies’ stock rebounds: https://english.mubasher.info/news/4564447/Canal-Shipping-Agencies-stock-rebounds/
  - Canal Shipping Agencies mulls EGP 100m capital raise: https://english.mubasher.info/news/4191441/Canal-Shipping-Agencies-mulls-EGP-100m-capital-raise/
- NINH.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=545 sources=3 expected=Nozha International Hospital summary=Nozha International Hospital’s net profits cross EGP 174m in 2025; Nozha International Hospital unveils EGP 58m capital increase, new asset details; Nozha International Hospital registers EGP 11.3m block trading
  - Nozha International Hospital’s net profits cross EGP 174m in 2025: https://english.mubasher.info/news/4558517/Nozha-International-Hospital-s-net-profits-cross-EGP-174m-in-2025/
  - Nozha International Hospital unveils EGP 58m capital increase, new asset details: https://english.mubasher.info/news/4558456/Nozha-International-Hospital-unveils-EGP-58m-capital-increase-new-asset-details/
  - Nozha International Hospital registers EGP 11.3m block trading: https://english.mubasher.info/news/4056645/Nozha-International-Hospital-registers-EGP-11-3m-block-trading/
- MHOT.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Hotels summary=Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26; Shareholder buys EGP 3.39m worth of shares in Misr Hotels; Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits
  - Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26: https://english.mubasher.info/news/4602482/Misr-Hotels-net-profits-cross-EGP-1-1bn-in-9M-25-26/
  - Shareholder buys EGP 3.39m worth of shares in Misr Hotels: https://english.mubasher.info/news/4013808/Shareholder-buys-EGP-3-39m-worth-of-shares-in-Misr-Hotels/
  - Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits: https://english.mubasher.info/news/3975543/Misr-Hotels-repays-EGP-383m-of-NBE-s-loan-unveils-estimated-profits/
- CAED.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Educational Services SAE summary=Cairo Educational Services&#39; OGM approves EGP 1/shr coupon distribution; Cairo Educational Services’ board proposes 80 piastres per-share dividends; Cairo Educational Services’ profit declines in FY18/19
  - Cairo Educational Services&#39; OGM approves EGP 1/shr coupon distribution: https://english.mubasher.info/news/3884789/Cairo-Educational-Services-OGM-approves-EGP-1-shr-coupon-distribution/
  - Cairo Educational Services’ board proposes 80 piastres per-share dividends: https://english.mubasher.info/news/3556129/Cairo-Educational-Services-board-proposes-80-piastres-per-share-dividends/
  - Cairo Educational Services’ profit declines in FY18/19: https://english.mubasher.info/news/3556119/Cairo-Educational-Services-profit-declines-in-FY18-19/
- ETRS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Transport and Commercial Services Company S.A.E. summary=Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- MASR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=545 sources=3 expected=Madinet Masr For Housing and Development summary=Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval; Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended; Madinet Masr to distribute treasury stocks in first-ever move
  - Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval: https://english.mubasher.info/news/4601386/Madinet-Masr-to-pay-out-EGP-0-15-shr-for-2025-upon-equityholders-approval/
  - Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended: https://english.mubasher.info/news/4578449/Madinet-Masr-logs-24-higher-consolidated-profits-in-2025-dividends-recommended/
  - Madinet Masr to distribute treasury stocks in first-ever move: https://english.mubasher.info/news/4577724/Madinet-Masr-to-distribute-treasury-stocks-in-first-ever-move/
- GGCC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Giza General - Contracting and Real Estate Investment S.A.E summary=EGX approves listing EGP 144m capital increase for Giza Contracting; Giza Contracting tests key EGP 0.51 level; Giza Contracting’s consolidated net profits leap to EGP 140m in 9M-25
  - EGX approves listing EGP 144m capital increase for Giza Contracting: https://english.mubasher.info/news/4588793/EGX-approves-listing-EGP-144m-capital-increase-for-Giza-Contracting/
  - Giza Contracting tests key EGP 0.51 level: https://english.mubasher.info/news/4563778/Giza-Contracting-tests-key-EGP-0-51-level/
  - Giza Contracting’s consolidated net profits leap to EGP 140m in 9M-25: https://english.mubasher.info/news/4530408/Giza-Contracting-s-consolidated-net-profits-leap-to-EGP-140m-in-9M-25/
- RUBX.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Rubex International for Plastic and Acrylic Manufacturing summary=Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.

## Warnings
- Evidence for CSAG.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for NINH.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for MHOT.CA matches the company but no source/report date was detected.
- Evidence for CAED.CA matches the company but no source/report date was detected.
- Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- Evidence for MASR.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for GGCC.CA matches the company but no source/report date was detected.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
