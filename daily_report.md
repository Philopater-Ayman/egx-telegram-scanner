# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-07-01T11:22:31.022179+00:00
Generated Cairo: 2026-07-01 14:22
Run timing: target 11:00 Cairo | generated Cairo 2026-07-01 14:22 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-07-01 14:19

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 177/190
- Top sector: Technology & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, July 01
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 30.0% / above MA50 35.0%
- EGX70 regime: BEARISH / above MA20 48.72% / above MA50 66.67%
- Sector breadth: 23.81%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=587910016.0 spike=0.89 score=4.95
- NIPH.CA: liquidity=273756352.0 spike=4.0 score=10.36
- COMI.CA: liquidity=253324208.0 spike=0.43 score=15.27
- BTFH.CA: liquidity=216800784.0 spike=1.18 score=14.8
- RUBX.CA: liquidity=197481120.0 spike=10.44 score=10.28

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b-20230311:free
- Summary: EGX30 BEARISH / EGX70 BEARISH / sector breadth 23.8% / risk mode DEFENSIVE_NO_NEW_BUY; scanner flags accumulation‑spike stocks with bullish‑watch outlook but holds due to defensive regime.
- Selected tickets show accumulation‑spike liquidity and bullish‑watch outlook, yet sit near resistance with modest support distance.
- Sector breadth is low (23.8%); leading sectors are Technology, Automotive, Education, but most flagged stocks lie in non‑leading sectors.
- EGX30/EGX70 bearish trend and weak MA breadth shift risk mode to DEFENSIVE_NO_NEW_BUY, blocking new buys despite individual bullish signals.

