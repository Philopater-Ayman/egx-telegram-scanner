# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-11-08T18:03:17.411895+00:00
Generated Cairo: 2026-11-08 20:03
Run timing: target 15:30 Cairo | generated Cairo 2026-11-08 20:03 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-11-08 19:59

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 172/187
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, November 08
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 70.59% / above MA50 11.76%
- EGX70 regime: BEARISH / above MA20 57.89% / above MA50 5.26%
- Sector breadth: 9.52%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- AMES.CA: liquidity=426769184.0 spike=6.83 score=10.14
- BIOC.CA: liquidity=311910464.0 spike=3.73 score=10.14
- PHDC.CA: liquidity=295954944.0 spike=2.81 score=20.37
- MFPC.CA: liquidity=199628672.0 spike=3.43 score=10.01
- TMGH.CA: liquidity=194132080.0 spike=0.72 score=18.75

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- SMFR.CA: spike=18.04 liquidity=55294844.0 outlook=CONSTRUCTIVE score=66.85 buy_ready=False
- CFGH.CA: spike=14.31 liquidity=87222.18 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EGSA.CA: spike=9.55 liquidity=56348.0 outlook=CONSTRUCTIVE score=66 buy_ready=False
- MPRC.CA: spike=7.36 liquidity=109644680.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AMES.CA: spike=6.83 liquidity=426769184.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=10.11 5d=2.95% 20d=-7.47% aboveMA50=50.0%
- #2 Tourism & Leisure: score=8.13 5d=2.61% 20d=-3.12% aboveMA50=0.0%
- #3 Industrial Goods & Cables: score=6.31 5d=6.62% 20d=-5.04% aboveMA50=0.0%
- #4 Education: score=6.28 5d=5.69% 20d=-5.83% aboveMA50=33.33%
- #5 Food, Beverages & Tobacco: score=5.56 5d=2.74% 20d=-1.36% aboveMA50=14.29%
- #6 Building Materials: score=4.48 5d=5.7% 20d=-8.88% aboveMA50=16.67%
- #7 Transportation & Logistics: score=4.39 5d=4.46% 20d=-2.91% aboveMA50=0.0%
- #8 Real Estate: score=4.37 5d=4.47% 20d=-8.49% aboveMA50=7.69%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- KZPC.CA: BULLISH_WATCH score=82.85 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- TALM.CA: BULLISH_WATCH score=76.28 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- SCEM.CA: BULLISH_WATCH score=75.48 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support; close to resistance
- EFIH.CA: BULLISH_WATCH score=73.54 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- SNFC.CA: BULLISH_WATCH score=72.85 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- UNIT.CA: CONSTRUCTIVE score=68.37 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended; sector is not leading
- MHOT.CA: CONSTRUCTIVE score=68.13 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=below MA50; far above support
- SMFR.CA: CONSTRUCTIVE score=66.85 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support; sector is not leading
- EGSA.CA: CONSTRUCTIVE score=66 liquidity=THIN sector=LEADING risk=liquidity below minimum; close to resistance
- POUL.CA: CONSTRUCTIVE score=65.56 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA50

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=19.86 buy_ready=False sector_rank=13 price=243.39 support=171.02 resistance=270.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=58.1 liquidity=22144874.0 spike=1.36
- ABUK.CA: score=6.97 buy_ready=False sector_rank=12 price=76.25 support=76.12 resistance=80.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=180774464.0 spike=1.91
- ACAMD.CA: score=18.14 buy_ready=False sector_rank=13 price=2.0 support=1.86 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=43.4 liquidity=44869644.0 spike=0.87
- ACGC.CA: score=9.79 buy_ready=False sector_rank=16 price=13.2 support=11.6 resistance=14.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:10 PM market time freshness=DELAYED_CURRENT RSI=55.65 liquidity=1370137.5 spike=0.18
- ADCI.CA: score=10.24 buy_ready=False sector_rank=13 price=257.96 support=221.0 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:13 PM market time freshness=DELAYED_CURRENT RSI=51.66 liquidity=1095109.75 spike=0.56
- ADIB.CA: score=19.67 buy_ready=False sector_rank=9 price=48.62 support=43.16 resistance=50.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=64.18 liquidity=53986132.0 spike=0.64
- ADPC.CA: score=13.59 buy_ready=False sector_rank=13 price=3.04 support=2.53 resistance=3.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=51.56 liquidity=5448541.0 spike=0.64
- AFDI.CA: score=9.57 buy_ready=False sector_rank=13 price=45.06 support=34.8 resistance=54.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=45.67 liquidity=2431490.0 spike=0.84
- AFMC.CA: score=19.38 buy_ready=False sector_rank=13 price=138.46 support=94.6 resistance=153.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=60.06 liquidity=19748002.0 spike=1.12
- AJWA.CA: score=10.14 buy_ready=False sector_rank=13 price=255.55 support=223.25 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=134454272.0 spike=4.57
- ALCN.CA: score=17.76 buy_ready=False sector_rank=7 price=32.17 support=27.11 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=53.46 liquidity=10104814.0 spike=0.85
- ALUM.CA: score=10.03 buy_ready=False sector_rank=13 price=20.32 support=16.02 resistance=23.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:10 PM market time freshness=DELAYED_CURRENT RSI=54.5 liquidity=1892308.63 spike=0.59
- AMER.CA: score=23.55 buy_ready=False sector_rank=8 price=4.54 support=3.21 resistance=5.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=56.63 liquidity=163062320.0 spike=2.9
- AMES.CA: score=10.14 buy_ready=False sector_rank=13 price=45.78 support=38.6 resistance=45.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=426769184.0 spike=6.83
- AMIA.CA: score=15.37 buy_ready=False sector_rank=13 price=17.99 support=14.0 resistance=19.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=56.57 liquidity=6228639.5 spike=0.51
- AMOC.CA: score=13.32 buy_ready=False sector_rank=19 price=13.19 support=12.55 resistance=15.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=52.35 liquidity=68009280.0 spike=0.47
- APSW.CA: score=9.94 buy_ready=False sector_rank=13 price=7.33 support=7.1 resistance=8.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:12 PM market time freshness=DELAYED_CURRENT RSI=39.11 liquidity=1037928.75 spike=2.38
- ARAB.CA: score=15.77 buy_ready=False sector_rank=8 price=0.25 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=105234448.0 spike=1.01
- ARCC.CA: score=19.79 buy_ready=False sector_rank=6 price=67.71 support=58.01 resistance=73.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=55.08 liquidity=15626001.0 spike=0.42
- AREH.CA: score=12.64 buy_ready=False sector_rank=13 price=1.11 support=0.91 resistance=1.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=51.06 liquidity=4497948.0 spike=0.58
- ASCM.CA: score=11.82 buy_ready=False sector_rank=13 price=46.19 support=38.2 resistance=58.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=50.13 liquidity=3682493.0 spike=0.44
- ASPI.CA: score=20.14 buy_ready=False sector_rank=13 price=0.32 support=0.27 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=51.66 liquidity=37243104.0 spike=2.0
- ATLC.CA: score=11.45 buy_ready=False sector_rank=18 price=5.0 support=3.93 resistance=6.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=53.17 liquidity=5459637.5 spike=0.69
- ATQA.CA: score=17.09 buy_ready=False sector_rank=12 price=9.95 support=8.25 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.93 liquidity=67904192.0 spike=1.47
- AXPH.CA: score=12.39 buy_ready=False sector_rank=13 price=1329.7 support=1135.0 resistance=1520.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:12 PM market time freshness=DELAYED_CURRENT RSI=50.75 liquidity=3253934.25 spike=0.68
- BINV.CA: score=0.99 buy_ready=False sector_rank=17 price=52.98 support=50.62 resistance=62.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=31.39 liquidity=1954478.25 spike=0.19
- BIOC.CA: score=10.14 buy_ready=False sector_rank=13 price=370.05 support=308.01 resistance=379.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=311910464.0 spike=3.73
- BTFH.CA: score=15.69 buy_ready=False sector_rank=18 price=2.4 support=2.05 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=39.82 liquidity=157380656.0 spike=1.35
- CAED.CA: score=20.2 buy_ready=False sector_rank=13 price=98.36 support=64.0 resistance=118.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=51.63 liquidity=23401420.0 spike=1.53
- CANA.CA: score=22.71 buy_ready=False sector_rank=9 price=47.12 support=38.1 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=61.54 liquidity=19933224.0 spike=1.02
- CCAP.CA: score=14.03 buy_ready=False sector_rank=17 price=5.8 support=5.55 resistance=6.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.86 liquidity=148310320.0 spike=0.34
- CCRS.CA: score=22.24 buy_ready=False sector_rank=13 price=2.11 support=1.3 resistance=2.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=56.83 liquidity=22537156.0 spike=2.55
- CEFM.CA: score=10.89 buy_ready=False sector_rank=13 price=119.06 support=97.79 resistance=131.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=49.94 liquidity=1745771.88 spike=0.8
- CERA.CA: score=14.14 buy_ready=False sector_rank=13 price=1.09 support=0.93 resistance=1.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=36.73 liquidity=71508496.0 spike=0.83
- CFGH.CA: score=4.23 buy_ready=False sector_rank=13 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=5 November 02:13 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=87222.18 spike=14.31
- CICH.CA: score=6.34 buy_ready=False sector_rank=18 price=10.69 support=9.63 resistance=12.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:12 PM market time freshness=DELAYED_CURRENT RSI=54.74 liquidity=1353656.25 spike=0.58
- CIEB.CA: score=17.95 buy_ready=False sector_rank=9 price=22.49 support=21.35 resistance=24.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=58.72 liquidity=13402753.0 spike=1.64
- CIRA.CA: score=20.4 buy_ready=False sector_rank=4 price=37.07 support=32.01 resistance=39.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=58.11 liquidity=10106021.0 spike=0.78
- CLHO.CA: score=18.06 buy_ready=False sector_rank=14 price=13.8 support=12.51 resistance=15.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=43.94 liquidity=19755792.0 spike=0.52
- CNFN.CA: score=10.79 buy_ready=False sector_rank=18 price=3.95 support=3.25 resistance=4.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=53.14 liquidity=3797495.0 spike=0.44
- COMI.CA: score=18.67 buy_ready=False sector_rank=9 price=127.4 support=117.41 resistance=129.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=54.8 liquidity=165041040.0 spike=0.31
- COPR.CA: score=18.56 buy_ready=False sector_rank=13 price=0.42 support=0.33 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=45.79 liquidity=25276518.0 spike=1.71
- COSG.CA: score=15.76 buy_ready=False sector_rank=13 price=1.34 support=1.11 resistance=1.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=48.44 liquidity=7623102.5 spike=0.8
- CPCI.CA: score=12.34 buy_ready=False sector_rank=13 price=598.9 support=502.25 resistance=620.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=54.45 liquidity=2203403.0 spike=0.46
- CSAG.CA: score=20.39 buy_ready=False sector_rank=7 price=35.12 support=30.1 resistance=37.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=51.97 liquidity=9817597.0 spike=1.41
- DAPH.CA: score=18.14 buy_ready=False sector_rank=13 price=86.23 support=65.2 resistance=109.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=16918378.0 spike=0.69
- DEIN.CA: score=8.14 buy_ready=False sector_rank=13 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=29 October 12:10 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=62.1 spike=0.02
- DOMT.CA: score=13.96 buy_ready=False sector_rank=5 price=23.97 support=20.27 resistance=24.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=53.03 liquidity=3377839.0 spike=1.68
- DSCW.CA: score=20.08 buy_ready=False sector_rank=13 price=1.54 support=1.23 resistance=1.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=50.75 liquidity=25463094.0 spike=1.97
- DTPP.CA: score=11.14 buy_ready=False sector_rank=13 price=48.1 support=36.0 resistance=302.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=33.54 liquidity=14763022.0 spike=0.46
- EALR.CA: score=19.94 buy_ready=False sector_rank=13 price=300.93 support=236.01 resistance=347.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=50.84 liquidity=10340840.0 spike=1.9
- EASB.CA: score=13.92 buy_ready=False sector_rank=13 price=6.55 support=5.03 resistance=8.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=53.74 liquidity=4776314.5 spike=0.78
- EAST.CA: score=19.97 buy_ready=False sector_rank=5 price=32.66 support=27.01 resistance=33.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=72.56 liquidity=7744504.0 spike=0.2
- EBSC.CA: score=9.75 buy_ready=False sector_rank=13 price=1.53 support=1.2 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:13 PM market time freshness=DELAYED_CURRENT RSI=52.44 liquidity=1612028.25 spike=0.51
- ECAP.CA: score=13.44 buy_ready=False sector_rank=13 price=28.21 support=24.8 resistance=30.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=52.64 liquidity=4055225.25 spike=1.62
- EDFM.CA: score=10.62 buy_ready=False sector_rank=13 price=364.89 support=312.92 resistance=382.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:10 PM market time freshness=DELAYED_CURRENT RSI=49.04 liquidity=1258907.0 spike=1.11
- EEII.CA: score=12.44 buy_ready=False sector_rank=13 price=1.79 support=1.42 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=49.33 liquidity=4299081.0 spike=0.63
- EFIC.CA: score=24.09 buy_ready=False sector_rank=12 price=167.25 support=121.0 resistance=168.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=59.4 liquidity=73609608.0 spike=2.97
- EFID.CA: score=19.22 buy_ready=False sector_rank=5 price=19.49 support=16.01 resistance=19.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=52.47 liquidity=35800112.0 spike=0.98
- EFIH.CA: score=22.76 buy_ready=False sector_rank=11 price=23.45 support=20.3 resistance=25.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.78 liquidity=67348856.0 spike=1.17
- EGAL.CA: score=17.15 buy_ready=False sector_rank=12 price=316.34 support=275.0 resistance=342.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=74.61 liquidity=89970928.0 spike=0.93
- EGAS.CA: score=6.71 buy_ready=False sector_rank=19 price=48.41 support=43.0 resistance=57.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.21 liquidity=2395016.25 spike=0.58
- EGBE.CA: score=5.69 buy_ready=False sector_rank=9 price=0.49 support=0.47 resistance=0.54 source=Yahoo Finance as_of=2026-11-04T22:00:00+00:00 freshness=FRESH RSI=44.9 liquidity=20646.15 spike=0.33
- EGCH.CA: score=16.15 buy_ready=False sector_rank=12 price=10.34 support=9.66 resistance=13.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=43.97 liquidity=34573356.0 spike=0.64
- EGSA.CA: score=19.46 buy_ready=False sector_rank=1 price=9.0 support=8.7 resistance=9.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=45.76 liquidity=56348.0 spike=9.55
- EGTS.CA: score=20.45 buy_ready=False sector_rank=8 price=13.13 support=10.19 resistance=16.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=53.35 liquidity=35101036.0 spike=1.85
- EHDR.CA: score=15.65 buy_ready=False sector_rank=13 price=2.09 support=1.8 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=50.88 liquidity=9447815.0 spike=1.03
- ELEC.CA: score=20.4 buy_ready=False sector_rank=3 price=1.67 support=1.34 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=53.06 liquidity=35252352.0 spike=0.67
- ELKA.CA: score=16.26 buy_ready=False sector_rank=13 price=1.5 support=1.21 resistance=1.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=53.62 liquidity=7115048.0 spike=0.53
- ELNA.CA: score=10.75 buy_ready=False sector_rank=13 price=41.29 support=33.46 resistance=41.59 source=Yahoo Finance as_of=2026-11-04T22:00:00+00:00 freshness=FRESH RSI=75.66 liquidity=926217.3 spike=1.34
- ELSH.CA: score=5.14 buy_ready=False sector_rank=13 price=11.4 support=10.25 resistance=11.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16024318.0 spike=1.0
- ELWA.CA: score=6.02 buy_ready=False sector_rank=13 price=1.33 support=1.3 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=12.12 liquidity=2457268.5 spike=3.21
- EMFD.CA: score=19.75 buy_ready=False sector_rank=8 price=12.17 support=10.6 resistance=12.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=60.08 liquidity=37913492.0 spike=0.68
- ENGC.CA: score=16.81 buy_ready=False sector_rank=13 price=35.86 support=26.91 resistance=37.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=58.51 liquidity=8673807.0 spike=0.94
- EOSB.CA: score=10.2 buy_ready=False sector_rank=13 price=1.61 support=1.55 resistance=1.72 source=Yahoo Finance as_of=2026-11-04T22:00:00+00:00 freshness=FRESH RSI=70.0 liquidity=55355.02 spike=0.64
- EPCO.CA: score=19.06 buy_ready=False sector_rank=13 price=8.93 support=7.0 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=54.81 liquidity=9223996.0 spike=1.85
- EPPK.CA: score=-4.44 buy_ready=False sector_rank=13 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=19.4 buy_ready=False sector_rank=1 price=129.51 support=115.0 resistance=148.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=40.31 liquidity=84176984.0 spike=0.35
- ETRS.CA: score=17.85 buy_ready=False sector_rank=13 price=10.88 support=9.51 resistance=11.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=63.84 liquidity=3706426.5 spike=0.26
- EXPA.CA: score=19.17 buy_ready=False sector_rank=9 price=14.51 support=12.0 resistance=15.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=50.99 liquidity=31263850.0 spike=1.25
- FAIT.CA: score=10.2 buy_ready=False sector_rank=9 price=44.36 support=40.0 resistance=46.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:08 PM market time freshness=DELAYED_CURRENT RSI=55.84 liquidity=531903.0 spike=0.2
- FAITA.CA: score=7.19 buy_ready=False sector_rank=9 price=0.98 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=51.72 liquidity=40396.01 spike=1.24
- FERC.CA: score=23.15 buy_ready=False sector_rank=12 price=69.47 support=53.57 resistance=77.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=57.55 liquidity=29420378.0 spike=4.83
- FWRY.CA: score=14.42 buy_ready=False sector_rank=11 price=17.21 support=15.27 resistance=19.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=40.88 liquidity=37202252.0 spike=0.35
- GBCO.CA: score=6.86 buy_ready=False sector_rank=21 price=22.9 support=20.9 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=20.52 liquidity=111496144.0 spike=1.03
- GDWA.CA: score=13.4 buy_ready=False sector_rank=13 price=0.56 support=0.46 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=50.41 liquidity=7255636.0 spike=0.58
- GGCC.CA: score=16.14 buy_ready=False sector_rank=13 price=0.56 support=0.49 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.73 liquidity=16857300.0 spike=0.85
- GIHD.CA: score=18.14 buy_ready=False sector_rank=13 price=47.63 support=32.1 resistance=63.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=47.29 liquidity=11906642.0 spike=0.78
- GMCI.CA: score=-0.32 buy_ready=False sector_rank=13 price=1.48 support=1.34 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:10 PM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=338199.84 spike=1.1
- GRCA.CA: score=18.78 buy_ready=False sector_rank=13 price=32.32 support=22.57 resistance=37.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=55.99 liquidity=11533553.0 spike=1.32
- GSSC.CA: score=12.89 buy_ready=False sector_rank=13 price=259.29 support=211.52 resistance=287.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:13 PM market time freshness=DELAYED_CURRENT RSI=45.64 liquidity=1865158.75 spike=1.94
- GTWL.CA: score=19.14 buy_ready=False sector_rank=13 price=119.7 support=73.02 resistance=159.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=52.83 liquidity=96892360.0 spike=0.48
- HDBK.CA: score=19.23 buy_ready=False sector_rank=9 price=99.48 support=83.01 resistance=108.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=53.73 liquidity=29575740.0 spike=1.28
- HELI.CA: score=19.75 buy_ready=False sector_rank=8 price=6.89 support=5.72 resistance=7.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=49397740.0 spike=0.66
- HRHO.CA: score=12.99 buy_ready=False sector_rank=18 price=23.6 support=21.87 resistance=26.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=47.66 liquidity=26567886.0 spike=0.51
- ICID.CA: score=1.28 buy_ready=False sector_rank=13 price=16.83 support=16.8 resistance=17.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5883197.5 spike=1.13
- IDRE.CA: score=14.56 buy_ready=False sector_rank=13 price=40.48 support=29.11 resistance=50.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=49.45 liquidity=6241978.0 spike=1.09
- IFAP.CA: score=20.68 buy_ready=False sector_rank=10 price=17.84 support=15.12 resistance=19.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=51.03 liquidity=13857049.0 spike=2.11
- INFI.CA: score=20.14 buy_ready=False sector_rank=13 price=123.04 support=93.44 resistance=138.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.79 liquidity=29516450.0 spike=1.5
- IRON.CA: score=8.2 buy_ready=False sector_rank=12 price=24.25 support=23.13 resistance=29.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=44.19 liquidity=4050506.0 spike=0.42
- ISMA.CA: score=16.32 buy_ready=False sector_rank=13 price=20.56 support=14.11 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=51.76 liquidity=8175046.5 spike=0.96
- ISMQ.CA: score=16.25 buy_ready=False sector_rank=12 price=7.39 support=5.96 resistance=8.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=53.87 liquidity=8106932.5 spike=0.56
- ISPH.CA: score=18.06 buy_ready=False sector_rank=14 price=10.36 support=9.02 resistance=11.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=46.45 liquidity=40451828.0 spike=0.71
- JUFO.CA: score=19.22 buy_ready=False sector_rank=5 price=23.69 support=21.01 resistance=25.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=52.7 liquidity=19285624.0 spike=0.9
- KABO.CA: score=15.42 buy_ready=False sector_rank=16 price=7.05 support=5.58 resistance=9.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=51.32 liquidity=10842244.0 spike=0.51
- KWIN.CA: score=8.54 buy_ready=False sector_rank=13 price=73.74 support=66.5 resistance=76.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20989550.0 spike=2.7
- KZPC.CA: score=28.86 buy_ready=False sector_rank=13 price=14.03 support=11.56 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=56.52 liquidity=25678832.0 spike=3.36
- LCSW.CA: score=8.31 buy_ready=False sector_rank=6 price=39.14 support=35.57 resistance=39.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46792964.0 spike=2.26
- LUTS.CA: score=19.78 buy_ready=False sector_rank=13 price=0.76 support=0.47 resistance=0.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=57.94 liquidity=78884048.0 spike=1.32
- MAAL.CA: score=12.67 buy_ready=False sector_rank=13 price=6.88 support=4.88 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=44.8 liquidity=5527752.5 spike=0.51
- MASR.CA: score=17.14 buy_ready=False sector_rank=13 price=6.73 support=5.6 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=46.72 liquidity=25125874.0 spike=0.55
- MBSC.CA: score=17.79 buy_ready=False sector_rank=6 price=319.97 support=262.0 resistance=401.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=45.75 liquidity=28013882.0 spike=0.41
- MCQE.CA: score=18.79 buy_ready=False sector_rank=6 price=171.54 support=144.0 resistance=203.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=55.63 liquidity=36629180.0 spike=0.66
- MCRO.CA: score=18.78 buy_ready=False sector_rank=13 price=1.32 support=1.07 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=53.85 liquidity=52629636.0 spike=1.32
- MENA.CA: score=10.65 buy_ready=False sector_rank=8 price=5.88 support=5.45 resistance=6.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=59.06 liquidity=1906236.38 spike=0.45
- MEPA.CA: score=16.14 buy_ready=False sector_rank=13 price=1.35 support=1.14 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.24 liquidity=13348085.0 spike=0.86
- MFPC.CA: score=10.01 buy_ready=False sector_rank=12 price=38.63 support=38.42 resistance=40.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=199628672.0 spike=3.43
- MFSC.CA: score=15.11 buy_ready=False sector_rank=13 price=36.08 support=28.55 resistance=44.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=44.56 liquidity=4452298.5 spike=2.26
- MHOT.CA: score=25.68 buy_ready=False sector_rank=2 price=15.93 support=13.0 resistance=16.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=50.14 liquidity=18698930.0 spike=3.14
- MICH.CA: score=24.14 buy_ready=False sector_rank=13 price=42.21 support=35.5 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=58.72 liquidity=24166794.0 spike=4.27
- MILS.CA: score=16.93 buy_ready=False sector_rank=13 price=140.4 support=94.24 resistance=182.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=47.55 liquidity=7785785.0 spike=0.95
- MIPH.CA: score=9.65 buy_ready=False sector_rank=14 price=776.93 support=610.0 resistance=826.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:05 PM market time freshness=DELAYED_CURRENT RSI=59.83 liquidity=591917.75 spike=0.18
- MOED.CA: score=17.3 buy_ready=False sector_rank=13 price=0.5 support=0.39 resistance=0.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=38.14 liquidity=20719670.0 spike=1.58
- MOIL.CA: score=3.33 buy_ready=False sector_rank=19 price=0.64 support=0.6 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.17 liquidity=9669.19 spike=0.06
- MOIN.CA: score=10.4 buy_ready=False sector_rank=13 price=28.97 support=25.7 resistance=36.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=51.7 liquidity=3255562.25 spike=0.51
- MOSC.CA: score=24.14 buy_ready=False sector_rank=13 price=271.46 support=198.01 resistance=286.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=55.77 liquidity=16188783.0 spike=4.52
- MPCI.CA: score=20.02 buy_ready=False sector_rank=13 price=325.96 support=238.6 resistance=350.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=145902896.0 spike=1.44
- MPCO.CA: score=17.46 buy_ready=False sector_rank=10 price=1.9 support=1.55 resistance=2.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=51.43 liquidity=52591124.0 spike=0.65
- MPRC.CA: score=10.14 buy_ready=False sector_rank=13 price=39.1 support=33.51 resistance=39.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=109644680.0 spike=7.36
- MTIE.CA: score=13.8 buy_ready=False sector_rank=21 price=7.06 support=6.05 resistance=8.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=46.4 liquidity=12882911.0 spike=0.64
- NAHO.CA: score=5.15 buy_ready=False sector_rank=13 price=0.12 support=0.12 resistance=0.13 source=Yahoo Finance as_of=2026-11-04T22:00:00+00:00 freshness=FRESH RSI=35.29 liquidity=13022.12 spike=0.75
- NCCW.CA: score=13.6 buy_ready=False sector_rank=13 price=5.41 support=4.05 resistance=7.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=50.76 liquidity=7460815.0 spike=0.44
- NEDA.CA: score=0.7 buy_ready=False sector_rank=13 price=2.36 support=2.26 resistance=2.66 source=Yahoo Finance as_of=2026-11-04T22:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=281873.67 spike=1.64
- NHPS.CA: score=12.34 buy_ready=False sector_rank=13 price=61.52 support=50.0 resistance=73.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=50.74 liquidity=4198889.5 spike=0.6
- NINH.CA: score=14.88 buy_ready=False sector_rank=13 price=16.09 support=12.36 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=53.43 liquidity=6743526.0 spike=0.75
- NIPH.CA: score=19.56 buy_ready=False sector_rank=14 price=286.96 support=205.0 resistance=318.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=56.98 liquidity=164818032.0 spike=1.25
- OBRI.CA: score=11.26 buy_ready=False sector_rank=13 price=24.03 support=18.11 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=46.85 liquidity=5119702.5 spike=0.45
- OCDI.CA: score=19.81 buy_ready=False sector_rank=8 price=24.77 support=21.0 resistance=27.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=53.69 liquidity=33199168.0 spike=1.03
- OCPH.CA: score=12.07 buy_ready=False sector_rank=13 price=189.92 support=147.96 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=47.57 liquidity=3768863.5 spike=1.08
- ODIN.CA: score=16.52 buy_ready=False sector_rank=13 price=2.13 support=1.7 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=51.69 liquidity=8063327.0 spike=1.16
- OFH.CA: score=19.92 buy_ready=False sector_rank=13 price=0.76 support=0.61 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=51.75 liquidity=29422310.0 spike=1.39
- OIH.CA: score=18.03 buy_ready=False sector_rank=17 price=1.78 support=1.5 resistance=1.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=29201674.0 spike=0.64
- OLFI.CA: score=19.17 buy_ready=False sector_rank=5 price=20.19 support=17.86 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=41.73 liquidity=9624695.0 spike=1.16
- ORAS.CA: score=4.6 buy_ready=False sector_rank=15 price=801.05 support=800.01 resistance=818.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=104020584.0 spike=1.0
- ORHD.CA: score=18.75 buy_ready=False sector_rank=8 price=10.52 support=8.5 resistance=12.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=53.54 liquidity=73850704.0 spike=0.62
- ORWE.CA: score=16.42 buy_ready=False sector_rank=16 price=24.93 support=22.2 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=42.62 liquidity=17993538.0 spike=0.51
- PHAR.CA: score=19.06 buy_ready=False sector_rank=14 price=103.72 support=90.2 resistance=115.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=51.42 liquidity=43631504.0 spike=0.81
- PHDC.CA: score=20.37 buy_ready=False sector_rank=8 price=12.01 support=10.33 resistance=13.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=43.29 liquidity=295954944.0 spike=2.81
- PHTV.CA: score=9.04 buy_ready=False sector_rank=13 price=322.0 support=300.0 resistance=345.67 source=Yahoo Finance as_of=2026-11-04T22:00:00+00:00 freshness=FRESH RSI=40.34 liquidity=1637048.0 spike=1.13
- POUL.CA: score=20.8 buy_ready=False sector_rank=5 price=10.0 support=8.81 resistance=10.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=55.19 liquidity=138456848.0 spike=1.79
- PRCL.CA: score=19.41 buy_ready=False sector_rank=6 price=22.04 support=16.65 resistance=26.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=56.77 liquidity=20259078.0 spike=1.31
- PRDC.CA: score=19.75 buy_ready=False sector_rank=8 price=6.4 support=5.08 resistance=7.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=58.66 liquidity=10885379.0 spike=0.53
- PRMH.CA: score=23.02 buy_ready=False sector_rank=13 price=2.0 support=1.7 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=54.95 liquidity=10905433.0 spike=3.44
- RACC.CA: score=11.03 buy_ready=False sector_rank=13 price=7.96 support=6.1 resistance=9.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:09 PM market time freshness=DELAYED_CURRENT RSI=48.45 liquidity=4893726.5 spike=0.79
- RAKT.CA: score=4.26 buy_ready=False sector_rank=13 price=22.35 support=20.4 resistance=23.99 source=Yahoo Finance as_of=2026-11-04T22:00:00+00:00 freshness=FRESH RSI=53.99 liquidity=115817.7 spike=0.39
- RAYA.CA: score=14.21 buy_ready=False sector_rank=20 price=5.55 support=5.02 resistance=6.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=47.66 liquidity=14088265.0 spike=0.7
- RMDA.CA: score=23.7 buy_ready=False sector_rank=14 price=5.55 support=4.5 resistance=5.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=63.35 liquidity=62126492.0 spike=2.32
- ROTO.CA: score=21.52 buy_ready=False sector_rank=13 price=34.0 support=25.0 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=41.61 liquidity=23521272.0 spike=2.69
- RREI.CA: score=17.42 buy_ready=False sector_rank=13 price=2.89 support=1.96 resistance=3.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=38.35 liquidity=17004590.0 spike=1.64
- RTVC.CA: score=0.19 buy_ready=False sector_rank=13 price=2.82 support=2.66 resistance=3.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=26.26 liquidity=1053445.75 spike=0.41
- RUBX.CA: score=15.14 buy_ready=False sector_rank=13 price=13.09 support=10.51 resistance=18.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=39.02 liquidity=19340846.0 spike=0.28
- SAUD.CA: score=9.21 buy_ready=False sector_rank=9 price=21.79 support=20.4 resistance=21.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31348684.0 spike=2.77
- SCEM.CA: score=27.23 buy_ready=False sector_rank=6 price=94.43 support=73.9 resistance=95.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=63.84 liquidity=114447872.0 spike=2.22
- SCFM.CA: score=10.23 buy_ready=False sector_rank=13 price=218.62 support=153.02 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=46.77 liquidity=2088498.75 spike=0.94
- SCTS.CA: score=16.6 buy_ready=False sector_rank=4 price=521.6 support=410.0 resistance=555.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=57.48 liquidity=5960461.5 spike=1.12
- SDTI.CA: score=22.46 buy_ready=False sector_rank=13 price=86.81 support=75.01 resistance=90.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=62.15 liquidity=20502642.0 spike=1.16
- SEIG.CA: score=19.42 buy_ready=False sector_rank=13 price=232.0 support=142.0 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=59.81 liquidity=7279585.5 spike=0.86
- SIPC.CA: score=7.28 buy_ready=False sector_rank=13 price=5.51 support=4.85 resistance=5.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=98995992.0 spike=2.07
- SKPC.CA: score=16.15 buy_ready=False sector_rank=12 price=14.91 support=14.01 resistance=16.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=52.28 liquidity=17158962.0 spike=0.35
- SMFR.CA: score=25.14 buy_ready=False sector_rank=13 price=232.15 support=165.0 resistance=238.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=65.23 liquidity=55294844.0 spike=18.04
- SNFC.CA: score=20.78 buy_ready=False sector_rank=13 price=11.16 support=10.08 resistance=11.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=49.8 liquidity=10545838.0 spike=1.32
- SPIN.CA: score=6.64 buy_ready=False sector_rank=16 price=14.34 support=12.0 resistance=16.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:12 PM market time freshness=DELAYED_CURRENT RSI=52.97 liquidity=1223055.25 spike=0.23
- SPMD.CA: score=16.14 buy_ready=False sector_rank=13 price=0.35 support=0.3 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=52.15 liquidity=10507074.0 spike=0.61
- SUGR.CA: score=19.16 buy_ready=False sector_rank=5 price=47.41 support=44.62 resistance=54.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=39.54 liquidity=24351886.0 spike=2.47
- SVCE.CA: score=21.02 buy_ready=False sector_rank=13 price=9.12 support=7.01 resistance=10.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=49.77 liquidity=89579848.0 spike=1.94
- SWDY.CA: score=24.5 buy_ready=False sector_rank=3 price=117.98 support=97.0 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=64.0 liquidity=81141688.0 spike=1.55
- TALM.CA: score=22.12 buy_ready=False sector_rank=4 price=20.21 support=17.0 resistance=22.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=53.3 liquidity=8723515.0 spike=0.39
- TMGH.CA: score=18.75 buy_ready=False sector_rank=8 price=83.0 support=76.5 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=51.64 liquidity=194132080.0 spike=0.72
- TRTO.CA: score=-4.21 buy_ready=False sector_rank=13 price=0.06 support=0.06 resistance=0.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6191.05 spike=1.32
- UEFM.CA: score=9.14 buy_ready=False sector_rank=13 price=486.09 support=422.0 resistance=520.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=51.51 liquidity=1004929.31 spike=0.54
- UEGC.CA: score=18.14 buy_ready=False sector_rank=13 price=1.48 support=1.21 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=46.75 liquidity=18772046.0 spike=0.4
- UNIP.CA: score=12.04 buy_ready=False sector_rank=13 price=0.3 support=0.25 resistance=0.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=48.31 liquidity=5896802.5 spike=0.81
- UNIT.CA: score=15.5 buy_ready=False sector_rank=8 price=17.99 support=15.06 resistance=18.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=69.35 liquidity=2376558.5 spike=1.19
- WCDF.CA: score=11.34 buy_ready=False sector_rank=13 price=517.72 support=432.5 resistance=623.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:09 PM market time freshness=DELAYED_CURRENT RSI=50.91 liquidity=2403610.25 spike=1.4
- WKOL.CA: score=9.36 buy_ready=False sector_rank=13 price=176.42 support=145.33 resistance=309.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=28.45 liquidity=12266471.0 spike=1.11
- ZEOT.CA: score=20.14 buy_ready=False sector_rank=13 price=11.51 support=7.9 resistance=12.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=59.72 liquidity=12332030.0 spike=1.5
- ZMID.CA: score=20.27 buy_ready=False sector_rank=8 price=7.02 support=5.91 resistance=7.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=53.98 liquidity=90877976.0 spike=1.26

