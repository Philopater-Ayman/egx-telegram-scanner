# Telegram-First EGX Scanner Report

Scan phase: Evening tomorrow plan
Generated UTC: 2026-06-29T18:31:05.903306+00:00
Generated Cairo: 2026-06-29 21:31
Run timing: target 19:30 Cairo | generated Cairo 2026-06-29 21:31 | cron 30 16 * * 0-4
Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-06-29 21:28

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 180/190
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, June 29
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 15.0% / above MA50 25.0%
- EGX70 regime: BEARISH / above MA20 32.5% / above MA50 55.0%
- Sector breadth: 9.52%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=666172352.0 spike=1.17 score=14.61
- CCAP.CA: liquidity=237804304.0 spike=0.35 score=8.76
- ORAS.CA: liquidity=235850560.0 spike=1.0 score=4.6
- TMGH.CA: liquidity=209350784.0 spike=0.53 score=14.92
- PHDC.CA: liquidity=168717632.0 spike=0.41 score=17.92

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The local scanner kept all tickets on HOLD because the EGX30 and EGX70 are in a bearish regime with weak breadth (≈9.5%). Defensive risk mode (NO_NEW_BUY) is active, so even stocks with constructive or bullish‑watch outlooks are not recommended for entry. Liquidity spikes and support/resistance levels suggest short‑term price stability, but sector breadth is low and the overall market outlook remains uncertain for the next 1‑3 days.
- EGX30/EGX70 trends are bearish; median 5‑day returns around –3.5% and only ~15‑33% of stocks sit above MA20, limiting market support.
- Top tickets (RUBX, MHOT, CPCI, CSAG, LCSW, POUL, OCPH, CLHO) show decent liquidity spikes and clear 20‑day support, but RSI extremes or non‑leading sectors keep risk flags high.
- Tourism & Leisure leads sector breadth (100% above MA20/50) but overall sector breadth is under 10%, reinforcing the defensive stance.
- Risk mode DEFENSIVE_NO_NEW_BUY means the scanner blocks new buys until market breadth improves; existing positions may be held but no fresh entries are advised.
- Uncertainty remains high: potential short‑term rebounds exist, yet the bearish macro backdrop and weak market breadth could trigger further downside in the next 1‑3 days.

## Top Liquidity Spikes
- AMES.CA: spike=12.36 liquidity=33500140.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DTPP.CA: spike=8.76 liquidity=12713925.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GTWL.CA: spike=6.43 liquidity=119999120.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CPCI.CA: spike=5.96 liquidity=11283094.0 outlook=BULLISH_WATCH score=83.07 buy_ready=False
- RUBX.CA: spike=4.5 liquidity=68097336.0 outlook=CONSTRUCTIVE score=69.07 buy_ready=False