## Top Liquidity Spikes
- DTPP.CA: spike=39.99 liquidity=145006448.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- NHPS.CA: spike=22.79 liquidity=102098624.0 outlook=BULLISH_WATCH score=85.21 buy_ready=False
- AXPH.CA: spike=14.18 liquidity=20358338.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RUBX.CA: spike=10.44 liquidity=197481120.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EBSC.CA: spike=8.21 liquidity=22328410.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Technology & Distribution: score=10.91 5d=8.17% 20d=2.67% aboveMA50=100.0%
- #2 Automotive & Distribution: score=10.56 5d=1.53% 20d=10.05% aboveMA50=100.0%
- #3 Education: score=5.74 5d=-1.75% 20d=0.67% aboveMA50=66.67%
- #4 Tourism & Leisure: score=5.59 5d=-4.44% 20d=2.64% aboveMA50=100.0%
- #5 Transportation & Logistics: score=4.85 5d=2.98% 20d=-0.3% aboveMA50=50.0%
- #6 Real Estate: score=3.66 5d=0.09% 20d=-2.39% aboveMA50=76.92%
- #7 Non-bank Financial Services: score=3.59 5d=-0.09% 20d=-1.73% aboveMA50=40.0%
- #8 Healthcare: score=3.41 5d=-0.33% 20d=-0.33% aboveMA50=66.67%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MTIE.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- OCPH.CA: BULLISH_WATCH score=91.21 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- LCSW.CA: BULLISH_WATCH score=90.08 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- SCTS.CA: BULLISH_WATCH score=88.74 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=below MA50
- NHPS.CA: BULLISH_WATCH score=85.21 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- CIRA.CA: BULLISH_WATCH score=80.74 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI
- MENA.CA: BULLISH_WATCH score=79.66 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- CNFN.CA: BULLISH_WATCH score=79.59 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- EEII.CA: BULLISH_WATCH score=79.21 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance; sector is not leading
- MASR.CA: BULLISH_WATCH score=79.21 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=12.22 buy_ready=False sector_rank=9 price=205.11 support=196.0 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=53.3 liquidity=3934384.75 spike=0.63
- ABUK.CA: score=8.65 buy_ready=False sector_rank=20 price=67.94 support=66.66 resistance=83.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=14.29 liquidity=85411496.0 spike=0.64
- ACAMD.CA: score=18.28 buy_ready=False sector_rank=9 price=2.22 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=27332022.0 spike=0.22
- ACGC.CA: score=17.05 buy_ready=False sector_rank=11 price=9.21 support=8.92 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=39.66 liquidity=8795652.0 spike=0.26
- ADCI.CA: score=17.72 buy_ready=False sector_rank=9 price=242.04 support=211.0 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=76.1 liquidity=12613669.0 spike=1.22
- ADIB.CA: score=20.27 buy_ready=False sector_rank=10 price=47.27 support=44.01 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=65.91 liquidity=61750752.0 spike=0.69
- ADPC.CA: score=8.25 buy_ready=False sector_rank=9 price=3.45 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=3961610.25 spike=0.21
- AFDI.CA: score=13.76 buy_ready=False sector_rank=9 price=44.13 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=54.95 liquidity=3478307.5 spike=0.23
- AFMC.CA: score=6.53 buy_ready=False sector_rank=9 price=70.07 support=66.0 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=46.38 liquidity=1241587.88 spike=0.54
- AJWA.CA: score=13.34 buy_ready=False sector_rank=9 price=179.41 support=132.15 resistance=190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=78.37 liquidity=8053151.5 spike=0.29
- ALCN.CA: score=9.62 buy_ready=False sector_rank=5 price=28.32 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=55.9 liquidity=3675782.25 spike=0.3
- ALUM.CA: score=2.8 buy_ready=False sector_rank=9 price=21.39 support=20.55 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=20.0 liquidity=2520577.75 spike=0.27
- AMER.CA: score=10.46 buy_ready=False sector_rank=6 price=2.42 support=2.28 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=33.78 liquidity=30488714.0 spike=0.43
- AMES.CA: score=10.28 buy_ready=False sector_rank=9 price=61.38 support=61.0 resistance=69.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=55828908.0 spike=4.57
- AMIA.CA: score=10.38 buy_ready=False sector_rank=9 price=8.67 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=45.28 liquidity=2094427.25 spike=0.17
- AMOC.CA: score=9.44 buy_ready=False sector_rank=17 price=7.75 support=7.42 resistance=8.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=34.4 liquidity=19618380.0 spike=0.41
- ANFI.CA: score=6.62 buy_ready=False sector_rank=9 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=STALE RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=4.78 buy_ready=False sector_rank=9 price=8.48 support=8.0 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=36.94 liquidity=497076.97 spike=0.54
- ARAB.CA: score=15.46 buy_ready=False sector_rank=6 price=0.21 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=63.89 liquidity=34433512.0 spike=0.43
- ARCC.CA: score=14.83 buy_ready=False sector_rank=15 price=55.5 support=53.0 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=45.61 liquidity=14028831.0 spike=0.42
- AREH.CA: score=20.28 buy_ready=False sector_rank=9 price=1.55 support=1.34 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=19246792.0 spike=0.54
- ARVA.CA: score=12.52 buy_ready=False sector_rank=9 price=10.92 support=9.82 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=46.76 liquidity=4236849.0 spike=0.13
- ASCM.CA: score=20.28 buy_ready=False sector_rank=9 price=59.42 support=49.72 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=59.92 liquidity=22821560.0 spike=0.24
- ASPI.CA: score=18.28 buy_ready=False sector_rank=9 price=0.32 support=0.27 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=45.69 liquidity=10812789.0 spike=0.15
- ATLC.CA: score=14.77 buy_ready=False sector_rank=7 price=5.24 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=62.9 liquidity=4338076.0 spike=0.65
- ATQA.CA: score=12.65 buy_ready=False sector_rank=20 price=9.49 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=46.63 liquidity=31200528.0 spike=0.93
- AXPH.CA: score=10.28 buy_ready=False sector_rank=9 price=1234.45 support=1090.02 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20358338.0 spike=14.18
- BINV.CA: score=9.05 buy_ready=False sector_rank=13 price=46.02 support=44.02 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=52.7 liquidity=1100655.88 spike=0.13
- BIOC.CA: score=9.94 buy_ready=False sector_rank=9 price=71.41 support=66.75 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=46.18 liquidity=1659725.38 spike=0.65
- BTFH.CA: score=14.8 buy_ready=False sector_rank=7 price=2.97 support=2.95 resistance=3.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=41.07 liquidity=216800784.0 spike=1.18
- CAED.CA: score=15.55 buy_ready=False sector_rank=9 price=71.33 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=53.5 liquidity=5063877.5 spike=1.1
- CANA.CA: score=8.57 buy_ready=False sector_rank=10 price=35.69 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=46.39 liquidity=1303637.38 spike=0.11
- CCAP.CA: score=4.95 buy_ready=False sector_rank=13 price=5.01 support=4.76 resistance=5.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=587910016.0 spike=0.89
- CCRS.CA: score=15.29 buy_ready=False sector_rank=9 price=2.31 support=2.18 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=37.7 liquidity=7002200.5 spike=0.47
- CEFM.CA: score=5.88 buy_ready=False sector_rank=9 price=100.23 support=95.75 resistance=109.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=35.08 liquidity=593645.88 spike=0.33
- CERA.CA: score=17.28 buy_ready=False sector_rank=9 price=1.22 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=10553826.0 spike=0.62
- CFGH.CA: score=-0.72 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=707.6 spike=0.12
- CICH.CA: score=9.42 buy_ready=False sector_rank=7 price=11.89 support=11.1 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=57.96 liquidity=1987386.88 spike=0.68
- CIEB.CA: score=14.05 buy_ready=False sector_rank=10 price=23.87 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=51.06 liquidity=3777711.0 spike=0.57
- CIRA.CA: score=21.38 buy_ready=False sector_rank=3 price=28.87 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=70.05 liquidity=26280180.0 spike=1.54
- CLHO.CA: score=20.36 buy_ready=False sector_rank=8 price=16.51 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=72.12 liquidity=31602604.0 spike=0.82
- CNFN.CA: score=22.44 buy_ready=False sector_rank=7 price=4.77 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=23442862.0 spike=0.56
- COMI.CA: score=15.27 buy_ready=False sector_rank=10 price=127.44 support=126.21 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=40.94 liquidity=253324208.0 spike=0.43
- COPR.CA: score=12.82 buy_ready=False sector_rank=9 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=43.55 liquidity=5531218.0 spike=0.21
- COSG.CA: score=10.28 buy_ready=False sector_rank=9 price=1.52 support=1.47 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=32.43 liquidity=19329810.0 spike=0.36
- CPCI.CA: score=20.33 buy_ready=False sector_rank=9 price=405.77 support=350.04 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=77.94 liquidity=7349802.0 spike=2.85
- CSAG.CA: score=22.94 buy_ready=False sector_rank=5 price=32.57 support=30.08 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=69.76 liquidity=11712052.0 spike=0.66
- DAPH.CA: score=16.47 buy_ready=False sector_rank=9 price=82.13 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=56.28 liquidity=4184883.25 spike=0.42
- DEIN.CA: score=6.28 buy_ready=False sector_rank=9 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=10.97 buy_ready=False sector_rank=12 price=27.19 support=23.7 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=80.08 liquidity=3824254.5 spike=0.95
- DSCW.CA: score=14.28 buy_ready=False sector_rank=9 price=1.73 support=1.71 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=19860318.0 spike=0.58
- DTPP.CA: score=10.28 buy_ready=False sector_rank=9 price=193.13 support=183.0 resistance=199.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=145006448.0 spike=39.99
- EALR.CA: score=2.79 buy_ready=False sector_rank=9 price=339.36 support=332.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=31.03 liquidity=2503281.75 spike=0.82
- EASB.CA: score=21.2 buy_ready=False sector_rank=9 price=7.51 support=4.66 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=72.71 liquidity=19447478.0 spike=1.46
- EAST.CA: score=14.14 buy_ready=False sector_rank=12 price=37.34 support=36.63 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=42.07 liquidity=14632393.0 spike=0.38
- EBSC.CA: score=10.28 buy_ready=False sector_rank=9 price=2.1 support=1.74 resistance=2.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22328410.0 spike=8.21
- ECAP.CA: score=18.21 buy_ready=False sector_rank=9 price=32.98 support=29.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=59.15 liquidity=7922310.5 spike=0.87
- EDFM.CA: score=0.53 buy_ready=False sector_rank=9 price=330.59 support=320.29 resistance=355.0 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=17.77 liquidity=246620.14 spike=0.52
- EEII.CA: score=22.18 buy_ready=False sector_rank=9 price=2.51 support=2.3 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=57.63 liquidity=26701768.0 spike=1.95
- EFIC.CA: score=6.37 buy_ready=False sector_rank=20 price=186.05 support=180.02 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=4.61 liquidity=5444383.0 spike=2.64
- EFID.CA: score=15.14 buy_ready=False sector_rank=12 price=27.51 support=25.5 resistance=29.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=45.86 liquidity=13244571.0 spike=0.17
- EFIH.CA: score=13.06 buy_ready=False sector_rank=21 price=20.71 support=20.0 resistance=22.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=42.98 liquidity=18764602.0 spike=0.45
- EGAL.CA: score=8.65 buy_ready=False sector_rank=20 price=284.95 support=272.28 resistance=332.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=29.65 liquidity=26859362.0 spike=0.44
- EGAS.CA: score=10.19 buy_ready=False sector_rank=17 price=49.11 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=48.29 liquidity=2742596.25 spike=0.32
- EGBE.CA: score=11.82 buy_ready=False sector_rank=10 price=0.45 support=0.43 resistance=0.47 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=55.36 liquidity=113399.07 spike=1.72
- EGCH.CA: score=8.65 buy_ready=False sector_rank=20 price=12.26 support=12.13 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=24.58 liquidity=17124562.0 spike=0.33
- EGSA.CA: score=2.04 buy_ready=False sector_rank=19 price=8.75 support=8.55 resistance=9.09 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=85.71 liquidity=446.25 spike=0.05
- EGTS.CA: score=18.46 buy_ready=False sector_rank=6 price=17.54 support=15.1 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=43.25 liquidity=46236152.0 spike=0.53
- EHDR.CA: score=18.28 buy_ready=False sector_rank=9 price=2.5 support=2.37 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=10760005.0 spike=0.18
- EKHO.CA: score=6.44 buy_ready=False sector_rank=17 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=12.58 buy_ready=False sector_rank=18 price=2.1 support=2.04 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=40.74 liquidity=9291852.0 spike=0.52
- ELKA.CA: score=24.38 buy_ready=False sector_rank=9 price=1.35 support=1.19 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=58.54 liquidity=112234856.0 spike=2.55
- ELNA.CA: score=-0.05 buy_ready=False sector_rank=9 price=37.81 support=35.55 resistance=41.51 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=33.8 liquidity=486123.19 spike=1.09
- ELSH.CA: score=13.28 buy_ready=False sector_rank=9 price=11.67 support=11.1 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=25.76 liquidity=28982728.0 spike=0.15
- ELWA.CA: score=1.12 buy_ready=False sector_rank=9 price=1.95 support=1.95 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=32.61 liquidity=834992.13 spike=0.29
- EMFD.CA: score=18.46 buy_ready=False sector_rank=6 price=11.6 support=11.11 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=51.12 liquidity=54343848.0 spike=0.19
- ENGC.CA: score=17.87 buy_ready=False sector_rank=9 price=36.43 support=33.0 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=63.74 liquidity=5582399.5 spike=0.38
- EOSB.CA: score=12.31 buy_ready=False sector_rank=9 price=1.48 support=1.39 resistance=1.55 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=28383.44 spike=0.22
- EPCO.CA: score=7.61 buy_ready=False sector_rank=9 price=8.7 support=8.5 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=40.13 liquidity=2322396.75 spike=0.29
- EPPK.CA: score=9.8 buy_ready=False sector_rank=9 price=14.13 support=11.67 resistance=13.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=80.49 liquidity=517543.88 spike=0.4
- ETEL.CA: score=14.04 buy_ready=False sector_rank=19 price=92.8 support=89.01 resistance=97.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=49.15 liquidity=13781142.0 spike=0.19
- ETRS.CA: score=22.28 buy_ready=False sector_rank=9 price=10.6 support=8.6 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=62.41 liquidity=69440824.0 spike=0.85
- EXPA.CA: score=10.27 buy_ready=False sector_rank=10 price=18.36 support=18.03 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=34.56 liquidity=21578168.0 spike=0.69
- FAIT.CA: score=11.29 buy_ready=False sector_rank=10 price=36.55 support=35.01 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=57.02 liquidity=2999102.5 spike=1.01
- FAITA.CA: score=5.28 buy_ready=False sector_rank=10 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=40.63 liquidity=14194.2 spike=0.43
- FERC.CA: score=0.2 buy_ready=False sector_rank=20 price=73.53 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=23.2 liquidity=2553830.5 spike=0.65
- FWRY.CA: score=13.06 buy_ready=False sector_rank=21 price=18.31 support=17.71 resistance=20.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=85981992.0 spike=0.36
- GBCO.CA: score=22.4 buy_ready=False sector_rank=2 price=32.0 support=25.25 resistance=32.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=89.02 liquidity=29128100.0 spike=0.31
- GDWA.CA: score=9.24 buy_ready=False sector_rank=9 price=0.76 support=0.76 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=39.5 liquidity=4957697.0 spike=0.34
- GGCC.CA: score=20.42 buy_ready=False sector_rank=9 price=0.49 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=87.0 liquidity=26065496.0 spike=2.07
- GIHD.CA: score=13.22 buy_ready=False sector_rank=9 price=42.05 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=60.39 liquidity=2938295.25 spike=0.34
- GMCI.CA: score=17.1 buy_ready=False sector_rank=9 price=1.86 support=1.66 resistance=1.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=59.26 liquidity=1338712.12 spike=2.74
- GRCA.CA: score=6.06 buy_ready=False sector_rank=9 price=52.08 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=53.45 liquidity=774446.5 spike=0.19
- GSSC.CA: score=7.38 buy_ready=False sector_rank=9 price=244.61 support=228.1 resistance=256.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=35.95 liquidity=2092958.25 spike=0.73
- GTWL.CA: score=24.28 buy_ready=False sector_rank=9 price=86.33 support=45.47 resistance=88.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=91.91 liquidity=182267552.0 spike=5.59
- HDBK.CA: score=20.27 buy_ready=False sector_rank=10 price=164.98 support=138.0 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=73.68 liquidity=29212474.0 spike=0.97
- HELI.CA: score=18.46 buy_ready=False sector_rank=6 price=6.43 support=6.28 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=50457124.0 spike=0.46
- HRHO.CA: score=17.44 buy_ready=False sector_rank=7 price=27.0 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=62.31 liquidity=64222936.0 spike=0.48
- ICID.CA: score=12.68 buy_ready=False sector_rank=9 price=8.07 support=5.5 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=78.53 liquidity=3396113.75 spike=0.19
- IDRE.CA: score=18.78 buy_ready=False sector_rank=9 price=43.76 support=41.1 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=45.21 liquidity=16352568.0 spike=1.25
- IFAP.CA: score=6.84 buy_ready=False sector_rank=14 price=19.17 support=18.47 resistance=20.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=47.66 liquidity=1003351.38 spike=0.15
- INFI.CA: score=5.35 buy_ready=False sector_rank=9 price=93.46 support=88.51 resistance=104.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=23.06 liquidity=6043635.0 spike=1.01
- IRON.CA: score=9.74 buy_ready=False sector_rank=20 price=32.22 support=30.51 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=55.6 liquidity=5089412.0 spike=0.66
- ISMA.CA: score=13.28 buy_ready=False sector_rank=9 price=27.97 support=26.22 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=32.38 liquidity=14414766.0 spike=0.43
- ISMQ.CA: score=18.73 buy_ready=False sector_rank=20 price=9.29 support=7.56 resistance=9.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=72.4 liquidity=123619984.0 spike=1.04
- ISPH.CA: score=15.36 buy_ready=False sector_rank=8 price=11.58 support=11.2 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=46.42 liquidity=16290646.0 spike=0.15
- JUFO.CA: score=14.96 buy_ready=False sector_rank=12 price=29.54 support=28.5 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=51.92 liquidity=6812699.5 spike=0.21
- KABO.CA: score=20.25 buy_ready=False sector_rank=11 price=6.31 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=63.08 liquidity=10443419.0 spike=0.65
- KWIN.CA: score=9.95 buy_ready=False sector_rank=9 price=67.19 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=40.07 liquidity=5667759.5 spike=0.48
- KZPC.CA: score=1.76 buy_ready=False sector_rank=9 price=8.43 support=8.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=8.85 liquidity=2471798.75 spike=0.39
- LCSW.CA: score=26.17 buy_ready=False sector_rank=15 price=28.41 support=26.0 resistance=31.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=55.63 liquidity=96058104.0 spike=3.17
- LUTS.CA: score=18.28 buy_ready=False sector_rank=9 price=0.74 support=0.56 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=67.74 liquidity=19428380.0 spike=0.4
- MAAL.CA: score=18.41 buy_ready=False sector_rank=9 price=7.23 support=5.44 resistance=7.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=85.87 liquidity=9128813.0 spike=0.51
- MASR.CA: score=20.28 buy_ready=False sector_rank=9 price=7.28 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=60.09 liquidity=53129464.0 spike=0.84
- MBSC.CA: score=7.17 buy_ready=False sector_rank=15 price=241.04 support=222.66 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=32.85 liquidity=7342884.5 spike=0.22
- MCQE.CA: score=9.83 buy_ready=False sector_rank=15 price=170.05 support=166.66 resistance=199.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=34.8 liquidity=13721311.0 spike=1.0
- MCRO.CA: score=14.28 buy_ready=False sector_rank=9 price=1.21 support=1.17 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=12412775.0 spike=0.36
- MENA.CA: score=16.17 buy_ready=False sector_rank=6 price=6.9 support=6.41 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=5708345.5 spike=0.45
- MEPA.CA: score=3.2 buy_ready=False sector_rank=9 price=1.57 support=1.52 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=26.92 liquidity=3912760.0 spike=0.35
- MFPC.CA: score=8.65 buy_ready=False sector_rank=20 price=35.81 support=34.22 resistance=43.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=15.93 liquidity=41346192.0 spike=0.5
- MFSC.CA: score=7.68 buy_ready=False sector_rank=9 price=49.43 support=47.0 resistance=53.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17521846.0 spike=2.2
- MHOT.CA: score=21.24 buy_ready=False sector_rank=4 price=34.07 support=28.83 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=68.18 liquidity=10356236.0 spike=0.56
- MICH.CA: score=15.33 buy_ready=False sector_rank=9 price=37.53 support=34.0 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=51.63 liquidity=5050104.5 spike=0.33
- MILS.CA: score=9.17 buy_ready=False sector_rank=9 price=129.29 support=126.31 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=36.79 liquidity=3881347.0 spike=0.42
- MIPH.CA: score=8.74 buy_ready=False sector_rank=8 price=658.5 support=630.13 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=49.25 liquidity=380009.91 spike=0.22
- MOED.CA: score=10.65 buy_ready=False sector_rank=9 price=0.68 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=48.63 liquidity=4370779.5 spike=0.47
- MOIL.CA: score=7.53 buy_ready=False sector_rank=17 price=0.48 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=50.94 liquidity=90207.51 spike=0.46
- MOIN.CA: score=4.82 buy_ready=False sector_rank=9 price=23.73 support=22.6 resistance=25.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=39.45 liquidity=533273.69 spike=0.53
- MOSC.CA: score=8.4 buy_ready=False sector_rank=9 price=267.99 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=53.87 liquidity=3111499.0 spike=0.33
- MPCI.CA: score=20.78 buy_ready=False sector_rank=9 price=246.35 support=204.36 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=59.99 liquidity=121822640.0 spike=1.25
- MPCO.CA: score=17.83 buy_ready=False sector_rank=14 price=1.84 support=1.6 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=58.21 liquidity=28401736.0 spike=0.26
- MPRC.CA: score=19.28 buy_ready=False sector_rank=9 price=38.71 support=31.15 resistance=40.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=85.5 liquidity=25408616.0 spike=0.58
- MTIE.CA: score=25.96 buy_ready=False sector_rank=2 price=9.35 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=52.89 liquidity=37938948.0 spike=2.28
- NAHO.CA: score=10.17 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=84760.25 spike=2.9
- NCCW.CA: score=16.7 buy_ready=False sector_rank=9 price=6.14 support=5.29 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=41.86 liquidity=8419988.0 spike=0.25
- NEDA.CA: score=6.24 buy_ready=False sector_rank=9 price=2.75 support=2.68 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=500130.84 spike=1.23
- NHPS.CA: score=29.28 buy_ready=False sector_rank=9 price=68.0 support=61.55 resistance=71.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=62.04 liquidity=102098624.0 spike=22.79
- NINH.CA: score=23.76 buy_ready=False sector_rank=9 price=18.19 support=16.8 resistance=18.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=71.37 liquidity=14818100.0 spike=2.74
- NIPH.CA: score=10.36 buy_ready=False sector_rank=8 price=178.55 support=165.0 resistance=181.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=273756352.0 spike=4.0
- OBRI.CA: score=10.28 buy_ready=False sector_rank=9 price=34.52 support=33.12 resistance=36.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=76693352.0 spike=5.16
- OCDI.CA: score=18.22 buy_ready=False sector_rank=6 price=25.48 support=20.0 resistance=25.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=76.98 liquidity=107714472.0 spike=1.38
- OCPH.CA: score=21.56 buy_ready=False sector_rank=9 price=359.0 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=51.93 liquidity=10473033.0 spike=1.64
- ODIN.CA: score=20.28 buy_ready=False sector_rank=9 price=2.18 support=1.99 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=53.66 liquidity=10638027.0 spike=0.96
- OFH.CA: score=14.28 buy_ready=False sector_rank=9 price=0.6 support=0.57 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=38.57 liquidity=10630986.0 spike=0.56
- OIH.CA: score=18.95 buy_ready=False sector_rank=13 price=1.41 support=1.33 resistance=1.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=63.16 liquidity=60813152.0 spike=0.8
- OLFI.CA: score=20.14 buy_ready=False sector_rank=12 price=22.01 support=21.0 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=58.59 liquidity=18387042.0 spike=0.87
- ORAS.CA: score=4.6 buy_ready=False sector_rank=16 price=727.64 support=721.31 resistance=733.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=134229856.0 spike=1.0
- ORHD.CA: score=20.46 buy_ready=False sector_rank=6 price=38.08 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=59.76 liquidity=68872736.0 spike=0.4
- ORWE.CA: score=10.25 buy_ready=False sector_rank=11 price=22.3 support=21.95 resistance=24.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=33.9 liquidity=10969543.0 spike=0.31
- PHAR.CA: score=20.36 buy_ready=False sector_rank=8 price=88.07 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=55.96 liquidity=21270884.0 spike=0.59
- PHDC.CA: score=18.46 buy_ready=False sector_rank=6 price=14.59 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=48.46 liquidity=154512608.0 spike=0.4
- PHTV.CA: score=11.79 buy_ready=False sector_rank=9 price=272.72 support=201.55 resistance=277.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=95.04 liquidity=2508755.5 spike=0.18
- POUL.CA: score=22.52 buy_ready=False sector_rank=12 price=38.0 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=56.03 liquidity=41677404.0 spike=1.19
- PRCL.CA: score=5.51 buy_ready=False sector_rank=15 price=32.54 support=30.83 resistance=33.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=55936828.0 spike=1.34
- PRDC.CA: score=18.46 buy_ready=False sector_rank=6 price=7.66 support=5.91 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=68.88 liquidity=63099656.0 spike=0.52
- PRMH.CA: score=18.28 buy_ready=False sector_rank=9 price=2.57 support=2.34 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=42.72 liquidity=19367282.0 spike=0.62
- RACC.CA: score=13.73 buy_ready=False sector_rank=9 price=9.82 support=9.36 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=58.0 liquidity=3450180.75 spike=0.4
- RAKT.CA: score=1.16 buy_ready=False sector_rank=9 price=21.67 support=21.4 resistance=24.1 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=29.78 liquidity=456456.88 spike=1.71
- RAYA.CA: score=24.4 buy_ready=False sector_rank=1 price=7.67 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=67.29 liquidity=63495312.0 spike=0.74
- RMDA.CA: score=14.15 buy_ready=False sector_rank=8 price=4.95 support=4.81 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=42.17 liquidity=5790430.5 spike=0.08
- ROTO.CA: score=20.28 buy_ready=False sector_rank=9 price=41.06 support=33.06 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=73.17 liquidity=21397876.0 spike=0.71
- RREI.CA: score=10.49 buy_ready=False sector_rank=9 price=3.48 support=3.34 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=54.29 liquidity=5203302.5 spike=0.31
- RTVC.CA: score=6.82 buy_ready=False sector_rank=9 price=3.79 support=3.55 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=42.25 liquidity=1535552.75 spike=0.29
- RUBX.CA: score=10.28 buy_ready=False sector_rank=9 price=12.17 support=11.22 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=197481120.0 spike=10.44
- SAUD.CA: score=9.33 buy_ready=False sector_rank=10 price=21.15 support=19.99 resistance=22.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=45.19 liquidity=4063195.0 spike=0.48
- SCEM.CA: score=18.85 buy_ready=False sector_rank=15 price=63.3 support=59.3 resistance=66.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=55.52 liquidity=9014109.0 spike=0.52
- SCFM.CA: score=2.77 buy_ready=False sector_rank=9 price=238.15 support=226.5 resistance=269.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=30.05 liquidity=2488386.0 spike=0.56
- SCTS.CA: score=26.28 buy_ready=False sector_rank=3 price=604.97 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=58.45 liquidity=13701970.0 spike=3.49
- SDTI.CA: score=11.49 buy_ready=False sector_rank=9 price=46.2 support=44.35 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=46.34 liquidity=3208782.0 spike=0.28
- SEIG.CA: score=13.12 buy_ready=False sector_rank=9 price=190.27 support=180.0 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=62.3 liquidity=2835670.25 spike=0.69
- SIPC.CA: score=3.9 buy_ready=False sector_rank=9 price=3.37 support=3.25 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=3616946.0 spike=0.31
- SKPC.CA: score=7.65 buy_ready=False sector_rank=20 price=15.92 support=15.58 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=27.78 liquidity=16664369.0 spike=0.5
- SMFR.CA: score=5.68 buy_ready=False sector_rank=9 price=194.71 support=187.01 resistance=214.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=38.45 liquidity=392471.09 spike=0.2
- SNFC.CA: score=17.17 buy_ready=False sector_rank=9 price=12.05 support=11.68 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=53.47 liquidity=8881165.0 spike=0.55
- SPIN.CA: score=13.71 buy_ready=False sector_rank=11 price=14.23 support=13.3 resistance=14.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=65.52 liquidity=6337969.5 spike=1.06
- SPMD.CA: score=17.7 buy_ready=False sector_rank=9 price=0.43 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=52.7 liquidity=7418770.0 spike=0.3
- SUGR.CA: score=1.28 buy_ready=False sector_rank=12 price=46.51 support=45.31 resistance=51.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=19.88 liquidity=2133926.75 spike=0.29
- SVCE.CA: score=6.42 buy_ready=False sector_rank=9 price=9.56 support=8.96 resistance=9.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=97455824.0 spike=1.57
- SWDY.CA: score=13.45 buy_ready=False sector_rank=18 price=86.4 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=49.08 liquidity=6166833.5 spike=0.36
- TALM.CA: score=16.88 buy_ready=False sector_rank=3 price=15.88 support=15.38 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=37.76 liquidity=6579929.0 spike=0.91
- TMGH.CA: score=15.46 buy_ready=False sector_rank=6 price=94.55 support=92.1 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=50.44 liquidity=168789248.0 spike=0.46
- TRTO.CA: score=6.28 buy_ready=False sector_rank=9 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=9.74 buy_ready=False sector_rank=9 price=478.11 support=460.0 resistance=505.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=47.04 liquidity=457577.59 spike=0.44
- UEGC.CA: score=16.79 buy_ready=False sector_rank=9 price=1.44 support=1.33 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=52.78 liquidity=6505484.5 spike=0.27
- UNIP.CA: score=10.57 buy_ready=False sector_rank=9 price=0.32 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=54.44 liquidity=2288378.75 spike=0.09
- UNIT.CA: score=5.0 buy_ready=False sector_rank=6 price=12.96 support=12.0 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=30.74 liquidity=1532040.88 spike=0.23
- WCDF.CA: score=11.42 buy_ready=False sector_rank=9 price=506.44 support=450.0 resistance=547.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=37.6 liquidity=1131868.0 spike=3.58
- WKOL.CA: score=1.06 buy_ready=False sector_rank=9 price=281.27 support=273.1 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=19.72 liquidity=773160.88 spike=0.29
- ZEOT.CA: score=20.9 buy_ready=False sector_rank=9 price=11.01 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=70.13 liquidity=42106232.0 spike=1.31
- ZMID.CA: score=22.46 buy_ready=False sector_rank=6 price=6.48 support=5.96 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=63.45 liquidity=82395552.0 spike=0.38

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
- MTIE.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=MM Group For Industry and International Trade summary=Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- RAYA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=546 sources=3 expected=Raya Holding summary=Raya stock maintains bullish momentum above EGP 9; Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt; Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn
  - Raya stock maintains bullish momentum above EGP 9: https://english.mubasher.info/news/4601857/Raya-stock-maintains-bullish-momentum-above-EGP-9/
  - Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt: https://english.mubasher.info/news/4577815/Aman-Holding-MSMEDA-partner-to-inject-EGP-300m-into-SMEs-across-Egypt/
  - Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn: https://english.mubasher.info/news/4564195/Raya-Holding-s-consolidated-profits-surge-in-2025-revenues-hit-EGP-63-8bn/
