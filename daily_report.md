# Telegram-First EGX Scanner Report

Scan phase: Evening tomorrow plan
Generated UTC: 2026-06-11T19:21:10.625097+00:00
Generated Cairo: 2026-06-11 22:21
Run timing: target 19:30 Cairo | generated Cairo 2026-06-11 22:21 | cron 30 16 * * 0-4
Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-06-11 22:17

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 183/190
- Top sector: Automotive & Distribution

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, June 11
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 5.0% / above MA50 30.0%
- EGX70 regime: BEARISH / above MA20 32.5% / above MA50 72.5%
- Sector breadth: 9.52%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- PRDC.CA: liquidity=1357701504.0 spike=67.57 score=26.69
- GDWA.CA: liquidity=911094208.0 spike=93.67 score=21.18
- CCAP.CA: liquidity=586168704.0 spike=0.69 score=18.37
- COMI.CA: liquidity=478139232.0 spike=0.73 score=14.5
- FWRY.CA: liquidity=287154432.0 spike=1.01 score=12.54

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The local scanner stays on HOLD because both EGX30 and EGX70 are in a bearish regime with weak breadth (≈9.5%). Defensive risk mode (no new buys) is enforced, so even top‑ranked tickets are not recommended for entry. Liquidity spikes and constructive outlooks exist, but over‑heated RSI and proximity to resistance add uncertainty for the next 1‑3 days.
- EGX30/EGX70 trends bearish, median 5‑day returns –3.4% / –2.3%, breadth below MA20/MA50.
- Defensive risk mode (DEFENSIVE_NO_NEW_BUY) blocks new positions despite constructive outlooks.
- Top tickets (PRDC, GBCO, ANFI, ISMQ, OLFI) show liquidity spikes but RSI >70 and near resistance.
- Sector breadth low; only Automotive & Distribution shows modest upside, Real Estate remains weak.
- Uncertainty remains high: market could tighten further or find short‑term support around key 20‑day levels.