## Sector Leaderboard
- #1 Tourism & Leisure: score=9.49 5d=2.1% 20d=8.17% aboveMA50=100.0%
- #2 Automotive & Distribution: score=7.49 5d=1.75% 20d=7.28% aboveMA50=50.0%
- #3 Transportation & Logistics: score=3.92 5d=-0.49% 20d=-1.76% aboveMA50=50.0%
- #4 Food, Beverages & Tobacco: score=2.82 5d=-3.6% 20d=0.24% aboveMA50=57.14%
- #5 Real Estate: score=2.29 5d=-4.04% 20d=1.47% aboveMA50=76.92%
- #6 Technology & Distribution: score=1.59 5d=-4.17% 20d=-4.81% aboveMA50=100.0%
- #7 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #8 Education: score=1.23 5d=-3.76% 20d=0.84% aboveMA50=33.33%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MHOT.CA: BULLISH_WATCH score=89.49 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- CSAG.CA: BULLISH_WATCH score=88.92 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- LCSW.CA: BULLISH_WATCH score=88.54 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- POUL.CA: BULLISH_WATCH score=83.82 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- CPCI.CA: BULLISH_WATCH score=83.07 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- MENA.CA: BULLISH_WATCH score=78.29 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- OLFI.CA: BULLISH_WATCH score=77.82 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- MFSC.CA: BULLISH_WATCH score=72.07 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- CNFN.CA: BULLISH_WATCH score=71.99 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- MTIE.CA: BULLISH_WATCH score=70.49 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=below MA20; below MA50

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=17.23 buy_ready=False sector_rank=11 price=202.0 support=196.0 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.98 liquidity=13740386.0 spike=2.4
- ABUK.CA: score=8.22 buy_ready=False sector_rank=20 price=66.96 support=67.69 resistance=84.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=9.15 liquidity=67650088.0 spike=0.5
- ACAMD.CA: score=17.43 buy_ready=False sector_rank=11 price=2.2 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.18 liquidity=66905392.0 spike=0.55
- ACGC.CA: score=14.38 buy_ready=False sector_rank=13 price=9.15 support=9.11 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.76 liquidity=14032849.0 spike=0.33
- ADCI.CA: score=19.37 buy_ready=False sector_rank=11 price=243.76 support=211.0 resistance=244.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=84.03 liquidity=22684720.0 spike=2.47
- ADIB.CA: score=14.27 buy_ready=False sector_rank=14 price=44.97 support=44.01 resistance=48.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.59 liquidity=31802828.0 spike=0.33
- ADPC.CA: score=13.43 buy_ready=False sector_rank=11 price=3.37 support=3.38 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=10212411.0 spike=0.45
- AFDI.CA: score=14.17 buy_ready=False sector_rank=11 price=42.36 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=46.07 liquidity=6737157.0 spike=0.44
- AFMC.CA: score=0.14 buy_ready=False sector_rank=11 price=67.39 support=66.66 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=29.03 liquidity=715486.63 spike=0.28
- AJWA.CA: score=11.82 buy_ready=False sector_rank=11 price=175.73 support=131.5 resistance=188.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=83.3 liquidity=5390474.0 spike=0.2
- ALCN.CA: score=8.94 buy_ready=False sector_rank=3 price=27.7 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=32.2 liquidity=7375432.0 spike=0.59
- ALUM.CA: score=3.11 buy_ready=False sector_rank=11 price=20.77 support=20.55 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=16.11 liquidity=3683697.75 spike=0.38
- AMER.CA: score=9.92 buy_ready=False sector_rank=5 price=2.32 support=2.3 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.56 liquidity=25521592.0 spike=0.34
- AMES.CA: score=9.43 buy_ready=False sector_rank=11 price=55.28 support=45.15 resistance=55.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33500140.0 spike=12.36
- AMIA.CA: score=8.65 buy_ready=False sector_rank=11 price=8.48 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.81 liquidity=4224105.0 spike=0.31
- AMOC.CA: score=9.44 buy_ready=False sector_rank=10 price=7.52 support=7.42 resistance=8.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=10.0 liquidity=22473004.0 spike=0.45
- ANFI.CA: score=5.76 buy_ready=False sector_rank=11 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=STALE RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=6.67 buy_ready=False sector_rank=11 price=8.01 support=8.24 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=12.5 liquidity=3237114.0 spike=4.16
- ARAB.CA: score=14.92 buy_ready=False sector_rank=5 price=0.21 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.88 liquidity=63758780.0 spike=0.75
- ARCC.CA: score=9.22 buy_ready=False sector_rank=15 price=53.76 support=53.0 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.02 liquidity=15072464.0 spike=0.44
- AREH.CA: score=19.43 buy_ready=False sector_rank=11 price=1.53 support=1.32 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=54.39 liquidity=13436781.0 spike=0.39
- ARVA.CA: score=17.43 buy_ready=False sector_rank=11 price=10.9 support=8.2 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.55 liquidity=16935618.0 spike=0.53
- ASCM.CA: score=19.43 buy_ready=False sector_rank=11 price=57.56 support=47.5 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.76 liquidity=46590980.0 spike=0.51
- ASPI.CA: score=10.4 buy_ready=False sector_rank=11 price=0.3 support=0.27 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.92 liquidity=6972374.0 spike=0.1
- ATLC.CA: score=8.85 buy_ready=False sector_rank=12 price=4.99 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=49.44 liquidity=1455190.5 spike=0.23
- ATQA.CA: score=12.22 buy_ready=False sector_rank=20 price=9.38 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.31 liquidity=15436175.0 spike=0.47
- AXPH.CA: score=6.13 buy_ready=False sector_rank=11 price=1117.31 support=1073.0 resistance=1174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=31.18 liquidity=1562786.38 spike=1.07
- BINV.CA: score=9.16 buy_ready=False sector_rank=19 price=45.09 support=42.97 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.05 liquidity=2392821.0 spike=0.23
- BIOC.CA: score=1.55 buy_ready=False sector_rank=11 price=68.17 support=66.75 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=31.39 liquidity=2123255.25 spike=0.86
- BTFH.CA: score=13.4 buy_ready=False sector_rank=12 price=2.98 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=122593120.0 spike=0.65
- CAED.CA: score=8.74 buy_ready=False sector_rank=11 price=70.46 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.65 liquidity=1314990.88 spike=0.26
- CANA.CA: score=2.2 buy_ready=False sector_rank=14 price=35.28 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=31.12 liquidity=3928645.0 spike=0.36
- CCAP.CA: score=8.76 buy_ready=False sector_rank=19 price=4.72 support=4.72 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.05 liquidity=237804304.0 spike=0.35
- CCRS.CA: score=14.43 buy_ready=False sector_rank=11 price=2.22 support=2.28 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.09 liquidity=14688432.0 spike=0.84
- CEFM.CA: score=1.44 buy_ready=False sector_rank=11 price=96.96 support=98.0 resistance=109.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=20.82 liquidity=2312191.75 spike=1.35
- CERA.CA: score=12.12 buy_ready=False sector_rank=11 price=1.2 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=53.85 liquidity=5693854.5 spike=0.34
- CFGH.CA: score=-0.2 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=11200.0 spike=1.68
- CICH.CA: score=8.32 buy_ready=False sector_rank=12 price=11.76 support=11.1 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=46.3 liquidity=1920740.25 spike=0.59
- CIEB.CA: score=12.31 buy_ready=False sector_rank=14 price=23.31 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.09 liquidity=7657778.0 spike=1.19
- CIRA.CA: score=16.28 buy_ready=False sector_rank=8 price=27.84 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=62.1 liquidity=6790902.0 spike=0.38
- CLHO.CA: score=21.58 buy_ready=False sector_rank=18 price=16.16 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.84 liquidity=45426888.0 spike=1.29
- CNFN.CA: score=21.4 buy_ready=False sector_rank=12 price=4.68 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.53 liquidity=16392221.0 spike=0.4
- COMI.CA: score=14.61 buy_ready=False sector_rank=14 price=126.57 support=129.8 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.33 liquidity=666172352.0 spike=1.17
- COPR.CA: score=16.43 buy_ready=False sector_rank=11 price=0.35 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.85 liquidity=13713672.0 spike=0.47
- COSG.CA: score=9.43 buy_ready=False sector_rank=11 price=1.5 support=1.48 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=29.73 liquidity=20409364.0 spike=0.38
- CPCI.CA: score=24.43 buy_ready=False sector_rank=11 price=388.12 support=347.11 resistance=378.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.92 liquidity=11283094.0 spike=5.96
- CSAG.CA: score=24.29 buy_ready=False sector_rank=3 price=32.26 support=30.08 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=60.25 liquidity=21490544.0 spike=1.36
- DAPH.CA: score=10.46 buy_ready=False sector_rank=11 price=80.48 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.51 liquidity=4031708.5 spike=0.39
- DEIN.CA: score=5.43 buy_ready=False sector_rank=11 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=13.29 buy_ready=False sector_rank=4 price=26.86 support=23.7 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=70.0 liquidity=3158584.75 spike=0.81
- DSCW.CA: score=13.43 buy_ready=False sector_rank=11 price=1.72 support=1.71 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.11 liquidity=13534408.0 spike=0.35
- DTPP.CA: score=9.43 buy_ready=False sector_rank=11 price=138.38 support=120.0 resistance=138.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12713925.0 spike=8.76
- EALR.CA: score=6.69 buy_ready=False sector_rank=11 price=341.31 support=332.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.22 liquidity=2263212.0 spike=0.72
- EASB.CA: score=21.57 buy_ready=False sector_rank=11 price=7.55 support=4.66 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=74.07 liquidity=24335240.0 spike=2.07
- EAST.CA: score=14.13 buy_ready=False sector_rank=4 price=37.0 support=37.0 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=36.67 liquidity=29655956.0 spike=0.73
- EBSC.CA: score=5.03 buy_ready=False sector_rank=11 price=1.74 support=1.66 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=599608.56 spike=0.22
- ECAP.CA: score=13.74 buy_ready=False sector_rank=11 price=31.95 support=29.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=55.96 liquidity=6308879.0 spike=0.72
- EDFM.CA: score=-0.3 buy_ready=False sector_rank=11 price=330.59 support=320.29 resistance=355.0 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=26.96 liquidity=272406.16 spike=0.51
- EEII.CA: score=9.35 buy_ready=False sector_rank=11 price=2.36 support=2.3 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.07 liquidity=4923096.5 spike=0.36
- EFIC.CA: score=-1.82 buy_ready=False sector_rank=20 price=189.13 support=192.0 resistance=213.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=13.84 liquidity=962186.31 spike=0.5
- EFID.CA: score=10.59 buy_ready=False sector_rank=4 price=27.08 support=25.5 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=25.19 liquidity=90898728.0 spike=1.23
- EFIH.CA: score=12.89 buy_ready=False sector_rank=21 price=20.22 support=20.0 resistance=22.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.16 liquidity=14849094.0 spike=0.33
- EGAL.CA: score=8.22 buy_ready=False sector_rank=20 price=274.38 support=273.1 resistance=334.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=10.52 liquidity=21278610.0 spike=0.32
- EGAS.CA: score=10.22 buy_ready=False sector_rank=10 price=48.42 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.34 liquidity=2776260.75 spike=0.29
- EGBE.CA: score=11.36 buy_ready=False sector_rank=14 price=0.45 support=0.43 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=52.31 liquidity=89810.06 spike=0.97
- EGCH.CA: score=8.22 buy_ready=False sector_rank=20 price=12.16 support=12.15 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.54 liquidity=24797218.0 spike=0.45
- EGSA.CA: score=7.21 buy_ready=False sector_rank=16 price=8.75 support=8.55 resistance=9.1 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=36.0 liquidity=1767.5 spike=0.19
- EGTS.CA: score=17.92 buy_ready=False sector_rank=5 price=16.98 support=16.11 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.49 liquidity=24575364.0 spike=0.27
- EHDR.CA: score=17.43 buy_ready=False sector_rank=11 price=2.41 support=2.27 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=20596914.0 spike=0.36
- EKHO.CA: score=9.44 buy_ready=False sector_rank=10 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=13.03 buy_ready=False sector_rank=17 price=2.06 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.74 liquidity=16933066.0 spike=0.87
- ELKA.CA: score=16.43 buy_ready=False sector_rank=11 price=1.2 support=1.16 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=13579502.0 spike=0.34
- ELNA.CA: score=-1.15 buy_ready=False sector_rank=11 price=36.03 support=35.55 resistance=41.51 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=33.43 liquidity=425190.02 spike=1.0
- ELSH.CA: score=12.43 buy_ready=False sector_rank=11 price=11.59 support=8.29 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.95 liquidity=43550380.0 spike=0.23
- ELWA.CA: score=8.28 buy_ready=False sector_rank=11 price=1.97 support=2.0 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=851030.19 spike=0.27
- EMFD.CA: score=17.92 buy_ready=False sector_rank=5 price=11.46 support=10.8 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.44 liquidity=41161956.0 spike=0.14
- ENGC.CA: score=21.43 buy_ready=False sector_rank=11 price=36.39 support=32.9 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=63.41 liquidity=11626116.0 spike=0.82
- EOSB.CA: score=11.49 buy_ready=False sector_rank=11 price=1.48 support=1.35 resistance=1.55 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=65744.56 spike=0.49
- EPCO.CA: score=7.56 buy_ready=False sector_rank=11 price=8.56 support=8.69 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.82 liquidity=3134987.5 spike=0.35
- EPPK.CA: score=13.74 buy_ready=False sector_rank=11 price=13.03 support=11.67 resistance=13.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=62.62 liquidity=312988.0 spike=0.28
- ETEL.CA: score=14.2 buy_ready=False sector_rank=16 price=90.34 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.04 liquidity=41868468.0 spike=0.57
- ETRS.CA: score=19.43 buy_ready=False sector_rank=11 price=10.35 support=8.01 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.32 liquidity=29402854.0 spike=0.4
- EXPA.CA: score=9.27 buy_ready=False sector_rank=14 price=18.15 support=18.03 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.55 liquidity=22107360.0 spike=0.69
- FAIT.CA: score=3.94 buy_ready=False sector_rank=14 price=35.91 support=35.01 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.38 liquidity=1667933.38 spike=0.54
- FAITA.CA: score=4.31 buy_ready=False sector_rank=14 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=34943.84 spike=0.89
- FERC.CA: score=2.19 buy_ready=False sector_rank=20 price=72.96 support=74.0 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=16.06 liquidity=4525645.5 spike=1.22
- FWRY.CA: score=12.89 buy_ready=False sector_rank=21 price=18.3 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.05 liquidity=70136600.0 spike=0.28
- GBCO.CA: score=20.92 buy_ready=False sector_rank=2 price=31.05 support=25.25 resistance=31.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=85.94 liquidity=112922976.0 spike=1.26
- GDWA.CA: score=4.56 buy_ready=False sector_rank=11 price=0.77 support=0.76 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=29.32 liquidity=6128143.5 spike=0.44
- GGCC.CA: score=21.03 buy_ready=False sector_rank=11 price=0.46 support=0.4 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=14077092.0 spike=1.3
- GIHD.CA: score=11.73 buy_ready=False sector_rank=11 price=40.99 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.38 liquidity=5298055.5 spike=0.66
- GMCI.CA: score=13.45 buy_ready=False sector_rank=11 price=1.77 support=1.66 resistance=1.84 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=48.39 liquidity=941578.04 spike=2.54
- GRCA.CA: score=7.23 buy_ready=False sector_rank=11 price=52.78 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.41 liquidity=2804230.0 spike=0.63
- GSSC.CA: score=0.41 buy_ready=False sector_rank=11 price=241.29 support=228.1 resistance=257.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=27.12 liquidity=1986251.5 spike=0.63
- GTWL.CA: score=9.43 buy_ready=False sector_rank=11 price=73.5 support=60.3 resistance=73.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=119999120.0 spike=6.43
- HDBK.CA: score=21.27 buy_ready=False sector_rank=14 price=154.02 support=138.0 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.41 liquidity=27407344.0 spike=1.0
- HELI.CA: score=17.92 buy_ready=False sector_rank=5 price=6.4 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.61 liquidity=44819872.0 spike=0.37
- HRHO.CA: score=15.4 buy_ready=False sector_rank=12 price=26.52 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=53.83 liquidity=46533680.0 spike=0.33
- ICID.CA: score=11.04 buy_ready=False sector_rank=11 price=7.59 support=5.0 resistance=8.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=73.78 liquidity=1610829.13 spike=0.1
- IDRE.CA: score=10.42 buy_ready=False sector_rank=11 price=41.6 support=42.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=41.92 liquidity=5988692.5 spike=0.38
- IFAP.CA: score=11.3 buy_ready=False sector_rank=9 price=19.03 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=49.12 liquidity=5816338.0 spike=0.88
- INFI.CA: score=1.92 buy_ready=False sector_rank=11 price=88.63 support=89.0 resistance=105.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=14.52 liquidity=3489176.0 spike=0.47
- IRON.CA: score=11.5 buy_ready=False sector_rank=20 price=32.31 support=30.75 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=28.36 liquidity=15387628.0 spike=2.14
- ISMA.CA: score=16.71 buy_ready=False sector_rank=11 price=28.99 support=25.95 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.23 liquidity=9285575.0 spike=0.24
- ISMQ.CA: score=20.94 buy_ready=False sector_rank=20 price=9.1 support=7.39 resistance=9.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.06 liquidity=147063952.0 spike=1.36
- ISPH.CA: score=9.0 buy_ready=False sector_rank=18 price=11.39 support=11.2 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.51 liquidity=30043254.0 spike=0.26
- JUFO.CA: score=18.13 buy_ready=False sector_rank=4 price=29.25 support=28.1 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.21 liquidity=14096992.0 spike=0.41
- KABO.CA: score=17.7 buy_ready=False sector_rank=13 price=6.26 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=41.43 liquidity=18324816.0 spike=1.16
- KWIN.CA: score=15.31 buy_ready=False sector_rank=11 price=67.53 support=65.75 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.59 liquidity=20640390.0 spike=1.94
- KZPC.CA: score=0.04 buy_ready=False sector_rank=11 price=8.4 support=8.35 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=14.05 liquidity=1615988.13 spike=0.25
- LCSW.CA: score=22.74 buy_ready=False sector_rank=15 price=27.53 support=26.0 resistance=31.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.03 liquidity=47262280.0 spike=1.76
- LUTS.CA: score=19.43 buy_ready=False sector_rank=11 price=0.72 support=0.55 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.35 liquidity=29617860.0 spike=0.67
- MAAL.CA: score=18.43 buy_ready=False sector_rank=11 price=7.11 support=5.24 resistance=7.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=78.13 liquidity=13429897.0 spike=0.76
- MASR.CA: score=6.59 buy_ready=False sector_rank=11 price=7.18 support=6.82 resistance=7.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=110931128.0 spike=2.08
- MBSC.CA: score=9.22 buy_ready=False sector_rank=15 price=229.86 support=228.11 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=11.36 liquidity=24328406.0 spike=0.69
- MCQE.CA: score=4.71 buy_ready=False sector_rank=15 price=168.76 support=166.66 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=20.75 liquidity=5489076.5 spike=0.34
- MCRO.CA: score=8.43 buy_ready=False sector_rank=11 price=1.19 support=1.18 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=23643748.0 spike=0.66
- MENA.CA: score=12.79 buy_ready=False sector_rank=5 price=6.82 support=6.22 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.54 liquidity=2875888.0 spike=0.22
- MEPA.CA: score=2.99 buy_ready=False sector_rank=11 price=1.54 support=1.52 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=17.24 liquidity=4566867.0 spike=0.39
- MFPC.CA: score=8.22 buy_ready=False sector_rank=20 price=34.52 support=34.22 resistance=43.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=5.78 liquidity=55178752.0 spike=0.64
- MFSC.CA: score=16.65 buy_ready=False sector_rank=11 price=47.33 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=54.08 liquidity=5224766.5 spike=0.59
- MHOT.CA: score=26.4 buy_ready=False sector_rank=1 price=33.99 support=28.83 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.67 liquidity=15511330.0 spike=0.68
- MICH.CA: score=11.56 buy_ready=False sector_rank=11 price=36.21 support=35.4 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.14 liquidity=4135058.0 spike=0.27
- MILS.CA: score=7.18 buy_ready=False sector_rank=11 price=127.26 support=128.06 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.55 liquidity=2750132.5 spike=0.28
- MIPH.CA: score=5.36 buy_ready=False sector_rank=18 price=651.64 support=630.13 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=38.59 liquidity=1362901.88 spike=0.7
- MOED.CA: score=7.1 buy_ready=False sector_rank=11 price=0.65 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.68 liquidity=1673733.62 spike=0.17
- MOIL.CA: score=5.36 buy_ready=False sector_rank=10 price=0.46 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.51 liquidity=258301.23 spike=1.33
- MOIN.CA: score=-1.38 buy_ready=False sector_rank=11 price=23.03 support=22.6 resistance=25.66 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=1.0 liquidity=187901.78 spike=0.29
- MOSC.CA: score=7.59 buy_ready=False sector_rank=11 price=284.78 support=250.55 resistance=298.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21829214.0 spike=2.58
- MPCI.CA: score=4.53 buy_ready=False sector_rank=11 price=236.57 support=223.51 resistance=243.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=98484848.0 spike=1.05
- MPCO.CA: score=16.48 buy_ready=False sector_rank=9 price=1.73 support=1.58 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=40397884.0 spike=0.38
- MPRC.CA: score=19.43 buy_ready=False sector_rank=11 price=38.21 support=31.15 resistance=40.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.69 liquidity=30674788.0 spike=0.73
- MTIE.CA: score=20.1 buy_ready=False sector_rank=2 price=8.9 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.15 liquidity=28572936.0 spike=1.85
- NAHO.CA: score=9.2 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=94711.1 spike=2.84
- NCCW.CA: score=17.08 buy_ready=False sector_rank=11 price=5.93 support=5.29 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.78 liquidity=9652277.0 spike=0.29
- NEDA.CA: score=-0.27 buy_ready=False sector_rank=11 price=2.74 support=2.68 resistance=2.84 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=33.33 liquidity=298218.86 spike=0.79
- NHPS.CA: score=4.24 buy_ready=False sector_rank=11 price=62.1 support=61.62 resistance=68.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.84 liquidity=812983.75 spike=0.23
- NINH.CA: score=11.1 buy_ready=False sector_rank=11 price=17.84 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.35 liquidity=2670295.75 spike=0.64
- NIPH.CA: score=12.12 buy_ready=False sector_rank=18 price=162.04 support=157.05 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=30.86 liquidity=71723232.0 spike=1.06
- OBRI.CA: score=14.43 buy_ready=False sector_rank=11 price=32.19 support=31.5 resistance=37.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.18 liquidity=10522209.0 spike=0.76
- OCDI.CA: score=19.92 buy_ready=False sector_rank=5 price=24.3 support=20.0 resistance=25.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=70.5 liquidity=60847600.0 spike=0.82
- OCPH.CA: score=21.93 buy_ready=False sector_rank=11 price=351.18 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=36.03 liquidity=13193336.0 spike=2.25
- ODIN.CA: score=9.79 buy_ready=False sector_rank=11 price=2.07 support=1.92 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=51.67 liquidity=2362597.75 spike=0.21
- OFH.CA: score=6.13 buy_ready=False sector_rank=11 price=0.58 support=0.58 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.89 liquidity=7705899.0 spike=0.4
- OIH.CA: score=15.76 buy_ready=False sector_rank=19 price=1.4 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=31986766.0 spike=0.4
- OLFI.CA: score=20.13 buy_ready=False sector_rank=4 price=22.0 support=21.1 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.31 liquidity=19701814.0 spike=0.98
- ORAS.CA: score=4.6 buy_ready=False sector_rank=7 price=702.89 support=695.0 resistance=718.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=235850560.0 spike=1.0
- ORHD.CA: score=17.92 buy_ready=False sector_rank=5 price=37.65 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.12 liquidity=109837024.0 spike=0.61
- ORWE.CA: score=9.38 buy_ready=False sector_rank=13 price=22.15 support=22.07 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.23 liquidity=14828325.0 spike=0.41
- PHAR.CA: score=10.67 buy_ready=False sector_rank=18 price=84.69 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.94 liquidity=4671665.0 spike=0.14
- PHDC.CA: score=17.92 buy_ready=False sector_rank=5 price=14.67 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.18 liquidity=168717632.0 spike=0.41
- PHTV.CA: score=18.43 buy_ready=False sector_rank=11 price=270.0 support=201.55 resistance=259.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=89.5 liquidity=13207253.0 spike=0.9
- POUL.CA: score=22.13 buy_ready=False sector_rank=4 price=37.11 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=55.23 liquidity=36891604.0 spike=0.98
- PRCL.CA: score=19.22 buy_ready=False sector_rank=15 price=30.8 support=22.11 resistance=32.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=65.11 liquidity=21395366.0 spike=0.53
- PRDC.CA: score=19.92 buy_ready=False sector_rank=5 price=7.16 support=5.74 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=64.47 liquidity=76005728.0 spike=0.66
- PRMH.CA: score=12.43 buy_ready=False sector_rank=11 price=2.5 support=2.26 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.53 liquidity=12586849.0 spike=0.41
- RACC.CA: score=8.04 buy_ready=False sector_rank=11 price=9.54 support=9.38 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.84 liquidity=3612056.25 spike=0.38
- RAKT.CA: score=1.72 buy_ready=False sector_rank=11 price=22.43 support=22.0 resistance=24.1 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=30.46 liquidity=371620.25 spike=1.46
- RAYA.CA: score=17.64 buy_ready=False sector_rank=6 price=7.23 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.18 liquidity=67542872.0 spike=0.81
- RMDA.CA: score=9.0 buy_ready=False sector_rank=18 price=4.9 support=4.85 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.0 liquidity=16368153.0 spike=0.21
- ROTO.CA: score=21.43 buy_ready=False sector_rank=11 price=40.74 support=32.91 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=64.72 liquidity=23076948.0 spike=0.82
- RREI.CA: score=9.86 buy_ready=False sector_rank=11 price=3.4 support=3.34 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.96 liquidity=5433323.5 spike=0.31
- RTVC.CA: score=1.88 buy_ready=False sector_rank=11 price=3.65 support=3.61 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=26.67 liquidity=3449860.25 spike=0.68
- RUBX.CA: score=26.43 buy_ready=False sector_rank=11 price=11.3 support=9.8 resistance=12.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=74.26 liquidity=68097336.0 spike=4.5
- SAUD.CA: score=3.51 buy_ready=False sector_rank=14 price=20.43 support=19.99 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.03 liquidity=4239668.0 spike=0.49
- SCEM.CA: score=9.61 buy_ready=False sector_rank=15 price=60.96 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=40.78 liquidity=5394680.0 spike=0.3
- SCFM.CA: score=0.93 buy_ready=False sector_rank=11 price=237.01 support=226.5 resistance=276.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=20.69 liquidity=1501863.5 spike=0.31
- SCTS.CA: score=0.5 buy_ready=False sector_rank=8 price=542.29 support=540.0 resistance=630.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=20.92 liquidity=1004783.75 spike=0.31
- SDTI.CA: score=10.82 buy_ready=False sector_rank=11 price=46.02 support=44.03 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.61 liquidity=3392712.25 spike=0.29
- SEIG.CA: score=9.74 buy_ready=False sector_rank=11 price=183.92 support=180.0 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=40.65 liquidity=2315753.5 spike=0.57
- SIPC.CA: score=6.13 buy_ready=False sector_rank=11 price=3.26 support=3.35 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=26.67 liquidity=7702661.5 spike=0.67
- SKPC.CA: score=7.22 buy_ready=False sector_rank=20 price=15.89 support=15.64 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=20.87 liquidity=17337394.0 spike=0.48
- SMFR.CA: score=-0.09 buy_ready=False sector_rank=11 price=190.82 support=187.01 resistance=214.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=27.43 liquidity=486431.56 spike=0.22
- SNFC.CA: score=12.72 buy_ready=False sector_rank=11 price=12.04 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.46 liquidity=5287161.0 spike=0.29
- SPIN.CA: score=14.37 buy_ready=False sector_rank=13 price=14.2 support=13.3 resistance=14.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.58 liquidity=5990089.0 spike=0.98
- SPMD.CA: score=17.43 buy_ready=False sector_rank=11 price=0.41 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.68 liquidity=11688427.0 spike=0.49
- SUGR.CA: score=4.84 buy_ready=False sector_rank=4 price=46.05 support=46.25 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=23.45 liquidity=5713501.0 spike=0.74
- SVCE.CA: score=17.43 buy_ready=False sector_rank=11 price=8.85 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=53.11 liquidity=26109378.0 spike=0.39
- SWDY.CA: score=14.03 buy_ready=False sector_rank=17 price=85.01 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.75 liquidity=13666083.0 spike=0.8
- TALM.CA: score=8.18 buy_ready=False sector_rank=8 price=15.6 support=15.38 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.56 liquidity=3686449.25 spike=0.48
- TMGH.CA: score=14.92 buy_ready=False sector_rank=5 price=92.22 support=92.91 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.74 liquidity=209350784.0 spike=0.53
- TRTO.CA: score=5.43 buy_ready=False sector_rank=11 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=340.0 spike=0.45
- UEFM.CA: score=7.35 buy_ready=False sector_rank=11 price=470.0 support=460.0 resistance=505.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.83 liquidity=1306861.38 spike=1.31
- UEGC.CA: score=5.27 buy_ready=False sector_rank=11 price=1.36 support=1.32 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=5845800.5 spike=0.25
- UNIP.CA: score=5.39 buy_ready=False sector_rank=11 price=0.32 support=0.3 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33472932.0 spike=1.48
- UNIT.CA: score=4.31 buy_ready=False sector_rank=5 price=12.43 support=12.5 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=16.0 liquidity=1392799.5 spike=0.21
- WCDF.CA: score=5.32 buy_ready=False sector_rank=11 price=518.05 support=450.0 resistance=547.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=35.83 liquidity=396079.84 spike=1.25
- WKOL.CA: score=1.48 buy_ready=False sector_rank=11 price=280.06 support=273.1 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=27.71 liquidity=2049122.63 spike=0.74
- ZEOT.CA: score=9.43 buy_ready=False sector_rank=11 price=11.03 support=10.6 resistance=11.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=92514528.0 spike=3.5
- ZMID.CA: score=19.92 buy_ready=False sector_rank=5 price=6.2 support=5.82 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.03 liquidity=136774672.0 spike=0.65

