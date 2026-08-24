# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-08-24T07:20:03.917167+00:00
Generated Cairo: 2026-08-24 10:20
Run timing: target 09:15 Cairo | generated Cairo 2026-08-24 10:20 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-08-24 10:17

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 175/189
- Top sector: Telecommunications

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, August 20
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 75.0% / above MA50 75.0%
- EGX70 regime: MIXED / above MA20 55.0% / above MA50 75.0%
- Sector breadth: 33.33%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=644385216.0 spike=1.33 score=15.06
- CCAP.CA: liquidity=444538624.0 spike=0.75 score=25.4
- ZMID.CA: liquidity=365721536.0 spike=1.5 score=21.26
- PHAR.CA: liquidity=241171152.0 spike=0.55 score=21.4
- TMGH.CA: liquidity=211126000.0 spike=0.74 score=15.26

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 show mixed trends with weak sector breadth (33%), prompting a defensive risk mode that blocks new buys; the scanner flags tickets with high rank scores and liquidity spikes but keeps them HOLD due to overextended momentum, cooling liquidity, or sector weakness.
- Top tickets (AXPH.CA, KWIN.CA, ETEL.CA, etc.) have high rank scores and liquidity spikes, yet their outlooks are only constructive or bullish watch and buy_ready is false.
- Liquidity regimes vary: accumulation spikes suggest short‑term interest, but many names show cooling liquidity or extended momentum, limiting near‑term upside.
- Support/resistance distances show prices are far above 20‑day support (10‑30% gap) and close to resistance, indicating limited room for gains in the next 1‑3 days.
- Sector breadth is low; leading sectors (Telecom, Textiles, Transport) represent a minority of stocks, reinforcing the defensive EGX30/EGX70 regime and the risk mode that prevents new buys.

