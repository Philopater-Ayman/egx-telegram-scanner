# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-06-28T09:34:14.249476+00:00
Generated Cairo: 2026-06-28 12:34
Run timing: target 09:15 Cairo | generated Cairo 2026-06-28 12:34 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-06-28 12:29

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 186/190
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, June 28
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 20.0% / above MA50 30.0%
- EGX70 regime: BEARISH / above MA20 40.0% / above MA50 62.5%
- Sector breadth: 23.81%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- ORAS.CA: liquidity=307902240.0 spike=1.0 score=4.6
- CCAP.CA: liquidity=192084944.0 spike=0.28 score=9.78
- PHDC.CA: liquidity=143107856.0 spike=0.35 score=18.01
- OCDI.CA: liquidity=122456720.0 spike=1.91 score=20.83
- ISMQ.CA: liquidity=102607536.0 spike=1.04 score=3.2

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: 

## Top Liquidity Spikes
- CSAG.CA: spike=6.2 liquidity=74273464.0 outlook=BULLISH_WATCH score=94.65 buy_ready=False
- RUBX.CA: spike=4.81 liquidity=44215020.0 outlook=BULLISH_WATCH score=86.66 buy_ready=False
- LCSW.CA: spike=4.56 liquidity=88388520.0 outlook=CONSTRUCTIVE score=69.93 buy_ready=False
- GGCC.CA: spike=3.96 liquidity=34929472.0 outlook=BULLISH_WATCH score=81.66 buy_ready=False
- GTWL.CA: spike=2.99 liquidity=46877860.0 outlook=CONSTRUCTIVE score=66.66 buy_ready=False