## Top Liquidity Spikes
- GDWA.CA: spike=93.67 liquidity=911094208.0 outlook=NEUTRAL score=39.96 buy_ready=False
- PRDC.CA: spike=67.57 liquidity=1357701504.0 outlook=CONSTRUCTIVE score=67.22 buy_ready=False
- ANFI.CA: spike=4.63 liquidity=168343687.25 outlook=CONSTRUCTIVE score=66.96 buy_ready=False
- EFIC.CA: spike=3.6 liquidity=12530164.0 outlook=WEAK_OR_RISKY score=23.34 buy_ready=False
- ISMQ.CA: spike=3.28 liquidity=185894640.0 outlook=CONSTRUCTIVE score=63.34 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=5.47 5d=2.25% 20d=-5.56% aboveMA50=100.0%
- #2 Textiles: score=4.38 5d=-2.88% 20d=3.46% aboveMA50=75.0%
- #3 Real Estate: score=4.22 5d=-3.4% 20d=3.87% aboveMA50=92.31%
- #4 Energy & Petrochemicals: score=4.14 5d=-0.59% 20d=-0.21% aboveMA50=75.0%
- #5 Investment Holding: score=3.43 5d=-5.16% 20d=9.48% aboveMA50=66.67%
- #6 Agriculture & Food Production: score=3.23 5d=0.3% 20d=-3.26% aboveMA50=50.0%
- #7 Tourism & Leisure: score=3.05 5d=-6.69% 20d=11.23% aboveMA50=100.0%
- #8 General / Verified EGX Expansion: score=2.96 5d=-0.85% 20d=-1.43% aboveMA50=60.58%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- EGAS.CA: BULLISH_WATCH score=91.14 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- MPCI.CA: BULLISH_WATCH score=90.96 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- KABO.CA: BULLISH_WATCH score=84.38 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ARAB.CA: BULLISH_WATCH score=84.22 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MENA.CA: BULLISH_WATCH score=84.22 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ORWE.CA: BULLISH_WATCH score=82.38 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- ACAMD.CA: BULLISH_WATCH score=78.96 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- EASB.CA: BULLISH_WATCH score=78.96 liquidity=TRADEABLE sector=IMPROVING risk=close to resistance; sector is not leading
- MICH.CA: BULLISH_WATCH score=76.96 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=overheated RSI; sector is not leading
- UNIT.CA: BULLISH_WATCH score=76.22 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=15.84 buy_ready=False sector_rank=8 price=204.13 support=195.1 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=50.99 liquidity=7660906.0 spike=0.94
- ABUK.CA: score=10.08 buy_ready=False sector_rank=14 price=76.79 support=79.0 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=20.62 liquidity=149304608.0 spike=1.27
- ACAMD.CA: score=20.5 buy_ready=False sector_rank=8 price=2.31 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=51.52 liquidity=146342992.0 spike=1.16
- ACGC.CA: score=15.75 buy_ready=False sector_rank=2 price=9.25 support=8.6 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=31.86 liquidity=24573382.0 spike=0.42
- ADCI.CA: score=21.28 buy_ready=False sector_rank=8 price=221.7 support=202.22 resistance=228.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=70.52 liquidity=10919403.0 spike=1.55
- ADIB.CA: score=14.5 buy_ready=False sector_rank=15 price=44.44 support=44.6 resistance=50.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=43.59 liquidity=61678428.0 spike=0.39
- ADPC.CA: score=10.18 buy_ready=False sector_rank=8 price=3.51 support=3.54 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=25.53 liquidity=13769443.0 spike=0.54
- AFDI.CA: score=5.18 buy_ready=False sector_rank=8 price=40.41 support=40.15 resistance=42.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11587963.0 spike=0.64
- AFMC.CA: score=9.97 buy_ready=False sector_rank=8 price=68.64 support=69.33 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=42.35 liquidity=1789582.75 spike=0.24
- AJWA.CA: score=17.18 buy_ready=False sector_rank=8 price=149.18 support=130.01 resistance=154.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=79.93 liquidity=17548738.0 spike=0.96
- ALCN.CA: score=13.98 buy_ready=False sector_rank=19 price=28.36 support=28.17 resistance=30.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=41.72 liquidity=23194862.0 spike=1.17
- ALUM.CA: score=16.79 buy_ready=False sector_rank=8 price=23.43 support=22.93 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=51.48 liquidity=6607151.5 spike=0.32
- AMER.CA: score=19.69 buy_ready=False sector_rank=3 price=2.57 support=2.43 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=55.67 liquidity=42881564.0 spike=0.38
- AMES.CA: score=0.68 buy_ready=False sector_rank=8 price=48.1 support=48.0 resistance=57.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT RSI=17.32 liquidity=1493940.75 spike=0.27
- AMIA.CA: score=20.18 buy_ready=False sector_rank=8 price=9.08 support=8.54 resistance=10.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=13576843.0 spike=0.49
- AMOC.CA: score=15.66 buy_ready=False sector_rank=4 price=7.97 support=8.09 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=36.17 liquidity=73092240.0 spike=0.96
- ANFI.CA: score=24.18 buy_ready=False sector_rank=8 price=19.75 support=13.5 resistance=21.99 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=87.25 liquidity=168343687.25 spike=4.63
- APSW.CA: score=1.67 buy_ready=False sector_rank=8 price=8.63 support=8.6 resistance=9.38 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=29.21 liquidity=1328726.6 spike=1.58
- ARAB.CA: score=21.69 buy_ready=False sector_rank=3 price=0.21 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=63736640.0 spike=0.76
- ARCC.CA: score=17.19 buy_ready=False sector_rank=17 price=54.93 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=58.09 liquidity=26774792.0 spike=0.61
- AREH.CA: score=17.18 buy_ready=False sector_rank=8 price=1.49 support=1.27 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=80.65 liquidity=22532092.0 spike=0.85
- ARVA.CA: score=5.18 buy_ready=False sector_rank=8 price=11.97 support=10.3 resistance=11.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20580688.0 spike=0.86
- ASCM.CA: score=20.18 buy_ready=False sector_rank=8 price=56.8 support=47.3 resistance=59.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=71.93 liquidity=42101764.0 spike=0.59
- ASPI.CA: score=5.18 buy_ready=False sector_rank=8 price=0.31 support=0.31 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=43017132.0 spike=0.66
- ATLC.CA: score=6.15 buy_ready=False sector_rank=20 price=4.71 support=4.71 resistance=5.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=59.32 liquidity=3076979.25 spike=0.51
- ATQA.CA: score=14.14 buy_ready=False sector_rank=14 price=9.12 support=9.41 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=54.04 liquidity=50429096.0 spike=1.3
- AXPH.CA: score=9.28 buy_ready=False sector_rank=8 price=1121.01 support=1111.0 resistance=1230.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=43.08 liquidity=1096308.75 spike=0.2
- BINV.CA: score=14.93 buy_ready=False sector_rank=5 price=45.05 support=40.8 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=4555230.0 spike=0.39
- BIOC.CA: score=10.85 buy_ready=False sector_rank=8 price=69.17 support=70.0 resistance=79.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=48.95 liquidity=2664630.5 spike=0.41
- BTFH.CA: score=12.07 buy_ready=False sector_rank=20 price=2.98 support=3.03 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=49.06 liquidity=147276944.0 spike=0.62
- CAED.CA: score=11.98 buy_ready=False sector_rank=8 price=67.98 support=70.41 resistance=84.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=36.79 liquidity=3800008.5 spike=0.27
- CANA.CA: score=14.51 buy_ready=False sector_rank=15 price=35.79 support=34.07 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=63.4 liquidity=6010612.5 spike=0.41
- CCAP.CA: score=18.37 buy_ready=False sector_rank=5 price=5.14 support=4.7 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=48.45 liquidity=586168704.0 spike=0.69
- CCRS.CA: score=17.33 buy_ready=False sector_rank=8 price=2.34 support=2.16 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=9150728.0 spike=0.34
- CEFM.CA: score=4.3 buy_ready=False sector_rank=8 price=103.34 support=103.07 resistance=119.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=29.98 liquidity=1119131.13 spike=0.26
- CERA.CA: score=15.53 buy_ready=False sector_rank=8 price=1.16 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=58.33 liquidity=6347452.0 spike=0.44
- CFGH.CA: score=2.82 buy_ready=False sector_rank=8 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=18346.9 spike=2.81
- CICH.CA: score=-0.69 buy_ready=False sector_rank=20 price=11.31 support=11.5 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=23.6 liquidity=1240890.88 spike=0.27
- CIEB.CA: score=10.83 buy_ready=False sector_rank=15 price=23.3 support=23.31 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=61.73 liquidity=6322325.5 spike=0.68
- CIRA.CA: score=6.82 buy_ready=False sector_rank=10 price=25.92 support=25.62 resistance=28.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=31.87 liquidity=3751593.25 spike=0.13
- CLHO.CA: score=15.59 buy_ready=False sector_rank=9 price=14.65 support=14.8 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=40.07 liquidity=7474723.0 spike=0.22
- CNFN.CA: score=7.58 buy_ready=False sector_rank=20 price=4.36 support=4.41 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=36.51 liquidity=5510926.5 spike=0.33
- COMI.CA: score=14.5 buy_ready=False sector_rank=15 price=131.66 support=129.8 resistance=139.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=48.17 liquidity=478139232.0 spike=0.73
- COPR.CA: score=21.18 buy_ready=False sector_rank=8 price=0.36 support=0.32 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=19017712.0 spike=0.46
- COSG.CA: score=5.22 buy_ready=False sector_rank=8 price=1.56 support=1.54 resistance=1.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=66062288.0 spike=1.02
- CPCI.CA: score=6.81 buy_ready=False sector_rank=8 price=355.75 support=340.01 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=79.86 liquidity=1626411.38 spike=0.38
- CSAG.CA: score=11.6 buy_ready=False sector_rank=19 price=30.12 support=30.4 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=56.74 liquidity=8966089.0 spike=0.55
- DAPH.CA: score=5.63 buy_ready=False sector_rank=8 price=76.96 support=78.6 resistance=96.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=27.7 liquidity=6450206.0 spike=0.21
- DEIN.CA: score=6.18 buy_ready=False sector_rank=8 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=1.55 buy_ready=False sector_rank=12 price=23.91 support=24.03 resistance=26.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=25.68 liquidity=1934485.5 spike=0.75
- DSCW.CA: score=16.18 buy_ready=False sector_rank=8 price=1.74 support=1.71 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=58.33 liquidity=20771544.0 spike=0.37
- DTPP.CA: score=1.91 buy_ready=False sector_rank=8 price=119.98 support=118.03 resistance=137.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=21.74 liquidity=1724581.63 spike=0.49
- EALR.CA: score=11.14 buy_ready=False sector_rank=8 price=351.54 support=346.01 resistance=392.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT RSI=52.5 liquidity=2953344.75 spike=0.52
- EASB.CA: score=13.37 buy_ready=False sector_rank=8 price=5.1 support=4.61 resistance=5.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=1870701.63 spike=1.66
- EAST.CA: score=19.62 buy_ready=False sector_rank=12 price=38.25 support=37.01 resistance=39.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=57.19 liquidity=26737962.0 spike=0.4
- EBSC.CA: score=10.81 buy_ready=False sector_rank=8 price=1.78 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=69.23 liquidity=629499.5 spike=0.23
- ECAP.CA: score=17.12 buy_ready=False sector_rank=8 price=31.31 support=28.7 resistance=32.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=89.66 liquidity=8736540.0 spike=1.6
- EDFM.CA: score=8.67 buy_ready=False sector_rank=8 price=334.11 support=320.2 resistance=355.0 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=50.28 liquidity=490807.57 spike=0.85
- EEII.CA: score=20.18 buy_ready=False sector_rank=8 price=2.32 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=63.89 liquidity=17981122.0 spike=0.93
- EFIC.CA: score=14.54 buy_ready=False sector_rank=14 price=205.0 support=203.01 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=9.24 liquidity=12530164.0 spike=3.6
- EFID.CA: score=14.62 buy_ready=False sector_rank=12 price=27.5 support=27.49 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=51.39 liquidity=27516584.0 spike=0.36
- EFIH.CA: score=12.52 buy_ready=False sector_rank=21 price=20.43 support=20.54 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=40.71 liquidity=35305888.0 spike=0.6
- EGAL.CA: score=9.54 buy_ready=False sector_rank=14 price=308.78 support=308.87 resistance=344.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=34.63 liquidity=56128780.0 spike=0.53
- EGAS.CA: score=22.96 buy_ready=False sector_rank=4 price=50.54 support=46.51 resistance=51.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=60.58 liquidity=23997840.0 spike=2.15
- EGBE.CA: score=2.56 buy_ready=False sector_rank=15 price=0.44 support=0.44 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=28.48 liquidity=52536.37 spike=0.38
- EGCH.CA: score=17.54 buy_ready=False sector_rank=14 price=13.72 support=13.18 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=51.46 liquidity=36826260.0 spike=0.32
- EGSA.CA: score=7.17 buy_ready=False sector_rank=18 price=8.74 support=8.3 resistance=9.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=45.05 liquidity=6600.55 spike=0.4
- EGTS.CA: score=19.69 buy_ready=False sector_rank=3 price=17.93 support=13.45 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=44.07 liquidity=90015696.0 spike=0.76
- EHDR.CA: score=20.36 buy_ready=False sector_rank=8 price=2.65 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=68.82 liquidity=57702996.0 spike=1.09
- EKHO.CA: score=10.66 buy_ready=False sector_rank=4 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=15.78 buy_ready=False sector_rank=11 price=2.07 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=54.17 liquidity=27155894.0 spike=1.02
- ELKA.CA: score=19.18 buy_ready=False sector_rank=8 price=1.21 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=70.97 liquidity=34944812.0 spike=0.81
- ELNA.CA: score=10.57 buy_ready=False sector_rank=8 price=39.38 support=37.11 resistance=42.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=60.24 liquidity=387854.5 spike=0.95
- ELSH.CA: score=5.82 buy_ready=False sector_rank=8 price=13.35 support=13.1 resistance=14.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=205843488.0 spike=1.32
- ELWA.CA: score=7.91 buy_ready=False sector_rank=8 price=2.09 support=1.79 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=88.57 liquidity=723094.06 spike=0.24
- EMFD.CA: score=21.69 buy_ready=False sector_rank=3 price=11.15 support=9.83 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=70.96 liquidity=133738264.0 spike=0.54
- ENGC.CA: score=18.18 buy_ready=False sector_rank=8 price=33.53 support=32.31 resistance=35.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=66.59 liquidity=9998886.0 spike=0.72
- EOSB.CA: score=12.7 buy_ready=False sector_rank=8 price=1.48 support=1.34 resistance=1.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=300469.19 spike=2.11
- EPCO.CA: score=7.79 buy_ready=False sector_rank=8 price=8.94 support=8.56 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=2607395.5 spike=0.22
- EPPK.CA: score=5.55 buy_ready=False sector_rank=8 price=12.17 support=11.67 resistance=13.6 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=45.77 liquidity=366913.33 spike=0.35
- ETEL.CA: score=14.16 buy_ready=False sector_rank=18 price=90.19 support=92.17 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=35.34 liquidity=80062464.0 spike=0.91
- ETRS.CA: score=5.18 buy_ready=False sector_rank=8 price=8.83 support=8.77 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29819732.0 spike=0.52
- EXPA.CA: score=17.5 buy_ready=False sector_rank=15 price=18.47 support=18.34 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=51.28 liquidity=32248122.0 spike=0.83
- FAIT.CA: score=6.33 buy_ready=False sector_rank=15 price=35.21 support=34.73 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=33.41 liquidity=3830574.75 spike=0.62
- FAITA.CA: score=7.52 buy_ready=False sector_rank=15 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=60.0 liquidity=17938.8 spike=0.44
- FERC.CA: score=7.59 buy_ready=False sector_rank=14 price=76.03 support=76.5 resistance=82.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=40.99 liquidity=3050809.75 spike=0.54
- FWRY.CA: score=12.54 buy_ready=False sector_rank=21 price=17.81 support=18.01 resistance=21.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=36.41 liquidity=287154432.0 spike=1.01
- GBCO.CA: score=24.19 buy_ready=False sector_rank=1 price=27.5 support=25.25 resistance=29.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=70.7 liquidity=88772928.0 spike=0.69
- GDWA.CA: score=21.18 buy_ready=False sector_rank=8 price=0.77 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=58.51 liquidity=911094208.0 spike=93.67
- GGCC.CA: score=15.88 buy_ready=False sector_rank=8 price=0.4 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=56.76 liquidity=9260468.0 spike=1.22
- GIHD.CA: score=5.38 buy_ready=False sector_rank=8 price=39.4 support=35.15 resistance=44.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=44.34 liquidity=1197000.75 spike=0.25
- GMCI.CA: score=6.54 buy_ready=False sector_rank=8 price=1.7 support=1.68 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=51.72 liquidity=356004.44 spike=0.87
- GRCA.CA: score=7.37 buy_ready=False sector_rank=8 price=54.54 support=52.18 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=26.07 liquidity=7185209.5 spike=0.8
- GSSC.CA: score=3.56 buy_ready=False sector_rank=8 price=247.61 support=228.1 resistance=272.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=10.31 liquidity=3375704.5 spike=0.51
- GTWL.CA: score=3.24 buy_ready=False sector_rank=8 price=46.67 support=45.47 resistance=59.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=32.04 liquidity=3051220.0 spike=0.43
- HDBK.CA: score=14.5 buy_ready=False sector_rank=15 price=138.0 support=138.75 resistance=147.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=43.16 liquidity=13655173.0 spike=0.93
- HELI.CA: score=19.69 buy_ready=False sector_rank=3 price=6.32 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=51.57 liquidity=68978872.0 spike=0.41
- HRHO.CA: score=12.07 buy_ready=False sector_rank=20 price=26.06 support=26.0 resistance=29.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=48.25 liquidity=62819884.0 spike=0.37
- ICID.CA: score=17.18 buy_ready=False sector_rank=8 price=6.8 support=4.5 resistance=6.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=84.81 liquidity=13057633.0 spike=0.86
- IDRE.CA: score=14.93 buy_ready=False sector_rank=8 price=42.06 support=40.0 resistance=49.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=59.23 liquidity=6750727.0 spike=0.21
- IFAP.CA: score=9.48 buy_ready=False sector_rank=6 price=18.9 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=44.84 liquidity=5191199.0 spike=0.51
- INFI.CA: score=10.49 buy_ready=False sector_rank=8 price=97.54 support=98.0 resistance=112.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=36.87 liquidity=3302304.0 spike=0.21
- IRON.CA: score=19.54 buy_ready=False sector_rank=14 price=32.12 support=32.1 resistance=32.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=13177248.0 spike=1.0
- ISMA.CA: score=17.66 buy_ready=False sector_rank=8 price=30.39 support=22.08 resistance=30.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=90.3 liquidity=50912624.0 spike=1.24
- ISMQ.CA: score=24.1 buy_ready=False sector_rank=14 price=8.15 support=7.27 resistance=8.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=65.14 liquidity=185894640.0 spike=3.28
- ISPH.CA: score=18.12 buy_ready=False sector_rank=9 price=11.41 support=11.12 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=65.37 liquidity=100000624.0 spike=0.67
- JUFO.CA: score=19.62 buy_ready=False sector_rank=12 price=29.16 support=26.51 resistance=30.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=69.52 liquidity=33216240.0 spike=0.7
- KABO.CA: score=22.75 buy_ready=False sector_rank=2 price=6.31 support=5.92 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=57.43 liquidity=13932143.0 spike=0.67
- KWIN.CA: score=10.77 buy_ready=False sector_rank=8 price=71.02 support=69.0 resistance=80.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=48.21 liquidity=2590356.5 spike=0.6
- KZPC.CA: score=16.36 buy_ready=False sector_rank=8 price=10.52 support=10.3 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT RSI=64.0 liquidity=8177713.0 spike=0.62
- LCSW.CA: score=12.13 buy_ready=False sector_rank=17 price=26.27 support=26.16 resistance=29.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=51.65 liquidity=7937486.0 spike=0.51
- LUTS.CA: score=17.44 buy_ready=False sector_rank=8 price=0.65 support=0.54 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=75.95 liquidity=22058314.0 spike=1.13
- MAAL.CA: score=15.68 buy_ready=False sector_rank=8 price=5.64 support=4.44 resistance=6.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=90.42 liquidity=8495915.0 spike=0.63
- MASR.CA: score=18.42 buy_ready=False sector_rank=8 price=6.6 support=6.63 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=51.38 liquidity=71947064.0 spike=1.12
- MBSC.CA: score=12.19 buy_ready=False sector_rank=17 price=271.72 support=261.52 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=24.23 liquidity=36988000.0 spike=0.77
- MCQE.CA: score=14.49 buy_ready=False sector_rank=17 price=174.2 support=179.0 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=35.24 liquidity=22244824.0 spike=1.15
- MCRO.CA: score=14.18 buy_ready=False sector_rank=8 price=1.21 support=1.21 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=30425516.0 spike=0.39
- MENA.CA: score=15.84 buy_ready=False sector_rank=3 price=6.64 support=5.83 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=59.57 liquidity=4150221.75 spike=0.25
- MEPA.CA: score=18.18 buy_ready=False sector_rank=8 price=1.68 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=11857513.0 spike=0.63
- MFPC.CA: score=10.62 buy_ready=False sector_rank=14 price=39.95 support=41.05 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=28.94 liquidity=125395248.0 spike=1.54
- MFSC.CA: score=13.18 buy_ready=False sector_rank=8 price=44.17 support=43.0 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=15.3 liquidity=11869266.0 spike=0.77
- MHOT.CA: score=15.06 buy_ready=False sector_rank=7 price=29.18 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=40.87 liquidity=6836076.5 spike=0.32
- MICH.CA: score=21.28 buy_ready=False sector_rank=8 price=36.58 support=35.01 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=83.56 liquidity=27108408.0 spike=2.05
- MILS.CA: score=20.18 buy_ready=False sector_rank=8 price=140.36 support=127.01 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=49.5 liquidity=11915673.0 spike=0.6
- MIPH.CA: score=9.0 buy_ready=False sector_rank=9 price=654.02 support=640.0 resistance=729.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=55.79 liquidity=880256.19 spike=0.28
- MOED.CA: score=8.17 buy_ready=False sector_rank=8 price=0.67 support=0.68 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=33.78 liquidity=8986922.0 spike=0.7
- MOIL.CA: score=8.83 buy_ready=False sector_rank=4 price=0.47 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=62.86 liquidity=177500.72 spike=0.93
- MOIN.CA: score=9.84 buy_ready=False sector_rank=8 price=25.01 support=24.02 resistance=26.4 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=55.47 liquidity=656687.58 spike=0.4
- MOSC.CA: score=5.63 buy_ready=False sector_rank=8 price=248.51 support=252.0 resistance=320.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=21.91 liquidity=2444443.0 spike=0.22
- MPCI.CA: score=24.08 buy_ready=False sector_rank=8 price=214.1 support=197.0 resistance=238.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=60.61 liquidity=172313280.0 spike=1.95
- MPCO.CA: score=19.29 buy_ready=False sector_rank=6 price=1.71 support=1.54 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=65.38 liquidity=38023468.0 spike=0.51
- MPRC.CA: score=19.69 buy_ready=False sector_rank=8 price=31.89 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=62.67 liquidity=9502242.0 spike=0.43
- MTIE.CA: score=22.19 buy_ready=False sector_rank=1 price=8.72 support=8.71 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=52.42 liquidity=17506584.0 spike=0.89
- NAHO.CA: score=4.19 buy_ready=False sector_rank=8 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=6384.48 spike=0.17
- NCCW.CA: score=17.18 buy_ready=False sector_rank=8 price=6.24 support=5.13 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=78.64 liquidity=17248734.0 spike=0.66
- NEDA.CA: score=8.69 buy_ready=False sector_rank=8 price=2.75 support=2.65 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=503533.88 spike=0.75
- NHPS.CA: score=7.79 buy_ready=False sector_rank=8 price=67.39 support=67.0 resistance=73.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=40.75 liquidity=3609312.0 spike=0.42
- NINH.CA: score=1.57 buy_ready=False sector_rank=8 price=16.84 support=17.0 resistance=20.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=31.1 liquidity=1388563.88 spike=0.15
- NIPH.CA: score=18.12 buy_ready=False sector_rank=9 price=159.67 support=155.1 resistance=183.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=57.19 liquidity=49226580.0 spike=0.44
- OBRI.CA: score=17.18 buy_ready=False sector_rank=8 price=34.21 support=33.63 resistance=39.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=45.72 liquidity=10775884.0 spike=0.87
- OCDI.CA: score=16.69 buy_ready=False sector_rank=3 price=20.08 support=20.19 resistance=23.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=29044048.0 spike=0.7
- OCPH.CA: score=14.36 buy_ready=False sector_rank=8 price=345.29 support=346.01 resistance=409.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=40.19 liquidity=6179110.0 spike=0.72
- ODIN.CA: score=18.46 buy_ready=False sector_rank=8 price=2.03 support=1.89 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=8277566.5 spike=0.78
- OFH.CA: score=14.18 buy_ready=False sector_rank=8 price=0.6 support=0.6 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=46.94 liquidity=10186557.0 spike=0.45
- OIH.CA: score=10.37 buy_ready=False sector_rank=5 price=1.34 support=1.35 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=29.63 liquidity=43088096.0 spike=0.4
- OLFI.CA: score=23.66 buy_ready=False sector_rank=12 price=22.1 support=21.0 resistance=22.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=74.37 liquidity=57879856.0 spike=3.02
- ORAS.CA: score=4.6 buy_ready=False sector_rank=13 price=740.05 support=731.0 resistance=761.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=247293904.0 spike=1.0
- ORHD.CA: score=17.69 buy_ready=False sector_rank=3 price=35.94 support=33.0 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=138829120.0 spike=0.73
- ORWE.CA: score=22.75 buy_ready=False sector_rank=2 price=23.0 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=67.82 liquidity=35471000.0 spike=0.78
- PHAR.CA: score=18.12 buy_ready=False sector_rank=9 price=84.58 support=83.96 resistance=92.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=55.91 liquidity=13108931.0 spike=0.39
- PHDC.CA: score=19.69 buy_ready=False sector_rank=3 price=14.47 support=13.01 resistance=16.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=64.91 liquidity=134749152.0 spike=0.34
- PHTV.CA: score=6.39 buy_ready=False sector_rank=8 price=202.9 support=203.25 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=23.43 liquidity=3204896.75 spike=0.22
- POUL.CA: score=17.62 buy_ready=False sector_rank=12 price=35.48 support=34.8 resistance=39.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=55.22 liquidity=19166362.0 spike=0.41
- PRCL.CA: score=21.19 buy_ready=False sector_rank=17 price=23.99 support=21.01 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=64.89 liquidity=21348190.0 spike=0.72
- PRDC.CA: score=26.69 buy_ready=False sector_rank=3 price=6.26 support=5.3 resistance=6.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=70.63 liquidity=1357701504.0 spike=67.57
- PRMH.CA: score=20.2 buy_ready=False sector_rank=8 price=2.63 support=2.19 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=69.7 liquidity=15261683.0 spike=1.01
- RACC.CA: score=18.18 buy_ready=False sector_rank=8 price=9.66 support=9.54 resistance=10.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=44.06 liquidity=11301922.0 spike=0.76
- RAKT.CA: score=9.23 buy_ready=False sector_rank=8 price=23.11 support=22.1 resistance=25.0 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=44.98 liquidity=562312.53 spike=2.24
- RAYA.CA: score=17.29 buy_ready=False sector_rank=16 price=6.92 support=6.9 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=45.3 liquidity=75116520.0 spike=0.68
- RMDA.CA: score=18.12 buy_ready=False sector_rank=9 price=5.0 support=4.95 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=51.7 liquidity=27394944.0 spike=0.26
- ROTO.CA: score=18.0 buy_ready=False sector_rank=8 price=33.32 support=32.66 resistance=36.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=49.82 liquidity=7820469.5 spike=0.59
- RREI.CA: score=13.31 buy_ready=False sector_rank=8 price=3.39 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=51.43 liquidity=8125994.5 spike=0.34
- RTVC.CA: score=9.91 buy_ready=False sector_rank=8 price=3.84 support=3.75 resistance=4.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=54.41 liquidity=2726274.0 spike=0.4
- RUBX.CA: score=9.03 buy_ready=False sector_rank=8 price=9.87 support=9.8 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=42.75 liquidity=4843145.0 spike=0.34
- SAUD.CA: score=14.84 buy_ready=False sector_rank=15 price=21.4 support=21.4 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=39.95 liquidity=16006459.0 spike=1.17
- SCEM.CA: score=8.19 buy_ready=False sector_rank=17 price=59.96 support=61.05 resistance=72.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=32.48 liquidity=22357470.0 spike=0.57
- SCFM.CA: score=4.37 buy_ready=False sector_rank=8 price=249.09 support=255.03 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=24.26 liquidity=4185979.25 spike=0.25
- SCTS.CA: score=5.17 buy_ready=False sector_rank=10 price=607.26 support=590.01 resistance=690.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=26.34 liquidity=2101099.0 spike=0.19
- SDTI.CA: score=22.92 buy_ready=False sector_rank=8 price=46.86 support=43.4 resistance=47.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=62.1 liquidity=26614794.0 spike=1.37
- SEIG.CA: score=10.36 buy_ready=False sector_rank=8 price=180.15 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=58.72 liquidity=2176355.25 spike=0.4
- SIPC.CA: score=12.37 buy_ready=False sector_rank=8 price=3.42 support=3.4 resistance=3.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=7182092.5 spike=0.45
- SKPC.CA: score=13.7 buy_ready=False sector_rank=14 price=16.41 support=16.8 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=40.44 liquidity=67623192.0 spike=1.08
- SMFR.CA: score=8.1 buy_ready=False sector_rank=8 price=195.37 support=201.0 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=37.37 liquidity=2912103.75 spike=0.49
- SNFC.CA: score=18.18 buy_ready=False sector_rank=8 price=12.27 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=43.11 liquidity=10533868.0 spike=0.39
- SPIN.CA: score=10.65 buy_ready=False sector_rank=2 price=14.04 support=13.61 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=25.23 liquidity=7038246.0 spike=1.43
- SPMD.CA: score=18.18 buy_ready=False sector_rank=8 price=0.4 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=62.77 liquidity=10558623.0 spike=0.43
- SUGR.CA: score=10.25 buy_ready=False sector_rank=12 price=48.26 support=48.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=52.18 liquidity=6637952.0 spike=0.43
- SVCE.CA: score=13.18 buy_ready=False sector_rank=8 price=8.28 support=8.41 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=31.52 liquidity=18971694.0 spike=0.17
- SWDY.CA: score=17.74 buy_ready=False sector_rank=11 price=84.19 support=85.25 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=47.96 liquidity=20740120.0 spike=0.78
- TALM.CA: score=20.78 buy_ready=False sector_rank=10 price=15.87 support=15.12 resistance=16.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=62.57 liquidity=8704228.0 spike=0.69
- TMGH.CA: score=14.69 buy_ready=False sector_rank=3 price=94.93 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=32.91 liquidity=276917568.0 spike=0.59
- TRTO.CA: score=7.16 buy_ready=False sector_rank=8 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=680.0 spike=1.49
- UEFM.CA: score=-0.02 buy_ready=False sector_rank=8 price=468.99 support=455.6 resistance=500.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT RSI=30.06 liquidity=799395.0 spike=0.72
- UEGC.CA: score=18.18 buy_ready=False sector_rank=8 price=1.37 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=14551748.0 spike=0.53
- UNIP.CA: score=16.18 buy_ready=False sector_rank=8 price=0.32 support=0.28 resistance=0.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=83.02 liquidity=16545815.0 spike=0.87
- UNIT.CA: score=11.48 buy_ready=False sector_rank=3 price=13.68 support=12.07 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=66.58 liquidity=1791131.75 spike=0.16
- WCDF.CA: score=10.36 buy_ready=False sector_rank=8 price=539.84 support=535.0 resistance=555.0 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=38.12 liquidity=577628.83 spike=1.8
- WKOL.CA: score=7.09 buy_ready=False sector_rank=8 price=291.98 support=290.0 resistance=324.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=58.14 liquidity=1907877.25 spike=0.45
- ZEOT.CA: score=20.21 buy_ready=False sector_rank=8 price=8.99 support=8.41 resistance=9.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=51.16 liquidity=9807264.0 spike=1.61
- ZMID.CA: score=21.69 buy_ready=False sector_rank=3 price=6.04 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=62.1 liquidity=167630784.0 spike=0.72