## Backtesting Lite
- RUBX.CA: 180d return=12.72%, max drawdown=-21.39%, MA20>MA50 days last20=10, as_of=2026-06-27T21:00:00+00:00
- MHOT.CA: 180d return=36.21%, max drawdown=-15.7%, MA20>MA50 days last20=20, as_of=2026-06-27T21:00:00+00:00
- CPCI.CA: 180d return=66.33%, max drawdown=-9.98%, MA20>MA50 days last20=20, as_of=2026-06-27T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- RUBX.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Rubex International for Plastic and Acrylic Manufacturing summary=Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- MHOT.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Hotels summary=Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26; Shareholder buys EGP 3.39m worth of shares in Misr Hotels; Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits
  - Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26: https://english.mubasher.info/news/4602482/Misr-Hotels-net-profits-cross-EGP-1-1bn-in-9M-25-26/
  - Shareholder buys EGP 3.39m worth of shares in Misr Hotels: https://english.mubasher.info/news/4013808/Shareholder-buys-EGP-3-39m-worth-of-shares-in-Misr-Hotels/
  - Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits: https://english.mubasher.info/news/3975543/Misr-Hotels-repays-EGP-383m-of-NBE-s-loan-unveils-estimated-profits/
- CPCI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Kahira Pharmaceuticals & Chemical Industries Company summary=Kahira Pharmaceuticals&#39; net profits up 22.5% in H1-21/22; Kahira Pharmaceuticals sees EGP 9m block trading deal; Adel Taha Abdel Wahab named Chairman of Kahira Pharmaceuticals
  - Kahira Pharmaceuticals&#39; net profits up 22.5% in H1-21/22: https://english.mubasher.info/news/3910780/Kahira-Pharmaceuticals-net-profits-up-22-5-in-H1-21-22/
  - Kahira Pharmaceuticals sees EGP 9m block trading deal: https://english.mubasher.info/news/3903033/Kahira-Pharmaceuticals-sees-EGP-9m-block-trading-deal/
  - Adel Taha Abdel Wahab named Chairman of Kahira Pharmaceuticals: https://english.mubasher.info/news/3816375/Adel-Taha-Abdel-Wahab-named-Chairman-of-Kahira-Pharmaceuticals/
