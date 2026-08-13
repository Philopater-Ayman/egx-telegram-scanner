# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-08-13T09:13:20.749334+00:00
Generated Cairo: 2026-08-13 12:13
Run timing: target 11:00 Cairo | generated Cairo 2026-08-13 12:13 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-08-13 12:06

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 59
- Data quality issues: 1
- Tradeable price/liquidity tickers: 178/189
- Top sector: Building Materials

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, August 13
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 70.0% / above MA50 85.0%
- EGX70 regime: BULLISH / above MA20 80.0% / above MA50 90.0%
- Sector breadth: 71.43%
- Risk mode: BROAD_RISK_ON

## Top Liquidity
- PHAR.CA: liquidity=611426688.0 spike=1.7 score=29.3
- NIPH.CA: liquidity=370366048.0 spike=1.66 score=28.22
- BIOC.CA: liquidity=270243264.0 spike=1.5 score=25.9
- COSG.CA: liquidity=229798560.0 spike=6.11 score=15.9
- ORAS.CA: liquidity=217781968.0 spike=1.0 score=9.1

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner prioritized Building Materials names (SCEM.CA, MBSC.CA, MCQE.CA) due to strong liquidity spikes, sector leadership, and bullish outlook, while the broader EGX30/EGX70 bullish breadth keeps risk mode broad risk‑on; uncertainty remains from extended momentum and overheated RSI.
- Liquidity & sector: Building Materials shows the highest liquidity spikes and sector strength, driving the top tickets.
- Outlook & technical: Most flagged stocks have a BULLISH_WATCH outlook but sit far above 20‑day support and near resistance, limiting near‑term upside.
- Market regime: EGX30 and EGX70 are both BULLISH with >70% above MA20, shifting risk mode to BROAD_RISK_ON, which favors buying but also raises caution.
- Uncertainty: Several names display overheated RSI (e.g., MBSC.CA >95) and cooling liquidity, increasing pull‑back risk and keeping confidence low.

## Top Liquidity Spikes
- COSG.CA: spike=6.11 liquidity=229798560.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ICID.CA: spike=5.4 liquidity=53223724.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- TRTO.CA: spike=4.76 liquidity=7752.43 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MOSC.CA: spike=2.86 liquidity=48155108.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- KZPC.CA: spike=2.85 liquidity=25172702.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Building Materials: score=24.05 5d=22.23% 20d=42.28% aboveMA50=100.0%
- #2 Healthcare: score=14.7 5d=6.91% 20d=25.39% aboveMA50=100.0%
- #3 Transportation & Logistics: score=13.88 5d=9.03% 20d=18.98% aboveMA50=100.0%
- #4 Tourism & Leisure: score=13.4 5d=14.34% 20d=18.28% aboveMA50=0.0%
- #5 Agriculture & Food Production: score=12.69 5d=8.64% 20d=14.26% aboveMA50=100.0%
- #6 Education: score=12.04 5d=4.13% 20d=20.24% aboveMA50=100.0%
- #7 Textiles: score=10.28 5d=2.73% 20d=14.54% aboveMA50=100.0%
- #8 Basic Resources & Chemicals: score=8.14 5d=2.88% 20d=4.61% aboveMA50=90.0%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CLHO.CA: BULLISH_WATCH score=100 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- MFPC.CA: BULLISH_WATCH score=90.14 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- MCQE.CA: BULLISH_WATCH score=89 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support
- FAIT.CA: BULLISH_WATCH score=88.76 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- SPIN.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- SCTS.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MBSC.CA: BULLISH_WATCH score=83 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support
- NIPH.CA: BULLISH_WATCH score=83 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support; high short-term volatility
- DOMT.CA: BULLISH_WATCH score=82.08 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- MENA.CA: BULLISH_WATCH score=78.44 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended; sector is not leading

