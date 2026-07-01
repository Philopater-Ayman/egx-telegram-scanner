# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-07-01T10:14:13.243110+00:00
Generated Cairo: 2026-07-01 13:14
Run timing: target 09:15 Cairo | generated Cairo 2026-07-01 13:14 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-07-01 13:09

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 180/190
- Top sector: Technology & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, July 01
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 25.0% / above MA50 30.0%
- EGX70 regime: BEARISH / above MA20 55.0% / above MA50 65.0%
- Sector breadth: 19.05%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=402755328.0 spike=0.61 score=9.51
- COMI.CA: liquidity=200983584.0 spike=0.34 score=15.02
- RUBX.CA: liquidity=162849920.0 spike=8.61 score=10.16
- BTFH.CA: liquidity=154345568.0 spike=0.84 score=14.38
- GTWL.CA: liquidity=152754528.0 spike=4.69 score=24.16

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b-20230311:free
- Summary: Scanner flagged several stocks with accumulation spikes and bullish watch scores, but the EGX30/EGX70 bearish trend and low sector breadth keep risk mode defensive, so no new buys are advised.
- NHPS.CA, SCTS.CA, LCSW.CA show accumulation spikes with liquidity well above average, placing them near key support levels (within 10‑15%).
- RAYA.CA and MTIE.CA have high outlook scores (>90) and are close to resistance, suggesting short‑term upside if momentum holds.
- EGX30 is BEARISH (only 25% above MA20, median 5‑day return –1%) and EGX70 similarly BEARISH, keeping sector breadth at ~19% and risk mode DEFENSIVE_NO_NEW_BUY.
- Given the bearish regime, the bullish watch signals are uncertain; a reversal or sideways move is likely over the next 1‑3 days.

## Top Liquidity Spikes
- DTPP.CA: spike=33.19 liquidity=120354064.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- NHPS.CA: spike=14.53 liquidity=65117400.0 outlook=BULLISH_WATCH score=78.9 buy_ready=False
- RUBX.CA: spike=8.61 liquidity=162849920.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AXPH.CA: spike=7.68 liquidity=11030647.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GTWL.CA: spike=4.69 liquidity=152754528.0 outlook=CONSTRUCTIVE score=54.9 buy_ready=False