- CSAG.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Canal Shipping Agencies summary=Canal Shipping Agencies targets EGP 970m net profits in FY26/27; Canal Shipping Agencies’ stock rebounds; Canal Shipping Agencies mulls EGP 100m capital raise
  - Canal Shipping Agencies targets EGP 970m net profits in FY26/27: https://english.mubasher.info/news/4582423/Canal-Shipping-Agencies-targets-EGP-970m-net-profits-in-FY26-27/
  - Canal Shipping Agencies’ stock rebounds: https://english.mubasher.info/news/4564447/Canal-Shipping-Agencies-stock-rebounds/
  - Canal Shipping Agencies mulls EGP 100m capital raise: https://english.mubasher.info/news/4191441/Canal-Shipping-Agencies-mulls-EGP-100m-capital-raise/
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- POUL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Poultry summary=Cairo Poultry stock approaching historic peak – Analysis; Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA; Cairo Poultry sees EGP 871m block-trading deal
  - Cairo Poultry stock approaching historic peak – Analysis: https://english.mubasher.info/news/4539104/Cairo-Poultry-stock-approaching-historic-peak-Analysis/
  - Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA: https://english.mubasher.info/news/3962334/Cairo-Poultry-cancels-commercial-license-in-Dubai-s-JAFZA/
  - Cairo Poultry sees EGP 871m block-trading deal: https://english.mubasher.info/news/3862165/Cairo-Poultry-sees-EGP-871m-block-trading-deal/
