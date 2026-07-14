# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-07-14T08:30:03.472279+00:00
Generated Cairo: 2026-07-14 11:30
Run timing: target 09:15 Cairo | generated Cairo 2026-07-14 11:30 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-07-14 11:26

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 77
- Data quality issues: 1
- Tradeable price/liquidity tickers: 175/189
- Top sector: Technology & Distribution

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, July 14
- Freshness: DELAYED
- EGX30 regime: CONSTRUCTIVE / above MA20 65.0% / above MA50 45.0%
- EGX70 regime: BULLISH / above MA20 74.36% / above MA50 74.36%
- Sector breadth: 52.38%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- CCAP.CA: liquidity=618912704.0 spike=0.95 score=26.4
- ABUK.CA: liquidity=197167120.0 spike=1.38 score=23.54
- AMES.CA: liquidity=120338240.0 spike=2.94 score=13.28
- MFPC.CA: liquidity=118700088.0 spike=1.19 score=23.16
- COMI.CA: liquidity=108481216.0 spike=0.25 score=25.56

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner flagged GDWA.CA, ETEL.CA, COSG.CA as watch/buy setups amid EGX30 constructive, EGX70 bullish breadth, but selective swing‑trade risk mode keeps confidence low.
- GDWA.CA: price above MA20/MA50, liquidity spike, RSI ~52, near support/resistance, sector not leading → bullish watch with low confidence.

## Top Liquidity Spikes
- SMFR.CA: spike=11.57 liquidity=21287420.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EPCO.CA: spike=10.81 liquidity=72784440.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AREH.CA: spike=3.03 liquidity=107658224.0 outlook=BULLISH_WATCH score=91.2 buy_ready=True
- AMES.CA: spike=2.94 liquidity=120338240.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CPCI.CA: spike=2.87 liquidity=7532670.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Technology & Distribution: score=11.92 5d=4.42% 20d=18.68% aboveMA50=100.0%
- #2 Telecommunications: score=10.22 5d=5.07% 20d=6.67% aboveMA50=100.0%
- #3 Transportation & Logistics: score=9.55 5d=3.01% 20d=7.21% aboveMA50=100.0%
- #4 Industrial Goods & Cables: score=9.1 5d=2.41% 20d=4.51% aboveMA50=100.0%
- #5 Fintech & Payments: score=8.38 5d=4.38% 20d=9.24% aboveMA50=50.0%
- #6 Real Estate: score=8.19 5d=3.05% 20d=8.58% aboveMA50=92.31%
- #7 Automotive & Distribution: score=8.02 5d=-0.72% 20d=9.65% aboveMA50=100.0%
- #8 Textiles: score=7.85 5d=3.17% 20d=5.0% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- Priority #1: BUY GDWA.CA
  - Entry: 0.85 | Take profit: 0.91 | Stop loss: 0.82
  - Confidence: LOW | score=30.4 | outlook=BULLISH_WATCH 92.2
  - Reason: WATCH/BUY SETUP: GDWA.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 51.8, support 0.76, resistance 0.82, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY ETEL.CA
  - Entry: 96.95 | Take profit: 104.71 | Stop loss: 93.07
  - Confidence: LOW | score=29.02 | outlook=BULLISH_WATCH 90
  - Reason: WATCH/BUY SETUP: ETEL.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 64.17, support 89.01, resistance 101.5, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY COSG.CA
  - Entry: 1.69 | Take profit: 1.83 | Stop loss: 1.62
  - Confidence: LOW | score=28.54 | outlook=BULLISH_WATCH 79.2
  - Reason: WATCH/BUY SETUP: COSG.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 54.55, support 1.47, resistance 1.66, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ALCN.CA: BULLISH_WATCH score=100 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- GDWA.CA: BULLISH_WATCH score=92.2 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- AREH.CA: BULLISH_WATCH score=91.2 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ETEL.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- CSAG.CA: BULLISH_WATCH score=87.55 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- DAPH.CA: BULLISH_WATCH score=86.2 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- CAED.CA: BULLISH_WATCH score=86.2 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- EFIH.CA: BULLISH_WATCH score=84.38 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ELWA.CA: BULLISH_WATCH score=83.2 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- GMCI.CA: BULLISH_WATCH score=81.2 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended; sector is not leading

