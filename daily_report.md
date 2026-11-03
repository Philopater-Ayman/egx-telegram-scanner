# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-11-03T13:02:11.571278+00:00
Generated Cairo: 2026-11-03 15:02
Run timing: target 08:45 Cairo | generated Cairo 2026-11-03 15:02 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-11-03 14:59

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 5
- Tradeable price/liquidity tickers: 165/185
- Top sector: Building Materials

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, November 03
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 26.32% / above MA50 0.0%
- EGX70 regime: BEARISH / above MA20 11.43% / above MA50 8.57%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=402637024.0 spike=0.75 score=15.74
- GTWL.CA: liquidity=332320736.0 spike=1.83 score=19.62
- EMFD.CA: liquidity=261490096.0 spike=5.67 score=23.21
- PHDC.CA: liquidity=241357744.0 spike=2.76 score=7.73
- ORAS.CA: liquidity=204893456.0 spike=1.0 score=4.6

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- KWIN.CA: spike=8.38 liquidity=36007624.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SEIG.CA: spike=7.81 liquidity=44774904.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CAED.CA: spike=7.52 liquidity=65591116.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EMFD.CA: spike=5.67 liquidity=261490096.0 outlook=CONSTRUCTIVE score=60.52 buy_ready=False
- GRCA.CA: spike=5.15 liquidity=21965278.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Building Materials: score=4.06 5d=11.62% 20d=-15.04% aboveMA50=16.67%
- #2 Tourism & Leisure: score=3.37 5d=9.93% 20d=-10.08% aboveMA50=0.0%
- #3 Food, Beverages & Tobacco: score=2.54 5d=4.62% 20d=-8.26% aboveMA50=0.0%
- #4 Transportation & Logistics: score=2.39 5d=3.72% 20d=-6.18% aboveMA50=0.0%
- #5 Banking & Financials: score=1.85 5d=2.31% 20d=-7.34% aboveMA50=20.0%
- #6 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #7 Fintech & Payments: score=1.25 5d=2.78% 20d=-10.83% aboveMA50=0.0%
- #8 Real Estate: score=0.52 5d=1.86% 20d=-11.64% aboveMA50=7.69%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- LCSW.CA: BULLISH_WATCH score=74.06 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- CANA.CA: BULLISH_WATCH score=71.85 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- EFIH.CA: BULLISH_WATCH score=71.25 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- UNIT.CA: BULLISH_WATCH score=70.52 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- SUGR.CA: CONSTRUCTIVE score=65.54 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=below MA20; below MA50
- AJWA.CA: CONSTRUCTIVE score=65 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- SCEM.CA: CONSTRUCTIVE score=62.06 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA50
- JUFO.CA: CONSTRUCTIVE score=60.54 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=below MA20; below MA50
- POUL.CA: CONSTRUCTIVE score=60.54 liquidity=TRADEABLE sector=LEADING risk=below MA50
- EMFD.CA: CONSTRUCTIVE score=60.52 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA50; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GDWA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- MILS.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=10.98 buy_ready=False sector_rank=11 price=216.99 support=171.02 resistance=275.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=39.94 liquidity=6013518.0 spike=0.68
- ABUK.CA: score=13.49 buy_ready=False sector_rank=14 price=77.76 support=79.01 resistance=95.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=45.42 liquidity=91297456.0 spike=1.0
- ACAMD.CA: score=14.12 buy_ready=False sector_rank=11 price=1.94 support=1.86 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=45.16 liquidity=69431072.0 spike=1.58
- ACGC.CA: score=4.61 buy_ready=False sector_rank=18 price=12.76 support=11.6 resistance=14.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=45.77 liquidity=1450625.5 spike=0.19
- ADCI.CA: score=6.36 buy_ready=False sector_rank=11 price=254.6 support=221.0 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=40.98 liquidity=399275.44 spike=0.22
- ADIB.CA: score=19.32 buy_ready=False sector_rank=5 price=48.06 support=43.16 resistance=50.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=55.17 liquidity=99422680.0 spike=1.29
- ADPC.CA: score=9.04 buy_ready=False sector_rank=11 price=2.99 support=2.53 resistance=3.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=41.18 liquidity=4074135.75 spike=0.45
- AFDI.CA: score=0.41 buy_ready=False sector_rank=11 price=43.76 support=34.8 resistance=54.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=34.93 liquidity=1445761.13 spike=0.39
- AFMC.CA: score=8.96 buy_ready=False sector_rank=11 price=132.0 support=117.5 resistance=134.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=56065884.0 spike=3.93
- AJWA.CA: score=15.95 buy_ready=False sector_rank=11 price=214.38 support=179.0 resistance=229.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=53.31 liquidity=6982454.0 spike=0.19
- ALCN.CA: score=5.52 buy_ready=False sector_rank=4 price=32.25 support=30.01 resistance=32.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16443271.0 spike=1.28
- ALUM.CA: score=4.72 buy_ready=False sector_rank=11 price=18.49 support=16.02 resistance=24.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=35.86 liquidity=1757160.5 spike=0.59
- AMER.CA: score=16.21 buy_ready=False sector_rank=8 price=4.27 support=3.21 resistance=5.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=39.46 liquidity=51658212.0 spike=0.94
- AMES.CA: score=10.58 buy_ready=False sector_rank=11 price=33.71 support=28.0 resistance=50.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=31.77 liquidity=59339016.0 spike=1.31
- AMIA.CA: score=14.88 buy_ready=False sector_rank=11 price=17.63 support=14.0 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=46.53 liquidity=21545736.0 spike=1.46
- AMOC.CA: score=18.94 buy_ready=False sector_rank=12 price=13.47 support=12.55 resistance=15.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=51.69 liquidity=90459808.0 spike=0.57
- APSW.CA: score=-1.56 buy_ready=False sector_rank=11 price=7.35 support=7.1 resistance=8.92 source=Yahoo Finance as_of=2026-11-01T22:00:00+00:00 freshness=FRESH RSI=33.13 liquidity=478940.69 spike=0.81
- ARAB.CA: score=9.21 buy_ready=False sector_rank=8 price=0.23 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=33.59 liquidity=57537832.0 spike=0.47
- ARCC.CA: score=18.32 buy_ready=False sector_rank=1 price=63.03 support=58.01 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=41.05 liquidity=9697464.0 spike=0.25
- AREH.CA: score=9.19 buy_ready=False sector_rank=11 price=1.04 support=0.91 resistance=1.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=38.0 liquidity=4222341.5 spike=0.59
- ASCM.CA: score=0.82 buy_ready=False sector_rank=11 price=42.2 support=38.2 resistance=59.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=33.54 liquidity=2854314.5 spike=0.36
- ASPI.CA: score=14.96 buy_ready=False sector_rank=11 price=0.3 support=0.27 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=40.61 liquidity=12107006.0 spike=0.66
- ATLC.CA: score=-2.41 buy_ready=False sector_rank=17 price=4.93 support=4.61 resistance=4.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4285669.5 spike=0.64
- ATQA.CA: score=7.49 buy_ready=False sector_rank=14 price=9.19 support=8.25 resistance=12.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=31.9 liquidity=28982616.0 spike=0.58
- AXPH.CA: score=9.84 buy_ready=False sector_rank=11 price=1315.98 support=1135.0 resistance=1550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=45.21 liquidity=3877853.25 spike=0.82
- BINV.CA: score=-1.1 buy_ready=False sector_rank=19 price=51.99 support=50.62 resistance=62.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=19.45 liquidity=1501685.25 spike=0.14
- BIOC.CA: score=5.66 buy_ready=False sector_rank=11 price=301.65 support=260.02 resistance=305.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=139854832.0 spike=1.85
- BTFH.CA: score=7.31 buy_ready=False sector_rank=17 price=2.28 support=2.05 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=34.4 liquidity=38030340.0 spike=0.33
- CAED.CA: score=8.96 buy_ready=False sector_rank=11 price=99.24 support=83.0 resistance=99.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=65591116.0 spike=7.52
- CANA.CA: score=17.94 buy_ready=False sector_rank=5 price=45.32 support=38.1 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=50.06 liquidity=6196821.5 spike=0.33
- CCAP.CA: score=12.4 buy_ready=False sector_rank=19 price=5.73 support=5.55 resistance=6.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=37.38 liquidity=117146280.0 spike=0.26
- CCRS.CA: score=1.62 buy_ready=False sector_rank=11 price=1.67 support=1.3 resistance=2.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=30.89 liquidity=3657435.5 spike=0.58
- CEFM.CA: score=6.87 buy_ready=False sector_rank=11 price=113.75 support=97.79 resistance=138.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=43.05 liquidity=2525263.5 spike=1.19
- CERA.CA: score=7.96 buy_ready=False sector_rank=11 price=1.02 support=0.93 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=32.79 liquidity=62364532.0 spike=0.59
- CFGH.CA: score=1.78 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=16.67 liquidity=16751.91 spike=2.9
- CICH.CA: score=9.08 buy_ready=False sector_rank=17 price=10.39 support=9.63 resistance=12.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=41.96 liquidity=3211002.0 spike=1.78
- CIEB.CA: score=9.85 buy_ready=False sector_rank=5 price=22.29 support=21.35 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=43.23 liquidity=4110035.5 spike=0.5
- CIRA.CA: score=13.84 buy_ready=False sector_rank=13 price=36.02 support=32.01 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=44.94 liquidity=12603087.0 spike=0.84
- CLHO.CA: score=9.44 buy_ready=False sector_rank=16 price=13.23 support=12.51 resistance=16.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=32.69 liquidity=23522388.0 spike=0.62
- CNFN.CA: score=2.3 buy_ready=False sector_rank=17 price=3.81 support=3.47 resistance=3.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8949152.0 spike=1.02
- COMI.CA: score=15.74 buy_ready=False sector_rank=5 price=123.48 support=117.41 resistance=129.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=50.69 liquidity=402637024.0 spike=0.75
- COPR.CA: score=6.74 buy_ready=False sector_rank=11 price=0.4 support=0.38 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33526166.0 spike=2.39
- COSG.CA: score=7.77 buy_ready=False sector_rank=11 price=1.26 support=1.11 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=4808847.5 spike=0.52
- CPCI.CA: score=8.1 buy_ready=False sector_rank=11 price=594.88 support=502.25 resistance=620.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=48.82 liquidity=1138935.63 spike=0.24
- CSAG.CA: score=18.1 buy_ready=False sector_rank=4 price=34.02 support=30.1 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=42.27 liquidity=10287200.0 spike=1.57
- DAPH.CA: score=9.96 buy_ready=False sector_rank=11 price=81.04 support=65.2 resistance=114.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=33.53 liquidity=19702598.0 spike=0.5
- DEIN.CA: score=6.96 buy_ready=False sector_rank=11 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=29 October 12:10 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=62.1 spike=0.02
- DOMT.CA: score=7.81 buy_ready=False sector_rank=3 price=23.05 support=20.27 resistance=25.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=46.46 liquidity=792772.19 spike=0.32
- DSCW.CA: score=16.12 buy_ready=False sector_rank=11 price=1.4 support=1.23 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=39.47 liquidity=19268432.0 spike=1.58
- DTPP.CA: score=9.96 buy_ready=False sector_rank=11 price=46.1 support=36.0 resistance=334.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=31.76 liquidity=15306360.0 spike=0.39
- EALR.CA: score=0.59 buy_ready=False sector_rank=11 price=252.85 support=236.01 resistance=355.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=27.25 liquidity=2624548.5 spike=0.79
- EASB.CA: score=7.92 buy_ready=False sector_rank=11 price=6.52 support=5.72 resistance=6.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14550192.0 spike=2.98
- EAST.CA: score=19.02 buy_ready=False sector_rank=3 price=31.17 support=27.01 resistance=32.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=62.48 liquidity=40168108.0 spike=0.99
- EBSC.CA: score=8.8 buy_ready=False sector_rank=11 price=1.51 support=1.37 resistance=1.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9836683.0 spike=3.99
- ECAP.CA: score=4.1 buy_ready=False sector_rank=11 price=26.39 support=24.8 resistance=31.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=35.47 liquidity=1134540.38 spike=0.38
- EDFM.CA: score=8.27 buy_ready=False sector_rank=11 price=349.45 support=312.92 resistance=396.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=39.17 liquidity=2362505.75 spike=1.97
- EEII.CA: score=8.12 buy_ready=False sector_rank=11 price=1.7 support=1.42 resistance=2.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=34.18 liquidity=7752851.5 spike=1.2
- EFIC.CA: score=11.96 buy_ready=False sector_rank=14 price=135.89 support=121.0 resistance=172.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.36 liquidity=7470001.0 spike=0.39
- EFID.CA: score=17.02 buy_ready=False sector_rank=3 price=18.2 support=16.01 resistance=19.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=47.3 liquidity=24369748.0 spike=0.72
- EFIH.CA: score=16.5 buy_ready=False sector_rank=7 price=23.32 support=20.3 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=46.63 liquidity=30748724.0 spike=0.45
- EGAL.CA: score=15.49 buy_ready=False sector_rank=14 price=302.61 support=275.0 resistance=350.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=40.39 liquidity=28960958.0 spike=0.32
- EGAS.CA: score=2.62 buy_ready=False sector_rank=12 price=45.77 support=43.0 resistance=58.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=32.81 liquidity=4499709.5 spike=1.09
- EGBE.CA: score=4.77 buy_ready=False sector_rank=5 price=0.49 support=0.47 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=36.7 liquidity=25876.97 spike=0.27
- EGCH.CA: score=7.49 buy_ready=False sector_rank=14 price=9.94 support=9.68 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=27.96 liquidity=26940934.0 spike=0.49
- EGSA.CA: score=5.15 buy_ready=False sector_rank=10 price=8.71 support=8.7 resistance=9.09 source=Yahoo Finance as_of=2026-11-01T22:00:00+00:00 freshness=FRESH RSI=40.7 liquidity=8710.0 spike=1.57
- EGTS.CA: score=4.1 buy_ready=False sector_rank=8 price=11.93 support=10.19 resistance=17.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=33.85 liquidity=5895677.5 spike=0.32
- EHDR.CA: score=8.85 buy_ready=False sector_rank=11 price=1.95 support=1.8 resistance=2.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=5883025.5 spike=0.66
- ELEC.CA: score=13.07 buy_ready=False sector_rank=9 price=1.54 support=1.34 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=28737446.0 spike=0.57
- ELKA.CA: score=12.28 buy_ready=False sector_rank=11 price=1.41 support=1.21 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=46.34 liquidity=7314540.5 spike=0.54
- ELNA.CA: score=8.38 buy_ready=False sector_rank=11 price=39.68 support=33.46 resistance=41.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=78.82 liquidity=415345.47 spike=0.66
- ELSH.CA: score=10.07 buy_ready=False sector_rank=11 price=9.96 support=8.57 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=37.57 liquidity=5110860.0 spike=0.31
- ELWA.CA: score=0.79 buy_ready=False sector_rank=11 price=1.36 support=1.43 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=667507.88 spike=2.08
- EMFD.CA: score=23.21 buy_ready=False sector_rank=8 price=12.18 support=10.6 resistance=13.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.46 liquidity=261490096.0 spike=5.67
- ENGC.CA: score=11.27 buy_ready=False sector_rank=11 price=34.01 support=26.91 resistance=38.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=49.49 liquidity=4306864.5 spike=0.47
- EOSB.CA: score=11.37 buy_ready=False sector_rank=11 price=1.61 support=1.55 resistance=1.72 source=Yahoo Finance as_of=2026-11-01T22:00:00+00:00 freshness=FRESH RSI=70.0 liquidity=189313.46 spike=2.11
- EPCO.CA: score=6.17 buy_ready=False sector_rank=11 price=8.25 support=7.0 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=43.16 liquidity=1207063.25 spike=0.22
- EPPK.CA: score=-5.62 buy_ready=False sector_rank=11 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=9.0 buy_ready=False sector_rank=10 price=122.84 support=115.0 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=27.88 liquidity=118988024.0 spike=0.47
- ETRS.CA: score=12.81 buy_ready=False sector_rank=11 price=10.61 support=9.51 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=51.03 liquidity=4845120.5 spike=0.36
- EXPA.CA: score=15.15 buy_ready=False sector_rank=5 price=13.69 support=12.0 resistance=16.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=40.56 liquidity=9410018.0 spike=0.29
- FAIT.CA: score=7.48 buy_ready=False sector_rank=5 price=42.43 support=40.0 resistance=45.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=51.3 liquidity=735206.94 spike=0.28
- FAITA.CA: score=11.74 buy_ready=False sector_rank=5 price=1.0 support=0.98 resistance=1.01 source=Yahoo Finance as_of=2026-11-01T22:00:00+00:00 freshness=FRESH RSI=60.44 liquidity=2052.95 spike=0.07
- FERC.CA: score=0.25 buy_ready=False sector_rank=14 price=58.04 support=53.57 resistance=77.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=33.49 liquidity=2756954.75 spike=0.78
- FWRY.CA: score=8.5 buy_ready=False sector_rank=7 price=16.1 support=15.27 resistance=19.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=21.76 liquidity=75561328.0 spike=0.62
- GBCO.CA: score=6.48 buy_ready=False sector_rank=21 price=21.6 support=20.9 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=17.88 liquidity=106553272.0 spike=1.04
- GGCC.CA: score=7.96 buy_ready=False sector_rank=11 price=0.53 support=0.49 resistance=0.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=33.24 liquidity=14586559.0 spike=0.84
- GIHD.CA: score=7.96 buy_ready=False sector_rank=11 price=42.81 support=32.1 resistance=68.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=27.16 liquidity=12147646.0 spike=0.84
- GMCI.CA: score=0.94 buy_ready=False sector_rank=11 price=1.36 support=1.34 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:09 PM market time freshness=DELAYED_CURRENT RSI=15.38 liquidity=633790.94 spike=2.17
- GRCA.CA: score=8.96 buy_ready=False sector_rank=11 price=29.31 support=25.0 resistance=29.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21965278.0 spike=5.15
- GSSC.CA: score=5.52 buy_ready=False sector_rank=11 price=242.69 support=211.52 resistance=288.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=46.0 liquidity=553027.06 spike=0.58
- GTWL.CA: score=19.62 buy_ready=False sector_rank=11 price=127.21 support=73.02 resistance=175.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=41.7 liquidity=332320736.0 spike=1.83
- HDBK.CA: score=13.74 buy_ready=False sector_rank=5 price=94.15 support=83.01 resistance=112.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=41.07 liquidity=10940613.0 spike=0.47
- HELI.CA: score=9.21 buy_ready=False sector_rank=8 price=6.35 support=5.72 resistance=7.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=32.28 liquidity=53671212.0 spike=0.79
- HRHO.CA: score=7.31 buy_ready=False sector_rank=17 price=22.55 support=21.87 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=27.39 liquidity=37277884.0 spike=0.39
- ICID.CA: score=5.02 buy_ready=False sector_rank=11 price=17.04 support=14.26 resistance=18.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=45.43 liquidity=1055702.75 spike=0.16
- IDRE.CA: score=7.02 buy_ready=False sector_rank=11 price=37.55 support=29.11 resistance=52.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=39.55 liquidity=4060844.25 spike=0.72
- IFAP.CA: score=-0.47 buy_ready=False sector_rank=20 price=15.65 support=15.12 resistance=19.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=24.64 liquidity=3128223.75 spike=0.65
- INFI.CA: score=13.96 buy_ready=False sector_rank=11 price=114.35 support=93.44 resistance=138.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=47.93 liquidity=10994305.0 spike=0.53
- IRON.CA: score=3.09 buy_ready=False sector_rank=14 price=23.88 support=23.34 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=32.98 liquidity=5595455.0 spike=0.53
- ISMA.CA: score=12.4 buy_ready=False sector_rank=11 price=19.05 support=14.11 resistance=27.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=39.32 liquidity=7392430.5 spike=1.02
- ISMQ.CA: score=14.69 buy_ready=False sector_rank=14 price=7.14 support=5.96 resistance=8.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=45.29 liquidity=15750257.0 spike=1.1
- ISPH.CA: score=7.44 buy_ready=False sector_rank=16 price=9.45 support=9.04 resistance=12.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=29.15 liquidity=45242780.0 spike=0.99
- JUFO.CA: score=22.02 buy_ready=False sector_rank=3 price=22.93 support=21.01 resistance=26.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.4 liquidity=82605832.0 spike=4.8
- KABO.CA: score=8.65 buy_ready=False sector_rank=18 price=6.77 support=5.58 resistance=9.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=38.97 liquidity=6498314.0 spike=0.3
- KWIN.CA: score=8.96 buy_ready=False sector_rank=11 price=63.55 support=51.0 resistance=63.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36007624.0 spike=8.38
- KZPC.CA: score=6.4 buy_ready=False sector_rank=11 price=12.74 support=11.56 resistance=13.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=46.72 liquidity=2439442.5 spike=0.35
- LCSW.CA: score=20.34 buy_ready=False sector_rank=1 price=35.16 support=28.0 resistance=36.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=59.5 liquidity=4718076.5 spike=0.18
- LUTS.CA: score=17.04 buy_ready=False sector_rank=11 price=0.71 support=0.47 resistance=0.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=43.87 liquidity=89842080.0 spike=1.54
- MAAL.CA: score=4.28 buy_ready=False sector_rank=11 price=6.7 support=4.88 resistance=11.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=31.3 liquidity=5320477.5 spike=0.45
- MASR.CA: score=13.96 buy_ready=False sector_rank=11 price=6.65 support=5.6 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=42.03 liquidity=25432798.0 spike=0.53
- MBSC.CA: score=18.62 buy_ready=False sector_rank=1 price=311.0 support=262.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=38.94 liquidity=66423924.0 spike=0.66
- MCQE.CA: score=19.62 buy_ready=False sector_rank=1 price=160.92 support=144.0 resistance=219.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=40.42 liquidity=56181760.0 spike=0.82
- MCRO.CA: score=14.96 buy_ready=False sector_rank=11 price=1.27 support=1.07 resistance=1.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=42.17 liquidity=41886848.0 spike=0.99
- MENA.CA: score=7.22 buy_ready=False sector_rank=8 price=5.78 support=5.45 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=42.24 liquidity=4010229.75 spike=0.94
- MEPA.CA: score=7.96 buy_ready=False sector_rank=11 price=1.26 support=1.14 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=29.11 liquidity=10117199.0 spike=0.73
- MFPC.CA: score=14.39 buy_ready=False sector_rank=14 price=40.14 support=40.66 resistance=47.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=43.23 liquidity=75075736.0 spike=1.45
- MFSC.CA: score=-1.49 buy_ready=False sector_rank=11 price=32.68 support=28.55 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=31.83 liquidity=543638.13 spike=0.29
- MHOT.CA: score=14.36 buy_ready=False sector_rank=2 price=14.97 support=13.0 resistance=16.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=43.99 liquidity=6008429.0 spike=0.94
- MICH.CA: score=10.41 buy_ready=False sector_rank=11 price=39.95 support=35.5 resistance=44.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=46.58 liquidity=4447023.0 spike=0.73
- MIPH.CA: score=4.18 buy_ready=False sector_rank=16 price=751.77 support=610.0 resistance=830.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=43.35 liquidity=738188.5 spike=0.21
- MOED.CA: score=7.96 buy_ready=False sector_rank=11 price=0.46 support=0.39 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=27.16 liquidity=11730385.0 spike=0.92
- MOIL.CA: score=-1.04 buy_ready=False sector_rank=12 price=0.62 support=0.6 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=33.14 liquidity=17405.1 spike=0.09
- MOIN.CA: score=1.05 buy_ready=False sector_rank=11 price=28.11 support=25.7 resistance=37.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=32.43 liquidity=2090497.25 spike=0.26
- MOSC.CA: score=3.56 buy_ready=False sector_rank=11 price=234.23 support=198.01 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=40.48 liquidity=598919.94 spike=0.2
- MPCI.CA: score=17.96 buy_ready=False sector_rank=11 price=310.91 support=238.6 resistance=369.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=46.89 liquidity=84141560.0 spike=0.86
- MPCO.CA: score=6.4 buy_ready=False sector_rank=20 price=1.76 support=1.55 resistance=2.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=33.62 liquidity=72806944.0 spike=0.92
- MPRC.CA: score=11.83 buy_ready=False sector_rank=11 price=33.27 support=27.0 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.21 liquidity=8865047.0 spike=0.62
- MTIE.CA: score=10.52 buy_ready=False sector_rank=21 price=6.64 support=6.05 resistance=8.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.01 liquidity=9122856.0 spike=0.49
- NAHO.CA: score=3.97 buy_ready=False sector_rank=11 price=0.12 support=0.12 resistance=0.13 source=Yahoo Finance as_of=2026-11-01T22:00:00+00:00 freshness=FRESH RSI=40.0 liquidity=6845.3 spike=0.39
- NCCW.CA: score=13.0 buy_ready=False sector_rank=11 price=5.33 support=4.05 resistance=7.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.46 liquidity=17787926.0 spike=1.02
- NEDA.CA: score=-1.93 buy_ready=False sector_rank=11 price=2.36 support=2.3 resistance=2.67 source=Yahoo Finance as_of=2026-11-01T22:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=108062.04 spike=0.69
- NHPS.CA: score=7.98 buy_ready=False sector_rank=11 price=59.67 support=53.5 resistance=60.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18511278.0 spike=3.01
- NINH.CA: score=6.23 buy_ready=False sector_rank=11 price=14.67 support=12.36 resistance=19.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=33.21 liquidity=6266958.0 spike=0.72
- NIPH.CA: score=15.44 buy_ready=False sector_rank=16 price=272.84 support=205.0 resistance=334.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=47.67 liquidity=118997912.0 spike=0.95
- OBRI.CA: score=11.22 buy_ready=False sector_rank=11 price=22.88 support=18.11 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=39.8 liquidity=8251889.0 spike=0.68
- OCDI.CA: score=13.21 buy_ready=False sector_rank=8 price=23.23 support=21.0 resistance=28.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=40.49 liquidity=12927355.0 spike=0.38
- OCPH.CA: score=5.88 buy_ready=False sector_rank=11 price=178.97 support=147.96 resistance=237.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=37.3 liquidity=918903.56 spike=0.3
- ODIN.CA: score=16.68 buy_ready=False sector_rank=11 price=1.99 support=1.7 resistance=2.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=40.31 liquidity=11605427.0 spike=1.86
- OFH.CA: score=10.96 buy_ready=False sector_rank=11 price=0.7 support=0.61 resistance=0.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=34.67 liquidity=13417320.0 spike=0.59
- OIH.CA: score=12.4 buy_ready=False sector_rank=19 price=1.63 support=1.5 resistance=1.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=37.1 liquidity=14487562.0 spike=0.33
- OLFI.CA: score=7.5 buy_ready=False sector_rank=3 price=18.8 support=17.86 resistance=21.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:12 PM market time freshness=DELAYED_CURRENT RSI=29.72 liquidity=7484648.0 spike=0.64
- ORAS.CA: score=4.6 buy_ready=False sector_rank=6 price=794.0 support=783.0 resistance=800.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=204893456.0 spike=1.0
- ORHD.CA: score=5.85 buy_ready=False sector_rank=8 price=10.2 support=9.5 resistance=10.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=199924128.0 spike=1.82
- ORWE.CA: score=13.16 buy_ready=False sector_rank=18 price=24.93 support=22.2 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=36.26 liquidity=12006887.0 spike=0.33
- PHAR.CA: score=13.44 buy_ready=False sector_rank=16 price=98.25 support=90.2 resistance=118.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=36.86 liquidity=39831416.0 spike=0.79
- PHDC.CA: score=7.73 buy_ready=False sector_rank=8 price=11.5 support=10.51 resistance=11.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=241357744.0 spike=2.76
- PHTV.CA: score=7.92 buy_ready=False sector_rank=11 price=315.61 support=300.0 resistance=355.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=37.45 liquidity=2116719.75 spike=1.92
- POUL.CA: score=19.36 buy_ready=False sector_rank=3 price=9.99 support=8.81 resistance=10.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=74761520.0 spike=1.17
- PRCL.CA: score=19.78 buy_ready=False sector_rank=1 price=21.0 support=16.65 resistance=27.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=48.99 liquidity=14662156.0 spike=1.08
- PRDC.CA: score=15.21 buy_ready=False sector_rank=8 price=6.09 support=5.08 resistance=7.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=46.59 liquidity=10335697.0 spike=0.31
- PRMH.CA: score=0.17 buy_ready=False sector_rank=11 price=1.93 support=1.81 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4910929.0 spike=1.65
- RACC.CA: score=1.73 buy_ready=False sector_rank=11 price=7.74 support=6.9 resistance=7.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7530968.0 spike=1.12
- RAKT.CA: score=3.01 buy_ready=False sector_rank=11 price=22.35 support=20.4 resistance=25.08 source=Yahoo Finance as_of=2026-11-01T22:00:00+00:00 freshness=FRESH RSI=53.99 liquidity=42442.65 spike=0.1
- RAYA.CA: score=10.5 buy_ready=False sector_rank=15 price=5.23 support=5.02 resistance=6.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=33.65 liquidity=45086776.0 spike=2.51
- RMDA.CA: score=17.84 buy_ready=False sector_rank=16 price=5.12 support=4.5 resistance=5.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.55 liquidity=28109518.0 spike=1.2
- ROTO.CA: score=3.37 buy_ready=False sector_rank=11 price=30.41 support=25.0 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=27.92 liquidity=5407142.0 spike=0.74
- RREI.CA: score=4.75 buy_ready=False sector_rank=11 price=2.67 support=1.96 resistance=4.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=30.0 liquidity=6785726.0 spike=0.62
- RTVC.CA: score=-1.44 buy_ready=False sector_rank=11 price=2.74 support=2.68 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=18.35 liquidity=594091.38 spike=0.21
- RUBX.CA: score=13.96 buy_ready=False sector_rank=11 price=12.81 support=10.51 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=36.29 liquidity=55823056.0 spike=0.66
- SAUD.CA: score=8.83 buy_ready=False sector_rank=5 price=19.98 support=19.3 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=35.74 liquidity=5089679.5 spike=0.46
- SCEM.CA: score=22.62 buy_ready=False sector_rank=1 price=88.04 support=73.9 resistance=95.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=54.34 liquidity=30284620.0 spike=0.57
- SCFM.CA: score=12.44 buy_ready=False sector_rank=11 price=211.8 support=153.02 resistance=252.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=40.5 liquidity=4613364.0 spike=2.43
- SCTS.CA: score=9.01 buy_ready=False sector_rank=13 price=491.65 support=410.0 resistance=588.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=45.78 liquidity=3165861.0 spike=0.73
- SDTI.CA: score=7.22 buy_ready=False sector_rank=11 price=86.07 support=81.55 resistance=87.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=43936964.0 spike=2.63
- SEIG.CA: score=8.96 buy_ready=False sector_rank=11 price=266.15 support=246.0 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=44774904.0 spike=7.81
- SIPC.CA: score=13.96 buy_ready=False sector_rank=11 price=4.56 support=3.73 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=40.77 liquidity=17012442.0 spike=0.29
- SKPC.CA: score=14.49 buy_ready=False sector_rank=14 price=14.42 support=14.01 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.65 liquidity=33201694.0 spike=0.63
- SMFR.CA: score=5.2 buy_ready=False sector_rank=11 price=186.03 support=165.0 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=35.22 liquidity=2231640.0 spike=0.82
- SNFC.CA: score=9.32 buy_ready=False sector_rank=11 price=10.6 support=10.08 resistance=11.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=39.91 liquidity=6352130.5 spike=0.84
- SPIN.CA: score=7.53 buy_ready=False sector_rank=18 price=14.52 support=12.0 resistance=17.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=41.11 liquidity=3376760.0 spike=0.63
- SPMD.CA: score=9.13 buy_ready=False sector_rank=11 price=0.34 support=0.3 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=4164847.75 spike=0.29
- SUGR.CA: score=18.06 buy_ready=False sector_rank=3 price=47.31 support=44.62 resistance=54.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=48.42 liquidity=16927432.0 spike=2.02
- SVCE.CA: score=14.96 buy_ready=False sector_rank=11 price=8.45 support=7.01 resistance=10.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.07 liquidity=24989348.0 spike=0.47
- SWDY.CA: score=16.07 buy_ready=False sector_rank=9 price=108.51 support=97.0 resistance=121.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=46.86 liquidity=34416748.0 spike=0.69
- TALM.CA: score=9.72 buy_ready=False sector_rank=13 price=19.15 support=17.0 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=25.32 liquidity=37538036.0 spike=1.44
- TMGH.CA: score=13.21 buy_ready=False sector_rank=8 price=79.53 support=76.5 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.94 liquidity=194675536.0 spike=0.76
- TRTO.CA: score=-1.03 buy_ready=False sector_rank=11 price=0.05 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-11-01T22:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=4468.47 spike=0.62
- UEFM.CA: score=5.94 buy_ready=False sector_rank=11 price=440.36 support=422.0 resistance=528.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:11 PM market time freshness=DELAYED_CURRENT RSI=23.58 liquidity=4935387.5 spike=2.52
- UEGC.CA: score=14.96 buy_ready=False sector_rank=11 price=1.42 support=1.21 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.57 liquidity=36058500.0 spike=0.79
- UNIP.CA: score=7.77 buy_ready=False sector_rank=11 price=0.28 support=0.25 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=37.93 liquidity=4804665.5 spike=0.64
- UNIT.CA: score=14.59 buy_ready=False sector_rank=8 price=18.01 support=15.06 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=56.7 liquidity=3282453.75 spike=1.05
- WCDF.CA: score=0.89 buy_ready=False sector_rank=11 price=492.15 support=432.5 resistance=630.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:11 PM market time freshness=DELAYED_CURRENT RSI=32.62 liquidity=926700.94 spike=0.52
- WKOL.CA: score=13.84 buy_ready=False sector_rank=11 price=247.8 support=218.0 resistance=309.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=35.22 liquidity=10142625.0 spike=1.44
- ZEOT.CA: score=8.72 buy_ready=False sector_rank=11 price=10.27 support=8.0 resistance=13.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=49.87 liquidity=3751675.25 spike=0.52
- ZMID.CA: score=16.67 buy_ready=False sector_rank=8 price=6.65 support=5.91 resistance=7.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.92 liquidity=82947048.0 spike=1.23

