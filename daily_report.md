# Telegram-First EGX Scanner Report

Scan phase: Evening tomorrow plan
Generated UTC: 2026-10-20T20:06:33.395024+00:00
Generated Cairo: 2026-10-20 23:06
Run timing: target 19:30 Cairo | generated Cairo 2026-10-20 23:06 | cron 30 16 * * 0-4
Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-10-20 23:03

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 162/187
- Top sector: Telecommunications

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, October 20
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 13.33% / above MA50 13.33%
- EGX70 regime: BEARISH / above MA20 8.82% / above MA50 8.82%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=632802176.0 spike=1.13 score=17.29
- COMI.CA: liquidity=401638368.0 spike=0.79 score=13.69
- TMGH.CA: liquidity=259522976.0 spike=1.2 score=7.4
- ELEC.CA: liquidity=258827168.0 spike=7.33 score=12.65
- GBCO.CA: liquidity=233380336.0 spike=2.3 score=6.96

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- ELEC.CA: spike=7.33 liquidity=258827168.0 outlook=WEAK_OR_RISKY score=4.13 buy_ready=False
- WKOL.CA: spike=5.94 liquidity=36860092.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MENA.CA: spike=5.1 liquidity=8473816.0 outlook=NEUTRAL score=48 buy_ready=False
- POUL.CA: spike=4.15 liquidity=166880448.0 outlook=WEAK_OR_RISKY score=29 buy_ready=False
- MOSC.CA: spike=2.73 liquidity=8200939.0 outlook=NEUTRAL score=42 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=6.34 5d=-1.18% 20d=2.23% aboveMA50=100.0%
- #2 Industrial Goods & Cables: score=4.13 5d=-1.25% 20d=-7.17% aboveMA50=0.0%
- #3 Fintech & Payments: score=2.24 5d=-2.96% 20d=-1.96% aboveMA50=50.0%
- #4 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #5 Building Materials: score=1.15 5d=-0.07% 20d=-4.75% aboveMA50=0.0%
- #6 Automotive & Distribution: score=0.91 5d=-1.98% 20d=-7.01% aboveMA50=0.0%
- #7 Energy & Petrochemicals: score=0.43 5d=-1.15% 20d=-7.88% aboveMA50=33.33%
- #8 Investment Holding: score=0.08 5d=0.0% 20d=-14.64% aboveMA50=66.67%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- AMOC.CA: BULLISH_WATCH score=93.43 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- EFIH.CA: BULLISH_WATCH score=82.24 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- KZPC.CA: BULLISH_WATCH score=76 liquidity=TRADEABLE sector=LAGGING risk=sector is not leading
- ETEL.CA: BULLISH_WATCH score=74.34 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20
- CPCI.CA: CONSTRUCTIVE score=65 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- SUGR.CA: CONSTRUCTIVE score=59 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- LCSW.CA: CONSTRUCTIVE score=54.15 liquidity=TRADEABLE sector=IMPROVING risk=below MA50
- BINV.CA: CONSTRUCTIVE score=53.08 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; below MA20; sector is not leading
- ARAB.CA: CONSTRUCTIVE score=53 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; momentum is extended; far above support; sector is not leading
- SNFC.CA: CONSTRUCTIVE score=53 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; below MA20; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=10.53 buy_ready=False sector_rank=19 price=228.0 support=201.0 resistance=309.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.06 liquidity=28062810.0 spike=2.54
- ABUK.CA: score=5.43 buy_ready=False sector_rank=17 price=93.38 support=87.5 resistance=93.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=167280464.0 spike=2.28
- ACAMD.CA: score=16.73 buy_ready=False sector_rank=19 price=2.06 support=1.87 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=53092520.0 spike=1.14
- ACGC.CA: score=10.25 buy_ready=False sector_rank=9 price=13.22 support=12.5 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=6460569.5 spike=0.57
- ADCI.CA: score=3.15 buy_ready=False sector_rank=19 price=257.07 support=241.55 resistance=288.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.61 liquidity=693273.31 spike=0.35
- ADIB.CA: score=7.69 buy_ready=False sector_rank=18 price=45.69 support=43.45 resistance=53.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=29.62 liquidity=31842714.0 spike=0.44
- ADPC.CA: score=5.06 buy_ready=False sector_rank=19 price=3.1 support=2.85 resistance=4.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=31.86 liquidity=8611307.0 spike=0.64
- AFDI.CA: score=5.58 buy_ready=False sector_rank=19 price=47.08 support=41.0 resistance=54.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.69 liquidity=3124152.5 spike=0.62
- AFMC.CA: score=12.45 buy_ready=False sector_rank=19 price=127.72 support=113.12 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.01 liquidity=10669150.0 spike=0.57
- AJWA.CA: score=13.37 buy_ready=False sector_rank=19 price=221.95 support=176.0 resistance=229.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=80.01 liquidity=8919250.0 spike=0.28
- ALCN.CA: score=10.06 buy_ready=False sector_rank=13 price=32.3 support=30.19 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=46.63 liquidity=6872573.0 spike=0.26
- ALUM.CA: score=-1.09 buy_ready=False sector_rank=19 price=20.21 support=18.01 resistance=26.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.1 liquidity=2455182.75 spike=0.59
- AMER.CA: score=3.88 buy_ready=False sector_rank=15 price=4.35 support=4.19 resistance=4.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=72656360.0 spike=1.44
- AMES.CA: score=13.45 buy_ready=False sector_rank=19 price=35.52 support=32.8 resistance=54.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=37.03 liquidity=23307506.0 spike=0.3
- AMIA.CA: score=8.98 buy_ready=False sector_rank=19 price=18.28 support=17.0 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.29 liquidity=3527671.5 spike=0.2
- AMOC.CA: score=20.87 buy_ready=False sector_rank=7 price=13.62 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.16 liquidity=219032080.0 spike=1.85
- APSW.CA: score=1.78 buy_ready=False sector_rank=19 price=7.94 support=7.72 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=45.81 liquidity=332289.41 spike=0.52
- ARAB.CA: score=18.0 buy_ready=False sector_rank=15 price=0.26 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=68.6 liquidity=73637288.0 spike=0.69
- ARCC.CA: score=14.46 buy_ready=False sector_rank=5 price=67.39 support=60.01 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.83 liquidity=20370274.0 spike=0.47
- AREH.CA: score=6.47 buy_ready=False sector_rank=19 price=1.13 support=1.09 resistance=1.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=42.55 liquidity=5020621.5 spike=0.6
- ASCM.CA: score=7.23 buy_ready=False sector_rank=19 price=47.44 support=44.25 resistance=61.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=25.14 liquidity=12544652.0 spike=1.39
- ASPI.CA: score=11.45 buy_ready=False sector_rank=19 price=0.33 support=0.3 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.96 liquidity=15130060.0 spike=0.6
- ATLC.CA: score=8.23 buy_ready=False sector_rank=14 price=5.17 support=4.72 resistance=7.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.49 liquidity=5158845.5 spike=0.69
- ATQA.CA: score=12.87 buy_ready=False sector_rank=17 price=10.81 support=10.15 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=37.42 liquidity=56015780.0 spike=0.84
- AXPH.CA: score=-0.09 buy_ready=False sector_rank=19 price=1315.97 support=1200.12 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=25.29 liquidity=2453796.5 spike=0.37
- BINV.CA: score=10.56 buy_ready=False sector_rank=8 price=58.31 support=52.11 resistance=65.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=57.63 liquidity=3530691.5 spike=0.24
- BIOC.CA: score=12.45 buy_ready=False sector_rank=19 price=282.45 support=225.21 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=63.3 liquidity=32010122.0 spike=0.29
- BTFH.CA: score=12.07 buy_ready=False sector_rank=14 price=2.68 support=2.55 resistance=3.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.7 liquidity=43286020.0 spike=0.43
- CAED.CA: score=8.64 buy_ready=False sector_rank=19 price=94.16 support=90.01 resistance=132.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=40.5 liquidity=6192863.5 spike=0.76
- CANA.CA: score=8.57 buy_ready=False sector_rank=18 price=41.08 support=38.1 resistance=49.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.65 liquidity=26292944.0 spike=1.44
- CCAP.CA: score=17.29 buy_ready=False sector_rank=8 price=6.39 support=5.87 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=632802176.0 spike=1.13
- CCRS.CA: score=1.93 buy_ready=False sector_rank=19 price=1.98 support=1.88 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9213072.0 spike=1.13
- CEFM.CA: score=3.46 buy_ready=False sector_rank=19 price=127.55 support=113.0 resistance=148.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=50.13 liquidity=1007589.75 spike=0.43
- CERA.CA: score=11.45 buy_ready=False sector_rank=19 price=1.23 support=1.18 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.0 liquidity=79946048.0 spike=0.66
- CFGH.CA: score=-3.54 buy_ready=False sector_rank=19 price=0.11 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=16.67 liquidity=4237.99 spike=0.71
- CICH.CA: score=2.83 buy_ready=False sector_rank=14 price=10.84 support=9.63 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=42.43 liquidity=763060.31 spike=0.23
- CIEB.CA: score=1.93 buy_ready=False sector_rank=18 price=22.58 support=21.4 resistance=25.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.74 liquidity=5233901.5 spike=0.54
- CIRA.CA: score=1.07 buy_ready=False sector_rank=21 price=36.6 support=33.15 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=34.31 liquidity=3674335.5 spike=0.18
- CLHO.CA: score=6.88 buy_ready=False sector_rank=16 price=13.99 support=13.0 resistance=16.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.66 liquidity=19953284.0 spike=0.52
- CNFN.CA: score=14.77 buy_ready=False sector_rank=14 price=4.09 support=3.72 resistance=4.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.31 liquidity=11774166.0 spike=1.35
- COMI.CA: score=13.69 buy_ready=False sector_rank=18 price=125.83 support=120.0 resistance=133.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.67 liquidity=401638368.0 spike=0.79
- COPR.CA: score=9.85 buy_ready=False sector_rank=19 price=0.44 support=0.41 resistance=0.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.68 liquidity=7396590.0 spike=0.39
- COSG.CA: score=7.19 buy_ready=False sector_rank=19 price=1.4 support=1.29 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.51 liquidity=5742849.5 spike=0.4
- CPCI.CA: score=10.01 buy_ready=False sector_rank=19 price=586.48 support=502.25 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.79 liquidity=2561237.0 spike=0.56
- CSAG.CA: score=14.36 buy_ready=False sector_rank=13 price=34.59 support=33.68 resistance=39.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=43.82 liquidity=10422255.0 spike=1.59
- DAPH.CA: score=11.45 buy_ready=False sector_rank=19 price=85.02 support=82.0 resistance=121.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.36 liquidity=27151874.0 spike=0.64
- DEIN.CA: score=5.45 buy_ready=False sector_rank=19 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 09:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37.26 spike=0.01
- DOMT.CA: score=3.19 buy_ready=False sector_rank=11 price=23.14 support=22.5 resistance=26.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.81 liquidity=769017.19 spike=0.18
- DSCW.CA: score=6.45 buy_ready=False sector_rank=19 price=1.55 support=1.45 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.69 liquidity=10192881.0 spike=0.6
- DTPP.CA: score=12.45 buy_ready=False sector_rank=19 price=245.6 support=225.0 resistance=349.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.54 liquidity=22225320.0 spike=0.42
- EALR.CA: score=5.47 buy_ready=False sector_rank=19 price=301.24 support=270.0 resistance=384.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=29.17 liquidity=7319627.5 spike=1.85
- EASB.CA: score=4.79 buy_ready=False sector_rank=19 price=6.92 support=6.05 resistance=7.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11146540.0 spike=2.17
- EAST.CA: score=11.61 buy_ready=False sector_rank=11 price=28.76 support=27.01 resistance=32.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.84 liquidity=7187301.5 spike=0.17
- EBSC.CA: score=6.36 buy_ready=False sector_rank=19 price=1.54 support=1.33 resistance=2.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=3543336.5 spike=1.68
- ECAP.CA: score=-1.85 buy_ready=False sector_rank=19 price=28.21 support=25.7 resistance=32.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=24.82 liquidity=1702729.38 spike=0.42
- EDFM.CA: score=2.83 buy_ready=False sector_rank=19 price=387.26 support=335.2 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.38 liquidity=376018.03 spike=0.32
- EEII.CA: score=-2.59 buy_ready=False sector_rank=19 price=1.86 support=1.71 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.62 liquidity=955501.56 spike=0.11
- EFIC.CA: score=11.87 buy_ready=False sector_rank=17 price=155.67 support=140.0 resistance=194.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.21 liquidity=29828082.0 spike=0.98
- EFID.CA: score=14.42 buy_ready=False sector_rank=11 price=18.51 support=16.98 resistance=21.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=40.46 liquidity=13514863.0 spike=0.29
- EFIH.CA: score=20.9 buy_ready=False sector_rank=3 price=23.86 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=57.73 liquidity=37341756.0 spike=0.57
- EGAL.CA: score=7.87 buy_ready=False sector_rank=17 price=302.21 support=275.0 resistance=373.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.81 liquidity=70021912.0 spike=0.89
- EGAS.CA: score=1.68 buy_ready=False sector_rank=7 price=51.78 support=47.0 resistance=60.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=30.81 liquidity=2509152.0 spike=0.31
- EGBE.CA: score=2.77 buy_ready=False sector_rank=18 price=0.5 support=0.5 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=49.37 liquidity=81552.27 spike=0.62
- EGCH.CA: score=6.89 buy_ready=False sector_rank=17 price=11.82 support=10.67 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.69 liquidity=76127512.0 spike=1.01
- EGSA.CA: score=11.23 buy_ready=False sector_rank=1 price=9.03 support=8.75 resistance=9.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=34.48 liquidity=13545.0 spike=1.91
- EGTS.CA: score=3.1 buy_ready=False sector_rank=15 price=13.13 support=12.06 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=18.84 liquidity=6103518.5 spike=0.17
- EHDR.CA: score=6.47 buy_ready=False sector_rank=19 price=2.26 support=2.07 resistance=2.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.21 liquidity=5018893.0 spike=0.46
- ELEC.CA: score=12.65 buy_ready=False sector_rank=2 price=1.8 support=1.65 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=258827168.0 spike=7.33
- ELKA.CA: score=11.45 buy_ready=False sector_rank=19 price=1.49 support=1.38 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=12479459.0 spike=0.95
- ELNA.CA: score=6.19 buy_ready=False sector_rank=19 price=35.22 support=33.46 resistance=36.39 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=201352.75 spike=1.27
- ELSH.CA: score=12.93 buy_ready=False sector_rank=19 price=10.69 support=10.0 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.52 liquidity=24351666.0 spike=1.24
- ELWA.CA: score=6.46 buy_ready=False sector_rank=19 price=1.65 support=1.43 resistance=1.73 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=61.29 liquidity=6147.9 spike=0.01
- EMFD.CA: score=13.16 buy_ready=False sector_rank=15 price=12.25 support=11.2 resistance=13.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.02 liquidity=61981760.0 spike=1.08
- ENGC.CA: score=0.85 buy_ready=False sector_rank=19 price=32.59 support=30.0 resistance=45.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=4397106.0 spike=0.28
- EOSB.CA: score=5.43 buy_ready=False sector_rank=19 price=1.57 support=1.57 resistance=1.64 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=57774.43 spike=1.46
- EPCO.CA: score=2.93 buy_ready=False sector_rank=19 price=8.8 support=8.32 resistance=9.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8635805.0 spike=1.92
- EPPK.CA: score=-7.13 buy_ready=False sector_rank=19 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=22.4 buy_ready=False sector_rank=1 price=141.14 support=129.0 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.92 liquidity=142122768.0 spike=0.58
- ETRS.CA: score=1.33 buy_ready=False sector_rank=19 price=10.69 support=10.12 resistance=10.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8873448.0 spike=0.87
- EXPA.CA: score=6.69 buy_ready=False sector_rank=18 price=14.29 support=12.0 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=20.17 liquidity=21083008.0 spike=0.56
- FAIT.CA: score=5.3 buy_ready=False sector_rank=18 price=43.81 support=38.48 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.28 liquidity=2609785.25 spike=0.92
- FAITA.CA: score=5.54 buy_ready=False sector_rank=18 price=0.99 support=0.98 resistance=1.01 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=51.09 liquidity=49125.48 spike=1.4
- FERC.CA: score=-3.34 buy_ready=False sector_rank=17 price=67.63 support=64.8 resistance=68.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3767775.75 spike=1.01
- FWRY.CA: score=15.9 buy_ready=False sector_rank=3 price=18.59 support=17.5 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.29 liquidity=58672848.0 spike=0.52
- GBCO.CA: score=6.96 buy_ready=False sector_rank=6 price=27.59 support=27.18 resistance=30.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=233380336.0 spike=2.3
- GDWA.CA: score=11.47 buy_ready=False sector_rank=19 price=0.62 support=0.57 resistance=0.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.96 liquidity=18452266.0 spike=1.01
- GGCC.CA: score=12.45 buy_ready=False sector_rank=19 price=0.64 support=0.61 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=42.64 liquidity=16115886.0 spike=0.97
- GIHD.CA: score=6.45 buy_ready=False sector_rank=19 price=47.18 support=45.46 resistance=78.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=16.63 liquidity=17310804.0 spike=0.92
- GMCI.CA: score=1.51 buy_ready=False sector_rank=19 price=1.54 support=1.47 resistance=1.77 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=46.67 liquidity=62907.46 spike=0.17
- GRCA.CA: score=0.85 buy_ready=False sector_rank=19 price=29.55 support=26.91 resistance=42.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.72 liquidity=2401052.75 spike=0.35
- GSSC.CA: score=3.55 buy_ready=False sector_rank=19 price=264.03 support=246.0 resistance=322.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.32 liquidity=1100749.88 spike=0.68
- GTWL.CA: score=7.45 buy_ready=False sector_rank=19 price=121.27 support=108.1 resistance=238.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=28.0 liquidity=61691376.0 spike=0.36
- HDBK.CA: score=6.69 buy_ready=False sector_rank=18 price=96.74 support=90.26 resistance=120.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=27.11 liquidity=16220211.0 spike=0.81
- HELI.CA: score=13.02 buy_ready=False sector_rank=15 price=7.02 support=6.63 resistance=8.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.18 liquidity=78016424.0 spike=1.01
- HRHO.CA: score=14.07 buy_ready=False sector_rank=14 price=25.09 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=56.89 liquidity=30561106.0 spike=0.23
- ICID.CA: score=9.89 buy_ready=False sector_rank=19 price=17.2 support=16.0 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.24 liquidity=4434037.0 spike=0.55
- IDRE.CA: score=4.16 buy_ready=False sector_rank=19 price=41.27 support=38.17 resistance=59.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.82 liquidity=2712487.25 spike=0.36
- IFAP.CA: score=0.55 buy_ready=False sector_rank=10 price=18.23 support=17.17 resistance=20.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=29.5 liquidity=2910383.75 spike=0.45
- INFI.CA: score=16.81 buy_ready=False sector_rank=19 price=127.98 support=104.0 resistance=138.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.7 liquidity=23193818.0 spike=1.18
- IRON.CA: score=6.68 buy_ready=False sector_rank=17 price=26.3 support=24.25 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.47 liquidity=4811174.5 spike=0.47
- ISMA.CA: score=9.54 buy_ready=False sector_rank=19 price=21.62 support=18.91 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.92 liquidity=7892905.0 spike=1.1
- ISMQ.CA: score=11.87 buy_ready=False sector_rank=17 price=7.59 support=6.61 resistance=9.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.32 liquidity=12736482.0 spike=0.7
- ISPH.CA: score=6.88 buy_ready=False sector_rank=16 price=10.64 support=10.03 resistance=12.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.32 liquidity=30203218.0 spike=0.65
- JUFO.CA: score=5.74 buy_ready=False sector_rank=11 price=23.56 support=22.1 resistance=27.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.71 liquidity=8315092.0 spike=0.48
- KABO.CA: score=3.79 buy_ready=False sector_rank=9 price=7.5 support=6.75 resistance=7.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18522642.0 spike=0.82
- KWIN.CA: score=0.43 buy_ready=False sector_rank=19 price=65.25 support=58.12 resistance=93.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=24.96 liquidity=3982154.0 spike=0.52
- KZPC.CA: score=18.11 buy_ready=False sector_rank=19 price=13.5 support=12.15 resistance=14.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.56 liquidity=10349966.0 spike=1.33
- LCSW.CA: score=16.46 buy_ready=False sector_rank=5 price=33.36 support=28.86 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.66 liquidity=17308360.0 spike=0.86
- LUTS.CA: score=12.45 buy_ready=False sector_rank=19 price=0.7 support=0.63 resistance=0.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.52 liquidity=26433600.0 spike=0.47
- MAAL.CA: score=7.45 buy_ready=False sector_rank=19 price=7.84 support=7.0 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=21.8 liquidity=17841078.0 spike=0.7
- MASR.CA: score=12.45 buy_ready=False sector_rank=19 price=7.08 support=6.66 resistance=7.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.63 liquidity=18994954.0 spike=0.35
- MBSC.CA: score=14.46 buy_ready=False sector_rank=5 price=336.2 support=288.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.93 liquidity=68522648.0 spike=0.75
- MCQE.CA: score=4.46 buy_ready=False sector_rank=5 price=170.9 support=163.21 resistance=177.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=45646136.0 spike=0.76
- MCRO.CA: score=11.55 buy_ready=False sector_rank=19 price=1.34 support=1.21 resistance=1.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.6 liquidity=56051204.0 spike=1.05
- MENA.CA: score=16.47 buy_ready=False sector_rank=15 price=5.99 support=5.57 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=42.27 liquidity=8473816.0 spike=5.1
- MEPA.CA: score=6.81 buy_ready=False sector_rank=19 price=1.57 support=1.47 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=5357058.5 spike=0.64
- MFPC.CA: score=3.93 buy_ready=False sector_rank=17 price=46.4 support=43.51 resistance=46.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=86349704.0 spike=1.53
- MFSC.CA: score=-2.94 buy_ready=False sector_rank=19 price=37.93 support=33.1 resistance=49.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=20.49 liquidity=608989.81 spike=0.31
- MHOT.CA: score=12.21 buy_ready=False sector_rank=12 price=15.71 support=15.08 resistance=19.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=42.45 liquidity=16284769.0 spike=0.95
- MICH.CA: score=3.63 buy_ready=False sector_rank=19 price=42.25 support=40.4 resistance=43.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13845243.0 spike=1.59
- MILS.CA: score=4.31 buy_ready=False sector_rank=19 price=148.53 support=134.01 resistance=203.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=32.37 liquidity=6862726.5 spike=0.89
- MIPH.CA: score=4.75 buy_ready=False sector_rank=16 price=751.34 support=666.66 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.33 liquidity=1877755.75 spike=0.21
- MOED.CA: score=1.48 buy_ready=False sector_rank=19 price=0.56 support=0.52 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=33.74 liquidity=5024159.0 spike=0.31
- MOIL.CA: score=-0.75 buy_ready=False sector_rank=7 price=0.67 support=0.63 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=29.7 liquidity=79344.91 spike=0.28
- MOIN.CA: score=4.36 buy_ready=False sector_rank=19 price=29.96 support=28.71 resistance=37.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=29.55 liquidity=6908477.5 spike=0.72
- MOSC.CA: score=14.11 buy_ready=False sector_rank=19 price=262.0 support=228.05 resistance=312.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=45.56 liquidity=8200939.0 spike=2.73
- MPCI.CA: score=12.77 buy_ready=False sector_rank=19 price=304.41 support=271.0 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=35.87 liquidity=123390272.0 spike=1.16
- MPCO.CA: score=3.64 buy_ready=False sector_rank=10 price=2.05 support=1.94 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=99823528.0 spike=0.91
- MPRC.CA: score=12.45 buy_ready=False sector_rank=19 price=34.7 support=32.01 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=38.75 liquidity=13646369.0 spike=0.81
- MTIE.CA: score=15.04 buy_ready=False sector_rank=6 price=7.5 support=7.05 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.49 liquidity=34473344.0 spike=1.84
- NAHO.CA: score=2.46 buy_ready=False sector_rank=19 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=12514.3 spike=0.39
- NCCW.CA: score=6.45 buy_ready=False sector_rank=19 price=5.67 support=5.05 resistance=7.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=23.08 liquidity=12955370.0 spike=0.36
- NEDA.CA: score=-0.41 buy_ready=False sector_rank=19 price=2.6 support=2.47 resistance=2.79 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=134323.8 spike=0.21
- NHPS.CA: score=-1.3 buy_ready=False sector_rank=19 price=61.7 support=56.13 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.28 liquidity=2243235.5 spike=0.16
- NINH.CA: score=2.73 buy_ready=False sector_rank=19 price=15.38 support=14.13 resistance=21.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=20.16 liquidity=6280040.0 spike=0.53
- NIPH.CA: score=3.36 buy_ready=False sector_rank=16 price=281.21 support=280.1 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=169474512.0 spike=1.24
- OBRI.CA: score=7.45 buy_ready=False sector_rank=19 price=25.74 support=22.8 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.77 liquidity=5996803.0 spike=0.41
- OCDI.CA: score=4.52 buy_ready=False sector_rank=15 price=26.38 support=24.6 resistance=26.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=70254352.0 spike=1.76
- OCPH.CA: score=4.39 buy_ready=False sector_rank=19 price=190.76 support=185.93 resistance=246.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=42.37 liquidity=2942899.5 spike=0.87
- ODIN.CA: score=5.25 buy_ready=False sector_rank=19 price=2.22 support=1.91 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=40.18 liquidity=3801084.25 spike=0.49
- OFH.CA: score=12.45 buy_ready=False sector_rank=19 price=0.75 support=0.69 resistance=1.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.79 liquidity=20995498.0 spike=0.24
- OIH.CA: score=14.03 buy_ready=False sector_rank=8 price=1.77 support=1.7 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.02 liquidity=50904056.0 spike=0.67
- OLFI.CA: score=7.42 buy_ready=False sector_rank=11 price=20.02 support=19.4 resistance=22.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.98 liquidity=10781441.0 spike=0.66
- ORAS.CA: score=4.6 buy_ready=False sector_rank=4 price=870.07 support=851.0 resistance=875.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=127968696.0 spike=1.0
- ORHD.CA: score=9.0 buy_ready=False sector_rank=15 price=10.27 support=9.5 resistance=43.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.44 liquidity=142823216.0 spike=0.99
- ORWE.CA: score=13.79 buy_ready=False sector_rank=9 price=26.39 support=25.01 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.06 liquidity=12732736.0 spike=0.29
- PHAR.CA: score=12.88 buy_ready=False sector_rank=16 price=104.39 support=98.05 resistance=119.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=48.46 liquidity=25796444.0 spike=0.39
- PHDC.CA: score=16.16 buy_ready=False sector_rank=15 price=12.85 support=12.2 resistance=13.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.25 liquidity=139680000.0 spike=1.58
- PHTV.CA: score=5.65 buy_ready=False sector_rank=19 price=330.0 support=310.02 resistance=370.0 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=41.08 liquidity=1498200.0 spike=1.85
- POUL.CA: score=19.42 buy_ready=False sector_rank=11 price=10.04 support=9.12 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.34 liquidity=166880448.0 spike=4.15
- PRCL.CA: score=5.44 buy_ready=False sector_rank=5 price=21.63 support=20.5 resistance=22.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14724968.0 spike=1.49
- PRDC.CA: score=12.0 buy_ready=False sector_rank=15 price=6.16 support=5.72 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.88 liquidity=11971802.0 spike=0.34
- PRMH.CA: score=2.92 buy_ready=False sector_rank=19 price=2.01 support=1.8 resistance=2.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=1466586.75 spike=0.43
- RACC.CA: score=0.17 buy_ready=False sector_rank=19 price=8.6 support=8.1 resistance=8.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7377366.0 spike=1.17
- RAKT.CA: score=1.52 buy_ready=False sector_rank=19 price=22.06 support=20.26 resistance=25.08 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=49.81 liquidity=68518.36 spike=0.2
- RAYA.CA: score=9.67 buy_ready=False sector_rank=20 price=5.87 support=5.36 resistance=7.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.6 liquidity=8272816.5 spike=0.24
- RMDA.CA: score=12.92 buy_ready=False sector_rank=16 price=5.19 support=4.8 resistance=6.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.15 liquidity=28075956.0 spike=1.02
- ROTO.CA: score=0.72 buy_ready=False sector_rank=19 price=35.27 support=33.3 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.75 liquidity=4263616.5 spike=0.5
- RREI.CA: score=6.22 buy_ready=False sector_rank=19 price=3.31 support=3.21 resistance=4.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=9224645.0 spike=1.27
- RTVC.CA: score=2.62 buy_ready=False sector_rank=19 price=3.29 support=3.1 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.48 liquidity=1171338.88 spike=0.45
- RUBX.CA: score=2.53 buy_ready=False sector_rank=19 price=18.22 support=16.8 resistance=18.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=107427616.0 spike=1.04
- SAUD.CA: score=12.69 buy_ready=False sector_rank=18 price=21.08 support=20.2 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.75 liquidity=15844761.0 spike=0.73
- SCEM.CA: score=18.46 buy_ready=False sector_rank=5 price=87.52 support=74.55 resistance=95.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=60.18 liquidity=46015740.0 spike=0.73
- SCFM.CA: score=2.99 buy_ready=False sector_rank=19 price=224.18 support=200.22 resistance=275.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=35.71 liquidity=1537698.63 spike=0.85
- SCTS.CA: score=-3.07 buy_ready=False sector_rank=21 price=469.43 support=420.11 resistance=606.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.72 liquidity=526639.38 spike=0.55
- SDTI.CA: score=17.45 buy_ready=False sector_rank=19 price=83.92 support=76.1 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.03 liquidity=13935345.0 spike=0.49
- SEIG.CA: score=3.15 buy_ready=False sector_rank=19 price=199.94 support=173.1 resistance=259.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.63 liquidity=701083.75 spike=0.34
- SIPC.CA: score=17.45 buy_ready=False sector_rank=19 price=5.53 support=4.22 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=31235202.0 spike=0.55
- SKPC.CA: score=2.89 buy_ready=False sector_rank=17 price=15.7 support=15.02 resistance=15.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=71898008.0 spike=1.01
- SMFR.CA: score=4.1 buy_ready=False sector_rank=19 price=197.63 support=180.11 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=38.09 liquidity=2651865.5 spike=0.83
- SNFC.CA: score=12.23 buy_ready=False sector_rank=19 price=11.2 support=10.8 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.88 liquidity=6775546.0 spike=0.68
- SPIN.CA: score=-5.0 buy_ready=False sector_rank=9 price=14.7 support=14.0 resistance=14.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1207545.13 spike=0.22
- SPMD.CA: score=13.45 buy_ready=False sector_rank=19 price=0.38 support=0.34 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.45 liquidity=13250695.0 spike=0.9
- SUGR.CA: score=14.31 buy_ready=False sector_rank=11 price=56.99 support=50.5 resistance=59.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.05 liquidity=3889110.0 spike=0.4
- SVCE.CA: score=12.45 buy_ready=False sector_rank=19 price=9.25 support=8.41 resistance=12.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.51 liquidity=51481112.0 spike=0.66
- SWDY.CA: score=17.65 buy_ready=False sector_rank=2 price=110.82 support=101.5 resistance=127.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.46 liquidity=48246808.0 spike=0.76
- TALM.CA: score=12.4 buy_ready=False sector_rank=21 price=19.7 support=18.28 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=56.29 liquidity=10470473.0 spike=0.31
- TMGH.CA: score=7.4 buy_ready=False sector_rank=15 price=84.49 support=80.01 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.45 liquidity=259522976.0 spike=1.2
- TRTO.CA: score=-0.54 buy_ready=False sector_rank=19 price=0.06 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=78.95 liquidity=4886.31 spike=0.55
- UEFM.CA: score=1.81 buy_ready=False sector_rank=19 price=482.41 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=62.99 liquidity=354811.91 spike=0.11
- UEGC.CA: score=15.45 buy_ready=False sector_rank=19 price=1.56 support=1.34 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.98 liquidity=31683510.0 spike=0.62
- UNIP.CA: score=6.95 buy_ready=False sector_rank=19 price=0.31 support=0.29 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.14 liquidity=5498935.0 spike=0.64
- UNIT.CA: score=3.93 buy_ready=False sector_rank=15 price=16.97 support=15.6 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.03 liquidity=933629.88 spike=0.21
- WCDF.CA: score=-2.45 buy_ready=False sector_rank=19 price=501.83 support=432.5 resistance=698.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=22.51 liquidity=1093116.13 spike=0.37
- WKOL.CA: score=7.45 buy_ready=False sector_rank=19 price=275.6 support=271.0 resistance=309.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36860092.0 spike=5.94
- ZEOT.CA: score=-0.62 buy_ready=False sector_rank=19 price=11.15 support=10.74 resistance=11.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6923046.0 spike=0.9
- ZMID.CA: score=8.0 buy_ready=False sector_rank=15 price=6.95 support=6.4 resistance=8.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.98 liquidity=55108316.0 spike=0.61