## Backtesting Lite
- KZPC.CA: 180d return=33.07%, max drawdown=-27.57%, MA20>MA50 days last20=9, as_of=2026-11-04T22:00:00+00:00
- SCEM.CA: 180d return=49.5%, max drawdown=-29.64%, MA20>MA50 days last20=0, as_of=2026-11-04T22:00:00+00:00
- MHOT.CA: 180d return=-30.92%, max drawdown=-59.1%, MA20>MA50 days last20=0, as_of=2026-11-04T22:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- KZPC.CA: status=OLD_ACCEPTED latest=2024-01-01 age_days=1042 sources=3 expected=Kafr El Zayat For Pesticides & Chemicals Co.(S.A.E) summary=Kafr El Zayat to set up fund with EGP 5m capital; Kafr El Zayat Pesticides targets EGP 1.73bn sales in 2024; Kafr El Zayat Pesticides’ EGM approves stock split, capital hike
  - Kafr El Zayat to set up fund with EGP 5m capital: https://english.mubasher.info/news/4201137/Kafr-El-Zayat-to-set-up-fund-with-EGP-5m-capital/
  - Kafr El Zayat Pesticides targets EGP 1.73bn sales in 2024: https://english.mubasher.info/news/4200526/Kafr-El-Zayat-Pesticides-targets-EGP-1-73bn-sales-in-2024/
  - Kafr El Zayat Pesticides’ EGM approves stock split, capital hike: https://english.mubasher.info/news/4052937/Kafr-El-Zayat-Pesticides-EGM-approves-stock-split-capital-hike/
