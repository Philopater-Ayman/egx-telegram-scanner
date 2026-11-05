# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-11-05T20:12:14.191768+00:00
Generated Cairo: 2026-11-05 22:12
Run timing: target 15:30 Cairo | generated Cairo 2026-11-05 22:12 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-11-05 22:08

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 164/186
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, November 05
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 73.68% / above MA50 10.53%
- EGX70 regime: BEARISH / above MA20 57.89% / above MA50 10.53%
- Sector breadth: 9.52%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=523990848.0 spike=0.99 score=18.63
- CCAP.CA: liquidity=428386816.0 spike=0.99 score=13.91
- TMGH.CA: liquidity=363178912.0 spike=1.41 score=17.54
- AMES.CA: liquidity=356522304.0 spike=7.6 score=10.15
- PHDC.CA: liquidity=265130608.0 spike=2.77 score=9.26

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- FERC.CA: spike=15.12 liquidity=52655980.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ELWA.CA: spike=12.69 liquidity=10070649.23 outlook=WEAK_OR_RISKY score=25.88 buy_ready=False
- EFIC.CA: spike=8.95 liquidity=155623696.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- IFAP.CA: spike=8.55 liquidity=41245884.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SMFR.CA: spike=7.61 liquidity=17380720.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Tourism & Leisure: score=8.91 5d=14.54% 20d=-1.17% aboveMA50=0.0%
- #2 Transportation & Logistics: score=6.61 5d=4.72% 20d=-7.07% aboveMA50=50.0%
- #3 Agriculture & Food Production: score=5.76 5d=1.69% 20d=-11.66% aboveMA50=0.0%
- #4 Healthcare: score=5.15 5d=5.14% 20d=-11.14% aboveMA50=16.67%
- #5 Fintech & Payments: score=5.07 5d=4.11% 20d=-6.53% aboveMA50=50.0%
- #6 Building Materials: score=5.06 5d=5.41% 20d=-9.77% aboveMA50=33.33%
- #7 Industrial Goods & Cables: score=5.01 5d=3.61% 20d=-9.98% aboveMA50=0.0%
- #8 Food, Beverages & Tobacco: score=4.98 5d=4.37% 20d=-4.2% aboveMA50=14.29%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ALCN.CA: BULLISH_WATCH score=87.61 liquidity=TRADEABLE sector=LEADING risk=far above support
- ETRS.CA: BULLISH_WATCH score=78.88 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- SDTI.CA: BULLISH_WATCH score=74.88 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- ICID.CA: BULLISH_WATCH score=74.88 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- SCEM.CA: BULLISH_WATCH score=72.06 liquidity=TRADEABLE sector=IMPROVING risk=far above support; close to resistance
- EFIH.CA: BULLISH_WATCH score=70.07 liquidity=TRADEABLE sector=IMPROVING risk=far above support
- LCSW.CA: BULLISH_WATCH score=70.06 liquidity=TRADEABLE sector=IMPROVING risk=far above support
- CSAG.CA: CONSTRUCTIVE score=69.61 liquidity=TRADEABLE sector=LEADING risk=below MA50
- RMDA.CA: CONSTRUCTIVE score=68.15 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA50; far above support
- CANA.CA: CONSTRUCTIVE score=64.07 liquidity=TRADEABLE sector=IMPROVING risk=far above support; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=7.37 buy_ready=False sector_rank=12 price=238.02 support=236.13 resistance=251.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31770796.0 spike=2.11
- ABUK.CA: score=14.33 buy_ready=False sector_rank=16 price=80.76 support=77.25 resistance=95.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=40.98 liquidity=76486008.0 spike=0.8
- ACAMD.CA: score=19.37 buy_ready=False sector_rank=12 price=2.02 support=1.86 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=40.35 liquidity=79872280.0 spike=1.61
- ACGC.CA: score=19.8 buy_ready=False sector_rank=13 price=13.43 support=11.6 resistance=14.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=44.16 liquidity=10095008.0 spike=1.43
- ADCI.CA: score=12.46 buy_ready=False sector_rank=12 price=260.46 support=221.0 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:08 PM market time freshness=DELAYED_CURRENT RSI=47.97 liquidity=2549908.25 spike=1.38
- ADIB.CA: score=23.03 buy_ready=False sector_rank=11 price=49.2 support=43.16 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=57.02 liquidity=137413056.0 spike=1.7
- ADPC.CA: score=13.16 buy_ready=False sector_rank=12 price=3.1 support=2.53 resistance=3.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=43.66 liquidity=5005374.0 spike=0.57
- AFDI.CA: score=6.08 buy_ready=False sector_rank=12 price=45.43 support=34.8 resistance=54.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=34.83 liquidity=3567690.5 spike=1.18
- AFMC.CA: score=19.47 buy_ready=False sector_rank=12 price=138.46 support=94.6 resistance=156.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=52.08 liquidity=19967722.0 spike=1.16
- AJWA.CA: score=20.15 buy_ready=False sector_rank=12 price=223.21 support=190.2 resistance=229.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=45.27 liquidity=14280049.0 spike=0.46
- ALCN.CA: score=23.4 buy_ready=False sector_rank=2 price=33.0 support=27.11 resistance=34.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=42.61 liquidity=11636842.0 spike=0.95
- ALUM.CA: score=15.35 buy_ready=False sector_rank=12 price=20.33 support=16.02 resistance=23.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=42.75 liquidity=5553016.0 spike=1.82
- AMER.CA: score=21.38 buy_ready=False sector_rank=10 price=4.52 support=3.21 resistance=5.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.45 liquidity=98206024.0 spike=1.83
- AMES.CA: score=10.15 buy_ready=False sector_rank=12 price=38.25 support=33.9 resistance=39.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=356522304.0 spike=7.6
- AMIA.CA: score=23.03 buy_ready=False sector_rank=12 price=18.15 support=14.0 resistance=19.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=43.18 liquidity=33306164.0 spike=2.94
- AMOC.CA: score=13.98 buy_ready=False sector_rank=18 price=13.3 support=12.55 resistance=15.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.37 liquidity=147285248.0 spike=0.98
- APSW.CA: score=0.01 buy_ready=False sector_rank=12 price=7.58 support=7.1 resistance=8.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:52 PM market time freshness=DELAYED_CURRENT RSI=31.9 liquidity=537433.44 spike=1.16
- ARAB.CA: score=15.72 buy_ready=False sector_rank=10 price=0.25 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=39.86 liquidity=105263648.0 spike=1.0
- ARCC.CA: score=20.02 buy_ready=False sector_rank=6 price=68.19 support=58.01 resistance=73.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=49.04 liquidity=35136672.0 spike=0.96
- AREH.CA: score=19.91 buy_ready=False sector_rank=12 price=1.12 support=0.91 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=39.22 liquidity=13733552.0 spike=1.88
- ASCM.CA: score=19.09 buy_ready=False sector_rank=12 price=46.65 support=38.2 resistance=58.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.08 liquidity=11596303.0 spike=1.47
- ASPI.CA: score=19.35 buy_ready=False sector_rank=12 price=0.32 support=0.27 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=44.32 liquidity=28735442.0 spike=1.6
- ATLC.CA: score=17.66 buy_ready=False sector_rank=15 price=5.1 support=3.93 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=42.73 liquidity=11775998.0 spike=1.57
- ATQA.CA: score=5.13 buy_ready=False sector_rank=16 price=9.77 support=9.33 resistance=9.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=63815068.0 spike=1.4
- AXPH.CA: score=11.01 buy_ready=False sector_rank=12 price=1335.59 support=1135.0 resistance=1520.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:13 PM market time freshness=DELAYED_CURRENT RSI=45.23 liquidity=3853965.75 spike=0.8
- BINV.CA: score=-0.22 buy_ready=False sector_rank=19 price=53.01 support=50.62 resistance=62.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=27.63 liquidity=873938.81 spike=0.08
- BIOC.CA: score=22.97 buy_ready=False sector_rank=12 price=315.95 support=212.05 resistance=343.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=52.82 liquidity=114086008.0 spike=1.41
- BTFH.CA: score=8.52 buy_ready=False sector_rank=15 price=2.38 support=2.05 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=97186608.0 spike=0.84
- CAED.CA: score=21.89 buy_ready=False sector_rank=12 price=99.53 support=64.0 resistance=122.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.94 liquidity=33186556.0 spike=2.37
- CANA.CA: score=23.41 buy_ready=False sector_rank=11 price=47.3 support=38.1 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=54.36 liquidity=26130528.0 spike=1.39
- CCAP.CA: score=13.91 buy_ready=False sector_rank=19 price=5.89 support=5.55 resistance=6.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.42 liquidity=428386816.0 spike=0.99
- CCRS.CA: score=10.15 buy_ready=False sector_rank=12 price=2.04 support=1.85 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36834856.0 spike=4.94
- CEFM.CA: score=11.18 buy_ready=False sector_rank=12 price=118.66 support=97.79 resistance=134.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=47.75 liquidity=2031737.5 spike=0.91
- CERA.CA: score=9.15 buy_ready=False sector_rank=12 price=1.07 support=0.93 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=28.3 liquidity=61539112.0 spike=0.68
- CFGH.CA: score=-0.85 buy_ready=False sector_rank=12 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-11-03T22:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=1000.0 spike=0.18
- CICH.CA: score=6.01 buy_ready=False sector_rank=15 price=10.77 support=9.63 resistance=12.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:02 PM market time freshness=DELAYED_CURRENT RSI=43.05 liquidity=488060.75 spike=0.2
- CIEB.CA: score=17.08 buy_ready=False sector_rank=11 price=22.92 support=21.35 resistance=24.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=47.51 liquidity=8371599.0 spike=1.04
- CIRA.CA: score=19.86 buy_ready=False sector_rank=9 price=37.12 support=32.01 resistance=40.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=45.48 liquidity=15047651.0 spike=1.06
- CLHO.CA: score=19.6 buy_ready=False sector_rank=4 price=13.85 support=12.51 resistance=15.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=40.69 liquidity=46737104.0 spike=1.27
- CNFN.CA: score=17.48 buy_ready=False sector_rank=15 price=4.0 support=3.25 resistance=4.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=41.18 liquidity=9740974.0 spike=1.11
- COMI.CA: score=18.63 buy_ready=False sector_rank=11 price=128.4 support=117.41 resistance=129.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=52.51 liquidity=523990848.0 spike=0.99
- COPR.CA: score=17.23 buy_ready=False sector_rank=12 price=0.41 support=0.33 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=28581794.0 spike=2.04
- COSG.CA: score=17.03 buy_ready=False sector_rank=12 price=1.34 support=1.11 resistance=1.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=36.62 liquidity=13447991.0 spike=1.44
- CPCI.CA: score=13.66 buy_ready=False sector_rank=12 price=598.04 support=502.25 resistance=620.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:13 PM market time freshness=DELAYED_CURRENT RSI=47.78 liquidity=3505747.5 spike=0.73
- CSAG.CA: score=21.18 buy_ready=False sector_rank=2 price=35.28 support=30.1 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=41.82 liquidity=8320956.5 spike=1.23
- DAPH.CA: score=18.15 buy_ready=False sector_rank=12 price=86.13 support=65.2 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.74 liquidity=24572768.0 spike=0.85
- DEIN.CA: score=8.15 buy_ready=False sector_rank=12 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=29 October 12:10 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=62.1 spike=0.02
- DOMT.CA: score=11.92 buy_ready=False sector_rank=8 price=23.91 support=20.27 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=2689423.75 spike=1.12
- DSCW.CA: score=16.63 buy_ready=False sector_rank=12 price=1.48 support=1.23 resistance=1.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=39.24 liquidity=15492907.0 spike=1.24
- DTPP.CA: score=13.79 buy_ready=False sector_rank=12 price=49.08 support=36.0 resistance=318.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=26.1 liquidity=71629472.0 spike=2.32
- EALR.CA: score=22.31 buy_ready=False sector_rank=12 price=294.01 support=236.01 resistance=353.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=49.62 liquidity=15230956.0 spike=3.08
- EASB.CA: score=16.08 buy_ready=False sector_rank=12 price=6.5 support=5.03 resistance=8.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=46.47 liquidity=6667904.0 spike=1.13
- EAST.CA: score=21.99 buy_ready=False sector_rank=8 price=33.22 support=27.01 resistance=33.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=66.78 liquidity=36686584.0 spike=0.96
- EBSC.CA: score=10.51 buy_ready=False sector_rank=12 price=1.53 support=1.2 resistance=1.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=43.88 liquidity=2359174.25 spike=0.77
- ECAP.CA: score=11.89 buy_ready=False sector_rank=12 price=27.87 support=24.8 resistance=30.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=43.76 liquidity=3178857.75 spike=1.28
- EDFM.CA: score=10.22 buy_ready=False sector_rank=12 price=361.29 support=312.92 resistance=382.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:13 PM market time freshness=DELAYED_CURRENT RSI=45.2 liquidity=1070496.0 spike=0.89
- EEII.CA: score=11.8 buy_ready=False sector_rank=12 price=1.79 support=1.42 resistance=2.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=41.57 liquidity=5645143.5 spike=0.81
- EFIC.CA: score=9.33 buy_ready=False sector_rank=16 price=168.65 support=143.89 resistance=168.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=155623696.0 spike=8.95
- EFID.CA: score=23.19 buy_ready=False sector_rank=8 price=19.37 support=16.01 resistance=19.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=53.31 liquidity=71554424.0 spike=2.1
- EFIH.CA: score=23.83 buy_ready=False sector_rank=5 price=24.39 support=20.3 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=46.45 liquidity=83077568.0 spike=1.4
- EGAL.CA: score=18.33 buy_ready=False sector_rank=16 price=323.72 support=275.0 resistance=344.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=57.36 liquidity=93838664.0 spike=0.97
- EGAS.CA: score=10.04 buy_ready=False sector_rank=18 price=47.79 support=43.0 resistance=57.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=35.33 liquidity=6057179.5 spike=1.5
- EGBE.CA: score=5.65 buy_ready=False sector_rank=11 price=0.49 support=0.47 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=42.55 liquidity=20623.11 spike=0.3
- EGCH.CA: score=8.33 buy_ready=False sector_rank=16 price=10.5 support=9.66 resistance=13.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=33.79 liquidity=37684628.0 spike=0.7
- EGSA.CA: score=4.65 buy_ready=False sector_rank=17 price=8.71 support=8.7 resistance=9.09 source=Yahoo Finance as_of=2026-11-03T22:00:00+00:00 freshness=FRESH RSI=42.19 liquidity=5269.55 spike=1.22
- EGTS.CA: score=19.56 buy_ready=False sector_rank=10 price=13.13 support=10.19 resistance=16.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=43.88 liquidity=25679940.0 spike=1.42
- EHDR.CA: score=16.11 buy_ready=False sector_rank=12 price=2.11 support=1.8 resistance=2.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=40.31 liquidity=9776423.0 spike=1.09
- ELEC.CA: score=19.0 buy_ready=False sector_rank=7 price=1.68 support=1.34 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=43.56 liquidity=48398692.0 spike=0.95
- ELKA.CA: score=19.21 buy_ready=False sector_rank=12 price=1.51 support=1.21 resistance=1.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=13849936.0 spike=1.03
- ELNA.CA: score=11.92 buy_ready=False sector_rank=12 price=41.29 support=33.46 resistance=41.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=71.06 liquidity=924497.44 spike=1.42
- ELSH.CA: score=20.29 buy_ready=False sector_rank=12 price=10.56 support=8.57 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=42.28 liquidity=25264288.0 spike=1.57
- ELWA.CA: score=14.15 buy_ready=False sector_rank=12 price=1.4 support=1.3 resistance=1.66 source=Yahoo Finance as_of=2026-11-03T22:00:00+00:00 freshness=FRESH RSI=12.12 liquidity=10070649.23 spike=12.69
- EMFD.CA: score=19.72 buy_ready=False sector_rank=10 price=12.25 support=10.6 resistance=12.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=53.21 liquidity=47934672.0 spike=0.87
- ENGC.CA: score=18.79 buy_ready=False sector_rank=12 price=34.98 support=26.91 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=53.68 liquidity=12304918.0 spike=1.32
- EOSB.CA: score=10.17 buy_ready=False sector_rank=12 price=1.61 support=1.55 resistance=1.72 source=Yahoo Finance as_of=2026-11-03T22:00:00+00:00 freshness=FRESH RSI=70.0 liquidity=16149.91 spike=0.18
- EPCO.CA: score=10.59 buy_ready=False sector_rank=12 price=8.55 support=7.0 resistance=9.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=45.05 liquidity=2441787.25 spike=0.49
- EPPK.CA: score=-4.43 buy_ready=False sector_rank=12 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=14.2 buy_ready=False sector_rank=17 price=130.75 support=115.0 resistance=150.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=35.89 liquidity=161640768.0 spike=0.67
- ETRS.CA: score=23.89 buy_ready=False sector_rank=12 price=10.98 support=9.51 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=52.16 liquidity=25774394.0 spike=1.87
- EXPA.CA: score=18.63 buy_ready=False sector_rank=11 price=14.37 support=12.0 resistance=16.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=42.44 liquidity=11772090.0 spike=0.47
- FAIT.CA: score=4.19 buy_ready=False sector_rank=11 price=45.91 support=43.2 resistance=46.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5825392.5 spike=2.37
- FAITA.CA: score=14.83 buy_ready=False sector_rank=11 price=1.0 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:03 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=65613.49 spike=2.07
- FERC.CA: score=9.33 buy_ready=False sector_rank=16 price=72.02 support=61.21 resistance=72.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=52655980.0 spike=15.12
- FWRY.CA: score=15.03 buy_ready=False sector_rank=5 price=17.3 support=15.27 resistance=19.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=35.51 liquidity=107648736.0 spike=0.91
- GBCO.CA: score=9.74 buy_ready=False sector_rank=21 price=22.44 support=20.9 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=15.12 liquidity=239948528.0 spike=2.37
- GDWA.CA: score=18.85 buy_ready=False sector_rank=12 price=0.57 support=0.46 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=40.09 liquidity=16165492.0 spike=1.35
- GGCC.CA: score=11.55 buy_ready=False sector_rank=12 price=0.56 support=0.49 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=30.59 liquidity=22844812.0 spike=1.2
- GIHD.CA: score=9.21 buy_ready=False sector_rank=12 price=46.99 support=45.25 resistance=48.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=41449444.0 spike=3.03
- GMCI.CA: score=1.01 buy_ready=False sector_rank=12 price=1.42 support=1.34 resistance=1.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=15.38 liquidity=501989.12 spike=1.68
- GRCA.CA: score=23.15 buy_ready=False sector_rank=12 price=32.12 support=22.57 resistance=37.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=50.79 liquidity=28421108.0 spike=3.79
- GSSC.CA: score=10.44 buy_ready=False sector_rank=12 price=258.88 support=211.52 resistance=287.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:12 PM market time freshness=DELAYED_CURRENT RSI=40.56 liquidity=1085880.5 spike=1.1
- HDBK.CA: score=17.11 buy_ready=False sector_rank=11 price=99.99 support=83.01 resistance=108.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.96 liquidity=27989556.0 spike=1.24
- HELI.CA: score=21.3 buy_ready=False sector_rank=10 price=6.94 support=5.72 resistance=7.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.92 liquidity=125655952.0 spike=1.79
- HRHO.CA: score=8.72 buy_ready=False sector_rank=15 price=23.81 support=21.87 resistance=27.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=33.24 liquidity=60309872.0 spike=1.1
- ICID.CA: score=22.75 buy_ready=False sector_rank=12 price=17.98 support=14.26 resistance=18.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=43.33 liquidity=10980340.0 spike=2.3
- IDRE.CA: score=19.02 buy_ready=False sector_rank=12 price=39.99 support=29.11 resistance=52.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=40.54 liquidity=9408897.0 spike=1.73
- IFAP.CA: score=12.3 buy_ready=False sector_rank=3 price=18.28 support=16.21 resistance=19.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=41245884.0 spike=8.55
- INFI.CA: score=19.15 buy_ready=False sector_rank=12 price=119.53 support=93.44 resistance=138.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=43.37 liquidity=16820152.0 spike=0.85
- IRON.CA: score=8.96 buy_ready=False sector_rank=16 price=24.18 support=23.13 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=37.2 liquidity=5630106.5 spike=0.52
- ISMA.CA: score=7.59 buy_ready=False sector_rank=12 price=20.71 support=19.7 resistance=20.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17178832.0 spike=2.22
- ISMQ.CA: score=17.33 buy_ready=False sector_rank=16 price=7.41 support=5.96 resistance=8.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=47.3 liquidity=14375043.0 spike=0.99
- ISPH.CA: score=21.04 buy_ready=False sector_rank=4 price=10.39 support=9.02 resistance=11.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.64 liquidity=104780840.0 spike=1.99
- JUFO.CA: score=18.99 buy_ready=False sector_rank=8 price=24.07 support=21.01 resistance=25.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=47.74 liquidity=21386542.0 spike=1.0
- KABO.CA: score=16.94 buy_ready=False sector_rank=13 price=7.13 support=5.58 resistance=9.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=46.23 liquidity=17184662.0 spike=0.83
- KWIN.CA: score=20.89 buy_ready=False sector_rank=12 price=69.46 support=44.02 resistance=79.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=55.57 liquidity=17048112.0 spike=2.37
- KZPC.CA: score=10.15 buy_ready=False sector_rank=12 price=13.56 support=12.72 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29197290.0 spike=4.53
- LCSW.CA: score=23.1 buy_ready=False sector_rank=6 price=36.01 support=28.0 resistance=36.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=54.61 liquidity=21674192.0 spike=1.04
- LUTS.CA: score=19.21 buy_ready=False sector_rank=12 price=0.75 support=0.47 resistance=0.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.98 liquidity=60982272.0 spike=1.03
- MAAL.CA: score=12.25 buy_ready=False sector_rank=12 price=6.9 support=4.88 resistance=10.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=37.74 liquidity=5096807.5 spike=0.47
- MASR.CA: score=17.15 buy_ready=False sector_rank=12 price=6.81 support=5.6 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=41.28 liquidity=35932300.0 spike=0.77
- MBSC.CA: score=18.02 buy_ready=False sector_rank=6 price=320.27 support=262.0 resistance=401.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.8 liquidity=35531604.0 spike=0.48
- MCQE.CA: score=19.02 buy_ready=False sector_rank=6 price=171.71 support=144.0 resistance=203.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=46.05 liquidity=43980412.0 spike=0.77
- MCRO.CA: score=18.63 buy_ready=False sector_rank=12 price=1.33 support=1.07 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=48454132.0 spike=1.24
- MENA.CA: score=11.9 buy_ready=False sector_rank=10 price=5.97 support=5.45 resistance=6.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:13 PM market time freshness=DELAYED_CURRENT RSI=49.36 liquidity=2173366.25 spike=0.51
- MEPA.CA: score=10.75 buy_ready=False sector_rank=12 price=1.35 support=1.14 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=26.32 liquidity=26092206.0 spike=1.8
- MFPC.CA: score=14.89 buy_ready=False sector_rank=16 price=40.89 support=39.59 resistance=47.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.36 liquidity=71348792.0 spike=1.28
- MFSC.CA: score=7.32 buy_ready=False sector_rank=12 price=35.27 support=28.55 resistance=45.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=43.11 liquidity=1170680.88 spike=0.58
- MHOT.CA: score=13.77 buy_ready=False sector_rank=1 price=15.7 support=13.0 resistance=16.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=52.45 liquidity=1370565.88 spike=0.22
- MICH.CA: score=13.28 buy_ready=False sector_rank=12 price=40.85 support=35.5 resistance=44.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=46.51 liquidity=4124093.25 spike=0.72
- MILS.CA: score=6.15 buy_ready=False sector_rank=12 price=135.07 support=130.0 resistance=136.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11763585.0 spike=1.5
- MIPH.CA: score=13.42 buy_ready=False sector_rank=4 price=793.31 support=610.0 resistance=830.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:59 PM market time freshness=DELAYED_CURRENT RSI=51.05 liquidity=358533.66 spike=0.1
- MOED.CA: score=13.55 buy_ready=False sector_rank=12 price=0.49 support=0.39 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=32.03 liquidity=26983022.0 spike=2.2
- MOIL.CA: score=4.09 buy_ready=False sector_rank=18 price=0.64 support=0.6 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=37.64 liquidity=110536.61 spike=0.65
- MOIN.CA: score=10.24 buy_ready=False sector_rank=12 price=29.57 support=25.7 resistance=36.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:12 PM market time freshness=DELAYED_CURRENT RSI=38.84 liquidity=3083297.0 spike=0.45
- MOSC.CA: score=9.67 buy_ready=False sector_rank=12 price=265.84 support=249.0 resistance=275.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10206158.0 spike=3.26
- MPCI.CA: score=19.91 buy_ready=False sector_rank=12 price=316.08 support=238.6 resistance=350.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.9 liquidity=135201600.0 spike=1.38
- MPCO.CA: score=17.98 buy_ready=False sector_rank=3 price=1.9 support=1.55 resistance=2.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=40.34 liquidity=105558752.0 spike=1.34
- MPRC.CA: score=19.49 buy_ready=False sector_rank=12 price=34.52 support=27.0 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.69 liquidity=16650484.0 spike=1.17
- MTIE.CA: score=14.72 buy_ready=False sector_rank=21 price=7.1 support=6.05 resistance=8.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.32 liquidity=43438636.0 spike=2.36
- NAHO.CA: score=5.17 buy_ready=False sector_rank=12 price=0.12 support=0.12 resistance=0.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:11 PM market time freshness=DELAYED_CURRENT RSI=42.11 liquidity=13045.8 spike=0.76
- NCCW.CA: score=16.61 buy_ready=False sector_rank=12 price=5.46 support=4.05 resistance=7.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=42.82 liquidity=20189492.0 spike=1.23
- NEDA.CA: score=0.22 buy_ready=False sector_rank=12 price=2.36 support=2.26 resistance=2.66 source=Yahoo Finance as_of=2026-11-03T22:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=227551.19 spike=1.42
- NHPS.CA: score=16.77 buy_ready=False sector_rank=12 price=62.15 support=50.0 resistance=75.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=42.26 liquidity=8202537.0 spike=1.21
- NINH.CA: score=20.03 buy_ready=False sector_rank=12 price=15.87 support=12.36 resistance=19.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=42.01 liquidity=16734110.0 spike=1.94
- NIPH.CA: score=20.14 buy_ready=False sector_rank=4 price=279.82 support=205.0 resistance=318.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=50.82 liquidity=131558168.0 spike=1.04
- OBRI.CA: score=18.15 buy_ready=False sector_rank=12 price=24.36 support=18.11 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.11 liquidity=10118175.0 spike=0.9
- OCDI.CA: score=20.0 buy_ready=False sector_rank=10 price=24.99 support=21.0 resistance=27.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=44.81 liquidity=35703156.0 spike=1.14
- OCPH.CA: score=20.65 buy_ready=False sector_rank=12 price=187.21 support=147.96 resistance=228.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=44.91 liquidity=10060485.0 spike=3.25
- ODIN.CA: score=15.58 buy_ready=False sector_rank=12 price=2.1 support=1.7 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=42.42 liquidity=8807893.0 spike=1.31
- OFH.CA: score=13.41 buy_ready=False sector_rank=12 price=0.74 support=0.61 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=34.23 liquidity=33529638.0 spike=1.63
- OIH.CA: score=6.29 buy_ready=False sector_rank=19 price=1.82 support=1.72 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=91629488.0 spike=2.19
- OLFI.CA: score=6.4 buy_ready=False sector_rank=8 price=19.58 support=17.86 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=31.06 liquidity=4403959.5 spike=0.51
- ORAS.CA: score=4.6 buy_ready=False sector_rank=14 price=813.63 support=802.5 resistance=815.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=101760416.0 spike=1.0
- ORHD.CA: score=19.02 buy_ready=False sector_rank=10 price=10.34 support=8.5 resistance=12.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=42.76 liquidity=134808128.0 spike=1.15
- ORWE.CA: score=13.94 buy_ready=False sector_rank=13 price=25.54 support=22.2 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=34.68 liquidity=21066372.0 spike=0.61
- PHAR.CA: score=20.38 buy_ready=False sector_rank=4 price=102.59 support=90.2 resistance=115.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=43.52 liquidity=60915048.0 spike=1.16
- PHDC.CA: score=9.26 buy_ready=False sector_rank=10 price=12.0 support=11.35 resistance=12.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=265130608.0 spike=2.77
- PHTV.CA: score=7.15 buy_ready=False sector_rank=12 price=322.0 support=300.0 resistance=355.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=38.94 liquidity=1637254.63 spike=1.18
- POUL.CA: score=20.95 buy_ready=False sector_rank=8 price=10.12 support=8.81 resistance=10.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=52.5 liquidity=141268272.0 spike=1.98
- PRCL.CA: score=20.98 buy_ready=False sector_rank=6 price=21.95 support=16.65 resistance=26.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=47.13 liquidity=28044938.0 spike=1.98
- PRDC.CA: score=19.72 buy_ready=False sector_rank=10 price=6.45 support=5.08 resistance=7.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=48.08 liquidity=16676309.0 spike=0.79
- PRMH.CA: score=10.71 buy_ready=False sector_rank=12 price=1.94 support=1.7 resistance=2.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=46.73 liquidity=3973370.5 spike=1.29
- RACC.CA: score=10.33 buy_ready=False sector_rank=12 price=8.04 support=6.1 resistance=9.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=34.82 liquidity=8381279.5 spike=1.4
- RAKT.CA: score=4.35 buy_ready=False sector_rank=12 price=22.35 support=20.4 resistance=25.08 source=Yahoo Finance as_of=2026-11-03T22:00:00+00:00 freshness=FRESH RSI=53.99 liquidity=201954.6 spike=0.67
- RAYA.CA: score=14.77 buy_ready=False sector_rank=20 price=5.6 support=5.02 resistance=6.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.5 liquidity=22926394.0 spike=1.19
- RMDA.CA: score=23.68 buy_ready=False sector_rank=4 price=5.5 support=4.5 resistance=5.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=57.02 liquidity=45662940.0 spike=1.81
- ROTO.CA: score=16.49 buy_ready=False sector_rank=12 price=32.57 support=25.0 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=36.66 liquidity=10215791.0 spike=1.17
- RREI.CA: score=9.16 buy_ready=False sector_rank=12 price=2.85 support=1.96 resistance=4.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=32.75 liquidity=8007479.0 spike=0.78
- RTVC.CA: score=1.0 buy_ready=False sector_rank=12 price=2.79 support=2.66 resistance=3.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=22.61 liquidity=1844433.38 spike=0.72
- RUBX.CA: score=15.15 buy_ready=False sector_rank=12 price=13.24 support=10.51 resistance=19.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=38.07 liquidity=31018236.0 spike=0.43
- SAUD.CA: score=15.63 buy_ready=False sector_rank=11 price=20.97 support=19.3 resistance=23.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=35.52 liquidity=10599892.0 spike=0.97
- SCEM.CA: score=25.02 buy_ready=False sector_rank=6 price=94.38 support=73.9 resistance=95.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=52.98 liquidity=42991076.0 spike=0.84
- SCFM.CA: score=11.28 buy_ready=False sector_rank=12 price=217.81 support=153.02 resistance=249.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=45.07 liquidity=2648455.0 spike=1.24
- SCTS.CA: score=10.74 buy_ready=False sector_rank=9 price=519.89 support=499.99 resistance=547.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17102448.0 spike=3.8
- SDTI.CA: score=24.23 buy_ready=False sector_rank=12 price=87.67 support=75.01 resistance=90.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=57.46 liquidity=18785252.0 spike=1.04
- SEIG.CA: score=3.1 buy_ready=False sector_rank=12 price=240.49 support=239.05 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7948405.0 spike=0.98
- SIPC.CA: score=6.87 buy_ready=False sector_rank=12 price=5.1 support=4.67 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=97319488.0 spike=1.86
- SKPC.CA: score=17.43 buy_ready=False sector_rank=16 price=15.12 support=14.01 resistance=16.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=43.81 liquidity=51260980.0 spike=1.05
- SMFR.CA: score=10.15 buy_ready=False sector_rank=12 price=227.71 support=198.98 resistance=227.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17380720.0 spike=7.61
- SNFC.CA: score=24.11 buy_ready=False sector_rank=12 price=11.1 support=10.08 resistance=11.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=35.68 liquidity=22910936.0 spike=2.98
- SPIN.CA: score=8.64 buy_ready=False sector_rank=13 price=14.46 support=12.0 resistance=16.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=45.73 liquidity=2695805.25 spike=0.51
- SPMD.CA: score=21.15 buy_ready=False sector_rank=12 price=0.35 support=0.3 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.9 liquidity=65580328.0 spike=4.6
- SUGR.CA: score=15.33 buy_ready=False sector_rank=8 price=47.87 support=44.62 resistance=54.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=35.32 liquidity=9340274.0 spike=0.97
- SVCE.CA: score=16.15 buy_ready=False sector_rank=12 price=8.82 support=7.01 resistance=10.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=45.15 liquidity=46727868.0 spike=0.98
- SWDY.CA: score=22.94 buy_ready=False sector_rank=7 price=116.97 support=97.0 resistance=118.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.69 liquidity=120413968.0 spike=2.47
- TALM.CA: score=21.04 buy_ready=False sector_rank=9 price=20.42 support=17.0 resistance=22.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=38.72 liquidity=25572536.0 spike=1.15
- TMGH.CA: score=17.54 buy_ready=False sector_rank=10 price=83.85 support=76.5 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=43.74 liquidity=363178912.0 spike=1.41
- TRTO.CA: score=0.15 buy_ready=False sector_rank=12 price=0.05 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-11-03T22:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=1057.76 spike=0.22
- UEFM.CA: score=7.93 buy_ready=False sector_rank=12 price=479.54 support=422.0 resistance=520.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:11 PM market time freshness=DELAYED_CURRENT RSI=44.56 liquidity=1777795.88 spike=0.84
- UEGC.CA: score=18.15 buy_ready=False sector_rank=12 price=1.49 support=1.21 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.64 liquidity=26249544.0 spike=0.56
- UNIP.CA: score=17.55 buy_ready=False sector_rank=12 price=0.3 support=0.25 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=37.06 liquidity=11983937.0 spike=1.7
- UNIT.CA: score=15.49 buy_ready=False sector_rank=10 price=18.52 support=15.06 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=60.32 liquidity=768062.06 spike=0.24
- WCDF.CA: score=7.04 buy_ready=False sector_rank=12 price=514.51 support=432.5 resistance=624.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:08 PM market time freshness=DELAYED_CURRENT RSI=38.46 liquidity=887714.5 spike=0.51
- WKOL.CA: score=7.27 buy_ready=False sector_rank=12 price=176.37 support=173.0 resistance=188.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21025198.0 spike=2.06
- ZEOT.CA: score=21.11 buy_ready=False sector_rank=12 price=11.28 support=7.9 resistance=12.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=47.96 liquidity=15151380.0 spike=1.98
- ZMID.CA: score=20.06 buy_ready=False sector_rank=10 price=6.9 support=5.91 resistance=7.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.05 liquidity=81707912.0 spike=1.17

