# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-11-12T15:07:29.638078+00:00
Generated Cairo: 2026-11-12 17:07
Run timing: target 09:15 Cairo | generated Cairo 2026-11-12 17:07 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-11-12 17:03

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 5
- Tradeable price/liquidity tickers: 173/185
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, November 12
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 88.89% / above MA50 38.89%
- EGX70 regime: BEARISH / above MA20 92.11% / above MA50 34.21%
- Sector breadth: 47.62%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- ETEL.CA: liquidity=647921664.0 spike=2.8 score=27.0
- BIOC.CA: liquidity=453240320.0 spike=3.05 score=24.5
- EAST.CA: liquidity=342024544.0 spike=9.0 score=27.4
- CCAP.CA: liquidity=323277184.0 spike=0.78 score=19.27
- MPCO.CA: liquidity=287061248.0 spike=3.02 score=29.44

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- INFI.CA: spike=10.69 liquidity=236440768.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EAST.CA: spike=9.0 liquidity=342024544.0 outlook=BULLISH_WATCH score=75.56 buy_ready=False
- SUGR.CA: spike=5.75 liquidity=94298392.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- PRCL.CA: spike=5.34 liquidity=108125304.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- OLFI.CA: spike=5.24 liquidity=41242080.0 outlook=CONSTRUCTIVE score=63.56 buy_ready=False

