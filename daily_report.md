# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-10-05T16:46:16.198697+00:00
Generated Cairo: 2026-10-05 19:46
Run timing: target 11:00 Cairo | generated Cairo 2026-10-05 19:46 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-10-05 19:42

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 179/187
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, October 05
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 15.79% / above MA50 42.11%
- EGX70 regime: BEARISH / above MA20 29.73% / above MA50 32.43%
- Sector breadth: 57.14%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=611605760.0 spike=1.11 score=9.56
- CCAP.CA: liquidity=481218240.0 spike=0.58 score=22.4
- MBSC.CA: liquidity=470803072.0 spike=10.31 score=11.1
- HRHO.CA: liquidity=447388096.0 spike=4.65 score=26.57
- ETEL.CA: liquidity=261036256.0 spike=0.83 score=23.4

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with weak breadth; sector breadth 57% and risk mode defensive, so the scanner flags accumulation spikes but maintains a HOLD stance.
- Tickets were selected for high outlook scores (>70) and liquidity‑spike patterns (accumulation) despite the bearish regime, indicating short‑term buying interest that is not yet actionable.
- Liquidity spikes (e.g., HRHO.CA 4.65×, AJWA.CA 6.16×) suggest institutional accumulation, but prices sit close to resistance or far above support, limiting near‑term upside.
- Leading sectors (Telecommunications, Education, Investment Holding) show better MA20/MA50 alignment, yet overall sector breadth remains moderate, keeping uncertainty elevated.
- With EGX30/EGX70 trending bearish and risk mode set to DEFENSIVE_NO_NEW_BUY, the scanner holds all tickets at LOW confidence; bullish watch signals are tentative and could reverse if breadth weakens further.

