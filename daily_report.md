# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-08-24T06:09:43.471189+00:00
Generated Cairo: 2026-08-24 09:09
Run timing: target 08:45 Cairo | generated Cairo 2026-08-24 09:09 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-08-24 09:06

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 167/189
- Top sector: Education

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, August 23
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 75.0% / above MA50 80.0%
- EGX70 regime: MIXED / above MA20 65.79% / above MA50 81.58%
- Sector breadth: 33.33%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=1386235520.0 spike=2.33 score=28.06
- NIPH.CA: liquidity=600648000.0 spike=1.99 score=8.38
- PHAR.CA: liquidity=448855776.0 spike=1.02 score=21.44
- MPCI.CA: liquidity=359661184.0 spike=2.21 score=8.21
- LUTS.CA: liquidity=343806944.0 spike=2.36 score=8.51

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 show mixed trends with weak sector breadth (33%), triggering DEFENSIVE_NO_NEW_BUY risk mode; scanner flags several tickets with accumulation spikes but mixed outlook and extended momentum, so no new buys are advised.
- CCAP.CA shows accumulation spike (liquidity 2.33×) and BULLISH_WATCH outlook, yet momentum is extended and sector not leading, limiting near‑term upside.
- TALM.CA (Education sector) has tradeable liquidity, BULLISH_WATCH outlook, but liquidity is cooling and price sits far above 20‑day support, suggesting limited short‑term pull‑back.
- COPR.CA and EMFD.CA display strong accumulation spikes with RSI near overbought (74‑64) and prices close to resistance, indicating possible short‑term consolidation or reversal.
- Overall, mixed EGX30/EGX70 regime and defensive risk mode increase uncertainty for 1‑3 day moves, so scanner maintains HOLD stance.