## Sector Leaderboard
- #1 Technology & Distribution: score=10.78 5d=8.17% 20d=2.67% aboveMA50=100.0%
- #2 Automotive & Distribution: score=9.62 5d=1.53% 20d=10.05% aboveMA50=100.0%
- #3 Education: score=6.31 5d=-1.75% 20d=0.67% aboveMA50=66.67%
- #4 Tourism & Leisure: score=5.31 5d=-4.44% 20d=2.64% aboveMA50=100.0%
- #5 Transportation & Logistics: score=4.7 5d=2.98% 20d=-0.3% aboveMA50=50.0%
- #6 Agriculture & Food Production: score=3.52 5d=-1.68% 20d=4.71% aboveMA50=50.0%
- #7 Non-bank Financial Services: score=3.44 5d=-0.09% 20d=-1.73% aboveMA50=40.0%
- #8 Real Estate: score=3.41 5d=0.09% 20d=-2.39% aboveMA50=76.92%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MTIE.CA: BULLISH_WATCH score=94.62 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- LCSW.CA: BULLISH_WATCH score=90.34 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- SCTS.CA: BULLISH_WATCH score=89.31 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=below MA50
- NIPH.CA: BULLISH_WATCH score=85.37 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- EEII.CA: BULLISH_WATCH score=84.9 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ELKA.CA: BULLISH_WATCH score=81.9 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CNFN.CA: BULLISH_WATCH score=79.44 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- NHPS.CA: BULLISH_WATCH score=78.9 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- IDRE.CA: BULLISH_WATCH score=78.9 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- GMCI.CA: BULLISH_WATCH score=78.9 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=11.76 buy_ready=False sector_rank=10 price=206.02 support=196.0 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=53.3 liquidity=3598405.25 spike=0.58
- ABUK.CA: score=8.64 buy_ready=False sector_rank=20 price=68.49 support=66.66 resistance=83.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=14.29 liquidity=57675016.0 spike=0.43
- ACAMD.CA: score=18.16 buy_ready=False sector_rank=10 price=2.23 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=19493640.0 spike=0.16
- ACGC.CA: score=10.75 buy_ready=False sector_rank=15 price=9.2 support=8.92 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=39.66 liquidity=6199674.0 spike=0.18
- ADCI.CA: score=11.03 buy_ready=False sector_rank=10 price=242.99 support=211.0 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=76.1 liquidity=3865212.75 spike=0.37
- ADIB.CA: score=20.02 buy_ready=False sector_rank=12 price=46.9 support=44.01 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=65.91 liquidity=47857052.0 spike=0.53
- ADPC.CA: score=6.88 buy_ready=False sector_rank=10 price=3.47 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=2722663.5 spike=0.14
- AFDI.CA: score=11.39 buy_ready=False sector_rank=10 price=44.21 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=54.95 liquidity=1228271.25 spike=0.08
- AFMC.CA: score=5.8 buy_ready=False sector_rank=10 price=70.4 support=66.0 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=46.38 liquidity=636702.19 spike=0.28
- AJWA.CA: score=12.91 buy_ready=False sector_rank=10 price=180.0 support=132.15 resistance=190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=78.37 liquidity=7749237.0 spike=0.28
- ALCN.CA: score=8.9 buy_ready=False sector_rank=5 price=28.26 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=55.9 liquidity=3024080.75 spike=0.25
- ALUM.CA: score=1.5 buy_ready=False sector_rank=10 price=21.24 support=20.55 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=20.0 liquidity=1341439.0 spike=0.14
- AMER.CA: score=10.36 buy_ready=False sector_rank=8 price=2.42 support=2.28 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=33.78 liquidity=23045012.0 spike=0.32
- AMES.CA: score=10.16 buy_ready=False sector_rank=10 price=62.59 support=62.05 resistance=69.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=47865960.0 spike=3.92
- AMIA.CA: score=9.65 buy_ready=False sector_rank=10 price=8.7 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=45.28 liquidity=1486396.75 spike=0.12
- AMOC.CA: score=9.32 buy_ready=False sector_rank=17 price=7.75 support=7.42 resistance=8.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=34.4 liquidity=16311763.0 spike=0.34
- ANFI.CA: score=6.49 buy_ready=False sector_rank=10 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=STALE RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=5.7 buy_ready=False sector_rank=10 price=8.34 support=8.0 resistance=9.21 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=36.94 liquidity=1015003.04 spike=1.26
- ARAB.CA: score=15.36 buy_ready=False sector_rank=8 price=0.21 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=63.89 liquidity=26139252.0 spike=0.33
- ARCC.CA: score=13.39 buy_ready=False sector_rank=13 price=55.44 support=53.0 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=45.61 liquidity=8457181.0 spike=0.25
- AREH.CA: score=20.16 buy_ready=False sector_rank=10 price=1.54 support=1.34 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=15181943.0 spike=0.43
- ARVA.CA: score=10.76 buy_ready=False sector_rank=10 price=10.89 support=9.82 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=46.76 liquidity=2597060.0 spike=0.08
- ASCM.CA: score=20.16 buy_ready=False sector_rank=10 price=59.57 support=49.72 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=59.92 liquidity=15259380.0 spike=0.16
- ASPI.CA: score=17.51 buy_ready=False sector_rank=10 price=0.32 support=0.27 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=45.69 liquidity=9349538.0 spike=0.13
- ATLC.CA: score=14.17 buy_ready=False sector_rank=7 price=5.23 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=62.9 liquidity=3796153.0 spike=0.57
- ATQA.CA: score=12.64 buy_ready=False sector_rank=20 price=9.5 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=46.63 liquidity=18251354.0 spike=0.54
- AXPH.CA: score=10.16 buy_ready=False sector_rank=10 price=1232.11 support=1090.02 resistance=1235.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11030647.0 spike=7.68
- BINV.CA: score=12.55 buy_ready=False sector_rank=16 price=46.5 support=44.02 resistance=48.89 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=52.7 liquidity=5046459.0 spike=0.99
- BIOC.CA: score=6.38 buy_ready=False sector_rank=10 price=71.27 support=66.75 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=46.18 liquidity=1221272.88 spike=0.48
- BTFH.CA: score=14.38 buy_ready=False sector_rank=7 price=2.94 support=2.95 resistance=3.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=41.07 liquidity=154345568.0 spike=0.84
- CAED.CA: score=12.92 buy_ready=False sector_rank=10 price=72.85 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=53.5 liquidity=2763374.5 spike=0.6
- CANA.CA: score=7.85 buy_ready=False sector_rank=12 price=35.79 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=46.39 liquidity=834832.0 spike=0.07
- CCAP.CA: score=9.51 buy_ready=False sector_rank=16 price=4.94 support=4.65 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=28.89 liquidity=402755328.0 spike=0.61
- CCRS.CA: score=13.45 buy_ready=False sector_rank=10 price=2.29 support=2.18 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=37.7 liquidity=5290471.5 spike=0.36
- CEFM.CA: score=5.5 buy_ready=False sector_rank=10 price=101.08 support=95.75 resistance=109.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=35.08 liquidity=339495.63 spike=0.19
- CERA.CA: score=16.15 buy_ready=False sector_rank=10 price=1.23 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=6991311.5 spike=0.41
- CFGH.CA: score=-0.84 buy_ready=False sector_rank=10 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=707.6 spike=0.12
- CICH.CA: score=10.98 buy_ready=False sector_rank=7 price=11.9 support=11.1 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=57.96 liquidity=1608829.25 spike=0.55
- CIEB.CA: score=9.66 buy_ready=False sector_rank=12 price=23.83 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=51.06 liquidity=2636874.75 spike=0.4
- CIRA.CA: score=20.9 buy_ready=False sector_rank=3 price=29.0 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=70.05 liquidity=21273726.0 spike=1.25
- CLHO.CA: score=20.35 buy_ready=False sector_rank=9 price=16.47 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=72.12 liquidity=23946076.0 spike=0.62
- CNFN.CA: score=22.38 buy_ready=False sector_rank=7 price=4.79 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=20509998.0 spike=0.49
- COMI.CA: score=15.02 buy_ready=False sector_rank=12 price=127.62 support=126.21 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=40.94 liquidity=200983584.0 spike=0.34
- COPR.CA: score=11.26 buy_ready=False sector_rank=10 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=43.55 liquidity=4096188.0 spike=0.15
- COSG.CA: score=10.16 buy_ready=False sector_rank=10 price=1.53 support=1.47 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=32.43 liquidity=12914919.0 spike=0.24
- CPCI.CA: score=13.42 buy_ready=False sector_rank=10 price=401.95 support=350.04 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=77.94 liquidity=3523897.0 spike=1.37
- CSAG.CA: score=21.93 buy_ready=False sector_rank=5 price=32.43 support=30.08 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=69.76 liquidity=9047881.0 spike=0.51
- DAPH.CA: score=12.21 buy_ready=False sector_rank=10 price=81.41 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=56.28 liquidity=3045654.5 spike=0.31
- DEIN.CA: score=6.16 buy_ready=False sector_rank=10 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=10.59 buy_ready=False sector_rank=11 price=27.03 support=23.7 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=80.08 liquidity=3493767.25 spike=0.87
- DSCW.CA: score=14.16 buy_ready=False sector_rank=10 price=1.73 support=1.71 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=13302586.0 spike=0.39
- DTPP.CA: score=10.16 buy_ready=False sector_rank=10 price=191.99 support=183.0 resistance=199.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=120354064.0 spike=33.19
- EALR.CA: score=1.53 buy_ready=False sector_rank=10 price=342.0 support=332.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=31.03 liquidity=1371964.5 spike=0.45
- EASB.CA: score=20.68 buy_ready=False sector_rank=10 price=7.66 support=4.66 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=72.71 liquidity=16734018.0 spike=1.26
- EAST.CA: score=14.1 buy_ready=False sector_rank=11 price=37.4 support=36.63 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=42.07 liquidity=12014316.0 spike=0.31
- EBSC.CA: score=-2.61 buy_ready=False sector_rank=10 price=1.93 support=1.74 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2230795.25 spike=0.82
- ECAP.CA: score=16.8 buy_ready=False sector_rank=10 price=33.27 support=29.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=59.15 liquidity=6642897.5 spike=0.73
- EDFM.CA: score=0.41 buy_ready=False sector_rank=10 price=330.59 support=320.29 resistance=355.0 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=17.77 liquidity=246620.14 spike=0.52
- EEII.CA: score=21.44 buy_ready=False sector_rank=10 price=2.5 support=2.3 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=57.63 liquidity=22423782.0 spike=1.64
- EFIC.CA: score=5.13 buy_ready=False sector_rank=20 price=189.46 support=180.02 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=4.61 liquidity=4810696.0 spike=2.34
- EFID.CA: score=11.57 buy_ready=False sector_rank=11 price=27.22 support=25.5 resistance=29.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=45.86 liquidity=6472763.5 spike=0.08
- EFIH.CA: score=12.2 buy_ready=False sector_rank=21 price=20.37 support=20.0 resistance=22.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=42.98 liquidity=9300681.0 spike=0.22
- EGAL.CA: score=8.64 buy_ready=False sector_rank=20 price=284.07 support=272.28 resistance=332.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=29.65 liquidity=20082124.0 spike=0.33
- EGAS.CA: score=9.63 buy_ready=False sector_rank=17 price=49.44 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=48.29 liquidity=2311668.0 spike=0.27
- EGBE.CA: score=11.57 buy_ready=False sector_rank=12 price=0.45 support=0.43 resistance=0.47 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=55.36 liquidity=113399.07 spike=1.72
- EGCH.CA: score=8.64 buy_ready=False sector_rank=20 price=12.38 support=12.13 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=24.58 liquidity=13175740.0 spike=0.25
- EGSA.CA: score=2.0 buy_ready=False sector_rank=19 price=8.75 support=8.55 resistance=9.09 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=85.71 liquidity=446.25 spike=0.05
- EGTS.CA: score=18.36 buy_ready=False sector_rank=8 price=17.76 support=15.1 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=43.25 liquidity=38193956.0 spike=0.44
- EHDR.CA: score=15.91 buy_ready=False sector_rank=10 price=2.51 support=2.37 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=7749976.0 spike=0.13
- EKHO.CA: score=6.32 buy_ready=False sector_rank=17 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=8.67 buy_ready=False sector_rank=18 price=2.09 support=2.04 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=40.74 liquidity=5494408.5 spike=0.31
- ELKA.CA: score=23.52 buy_ready=False sector_rank=10 price=1.38 support=1.19 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=58.54 liquidity=96122136.0 spike=2.18
- ELNA.CA: score=-0.17 buy_ready=False sector_rank=10 price=37.81 support=35.55 resistance=41.51 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=33.8 liquidity=486123.19 spike=1.09
- ELSH.CA: score=13.16 buy_ready=False sector_rank=10 price=11.72 support=11.1 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=25.76 liquidity=10496914.0 spike=0.05
- ELWA.CA: score=4.29 buy_ready=False sector_rank=10 price=1.97 support=1.95 resistance=2.22 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=32.61 liquidity=1126922.76 spike=0.58
- EMFD.CA: score=18.36 buy_ready=False sector_rank=8 price=11.6 support=11.11 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=51.12 liquidity=27999158.0 spike=0.1
- ENGC.CA: score=16.67 buy_ready=False sector_rank=10 price=36.91 support=33.0 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=63.74 liquidity=4512388.5 spike=0.31
- EOSB.CA: score=12.19 buy_ready=False sector_rank=10 price=1.48 support=1.39 resistance=1.55 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=28383.44 spike=0.22
- EPCO.CA: score=6.82 buy_ready=False sector_rank=10 price=8.72 support=8.5 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=40.13 liquidity=1655315.13 spike=0.21
- EPPK.CA: score=9.59 buy_ready=False sector_rank=10 price=14.18 support=11.67 resistance=13.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=80.49 liquidity=431337.66 spike=0.33
- ETEL.CA: score=10.66 buy_ready=False sector_rank=19 price=92.55 support=89.01 resistance=97.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=49.15 liquidity=6654073.5 spike=0.09
- ETRS.CA: score=22.16 buy_ready=False sector_rank=10 price=10.59 support=8.6 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=62.41 liquidity=53399180.0 spike=0.65
- EXPA.CA: score=10.02 buy_ready=False sector_rank=12 price=18.25 support=18.03 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=34.56 liquidity=11250384.0 spike=0.36
- FAIT.CA: score=10.22 buy_ready=False sector_rank=12 price=36.53 support=35.01 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=57.02 liquidity=2200369.5 spike=0.74
- FAITA.CA: score=5.03 buy_ready=False sector_rank=12 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=40.63 liquidity=14194.2 spike=0.43
- FERC.CA: score=-0.24 buy_ready=False sector_rank=20 price=73.49 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=23.2 liquidity=2122362.25 spike=0.54
- FWRY.CA: score=12.9 buy_ready=False sector_rank=21 price=18.41 support=17.71 resistance=20.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=21371676.0 spike=0.09
- GBCO.CA: score=22.4 buy_ready=False sector_rank=2 price=32.2 support=25.25 resistance=32.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=89.02 liquidity=17174204.0 spike=0.18
- GDWA.CA: score=6.28 buy_ready=False sector_rank=10 price=0.77 support=0.76 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=39.5 liquidity=2119268.25 spike=0.15
- GGCC.CA: score=19.82 buy_ready=False sector_rank=10 price=0.48 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=87.0 liquidity=22988360.0 spike=1.83
- GIHD.CA: score=12.57 buy_ready=False sector_rank=10 price=42.28 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=60.39 liquidity=2410579.5 spike=0.28
- GMCI.CA: score=16.88 buy_ready=False sector_rank=10 price=1.86 support=1.66 resistance=1.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=59.26 liquidity=1320904.5 spike=2.7
- GRCA.CA: score=5.63 buy_ready=False sector_rank=10 price=52.19 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:13 AM market time freshness=DELAYED_CURRENT RSI=53.45 liquidity=471316.78 spike=0.11
- GSSC.CA: score=6.18 buy_ready=False sector_rank=10 price=245.15 support=228.1 resistance=256.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=35.95 liquidity=1016083.88 spike=0.36
- GTWL.CA: score=24.16 buy_ready=False sector_rank=10 price=92.06 support=45.47 resistance=88.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=91.91 liquidity=152754528.0 spike=4.69
- HDBK.CA: score=20.02 buy_ready=False sector_rank=12 price=161.8 support=138.0 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=73.68 liquidity=12954000.0 spike=0.43
- HELI.CA: score=18.36 buy_ready=False sector_rank=8 price=6.44 support=6.28 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=21687654.0 spike=0.2
- HRHO.CA: score=14.38 buy_ready=False sector_rank=7 price=26.66 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=62.31 liquidity=32563576.0 spike=0.25
- ICID.CA: score=12.06 buy_ready=False sector_rank=10 price=8.04 support=5.5 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=78.53 liquidity=2899803.5 spike=0.16
- IDRE.CA: score=20.16 buy_ready=False sector_rank=10 price=44.35 support=41.1 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=45.21 liquidity=12396153.0 spike=0.95
- IFAP.CA: score=6.99 buy_ready=False sector_rank=6 price=19.17 support=18.47 resistance=20.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=47.66 liquidity=580497.88 spike=0.09
- INFI.CA: score=4.75 buy_ready=False sector_rank=10 price=93.34 support=88.51 resistance=104.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=23.06 liquidity=5589280.5 spike=0.93
- IRON.CA: score=9.87 buy_ready=False sector_rank=20 price=32.4 support=30.51 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=55.6 liquidity=3235967.75 spike=0.42
- ISMA.CA: score=11.93 buy_ready=False sector_rank=10 price=28.48 support=26.22 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=32.38 liquidity=8767599.0 spike=0.26
- ISMQ.CA: score=18.64 buy_ready=False sector_rank=20 price=9.35 support=7.56 resistance=9.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=72.4 liquidity=107215152.0 spike=0.9
- ISPH.CA: score=15.35 buy_ready=False sector_rank=9 price=11.6 support=11.2 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=46.42 liquidity=10216192.0 spike=0.09
- JUFO.CA: score=11.37 buy_ready=False sector_rank=11 price=29.66 support=28.5 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=51.92 liquidity=3269225.0 spike=0.1
- KABO.CA: score=16.55 buy_ready=False sector_rank=15 price=6.26 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=63.08 liquidity=8994987.0 spike=0.56
- KWIN.CA: score=8.37 buy_ready=False sector_rank=10 price=67.89 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=40.07 liquidity=4213742.0 spike=0.36
- KZPC.CA: score=1.16 buy_ready=False sector_rank=10 price=8.41 support=8.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=8.85 liquidity=1995845.38 spike=0.32
- LCSW.CA: score=24.98 buy_ready=False sector_rank=13 price=28.6 support=26.0 resistance=31.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=55.63 liquidity=76561400.0 spike=2.52
- LUTS.CA: score=18.16 buy_ready=False sector_rank=10 price=0.75 support=0.56 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=67.74 liquidity=13292660.0 spike=0.28
- MAAL.CA: score=13.75 buy_ready=False sector_rank=10 price=7.19 support=5.44 resistance=7.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=85.87 liquidity=4593873.5 spike=0.26
- MASR.CA: score=20.16 buy_ready=False sector_rank=10 price=7.28 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=60.09 liquidity=34771636.0 spike=0.55
- MBSC.CA: score=4.92 buy_ready=False sector_rank=13 price=239.2 support=222.66 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=32.85 liquidity=4987034.0 spike=0.15
- MCQE.CA: score=6.58 buy_ready=False sector_rank=13 price=171.34 support=166.66 resistance=199.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=34.8 liquidity=6641941.5 spike=0.48
- MCRO.CA: score=14.16 buy_ready=False sector_rank=10 price=1.2 support=1.17 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=10866891.0 spike=0.31
- MENA.CA: score=12.98 buy_ready=False sector_rank=8 price=6.83 support=6.41 resistance=7.75 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=51.11 liquidity=2612543.27 spike=0.3
- MEPA.CA: score=2.26 buy_ready=False sector_rank=10 price=1.57 support=1.52 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=26.92 liquidity=3103654.25 spike=0.28
- MFPC.CA: score=8.64 buy_ready=False sector_rank=20 price=35.92 support=34.22 resistance=43.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=15.93 liquidity=34654640.0 spike=0.42
- MFSC.CA: score=7.24 buy_ready=False sector_rank=10 price=50.08 support=47.0 resistance=53.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16257752.0 spike=2.04
- MHOT.CA: score=17.96 buy_ready=False sector_rank=4 price=34.61 support=28.83 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=68.18 liquidity=6834977.0 spike=0.37
- MICH.CA: score=14.41 buy_ready=False sector_rank=10 price=37.74 support=34.0 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=51.63 liquidity=4249991.0 spike=0.27
- MILS.CA: score=8.03 buy_ready=False sector_rank=10 price=129.7 support=126.31 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=36.79 liquidity=2867805.75 spike=0.31
- MIPH.CA: score=5.72 buy_ready=False sector_rank=9 price=656.35 support=630.13 resistance=710.0 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=49.25 liquidity=375432.19 spike=0.24
- MOED.CA: score=9.47 buy_ready=False sector_rank=10 price=0.69 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=48.63 liquidity=3305815.5 spike=0.36
- MOIL.CA: score=7.33 buy_ready=False sector_rank=17 price=0.47 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=50.94 liquidity=10722.45 spike=0.05
- MOIN.CA: score=4.46 buy_ready=False sector_rank=10 price=23.93 support=22.6 resistance=25.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=39.45 liquidity=303515.19 spike=0.3
- MOSC.CA: score=7.38 buy_ready=False sector_rank=10 price=268.68 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=53.87 liquidity=2218166.0 spike=0.24
- MPCI.CA: score=20.16 buy_ready=False sector_rank=10 price=245.26 support=204.36 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=59.99 liquidity=53009380.0 spike=0.55
- MPCO.CA: score=20.41 buy_ready=False sector_rank=6 price=1.85 support=1.6 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=58.21 liquidity=26149098.0 spike=0.24
- MPRC.CA: score=19.16 buy_ready=False sector_rank=10 price=38.18 support=31.15 resistance=40.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=85.5 liquidity=20045600.0 spike=0.46
- MTIE.CA: score=23.7 buy_ready=False sector_rank=2 price=9.15 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=52.89 liquidity=19045774.0 spike=1.15
- NAHO.CA: score=10.04 buy_ready=False sector_rank=10 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=84760.25 spike=2.9
- NCCW.CA: score=14.13 buy_ready=False sector_rank=10 price=6.13 support=5.29 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=41.86 liquidity=5973244.5 spike=0.18
- NEDA.CA: score=5.38 buy_ready=False sector_rank=10 price=2.74 support=2.68 resistance=2.84 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=35.29 liquidity=223674.42 spike=0.62
- NHPS.CA: score=29.16 buy_ready=False sector_rank=10 price=71.0 support=61.55 resistance=71.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=62.04 liquidity=65117400.0 spike=14.53
- NINH.CA: score=15.61 buy_ready=False sector_rank=10 price=18.06 support=16.8 resistance=18.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=71.37 liquidity=7632497.0 spike=1.41
- NIPH.CA: score=21.57 buy_ready=False sector_rank=9 price=171.58 support=157.01 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=52.9 liquidity=110326648.0 spike=1.61
- OBRI.CA: score=10.16 buy_ready=False sector_rank=10 price=34.95 support=33.12 resistance=36.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=68514152.0 spike=4.61
- OCDI.CA: score=17.36 buy_ready=False sector_rank=8 price=25.27 support=20.0 resistance=25.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=76.98 liquidity=52561256.0 spike=0.67
- OCPH.CA: score=13.17 buy_ready=False sector_rank=10 price=355.16 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=51.93 liquidity=3006417.25 spike=0.47
- ODIN.CA: score=19.39 buy_ready=False sector_rank=10 price=2.18 support=1.99 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=53.66 liquidity=9233841.0 spike=0.83
- OFH.CA: score=12.81 buy_ready=False sector_rank=10 price=0.6 support=0.57 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=38.57 liquidity=8652393.0 spike=0.46
- OIH.CA: score=18.51 buy_ready=False sector_rank=16 price=1.41 support=1.33 resistance=1.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=63.16 liquidity=19777784.0 spike=0.26
- OLFI.CA: score=20.1 buy_ready=False sector_rank=11 price=22.2 support=21.0 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=58.59 liquidity=12866437.0 spike=0.61
- ORAS.CA: score=4.6 buy_ready=False sector_rank=14 price=724.03 support=722.0 resistance=733.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=106671280.0 spike=1.0
- ORHD.CA: score=20.36 buy_ready=False sector_rank=8 price=38.09 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=59.76 liquidity=30143402.0 spike=0.17
- ORWE.CA: score=5.0 buy_ready=False sector_rank=15 price=22.36 support=21.95 resistance=24.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=33.9 liquidity=5447017.0 spike=0.16
- PHAR.CA: score=12.92 buy_ready=False sector_rank=9 price=87.51 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=55.96 liquidity=2568507.0 spike=0.07
- PHDC.CA: score=18.36 buy_ready=False sector_rank=8 price=14.62 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=48.46 liquidity=78795624.0 spike=0.2
- PHTV.CA: score=10.18 buy_ready=False sector_rank=10 price=272.68 support=201.55 resistance=277.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=95.04 liquidity=1016494.0 spike=0.07
- POUL.CA: score=22.1 buy_ready=False sector_rank=11 price=38.13 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=56.03 liquidity=27196456.0 spike=0.78
- PRCL.CA: score=19.94 buy_ready=False sector_rank=13 price=32.33 support=22.86 resistance=32.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=74.2 liquidity=38795236.0 spike=0.93
- PRDC.CA: score=18.36 buy_ready=False sector_rank=8 price=7.55 support=5.91 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=68.88 liquidity=26886292.0 spike=0.22
- PRMH.CA: score=14.41 buy_ready=False sector_rank=10 price=2.5 support=2.34 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=42.72 liquidity=6248078.0 spike=0.2
- RACC.CA: score=7.5 buy_ready=False sector_rank=10 price=9.7 support=9.36 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=58.0 liquidity=2336159.5 spike=0.27
- RAKT.CA: score=1.04 buy_ready=False sector_rank=10 price=21.67 support=21.4 resistance=24.1 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=29.78 liquidity=456456.88 spike=1.71
- RAYA.CA: score=24.4 buy_ready=False sector_rank=1 price=7.69 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=67.29 liquidity=55511544.0 spike=0.65
- RMDA.CA: score=12.04 buy_ready=False sector_rank=9 price=4.95 support=4.81 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=42.17 liquidity=3692509.25 spike=0.05
- ROTO.CA: score=20.16 buy_ready=False sector_rank=10 price=41.8 support=33.06 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=73.17 liquidity=15957028.0 spike=0.53
- RREI.CA: score=7.48 buy_ready=False sector_rank=10 price=3.5 support=3.34 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=54.29 liquidity=2324383.0 spike=0.14
- RTVC.CA: score=6.4 buy_ready=False sector_rank=10 price=3.8 support=3.55 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=42.25 liquidity=1235450.63 spike=0.23
- RUBX.CA: score=10.16 buy_ready=False sector_rank=10 price=12.6 support=11.22 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=162849920.0 spike=8.61
- SAUD.CA: score=8.17 buy_ready=False sector_rank=12 price=21.25 support=19.99 resistance=22.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=45.19 liquidity=3146704.0 spike=0.37
- SCEM.CA: score=14.28 buy_ready=False sector_rank=13 price=63.38 support=59.3 resistance=66.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=55.52 liquidity=4344729.0 spike=0.25
- SCFM.CA: score=2.27 buy_ready=False sector_rank=10 price=239.69 support=226.5 resistance=269.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=30.05 liquidity=2111741.75 spike=0.48
- SCTS.CA: score=25.14 buy_ready=False sector_rank=3 price=605.95 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=58.45 liquidity=11276486.0 spike=2.87
- SDTI.CA: score=10.68 buy_ready=False sector_rank=10 price=46.55 support=44.35 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=46.34 liquidity=2518214.5 spike=0.22
- SEIG.CA: score=12.75 buy_ready=False sector_rank=10 price=192.0 support=180.0 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=62.3 liquidity=2586869.75 spike=0.63
- SIPC.CA: score=1.83 buy_ready=False sector_rank=10 price=3.34 support=3.25 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=1673283.5 spike=0.14
- SKPC.CA: score=7.64 buy_ready=False sector_rank=20 price=15.9 support=15.58 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=27.78 liquidity=12664880.0 spike=0.38
- SMFR.CA: score=5.64 buy_ready=False sector_rank=10 price=193.51 support=187.01 resistance=214.0 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=38.45 liquidity=475647.57 spike=0.28
- SNFC.CA: score=12.98 buy_ready=False sector_rank=10 price=12.08 support=11.68 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=53.47 liquidity=4822725.5 spike=0.3
- SPIN.CA: score=9.25 buy_ready=False sector_rank=15 price=14.05 support=13.3 resistance=14.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=65.52 liquidity=2694445.5 spike=0.45
- SPMD.CA: score=16.22 buy_ready=False sector_rank=10 price=0.43 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=52.7 liquidity=6059727.0 spike=0.25
- SUGR.CA: score=0.4 buy_ready=False sector_rank=11 price=46.68 support=45.31 resistance=51.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=19.88 liquidity=1296580.75 spike=0.17
- SVCE.CA: score=5.16 buy_ready=False sector_rank=10 price=9.47 support=8.96 resistance=9.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39226628.0 spike=0.63
- SWDY.CA: score=10.93 buy_ready=False sector_rank=18 price=86.53 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=49.08 liquidity=3748545.75 spike=0.22
- TALM.CA: score=17.43 buy_ready=False sector_rank=3 price=16.07 support=15.38 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=37.76 liquidity=5028943.0 spike=0.69
- TMGH.CA: score=15.36 buy_ready=False sector_rank=8 price=94.65 support=92.1 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=50.44 liquidity=94232696.0 spike=0.26
- TRTO.CA: score=6.16 buy_ready=False sector_rank=10 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=9.48 buy_ready=False sector_rank=10 price=479.01 support=460.0 resistance=505.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=47.04 liquidity=322637.69 spike=0.31
- UEGC.CA: score=13.58 buy_ready=False sector_rank=10 price=1.43 support=1.33 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=52.78 liquidity=3422940.75 spike=0.14
- UNIP.CA: score=9.66 buy_ready=False sector_rank=10 price=0.32 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=54.44 liquidity=1502206.0 spike=0.06
- UNIT.CA: score=4.2 buy_ready=False sector_rank=8 price=13.06 support=12.0 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=30.74 liquidity=831911.56 spike=0.13
- WCDF.CA: score=5.39 buy_ready=False sector_rank=10 price=518.05 support=450.0 resistance=547.9 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=37.6 liquidity=230532.24 spike=0.82
- WKOL.CA: score=0.9 buy_ready=False sector_rank=10 price=281.54 support=273.1 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=19.72 liquidity=735573.56 spike=0.27
- ZEOT.CA: score=20.16 buy_ready=False sector_rank=10 price=11.2 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=70.13 liquidity=30343852.0 spike=0.95
- ZMID.CA: score=22.36 buy_ready=False sector_rank=8 price=6.57 support=5.96 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=63.45 liquidity=60575916.0 spike=0.28

