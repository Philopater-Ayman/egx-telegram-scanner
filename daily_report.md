# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-09-16T10:19:34.749516+00:00
Generated Cairo: 2026-09-16 13:19
Run timing: target 08:45 Cairo | generated Cairo 2026-09-16 13:19 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-16 13:16

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 179/189
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, September 16
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 35.0% / above MA50 50.0%
- EGX70 regime: BEARISH / above MA20 30.77% / above MA50 56.41%
- Sector breadth: 19.05%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=664645504.0 spike=0.76 score=19.4
- SPMD.CA: liquidity=365990528.0 spike=7.77 score=9.42
- COMI.CA: liquidity=288020928.0 spike=0.52 score=9.52
- AMES.CA: liquidity=244664976.0 spike=0.98 score=8.42
- ETEL.CA: liquidity=194518336.0 spike=1.02 score=23.44

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner highlighted several stocks with bullish watch outlooks despite a bearish EGX30/EGX70 regime and defensive risk mode, pointing to liquidity strength and sector leadership while noting extended momentum and uncertainty.
- Selected tickets earned high rank scores and bullish watch tags, backed by liquidity spikes and placement in leading sectors such as Telecommunications, Agriculture & Food Production, and Investment Holding.
- Liquidity regimes show recent accumulation or tradeable conditions, with prices above key support and close to near‑term resistance, suggesting possible short‑term upside if momentum persists.
- Broad‑market breadth is weak in both EGX30 and EGX70, shifting the risk mode to defensive and blocking new buys, which adds uncertainty to any short‑term bullish signals.
- Several names display elevated RSI and momentum readings, indicating overheated conditions that could limit gains or trigger a pullback in the next few days.
- Overall, the scanner presents tentative opportunities but the prevailing bearish regime keeps confidence low and urges caution for any near‑term positioning.

