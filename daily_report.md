# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-09-14T11:01:24.209703+00:00
Generated Cairo: 2026-09-14 14:01
Run timing: target 08:45 Cairo | generated Cairo 2026-09-14 14:01 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-14 13:57

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 167/189
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, September 14
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 36.84% / above MA50 47.37%
- EGX70 regime: BEARISH / above MA20 31.43% / above MA50 60.0%
- Sector breadth: 14.29%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=1572125184.0 spike=2.03 score=8.46
- COMI.CA: liquidity=530186656.0 spike=1.07 score=15.18
- CERA.CA: liquidity=353077312.0 spike=5.22 score=9.86
- TALM.CA: liquidity=324727456.0 spike=12.04 score=12.4
- DTPP.CA: liquidity=246482976.0 spike=5.75 score=9.86

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: 

## Top Liquidity Spikes
- UNIT.CA: spike=18.8 liquidity=112301504.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SPMD.CA: spike=13.9 liquidity=153241456.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- TALM.CA: spike=12.04 liquidity=324727456.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DTPP.CA: spike=5.75 liquidity=246482976.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CERA.CA: spike=5.22 liquidity=353077312.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=10.79 5d=4.71% 20d=7.92% aboveMA50=100.0%
- #2 Textiles: score=10.37 5d=4.06% 20d=13.56% aboveMA50=100.0%
- #3 Education: score=9.75 5d=0.0% 20d=0.0% aboveMA50=33.33%
- #4 Investment Holding: score=6.71 5d=3.57% 20d=4.29% aboveMA50=66.67%
- #5 Basic Resources & Chemicals: score=4.24 5d=-2.21% 20d=3.93% aboveMA50=80.0%
- #6 Industrial Goods & Cables: score=3.97 5d=-3.25% 20d=5.64% aboveMA50=50.0%
- #7 Energy & Petrochemicals: score=3.95 5d=0.0% 20d=0.07% aboveMA50=75.0%
- #8 Real Estate: score=2.77 5d=-0.47% 20d=-0.25% aboveMA50=46.15%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CIRA.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=far above support
- ORWE.CA: BULLISH_WATCH score=96 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MOED.CA: BULLISH_WATCH score=84.14 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- KABO.CA: BULLISH_WATCH score=82 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; overheated RSI
- MASR.CA: BULLISH_WATCH score=78.14 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- ACGC.CA: BULLISH_WATCH score=78 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended; far above support
- SWDY.CA: BULLISH_WATCH score=73.97 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- HELI.CA: BULLISH_WATCH score=73.77 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- SDTI.CA: BULLISH_WATCH score=73.14 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- EBSC.CA: BULLISH_WATCH score=73.14 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=12.86 buy_ready=False sector_rank=11 price=309.96 support=295.0 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=24.51 liquidity=10471745.0 spike=0.29
- ABUK.CA: score=20.7 buy_ready=False sector_rank=5 price=88.51 support=75.01 resistance=94.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=68.87 liquidity=30255460.0 spike=0.18
- ACAMD.CA: score=16.86 buy_ready=False sector_rank=11 price=2.07 support=1.95 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=53.45 liquidity=28128644.0 spike=0.5
- ACGC.CA: score=25.4 buy_ready=False sector_rank=2 price=14.4 support=11.25 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=62.68 liquidity=21849544.0 spike=0.52
- ADCI.CA: score=5.21 buy_ready=False sector_rank=11 price=280.32 support=280.0 resistance=319.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=30.68 liquidity=2354831.0 spike=0.29
- ADIB.CA: score=15.04 buy_ready=False sector_rank=10 price=51.02 support=51.15 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=36.52 liquidity=37986632.0 spike=0.55
- ADPC.CA: score=14.86 buy_ready=False sector_rank=11 price=3.83 support=3.85 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=10496957.0 spike=0.38
- AFDI.CA: score=4.25 buy_ready=False sector_rank=11 price=52.22 support=52.11 resistance=68.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=17.72 liquidity=4391885.0 spike=0.16
- AFMC.CA: score=9.86 buy_ready=False sector_rank=11 price=162.49 support=157.0 resistance=267.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=21.7 liquidity=28253022.0 spike=0.39
- AJWA.CA: score=14.86 buy_ready=False sector_rank=11 price=179.0 support=175.15 resistance=202.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=39.16 liquidity=10660989.0 spike=0.19
- ALCN.CA: score=16.67 buy_ready=False sector_rank=19 price=30.95 support=30.03 resistance=34.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=46.26 liquidity=7810826.0 spike=0.25
- ALUM.CA: score=1.59 buy_ready=False sector_rank=11 price=25.6 support=25.53 resistance=27.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6733804.0 spike=0.32
- AMER.CA: score=13.11 buy_ready=False sector_rank=8 price=5.05 support=5.12 resistance=6.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=34.85 liquidity=22819236.0 spike=0.31
- AMES.CA: score=8.86 buy_ready=False sector_rank=11 price=55.37 support=57.01 resistance=173.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=0.55 liquidity=194545632.0 spike=0.84
- AMIA.CA: score=17.86 buy_ready=False sector_rank=11 price=17.79 support=12.71 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=48.73 liquidity=11234688.0 spike=0.16
- AMOC.CA: score=17.58 buy_ready=False sector_rank=7 price=12.93 support=10.3 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=75.7 liquidity=137286928.0 spike=0.71
- APSW.CA: score=4.55 buy_ready=False sector_rank=11 price=8.51 support=8.41 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=39.78 liquidity=694494.56 spike=0.58
- ARAB.CA: score=18.11 buy_ready=False sector_rank=8 price=0.25 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=56.36 liquidity=71090360.0 spike=0.73
- ARCC.CA: score=17.82 buy_ready=False sector_rank=12 price=72.23 support=71.51 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=60.5 liquidity=23753526.0 spike=0.28
- AREH.CA: score=16.86 buy_ready=False sector_rank=11 price=1.43 support=1.39 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=45.16 liquidity=10850693.0 spike=0.61
- ARVA.CA: score=4.86 buy_ready=False sector_rank=11 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=13.91 buy_ready=False sector_rank=11 price=61.41 support=62.01 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=41.04 liquidity=9050627.0 spike=0.34
- ASPI.CA: score=12.86 buy_ready=False sector_rank=11 price=0.44 support=0.41 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=25.89 liquidity=40535600.0 spike=0.77
- ATLC.CA: score=18.74 buy_ready=False sector_rank=13 price=6.85 support=5.2 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=8958153.0 spike=0.3
- ATQA.CA: score=17.7 buy_ready=False sector_rank=5 price=12.77 support=10.8 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=82.14 liquidity=49934164.0 spike=0.46
- AXPH.CA: score=10.18 buy_ready=False sector_rank=11 price=1663.22 support=1305.43 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=73.88 liquidity=2324524.0 spike=0.19
- BINV.CA: score=12.67 buy_ready=False sector_rank=4 price=51.87 support=46.25 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=65.86 liquidity=1272099.38 spike=0.11
- BIOC.CA: score=9.86 buy_ready=False sector_rank=11 price=287.07 support=285.0 resistance=555.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=8.94 liquidity=33091942.0 spike=0.23
- BTFH.CA: score=13.78 buy_ready=False sector_rank=13 price=2.89 support=2.91 resistance=3.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=35.71 liquidity=58806960.0 spike=0.57
- CAED.CA: score=9.58 buy_ready=False sector_rank=11 price=138.76 support=131.0 resistance=150.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=128906400.0 spike=3.36
- CANA.CA: score=18.04 buy_ready=False sector_rank=10 price=41.87 support=41.0 resistance=44.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=51.8 liquidity=11396161.0 spike=0.65
- CCAP.CA: score=8.46 buy_ready=False sector_rank=4 price=6.8 support=6.25 resistance=6.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1572125184.0 spike=2.03
- CCRS.CA: score=14.86 buy_ready=False sector_rank=11 price=2.48 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=24654658.0 spike=0.49
- CEFM.CA: score=14.14 buy_ready=False sector_rank=11 price=145.98 support=133.1 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=43.38 liquidity=4284903.0 spike=0.28
- CERA.CA: score=9.86 buy_ready=False sector_rank=11 price=1.36 support=1.34 resistance=1.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=353077312.0 spike=5.22
- CFGH.CA: score=7.86 buy_ready=False sector_rank=11 price=0.12 support=0.1 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=6705.16 spike=0.26
- CICH.CA: score=17.0 buy_ready=False sector_rank=13 price=12.55 support=12.0 resistance=13.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=62.81 liquidity=5075021.5 spike=1.07
- CIEB.CA: score=15.04 buy_ready=False sector_rank=10 price=24.45 support=24.3 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=50.13 liquidity=13640618.0 spike=0.93
- CIRA.CA: score=31.4 buy_ready=False sector_rank=3 price=39.8 support=32.1 resistance=39.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=56.62 liquidity=178061360.0 spike=5.17
- CLHO.CA: score=9.26 buy_ready=False sector_rank=18 price=15.93 support=16.0 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=26.96 liquidity=41660008.0 spike=0.52
- CNFN.CA: score=4.38 buy_ready=False sector_rank=13 price=4.57 support=4.72 resistance=4.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=33.93 liquidity=5596178.0 spike=0.39
- COMI.CA: score=15.18 buy_ready=False sector_rank=10 price=133.4 support=135.35 resistance=142.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=43.06 liquidity=530186656.0 spike=1.07
- COPR.CA: score=12.86 buy_ready=False sector_rank=11 price=0.46 support=0.43 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=28.48 liquidity=24673838.0 spike=0.26
- COSG.CA: score=17.86 buy_ready=False sector_rank=11 price=1.84 support=1.74 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=51.28 liquidity=17383480.0 spike=0.31
- CPCI.CA: score=6.33 buy_ready=False sector_rank=11 price=530.12 support=525.01 resistance=569.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=26.53 liquidity=3470388.25 spike=0.71
- CSAG.CA: score=10.8 buy_ready=False sector_rank=19 price=38.62 support=38.13 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=40.24 liquidity=3931059.5 spike=0.2
- DAPH.CA: score=17.86 buy_ready=False sector_rank=11 price=119.16 support=108.11 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=52.07 liquidity=14153895.0 spike=0.22
- DEIN.CA: score=7.86 buy_ready=False sector_rank=11 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=10.37 buy_ready=False sector_rank=17 price=27.37 support=27.79 resistance=29.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=50.73 liquidity=6029952.0 spike=0.75
- DSCW.CA: score=13.86 buy_ready=False sector_rank=11 price=1.81 support=1.84 resistance=2.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=30983804.0 spike=0.56
- DTPP.CA: score=9.86 buy_ready=False sector_rank=11 price=331.66 support=331.13 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=246482976.0 spike=5.75
- EALR.CA: score=5.78 buy_ready=False sector_rank=11 price=376.02 support=340.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=30.67 liquidity=5924582.5 spike=0.21
- EASB.CA: score=4.86 buy_ready=False sector_rank=11 price=8.7 support=8.63 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15513336.0 spike=0.99
- EAST.CA: score=8.34 buy_ready=False sector_rank=17 price=33.75 support=34.29 resistance=37.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=29.75 liquidity=27795882.0 spike=0.42
- EBSC.CA: score=14.2 buy_ready=False sector_rank=11 price=2.09 support=1.88 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=57.76 liquidity=2347664.75 spike=0.16
- ECAP.CA: score=1.58 buy_ready=False sector_rank=11 price=32.23 support=31.16 resistance=40.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=29.42 liquidity=1727731.13 spike=0.13
- EDFM.CA: score=11.53 buy_ready=False sector_rank=11 price=422.3 support=394.0 resistance=432.0 source=Yahoo Finance as_of=2026-09-12T21:00:00+00:00 freshness=FRESH RSI=64.44 liquidity=1637679.35 spike=1.02
- EEII.CA: score=8.86 buy_ready=False sector_rank=11 price=2.22 support=2.29 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=20.04 liquidity=11071667.0 spike=0.39
- EFIC.CA: score=19.7 buy_ready=False sector_rank=5 price=201.29 support=192.75 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=46.16 liquidity=88317264.0 spike=0.93
- EFID.CA: score=17.7 buy_ready=False sector_rank=17 price=30.15 support=29.71 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=36.72 liquidity=65644892.0 spike=1.18
- EFIH.CA: score=14.43 buy_ready=False sector_rank=16 price=22.98 support=22.16 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=38.62 liquidity=26942956.0 spike=0.34
- EGAL.CA: score=18.7 buy_ready=False sector_rank=5 price=360.08 support=321.01 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=70.98 liquidity=48727612.0 spike=0.34
- EGAS.CA: score=13.9 buy_ready=False sector_rank=7 price=56.44 support=55.21 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=38.96 liquidity=5316919.0 spike=0.53
- EGBE.CA: score=3.11 buy_ready=False sector_rank=10 price=0.49 support=0.51 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=15.69 liquidity=75886.8 spike=0.47
- EGCH.CA: score=18.7 buy_ready=False sector_rank=5 price=13.69 support=13.3 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=52.4 liquidity=61517348.0 spike=0.46
- EGSA.CA: score=11.91 buy_ready=False sector_rank=1 price=8.98 support=8.66 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=83.67 liquidity=9630.9 spike=1.25
- EGTS.CA: score=17.11 buy_ready=False sector_rank=8 price=16.76 support=16.17 resistance=19.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=48.57 liquidity=13392917.0 spike=0.47
- EHDR.CA: score=14.86 buy_ready=False sector_rank=11 price=2.84 support=2.81 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=41.51 liquidity=10625112.0 spike=0.42
- EKHO.CA: score=6.58 buy_ready=False sector_rank=7 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-09-12T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=14.75 buy_ready=False sector_rank=6 price=1.99 support=2.02 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=38.24 liquidity=72354136.0 spike=1.08
- ELKA.CA: score=14.86 buy_ready=False sector_rank=11 price=1.71 support=1.7 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=48.21 liquidity=32845566.0 spike=0.66
- ELNA.CA: score=-1.05 buy_ready=False sector_rank=11 price=35.74 support=35.17 resistance=38.99 source=Yahoo Finance as_of=2026-09-12T21:00:00+00:00 freshness=FRESH RSI=22.51 liquidity=95425.8 spike=0.21
- ELSH.CA: score=14.86 buy_ready=False sector_rank=11 price=13.02 support=12.97 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=48.39 liquidity=29765954.0 spike=0.71
- ELWA.CA: score=5.49 buy_ready=False sector_rank=11 price=1.74 support=1.62 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=47.69 liquidity=629063.12 spike=0.25
- EMFD.CA: score=17.11 buy_ready=False sector_rank=8 price=14.6 support=11.51 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=89.83 liquidity=62637152.0 spike=0.39
- ENGC.CA: score=6.94 buy_ready=False sector_rank=11 price=41.24 support=41.8 resistance=54.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=31.42 liquidity=7079662.0 spike=0.42
- EOSB.CA: score=11.88 buy_ready=False sector_rank=11 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-09-12T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=20235.73 spike=0.35
- EPCO.CA: score=17.86 buy_ready=False sector_rank=11 price=11.33 support=10.8 resistance=12.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=51.0 liquidity=11294978.0 spike=0.52
- EPPK.CA: score=-4.72 buy_ready=False sector_rank=11 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=26.4 buy_ready=False sector_rank=1 price=125.9 support=112.1 resistance=131.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=97907016.0 spike=0.51
- ETRS.CA: score=15.54 buy_ready=False sector_rank=11 price=10.83 support=10.7 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=45.16 liquidity=7679850.0 spike=0.32
- EXPA.CA: score=20.04 buy_ready=False sector_rank=10 price=20.74 support=19.8 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=63.66 liquidity=26072100.0 spike=0.7
- FAIT.CA: score=13.67 buy_ready=False sector_rank=10 price=45.96 support=39.58 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=74.18 liquidity=3632457.75 spike=0.41
- FAITA.CA: score=5.04 buy_ready=False sector_rank=10 price=0.99 support=0.98 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=46.51 liquidity=7412.74 spike=0.13
- FERC.CA: score=20.7 buy_ready=False sector_rank=5 price=78.79 support=76.7 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=57.57 liquidity=10261020.0 spike=0.5
- FWRY.CA: score=16.43 buy_ready=False sector_rank=16 price=18.8 support=18.66 resistance=19.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=46.84 liquidity=106710984.0 spike=0.78
- GBCO.CA: score=15.65 buy_ready=False sector_rank=20 price=29.0 support=27.51 resistance=31.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=56.7 liquidity=24440208.0 spike=0.49
- GDWA.CA: score=13.86 buy_ready=False sector_rank=11 price=0.77 support=0.77 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=48.45 liquidity=22511822.0 spike=0.53
- GGCC.CA: score=14.86 buy_ready=False sector_rank=11 price=0.86 support=0.83 resistance=1.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=44.87 liquidity=16077897.0 spike=0.35
- GIHD.CA: score=19.86 buy_ready=False sector_rank=11 price=73.69 support=58.01 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=74.67 liquidity=16527383.0 spike=0.53
- GMCI.CA: score=4.29 buy_ready=False sector_rank=11 price=1.83 support=1.79 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=35.0 liquidity=436344.81 spike=0.86
- GRCA.CA: score=4.86 buy_ready=False sector_rank=11 price=42.13 support=42.0 resistance=48.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46791748.0 spike=0.62
- GSSC.CA: score=14.42 buy_ready=False sector_rank=11 price=286.12 support=278.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=56.31 liquidity=4565900.0 spike=0.34
- GTWL.CA: score=17.86 buy_ready=False sector_rank=11 price=239.96 support=133.35 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=74.58 liquidity=86014040.0 spike=0.28
- HDBK.CA: score=19.04 buy_ready=False sector_rank=10 price=106.56 support=87.45 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=69.2 liquidity=27016984.0 spike=0.47
- HELI.CA: score=22.11 buy_ready=False sector_rank=8 price=7.91 support=7.34 resistance=8.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=52.13 liquidity=75136208.0 spike=0.48
- HRHO.CA: score=15.78 buy_ready=False sector_rank=13 price=25.27 support=25.33 resistance=26.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=41.03 liquidity=43421560.0 spike=0.44
- ICID.CA: score=11.7 buy_ready=False sector_rank=11 price=18.31 support=13.4 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=64.78 liquidity=1841813.5 spike=0.06
- IDRE.CA: score=10.1 buy_ready=False sector_rank=11 price=51.6 support=51.02 resistance=57.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=50.57 liquidity=2242696.25 spike=0.22
- IFAP.CA: score=17.66 buy_ready=False sector_rank=14 price=20.43 support=20.2 resistance=22.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=49.05 liquidity=10790814.0 spike=0.42
- INFI.CA: score=4.86 buy_ready=False sector_rank=11 price=135.14 support=135.1 resistance=146.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15092110.0 spike=0.35
- IRON.CA: score=10.54 buy_ready=False sector_rank=5 price=28.0 support=27.84 resistance=33.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=7.12 liquidity=19519436.0 spike=1.42
- ISMA.CA: score=12.54 buy_ready=False sector_rank=11 price=29.95 support=29.0 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=36.94 liquidity=7684893.0 spike=0.28
- ISMQ.CA: score=15.7 buy_ready=False sector_rank=5 price=8.94 support=9.0 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=41.28 liquidity=18341754.0 spike=0.54
- ISPH.CA: score=9.26 buy_ready=False sector_rank=18 price=12.3 support=12.75 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=30.17 liquidity=55655500.0 spike=0.79
- JUFO.CA: score=12.5 buy_ready=False sector_rank=17 price=26.77 support=26.45 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=54.37 liquidity=7153899.0 spike=0.27
- KABO.CA: score=25.4 buy_ready=False sector_rank=2 price=9.65 support=8.77 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=71.57 liquidity=26813922.0 spike=0.52
- KWIN.CA: score=14.86 buy_ready=False sector_rank=11 price=85.34 support=84.5 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=44.6 liquidity=11381969.0 spike=0.17
- KZPC.CA: score=21.86 buy_ready=False sector_rank=11 price=13.81 support=10.48 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=51.86 liquidity=19677574.0 spike=0.3
- LCSW.CA: score=12.01 buy_ready=False sector_rank=12 price=33.95 support=32.61 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=48.41 liquidity=4186170.25 spike=0.13
- LUTS.CA: score=4.86 buy_ready=False sector_rank=11 price=0.89 support=0.87 resistance=0.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=69435504.0 spike=0.25
- MAAL.CA: score=8.92 buy_ready=False sector_rank=11 price=8.53 support=8.18 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=50.46 liquidity=4060157.25 spike=0.35
- MASR.CA: score=21.94 buy_ready=False sector_rank=11 price=7.94 support=7.49 resistance=8.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=61.19 liquidity=93690880.0 spike=1.04
- MBSC.CA: score=4.82 buy_ready=False sector_rank=12 price=386.53 support=385.05 resistance=409.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14677299.0 spike=0.16
- MCQE.CA: score=17.82 buy_ready=False sector_rank=12 price=215.01 support=212.01 resistance=255.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=53.82 liquidity=20916540.0 spike=0.39
- MCRO.CA: score=20.8 buy_ready=False sector_rank=11 price=1.72 support=1.44 resistance=1.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=65.79 liquidity=155841968.0 spike=1.47
- MENA.CA: score=0.84 buy_ready=False sector_rank=8 price=6.68 support=6.58 resistance=7.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=32.14 liquidity=728799.44 spike=0.13
- MEPA.CA: score=21.86 buy_ready=False sector_rank=11 price=1.95 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=62.16 liquidity=25006452.0 spike=0.72
- MFPC.CA: score=17.7 buy_ready=False sector_rank=5 price=46.61 support=38.93 resistance=48.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=80.13 liquidity=64920736.0 spike=0.48
- MFSC.CA: score=11.25 buy_ready=False sector_rank=11 price=49.62 support=48.88 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=3398368.5 spike=0.6
- MHOT.CA: score=13.06 buy_ready=False sector_rank=9 price=17.95 support=17.72 resistance=19.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=4022149.0 spike=0.29
- MICH.CA: score=12.3 buy_ready=False sector_rank=11 price=48.89 support=47.11 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=50.42 liquidity=4441792.0 spike=0.16
- MILS.CA: score=12.86 buy_ready=False sector_rank=11 price=200.7 support=190.25 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=32.05 liquidity=13481655.0 spike=0.23
- MIPH.CA: score=7.79 buy_ready=False sector_rank=18 price=789.93 support=700.2 resistance=820.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=53.98 liquidity=528188.63 spike=0.13
- MOED.CA: score=21.68 buy_ready=False sector_rank=11 price=0.81 support=0.68 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=47.41 liquidity=219175424.0 spike=1.91
- MOIL.CA: score=8.76 buy_ready=False sector_rank=7 price=0.67 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=183750.86 spike=0.8
- MOIN.CA: score=19.86 buy_ready=False sector_rank=11 price=35.0 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=53.87 liquidity=13934749.0 spike=0.47
- MOSC.CA: score=4.01 buy_ready=False sector_rank=11 price=306.05 support=300.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=32.6 liquidity=1154988.38 spike=0.09
- MPCI.CA: score=19.86 buy_ready=False sector_rank=11 price=415.01 support=345.0 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=49.17 liquidity=87680528.0 spike=0.52
- MPCO.CA: score=5.04 buy_ready=False sector_rank=14 price=2.54 support=2.54 resistance=2.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=175112016.0 spike=1.19
- MPRC.CA: score=14.86 buy_ready=False sector_rank=11 price=39.0 support=38.6 resistance=46.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=40.6 liquidity=22944880.0 spike=0.54
- MTIE.CA: score=14.65 buy_ready=False sector_rank=20 price=8.25 support=8.25 resistance=9.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=48.37 liquidity=16519897.0 spike=0.3
- NAHO.CA: score=2.87 buy_ready=False sector_rank=11 price=0.14 support=0.11 resistance=0.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=9672.57 spike=0.09
- NCCW.CA: score=6.0 buy_ready=False sector_rank=11 price=7.71 support=7.62 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=78508904.0 spike=1.57
- NEDA.CA: score=5.88 buy_ready=False sector_rank=11 price=2.73 support=2.7 resistance=2.97 source=Yahoo Finance as_of=2026-09-12T21:00:00+00:00 freshness=FRESH RSI=43.18 liquidity=965194.24 spike=1.03
- NHPS.CA: score=9.86 buy_ready=False sector_rank=11 price=77.71 support=80.5 resistance=98.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=19.41 liquidity=11237351.0 spike=0.43
- NINH.CA: score=12.67 buy_ready=False sector_rank=11 price=21.74 support=21.53 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=49.66 liquidity=7817896.5 spike=0.26
- NIPH.CA: score=12.26 buy_ready=False sector_rank=18 price=317.58 support=326.51 resistance=414.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=16.88 liquidity=113066144.0 spike=0.45
- OBRI.CA: score=14.26 buy_ready=False sector_rank=11 price=31.5 support=31.81 resistance=34.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=42.11 liquidity=8407955.0 spike=0.38
- OCDI.CA: score=5.49 buy_ready=False sector_rank=8 price=30.01 support=30.0 resistance=31.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=108753960.0 spike=1.19
- OCPH.CA: score=3.94 buy_ready=False sector_rank=11 price=242.51 support=242.0 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=27.32 liquidity=3081442.5 spike=0.25
- ODIN.CA: score=9.86 buy_ready=False sector_rank=11 price=2.72 support=2.55 resistance=3.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=28.05 liquidity=10025966.0 spike=0.3
- OFH.CA: score=17.86 buy_ready=False sector_rank=11 price=1.08 support=0.86 resistance=1.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=69.62 liquidity=43485504.0 spike=0.39
- OIH.CA: score=23.4 buy_ready=False sector_rank=4 price=2.11 support=1.75 resistance=2.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=74.14 liquidity=37995904.0 spike=0.28
- OLFI.CA: score=7.74 buy_ready=False sector_rank=17 price=22.4 support=22.07 resistance=25.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=34.56 liquidity=8399298.0 spike=0.18
- ORAS.CA: score=4.6 buy_ready=False sector_rank=15 price=860.02 support=850.05 resistance=868.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=113661568.0 spike=1.0
- ORHD.CA: score=20.11 buy_ready=False sector_rank=8 price=42.25 support=40.28 resistance=43.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=52.82 liquidity=84221208.0 spike=0.62
- ORWE.CA: score=25.4 buy_ready=False sector_rank=2 price=26.63 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=59.88 liquidity=37894032.0 spike=0.65
- PHAR.CA: score=4.26 buy_ready=False sector_rank=18 price=118.85 support=118.16 resistance=125.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=93863336.0 spike=0.42
- PHDC.CA: score=10.11 buy_ready=False sector_rank=8 price=13.81 support=13.82 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=32.01 liquidity=98769912.0 spike=0.46
- PHTV.CA: score=8.6 buy_ready=False sector_rank=11 price=350.0 support=311.27 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=38.58 liquidity=744288.25 spike=0.36
- POUL.CA: score=21.34 buy_ready=False sector_rank=17 price=39.0 support=36.97 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=65.0 liquidity=14002307.0 spike=0.59
- PRCL.CA: score=14.82 buy_ready=False sector_rank=12 price=32.35 support=30.9 resistance=36.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=42.03 liquidity=20691220.0 spike=0.97
- PRDC.CA: score=10.11 buy_ready=False sector_rank=8 price=7.92 support=8.0 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=24.0 liquidity=16677625.0 spike=0.25
- PRMH.CA: score=6.89 buy_ready=False sector_rank=11 price=2.57 support=2.28 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=67.07 liquidity=2038514.88 spike=0.16
- RACC.CA: score=14.98 buy_ready=False sector_rank=11 price=9.6 support=9.4 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=43.26 liquidity=8122777.0 spike=0.34
- RAKT.CA: score=6.77 buy_ready=False sector_rank=11 price=22.15 support=21.4 resistance=23.09 source=Yahoo Finance as_of=2026-09-12T21:00:00+00:00 freshness=FRESH RSI=47.52 liquidity=334376.39 spike=1.29
- RAYA.CA: score=15.5 buy_ready=False sector_rank=21 price=7.09 support=6.95 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=51.72 liquidity=27319724.0 spike=0.43
- RMDA.CA: score=17.26 buy_ready=False sector_rank=18 price=6.1 support=5.77 resistance=6.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=46.09 liquidity=23000618.0 spike=0.36
- ROTO.CA: score=-1.29 buy_ready=False sector_rank=11 price=35.06 support=35.02 resistance=42.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3856334.25 spike=0.26
- RREI.CA: score=17.86 buy_ready=False sector_rank=11 price=4.33 support=4.24 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=43.04 liquidity=11598002.0 spike=0.39
- RTVC.CA: score=9.73 buy_ready=False sector_rank=11 price=3.97 support=3.76 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=49.23 liquidity=1871102.75 spike=0.25
- RUBX.CA: score=15.17 buy_ready=False sector_rank=11 price=12.74 support=12.36 resistance=13.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=56.52 liquidity=8316766.0 spike=0.4
- SAUD.CA: score=14.4 buy_ready=False sector_rank=10 price=22.85 support=22.85 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=40.77 liquidity=6364695.5 spike=0.38
- SCEM.CA: score=17.82 buy_ready=False sector_rank=12 price=95.09 support=94.0 resistance=112.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=44237196.0 spike=0.23
- SCFM.CA: score=6.84 buy_ready=False sector_rank=11 price=271.84 support=270.55 resistance=305.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=39.15 liquidity=1986804.75 spike=0.18
- SCTS.CA: score=19.5 buy_ready=False sector_rank=3 price=602.47 support=566.66 resistance=660.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=44.8 liquidity=10083236.0 spike=2.05
- SDTI.CA: score=19.86 buy_ready=False sector_rank=11 price=72.0 support=67.0 resistance=76.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=58.09 liquidity=13437211.0 spike=0.67
- SEIG.CA: score=5.48 buy_ready=False sector_rank=11 price=250.0 support=250.02 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=38.16 liquidity=621446.94 spike=0.28
- SIPC.CA: score=19.86 buy_ready=False sector_rank=11 price=5.96 support=4.1 resistance=6.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=65.96 liquidity=57234880.0 spike=0.97
- SKPC.CA: score=20.7 buy_ready=False sector_rank=5 price=17.62 support=16.6 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=61.85 liquidity=74050704.0 spike=0.53
- SMFR.CA: score=10.27 buy_ready=False sector_rank=11 price=240.0 support=246.0 resistance=276.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=35.05 liquidity=5413525.5 spike=0.43
- SNFC.CA: score=15.86 buy_ready=False sector_rank=11 price=10.6 support=10.26 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=45.77 liquidity=12777677.0 spike=0.96
- SPIN.CA: score=16.61 buy_ready=False sector_rank=2 price=18.15 support=16.5 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=39.82 liquidity=5208666.5 spike=0.14
- SPMD.CA: score=9.86 buy_ready=False sector_rank=11 price=0.52 support=0.43 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=153241456.0 spike=13.9
- SUGR.CA: score=4.34 buy_ready=False sector_rank=17 price=60.3 support=60.0 resistance=63.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15972259.0 spike=0.22
- SVCE.CA: score=19.86 buy_ready=False sector_rank=11 price=11.9 support=10.28 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=72.07 liquidity=136406160.0 spike=0.75
- SWDY.CA: score=20.59 buy_ready=False sector_rank=6 price=126.52 support=107.53 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=60.9 liquidity=41985148.0 spike=0.44
- TALM.CA: score=12.4 buy_ready=False sector_rank=3 price=22.67 support=19.45 resistance=22.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=324727456.0 spike=12.04
- TMGH.CA: score=17.11 buy_ready=False sector_rank=8 price=96.0 support=94.9 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=50.36 liquidity=170155568.0 spike=0.63
- TRTO.CA: score=9.88 buy_ready=False sector_rank=11 price=0.07 support=0.04 resistance=0.08 source=Yahoo Finance as_of=2026-09-12T21:00:00+00:00 freshness=FRESH RSI=67.92 liquidity=27071.03 spike=0.84
- UEFM.CA: score=14.12 buy_ready=False sector_rank=11 price=534.54 support=440.66 resistance=570.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=44.04 liquidity=5728904.0 spike=1.27
- UEGC.CA: score=9.37 buy_ready=False sector_rank=11 price=1.69 support=1.66 resistance=2.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=18.92 liquidity=9515510.0 spike=0.21
- UNIP.CA: score=16.86 buy_ready=False sector_rank=11 price=0.37 support=0.35 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=50.57 liquidity=10002253.0 spike=0.27
- UNIT.CA: score=10.11 buy_ready=False sector_rank=8 price=19.97 support=18.25 resistance=21.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=112301504.0 spike=18.8
- WCDF.CA: score=10.5 buy_ready=False sector_rank=11 price=712.91 support=630.0 resistance=729.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=82.65 liquidity=1646782.25 spike=0.43
- WKOL.CA: score=12.37 buy_ready=False sector_rank=11 price=343.32 support=323.02 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=45.78 liquidity=4509830.0 spike=0.22
- ZEOT.CA: score=11.23 buy_ready=False sector_rank=11 price=13.32 support=13.25 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=42.48 liquidity=3378337.25 spike=0.26
- ZMID.CA: score=20.11 buy_ready=False sector_rank=8 price=9.35 support=7.39 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=71.16 liquidity=46402780.0 spike=0.18