## Top Liquidity Spikes
- GRCA.CA: spike=8.53 liquidity=226897392.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AXPH.CA: spike=4.38 liquidity=28777630.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EMFD.CA: spike=3.62 liquidity=218317104.0 outlook=BULLISH_WATCH score=71.74 buy_ready=False
- MOED.CA: spike=3.38 liquidity=250753856.0 outlook=CONSTRUCTIVE score=62.47 buy_ready=False
- AMIA.CA: spike=3.19 liquidity=109916608.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Education: score=10.01 5d=0.4% 20d=17.32% aboveMA50=100.0%
- #2 Transportation & Logistics: score=9.74 5d=-1.54% 20d=14.23% aboveMA50=100.0%
- #3 Building Materials: score=9.7 5d=-1.94% 20d=20.36% aboveMA50=100.0%
- #4 Agriculture & Food Production: score=9.39 5d=-1.62% 20d=13.87% aboveMA50=100.0%
- #5 Banking & Financials: score=7.9 5d=0.24% 20d=9.59% aboveMA50=90.0%
- #6 Fintech & Payments: score=7.89 5d=1.12% 20d=2.14% aboveMA50=100.0%
- #7 Textiles: score=7.85 5d=1.59% 20d=6.26% aboveMA50=75.0%
- #8 Investment Holding: score=7.61 5d=3.83% 20d=1.63% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ALCN.CA: BULLISH_WATCH score=98.74 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- SCTS.CA: BULLISH_WATCH score=96 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- LCSW.CA: BULLISH_WATCH score=94.7 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- UNIT.CA: BULLISH_WATCH score=91.74 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CIRA.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- KABO.CA: BULLISH_WATCH score=86.85 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- TALM.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- IFAP.CA: BULLISH_WATCH score=85.39 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- CCAP.CA: BULLISH_WATCH score=83.61 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- ADIB.CA: BULLISH_WATCH score=77.9 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=22.79 buy_ready=False sector_rank=15 price=327.62 support=235.7 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=53.37 liquidity=50691392.0 spike=0.85
- ABUK.CA: score=23.4 buy_ready=False sector_rank=12 price=76.5 support=70.6 resistance=80.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=54.85 liquidity=44915380.0 spike=0.4
- ACAMD.CA: score=11.23 buy_ready=False sector_rank=15 price=2.05 support=2.09 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=31.75 liquidity=72470720.0 spike=1.22
- ACGC.CA: score=20.4 buy_ready=False sector_rank=7 price=13.75 support=10.12 resistance=13.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=77.37 liquidity=37983740.0 spike=0.87
- ADCI.CA: score=20.79 buy_ready=False sector_rank=15 price=301.25 support=245.0 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=48.93 liquidity=13513163.0 spike=0.61
- ADIB.CA: score=21.4 buy_ready=False sector_rank=5 price=54.2 support=48.62 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=51.58 liquidity=30535496.0 spike=0.28
- ADPC.CA: score=18.79 buy_ready=False sector_rank=15 price=4.05 support=3.81 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=22302662.0 spike=0.42
- AFDI.CA: score=18.79 buy_ready=False sector_rank=15 price=64.74 support=48.35 resistance=69.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=66.32 liquidity=14852780.0 spike=0.6
- AFMC.CA: score=20.79 buy_ready=False sector_rank=15 price=227.0 support=102.11 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=53.06 liquidity=39969092.0 spike=0.23
- AJWA.CA: score=18.79 buy_ready=False sector_rank=15 price=185.11 support=175.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=51.21 liquidity=38539592.0 spike=0.83
- ALCN.CA: score=24.48 buy_ready=False sector_rank=2 price=31.61 support=28.8 resistance=32.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=65.03 liquidity=36716352.0 spike=1.54
- ALUM.CA: score=16.78 buy_ready=False sector_rank=15 price=26.97 support=22.72 resistance=30.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=68.23 liquidity=5991108.5 spike=0.29
- AMER.CA: score=20.5 buy_ready=False sector_rank=16 price=5.96 support=4.14 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=59.61 liquidity=66447660.0 spike=0.66
- AMES.CA: score=21.83 buy_ready=False sector_rank=15 price=150.0 support=110.54 resistance=173.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=69.62 liquidity=106213368.0 spike=1.52
- AMIA.CA: score=10.17 buy_ready=False sector_rank=15 price=18.81 support=15.92 resistance=19.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=109916608.0 spike=3.19
- AMOC.CA: score=21.4 buy_ready=False sector_rank=9 price=11.23 support=8.23 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=72.41 liquidity=107800776.0 spike=0.8
- APSW.CA: score=8.95 buy_ready=False sector_rank=15 price=8.75 support=8.6 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=52.67 liquidity=1162971.0 spike=0.6
- ARAB.CA: score=21.7 buy_ready=False sector_rank=16 price=0.24 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=36.67 liquidity=201205680.0 spike=2.6
- ARCC.CA: score=19.4 buy_ready=False sector_rank=3 price=72.25 support=55.4 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=79.63 liquidity=34768660.0 spike=0.35
- AREH.CA: score=14.7 buy_ready=False sector_rank=15 price=1.47 support=1.38 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=54.0 liquidity=8914691.0 spike=0.28
- ARVA.CA: score=5.79 buy_ready=False sector_rank=15 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=13.79 buy_ready=False sector_rank=15 price=63.36 support=60.99 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=34.64 liquidity=20851956.0 spike=0.36
- ASPI.CA: score=21.93 buy_ready=False sector_rank=15 price=0.53 support=0.36 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=66.37 liquidity=64017036.0 spike=1.57
- ATLC.CA: score=19.71 buy_ready=False sector_rank=18 price=5.48 support=5.0 resistance=5.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=45.31 liquidity=12014879.0 spike=0.63
- ATQA.CA: score=18.62 buy_ready=False sector_rank=12 price=10.99 support=9.66 resistance=11.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=77.25 liquidity=85446968.0 spike=1.11
- AXPH.CA: score=10.79 buy_ready=False sector_rank=15 price=1529.25 support=1443.0 resistance=1599.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28777630.0 spike=4.38
- BINV.CA: score=9.92 buy_ready=False sector_rank=8 price=48.09 support=46.01 resistance=50.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:12 PM market time freshness=DELAYED_CURRENT RSI=54.73 liquidity=523361.03 spike=0.08
- BIOC.CA: score=5.79 buy_ready=False sector_rank=15 price=487.49 support=433.8 resistance=501.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=226799568.0 spike=0.96
- BTFH.CA: score=8.71 buy_ready=False sector_rank=18 price=3.01 support=2.98 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=97567008.0 spike=0.44
- CAED.CA: score=17.79 buy_ready=False sector_rank=15 price=166.81 support=118.0 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=78.03 liquidity=34530096.0 spike=0.62
- CANA.CA: score=18.4 buy_ready=False sector_rank=5 price=42.1 support=36.5 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=76.15 liquidity=20110572.0 spike=0.95
- CCAP.CA: score=28.06 buy_ready=False sector_rank=8 price=5.79 support=5.14 resistance=5.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=62.37 liquidity=1386235520.0 spike=2.33
- CCRS.CA: score=9.68 buy_ready=False sector_rank=15 price=2.44 support=2.4 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=34.78 liquidity=8887490.0 spike=0.52
- CEFM.CA: score=24.79 buy_ready=False sector_rank=15 price=148.55 support=121.4 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=63.22 liquidity=14232416.0 spike=0.38
- CERA.CA: score=19.11 buy_ready=False sector_rank=15 price=1.31 support=1.23 resistance=1.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=35.71 liquidity=18944066.0 spike=1.16
- CFGH.CA: score=0.23 buy_ready=False sector_rank=15 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=57910.9 spike=3.19
- CICH.CA: score=9.38 buy_ready=False sector_rank=18 price=12.28 support=11.92 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:12 PM market time freshness=DELAYED_CURRENT RSI=38.75 liquidity=1666869.75 spike=0.24
- CIEB.CA: score=19.88 buy_ready=False sector_rank=5 price=25.0 support=23.75 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=60.23 liquidity=6478388.0 spike=0.47
- CIRA.CA: score=24.4 buy_ready=False sector_rank=1 price=36.71 support=31.61 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=52.16 liquidity=14237598.0 spike=0.26
- CLHO.CA: score=21.4 buy_ready=False sector_rank=10 price=17.71 support=16.0 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=36.44 liquidity=37435736.0 spike=0.59
- CNFN.CA: score=18.09 buy_ready=False sector_rank=18 price=4.89 support=4.68 resistance=5.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=47.17 liquidity=23226604.0 spike=1.19
- COMI.CA: score=14.4 buy_ready=False sector_rank=5 price=139.12 support=135.35 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=28.45 liquidity=254878272.0 spike=0.53
- COPR.CA: score=25.61 buy_ready=False sector_rank=15 price=0.54 support=0.39 resistance=0.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=74.44 liquidity=186126032.0 spike=2.41
- COSG.CA: score=22.17 buy_ready=False sector_rank=15 price=1.87 support=1.6 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=69.44 liquidity=85521744.0 spike=1.69
- CPCI.CA: score=20.33 buy_ready=False sector_rank=15 price=551.38 support=440.01 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=67.16 liquidity=14766757.0 spike=1.77
- CSAG.CA: score=23.4 buy_ready=False sector_rank=2 price=41.02 support=31.35 resistance=43.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=73.88 liquidity=11511413.0 spike=0.48
- DAPH.CA: score=6.69 buy_ready=False sector_rank=15 price=118.02 support=112.52 resistance=125.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=60801704.0 spike=1.45
- DEIN.CA: score=-4.21 buy_ready=False sector_rank=15 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=11.98 buy_ready=False sector_rank=17 price=28.13 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=57.91 liquidity=3569626.5 spike=0.23
- DSCW.CA: score=18.79 buy_ready=False sector_rank=15 price=1.96 support=1.89 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=44.23 liquidity=49749172.0 spike=0.54
- DTPP.CA: score=18.79 buy_ready=False sector_rank=15 price=293.29 support=225.11 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=71.07 liquidity=30147236.0 spike=0.54
- EALR.CA: score=22.79 buy_ready=False sector_rank=15 price=398.58 support=362.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=48.71 liquidity=31160502.0 spike=0.64
- EASB.CA: score=10.62 buy_ready=False sector_rank=15 price=7.21 support=6.71 resistance=8.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=4833233.5 spike=0.49
- EAST.CA: score=16.41 buy_ready=False sector_rank=17 price=36.22 support=36.0 resistance=37.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=42.21 liquidity=11538380.0 spike=0.19
- EBSC.CA: score=8.26 buy_ready=False sector_rank=15 price=1.9 support=1.85 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=48.0 liquidity=2476116.75 spike=0.46
- ECAP.CA: score=17.28 buy_ready=False sector_rank=15 price=37.02 support=32.12 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=57.82 liquidity=4494554.0 spike=0.36
- EDFM.CA: score=10.52 buy_ready=False sector_rank=15 price=405.04 support=352.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:09 PM market time freshness=DELAYED_CURRENT RSI=65.26 liquidity=1732896.75 spike=0.43
- EEII.CA: score=8.85 buy_ready=False sector_rank=15 price=2.88 support=2.82 resistance=3.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=59564300.0 spike=2.53
- EFIC.CA: score=23.4 buy_ready=False sector_rank=12 price=213.33 support=184.0 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=61.75 liquidity=17380980.0 spike=0.38
- EFID.CA: score=17.41 buy_ready=False sector_rank=17 price=33.03 support=26.64 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=83.6 liquidity=27390228.0 spike=0.3
- EFIH.CA: score=21.4 buy_ready=False sector_rank=6 price=24.76 support=22.15 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=65.65 liquidity=68003768.0 spike=0.57
- EGAL.CA: score=21.4 buy_ready=False sector_rank=12 price=331.6 support=292.0 resistance=359.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=70.89 liquidity=73482072.0 spike=0.71
- EGAS.CA: score=11.15 buy_ready=False sector_rank=9 price=59.07 support=50.0 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=30.48 liquidity=4754067.0 spike=0.19
- EGBE.CA: score=9.54 buy_ready=False sector_rank=5 price=0.55 support=0.47 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=69.5 liquidity=139842.02 spike=0.66
- EGCH.CA: score=21.4 buy_ready=False sector_rank=12 price=13.91 support=12.69 resistance=14.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=52.29 liquidity=94324256.0 spike=0.77
- EGSA.CA: score=7.12 buy_ready=False sector_rank=13 price=8.69 support=8.65 resistance=9.0 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=36.36 liquidity=17380.0 spike=1.44
- EGTS.CA: score=16.64 buy_ready=False sector_rank=16 price=17.0 support=16.63 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=42.76 liquidity=53684212.0 spike=1.57
- EHDR.CA: score=22.79 buy_ready=False sector_rank=15 price=2.95 support=2.71 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=58.62 liquidity=17305486.0 spike=0.41
- EKHO.CA: score=7.4 buy_ready=False sector_rank=9 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=10.4 buy_ready=False sector_rank=11 price=2.09 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=27.78 liquidity=41164268.0 spike=0.66
- ELKA.CA: score=18.79 buy_ready=False sector_rank=15 price=1.73 support=1.69 resistance=2.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=46.15 liquidity=55682024.0 spike=0.81
- ELNA.CA: score=0.38 buy_ready=False sector_rank=15 price=37.01 support=36.1 resistance=39.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:12 PM market time freshness=DELAYED_CURRENT RSI=30.18 liquidity=531806.94 spike=1.03
- ELSH.CA: score=10.79 buy_ready=False sector_rank=15 price=13.25 support=13.14 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=24.49 liquidity=33715976.0 spike=0.43
- ELWA.CA: score=17.38 buy_ready=False sector_rank=15 price=1.82 support=1.62 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:10 PM market time freshness=DELAYED_CURRENT RSI=47.5 liquidity=4211685.5 spike=2.69
- EMFD.CA: score=25.5 buy_ready=False sector_rank=16 price=12.1 support=11.08 resistance=12.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=63.58 liquidity=218317104.0 spike=3.62
- ENGC.CA: score=5.79 buy_ready=False sector_rank=15 price=47.66 support=45.49 resistance=49.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18241972.0 spike=0.64
- EOSB.CA: score=12.79 buy_ready=False sector_rank=15 price=1.55 support=1.53 resistance=1.62 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=266.6 spike=0.01
- EPCO.CA: score=15.91 buy_ready=False sector_rank=15 price=11.2 support=10.32 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=52.75 liquidity=7123890.5 spike=0.28
- EPPK.CA: score=1.77 buy_ready=False sector_rank=15 price=12.58 support=12.62 resistance=15.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=23.4 liquidity=900314.5 spike=1.04
- ETEL.CA: score=23.22 buy_ready=False sector_rank=13 price=117.89 support=102.5 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=52.91 liquidity=83452184.0 spike=0.59
- ETRS.CA: score=22.79 buy_ready=False sector_rank=15 price=11.01 support=10.21 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=58.79 liquidity=10601037.0 spike=0.34
- EXPA.CA: score=19.52 buy_ready=False sector_rank=5 price=20.28 support=19.6 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=50.16 liquidity=40027204.0 spike=1.06
- FAIT.CA: score=15.0 buy_ready=False sector_rank=5 price=42.5 support=36.1 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=72.89 liquidity=3601196.0 spike=0.83
- FAITA.CA: score=13.41 buy_ready=False sector_rank=5 price=0.99 support=0.96 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=57.75 liquidity=9818.35 spike=0.19
- FERC.CA: score=18.4 buy_ready=False sector_rank=12 price=77.59 support=75.01 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=51.99 liquidity=11307991.0 spike=0.49
- FWRY.CA: score=23.4 buy_ready=False sector_rank=6 price=19.16 support=18.69 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=51.28 liquidity=92848792.0 spike=0.78
- GBCO.CA: score=12.57 buy_ready=False sector_rank=21 price=29.51 support=29.31 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=44.83 liquidity=28007988.0 spike=0.56
- GDWA.CA: score=9.79 buy_ready=False sector_rank=15 price=0.79 support=0.78 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=33.87 liquidity=24177106.0 spike=0.23
- GGCC.CA: score=18.79 buy_ready=False sector_rank=15 price=0.94 support=0.81 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=55.65 liquidity=16341473.0 spike=0.32
- GIHD.CA: score=18.79 buy_ready=False sector_rank=15 price=61.63 support=56.51 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=19133914.0 spike=0.46
- GMCI.CA: score=0.86 buy_ready=False sector_rank=15 price=1.91 support=1.88 resistance=2.1 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=17.39 liquidity=71053.91 spike=0.14
- GRCA.CA: score=10.79 buy_ready=False sector_rank=15 price=74.4 support=63.0 resistance=74.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=226897392.0 spike=8.53
- GSSC.CA: score=19.56 buy_ready=False sector_rank=15 price=285.69 support=264.0 resistance=301.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=48.98 liquidity=8768184.0 spike=0.46
- GTWL.CA: score=14.79 buy_ready=False sector_rank=15 price=185.89 support=186.1 resistance=186.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=211558112.0 spike=1.0
- HDBK.CA: score=14.4 buy_ready=False sector_rank=5 price=92.44 support=80.8 resistance=93.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=76.45 liquidity=14280399.0 spike=0.34
- HELI.CA: score=13.5 buy_ready=False sector_rank=16 price=7.8 support=7.5 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=21.26 liquidity=72162024.0 spike=0.44
- HRHO.CA: score=13.71 buy_ready=False sector_rank=18 price=26.3 support=25.95 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=46.92 liquidity=54526660.0 spike=0.55
- ICID.CA: score=21.27 buy_ready=False sector_rank=15 price=17.49 support=7.85 resistance=16.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=98.22 liquidity=39025864.0 spike=1.74
- IDRE.CA: score=16.98 buy_ready=False sector_rank=15 price=52.73 support=46.04 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=60.43 liquidity=6195852.5 spike=0.22
- IFAP.CA: score=21.4 buy_ready=False sector_rank=4 price=20.72 support=19.0 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=11843563.0 spike=0.39
- INFI.CA: score=20.79 buy_ready=False sector_rank=15 price=158.54 support=104.0 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=72.54 liquidity=42404044.0 spike=0.69
- IRON.CA: score=18.04 buy_ready=False sector_rank=12 price=30.8 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=56.8 liquidity=14303062.0 spike=1.32
- ISMA.CA: score=19.79 buy_ready=False sector_rank=15 price=35.34 support=28.11 resistance=36.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=89.06 liquidity=15770488.0 spike=0.53
- ISMQ.CA: score=19.4 buy_ready=False sector_rank=12 price=9.22 support=8.96 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=41484420.0 spike=0.73
- ISPH.CA: score=21.4 buy_ready=False sector_rank=10 price=13.31 support=11.3 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=61.93 liquidity=109739232.0 spike=0.58
- JUFO.CA: score=13.41 buy_ready=False sector_rank=17 price=26.88 support=22.78 resistance=29.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=83.06 liquidity=12456745.0 spike=0.21
- KABO.CA: score=23.36 buy_ready=False sector_rank=7 price=9.12 support=7.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=69.69 liquidity=83990656.0 spike=1.98
- KWIN.CA: score=6.51 buy_ready=False sector_rank=15 price=96.56 support=96.53 resistance=107.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=80077224.0 spike=1.36
- KZPC.CA: score=8.71 buy_ready=False sector_rank=15 price=13.81 support=13.75 resistance=15.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=96539104.0 spike=2.46
- LCSW.CA: score=22.4 buy_ready=False sector_rank=3 price=34.65 support=30.2 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=45.34 liquidity=39510872.0 spike=0.9
- LUTS.CA: score=8.51 buy_ready=False sector_rank=15 price=1.59 support=1.58 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=343806944.0 spike=2.36
- MAAL.CA: score=14.43 buy_ready=False sector_rank=15 price=8.82 support=8.32 resistance=9.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=42.59 liquidity=3644192.75 spike=0.29
- MASR.CA: score=18.79 buy_ready=False sector_rank=15 price=7.72 support=7.45 resistance=8.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=35.42 liquidity=35027092.0 spike=0.51
- MBSC.CA: score=19.4 buy_ready=False sector_rank=3 price=366.55 support=240.02 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=83.28 liquidity=21317312.0 spike=0.27
- MCQE.CA: score=22.4 buy_ready=False sector_rank=3 price=224.02 support=178.0 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=65.47 liquidity=19854984.0 spike=0.37
- MCRO.CA: score=20.79 buy_ready=False sector_rank=15 price=1.55 support=1.44 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=52.27 liquidity=92406104.0 spike=0.52
- MENA.CA: score=11.45 buy_ready=False sector_rank=16 price=6.99 support=6.82 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:11 PM market time freshness=DELAYED_CURRENT RSI=47.27 liquidity=2957239.0 spike=0.48
- MEPA.CA: score=18.79 buy_ready=False sector_rank=15 price=1.87 support=1.78 resistance=2.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=10516768.0 spike=0.17
- MFPC.CA: score=23.4 buy_ready=False sector_rank=12 price=39.27 support=35.37 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=63.91 liquidity=48988808.0 spike=0.59
- MFSC.CA: score=9.92 buy_ready=False sector_rank=15 price=50.26 support=46.02 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=26.1 liquidity=4132419.75 spike=0.36
- MHOT.CA: score=19.13 buy_ready=False sector_rank=14 price=18.27 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=61.01 liquidity=16632545.0 spike=0.96
- MICH.CA: score=20.79 buy_ready=False sector_rank=15 price=49.5 support=39.01 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=70.61 liquidity=23693116.0 spike=0.57
- MILS.CA: score=22.79 buy_ready=False sector_rank=15 price=219.01 support=165.55 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=57.01 liquidity=72744360.0 spike=0.82
- MIPH.CA: score=15.08 buy_ready=False sector_rank=10 price=794.08 support=722.7 resistance=828.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=54.24 liquidity=3682336.5 spike=0.91
- MOED.CA: score=24.55 buy_ready=False sector_rank=15 price=0.81 support=0.65 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=92.27 liquidity=250753856.0 spike=3.38
- MOIL.CA: score=13.08 buy_ready=False sector_rank=9 price=0.68 support=0.58 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:12 PM market time freshness=DELAYED_CURRENT RSI=40.7 liquidity=862882.88 spike=1.41
- MOIN.CA: score=20.6 buy_ready=False sector_rank=15 price=34.67 support=23.11 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=70.36 liquidity=9811287.0 spike=0.32
- MOSC.CA: score=14.49 buy_ready=False sector_rank=15 price=330.79 support=282.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=77.74 liquidity=6701221.5 spike=0.46
- MPCI.CA: score=8.21 buy_ready=False sector_rank=15 price=416.98 support=345.0 resistance=429.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=359661184.0 spike=2.21
- MPCO.CA: score=22.0 buy_ready=False sector_rank=4 price=2.32 support=1.83 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=67.61 liquidity=154107264.0 spike=1.3
- MPRC.CA: score=18.79 buy_ready=False sector_rank=15 price=42.25 support=39.5 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=42.49 liquidity=17758122.0 spike=0.64
- MTIE.CA: score=9.11 buy_ready=False sector_rank=21 price=8.5 support=8.01 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=34.76 liquidity=96568224.0 spike=1.77
- NAHO.CA: score=-4.18 buy_ready=False sector_rank=15 price=0.14 support=0.14 resistance=0.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36054.41 spike=0.41
- NCCW.CA: score=15.79 buy_ready=False sector_rank=15 price=5.98 support=5.59 resistance=7.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=45.65 liquidity=11331610.0 spike=0.35
- NEDA.CA: score=13.5 buy_ready=False sector_rank=15 price=2.79 support=2.7 resistance=2.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:12 PM market time freshness=DELAYED_CURRENT RSI=50.94 liquidity=709857.13 spike=0.79
- NHPS.CA: score=20.79 buy_ready=False sector_rank=15 price=90.74 support=82.25 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=61.02 liquidity=23849242.0 spike=0.53
- NINH.CA: score=13.79 buy_ready=False sector_rank=15 price=22.3 support=21.22 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=21.27 liquidity=17714786.0 spike=0.48
- NIPH.CA: score=8.38 buy_ready=False sector_rank=10 price=396.52 support=335.0 resistance=398.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=600648000.0 spike=1.99
- OBRI.CA: score=16.79 buy_ready=False sector_rank=15 price=32.7 support=31.61 resistance=35.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=51.34 liquidity=13409184.0 spike=0.39
- OCDI.CA: score=20.5 buy_ready=False sector_rank=16 price=33.74 support=26.6 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=63.99 liquidity=74036224.0 spike=0.55
- OCPH.CA: score=6.13 buy_ready=False sector_rank=15 price=266.41 support=242.0 resistance=277.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29384772.0 spike=1.17
- ODIN.CA: score=22.79 buy_ready=False sector_rank=15 price=3.12 support=2.54 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=58.12 liquidity=26040360.0 spike=0.63
- OFH.CA: score=19.93 buy_ready=False sector_rank=15 price=0.94 support=0.69 resistance=0.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=86.77 liquidity=81800736.0 spike=1.07
- OIH.CA: score=20.4 buy_ready=False sector_rank=8 price=1.9 support=1.43 resistance=1.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=88.68 liquidity=67063872.0 spike=0.5
- OLFI.CA: score=14.87 buy_ready=False sector_rank=17 price=24.24 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=55.84 liquidity=4458765.0 spike=0.07
- ORAS.CA: score=4.6 buy_ready=False sector_rank=19 price=781.67 support=764.01 resistance=794.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=117198880.0 spike=1.0
- ORHD.CA: score=20.5 buy_ready=False sector_rank=16 price=42.13 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=61.0 liquidity=121174848.0 spike=0.76
- ORWE.CA: score=19.4 buy_ready=False sector_rank=7 price=25.94 support=22.55 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=72.2 liquidity=37706880.0 spike=0.5
- PHAR.CA: score=21.44 buy_ready=False sector_rank=10 price=137.84 support=90.01 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=53.49 liquidity=448855776.0 spike=1.02
- PHDC.CA: score=20.5 buy_ready=False sector_rank=16 price=15.17 support=14.32 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=64.14 liquidity=96066616.0 spike=0.4
- PHTV.CA: score=10.87 buy_ready=False sector_rank=15 price=365.05 support=310.0 resistance=447.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=65.28 liquidity=2084806.75 spike=0.75
- POUL.CA: score=15.41 buy_ready=False sector_rank=17 price=37.09 support=36.5 resistance=40.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=45.82 liquidity=21917928.0 spike=0.84
- PRCL.CA: score=15.4 buy_ready=False sector_rank=3 price=33.11 support=32.0 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=33.61 liquidity=29122140.0 spike=0.93
- PRDC.CA: score=6.56 buy_ready=False sector_rank=16 price=9.61 support=9.25 resistance=9.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=110730944.0 spike=1.53
- PRMH.CA: score=15.79 buy_ready=False sector_rank=15 price=2.36 support=2.36 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=10616414.0 spike=0.88
- RACC.CA: score=15.79 buy_ready=False sector_rank=15 price=9.97 support=9.8 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=44.55 liquidity=17426764.0 spike=0.88
- RAKT.CA: score=0.81 buy_ready=False sector_rank=15 price=22.25 support=21.65 resistance=24.0 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=22.55 liquidity=366924.75 spike=1.33
- RAYA.CA: score=8.38 buy_ready=False sector_rank=20 price=7.07 support=6.95 resistance=7.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=19.32 liquidity=45267820.0 spike=0.54
- RMDA.CA: score=21.4 buy_ready=False sector_rank=10 price=6.31 support=4.98 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=60.92 liquidity=52065992.0 spike=0.43
- ROTO.CA: score=18.79 buy_ready=False sector_rank=15 price=45.7 support=41.85 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=55.44 liquidity=17380336.0 spike=0.72
- RREI.CA: score=18.79 buy_ready=False sector_rank=15 price=4.52 support=3.76 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=45.4 liquidity=63842448.0 spike=0.95
- RTVC.CA: score=18.6 buy_ready=False sector_rank=15 price=4.02 support=3.73 resistance=4.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=81.82 liquidity=8587185.0 spike=1.11
- RUBX.CA: score=17.88 buy_ready=False sector_rank=15 price=12.45 support=12.02 resistance=13.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=50.29 liquidity=9094331.0 spike=0.45
- SAUD.CA: score=20.4 buy_ready=False sector_rank=5 price=24.35 support=21.4 resistance=24.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=88.45 liquidity=11633624.0 spike=0.51
- SCEM.CA: score=22.4 buy_ready=False sector_rank=3 price=97.0 support=76.75 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=70.54 liquidity=177935616.0 spike=0.84
- SCFM.CA: score=14.22 buy_ready=False sector_rank=15 price=282.26 support=270.51 resistance=319.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=43.62 liquidity=5432437.5 spike=0.19
- SCTS.CA: score=18.86 buy_ready=False sector_rank=1 price=618.5 support=603.13 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=61.7 liquidity=2459172.75 spike=0.24
- SDTI.CA: score=18.87 buy_ready=False sector_rank=15 price=68.94 support=50.3 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=60.97 liquidity=8080646.5 spike=0.26
- SEIG.CA: score=9.85 buy_ready=False sector_rank=15 price=262.27 support=242.1 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:12 PM market time freshness=DELAYED_CURRENT RSI=55.69 liquidity=1066344.88 spike=0.1
- SIPC.CA: score=5.79 buy_ready=False sector_rank=15 price=5.05 support=4.8 resistance=5.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39552256.0 spike=0.64
- SKPC.CA: score=20.78 buy_ready=False sector_rank=12 price=17.49 support=15.61 resistance=18.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=84.15 liquidity=81254176.0 spike=1.19
- SMFR.CA: score=19.81 buy_ready=False sector_rank=15 price=261.55 support=228.88 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=64.94 liquidity=9024558.0 spike=0.33
- SNFC.CA: score=17.79 buy_ready=False sector_rank=15 price=10.91 support=10.6 resistance=11.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=46.62 liquidity=10703563.0 spike=0.89
- SPIN.CA: score=6.54 buy_ready=False sector_rank=7 price=19.32 support=18.31 resistance=20.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=49842040.0 spike=1.07
- SPMD.CA: score=17.63 buy_ready=False sector_rank=15 price=0.47 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=42.47 liquidity=8844819.0 spike=0.29
- SUGR.CA: score=22.73 buy_ready=False sector_rank=17 price=52.31 support=46.47 resistance=53.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=72.94 liquidity=46786100.0 spike=2.16
- SVCE.CA: score=20.79 buy_ready=False sector_rank=15 price=10.43 support=9.06 resistance=12.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=65.56 liquidity=33705208.0 spike=0.34
- SWDY.CA: score=21.4 buy_ready=False sector_rank=11 price=120.98 support=91.8 resistance=133.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=68.64 liquidity=51264224.0 spike=0.56
- TALM.CA: score=26.4 buy_ready=False sector_rank=1 price=19.45 support=15.7 resistance=20.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=61.1 liquidity=11398805.0 spike=0.26
- TMGH.CA: score=18.5 buy_ready=False sector_rank=16 price=98.17 support=95.2 resistance=101.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=45.01 liquidity=196014720.0 spike=0.68
- TRTO.CA: score=18.86 buy_ready=False sector_rank=15 price=0.05 support=0.03 resistance=0.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:13 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=30896.57 spike=3.02
- UEFM.CA: score=10.72 buy_ready=False sector_rank=15 price=544.77 support=531.0 resistance=594.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:09 PM market time freshness=DELAYED_CURRENT RSI=46.53 liquidity=1927906.13 spike=0.36
- UEGC.CA: score=14.51 buy_ready=False sector_rank=15 price=2.19 support=1.95 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=34.45 liquidity=51962852.0 spike=1.36
- UNIP.CA: score=7.63 buy_ready=False sector_rank=15 price=0.38 support=0.36 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=74147888.0 spike=1.92
- UNIT.CA: score=21.54 buy_ready=False sector_rank=16 price=19.21 support=17.32 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=55.67 liquidity=19267128.0 spike=1.52
- WCDF.CA: score=9.5 buy_ready=False sector_rank=15 price=645.0 support=555.55 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 12:58 PM market time freshness=DELAYED_CURRENT RSI=76.66 liquidity=1715438.5 spike=0.35
- WKOL.CA: score=22.79 buy_ready=False sector_rank=15 price=348.76 support=310.0 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=46.35 liquidity=25410344.0 spike=0.74
- ZEOT.CA: score=22.79 buy_ready=False sector_rank=15 price=13.56 support=11.56 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=64.74 liquidity=10488770.0 spike=0.4
- ZMID.CA: score=21.24 buy_ready=False sector_rank=16 price=8.2 support=7.06 resistance=8.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=23 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=71.63 liquidity=334088448.0 spike=1.37

