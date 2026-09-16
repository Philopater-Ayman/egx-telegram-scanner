# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-09-16T11:29:29.011442+00:00
Generated Cairo: 2026-09-16 14:29
Run timing: target 09:15 Cairo | generated Cairo 2026-09-16 14:29 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-09-16 14:26

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 177/189
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, September 16
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 26.32% / above MA50 57.89%
- EGX70 regime: BEARISH / above MA20 33.33% / above MA50 56.41%
- Sector breadth: 19.05%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=730318208.0 spike=0.84 score=19.4
- SPMD.CA: liquidity=384009024.0 spike=8.15 score=9.47
- COMI.CA: liquidity=345019648.0 spike=0.63 score=9.6
- DTPP.CA: liquidity=299952352.0 spike=5.84 score=9.47
- AMES.CA: liquidity=261136672.0 spike=1.05 score=8.57

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: ...
- Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.
- Defensive regime (EGX30/EGX70 bearish, low sector breadth) blocks new buys, so all tickets stay in HOLD.
- Top tickets such as MPCO.CA, UNIT.CA and ETEL.CA show high rank scores and solid liquidity, with BULLISH_WATCH outlook but mixed RSI and resistance proximity.
- Leading sectors (Telecom, Agriculture & Food Production, Investment Holding) give relative strength, yet extended momentum, overheated RSI or cooling liquidity add uncertainty for the next 1‑3 days.
- Liquidity spikes and support/resistance distances suggest limited upside; risk notes warn of extended momentum or cooling liquidity, reinforcing the defensive stance.