- OCPH.CA: status=OLD_ACCEPTED latest=2022-01-01 age_days=1640 sources=3 expected=October Pharma S.A.E summary=October Pharma targets EGP 135m net profits in 2022; October Pharma&#39;s profit hikes 65% in nine months; October Pharma’s Q1 profits leap 402%
  - October Pharma targets EGP 135m net profits in 2022: https://english.mubasher.info/news/3895021/October-Pharma-targets-EGP-135m-net-profits-in-2022/
  - October Pharma&#39;s profit hikes 65% in nine months: https://english.mubasher.info/news/3870893/October-Pharma-s-profit-hikes-65-in-nine-months/
  - October Pharma’s Q1 profits leap 402%: https://english.mubasher.info/news/3818864/October-Pharma-s-Q1-profits-leap-402-/
- CLHO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=544 sources=3 expected=Cleopatra Hospital Group summary=Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025; Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn; Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo
  - Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025: https://english.mubasher.info/news/4594702/Cleopatra-Hospitals-unveils-EGP-84m-dividends-to-employee-for-2025/
  - Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn: https://english.mubasher.info/news/4579844/Cleopatra-Hospitals-posts-higher-consolidated-profits-in-2025-revenues-cross-EGP-7-2bn/
  - Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo: https://english.mubasher.info/news/4553462/Cleopatra-Hospitals-launches-EGP-3-5bn-Sky-hospital-in-East-Cairo/

## Warnings
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for MHOT.CA matches the company but no source/report date was detected.
- Evidence for CPCI.CA matches the company but no source/report date was detected.
- Evidence for CSAG.CA matches the company but no source/report date was detected.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence for POUL.CA matches the company but no source/report date was detected.
- Evidence for OCPH.CA matches the company but appears old; latest detected date is 2022-01-01.
- Evidence for CLHO.CA matches the company but appears old; latest detected date is 2025-01-01.