- SCEM.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=676 sources=3 expected=Sinai Cement summary=Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn; Upward trend line ends several-day decline for Sinai Cement stock; Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25
  - Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn: https://english.mubasher.info/news/4564824/Sinai-Cement-s-consolidated-profits-fall-in-2025-net-sales-cross-EGP-9bn/
  - Upward trend line ends several-day decline for Sinai Cement stock: https://english.mubasher.info/news/4529647/Upward-trend-line-ends-several-day-decline-for-Sinai-Cement-stock/
  - Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25: https://english.mubasher.info/news/4526073/Sinai-Cement-reports-lower-consolidated-net-profits-at-EGP-1-5bn-in-9M-25/
- MHOT.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Hotels summary=Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26; Shareholder buys EGP 3.39m worth of shares in Misr Hotels; Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits
  - Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26: https://english.mubasher.info/news/4602482/Misr-Hotels-net-profits-cross-EGP-1-1bn-in-9M-25-26/
  - Shareholder buys EGP 3.39m worth of shares in Misr Hotels: https://english.mubasher.info/news/4013808/Shareholder-buys-EGP-3-39m-worth-of-shares-in-Misr-Hotels/
  - Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits: https://english.mubasher.info/news/3975543/Misr-Hotels-repays-EGP-383m-of-NBE-s-loan-unveils-estimated-profits/
