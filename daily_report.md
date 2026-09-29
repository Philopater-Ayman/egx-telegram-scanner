# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-09-29T18:13:24.371296+00:00
Generated Cairo: 2026-09-29 21:13
Run timing: target 15:30 Cairo | generated Cairo 2026-09-29 21:13 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-09-29 21:09

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 170/186
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, September 29
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 5.88% / above MA50 29.41%
- EGX70 regime: BEARISH / above MA20 5.41% / above MA50 18.92%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=470100928.0 spike=0.83 score=9.0
- GTWL.CA: liquidity=425825504.0 spike=3.39 score=7.3
- CCAP.CA: liquidity=415215200.0 spike=0.49 score=21.52
- NIPH.CA: liquidity=167717824.0 spike=1.38 score=8.19
- TMGH.CA: liquidity=161729792.0 spike=0.59 score=7.05

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: 

## Top Liquidity Spikes
- EGSA.CA: spike=3.76 liquidity=29497.65 outlook=WEAK_OR_RISKY score=4.06 buy_ready=False
- UEFM.CA: spike=3.56 liquidity=10914037.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GTWL.CA: spike=3.39 liquidity=425825504.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RAKT.CA: spike=3.21 liquidity=533374.88 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CPCI.CA: spike=2.53 liquidity=7795760.5 outlook=CONSTRUCTIVE score=54 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=8.06 5d=-0.2% 20d=9.54% aboveMA50=50.0%
- #2 Energy & Petrochemicals: score=4.31 5d=-0.57% 20d=3.34% aboveMA50=66.67%
- #3 Investment Holding: score=3.8 5d=-6.17% 20d=7.69% aboveMA50=66.67%
- #4 Education: score=1.79 5d=-5.78% 20d=8.12% aboveMA50=66.67%
- #5 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #6 Transportation & Logistics: score=0.36 5d=-6.62% 20d=-3.58% aboveMA50=50.0%
- #7 Banking & Financials: score=0.01 5d=-4.11% 20d=-2.48% aboveMA50=40.0%
- #8 Tourism & Leisure: score=-0.2 5d=-0.75% 20d=-6.7% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- BINV.CA: BULLISH_WATCH score=83.8 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- CCAP.CA: BULLISH_WATCH score=83.8 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- CANA.CA: BULLISH_WATCH score=76.01 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ALCN.CA: CONSTRUCTIVE score=64.36 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ETEL.CA: CONSTRUCTIVE score=60.06 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; overheated RSI
- TALM.CA: CONSTRUCTIVE score=59.79 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; below MA20
- EXPA.CA: CONSTRUCTIVE score=58.01 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; below MA20
- SNFC.CA: CONSTRUCTIVE score=57 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; momentum is extended; sector is not leading
- CPCI.CA: CONSTRUCTIVE score=54 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=overheated RSI; close to resistance; sector is not leading
- CIRA.CA: CONSTRUCTIVE score=53.79 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; below MA20

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- EFID.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=4.53 buy_ready=False sector_rank=16 price=253.24 support=240.1 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=18.56 liquidity=7009763.0 spike=0.29
- ABUK.CA: score=16.08 buy_ready=False sector_rank=13 price=88.64 support=80.7 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.46 liquidity=38007848.0 spike=0.21
- ACAMD.CA: score=7.52 buy_ready=False sector_rank=16 price=2.03 support=1.87 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.09 liquidity=45058420.0 spike=0.88
- ACGC.CA: score=11.5 buy_ready=False sector_rank=10 price=13.95 support=13.11 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.89 liquidity=13305393.0 spike=0.53
- ADCI.CA: score=-0.52 buy_ready=False sector_rank=16 price=271.5 support=256.0 resistance=311.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=30.37 liquidity=1955981.88 spike=0.63
- ADIB.CA: score=14.0 buy_ready=False sector_rank=7 price=50.42 support=49.0 resistance=54.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.97 liquidity=39059408.0 spike=0.46
- ADPC.CA: score=2.74 buy_ready=False sector_rank=16 price=3.49 support=3.4 resistance=4.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=23.26 liquidity=6216332.5 spike=0.33
- AFDI.CA: score=1.61 buy_ready=False sector_rank=16 price=49.9 support=48.03 resistance=57.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=33.09 liquidity=4088841.25 spike=0.39
- AFMC.CA: score=2.52 buy_ready=False sector_rank=16 price=151.0 support=133.17 resistance=153.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=43587632.0 spike=0.86
- AJWA.CA: score=9.1 buy_ready=False sector_rank=16 price=179.25 support=175.15 resistance=188.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.0 liquidity=4582483.5 spike=0.26
- ALCN.CA: score=19.14 buy_ready=False sector_rank=6 price=33.8 support=30.16 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.87 liquidity=21747606.0 spike=0.57
- ALUM.CA: score=1.58 buy_ready=False sector_rank=16 price=22.58 support=21.65 resistance=30.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=16.94 liquidity=4063651.5 spike=0.64
- AMER.CA: score=3.05 buy_ready=False sector_rank=14 price=4.29 support=4.21 resistance=4.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35816712.0 spike=0.82
- AMES.CA: score=6.52 buy_ready=False sector_rank=16 price=42.98 support=40.15 resistance=126.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=16.63 liquidity=60624256.0 spike=0.22
- AMIA.CA: score=12.45 buy_ready=False sector_rank=16 price=18.3 support=17.12 resistance=21.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.52 liquidity=6934214.0 spike=0.22
- AMOC.CA: score=20.72 buy_ready=False sector_rank=2 price=13.37 support=12.18 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.22 liquidity=91787200.0 spike=0.58
- APSW.CA: score=-2.98 buy_ready=False sector_rank=16 price=8.03 support=7.81 resistance=8.75 source=Yahoo Finance as_of=2026-09-27T21:00:00+00:00 freshness=FRESH RSI=26.81 liquidity=499811.27 spike=0.67
- ARAB.CA: score=7.05 buy_ready=False sector_rank=14 price=0.22 support=0.2 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.88 liquidity=37519484.0 spike=0.49
- ARCC.CA: score=7.4 buy_ready=False sector_rank=21 price=62.64 support=60.01 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=8.41 liquidity=15325820.0 spike=0.54
- AREH.CA: score=4.55 buy_ready=False sector_rank=16 price=1.2 support=1.2 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=10.81 liquidity=8025996.0 spike=0.59
- ASCM.CA: score=1.36 buy_ready=False sector_rank=16 price=56.36 support=56.1 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=16.64 liquidity=3843757.5 spike=0.23
- ASPI.CA: score=6.52 buy_ready=False sector_rank=16 price=0.34 support=0.34 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=21.74 liquidity=12623976.0 spike=0.23
- ATLC.CA: score=2.24 buy_ready=False sector_rank=19 price=5.45 support=5.41 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.62 liquidity=4841386.5 spike=0.17
- ATQA.CA: score=16.08 buy_ready=False sector_rank=13 price=11.45 support=11.05 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.46 liquidity=24690980.0 spike=0.25
- AXPH.CA: score=8.97 buy_ready=False sector_rank=16 price=1541.15 support=1334.35 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=28.58 liquidity=8014698.0 spike=1.22
- BINV.CA: score=21.52 buy_ready=False sector_rank=3 price=57.92 support=49.51 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=61.46 liquidity=10776176.0 spike=0.49
- BIOC.CA: score=5.04 buy_ready=False sector_rank=16 price=267.04 support=235.53 resistance=275.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=134447392.0 spike=2.26
- BTFH.CA: score=6.64 buy_ready=False sector_rank=19 price=2.7 support=2.65 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=24.19 liquidity=100393256.0 spike=1.12
- CAED.CA: score=2.52 buy_ready=False sector_rank=16 price=112.0 support=105.03 resistance=118.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15476694.0 spike=0.79
- CANA.CA: score=21.0 buy_ready=False sector_rank=7 price=45.14 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=54.04 liquidity=13949677.0 spike=0.57
- CCAP.CA: score=21.52 buy_ready=False sector_rank=3 price=6.78 support=5.85 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.93 liquidity=415215200.0 spike=0.49
- CCRS.CA: score=10.45 buy_ready=False sector_rank=16 price=2.3 support=2.23 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=37.96 liquidity=7927287.0 spike=0.4
- CEFM.CA: score=-2.86 buy_ready=False sector_rank=16 price=134.12 support=127.15 resistance=145.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4620206.0 spike=0.6
- CERA.CA: score=6.52 buy_ready=False sector_rank=16 price=1.2 support=1.18 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.25 liquidity=59792396.0 spike=0.4
- CFGH.CA: score=-3.47 buy_ready=False sector_rank=16 price=0.11 support=0.11 resistance=0.12 source=Yahoo Finance as_of=2026-09-27T21:00:00+00:00 freshness=FRESH RSI=8.33 liquidity=13449.59 spike=0.95
- CICH.CA: score=-0.21 buy_ready=False sector_rank=19 price=11.41 support=10.75 resistance=13.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=28.22 liquidity=2389167.75 spike=0.38
- CIEB.CA: score=4.79 buy_ready=False sector_rank=7 price=23.59 support=23.7 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.44 liquidity=5786892.5 spike=0.43
- CIRA.CA: score=16.83 buy_ready=False sector_rank=4 price=38.23 support=33.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=51.15 liquidity=9115863.0 spike=0.23
- CLHO.CA: score=7.43 buy_ready=False sector_rank=17 price=15.3 support=13.9 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=16.8 liquidity=20336230.0 spike=0.31
- CNFN.CA: score=0.71 buy_ready=False sector_rank=19 price=3.96 support=3.84 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=13.45 liquidity=4313766.0 spike=0.39
- COMI.CA: score=9.0 buy_ready=False sector_rank=7 price=128.08 support=126.81 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.56 liquidity=470100928.0 spike=0.83
- COPR.CA: score=7.52 buy_ready=False sector_rank=16 price=0.45 support=0.44 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.06 liquidity=12445261.0 spike=0.39
- COSG.CA: score=6.52 buy_ready=False sector_rank=16 price=1.52 support=1.51 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=16.67 liquidity=10506526.0 spike=0.38
- CPCI.CA: score=16.38 buy_ready=False sector_rank=16 price=575.51 support=530.0 resistance=584.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=70.88 liquidity=7795760.5 spike=2.53
- CSAG.CA: score=4.91 buy_ready=False sector_rank=6 price=35.29 support=35.01 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=21.68 liquidity=5768609.0 spike=0.4
- DAPH.CA: score=7.52 buy_ready=False sector_rank=16 price=94.19 support=91.65 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=11.0 liquidity=20652628.0 spike=0.6
- DEIN.CA: score=5.52 buy_ready=False sector_rank=16 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=2.28 buy_ready=False sector_rank=15 price=24.68 support=24.01 resistance=29.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=21.84 liquidity=5482532.0 spike=1.08
- DSCW.CA: score=6.52 buy_ready=False sector_rank=16 price=1.7 support=1.67 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=14.71 liquidity=17788660.0 spike=0.83
- DTPP.CA: score=15.52 buy_ready=False sector_rank=16 price=291.17 support=290.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.4 liquidity=35667584.0 spike=0.43
- EALR.CA: score=-1.18 buy_ready=False sector_rank=16 price=331.76 support=322.52 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=20.63 liquidity=2299257.5 spike=0.18
- EASB.CA: score=6.04 buy_ready=False sector_rank=16 price=7.1 support=6.04 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.87 liquidity=3521143.75 spike=0.23
- EAST.CA: score=6.9 buy_ready=False sector_rank=15 price=29.0 support=29.55 resistance=36.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=3.42 liquidity=49893640.0 spike=1.13
- EBSC.CA: score=-1.69 buy_ready=False sector_rank=16 price=1.7 support=1.65 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=28.74 liquidity=1787378.88 spike=0.23
- ECAP.CA: score=-1.74 buy_ready=False sector_rank=16 price=30.0 support=29.13 resistance=34.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=21.04 liquidity=1737409.88 spike=0.24
- EDFM.CA: score=0.0 buy_ready=False sector_rank=16 price=387.28 support=354.0 resistance=465.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=25.24 liquidity=2081691.5 spike=1.2
- EEII.CA: score=11.48 buy_ready=False sector_rank=16 price=2.09 support=2.06 resistance=2.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=37.66 liquidity=7960460.5 spike=0.69
- EFIC.CA: score=7.08 buy_ready=False sector_rank=13 price=160.88 support=147.0 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=7.94 liquidity=25744844.0 spike=0.07
- EFIH.CA: score=8.43 buy_ready=False sector_rank=11 price=22.3 support=20.2 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.64 liquidity=27928528.0 spike=0.52
- EGAL.CA: score=11.08 buy_ready=False sector_rank=13 price=342.53 support=340.0 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.42 liquidity=27841626.0 spike=0.47
- EGAS.CA: score=13.06 buy_ready=False sector_rank=2 price=55.84 support=53.62 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=41.11 liquidity=5338485.0 spike=0.41
- EGBE.CA: score=4.01 buy_ready=False sector_rank=7 price=0.51 support=0.49 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=7247.65 spike=0.08
- EGCH.CA: score=13.08 buy_ready=False sector_rank=13 price=13.47 support=13.4 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.41 liquidity=66104472.0 spike=0.49
- EGSA.CA: score=9.43 buy_ready=False sector_rank=1 price=8.85 support=8.82 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=28 September 12:29 PM market time freshness=DELAYED_CURRENT RSI=17.24 liquidity=29497.65 spike=3.76
- EGTS.CA: score=17.05 buy_ready=False sector_rank=14 price=17.36 support=16.51 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.56 liquidity=12646468.0 spike=0.36
- EHDR.CA: score=6.01 buy_ready=False sector_rank=16 price=2.44 support=2.43 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=12.86 liquidity=8491036.0 spike=0.5
- ELEC.CA: score=6.4 buy_ready=False sector_rank=18 price=1.8 support=1.72 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.22 liquidity=25691540.0 spike=0.32
- ELKA.CA: score=3.14 buy_ready=False sector_rank=16 price=1.49 support=1.43 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=9.09 liquidity=6624612.5 spike=0.26
- ELNA.CA: score=-3.37 buy_ready=False sector_rank=16 price=35.22 support=33.46 resistance=38.99 source=Yahoo Finance as_of=2026-09-27T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=106787.04 spike=0.31
- ELSH.CA: score=6.59 buy_ready=False sector_rank=16 price=11.2 support=10.8 resistance=14.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=15.95 liquidity=9069833.0 spike=0.3
- ELWA.CA: score=-2.96 buy_ready=False sector_rank=16 price=1.51 support=1.55 resistance=1.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=6.67 liquidity=522967.78 spike=0.46
- EMFD.CA: score=8.05 buy_ready=False sector_rank=14 price=12.23 support=12.0 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.22 liquidity=41199216.0 spike=0.33
- ENGC.CA: score=2.52 buy_ready=False sector_rank=16 price=35.96 support=35.7 resistance=39.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17875442.0 spike=0.99
- EOSB.CA: score=7.54 buy_ready=False sector_rank=16 price=1.57 support=1.53 resistance=1.64 source=Yahoo Finance as_of=2026-09-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=23771.37 spike=0.38
- EPCO.CA: score=-0.48 buy_ready=False sector_rank=16 price=9.8 support=9.25 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.73 liquidity=1995627.38 spike=0.13
- EPPK.CA: score=-7.06 buy_ready=False sector_rank=16 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=24.4 buy_ready=False sector_rank=1 price=134.0 support=112.5 resistance=140.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.45 liquidity=157998672.0 spike=0.55
- ETRS.CA: score=7.62 buy_ready=False sector_rank=16 price=9.99 support=10.02 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=20.51 liquidity=12792234.0 spike=1.05
- EXPA.CA: score=19.0 buy_ready=False sector_rank=7 price=21.3 support=20.6 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.4 liquidity=12143159.0 spike=0.34
- FAIT.CA: score=4.27 buy_ready=False sector_rank=7 price=43.58 support=38.48 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=27.29 liquidity=2264330.0 spike=0.41
- FAITA.CA: score=3.03 buy_ready=False sector_rank=7 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=25148.02 spike=0.7
- FERC.CA: score=-1.3 buy_ready=False sector_rank=13 price=73.74 support=70.42 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=33.78 liquidity=1628320.75 spike=0.12
- FWRY.CA: score=7.43 buy_ready=False sector_rank=11 price=18.24 support=17.5 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=11.19 liquidity=39817044.0 spike=0.38
- GBCO.CA: score=13.34 buy_ready=False sector_rank=12 price=29.46 support=27.0 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.13 liquidity=11485121.0 spike=0.15
- GDWA.CA: score=6.52 buy_ready=False sector_rank=16 price=0.65 support=0.61 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=7.03 liquidity=16393843.0 spike=0.38
- GGCC.CA: score=7.52 buy_ready=False sector_rank=16 price=0.67 support=0.67 resistance=0.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=21.75 liquidity=12366188.0 spike=0.62
- GIHD.CA: score=15.52 buy_ready=False sector_rank=16 price=66.89 support=66.1 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.19 liquidity=18762400.0 spike=0.64
- GMCI.CA: score=-2.95 buy_ready=False sector_rank=16 price=1.5 support=1.56 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=10.26 liquidity=494315.53 spike=1.02
- GRCA.CA: score=0.71 buy_ready=False sector_rank=16 price=34.01 support=32.11 resistance=63.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=11.94 liquidity=4190723.75 spike=0.12
- GSSC.CA: score=0.2 buy_ready=False sector_rank=16 price=263.85 support=246.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.66 liquidity=2681940.75 spike=0.34
- GTWL.CA: score=7.3 buy_ready=False sector_rank=16 price=151.96 support=151.96 resistance=199.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=425825504.0 spike=3.39
- HDBK.CA: score=16.0 buy_ready=False sector_rank=7 price=107.34 support=102.5 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.2 liquidity=15197286.0 spike=0.28
- HELI.CA: score=13.05 buy_ready=False sector_rank=14 price=7.31 support=7.02 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.74 liquidity=40893428.0 spike=0.26
- HRHO.CA: score=6.4 buy_ready=False sector_rank=19 price=23.59 support=23.02 resistance=26.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=9.56 liquidity=49057584.0 spike=0.63
- ICID.CA: score=11.42 buy_ready=False sector_rank=16 price=17.6 support=16.52 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.71 liquidity=5903310.5 spike=0.64
- IDRE.CA: score=7.37 buy_ready=False sector_rank=16 price=45.76 support=45.0 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.31 liquidity=4846647.5 spike=0.29
- IFAP.CA: score=2.81 buy_ready=False sector_rank=9 price=19.09 support=17.17 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=24.95 liquidity=5195112.5 spike=0.29
- INFI.CA: score=7.8 buy_ready=False sector_rank=16 price=116.5 support=104.0 resistance=160.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=17.79 liquidity=19766698.0 spike=1.14
- IRON.CA: score=2.3 buy_ready=False sector_rank=13 price=26.09 support=25.82 resistance=30.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=28.2 liquidity=5226207.0 spike=0.39
- ISMA.CA: score=7.52 buy_ready=False sector_rank=16 price=23.92 support=24.51 resistance=37.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=22.33 liquidity=11766189.0 spike=0.71
- ISMQ.CA: score=7.08 buy_ready=False sector_rank=13 price=7.77 support=7.7 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=16.67 liquidity=22290810.0 spike=0.89
- ISPH.CA: score=7.43 buy_ready=False sector_rank=17 price=11.71 support=11.22 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.75 liquidity=44631884.0 spike=0.65
- JUFO.CA: score=6.64 buy_ready=False sector_rank=15 price=24.92 support=24.5 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=19.54 liquidity=13082180.0 spike=0.65
- KABO.CA: score=10.48 buy_ready=False sector_rank=10 price=8.32 support=8.2 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.35 liquidity=6980816.0 spike=0.21
- KWIN.CA: score=1.63 buy_ready=False sector_rank=16 price=77.57 support=74.0 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=27.88 liquidity=4108228.5 spike=0.18
- KZPC.CA: score=10.52 buy_ready=False sector_rank=16 price=12.9 support=12.8 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.98 liquidity=10924813.0 spike=0.36
- LCSW.CA: score=2.45 buy_ready=False sector_rank=21 price=29.94 support=29.2 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=15.12 liquidity=5047757.0 spike=0.23
- LUTS.CA: score=12.52 buy_ready=False sector_rank=16 price=0.82 support=0.72 resistance=1.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.78 liquidity=78968576.0 spike=0.71
- MAAL.CA: score=17.52 buy_ready=False sector_rank=16 price=10.79 support=8.18 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=70.42 liquidity=12912649.0 spike=0.56
- MASR.CA: score=7.52 buy_ready=False sector_rank=16 price=7.31 support=6.82 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=13.33 liquidity=57146648.0 spike=0.6
- MBSC.CA: score=8.46 buy_ready=False sector_rank=21 price=300.38 support=295.22 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=10.5 liquidity=66225540.0 spike=1.53
- MCQE.CA: score=7.4 buy_ready=False sector_rank=21 price=183.37 support=180.04 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=10.83 liquidity=17139880.0 spike=0.72
- MCRO.CA: score=7.52 buy_ready=False sector_rank=16 price=1.45 support=1.41 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.19 liquidity=53149288.0 spike=0.42
- MENA.CA: score=-1.33 buy_ready=False sector_rank=14 price=6.2 support=5.8 resistance=7.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.09 liquidity=625966.13 spike=0.45
- MEPA.CA: score=3.39 buy_ready=False sector_rank=16 price=1.6 support=1.61 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=13.56 liquidity=6870557.0 spike=0.18
- MFPC.CA: score=16.08 buy_ready=False sector_rank=13 price=46.06 support=41.56 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.02 liquidity=32564592.0 spike=0.19
- MFSC.CA: score=4.77 buy_ready=False sector_rank=16 price=47.72 support=45.22 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.04 liquidity=2254522.5 spike=0.5
- MHOT.CA: score=14.92 buy_ready=False sector_rank=8 price=17.25 support=16.61 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.22 liquidity=16553242.0 spike=0.96
- MICH.CA: score=7.66 buy_ready=False sector_rank=16 price=42.97 support=43.5 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=23.0 liquidity=14098203.0 spike=1.07
- MILS.CA: score=7.52 buy_ready=False sector_rank=16 price=180.14 support=165.5 resistance=232.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.07 liquidity=17467792.0 spike=0.95
- MIPH.CA: score=5.91 buy_ready=False sector_rank=17 price=786.76 support=700.2 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.27 liquidity=3480479.75 spike=0.36
- MOED.CA: score=6.52 buy_ready=False sector_rank=16 price=0.63 support=0.62 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=10.48 liquidity=11760664.0 spike=0.22
- MOIL.CA: score=12.38 buy_ready=False sector_rank=2 price=0.71 support=0.67 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=81.03 liquidity=277216.28 spike=1.19
- MOIN.CA: score=6.19 buy_ready=False sector_rank=16 price=34.86 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.96 liquidity=5666100.0 spike=0.19
- MOSC.CA: score=0.31 buy_ready=False sector_rank=16 price=271.33 support=257.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=9.65 liquidity=2785707.0 spike=0.7
- MPCI.CA: score=7.52 buy_ready=False sector_rank=16 price=339.43 support=341.01 resistance=472.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=12.77 liquidity=116732312.0 spike=0.98
- MPCO.CA: score=16.62 buy_ready=False sector_rank=9 price=2.37 support=2.07 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.26 liquidity=114469688.0 spike=0.62
- MPRC.CA: score=7.52 buy_ready=False sector_rank=16 price=38.0 support=37.65 resistance=44.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.97 liquidity=14954252.0 spike=0.47
- MTIE.CA: score=7.34 buy_ready=False sector_rank=12 price=7.82 support=7.5 resistance=8.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=21.77 liquidity=16808898.0 spike=0.71
- NAHO.CA: score=5.53 buy_ready=False sector_rank=16 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance as_of=2026-09-27T21:00:00+00:00 freshness=FRESH RSI=40.0 liquidity=7671.55 spike=0.15
- NCCW.CA: score=15.52 buy_ready=False sector_rank=16 price=6.95 support=5.83 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=44787904.0 spike=0.56
- NEDA.CA: score=-2.16 buy_ready=False sector_rank=16 price=2.66 support=2.48 resistance=2.89 source=Yahoo Finance as_of=2026-09-27T21:00:00+00:00 freshness=FRESH RSI=30.61 liquidity=317904.59 spike=0.34
- NHPS.CA: score=5.15 buy_ready=False sector_rank=16 price=69.68 support=70.8 resistance=91.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.43 liquidity=8628942.0 spike=0.58
- NINH.CA: score=7.52 buy_ready=False sector_rank=16 price=19.32 support=18.53 resistance=24.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=16.67 liquidity=16422635.0 spike=0.98
- NIPH.CA: score=8.19 buy_ready=False sector_rank=17 price=305.64 support=290.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=33.96 liquidity=167717824.0 spike=1.38
- OBRI.CA: score=6.52 buy_ready=False sector_rank=16 price=24.07 support=24.0 resistance=34.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=9.54 liquidity=10442467.0 spike=0.8
- OCDI.CA: score=3.07 buy_ready=False sector_rank=14 price=25.0 support=24.5 resistance=27.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=65180848.0 spike=1.01
- OCPH.CA: score=3.06 buy_ready=False sector_rank=16 price=208.47 support=190.0 resistance=263.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=17.08 liquidity=6121810.5 spike=1.21
- ODIN.CA: score=3.59 buy_ready=False sector_rank=16 price=2.46 support=2.35 resistance=3.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=26.73 liquidity=6066955.0 spike=0.43
- OFH.CA: score=7.52 buy_ready=False sector_rank=16 price=0.87 support=0.83 resistance=1.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=23.91 liquidity=42994100.0 spike=0.33
- OIH.CA: score=11.56 buy_ready=False sector_rank=3 price=1.79 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.0 liquidity=114657816.0 spike=1.02
- OLFI.CA: score=2.93 buy_ready=False sector_rank=15 price=22.04 support=21.2 resistance=23.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=31.39 liquidity=6298409.5 spike=0.37
- ORAS.CA: score=4.6 buy_ready=False sector_rank=5 price=777.66 support=776.0 resistance=805.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=98669936.0 spike=1.0
- ORHD.CA: score=8.05 buy_ready=False sector_rank=14 price=38.79 support=38.02 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.5 liquidity=85706280.0 spike=0.51
- ORWE.CA: score=16.5 buy_ready=False sector_rank=10 price=26.8 support=26.01 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.1 liquidity=25963502.0 spike=0.46
- PHAR.CA: score=8.91 buy_ready=False sector_rank=17 price=108.0 support=102.0 resistance=133.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=14.63 liquidity=143034560.0 spike=1.74
- PHDC.CA: score=8.05 buy_ready=False sector_rank=14 price=12.88 support=12.5 resistance=15.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=12.45 liquidity=64479344.0 spike=0.46
- PHTV.CA: score=3.24 buy_ready=False sector_rank=16 price=331.71 support=320.11 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.87 liquidity=723792.94 spike=0.44
- POUL.CA: score=7.74 buy_ready=False sector_rank=15 price=9.77 support=9.12 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=5.69 liquidity=43336196.0 spike=1.55
- PRCL.CA: score=-2.55 buy_ready=False sector_rank=21 price=25.04 support=24.25 resistance=27.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5049115.0 spike=0.3
- PRDC.CA: score=8.05 buy_ready=False sector_rank=14 price=7.2 support=6.81 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=17.09 liquidity=33212460.0 spike=0.68
- PRMH.CA: score=5.26 buy_ready=False sector_rank=16 price=2.24 support=2.2 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.81 liquidity=7241574.5 spike=1.25
- RACC.CA: score=-0.36 buy_ready=False sector_rank=16 price=9.1 support=8.51 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.11 liquidity=3117981.75 spike=0.23
- RAKT.CA: score=1.47 buy_ready=False sector_rank=16 price=21.32 support=21.2 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=30.86 liquidity=533374.88 spike=3.21
- RAYA.CA: score=7.4 buy_ready=False sector_rank=20 price=6.14 support=5.72 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=16.67 liquidity=38609540.0 spike=0.73
- RMDA.CA: score=7.43 buy_ready=False sector_rank=17 price=5.29 support=4.83 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=12.67 liquidity=30128666.0 spike=0.51
- ROTO.CA: score=2.05 buy_ready=False sector_rank=16 price=38.63 support=35.02 resistance=45.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.25 liquidity=4525482.0 spike=0.56
- RREI.CA: score=-4.42 buy_ready=False sector_rank=16 price=3.64 support=3.6 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3055128.25 spike=0.21
- RTVC.CA: score=1.28 buy_ready=False sector_rank=16 price=3.41 support=3.43 resistance=4.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=20.0 liquidity=3895747.5 spike=1.43
- RUBX.CA: score=2.52 buy_ready=False sector_rank=16 price=14.19 support=14.16 resistance=15.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=50484452.0 spike=0.77
- SAUD.CA: score=12.86 buy_ready=False sector_rank=7 price=22.02 support=21.6 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.54 liquidity=8859382.0 spike=0.43
- SCEM.CA: score=7.4 buy_ready=False sector_rank=21 price=76.95 support=76.01 resistance=105.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=4.19 liquidity=24478076.0 spike=0.31
- SCFM.CA: score=0.67 buy_ready=False sector_rank=16 price=250.72 support=223.11 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=15.65 liquidity=4151898.5 spike=0.68
- SCTS.CA: score=0.44 buy_ready=False sector_rank=4 price=543.3 support=520.3 resistance=639.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=17.03 liquidity=724842.44 spike=0.32
- SDTI.CA: score=16.52 buy_ready=False sector_rank=16 price=84.02 support=68.57 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=77.45 liquidity=19555972.0 spike=0.57
- SEIG.CA: score=-2.09 buy_ready=False sector_rank=16 price=218.01 support=211.15 resistance=268.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=28.8 liquidity=385021.84 spike=0.21
- SIPC.CA: score=2.52 buy_ready=False sector_rank=16 price=4.92 support=4.5 resistance=5.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46481276.0 spike=0.66
- SKPC.CA: score=7.08 buy_ready=False sector_rank=13 price=15.92 support=15.7 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.04 liquidity=98792232.0 spike=0.72
- SMFR.CA: score=-1.72 buy_ready=False sector_rank=16 price=217.04 support=205.01 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=9.13 liquidity=757463.5 spike=0.11
- SNFC.CA: score=14.63 buy_ready=False sector_rank=16 price=11.42 support=10.26 resistance=11.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=66.46 liquidity=7106305.5 spike=0.5
- SPIN.CA: score=6.36 buy_ready=False sector_rank=10 price=16.13 support=15.11 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.11 liquidity=7786881.5 spike=1.04
- SPMD.CA: score=11.52 buy_ready=False sector_rank=16 price=0.37 support=0.37 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=41.01 liquidity=10129955.0 spike=0.13
- SUGR.CA: score=5.46 buy_ready=False sector_rank=15 price=52.99 support=51.2 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.07 liquidity=7823033.5 spike=0.26
- SVCE.CA: score=7.52 buy_ready=False sector_rank=16 price=9.73 support=9.6 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=10.4 liquidity=64596672.0 spike=0.33
- SWDY.CA: score=7.88 buy_ready=False sector_rank=18 price=107.97 support=108.01 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=11.28 liquidity=79259080.0 spike=1.24
- TALM.CA: score=17.72 buy_ready=False sector_rank=4 price=19.6 support=17.61 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.61 liquidity=30082320.0 spike=0.46
- TMGH.CA: score=7.05 buy_ready=False sector_rank=14 price=87.21 support=86.1 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=14.82 liquidity=161729792.0 spike=0.59
- TRTO.CA: score=-2.48 buy_ready=False sector_rank=16 price=0.05 support=0.05 resistance=0.08 source=Yahoo Finance as_of=2026-09-27T21:00:00+00:00 freshness=FRESH RSI=12.0 liquidity=3716.5 spike=0.13
- UEFM.CA: score=7.52 buy_ready=False sector_rank=16 price=509.46 support=437.5 resistance=509.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10914037.0 spike=3.56
- UEGC.CA: score=6.52 buy_ready=False sector_rank=16 price=1.43 support=1.42 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=21.82 liquidity=23369046.0 spike=0.55
- UNIP.CA: score=2.69 buy_ready=False sector_rank=16 price=0.32 support=0.32 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=20.59 liquidity=6165788.0 spike=0.3
- UNIT.CA: score=13.11 buy_ready=False sector_rank=14 price=17.0 support=16.66 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=41.72 liquidity=14764456.0 spike=1.03
- WCDF.CA: score=4.31 buy_ready=False sector_rank=16 price=625.44 support=575.5 resistance=796.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.96 liquidity=6411452.0 spike=1.19
- WKOL.CA: score=6.52 buy_ready=False sector_rank=16 price=291.32 support=293.03 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=20.92 liquidity=10683213.0 spike=0.8
- ZEOT.CA: score=2.8 buy_ready=False sector_rank=16 price=11.26 support=10.6 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=13.13 liquidity=5280775.5 spike=0.87
- ZMID.CA: score=3.05 buy_ready=False sector_rank=14 price=7.41 support=7.3 resistance=7.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=78149880.0 spike=0.45