## Backtesting Lite
- EMFD.CA: 180d return=25.34%, max drawdown=-22.82%, MA20>MA50 days last20=7, as_of=2026-11-01T22:00:00+00:00
- SCEM.CA: 180d return=35.65%, max drawdown=-29.64%, MA20>MA50 days last20=0, as_of=2026-11-01T22:00:00+00:00
- JUFO.CA: 180d return=-25.93%, max drawdown=-33.71%, MA20>MA50 days last20=0, as_of=2026-11-01T22:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- EMFD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=671 sources=3 expected=Emaar Misr for Development summary=Emaar Misr posts higher revenues at EGP 19.8bn in 2025; Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25; Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea
  - Emaar Misr posts higher revenues at EGP 19.8bn in 2025: https://english.mubasher.info/news/4561643/Emaar-Misr-posts-higher-revenues-at-EGP-19-8bn-in-2025/
  - Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25: https://english.mubasher.info/news/4525192/Emaar-Misr-s-consolidated-net-profits-drop-to-EGP-4-2bn-in-9M-25/
  - Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea: https://english.mubasher.info/news/4495287/Emaar-Misr-Golden-Coast-to-establish-EGP-900bn-project-in-Red-Sea/
- SCEM.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=671 sources=3 expected=Sinai Cement summary=Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn; Upward trend line ends several-day decline for Sinai Cement stock; Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25
  - Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn: https://english.mubasher.info/news/4564824/Sinai-Cement-s-consolidated-profits-fall-in-2025-net-sales-cross-EGP-9bn/
  - Upward trend line ends several-day decline for Sinai Cement stock: https://english.mubasher.info/news/4529647/Upward-trend-line-ends-several-day-decline-for-Sinai-Cement-stock/
  - Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25: https://english.mubasher.info/news/4526073/Sinai-Cement-reports-lower-consolidated-net-profits-at-EGP-1-5bn-in-9M-25/
