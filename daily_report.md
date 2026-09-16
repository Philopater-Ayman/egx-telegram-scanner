# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-09-16T13:04:15.096342+00:00
Generated Cairo: 2026-09-16 16:04
Run timing: target 11:00 Cairo | generated Cairo 2026-09-16 16:04 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-09-16 16:01

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 175/189
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, September 16
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 31.58% / above MA50 57.89%
- EGX70 regime: BEARISH / above MA20 35.9% / above MA50 53.85%
- Sector breadth: 19.05%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=790994240.0 spike=0.91 score=19.4
- SPMD.CA: liquidity=384768160.0 spike=8.17 score=9.52
- COMI.CA: liquidity=383691264.0 spike=0.7 score=9.61
- DTPP.CA: liquidity=309759712.0 spike=6.03 score=9.52
- AMES.CA: liquidity=272580320.0 spike=1.09 score=4.7

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are BEARISH with weak breadth (≈19% above MA20), risk mode DEFENSIVE_NO_NEW_BUY, so the scanner holds all tickets despite some bullish watch signals.
- Top tickets (MPCO.CA, UNIT.CA, ETEL.CA, CIRA.CA) have high rank scores and BULLISH_WATCH outlook, appearing in leading sectors (Telecom, Agri & Food, Education) with varied liquidity regimes.
- Liquidity ranges from high (ETEL.CA ~251M, TRADEABLE) to moderate spikes (UNIT.CA ACCUMULATION_SPIKE), but many stocks sit far above their 20‑day support, limiting near‑term upside.
- Support/resistance distances are tight for some (e.g., ORHD.CA 6.5% below support, 2.5% below resistance) while RSI readings are elevated (68‑89), hinting at possible short‑term pull‑backs.
- The bearish EGX30/EGX70 regime and defensive risk mode override individual bullish watches, keeping confidence LOW and advising HOLD with uncertainty about short‑term reversals.