## Top Liquidity Spikes
- MBSC.CA: spike=10.31 liquidity=470803072.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MCQE.CA: spike=8.73 liquidity=244416416.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- PRDC.CA: spike=7.34 liquidity=207127824.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RAKT.CA: spike=7.21 liquidity=1384144.25 outlook=NEUTRAL score=44.21 buy_ready=False
- AJWA.CA: spike=6.16 liquidity=82162768.0 outlook=BULLISH_WATCH score=83.21 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=13.04 5d=5.58% 20d=12.54% aboveMA50=100.0%
- #2 Education: score=7.84 5d=2.0% 20d=5.06% aboveMA50=66.67%
- #3 Investment Holding: score=7.48 5d=0.15% 20d=12.75% aboveMA50=66.67%
- #4 Fintech & Payments: score=6.96 5d=3.35% 20d=-0.18% aboveMA50=50.0%
- #5 Transportation & Logistics: score=6.5 5d=6.83% 20d=-1.24% aboveMA50=50.0%
- #6 Energy & Petrochemicals: score=6.37 5d=0.19% 20d=2.66% aboveMA50=66.67%
- #7 Automotive & Distribution: score=6.23 5d=4.47% 20d=1.5% aboveMA50=50.0%
- #8 Building Materials: score=5.25 5d=4.2% 20d=-4.17% aboveMA50=16.67%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CIRA.CA: BULLISH_WATCH score=92.84 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- EFIH.CA: BULLISH_WATCH score=87.96 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- CCAP.CA: BULLISH_WATCH score=87.48 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ARCC.CA: BULLISH_WATCH score=83.25 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- AJWA.CA: BULLISH_WATCH score=83.21 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- BINV.CA: BULLISH_WATCH score=79.48 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- TALM.CA: BULLISH_WATCH score=78.84 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support
- AMOC.CA: BULLISH_WATCH score=76.37 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ACGC.CA: BULLISH_WATCH score=75.63 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- HRHO.CA: BULLISH_WATCH score=74.93 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=3.36 buy_ready=False sector_rank=18 price=261.71 support=230.11 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.79 liquidity=3873020.75 spike=0.17
- ABUK.CA: score=17.7 buy_ready=False sector_rank=15 price=86.06 support=83.55 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=58475680.0 spike=0.48
- ACAMD.CA: score=18.48 buy_ready=False sector_rank=18 price=2.06 support=1.87 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=51.02 liquidity=43309368.0 spike=0.93
- ACGC.CA: score=18.11 buy_ready=False sector_rank=9 price=14.56 support=13.11 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=51.15 liquidity=7257442.5 spike=0.32
- ADCI.CA: score=5.33 buy_ready=False sector_rank=18 price=273.22 support=256.0 resistance=298.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.9 liquidity=847433.19 spike=0.34
- ADIB.CA: score=15.34 buy_ready=False sector_rank=11 price=49.24 support=48.2 resistance=54.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.63 liquidity=55017332.0 spike=0.73
- ADPC.CA: score=10.75 buy_ready=False sector_rank=18 price=3.59 support=3.4 resistance=4.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.94 liquidity=7266958.5 spike=0.44
- AFDI.CA: score=18.06 buy_ready=False sector_rank=18 price=53.5 support=47.7 resistance=56.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=50.73 liquidity=12670302.0 spike=1.79
- AFMC.CA: score=16.48 buy_ready=False sector_rank=18 price=158.61 support=131.0 resistance=188.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.71 liquidity=17384400.0 spike=0.34
- AJWA.CA: score=26.48 buy_ready=False sector_rank=18 price=190.23 support=176.0 resistance=188.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.08 liquidity=82162768.0 spike=6.16
- ALCN.CA: score=23.4 buy_ready=False sector_rank=5 price=35.07 support=30.4 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.94 liquidity=21914722.0 spike=0.64
- ALUM.CA: score=6.9 buy_ready=False sector_rank=18 price=24.32 support=21.65 resistance=28.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.03 liquidity=2419370.0 spike=0.42
- AMER.CA: score=14.12 buy_ready=False sector_rank=19 price=4.71 support=4.05 resistance=5.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.84 liquidity=44686616.0 spike=1.11
- AMES.CA: score=15.48 buy_ready=False sector_rank=18 price=48.42 support=40.15 resistance=82.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.74 liquidity=77330320.0 spike=0.33
- AMIA.CA: score=22.48 buy_ready=False sector_rank=18 price=19.35 support=17.12 resistance=20.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=73.31 liquidity=63232148.0 spike=4.06
- AMOC.CA: score=21.4 buy_ready=False sector_rank=6 price=13.77 support=12.18 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.85 liquidity=69947528.0 spike=0.51
- APSW.CA: score=12.01 buy_ready=False sector_rank=18 price=8.56 support=7.81 resistance=8.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=39.76 liquidity=2010995.25 spike=3.26
- ARAB.CA: score=23.84 buy_ready=False sector_rank=19 price=0.26 support=0.2 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.4 liquidity=240680112.0 spike=3.47
- ARCC.CA: score=23.84 buy_ready=False sector_rank=8 price=72.21 support=60.01 resistance=78.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.39 liquidity=62735520.0 spike=2.37
- AREH.CA: score=9.74 buy_ready=False sector_rank=18 price=1.32 support=1.14 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.91 liquidity=6253567.0 spike=0.5
- ASCM.CA: score=10.32 buy_ready=False sector_rank=18 price=59.48 support=53.8 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.43 liquidity=5831983.0 spike=0.38
- ASPI.CA: score=4.48 buy_ready=False sector_rank=18 price=0.36 support=0.36 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32385704.0 spike=0.66
- ATLC.CA: score=12.83 buy_ready=False sector_rank=10 price=6.38 support=5.2 resistance=7.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.81 liquidity=4262063.0 spike=0.31
- ATQA.CA: score=17.7 buy_ready=False sector_rank=15 price=12.02 support=10.91 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=41.5 liquidity=76080912.0 spike=0.9
- AXPH.CA: score=10.63 buy_ready=False sector_rank=18 price=1525.7 support=1334.35 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=36.47 liquidity=3150293.5 spike=0.47
- BINV.CA: score=18.36 buy_ready=False sector_rank=3 price=59.31 support=49.91 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=69.82 liquidity=5956683.5 spike=0.24
- BIOC.CA: score=16.66 buy_ready=False sector_rank=18 price=339.21 support=225.21 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.76 liquidity=94369488.0 spike=1.09
- BTFH.CA: score=15.07 buy_ready=False sector_rank=10 price=2.81 support=2.65 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.89 liquidity=112652856.0 spike=1.25
- CAED.CA: score=14.48 buy_ready=False sector_rank=18 price=123.11 support=103.1 resistance=150.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.39 liquidity=13354284.0 spike=0.69
- CANA.CA: score=18.34 buy_ready=False sector_rank=11 price=46.05 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=68.53 liquidity=15002852.0 spike=0.66
- CCAP.CA: score=22.4 buy_ready=False sector_rank=3 price=6.8 support=5.97 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.98 liquidity=481218240.0 spike=0.58
- CCRS.CA: score=10.56 buy_ready=False sector_rank=18 price=2.36 support=2.21 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.49 liquidity=6072269.0 spike=0.38
- CEFM.CA: score=8.8 buy_ready=False sector_rank=18 price=141.01 support=113.0 resistance=167.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.76 liquidity=1319752.38 spike=0.17
- CERA.CA: score=20.02 buy_ready=False sector_rank=18 price=1.47 support=1.18 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.93 liquidity=185445264.0 spike=1.27
- CFGH.CA: score=-1.52 buy_ready=False sector_rank=18 price=0.11 support=0.11 resistance=0.12 source=Yahoo Finance as_of=2026-10-03T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=981.53 spike=0.12
- CICH.CA: score=10.07 buy_ready=False sector_rank=10 price=12.01 support=10.75 resistance=13.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=53.07 liquidity=1501887.13 spike=0.28
- CIEB.CA: score=10.15 buy_ready=False sector_rank=11 price=24.43 support=23.0 resistance=26.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.76 liquidity=4810618.0 spike=0.42
- CIRA.CA: score=24.1 buy_ready=False sector_rank=2 price=40.19 support=36.5 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.98 liquidity=45520232.0 spike=1.35
- CLHO.CA: score=16.87 buy_ready=False sector_rank=13 price=15.68 support=13.9 resistance=17.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.89 liquidity=28081186.0 spike=0.57
- CNFN.CA: score=10.35 buy_ready=False sector_rank=10 price=4.19 support=3.84 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.34 liquidity=5775161.0 spike=0.58
- COMI.CA: score=9.56 buy_ready=False sector_rank=11 price=126.48 support=124.5 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=27.82 liquidity=611605760.0 spike=1.11
- COPR.CA: score=21.84 buy_ready=False sector_rank=18 price=0.5 support=0.44 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=63.76 liquidity=32026142.0 spike=1.18
- COSG.CA: score=9.2 buy_ready=False sector_rank=18 price=1.66 support=1.46 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.48 liquidity=9713425.0 spike=0.53
- CPCI.CA: score=10.39 buy_ready=False sector_rank=18 price=602.1 support=530.0 resistance=613.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=94.61 liquidity=1910614.63 spike=0.51
- CSAG.CA: score=13.15 buy_ready=False sector_rank=5 price=37.01 support=34.52 resistance=42.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.05 liquidity=6746728.0 spike=0.71
- DAPH.CA: score=10.92 buy_ready=False sector_rank=18 price=95.31 support=89.1 resistance=140.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.96 liquidity=44927316.0 spike=1.72
- DEIN.CA: score=7.48 buy_ready=False sector_rank=18 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=6.55 buy_ready=False sector_rank=20 price=24.9 support=23.81 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=4026776.0 spike=0.87
- DSCW.CA: score=13.48 buy_ready=False sector_rank=18 price=1.71 support=1.58 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=15684694.0 spike=0.72
- DTPP.CA: score=14.48 buy_ready=False sector_rank=18 price=292.87 support=250.01 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.77 liquidity=35132952.0 spike=0.4
- EALR.CA: score=6.0 buy_ready=False sector_rank=18 price=343.35 support=312.0 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=35.19 liquidity=2517116.75 spike=0.23
- EASB.CA: score=4.42 buy_ready=False sector_rank=18 price=7.52 support=6.04 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=33.64 liquidity=4936082.5 spike=0.34
- EAST.CA: score=8.04 buy_ready=False sector_rank=20 price=29.0 support=27.91 resistance=36.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.75 liquidity=61814364.0 spike=1.26
- EBSC.CA: score=2.0 buy_ready=False sector_rank=18 price=1.86 support=1.61 resistance=2.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.77 liquidity=2517873.5 spike=0.54
- ECAP.CA: score=6.97 buy_ready=False sector_rank=18 price=30.48 support=29.13 resistance=34.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.99 liquidity=7242157.5 spike=1.62
- EDFM.CA: score=9.79 buy_ready=False sector_rank=18 price=398.14 support=354.0 resistance=465.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.48 liquidity=3365670.5 spike=1.97
- EEII.CA: score=10.05 buy_ready=False sector_rank=18 price=2.15 support=2.02 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=50.63 liquidity=4563506.5 spike=0.44
- EFIC.CA: score=8.7 buy_ready=False sector_rank=15 price=165.52 support=147.0 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=25.03 liquidity=23843192.0 spike=0.07
- EFID.CA: score=7.52 buy_ready=False sector_rank=20 price=18.92 support=18.1 resistance=32.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=15.26 liquidity=46588968.0 spike=0.71
- EFIH.CA: score=25.08 buy_ready=False sector_rank=4 price=24.14 support=20.2 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.02 liquidity=95615912.0 spike=1.84
- EGAL.CA: score=18.48 buy_ready=False sector_rank=15 price=345.96 support=331.5 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.98 liquidity=73169376.0 spike=1.39
- EGAS.CA: score=14.89 buy_ready=False sector_rank=6 price=57.03 support=53.62 resistance=60.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.49 liquidity=6487637.0 spike=0.54
- EGBE.CA: score=15.74 buy_ready=False sector_rank=11 price=0.54 support=0.49 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=69.15 liquidity=393094.72 spike=3.59
- EGCH.CA: score=14.7 buy_ready=False sector_rank=15 price=13.4 support=12.88 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.57 liquidity=44125804.0 spike=0.43
- EGSA.CA: score=12.43 buy_ready=False sector_rank=1 price=8.87 support=8.82 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=11.76 liquidity=30250.42 spike=4.23
- EGTS.CA: score=14.08 buy_ready=False sector_rank=19 price=16.99 support=15.65 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.07 liquidity=38076084.0 spike=1.09
- EHDR.CA: score=7.97 buy_ready=False sector_rank=18 price=2.53 support=2.35 resistance=3.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=33.78 liquidity=8481368.0 spike=0.64
- ELEC.CA: score=13.73 buy_ready=False sector_rank=14 price=1.91 support=1.72 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.14 liquidity=28414888.0 spike=0.41
- ELKA.CA: score=14.48 buy_ready=False sector_rank=18 price=1.62 support=1.43 resistance=1.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.1 liquidity=11900755.0 spike=0.79
- ELNA.CA: score=0.62 buy_ready=False sector_rank=18 price=35.22 support=33.46 resistance=38.99 source=Yahoo Finance as_of=2026-10-03T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=139189.44 spike=0.51
- ELSH.CA: score=14.78 buy_ready=False sector_rank=18 price=11.97 support=10.8 resistance=14.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=29886622.0 spike=1.15
- ELWA.CA: score=0.18 buy_ready=False sector_rank=18 price=1.55 support=1.43 resistance=1.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=12.5 liquidity=1173048.0 spike=1.26
- EMFD.CA: score=13.9 buy_ready=False sector_rank=19 price=12.8 support=11.7 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.18 liquidity=80143520.0 spike=0.89
- ENGC.CA: score=14.48 buy_ready=False sector_rank=18 price=37.13 support=33.33 resistance=46.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.39 liquidity=10769314.0 spike=0.61
- EOSB.CA: score=9.48 buy_ready=False sector_rank=18 price=1.57 support=1.57 resistance=1.64 source=Yahoo Finance as_of=2026-10-03T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=25.12 spike=0.0
- EPCO.CA: score=12.18 buy_ready=False sector_rank=18 price=9.98 support=9.25 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.57 liquidity=7697708.0 spike=0.54
- EPPK.CA: score=-5.1 buy_ready=False sector_rank=18 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=23.4 buy_ready=False sector_rank=1 price=149.93 support=118.51 resistance=154.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=77.75 liquidity=261036256.0 spike=0.83
- ETRS.CA: score=19.16 buy_ready=False sector_rank=18 price=10.99 support=9.82 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=53.26 liquidity=9596250.0 spike=1.04
- EXPA.CA: score=18.4 buy_ready=False sector_rank=11 price=21.28 support=20.4 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.88 liquidity=33914712.0 spike=1.03
- FAIT.CA: score=11.06 buy_ready=False sector_rank=11 price=44.84 support=38.48 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=44.56 liquidity=2715894.75 spike=0.6
- FAITA.CA: score=6.38 buy_ready=False sector_rank=11 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-10-03T21:00:00+00:00 freshness=FRESH RSI=52.63 liquidity=51273.97 spike=1.49
- FERC.CA: score=5.3 buy_ready=False sector_rank=15 price=76.46 support=70.42 resistance=82.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=46.84 liquidity=1596646.0 spike=0.21
- FWRY.CA: score=17.8 buy_ready=False sector_rank=4 price=18.77 support=17.5 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.03 liquidity=162070592.0 spike=1.7
- GBCO.CA: score=23.4 buy_ready=False sector_rank=7 price=31.88 support=27.0 resistance=32.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.43 liquidity=71393496.0 spike=0.76
- GDWA.CA: score=8.48 buy_ready=False sector_rank=18 price=0.68 support=0.61 resistance=0.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=26.11 liquidity=13952936.0 spike=0.45
- GGCC.CA: score=9.48 buy_ready=False sector_rank=18 price=0.73 support=0.65 resistance=0.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.85 liquidity=12159842.0 spike=0.78
- GIHD.CA: score=14.48 buy_ready=False sector_rank=18 price=65.2 support=60.9 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=36.25 liquidity=23207722.0 spike=0.84
- GMCI.CA: score=-1.2 buy_ready=False sector_rank=18 price=1.69 support=1.49 resistance=1.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=317455.03 spike=0.67
- GRCA.CA: score=7.57 buy_ready=False sector_rank=18 price=37.96 support=32.11 resistance=63.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=40.92 liquidity=4083940.0 spike=0.16
- GSSC.CA: score=5.08 buy_ready=False sector_rank=18 price=284.47 support=246.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.38 liquidity=597860.56 spike=0.12
- GTWL.CA: score=9.48 buy_ready=False sector_rank=18 price=167.79 support=124.5 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.79 liquidity=108169360.0 spike=0.7
- HDBK.CA: score=17.34 buy_ready=False sector_rank=11 price=110.52 support=102.03 resistance=123.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.9 liquidity=10929962.0 spike=0.3
- HELI.CA: score=13.9 buy_ready=False sector_rank=19 price=7.49 support=6.94 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.24 liquidity=69910432.0 spike=0.57
- HRHO.CA: score=26.57 buy_ready=False sector_rank=10 price=26.15 support=22.81 resistance=26.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.39 liquidity=447388096.0 spike=4.65
- ICID.CA: score=22.48 buy_ready=False sector_rank=18 price=18.06 support=16.52 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.44 liquidity=26339942.0 spike=3.92
- IDRE.CA: score=10.6 buy_ready=False sector_rank=18 price=50.97 support=45.0 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.03 liquidity=6111588.5 spike=0.41
- IFAP.CA: score=7.45 buy_ready=False sector_rank=12 price=19.67 support=17.17 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=43.78 liquidity=2209400.0 spike=0.15
- INFI.CA: score=10.63 buy_ready=False sector_rank=18 price=125.07 support=104.0 resistance=152.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.19 liquidity=6145696.0 spike=0.44
- IRON.CA: score=10.67 buy_ready=False sector_rank=15 price=29.26 support=25.01 resistance=30.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.59 liquidity=2969656.0 spike=0.23
- ISMA.CA: score=10.0 buy_ready=False sector_rank=18 price=26.37 support=22.7 resistance=34.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.53 liquidity=5519680.5 spike=0.39
- ISMQ.CA: score=14.7 buy_ready=False sector_rank=15 price=8.31 support=7.6 resistance=9.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.8 liquidity=20996778.0 spike=0.97
- ISPH.CA: score=14.87 buy_ready=False sector_rank=13 price=11.85 support=11.22 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.35 liquidity=51193988.0 spike=0.7
- JUFO.CA: score=12.52 buy_ready=False sector_rank=20 price=25.58 support=24.4 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.79 liquidity=11389728.0 spike=0.61
- KABO.CA: score=16.39 buy_ready=False sector_rank=9 price=8.9 support=7.97 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.22 liquidity=41656284.0 spike=1.27
- KWIN.CA: score=9.51 buy_ready=False sector_rank=18 price=78.71 support=72.21 resistance=102.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.55 liquidity=5030108.5 spike=0.36
- KZPC.CA: score=12.71 buy_ready=False sector_rank=18 price=12.84 support=12.15 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=37.17 liquidity=5223916.0 spike=0.19
- LCSW.CA: score=21.1 buy_ready=False sector_rank=8 price=33.54 support=28.86 resistance=35.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.17 liquidity=22751282.0 spike=1.5
- LUTS.CA: score=21.48 buy_ready=False sector_rank=18 price=0.93 support=0.72 resistance=1.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.13 liquidity=74256376.0 spike=0.83
- MAAL.CA: score=19.48 buy_ready=False sector_rank=18 price=10.69 support=8.18 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=72.32 liquidity=18983856.0 spike=0.85
- MASR.CA: score=14.48 buy_ready=False sector_rank=18 price=7.7 support=6.82 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.5 liquidity=38525040.0 spike=0.49
- MBSC.CA: score=11.1 buy_ready=False sector_rank=8 price=401.44 support=350.04 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=470803072.0 spike=10.31
- MCQE.CA: score=11.1 buy_ready=False sector_rank=8 price=207.86 support=203.13 resistance=219.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=244416416.0 spike=8.73
- MCRO.CA: score=14.48 buy_ready=False sector_rank=18 price=1.54 support=1.41 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.85 liquidity=86332032.0 spike=0.8
- MENA.CA: score=3.53 buy_ready=False sector_rank=19 price=6.68 support=6.31 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4635941.5 spike=4.45
- MEPA.CA: score=10.67 buy_ready=False sector_rank=18 price=1.77 support=1.56 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=6189105.0 spike=0.27
- MFPC.CA: score=17.7 buy_ready=False sector_rank=15 price=46.39 support=43.0 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.71 liquidity=52346144.0 spike=0.43
- MFSC.CA: score=6.34 buy_ready=False sector_rank=18 price=46.14 support=42.5 resistance=50.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=49.2 liquidity=1852644.0 spike=0.64
- MHOT.CA: score=11.09 buy_ready=False sector_rank=21 price=17.39 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.47 liquidity=9060143.0 spike=0.5
- MICH.CA: score=13.33 buy_ready=False sector_rank=18 price=46.09 support=42.01 resistance=52.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.72 liquidity=8841518.0 spike=0.82
- MILS.CA: score=13.75 buy_ready=False sector_rank=18 price=182.68 support=165.5 resistance=232.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.45 liquidity=9263425.0 spike=0.5
- MIPH.CA: score=9.11 buy_ready=False sector_rank=13 price=811.22 support=739.69 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=51.38 liquidity=1240500.0 spike=0.14
- MOED.CA: score=8.48 buy_ready=False sector_rank=18 price=0.7 support=0.59 resistance=0.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.63 liquidity=28305388.0 spike=0.7
- MOIL.CA: score=6.52 buy_ready=False sector_rank=6 price=0.7 support=0.67 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=75.86 liquidity=115338.87 spike=0.44
- MOIN.CA: score=18.02 buy_ready=False sector_rank=18 price=35.71 support=32.0 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.03 liquidity=24655884.0 spike=1.27
- MOSC.CA: score=14.21 buy_ready=False sector_rank=18 price=285.16 support=257.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.18 liquidity=7563997.0 spike=2.08
- MPCI.CA: score=14.48 buy_ready=False sector_rank=18 price=356.7 support=305.45 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.26 liquidity=89530856.0 spike=0.82
- MPCO.CA: score=18.24 buy_ready=False sector_rank=12 price=2.47 support=2.18 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.38 liquidity=82110288.0 spike=0.43
- MPRC.CA: score=18.48 buy_ready=False sector_rank=18 price=40.87 support=37.65 resistance=42.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=60.48 liquidity=17381012.0 spike=0.71
- MTIE.CA: score=17.4 buy_ready=False sector_rank=7 price=8.08 support=7.5 resistance=8.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.83 liquidity=14819181.0 spike=0.76
- NAHO.CA: score=4.49 buy_ready=False sector_rank=18 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.87 liquidity=8107.73 spike=0.2
- NCCW.CA: score=17.48 buy_ready=False sector_rank=18 price=7.21 support=6.22 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.28 liquidity=32077274.0 spike=0.42
- NEDA.CA: score=4.78 buy_ready=False sector_rank=18 price=2.61 support=2.48 resistance=2.89 source=Yahoo Finance as_of=2026-10-03T21:00:00+00:00 freshness=FRESH RSI=35.71 liquidity=293390.09 spike=0.31
- NHPS.CA: score=10.05 buy_ready=False sector_rank=18 price=73.95 support=66.0 resistance=88.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.46 liquidity=5562590.0 spike=0.37
- NINH.CA: score=12.35 buy_ready=False sector_rank=18 price=19.39 support=18.53 resistance=24.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.8 liquidity=7864053.5 spike=0.51
- NIPH.CA: score=14.87 buy_ready=False sector_rank=13 price=323.14 support=290.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.83 liquidity=110118464.0 spike=0.87
- OBRI.CA: score=15.14 buy_ready=False sector_rank=18 price=28.99 support=22.8 resistance=33.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.39 liquidity=21974648.0 spike=1.83
- OCDI.CA: score=8.9 buy_ready=False sector_rank=19 price=27.49 support=24.2 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.89 liquidity=48638060.0 spike=0.96
- OCPH.CA: score=6.95 buy_ready=False sector_rank=18 price=229.11 support=190.0 resistance=263.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.42 liquidity=1467791.38 spike=0.31
- ODIN.CA: score=12.14 buy_ready=False sector_rank=18 price=2.56 support=2.35 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.27 liquidity=7654014.5 spike=0.75
- OFH.CA: score=14.48 buy_ready=False sector_rank=18 price=0.91 support=0.83 resistance=1.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.78 liquidity=37839040.0 spike=0.31
- OIH.CA: score=12.4 buy_ready=False sector_rank=3 price=1.89 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=24.53 liquidity=91849176.0 spike=0.83
- OLFI.CA: score=12.8 buy_ready=False sector_rank=20 price=21.24 support=21.2 resistance=23.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.38 liquidity=17284912.0 spike=1.14
- ORAS.CA: score=4.6 buy_ready=False sector_rank=17 price=826.71 support=814.0 resistance=835.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=69163824.0 spike=1.0
- ORHD.CA: score=8.9 buy_ready=False sector_rank=19 price=38.7 support=37.41 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=34.67 liquidity=110227984.0 spike=0.7
- ORWE.CA: score=18.85 buy_ready=False sector_rank=9 price=27.39 support=26.01 resistance=29.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.59 liquidity=24933300.0 spike=0.58
- PHAR.CA: score=14.87 buy_ready=False sector_rank=13 price=113.98 support=102.0 resistance=132.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.46 liquidity=40169076.0 spike=0.49
- PHDC.CA: score=8.9 buy_ready=False sector_rank=19 price=13.18 support=12.36 resistance=15.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.92 liquidity=66117676.0 spike=0.56
- PHTV.CA: score=5.31 buy_ready=False sector_rank=18 price=336.55 support=315.1 resistance=378.89 source=Yahoo Finance as_of=2026-10-03T21:00:00+00:00 freshness=FRESH RSI=44.07 liquidity=829259.17 spike=0.56
- POUL.CA: score=7.52 buy_ready=False sector_rank=20 price=10.08 support=9.12 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=4.93 liquidity=25506480.0 spike=0.76
- PRCL.CA: score=11.05 buy_ready=False sector_rank=8 price=26.08 support=22.8 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.52 liquidity=9948251.0 spike=0.75
- PRDC.CA: score=8.9 buy_ready=False sector_rank=19 price=7.37 support=7.25 resistance=7.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=207127824.0 spike=7.34
- PRMH.CA: score=11.34 buy_ready=False sector_rank=18 price=2.29 support=2.03 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.3 liquidity=6054538.5 spike=1.4
- RACC.CA: score=10.97 buy_ready=False sector_rank=18 price=9.31 support=8.51 resistance=10.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.8 liquidity=6481672.5 spike=0.83
- RAKT.CA: score=14.87 buy_ready=False sector_rank=18 price=22.77 support=20.26 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=39.55 liquidity=1384144.25 spike=7.21
- RAYA.CA: score=14.61 buy_ready=False sector_rank=16 price=6.62 support=5.72 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=23797614.0 spike=0.6
- RMDA.CA: score=9.87 buy_ready=False sector_rank=13 price=5.47 support=4.83 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.03 liquidity=15474256.0 spike=0.32
- ROTO.CA: score=9.76 buy_ready=False sector_rank=18 price=39.53 support=35.02 resistance=44.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.73 liquidity=5271576.0 spike=0.68
- RREI.CA: score=15.26 buy_ready=False sector_rank=18 price=4.05 support=3.53 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.69 liquidity=16560984.0 spike=1.39
- RTVC.CA: score=1.74 buy_ready=False sector_rank=18 price=3.66 support=3.37 resistance=4.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=32.67 liquidity=2953735.75 spike=1.15
- RUBX.CA: score=22.2 buy_ready=False sector_rank=18 price=16.47 support=12.63 resistance=18.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.05 liquidity=99135520.0 spike=1.36
- SAUD.CA: score=15.68 buy_ready=False sector_rank=11 price=23.29 support=21.6 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=56.27 liquidity=7339491.0 spike=0.37
- SCEM.CA: score=16.74 buy_ready=False sector_rank=8 price=87.48 support=74.55 resistance=104.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.39 liquidity=87560296.0 spike=1.32
- SCFM.CA: score=5.19 buy_ready=False sector_rank=18 price=251.31 support=223.11 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.02 liquidity=1708626.38 spike=0.3
- SCTS.CA: score=4.51 buy_ready=False sector_rank=2 price=562.91 support=520.3 resistance=639.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=32.42 liquidity=1114330.13 spike=0.57
- SDTI.CA: score=16.48 buy_ready=False sector_rank=18 price=83.76 support=70.0 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=75.52 liquidity=18411166.0 spike=0.55
- SEIG.CA: score=10.52 buy_ready=False sector_rank=18 price=242.52 support=200.0 resistance=267.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.7 liquidity=2799953.0 spike=1.62
- SIPC.CA: score=17.88 buy_ready=False sector_rank=18 price=5.5 support=4.22 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.13 liquidity=70421120.0 spike=1.2
- SKPC.CA: score=8.7 buy_ready=False sector_rank=15 price=16.4 support=15.4 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.92 liquidity=98767936.0 spike=0.99
- SMFR.CA: score=5.83 buy_ready=False sector_rank=18 price=224.44 support=205.01 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=41.78 liquidity=1347284.75 spike=0.21
- SNFC.CA: score=18.6 buy_ready=False sector_rank=18 price=11.61 support=10.58 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=65.71 liquidity=7118202.0 spike=0.55
- SPIN.CA: score=9.07 buy_ready=False sector_rank=9 price=16.86 support=15.11 resistance=19.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=37.09 liquidity=3222282.75 spike=0.46
- SPMD.CA: score=7.65 buy_ready=False sector_rank=18 price=0.39 support=0.36 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.44 liquidity=9166812.0 spike=0.12
- SUGR.CA: score=13.52 buy_ready=False sector_rank=20 price=54.41 support=50.5 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.62 liquidity=16235466.0 spike=0.77
- SVCE.CA: score=14.48 buy_ready=False sector_rank=18 price=10.75 support=9.24 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.78 liquidity=122148288.0 spike=0.94
- SWDY.CA: score=17.73 buy_ready=False sector_rank=14 price=118.96 support=102.31 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.92 liquidity=45534640.0 spike=0.63
- TALM.CA: score=24.5 buy_ready=False sector_rank=2 price=21.84 support=17.61 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.94 liquidity=103010936.0 spike=1.55
- TMGH.CA: score=7.9 buy_ready=False sector_rank=19 price=88.92 support=84.4 resistance=100.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.91 liquidity=200094656.0 spike=0.81
- TRTO.CA: score=-2.55 buy_ready=False sector_rank=18 price=0.06 support=0.06 resistance=0.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30845.05 spike=2.47
- UEFM.CA: score=8.82 buy_ready=False sector_rank=18 price=499.92 support=407.57 resistance=574.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.11 liquidity=2331483.0 spike=0.6
- UEGC.CA: score=16.48 buy_ready=False sector_rank=18 price=1.6 support=1.37 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.62 liquidity=26243664.0 spike=0.76
- UNIP.CA: score=14.04 buy_ready=False sector_rank=18 price=0.36 support=0.32 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.21 liquidity=9554819.0 spike=0.68
- UNIT.CA: score=3.59 buy_ready=False sector_rank=19 price=17.8 support=16.41 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=20.15 liquidity=4693517.0 spike=0.31
- WCDF.CA: score=8.78 buy_ready=False sector_rank=18 price=654.96 support=575.5 resistance=796.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.16 liquidity=1299903.13 spike=0.25
- WKOL.CA: score=2.64 buy_ready=False sector_rank=18 price=293.11 support=266.18 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=29.89 liquidity=4160219.0 spike=0.31
- ZEOT.CA: score=10.87 buy_ready=False sector_rank=18 price=13.1 support=10.6 resistance=14.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=49.09 liquidity=4381354.5 spike=0.75
- ZMID.CA: score=8.9 buy_ready=False sector_rank=19 price=7.63 support=7.07 resistance=9.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.39 liquidity=55070180.0 spike=0.45