- SMFR.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Samad Misr EGYFERT.S.A.E summary=Evidence rejected for SMFR.CA: source text did not clearly match SMFR.CA / Samad Misr EGYFERT.S.A.E.
- SWDY.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Elsewedy Electric summary=Elsewedy-Sinohydro JV signs contract for Rabigh 2 IPP expansion project; Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26; Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations
  - Elsewedy-Sinohydro JV signs contract for Rabigh 2 IPP expansion project: https://english.mubasher.info/news/4684693/Elsewedy-Sinohydro-JV-signs-contract-for-Rabigh-2-IPP-expansion-project/
  - Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26: https://english.mubasher.info/news/4614341/Elsewedy-Electric-s-consolidated-revenues-total-EGP-75-2bn-in-Q1-26/
  - Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations: https://english.mubasher.info/news/4593166/Elsewedy-Electric-accelerates-power-transformation-project-in-KSA-with-6-high-voltage-substations/
- MICH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Chemical Industries Co. summary=Misr Chemical Industries’ net profits decline to EGP 397m in 9M-25/26; Surpassing Misr Chemical stock’s current levels would lead to historical levels – Analysis; Misr Chemical Industries posts 10% decrease in H1-25/26 net profits
  - Misr Chemical Industries’ net profits decline to EGP 397m in 9M-25/26: https://english.mubasher.info/news/4597505/Misr-Chemical-Industries-net-profits-decline-to-EGP-397m-in-9M-25-26/
  - Surpassing Misr Chemical stock’s current levels would lead to historical levels – Analysis: https://english.mubasher.info/news/4586207/Surpassing-Misr-Chemical-stock-s-current-levels-would-lead-to-historical-levels-Analysis/
  - Misr Chemical Industries posts 10% decrease in H1-25/26 net profits: https://english.mubasher.info/news/4554378/Misr-Chemical-Industries-posts-10-decrease-in-H1-25-26-net-profits/