## Sector Leaderboard
- #1 Tourism & Leisure: score=15.66 5d=16.81% 20d=14.02% aboveMA50=100.0%
- #2 Technology & Distribution: score=8.69 5d=5.56% 20d=-1.07% aboveMA50=100.0%
- #3 Automotive & Distribution: score=8.56 5d=4.46% 20d=8.94% aboveMA50=100.0%
- #4 Transportation & Logistics: score=7.65 5d=-0.42% 20d=-1.81% aboveMA50=50.0%
- #5 Non-bank Financial Services: score=4.38 5d=1.74% 20d=1.56% aboveMA50=40.0%
- #6 Healthcare: score=3.29 5d=0.35% 20d=2.16% aboveMA50=50.0%
- #7 Education: score=3.06 5d=-1.97% 20d=2.38% aboveMA50=66.67%
- #8 Textiles: score=3.04 5d=-0.53% 20d=-1.79% aboveMA50=75.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- RAYA.CA: BULLISH_WATCH score=94.69 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- CSAG.CA: BULLISH_WATCH score=94.65 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- RUBX.CA: BULLISH_WATCH score=86.66 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- GGCC.CA: BULLISH_WATCH score=81.66 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CNFN.CA: BULLISH_WATCH score=80.38 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MTIE.CA: BULLISH_WATCH score=76.56 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20
- ATLC.CA: BULLISH_WATCH score=74.38 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- AFDI.CA: BULLISH_WATCH score=73.66 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- PHAR.CA: BULLISH_WATCH score=73.29 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- CIRA.CA: BULLISH_WATCH score=73.06 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=7.51 buy_ready=False sector_rank=9 price=197.87 support=200.0 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=2447272.25 spike=0.42
- ABUK.CA: score=8.12 buy_ready=False sector_rank=21 price=68.98 support=68.01 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=12.55 liquidity=29914172.0 spike=0.22
- ACAMD.CA: score=18.06 buy_ready=False sector_rank=9 price=2.2 support=2.17 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=36.21 liquidity=12462619.0 spike=0.1
- ACGC.CA: score=12.74 buy_ready=False sector_rank=8 price=9.44 support=9.11 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=37.16 liquidity=4522517.5 spike=0.08
- ADCI.CA: score=8.63 buy_ready=False sector_rank=9 price=235.33 support=211.0 resistance=244.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:12 AM market time freshness=DELAYED_CURRENT RSI=85.03 liquidity=1563106.13 spike=0.17
- ADIB.CA: score=14.68 buy_ready=False sector_rank=17 price=44.75 support=44.01 resistance=48.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=39.2 liquidity=13646505.0 spike=0.14
- ADPC.CA: score=9.17 buy_ready=False sector_rank=9 price=3.46 support=3.43 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:10 AM market time freshness=DELAYED_CURRENT RSI=38.89 liquidity=5109252.5 spike=0.22
- AFDI.CA: score=14.82 buy_ready=False sector_rank=9 price=44.0 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:10 AM market time freshness=DELAYED_CURRENT RSI=50.15 liquidity=2757371.25 spike=0.18
- AFMC.CA: score=0.5 buy_ready=False sector_rank=9 price=69.72 support=67.0 resistance=74.69 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=33.54 liquidity=433588.69 spike=0.25
- AJWA.CA: score=10.22 buy_ready=False sector_rank=9 price=176.53 support=131.5 resistance=188.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:12 AM market time freshness=DELAYED_CURRENT RSI=82.78 liquidity=3157597.5 spike=0.12
- ALCN.CA: score=10.09 buy_ready=False sector_rank=4 price=28.12 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:13 AM market time freshness=DELAYED_CURRENT RSI=31.15 liquidity=8694816.0 spike=0.71
- ALUM.CA: score=1.9 buy_ready=False sector_rank=9 price=21.56 support=21.5 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=17.63 liquidity=1835974.63 spike=0.18
- AMER.CA: score=9.99 buy_ready=False sector_rank=10 price=2.35 support=2.35 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=9978331.0 spike=0.13
- AMES.CA: score=-0.06 buy_ready=False sector_rank=9 price=47.05 support=48.0 resistance=53.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=32.52 liquidity=871705.31 spike=0.28
- AMIA.CA: score=9.8 buy_ready=False sector_rank=9 price=8.7 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=40.15 liquidity=1740769.25 spike=0.13
- AMOC.CA: score=9.09 buy_ready=False sector_rank=13 price=7.56 support=7.53 resistance=8.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=21.9 liquidity=9233715.0 spike=0.18
- ANFI.CA: score=15.4 buy_ready=False sector_rank=9 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=-0.55 buy_ready=False sector_rank=9 price=8.45 support=8.24 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:59 AM market time freshness=DELAYED_CURRENT RSI=13.11 liquidity=390233.44 spike=0.49
- ARAB.CA: score=15.01 buy_ready=False sector_rank=10 price=0.21 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=47.06 liquidity=42455568.0 spike=0.5
- ARCC.CA: score=7.69 buy_ready=False sector_rank=16 price=54.94 support=53.0 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=31.64 liquidity=7921538.5 spike=0.23
- AREH.CA: score=22.06 buy_ready=False sector_rank=9 price=1.59 support=1.32 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=60.38 liquidity=13123031.0 spike=0.39
- ARVA.CA: score=14.44 buy_ready=False sector_rank=9 price=11.15 support=8.08 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:13 AM market time freshness=DELAYED_CURRENT RSI=52.31 liquidity=4379830.5 spike=0.14
- ASCM.CA: score=22.06 buy_ready=False sector_rank=9 price=59.56 support=47.49 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=61.62 liquidity=25878184.0 spike=0.28
- ASPI.CA: score=11.31 buy_ready=False sector_rank=9 price=0.31 support=0.26 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=34.53 liquidity=8242881.5 spike=0.12
- ATLC.CA: score=14.31 buy_ready=False sector_rank=5 price=5.15 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=58.06 liquidity=1556821.13 spike=0.25
- ATQA.CA: score=12.12 buy_ready=False sector_rank=21 price=9.56 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=40.18 liquidity=14273568.0 spike=0.45
- AXPH.CA: score=9.36 buy_ready=False sector_rank=9 price=1100.31 support=1073.0 resistance=1174.0 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=40.71 liquidity=1231246.96 spike=1.03
- BINV.CA: score=11.09 buy_ready=False sector_rank=14 price=47.2 support=42.97 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:13 AM market time freshness=DELAYED_CURRENT RSI=60.78 liquidity=1311995.75 spike=0.13
- BIOC.CA: score=5.8 buy_ready=False sector_rank=9 price=70.76 support=68.34 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=39.09 liquidity=734779.75 spike=0.31
- BTFH.CA: score=14.75 buy_ready=False sector_rank=5 price=2.99 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=38006328.0 spike=0.19
- CAED.CA: score=9.13 buy_ready=False sector_rank=9 price=70.43 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=48.33 liquidity=1064500.0 spike=0.21
- CANA.CA: score=8.27 buy_ready=False sector_rank=17 price=35.02 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=41.16 liquidity=4596010.5 spike=0.43
- CCAP.CA: score=9.78 buy_ready=False sector_rank=14 price=4.87 support=4.85 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=17.46 liquidity=192084944.0 spike=0.28
- CCRS.CA: score=7.21 buy_ready=False sector_rank=9 price=2.34 support=2.32 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=31.75 liquidity=4143456.0 spike=0.23
- CEFM.CA: score=0.94 buy_ready=False sector_rank=9 price=99.9 support=100.0 resistance=109.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=23.51 liquidity=873489.56 spike=0.42
- CERA.CA: score=18.24 buy_ready=False sector_rank=9 price=1.24 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=61.54 liquidity=7176133.0 spike=0.43
- CFGH.CA: score=0.09 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=10054.09 spike=1.51
- CICH.CA: score=9.1 buy_ready=False sector_rank=5 price=11.9 support=11.1 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:13 AM market time freshness=DELAYED_CURRENT RSI=46.48 liquidity=1347375.25 spike=0.44
- CIEB.CA: score=8.98 buy_ready=False sector_rank=17 price=23.66 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:11 AM market time freshness=DELAYED_CURRENT RSI=58.19 liquidity=2303095.25 spike=0.35
- CIRA.CA: score=19.5 buy_ready=False sector_rank=7 price=28.34 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=59.81 liquidity=7280519.0 spike=0.42
- CLHO.CA: score=17.75 buy_ready=False sector_rank=6 price=16.65 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=63.34 liquidity=5435790.5 spike=0.15
- CNFN.CA: score=22.75 buy_ready=False sector_rank=5 price=4.77 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=60.4 liquidity=10378883.0 spike=0.26
- COMI.CA: score=14.68 buy_ready=False sector_rank=17 price=131.43 support=129.8 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=50.27 liquidity=82312704.0 spike=0.14
- COPR.CA: score=12.23 buy_ready=False sector_rank=9 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=50.85 liquidity=5164481.5 spike=0.15
- COSG.CA: score=8.11 buy_ready=False sector_rank=9 price=1.52 support=1.52 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=32.35 liquidity=8042360.0 spike=0.15
- CPCI.CA: score=12.38 buy_ready=False sector_rank=9 price=373.37 support=347.11 resistance=378.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=72.05 liquidity=318248.84 spike=0.16
- CSAG.CA: score=26.4 buy_ready=False sector_rank=4 price=32.99 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=49.89 liquidity=74273464.0 spike=6.2
- DAPH.CA: score=15.99 buy_ready=False sector_rank=9 price=80.67 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:11 AM market time freshness=DELAYED_CURRENT RSI=54.9 liquidity=4924721.0 spike=0.47
- DEIN.CA: score=6.06 buy_ready=False sector_rank=9 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=11.4 buy_ready=False sector_rank=12 price=26.77 support=23.7 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=73.9 liquidity=1466127.0 spike=0.39
- DSCW.CA: score=14.06 buy_ready=False sector_rank=9 price=1.75 support=1.74 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=39.39 liquidity=16214954.0 spike=0.35
- DTPP.CA: score=1.05 buy_ready=False sector_rank=9 price=116.0 support=114.0 resistance=130.89 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=19.44 liquidity=990292.0 spike=0.87
- EALR.CA: score=6.72 buy_ready=False sector_rank=9 price=341.37 support=350.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=44.67 liquidity=1653881.88 spike=0.51
- EASB.CA: score=5.22 buy_ready=False sector_rank=9 price=7.51 support=7.5 resistance=8.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11799038.0 spike=1.08
- EAST.CA: score=9.99 buy_ready=False sector_rank=12 price=37.32 support=37.01 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=47.42 liquidity=6058114.5 spike=0.14
- EBSC.CA: score=5.37 buy_ready=False sector_rank=9 price=1.78 support=1.66 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=304624.5 spike=0.11
- ECAP.CA: score=18.37 buy_ready=False sector_rank=9 price=33.24 support=29.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=69.97 liquidity=8288587.0 spike=1.01
- EDFM.CA: score=0.45 buy_ready=False sector_rank=9 price=330.59 support=322.11 resistance=355.0 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=26.96 liquidity=384806.76 spike=0.73
- EEII.CA: score=11.9 buy_ready=False sector_rank=9 price=2.4 support=2.3 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=53.45 liquidity=3833005.0 spike=0.28
- EFIC.CA: score=-2.3 buy_ready=False sector_rank=21 price=194.01 support=192.01 resistance=213.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=15.79 liquidity=576870.56 spike=0.3
- EFID.CA: score=9.93 buy_ready=False sector_rank=12 price=26.0 support=26.67 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=27.31 liquidity=27959814.0 spike=0.39
- EFIH.CA: score=8.54 buy_ready=False sector_rank=20 price=20.58 support=20.09 resistance=22.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=41.24 liquidity=5224522.5 spike=0.11
- EGAL.CA: score=8.12 buy_ready=False sector_rank=21 price=277.68 support=280.0 resistance=334.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=10.2 liquidity=15032845.0 spike=0.2
- EGAS.CA: score=10.82 buy_ready=False sector_rank=13 price=48.09 support=48.2 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=42.15 liquidity=2963171.25 spike=0.3
- EGBE.CA: score=9.7 buy_ready=False sector_rank=17 price=0.46 support=0.43 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=65.52 liquidity=20109.76 spike=0.23
- EGCH.CA: score=5.13 buy_ready=False sector_rank=21 price=12.75 support=12.69 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=28.76 liquidity=7013871.0 spike=0.12
- EGSA.CA: score=4.88 buy_ready=False sector_rank=11 price=8.75 support=8.55 resistance=9.1 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=31.03 liquidity=17500.0 spike=1.95
- EGTS.CA: score=14.23 buy_ready=False sector_rank=10 price=16.26 support=16.7 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=46.38 liquidity=9217442.0 spike=0.1
- EHDR.CA: score=18.06 buy_ready=False sector_rank=9 price=2.5 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=44.05 liquidity=14075589.0 spike=0.25
- EKHO.CA: score=9.86 buy_ready=False sector_rank=13 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=5.76 buy_ready=False sector_rank=19 price=2.09 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=36.67 liquidity=2651081.0 spike=0.13
- ELKA.CA: score=11.31 buy_ready=False sector_rank=9 price=1.24 support=1.15 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:12 AM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=4243506.5 spike=0.1
- ELNA.CA: score=0.84 buy_ready=False sector_rank=9 price=36.1 support=36.0 resistance=41.51 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=33.65 liquidity=636226.37 spike=1.57
- ELSH.CA: score=18.06 buy_ready=False sector_rank=9 price=11.48 support=8.28 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=52.69 liquidity=10730887.0 spike=0.06
- ELWA.CA: score=9.42 buy_ready=False sector_rank=9 price=2.04 support=2.0 resistance=2.22 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=50.98 liquidity=1351612.17 spike=0.65
- EMFD.CA: score=18.01 buy_ready=False sector_rank=10 price=11.57 support=10.5 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=43.95 liquidity=22847878.0 spike=0.08
- ENGC.CA: score=6.64 buy_ready=False sector_rank=9 price=37.52 support=35.26 resistance=38.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23100322.0 spike=1.79
- EOSB.CA: score=12.11 buy_ready=False sector_rank=9 price=1.48 support=1.35 resistance=1.55 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=50716.64 spike=0.39
- EPCO.CA: score=6.14 buy_ready=False sector_rank=9 price=8.82 support=8.89 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=40.24 liquidity=1078400.88 spike=0.12
- EPPK.CA: score=13.74 buy_ready=False sector_rank=9 price=13.25 support=11.67 resistance=13.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=67.48 liquidity=1200167.63 spike=1.24
- ETEL.CA: score=16.96 buy_ready=False sector_rank=11 price=92.2 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=46.73 liquidity=17272224.0 spike=0.23
- ETRS.CA: score=22.82 buy_ready=False sector_rank=9 price=10.94 support=7.93 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=70.92 liquidity=94096976.0 spike=1.38
- EXPA.CA: score=5.63 buy_ready=False sector_rank=17 price=18.28 support=18.2 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=18.55 liquidity=5949938.0 spike=0.18
- FAIT.CA: score=8.17 buy_ready=False sector_rank=17 price=35.99 support=35.01 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:12 AM market time freshness=DELAYED_CURRENT RSI=38.43 liquidity=497265.13 spike=0.16
- FAITA.CA: score=7.71 buy_ready=False sector_rank=17 price=0.99 support=0.99 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=30973.62 spike=0.87
- FERC.CA: score=0.56 buy_ready=False sector_rank=21 price=75.14 support=75.0 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=23.06 liquidity=1436336.0 spike=0.38
- FWRY.CA: score=15.31 buy_ready=False sector_rank=20 price=18.58 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=20277676.0 spike=0.08
- GBCO.CA: score=21.4 buy_ready=False sector_rank=3 price=30.57 support=25.25 resistance=31.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=94.21 liquidity=32018482.0 spike=0.35
- GDWA.CA: score=1.36 buy_ready=False sector_rank=9 price=0.78 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:13 AM market time freshness=DELAYED_CURRENT RSI=30.95 liquidity=2293001.25 spike=0.16
- GGCC.CA: score=28.06 buy_ready=False sector_rank=9 price=0.46 support=0.4 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=52.38 liquidity=34929472.0 spike=3.96
- GIHD.CA: score=15.24 buy_ready=False sector_rank=9 price=42.32 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:11 AM market time freshness=DELAYED_CURRENT RSI=58.27 liquidity=3179458.25 spike=0.41
- GMCI.CA: score=11.77 buy_ready=False sector_rank=9 price=1.79 support=1.66 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=36.0 liquidity=601902.62 spike=1.55
- GRCA.CA: score=6.01 buy_ready=False sector_rank=9 price=51.46 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=39.48 liquidity=942070.5 spike=0.2
- GSSC.CA: score=7.02 buy_ready=False sector_rank=9 price=245.91 support=228.1 resistance=257.49 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=39.18 liquidity=1955722.26 spike=0.86
- GTWL.CA: score=23.04 buy_ready=False sector_rank=9 price=60.85 support=45.47 resistance=68.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=86.73 liquidity=46877860.0 spike=2.99
- HDBK.CA: score=16.68 buy_ready=False sector_rank=17 price=160.18 support=138.0 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=80.29 liquidity=12754332.0 spike=0.49
- HELI.CA: score=18.01 buy_ready=False sector_rank=10 price=6.45 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=52.53 liquidity=22933316.0 spike=0.17
- HRHO.CA: score=19.75 buy_ready=False sector_rank=5 price=26.96 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=57.49 liquidity=28295666.0 spike=0.2
- ICID.CA: score=14.43 buy_ready=False sector_rank=9 price=7.73 support=5.0 resistance=8.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:13 AM market time freshness=DELAYED_CURRENT RSI=80.91 liquidity=5369152.0 spike=0.33
- IDRE.CA: score=11.17 buy_ready=False sector_rank=9 price=42.76 support=42.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:59 AM market time freshness=DELAYED_CURRENT RSI=43.82 liquidity=3110167.25 spike=0.19
- IFAP.CA: score=6.51 buy_ready=False sector_rank=15 price=19.21 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:13 AM market time freshness=DELAYED_CURRENT RSI=44.94 liquidity=2739199.25 spike=0.42
- INFI.CA: score=1.27 buy_ready=False sector_rank=9 price=90.82 support=92.5 resistance=105.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=18.57 liquidity=2204715.25 spike=0.28
- IRON.CA: score=4.38 buy_ready=False sector_rank=21 price=31.2 support=30.95 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:13 AM market time freshness=DELAYED_CURRENT RSI=35.08 liquidity=2263768.25 spike=0.31
- ISMA.CA: score=20.06 buy_ready=False sector_rank=9 price=29.38 support=25.95 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=54.84 liquidity=10816494.0 spike=0.29
- ISMQ.CA: score=3.2 buy_ready=False sector_rank=21 price=9.1 support=8.6 resistance=9.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=102607536.0 spike=1.04
- ISPH.CA: score=15.32 buy_ready=False sector_rank=6 price=11.51 support=11.3 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=39.94 liquidity=67200360.0 spike=0.59
- JUFO.CA: score=14.67 buy_ready=False sector_rank=12 price=29.8 support=28.09 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=58.37 liquidity=6735419.0 spike=0.19
- KABO.CA: score=20.22 buy_ready=False sector_rank=8 price=6.38 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=38.16 liquidity=16707196.0 spike=0.97
- KWIN.CA: score=15.46 buy_ready=False sector_rank=9 price=70.93 support=65.75 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=44.26 liquidity=11501070.0 spike=1.2
- KZPC.CA: score=-0.28 buy_ready=False sector_rank=9 price=8.59 support=8.6 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=14.44 liquidity=651205.19 spike=0.1
- LCSW.CA: score=26.77 buy_ready=False sector_rank=16 price=29.79 support=26.0 resistance=31.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=70.94 liquidity=88388520.0 spike=4.56
- LUTS.CA: score=20.73 buy_ready=False sector_rank=9 price=0.72 support=0.55 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=61.21 liquidity=8664157.0 spike=0.2
- MAAL.CA: score=20.52 buy_ready=False sector_rank=9 price=7.04 support=5.16 resistance=7.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:13 AM market time freshness=DELAYED_CURRENT RSI=78.24 liquidity=28255634.0 spike=1.73
- MASR.CA: score=18.06 buy_ready=False sector_rank=9 price=6.9 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=56.89 liquidity=12595803.0 spike=0.23
- MBSC.CA: score=9.77 buy_ready=False sector_rank=16 price=235.55 support=242.0 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=34.9 liquidity=13234145.0 spike=0.36
- MCQE.CA: score=4.95 buy_ready=False sector_rank=16 price=170.58 support=166.66 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=17.86 liquidity=5175807.0 spike=0.32
- MCRO.CA: score=9.06 buy_ready=False sector_rank=9 price=1.2 support=1.2 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=11962604.0 spike=0.32
- MENA.CA: score=8.4 buy_ready=False sector_rank=10 price=6.73 support=6.22 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:06 AM market time freshness=DELAYED_CURRENT RSI=49.28 liquidity=385241.81 spike=0.03
- MEPA.CA: score=2.99 buy_ready=False sector_rank=9 price=1.55 support=1.58 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=20.0 liquidity=3925279.5 spike=0.32
- MFPC.CA: score=8.12 buy_ready=False sector_rank=21 price=34.85 support=35.15 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=8.54 liquidity=34080800.0 spike=0.4
- MFSC.CA: score=18.71 buy_ready=False sector_rank=9 price=49.93 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=56.14 liquidity=6650843.0 spike=0.73
- MHOT.CA: score=16.95 buy_ready=False sector_rank=1 price=34.16 support=28.83 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=73.12 liquidity=2546671.0 spike=0.09
- MICH.CA: score=14.2 buy_ready=False sector_rank=9 price=37.29 support=35.4 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:13 AM market time freshness=DELAYED_CURRENT RSI=54.58 liquidity=4137402.75 spike=0.27
- MILS.CA: score=9.64 buy_ready=False sector_rank=9 price=131.89 support=130.11 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:10 AM market time freshness=DELAYED_CURRENT RSI=36.62 liquidity=1578253.5 spike=0.14
- MIPH.CA: score=5.83 buy_ready=False sector_rank=6 price=630.51 support=640.0 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=46.16 liquidity=515207.41 spike=0.24
- MOED.CA: score=7.61 buy_ready=False sector_rank=9 price=0.67 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=1545502.12 spike=0.15
- MOIL.CA: score=7.92 buy_ready=False sector_rank=13 price=0.48 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=60.87 liquidity=59327.31 spike=0.33
- MOIN.CA: score=-0.4 buy_ready=False sector_rank=9 price=23.03 support=22.61 resistance=25.66 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=0.97 liquidity=535194.19 spike=0.85
- MOSC.CA: score=7.28 buy_ready=False sector_rank=9 price=253.49 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:11 AM market time freshness=DELAYED_CURRENT RSI=46.6 liquidity=2220862.25 spike=0.26
- MPCI.CA: score=22.06 buy_ready=False sector_rank=9 price=231.54 support=204.36 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=60.69 liquidity=27413660.0 spike=0.29
- MPCO.CA: score=17.77 buy_ready=False sector_rank=15 price=1.82 support=1.58 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=54.84 liquidity=12716626.0 spike=0.12
- MPRC.CA: score=20.68 buy_ready=False sector_rank=9 price=39.65 support=31.1 resistance=38.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=75.37 liquidity=69081120.0 spike=1.81
- MTIE.CA: score=15.12 buy_ready=False sector_rank=3 price=8.97 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:12 AM market time freshness=DELAYED_CURRENT RSI=51.52 liquidity=4720920.0 spike=0.3
- NAHO.CA: score=6.37 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=60.0 liquidity=24189.78 spike=1.14
- NCCW.CA: score=15.08 buy_ready=False sector_rank=9 price=6.14 support=5.29 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=51.67 liquidity=7015773.0 spike=0.22
- NEDA.CA: score=0.18 buy_ready=False sector_rank=9 price=2.74 support=2.68 resistance=2.84 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=28.57 liquidity=117806.3 spike=0.32
- NHPS.CA: score=5.26 buy_ready=False sector_rank=9 price=63.22 support=61.62 resistance=68.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:12 AM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=1195228.75 spike=0.3
- NINH.CA: score=13.81 buy_ready=False sector_rank=9 price=18.0 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=49.07 liquidity=4545768.5 spike=1.1
- NIPH.CA: score=13.32 buy_ready=False sector_rank=6 price=160.82 support=157.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=32.48 liquidity=10160882.0 spike=0.14
- OBRI.CA: score=8.43 buy_ready=False sector_rank=9 price=33.05 support=33.55 resistance=37.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=45.44 liquidity=3365307.25 spike=0.25
- OCDI.CA: score=20.83 buy_ready=False sector_rank=10 price=24.4 support=20.0 resistance=25.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:13 AM market time freshness=DELAYED_CURRENT RSI=76.51 liquidity=122456720.0 spike=1.91
- OCPH.CA: score=6.49 buy_ready=False sector_rank=9 price=343.01 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=36.11 liquidity=1422385.5 spike=0.23
- ODIN.CA: score=11.94 buy_ready=False sector_rank=9 price=2.09 support=1.91 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=51.67 liquidity=3878364.25 spike=0.36
- OFH.CA: score=2.93 buy_ready=False sector_rank=9 price=0.59 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=24.36 liquidity=3861024.0 spike=0.2
- OIH.CA: score=16.78 buy_ready=False sector_rank=14 price=1.4 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=58.62 liquidity=14228108.0 spike=0.17
- OLFI.CA: score=10.67 buy_ready=False sector_rank=12 price=21.58 support=21.39 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:13 AM market time freshness=DELAYED_CURRENT RSI=51.8 liquidity=5736601.5 spike=0.29
- ORAS.CA: score=4.6 buy_ready=False sector_rank=18 price=692.14 support=680.0 resistance=732.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=307902240.0 spike=1.0
- ORHD.CA: score=20.01 buy_ready=False sector_rank=10 price=38.54 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=60.63 liquidity=99529456.0 spike=0.57
- ORWE.CA: score=11.2 buy_ready=False sector_rank=8 price=22.55 support=22.61 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=7981888.5 spike=0.22
- PHAR.CA: score=13.83 buy_ready=False sector_rank=6 price=87.23 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:13 AM market time freshness=DELAYED_CURRENT RSI=59.17 liquidity=1516756.0 spike=0.04
- PHDC.CA: score=18.01 buy_ready=False sector_rank=10 price=14.76 support=14.43 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=54.93 liquidity=143107856.0 spike=0.35
- PHTV.CA: score=13.47 buy_ready=False sector_rank=9 price=257.91 support=201.55 resistance=256.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=85.23 liquidity=6403127.5 spike=0.32
- POUL.CA: score=21.93 buy_ready=False sector_rank=12 price=39.13 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=55.39 liquidity=10035090.0 spike=0.27
- PRCL.CA: score=19.77 buy_ready=False sector_rank=16 price=30.82 support=22.02 resistance=32.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=67.99 liquidity=21139754.0 spike=0.54
- PRDC.CA: score=20.01 buy_ready=False sector_rank=10 price=7.0 support=5.7 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=63.47 liquidity=22105552.0 spike=0.19
- PRMH.CA: score=14.99 buy_ready=False sector_rank=9 price=2.5 support=2.26 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=38.0 liquidity=6930223.5 spike=0.23
- RACC.CA: score=7.93 buy_ready=False sector_rank=9 price=9.77 support=9.38 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=2870355.5 spike=0.3
- RAKT.CA: score=6.13 buy_ready=False sector_rank=9 price=23.11 support=22.0 resistance=24.1 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=37.86 liquidity=67226.99 spike=0.28
- RAYA.CA: score=23.4 buy_ready=False sector_rank=2 price=7.38 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:13 AM market time freshness=DELAYED_CURRENT RSI=42.38 liquidity=39844388.0 spike=0.45
- RMDA.CA: score=14.95 buy_ready=False sector_rank=6 price=4.88 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=39.39 liquidity=9632125.0 spike=0.12
- ROTO.CA: score=17.82 buy_ready=False sector_rank=9 price=39.89 support=32.76 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=73.14 liquidity=7756469.5 spike=0.28
- RREI.CA: score=6.58 buy_ready=False sector_rank=9 price=3.44 support=3.35 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:09 AM market time freshness=DELAYED_CURRENT RSI=40.54 liquidity=1520863.63 spike=0.08
- RTVC.CA: score=5.18 buy_ready=False sector_rank=9 price=3.64 support=3.63 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=40.86 liquidity=1115198.38 spike=0.21
- RUBX.CA: score=29.06 buy_ready=False sector_rank=9 price=11.02 support=9.8 resistance=10.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=58.51 liquidity=44215020.0 spike=4.81
- SAUD.CA: score=1.92 buy_ready=False sector_rank=17 price=20.92 support=20.82 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:13 AM market time freshness=DELAYED_CURRENT RSI=25.28 liquidity=2248649.5 spike=0.25
- SCEM.CA: score=7.38 buy_ready=False sector_rank=16 price=62.4 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:13 AM market time freshness=DELAYED_CURRENT RSI=42.29 liquidity=2611484.5 spike=0.14
- SCFM.CA: score=1.17 buy_ready=False sector_rank=9 price=235.99 support=226.5 resistance=276.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=20.9 liquidity=1102213.63 spike=0.18
- SCTS.CA: score=1.11 buy_ready=False sector_rank=7 price=553.35 support=552.8 resistance=630.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=29.99 liquidity=885323.0 spike=0.25
- SDTI.CA: score=11.06 buy_ready=False sector_rank=9 price=47.2 support=44.03 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:06 AM market time freshness=DELAYED_CURRENT RSI=59.39 liquidity=991533.13 spike=0.08
- SEIG.CA: score=8.83 buy_ready=False sector_rank=9 price=184.82 support=179.43 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:12 AM market time freshness=DELAYED_CURRENT RSI=42.41 liquidity=765289.75 spike=0.19
- SIPC.CA: score=5.42 buy_ready=False sector_rank=9 price=3.39 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=29.09 liquidity=5353519.5 spike=0.46
- SKPC.CA: score=7.12 buy_ready=False sector_rank=21 price=15.91 support=15.9 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=31.8 liquidity=12441098.0 spike=0.33
- SMFR.CA: score=0.53 buy_ready=False sector_rank=9 price=195.1 support=192.0 resistance=214.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:13 AM market time freshness=DELAYED_CURRENT RSI=31.3 liquidity=470723.16 spike=0.2
- SNFC.CA: score=9.43 buy_ready=False sector_rank=9 price=12.01 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=68.84 liquidity=3363337.0 spike=0.17
- SPIN.CA: score=8.62 buy_ready=False sector_rank=8 price=13.96 support=13.3 resistance=14.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=45.63 liquidity=3403965.0 spike=0.6
- SPMD.CA: score=12.71 buy_ready=False sector_rank=9 price=0.42 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=49.01 liquidity=4649461.0 spike=0.19
- SUGR.CA: score=1.89 buy_ready=False sector_rank=12 price=46.9 support=47.03 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=23.54 liquidity=2956947.75 spike=0.36
- SVCE.CA: score=22.06 buy_ready=False sector_rank=9 price=9.09 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=54.92 liquidity=11278877.0 spike=0.16
- SWDY.CA: score=14.1 buy_ready=False sector_rank=19 price=85.3 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=44.21 liquidity=10476471.0 spike=0.6
- TALM.CA: score=9.96 buy_ready=False sector_rank=7 price=15.92 support=15.5 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=52.7 liquidity=1738347.63 spike=0.22
- TMGH.CA: score=18.01 buy_ready=False sector_rank=10 price=95.63 support=92.91 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=54.96 liquidity=77099608.0 spike=0.17
- TRTO.CA: score=6.06 buy_ready=False sector_rank=9 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=491.27 spike=0.67
- UEFM.CA: score=10.42 buy_ready=False sector_rank=9 price=486.78 support=465.01 resistance=505.0 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=62.58 liquidity=998385.78 spike=1.18
- UEGC.CA: score=7.59 buy_ready=False sector_rank=9 price=1.39 support=1.32 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=34.37 liquidity=4524620.0 spike=0.19
- UNIP.CA: score=11.73 buy_ready=False sector_rank=9 price=0.31 support=0.28 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=3670489.25 spike=0.16
- UNIT.CA: score=4.11 buy_ready=False sector_rank=10 price=12.96 support=12.91 resistance=15.8 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=33.47 liquidity=1097919.36 spike=0.18
- WCDF.CA: score=5.24 buy_ready=False sector_rank=9 price=531.95 support=450.0 resistance=547.9 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=43.92 liquidity=179267.15 spike=0.69
- WKOL.CA: score=0.78 buy_ready=False sector_rank=9 price=278.86 support=284.0 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=34.43 liquidity=720340.94 spike=0.25
- ZEOT.CA: score=20.06 buy_ready=False sector_rank=9 price=10.84 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=67.52 liquidity=18549634.0 spike=0.73
- ZMID.CA: score=22.01 buy_ready=False sector_rank=10 price=6.4 support=5.82 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=62.07 liquidity=98887144.0 spike=0.48