## Backtesting Lite
- HRHO.CA: 180d return=1.94%, max drawdown=-22.96%, MA20>MA50 days last20=0, as_of=2026-10-03T21:00:00+00:00
- AJWA.CA: 180d return=53.74%, max drawdown=-15.08%, MA20>MA50 days last20=5, as_of=2026-10-03T21:00:00+00:00
- EFIH.CA: 180d return=13.91%, max drawdown=-22.68%, MA20>MA50 days last20=12, as_of=2026-10-03T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- HRHO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=EFG Holding summary=Evidence rejected for HRHO.CA: source text did not clearly match HRHO.CA / EFG Holding.
- AJWA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=AJWA For Food Industries Co. Egypt summary=Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture; AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3; Ajwa Egypt turns to losses in 9M
  - Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture: https://english.mubasher.info/news/4532004/Ajwa-Egypt-s-board-approves-capital-increase-to-EGP-500m-joins-new-food-venture/
  - AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3: https://english.mubasher.info/news/4527545/AJWA-Egypt-s-standalone-net-profits-retreat-to-EGP-14m-in-9M-25-amid-shift-to-profitability-in-Q3/
  - Ajwa Egypt turns to losses in 9M: https://english.mubasher.info/news/3883210/Ajwa-Egypt-turns-to-losses-in-9M/
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- CIRA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Investment and Real Estate Development summary=CIRA Education take over 51% of L’École Française Hurghada; CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion; CIRA Education launches Middle East’s 1st initiative for care economy
  - CIRA Education take over 51% of L’École Française Hurghada: https://english.mubasher.info/news/4488666/CIRA-Education-take-over-51-of-L-%C3%89cole-Fran%C3%A7aise-Hurghada/
  - CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion: https://english.mubasher.info/news/4393636/CIRA-s-majority-shareholder-acquires-37-5-additional-equity-backs-regional-expansion/
  - CIRA Education launches Middle East’s 1st initiative for care economy: https://english.mubasher.info/news/4391766/CIRA-Education-launches-Middle-East-s-1st-initiative-for-care-economy/
- ARCC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=642 sources=3 expected=Arabian Cement Company summary=Arabian Cement to pay out EGP 2bn dividends for 2025; Arabian Cement’s EGM approves nearly EGP 8m capital cut; Arabian Cement’s consolidated profits near EGP 3.6bn in 2025
  - Arabian Cement to pay out EGP 2bn dividends for 2025: https://english.mubasher.info/news/4587912/Arabian-Cement-to-pay-out-EGP-2bn-dividends-for-2025/
  - Arabian Cement’s EGM approves nearly EGP 8m capital cut: https://english.mubasher.info/news/4583762/Arabian-Cement-s-EGM-approves-nearly-EGP-8m-capital-cut/
  - Arabian Cement’s consolidated profits near EGP 3.6bn in 2025: https://english.mubasher.info/news/4562679/Arabian-Cement-s-consolidated-profits-near-EGP-3-6bn-in-2025/
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.

## Warnings
- Evidence rejected for HRHO.CA: source text did not clearly match HRHO.CA / EFG Holding.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for AJWA.CA matches the company but no source/report date was detected.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
- Evidence for ARCC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