## BUY-Ready Candidates
- AREH.CA: rank=32.46 outlook=BULLISH_WATCH outlook_score=91.2 sector_rank=9 price=1.72 support=1.51 resistance=1.76 liquidity=107658224.0
- GDWA.CA: rank=30.4 outlook=BULLISH_WATCH outlook_score=92.2 sector_rank=9 price=0.85 support=0.76 resistance=0.82 liquidity=40616572.0
- RAYA.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=70 sector_rank=1 price=8.16 support=6.8 resistance=8.29 liquidity=31880620.0
- ETEL.CA: rank=29.02 outlook=BULLISH_WATCH outlook_score=90 sector_rank=2 price=96.95 support=89.01 resistance=101.5 liquidity=8619881.0
- COSG.CA: rank=28.54 outlook=BULLISH_WATCH outlook_score=79.2 sector_rank=9 price=1.69 support=1.47 resistance=1.66 liquidity=42943656.0
- ELSH.CA: rank=28.4 outlook=CONSTRUCTIVE outlook_score=56.2 sector_rank=9 price=14.83 support=11.1 resistance=15.11 liquidity=57567996.0
- MASR.CA: rank=28.4 outlook=CONSTRUCTIVE outlook_score=62.2 sector_rank=9 price=8.12 support=6.71 resistance=7.95 liquidity=26201302.0
- ADPC.CA: rank=28.18 outlook=CONSTRUCTIVE outlook_score=55.2 sector_rank=9 price=3.87 support=3.32 resistance=3.94 liquidity=30209344.0
- EGCH.CA: rank=28.08 outlook=BULLISH_WATCH outlook_score=80.44 sector_rank=12 price=13.64 support=12.13 resistance=14.08 liquidity=95812520.0
- ELEC.CA: rank=28.04 outlook=BULLISH_WATCH outlook_score=81.1 sector_rank=4 price=2.15 support=2.04 resistance=2.18 liquidity=25118916.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=17.41 buy_ready=False sector_rank=9 price=231.86 support=196.0 resistance=247.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=70.14 liquidity=1012273.63 spike=0.07
- ABUK.CA: score=23.54 buy_ready=False sector_rank=12 price=71.45 support=66.66 resistance=77.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=42.84 liquidity=197167120.0 spike=1.38
- ACAMD.CA: score=26.4 buy_ready=True sector_rank=9 price=2.32 support=2.14 resistance=2.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=45.0 liquidity=11076638.0 spike=0.12
- ACGC.CA: score=24.65 buy_ready=True sector_rank=8 price=9.96 support=8.92 resistance=9.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=54.07 liquidity=6250998.5 spike=0.29
- ADCI.CA: score=15.19 buy_ready=False sector_rank=9 price=233.33 support=223.0 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=51.65 liquidity=2792881.5 spike=0.23
- ADIB.CA: score=20.56 buy_ready=False sector_rank=16 price=46.51 support=44.1 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=49.79 liquidity=29844686.0 spike=0.32
- ADPC.CA: score=28.18 buy_ready=True sector_rank=9 price=3.87 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=39.0 liquidity=30209344.0 spike=1.89
- AFDI.CA: score=21.26 buy_ready=True sector_rank=9 price=46.86 support=40.8 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=59.42 liquidity=2864698.75 spike=0.21
- AFMC.CA: score=18.43 buy_ready=True sector_rank=9 price=74.96 support=66.0 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=57.13 liquidity=2032025.0 spike=0.6
- AJWA.CA: score=24.4 buy_ready=True sector_rank=9 price=180.38 support=150.51 resistance=190.0 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=57.66 liquidity=15619826.14 spike=0.96
- ALCN.CA: score=27.4 buy_ready=True sector_rank=3 price=29.91 support=27.7 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=66.15 liquidity=15368684.0 spike=0.93
- ALUM.CA: score=15.54 buy_ready=False sector_rank=9 price=23.01 support=20.55 resistance=24.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=44.37 liquidity=2136206.25 spike=0.27
- AMER.CA: score=23.37 buy_ready=False sector_rank=6 price=3.16 support=2.28 resistance=3.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=76.8 liquidity=9969719.0 spike=0.12
- AMES.CA: score=13.28 buy_ready=False sector_rank=9 price=116.83 support=102.31 resistance=118.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=120338240.0 spike=2.94
- AMIA.CA: score=19.48 buy_ready=True sector_rank=9 price=8.95 support=8.4 resistance=9.51 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=46.46 liquidity=5083107.64 spike=0.68
- AMOC.CA: score=26.65 buy_ready=True sector_rank=19 price=8.36 support=7.42 resistance=8.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=56.63 liquidity=89043656.0 spike=1.72
- APSW.CA: score=13.24 buy_ready=False sector_rank=9 price=8.5 support=8.0 resistance=8.98 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=45.6 liquidity=798090.5 spike=1.02
- ARAB.CA: score=26.4 buy_ready=False sector_rank=6 price=0.25 support=0.2 resistance=0.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=57990676.0 spike=0.64
- ARCC.CA: score=18.42 buy_ready=False sector_rank=18 price=54.79 support=53.0 resistance=57.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=46.04 liquidity=18333798.0 spike=0.89
- AREH.CA: score=32.46 buy_ready=True sector_rank=9 price=1.72 support=1.51 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 July 01:29 PM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=107658224.0 spike=3.03
- ARVA.CA: score=14.25 buy_ready=False sector_rank=9 price=10.77 support=10.5 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=46.12 liquidity=1852590.63 spike=0.09
- ASCM.CA: score=23.53 buy_ready=True sector_rank=9 price=62.41 support=56.29 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=57.49 liquidity=9133159.0 spike=0.11
- ASPI.CA: score=19.4 buy_ready=False sector_rank=9 price=0.31 support=0.3 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=39.06 liquidity=11671125.0 spike=0.41
- ATLC.CA: score=14.77 buy_ready=True sector_rank=17 price=5.2 support=4.77 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=44.85 liquidity=1308705.88 spike=0.19
- ATQA.CA: score=18.25 buy_ready=False sector_rank=12 price=9.54 support=9.21 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=52.34 liquidity=6473368.0 spike=0.2
- AXPH.CA: score=17.57 buy_ready=True sector_rank=9 price=1212.93 support=1073.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=63.99 liquidity=1170745.5 spike=0.4
- BINV.CA: score=15.34 buy_ready=False sector_rank=10 price=48.53 support=45.01 resistance=51.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=54.5 liquidity=942859.13 spike=0.15
- BIOC.CA: score=18.98 buy_ready=False sector_rank=9 price=73.37 support=66.75 resistance=76.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=52.12 liquidity=584258.56 spike=0.18
- BTFH.CA: score=21.46 buy_ready=False sector_rank=17 price=3.05 support=2.91 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=43.9 liquidity=25481882.0 spike=0.13
- CAED.CA: score=19.89 buy_ready=True sector_rank=9 price=74.35 support=68.0 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=51.31 liquidity=1494773.75 spike=0.23
- CANA.CA: score=22.56 buy_ready=False sector_rank=16 price=36.0 support=34.7 resistance=38.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=41.44 liquidity=10319439.0 spike=0.99
- CCAP.CA: score=26.4 buy_ready=True sector_rank=10 price=5.5 support=4.65 resistance=5.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=59.41 liquidity=618912704.0 spike=0.95
- CCRS.CA: score=3.32 buy_ready=False sector_rank=9 price=2.53 support=2.5 resistance=2.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3915343.75 spike=0.35
- CEFM.CA: score=14.19 buy_ready=False sector_rank=9 price=103.68 support=95.75 resistance=110.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=55.4 liquidity=791005.63 spike=0.36
- CERA.CA: score=18.08 buy_ready=True sector_rank=9 price=1.3 support=1.17 resistance=1.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=1676607.62 spike=0.08
- CFGH.CA: score=1.23 buy_ready=False sector_rank=9 price=0.11 support=0.11 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12170.94 spike=1.91
- CICH.CA: score=4.22 buy_ready=False sector_rank=17 price=11.84 support=11.36 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=34.72 liquidity=753157.69 spike=0.2
- CIEB.CA: score=17.04 buy_ready=True sector_rank=16 price=24.36 support=23.3 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=53.42 liquidity=1476784.38 spike=0.21
- CIRA.CA: score=23.3 buy_ready=False sector_rank=13 price=30.87 support=26.0 resistance=31.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=70.57 liquidity=7557872.5 spike=0.32
- CLHO.CA: score=23.61 buy_ready=True sector_rank=14 price=16.21 support=14.85 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=55.59 liquidity=25604314.0 spike=0.72
- CNFN.CA: score=25.46 buy_ready=True sector_rank=17 price=5.0 support=4.4 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=22291166.0 spike=0.51
- COMI.CA: score=25.56 buy_ready=True sector_rank=16 price=137.0 support=126.21 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=45.96 liquidity=108481216.0 spike=0.25
- COPR.CA: score=9.4 buy_ready=False sector_rank=9 price=0.38 support=0.37 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16381011.0 spike=0.78
- COSG.CA: score=28.54 buy_ready=True sector_rank=9 price=1.69 support=1.47 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=42943656.0 spike=1.07
- CPCI.CA: score=10.67 buy_ready=False sector_rank=9 price=433.29 support=431.0 resistance=445.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7532670.0 spike=2.87
- CSAG.CA: score=22.04 buy_ready=True sector_rank=3 price=32.2 support=30.85 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=64.2 liquidity=4640311.5 spike=0.27
- DAPH.CA: score=20.3 buy_ready=True sector_rank=9 price=83.5 support=77.12 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=59.99 liquidity=1903649.75 spike=0.21
- DEIN.CA: score=-0.6 buy_ready=False sector_rank=9 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=15.96 buy_ready=False sector_rank=15 price=26.91 support=24.21 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=60.17 liquidity=383731.88 spike=0.07
- DSCW.CA: score=25.76 buy_ready=True sector_rank=9 price=1.87 support=1.71 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=40.91 liquidity=32758754.0 spike=1.18
- DTPP.CA: score=19.31 buy_ready=False sector_rank=9 price=205.22 support=114.0 resistance=234.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=89.03 liquidity=5910679.5 spike=0.16
- EALR.CA: score=17.2 buy_ready=False sector_rank=9 price=367.41 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=57.03 liquidity=799903.19 spike=0.07
- EASB.CA: score=14.33 buy_ready=False sector_rank=9 price=7.21 support=5.06 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=36.74 liquidity=1932887.13 spike=0.11
- EAST.CA: score=5.31 buy_ready=False sector_rank=15 price=36.55 support=36.6 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=29.64 liquidity=2742399.75 spike=0.06
- EBSC.CA: score=18.01 buy_ready=True sector_rank=9 price=1.92 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=51.95 liquidity=1611993.63 spike=0.28
- ECAP.CA: score=15.99 buy_ready=True sector_rank=9 price=32.85 support=31.15 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=35.35 liquidity=1585588.25 spike=0.17
- EDFM.CA: score=16.85 buy_ready=False sector_rank=9 price=352.13 support=310.2 resistance=349.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=66.15 liquidity=445799.91 spike=0.6
- EEII.CA: score=18.02 buy_ready=True sector_rank=9 price=2.74 support=2.35 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=67.03 liquidity=3615648.5 spike=0.17
- EFIC.CA: score=9.43 buy_ready=False sector_rank=12 price=188.98 support=180.02 resistance=207.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=19.85 liquidity=4896638.0 spike=1.88
- EFID.CA: score=20.57 buy_ready=False sector_rank=15 price=27.87 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=52.8 liquidity=24201934.0 spike=0.5
- EFIH.CA: score=24.54 buy_ready=True sector_rank=5 price=22.3 support=20.0 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=60.96 liquidity=8143791.0 spike=0.18
- EGAL.CA: score=22.78 buy_ready=False sector_rank=12 price=297.29 support=272.28 resistance=314.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=45.96 liquidity=22365800.0 spike=0.46
- EGAS.CA: score=10.37 buy_ready=False sector_rank=19 price=54.58 support=53.7 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16964476.0 spike=2.08
- EGBE.CA: score=-1.44 buy_ready=False sector_rank=16 price=0.45 support=0.45 resistance=0.45 source=StockAnalysis EGX public list (quote-only fallback) as_of=2026-07-14 freshness=QUOTE_ONLY RSI=50.0 liquidity=0.0 spike=0.0
- EGCH.CA: score=28.08 buy_ready=True sector_rank=12 price=13.64 support=12.13 resistance=14.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=40.88 liquidity=95812520.0 spike=2.15
- EGSA.CA: score=15.47 buy_ready=False sector_rank=2 price=8.97 support=8.67 resistance=9.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 July 12:27 PM market time freshness=DELAYED_CURRENT RSI=91.67 liquidity=9586.75 spike=1.03
- EGTS.CA: score=19.36 buy_ready=True sector_rank=6 price=18.09 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=48.79 liquidity=2962340.75 spike=0.05
- EHDR.CA: score=23.29 buy_ready=True sector_rank=9 price=2.69 support=2.37 resistance=2.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=51.76 liquidity=6894688.5 spike=0.16
- EKHO.CA: score=7.21 buy_ready=False sector_rank=19 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=28.04 buy_ready=True sector_rank=4 price=2.15 support=2.04 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=25118916.0 spike=1.32
- ELKA.CA: score=26.4 buy_ready=False sector_rank=9 price=1.71 support=1.19 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=72.22 liquidity=32804230.0 spike=0.65
- ELNA.CA: score=12.63 buy_ready=False sector_rank=9 price=38.81 support=35.55 resistance=40.99 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=46.25 liquidity=226262.31 spike=0.43
- ELSH.CA: score=28.4 buy_ready=True sector_rank=9 price=14.83 support=11.1 resistance=15.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=64.31 liquidity=57567996.0 spike=0.33
- ELWA.CA: score=17.75 buy_ready=True sector_rank=9 price=2.04 support=1.87 resistance=2.22 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=43.9 liquidity=2370012.8 spike=1.49
- EMFD.CA: score=20.34 buy_ready=False sector_rank=6 price=11.71 support=11.24 resistance=12.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=43.69 liquidity=7936637.0 spike=0.05
- ENGC.CA: score=22.91 buy_ready=False sector_rank=9 price=42.0 support=33.91 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=73.42 liquidity=6512557.5 spike=0.27
- EOSB.CA: score=14.44 buy_ready=False sector_rank=9 price=1.48 support=1.42 resistance=1.55 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=35839.68 spike=0.47
- EPCO.CA: score=14.4 buy_ready=False sector_rank=9 price=10.37 support=9.72 resistance=10.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=72784440.0 spike=10.81
- EPPK.CA: score=14.81 buy_ready=False sector_rank=9 price=14.12 support=11.72 resistance=15.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=69.3 liquidity=409497.81 spike=0.41
- ETEL.CA: score=29.02 buy_ready=True sector_rank=2 price=96.95 support=89.01 resistance=101.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=64.17 liquidity=8619881.0 spike=0.12
- ETRS.CA: score=18.75 buy_ready=True sector_rank=9 price=10.82 support=9.15 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=50.55 liquidity=4354434.0 spike=0.05
- EXPA.CA: score=23.1 buy_ready=True sector_rank=16 price=18.78 support=18.03 resistance=18.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=56.44 liquidity=5538611.5 spike=0.21
- FAIT.CA: score=18.88 buy_ready=True sector_rank=16 price=37.51 support=35.06 resistance=37.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=50.44 liquidity=2994233.5 spike=1.16
- FAITA.CA: score=8.57 buy_ready=False sector_rank=16 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=44.83 liquidity=9466.08 spike=0.32
- FERC.CA: score=19.79 buy_ready=True sector_rank=12 price=77.42 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=48.71 liquidity=4653819.5 spike=1.18
- FWRY.CA: score=23.4 buy_ready=False sector_rank=5 price=19.03 support=18.13 resistance=19.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=60.28 liquidity=35009292.0 spike=0.19
- GBCO.CA: score=24.4 buy_ready=True sector_rank=7 price=31.65 support=27.77 resistance=32.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=64.63 liquidity=10426110.0 spike=0.12
- GDWA.CA: score=30.4 buy_ready=True sector_rank=9 price=0.85 support=0.76 resistance=0.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=51.8 liquidity=40616572.0 spike=2.5
- GGCC.CA: score=22.74 buy_ready=False sector_rank=9 price=0.59 support=0.41 resistance=0.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=92.74 liquidity=9344053.0 spike=0.54
- GIHD.CA: score=20.6 buy_ready=True sector_rank=9 price=48.79 support=40.0 resistance=52.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=69.42 liquidity=6200333.5 spike=0.28
- GMCI.CA: score=17.53 buy_ready=True sector_rank=9 price=1.99 support=1.66 resistance=2.26 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=65.28 liquidity=1746139.44 spike=1.69
- GRCA.CA: score=-0.0 buy_ready=False sector_rank=9 price=51.46 support=51.0 resistance=51.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=599275.06 spike=0.2
- GSSC.CA: score=17.77 buy_ready=True sector_rank=9 price=260.0 support=240.0 resistance=263.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=65.51 liquidity=1369160.5 spike=0.31
- GTWL.CA: score=21.4 buy_ready=False sector_rank=9 price=110.3 support=46.0 resistance=117.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=89.45 liquidity=26138304.0 spike=0.28
- HDBK.CA: score=8.44 buy_ready=False sector_rank=16 price=77.44 support=75.3 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=10.6 liquidity=5875413.5 spike=0.15
- HELI.CA: score=23.4 buy_ready=False sector_rank=6 price=7.39 support=6.34 resistance=7.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=75.72 liquidity=18667902.0 spike=0.12
- HRHO.CA: score=17.46 buy_ready=False sector_rank=17 price=26.6 support=26.09 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=36.62 liquidity=24363336.0 spike=0.19
- ICID.CA: score=26.96 buy_ready=True sector_rank=9 price=8.29 support=6.55 resistance=8.47 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=59.95 liquidity=16937216.02 spike=2.28
- IDRE.CA: score=26.78 buy_ready=True sector_rank=9 price=45.98 support=41.1 resistance=47.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=57.98 liquidity=8381665.5 spike=0.64
- IFAP.CA: score=13.73 buy_ready=False sector_rank=11 price=19.6 support=18.47 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=57.21 liquidity=636882.75 spike=0.13
- INFI.CA: score=21.69 buy_ready=False sector_rank=9 price=102.85 support=88.51 resistance=106.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=71.89 liquidity=6286531.0 spike=0.64
- IRON.CA: score=11.14 buy_ready=False sector_rank=12 price=31.92 support=30.51 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=49.19 liquidity=1365849.25 spike=0.17
- ISMA.CA: score=12.21 buy_ready=False sector_rank=9 price=27.42 support=26.54 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=16.02 liquidity=4809680.5 spike=0.17
- ISMQ.CA: score=23.78 buy_ready=False sector_rank=12 price=9.5 support=8.06 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=72.31 liquidity=34522392.0 spike=0.24
- ISPH.CA: score=13.61 buy_ready=False sector_rank=14 price=11.4 support=11.2 resistance=12.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=27.27 liquidity=11751359.0 spike=0.19
- JUFO.CA: score=15.56 buy_ready=False sector_rank=15 price=30.22 support=29.1 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=40.22 liquidity=3984694.25 spike=0.16
- KABO.CA: score=18.01 buy_ready=False sector_rank=8 price=7.55 support=6.04 resistance=7.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=88.76 liquidity=4608059.5 spike=0.16
- KWIN.CA: score=5.52 buy_ready=False sector_rank=9 price=68.77 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:00 AM market time freshness=DELAYED_CURRENT RSI=33.96 liquidity=1119791.25 spike=0.08
- KZPC.CA: score=8.9 buy_ready=False sector_rank=9 price=8.75 support=8.26 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=29.44 liquidity=3502579.75 spike=0.53
- LCSW.CA: score=25.42 buy_ready=True sector_rank=18 price=31.01 support=26.41 resistance=32.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=67.42 liquidity=17628398.0 spike=0.3
- LUTS.CA: score=22.4 buy_ready=False sector_rank=9 price=0.73 support=0.69 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=42.08 liquidity=10331481.0 spike=0.21
- MAAL.CA: score=14.38 buy_ready=False sector_rank=9 price=8.43 support=5.72 resistance=8.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=98.01 liquidity=2980611.5 spike=0.18
- MASR.CA: score=28.4 buy_ready=True sector_rank=9 price=8.12 support=6.71 resistance=7.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=62.67 liquidity=26201302.0 spike=0.31
- MBSC.CA: score=16.65 buy_ready=False sector_rank=18 price=236.07 support=222.66 resistance=256.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=39.92 liquidity=6229453.5 spike=0.27
- MCQE.CA: score=13.67 buy_ready=False sector_rank=18 price=175.8 support=166.66 resistance=182.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=46.1 liquidity=1243708.38 spike=0.08
- MCRO.CA: score=26.02 buy_ready=True sector_rank=9 price=1.35 support=1.17 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=65.52 liquidity=44582600.0 spike=1.31
- MENA.CA: score=16.82 buy_ready=False sector_rank=6 price=7.03 support=6.41 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=58.06 liquidity=419484.72 spike=0.05
- MEPA.CA: score=17.58 buy_ready=False sector_rank=9 price=1.65 support=1.52 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=44.74 liquidity=4178252.0 spike=0.39
- MFPC.CA: score=23.16 buy_ready=False sector_rank=12 price=38.0 support=34.22 resistance=40.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=49.84 liquidity=118700088.0 spike=1.19
- MFSC.CA: score=14.36 buy_ready=False sector_rank=9 price=46.74 support=44.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=51.37 liquidity=1955207.0 spike=0.25
- MHOT.CA: score=0.74 buy_ready=False sector_rank=21 price=16.28 support=16.12 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=15.69 liquidity=1343252.63 spike=0.09
- MICH.CA: score=24.4 buy_ready=True sector_rank=9 price=38.0 support=34.0 resistance=39.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=38.69 liquidity=13153901.0 spike=0.81
- MILS.CA: score=17.47 buy_ready=True sector_rank=9 price=136.7 support=126.31 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=48.18 liquidity=3072224.75 spike=0.28
- MIPH.CA: score=17.02 buy_ready=True sector_rank=14 price=698.08 support=630.13 resistance=710.0 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=51.34 liquidity=1409423.55 spike=0.75
- MOED.CA: score=20.61 buy_ready=True sector_rank=9 price=0.73 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=55.62 liquidity=6208197.5 spike=0.58
- MOIL.CA: score=-1.7 buy_ready=False sector_rank=19 price=0.55 support=0.54 resistance=0.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=89162.13 spike=0.3
- MOIN.CA: score=12.82 buy_ready=False sector_rank=9 price=23.95 support=22.6 resistance=25.25 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=48.18 liquidity=418933.41 spike=0.55
- MOSC.CA: score=23.67 buy_ready=True sector_rank=9 price=285.17 support=250.0 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=47.82 liquidity=9250512.0 spike=1.01
- MPCI.CA: score=24.4 buy_ready=True sector_rank=9 price=240.78 support=215.0 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=49.77 liquidity=22816226.0 spike=0.23
- MPCO.CA: score=22.1 buy_ready=False sector_rank=11 price=1.87 support=1.7 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=13005668.0 spike=0.16
- MPRC.CA: score=23.4 buy_ready=False sector_rank=9 price=41.6 support=31.72 resistance=43.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=89.47 liquidity=11126646.0 spike=0.24
- MTIE.CA: score=24.29 buy_ready=True sector_rank=7 price=9.6 support=8.75 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=55.23 liquidity=7892218.0 spike=0.38
- NAHO.CA: score=10.41 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=14567.5 spike=0.56
- NCCW.CA: score=21.05 buy_ready=True sector_rank=9 price=6.56 support=5.82 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=51.79 liquidity=6649539.0 spike=0.27
- NEDA.CA: score=17.23 buy_ready=False sector_rank=9 price=2.8 support=2.7 resistance=2.83 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=57.14 liquidity=386822.79 spike=1.22
- NHPS.CA: score=26.08 buy_ready=False sector_rank=9 price=84.97 support=61.55 resistance=83.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=75.67 liquidity=74362688.0 spike=2.34
- NINH.CA: score=18.29 buy_ready=False sector_rank=9 price=17.99 support=16.82 resistance=18.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=51.8 liquidity=6886639.0 spike=0.94
- NIPH.CA: score=25.61 buy_ready=True sector_rank=14 price=178.54 support=157.01 resistance=185.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=60.61 liquidity=14920489.0 spike=0.17
- OBRI.CA: score=20.69 buy_ready=False sector_rank=9 price=35.96 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=55.18 liquidity=7292185.5 spike=0.22
- OCDI.CA: score=20.56 buy_ready=False sector_rank=6 price=26.92 support=20.24 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=78.6 liquidity=9155816.0 spike=0.09
- OCPH.CA: score=22.81 buy_ready=True sector_rank=9 price=371.21 support=337.0 resistance=374.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=65.84 liquidity=7888100.0 spike=1.26
- ODIN.CA: score=18.71 buy_ready=True sector_rank=9 price=2.45 support=2.05 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=61.67 liquidity=2311138.75 spike=0.16
- OFH.CA: score=21.44 buy_ready=True sector_rank=9 price=0.63 support=0.57 resistance=0.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=61.46 liquidity=5038869.0 spike=0.24
- OIH.CA: score=18.83 buy_ready=False sector_rank=10 price=1.42 support=1.35 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=7434482.0 spike=0.11
- OLFI.CA: score=18.94 buy_ready=True sector_rank=15 price=22.96 support=21.0 resistance=23.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=58.56 liquidity=3366426.75 spike=0.1
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=682.2 support=681.5 resistance=684.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25439540.0 spike=1.0
- ORHD.CA: score=24.4 buy_ready=True sector_rank=6 price=39.11 support=36.92 resistance=39.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=47.12 liquidity=25584206.0 spike=0.16
- ORWE.CA: score=20.71 buy_ready=False sector_rank=8 price=22.7 support=21.95 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=37.21 liquidity=8305034.5 spike=0.43
- PHAR.CA: score=11.62 buy_ready=False sector_rank=14 price=86.23 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=39.19 liquidity=3009899.0 spike=0.14
- PHDC.CA: score=17.4 buy_ready=False sector_rank=6 price=14.74 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=24679854.0 spike=0.08
- PHTV.CA: score=20.93 buy_ready=False sector_rank=9 price=301.85 support=204.03 resistance=304.0 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=89.79 liquidity=7525724.35 spike=0.57
- POUL.CA: score=23.57 buy_ready=True sector_rank=15 price=38.8 support=34.99 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=69.01 liquidity=14930815.0 spike=0.35
- PRCL.CA: score=19.84 buy_ready=False sector_rank=18 price=34.8 support=24.14 resistance=36.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=75.45 liquidity=9417397.0 spike=0.19
- PRDC.CA: score=26.4 buy_ready=True sector_rank=6 price=8.45 support=6.2 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=59.52 liquidity=73662384.0 spike=0.51
- PRMH.CA: score=24.4 buy_ready=True sector_rank=9 price=2.8 support=2.34 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=46.24 liquidity=16534948.0 spike=0.53
- RACC.CA: score=26.21 buy_ready=True sector_rank=9 price=10.38 support=9.36 resistance=10.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=58.48 liquidity=9808629.0 spike=0.94
- RAKT.CA: score=13.55 buy_ready=False sector_rank=9 price=23.1 support=21.25 resistance=23.79 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=57.11 liquidity=352090.21 spike=1.4
- RAYA.CA: score=29.4 buy_ready=True sector_rank=1 price=8.16 support=6.8 resistance=8.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=63.79 liquidity=31880620.0 spike=0.28
- RMDA.CA: score=14.19 buy_ready=False sector_rank=14 price=4.96 support=4.81 resistance=5.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=5579272.0 spike=0.25
- ROTO.CA: score=20.34 buy_ready=True sector_rank=9 price=42.68 support=33.7 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=54.28 liquidity=3942901.0 spike=0.12
- RREI.CA: score=25.23 buy_ready=True sector_rank=9 price=3.8 support=3.34 resistance=3.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=60.87 liquidity=6834246.0 spike=0.35
- RTVC.CA: score=14.33 buy_ready=False sector_rank=9 price=3.83 support=3.55 resistance=3.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=926845.44 spike=0.21
- RUBX.CA: score=21.4 buy_ready=False sector_rank=9 price=13.47 support=9.8 resistance=14.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=80.15 liquidity=12595158.0 spike=0.23
- SAUD.CA: score=14.03 buy_ready=False sector_rank=16 price=21.45 support=19.99 resistance=22.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=49.15 liquidity=1461128.5 spike=0.21
- SCEM.CA: score=12.45 buy_ready=False sector_rank=18 price=61.62 support=60.14 resistance=67.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=52.02 liquidity=2027608.38 spike=0.12
- SCFM.CA: score=16.25 buy_ready=False sector_rank=9 price=253.88 support=226.5 resistance=269.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=54.22 liquidity=854846.25 spike=0.16
- SCTS.CA: score=16.37 buy_ready=False sector_rank=13 price=615.89 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=59.37 liquidity=623826.81 spike=0.11
- SDTI.CA: score=14.81 buy_ready=False sector_rank=9 price=46.9 support=45.55 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:47 AM market time freshness=DELAYED_CURRENT RSI=49.44 liquidity=414304.94 spike=0.05
- SEIG.CA: score=17.21 buy_ready=False sector_rank=9 price=257.15 support=180.6 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=85.04 liquidity=3814273.0 spike=0.2
- SIPC.CA: score=14.74 buy_ready=False sector_rank=9 price=3.48 support=3.25 resistance=3.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=46.75 liquidity=1341063.0 spike=0.16
- SKPC.CA: score=21.78 buy_ready=False sector_rank=12 price=16.6 support=15.58 resistance=16.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=48.21 liquidity=22902044.0 spike=0.72
- SMFR.CA: score=14.4 buy_ready=False sector_rank=9 price=226.98 support=206.41 resistance=227.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21287420.0 spike=11.57
- SNFC.CA: score=10.35 buy_ready=False sector_rank=9 price=11.64 support=11.26 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=46.55 liquidity=953708.94 spike=0.08
- SPIN.CA: score=12.25 buy_ready=False sector_rank=8 price=14.7 support=13.3 resistance=14.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:00 AM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=850558.56 spike=0.09
- SPMD.CA: score=24.61 buy_ready=True sector_rank=9 price=0.44 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=8214954.5 spike=0.47
- SUGR.CA: score=5.09 buy_ready=False sector_rank=15 price=47.04 support=45.31 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=2514713.75 spike=0.52
- SVCE.CA: score=24.72 buy_ready=True sector_rank=9 price=9.33 support=8.35 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=52.6 liquidity=8318574.5 spike=0.12
- SWDY.CA: score=20.6 buy_ready=True sector_rank=4 price=87.59 support=84.3 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=56.06 liquidity=4198025.0 spike=0.32
- TALM.CA: score=5.58 buy_ready=False sector_rank=13 price=15.64 support=15.27 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=30.07 liquidity=1834185.88 spike=0.16
- TMGH.CA: score=26.4 buy_ready=True sector_rank=6 price=97.58 support=92.1 resistance=99.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=48.25 liquidity=45706296.0 spike=0.13
- TRTO.CA: score=13.36 buy_ready=False sector_rank=9 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=751.23 spike=2.48
- UEFM.CA: score=17.06 buy_ready=False sector_rank=9 price=519.23 support=460.0 resistance=529.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=60.58 liquidity=663287.75 spike=0.42
- UEGC.CA: score=23.4 buy_ready=False sector_rank=9 price=1.91 support=1.33 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=80.3 liquidity=10240171.0 spike=0.45
- UNIP.CA: score=22.81 buy_ready=True sector_rank=9 price=0.34 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=4407930.0 spike=0.25
- UNIT.CA: score=12.84 buy_ready=False sector_rank=6 price=20.83 support=19.01 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=58081920.0 spike=2.72
- WCDF.CA: score=12.57 buy_ready=False sector_rank=9 price=515.94 support=450.0 resistance=544.99 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=39.17 liquidity=767718.72 spike=2.2
- WKOL.CA: score=17.03 buy_ready=False sector_rank=9 price=310.55 support=273.1 resistance=334.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=629952.5 spike=0.09
- ZEOT.CA: score=24.4 buy_ready=True sector_rank=9 price=11.68 support=9.05 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=42.32 liquidity=11195713.0 spike=0.29
- ZMID.CA: score=26.4 buy_ready=True sector_rank=6 price=7.27 support=6.11 resistance=7.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=68.84 liquidity=63858700.0 spike=0.29

