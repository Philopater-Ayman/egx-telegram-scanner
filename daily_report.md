# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-06-28T08:38:35.958942+00:00
Generated Cairo: 2026-06-28 11:38
Run timing: target 08:45 Cairo | generated Cairo 2026-06-28 11:38 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-06-28 11:34

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 188/190
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, June 28
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 25.0% / above MA50 30.0%
- EGX70 regime: BEARISH / above MA20 37.5% / above MA50 62.5%
- Sector breadth: 28.57%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- ORAS.CA: liquidity=236360256.0 spike=1.0 score=4.6
- CCAP.CA: liquidity=171178240.0 spike=0.25 score=9.76
- PHDC.CA: liquidity=96387208.0 spike=0.24 score=18.08
- ZMID.CA: liquidity=79647176.0 spike=0.38 score=22.08
- ETRS.CA: liquidity=79255920.0 spike=1.16 score=22.37

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b-20230311:free
- Summary: EGX30 and EGX70 are bearish with weak breadth; the scanner stays in defensive mode, allowing only HOLDs.
- Prioritized tickets (GGCC.CA, CSAG.CA, RAYA.CA, etc.) show accumulation‑spike liquidity and bullish‑watch/constructive outlooks, but their sectors are not among the current leaders.
- Liquidity spikes hint at short‑term buying interest, yet prices sit near key support or resistance levels, limiting near‑term upside over the next 1‑3 days.
- Sector breadth is low at ~28 %; only Tourism & Leisure, Technology & Distribution and Automotive & Distribution display strength, leaving most stocks without sector tailwind.

## Top Liquidity Spikes
- CFGH.CA: spike=40.61 liquidity=271172.86 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CSAG.CA: spike=5.66 liquidity=67709360.0 outlook=BULLISH_WATCH score=94.2 buy_ready=False
- LCSW.CA: spike=3.61 liquidity=69972808.0 outlook=CONSTRUCTIVE score=63.76 buy_ready=False
- GGCC.CA: spike=3.49 liquidity=30787008.0 outlook=BULLISH_WATCH score=81.63 buy_ready=False
- EGBE.CA: spike=2.9 liquidity=172496.79 outlook=NEUTRAL score=43.04 buy_ready=False