## Backtesting Lite
- PRDC.CA: 180d return=86.81%, max drawdown=-15.38%, MA20>MA50 days last20=20, as_of=2026-06-09T21:00:00+00:00
- GBCO.CA: 180d return=30.78%, max drawdown=-24.35%, MA20>MA50 days last20=20, as_of=2026-06-09T21:00:00+00:00
- ANFI.CA: 180d return=218.24%, max drawdown=-19.31%, MA20>MA50 days last20=20, as_of=2026-06-09T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- PRDC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Pioneers Properties For Urban Development summary=Evidence rejected for PRDC.CA: source text did not clearly match PRDC.CA / Pioneers Properties For Urban Development.
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- ANFI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tycoon Holding Company For Financial Investments summary=Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- ISMQ.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Iron and Steel for Mines and Quarries summary=Iron and Steel for Mines and Quarries stock stabilizes above key support after correction; Will Iron and Steel for Mines and Quarries stock hit new historical peaks?; Iron and Steel for Mines and Quarries expects EGP 448m net profit in FY24/25
  - Iron and Steel for Mines and Quarries stock stabilizes above key support after correction: https://english.mubasher.info/news/4578786/Iron-and-Steel-for-Mines-and-Quarries-stock-stabilizes-above-key-support-after-correction/
  - Will Iron and Steel for Mines and Quarries stock hit new historical peaks?: https://english.mubasher.info/news/4556956/Will-Iron-and-Steel-for-Mines-and-Quarries-stock-hit-new-historical-peaks-/
  - Iron and Steel for Mines and Quarries expects EGP 448m net profit in FY24/25: https://english.mubasher.info/news/4249734/Iron-and-Steel-for-Mines-and-Quarries-expects-EGP-448m-net-profit-in-FY24-25/