## Backtesting Lite
- CCAP.CA: 180d return=42.49%, max drawdown=-23.12%, MA20>MA50 days last20=19, as_of=2026-08-19T21:00:00+00:00
- TALM.CA: 180d return=22.32%, max drawdown=-10.12%, MA20>MA50 days last20=17, as_of=2026-08-19T21:00:00+00:00
- COPR.CA: 180d return=-2.78%, max drawdown=-52.45%, MA20>MA50 days last20=20, as_of=2026-08-19T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- COPR.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Copper for Commercial Investment & Real Estate Development summary=Copper for Commercial Investment swings to EGP 7m net losses in 9M-25; NRPD’s EGM approves capital cut, increase; Two shareholders sell entire stakes in NRPD
  - Copper for Commercial Investment swings to EGP 7m net losses in 9M-25: https://english.mubasher.info/news/4530417/Copper-for-Commercial-Investment-swings-to-EGP-7m-net-losses-in-9M-25/
  - NRPD’s EGM approves capital cut, increase: https://english.mubasher.info/news/4042300/NRPD-s-EGM-approves-capital-cut-increase/
  - Two shareholders sell entire stakes in NRPD: https://english.mubasher.info/news/4006432/Two-shareholders-sell-entire-stakes-in-NRPD/
- EMFD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=600 sources=3 expected=Emaar Misr for Development summary=Emaar Misr posts higher revenues at EGP 19.8bn in 2025; Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25; Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea
  - Emaar Misr posts higher revenues at EGP 19.8bn in 2025: https://english.mubasher.info/news/4561643/Emaar-Misr-posts-higher-revenues-at-EGP-19-8bn-in-2025/
  - Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25: https://english.mubasher.info/news/4525192/Emaar-Misr-s-consolidated-net-profits-drop-to-EGP-4-2bn-in-9M-25/
  - Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea: https://english.mubasher.info/news/4495287/Emaar-Misr-Golden-Coast-to-establish-EGP-900bn-project-in-Red-Sea/