## Sector Leaderboard
- #1 Tourism & Leisure: score=15.63 5d=16.81% 20d=14.02% aboveMA50=100.0%
- #2 Technology & Distribution: score=8.55 5d=5.56% 20d=-1.07% aboveMA50=100.0%
- #3 Automotive & Distribution: score=8.43 5d=4.46% 20d=8.94% aboveMA50=100.0%
- #4 Transportation & Logistics: score=7.2 5d=-0.42% 20d=-1.81% aboveMA50=50.0%
- #5 Non-bank Financial Services: score=5.43 5d=1.74% 20d=1.56% aboveMA50=60.0%
- #6 Healthcare: score=3.25 5d=0.35% 20d=2.16% aboveMA50=50.0%
- #7 Education: score=2.97 5d=-1.97% 20d=2.38% aboveMA50=66.67%
- #8 Real Estate: score=2.69 5d=-3.67% 20d=2.51% aboveMA50=84.62%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- RAYA.CA: BULLISH_WATCH score=94.55 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- CSAG.CA: BULLISH_WATCH score=94.2 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- RUBX.CA: BULLISH_WATCH score=92.63 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- GGCC.CA: BULLISH_WATCH score=81.63 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CNFN.CA: BULLISH_WATCH score=81.43 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- CIRA.CA: BULLISH_WATCH score=78.97 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MTIE.CA: BULLISH_WATCH score=76.43 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20
- SVCE.CA: BULLISH_WATCH score=73.63 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- ENGC.CA: BULLISH_WATCH score=73.63 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- AFDI.CA: BULLISH_WATCH score=73.63 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=6.42 buy_ready=False sector_rank=9 price=198.6 support=200.0 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=1367832.13 spike=0.24
- ABUK.CA: score=8.31 buy_ready=False sector_rank=20 price=68.66 support=68.01 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=12.55 liquidity=18135572.0 spike=0.14
- ACAMD.CA: score=18.05 buy_ready=False sector_rank=9 price=2.2 support=2.17 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=36.21 liquidity=10420399.0 spike=0.08
- ACGC.CA: score=11.05 buy_ready=False sector_rank=12 price=9.35 support=9.11 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=37.16 liquidity=3234636.5 spike=0.06
- ADCI.CA: score=8.42 buy_ready=False sector_rank=9 price=235.63 support=211.0 resistance=244.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=85.03 liquidity=1372477.75 spike=0.15
- ADIB.CA: score=13.85 buy_ready=False sector_rank=13 price=44.62 support=44.01 resistance=48.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=39.2 liquidity=9034277.0 spike=0.09
- ADPC.CA: score=7.64 buy_ready=False sector_rank=9 price=3.45 support=3.43 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=38.89 liquidity=3584489.0 spike=0.15
- AFDI.CA: score=14.31 buy_ready=False sector_rank=9 price=43.77 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=50.15 liquidity=2259617.5 spike=0.15
- AFMC.CA: score=0.49 buy_ready=False sector_rank=9 price=69.72 support=67.0 resistance=74.69 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=33.54 liquidity=433588.69 spike=0.25
- AJWA.CA: score=7.71 buy_ready=False sector_rank=9 price=175.01 support=131.5 resistance=188.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=82.78 liquidity=655439.44 spike=0.02
- ALCN.CA: score=9.41 buy_ready=False sector_rank=4 price=28.21 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=31.15 liquidity=8009713.5 spike=0.65
- ALUM.CA: score=1.31 buy_ready=False sector_rank=9 price=21.41 support=21.5 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=17.63 liquidity=1261380.0 spike=0.13
- AMER.CA: score=6.77 buy_ready=False sector_rank=8 price=2.36 support=2.35 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=6693379.5 spike=0.09
- AMES.CA: score=-0.39 buy_ready=False sector_rank=9 price=47.26 support=48.0 resistance=53.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=32.52 liquidity=560495.75 spike=0.18
- AMIA.CA: score=9.35 buy_ready=False sector_rank=9 price=8.68 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=40.15 liquidity=1299869.88 spike=0.09
- AMOC.CA: score=4.77 buy_ready=False sector_rank=14 price=7.58 support=7.53 resistance=8.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=21.9 liquidity=4970952.0 spike=0.1
- ANFI.CA: score=15.38 buy_ready=False sector_rank=9 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=1.27 buy_ready=False sector_rank=9 price=8.46 support=8.24 resistance=9.21 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=13.11 liquidity=996410.34 spike=1.61
- ARAB.CA: score=14.08 buy_ready=False sector_rank=8 price=0.2 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=47.06 liquidity=23482152.0 spike=0.28
- ARCC.CA: score=6.27 buy_ready=False sector_rank=17 price=55.08 support=53.0 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=31.64 liquidity=6569493.0 spike=0.19
- AREH.CA: score=18.08 buy_ready=False sector_rank=9 price=1.53 support=1.32 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=60.38 liquidity=6032811.0 spike=0.18
- ARVA.CA: score=14.01 buy_ready=False sector_rank=9 price=11.1 support=8.08 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=52.31 liquidity=3956163.0 spike=0.12
- ASCM.CA: score=22.05 buy_ready=False sector_rank=9 price=60.03 support=47.49 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=61.62 liquidity=20546986.0 spike=0.22
- ASPI.CA: score=8.65 buy_ready=False sector_rank=9 price=0.31 support=0.26 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=34.53 liquidity=5602797.0 spike=0.08
- ATLC.CA: score=14.11 buy_ready=False sector_rank=5 price=5.17 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=58.06 liquidity=940780.13 spike=0.15
- ATQA.CA: score=11.23 buy_ready=False sector_rank=20 price=9.5 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=40.18 liquidity=8920673.0 spike=0.28
- AXPH.CA: score=9.34 buy_ready=False sector_rank=9 price=1100.31 support=1073.0 resistance=1174.0 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=40.71 liquidity=1231246.96 spike=1.03
- BINV.CA: score=10.63 buy_ready=False sector_rank=15 price=47.49 support=42.97 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=60.78 liquidity=862682.88 spike=0.09
- BIOC.CA: score=5.68 buy_ready=False sector_rank=9 price=70.83 support=68.34 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=39.09 liquidity=623078.25 spike=0.26
- BTFH.CA: score=15.17 buy_ready=False sector_rank=5 price=2.99 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=26722746.0 spike=0.14
- CAED.CA: score=8.95 buy_ready=False sector_rank=9 price=70.88 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=48.33 liquidity=899674.0 spike=0.17
- CANA.CA: score=6.25 buy_ready=False sector_rank=13 price=35.03 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=41.16 liquidity=2433227.25 spike=0.23
- CCAP.CA: score=9.76 buy_ready=False sector_rank=15 price=4.85 support=4.85 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=17.46 liquidity=171178240.0 spike=0.25
- CCRS.CA: score=4.71 buy_ready=False sector_rank=9 price=2.34 support=2.32 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=31.75 liquidity=1653355.25 spike=0.09
- CEFM.CA: score=0.6 buy_ready=False sector_rank=9 price=100.24 support=100.0 resistance=109.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=23.51 liquidity=552816.63 spike=0.27
- CERA.CA: score=16.26 buy_ready=False sector_rank=9 price=1.24 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=61.54 liquidity=5211693.0 spike=0.31
- CFGH.CA: score=4.32 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 01:06 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=271172.86 spike=40.61
- CICH.CA: score=14.13 buy_ready=False sector_rank=5 price=11.99 support=11.1 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=46.48 liquidity=957754.56 spike=0.31
- CIEB.CA: score=13.3 buy_ready=False sector_rank=13 price=23.93 support=23.27 resistance=24.75 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=58.19 liquidity=4485032.45 spike=0.82
- CIRA.CA: score=16.37 buy_ready=False sector_rank=7 price=28.23 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=59.81 liquidity=4181999.0 spike=0.24
- CLHO.CA: score=17.0 buy_ready=False sector_rank=6 price=16.49 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=63.34 liquidity=4702214.0 spike=0.13
- CNFN.CA: score=19.91 buy_ready=False sector_rank=5 price=4.78 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=60.4 liquidity=6742931.0 spike=0.17
- COMI.CA: score=14.82 buy_ready=False sector_rank=13 price=131.86 support=129.8 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=50.27 liquidity=48861408.0 spike=0.08
- COPR.CA: score=10.68 buy_ready=False sector_rank=9 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=50.85 liquidity=3631734.0 spike=0.11
- COSG.CA: score=2.37 buy_ready=False sector_rank=9 price=1.51 support=1.52 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=32.35 liquidity=2318518.75 spike=0.04
- CPCI.CA: score=12.71 buy_ready=False sector_rank=9 price=377.33 support=347.11 resistance=378.5 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=72.05 liquidity=655422.19 spike=0.4
- CSAG.CA: score=26.4 buy_ready=False sector_rank=4 price=33.01 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=49.89 liquidity=67709360.0 spike=5.66
- DAPH.CA: score=14.6 buy_ready=False sector_rank=9 price=81.24 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=54.9 liquidity=3551701.25 spike=0.34
- DEIN.CA: score=6.05 buy_ready=False sector_rank=9 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=11.15 buy_ready=False sector_rank=11 price=26.78 support=23.7 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=73.9 liquidity=1313928.63 spike=0.35
- DSCW.CA: score=14.05 buy_ready=False sector_rank=9 price=1.74 support=1.74 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=39.39 liquidity=10390815.0 spike=0.22
- DTPP.CA: score=1.04 buy_ready=False sector_rank=9 price=116.0 support=114.0 resistance=130.89 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=19.44 liquidity=990292.0 spike=0.87
- EALR.CA: score=5.57 buy_ready=False sector_rank=9 price=350.23 support=350.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=44.67 liquidity=515138.56 spike=0.16
- EASB.CA: score=14.4 buy_ready=False sector_rank=9 price=7.85 support=4.66 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=84.18 liquidity=5348705.5 spike=0.49
- EAST.CA: score=6.18 buy_ready=False sector_rank=11 price=37.5 support=37.01 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=47.42 liquidity=2342939.5 spike=0.05
- EBSC.CA: score=8.99 buy_ready=False sector_rank=9 price=1.79 support=1.66 resistance=2.09 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=35.29 liquidity=936100.17 spike=0.36
- ECAP.CA: score=16.02 buy_ready=False sector_rank=9 price=33.43 support=29.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=69.97 liquidity=5970876.0 spike=0.72
- EDFM.CA: score=0.44 buy_ready=False sector_rank=9 price=330.59 support=322.11 resistance=355.0 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=26.96 liquidity=384806.76 spike=0.73
- EEII.CA: score=12.53 buy_ready=False sector_rank=9 price=2.43 support=2.3 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=53.45 liquidity=2482980.0 spike=0.18
- EFIC.CA: score=-2.12 buy_ready=False sector_rank=20 price=194.01 support=192.01 resistance=213.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=15.79 liquidity=565036.56 spike=0.3
- EFID.CA: score=9.84 buy_ready=False sector_rank=11 price=25.99 support=26.67 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=27.31 liquidity=18139784.0 spike=0.25
- EFIH.CA: score=7.02 buy_ready=False sector_rank=21 price=20.51 support=20.09 resistance=22.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=41.24 liquidity=3731874.5 spike=0.08
- EGAL.CA: score=7.87 buy_ready=False sector_rank=20 price=278.04 support=280.0 resistance=334.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=10.2 liquidity=9560496.0 spike=0.13
- EGAS.CA: score=7.28 buy_ready=False sector_rank=14 price=47.6 support=48.2 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=42.15 liquidity=2472198.75 spike=0.25
- EGBE.CA: score=13.79 buy_ready=False sector_rank=13 price=0.46 support=0.43 resistance=0.46 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=65.52 liquidity=172496.79 spike=2.9
- EGCH.CA: score=2.36 buy_ready=False sector_rank=20 price=12.71 support=12.69 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=28.76 liquidity=4052236.5 spike=0.07
- EGSA.CA: score=4.85 buy_ready=False sector_rank=10 price=8.75 support=8.55 resistance=9.1 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=31.03 liquidity=17500.0 spike=1.95
- EGTS.CA: score=14.19 buy_ready=False sector_rank=8 price=16.51 support=16.7 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=46.38 liquidity=6113501.5 spike=0.06
- EHDR.CA: score=4.33 buy_ready=False sector_rank=9 price=2.45 support=2.44 resistance=2.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9280606.0 spike=0.16
- EKHO.CA: score=9.8 buy_ready=False sector_rank=14 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=4.94 buy_ready=False sector_rank=19 price=2.09 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=36.67 liquidity=1907511.38 spike=0.09
- ELKA.CA: score=9.67 buy_ready=False sector_rank=9 price=1.23 support=1.15 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=2613099.75 spike=0.06
- ELNA.CA: score=0.83 buy_ready=False sector_rank=9 price=36.1 support=36.0 resistance=41.51 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=33.65 liquidity=636226.37 spike=1.57
- ELSH.CA: score=14.77 buy_ready=False sector_rank=9 price=11.41 support=8.28 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=52.69 liquidity=6714176.0 spike=0.04
- ELWA.CA: score=9.4 buy_ready=False sector_rank=9 price=2.04 support=2.0 resistance=2.22 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=50.98 liquidity=1351612.17 spike=0.65
- EMFD.CA: score=18.08 buy_ready=False sector_rank=8 price=11.47 support=10.5 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=43.95 liquidity=17742656.0 spike=0.06
- ENGC.CA: score=16.83 buy_ready=False sector_rank=9 price=36.38 support=32.81 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=59.63 liquidity=4777859.0 spike=0.37
- EOSB.CA: score=12.1 buy_ready=False sector_rank=9 price=1.48 support=1.35 resistance=1.55 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=50716.64 spike=0.39
- EPCO.CA: score=5.65 buy_ready=False sector_rank=9 price=8.85 support=8.89 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=40.24 liquidity=602181.13 spike=0.07
- EPPK.CA: score=12.52 buy_ready=False sector_rank=9 price=12.91 support=11.67 resistance=13.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=67.48 liquidity=471391.41 spike=0.49
- ETEL.CA: score=16.4 buy_ready=False sector_rank=10 price=92.19 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=46.73 liquidity=9472426.0 spike=0.12
- ETRS.CA: score=22.37 buy_ready=False sector_rank=9 price=10.89 support=7.93 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=70.92 liquidity=79255920.0 spike=1.16
- EXPA.CA: score=5.23 buy_ready=False sector_rank=13 price=18.21 support=18.2 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=18.55 liquidity=5414592.0 spike=0.17
- FAIT.CA: score=8.6 buy_ready=False sector_rank=13 price=36.15 support=35.01 resistance=38.29 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=38.43 liquidity=781779.93 spike=0.37
- FAITA.CA: score=7.83 buy_ready=False sector_rank=13 price=0.99 support=0.99 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=11695.99 spike=0.33
- FERC.CA: score=0.15 buy_ready=False sector_rank=20 price=75.03 support=75.0 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=23.06 liquidity=840239.25 spike=0.22
- FWRY.CA: score=15.29 buy_ready=False sector_rank=21 price=18.55 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=13747751.0 spike=0.05
- GBCO.CA: score=21.4 buy_ready=False sector_rank=3 price=30.5 support=25.25 resistance=31.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=94.21 liquidity=22191912.0 spike=0.24
- GDWA.CA: score=0.72 buy_ready=False sector_rank=9 price=0.78 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=30.95 liquidity=1672864.0 spike=0.12
- GGCC.CA: score=28.03 buy_ready=False sector_rank=9 price=0.46 support=0.4 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=52.38 liquidity=30787008.0 spike=3.49
- GIHD.CA: score=14.35 buy_ready=False sector_rank=9 price=42.69 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=58.27 liquidity=2297036.0 spike=0.29
- GMCI.CA: score=4.23 buy_ready=False sector_rank=9 price=1.71 support=1.66 resistance=1.84 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=36.0 liquidity=173573.55 spike=0.54
- GRCA.CA: score=5.36 buy_ready=False sector_rank=9 price=52.78 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=39.48 liquidity=310427.63 spike=0.07
- GSSC.CA: score=7.01 buy_ready=False sector_rank=9 price=245.91 support=228.1 resistance=257.49 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=39.18 liquidity=1955722.26 spike=0.86
- GTWL.CA: score=22.55 buy_ready=False sector_rank=9 price=61.2 support=45.47 resistance=68.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=86.73 liquidity=43236012.0 spike=2.75
- HDBK.CA: score=16.82 buy_ready=False sector_rank=13 price=158.26 support=138.0 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=80.29 liquidity=11053386.0 spike=0.42
- HELI.CA: score=18.08 buy_ready=False sector_rank=8 price=6.42 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=52.53 liquidity=17029998.0 spike=0.13
- HRHO.CA: score=19.17 buy_ready=False sector_rank=5 price=26.82 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=57.49 liquidity=20003554.0 spike=0.14
- ICID.CA: score=14.07 buy_ready=False sector_rank=9 price=7.86 support=5.0 resistance=8.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=80.91 liquidity=5020100.5 spike=0.31
- IDRE.CA: score=10.73 buy_ready=False sector_rank=9 price=42.95 support=42.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=43.82 liquidity=2682371.5 spike=0.17
- IFAP.CA: score=5.68 buy_ready=False sector_rank=16 price=19.34 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=44.94 liquidity=1965440.13 spike=0.3
- INFI.CA: score=0.57 buy_ready=False sector_rank=9 price=90.76 support=92.5 resistance=105.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=18.57 liquidity=1514441.5 spike=0.19
- IRON.CA: score=3.95 buy_ready=False sector_rank=20 price=31.56 support=30.95 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=35.08 liquidity=1641943.5 spike=0.22
- ISMA.CA: score=18.59 buy_ready=False sector_rank=9 price=29.4 support=25.95 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=54.84 liquidity=8533044.0 spike=0.23
- ISMQ.CA: score=18.31 buy_ready=False sector_rank=20 price=8.8 support=7.38 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=67.47 liquidity=54412688.0 spike=0.55
- ISPH.CA: score=15.3 buy_ready=False sector_rank=6 price=11.5 support=11.3 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=39.94 liquidity=52434932.0 spike=0.46
- JUFO.CA: score=12.79 buy_ready=False sector_rank=11 price=29.95 support=28.09 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=58.37 liquidity=4946872.0 spike=0.14
- KABO.CA: score=13.88 buy_ready=False sector_rank=12 price=6.2 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=38.16 liquidity=6064395.0 spike=0.35
- KWIN.CA: score=11.42 buy_ready=False sector_rank=9 price=69.68 support=65.75 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=44.26 liquidity=6371292.0 spike=0.66
- KZPC.CA: score=-0.61 buy_ready=False sector_rank=9 price=8.65 support=8.6 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=14.44 liquidity=338321.81 spike=0.05
- LCSW.CA: score=26.7 buy_ready=False sector_rank=17 price=29.84 support=26.0 resistance=31.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=70.94 liquidity=69972808.0 spike=3.61
- LUTS.CA: score=17.01 buy_ready=False sector_rank=9 price=0.7 support=0.55 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=61.21 liquidity=4955459.0 spike=0.11
- MAAL.CA: score=20.01 buy_ready=False sector_rank=9 price=7.15 support=5.16 resistance=7.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=78.24 liquidity=24166132.0 spike=1.48
- MASR.CA: score=16.38 buy_ready=False sector_rank=9 price=6.87 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=56.89 liquidity=8325315.0 spike=0.15
- MBSC.CA: score=7.53 buy_ready=False sector_rank=17 price=236.39 support=242.0 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=34.9 liquidity=7830980.5 spike=0.21
- MCQE.CA: score=3.59 buy_ready=False sector_rank=17 price=170.02 support=166.66 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=17.86 liquidity=3889782.25 spike=0.24
- MCRO.CA: score=8.92 buy_ready=False sector_rank=9 price=1.2 support=1.2 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=9868808.0 spike=0.26
- MENA.CA: score=8.9 buy_ready=False sector_rank=8 price=6.69 support=6.22 resistance=7.75 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=49.28 liquidity=826756.9 spike=0.07
- MEPA.CA: score=2.0 buy_ready=False sector_rank=9 price=1.54 support=1.58 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=20.0 liquidity=2945246.5 spike=0.24
- MFPC.CA: score=8.31 buy_ready=False sector_rank=20 price=35.0 support=35.15 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=8.54 liquidity=21784640.0 spike=0.26
- MFSC.CA: score=16.35 buy_ready=False sector_rank=9 price=50.2 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=56.14 liquidity=4295042.0 spike=0.47
- MHOT.CA: score=16.38 buy_ready=False sector_rank=1 price=34.18 support=28.83 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=73.12 liquidity=1984779.38 spike=0.07
- MICH.CA: score=12.79 buy_ready=False sector_rank=9 price=37.0 support=35.4 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=54.58 liquidity=2741400.5 spike=0.18
- MILS.CA: score=8.89 buy_ready=False sector_rank=9 price=130.07 support=130.11 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=36.62 liquidity=836896.94 spike=0.07
- MIPH.CA: score=7.86 buy_ready=False sector_rank=6 price=641.55 support=640.0 resistance=710.0 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=46.16 liquidity=1982389.46 spike=1.29
- MOED.CA: score=7.17 buy_ready=False sector_rank=9 price=0.67 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=1114632.38 spike=0.11
- MOIL.CA: score=9.84 buy_ready=False sector_rank=14 price=0.49 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=60.87 liquidity=36501.2 spike=0.2
- MOIN.CA: score=-0.41 buy_ready=False sector_rank=9 price=23.03 support=22.61 resistance=25.66 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=0.97 liquidity=535194.19 spike=0.85
- MOSC.CA: score=6.31 buy_ready=False sector_rank=9 price=255.12 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=46.6 liquidity=1261115.13 spike=0.15
- MPCI.CA: score=22.05 buy_ready=False sector_rank=9 price=232.31 support=204.36 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=60.69 liquidity=12776591.0 spike=0.13
- MPCO.CA: score=14.33 buy_ready=False sector_rank=16 price=1.8 support=1.58 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=54.84 liquidity=6616048.5 spike=0.06
- MPRC.CA: score=20.19 buy_ready=False sector_rank=9 price=39.13 support=31.1 resistance=38.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=75.37 liquidity=59725576.0 spike=1.57
- MTIE.CA: score=14.25 buy_ready=False sector_rank=3 price=8.94 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=51.52 liquidity=3851278.75 spike=0.24
- NAHO.CA: score=6.36 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=60.0 liquidity=24189.78 spike=1.14
- NCCW.CA: score=12.97 buy_ready=False sector_rank=9 price=6.05 support=5.29 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=51.67 liquidity=4916681.5 spike=0.15
- NEDA.CA: score=0.17 buy_ready=False sector_rank=9 price=2.74 support=2.68 resistance=2.84 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=28.57 liquidity=117806.3 spike=0.32
- NHPS.CA: score=5.05 buy_ready=False sector_rank=9 price=63.1 support=61.62 resistance=68.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=993014.75 spike=0.25
- NINH.CA: score=7.75 buy_ready=False sector_rank=9 price=17.54 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=49.07 liquidity=698200.25 spike=0.17
- NIPH.CA: score=8.57 buy_ready=False sector_rank=6 price=160.8 support=157.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=32.48 liquidity=5273358.0 spike=0.08
- OBRI.CA: score=7.64 buy_ready=False sector_rank=9 price=32.55 support=33.55 resistance=37.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=45.44 liquidity=2585950.0 spike=0.19
- OCDI.CA: score=19.08 buy_ready=False sector_rank=8 price=24.25 support=20.0 resistance=25.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=76.51 liquidity=62910400.0 spike=0.98
- OCPH.CA: score=6.28 buy_ready=False sector_rank=9 price=343.09 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=36.11 liquidity=1225711.63 spike=0.2
- ODIN.CA: score=11.31 buy_ready=False sector_rank=9 price=2.1 support=1.91 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=51.67 liquidity=3253424.0 spike=0.3
- OFH.CA: score=2.24 buy_ready=False sector_rank=9 price=0.59 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=24.36 liquidity=3186730.75 spike=0.16
- OIH.CA: score=16.76 buy_ready=False sector_rank=15 price=1.4 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=58.62 liquidity=11562558.0 spike=0.14
- OLFI.CA: score=7.34 buy_ready=False sector_rank=11 price=21.41 support=21.39 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=51.8 liquidity=2499534.75 spike=0.12
- ORAS.CA: score=4.6 buy_ready=False sector_rank=18 price=686.62 support=680.0 resistance=732.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=236360256.0 spike=1.0
- ORHD.CA: score=20.08 buy_ready=False sector_rank=8 price=38.4 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=60.63 liquidity=78815296.0 spike=0.45
- ORWE.CA: score=8.48 buy_ready=False sector_rank=12 price=22.49 support=22.61 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=5662220.5 spike=0.15
- PHAR.CA: score=13.27 buy_ready=False sector_rank=6 price=87.03 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=59.17 liquidity=973005.06 spike=0.03
- PHDC.CA: score=18.08 buy_ready=False sector_rank=8 price=14.61 support=14.43 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=54.93 liquidity=96387208.0 spike=0.24
- PHTV.CA: score=10.73 buy_ready=False sector_rank=9 price=256.43 support=201.55 resistance=256.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=85.23 liquidity=3674530.5 spike=0.18
- POUL.CA: score=19.93 buy_ready=False sector_rank=11 price=38.66 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=55.39 liquidity=8093173.0 spike=0.21
- PRCL.CA: score=19.7 buy_ready=False sector_rank=17 price=30.5 support=22.02 resistance=32.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=67.99 liquidity=10309525.0 spike=0.26
- PRDC.CA: score=20.08 buy_ready=False sector_rank=8 price=6.88 support=5.7 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=63.47 liquidity=12507220.0 spike=0.11
- PRMH.CA: score=12.44 buy_ready=False sector_rank=9 price=2.46 support=2.26 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=38.0 liquidity=4383991.0 spike=0.14
- RACC.CA: score=7.34 buy_ready=False sector_rank=9 price=9.77 support=9.38 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=2291318.75 spike=0.24
- RAKT.CA: score=6.12 buy_ready=False sector_rank=9 price=23.11 support=22.0 resistance=24.1 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=37.86 liquidity=67226.99 spike=0.28
- RAYA.CA: score=23.4 buy_ready=False sector_rank=2 price=7.3 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=42.38 liquidity=31968380.0 spike=0.36
- RMDA.CA: score=13.83 buy_ready=False sector_rank=6 price=4.89 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=39.39 liquidity=8528045.0 spike=0.11
- ROTO.CA: score=15.8 buy_ready=False sector_rank=9 price=40.01 support=32.76 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=73.14 liquidity=5747844.0 spike=0.21
- RREI.CA: score=6.17 buy_ready=False sector_rank=9 price=3.45 support=3.35 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=40.54 liquidity=1121692.5 spike=0.06
- RTVC.CA: score=4.93 buy_ready=False sector_rank=9 price=3.66 support=3.63 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=40.86 liquidity=874941.19 spike=0.17
- RUBX.CA: score=26.55 buy_ready=False sector_rank=9 price=10.94 support=9.8 resistance=10.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=58.51 liquidity=20658904.0 spike=2.25
- SAUD.CA: score=0.97 buy_ready=False sector_rank=13 price=21.02 support=20.82 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=25.28 liquidity=1151003.63 spike=0.13
- SCEM.CA: score=6.54 buy_ready=False sector_rank=17 price=62.32 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=42.29 liquidity=1836554.5 spike=0.1
- SCFM.CA: score=0.6 buy_ready=False sector_rank=9 price=238.53 support=226.5 resistance=276.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=20.9 liquidity=544966.81 spike=0.09
- SCTS.CA: score=0.72 buy_ready=False sector_rank=7 price=564.8 support=552.8 resistance=630.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=29.99 liquidity=530993.63 spike=0.15
- SDTI.CA: score=10.89 buy_ready=False sector_rank=9 price=47.33 support=44.03 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=59.39 liquidity=833395.19 spike=0.07
- SEIG.CA: score=10.4 buy_ready=False sector_rank=9 price=186.21 support=179.43 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=42.41 liquidity=350691.0 spike=0.08
- SIPC.CA: score=4.04 buy_ready=False sector_rank=9 price=3.41 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=29.09 liquidity=3987225.5 spike=0.35
- SKPC.CA: score=7.31 buy_ready=False sector_rank=20 price=16.0 support=15.9 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=31.8 liquidity=10597436.0 spike=0.28
- SMFR.CA: score=1.32 buy_ready=False sector_rank=9 price=196.11 support=192.0 resistance=214.0 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=31.3 liquidity=1266086.16 spike=0.69
- SNFC.CA: score=8.46 buy_ready=False sector_rank=9 price=12.01 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=68.84 liquidity=2412995.0 spike=0.12
- SPIN.CA: score=7.71 buy_ready=False sector_rank=12 price=14.0 support=13.3 resistance=14.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=45.63 liquidity=2886197.5 spike=0.51
- SPMD.CA: score=10.91 buy_ready=False sector_rank=9 price=0.42 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=49.01 liquidity=2858411.25 spike=0.12
- SUGR.CA: score=-0.0 buy_ready=False sector_rank=11 price=47.02 support=47.03 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=23.54 liquidity=1159915.0 spike=0.14
- SVCE.CA: score=19.4 buy_ready=False sector_rank=9 price=9.07 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=54.92 liquidity=7346004.0 spike=0.1
- SWDY.CA: score=10.86 buy_ready=False sector_rank=19 price=85.26 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=44.21 liquidity=6829288.0 spike=0.39
- TALM.CA: score=9.69 buy_ready=False sector_rank=7 price=15.96 support=15.5 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=52.7 liquidity=1506015.0 spike=0.19
- TMGH.CA: score=18.08 buy_ready=False sector_rank=8 price=95.44 support=92.91 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=54.96 liquidity=56615152.0 spike=0.13
- TRTO.CA: score=6.05 buy_ready=False sector_rank=9 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=491.27 spike=0.67
- UEFM.CA: score=10.41 buy_ready=False sector_rank=9 price=486.78 support=465.01 resistance=505.0 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=62.58 liquidity=998385.78 spike=1.18
- UEGC.CA: score=6.3 buy_ready=False sector_rank=9 price=1.39 support=1.32 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=34.37 liquidity=3251684.5 spike=0.14
- UNIP.CA: score=6.89 buy_ready=False sector_rank=9 price=0.3 support=0.28 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=1840857.75 spike=0.08
- UNIT.CA: score=4.17 buy_ready=False sector_rank=8 price=12.96 support=12.91 resistance=15.8 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=33.47 liquidity=1097919.36 spike=0.18
- WCDF.CA: score=5.23 buy_ready=False sector_rank=9 price=531.95 support=450.0 resistance=547.9 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=43.92 liquidity=179267.15 spike=0.69
- WKOL.CA: score=0.64 buy_ready=False sector_rank=9 price=281.1 support=284.0 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:59 AM market time freshness=DELAYED_CURRENT RSI=34.43 liquidity=585610.75 spike=0.2
- ZEOT.CA: score=15.61 buy_ready=False sector_rank=9 price=10.68 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=67.52 liquidity=5561567.0 spike=0.22
- ZMID.CA: score=22.08 buy_ready=False sector_rank=8 price=6.37 support=5.82 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=62.07 liquidity=79647176.0 spike=0.38