## Top Liquidity Spikes
- BINV.CA: spike=10.11 liquidity=113139328.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SPMD.CA: spike=8.15 liquidity=384009024.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SEIG.CA: spike=7.16 liquidity=10943656.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DTPP.CA: spike=5.84 liquidity=299952352.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RUBX.CA: spike=3.28 liquidity=66083632.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=11.51 5d=4.73% 20d=8.8% aboveMA50=100.0%
- #2 Agriculture & Food Production: score=11.48 5d=11.18% 20d=15.15% aboveMA50=50.0%
- #3 Investment Holding: score=10.9 5d=3.37% 20d=21.47% aboveMA50=66.67%
- #4 Education: score=7.82 5d=3.67% 20d=6.73% aboveMA50=66.67%
- #5 Energy & Petrochemicals: score=3.37 5d=-2.48% 20d=0.38% aboveMA50=75.0%
- #6 Basic Resources & Chemicals: score=2.69 5d=-3.77% 20d=2.63% aboveMA50=60.0%
- #7 Real Estate: score=2.44 5d=-2.12% 20d=-0.58% aboveMA50=46.15%
- #8 Tourism & Leisure: score=2.1 5d=-0.67% 20d=-5.13% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- UNIT.CA: BULLISH_WATCH score=95.44 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- MPCO.CA: BULLISH_WATCH score=91 liquidity=TRADEABLE sector=LEADING risk=momentum is extended; far above support
- SKPC.CA: BULLISH_WATCH score=78.69 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ORHD.CA: BULLISH_WATCH score=77.44 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- AALR.CA: BULLISH_WATCH score=77.17 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- TALM.CA: BULLISH_WATCH score=76.82 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=overheated RSI; far above support
- ETEL.CA: BULLISH_WATCH score=75 liquidity=TRADEABLE sector=LEADING risk=overheated RSI
- CIRA.CA: BULLISH_WATCH score=73.82 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended; far above support
- KABO.CA: BULLISH_WATCH score=72.53 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- MEPA.CA: BULLISH_WATCH score=72.17 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=19.47 buy_ready=False sector_rank=12 price=317.63 support=295.0 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=27832776.0 spike=0.85
- ABUK.CA: score=20.08 buy_ready=False sector_rank=6 price=88.85 support=75.01 resistance=94.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=65.2 liquidity=60719520.0 spike=0.39
- ACAMD.CA: score=16.47 buy_ready=False sector_rank=12 price=2.06 support=1.95 resistance=2.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=46.94 liquidity=37350596.0 spike=0.65
- ACGC.CA: score=17.61 buy_ready=False sector_rank=9 price=14.09 support=12.04 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=50.19 liquidity=11952935.0 spike=0.27
- ADCI.CA: score=4.79 buy_ready=False sector_rank=12 price=280.53 support=267.66 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=31.74 liquidity=2321363.0 spike=0.34
- ADIB.CA: score=17.6 buy_ready=False sector_rank=10 price=52.38 support=50.51 resistance=55.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=40.97 liquidity=54008428.0 spike=0.81
- ADPC.CA: score=12.26 buy_ready=False sector_rank=12 price=3.82 support=3.81 resistance=4.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=45.28 liquidity=7787574.5 spike=0.33
- AFDI.CA: score=11.76 buy_ready=False sector_rank=12 price=55.26 support=51.6 resistance=68.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=31.12 liquidity=9289100.0 spike=0.36
- AFMC.CA: score=9.47 buy_ready=False sector_rank=12 price=159.2 support=157.0 resistance=267.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=20.95 liquidity=17001292.0 spike=0.29
- AJWA.CA: score=6.15 buy_ready=False sector_rank=12 price=179.9 support=175.15 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=46.93 liquidity=1678457.25 spike=0.03
- ALCN.CA: score=16.84 buy_ready=False sector_rank=18 price=30.89 support=30.03 resistance=34.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=51.9 liquidity=9978374.0 spike=0.34
- ALUM.CA: score=4.81 buy_ready=False sector_rank=12 price=25.85 support=25.0 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=22.87 liquidity=2344665.25 spike=0.15
- AMER.CA: score=17.98 buy_ready=False sector_rank=7 price=5.43 support=4.8 resistance=6.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=46.3 liquidity=50569724.0 spike=0.79
- AMES.CA: score=8.57 buy_ready=False sector_rank=12 price=54.14 support=51.22 resistance=173.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=0.55 liquidity=261136672.0 spike=1.05
- AMIA.CA: score=7.23 buy_ready=False sector_rank=12 price=17.5 support=15.3 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=31.84 liquidity=4760305.5 spike=0.07
- AMOC.CA: score=18.35 buy_ready=False sector_rank=5 price=13.45 support=10.65 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=72.71 liquidity=103806576.0 spike=0.55
- APSW.CA: score=3.96 buy_ready=False sector_rank=12 price=8.42 support=8.37 resistance=9.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=39.78 liquidity=487859.44 spike=0.41
- ARAB.CA: score=14.98 buy_ready=False sector_rank=7 price=0.25 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=50.88 liquidity=57474532.0 spike=0.58
- ARCC.CA: score=16.57 buy_ready=False sector_rank=21 price=73.18 support=71.5 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=36.74 liquidity=12597166.0 spike=0.27
- AREH.CA: score=11.92 buy_ready=False sector_rank=12 price=1.42 support=1.39 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=45.16 liquidity=7453883.5 spike=0.43
- ARVA.CA: score=4.47 buy_ready=False sector_rank=12 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=4.76 buy_ready=False sector_rank=12 price=60.22 support=60.15 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=34.25 liquidity=5292450.0 spike=0.25
- ASPI.CA: score=12.47 buy_ready=False sector_rank=12 price=0.44 support=0.41 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=32.79 liquidity=40844292.0 spike=0.74
- ATLC.CA: score=15.11 buy_ready=False sector_rank=16 price=6.97 support=5.2 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=68.74 liquidity=6055549.5 spike=0.21
- ATQA.CA: score=18.08 buy_ready=False sector_rank=6 price=12.6 support=10.8 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=67.63 liquidity=62212928.0 spike=0.57
- AXPH.CA: score=9.86 buy_ready=False sector_rank=12 price=1708.35 support=1345.01 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=77.32 liquidity=5395568.5 spike=0.44
- BINV.CA: score=12.4 buy_ready=False sector_rank=3 price=62.37 support=50.0 resistance=62.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=113139328.0 spike=10.11
- BIOC.CA: score=9.47 buy_ready=False sector_rank=12 price=283.47 support=272.01 resistance=535.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=9.64 liquidity=96853568.0 spike=0.74
- BTFH.CA: score=13.05 buy_ready=False sector_rank=16 price=2.93 support=2.87 resistance=3.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=41.94 liquidity=43462232.0 spike=0.43
- CAED.CA: score=12.47 buy_ready=False sector_rank=12 price=127.62 support=123.56 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=29.63 liquidity=11782536.0 spike=0.28
- CANA.CA: score=9.18 buy_ready=False sector_rank=10 price=41.75 support=41.0 resistance=44.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=1584656.75 spike=0.11
- CCAP.CA: score=19.4 buy_ready=False sector_rank=3 price=6.88 support=5.42 resistance=6.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=75.86 liquidity=730318208.0 spike=0.84
- CCRS.CA: score=17.47 buy_ready=False sector_rank=12 price=2.58 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=38.32 liquidity=11099002.0 spike=0.21
- CEFM.CA: score=9.35 buy_ready=False sector_rank=12 price=145.19 support=135.9 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=46.29 liquidity=1883946.63 spike=0.13
- CERA.CA: score=22.31 buy_ready=False sector_rank=12 price=1.46 support=1.22 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=55.75 liquidity=130226920.0 spike=1.42
- CFGH.CA: score=5.47 buy_ready=False sector_rank=12 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=4096.69 spike=0.19
- CICH.CA: score=9.56 buy_ready=False sector_rank=16 price=12.47 support=12.0 resistance=13.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=57.61 liquidity=505005.88 spike=0.1
- CIEB.CA: score=13.78 buy_ready=False sector_rank=10 price=24.65 support=24.01 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=46.47 liquidity=6181776.0 spike=0.44
- CIRA.CA: score=23.4 buy_ready=False sector_rank=4 price=39.0 support=32.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=26145562.0 spike=0.67
- CLHO.CA: score=9.28 buy_ready=False sector_rank=15 price=16.3 support=15.81 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=29.36 liquidity=23183206.0 spike=0.3
- CNFN.CA: score=0.27 buy_ready=False sector_rank=16 price=4.6 support=4.46 resistance=4.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=31.34 liquidity=2215632.25 spike=0.18
- COMI.CA: score=9.6 buy_ready=False sector_rank=10 price=131.78 support=131.56 resistance=142.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=30.05 liquidity=345019648.0 spike=0.63
- COPR.CA: score=12.47 buy_ready=False sector_rank=12 price=0.5 support=0.44 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=29.08 liquidity=38126268.0 spike=0.42
- COSG.CA: score=17.07 buy_ready=False sector_rank=12 price=1.8 support=1.74 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=9600192.0 spike=0.22
- CPCI.CA: score=9.33 buy_ready=False sector_rank=12 price=532.22 support=525.01 resistance=569.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=36.59 liquidity=1862902.88 spike=0.43
- CSAG.CA: score=15.11 buy_ready=False sector_rank=18 price=37.36 support=37.04 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=37.06 liquidity=8254499.0 spike=0.5
- DAPH.CA: score=17.47 buy_ready=False sector_rank=12 price=121.49 support=108.11 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=58.73 liquidity=11442337.0 spike=0.19
- DEIN.CA: score=7.47 buy_ready=False sector_rank=12 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=5.53 buy_ready=False sector_rank=20 price=26.9 support=26.51 resistance=29.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=35.97 liquidity=1870629.75 spike=0.31
- DSCW.CA: score=11.79 buy_ready=False sector_rank=12 price=1.82 support=1.8 resistance=2.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=8320777.0 spike=0.19
- DTPP.CA: score=9.47 buy_ready=False sector_rank=12 price=354.2 support=325.25 resistance=379.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=299952352.0 spike=5.84
- EALR.CA: score=12.79 buy_ready=False sector_rank=12 price=385.19 support=340.0 resistance=456.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=30565474.0 spike=1.16
- EASB.CA: score=21.51 buy_ready=False sector_rank=12 price=8.18 support=7.16 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=17247734.0 spike=1.02
- EAST.CA: score=8.64 buy_ready=False sector_rank=20 price=32.75 support=33.04 resistance=36.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=30.25 liquidity=101425576.0 spike=1.49
- EBSC.CA: score=9.52 buy_ready=False sector_rank=12 price=2.01 support=1.88 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=2051651.75 spike=0.14
- ECAP.CA: score=6.65 buy_ready=False sector_rank=12 price=32.09 support=31.16 resistance=39.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=39.53 liquidity=2183873.0 spike=0.18
- EDFM.CA: score=10.01 buy_ready=False sector_rank=12 price=413.37 support=394.0 resistance=432.0 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=56.63 liquidity=543168.17 spike=0.33
- EEII.CA: score=5.53 buy_ready=False sector_rank=12 price=2.18 support=2.15 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=35.13 liquidity=2063176.13 spike=0.09
- EFIC.CA: score=14.08 buy_ready=False sector_rank=6 price=194.86 support=192.75 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=48140140.0 spike=0.51
- EFID.CA: score=16.66 buy_ready=False sector_rank=20 price=30.76 support=29.71 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=42.82 liquidity=53085448.0 spike=0.91
- EFIH.CA: score=17.42 buy_ready=False sector_rank=13 price=23.6 support=22.16 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=48.53 liquidity=46615668.0 spike=0.7
- EGAL.CA: score=18.08 buy_ready=False sector_rank=6 price=359.52 support=321.01 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=55.66 liquidity=32252386.0 spike=0.28
- EGAS.CA: score=10.8 buy_ready=False sector_rank=5 price=56.23 support=55.0 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=38.85 liquidity=2456021.5 spike=0.27
- EGBE.CA: score=2.62 buy_ready=False sector_rank=10 price=0.5 support=0.49 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=19569.75 spike=0.14
- EGCH.CA: score=18.08 buy_ready=False sector_rank=6 price=13.92 support=13.3 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=59.09 liquidity=31695078.0 spike=0.27
- EGSA.CA: score=11.83 buy_ready=False sector_rank=1 price=9.0 support=8.67 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=78.18 liquidity=10410.0 spike=1.21
- EGTS.CA: score=14.98 buy_ready=False sector_rank=7 price=17.0 support=16.17 resistance=18.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=46.26 liquidity=14439505.0 spike=0.58
- EHDR.CA: score=14.49 buy_ready=False sector_rank=12 price=2.74 support=2.79 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=44.0 liquidity=22063972.0 spike=1.01
- EKHO.CA: score=6.35 buy_ready=False sector_rank=5 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=13.42 buy_ready=False sector_rank=17 price=1.94 support=1.98 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=38.24 liquidity=88366424.0 spike=1.25
- ELKA.CA: score=14.47 buy_ready=False sector_rank=12 price=1.75 support=1.7 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=50.88 liquidity=12749231.0 spike=0.29
- ELNA.CA: score=-1.24 buy_ready=False sector_rank=12 price=35.74 support=33.96 resistance=38.99 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=22.51 liquidity=288922.17 spike=0.62
- ELSH.CA: score=14.47 buy_ready=False sector_rank=12 price=12.72 support=12.71 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=45.15 liquidity=13423727.0 spike=0.35
- ELWA.CA: score=6.07 buy_ready=False sector_rank=12 price=1.7 support=1.62 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=1597306.88 spike=0.65
- EMFD.CA: score=19.98 buy_ready=False sector_rank=7 price=14.19 support=11.51 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=73.22 liquidity=122405952.0 spike=0.76
- ENGC.CA: score=1.54 buy_ready=False sector_rank=12 price=41.3 support=41.0 resistance=51.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=31.07 liquidity=2070823.75 spike=0.13
- EOSB.CA: score=9.49 buy_ready=False sector_rank=12 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=17259.01 spike=0.25
- EPCO.CA: score=17.47 buy_ready=False sector_rank=12 price=11.21 support=10.8 resistance=12.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=58.03 liquidity=10188287.0 spike=0.5
- EPPK.CA: score=-5.11 buy_ready=False sector_rank=12 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=23.94 buy_ready=False sector_rank=1 price=131.54 support=112.1 resistance=135.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=88.67 liquidity=242744560.0 spike=1.27
- ETRS.CA: score=16.3 buy_ready=False sector_rank=12 price=10.88 support=10.66 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=50.56 liquidity=8834612.0 spike=0.41
- EXPA.CA: score=17.6 buy_ready=False sector_rank=10 price=20.8 support=19.8 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=60.89 liquidity=11319207.0 spike=0.32
- FAIT.CA: score=11.09 buy_ready=False sector_rank=10 price=45.68 support=39.58 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=67.11 liquidity=1491310.63 spike=0.18
- FAITA.CA: score=4.62 buy_ready=False sector_rank=10 price=0.99 support=0.98 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=47.14 liquidity=15605.02 spike=0.3
- FERC.CA: score=7.55 buy_ready=False sector_rank=6 price=77.93 support=76.7 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=48.11 liquidity=3472553.5 spike=0.18
- FWRY.CA: score=14.42 buy_ready=False sector_rank=13 price=18.83 support=18.66 resistance=19.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=74360320.0 spike=0.55
- GBCO.CA: score=19.45 buy_ready=False sector_rank=14 price=30.55 support=27.51 resistance=31.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=62.86 liquidity=80534920.0 spike=1.55
- GDWA.CA: score=13.47 buy_ready=False sector_rank=12 price=0.77 support=0.76 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=49.68 liquidity=21569762.0 spike=0.53
- GGCC.CA: score=17.47 buy_ready=False sector_rank=12 price=0.88 support=0.83 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=48.14 liquidity=25995270.0 spike=0.63
- GIHD.CA: score=19.47 buy_ready=False sector_rank=12 price=72.72 support=58.01 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=73.32 liquidity=11306761.0 spike=0.38
- GMCI.CA: score=0.71 buy_ready=False sector_rank=12 price=1.75 support=1.75 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=24.14 liquidity=839412.19 spike=1.7
- GRCA.CA: score=4.63 buy_ready=False sector_rank=12 price=43.52 support=40.0 resistance=46.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=85200304.0 spike=1.08
- GSSC.CA: score=12.15 buy_ready=False sector_rank=12 price=292.69 support=278.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=46.66 liquidity=2684278.75 spike=0.21
- GTWL.CA: score=17.47 buy_ready=False sector_rank=12 price=236.69 support=165.0 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=66.99 liquidity=56765668.0 spike=0.2
- HDBK.CA: score=4.64 buy_ready=False sector_rank=10 price=115.0 support=109.98 resistance=115.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=58725576.0 spike=1.02
- HELI.CA: score=20.74 buy_ready=False sector_rank=7 price=8.19 support=7.34 resistance=8.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=69.7 liquidity=209058512.0 spike=1.38
- HRHO.CA: score=13.05 buy_ready=False sector_rank=16 price=25.19 support=25.21 resistance=26.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=42.59 liquidity=33116270.0 spike=0.33
- ICID.CA: score=15.05 buy_ready=False sector_rank=12 price=18.21 support=14.5 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=62.93 liquidity=5585851.5 spike=0.25
- IDRE.CA: score=16.8 buy_ready=False sector_rank=12 price=53.73 support=51.0 resistance=57.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=58.73 liquidity=9336583.0 spike=0.91
- IFAP.CA: score=15.86 buy_ready=False sector_rank=2 price=20.3 support=20.05 resistance=22.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=40.83 liquidity=7462384.0 spike=0.31
- INFI.CA: score=10.33 buy_ready=False sector_rank=12 price=133.26 support=130.15 resistance=174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=16.76 liquidity=7860791.5 spike=0.21
- IRON.CA: score=9.54 buy_ready=False sector_rank=6 price=27.03 support=27.08 resistance=33.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=5.54 liquidity=17532944.0 spike=1.23
- ISMA.CA: score=5.85 buy_ready=False sector_rank=12 price=30.09 support=28.05 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=25.48 liquidity=6386248.5 spike=0.24
- ISMQ.CA: score=13.17 buy_ready=False sector_rank=6 price=8.81 support=8.68 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=36.59 liquidity=8093789.5 spike=0.27
- ISPH.CA: score=10.4 buy_ready=False sector_rank=15 price=12.28 support=11.9 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=33.74 liquidity=102687992.0 spike=1.56
- JUFO.CA: score=9.31 buy_ready=False sector_rank=20 price=27.08 support=26.45 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=51.33 liquidity=4645894.0 spike=0.21
- KABO.CA: score=19.61 buy_ready=False sector_rank=9 price=9.36 support=8.82 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=60.58 liquidity=38023056.0 spike=0.71
- KWIN.CA: score=9.47 buy_ready=False sector_rank=12 price=87.44 support=84.5 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=26.96 liquidity=15394466.0 spike=0.23
- KZPC.CA: score=19.47 buy_ready=False sector_rank=12 price=14.45 support=12.14 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=64.52 liquidity=13301167.0 spike=0.21
- LCSW.CA: score=11.38 buy_ready=False sector_rank=21 price=32.66 support=32.83 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=38.59 liquidity=7807237.0 spike=0.28
- LUTS.CA: score=17.47 buy_ready=False sector_rank=12 price=0.98 support=0.79 resistance=1.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=47.19 liquidity=110934264.0 spike=0.4
- MAAL.CA: score=5.88 buy_ready=False sector_rank=12 price=8.54 support=8.18 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=39.87 liquidity=1416988.63 spike=0.13
- MASR.CA: score=18.47 buy_ready=False sector_rank=12 price=7.89 support=7.49 resistance=8.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=56.3 liquidity=45158836.0 spike=0.5
- MBSC.CA: score=16.57 buy_ready=False sector_rank=21 price=381.66 support=355.04 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=48.68 liquidity=43897420.0 spike=0.73
- MCQE.CA: score=11.57 buy_ready=False sector_rank=21 price=222.93 support=212.01 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=31.0 liquidity=25132378.0 spike=0.65
- MCRO.CA: score=16.59 buy_ready=False sector_rank=12 price=1.71 support=1.44 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=77.5 liquidity=123789816.0 spike=1.06
- MENA.CA: score=0.83 buy_ready=False sector_rank=7 price=6.65 support=6.58 resistance=7.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=29.21 liquidity=855767.31 spike=0.3
- MEPA.CA: score=19.58 buy_ready=False sector_rank=12 price=1.93 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=58.23 liquidity=8109906.5 spike=0.23
- MFPC.CA: score=17.3 buy_ready=False sector_rank=6 price=48.64 support=38.93 resistance=48.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=80.29 liquidity=140849696.0 spike=1.11
- MFSC.CA: score=5.87 buy_ready=False sector_rank=12 price=48.75 support=48.6 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=46.13 liquidity=1404946.75 spike=0.28
- MHOT.CA: score=9.67 buy_ready=False sector_rank=8 price=17.77 support=17.72 resistance=19.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=50.89 liquidity=2830224.75 spike=0.26
- MICH.CA: score=12.24 buy_ready=False sector_rank=12 price=48.7 support=47.2 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=47.97 liquidity=4773388.5 spike=0.19
- MILS.CA: score=8.21 buy_ready=False sector_rank=12 price=200.0 support=192.22 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=21.55 liquidity=5738335.5 spike=0.11
- MIPH.CA: score=9.28 buy_ready=False sector_rank=15 price=809.0 support=700.2 resistance=820.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=75.41 liquidity=3000249.25 spike=0.73
- MOED.CA: score=16.47 buy_ready=False sector_rank=12 price=0.79 support=0.69 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=55.04 liquidity=29196154.0 spike=0.24
- MOIL.CA: score=10.44 buy_ready=False sector_rank=5 price=0.68 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=47.14 liquidity=93051.96 spike=0.44
- MOIN.CA: score=15.48 buy_ready=False sector_rank=12 price=36.43 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=56.28 liquidity=6008944.5 spike=0.2
- MOSC.CA: score=4.37 buy_ready=False sector_rank=12 price=309.08 support=305.0 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=24.31 liquidity=1903488.75 spike=0.22
- MPCI.CA: score=19.47 buy_ready=False sector_rank=12 price=413.09 support=345.0 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=51.36 liquidity=110536112.0 spike=0.7
- MPCO.CA: score=25.4 buy_ready=False sector_rank=2 price=2.71 support=2.07 resistance=2.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=68.67 liquidity=153178304.0 spike=0.99
- MPRC.CA: score=14.47 buy_ready=False sector_rank=12 price=38.6 support=38.31 resistance=46.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=36.12 liquidity=10310104.0 spike=0.26
- MTIE.CA: score=14.35 buy_ready=False sector_rank=14 price=8.41 support=8.1 resistance=9.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=39.55 liquidity=13263730.0 spike=0.3
- NAHO.CA: score=-5.5 buy_ready=False sector_rank=12 price=0.14 support=0.14 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29300.51 spike=0.28
- NCCW.CA: score=18.73 buy_ready=False sector_rank=12 price=8.28 support=5.59 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=81.34 liquidity=66611404.0 spike=1.13
- NEDA.CA: score=4.8 buy_ready=False sector_rank=12 price=2.72 support=2.7 resistance=2.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=51.35 liquidity=334828.63 spike=0.35
- NHPS.CA: score=3.14 buy_ready=False sector_rank=12 price=76.39 support=75.31 resistance=98.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=4.03 liquidity=3676449.0 spike=0.16
- NINH.CA: score=9.47 buy_ready=False sector_rank=12 price=20.78 support=20.5 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=15.11 liquidity=15400599.0 spike=0.5
- NIPH.CA: score=12.28 buy_ready=False sector_rank=15 price=318.06 support=301.0 resistance=414.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=19.41 liquidity=134865312.0 spike=0.65
- OBRI.CA: score=8.61 buy_ready=False sector_rank=12 price=30.53 support=30.1 resistance=34.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=39.46 liquidity=5143368.0 spike=0.24
- OCDI.CA: score=14.98 buy_ready=False sector_rank=7 price=29.6 support=29.25 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=35.4 liquidity=39708160.0 spike=0.47
- OCPH.CA: score=6.53 buy_ready=False sector_rank=12 price=241.94 support=210.0 resistance=277.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=27.82 liquidity=6062778.5 spike=0.64
- ODIN.CA: score=3.64 buy_ready=False sector_rank=12 price=2.74 support=2.55 resistance=3.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=22.22 liquidity=4172264.25 spike=0.14
- OFH.CA: score=19.47 buy_ready=False sector_rank=12 price=1.04 support=0.88 resistance=1.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=56.28 liquidity=45500336.0 spike=0.41
- OIH.CA: score=20.4 buy_ready=False sector_rank=3 price=2.16 support=1.76 resistance=2.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=68.52 liquidity=78073312.0 spike=0.63
- OLFI.CA: score=14.54 buy_ready=False sector_rank=20 price=22.51 support=22.07 resistance=25.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=41.34 liquidity=23215342.0 spike=1.44
- ORAS.CA: score=4.6 buy_ready=False sector_rank=11 price=837.55 support=829.0 resistance=855.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=145929872.0 spike=1.0
- ORHD.CA: score=20.68 buy_ready=False sector_rank=7 price=42.85 support=40.28 resistance=43.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=52.03 liquidity=177328256.0 spike=1.35
- ORWE.CA: score=17.61 buy_ready=False sector_rank=9 price=26.61 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=53.3 liquidity=17246972.0 spike=0.33
- PHAR.CA: score=12.28 buy_ready=False sector_rank=15 price=117.93 support=117.01 resistance=141.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=18.95 liquidity=106898976.0 spike=0.59
- PHDC.CA: score=9.98 buy_ready=False sector_rank=7 price=13.71 support=13.65 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=30.15 liquidity=42265808.0 spike=0.2
- PHTV.CA: score=11.36 buy_ready=False sector_rank=12 price=367.22 support=311.27 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=66.55 liquidity=3007725.0 spike=1.44
- POUL.CA: score=12.66 buy_ready=False sector_rank=20 price=38.01 support=36.97 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=52.85 liquidity=8993380.0 spike=0.37
- PRCL.CA: score=13.57 buy_ready=False sector_rank=21 price=32.31 support=30.9 resistance=36.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=45.12 liquidity=12421069.0 spike=0.58
- PRDC.CA: score=9.98 buy_ready=False sector_rank=7 price=7.95 support=7.77 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=27.27 liquidity=14688176.0 spike=0.22
- PRMH.CA: score=7.87 buy_ready=False sector_rank=12 price=2.53 support=2.28 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=59.15 liquidity=3404652.75 spike=0.31
- RACC.CA: score=7.41 buy_ready=False sector_rank=12 price=9.65 support=9.4 resistance=10.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=47.55 liquidity=2945770.5 spike=0.14
- RAKT.CA: score=11.1 buy_ready=False sector_rank=12 price=22.65 support=21.4 resistance=23.02 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=57.94 liquidity=315582.44 spike=1.16
- RAYA.CA: score=13.8 buy_ready=False sector_rank=19 price=7.06 support=6.95 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=43.09 liquidity=30935714.0 spike=0.54
- RMDA.CA: score=19.28 buy_ready=False sector_rank=15 price=6.15 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=48.15 liquidity=28003514.0 spike=0.48
- ROTO.CA: score=5.73 buy_ready=False sector_rank=12 price=40.47 support=35.02 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=13.49 liquidity=6258394.5 spike=0.52
- RREI.CA: score=12.1 buy_ready=False sector_rank=12 price=4.35 support=4.24 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=53.12 liquidity=4631234.0 spike=0.16
- RTVC.CA: score=0.99 buy_ready=False sector_rank=12 price=3.87 support=3.78 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=34.62 liquidity=1522728.75 spike=0.21
- RUBX.CA: score=9.03 buy_ready=False sector_rank=12 price=13.89 support=12.94 resistance=14.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=66083632.0 spike=3.28
- SAUD.CA: score=9.77 buy_ready=False sector_rank=10 price=23.1 support=22.7 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=46.51 liquidity=2174903.0 spike=0.14
- SCEM.CA: score=16.57 buy_ready=False sector_rank=21 price=94.94 support=94.0 resistance=112.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=49.69 liquidity=46386480.0 spike=0.31
- SCFM.CA: score=5.62 buy_ready=False sector_rank=12 price=270.47 support=265.51 resistance=305.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=36.63 liquidity=1151588.75 spike=0.12
- SCTS.CA: score=1.83 buy_ready=False sector_rank=4 price=604.55 support=566.66 resistance=660.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=27.62 liquidity=425695.44 spike=0.08
- SDTI.CA: score=11.72 buy_ready=False sector_rank=12 price=73.79 support=67.0 resistance=76.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=70.2 liquidity=4253024.0 spike=0.21
- SEIG.CA: score=9.47 buy_ready=False sector_rank=12 price=248.05 support=230.5 resistance=267.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10943656.0 spike=7.16
- SIPC.CA: score=19.47 buy_ready=False sector_rank=12 price=5.95 support=4.1 resistance=6.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=65.96 liquidity=59362100.0 spike=0.95
- SKPC.CA: score=20.08 buy_ready=False sector_rank=6 price=18.21 support=16.8 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=57.96 liquidity=109829872.0 spike=0.77
- SMFR.CA: score=2.0 buy_ready=False sector_rank=12 price=238.73 support=236.1 resistance=276.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=26.97 liquidity=2532856.25 spike=0.25
- SNFC.CA: score=17.4 buy_ready=False sector_rank=12 price=10.95 support=10.26 resistance=11.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=57.39 liquidity=8935420.0 spike=0.66
- SPIN.CA: score=15.03 buy_ready=False sector_rank=9 price=17.21 support=17.21 resistance=20.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=38.77 liquidity=7418660.0 spike=0.25
- SPMD.CA: score=9.47 buy_ready=False sector_rank=12 price=0.48 support=0.48 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=384009024.0 spike=8.15
- SUGR.CA: score=20.66 buy_ready=False sector_rank=20 price=60.67 support=50.0 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=61.6 liquidity=14000979.0 spike=0.2
- SVCE.CA: score=19.47 buy_ready=False sector_rank=12 price=11.64 support=10.28 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=59.71 liquidity=59673076.0 spike=0.36
- SWDY.CA: score=16.92 buy_ready=False sector_rank=17 price=124.44 support=115.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=47.74 liquidity=27061236.0 spike=0.28
- TALM.CA: score=21.6 buy_ready=False sector_rank=4 price=22.46 support=17.11 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=77.24 liquidity=90593168.0 spike=1.6
- TMGH.CA: score=14.98 buy_ready=False sector_rank=7 price=95.09 support=94.9 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=40.6 liquidity=152931440.0 spike=0.57
- TRTO.CA: score=9.48 buy_ready=False sector_rank=12 price=0.07 support=0.04 resistance=0.08 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=67.92 liquidity=10220.28 spike=0.37
- UEFM.CA: score=4.6 buy_ready=False sector_rank=12 price=534.5 support=440.66 resistance=557.0 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=46.56 liquidity=128280.0 spike=0.05
- UEGC.CA: score=5.23 buy_ready=False sector_rank=12 price=1.8 support=1.69 resistance=1.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=62793912.0 spike=1.38
- UNIP.CA: score=14.47 buy_ready=False sector_rank=12 price=0.38 support=0.35 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=53.61 liquidity=13335754.0 spike=0.39
- UNIT.CA: score=24.22 buy_ready=False sector_rank=7 price=19.64 support=18.11 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=55.02 liquidity=27727982.0 spike=2.12
- WCDF.CA: score=13.82 buy_ready=False sector_rank=12 price=751.54 support=630.0 resistance=759.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=88.79 liquidity=4528786.0 spike=1.41
- WKOL.CA: score=19.47 buy_ready=False sector_rank=12 price=355.03 support=332.56 resistance=372.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=53.8 liquidity=17188514.0 spike=0.89
- ZEOT.CA: score=10.38 buy_ready=False sector_rank=12 price=13.04 support=13.04 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=43.46 liquidity=2915825.0 spike=0.37
- ZMID.CA: score=17.98 buy_ready=False sector_rank=7 price=9.18 support=7.39 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=69.21 liquidity=121357016.0 spike=0.49

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
- HELI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Heliopolis Housing summary=Evidence rejected for HELI.CA: source text did not clearly match HELI.CA / Heliopolis Housing.

## Warnings
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for UNIT.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
- Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence rejected for EASB.CA: source text did not clearly match EASB.CA / Egyptian Arabian Company (Themar) for securities Brokerage EAC.
- Evidence rejected for HELI.CA: source text did not clearly match HELI.CA / Heliopolis Housing.