## Top Liquidity Spikes
- EGBE.CA: spike=163.96 liquidity=34587760.89 outlook=BULLISH_WATCH score=82.29 buy_ready=False
- NAHO.CA: spike=80.38 liquidity=7079554.4 outlook=CONSTRUCTIVE score=60.65 buy_ready=False
- EGSA.CA: spike=51.67 liquidity=881841.98 outlook=WEAK_OR_RISKY score=4 buy_ready=False
- TRTO.CA: spike=36.9 liquidity=377048.06 outlook=NEUTRAL score=43.65 buy_ready=False
- CFGH.CA: spike=13.25 liquidity=240442.17 outlook=WEAK_OR_RISKY score=12.65 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=43.34 5d=0.56% 20d=4.0% aboveMA50=50.0%
- #2 Textiles: score=13.63 5d=8.11% 20d=16.16% aboveMA50=100.0%
- #3 Transportation & Logistics: score=11.06 5d=-1.54% 20d=14.23% aboveMA50=100.0%
- #4 Education: score=10.16 5d=0.4% 20d=17.32% aboveMA50=100.0%
- #5 Banking & Financials: score=9.29 5d=0.24% 20d=9.59% aboveMA50=90.0%
- #6 Agriculture & Food Production: score=9.12 5d=-1.62% 20d=13.87% aboveMA50=100.0%
- #7 Building Materials: score=8.55 5d=-1.94% 20d=20.36% aboveMA50=83.33%
- #8 Industrial Goods & Cables: score=8.18 5d=1.86% 20d=8.6% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- KABO.CA: BULLISH_WATCH score=99 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- ALCN.CA: BULLISH_WATCH score=99 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- KWIN.CA: BULLISH_WATCH score=90.65 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- ETEL.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- SCTS.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- EXPA.CA: BULLISH_WATCH score=84.29 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA20
- DAPH.CA: BULLISH_WATCH score=82.65 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- EGBE.CA: BULLISH_WATCH score=82.29 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- CSAG.CA: BULLISH_WATCH score=81 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support
- SCFM.CA: BULLISH_WATCH score=80.65 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=22.86 buy_ready=False sector_rank=14 price=320.43 support=235.7 resistance=375.0 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=53.37 liquidity=24058845.14 spike=0.41
- ABUK.CA: score=23.4 buy_ready=False sector_rank=12 price=75.86 support=70.6 resistance=80.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=54.85 liquidity=75610176.0 spike=0.67
- ACAMD.CA: score=5.34 buy_ready=False sector_rank=14 price=2.04 support=2.09 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:00 AM market time freshness=DELAYED_CURRENT RSI=31.75 liquidity=4481298.5 spike=0.08
- ACGC.CA: score=22.98 buy_ready=False sector_rank=2 price=13.61 support=10.12 resistance=13.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=77.37 liquidity=56789812.0 spike=1.29
- ADCI.CA: score=17.92 buy_ready=False sector_rank=14 price=286.96 support=245.0 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=48.93 liquidity=7062755.5 spike=0.32
- ADIB.CA: score=21.4 buy_ready=False sector_rank=5 price=54.0 support=48.62 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=51.58 liquidity=85355288.0 spike=0.78
- ADPC.CA: score=18.86 buy_ready=False sector_rank=14 price=3.99 support=3.81 resistance=4.61 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=54.55 liquidity=42471706.72 spike=0.99
- AFDI.CA: score=18.86 buy_ready=False sector_rank=14 price=62.53 support=48.35 resistance=69.89 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=66.32 liquidity=10993086.44 spike=0.51
- AFMC.CA: score=20.86 buy_ready=False sector_rank=14 price=230.2 support=102.11 resistance=300.0 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=53.06 liquidity=65421227.73 spike=0.41
- AJWA.CA: score=20.86 buy_ready=False sector_rank=14 price=192.0 support=175.0 resistance=210.0 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=51.21 liquidity=24206976.0 spike=0.55
- ALCN.CA: score=24.52 buy_ready=False sector_rank=3 price=31.59 support=28.8 resistance=32.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=65.03 liquidity=49238444.0 spike=2.06
- ALUM.CA: score=18.52 buy_ready=False sector_rank=14 price=26.58 support=22.72 resistance=30.6 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=68.23 liquidity=7663758.22 spike=0.4
- AMER.CA: score=20.26 buy_ready=False sector_rank=16 price=5.74 support=4.14 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=59.61 liquidity=73311792.0 spike=0.73
- AMES.CA: score=11.67 buy_ready=False sector_rank=14 price=154.53 support=110.54 resistance=173.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:00 AM market time freshness=DELAYED_CURRENT RSI=69.62 liquidity=814736.13 spike=0.01
- AMIA.CA: score=0.25 buy_ready=False sector_rank=14 price=20.71 support=18.91 resistance=20.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:00 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4388237.0 spike=0.13
- AMOC.CA: score=21.2 buy_ready=False sector_rank=13 price=11.4 support=8.23 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=72.41 liquidity=103927512.0 spike=0.77
- APSW.CA: score=9.14 buy_ready=False sector_rank=14 price=8.79 support=8.6 resistance=9.39 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=52.67 liquidity=1277855.03 spike=0.89
- ARAB.CA: score=15.26 buy_ready=False sector_rank=16 price=0.23 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=36.67 liquidity=38480652.0 spike=0.5
- ARCC.CA: score=18.4 buy_ready=False sector_rank=7 price=72.49 support=55.4 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=79.63 liquidity=31745292.0 spike=0.32
- AREH.CA: score=6.22 buy_ready=False sector_rank=14 price=1.49 support=1.38 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:00 AM market time freshness=DELAYED_CURRENT RSI=54.0 liquidity=363210.5 spike=0.01
- ARVA.CA: score=5.86 buy_ready=False sector_rank=14 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=13.86 buy_ready=False sector_rank=14 price=63.9 support=60.99 resistance=69.95 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=34.64 liquidity=29259682.9 spike=0.58
- ASPI.CA: score=20.86 buy_ready=False sector_rank=14 price=0.51 support=0.36 resistance=0.57 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=66.37 liquidity=35359526.59 spike=0.97
- ATLC.CA: score=16.68 buy_ready=False sector_rank=19 price=5.26 support=5.0 resistance=5.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=45.31 liquidity=9143313.0 spike=0.48
- ATQA.CA: score=18.4 buy_ready=False sector_rank=12 price=11.04 support=9.66 resistance=11.7 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=77.25 liquidity=56433300.29 spike=0.8
- AXPH.CA: score=27.86 buy_ready=False sector_rank=14 price=1442.39 support=1121.56 resistance=1630.0 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=73.95 liquidity=49743704.44 spike=7.91
- BINV.CA: score=10.78 buy_ready=False sector_rank=9 price=48.44 support=46.01 resistance=50.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=54.73 liquidity=1383349.0 spike=0.2
- BIOC.CA: score=-2.1 buy_ready=False sector_rank=14 price=505.27 support=503.0 resistance=506.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:00 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2037302.25 spike=0.01
- BTFH.CA: score=8.54 buy_ready=False sector_rank=19 price=2.98 support=2.98 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=207124160.0 spike=0.93
- CAED.CA: score=18.04 buy_ready=False sector_rank=14 price=164.93 support=118.0 resistance=185.7 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=78.03 liquidity=50193639.46 spike=1.09
- CANA.CA: score=18.4 buy_ready=False sector_rank=5 price=41.63 support=36.5 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=76.15 liquidity=16523238.0 spike=0.78
- CCAP.CA: score=25.4 buy_ready=False sector_rank=9 price=5.59 support=5.14 resistance=5.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=62.37 liquidity=444538624.0 spike=0.75
- CCRS.CA: score=7.27 buy_ready=False sector_rank=14 price=2.41 support=2.4 resistance=2.76 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=34.78 liquidity=6407481.69 spike=0.47
- CEFM.CA: score=25.0 buy_ready=False sector_rank=14 price=151.05 support=121.4 resistance=168.0 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=63.22 liquidity=31408884.48 spike=1.07
- CERA.CA: score=12.65 buy_ready=False sector_rank=14 price=1.26 support=1.23 resistance=1.38 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=35.71 liquidity=6788728.75 spike=0.51
- CFGH.CA: score=10.1 buy_ready=False sector_rank=14 price=0.11 support=0.1 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=81.25 liquidity=240442.17 spike=13.25
- CICH.CA: score=13.79 buy_ready=False sector_rank=19 price=12.24 support=11.92 resistance=13.25 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=38.75 liquidity=6253501.56 spike=0.96
- CIEB.CA: score=20.1 buy_ready=False sector_rank=5 price=24.58 support=23.75 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=60.23 liquidity=6698972.5 spike=0.49
- CIRA.CA: score=21.4 buy_ready=False sector_rank=4 price=37.18 support=31.61 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=52.16 liquidity=13177185.0 spike=0.24
- CLHO.CA: score=21.88 buy_ready=False sector_rank=11 price=17.43 support=16.0 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=36.44 liquidity=78454216.0 spike=1.24
- CNFN.CA: score=17.54 buy_ready=False sector_rank=19 price=4.81 support=4.68 resistance=5.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=47.17 liquidity=12935078.0 spike=0.66
- COMI.CA: score=15.06 buy_ready=False sector_rank=5 price=138.03 support=135.35 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=28.45 liquidity=644385216.0 spike=1.33
- COPR.CA: score=-3.78 buy_ready=False sector_rank=14 price=0.55 support=0.54 resistance=0.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:00 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=362857.78 spike=0.0
- COSG.CA: score=11.31 buy_ready=False sector_rank=14 price=1.88 support=1.6 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:00 AM market time freshness=DELAYED_CURRENT RSI=69.44 liquidity=451873.44 spike=0.01
- CPCI.CA: score=20.86 buy_ready=False sector_rank=14 price=532.09 support=440.01 resistance=644.0 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=67.16 liquidity=14630347.38 spike=2.0
- CSAG.CA: score=23.82 buy_ready=False sector_rank=3 price=41.52 support=31.35 resistance=43.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=73.88 liquidity=41400800.0 spike=1.71
- DAPH.CA: score=23.92 buy_ready=False sector_rank=14 price=111.84 support=92.1 resistance=147.0 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=59.86 liquidity=51528824.39 spike=1.53
- DEIN.CA: score=-4.14 buy_ready=False sector_rank=14 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=13.85 buy_ready=False sector_rank=17 price=28.13 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=57.91 liquidity=5602023.0 spike=0.37
- DSCW.CA: score=9.23 buy_ready=False sector_rank=14 price=1.97 support=1.89 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:00 AM market time freshness=DELAYED_CURRENT RSI=44.23 liquidity=366821.88 spike=0.0
- DTPP.CA: score=18.86 buy_ready=False sector_rank=14 price=296.22 support=225.11 resistance=340.0 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=71.07 liquidity=21014735.55 spike=0.42
- EALR.CA: score=22.86 buy_ready=False sector_rank=14 price=394.03 support=362.0 resistance=471.18 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=48.71 liquidity=17728591.74 spike=0.39
- EASB.CA: score=12.1 buy_ready=False sector_rank=14 price=7.18 support=6.71 resistance=8.43 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=45.45 liquidity=6242248.77 spike=0.97
- EAST.CA: score=16.25 buy_ready=False sector_rank=17 price=36.03 support=36.0 resistance=37.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=42.21 liquidity=24816720.0 spike=0.41
- EBSC.CA: score=8.36 buy_ready=False sector_rank=14 price=1.89 support=1.85 resistance=2.06 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=48.0 liquidity=2503518.55 spike=0.51
- ECAP.CA: score=22.86 buy_ready=False sector_rank=14 price=36.23 support=32.12 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=57.82 liquidity=11863147.0 spike=0.94
- EDFM.CA: score=10.3 buy_ready=False sector_rank=14 price=407.14 support=352.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:08 PM market time freshness=DELAYED_CURRENT RSI=65.26 liquidity=1444224.88 spike=0.36
- EEII.CA: score=11.53 buy_ready=False sector_rank=14 price=2.91 support=2.54 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:00 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=667999.13 spike=0.03
- EFIC.CA: score=23.4 buy_ready=False sector_rank=12 price=213.65 support=184.0 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=61.75 liquidity=29552814.0 spike=0.65
- EFID.CA: score=17.25 buy_ready=False sector_rank=17 price=32.17 support=26.64 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=83.6 liquidity=18746882.0 spike=0.21
- EFIH.CA: score=21.4 buy_ready=False sector_rank=10 price=24.46 support=22.15 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=65.65 liquidity=61508124.0 spike=0.51
- EGAL.CA: score=21.4 buy_ready=False sector_rank=12 price=331.78 support=292.0 resistance=359.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=70.89 liquidity=74328072.0 spike=0.72
- EGAS.CA: score=10.16 buy_ready=False sector_rank=13 price=56.99 support=50.0 resistance=67.7 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=30.48 liquidity=5952548.69 spike=0.26
- EGBE.CA: score=24.4 buy_ready=False sector_rank=5 price=0.55 support=0.47 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=69.5 liquidity=34587760.89 spike=163.96
- EGCH.CA: score=19.4 buy_ready=False sector_rank=12 price=13.79 support=12.69 resistance=14.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=52.29 liquidity=96747720.0 spike=0.79
- EGSA.CA: score=15.28 buy_ready=False sector_rank=1 price=8.69 support=8.65 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:02 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=881841.98 spike=51.67
- EGTS.CA: score=16.16 buy_ready=False sector_rank=16 price=16.79 support=16.63 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=42.76 liquidity=49698956.0 spike=1.45
- EHDR.CA: score=13.38 buy_ready=False sector_rank=14 price=3.0 support=2.71 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:00 AM market time freshness=DELAYED_CURRENT RSI=58.62 liquidity=515119.88 spike=0.01
- EKHO.CA: score=7.2 buy_ready=False sector_rank=13 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=13.96 buy_ready=False sector_rank=8 price=2.08 support=2.06 resistance=2.25 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=27.78 liquidity=137362758.16 spike=2.78
- ELKA.CA: score=9.24 buy_ready=False sector_rank=14 price=1.75 support=1.69 resistance=2.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:00 AM market time freshness=DELAYED_CURRENT RSI=46.15 liquidity=375739.0 spike=0.01
- ELNA.CA: score=3.0 buy_ready=False sector_rank=14 price=36.45 support=36.1 resistance=39.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=30.18 liquidity=1055775.38 spike=2.04
- ELSH.CA: score=10.86 buy_ready=False sector_rank=14 price=13.25 support=13.14 resistance=15.59 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=24.49 liquidity=40820759.0 spike=0.7
- ELWA.CA: score=15.32 buy_ready=False sector_rank=14 price=1.74 support=1.62 resistance=1.94 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=47.5 liquidity=3924582.2 spike=2.77
- EMFD.CA: score=20.26 buy_ready=False sector_rank=16 price=11.81 support=11.08 resistance=12.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=63.58 liquidity=49533952.0 spike=0.82
- ENGC.CA: score=18.86 buy_ready=False sector_rank=14 price=45.1 support=40.11 resistance=54.79 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=58.78 liquidity=11429106.31 spike=0.43
- EOSB.CA: score=12.86 buy_ready=False sector_rank=14 price=1.55 support=1.53 resistance=1.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 11:41 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=278.64 spike=0.01
- EPCO.CA: score=18.86 buy_ready=False sector_rank=14 price=11.32 support=10.32 resistance=13.05 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=52.75 liquidity=16532667.11 spike=0.86
- EPPK.CA: score=1.35 buy_ready=False sector_rank=14 price=12.94 support=12.62 resistance=15.93 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=23.4 liquidity=492884.58 spike=0.68
- ETEL.CA: score=26.4 buy_ready=False sector_rank=1 price=114.63 support=102.5 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=52.91 liquidity=106013960.0 spike=0.75
- ETRS.CA: score=22.86 buy_ready=False sector_rank=14 price=10.94 support=10.21 resistance=11.66 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=58.79 liquidity=20575054.13 spike=0.74
- EXPA.CA: score=21.04 buy_ready=False sector_rank=5 price=20.29 support=19.6 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=50.16 liquidity=68896832.0 spike=1.82
- FAIT.CA: score=22.47 buy_ready=False sector_rank=5 price=42.44 support=36.1 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=72.89 liquidity=8928466.0 spike=2.07
- FAITA.CA: score=18.63 buy_ready=False sector_rank=5 price=0.99 support=0.96 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:13 PM market time freshness=DELAYED_CURRENT RSI=57.75 liquidity=231601.01 spike=4.51
- FERC.CA: score=18.4 buy_ready=False sector_rank=12 price=77.0 support=75.01 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=51.99 liquidity=15609411.0 spike=0.67
- FWRY.CA: score=23.4 buy_ready=False sector_rank=10 price=19.2 support=18.69 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=51.28 liquidity=85373920.0 spike=0.71
- GBCO.CA: score=12.4 buy_ready=False sector_rank=21 price=29.36 support=29.31 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=44.83 liquidity=40952604.0 spike=0.82
- GDWA.CA: score=9.86 buy_ready=False sector_rank=14 price=0.79 support=0.78 resistance=0.88 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=33.87 liquidity=38531116.61 spike=0.59
- GGCC.CA: score=18.86 buy_ready=False sector_rank=14 price=0.93 support=0.81 resistance=1.28 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=55.65 liquidity=35391964.95 spike=0.85
- GIHD.CA: score=19.06 buy_ready=False sector_rank=14 price=60.7 support=56.51 resistance=76.5 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=57.69 liquidity=30422354.78 spike=1.1
- GMCI.CA: score=0.93 buy_ready=False sector_rank=14 price=1.91 support=1.88 resistance=2.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:11 PM market time freshness=DELAYED_CURRENT RSI=17.39 liquidity=71202.89 spike=0.11
- GRCA.CA: score=4.18 buy_ready=False sector_rank=14 price=79.89 support=78.0 resistance=80.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:00 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8323587.5 spike=0.31
- GSSC.CA: score=20.18 buy_ready=False sector_rank=14 price=283.06 support=264.0 resistance=301.0 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=48.98 liquidity=9324279.38 spike=0.54
- GTWL.CA: score=11.67 buy_ready=False sector_rank=14 price=188.08 support=186.1 resistance=186.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:00 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=812912.06 spike=1.0
- HDBK.CA: score=14.4 buy_ready=False sector_rank=5 price=92.42 support=80.8 resistance=93.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=76.45 liquidity=23612398.0 spike=0.56
- HELI.CA: score=13.48 buy_ready=False sector_rank=16 price=7.65 support=7.5 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=21.26 liquidity=183334048.0 spike=1.11
- HRHO.CA: score=13.54 buy_ready=False sector_rank=19 price=26.25 support=25.95 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=46.92 liquidity=49294152.0 spike=0.5
- ICID.CA: score=22.34 buy_ready=False sector_rank=14 price=16.69 support=7.85 resistance=16.99 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=98.22 liquidity=48940622.65 spike=2.24
- IDRE.CA: score=16.9 buy_ready=False sector_rank=14 price=52.5 support=46.04 resistance=58.95 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=60.43 liquidity=6038655.0 spike=0.32
- IFAP.CA: score=12.31 buy_ready=False sector_rank=6 price=21.39 support=19.0 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:00 AM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=906333.75 spike=0.03
- INFI.CA: score=12.36 buy_ready=False sector_rank=14 price=159.88 support=104.0 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:00 AM market time freshness=DELAYED_CURRENT RSI=72.54 liquidity=1502412.5 spike=0.02
- IRON.CA: score=18.28 buy_ready=False sector_rank=12 price=31.76 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=56.8 liquidity=8880431.0 spike=0.82
- ISMA.CA: score=19.86 buy_ready=False sector_rank=14 price=36.0 support=28.11 resistance=36.9 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=89.06 liquidity=20137716.0 spike=0.76
- ISMQ.CA: score=19.4 buy_ready=False sector_rank=12 price=9.16 support=8.96 resistance=9.97 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=21577918.52 spike=0.43
- ISPH.CA: score=21.4 buy_ready=False sector_rank=11 price=13.2 support=11.3 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=61.93 liquidity=73346592.0 spike=0.39
- JUFO.CA: score=13.25 buy_ready=False sector_rank=17 price=26.71 support=22.78 resistance=29.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=83.06 liquidity=15056212.0 spike=0.25
- KABO.CA: score=24.98 buy_ready=False sector_rank=2 price=9.0 support=7.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=69.69 liquidity=76191104.0 spike=1.79
- KWIN.CA: score=27.86 buy_ready=False sector_rank=14 price=102.28 support=84.08 resistance=111.95 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=54.52 liquidity=199329602.98 spike=5.01
- KZPC.CA: score=-3.47 buy_ready=False sector_rank=14 price=13.56 support=13.52 resistance=13.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:00 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=674979.44 spike=0.02
- LCSW.CA: score=19.4 buy_ready=False sector_rank=7 price=34.23 support=30.2 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=45.34 liquidity=17509716.0 spike=0.4
- LUTS.CA: score=0.63 buy_ready=False sector_rank=14 price=1.52 support=1.52 resistance=1.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:01 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4766342.0 spike=0.03
- MAAL.CA: score=11.54 buy_ready=False sector_rank=14 price=8.69 support=8.32 resistance=9.76 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=42.59 liquidity=2682029.33 spike=0.26
- MASR.CA: score=10.08 buy_ready=False sector_rank=14 price=7.75 support=7.45 resistance=8.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:01 AM market time freshness=DELAYED_CURRENT RSI=35.42 liquidity=1224865.25 spike=0.02
- MBSC.CA: score=18.4 buy_ready=False sector_rank=7 price=373.25 support=240.02 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=83.28 liquidity=48500632.0 spike=0.61
- MCQE.CA: score=21.4 buy_ready=False sector_rank=7 price=222.0 support=178.0 resistance=292.32 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=65.47 liquidity=31436310.0 spike=0.67
- MCRO.CA: score=12.6 buy_ready=False sector_rank=14 price=1.58 support=1.44 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:01 AM market time freshness=DELAYED_CURRENT RSI=52.27 liquidity=1739195.75 spike=0.01
- MENA.CA: score=10.93 buy_ready=False sector_rank=16 price=6.94 support=6.82 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=47.27 liquidity=5677909.0 spike=0.92
- MEPA.CA: score=18.86 buy_ready=False sector_rank=14 price=1.82 support=1.78 resistance=2.02 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=40.0 liquidity=12767577.01 spike=0.39
- MFPC.CA: score=23.4 buy_ready=False sector_rank=12 price=39.12 support=35.37 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=63.91 liquidity=62721472.0 spike=0.75
- MFSC.CA: score=6.11 buy_ready=False sector_rank=14 price=49.01 support=46.02 resistance=65.0 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=26.1 liquidity=2249705.95 spike=0.21
- MHOT.CA: score=12.16 buy_ready=False sector_rank=15 price=18.26 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=61.01 liquidity=3486668.75 spike=0.2
- MICH.CA: score=22.86 buy_ready=False sector_rank=14 price=50.0 support=39.01 resistance=53.9 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=70.61 liquidity=74509300.0 spike=2.0
- MILS.CA: score=23.62 buy_ready=False sector_rank=14 price=225.13 support=165.55 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=57.01 liquidity=122580904.0 spike=1.38
- MIPH.CA: score=17.04 buy_ready=False sector_rank=11 price=790.19 support=722.7 resistance=828.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=54.24 liquidity=5119201.0 spike=1.26
- MOED.CA: score=13.03 buy_ready=False sector_rank=14 price=0.81 support=0.65 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:01 AM market time freshness=DELAYED_CURRENT RSI=92.27 liquidity=3169736.0 spike=0.04
- MOIL.CA: score=9.52 buy_ready=False sector_rank=13 price=0.66 support=0.58 resistance=0.69 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=40.7 liquidity=318910.29 spike=0.66
- MOIN.CA: score=20.86 buy_ready=False sector_rank=14 price=34.74 support=23.11 resistance=40.8 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=70.36 liquidity=19031997.26 spike=0.62
- MOSC.CA: score=16.59 buy_ready=False sector_rank=14 price=330.04 support=282.0 resistance=380.0 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=77.74 liquidity=8731538.47 spike=0.65
- MPCI.CA: score=-0.55 buy_ready=False sector_rank=14 price=419.0 support=419.0 resistance=423.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:01 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3593609.25 spike=0.02
- MPCO.CA: score=22.0 buy_ready=False sector_rank=6 price=2.22 support=1.83 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=67.61 liquidity=153759728.0 spike=1.3
- MPRC.CA: score=19.38 buy_ready=False sector_rank=14 price=42.88 support=39.5 resistance=52.49 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=42.49 liquidity=30947397.25 spike=1.26
- MTIE.CA: score=7.4 buy_ready=False sector_rank=21 price=8.46 support=8.01 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=34.76 liquidity=25944740.0 spike=0.48
- NAHO.CA: score=19.94 buy_ready=False sector_rank=14 price=0.15 support=0.1 resistance=0.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 12:59 PM market time freshness=DELAYED_CURRENT RSI=92.16 liquidity=7079554.4 spike=80.38
- NCCW.CA: score=15.86 buy_ready=False sector_rank=14 price=5.8 support=5.59 resistance=7.11 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=45.65 liquidity=25385208.83 spike=0.85
- NEDA.CA: score=13.39 buy_ready=False sector_rank=14 price=2.76 support=2.7 resistance=2.97 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=50.94 liquidity=1551804.47 spike=1.99
- NHPS.CA: score=11.23 buy_ready=False sector_rank=14 price=91.75 support=82.25 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:00 AM market time freshness=DELAYED_CURRENT RSI=61.02 liquidity=367037.5 spike=0.01
- NINH.CA: score=13.86 buy_ready=False sector_rank=14 price=21.71 support=21.22 resistance=25.99 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=21.27 liquidity=16069502.51 spike=0.56
- NIPH.CA: score=2.37 buy_ready=False sector_rank=11 price=406.51 support=405.0 resistance=408.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:00 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5973232.5 spike=0.02
- OBRI.CA: score=16.86 buy_ready=False sector_rank=14 price=32.49 support=31.61 resistance=35.59 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=51.34 liquidity=16248444.78 spike=0.56
- OCDI.CA: score=20.26 buy_ready=False sector_rank=16 price=32.74 support=26.6 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=63.99 liquidity=83954776.0 spike=0.63
- OCPH.CA: score=15.88 buy_ready=False sector_rank=14 price=248.3 support=225.0 resistance=483.99 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=51.11 liquidity=9020490.81 spike=0.43
- ODIN.CA: score=22.86 buy_ready=False sector_rank=14 price=3.21 support=2.54 resistance=3.92 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=58.12 liquidity=33714148.9 spike=0.88
- OFH.CA: score=19.86 buy_ready=False sector_rank=14 price=0.91 support=0.69 resistance=0.95 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=86.77 liquidity=60249607.87 spike=0.94
- OIH.CA: score=20.4 buy_ready=False sector_rank=9 price=1.88 support=1.43 resistance=1.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=88.68 liquidity=110361496.0 spike=0.82
- OLFI.CA: score=13.99 buy_ready=False sector_rank=17 price=23.98 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=55.84 liquidity=5740719.0 spike=0.09
- ORAS.CA: score=4.6 buy_ready=False sector_rank=18 price=757.19 support=740.0 resistance=760.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=125781992.0 spike=1.0
- ORHD.CA: score=18.26 buy_ready=False sector_rank=16 price=40.99 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=61.0 liquidity=152962832.0 spike=0.96
- ORWE.CA: score=21.4 buy_ready=False sector_rank=2 price=25.36 support=22.55 resistance=27.41 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=72.2 liquidity=15805087.82 spike=0.23
- PHAR.CA: score=21.4 buy_ready=False sector_rank=11 price=130.35 support=90.01 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=53.49 liquidity=241171152.0 spike=0.55
- PHDC.CA: score=20.26 buy_ready=False sector_rank=16 price=15.13 support=14.32 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=64.14 liquidity=138087504.0 spike=0.57
- PHTV.CA: score=9.56 buy_ready=False sector_rank=14 price=375.0 support=310.0 resistance=447.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=65.28 liquidity=701894.44 spike=0.25
- POUL.CA: score=15.25 buy_ready=False sector_rank=17 price=37.33 support=36.5 resistance=40.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=45.82 liquidity=10261873.0 spike=0.39
- PRCL.CA: score=11.4 buy_ready=False sector_rank=7 price=32.5 support=32.0 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=33.61 liquidity=21086086.0 spike=0.67
- PRDC.CA: score=18.26 buy_ready=False sector_rank=16 price=9.05 support=8.7 resistance=9.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=37.64 liquidity=63977936.0 spike=0.88
- PRMH.CA: score=13.98 buy_ready=False sector_rank=14 price=2.36 support=2.36 resistance=2.93 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=35.29 liquidity=8116665.04 spike=0.74
- RACC.CA: score=16.26 buy_ready=False sector_rank=14 price=10.03 support=9.8 resistance=10.88 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=44.55 liquidity=20201683.24 spike=1.2
- RAKT.CA: score=0.67 buy_ready=False sector_rank=14 price=22.25 support=21.65 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:12 PM market time freshness=DELAYED_CURRENT RSI=22.55 liquidity=367054.94 spike=1.22
- RAYA.CA: score=8.26 buy_ready=False sector_rank=20 price=7.0 support=6.95 resistance=7.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=19.32 liquidity=28215234.0 spike=0.33
- RMDA.CA: score=21.4 buy_ready=False sector_rank=11 price=6.12 support=4.98 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=60.92 liquidity=33235898.0 spike=0.28
- ROTO.CA: score=18.86 buy_ready=False sector_rank=14 price=46.33 support=41.85 resistance=52.77 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=55.44 liquidity=14795995.71 spike=0.73
- RREI.CA: score=18.86 buy_ready=False sector_rank=14 price=4.45 support=3.76 resistance=5.09 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=45.4 liquidity=29449604.79 spike=0.45
- RTVC.CA: score=23.6 buy_ready=False sector_rank=14 price=4.2 support=3.73 resistance=4.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=81.82 liquidity=22274982.0 spike=2.87
- RUBX.CA: score=9.19 buy_ready=False sector_rank=14 price=12.63 support=12.02 resistance=13.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:01 AM market time freshness=DELAYED_CURRENT RSI=50.29 liquidity=331270.34 spike=0.02
- SAUD.CA: score=21.54 buy_ready=False sector_rank=5 price=24.5 support=21.4 resistance=24.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=88.45 liquidity=35751016.0 spike=1.57
- SCEM.CA: score=12.26 buy_ready=False sector_rank=7 price=97.48 support=76.75 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:00 AM market time freshness=DELAYED_CURRENT RSI=70.54 liquidity=861654.44 spike=0.0
- SCFM.CA: score=20.86 buy_ready=False sector_rank=14 price=283.01 support=270.51 resistance=319.0 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=43.62 liquidity=17306628.12 spike=0.86
- SCTS.CA: score=17.09 buy_ready=False sector_rank=4 price=620.16 support=603.13 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=61.7 liquidity=3686153.75 spike=0.36
- SDTI.CA: score=11.24 buy_ready=False sector_rank=14 price=69.0 support=50.3 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:00 AM market time freshness=DELAYED_CURRENT RSI=60.97 liquidity=379454.38 spike=0.01
- SEIG.CA: score=10.05 buy_ready=False sector_rank=14 price=263.41 support=242.1 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=55.69 liquidity=1185175.63 spike=0.11
- SIPC.CA: score=-3.66 buy_ready=False sector_rank=14 price=5.11 support=5.1 resistance=5.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:01 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=481225.19 spike=0.01
- SKPC.CA: score=22.3 buy_ready=False sector_rank=12 price=17.73 support=15.61 resistance=18.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=84.15 liquidity=133216192.0 spike=1.95
- SMFR.CA: score=18.58 buy_ready=False sector_rank=14 price=261.9 support=228.88 resistance=309.0 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=64.94 liquidity=7723692.72 spike=0.31
- SNFC.CA: score=8.71 buy_ready=False sector_rank=14 price=10.83 support=10.6 resistance=11.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:01 AM market time freshness=DELAYED_CURRENT RSI=46.62 liquidity=849180.31 spike=0.07
- SPIN.CA: score=23.4 buy_ready=False sector_rank=2 price=18.31 support=14.91 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=65.62 liquidity=11838994.0 spike=0.25
- SPMD.CA: score=9.35 buy_ready=False sector_rank=14 price=0.47 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:01 AM market time freshness=DELAYED_CURRENT RSI=42.47 liquidity=493577.09 spike=0.02
- SUGR.CA: score=11.69 buy_ready=False sector_rank=17 price=53.03 support=46.47 resistance=53.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:00 AM market time freshness=DELAYED_CURRENT RSI=72.94 liquidity=1440256.0 spike=0.07
- SVCE.CA: score=20.86 buy_ready=False sector_rank=14 price=10.36 support=9.06 resistance=12.85 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=65.56 liquidity=29012422.76 spike=0.32
- SWDY.CA: score=21.4 buy_ready=False sector_rank=8 price=116.51 support=91.8 resistance=133.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=68.64 liquidity=76819720.0 spike=0.84
- TALM.CA: score=23.4 buy_ready=False sector_rank=4 price=19.4 support=15.7 resistance=20.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=61.1 liquidity=30658148.0 spike=0.7
- TMGH.CA: score=15.26 buy_ready=False sector_rank=16 price=96.54 support=95.2 resistance=101.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=45.01 liquidity=211126000.0 spike=0.74
- TRTO.CA: score=20.24 buy_ready=False sector_rank=14 price=0.05 support=0.03 resistance=0.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 11:15 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=377048.06 spike=36.9
- UEFM.CA: score=9.63 buy_ready=False sector_rank=14 price=538.85 support=531.0 resistance=594.0 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=46.53 liquidity=765705.82 spike=0.18
- UEGC.CA: score=-3.77 buy_ready=False sector_rank=14 price=2.23 support=2.22 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:01 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=365840.19 spike=0.01
- UNIP.CA: score=17.38 buy_ready=False sector_rank=14 price=0.36 support=0.35 resistance=0.44 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=35.79 liquidity=51014241.59 spike=1.76
- UNIT.CA: score=12.84 buy_ready=False sector_rank=16 price=18.81 support=17.32 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=55.67 liquidity=2588434.75 spike=0.2
- WCDF.CA: score=9.24 buy_ready=False sector_rank=14 price=639.6 support=555.55 resistance=700.0 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=76.66 liquidity=1382175.55 spike=0.33
- WKOL.CA: score=-2.55 buy_ready=False sector_rank=14 price=363.35 support=350.0 resistance=364.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:01 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1591797.88 spike=0.05
- ZEOT.CA: score=20.85 buy_ready=False sector_rank=14 price=13.81 support=11.56 resistance=14.99 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=64.74 liquidity=7987248.51 spike=0.33
- ZMID.CA: score=21.26 buy_ready=False sector_rank=16 price=7.85 support=7.06 resistance=8.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=71.63 liquidity=365721536.0 spike=1.5