## Backtesting Lite
- CIRA.CA: 180d return=117.93%, max drawdown=-16.44%, MA20>MA50 days last20=20, as_of=2026-09-12T21:00:00+00:00
- ETEL.CA: 180d return=101.4%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-09-12T21:00:00+00:00
- ACGC.CA: 180d return=81.51%, max drawdown=-15.74%, MA20>MA50 days last20=20, as_of=2026-09-12T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CIRA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Investment and Real Estate Development summary=CIRA Education take over 51% of L’École Française Hurghada; CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion; CIRA Education launches Middle East’s 1st initiative for care economy
  - CIRA Education take over 51% of L’École Française Hurghada: https://english.mubasher.info/news/4488666/CIRA-Education-take-over-51-of-L-%C3%89cole-Fran%C3%A7aise-Hurghada/
  - CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion: https://english.mubasher.info/news/4393636/CIRA-s-majority-shareholder-acquires-37-5-additional-equity-backs-regional-expansion/
  - CIRA Education launches Middle East’s 1st initiative for care economy: https://english.mubasher.info/news/4391766/CIRA-Education-launches-Middle-East-s-1st-initiative-for-care-economy/
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- ACGC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Cotton Ginning summary=Arab Cotton Ginning’s stock nears significant resistance level; Arab Cotton Ginning’s standalone profit grows 142% YoY in 9M-23/24; Arab Cotton Ginning’s consolidated profit leaps 371% YoY in H1-23/24
  - Arab Cotton Ginning’s stock nears significant resistance level: https://english.mubasher.info/news/4549011/Arab-Cotton-Ginning-s-stock-nears-significant-resistance-level/
  - Arab Cotton Ginning’s standalone profit grows 142% YoY in 9M-23/24: https://english.mubasher.info/news/4302757/Arab-Cotton-Ginning-s-standalone-profit-grows-142-YoY-in-9M-23-24/
  - Arab Cotton Ginning’s consolidated profit leaps 371% YoY in H1-23/24: https://english.mubasher.info/news/4279332/Arab-Cotton-Ginning-s-consolidated-profit-leaps-371-YoY-in-H1-23-24/