## Backtesting Lite
- AREH.CA: 180d return=42.5%, max drawdown=-37.58%, MA20>MA50 days last20=20, as_of=2026-07-11T21:00:00+00:00
- GDWA.CA: 180d return=-30.76%, max drawdown=-39.84%, MA20>MA50 days last20=13, as_of=2026-07-11T21:00:00+00:00
- RAYA.CA: 180d return=177.18%, max drawdown=-12.86%, MA20>MA50 days last20=20, as_of=2026-07-11T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- AREH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Real Estate Egyptian Consortium S.A.E summary=Real Estate Egyptian Consortium’s net profits approach EGP 2m in 9M-25; Shareholder ups stake in Real Estate Egyptian; Target for Real Estate Investment cuts stake in Real Estate Egyptian Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Real Estate Egyptian Consortium’s net profits approach EGP 2m in 9M-25: https://english.mubasher.info/news/4528467/Real-Estate-Egyptian-Consortium-s-net-profits-approach-EGP-2m-in-9M-25/
  - Shareholder ups stake in Real Estate Egyptian: https://english.mubasher.info/news/4026301/Shareholder-ups-stake-in-Real-Estate-Egyptian/
  - Target for Real Estate Investment cuts stake in Real Estate Egyptian: https://english.mubasher.info/news/4010821/Target-for-Real-Estate-Investment-cuts-stake-in-Real-Estate-Egyptian/