## BUY-Ready Candidates
- SCEM.CA: rank=30.9 outlook=BULLISH_WATCH outlook_score=78 sector_rank=1 price=96.02 support=61.97 resistance=113.0 liquidity=133402960.0
- ABUK.CA: rank=30.02 outlook=BULLISH_WATCH outlook_score=78.14 sector_rank=8 price=77.97 support=70.6 resistance=75.59 liquidity=156474032.0
- ADPC.CA: rank=29.9 outlook=CONSTRUCTIVE outlook_score=69.8 sector_rank=13 price=4.55 support=3.76 resistance=4.55 liquidity=29530452.0
- PRMH.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=77.8 sector_rank=13 price=2.76 support=2.56 resistance=2.93 liquidity=11047556.0
- DOMT.CA: rank=29.68 outlook=BULLISH_WATCH outlook_score=82.08 sector_rank=9 price=30.0 support=26.01 resistance=32.0 liquidity=24148822.0
- MFPC.CA: rank=29.46 outlook=BULLISH_WATCH outlook_score=90.14 sector_rank=8 price=39.6 support=35.37 resistance=38.8 liquidity=142330048.0
- ETEL.CA: rank=28.03 outlook=CONSTRUCTIVE outlook_score=62.42 sector_rank=18 price=112.9 support=97.0 resistance=114.87 liquidity=145750928.0
- SAUD.CA: rank=27.9 outlook=BULLISH_WATCH outlook_score=71.76 sector_rank=14 price=23.28 support=21.3 resistance=23.25 liquidity=11632313.0
- EMFD.CA: rank=27.9 outlook=BULLISH_WATCH outlook_score=72.44 sector_rank=11 price=11.84 support=11.08 resistance=12.12 liquidity=20298374.0
- ORHD.CA: rank=27.9 outlook=CONSTRUCTIVE outlook_score=58.44 sector_rank=11 price=42.96 support=38.0 resistance=44.0 liquidity=44584704.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=25.9 buy_ready=True sector_rank=13 price=293.24 support=227.0 resistance=325.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=68.45 liquidity=14550438.0 spike=0.37
- ABUK.CA: score=30.02 buy_ready=True sector_rank=8 price=77.97 support=70.6 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=62.91 liquidity=156474032.0 spike=1.06
- ACAMD.CA: score=20.9 buy_ready=False sector_rank=13 price=2.24 support=2.2 resistance=2.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=40.64 liquidity=12460563.0 spike=0.2
- ACGC.CA: score=20.3 buy_ready=False sector_rank=7 price=11.99 support=9.75 resistance=12.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=75.12 liquidity=5400124.5 spike=0.16
- ADCI.CA: score=23.45 buy_ready=True sector_rank=13 price=312.72 support=234.1 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=63.92 liquidity=5550916.5 spike=0.25
- ADIB.CA: score=24.9 buy_ready=False sector_rank=14 price=54.04 support=46.02 resistance=54.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=79.8 liquidity=17493344.0 spike=0.15
- ADPC.CA: score=29.9 buy_ready=True sector_rank=13 price=4.55 support=3.76 resistance=4.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=61.87 liquidity=29530452.0 spike=0.59
- AFDI.CA: score=16.91 buy_ready=False sector_rank=13 price=66.91 support=46.4 resistance=69.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=83.78 liquidity=4008588.5 spike=0.16
- AFMC.CA: score=22.9 buy_ready=False sector_rank=13 price=239.87 support=73.75 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=75.96 liquidity=36479044.0 spike=0.23
- AJWA.CA: score=25.9 buy_ready=False sector_rank=13 price=195.42 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=74.42 liquidity=12224642.0 spike=0.32
- ALCN.CA: score=22.38 buy_ready=False sector_rank=3 price=31.51 support=28.8 resistance=32.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=72.19 liquidity=3481605.25 spike=0.13
- ALUM.CA: score=24.9 buy_ready=False sector_rank=13 price=28.97 support=22.7 resistance=30.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=85.35 liquidity=10394451.0 spike=0.59
- AMER.CA: score=22.9 buy_ready=False sector_rank=11 price=6.59 support=3.18 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=83.76 liquidity=59186772.0 spike=0.52
- AMES.CA: score=18.81 buy_ready=False sector_rank=13 price=120.53 support=106.59 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=49.19 liquidity=4914313.5 spike=0.06
- AMIA.CA: score=20.68 buy_ready=False sector_rank=13 price=12.7 support=8.81 resistance=13.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=79.04 liquidity=7778846.0 spike=0.45
- AMOC.CA: score=26.1 buy_ready=False sector_rank=10 price=9.88 support=8.13 resistance=9.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=72.52 liquidity=110337232.0 spike=1.1
- APSW.CA: score=13.6 buy_ready=False sector_rank=13 price=8.72 support=8.32 resistance=9.34 source=Yahoo Finance as_of=2026-08-11T21:00:00+00:00 freshness=FRESH RSI=43.54 liquidity=700460.18 spike=0.4
- ARAB.CA: score=23.9 buy_ready=False sector_rank=11 price=0.24 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=62.26 liquidity=19210714.0 spike=0.17
- ARCC.CA: score=26.86 buy_ready=False sector_rank=1 price=74.07 support=54.2 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=86.05 liquidity=124062272.0 spike=1.48
- AREH.CA: score=15.94 buy_ready=False sector_rank=13 price=1.51 support=1.38 resistance=1.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=3044491.5 spike=0.08
- ARVA.CA: score=4.9 buy_ready=False sector_rank=13 price=12.35 support=12.35 resistance=12.35 source=Yahoo Finance as_of=2026-08-11T21:00:00+00:00 freshness=FRESH RSI=87.23 liquidity=0.0 spike=0.0
- ASCM.CA: score=23.9 buy_ready=True sector_rank=13 price=65.73 support=60.1 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=67.06 liquidity=11990643.0 spike=0.2
- ASPI.CA: score=19.9 buy_ready=False sector_rank=13 price=0.49 support=0.31 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=74.18 liquidity=4003322.25 spike=0.09
- ATLC.CA: score=18.18 buy_ready=True sector_rank=16 price=5.63 support=5.0 resistance=5.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=2488139.5 spike=0.14
- ATQA.CA: score=22.9 buy_ready=False sector_rank=8 price=10.85 support=9.49 resistance=11.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=76.89 liquidity=17956726.0 spike=0.32
- AXPH.CA: score=17.46 buy_ready=True sector_rank=13 price=1309.28 support=1121.56 resistance=1460.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT RSI=67.46 liquidity=1562620.63 spike=0.33
- BINV.CA: score=17.31 buy_ready=True sector_rank=15 price=49.0 support=46.01 resistance=50.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=67.31 liquidity=3407633.5 spike=0.49
- BIOC.CA: score=25.9 buy_ready=False sector_rank=13 price=507.65 support=73.23 resistance=560.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=84.81 liquidity=270243264.0 spike=1.5
- BTFH.CA: score=23.7 buy_ready=False sector_rank=16 price=3.1 support=3.03 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=24852024.0 spike=0.11
- CAED.CA: score=25.9 buy_ready=True sector_rank=13 price=131.31 support=93.2 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=57.62 liquidity=18705828.0 spike=0.26
- CANA.CA: score=10.9 buy_ready=False sector_rank=14 price=42.8 support=40.45 resistance=42.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12532236.0 spike=0.63
- CCAP.CA: score=23.9 buy_ready=False sector_rank=15 price=5.33 support=5.14 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=41.35 liquidity=90952104.0 spike=0.15
- CCRS.CA: score=9.97 buy_ready=False sector_rank=13 price=2.55 support=2.44 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=30.77 liquidity=1066860.88 spike=0.05
- CEFM.CA: score=17.62 buy_ready=True sector_rank=13 price=135.14 support=103.01 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=61.24 liquidity=1722144.0 spike=0.05
- CERA.CA: score=25.9 buy_ready=True sector_rank=13 price=1.35 support=1.25 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=12337283.0 spike=0.61
- CFGH.CA: score=9.92 buy_ready=False sector_rank=13 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 August 12:57 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=15552.25 spike=0.86
- CICH.CA: score=18.73 buy_ready=True sector_rank=16 price=12.64 support=11.77 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=55.31 liquidity=1033676.69 spike=0.13
- CIEB.CA: score=21.17 buy_ready=False sector_rank=14 price=24.11 support=23.75 resistance=24.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=46.95 liquidity=7266894.5 spike=0.65
- CIRA.CA: score=22.9 buy_ready=False sector_rank=6 price=38.69 support=30.91 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=75.82 liquidity=31248318.0 spike=0.52
- CLHO.CA: score=27.9 buy_ready=True sector_rank=2 price=17.2 support=16.0 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=57.91 liquidity=44926152.0 spike=0.85
- CNFN.CA: score=21.57 buy_ready=True sector_rank=16 price=4.94 support=4.68 resistance=5.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=60.78 liquidity=3876906.0 spike=0.17
- COMI.CA: score=23.9 buy_ready=False sector_rank=14 price=139.05 support=132.81 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=49.96 liquidity=42996980.0 spike=0.1
- COPR.CA: score=14.48 buy_ready=False sector_rank=13 price=0.44 support=0.42 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=95033592.0 spike=2.79
- COSG.CA: score=15.9 buy_ready=False sector_rank=13 price=1.84 support=1.73 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=229798560.0 spike=6.11
- CPCI.CA: score=20.0 buy_ready=False sector_rank=13 price=537.71 support=430.03 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=73.04 liquidity=4103198.0 spike=0.27
- CSAG.CA: score=25.9 buy_ready=False sector_rank=3 price=42.09 support=31.35 resistance=42.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=82.45 liquidity=11780076.0 spike=0.5
- DAPH.CA: score=22.9 buy_ready=False sector_rank=13 price=126.45 support=82.77 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=82.11 liquidity=10075136.0 spike=0.26
- DEIN.CA: score=0.9 buy_ready=False sector_rank=13 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=29.68 buy_ready=True sector_rank=9 price=30.0 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=64.34 liquidity=24148822.0 spike=1.89
- DSCW.CA: score=24.9 buy_ready=False sector_rank=13 price=2.16 support=1.84 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=82.86 liquidity=15004997.0 spike=0.15
- DTPP.CA: score=24.9 buy_ready=False sector_rank=13 price=315.45 support=201.21 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=83.94 liquidity=19468412.0 spike=0.31
- EALR.CA: score=24.6 buy_ready=True sector_rank=13 price=386.71 support=360.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=61.79 liquidity=6695907.5 spike=0.21
- EASB.CA: score=16.73 buy_ready=False sector_rank=13 price=7.39 support=6.71 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=19.3 liquidity=5832786.5 spike=0.56
- EAST.CA: score=16.9 buy_ready=False sector_rank=9 price=36.6 support=36.01 resistance=37.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=34.55 liquidity=13456872.0 spike=0.2
- EBSC.CA: score=18.67 buy_ready=False sector_rank=13 price=1.92 support=1.85 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=58.06 liquidity=767664.69 spike=0.13
- ECAP.CA: score=18.67 buy_ready=False sector_rank=13 price=38.79 support=32.12 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=75.12 liquidity=5767592.5 spike=0.52
- EDFM.CA: score=18.23 buy_ready=False sector_rank=13 price=413.95 support=349.02 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=68.63 liquidity=334309.31 spike=0.06
- EEII.CA: score=30.32 buy_ready=False sector_rank=13 price=3.06 support=2.54 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=72.28 liquidity=38627156.0 spike=2.21
- EFIC.CA: score=20.28 buy_ready=True sector_rank=8 price=212.96 support=184.0 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=69.62 liquidity=4377956.5 spike=0.16
- EFID.CA: score=24.9 buy_ready=False sector_rank=9 price=32.23 support=26.64 resistance=32.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=83.18 liquidity=23698808.0 spike=0.28
- EFIH.CA: score=25.52 buy_ready=True sector_rank=17 price=23.98 support=21.9 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=51.88 liquidity=58846360.0 spike=0.59
- EGAL.CA: score=24.9 buy_ready=False sector_rank=8 price=332.47 support=292.0 resistance=358.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=80.01 liquidity=59059228.0 spike=0.65
- EGAS.CA: score=19.87 buy_ready=False sector_rank=10 price=60.53 support=50.0 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=78.17 liquidity=6969844.5 spike=0.25
- EGBE.CA: score=15.94 buy_ready=False sector_rank=14 price=0.55 support=0.44 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=63.98 liquidity=35795.66 spike=0.22
- EGCH.CA: score=22.9 buy_ready=False sector_rank=8 price=14.4 support=12.69 resistance=14.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=75.46 liquidity=36632568.0 spike=0.33
- EGSA.CA: score=5.27 buy_ready=False sector_rank=18 price=8.65 support=8.67 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=19.15 liquidity=6664.14 spike=0.32
- EGTS.CA: score=22.87 buy_ready=False sector_rank=11 price=19.02 support=17.11 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=70.9 liquidity=6973002.5 spike=0.18
- EHDR.CA: score=27.9 buy_ready=True sector_rank=13 price=3.05 support=2.69 resistance=3.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=11437047.0 spike=0.24
- EKHO.CA: score=9.9 buy_ready=False sector_rank=10 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-11T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=18.72 buy_ready=False sector_rank=12 price=2.19 support=2.12 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=5819870.0 spike=0.07
- ELKA.CA: score=18.9 buy_ready=False sector_rank=13 price=1.78 support=1.69 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=26.32 liquidity=12547984.0 spike=0.15
- ELNA.CA: score=5.12 buy_ready=False sector_rank=13 price=37.88 support=36.5 resistance=39.49 source=Yahoo Finance as_of=2026-08-11T21:00:00+00:00 freshness=FRESH RSI=33.57 liquidity=222204.09 spike=0.46
- ELSH.CA: score=22.43 buy_ready=False sector_rank=13 price=14.04 support=13.31 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=35.89 liquidity=8525078.0 spike=0.09
- ELWA.CA: score=6.3 buy_ready=False sector_rank=13 price=1.75 support=1.65 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=29.73 liquidity=396183.34 spike=0.25
- EMFD.CA: score=27.9 buy_ready=True sector_rank=11 price=11.84 support=11.08 resistance=12.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=50.57 liquidity=20298374.0 spike=0.35
- ENGC.CA: score=16.93 buy_ready=False sector_rank=13 price=49.24 support=40.11 resistance=51.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=75.13 liquidity=4027974.5 spike=0.15
- EOSB.CA: score=19.93 buy_ready=False sector_rank=13 price=1.55 support=1.52 resistance=1.62 source=Yahoo Finance as_of=2026-08-11T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=28405.3 spike=0.58
- EPCO.CA: score=24.74 buy_ready=True sector_rank=13 price=12.14 support=10.11 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=61.69 liquidity=6836187.0 spike=0.2
- EPPK.CA: score=6.7 buy_ready=False sector_rank=13 price=12.77 support=12.62 resistance=15.93 source=Yahoo Finance as_of=2026-08-11T21:00:00+00:00 freshness=FRESH RSI=19.53 liquidity=798674.14 spike=0.93
- ETEL.CA: score=28.03 buy_ready=True sector_rank=18 price=112.9 support=97.0 resistance=114.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=57.95 liquidity=145750928.0 spike=1.38
- ETRS.CA: score=25.9 buy_ready=True sector_rank=13 price=10.88 support=10.21 resistance=10.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=68.24 liquidity=13749363.0 spike=0.59
- EXPA.CA: score=25.9 buy_ready=True sector_rank=14 price=21.0 support=18.8 resistance=21.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=65.65 liquidity=14313169.0 spike=0.4
- FAIT.CA: score=25.24 buy_ready=True sector_rank=14 price=39.96 support=36.1 resistance=39.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=65.46 liquidity=5737445.5 spike=1.8
- FAITA.CA: score=12.91 buy_ready=False sector_rank=14 price=0.98 support=0.96 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=55.06 liquidity=14731.6 spike=0.33
- FERC.CA: score=24.09 buy_ready=True sector_rank=8 price=82.59 support=75.01 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=63.09 liquidity=6188866.0 spike=0.36
- FWRY.CA: score=23.52 buy_ready=False sector_rank=17 price=19.0 support=18.43 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=42.61 liquidity=43548872.0 spike=0.35
- GBCO.CA: score=21.35 buy_ready=True sector_rank=19 price=31.91 support=29.53 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=56.05 liquidity=4118336.5 spike=0.06
- GDWA.CA: score=14.9 buy_ready=False sector_rank=13 price=0.81 support=0.8 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=16.67 liquidity=10273298.0 spike=0.09
- GGCC.CA: score=25.9 buy_ready=False sector_rank=13 price=1.11 support=0.64 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=72.39 liquidity=30302776.0 spike=0.66
- GIHD.CA: score=23.88 buy_ready=False sector_rank=13 price=68.08 support=48.72 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=76.8 liquidity=8982288.0 spike=0.19
- GMCI.CA: score=14.59 buy_ready=False sector_rank=13 price=1.94 support=1.91 resistance=2.2 source=Yahoo Finance as_of=2026-08-11T21:00:00+00:00 freshness=FRESH RSI=40.0 liquidity=668169.0 spike=1.01
- GRCA.CA: score=12.09 buy_ready=False sector_rank=13 price=55.83 support=51.6 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=30.67 liquidity=3190084.5 spike=0.17
- GSSC.CA: score=17.13 buy_ready=True sector_rank=13 price=280.17 support=258.15 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=60.77 liquidity=1229354.38 spike=0.07
- GTWL.CA: score=12.38 buy_ready=False sector_rank=13 price=131.06 support=125.1 resistance=136.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=150139840.0 spike=1.74
- HDBK.CA: score=23.9 buy_ready=False sector_rank=14 price=86.97 support=76.96 resistance=86.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=72.14 liquidity=21896814.0 spike=0.59
- HELI.CA: score=25.9 buy_ready=True sector_rank=11 price=8.24 support=7.4 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=45.71 liquidity=24056692.0 spike=0.14
- HRHO.CA: score=27.7 buy_ready=True sector_rank=16 price=27.11 support=25.95 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=55.1 liquidity=20129230.0 spike=0.21
- ICID.CA: score=15.9 buy_ready=False sector_rank=13 price=13.2 support=10.6 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=53223724.0 spike=5.4
- IDRE.CA: score=22.06 buy_ready=False sector_rank=13 price=56.71 support=44.52 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=78.18 liquidity=7162982.0 spike=0.25
- IFAP.CA: score=17.96 buy_ready=False sector_rank=5 price=21.82 support=18.96 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=83.86 liquidity=3057473.25 spike=0.14
- INFI.CA: score=22.9 buy_ready=False sector_rank=13 price=159.16 support=100.0 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=85.64 liquidity=28338998.0 spike=0.57
- IRON.CA: score=16.61 buy_ready=False sector_rank=8 price=30.61 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT RSI=47.56 liquidity=4714623.5 spike=0.53
- ISMA.CA: score=19.26 buy_ready=False sector_rank=13 price=35.0 support=27.1 resistance=36.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=83.76 liquidity=4355609.5 spike=0.16
- ISMQ.CA: score=27.9 buy_ready=True sector_rank=8 price=9.68 support=8.96 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=60.1 liquidity=10873658.0 spike=0.16
- ISPH.CA: score=27.9 buy_ready=True sector_rank=2 price=13.78 support=11.2 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=67.91 liquidity=51870892.0 spike=0.29
- JUFO.CA: score=24.9 buy_ready=False sector_rank=9 price=27.41 support=22.78 resistance=30.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=41.82 liquidity=44389840.0 spike=0.8
- KABO.CA: score=19.21 buy_ready=True sector_rank=7 price=8.64 support=7.56 resistance=8.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT RSI=45.29 liquidity=3311823.0 spike=0.09
- KWIN.CA: score=12.43 buy_ready=False sector_rank=13 price=88.34 support=71.25 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=30.49 liquidity=3533812.0 spike=0.06
- KZPC.CA: score=14.6 buy_ready=False sector_rank=13 price=10.1 support=9.63 resistance=10.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25172702.0 spike=2.85
- LCSW.CA: score=26.9 buy_ready=False sector_rank=1 price=33.81 support=30.2 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=52.77 liquidity=10444911.0 spike=0.22
- LUTS.CA: score=24.9 buy_ready=False sector_rank=13 price=0.96 support=0.54 resistance=1.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=89.59 liquidity=41633512.0 spike=0.68
- MAAL.CA: score=17.1 buy_ready=False sector_rank=13 price=8.65 support=8.22 resistance=9.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=3199032.0 spike=0.2
- MASR.CA: score=18.9 buy_ready=False sector_rank=13 price=7.66 support=7.45 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=30.26 liquidity=33748972.0 spike=0.44
- MBSC.CA: score=30.78 buy_ready=False sector_rank=1 price=368.02 support=231.51 resistance=381.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=95.94 liquidity=133423408.0 spike=2.44
- MCQE.CA: score=29.96 buy_ready=False sector_rank=1 price=252.72 support=175.51 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=88.82 liquidity=76397576.0 spike=2.03
- MCRO.CA: score=27.9 buy_ready=True sector_rank=13 price=1.58 support=1.32 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=18915324.0 spike=0.1
- MENA.CA: score=21.09 buy_ready=True sector_rank=11 price=7.25 support=6.83 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=67.29 liquidity=3191661.0 spike=0.54
- MEPA.CA: score=21.0 buy_ready=True sector_rank=13 price=1.89 support=1.65 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=43.48 liquidity=5100995.0 spike=0.08
- MFPC.CA: score=29.46 buy_ready=True sector_rank=8 price=39.6 support=35.37 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=59.2 liquidity=142330048.0 spike=1.78
- MFSC.CA: score=19.33 buy_ready=True sector_rank=13 price=50.23 support=45.95 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=58.58 liquidity=1434902.25 spike=0.12
- MHOT.CA: score=21.9 buy_ready=False sector_rank=4 price=19.55 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=66.75 liquidity=10904461.0 spike=0.67
- MICH.CA: score=20.94 buy_ready=False sector_rank=13 price=48.76 support=37.6 resistance=53.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=71.89 liquidity=5042775.5 spike=0.15
- MILS.CA: score=21.17 buy_ready=True sector_rank=13 price=191.51 support=135.3 resistance=211.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=60.13 liquidity=5267665.0 spike=0.08
- MIPH.CA: score=18.3 buy_ready=False sector_rank=2 price=773.72 support=709.95 resistance=828.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=59.87 liquidity=396401.03 spike=0.08
- MOED.CA: score=14.9 buy_ready=False sector_rank=13 price=0.68 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=28.92 liquidity=10255011.0 spike=0.3
- MOIL.CA: score=10.93 buy_ready=False sector_rank=10 price=0.66 support=0.53 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=76.92 liquidity=30179.13 spike=0.04
- MOIN.CA: score=18.23 buy_ready=False sector_rank=13 price=34.63 support=23.03 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=82.15 liquidity=5328724.0 spike=0.21
- MOSC.CA: score=14.62 buy_ready=False sector_rank=13 price=337.34 support=316.02 resistance=370.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48155108.0 spike=2.86
- MPCI.CA: score=25.9 buy_ready=False sector_rank=13 price=380.83 support=242.02 resistance=460.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=73.25 liquidity=54571580.0 spike=0.37
- MPCO.CA: score=22.9 buy_ready=False sector_rank=5 price=2.21 support=1.82 resistance=2.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=81.36 liquidity=37860752.0 spike=0.37
- MPRC.CA: score=27.9 buy_ready=True sector_rank=13 price=47.11 support=42.02 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=62.57 liquidity=12888053.0 spike=0.48
- MTIE.CA: score=19.23 buy_ready=False sector_rank=19 price=9.75 support=9.98 resistance=9.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=19379688.0 spike=1.0
- NAHO.CA: score=14.71 buy_ready=False sector_rank=13 price=0.1 support=0.1 resistance=0.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:02 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=26691.79 spike=1.39
- NCCW.CA: score=20.48 buy_ready=False sector_rank=13 price=6.03 support=5.67 resistance=7.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=43.37 liquidity=9584603.0 spike=0.27
- NEDA.CA: score=6.99 buy_ready=False sector_rank=13 price=2.71 support=2.7 resistance=3.02 source=Yahoo Finance as_of=2026-08-11T21:00:00+00:00 freshness=FRESH RSI=25.0 liquidity=828888.74 spike=1.13
- NHPS.CA: score=25.9 buy_ready=True sector_rank=13 price=90.97 support=82.1 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=45.89 liquidity=24919168.0 spike=0.36
- NINH.CA: score=19.33 buy_ready=False sector_rank=13 price=22.42 support=17.86 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=54.07 liquidity=5425655.0 spike=0.09
- NIPH.CA: score=28.22 buy_ready=False sector_rank=2 price=409.49 support=186.3 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=86.95 liquidity=370366048.0 spike=1.66
- OBRI.CA: score=10.92 buy_ready=False sector_rank=13 price=32.69 support=31.61 resistance=36.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=31.36 liquidity=6021902.0 spike=0.19
- OCDI.CA: score=24.9 buy_ready=False sector_rank=11 price=35.76 support=26.56 resistance=36.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=88.97 liquidity=67066948.0 spike=0.51
- OCPH.CA: score=20.9 buy_ready=False sector_rank=13 price=298.51 support=225.0 resistance=496.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=39.72 liquidity=20411332.0 spike=0.58
- ODIN.CA: score=26.14 buy_ready=False sector_rank=13 price=3.57 support=2.41 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=37507184.0 spike=1.12
- OFH.CA: score=24.9 buy_ready=False sector_rank=13 price=0.91 support=0.64 resistance=0.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=83.1 liquidity=19598636.0 spike=0.21
- OIH.CA: score=24.9 buy_ready=False sector_rank=15 price=1.76 support=1.41 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=91.89 liquidity=50697608.0 spike=0.47
- OLFI.CA: score=27.9 buy_ready=True sector_rank=9 price=25.49 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=69.39 liquidity=18243994.0 spike=0.45
- ORAS.CA: score=9.1 buy_ready=False sector_rank=20 price=747.33 support=727.0 resistance=761.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=217781968.0 spike=1.0
- ORHD.CA: score=27.9 buy_ready=True sector_rank=11 price=42.96 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=63.81 liquidity=44584704.0 spike=0.27
- ORWE.CA: score=24.9 buy_ready=False sector_rank=7 price=26.62 support=22.5 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=82.5 liquidity=16267535.0 spike=0.22
- PHAR.CA: score=29.3 buy_ready=False sector_rank=2 price=145.7 support=86.0 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=72.1 liquidity=611426688.0 spike=1.7
- PHDC.CA: score=27.9 buy_ready=True sector_rank=11 price=15.3 support=14.32 resistance=15.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=54.26 liquidity=27409352.0 spike=0.12
- PHTV.CA: score=14.32 buy_ready=False sector_rank=13 price=390.91 support=291.51 resistance=447.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=86.61 liquidity=1419913.38 spike=0.55
- POUL.CA: score=21.01 buy_ready=True sector_rank=9 price=39.23 support=36.5 resistance=40.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=58.74 liquidity=3113910.75 spike=0.11
- PRCL.CA: score=19.68 buy_ready=False sector_rank=1 price=34.02 support=32.76 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=41.29 liquidity=2777140.5 spike=0.08
- PRDC.CA: score=17.42 buy_ready=False sector_rank=11 price=9.0 support=8.8 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=32.56 liquidity=8522505.0 spike=0.08
- PRMH.CA: score=29.9 buy_ready=True sector_rank=13 price=2.76 support=2.56 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=64.81 liquidity=11047556.0 spike=0.79
- RACC.CA: score=26.32 buy_ready=True sector_rank=13 price=10.45 support=9.8 resistance=10.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=59.52 liquidity=27774710.0 spike=1.21
- RAKT.CA: score=13.18 buy_ready=False sector_rank=13 price=22.63 support=21.66 resistance=24.0 source=Yahoo Finance as_of=2026-08-11T21:00:00+00:00 freshness=FRESH RSI=49.49 liquidity=380840.26 spike=1.45
- RAYA.CA: score=12.05 buy_ready=False sector_rank=21 price=7.25 support=7.13 resistance=8.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=18.89 liquidity=17626146.0 spike=0.18
- RMDA.CA: score=27.9 buy_ready=False sector_rank=2 price=6.6 support=4.95 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=74.68 liquidity=27046512.0 spike=0.24
- ROTO.CA: score=22.9 buy_ready=False sector_rank=13 price=50.14 support=40.5 resistance=51.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=78.29 liquidity=12119874.0 spike=0.54
- RREI.CA: score=19.73 buy_ready=False sector_rank=13 price=4.56 support=3.72 resistance=4.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=70.18 liquidity=3833516.75 spike=0.06
- RTVC.CA: score=7.03 buy_ready=False sector_rank=13 price=3.79 support=3.73 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=32.53 liquidity=1134788.0 spike=0.21
- RUBX.CA: score=20.75 buy_ready=False sector_rank=13 price=12.6 support=12.02 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=37.9 liquidity=6848101.0 spike=0.2
- SAUD.CA: score=27.9 buy_ready=True sector_rank=14 price=23.28 support=21.3 resistance=23.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT RSI=65.57 liquidity=11632313.0 spike=0.74
- SCEM.CA: score=30.9 buy_ready=True sector_rank=1 price=96.02 support=61.97 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=62.49 liquidity=133402960.0 spike=0.79
- SCFM.CA: score=18.83 buy_ready=True sector_rank=13 price=281.46 support=252.2 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=54.42 liquidity=2929776.0 spike=0.1
- SCTS.CA: score=17.83 buy_ready=True sector_rank=6 price=618.42 support=602.0 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=58.82 liquidity=1933172.88 spike=0.23
- SDTI.CA: score=15.03 buy_ready=False sector_rank=13 price=72.98 support=46.6 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=82.68 liquidity=2131675.25 spike=0.08
- SEIG.CA: score=16.79 buy_ready=False sector_rank=13 price=284.03 support=237.0 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=87.23 liquidity=1894143.5 spike=0.14
- SIPC.CA: score=25.9 buy_ready=False sector_rank=13 price=4.7 support=3.47 resistance=5.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=72.91 liquidity=11421952.0 spike=0.2
- SKPC.CA: score=26.9 buy_ready=True sector_rank=8 price=16.8 support=14.8 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=66.5 liquidity=25978930.0 spike=0.57
- SMFR.CA: score=19.97 buy_ready=True sector_rank=13 price=265.12 support=223.0 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=69.33 liquidity=4073260.75 spike=0.1
- SNFC.CA: score=7.51 buy_ready=False sector_rank=13 price=10.71 support=10.6 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT RSI=19.44 liquidity=1607961.88 spike=0.14
- SPIN.CA: score=25.9 buy_ready=True sector_rank=7 price=15.98 support=14.57 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=55.34 liquidity=13382331.0 spike=0.45
- SPMD.CA: score=25.9 buy_ready=True sector_rank=13 price=0.48 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=65.71 liquidity=10038275.0 spike=0.3
- SUGR.CA: score=27.9 buy_ready=False sector_rank=9 price=50.56 support=46.47 resistance=51.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=73.43 liquidity=10436170.0 spike=0.79
- SVCE.CA: score=26.06 buy_ready=False sector_rank=13 price=10.9 support=9.06 resistance=12.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=71.39 liquidity=97180264.0 spike=1.08
- SWDY.CA: score=25.9 buy_ready=False sector_rank=12 price=108.59 support=89.0 resistance=114.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=70.96 liquidity=20279088.0 spike=0.32
- TALM.CA: score=20.41 buy_ready=False sector_rank=6 price=19.04 support=15.6 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=74.45 liquidity=4507402.5 spike=0.11
- TMGH.CA: score=23.9 buy_ready=False sector_rank=11 price=98.32 support=95.2 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=41.45 liquidity=60511364.0 spike=0.18
- TRTO.CA: score=5.91 buy_ready=False sector_rank=13 price=0.04 support=0.04 resistance=0.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7752.43 spike=4.76
- UEFM.CA: score=16.11 buy_ready=False sector_rank=13 price=573.76 support=511.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=76.07 liquidity=1213002.5 spike=0.2
- UEGC.CA: score=19.81 buy_ready=True sector_rank=13 price=2.6 support=2.08 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=60.91 liquidity=3913671.75 spike=0.07
- UNIP.CA: score=25.9 buy_ready=True sector_rank=13 price=0.42 support=0.34 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=53.13 liquidity=26707076.0 spike=0.91
- UNIT.CA: score=16.87 buy_ready=False sector_rank=11 price=20.28 support=17.32 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=72.26 liquidity=974748.94 spike=0.05
- WCDF.CA: score=17.71 buy_ready=False sector_rank=13 price=630.31 support=519.26 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=91.64 liquidity=2808294.5 spike=0.55
- WKOL.CA: score=19.23 buy_ready=True sector_rank=13 price=323.01 support=307.0 resistance=363.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=55.48 liquidity=3333407.5 spike=0.14
- ZEOT.CA: score=14.14 buy_ready=False sector_rank=13 price=13.67 support=13.0 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=79141312.0 spike=2.62
- ZMID.CA: score=25.9 buy_ready=True sector_rank=11 price=7.7 support=7.06 resistance=7.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=59.57 liquidity=56304572.0 spike=0.22