## Backtesting Lite
- ETEL.CA: 180d return=78.69%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-10-18T21:00:00+00:00
- EFIH.CA: 180d return=9.97%, max drawdown=-22.68%, MA20>MA50 days last20=3, as_of=2026-10-18T21:00:00+00:00
- AMOC.CA: 180d return=96.34%, max drawdown=-16.73%, MA20>MA50 days last20=20, as_of=2026-10-18T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- AMOC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria Mineral Oils summary=AMOC achieves EGP 10.5bn consolidated sales in Q1-26; AMOC studies potential project with Germany’s SULZER; AMOC to pay out EGP 0.4/shr dividends for H2-25
  - AMOC achieves EGP 10.5bn consolidated sales in Q1-26: https://english.mubasher.info/news/4604903/AMOC-achieves-EGP-10-5bn-consolidated-sales-in-Q1-26/
  - AMOC studies potential project with Germany’s SULZER: https://english.mubasher.info/news/4586853/AMOC-studies-potential-project-with-Germany-s-SULZER/
  - AMOC to pay out EGP 0.4/shr dividends for H2-25: https://english.mubasher.info/news/4586775/AMOC-to-pay-out-EGP-0-4-shr-dividends-for-H2-25/
- POUL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Poultry summary=Cairo Poultry stock approaching historic peak – Analysis; Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA; Cairo Poultry sees EGP 871m block-trading deal
  - Cairo Poultry stock approaching historic peak – Analysis: https://english.mubasher.info/news/4539104/Cairo-Poultry-stock-approaching-historic-peak-Analysis/
  - Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA: https://english.mubasher.info/news/3962334/Cairo-Poultry-cancels-commercial-license-in-Dubai-s-JAFZA/
  - Cairo Poultry sees EGP 871m block-trading deal: https://english.mubasher.info/news/3862165/Cairo-Poultry-sees-EGP-871m-block-trading-deal/