- MOSC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Oils & Soap summary=Misr Oils and Soap not to pay dividends for FY20/21; Misr Oils and Soap&#39;s profit plunges 78% in FY20/21; Misr Oils and Soap swings to loss in 10 months
  - Misr Oils and Soap not to pay dividends for FY20/21: https://english.mubasher.info/news/3856493/Misr-Oils-and-Soap-not-to-pay-dividends-for-FY20-21/
  - Misr Oils and Soap&#39;s profit plunges 78% in FY20/21: https://english.mubasher.info/news/3851183/Misr-Oils-and-Soap-s-profit-plunges-78-in-FY20-21/
  - Misr Oils and Soap swings to loss in 10 months: https://english.mubasher.info/news/3811105/Misr-Oils-and-Soap-swings-to-loss-in-10-months/
- EFIC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=676 sources=3 expected=Egyptian Financial and Industrial summary=EFIC’s consolidated profits near EGP 820m in 2025; dividends proposed; EFIC ordered to pay over EGP 126m as penalties; EFIC generates lower consolidated net profits at EGP 803m in 9M-25; net sales near EGP 8bn
  - EFIC’s consolidated profits near EGP 820m in 2025; dividends proposed: https://english.mubasher.info/news/4579891/EFIC-s-consolidated-profits-near-EGP-820m-in-2025-dividends-proposed/
  - EFIC ordered to pay over EGP 126m as penalties: https://english.mubasher.info/news/4535935/EFIC-ordered-to-pay-over-EGP-126m-as-penalties/
  - EFIC generates lower consolidated net profits at EGP 803m in 9M-25; net sales near EGP 8bn: https://english.mubasher.info/news/4528902/EFIC-generates-lower-consolidated-net-profits-at-EGP-803m-in-9M-25-net-sales-near-EGP-8bn/

## Warnings
- OpenRouter API error: 404
- Evidence for KZPC.CA matches the company but appears old; latest detected date is 2024-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for SCEM.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for MHOT.CA matches the company but no source/report date was detected.
- Evidence rejected for SMFR.CA: source text did not clearly match SMFR.CA / Samad Misr EGYFERT.S.A.E.
- Evidence for SWDY.CA matches the company but no source/report date was detected.
- Evidence for MICH.CA matches the company but no source/report date was detected.
- Evidence for MOSC.CA matches the company but no source/report date was detected.
- Evidence for EFIC.CA matches the company but appears old; latest detected date is 2025-01-01.