## Backtesting Lite
- SCEM.CA: 180d return=56.94%, max drawdown=-14.53%, MA20>MA50 days last20=16, as_of=2026-08-11T21:00:00+00:00
- MBSC.CA: 180d return=71.35%, max drawdown=-16.25%, MA20>MA50 days last20=2, as_of=2026-08-11T21:00:00+00:00
- EEII.CA: 180d return=66.49%, max drawdown=-32.26%, MA20>MA50 days last20=20, as_of=2026-08-11T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- SCEM.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=589 sources=3 expected=Sinai Cement summary=Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn; Upward trend line ends several-day decline for Sinai Cement stock; Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25
  - Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn: https://english.mubasher.info/news/4564824/Sinai-Cement-s-consolidated-profits-fall-in-2025-net-sales-cross-EGP-9bn/
  - Upward trend line ends several-day decline for Sinai Cement stock: https://english.mubasher.info/news/4529647/Upward-trend-line-ends-several-day-decline-for-Sinai-Cement-stock/
  - Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25: https://english.mubasher.info/news/4526073/Sinai-Cement-reports-lower-consolidated-net-profits-at-EGP-1-5bn-in-9M-25/
- MBSC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=589 sources=3 expected=Misr Beni Suef Cement summary=Misr Beni Suef’s consolidated net profits near EGP 4bn in 2025; Misr Beni Suef’s consolidated net profits hit EGP 953m in H1-25; Misr Beni Suef Cement’s consolidate profits fall to EGP 574m in Q1-25
  - Misr Beni Suef’s consolidated net profits near EGP 4bn in 2025: https://english.mubasher.info/news/4599415/Misr-Beni-Suef-s-consolidated-net-profits-near-EGP-4bn-in-2025/
  - Misr Beni Suef’s consolidated net profits hit EGP 953m in H1-25: https://english.mubasher.info/news/4488249/Misr-Beni-Suef-s-consolidated-net-profits-hit-EGP-953m-in-H1-25/
  - Misr Beni Suef Cement’s consolidate profits fall to EGP 574m in Q1-25: https://english.mubasher.info/news/4455784/Misr-Beni-Suef-Cement-s-consolidate-profits-fall-to-EGP-574m-in-Q1-25/