- CEFM.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Middle Egypt Flour Mills summary=Middle Egypt Flour Mills posts lower net profits at EGP 77m in 9M-25/26; Middle Egypt Flour Mills shareholders approve EGP 3.25/shr dividend; Middle Egypt Mills reports 23% profit drop in FY19/20
  - Middle Egypt Flour Mills posts lower net profits at EGP 77m in 9M-25/26: https://english.mubasher.info/news/4601809/Middle-Egypt-Flour-Mills-posts-lower-net-profits-at-EGP-77m-in-9M-25-26/
  - Middle Egypt Flour Mills shareholders approve EGP 3.25/shr dividend: https://english.mubasher.info/news/3870911/Middle-Egypt-Flour-Mills-shareholders-approve-EGP-3-25-shr-dividend/
  - Middle Egypt Mills reports 23% profit drop in FY19/20: https://english.mubasher.info/news/3703590/Middle-Egypt-Mills-reports-23-profit-drop-in-FY19-20/
- MOED.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=The Egyptian Modern Education Systems, S.A.E. summary=Egyptian Modern Education swings to over EGP 1.5m net profits in Q1-25/26; Egyptian Modern Education shifts to over EGP 1.5m net profits in Q1-25/26; Egyptian Modern Education&#39;s net profits near EGP 5m in FY24/25
  - Egyptian Modern Education swings to over EGP 1.5m net profits in Q1-25/26: https://english.mubasher.info/news/4542751/Egyptian-Modern-Education-swings-to-over-EGP-1-5m-net-profits-in-Q1-25-26/
  - Egyptian Modern Education shifts to over EGP 1.5m net profits in Q1-25/26: https://english.mubasher.info/news/4540647/Egyptian-Modern-Education-shifts-to-over-EGP-1-5m-net-profits-in-Q1-25-26/
  - Egyptian Modern Education&#39;s net profits near EGP 5m in FY24/25: https://english.mubasher.info/news/4534544/Egyptian-Modern-Education-s-net-profits-near-EGP-5m-in-FY24-25/
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- CIRA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Investment and Real Estate Development summary=CIRA Education take over 51% of L’École Française Hurghada; CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion; CIRA Education launches Middle East’s 1st initiative for care economy
  - CIRA Education take over 51% of L’École Française Hurghada: https://english.mubasher.info/news/4488666/CIRA-Education-take-over-51-of-L-%C3%89cole-Fran%C3%A7aise-Hurghada/
  - CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion: https://english.mubasher.info/news/4393636/CIRA-s-majority-shareholder-acquires-37-5-additional-equity-backs-regional-expansion/
  - CIRA Education launches Middle East’s 1st initiative for care economy: https://english.mubasher.info/news/4391766/CIRA-Education-launches-Middle-East-s-1st-initiative-for-care-economy/

## Warnings
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence for COPR.CA matches the company but no source/report date was detected.
- Evidence for EMFD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CEFM.CA matches the company but no source/report date was detected.
- Evidence for MOED.CA matches the company but no source/report date was detected.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