- MPCI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Memphis Pharmaceuticals & Chemical Industries summary=Evidence rejected for MPCI.CA: source text did not clearly match MPCI.CA / Memphis Pharmaceuticals & Chemical Industries.
- OLFI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Obour Land For Food Industries summary=Obour Land stock breaks through historical resistance barrier, settles at record levels – Analysis; Obour Land records over EGP 721.5m consolidated profits in 9M-24; Obour Land’s consolidated profits leap in H1-24; sales exceed EGP 3.8bn
  - Obour Land stock breaks through historical resistance barrier, settles at record levels – Analysis: https://english.mubasher.info/news/4550021/Obour-Land-stock-breaks-through-historical-resistance-barrier-settles-at-record-levels-Analysis/
  - Obour Land records over EGP 721.5m consolidated profits in 9M-24: https://english.mubasher.info/news/4353735/Obour-Land-records-over-EGP-721-5m-consolidated-profits-in-9M-24/
  - Obour Land’s consolidated profits leap in H1-24; sales exceed EGP 3.8bn: https://english.mubasher.info/news/4317274/Obour-Land-s-consolidated-profits-leap-in-H1-24-sales-exceed-EGP-3-8bn/
- EGAS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Natural Gas and Mining Project summary=Evidence rejected for EGAS.CA: source text did not clearly match EGAS.CA / Natural Gas and Mining Project.
- SDTI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=SHARM DREAMS Co. for Touristic Investment S.A.E summary=Sharm Dreams stock maintains strong uptrend - Analysis; Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis; Sharm Dreams stock hits historic level halting driving buying force
  - Sharm Dreams stock maintains strong uptrend - Analysis: https://english.mubasher.info/news/4577977/Sharm-Dreams-stock-maintains-strong-uptrend-Analysis/
  - Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis: https://english.mubasher.info/news/4547831/Sharm-Dreams-stock-is-experiencing-sideways-movement-amid-anticipation-of-next-trend-Analysis/
  - Sharm Dreams stock hits historic level halting driving buying force: https://english.mubasher.info/news/4529096/Sharm-Dreams-stock-hits-historic-level-halting-driving-buying-force/

## Warnings
- Evidence rejected for PRDC.CA: source text did not clearly match PRDC.CA / Pioneers Properties For Urban Development.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- Evidence for ISMQ.CA matches the company but no source/report date was detected.
- Evidence rejected for MPCI.CA: source text did not clearly match MPCI.CA / Memphis Pharmaceuticals & Chemical Industries.
- Evidence for OLFI.CA matches the company but no source/report date was detected.
- Evidence rejected for EGAS.CA: source text did not clearly match EGAS.CA / Natural Gas and Mining Project.
- Evidence for SDTI.CA matches the company but no source/report date was detected.