## Top Liquidity Spikes
- BINV.CA: spike=10.24 liquidity=114632032.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SPMD.CA: spike=8.17 liquidity=384768160.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SEIG.CA: spike=7.38 liquidity=11281761.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DTPP.CA: spike=6.03 liquidity=309759712.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RUBX.CA: spike=3.35 liquidity=67662296.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=11.55 5d=4.73% 20d=8.8% aboveMA50=100.0%
- #2 Agriculture & Food Production: score=11.54 5d=11.18% 20d=15.15% aboveMA50=50.0%
- #3 Investment Holding: score=11.01 5d=3.37% 20d=21.47% aboveMA50=66.67%
- #4 Education: score=7.89 5d=3.67% 20d=6.73% aboveMA50=66.67%
- #5 Energy & Petrochemicals: score=3.41 5d=-2.48% 20d=0.38% aboveMA50=75.0%
- #6 Textiles: score=3.12 5d=-7.11% 20d=0.87% aboveMA50=100.0%
- #7 Basic Resources & Chemicals: score=3.07 5d=-3.77% 20d=2.63% aboveMA50=60.0%
- #8 Real Estate: score=2.47 5d=-2.12% 20d=-0.58% aboveMA50=46.15%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MPCO.CA: BULLISH_WATCH score=91 liquidity=TRADEABLE sector=LEADING risk=momentum is extended; far above support
- UNIT.CA: BULLISH_WATCH score=90.47 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- SKPC.CA: BULLISH_WATCH score=84.07 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- KABO.CA: BULLISH_WATCH score=79.12 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ORWE.CA: BULLISH_WATCH score=79.12 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- AALR.CA: BULLISH_WATCH score=77.31 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- TALM.CA: BULLISH_WATCH score=76.89 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=overheated RSI; far above support
- ETEL.CA: BULLISH_WATCH score=75 liquidity=TRADEABLE sector=LEADING risk=overheated RSI
- CIRA.CA: BULLISH_WATCH score=73.89 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended; far above support
- ACGC.CA: BULLISH_WATCH score=73.12 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=19.52 buy_ready=False sector_rank=12 price=318.89 support=295.0 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=28411388.0 spike=0.86
- ABUK.CA: score=20.23 buy_ready=False sector_rank=7 price=88.97 support=75.01 resistance=94.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=65.2 liquidity=68786984.0 spike=0.44
- ACAMD.CA: score=16.52 buy_ready=False sector_rank=12 price=2.06 support=1.95 resistance=2.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.94 liquidity=39498228.0 spike=0.69
- ACGC.CA: score=20.25 buy_ready=False sector_rank=6 price=14.4 support=12.04 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.19 liquidity=15421907.0 spike=0.35
- ADCI.CA: score=4.85 buy_ready=False sector_rank=12 price=280.51 support=267.66 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.74 liquidity=2323622.75 spike=0.34
- ADIB.CA: score=17.61 buy_ready=False sector_rank=10 price=52.28 support=50.51 resistance=55.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.97 liquidity=63261332.0 spike=0.95
- ADPC.CA: score=13.73 buy_ready=False sector_rank=12 price=3.82 support=3.81 resistance=4.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.28 liquidity=9202155.0 spike=0.38
- AFDI.CA: score=12.42 buy_ready=False sector_rank=12 price=55.19 support=51.6 resistance=68.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=31.12 liquidity=9894358.0 spike=0.39
- AFMC.CA: score=9.52 buy_ready=False sector_rank=12 price=159.23 support=157.0 resistance=267.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=20.95 liquidity=18538090.0 spike=0.31
- AJWA.CA: score=6.2 buy_ready=False sector_rank=12 price=179.9 support=175.15 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=46.93 liquidity=1678457.25 spike=0.03
- ALCN.CA: score=16.38 buy_ready=False sector_rank=21 price=30.97 support=30.03 resistance=34.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.9 liquidity=12349923.0 spike=0.42
- ALUM.CA: score=4.97 buy_ready=False sector_rank=12 price=25.85 support=25.0 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=22.87 liquidity=2449771.25 spike=0.16
- AMER.CA: score=17.99 buy_ready=False sector_rank=8 price=5.4 support=4.8 resistance=6.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.3 liquidity=53128468.0 spike=0.83
- AMES.CA: score=4.7 buy_ready=False sector_rank=12 price=54.28 support=53.0 resistance=59.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=272580320.0 spike=1.09
- AMIA.CA: score=7.36 buy_ready=False sector_rank=12 price=17.47 support=15.3 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=31.84 liquidity=4835385.0 spike=0.07
- AMOC.CA: score=18.36 buy_ready=False sector_rank=5 price=13.45 support=10.65 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.71 liquidity=119104456.0 spike=0.63
- APSW.CA: score=4.01 buy_ready=False sector_rank=12 price=8.42 support=8.37 resistance=9.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=39.78 liquidity=487884.69 spike=0.41
- ARAB.CA: score=14.99 buy_ready=False sector_rank=8 price=0.25 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.88 liquidity=59293032.0 spike=0.6
- ARCC.CA: score=16.6 buy_ready=False sector_rank=20 price=73.03 support=71.5 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.74 liquidity=15989417.0 spike=0.34
- AREH.CA: score=13.0 buy_ready=False sector_rank=12 price=1.42 support=1.39 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.16 liquidity=8471757.0 spike=0.48
- ARVA.CA: score=4.52 buy_ready=False sector_rank=12 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=5.93 buy_ready=False sector_rank=12 price=60.21 support=60.15 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=34.25 liquidity=6410053.5 spike=0.3
- ASPI.CA: score=12.52 buy_ready=False sector_rank=12 price=0.44 support=0.41 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=32.79 liquidity=43008832.0 spike=0.77
- ATLC.CA: score=15.78 buy_ready=False sector_rank=16 price=6.96 support=5.2 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.74 liquidity=6719346.5 spike=0.23
- ATQA.CA: score=18.23 buy_ready=False sector_rank=7 price=12.63 support=10.8 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.63 liquidity=65859420.0 spike=0.61
- AXPH.CA: score=10.29 buy_ready=False sector_rank=12 price=1704.97 support=1345.01 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.32 liquidity=5766681.0 spike=0.48
- BINV.CA: score=12.4 buy_ready=False sector_rank=3 price=62.25 support=50.0 resistance=62.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=114632032.0 spike=10.24
- BIOC.CA: score=9.52 buy_ready=False sector_rank=12 price=283.8 support=272.01 resistance=535.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=9.64 liquidity=98222328.0 spike=0.75
- BTFH.CA: score=13.06 buy_ready=False sector_rank=16 price=2.93 support=2.87 resistance=3.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.94 liquidity=44869004.0 spike=0.44
- CAED.CA: score=12.52 buy_ready=False sector_rank=12 price=128.03 support=123.56 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.63 liquidity=12180519.0 spike=0.29
- CANA.CA: score=9.2 buy_ready=False sector_rank=10 price=41.75 support=41.0 resistance=44.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=1586118.0 spike=0.11
- CCAP.CA: score=19.4 buy_ready=False sector_rank=3 price=6.86 support=5.42 resistance=6.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.86 liquidity=790994240.0 spike=0.91
- CCRS.CA: score=19.52 buy_ready=False sector_rank=12 price=2.63 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.32 liquidity=13052332.0 spike=0.25
- CEFM.CA: score=9.41 buy_ready=False sector_rank=12 price=145.19 support=135.9 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=46.29 liquidity=1883946.63 spike=0.13
- CERA.CA: score=22.5 buy_ready=False sector_rank=12 price=1.47 support=1.22 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=55.75 liquidity=136568528.0 spike=1.49
- CFGH.CA: score=5.53 buy_ready=False sector_rank=12 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=4096.69 spike=0.19
- CICH.CA: score=9.57 buy_ready=False sector_rank=16 price=12.47 support=12.0 resistance=13.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=57.61 liquidity=505005.88 spike=0.1
- CIEB.CA: score=14.25 buy_ready=False sector_rank=10 price=24.64 support=24.01 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.47 liquidity=6636163.5 spike=0.47
- CIRA.CA: score=23.4 buy_ready=False sector_rank=4 price=39.0 support=32.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=28245954.0 spike=0.72
- CLHO.CA: score=9.3 buy_ready=False sector_rank=15 price=16.32 support=15.81 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.36 liquidity=26475670.0 spike=0.34
- CNFN.CA: score=0.66 buy_ready=False sector_rank=16 price=4.62 support=4.46 resistance=4.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=31.34 liquidity=2594835.25 spike=0.21
- COMI.CA: score=9.61 buy_ready=False sector_rank=10 price=131.63 support=131.56 resistance=142.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.05 liquidity=383691264.0 spike=0.7
- COPR.CA: score=12.52 buy_ready=False sector_rank=12 price=0.51 support=0.44 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.08 liquidity=41184372.0 spike=0.46
- COSG.CA: score=17.52 buy_ready=False sector_rank=12 price=1.81 support=1.74 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=10369786.0 spike=0.24
- CPCI.CA: score=9.44 buy_ready=False sector_rank=12 price=532.22 support=525.01 resistance=569.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.59 liquidity=1914528.25 spike=0.45
- CSAG.CA: score=13.38 buy_ready=False sector_rank=21 price=36.95 support=37.04 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=37.06 liquidity=13780110.0 spike=0.84
- DAPH.CA: score=17.52 buy_ready=False sector_rank=12 price=121.49 support=108.11 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=58.73 liquidity=12233076.0 spike=0.2
- DEIN.CA: score=7.52 buy_ready=False sector_rank=12 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=6.03 buy_ready=False sector_rank=19 price=26.89 support=26.51 resistance=29.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=35.97 liquidity=2307711.5 spike=0.38
- DSCW.CA: score=12.37 buy_ready=False sector_rank=12 price=1.82 support=1.8 resistance=2.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=8842948.0 spike=0.21
- DTPP.CA: score=9.52 buy_ready=False sector_rank=12 price=352.19 support=325.25 resistance=379.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=309759712.0 spike=6.03
- EALR.CA: score=12.86 buy_ready=False sector_rank=12 price=385.01 support=340.0 resistance=456.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=30815726.0 spike=1.17
- EASB.CA: score=21.6 buy_ready=False sector_rank=12 price=8.17 support=7.16 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=17624910.0 spike=1.04
- EAST.CA: score=8.82 buy_ready=False sector_rank=19 price=32.76 support=33.04 resistance=36.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.25 liquidity=105060488.0 spike=1.55
- EBSC.CA: score=9.61 buy_ready=False sector_rank=12 price=2.02 support=1.88 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=2089077.13 spike=0.14
- ECAP.CA: score=7.01 buy_ready=False sector_rank=12 price=32.09 support=31.16 resistance=39.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.53 liquidity=2482316.0 spike=0.2
- EDFM.CA: score=10.07 buy_ready=False sector_rank=12 price=413.37 support=394.0 resistance=432.0 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=56.63 liquidity=543168.17 spike=0.33
- EEII.CA: score=5.59 buy_ready=False sector_rank=12 price=2.18 support=2.15 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.13 liquidity=2065138.13 spike=0.09
- EFIC.CA: score=14.23 buy_ready=False sector_rank=7 price=195.0 support=192.75 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=52830176.0 spike=0.56
- EFID.CA: score=16.72 buy_ready=False sector_rank=19 price=30.75 support=29.71 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.82 liquidity=56448620.0 spike=0.97
- EFIH.CA: score=17.43 buy_ready=False sector_rank=13 price=23.61 support=22.16 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.53 liquidity=48667588.0 spike=0.73
- EGAL.CA: score=20.23 buy_ready=False sector_rank=7 price=359.97 support=321.01 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=55.66 liquidity=33311872.0 spike=0.29
- EGAS.CA: score=11.23 buy_ready=False sector_rank=5 price=56.18 support=55.0 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.85 liquidity=2862802.75 spike=0.32
- EGBE.CA: score=2.63 buy_ready=False sector_rank=10 price=0.5 support=0.49 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=19569.75 spike=0.14
- EGCH.CA: score=18.23 buy_ready=False sector_rank=7 price=13.88 support=13.3 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.09 liquidity=35066504.0 spike=0.3
- EGSA.CA: score=11.83 buy_ready=False sector_rank=1 price=9.0 support=8.67 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=78.18 liquidity=10410.0 spike=1.21
- EGTS.CA: score=14.99 buy_ready=False sector_rank=8 price=17.0 support=16.17 resistance=18.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.26 liquidity=14796808.0 spike=0.59
- EHDR.CA: score=14.68 buy_ready=False sector_rank=12 price=2.73 support=2.79 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.0 liquidity=23589778.0 spike=1.08
- EKHO.CA: score=6.36 buy_ready=False sector_rank=5 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=13.61 buy_ready=False sector_rank=17 price=1.94 support=1.98 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.24 liquidity=93817920.0 spike=1.33
- ELKA.CA: score=14.52 buy_ready=False sector_rank=12 price=1.75 support=1.7 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.88 liquidity=13769303.0 spike=0.31
- ELNA.CA: score=-1.19 buy_ready=False sector_rank=12 price=35.74 support=33.96 resistance=38.99 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=22.51 liquidity=288922.17 spike=0.62
- ELSH.CA: score=14.52 buy_ready=False sector_rank=12 price=12.72 support=12.71 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.15 liquidity=14836793.0 spike=0.38
- ELWA.CA: score=6.12 buy_ready=False sector_rank=12 price=1.7 support=1.62 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=1597306.88 spike=0.65
- EMFD.CA: score=19.99 buy_ready=False sector_rank=8 price=14.19 support=11.51 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=73.22 liquidity=122725120.0 spike=0.76
- ENGC.CA: score=1.66 buy_ready=False sector_rank=12 price=41.3 support=41.0 resistance=51.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=31.07 liquidity=2133281.0 spike=0.13
- EOSB.CA: score=9.54 buy_ready=False sector_rank=12 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=17259.01 spike=0.25
- EPCO.CA: score=17.52 buy_ready=False sector_rank=12 price=11.03 support=10.8 resistance=12.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.03 liquidity=11783140.0 spike=0.58
- EPPK.CA: score=-5.06 buy_ready=False sector_rank=12 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=24.04 buy_ready=False sector_rank=1 price=131.19 support=112.1 resistance=135.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=88.67 liquidity=251794528.0 spike=1.32
- ETRS.CA: score=16.9 buy_ready=False sector_rank=12 price=10.88 support=10.66 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.56 liquidity=9380039.0 spike=0.44
- EXPA.CA: score=17.61 buy_ready=False sector_rank=10 price=20.8 support=19.8 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.89 liquidity=11613206.0 spike=0.33
- FAIT.CA: score=12.29 buy_ready=False sector_rank=10 price=45.68 support=39.58 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=67.11 liquidity=2675817.0 spike=0.33
- FAITA.CA: score=4.63 buy_ready=False sector_rank=10 price=0.99 support=0.98 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=47.14 liquidity=15605.02 spike=0.3
- FERC.CA: score=8.48 buy_ready=False sector_rank=7 price=77.53 support=76.7 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.11 liquidity=4250720.5 spike=0.22
- FWRY.CA: score=14.43 buy_ready=False sector_rank=13 price=18.87 support=18.66 resistance=19.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=76518576.0 spike=0.57
- GBCO.CA: score=19.56 buy_ready=False sector_rank=14 price=30.55 support=27.51 resistance=31.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=62.86 liquidity=82733056.0 spike=1.59
- GDWA.CA: score=13.52 buy_ready=False sector_rank=12 price=0.77 support=0.76 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.68 liquidity=22753662.0 spike=0.55
- GGCC.CA: score=17.52 buy_ready=False sector_rank=12 price=0.88 support=0.83 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.14 liquidity=26554678.0 spike=0.64
- GIHD.CA: score=19.52 buy_ready=False sector_rank=12 price=72.82 support=58.01 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=73.32 liquidity=12759785.0 spike=0.43
- GMCI.CA: score=0.76 buy_ready=False sector_rank=12 price=1.75 support=1.75 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=24.14 liquidity=839412.19 spike=1.7
- GRCA.CA: score=4.74 buy_ready=False sector_rank=12 price=43.43 support=40.0 resistance=46.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=87466264.0 spike=1.11
- GSSC.CA: score=12.21 buy_ready=False sector_rank=12 price=292.69 support=278.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=46.66 liquidity=2684278.75 spike=0.21
- GTWL.CA: score=17.52 buy_ready=False sector_rank=12 price=236.89 support=165.0 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=66.99 liquidity=59167216.0 spike=0.2
- HDBK.CA: score=4.75 buy_ready=False sector_rank=10 price=116.28 support=109.98 resistance=116.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=61658680.0 spike=1.07
- HELI.CA: score=20.85 buy_ready=False sector_rank=8 price=8.21 support=7.34 resistance=8.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.7 liquidity=216391296.0 spike=1.43
- HRHO.CA: score=13.06 buy_ready=False sector_rank=16 price=25.19 support=25.21 resistance=26.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.59 liquidity=36760176.0 spike=0.37
- ICID.CA: score=15.2 buy_ready=False sector_rank=12 price=18.19 support=14.5 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.93 liquidity=5673407.0 spike=0.26
- IDRE.CA: score=17.52 buy_ready=False sector_rank=12 price=53.71 support=51.0 resistance=57.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=58.73 liquidity=10321670.0 spike=1.0
- IFAP.CA: score=16.17 buy_ready=False sector_rank=2 price=20.31 support=20.05 resistance=22.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=40.83 liquidity=7774591.0 spike=0.32
- INFI.CA: score=10.52 buy_ready=False sector_rank=12 price=133.29 support=130.15 resistance=174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=16.76 liquidity=7991482.0 spike=0.21
- IRON.CA: score=10.07 buy_ready=False sector_rank=7 price=27.45 support=27.08 resistance=33.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=5.54 liquidity=20290338.0 spike=1.42
- ISMA.CA: score=6.74 buy_ready=False sector_rank=12 price=30.02 support=28.05 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.48 liquidity=7211709.0 spike=0.27
- ISMQ.CA: score=13.73 buy_ready=False sector_rank=7 price=8.82 support=8.68 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.59 liquidity=8500110.0 spike=0.29
- ISPH.CA: score=10.74 buy_ready=False sector_rank=15 price=12.21 support=11.9 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.74 liquidity=113346528.0 spike=1.72
- JUFO.CA: score=10.06 buy_ready=False sector_rank=19 price=27.08 support=26.45 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=51.33 liquidity=5342808.0 spike=0.25
- KABO.CA: score=20.25 buy_ready=False sector_rank=6 price=9.3 support=8.82 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=60.58 liquidity=42299780.0 spike=0.79
- KWIN.CA: score=9.52 buy_ready=False sector_rank=12 price=87.44 support=84.5 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=26.96 liquidity=17048534.0 spike=0.26
- KZPC.CA: score=19.52 buy_ready=False sector_rank=12 price=14.45 support=12.14 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.52 liquidity=13409051.0 spike=0.21
- LCSW.CA: score=13.33 buy_ready=False sector_rank=20 price=32.79 support=32.83 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.59 liquidity=9736294.0 spike=0.34
- LUTS.CA: score=4.52 buy_ready=False sector_rank=12 price=1.0 support=0.93 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=121286688.0 spike=0.44
- MAAL.CA: score=6.02 buy_ready=False sector_rank=12 price=8.54 support=8.18 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=39.87 liquidity=1499980.38 spike=0.14
- MASR.CA: score=18.52 buy_ready=False sector_rank=12 price=7.89 support=7.49 resistance=8.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.3 liquidity=50370864.0 spike=0.56
- MBSC.CA: score=16.6 buy_ready=False sector_rank=20 price=380.86 support=355.04 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.68 liquidity=44761044.0 spike=0.74
- MCQE.CA: score=11.6 buy_ready=False sector_rank=20 price=223.0 support=212.01 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.0 liquidity=28079988.0 spike=0.72
- MCRO.CA: score=16.7 buy_ready=False sector_rank=12 price=1.72 support=1.44 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.5 liquidity=126797584.0 spike=1.09
- MENA.CA: score=0.89 buy_ready=False sector_rank=8 price=6.66 support=6.58 resistance=7.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=29.21 liquidity=899182.5 spike=0.31
- MEPA.CA: score=20.31 buy_ready=False sector_rank=12 price=1.93 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=58.23 liquidity=8781636.0 spike=0.25
- MFPC.CA: score=17.61 buy_ready=False sector_rank=7 price=48.74 support=38.93 resistance=48.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=80.29 liquidity=151399248.0 spike=1.19
- MFSC.CA: score=6.01 buy_ready=False sector_rank=12 price=48.72 support=48.6 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.13 liquidity=1484088.25 spike=0.3
- MHOT.CA: score=10.3 buy_ready=False sector_rank=9 price=17.81 support=17.72 resistance=19.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=50.89 liquidity=3433354.5 spike=0.31
- MICH.CA: score=12.43 buy_ready=False sector_rank=12 price=48.7 support=47.2 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.97 liquidity=4904586.0 spike=0.19
- MILS.CA: score=8.46 buy_ready=False sector_rank=12 price=200.0 support=192.22 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=21.55 liquidity=5938335.5 spike=0.11
- MIPH.CA: score=9.34 buy_ready=False sector_rank=15 price=809.0 support=700.2 resistance=820.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.41 liquidity=3046362.25 spike=0.74
- MOED.CA: score=16.52 buy_ready=False sector_rank=12 price=0.79 support=0.69 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=55.04 liquidity=32664284.0 spike=0.27
- MOIL.CA: score=10.46 buy_ready=False sector_rank=5 price=0.68 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.14 liquidity=93110.01 spike=0.44
- MOIN.CA: score=15.81 buy_ready=False sector_rank=12 price=36.4 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.28 liquidity=6283026.5 spike=0.21
- MOSC.CA: score=4.43 buy_ready=False sector_rank=12 price=309.08 support=305.0 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=24.31 liquidity=1903488.75 spike=0.22
- MPCI.CA: score=17.52 buy_ready=False sector_rank=12 price=410.0 support=345.0 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.36 liquidity=113515584.0 spike=0.72
- MPCO.CA: score=25.52 buy_ready=False sector_rank=2 price=2.7 support=2.07 resistance=2.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.67 liquidity=164359648.0 spike=1.06
- MPRC.CA: score=14.52 buy_ready=False sector_rank=12 price=38.6 support=38.31 resistance=46.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.12 liquidity=10602006.0 spike=0.27
- MTIE.CA: score=14.38 buy_ready=False sector_rank=14 price=8.41 support=8.1 resistance=9.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.55 liquidity=15452135.0 spike=0.35
- NAHO.CA: score=-5.44 buy_ready=False sector_rank=12 price=0.14 support=0.14 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33410.51 spike=0.32
- NCCW.CA: score=18.98 buy_ready=False sector_rank=12 price=8.3 support=5.59 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=81.34 liquidity=72742224.0 spike=1.23
- NEDA.CA: score=4.86 buy_ready=False sector_rank=12 price=2.72 support=2.7 resistance=2.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=51.35 liquidity=334828.63 spike=0.35
- NHPS.CA: score=3.26 buy_ready=False sector_rank=12 price=76.39 support=75.31 resistance=98.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=4.03 liquidity=3731373.25 spike=0.16
- NINH.CA: score=9.52 buy_ready=False sector_rank=12 price=20.98 support=20.5 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=15.11 liquidity=16115541.0 spike=0.52
- NIPH.CA: score=12.3 buy_ready=False sector_rank=15 price=318.55 support=301.0 resistance=414.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=19.41 liquidity=138866832.0 spike=0.67
- OBRI.CA: score=9.33 buy_ready=False sector_rank=12 price=30.54 support=30.1 resistance=34.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.46 liquidity=5805899.0 spike=0.27
- OCDI.CA: score=14.99 buy_ready=False sector_rank=8 price=29.6 support=29.25 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.4 liquidity=43946512.0 spike=0.52
- OCPH.CA: score=6.66 buy_ready=False sector_rank=12 price=241.94 support=210.0 resistance=277.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.82 liquidity=6137537.5 spike=0.64
- ODIN.CA: score=3.89 buy_ready=False sector_rank=12 price=2.74 support=2.55 resistance=3.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=22.22 liquidity=4364072.0 spike=0.15
- OFH.CA: score=19.52 buy_ready=False sector_rank=12 price=1.04 support=0.88 resistance=1.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.28 liquidity=48291500.0 spike=0.43
- OIH.CA: score=20.4 buy_ready=False sector_rank=3 price=2.17 support=1.76 resistance=2.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=68.52 liquidity=94473624.0 spike=0.77
- OLFI.CA: score=14.6 buy_ready=False sector_rank=19 price=22.51 support=22.07 resistance=25.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=41.34 liquidity=23248026.0 spike=1.44
- ORAS.CA: score=4.6 buy_ready=False sector_rank=11 price=844.34 support=829.0 resistance=855.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=150633008.0 spike=1.0
- ORHD.CA: score=20.89 buy_ready=False sector_rank=8 price=42.92 support=40.28 resistance=43.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.03 liquidity=190757808.0 spike=1.45
- ORWE.CA: score=20.25 buy_ready=False sector_rank=6 price=26.78 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.3 liquidity=19506084.0 spike=0.37
- PHAR.CA: score=12.3 buy_ready=False sector_rank=15 price=117.5 support=117.01 resistance=141.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=18.95 liquidity=114476536.0 spike=0.63
- PHDC.CA: score=9.99 buy_ready=False sector_rank=8 price=13.72 support=13.65 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.15 liquidity=44788804.0 spike=0.21
- PHTV.CA: score=11.45 buy_ready=False sector_rank=12 price=367.22 support=311.27 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=66.55 liquidity=3026086.0 spike=1.45
- POUL.CA: score=13.72 buy_ready=False sector_rank=19 price=38.0 support=36.97 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.85 liquidity=10931403.0 spike=0.46
- PRCL.CA: score=13.6 buy_ready=False sector_rank=20 price=32.28 support=30.9 resistance=36.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.12 liquidity=13466418.0 spike=0.63
- PRDC.CA: score=9.99 buy_ready=False sector_rank=8 price=7.95 support=7.77 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=27.27 liquidity=16684979.0 spike=0.25
- PRMH.CA: score=8.06 buy_ready=False sector_rank=12 price=2.53 support=2.28 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=59.15 liquidity=3534454.5 spike=0.32
- RACC.CA: score=7.71 buy_ready=False sector_rank=12 price=9.65 support=9.4 resistance=10.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.55 liquidity=3190666.5 spike=0.15
- RAKT.CA: score=11.16 buy_ready=False sector_rank=12 price=22.65 support=21.4 resistance=23.02 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=57.94 liquidity=315582.44 spike=1.16
- RAYA.CA: score=13.82 buy_ready=False sector_rank=18 price=7.1 support=6.95 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.09 liquidity=32349028.0 spike=0.56
- RMDA.CA: score=19.3 buy_ready=False sector_rank=15 price=6.17 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.15 liquidity=30732796.0 spike=0.53
- ROTO.CA: score=6.12 buy_ready=False sector_rank=12 price=40.47 support=35.02 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=13.49 liquidity=6597493.0 spike=0.55
- RREI.CA: score=13.32 buy_ready=False sector_rank=12 price=4.35 support=4.24 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.12 liquidity=5791814.0 spike=0.2
- RTVC.CA: score=1.19 buy_ready=False sector_rank=12 price=3.87 support=3.78 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.62 liquidity=1669691.63 spike=0.23
- RUBX.CA: score=9.22 buy_ready=False sector_rank=12 price=13.8 support=12.94 resistance=14.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=67662296.0 spike=3.35
- SAUD.CA: score=10.48 buy_ready=False sector_rank=10 price=23.1 support=22.7 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.51 liquidity=2863560.0 spike=0.19
- SCEM.CA: score=16.6 buy_ready=False sector_rank=20 price=95.2 support=94.0 resistance=112.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.69 liquidity=49295844.0 spike=0.33
- SCFM.CA: score=5.68 buy_ready=False sector_rank=12 price=270.47 support=265.51 resistance=305.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=36.63 liquidity=1151588.75 spike=0.12
- SCTS.CA: score=1.83 buy_ready=False sector_rank=4 price=604.58 support=566.66 resistance=660.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=27.62 liquidity=428131.31 spike=0.08
- SDTI.CA: score=13.66 buy_ready=False sector_rank=12 price=73.79 support=67.0 resistance=76.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=70.2 liquidity=6135088.5 spike=0.3
- SEIG.CA: score=9.52 buy_ready=False sector_rank=12 price=248.3 support=230.5 resistance=267.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11281761.0 spike=7.38
- SIPC.CA: score=19.52 buy_ready=False sector_rank=12 price=5.96 support=4.1 resistance=6.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=65.96 liquidity=61552652.0 spike=0.99
- SKPC.CA: score=20.23 buy_ready=False sector_rank=7 price=18.28 support=16.8 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.96 liquidity=116295856.0 spike=0.82
- SMFR.CA: score=2.08 buy_ready=False sector_rank=12 price=238.65 support=236.1 resistance=276.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.97 liquidity=2558100.0 spike=0.25
- SNFC.CA: score=18.18 buy_ready=False sector_rank=12 price=11.0 support=10.26 resistance=11.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.39 liquidity=9657219.0 spike=0.71
- SPIN.CA: score=15.86 buy_ready=False sector_rank=6 price=17.2 support=17.21 resistance=20.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.77 liquidity=7611951.0 spike=0.26
- SPMD.CA: score=9.52 buy_ready=False sector_rank=12 price=0.48 support=0.48 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=384768160.0 spike=8.17
- SUGR.CA: score=20.72 buy_ready=False sector_rank=19 price=60.67 support=50.0 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.6 liquidity=19013232.0 spike=0.27
- SVCE.CA: score=19.52 buy_ready=False sector_rank=12 price=11.64 support=10.28 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.71 liquidity=63732512.0 spike=0.39
- SWDY.CA: score=16.95 buy_ready=False sector_rank=17 price=124.41 support=115.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.74 liquidity=29187756.0 spike=0.3
- TALM.CA: score=21.68 buy_ready=False sector_rank=4 price=22.52 support=17.11 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.24 liquidity=93122376.0 spike=1.64
- TMGH.CA: score=14.99 buy_ready=False sector_rank=8 price=94.99 support=94.9 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.6 liquidity=174744640.0 spike=0.65
- TRTO.CA: score=9.53 buy_ready=False sector_rank=12 price=0.07 support=0.04 resistance=0.08 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=67.92 liquidity=10220.28 spike=0.37
- UEFM.CA: score=4.65 buy_ready=False sector_rank=12 price=534.5 support=440.66 resistance=557.0 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=46.56 liquidity=128280.0 spike=0.05
- UEGC.CA: score=5.42 buy_ready=False sector_rank=12 price=1.8 support=1.69 resistance=1.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=66206300.0 spike=1.45
- UNIP.CA: score=14.52 buy_ready=False sector_rank=12 price=0.38 support=0.35 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=53.61 liquidity=14136810.0 spike=0.41
- UNIT.CA: score=24.67 buy_ready=False sector_rank=8 price=19.61 support=18.11 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.02 liquidity=30606082.0 spike=2.34
- WCDF.CA: score=13.87 buy_ready=False sector_rank=12 price=751.54 support=630.0 resistance=759.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=88.79 liquidity=4528786.0 spike=1.41
- WKOL.CA: score=19.52 buy_ready=False sector_rank=12 price=355.03 support=332.56 resistance=372.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.8 liquidity=17396206.0 spike=0.9
- ZEOT.CA: score=10.66 buy_ready=False sector_rank=12 price=13.04 support=13.04 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.46 liquidity=3135549.0 spike=0.39
- ZMID.CA: score=17.99 buy_ready=False sector_rank=8 price=9.17 support=7.39 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=69.21 liquidity=124071632.0 spike=0.51