## Top Liquidity Spikes
- SPMD.CA: spike=7.77 liquidity=365990528.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SEIG.CA: spike=6.29 liquidity=9606045.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- BINV.CA: spike=4.19 liquidity=46899440.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DTPP.CA: spike=2.33 liquidity=119899528.0 outlook=BULLISH_WATCH score=75.04 buy_ready=False
- RUBX.CA: spike=2.3 liquidity=46501936.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=11.44 5d=4.73% 20d=8.8% aboveMA50=100.0%
- #2 Agriculture & Food Production: score=11.26 5d=11.18% 20d=15.15% aboveMA50=50.0%
- #3 Investment Holding: score=10.78 5d=3.37% 20d=21.47% aboveMA50=66.67%
- #4 Education: score=7.35 5d=3.67% 20d=6.73% aboveMA50=66.67%
- #5 Basic Resources & Chemicals: score=2.76 5d=-3.77% 20d=2.63% aboveMA50=60.0%
- #6 Energy & Petrochemicals: score=2.51 5d=-2.48% 20d=0.38% aboveMA50=50.0%
- #7 Real Estate: score=2.17 5d=-2.12% 20d=-0.58% aboveMA50=46.15%
- #8 Textiles: score=2.12 5d=-7.11% 20d=0.87% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- UNIT.CA: BULLISH_WATCH score=95.17 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- MPCO.CA: BULLISH_WATCH score=91 liquidity=TRADEABLE sector=LEADING risk=momentum is extended; far above support
- SKPC.CA: BULLISH_WATCH score=78.76 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ORHD.CA: BULLISH_WATCH score=77.17 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- DTPP.CA: BULLISH_WATCH score=75.04 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- ETEL.CA: BULLISH_WATCH score=75 liquidity=TRADEABLE sector=LEADING risk=overheated RSI
- CIRA.CA: BULLISH_WATCH score=73.35 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended; far above support
- KABO.CA: BULLISH_WATCH score=73.12 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- ORWE.CA: BULLISH_WATCH score=73.12 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- EGAL.CA: BULLISH_WATCH score=72.76 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=19.42 buy_ready=False sector_rank=12 price=315.23 support=295.0 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=24444692.0 spike=0.74
- ABUK.CA: score=20.1 buy_ready=False sector_rank=5 price=87.05 support=75.01 resistance=94.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=65.2 liquidity=30839510.0 spike=0.2
- ACAMD.CA: score=16.42 buy_ready=False sector_rank=12 price=2.05 support=1.95 resistance=2.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=46.94 liquidity=23546578.0 spike=0.41
- ACGC.CA: score=14.61 buy_ready=False sector_rank=8 price=13.83 support=12.04 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=50.19 liquidity=6765436.5 spike=0.15
- ADCI.CA: score=4.49 buy_ready=False sector_rank=12 price=278.01 support=267.66 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=31.74 liquidity=2077142.0 spike=0.3
- ADIB.CA: score=14.52 buy_ready=False sector_rank=11 price=51.51 support=50.51 resistance=55.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=40.97 liquidity=28936692.0 spike=0.43
- ADPC.CA: score=9.08 buy_ready=False sector_rank=12 price=3.83 support=3.81 resistance=4.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=45.28 liquidity=4666425.0 spike=0.19
- AFDI.CA: score=1.36 buy_ready=False sector_rank=12 price=53.73 support=51.6 resistance=68.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=31.12 liquidity=1945160.25 spike=0.08
- AFMC.CA: score=9.42 buy_ready=False sector_rank=12 price=162.19 support=157.0 resistance=267.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=20.95 liquidity=11180079.0 spike=0.19
- AJWA.CA: score=5.19 buy_ready=False sector_rank=12 price=179.84 support=175.15 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=46.93 liquidity=776433.13 spike=0.01
- ALCN.CA: score=13.47 buy_ready=False sector_rank=18 price=30.77 support=30.03 resistance=34.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=51.9 liquidity=6727236.0 spike=0.23
- ALUM.CA: score=3.56 buy_ready=False sector_rank=12 price=25.86 support=25.0 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=22.87 liquidity=1148302.13 spike=0.07
- AMER.CA: score=17.87 buy_ready=False sector_rank=7 price=5.46 support=4.8 resistance=6.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=46.3 liquidity=38778264.0 spike=0.61
- AMES.CA: score=8.42 buy_ready=False sector_rank=12 price=54.05 support=51.22 resistance=173.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=0.55 liquidity=244664976.0 spike=0.98
- AMIA.CA: score=5.33 buy_ready=False sector_rank=12 price=17.4 support=15.3 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=31.84 liquidity=2910701.5 spike=0.04
- AMOC.CA: score=18.0 buy_ready=False sector_rank=6 price=13.25 support=10.65 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=72.71 liquidity=72162464.0 spike=0.38
- APSW.CA: score=3.82 buy_ready=False sector_rank=12 price=8.43 support=8.37 resistance=9.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=39.78 liquidity=399615.75 spike=0.33
- ARAB.CA: score=14.87 buy_ready=False sector_rank=7 price=0.25 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=50.88 liquidity=40787268.0 spike=0.41
- ARCC.CA: score=12.02 buy_ready=False sector_rank=21 price=72.69 support=71.5 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=36.74 liquidity=5584163.5 spike=0.12
- AREH.CA: score=9.46 buy_ready=False sector_rank=12 price=1.43 support=1.39 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=45.16 liquidity=5047024.5 spike=0.29
- ARVA.CA: score=4.42 buy_ready=False sector_rank=12 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=2.6 buy_ready=False sector_rank=12 price=60.38 support=60.15 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=34.25 liquidity=3188250.75 spike=0.15
- ASPI.CA: score=12.42 buy_ready=False sector_rank=12 price=0.44 support=0.41 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=32.79 liquidity=36794288.0 spike=0.66
- ATLC.CA: score=12.73 buy_ready=False sector_rank=15 price=6.97 support=5.2 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=68.74 liquidity=3726448.5 spike=0.13
- ATQA.CA: score=18.1 buy_ready=False sector_rank=5 price=12.8 support=10.8 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=67.63 liquidity=44729104.0 spike=0.41
- AXPH.CA: score=6.74 buy_ready=False sector_rank=12 price=1688.88 support=1345.01 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=77.32 liquidity=2321415.75 spike=0.19
- BINV.CA: score=12.4 buy_ready=False sector_rank=3 price=59.75 support=50.0 resistance=59.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46899440.0 spike=4.19
- BIOC.CA: score=9.42 buy_ready=False sector_rank=12 price=285.19 support=272.01 resistance=535.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=9.64 liquidity=91789248.0 spike=0.7
- BTFH.CA: score=13.01 buy_ready=False sector_rank=15 price=2.91 support=2.87 resistance=3.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=41.94 liquidity=19332188.0 spike=0.19
- CAED.CA: score=12.42 buy_ready=False sector_rank=12 price=127.01 support=123.56 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=29.63 liquidity=10230142.0 spike=0.25
- CANA.CA: score=8.99 buy_ready=False sector_rank=11 price=41.8 support=41.0 resistance=44.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=1468559.75 spike=0.1
- CCAP.CA: score=19.4 buy_ready=False sector_rank=3 price=6.9 support=5.42 resistance=6.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=75.86 liquidity=664645504.0 spike=0.76
- CCRS.CA: score=14.2 buy_ready=False sector_rank=12 price=2.56 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=38.32 liquidity=6781787.0 spike=0.13
- CEFM.CA: score=10.49 buy_ready=False sector_rank=12 price=147.45 support=135.9 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=46.29 liquidity=1074191.38 spike=0.08
- CERA.CA: score=21.42 buy_ready=False sector_rank=12 price=1.45 support=1.22 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=55.75 liquidity=83634016.0 spike=0.91
- CFGH.CA: score=5.42 buy_ready=False sector_rank=12 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=4096.69 spike=0.19
- CICH.CA: score=9.35 buy_ready=False sector_rank=15 price=12.49 support=12.0 resistance=13.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=57.61 liquidity=339941.28 spike=0.07
- CIEB.CA: score=8.26 buy_ready=False sector_rank=11 price=24.51 support=24.01 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=46.47 liquidity=3737887.25 spike=0.27
- CIRA.CA: score=22.45 buy_ready=False sector_rank=4 price=39.56 support=32.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=9046584.0 spike=0.23
- CLHO.CA: score=8.93 buy_ready=False sector_rank=16 price=16.2 support=15.81 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=29.36 liquidity=16381182.0 spike=0.21
- CNFN.CA: score=-0.24 buy_ready=False sector_rank=15 price=4.59 support=4.46 resistance=4.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=31.34 liquidity=1749070.5 spike=0.14
- COMI.CA: score=9.52 buy_ready=False sector_rank=11 price=131.21 support=131.56 resistance=142.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=30.05 liquidity=288020928.0 spike=0.52
- COPR.CA: score=12.42 buy_ready=False sector_rank=12 price=0.5 support=0.44 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=29.08 liquidity=29481188.0 spike=0.33
- COSG.CA: score=14.54 buy_ready=False sector_rank=12 price=1.81 support=1.74 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=7124032.5 spike=0.17
- CPCI.CA: score=9.16 buy_ready=False sector_rank=12 price=532.02 support=525.01 resistance=569.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=36.59 liquidity=1745163.25 spike=0.41
- CSAG.CA: score=10.54 buy_ready=False sector_rank=18 price=37.32 support=37.04 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=37.06 liquidity=3798785.0 spike=0.23
- DAPH.CA: score=15.71 buy_ready=False sector_rank=12 price=120.53 support=108.11 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=58.73 liquidity=8295704.5 spike=0.13
- DEIN.CA: score=7.42 buy_ready=False sector_rank=12 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=4.74 buy_ready=False sector_rank=20 price=26.69 support=26.51 resistance=29.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=35.97 liquidity=1164119.63 spike=0.19
- DSCW.CA: score=9.12 buy_ready=False sector_rank=12 price=1.81 support=1.8 resistance=2.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=5706759.0 spike=0.13
- DTPP.CA: score=24.08 buy_ready=False sector_rank=12 price=336.04 support=290.1 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=119899528.0 spike=2.33
- EALR.CA: score=9.42 buy_ready=False sector_rank=12 price=382.38 support=340.0 resistance=456.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=24624890.0 spike=0.93
- EASB.CA: score=21.42 buy_ready=False sector_rank=12 price=8.21 support=7.16 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=15032437.0 spike=0.89
- EAST.CA: score=7.58 buy_ready=False sector_rank=20 price=32.3 support=33.04 resistance=36.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=30.25 liquidity=61721004.0 spike=0.91
- EBSC.CA: score=8.24 buy_ready=False sector_rank=12 price=2.07 support=1.88 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=819493.19 spike=0.06
- ECAP.CA: score=6.03 buy_ready=False sector_rank=12 price=32.27 support=31.16 resistance=39.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=39.53 liquidity=1616895.5 spike=0.13
- EDFM.CA: score=9.96 buy_ready=False sector_rank=12 price=413.37 support=394.0 resistance=432.0 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=56.63 liquidity=543168.17 spike=0.33
- EEII.CA: score=4.64 buy_ready=False sector_rank=12 price=2.2 support=2.15 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=35.13 liquidity=1228382.75 spike=0.05
- EFIC.CA: score=14.1 buy_ready=False sector_rank=5 price=193.93 support=192.75 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=39045216.0 spike=0.41
- EFID.CA: score=16.58 buy_ready=False sector_rank=20 price=30.72 support=29.71 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=42.82 liquidity=34105640.0 spike=0.59
- EFIH.CA: score=17.29 buy_ready=False sector_rank=13 price=23.44 support=22.16 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=48.53 liquidity=34122108.0 spike=0.51
- EGAL.CA: score=20.1 buy_ready=False sector_rank=5 price=362.0 support=321.01 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=55.66 liquidity=11487170.0 spike=0.1
- EGAS.CA: score=6.73 buy_ready=False sector_rank=6 price=56.13 support=55.0 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=38.85 liquidity=1721646.63 spike=0.19
- EGBE.CA: score=2.53 buy_ready=False sector_rank=11 price=0.51 support=0.49 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=8846.65 spike=0.06
- EGCH.CA: score=18.1 buy_ready=False sector_rank=5 price=13.75 support=13.3 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=59.09 liquidity=13098384.0 spike=0.11
- EGSA.CA: score=12.13 buy_ready=False sector_rank=1 price=9.0 support=8.67 resistance=9.1 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=78.18 liquidity=9954.0 spike=1.36
- EGTS.CA: score=7.13 buy_ready=False sector_rank=7 price=16.71 support=16.17 resistance=18.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=46.26 liquidity=2265578.75 spike=0.09
- EHDR.CA: score=14.42 buy_ready=False sector_rank=12 price=2.74 support=2.79 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=44.0 liquidity=19870292.0 spike=0.91
- EKHO.CA: score=6.0 buy_ready=False sector_rank=6 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=12.77 buy_ready=False sector_rank=17 price=1.95 support=1.98 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=38.24 liquidity=61023456.0 spike=0.87
- ELKA.CA: score=14.42 buy_ready=False sector_rank=12 price=1.73 support=1.7 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=50.88 liquidity=10356937.0 spike=0.23
- ELNA.CA: score=-1.3 buy_ready=False sector_rank=12 price=35.74 support=33.96 resistance=38.99 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=22.51 liquidity=288922.17 spike=0.62
- ELSH.CA: score=14.27 buy_ready=False sector_rank=12 price=12.72 support=12.71 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=45.15 liquidity=9855527.0 spike=0.26
- ELWA.CA: score=5.5 buy_ready=False sector_rank=12 price=1.69 support=1.62 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=1082504.0 spike=0.44
- EMFD.CA: score=19.87 buy_ready=False sector_rank=7 price=13.92 support=11.51 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=73.22 liquidity=68662472.0 spike=0.43
- ENGC.CA: score=0.82 buy_ready=False sector_rank=12 price=41.52 support=41.0 resistance=51.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=31.07 liquidity=1400500.13 spike=0.09
- EOSB.CA: score=9.43 buy_ready=False sector_rank=12 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=17259.01 spike=0.25
- EPCO.CA: score=16.86 buy_ready=False sector_rank=12 price=11.31 support=10.8 resistance=12.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=58.03 liquidity=7442612.0 spike=0.37
- EPPK.CA: score=-5.16 buy_ready=False sector_rank=12 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=23.44 buy_ready=False sector_rank=1 price=132.26 support=112.1 resistance=135.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=88.67 liquidity=194518336.0 spike=1.02
- ETRS.CA: score=12.87 buy_ready=False sector_rank=12 price=10.8 support=10.66 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=50.56 liquidity=8453783.0 spike=0.4
- EXPA.CA: score=15.64 buy_ready=False sector_rank=11 price=20.81 support=19.8 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=60.89 liquidity=8119739.5 spike=0.23
- FAIT.CA: score=10.05 buy_ready=False sector_rank=11 price=45.99 support=39.58 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=67.11 liquidity=529122.81 spike=0.06
- FAITA.CA: score=4.54 buy_ready=False sector_rank=11 price=0.99 support=0.98 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=47.14 liquidity=15480.28 spike=0.3
- FERC.CA: score=6.68 buy_ready=False sector_rank=5 price=77.5 support=76.7 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=48.11 liquidity=2575724.75 spike=0.13
- FWRY.CA: score=14.29 buy_ready=False sector_rank=13 price=18.76 support=18.66 resistance=19.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=44571792.0 spike=0.33
- GBCO.CA: score=18.38 buy_ready=False sector_rank=14 price=30.54 support=27.51 resistance=31.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=62.86 liquidity=57129920.0 spike=1.1
- GDWA.CA: score=13.42 buy_ready=False sector_rank=12 price=0.77 support=0.76 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=49.68 liquidity=16542451.0 spike=0.4
- GGCC.CA: score=17.42 buy_ready=False sector_rank=12 price=0.89 support=0.83 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=48.14 liquidity=23866888.0 spike=0.58
- GIHD.CA: score=17.11 buy_ready=False sector_rank=12 price=73.66 support=58.01 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=73.32 liquidity=7693885.5 spike=0.26
- GMCI.CA: score=0.21 buy_ready=False sector_rank=12 price=1.74 support=1.75 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=24.14 liquidity=752717.06 spike=1.52
- GRCA.CA: score=4.42 buy_ready=False sector_rank=12 price=46.08 support=40.0 resistance=46.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=52722840.0 spike=0.67
- GSSC.CA: score=11.88 buy_ready=False sector_rank=12 price=293.89 support=278.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=46.66 liquidity=2468204.0 spike=0.19
- GTWL.CA: score=17.42 buy_ready=False sector_rank=12 price=236.63 support=165.0 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=66.99 liquidity=42438312.0 spike=0.15
- HDBK.CA: score=17.52 buy_ready=False sector_rank=11 price=114.18 support=89.01 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=69.19 liquidity=39544932.0 spike=0.68
- HELI.CA: score=20.43 buy_ready=False sector_rank=7 price=8.23 support=7.34 resistance=8.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=69.7 liquidity=193491824.0 spike=1.28
- HRHO.CA: score=13.01 buy_ready=False sector_rank=15 price=25.21 support=25.21 resistance=26.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=42.59 liquidity=15972950.0 spike=0.16
- ICID.CA: score=11.65 buy_ready=False sector_rank=12 price=18.13 support=14.5 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=62.93 liquidity=2235976.0 spike=0.1
- IDRE.CA: score=14.31 buy_ready=False sector_rank=12 price=53.71 support=51.0 resistance=57.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=58.73 liquidity=6897616.0 spike=0.67
- IFAP.CA: score=13.55 buy_ready=False sector_rank=2 price=20.31 support=20.05 resistance=22.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=40.83 liquidity=5154410.0 spike=0.21
- INFI.CA: score=7.28 buy_ready=False sector_rank=12 price=134.24 support=130.15 resistance=174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=16.76 liquidity=4866968.5 spike=0.13
- IRON.CA: score=9.1 buy_ready=False sector_rank=5 price=26.72 support=27.08 resistance=33.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=5.54 liquidity=10322262.0 spike=0.72
- ISMA.CA: score=4.98 buy_ready=False sector_rank=12 price=30.03 support=28.05 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=25.48 liquidity=5566038.5 spike=0.21
- ISMQ.CA: score=10.18 buy_ready=False sector_rank=5 price=8.84 support=8.68 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=36.59 liquidity=5079987.5 spike=0.17
- ISPH.CA: score=9.17 buy_ready=False sector_rank=16 price=12.27 support=11.9 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=33.74 liquidity=73869128.0 spike=1.12
- JUFO.CA: score=6.49 buy_ready=False sector_rank=20 price=26.85 support=26.45 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=51.33 liquidity=1913800.13 spike=0.09
- KABO.CA: score=19.85 buy_ready=False sector_rank=8 price=9.38 support=8.82 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=60.58 liquidity=32268320.0 spike=0.6
- KWIN.CA: score=9.42 buy_ready=False sector_rank=12 price=88.64 support=84.5 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=26.96 liquidity=13421861.0 spike=0.2
- KZPC.CA: score=11.55 buy_ready=False sector_rank=12 price=14.16 support=12.14 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=64.52 liquidity=2134855.5 spike=0.03
- LCSW.CA: score=8.75 buy_ready=False sector_rank=21 price=32.99 support=32.83 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=38.59 liquidity=5320939.5 spike=0.19
- LUTS.CA: score=17.42 buy_ready=False sector_rank=12 price=0.93 support=0.79 resistance=1.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=47.19 liquidity=42346308.0 spike=0.15
- MAAL.CA: score=4.76 buy_ready=False sector_rank=12 price=8.71 support=8.18 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=39.87 liquidity=341256.25 spike=0.03
- MASR.CA: score=18.42 buy_ready=False sector_rank=12 price=7.91 support=7.49 resistance=8.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=56.3 liquidity=38576332.0 spike=0.43
- MBSC.CA: score=16.43 buy_ready=False sector_rank=21 price=379.19 support=355.04 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=48.68 liquidity=35267736.0 spike=0.59
- MCQE.CA: score=10.36 buy_ready=False sector_rank=21 price=219.67 support=212.01 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=31.0 liquidity=8932713.0 spike=0.23
- MCRO.CA: score=16.42 buy_ready=False sector_rank=12 price=1.71 support=1.44 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=77.5 liquidity=98135984.0 spike=0.84
- MENA.CA: score=0.63 buy_ready=False sector_rank=7 price=6.65 support=6.58 resistance=7.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=29.21 liquidity=764364.75 spike=0.27
- MEPA.CA: score=17.1 buy_ready=False sector_rank=12 price=1.95 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=58.23 liquidity=5684066.5 spike=0.16
- MFPC.CA: score=17.1 buy_ready=False sector_rank=5 price=47.16 support=38.93 resistance=48.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=80.29 liquidity=49249776.0 spike=0.39
- MFSC.CA: score=5.43 buy_ready=False sector_rank=12 price=49.01 support=48.6 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=46.13 liquidity=1013171.5 spike=0.2
- MHOT.CA: score=8.19 buy_ready=False sector_rank=9 price=17.96 support=17.72 resistance=19.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=50.89 liquidity=1425091.75 spike=0.13
- MICH.CA: score=10.44 buy_ready=False sector_rank=12 price=48.83 support=47.2 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=47.97 liquidity=3027332.25 spike=0.12
- MILS.CA: score=7.38 buy_ready=False sector_rank=12 price=199.48 support=192.22 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=21.55 liquidity=4960215.0 spike=0.09
- MIPH.CA: score=6.31 buy_ready=False sector_rank=16 price=801.17 support=700.2 resistance=820.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:27 AM market time freshness=DELAYED_CURRENT RSI=75.41 liquidity=375158.03 spike=0.09
- MOED.CA: score=16.42 buy_ready=False sector_rank=12 price=0.79 support=0.69 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=55.04 liquidity=24343496.0 spike=0.2
- MOIL.CA: score=10.09 buy_ready=False sector_rank=6 price=0.68 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=47.14 liquidity=89515.91 spike=0.42
- MOIN.CA: score=14.06 buy_ready=False sector_rank=12 price=36.56 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=56.28 liquidity=4641131.0 spike=0.15
- MOSC.CA: score=4.24 buy_ready=False sector_rank=12 price=309.86 support=305.0 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=24.31 liquidity=1820208.0 spike=0.21
- MPCI.CA: score=19.42 buy_ready=False sector_rank=12 price=413.0 support=345.0 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=51.36 liquidity=40386400.0 spike=0.26
- MPCO.CA: score=25.4 buy_ready=False sector_rank=2 price=2.77 support=2.07 resistance=2.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=68.67 liquidity=124886992.0 spike=0.8
- MPRC.CA: score=11.26 buy_ready=False sector_rank=12 price=38.48 support=38.31 resistance=46.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=36.12 liquidity=6848051.0 spike=0.17
- MTIE.CA: score=11.91 buy_ready=False sector_rank=14 price=8.42 support=8.1 resistance=9.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=39.55 liquidity=7727621.0 spike=0.18
- NAHO.CA: score=-5.56 buy_ready=False sector_rank=12 price=0.14 support=0.14 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25053.51 spike=0.24
- NCCW.CA: score=18.42 buy_ready=False sector_rank=12 price=8.28 support=5.59 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=81.34 liquidity=48560112.0 spike=0.82
- NEDA.CA: score=4.75 buy_ready=False sector_rank=12 price=2.72 support=2.7 resistance=2.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=51.35 liquidity=331814.63 spike=0.34
- NHPS.CA: score=2.31 buy_ready=False sector_rank=12 price=76.05 support=75.31 resistance=98.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=4.03 liquidity=2897350.5 spike=0.13
- NINH.CA: score=9.42 buy_ready=False sector_rank=12 price=20.96 support=20.5 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=15.11 liquidity=11524016.0 spike=0.38
- NIPH.CA: score=11.93 buy_ready=False sector_rank=16 price=319.16 support=301.0 resistance=414.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=19.41 liquidity=115123608.0 spike=0.56
- OBRI.CA: score=6.78 buy_ready=False sector_rank=12 price=30.6 support=30.1 resistance=34.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=39.46 liquidity=3364199.25 spike=0.16
- OCDI.CA: score=14.87 buy_ready=False sector_rank=7 price=29.6 support=29.25 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=35.4 liquidity=33298608.0 spike=0.4
- OCPH.CA: score=5.56 buy_ready=False sector_rank=12 price=240.29 support=210.0 resistance=277.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=27.82 liquidity=5139450.5 spike=0.54
- ODIN.CA: score=2.25 buy_ready=False sector_rank=12 price=2.76 support=2.55 resistance=3.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=22.22 liquidity=2830200.25 spike=0.1
- OFH.CA: score=19.42 buy_ready=False sector_rank=12 price=1.05 support=0.88 resistance=1.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=56.28 liquidity=33982060.0 spike=0.3
- OIH.CA: score=20.4 buy_ready=False sector_rank=3 price=2.15 support=1.76 resistance=2.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=68.52 liquidity=23001000.0 spike=0.19
- OLFI.CA: score=11.15 buy_ready=False sector_rank=20 price=22.52 support=22.07 resistance=25.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=41.34 liquidity=7568679.0 spike=0.47
- ORAS.CA: score=4.6 buy_ready=False sector_rank=10 price=837.21 support=829.0 resistance=855.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=78621864.0 spike=1.0
- ORHD.CA: score=19.99 buy_ready=False sector_rank=7 price=42.97 support=40.28 resistance=43.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=52.03 liquidity=138935280.0 spike=1.06
- ORWE.CA: score=19.85 buy_ready=False sector_rank=8 price=26.75 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=53.3 liquidity=10169161.0 spike=0.19
- PHAR.CA: score=11.93 buy_ready=False sector_rank=16 price=118.73 support=117.01 resistance=141.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=18.95 liquidity=82053720.0 spike=0.45
- PHDC.CA: score=9.87 buy_ready=False sector_rank=7 price=13.8 support=13.65 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=30.15 liquidity=25423860.0 spike=0.12
- PHTV.CA: score=9.99 buy_ready=False sector_rank=12 price=374.57 support=311.27 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=66.55 liquidity=2337937.0 spike=1.12
- POUL.CA: score=9.13 buy_ready=False sector_rank=20 price=38.14 support=36.97 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=52.85 liquidity=5547371.5 spike=0.23
- PRCL.CA: score=11.91 buy_ready=False sector_rank=21 price=32.57 support=30.9 resistance=36.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=45.12 liquidity=8480164.0 spike=0.4
- PRDC.CA: score=3.47 buy_ready=False sector_rank=7 price=7.87 support=7.77 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=27.27 liquidity=3603512.5 spike=0.05
- PRMH.CA: score=5.8 buy_ready=False sector_rank=12 price=2.55 support=2.28 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=59.15 liquidity=1385303.25 spike=0.13
- RACC.CA: score=6.56 buy_ready=False sector_rank=12 price=9.64 support=9.4 resistance=10.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=47.55 liquidity=2148650.0 spike=0.1
- RAKT.CA: score=11.05 buy_ready=False sector_rank=12 price=22.65 support=21.4 resistance=23.02 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=57.94 liquidity=315582.44 spike=1.16
- RAYA.CA: score=13.61 buy_ready=False sector_rank=19 price=7.1 support=6.95 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=43.09 liquidity=12931581.0 spike=0.22
- RMDA.CA: score=16.93 buy_ready=False sector_rank=16 price=6.14 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=48.15 liquidity=17690510.0 spike=0.3
- ROTO.CA: score=4.67 buy_ready=False sector_rank=12 price=40.31 support=35.02 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=13.49 liquidity=5249788.5 spike=0.44
- RREI.CA: score=10.71 buy_ready=False sector_rank=12 price=4.35 support=4.24 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=53.12 liquidity=3296822.75 spike=0.11
- RTVC.CA: score=0.18 buy_ready=False sector_rank=12 price=3.91 support=3.78 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=34.62 liquidity=763085.81 spike=0.11
- RUBX.CA: score=7.02 buy_ready=False sector_rank=12 price=14.0 support=12.94 resistance=14.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46501936.0 spike=2.3
- SAUD.CA: score=8.72 buy_ready=False sector_rank=11 price=23.12 support=22.7 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=46.51 liquidity=1196742.0 spike=0.08
- SCEM.CA: score=16.43 buy_ready=False sector_rank=21 price=95.07 support=94.0 resistance=112.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=49.69 liquidity=19351696.0 spike=0.13
- SCFM.CA: score=5.39 buy_ready=False sector_rank=12 price=270.25 support=265.51 resistance=305.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=36.63 liquidity=973696.44 spike=0.1
- SCTS.CA: score=3.17 buy_ready=False sector_rank=4 price=605.87 support=566.66 resistance=660.0 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=27.62 liquidity=1771563.87 spike=0.36
- SDTI.CA: score=8.89 buy_ready=False sector_rank=12 price=73.78 support=67.0 resistance=76.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=70.2 liquidity=1478139.75 spike=0.07
- SEIG.CA: score=9.02 buy_ready=False sector_rank=12 price=257.84 support=230.5 resistance=267.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9606045.0 spike=6.29
- SIPC.CA: score=19.42 buy_ready=False sector_rank=12 price=5.96 support=4.1 resistance=6.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=65.96 liquidity=47587652.0 spike=0.77
- SKPC.CA: score=20.1 buy_ready=False sector_rank=5 price=17.96 support=16.8 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=57.96 liquidity=84577160.0 spike=0.6
- SMFR.CA: score=1.59 buy_ready=False sector_rank=12 price=242.71 support=236.1 resistance=276.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=26.97 liquidity=2176355.5 spike=0.21
- SNFC.CA: score=15.4 buy_ready=False sector_rank=12 price=11.01 support=10.26 resistance=11.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=57.39 liquidity=6988683.0 spike=0.51
- SPIN.CA: score=13.77 buy_ready=False sector_rank=8 price=17.11 support=17.21 resistance=20.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=38.77 liquidity=5923186.0 spike=0.2
- SPMD.CA: score=9.42 buy_ready=False sector_rank=12 price=0.48 support=0.48 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=365990528.0 spike=7.77
- SUGR.CA: score=20.58 buy_ready=False sector_rank=20 price=60.69 support=50.0 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=61.6 liquidity=10045223.0 spike=0.14
- SVCE.CA: score=19.42 buy_ready=False sector_rank=12 price=11.78 support=10.28 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=59.71 liquidity=28633004.0 spike=0.17
- SWDY.CA: score=16.77 buy_ready=False sector_rank=17 price=124.67 support=115.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=47.74 liquidity=17664400.0 spike=0.18
- TALM.CA: score=20.92 buy_ready=False sector_rank=4 price=22.43 support=17.11 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=77.24 liquidity=71266664.0 spike=1.26
- TMGH.CA: score=14.87 buy_ready=False sector_rank=7 price=95.54 support=94.9 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=40.6 liquidity=99314160.0 spike=0.37
- TRTO.CA: score=9.43 buy_ready=False sector_rank=12 price=0.07 support=0.04 resistance=0.08 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=67.92 liquidity=10220.28 spike=0.37
- UEFM.CA: score=4.54 buy_ready=False sector_rank=12 price=534.5 support=440.66 resistance=557.0 source=Yahoo Finance as_of=2026-09-14T21:00:00+00:00 freshness=FRESH RSI=46.56 liquidity=128280.0 spike=0.05
- UEGC.CA: score=4.9 buy_ready=False sector_rank=12 price=1.78 support=1.69 resistance=1.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=56434044.0 spike=1.24
- UNIP.CA: score=12.69 buy_ready=False sector_rank=12 price=0.38 support=0.35 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=53.61 liquidity=8273942.0 spike=0.24
- UNIT.CA: score=22.89 buy_ready=False sector_rank=7 price=19.47 support=18.11 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=55.02 liquidity=19709148.0 spike=1.51
- WCDF.CA: score=12.55 buy_ready=False sector_rank=12 price=747.55 support=630.0 resistance=759.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=88.79 liquidity=3773501.5 spike=1.18
- WKOL.CA: score=19.42 buy_ready=False sector_rank=12 price=353.0 support=332.56 resistance=372.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=53.8 liquidity=13799643.0 spike=0.72
- ZEOT.CA: score=8.53 buy_ready=False sector_rank=12 price=13.12 support=13.04 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=43.46 liquidity=1118317.63 spike=0.14
- ZMID.CA: score=17.87 buy_ready=False sector_rank=7 price=9.21 support=7.39 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=69.21 liquidity=57012432.0 spike=0.23