## Backtesting Lite
- GGCC.CA: 180d return=-16.12%, max drawdown=-45.58%, MA20>MA50 days last20=19, as_of=2026-06-24T21:00:00+00:00
- LCSW.CA: 180d return=14.22%, max drawdown=-15.87%, MA20>MA50 days last20=20, as_of=2026-06-24T21:00:00+00:00
- RUBX.CA: 180d return=0.0%, max drawdown=-21.39%, MA20>MA50 days last20=11, as_of=2026-06-24T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- GGCC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Giza General - Contracting and Real Estate Investment S.A.E summary=EGX approves listing EGP 144m capital increase for Giza Contracting; Giza Contracting tests key EGP 0.51 level; Giza Contracting’s consolidated net profits leap to EGP 140m in 9M-25
  - EGX approves listing EGP 144m capital increase for Giza Contracting: https://english.mubasher.info/news/4588793/EGX-approves-listing-EGP-144m-capital-increase-for-Giza-Contracting/
  - Giza Contracting tests key EGP 0.51 level: https://english.mubasher.info/news/4563778/Giza-Contracting-tests-key-EGP-0-51-level/
  - Giza Contracting’s consolidated net profits leap to EGP 140m in 9M-25: https://english.mubasher.info/news/4530408/Giza-Contracting-s-consolidated-net-profits-leap-to-EGP-140m-in-9M-25/
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- RUBX.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Rubex International for Plastic and Acrylic Manufacturing summary=Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- CSAG.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Canal Shipping Agencies summary=Canal Shipping Agencies targets EGP 970m net profits in FY26/27; Canal Shipping Agencies’ stock rebounds; Canal Shipping Agencies mulls EGP 100m capital raise
  - Canal Shipping Agencies targets EGP 970m net profits in FY26/27: https://english.mubasher.info/news/4582423/Canal-Shipping-Agencies-targets-EGP-970m-net-profits-in-FY26-27/
  - Canal Shipping Agencies’ stock rebounds: https://english.mubasher.info/news/4564447/Canal-Shipping-Agencies-stock-rebounds/
  - Canal Shipping Agencies mulls EGP 100m capital raise: https://english.mubasher.info/news/4191441/Canal-Shipping-Agencies-mulls-EGP-100m-capital-raise/