- EEII.CA: status=OLD_ACCEPTED latest=2019-01-01 age_days=2781 sources=3 expected=Arab Engineering Industries summary=Shareholder cuts stake in Arab Engineering Industries to 9%; Arab Moltaqa cuts stake in Arab Engineering Industries; Lower sales weigh on Arab Engineering Industries’ profit in 2019
  - Shareholder cuts stake in Arab Engineering Industries to 9%: https://english.mubasher.info/news/4009461/Shareholder-cuts-stake-in-Arab-Engineering-Industries-to-9-/
  - Arab Moltaqa cuts stake in Arab Engineering Industries: https://english.mubasher.info/news/3707590/Arab-Moltaqa-cuts-stake-in-Arab-Engineering-Industries/
  - Lower sales weigh on Arab Engineering Industries’ profit in 2019: https://english.mubasher.info/news/3586813/Lower-sales-weigh-on-Arab-Engineering-Industries-profit-in-2019/
- ABUK.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Qir Fertilizers summary=Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results; Abu Qir Fertilizers&#39; board approves $5.6m coated urea project; Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26
  - Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results: https://english.mubasher.info/news/4604919/Abu-Qir-Fertilizers-generates-EGP-5-6bn-net-profits-in-Q1-26-unaudited-results/
  - Abu Qir Fertilizers&#39; board approves $5.6m coated urea project: https://english.mubasher.info/news/4585599/Abu-Qir-Fertilizers-board-approves-5-6m-coated-urea-project/
  - Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26: https://english.mubasher.info/news/4554415/Abu-Qir-Fertilizers-profits-exceed-EGP-5-1bn-in-H1-25-26/