## Backtesting Lite
- SCEM.CA: 180d return=46.03%, max drawdown=-29.64%, MA20>MA50 days last20=0, as_of=2026-11-03T22:00:00+00:00
- SDTI.CA: 180d return=211.98%, max drawdown=-9.43%, MA20>MA50 days last20=20, as_of=2026-11-03T22:00:00+00:00
- SNFC.CA: 180d return=10.13%, max drawdown=-18.57%, MA20>MA50 days last20=18, as_of=2026-11-03T22:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- SCEM.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=673 sources=3 expected=Sinai Cement summary=Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn; Upward trend line ends several-day decline for Sinai Cement stock; Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25
  - Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn: https://english.mubasher.info/news/4564824/Sinai-Cement-s-consolidated-profits-fall-in-2025-net-sales-cross-EGP-9bn/
  - Upward trend line ends several-day decline for Sinai Cement stock: https://english.mubasher.info/news/4529647/Upward-trend-line-ends-several-day-decline-for-Sinai-Cement-stock/
  - Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25: https://english.mubasher.info/news/4526073/Sinai-Cement-reports-lower-consolidated-net-profits-at-EGP-1-5bn-in-9M-25/
- SDTI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=SHARM DREAMS Co. for Touristic Investment S.A.E summary=Sharm Dreams stock maintains strong uptrend - Analysis; Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis; Sharm Dreams stock hits historic level halting driving buying force
  - Sharm Dreams stock maintains strong uptrend - Analysis: https://english.mubasher.info/news/4577977/Sharm-Dreams-stock-maintains-strong-uptrend-Analysis/
  - Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis: https://english.mubasher.info/news/4547831/Sharm-Dreams-stock-is-experiencing-sideways-movement-amid-anticipation-of-next-trend-Analysis/
  - Sharm Dreams stock hits historic level halting driving buying force: https://english.mubasher.info/news/4529096/Sharm-Dreams-stock-hits-historic-level-halting-driving-buying-force/