## Backtesting Lite
- AXPH.CA: 180d return=76.91%, max drawdown=-8.16%, MA20>MA50 days last20=20, as_of=2026-08-19T21:00:00+00:00
- KWIN.CA: 180d return=57.45%, max drawdown=-34.04%, MA20>MA50 days last20=20, as_of=2026-08-19T21:00:00+00:00
- ETEL.CA: 180d return=88.23%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-08-19T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- AXPH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria Co. For Pharmaceuticals & Chemical Industries summary=Alexandria Pharmaceuticals’ profits retreat 25% in 8M-21/22; Alexandria Pharmaceuticals profits fall 22.5% in 7M-21/22; Alexandria Pharmaceuticals posts 27% lower profits in 6M
  - Alexandria Pharmaceuticals’ profits retreat 25% in 8M-21/22: https://english.mubasher.info/news/3938982/Alexandria-Pharmaceuticals-profits-retreat-25-in-8M-21-22/
  - Alexandria Pharmaceuticals profits fall 22.5% in 7M-21/22: https://english.mubasher.info/news/3923195/Alexandria-Pharmaceuticals-profits-fall-22-5-in-7M-21-22/
  - Alexandria Pharmaceuticals posts 27% lower profits in 6M: https://english.mubasher.info/news/3906523/Alexandria-Pharmaceuticals-posts-27-lower-profits-in-6M/