- RAYA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=543 sources=3 expected=Raya Holding summary=Raya stock maintains bullish momentum above EGP 9; Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt; Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn
  - Raya stock maintains bullish momentum above EGP 9: https://english.mubasher.info/news/4601857/Raya-stock-maintains-bullish-momentum-above-EGP-9/
  - Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt: https://english.mubasher.info/news/4577815/Aman-Holding-MSMEDA-partner-to-inject-EGP-300m-into-SMEs-across-Egypt/
  - Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn: https://english.mubasher.info/news/4564195/Raya-Holding-s-consolidated-profits-surge-in-2025-revenues-hit-EGP-63-8bn/
- GTWL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Golden Textiles & Clothes Wool summary=Golden Textiles profits jump 214%; Golden Textiles OGM OKs 50 piasters/shr dividends; Golden Textiles consolidated profits down 18.5% in FY16
  - Golden Textiles profits jump 214%: https://english.mubasher.info/news/3108548/Golden-Textiles-profits-jump-214-/
  - Golden Textiles OGM OKs 50 piasters/shr dividends: https://english.mubasher.info/news/3103061/Golden-Textiles-OGM-OKs-50-piasters-shr-dividends/
  - Golden Textiles consolidated profits down 18.5% in FY16: https://english.mubasher.info/news/3092552/Golden-Textiles-consolidated-profits-down-18-5-in-FY16/
- ETRS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Transport and Commercial Services Company S.A.E. summary=Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- ZMID.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=543 sources=3 expected=Zahraa Maadi Investment and Development summary=Zahraa Maadi unveils distribution date for 2025 cash dividends; Zahraa Maadi to disburse EGP 250m dividends for 2025; Zahraa Maadi’s stock faces key resistance at EGP 5.22
  - Zahraa Maadi unveils distribution date for 2025 cash dividends: https://english.mubasher.info/news/4594804/Zahraa-Maadi-unveils-distribution-date-for-2025-cash-dividends/
  - Zahraa Maadi to disburse EGP 250m dividends for 2025: https://english.mubasher.info/news/4583591/Zahraa-Maadi-to-disburse-EGP-250m-dividends-for-2025/
  - Zahraa Maadi’s stock faces key resistance at EGP 5.22: https://english.mubasher.info/news/4563531/Zahraa-Maadi-s-stock-faces-key-resistance-at-EGP-5-22/

## Warnings
- Evidence for GGCC.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Evidence for CSAG.CA matches the company but no source/report date was detected.
- Evidence for RAYA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for GTWL.CA matches the company but no source/report date was detected.
- Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- Evidence for ZMID.CA matches the company but appears old; latest detected date is 2025-01-01.