- SNFC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Sharkia National Company for Food Security summary=Sharkia National Food sells EGP 6.5m asset; Sharkia Food turns profitable in Q4; Sharkia National Food turns profitable in Q4
  - Sharkia National Food sells EGP 6.5m asset: https://english.mubasher.info/news/3344769/Sharkia-National-Food-sells-EGP-6-5m-asset/
  - Sharkia Food turns profitable in Q4: https://english.mubasher.info/news/3055832/Sharkia-Food-turns-profitable-in-Q4/
  - Sharkia National Food turns profitable in Q4: https://english.mubasher.info/news/3053492/Sharkia-National-Food-turns-profitable-in-Q4/
- ETRS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Transport and Commercial Services Company S.A.E. summary=Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- RMDA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tenth of Ramadan Pharmaceutical Industries summary=Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- CANA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=673 sources=3 expected=Suez Canal Bank summary=Suez Canal Bank delivers EGP 1.6bn profits in Q1-26; Suez Canal Bank unveils details for previous dividends payout; Suez Canal Bank to distribute EGP 5bn bonus shares for 2025
  - Suez Canal Bank delivers EGP 1.6bn profits in Q1-26: https://english.mubasher.info/news/4611255/Suez-Canal-Bank-delivers-EGP-1-6bn-profits-in-Q1-26/
  - Suez Canal Bank unveils details for previous dividends payout: https://english.mubasher.info/news/4586807/Suez-Canal-Bank-unveils-details-for-previous-dividends-payout/
  - Suez Canal Bank to distribute EGP 5bn bonus shares for 2025: https://english.mubasher.info/news/4581661/Suez-Canal-Bank-to-distribute-EGP-5bn-bonus-shares-for-2025/
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.

## Warnings
- OpenRouter API error: 404
- Evidence for SCEM.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for SDTI.CA matches the company but no source/report date was detected.
- Evidence for SNFC.CA matches the company but no source/report date was detected.
- Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