## Backtesting Lite
- MPCO.CA: 180d return=63.95%, max drawdown=-16.86%, MA20>MA50 days last20=20, as_of=2026-09-14T21:00:00+00:00
- UNIT.CA: 180d return=82.24%, max drawdown=-23.72%, MA20>MA50 days last20=20, as_of=2026-09-14T21:00:00+00:00
- ETEL.CA: 180d return=106.98%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-09-14T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=623 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- UNIT.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=623 sources=3 expected=United Housing and Development summary=United Housing’s shareholders pass EGP 0.12/shr dividends for 2025; United Housing unveils EGP 5.9bn mixed-use project in Alexandria; United Housing’s consolidated net profits exceed EGP 174.5m in 9M-25
  - United Housing’s shareholders pass EGP 0.12/shr dividends for 2025: https://english.mubasher.info/news/4591202/United-Housing-s-shareholders-pass-EGP-0-12-shr-dividends-for-2025/
  - United Housing unveils EGP 5.9bn mixed-use project in Alexandria: https://english.mubasher.info/news/4540667/United-Housing-unveils-EGP-5-9bn-mixed-use-project-in-Alexandria/
  - United Housing’s consolidated net profits exceed EGP 174.5m in 9M-25: https://english.mubasher.info/news/4530945/United-Housing-s-consolidated-net-profits-exceed-EGP-174-5m-in-9M-25/
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- CIRA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Investment and Real Estate Development summary=CIRA Education take over 51% of L’École Française Hurghada; CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion; CIRA Education launches Middle East’s 1st initiative for care economy
  - CIRA Education take over 51% of L’École Française Hurghada: https://english.mubasher.info/news/4488666/CIRA-Education-take-over-51-of-L-%C3%89cole-Fran%C3%A7aise-Hurghada/
  - CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion: https://english.mubasher.info/news/4393636/CIRA-s-majority-shareholder-acquires-37-5-additional-equity-backs-regional-expansion/
  - CIRA Education launches Middle East’s 1st initiative for care economy: https://english.mubasher.info/news/4391766/CIRA-Education-launches-Middle-East-s-1st-initiative-for-care-economy/
- CERA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=The Arab Ceramic Co. summary=Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- EASB.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Arabian Company (Themar) for securities Brokerage EAC summary=Evidence rejected for EASB.CA: source text did not clearly match EASB.CA / Egyptian Arabian Company (Themar) for securities Brokerage EAC.
- ORHD.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Development Egypt summary=Evidence rejected for ORHD.CA: source text did not clearly match ORHD.CA / Orascom Development Egypt.

## Warnings
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for UNIT.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
- Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence rejected for EASB.CA: source text did not clearly match EASB.CA / Egyptian Arabian Company (Themar) for securities Brokerage EAC.
- Evidence rejected for ORHD.CA: source text did not clearly match ORHD.CA / Orascom Development Egypt.