- KWIN.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Kahera El Watania Investment summary=ADIB Egypt&#39;s Cairo National unveils equity reduction transaction worth over EGP 3m; El Kahera El Watania to buy stake in Assiut for Agricultural Development; Tycoon Holding acquires 85% of Alexandria National Investment
  - ADIB Egypt&#39;s Cairo National unveils equity reduction transaction worth over EGP 3m: https://english.mubasher.info/news/4546852/ADIB-Egypt-s-Cairo-National-unveils-equity-reduction-transaction-worth-over-EGP-3m/
  - El Kahera El Watania to buy stake in Assiut for Agricultural Development: https://english.mubasher.info/news/4009433/El-Kahera-El-Watania-to-buy-stake-in-Assiut-for-Agricultural-Development/
  - Tycoon Holding acquires 85% of Alexandria National Investment: https://english.mubasher.info/news/3844623/Tycoon-Holding-acquires-85-of-Alexandria-National-Investment/
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- CEFM.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Middle Egypt Flour Mills summary=Middle Egypt Flour Mills posts lower net profits at EGP 77m in 9M-25/26; Middle Egypt Flour Mills shareholders approve EGP 3.25/shr dividend; Middle Egypt Mills reports 23% profit drop in FY19/20
  - Middle Egypt Flour Mills posts lower net profits at EGP 77m in 9M-25/26: https://english.mubasher.info/news/4601809/Middle-Egypt-Flour-Mills-posts-lower-net-profits-at-EGP-77m-in-9M-25-26/
  - Middle Egypt Flour Mills shareholders approve EGP 3.25/shr dividend: https://english.mubasher.info/news/3870911/Middle-Egypt-Flour-Mills-shareholders-approve-EGP-3-25-shr-dividend/
  - Middle Egypt Mills reports 23% profit drop in FY19/20: https://english.mubasher.info/news/3703590/Middle-Egypt-Mills-reports-23-profit-drop-in-FY19-20/