- SCEM.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=657 sources=3 expected=Sinai Cement summary=Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn; Upward trend line ends several-day decline for Sinai Cement stock; Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25
  - Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn: https://english.mubasher.info/news/4564824/Sinai-Cement-s-consolidated-profits-fall-in-2025-net-sales-cross-EGP-9bn/
  - Upward trend line ends several-day decline for Sinai Cement stock: https://english.mubasher.info/news/4529647/Upward-trend-line-ends-several-day-decline-for-Sinai-Cement-stock/
  - Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25: https://english.mubasher.info/news/4526073/Sinai-Cement-reports-lower-consolidated-net-profits-at-EGP-1-5bn-in-9M-25/
- KZPC.CA: status=OLD_ACCEPTED latest=2024-01-01 age_days=1023 sources=3 expected=Kafr El Zayat For Pesticides & Chemicals Co.(S.A.E) summary=Kafr El Zayat to set up fund with EGP 5m capital; Kafr El Zayat Pesticides targets EGP 1.73bn sales in 2024; Kafr El Zayat Pesticides’ EGM approves stock split, capital hike
  - Kafr El Zayat to set up fund with EGP 5m capital: https://english.mubasher.info/news/4201137/Kafr-El-Zayat-to-set-up-fund-with-EGP-5m-capital/
  - Kafr El Zayat Pesticides targets EGP 1.73bn sales in 2024: https://english.mubasher.info/news/4200526/Kafr-El-Zayat-Pesticides-targets-EGP-1-73bn-sales-in-2024/
  - Kafr El Zayat Pesticides’ EGM approves stock split, capital hike: https://english.mubasher.info/news/4052937/Kafr-El-Zayat-Pesticides-EGM-approves-stock-split-capital-hike/
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- SWDY.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Elsewedy Electric summary=Elsewedy-Sinohydro JV signs contract for Rabigh 2 IPP expansion project; Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26; Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations
  - Elsewedy-Sinohydro JV signs contract for Rabigh 2 IPP expansion project: https://english.mubasher.info/news/4684693/Elsewedy-Sinohydro-JV-signs-contract-for-Rabigh-2-IPP-expansion-project/
  - Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26: https://english.mubasher.info/news/4614341/Elsewedy-Electric-s-consolidated-revenues-total-EGP-75-2bn-in-Q1-26/
  - Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations: https://english.mubasher.info/news/4593166/Elsewedy-Electric-accelerates-power-transformation-project-in-KSA-with-6-high-voltage-substations/

## Warnings
- OpenRouter API error: 404
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence for POUL.CA matches the company but no source/report date was detected.
- Evidence for SCEM.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for KZPC.CA matches the company but appears old; latest detected date is 2024-01-01.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence for SWDY.CA matches the company but no source/report date was detected.