- JUFO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Juhayna Food Industries summary=Evidence rejected for JUFO.CA: source text did not clearly match JUFO.CA / Juhayna Food Industries.
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- PRCL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Ceramic and Porcelain summary=Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- MCQE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=671 sources=3 expected=Misr Cement Qena summary=Misr Cement to distribute EGP 10/shr dividends for 2025; Misr Cement stock is testing technical level ahead of historical peak – Analysis; Misr Cement witnesses 3,254% remarkable jump in 9M-25 consolidated net profits
  - Misr Cement to distribute EGP 10/shr dividends for 2025: https://english.mubasher.info/news/4586191/Misr-Cement-to-distribute-EGP-10-shr-dividends-for-2025/
  - Misr Cement stock is testing technical level ahead of historical peak – Analysis: https://english.mubasher.info/news/4560306/Misr-Cement-stock-is-testing-technical-level-ahead-of-historical-peak-Analysis/
  - Misr Cement witnesses 3,254% remarkable jump in 9M-25 consolidated net profits: https://english.mubasher.info/news/4524754/Misr-Cement-witnesses-3-254-remarkable-jump-in-9M-25-consolidated-net-profits/
- GTWL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Golden Textiles & Clothes Wool summary=Golden Textiles profits jump 214%; Golden Textiles OGM OKs 50 piasters/shr dividends; Golden Textiles consolidated profits down 18.5% in FY16
  - Golden Textiles profits jump 214%: https://english.mubasher.info/news/3108548/Golden-Textiles-profits-jump-214-/
  - Golden Textiles OGM OKs 50 piasters/shr dividends: https://english.mubasher.info/news/3103061/Golden-Textiles-OGM-OKs-50-piasters-shr-dividends/
  - Golden Textiles consolidated profits down 18.5% in FY16: https://english.mubasher.info/news/3092552/Golden-Textiles-consolidated-profits-down-18-5-in-FY16/
- POUL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Poultry summary=Cairo Poultry stock approaching historic peak – Analysis; Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA; Cairo Poultry sees EGP 871m block-trading deal
  - Cairo Poultry stock approaching historic peak – Analysis: https://english.mubasher.info/news/4539104/Cairo-Poultry-stock-approaching-historic-peak-Analysis/
  - Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA: https://english.mubasher.info/news/3962334/Cairo-Poultry-cancels-commercial-license-in-Dubai-s-JAFZA/
  - Cairo Poultry sees EGP 871m block-trading deal: https://english.mubasher.info/news/3862165/Cairo-Poultry-sees-EGP-871m-block-trading-deal/

## Warnings
- OpenRouter API error: 404
- Evidence for EMFD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for SCEM.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for JUFO.CA: source text did not clearly match JUFO.CA / Juhayna Food Industries.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- Evidence for MCQE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for GTWL.CA matches the company but no source/report date was detected.
- Evidence for POUL.CA matches the company but no source/report date was detected.