## Backtesting Lite
- NHPS.CA: 180d return=5.84%, max drawdown=-40.18%, MA20>MA50 days last20=12, as_of=2026-06-29T21:00:00+00:00
- SCTS.CA: 180d return=237.76%, max drawdown=-25.28%, MA20>MA50 days last20=16, as_of=2026-06-29T21:00:00+00:00
- LCSW.CA: 180d return=4.49%, max drawdown=-15.87%, MA20>MA50 days last20=20, as_of=2026-06-29T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- NHPS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=National Company for Housing Professional Syndicates SAE summary=Evidence rejected for NHPS.CA: source text did not clearly match NHPS.CA / National Company for Housing Professional Syndicates SAE.
- SCTS.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Suez Canal Company for Technology Settling summary=Suez Canal Technology’s consolidated net profits cross EGP 1.5bn in H1-25/26; Suez Canal Technology’s shareholders greenlight EGP 11/shr dividends; Suez Canal Technology logs EGP 1.3bn consolidated profits in FY23/24
  - Suez Canal Technology’s consolidated net profits cross EGP 1.5bn in H1-25/26: https://english.mubasher.info/news/4600018/Suez-Canal-Technology-s-consolidated-net-profits-cross-EGP-1-5bn-in-H1-25-26/
  - Suez Canal Technology’s shareholders greenlight EGP 11/shr dividends: https://english.mubasher.info/news/4463096/Suez-Canal-Technology-s-shareholders-greenlight-EGP-11-shr-dividends/
  - Suez Canal Technology logs EGP 1.3bn consolidated profits in FY23/24: https://english.mubasher.info/news/4366060/Suez-Canal-Technology-logs-EGP-1-3bn-consolidated-profits-in-FY23-24/
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- RAYA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=546 sources=3 expected=Raya Holding summary=Raya stock maintains bullish momentum above EGP 9; Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt; Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn
  - Raya stock maintains bullish momentum above EGP 9: https://english.mubasher.info/news/4601857/Raya-stock-maintains-bullish-momentum-above-EGP-9/
  - Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt: https://english.mubasher.info/news/4577815/Aman-Holding-MSMEDA-partner-to-inject-EGP-300m-into-SMEs-across-Egypt/
  - Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn: https://english.mubasher.info/news/4564195/Raya-Holding-s-consolidated-profits-surge-in-2025-revenues-hit-EGP-63-8bn/