## Sector Leaderboard
- #1 Tourism & Leisure: score=12.53 5d=5.29% 20d=6.15% aboveMA50=100.0%
- #2 Agriculture & Food Production: score=12.47 5d=13.48% 20d=-0.71% aboveMA50=50.0%
- #3 Technology & Distribution: score=11.68 5d=14.86% 20d=6.28% aboveMA50=0.0%
- #4 Telecommunications: score=9.72 5d=4.41% 20d=-3.17% aboveMA50=100.0%
- #5 Healthcare: score=9.61 5d=5.79% 20d=5.07% aboveMA50=66.67%
- #6 Food, Beverages & Tobacco: score=9.56 5d=3.13% 20d=5.37% aboveMA50=28.57%
- #7 Building Materials: score=9.51 5d=7.63% 20d=5.13% aboveMA50=50.0%
- #8 Industrial Goods & Cables: score=9.25 5d=8.29% 20d=3.56% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ETEL.CA: BULLISH_WATCH score=96.72 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- MHOT.CA: BULLISH_WATCH score=92 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended; far above support
- MPCO.CA: BULLISH_WATCH score=91 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=far above support; close to resistance
- KZPC.CA: BULLISH_WATCH score=89.91 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- MOIN.CA: BULLISH_WATCH score=87.91 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- UEFM.CA: BULLISH_WATCH score=87.91 liquidity=TRADEABLE sector=IMPROVING risk=far above support; sector is not leading
- SIPC.CA: BULLISH_WATCH score=85.91 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- GMCI.CA: BULLISH_WATCH score=82.91 liquidity=TRADEABLE sector=IMPROVING risk=far above support; sector is not leading
- SAUD.CA: BULLISH_WATCH score=82.9 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- PRMH.CA: BULLISH_WATCH score=79.91 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- CANA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=22.4 buy_ready=False sector_rank=11 price=250.32 support=171.02 resistance=269.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=61.16 liquidity=10491261.0 spike=0.52
- ABUK.CA: score=10.08 buy_ready=False sector_rank=18 price=77.76 support=73.6 resistance=95.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=28.18 liquidity=66690852.0 spike=0.49
- ACAMD.CA: score=23.7 buy_ready=False sector_rank=11 price=2.09 support=1.86 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=55.36 liquidity=65870252.0 spike=1.15
- ACGC.CA: score=21.98 buy_ready=False sector_rank=13 price=14.03 support=11.6 resistance=14.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=59.23 liquidity=8515224.0 spike=1.03
- ADCI.CA: score=17.16 buy_ready=False sector_rank=11 price=270.81 support=221.0 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:10 PM market time freshness=DELAYED_CURRENT RSI=58.67 liquidity=1757603.25 spike=0.71
- ADIB.CA: score=21.4 buy_ready=False sector_rank=14 price=49.41 support=43.16 resistance=50.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=66.47 liquidity=29832116.0 spike=0.37
- ADPC.CA: score=21.6 buy_ready=False sector_rank=11 price=3.07 support=2.53 resistance=3.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=58.91 liquidity=16629590.0 spike=2.1
- AFDI.CA: score=12.33 buy_ready=False sector_rank=11 price=45.9 support=34.8 resistance=50.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=58.79 liquidity=1931029.75 spike=0.69
- AFMC.CA: score=23.62 buy_ready=False sector_rank=11 price=151.57 support=94.6 resistance=156.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=69.38 liquidity=44105500.0 spike=2.11
- AJWA.CA: score=22.76 buy_ready=False sector_rank=11 price=270.97 support=190.2 resistance=273.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=74.83 liquidity=54017868.0 spike=1.68
- ALCN.CA: score=23.58 buy_ready=False sector_rank=15 price=32.95 support=27.11 resistance=33.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=50.29 liquidity=12721618.0 spike=1.09
- ALUM.CA: score=11.93 buy_ready=False sector_rank=11 price=20.93 support=16.02 resistance=21.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=54.72 liquidity=2528440.25 spike=0.83
- AMER.CA: score=20.66 buy_ready=False sector_rank=16 price=4.4 support=3.21 resistance=4.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=58.78 liquidity=72634824.0 spike=1.13
- AMES.CA: score=20.06 buy_ready=False sector_rank=11 price=51.46 support=28.0 resistance=53.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=78.38 liquidity=202247920.0 spike=1.33
- AMIA.CA: score=18.4 buy_ready=False sector_rank=11 price=17.31 support=14.0 resistance=19.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.02 liquidity=12277023.0 spike=0.94
- AMOC.CA: score=16.4 buy_ready=False sector_rank=12 price=13.06 support=12.55 resistance=15.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=45.29 liquidity=68034856.0 spike=0.47
- APSW.CA: score=9.74 buy_ready=False sector_rank=11 price=7.97 support=7.1 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=340565.25 spike=0.7
- ARAB.CA: score=23.4 buy_ready=False sector_rank=16 price=0.26 support=0.2 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=53.45 liquidity=30515852.0 spike=0.34
- ARCC.CA: score=25.4 buy_ready=False sector_rank=7 price=69.57 support=58.01 resistance=71.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=62.72 liquidity=19383928.0 spike=0.54
- AREH.CA: score=13.42 buy_ready=False sector_rank=11 price=1.12 support=0.91 resistance=1.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=55.32 liquidity=4017496.25 spike=0.51
- ASCM.CA: score=12.25 buy_ready=False sector_rank=11 price=49.12 support=38.2 resistance=50.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=55.38 liquidity=2849363.5 spike=0.37
- ASPI.CA: score=19.4 buy_ready=False sector_rank=11 price=0.34 support=0.27 resistance=0.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=60.49 liquidity=14481299.0 spike=0.61
- ATLC.CA: score=11.35 buy_ready=False sector_rank=17 price=5.62 support=5.1 resistance=5.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36751588.0 spike=4.15
- ATQA.CA: score=20.72 buy_ready=False sector_rank=18 price=10.3 support=8.25 resistance=11.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=50.12 liquidity=57450888.0 spike=1.32
- AXPH.CA: score=17.94 buy_ready=False sector_rank=11 price=1483.54 support=1135.0 resistance=1475.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=68.76 liquidity=6764536.0 spike=1.39
- BINV.CA: score=17.97 buy_ready=False sector_rank=19 price=54.18 support=50.62 resistance=62.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=44.15 liquidity=13660559.0 spike=1.35
- BIOC.CA: score=24.5 buy_ready=False sector_rank=11 price=425.04 support=212.05 resistance=446.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=78.33 liquidity=453240320.0 spike=3.05
- BTFH.CA: score=19.35 buy_ready=False sector_rank=17 price=2.45 support=2.05 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=47.52 liquidity=87695920.0 spike=0.71
- CAED.CA: score=22.28 buy_ready=False sector_rank=11 price=110.14 support=64.0 resistance=116.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=65.75 liquidity=45421880.0 spike=1.94
- CCAP.CA: score=19.27 buy_ready=False sector_rank=19 price=6.1 support=5.55 resistance=6.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=323277184.0 spike=0.78
- CCRS.CA: score=23.7 buy_ready=False sector_rank=11 price=2.1 support=1.3 resistance=2.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=60.42 liquidity=41600588.0 spike=2.65
- CEFM.CA: score=12.56 buy_ready=False sector_rank=11 price=126.41 support=97.79 resistance=132.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:08 PM market time freshness=DELAYED_CURRENT RSI=53.14 liquidity=2157159.5 spike=0.88
- CERA.CA: score=19.4 buy_ready=False sector_rank=11 price=1.12 support=0.93 resistance=1.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=32526788.0 spike=0.41
- CFGH.CA: score=-2.69 buy_ready=False sector_rank=11 price=0.11 support=0.11 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7786.04 spike=1.45
- CICH.CA: score=8.49 buy_ready=False sector_rank=17 price=10.61 support=9.63 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:12 PM market time freshness=DELAYED_CURRENT RSI=46.91 liquidity=1142953.63 spike=0.54
- CIEB.CA: score=26.16 buy_ready=False sector_rank=14 price=23.15 support=21.35 resistance=23.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=52.57 liquidity=27193732.0 spike=3.38
- CIRA.CA: score=23.96 buy_ready=False sector_rank=9 price=39.02 support=32.01 resistance=39.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=66.64 liquidity=16895052.0 spike=1.28
- CLHO.CA: score=19.4 buy_ready=False sector_rank=5 price=14.42 support=12.51 resistance=15.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=63.11 liquidity=16241364.0 spike=0.37
- CNFN.CA: score=11.43 buy_ready=False sector_rank=17 price=4.19 support=3.25 resistance=4.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=54.59 liquidity=2079394.75 spike=0.24
- COMI.CA: score=22.4 buy_ready=False sector_rank=14 price=128.81 support=117.41 resistance=131.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=59.03 liquidity=195606960.0 spike=0.39
- COPR.CA: score=20.68 buy_ready=False sector_rank=11 price=0.42 support=0.33 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=55.93 liquidity=21338112.0 spike=1.14
- COSG.CA: score=14.46 buy_ready=False sector_rank=11 price=1.4 support=1.11 resistance=1.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=57.38 liquidity=5062439.5 spike=0.55
- CPCI.CA: score=17.13 buy_ready=False sector_rank=11 price=595.62 support=502.25 resistance=620.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=54.43 liquidity=5490431.0 spike=1.12
- CSAG.CA: score=15.39 buy_ready=False sector_rank=15 price=35.43 support=30.1 resistance=37.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=4986233.0 spike=0.73
- DAPH.CA: score=20.4 buy_ready=False sector_rank=11 price=90.27 support=65.2 resistance=98.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=60.67 liquidity=12722780.0 spike=0.56
- DEIN.CA: score=9.4 buy_ready=False sector_rank=11 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=29 October 12:10 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=62.1 spike=0.02
- DOMT.CA: score=13.84 buy_ready=False sector_rank=6 price=25.34 support=20.27 resistance=25.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=65.92 liquidity=1444770.63 spike=0.63
- DSCW.CA: score=19.9 buy_ready=False sector_rank=11 price=1.57 support=1.23 resistance=1.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=55.22 liquidity=18046868.0 spike=1.25
- DTPP.CA: score=11.4 buy_ready=False sector_rank=11 price=64.02 support=63.31 resistance=69.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=202918992.0 spike=4.59
- EALR.CA: score=16.34 buy_ready=False sector_rank=11 price=312.94 support=236.01 resistance=337.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=61.39 liquidity=4937571.5 spike=0.64
- EASB.CA: score=14.22 buy_ready=False sector_rank=11 price=6.69 support=5.03 resistance=7.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=57.96 liquidity=3822064.25 spike=0.54
- EAST.CA: score=27.4 buy_ready=False sector_rank=6 price=34.94 support=27.02 resistance=35.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=69.45 liquidity=342024544.0 spike=9.0
- EBSC.CA: score=14.93 buy_ready=False sector_rank=11 price=1.66 support=1.2 resistance=1.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=60.49 liquidity=5051695.5 spike=1.24
- ECAP.CA: score=23.02 buy_ready=False sector_rank=11 price=30.06 support=24.8 resistance=30.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=62.24 liquidity=7215666.5 spike=2.7
- EDFM.CA: score=10.9 buy_ready=False sector_rank=11 price=366.36 support=326.73 resistance=378.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:01 PM market time freshness=DELAYED_CURRENT RSI=56.54 liquidity=502604.78 spike=0.43
- EEII.CA: score=11.4 buy_ready=False sector_rank=11 price=2.15 support=2.02 resistance=2.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=50440260.0 spike=4.68
- EFIC.CA: score=22.08 buy_ready=False sector_rank=18 price=169.66 support=121.0 resistance=174.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=60.43 liquidity=14890013.0 spike=0.53
- EFID.CA: score=19.4 buy_ready=False sector_rank=6 price=19.4 support=16.01 resistance=20.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=59.9 liquidity=22441694.0 spike=0.65
- EFIH.CA: score=20.4 buy_ready=False sector_rank=10 price=24.92 support=20.3 resistance=25.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=87.25 liquidity=29654750.0 spike=0.51
- EGAL.CA: score=20.08 buy_ready=False sector_rank=18 price=322.79 support=275.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=64.17 liquidity=63143364.0 spike=0.58
- EGAS.CA: score=24.82 buy_ready=False sector_rank=12 price=51.75 support=43.0 resistance=53.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=55.23 liquidity=13414661.0 spike=3.21
- EGBE.CA: score=6.42 buy_ready=False sector_rank=14 price=0.5 support=0.47 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=47.19 liquidity=24563.08 spike=0.41
- EGCH.CA: score=19.08 buy_ready=False sector_rank=18 price=11.01 support=9.66 resistance=12.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=45.5 liquidity=30593094.0 spike=0.6
- EGSA.CA: score=13.4 buy_ready=False sector_rank=4 price=9.0 support=8.7 resistance=9.07 source=Yahoo Finance as_of=2026-11-10T22:00:00+00:00 freshness=FRESH RSI=47.54 liquidity=4500.0 spike=0.65
- EGTS.CA: score=25.76 buy_ready=False sector_rank=16 price=13.98 support=10.19 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=60.1 liquidity=53213736.0 spike=2.68
- EHDR.CA: score=15.45 buy_ready=False sector_rank=11 price=2.23 support=1.8 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=54.46 liquidity=6047499.5 spike=0.6
- ELEC.CA: score=19.4 buy_ready=False sector_rank=8 price=1.73 support=1.34 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=56.96 liquidity=20243314.0 spike=0.38
- ELKA.CA: score=22.8 buy_ready=False sector_rank=11 price=1.59 support=1.21 resistance=1.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=60.81 liquidity=9402094.0 spike=0.71
- ELNA.CA: score=10.54 buy_ready=False sector_rank=11 price=43.4 support=33.46 resistance=44.2 source=Yahoo Finance as_of=2026-11-10T22:00:00+00:00 freshness=FRESH RSI=76.35 liquidity=139704.6 spike=0.19
- ELSH.CA: score=21.62 buy_ready=False sector_rank=11 price=11.54 support=8.57 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=60.38 liquidity=25262862.0 spike=1.61
- ELWA.CA: score=1.42 buy_ready=False sector_rank=11 price=1.3 support=1.27 resistance=1.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=19.23 liquidity=1018156.25 spike=0.87
- EMFD.CA: score=15.4 buy_ready=False sector_rank=16 price=12.63 support=10.6 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=76.17 liquidity=48518816.0 spike=0.83
- ENGC.CA: score=11.4 buy_ready=False sector_rank=11 price=42.06 support=39.51 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=58502024.0 spike=4.26
- EOSB.CA: score=9.46 buy_ready=False sector_rank=11 price=1.61 support=1.55 resistance=1.72 source=Yahoo Finance as_of=2026-11-10T22:00:00+00:00 freshness=FRESH RSI=70.0 liquidity=61315.24 spike=0.65
- EPCO.CA: score=23.18 buy_ready=False sector_rank=11 price=9.27 support=7.0 resistance=9.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=62.63 liquidity=15746702.0 spike=2.89
- EPPK.CA: score=-3.18 buy_ready=False sector_rank=11 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=27.0 buy_ready=False sector_rank=4 price=133.89 support=115.0 resistance=146.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=51.07 liquidity=647921664.0 spike=2.8
- ETRS.CA: score=26.34 buy_ready=False sector_rank=11 price=11.05 support=9.51 resistance=11.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=61.75 liquidity=34024272.0 spike=2.47
- EXPA.CA: score=21.4 buy_ready=False sector_rank=14 price=14.63 support=12.0 resistance=15.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=55.86 liquidity=11706605.0 spike=0.5
- FAIT.CA: score=19.81 buy_ready=False sector_rank=14 price=46.85 support=40.0 resistance=46.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=58.01 liquidity=3611731.5 spike=1.4
- FAITA.CA: score=13.43 buy_ready=False sector_rank=14 price=1.0 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:09 PM market time freshness=DELAYED_CURRENT RSI=50.54 liquidity=33942.5 spike=0.97
- FERC.CA: score=12.12 buy_ready=False sector_rank=18 price=68.12 support=52.63 resistance=72.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=57.22 liquidity=3035657.75 spike=0.39
- FWRY.CA: score=20.16 buy_ready=False sector_rank=10 price=18.2 support=15.27 resistance=18.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=51.58 liquidity=150826032.0 spike=1.38
- GBCO.CA: score=15.76 buy_ready=False sector_rank=20 price=23.38 support=20.9 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=39.72 liquidity=69874072.0 spike=0.57
- GDWA.CA: score=14.58 buy_ready=False sector_rank=11 price=0.57 support=0.46 resistance=0.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=52.86 liquidity=5184426.0 spike=0.42
- GGCC.CA: score=19.68 buy_ready=False sector_rank=11 price=0.58 support=0.49 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=51.2 liquidity=26839968.0 spike=1.14
- GIHD.CA: score=21.98 buy_ready=False sector_rank=11 price=55.43 support=32.1 resistance=57.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=63.38 liquidity=28607798.0 spike=1.79
- GMCI.CA: score=20.92 buy_ready=False sector_rank=11 price=1.7 support=1.34 resistance=1.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=1519416.88 spike=4.66
- GRCA.CA: score=19.4 buy_ready=False sector_rank=11 price=35.08 support=22.57 resistance=37.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=65.43 liquidity=10271430.0 spike=0.92
- GSSC.CA: score=11.77 buy_ready=False sector_rank=11 price=267.14 support=211.52 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=51.62 liquidity=1374560.25 spike=0.9
- HDBK.CA: score=11.4 buy_ready=False sector_rank=14 price=109.0 support=103.06 resistance=111.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=100632296.0 spike=4.03
- HELI.CA: score=20.4 buy_ready=False sector_rank=16 price=7.01 support=5.72 resistance=7.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=47039212.0 spike=0.59
- HRHO.CA: score=22.35 buy_ready=False sector_rank=17 price=25.09 support=21.87 resistance=26.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=55.67 liquidity=30506740.0 spike=0.55
- ICID.CA: score=11.48 buy_ready=False sector_rank=11 price=17.48 support=14.26 resistance=18.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=53.67 liquidity=1084969.5 spike=0.24
- IDRE.CA: score=27.4 buy_ready=False sector_rank=11 price=45.33 support=29.11 resistance=44.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=58.65 liquidity=27372388.0 spike=4.19
- IFAP.CA: score=15.41 buy_ready=False sector_rank=2 price=17.8 support=15.12 resistance=19.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=49.3 liquidity=4014048.0 spike=0.6
- INFI.CA: score=11.4 buy_ready=False sector_rank=11 price=147.88 support=125.61 resistance=150.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=236440768.0 spike=10.69
- IRON.CA: score=23.46 buy_ready=False sector_rank=18 price=26.9 support=23.13 resistance=27.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=50.53 liquidity=14789778.0 spike=1.69
- ISMA.CA: score=23.16 buy_ready=False sector_rank=11 price=21.95 support=14.11 resistance=23.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=54.94 liquidity=30108854.0 spike=2.88
- ISMQ.CA: score=15.36 buy_ready=False sector_rank=18 price=7.57 support=5.96 resistance=7.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=56.95 liquidity=6279264.0 spike=0.47
- ISPH.CA: score=19.4 buy_ready=False sector_rank=5 price=10.33 support=9.02 resistance=11.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=53.3 liquidity=34952868.0 spike=0.56
- JUFO.CA: score=22.48 buy_ready=False sector_rank=6 price=24.07 support=21.01 resistance=25.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=56.82 liquidity=59384052.0 spike=2.54
- KABO.CA: score=20.46 buy_ready=False sector_rank=13 price=7.39 support=5.58 resistance=8.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=52.41 liquidity=20588154.0 spike=1.03
- KWIN.CA: score=25.86 buy_ready=False sector_rank=11 price=77.42 support=44.02 resistance=85.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=66.13 liquidity=24896432.0 spike=2.23
- KZPC.CA: score=24.42 buy_ready=False sector_rank=11 price=13.62 support=11.56 resistance=14.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=57.17 liquidity=14560269.0 spike=1.51
- LCSW.CA: score=23.9 buy_ready=False sector_rank=7 price=41.32 support=28.0 resistance=40.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=72.09 liquidity=28281672.0 spike=1.25
- LUTS.CA: score=8.66 buy_ready=False sector_rank=11 price=0.82 support=0.77 resistance=0.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=132120408.0 spike=2.13
- MAAL.CA: score=19.44 buy_ready=False sector_rank=11 price=6.81 support=4.88 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=54.15 liquidity=29373332.0 spike=1.52
- MASR.CA: score=20.4 buy_ready=False sector_rank=11 price=6.91 support=5.6 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=53.94 liquidity=17520878.0 spike=0.44
- MBSC.CA: score=20.4 buy_ready=False sector_rank=7 price=341.3 support=262.0 resistance=400.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=59.54 liquidity=28767000.0 spike=0.46
- MCQE.CA: score=19.4 buy_ready=False sector_rank=7 price=183.37 support=144.0 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=66.92 liquidity=42014596.0 spike=0.82
- MCRO.CA: score=22.4 buy_ready=False sector_rank=11 price=1.41 support=1.07 resistance=1.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=59.46 liquidity=36414732.0 spike=0.71
- MENA.CA: score=13.19 buy_ready=False sector_rank=16 price=5.96 support=5.45 resistance=6.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=56.08 liquidity=1788525.0 spike=0.45
- MEPA.CA: score=18.43 buy_ready=False sector_rank=11 price=1.43 support=1.14 resistance=1.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=47.76 liquidity=9028691.0 spike=0.51
- MFPC.CA: score=10.08 buy_ready=False sector_rank=18 price=39.21 support=37.23 resistance=47.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=52774516.0 spike=0.62
- MFSC.CA: score=10.02 buy_ready=False sector_rank=11 price=37.47 support=28.55 resistance=42.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:11 PM market time freshness=DELAYED_CURRENT RSI=47.24 liquidity=623583.06 spike=0.28
- MHOT.CA: score=27.64 buy_ready=False sector_rank=1 price=16.43 support=13.0 resistance=17.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=66.19 liquidity=12160767.0 spike=2.12
- MICH.CA: score=23.73 buy_ready=False sector_rank=11 price=46.35 support=35.5 resistance=45.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=65.82 liquidity=9548287.0 spike=1.39
- MILS.CA: score=20.7 buy_ready=False sector_rank=11 price=153.34 support=94.24 resistance=158.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:13 PM market time freshness=DELAYED_CURRENT RSI=59.71 liquidity=10681847.0 spike=1.15
- MIPH.CA: score=17.44 buy_ready=False sector_rank=5 price=792.68 support=610.0 resistance=819.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=63.76 liquidity=2037929.75 spike=0.65
- MOED.CA: score=18.64 buy_ready=False sector_rank=11 price=0.52 support=0.39 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=49.33 liquidity=9241692.0 spike=0.63
- MOIL.CA: score=15.6 buy_ready=False sector_rank=12 price=0.68 support=0.6 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=200450.62 spike=0.96
- MOIN.CA: score=30.4 buy_ready=False sector_rank=11 price=34.0 support=25.7 resistance=33.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=61.38 liquidity=33748508.0 spike=3.98
- MOSC.CA: score=20.43 buy_ready=False sector_rank=11 price=287.0 support=198.01 resistance=303.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=63.9 liquidity=5034219.5 spike=0.9
- MPCI.CA: score=24.78 buy_ready=False sector_rank=11 price=372.3 support=238.6 resistance=366.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=65.02 liquidity=191452000.0 spike=1.69
- MPCO.CA: score=29.44 buy_ready=False sector_rank=2 price=2.25 support=1.55 resistance=2.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=60.75 liquidity=287061248.0 spike=3.02
- MPRC.CA: score=24.42 buy_ready=False sector_rank=11 price=39.91 support=27.0 resistance=40.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=66.08 liquidity=30926920.0 spike=1.51
- MTIE.CA: score=17.76 buy_ready=False sector_rank=20 price=7.21 support=6.05 resistance=7.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=50.13 liquidity=14305413.0 spike=0.66
- NAHO.CA: score=10.03 buy_ready=False sector_rank=11 price=0.13 support=0.12 resistance=0.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=42.11 liquidity=29397.95 spike=1.8
- NCCW.CA: score=25.0 buy_ready=False sector_rank=11 price=6.09 support=4.05 resistance=6.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=59.06 liquidity=55825152.0 spike=3.3
- NEDA.CA: score=3.84 buy_ready=False sector_rank=11 price=2.46 support=2.26 resistance=2.6 source=Yahoo Finance as_of=2026-11-10T22:00:00+00:00 freshness=FRESH RSI=29.41 liquidity=297389.4 spike=1.57
- NHPS.CA: score=14.49 buy_ready=False sector_rank=11 price=65.23 support=50.0 resistance=69.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=61.48 liquidity=5088007.5 spike=0.62
- NINH.CA: score=20.3 buy_ready=False sector_rank=11 price=17.12 support=12.36 resistance=18.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=67.07 liquidity=9901909.0 spike=0.85
- NIPH.CA: score=23.56 buy_ready=False sector_rank=5 price=332.63 support=205.0 resistance=325.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=66.3 liquidity=163611584.0 spike=1.08
- OBRI.CA: score=15.69 buy_ready=False sector_rank=11 price=25.28 support=18.11 resistance=27.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=53.24 liquidity=6294580.5 spike=0.68
- OCDI.CA: score=20.4 buy_ready=False sector_rank=16 price=26.16 support=21.0 resistance=26.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=57.8 liquidity=16218404.0 spike=0.46
- OCPH.CA: score=17.41 buy_ready=False sector_rank=11 price=210.61 support=147.96 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=62.05 liquidity=5729131.0 spike=1.14
- ODIN.CA: score=16.29 buy_ready=False sector_rank=11 price=2.19 support=1.7 resistance=2.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=56.86 liquidity=6890235.0 spike=0.83
- OFH.CA: score=18.4 buy_ready=False sector_rank=11 price=0.79 support=0.61 resistance=0.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=65.55 liquidity=12500599.0 spike=0.58
- OIH.CA: score=19.27 buy_ready=False sector_rank=19 price=1.76 support=1.5 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.75 liquidity=28401944.0 spike=0.64
- OLFI.CA: score=24.4 buy_ready=False sector_rank=6 price=20.71 support=17.86 resistance=21.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=57.64 liquidity=41242080.0 spike=5.24
- ORAS.CA: score=4.6 buy_ready=False sector_rank=21 price=799.0 support=798.8 resistance=811.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=125156808.0 spike=1.0
- ORHD.CA: score=19.4 buy_ready=False sector_rank=16 price=10.29 support=8.5 resistance=11.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=60.06 liquidity=87184456.0 spike=0.77
- ORWE.CA: score=20.4 buy_ready=False sector_rank=13 price=26.39 support=22.2 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=55.5 liquidity=26566364.0 spike=0.78
- PHAR.CA: score=25.52 buy_ready=False sector_rank=5 price=112.27 support=90.2 resistance=113.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=62.27 liquidity=70496520.0 spike=1.06
- PHDC.CA: score=20.4 buy_ready=False sector_rank=16 price=12.4 support=10.33 resistance=13.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=63066724.0 spike=0.48
- PHTV.CA: score=13.4 buy_ready=False sector_rank=11 price=330.1 support=300.0 resistance=343.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=54.59 liquidity=1995304.0 spike=1.5
- POUL.CA: score=20.92 buy_ready=False sector_rank=6 price=10.18 support=8.81 resistance=10.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=60.98 liquidity=187641872.0 spike=1.76
- PRCL.CA: score=11.4 buy_ready=False sector_rank=7 price=21.08 support=20.8 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=108125304.0 spike=5.34
- PRDC.CA: score=20.4 buy_ready=False sector_rank=16 price=6.85 support=5.08 resistance=7.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=61.37 liquidity=13082868.0 spike=0.62
- PRMH.CA: score=28.4 buy_ready=False sector_rank=11 price=2.37 support=1.7 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=69.44 liquidity=20727260.0 spike=3.51
- RACC.CA: score=15.13 buy_ready=False sector_rank=11 price=8.16 support=6.1 resistance=9.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=54.58 liquidity=5727692.5 spike=0.82
- RAKT.CA: score=13.99 buy_ready=False sector_rank=11 price=22.47 support=20.4 resistance=23.16 source=Yahoo Finance as_of=2026-11-10T22:00:00+00:00 freshness=FRESH RSI=39.43 liquidity=430300.49 spike=1.58
- RAYA.CA: score=22.4 buy_ready=False sector_rank=3 price=6.23 support=5.02 resistance=6.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=63.01 liquidity=24328958.0 spike=0.99
- RMDA.CA: score=21.6 buy_ready=False sector_rank=5 price=5.6 support=4.5 resistance=5.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=34581876.0 spike=1.1
- ROTO.CA: score=20.74 buy_ready=False sector_rank=11 price=35.94 support=25.0 resistance=37.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=60.47 liquidity=16303860.0 spike=1.67
- RREI.CA: score=16.35 buy_ready=False sector_rank=11 price=2.86 support=1.96 resistance=3.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=47.89 liquidity=8945165.0 spike=0.77
- RTVC.CA: score=15.52 buy_ready=False sector_rank=11 price=3.11 support=2.66 resistance=3.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 November 02:14 PM market time freshness=DELAYED_CURRENT RSI=46.22 liquidity=4717888.5 spike=1.7
- RUBX.CA: score=25.9 buy_ready=False sector_rank=11 price=14.73 support=10.51 resistance=18.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=42.21 liquidity=141028096.0 spike=2.25
- SAUD.CA: score=28.04 buy_ready=False sector_rank=14 price=22.5 support=19.3 resistance=23.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=62.97 liquidity=40798288.0 spike=2.32
- SCEM.CA: score=21.58 buy_ready=False sector_rank=7 price=100.03 support=73.9 resistance=99.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=70.94 liquidity=50320668.0 spike=1.09
- SCFM.CA: score=13.7 buy_ready=False sector_rank=11 price=224.89 support=153.02 resistance=238.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:13 PM market time freshness=DELAYED_CURRENT RSI=51.09 liquidity=3678236.0 spike=1.31
- SCTS.CA: score=11.89 buy_ready=False sector_rank=9 price=501.42 support=410.0 resistance=555.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=53.02 liquidity=1491503.25 spike=0.24
- SDTI.CA: score=23.4 buy_ready=False sector_rank=11 price=85.45 support=75.01 resistance=90.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=63.85 liquidity=16540667.0 spike=0.86
- SEIG.CA: score=22.78 buy_ready=False sector_rank=11 price=238.02 support=142.0 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=65.37 liquidity=16502271.0 spike=1.69
- SIPC.CA: score=25.32 buy_ready=False sector_rank=11 price=5.63 support=3.73 resistance=6.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=57.06 liquidity=89194464.0 spike=1.96
- SKPC.CA: score=19.08 buy_ready=False sector_rank=18 price=14.96 support=14.01 resistance=15.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=53.85 liquidity=26746726.0 spike=0.68
- SMFR.CA: score=18.07 buy_ready=False sector_rank=11 price=224.18 support=165.0 resistance=264.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=62.42 liquidity=4667159.0 spike=0.61
- SNFC.CA: score=23.98 buy_ready=False sector_rank=11 price=11.25 support=10.08 resistance=11.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=51.74 liquidity=12573547.0 spike=1.29
- SPIN.CA: score=12.56 buy_ready=False sector_rank=13 price=15.28 support=12.0 resistance=16.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=61.96 liquidity=2159238.0 spike=0.36
- SPMD.CA: score=17.18 buy_ready=False sector_rank=11 price=0.35 support=0.3 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=51.77 liquidity=9781278.0 spike=0.54
- SUGR.CA: score=11.4 buy_ready=False sector_rank=6 price=53.5 support=50.0 resistance=55.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=94298392.0 spike=5.75
- SVCE.CA: score=20.4 buy_ready=False sector_rank=11 price=9.26 support=7.01 resistance=9.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=56.36 liquidity=30333028.0 spike=0.58
- SWDY.CA: score=21.4 buy_ready=False sector_rank=8 price=120.13 support=97.0 resistance=123.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=71.03 liquidity=33290050.0 spike=0.59
- TALM.CA: score=22.9 buy_ready=False sector_rank=9 price=20.61 support=17.0 resistance=21.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=61.09 liquidity=9496121.0 spike=0.49
- TMGH.CA: score=19.4 buy_ready=False sector_rank=16 price=84.53 support=76.5 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=171312896.0 spike=0.64
- TRTO.CA: score=10.19 buy_ready=False sector_rank=11 price=0.06 support=0.05 resistance=0.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:11 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=10280.62 spike=1.89
- UEFM.CA: score=21.53 buy_ready=False sector_rank=11 price=520.19 support=422.0 resistance=520.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=60.29 liquidity=3754241.5 spike=2.19
- UEGC.CA: score=19.4 buy_ready=False sector_rank=11 price=1.53 support=1.21 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=56.76 liquidity=21242606.0 spike=0.43
- UNIP.CA: score=16.13 buy_ready=False sector_rank=11 price=0.33 support=0.25 resistance=0.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=59.2 liquidity=5733753.0 spike=0.77
- UNIT.CA: score=13.78 buy_ready=False sector_rank=16 price=17.57 support=15.06 resistance=19.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=58.02 liquidity=2720799.0 spike=1.33
- WCDF.CA: score=12.73 buy_ready=False sector_rank=11 price=548.58 support=432.5 resistance=559.0 source=Yahoo Finance as_of=2026-11-10T22:00:00+00:00 freshness=FRESH RSI=71.79 liquidity=1768621.98 spike=1.28
- WKOL.CA: score=7.61 buy_ready=False sector_rank=11 price=184.81 support=145.33 resistance=309.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=27.06 liquidity=5211469.5 spike=0.42
- ZEOT.CA: score=21.76 buy_ready=False sector_rank=11 price=12.19 support=7.9 resistance=12.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=60.83 liquidity=6358408.0 spike=0.67
- ZMID.CA: score=20.4 buy_ready=False sector_rank=16 price=6.99 support=5.91 resistance=7.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=54.79 liquidity=39512348.0 spike=0.47