- KABO.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Nasr Clothing and Textiles summary=KABO posts EGP 17m in Q1-25/26 unaudited consolidated net profits; KABO sells over 1.9m shares in Spinalex for EGP 20m; KABO unveils international agreements, expansion plan including export lines
  - KABO posts EGP 17m in Q1-25/26 unaudited consolidated net profits: https://english.mubasher.info/news/4600162/KABO-posts-EGP-17m-in-Q1-25-26-unaudited-consolidated-net-profits/
  - KABO sells over 1.9m shares in Spinalex for EGP 20m: https://english.mubasher.info/news/4543747/KABO-sells-over-1-9m-shares-in-Spinalex-for-EGP-20m/
  - KABO unveils international agreements, expansion plan including export lines: https://english.mubasher.info/news/4533185/KABO-unveils-international-agreements-expansion-plan-including-export-lines/
- ORWE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=621 sources=3 expected=Oriental Weavers summary=Oriental Weavers to disburse EGP 1.5/shr dividends for 2025; Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025; Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25
  - Oriental Weavers to disburse EGP 1.5/shr dividends for 2025: https://english.mubasher.info/news/4590236/Oriental-Weavers-to-disburse-EGP-1-5-shr-dividends-for-2025/
  - Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025: https://english.mubasher.info/news/4562972/Oriental-Weavers-consolidated-profits-cross-EGP-2-2bn-in-2025/
  - Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25: https://english.mubasher.info/news/4487417/Oriental-Weavers-generates-EGP-12-5bn-consolidated-sales-in-H1-25/
- OIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Investment Holding summary=Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- HELI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Heliopolis Housing summary=Evidence rejected for HELI.CA: source text did not clearly match HELI.CA / Heliopolis Housing.
- MASR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=621 sources=3 expected=Madinet Masr For Housing and Development summary=Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval; Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended; Madinet Masr to distribute treasury stocks in first-ever move
  - Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval: https://english.mubasher.info/news/4601386/Madinet-Masr-to-pay-out-EGP-0-15-shr-for-2025-upon-equityholders-approval/
  - Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended: https://english.mubasher.info/news/4578449/Madinet-Masr-logs-24-higher-consolidated-profits-in-2025-dividends-recommended/
  - Madinet Masr to distribute treasury stocks in first-ever move: https://english.mubasher.info/news/4577724/Madinet-Masr-to-distribute-treasury-stocks-in-first-ever-move/

## Warnings
- Evidence for CIRA.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for ACGC.CA matches the company but no source/report date was detected.
- Evidence for KABO.CA matches the company but no source/report date was detected.
- Evidence for ORWE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence rejected for HELI.CA: source text did not clearly match HELI.CA / Heliopolis Housing.
- Evidence for MASR.CA matches the company but appears old; latest detected date is 2025-01-01.