## Backtesting Lite
- ETEL.CA: 180d return=101.7%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-09-27T21:00:00+00:00
- BINV.CA: 180d return=52.39%, max drawdown=-17.77%, MA20>MA50 days last20=20, as_of=2026-09-27T21:00:00+00:00
- CCAP.CA: 180d return=99.7%, max drawdown=-17.02%, MA20>MA50 days last20=20, as_of=2026-09-27T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- CANA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=636 sources=3 expected=Suez Canal Bank summary=Suez Canal Bank delivers EGP 1.6bn profits in Q1-26; Suez Canal Bank unveils details for previous dividends payout; Suez Canal Bank to distribute EGP 5bn bonus shares for 2025
  - Suez Canal Bank delivers EGP 1.6bn profits in Q1-26: https://english.mubasher.info/news/4611255/Suez-Canal-Bank-delivers-EGP-1-6bn-profits-in-Q1-26/
  - Suez Canal Bank unveils details for previous dividends payout: https://english.mubasher.info/news/4586807/Suez-Canal-Bank-unveils-details-for-previous-dividends-payout/
  - Suez Canal Bank to distribute EGP 5bn bonus shares for 2025: https://english.mubasher.info/news/4581661/Suez-Canal-Bank-to-distribute-EGP-5bn-bonus-shares-for-2025/
- AMOC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria Mineral Oils summary=AMOC achieves EGP 10.5bn consolidated sales in Q1-26; AMOC studies potential project with Germany’s SULZER; AMOC to pay out EGP 0.4/shr dividends for H2-25
  - AMOC achieves EGP 10.5bn consolidated sales in Q1-26: https://english.mubasher.info/news/4604903/AMOC-achieves-EGP-10-5bn-consolidated-sales-in-Q1-26/
  - AMOC studies potential project with Germany’s SULZER: https://english.mubasher.info/news/4586853/AMOC-studies-potential-project-with-Germany-s-SULZER/
  - AMOC to pay out EGP 0.4/shr dividends for H2-25: https://english.mubasher.info/news/4586775/AMOC-to-pay-out-EGP-0-4-shr-dividends-for-H2-25/
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- EXPA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Export Development Bank of Egypt summary=Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.

## Warnings
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