- MCQE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=589 sources=3 expected=Misr Cement Qena summary=Misr Cement to distribute EGP 10/shr dividends for 2025; Misr Cement stock is testing technical level ahead of historical peak – Analysis; Misr Cement witnesses 3,254% remarkable jump in 9M-25 consolidated net profits
  - Misr Cement to distribute EGP 10/shr dividends for 2025: https://english.mubasher.info/news/4586191/Misr-Cement-to-distribute-EGP-10-shr-dividends-for-2025/
  - Misr Cement stock is testing technical level ahead of historical peak – Analysis: https://english.mubasher.info/news/4560306/Misr-Cement-stock-is-testing-technical-level-ahead-of-historical-peak-Analysis/
  - Misr Cement witnesses 3,254% remarkable jump in 9M-25 consolidated net profits: https://english.mubasher.info/news/4524754/Misr-Cement-witnesses-3-254-remarkable-jump-in-9M-25-consolidated-net-profits/
- ADPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=The Arab Dairy Products Co. summary=Evidence rejected for ADPC.CA: source text did not clearly match ADPC.CA / The Arab Dairy Products Co..
- PRMH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Prime Holding S.A.E summary=Evidence rejected for PRMH.CA: source text did not clearly match PRMH.CA / Prime Holding S.A.E.
- DOMT.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=589 sources=3 expected=Arabian Food Industries Domty summary=Domty posts lower consolidated net profits at EGP 161m in 2025; net sales exceed EGP 9.3bn; Selling pressure pushes Domty’s stock toward EGP 23.50–22.85; Domty unveils demerger, establishes Dairy Products Euro Arabian
  - Domty posts lower consolidated net profits at EGP 161m in 2025; net sales exceed EGP 9.3bn: https://english.mubasher.info/news/4593671/Domty-posts-lower-consolidated-net-profits-at-EGP-161m-in-2025-net-sales-exceed-EGP-9-3bn/
  - Selling pressure pushes Domty’s stock toward EGP 23.50–22.85: https://english.mubasher.info/news/4562323/Selling-pressure-pushes-Domty-s-stock-toward-EGP-23-50-22-85/
  - Domty unveils demerger, establishes Dairy Products Euro Arabian: https://english.mubasher.info/news/4543153/Domty-unveils-demerger-establishes-Dairy-Products-Euro-Arabian/

## Warnings
- Evidence for SCEM.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence for MBSC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for EEII.CA matches the company but appears old; latest detected date is 2019-01-01.
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Evidence for MCQE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ADPC.CA: source text did not clearly match ADPC.CA / The Arab Dairy Products Co..
- Evidence rejected for PRMH.CA: source text did not clearly match PRMH.CA / Prime Holding S.A.E.
- Evidence for DOMT.CA matches the company but appears old; latest detected date is 2025-01-01.