- GDWA.CA: status=RECENT_ACCEPTED latest=2026-07-09 age_days=5 sources=3 expected=Gadwa for Industrial Development summary=Gadwa for Industrial Development (GDWA.CA) has released its consolidated results for Q1 2026, showing a top-line revenue of EGP 3.26 billion and total assets of EGP 22.6 billion as of March 31, 2026. The company's financial metrics for the last 12 months (ending July 09, 2026) include a revenue of EGP 13.72 billion and a loss of EGP 359.94 million.
  - GADWA for Industrial Development Announces its Consolidated Results for the period ended on the 31st of March, 2026 (June 30, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHimS01vJuAzPKaF0bDBp1d5mHQlOxb5gtJlA2-Ga-cbo2vkc25bo0VSPQsQhfDiaZ7UZk80kGVH7cgf5Fwkpx5JheC3QV-eQRJvJwe52TLbq2Tlu6Y79JHctIodfWY2enWAHBDDYeut-adCAWH
  - Gadwa for Industrial Development (EGX:GDWA) Statistics & Valuation Metrics (July 09, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEicAjq18zvMXdJTDBmTTTEITN8klJMWIisHLljpslnUMliFuVhOVCK9MpbpfLYfBlO-4N_f0kHth_YhkcTdqkpsSnGOQoYzJ3SH-SGPnhH1iL7NthHh_g4DLpOr06HwbOMMUeYcEl0xsvrGbgKKw==
  - Gadwa for Industrial Development Annual Report | EGX:GDWA Financials: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQuqVBFFDNlr6Mg9viC3mgbi2OizfCg_teFww3h9XvBHalJ5IU9LjL92K2RWktBHLKp1kitdOFjKCljrkZyp0z7rhNzyNvKelnMl5GybUHdm6C6oLirAiFzoNE1BdzxNj9-09gBRelvYCaY9kfYyOr3UCNoP1UZ6ljbp14vF1LlRKMJOnmn_oy5UQmX2P8
- RAYA.CA: status=RECENT_ACCEPTED latest=2026-07-12 age_days=2 sources=3 expected=Raya Holding summary=Raya Holding (RAYA.CA) reported revenue of EGP 66.76 billion and profits of EGP 2.60 billion for the last 12 months ending July 12, 2026. The company's stock price increased by over 142% in the last 52 weeks. In 2025, revenue increased by 41.47% to EGP 63.83 billion, and earnings rose by 53.29% to EGP 2.59 billion.
  - Raya Holding Company for Financial Investments (S.A.E) (EGX:RAYA) Statistics & Valuation Metrics (July 12, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGd7NgjrA7uL-FDdlz1WTnr4t0MqGbRw5_Ui2W2VAY4wFgKjjWzrLVB3W2yKl2co4WhqJrBLIVAAhA54-BsTLBPz9ejJ0hwte1j1ndr8bFyHGR_XrD09eoJj6OEyqSZqMr-6UAcWMgkSbwW5__yMA==
  - Raya Holding Company for Financial Investments (SAE) (EGX:RAYA) - Stock Analysis (2025 Financial Performance): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVDrTQ6DUFu_vamrFAoPNJYluIrAvTksGnpzMqtkt7wgcEIC-j3fscOZ_rQ47vix_Lb8tg6iviPOO9XhxVAVl_6UQtuTUULhqNk7xLzdwmj4Z097jZHHnwrxPjV1S4445hB7k=
  - Raya Holding Income Statement - Investing.com (Latest Quarter and Fiscal Year): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGO4BpOKK0hRl8qJfyxzH7bvEJ-ZBdnXMo28kQN7aTjdAu37s-ZTDPEfc6dsnpqHawTcxZZTkKlYovKLwsvzS3PlrcA_pouktsDZQK6u3XxjXGSnu3yvOQdru8m1v5-JzjgdKd9bLUGpdMCiO4jeMF8Gix0E6iC-hKPaKOR
- ETEL.CA: status=RECENT_ACCEPTED latest=2026-07-07 age_days=7 sources=3 expected=Telecom Egypt summary=Telecom Egypt (ETEL.CA) reported revenue of EGP 110.17 billion and profits of EGP 19.30 billion for the last 12 months ending July 07, 2026. The company's stock price has seen a significant increase of over 152% in the last 52 weeks. For Q1 2026, earnings were EGP 2.05 per share and revenue was EGP 28.2 billion. Telecom Egypt also announced its 2025 dividends and financial guidance for 2026.
  - Telecom Egypt Company (EGX:ETEL) Statistics & Valuation Metrics (July 07, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHS_A1undk28zhDMlsx9TInmzpGHHw3f5TK3tinNbCBgvCO5da0Bx1VvK9fQvYM93Bk47WExk4_Ju24eMSH7lxDc3hclpkS0dCXLzjzWQyV2Utw7xupiluAMUj4ZxAXzmuTjdw1KNFHCKbdFIjxHg==
  - Telecom Egypt (CASE:ETEL) - Stock Analysis - Simply Wall St (Q1 2026 Earnings, May 22, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWruiu_MERaYlPEy7ky2yrqvEl6AZIVa1SDz44bjnIVAU8CLuvKqh3wNvbURwDk7bTxUKoE7TBHXtZdqwoi39AyMA8vRYZofzAHjz0W99UAdJ8d1S3ptPYBipdmevHZEDeVUPHNjWZeel-Lg9i1geCrny1T084nvz8rI0w2mwO4w==
  - Telecom Egypt :: Investor Relations (FY 2025 Results, Q1 2026 Results May 21, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRT-HvV9LRLJEel25mvxdqglwT0pvu_C7szgqdlWVdXDgIkjmeFeZAWoCRkrtRmLsSgrskJ6f5j2pyCCXj3Gm1MjGlHmcOLvUL7FU=
- COSG.CA: status=RECENT_ACCEPTED latest=2026-07-07 age_days=7 sources=3 expected=Cairo Oil & Soap Company summary=Cairo Oil & Soap Company (COSG.CA) reported revenue of EGP 283.63 million for the quarter ending March 31, 2026, bringing its last twelve months' revenue to EGP 802.09 million. The company's total assets for Q1 2026 were EGP 805.26 million. Recent market announcements include board decisions and shareholder structure disclosures in July and April 2026.
  - Cairo Oil & Soap Company (EGX:COSG) Revenue - Stock Analysis (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGp4IF_QxFQfqoFxnDu5Y6OlBWJDEpNGS7ZeWm9mV5viANwfm4A9HoQK8xSE_cjg4QzyUd3WfvZ8uAUmZK10KxFNovwmE2YeHNIyhwjkDnAHbjW1lrQmwBTX-SE9vd_TvQaXqBORqoI7NtauA==
  - Cairo Oils and Soap (COSG) - Mubasher Info (Market Announcements: July 7, 2026, July 5, 2026, April 26, 2026, April 9, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzaZ9-xCfpDbfu3-Cz7Mj6jnYuPTueeaAmIhBGTqphdD0t5rSv6vDigPfogkoj3fXbYNaKbCvNk7PWKCAwoNuwj2gsGyPSZBc3bogM21ZZjqhWa4Yl1ipzu75M5F0l0LomPhH5pJN6yLvXz-pcdSRV
  - Cairo Oils & Soap Balance Sheet – EGX:COSG - TradingView (Q1 2026 Total Assets): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQaRdLDAzKPaNl5_QtG1WaX4r0VGghxDhHowt2YFOVywTmlO73onpFDkD3ON3FebML0cwyVelD2PrGgog4J3lblfAwEnd8usKbLsLPhunq8MKTfDL1PmAP294CITnFvgCXIThvWr-sBGqWOGPUuhEKw-_mEYBnk3TjzJXE2pnFjQ==
- ELSH.CA: status=RECENT_ACCEPTED latest=2026-07-04 age_days=10 sources=3 expected=Al Shams Housing and Urbanization SAE summary=Al Shams Housing and Urbanization SAE (ELSH.CA) reported profits of EGP 162.33 million on revenue of EGP 220.86 million for the last 12 months ending July 04, 2026. The company's stock price increased by over 56% in the last 52 weeks. Recent news includes a 6.8% YoY higher profit in Q1 2026 and the declaration of an annual dividend payable on June 29, 2026.
  - Al Shams Housing and Urbanization SAE (EGX:ELSH) Statistics & Valuation Metrics (July 04, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDZfBEIFsYsRrkH7tq-F2QavQ16lu_zFjaOnts7JtkK-UlPJlajIjS9X51pqUZKq6x0IWAgCwiZqi15-WTa8p0ioOMP23EuK99wAfx7tOkOUjCLN6I8KI4AkJbE64UDuV6ybBUbB-lBMO5_11sGw==
  - Al Shams Housing and Urbanization SAE (CASE:ELSH) - Stock Analysis - Simply Wall St (Dividend Declaration June 13, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDFpbYRHmYLke8sbU3RJrfv8Mp_ji0NDvrjU1xBhMqub5xZSjvlsDKkkVlhDUZcrOQLkURMJ9TGZpfdF1cMd5Pf8WMqxDBRVoPiSNsRwbCtGxjKKbSH8RfTpFEl6CYpTIwLdvgRjIq73Cvh-VG5Z4oDJ97gNX4DOhoeyEhic-EVQ39I_CSbVdV7U-JC55zxVBm-ZLUEPkVPhnxFMW_XYQR5qjZ3if4pS9toaBum1-Mx9cIaxd8iHo=
  - El Shams Housing & Urbanization (ELSH) - Mubasher Info (Q1 2026 Profits, June 3, 2026; 2025 Net Profits, Feb 17, 2026; 9-month Profits, Nov 12, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBtny5taVPGFCjCfFDH800jAXNMCIDidWSPzDM40r2LPmxzo2hpDReY3JsN0u61VpGFygyyLg8BoaTREZRPl_y6seMS-QwlIA-c8ijCh1LQDr-DYlG75_3du9yG6Me8M971bRK0GPKM8hDG95IW590
- MASR.CA: status=RECENT_ACCEPTED latest=2026-08-11 age_days=0 sources=3 expected=Madinet Masr For Housing and Development summary=Madinet Masr For Housing and Development (MASR.CA) reported a revenue of EGP 11.71 billion in 2025, a 38.40% increase from the previous year, with earnings of EGP 3.16 billion, up 24.55%. The company's Q1 2026 net income was EGP 594.19 million on a total revenue of EGP 3.02 billion. The next earnings date is projected for August 11, 2026.
  - Madinet Masr For Housing and Development (EGX:MASR) Stock Price & Overview (2025 Financial Performance, Next Earnings Aug 11, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqrvB2I6bOhshDYfQVHLX8AUBMRu7fdoJX3srl6eHb-e-Yu87DgtFSUFycrZTIHzFSzyKMJCgSeXV7hC33TP7KpkgW_TUh0QLX7HrdGzBQhwGxkl7qWw9hfttgLp_so0cBAaw=
  - Madinet Masr for Housing & Development Income Statement – EGX:MASR - TradingView (Q1 2026 Performance): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRfcCcs8NLHM16pAjNC02BUt2VYBoqCd1t4E1F4r1IfnpL-C0Z1BJaT512BC5VV6luoSoUnsqkP0tf0jwbNi11pifRKTrY67qWQxTyXaEw221F3GuLcf7aaFZ7xTTfyfcnjpUCAAh6OL-Uo3ox58UaRU8za4WHroyNj6n9c1Pq_YE9yA==
  - Madinet Masr For Housing and Development (EGX:MASR) Financials & Income Statement (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3UPQ1ClPSEnE7_9vOAuF2_eE3jBkgXihlqsjRfTjdC2E6BZtSoejvHaOxAMZJxFAIt12ZhHKaRj0_ysVXH8RU-tr-AaXqAjA7ciApLOSZcdfbjHChF82bcPW0BDoaCE-FvrEaEOFwmOOISuDw1w==
- ADPC.CA: status=RECENT_ACCEPTED latest=2026-06-30 age_days=14 sources=3 expected=The Arab Dairy Products Co. summary=The Arab Dairy Products Co. (ADPC.CA) reported a net loss of EGP 122.929 million on revenue of EGP 564.036 million for the latest quarter. The company's trailing twelve months (TTM) net profit margin is -8.739%. The company also reported its Q1 2026 earnings results on June 23, 2026.
  - ARAB DAIRY - EGX:ADPC Financials - Investing.com (Latest Quarter Performance): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzjhmy5c3Spq_JqjDGWktAJPLmjiykjc_V2JOBp3JU5UR80T7BGLytehdRqMH4KzqgtGeyMW_wJR1-oe3nSyD_qRoXjPT4ZAZSZoTcNJEmsmRLt6nw7d3uXzm-VnPyJVl2HWjF50X9ScfyfNORR47PSAb9Awg7UjiRyxQ8m9ykTdSYCiErAeTElMk=
  - The Arab Dairy Products Co. Stock (ADPC) - Quote Egyptian Exchange- MarketScreener (Q1 2026 Earnings, June 23, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7spFeYPF4ejGu0yUBgrdmJC6TQFtH59haCf8J8KOtJ29vQ9nXd0zj3QTjICnudlKXl3hYzCLbkEXt9RC-G3nQYj4avNMZGkqSDCNz89zHnvsIvVeq5ExEs4l4u7caGMnQRPDv2rO5ix7m_9RoA4YvlPfIrySHat07QFDFiBw4L5TWpWxRJLsn
  - GADWA for Industrial Development Announces its Consolidated Results for the period ended on the 31st of March, 2026 (June 30, 2026) - Mentions Arab Dairy as part of Gadwa's Food segment.: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHimS01vJuAzPKaF0bDBp1d5mHQlOxb5gtJlA2-Ga-cbo2vkc25bo0VSPQsQhfDiaZ7UZk80kGVH7cgf5Fwkpx5JheC3QV-eQRJvJwe52TLbq2Tlu6Y79JHctIodfWY2enWAHBDDYeut-adCAWH

## Warnings
- Evidence for AREH.CA matches the company but no source/report date was detected.