- GTWL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Golden Textiles & Clothes Wool summary=Golden Textiles profits jump 214%; Golden Textiles OGM OKs 50 piasters/shr dividends; Golden Textiles consolidated profits down 18.5% in FY16
  - Golden Textiles profits jump 214%: https://english.mubasher.info/news/3108548/Golden-Textiles-profits-jump-214-/
  - Golden Textiles OGM OKs 50 piasters/shr dividends: https://english.mubasher.info/news/3103061/Golden-Textiles-OGM-OKs-50-piasters-shr-dividends/
  - Golden Textiles consolidated profits down 18.5% in FY16: https://english.mubasher.info/news/3092552/Golden-Textiles-consolidated-profits-down-18-5-in-FY16/
- MTIE.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=MM Group For Industry and International Trade summary=Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- ELKA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=546 sources=3 expected=Cairo for Housing and Development Company (S.A.E) summary=Cairo for Housing’s consolidated profits near EGP 599m in 2025; Cairo Housing stock tests important demand zone; Cairo Housing unveils EGP 398m capital hike via H1-25’s share premium
  - Cairo for Housing’s consolidated profits near EGP 599m in 2025: https://english.mubasher.info/news/4579798/Cairo-for-Housing-s-consolidated-profits-near-EGP-599m-in-2025/
  - Cairo Housing stock tests important demand zone: https://english.mubasher.info/news/4547365/Cairo-Housing-stock-tests-important-demand-zone/
  - Cairo Housing unveils EGP 398m capital hike via H1-25’s share premium: https://english.mubasher.info/news/4540047/Cairo-Housing-unveils-EGP-398m-capital-hike-via-H1-25-s-share-premium/
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.

## Warnings
- Evidence rejected for NHPS.CA: source text did not clearly match NHPS.CA / National Company for Housing Professional Syndicates SAE.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for SCTS.CA matches the company but no source/report date was detected.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence for RAYA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for GTWL.CA matches the company but no source/report date was detected.
- Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- Evidence for ELKA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