## Backtesting Lite
- RUBX.CA: 180d return=0.0%, max drawdown=-21.39%, MA20>MA50 days last20=11, as_of=2026-06-24T21:00:00+00:00
- GGCC.CA: 180d return=-16.12%, max drawdown=-45.58%, MA20>MA50 days last20=19, as_of=2026-06-24T21:00:00+00:00
- LCSW.CA: 180d return=14.22%, max drawdown=-15.87%, MA20>MA50 days last20=20, as_of=2026-06-24T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- RUBX.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Rubex International for Plastic and Acrylic Manufacturing summary=Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- GGCC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Giza General - Contracting and Real Estate Investment S.A.E summary=EGX approves listing EGP 144m capital increase for Giza Contracting; Giza Contracting tests key EGP 0.51 level; Giza Contracting’s consolidated net profits leap to EGP 140m in 9M-25
  - EGX approves listing EGP 144m capital increase for Giza Contracting: https://english.mubasher.info/news/4588793/EGX-approves-listing-EGP-144m-capital-increase-for-Giza-Contracting/
  - Giza Contracting tests key EGP 0.51 level: https://english.mubasher.info/news/4563778/Giza-Contracting-tests-key-EGP-0-51-level/
  - Giza Contracting’s consolidated net profits leap to EGP 140m in 9M-25: https://english.mubasher.info/news/4530408/Giza-Contracting-s-consolidated-net-profits-leap-to-EGP-140m-in-9M-25/
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
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
- CNFN.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=543 sources=3 expected=Contact Financial Holding summary=Contact’s consolidated profits approach EGP 471m in 2025; Contact logs lower consolidated net profits at EGP 291m in 9M-25; Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem
  - Contact’s consolidated profits approach EGP 471m in 2025: https://english.mubasher.info/news/4582855/Contact-s-consolidated-profits-approach-EGP-471m-in-2025/
  - Contact logs lower consolidated net profits at EGP 291m in 9M-25: https://english.mubasher.info/news/4526894/Contact-logs-lower-consolidated-net-profits-at-EGP-291m-in-9M-25/
  - Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem: https://english.mubasher.info/news/4509412/Contact-e-money-forge-partnership-to-boost-Egypt-s-financial-ecosystem/

## Warnings
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for GGCC.CA matches the company but no source/report date was detected.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence for CSAG.CA matches the company but no source/report date was detected.
- Evidence for RAYA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for GTWL.CA matches the company but no source/report date was detected.
- Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- Evidence for CNFN.CA matches the company but appears old; latest detected date is 2025-01-01.