## Backtesting Lite
- MOIN.CA: 180d return=46.67%, max drawdown=-38.72%, MA20>MA50 days last20=0, as_of=2026-11-10T22:00:00+00:00
- MPCO.CA: 180d return=27.98%, max drawdown=-42.18%, MA20>MA50 days last20=3, as_of=2026-11-10T22:00:00+00:00
- PRMH.CA: 180d return=13.4%, max drawdown=-40.0%, MA20>MA50 days last20=0, as_of=2026-11-10T22:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- MOIN.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Mohandes Insurance Company summary=Mohandes Insurance unveils EGP 150m capital hike; Mohandes Insurance targets EGP 1.39bn investments in FY23/24; Mohandes Insurance eyes EGP 1bn investments in FY22/23
  - Mohandes Insurance unveils EGP 150m capital hike: https://english.mubasher.info/news/4538925/Mohandes-Insurance-unveils-EGP-150m-capital-hike/
  - Mohandes Insurance targets EGP 1.39bn investments in FY23/24: https://english.mubasher.info/news/4147038/Mohandes-Insurance-targets-EGP-1-39bn-investments-in-FY23-24/
  - Mohandes Insurance eyes EGP 1bn investments in FY22/23: https://english.mubasher.info/news/3986755/Mohandes-Insurance-eyes-EGP-1bn-investments-in-FY22-23/
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=680 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- PRMH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Prime Holding S.A.E summary=Evidence rejected for PRMH.CA: source text did not clearly match PRMH.CA / Prime Holding S.A.E.
- SAUD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=680 sources=3 expected=Al Baraka Bank Egypt summary=Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26; Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE; Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025
  - Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26: https://english.mubasher.info/news/4611927/Al-Baraka-Bank-Egypt-records-EGP-2-2bn-operating-income-in-Q1-26/
  - Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE: https://english.mubasher.info/news/4583822/Al-Baraka-Bank-Egypt-files-MTO-to-acquire-majority-stake-in-A-T-LEASE/
  - Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025: https://english.mubasher.info/news/4583458/Al-Baraka-Bank-Egypt-to-pay-EGP-1-1-share-dividends-for-2025/
- MHOT.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Hotels summary=Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26; Shareholder buys EGP 3.39m worth of shares in Misr Hotels; Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits
  - Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26: https://english.mubasher.info/news/4602482/Misr-Hotels-net-profits-cross-EGP-1-1bn-in-9M-25-26/
  - Shareholder buys EGP 3.39m worth of shares in Misr Hotels: https://english.mubasher.info/news/4013808/Shareholder-buys-EGP-3-39m-worth-of-shares-in-Misr-Hotels/
  - Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits: https://english.mubasher.info/news/3975543/Misr-Hotels-repays-EGP-383m-of-NBE-s-loan-unveils-estimated-profits/
- EAST.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Eastern Company summary=Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- IDRE.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Ismailia Development and Real Estate Co summary=Evidence rejected for IDRE.CA: source text did not clearly match IDRE.CA / Ismailia Development and Real Estate Co.
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.

## Warnings
- OpenRouter API error: 404
- Evidence for MOIN.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for PRMH.CA: source text did not clearly match PRMH.CA / Prime Holding S.A.E.
- Evidence for SAUD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for MHOT.CA matches the company but no source/report date was detected.
- Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- Evidence rejected for IDRE.CA: source text did not clearly match IDRE.CA / Ismailia Development and Real Estate Co.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