- ELKA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=546 sources=3 expected=Cairo for Housing and Development Company (S.A.E) summary=Cairo for Housing’s consolidated profits near EGP 599m in 2025; Cairo Housing stock tests important demand zone; Cairo Housing unveils EGP 398m capital hike via H1-25’s share premium
  - Cairo for Housing’s consolidated profits near EGP 599m in 2025: https://english.mubasher.info/news/4579798/Cairo-for-Housing-s-consolidated-profits-near-EGP-599m-in-2025/
  - Cairo Housing stock tests important demand zone: https://english.mubasher.info/news/4547365/Cairo-Housing-stock-tests-important-demand-zone/
  - Cairo Housing unveils EGP 398m capital hike via H1-25’s share premium: https://english.mubasher.info/news/4540047/Cairo-Housing-unveils-EGP-398m-capital-hike-via-H1-25-s-share-premium/
- GTWL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Golden Textiles & Clothes Wool summary=Golden Textiles profits jump 214%; Golden Textiles OGM OKs 50 piasters/shr dividends; Golden Textiles consolidated profits down 18.5% in FY16
  - Golden Textiles profits jump 214%: https://english.mubasher.info/news/3108548/Golden-Textiles-profits-jump-214-/
  - Golden Textiles OGM OKs 50 piasters/shr dividends: https://english.mubasher.info/news/3103061/Golden-Textiles-OGM-OKs-50-piasters-shr-dividends/
  - Golden Textiles consolidated profits down 18.5% in FY16: https://english.mubasher.info/news/3092552/Golden-Textiles-consolidated-profits-down-18-5-in-FY16/
- NINH.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=546 sources=3 expected=Nozha International Hospital summary=Nozha International Hospital’s net profits cross EGP 174m in 2025; Nozha International Hospital unveils EGP 58m capital increase, new asset details; Nozha International Hospital registers EGP 11.3m block trading
  - Nozha International Hospital’s net profits cross EGP 174m in 2025: https://english.mubasher.info/news/4558517/Nozha-International-Hospital-s-net-profits-cross-EGP-174m-in-2025/
  - Nozha International Hospital unveils EGP 58m capital increase, new asset details: https://english.mubasher.info/news/4558456/Nozha-International-Hospital-unveils-EGP-58m-capital-increase-new-asset-details/
  - Nozha International Hospital registers EGP 11.3m block trading: https://english.mubasher.info/news/4056645/Nozha-International-Hospital-registers-EGP-11-3m-block-trading/

## Warnings
- Evidence rejected for NHPS.CA: source text did not clearly match NHPS.CA / National Company for Housing Professional Syndicates SAE.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for SCTS.CA matches the company but no source/report date was detected.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- Evidence for RAYA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ELKA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for GTWL.CA matches the company but no source/report date was detected.
- Evidence for NINH.CA matches the company but appears old; latest detected date is 2025-01-01.