## Backtesting Lite
- MPCO.CA: 180d return=63.95%, max drawdown=-16.86%, MA20>MA50 days last20=20, as_of=2026-09-14T21:00:00+00:00
- DTPP.CA: 180d return=189.05%, max drawdown=-24.75%, MA20>MA50 days last20=20, as_of=2026-09-14T21:00:00+00:00
- ETEL.CA: 180d return=106.98%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-09-14T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=623 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- DTPP.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=623 sources=3 expected=Delta Co. For Printing & Packaging S.A.E summary=Delta for Printing to disburse EGP 56m dividends for 2025; Delta for Printing&#39;s profit leaps 89% in 2020; dividends proposed; Delta for Printing Q1 profits rise 175%
  - Delta for Printing to disburse EGP 56m dividends for 2025: https://english.mubasher.info/news/4596419/Delta-for-Printing-to-disburse-EGP-56m-dividends-for-2025/
  - Delta for Printing&#39;s profit leaps 89% in 2020; dividends proposed: https://english.mubasher.info/news/3759564/Delta-for-Printing-s-profit-leaps-89-in-2020-dividends-proposed/
  - Delta for Printing Q1 profits rise 175%: https://english.mubasher.info/news/3106332/Delta-for-Printing-Q1-profits-rise-175-/
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- UNIT.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=623 sources=3 expected=United Housing and Development summary=United Housing’s shareholders pass EGP 0.12/shr dividends for 2025; United Housing unveils EGP 5.9bn mixed-use project in Alexandria; United Housing’s consolidated net profits exceed EGP 174.5m in 9M-25
  - United Housing’s shareholders pass EGP 0.12/shr dividends for 2025: https://english.mubasher.info/news/4591202/United-Housing-s-shareholders-pass-EGP-0-12-shr-dividends-for-2025/
  - United Housing unveils EGP 5.9bn mixed-use project in Alexandria: https://english.mubasher.info/news/4540667/United-Housing-unveils-EGP-5-9bn-mixed-use-project-in-Alexandria/
  - United Housing’s consolidated net profits exceed EGP 174.5m in 9M-25: https://english.mubasher.info/news/4530945/United-Housing-s-consolidated-net-profits-exceed-EGP-174-5m-in-9M-25/
- CIRA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Investment and Real Estate Development summary=CIRA Education take over 51% of L’École Française Hurghada; CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion; CIRA Education launches Middle East’s 1st initiative for care economy
  - CIRA Education take over 51% of L’École Française Hurghada: https://english.mubasher.info/news/4488666/CIRA-Education-take-over-51-of-L-%C3%89cole-Fran%C3%A7aise-Hurghada/
  - CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion: https://english.mubasher.info/news/4393636/CIRA-s-majority-shareholder-acquires-37-5-additional-equity-backs-regional-expansion/
  - CIRA Education launches Middle East’s 1st initiative for care economy: https://english.mubasher.info/news/4391766/CIRA-Education-launches-Middle-East-s-1st-initiative-for-care-economy/
- CERA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=The Arab Ceramic Co. summary=Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- EASB.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Arabian Company (Themar) for securities Brokerage EAC summary=Evidence rejected for EASB.CA: source text did not clearly match EASB.CA / Egyptian Arabian Company (Themar) for securities Brokerage EAC.
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.

## Warnings
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for DTPP.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for UNIT.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
- Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- Evidence rejected for EASB.CA: source text did not clearly match EASB.CA / Egyptian Arabian Company (Themar) for securities Brokerage EAC.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