- KABO.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Nasr Clothing and Textiles summary=KABO posts EGP 17m in Q1-25/26 unaudited consolidated net profits; KABO sells over 1.9m shares in Spinalex for EGP 20m; KABO unveils international agreements, expansion plan including export lines
  - KABO posts EGP 17m in Q1-25/26 unaudited consolidated net profits: https://english.mubasher.info/news/4600162/KABO-posts-EGP-17m-in-Q1-25-26-unaudited-consolidated-net-profits/
  - KABO sells over 1.9m shares in Spinalex for EGP 20m: https://english.mubasher.info/news/4543747/KABO-sells-over-1-9m-shares-in-Spinalex-for-EGP-20m/
  - KABO unveils international agreements, expansion plan including export lines: https://english.mubasher.info/news/4533185/KABO-unveils-international-agreements-expansion-plan-including-export-lines/
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- EGBE.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Gulf Bank summary=Evidence rejected for EGBE.CA: source text did not clearly match EGBE.CA / Egyptian Gulf Bank.

## Warnings
- Evidence for AXPH.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for KWIN.CA matches the company but no source/report date was detected.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for CEFM.CA matches the company but no source/report date was detected.
- Evidence for KABO.CA matches the company but no source/report date was detected.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence rejected for EGBE.CA: source text did not clearly match EGBE.CA / Egyptian Gulf Bank.
