# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-08-16T08:25:41.249083+00:00
Generated Cairo: 2026-08-16 11:25
Run timing: target 11:00 Cairo | generated Cairo 2026-08-16 11:25 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-08-16 11:21

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 57
- Data quality issues: 1
- Tradeable price/liquidity tickers: 174/189
- Top sector: Transportation & Logistics

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, August 16
- Freshness: DELAYED
- EGX30 regime: CONSTRUCTIVE / above MA20 73.68% / above MA50 73.68%
- EGX70 regime: BULLISH / above MA20 74.29% / above MA50 91.43%
- Sector breadth: 66.67%
- Risk mode: BROAD_RISK_ON

## Top Liquidity
- ETEL.CA: liquidity=184484512.0 spike=1.5 score=30.9
- GTWL.CA: liquidity=156823536.0 spike=1.0 score=10.9
- ORAS.CA: liquidity=137321936.0 spike=1.0 score=9.1
- EGCH.CA: liquidity=127446224.0 spike=1.08 score=25.06
- AMOC.CA: liquidity=123211848.0 spike=1.12 score=10.48

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 is constructive and EGX70 bullish with ~67% sector breadth, keeping risk mode in broad risk‑on; the scanner favors buy setups but flags low confidence due to extended momentum and cooling liquidity.
- ETEL.CA (Telecom) trades above its MA20/MA50 with RSI ~64, near resistance and showing an accumulation liquidity spike; outlook is bullish watch, yet momentum is extended and the sector is not leading.
- COSG.CA (Oil & Soap) also sits above MA20/MA50, RSI ~64, with liquidity cooling and a constructive outlook; sector weakness and extended momentum temper the signal.
- SCEM.CA (Building Materials) is far above its 20‑day support, liquidity cooling, RSI ~64, and carries a bullish watch outlook; again momentum is extended and the sector lacks leadership.
- All three tickets receive low confidence scores; traders should verify price action on Thndr and remain alert for sudden shifts in liquidity or sector rotation.

## Top Liquidity Spikes
- TRTO.CA: spike=9.37 liquidity=21261.14 outlook=CONSTRUCTIVE score=52.04 buy_ready=False
- NAHO.CA: spike=9.22 liquidity=260089.59 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- KABO.CA: spike=3.56 liquidity=121049248.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MOIN.CA: spike=2.82 liquidity=72740152.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SPIN.CA: spike=2.57 liquidity=75682664.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Transportation & Logistics: score=13.87 5d=8.95% 20d=18.85% aboveMA50=100.0%
- #2 Building Materials: score=12.79 5d=9.74% 20d=19.5% aboveMA50=83.33%
- #3 Education: score=11.89 5d=4.4% 20d=19.39% aboveMA50=100.0%
- #4 Healthcare: score=11.71 5d=1.24% 20d=24.86% aboveMA50=100.0%
- #5 Agriculture & Food Production: score=11.63 5d=6.85% 20d=12.6% aboveMA50=100.0%
- #6 Tourism & Leisure: score=10.75 5d=11.05% 20d=15.02% aboveMA50=0.0%
- #7 Basic Resources & Chemicals: score=8.87 5d=4.33% 20d=5.83% aboveMA50=90.0%
- #8 Banking & Financials: score=8.81 5d=3.32% 20d=11.68% aboveMA50=80.0%

## Today's Prioritized Action Tickets
- Priority #1: BUY ETEL.CA
  - Entry: 117.9 | Take profit: 127.34 | Stop loss: 113.18
  - Confidence: LOW | score=30.9 | outlook=BULLISH_WATCH 78.43
  - Reason: BUY SETUP: ETEL.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 64.46, support 97.0, resistance 116.25, and evidence sources. Macro trend is Bullish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY COSG.CA
  - Entry: 1.86 | Take profit: 2.0 | Stop loss: 1.79
  - Confidence: LOW | score=29.9 | outlook=CONSTRUCTIVE 66.04
  - Reason: BUY SETUP: COSG.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 64.29, support 1.6, resistance 1.93, and evidence sources. Macro trend is Bullish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY SCEM.CA
  - Entry: 97.89 | Take profit: 112.44 | Stop loss: 93.97
  - Confidence: LOW | score=29.9 | outlook=BULLISH_WATCH 78
  - Reason: BUY SETUP: SCEM.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 63.85, support 61.97, resistance 113.0, and evidence sources. Macro trend is Bullish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- SCTS.CA: BULLISH_WATCH score=96 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- APSW.CA: BULLISH_WATCH score=89.04 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- CLHO.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ISMQ.CA: BULLISH_WATCH score=78.87 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ETEL.CA: BULLISH_WATCH score=78.43 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support; sector is not leading
- EALR.CA: BULLISH_WATCH score=78.04 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- NHPS.CA: BULLISH_WATCH score=78.04 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- WKOL.CA: BULLISH_WATCH score=78.04 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- MFSC.CA: BULLISH_WATCH score=78.04 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- MPRC.CA: BULLISH_WATCH score=78.04 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- ETEL.CA: rank=30.9 outlook=BULLISH_WATCH outlook_score=78.43 sector_rank=13 price=117.9 support=97.0 resistance=116.25 liquidity=184484512.0
- COSG.CA: rank=29.9 outlook=CONSTRUCTIVE outlook_score=66.04 sector_rank=10 price=1.86 support=1.6 resistance=1.93 liquidity=24941100.0
- SCEM.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=78 sector_rank=2 price=97.89 support=61.97 resistance=113.0 liquidity=107773408.0
- EFIH.CA: rank=27.9 outlook=CONSTRUCTIVE outlook_score=61.42 sector_rank=9 price=24.7 support=21.9 resistance=25.0 liquidity=80113288.0
- MTIE.CA: rank=27.9 outlook=BULLISH_WATCH outlook_score=71.39 sector_rank=14 price=9.57 support=8.01 resistance=10.4 liquidity=11270342.0
- EHDR.CA: rank=27.9 outlook=CONSTRUCTIVE outlook_score=66.04 sector_rank=10 price=3.05 support=2.69 resistance=3.19 liquidity=15864910.0
- EPCO.CA: rank=27.9 outlook=CONSTRUCTIVE outlook_score=68.04 sector_rank=10 price=12.24 support=10.11 resistance=13.05 liquidity=22854396.0
- GGCC.CA: rank=27.9 outlook=CONSTRUCTIVE outlook_score=68.04 sector_rank=10 price=1.0 support=0.64 resistance=1.28 liquidity=20811586.0
- RACC.CA: rank=27.9 outlook=CONSTRUCTIVE outlook_score=66.04 sector_rank=10 price=10.49 support=9.8 resistance=10.6 liquidity=11192284.0
- SKPC.CA: rank=26.9 outlook=CONSTRUCTIVE outlook_score=59.87 sector_rank=7 price=16.93 support=14.8 resistance=16.93 liquidity=34632520.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=25.52 buy_ready=True sector_rank=10 price=307.0 support=227.0 resistance=325.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=68.47 liquidity=9618455.0 spike=0.24
- ABUK.CA: score=24.9 buy_ready=False sector_rank=7 price=79.8 support=70.6 resistance=78.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=78.91 liquidity=75290416.0 spike=0.5
- ACAMD.CA: score=23.9 buy_ready=False sector_rank=10 price=2.28 support=2.2 resistance=2.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=40.53 liquidity=26780374.0 spike=0.47
- ACGC.CA: score=13.12 buy_ready=False sector_rank=16 price=13.2 support=12.31 resistance=13.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=78926096.0 spike=2.28
- ADCI.CA: score=18.48 buy_ready=True sector_rank=10 price=308.05 support=234.1 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=66.43 liquidity=2577083.5 spike=0.12
- ADIB.CA: score=24.9 buy_ready=False sector_rank=8 price=55.14 support=46.02 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=83.43 liquidity=23437874.0 spike=0.2
- ADPC.CA: score=25.22 buy_ready=True sector_rank=10 price=4.43 support=3.76 resistance=4.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=66.15 liquidity=9317303.0 spike=0.18
- AFDI.CA: score=16.89 buy_ready=False sector_rank=10 price=65.83 support=46.4 resistance=69.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=83.6 liquidity=3993674.75 spike=0.16
- AFMC.CA: score=20.44 buy_ready=False sector_rank=10 price=235.82 support=73.75 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=75.09 liquidity=7536735.5 spike=0.05
- AJWA.CA: score=27.9 buy_ready=False sector_rank=10 price=199.0 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=70.98 liquidity=32197290.0 spike=0.82
- ALCN.CA: score=27.9 buy_ready=False sector_rank=1 price=32.26 support=28.8 resistance=32.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=76.0 liquidity=15992708.0 spike=0.61
- ALUM.CA: score=19.99 buy_ready=False sector_rank=10 price=27.97 support=22.7 resistance=30.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=80.68 liquidity=7086153.5 spike=0.38
- AMER.CA: score=22.9 buy_ready=False sector_rank=12 price=6.76 support=3.18 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=75.81 liquidity=45586600.0 spike=0.39
- AMES.CA: score=17.39 buy_ready=True sector_rank=10 price=122.25 support=106.59 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=54.58 liquidity=1490112.5 spike=0.02
- AMIA.CA: score=15.69 buy_ready=False sector_rank=10 price=13.09 support=8.81 resistance=13.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:55 AM market time freshness=DELAYED_CURRENT RSI=85.42 liquidity=792247.13 spike=0.05
- AMOC.CA: score=10.48 buy_ready=False sector_rank=17 price=11.05 support=10.61 resistance=11.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=123211848.0 spike=1.12
- APSW.CA: score=21.64 buy_ready=True sector_rank=10 price=9.13 support=8.32 resistance=9.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=48.85 liquidity=3542753.5 spike=2.1
- ARAB.CA: score=25.9 buy_ready=True sector_rank=12 price=0.25 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=47.5 liquidity=19458256.0 spike=0.18
- ARCC.CA: score=24.9 buy_ready=False sector_rank=2 price=76.31 support=54.2 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=83.42 liquidity=59446560.0 spike=0.68
- AREH.CA: score=13.33 buy_ready=False sector_rank=10 price=1.51 support=1.38 resistance=1.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=52.27 liquidity=2425407.0 spike=0.06
- ARVA.CA: score=4.9 buy_ready=False sector_rank=10 price=12.35 support=12.35 resistance=12.35 source=Yahoo Finance as_of=2026-08-12T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=0.0 spike=0.0
- ASCM.CA: score=17.61 buy_ready=True sector_rank=10 price=65.83 support=60.63 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=67.34 liquidity=3712240.25 spike=0.06
- ASPI.CA: score=10.9 buy_ready=False sector_rank=10 price=0.56 support=0.5 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40028656.0 spike=0.91
- ATLC.CA: score=19.05 buy_ready=True sector_rank=18 price=5.5 support=5.0 resistance=5.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=65.19 liquidity=4093135.75 spike=0.23
- ATQA.CA: score=23.79 buy_ready=False sector_rank=7 price=10.9 support=9.49 resistance=11.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=73.3 liquidity=7889075.5 spike=0.14
- AXPH.CA: score=22.28 buy_ready=True sector_rank=10 price=1354.34 support=1121.56 resistance=1460.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=63.19 liquidity=4382030.0 spike=0.92
- BINV.CA: score=14.1 buy_ready=False sector_rank=15 price=49.13 support=46.01 resistance=50.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:01 AM market time freshness=DELAYED_CURRENT RSI=73.07 liquidity=381015.66 spike=0.06
- BIOC.CA: score=24.9 buy_ready=False sector_rank=10 price=508.94 support=73.23 resistance=563.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=84.67 liquidity=35652140.0 spike=0.17
- BTFH.CA: score=22.95 buy_ready=False sector_rank=18 price=3.09 support=3.03 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=51.22 liquidity=12617594.0 spike=0.06
- CAED.CA: score=21.35 buy_ready=True sector_rank=10 price=128.04 support=93.2 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=57.49 liquidity=5445835.0 spike=0.08
- CANA.CA: score=24.9 buy_ready=False sector_rank=8 price=42.11 support=35.45 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=79.9 liquidity=10201212.0 spike=0.49
- CCAP.CA: score=23.72 buy_ready=False sector_rank=15 price=5.3 support=5.14 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=38.68 liquidity=37838092.0 spike=0.06
- CCRS.CA: score=16.36 buy_ready=False sector_rank=10 price=2.56 support=2.44 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=26.09 liquidity=5458237.5 spike=0.29
- CEFM.CA: score=17.03 buy_ready=True sector_rank=10 price=134.36 support=103.01 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=63.74 liquidity=1130727.88 spike=0.04
- CERA.CA: score=17.72 buy_ready=False sector_rank=10 price=1.33 support=1.25 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=45.0 liquidity=3818061.5 spike=0.19
- CFGH.CA: score=9.9 buy_ready=False sector_rank=10 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-08-12T21:00:00+00:00 freshness=FRESH RSI=53.33 liquidity=809.79 spike=0.05
- CICH.CA: score=15.65 buy_ready=False sector_rank=18 price=12.7 support=11.77 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=61.68 liquidity=696339.75 spike=0.09
- CIEB.CA: score=26.22 buy_ready=True sector_rank=8 price=24.47 support=23.75 resistance=24.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=56.5 liquidity=8322351.5 spike=0.72
- CIRA.CA: score=23.52 buy_ready=False sector_rank=3 price=39.05 support=31.0 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=73.97 liquidity=6621677.5 spike=0.11
- CLHO.CA: score=19.58 buy_ready=True sector_rank=4 price=17.28 support=16.0 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=55.53 liquidity=3679317.75 spike=0.07
- CNFN.CA: score=16.15 buy_ready=True sector_rank=18 price=4.95 support=4.68 resistance=5.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=1196481.13 spike=0.05
- COMI.CA: score=23.9 buy_ready=False sector_rank=8 price=138.7 support=132.81 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=52.62 liquidity=40696588.0 spike=0.1
- COPR.CA: score=12.04 buy_ready=False sector_rank=10 price=0.46 support=0.44 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=59033260.0 spike=1.57
- COSG.CA: score=29.9 buy_ready=True sector_rank=10 price=1.86 support=1.6 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=64.29 liquidity=24941100.0 spike=0.5
- CPCI.CA: score=16.88 buy_ready=False sector_rank=10 price=536.25 support=430.03 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=71.17 liquidity=983038.69 spike=0.06
- CSAG.CA: score=18.02 buy_ready=False sector_rank=1 price=41.73 support=31.35 resistance=43.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=83.67 liquidity=2119338.5 spike=0.08
- DAPH.CA: score=21.07 buy_ready=False sector_rank=10 price=127.04 support=82.77 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=80.08 liquidity=8173367.5 spike=0.21
- DEIN.CA: score=0.9 buy_ready=False sector_rank=10 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=18.77 buy_ready=True sector_rank=11 price=29.01 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=65.52 liquidity=2870060.75 spike=0.2
- DSCW.CA: score=25.9 buy_ready=True sector_rank=10 price=2.14 support=1.84 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=68.29 liquidity=24255016.0 spike=0.25
- DTPP.CA: score=25.9 buy_ready=True sector_rank=10 price=294.56 support=201.21 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=69.83 liquidity=13041952.0 spike=0.21
- EALR.CA: score=23.71 buy_ready=True sector_rank=10 price=393.67 support=360.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=60.24 liquidity=5809789.0 spike=0.18
- EASB.CA: score=13.77 buy_ready=False sector_rank=10 price=7.42 support=6.71 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=20.37 liquidity=2873169.75 spike=0.29
- EAST.CA: score=13.2 buy_ready=False sector_rank=11 price=36.38 support=36.01 resistance=37.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:01 AM market time freshness=DELAYED_CURRENT RSI=41.3 liquidity=1304957.38 spike=0.02
- EBSC.CA: score=14.33 buy_ready=False sector_rank=10 price=1.91 support=1.85 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=425158.0 spike=0.07
- ECAP.CA: score=17.52 buy_ready=True sector_rank=10 price=38.74 support=32.12 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=69.38 liquidity=1620710.13 spike=0.14
- EDFM.CA: score=16.41 buy_ready=False sector_rank=10 price=410.59 support=349.02 resistance=430.0 source=Yahoo Finance as_of=2026-08-12T21:00:00+00:00 freshness=FRESH RSI=69.25 liquidity=512826.91 spike=0.1
- EEII.CA: score=21.04 buy_ready=True sector_rank=10 price=3.07 support=2.54 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=64.04 liquidity=3137404.25 spike=0.16
- EFIC.CA: score=26.44 buy_ready=False sector_rank=7 price=228.0 support=184.0 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=76.15 liquidity=62463688.0 spike=1.77
- EFID.CA: score=24.9 buy_ready=False sector_rank=11 price=33.64 support=26.64 resistance=32.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=84.63 liquidity=42961172.0 spike=0.49
- EFIH.CA: score=27.9 buy_ready=True sector_rank=9 price=24.7 support=21.9 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=57.46 liquidity=80113288.0 spike=0.76
- EGAL.CA: score=22.9 buy_ready=False sector_rank=7 price=329.65 support=292.0 resistance=358.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=77.82 liquidity=23488410.0 spike=0.25
- EGAS.CA: score=21.23 buy_ready=False sector_rank=17 price=60.17 support=50.0 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=71.1 liquidity=5989337.0 spike=0.21
- EGBE.CA: score=13.91 buy_ready=False sector_rank=8 price=0.55 support=0.44 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:59 AM market time freshness=DELAYED_CURRENT RSI=66.47 liquidity=11349.54 spike=0.08
- EGCH.CA: score=25.06 buy_ready=False sector_rank=7 price=14.76 support=12.69 resistance=14.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=77.14 liquidity=127446224.0 spike=1.08
- EGSA.CA: score=5.91 buy_ready=False sector_rank=13 price=8.66 support=8.65 resistance=9.21 source=Yahoo Finance as_of=2026-08-12T21:00:00+00:00 freshness=FRESH RSI=18.37 liquidity=7750.7 spike=0.44
- EGTS.CA: score=23.15 buy_ready=True sector_rank=12 price=19.09 support=17.11 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=66.38 liquidity=7248509.0 spike=0.18
- EHDR.CA: score=27.9 buy_ready=True sector_rank=10 price=3.05 support=2.69 resistance=3.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=53.09 liquidity=15864910.0 spike=0.35
- EKHO.CA: score=9.24 buy_ready=False sector_rank=17 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-12T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=20.43 buy_ready=False sector_rank=19 price=2.18 support=2.12 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=8838803.0 spike=0.12
- ELKA.CA: score=18.81 buy_ready=False sector_rank=10 price=1.78 support=1.69 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=26.79 liquidity=9910649.0 spike=0.12
- ELNA.CA: score=12.15 buy_ready=False sector_rank=10 price=37.88 support=36.5 resistance=39.49 source=Yahoo Finance as_of=2026-08-12T21:00:00+00:00 freshness=FRESH RSI=36.33 liquidity=253796.01 spike=0.58
- ELSH.CA: score=13.96 buy_ready=False sector_rank=10 price=13.97 support=13.31 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=33.78 liquidity=5057861.5 spike=0.06
- ELWA.CA: score=8.47 buy_ready=False sector_rank=10 price=1.75 support=1.65 resistance=2.09 source=Yahoo Finance as_of=2026-08-12T21:00:00+00:00 freshness=FRESH RSI=28.95 liquidity=571070.5 spike=0.4
- EMFD.CA: score=23.95 buy_ready=False sector_rank=12 price=11.76 support=11.08 resistance=12.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=52.69 liquidity=9045439.0 spike=0.15
- ENGC.CA: score=16.28 buy_ready=False sector_rank=10 price=49.48 support=40.11 resistance=51.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=75.88 liquidity=1376774.88 spike=0.05
- EOSB.CA: score=19.93 buy_ready=False sector_rank=10 price=1.55 support=1.53 resistance=1.62 source=Yahoo Finance as_of=2026-08-12T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=30970.55 spike=0.64
- EPCO.CA: score=27.9 buy_ready=True sector_rank=10 price=12.24 support=10.11 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=56.69 liquidity=22854396.0 spike=0.67
- EPPK.CA: score=6.21 buy_ready=False sector_rank=10 price=13.18 support=12.62 resistance=15.93 source=Yahoo Finance as_of=2026-08-12T21:00:00+00:00 freshness=FRESH RSI=11.85 liquidity=306329.57 spike=0.36
- ETEL.CA: score=30.9 buy_ready=True sector_rank=13 price=117.9 support=97.0 resistance=116.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=64.46 liquidity=184484512.0 spike=1.5
- ETRS.CA: score=25.9 buy_ready=False sector_rank=10 price=11.08 support=10.21 resistance=10.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=72.75 liquidity=18916048.0 spike=0.76
- EXPA.CA: score=24.9 buy_ready=False sector_rank=8 price=21.4 support=18.8 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=76.36 liquidity=10629559.0 spike=0.29
- FAIT.CA: score=16.76 buy_ready=False sector_rank=8 price=41.12 support=36.1 resistance=40.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=82.34 liquidity=1857952.25 spike=0.5
- FAITA.CA: score=12.91 buy_ready=False sector_rank=8 price=0.98 support=0.96 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=61.73 liquidity=7346.52 spike=0.16
- FERC.CA: score=17.92 buy_ready=False sector_rank=7 price=81.62 support=75.01 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=72.32 liquidity=2018395.38 spike=0.14
- FWRY.CA: score=25.9 buy_ready=True sector_rank=9 price=19.37 support=18.43 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=51.74 liquidity=56374904.0 spike=0.45
- GBCO.CA: score=25.9 buy_ready=False sector_rank=14 price=30.43 support=29.53 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=53.93 liquidity=23720374.0 spike=0.38
- GDWA.CA: score=13.01 buy_ready=False sector_rank=10 price=0.81 support=0.8 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=20.62 liquidity=8111536.5 spike=0.08
- GGCC.CA: score=27.9 buy_ready=True sector_rank=10 price=1.0 support=0.64 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=58.32 liquidity=20811586.0 spike=0.44
- GIHD.CA: score=25.9 buy_ready=True sector_rank=10 price=66.02 support=48.72 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=67.23 liquidity=10801291.0 spike=0.23
- GMCI.CA: score=11.63 buy_ready=False sector_rank=10 price=1.9 support=1.88 resistance=2.12 source=Yahoo Finance as_of=2026-08-12T21:00:00+00:00 freshness=FRESH RSI=39.13 liquidity=669464.99 spike=1.03
- GRCA.CA: score=15.1 buy_ready=False sector_rank=10 price=56.4 support=51.6 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=36.93 liquidity=1199800.75 spike=0.08
- GSSC.CA: score=14.67 buy_ready=False sector_rank=10 price=279.04 support=258.15 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=65.23 liquidity=773680.63 spike=0.04
- GTWL.CA: score=10.9 buy_ready=False sector_rank=10 price=149.33 support=133.35 resistance=160.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=156823536.0 spike=1.0
- HDBK.CA: score=20.44 buy_ready=False sector_rank=8 price=86.94 support=76.96 resistance=87.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=84.98 liquidity=9542539.0 spike=0.26
- HELI.CA: score=23.9 buy_ready=False sector_rank=12 price=7.84 support=7.4 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=36.53 liquidity=14852203.0 spike=0.09
- HRHO.CA: score=20.95 buy_ready=False sector_rank=18 price=26.75 support=25.95 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=48.5 liquidity=19840676.0 spike=0.21
- ICID.CA: score=27.4 buy_ready=False sector_rank=10 price=13.1 support=7.83 resistance=13.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=93.87 liquidity=33090344.0 spike=2.25
- IDRE.CA: score=20.37 buy_ready=True sector_rank=10 price=54.91 support=44.52 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:01 AM market time freshness=DELAYED_CURRENT RSI=67.41 liquidity=4468166.5 spike=0.15
- IFAP.CA: score=18.14 buy_ready=False sector_rank=5 price=21.5 support=19.0 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=76.55 liquidity=5242538.0 spike=0.23
- INFI.CA: score=22.9 buy_ready=False sector_rank=10 price=155.0 support=100.0 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=77.19 liquidity=12166693.0 spike=0.24
- IRON.CA: score=12.42 buy_ready=False sector_rank=7 price=31.1 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=49.69 liquidity=2518113.0 spike=0.27
- ISMA.CA: score=17.87 buy_ready=False sector_rank=10 price=34.01 support=27.1 resistance=36.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=77.86 liquidity=2974198.0 spike=0.11
- ISMQ.CA: score=23.25 buy_ready=True sector_rank=7 price=9.57 support=8.96 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=53.85 liquidity=5353916.5 spike=0.08
- ISPH.CA: score=25.9 buy_ready=True sector_rank=4 price=13.57 support=11.2 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=67.78 liquidity=10172607.0 spike=0.06
- JUFO.CA: score=21.55 buy_ready=False sector_rank=11 price=27.3 support=22.78 resistance=30.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=40.64 liquidity=6651076.0 spike=0.12
- KABO.CA: score=15.56 buy_ready=False sector_rank=16 price=9.41 support=8.77 resistance=9.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=121049248.0 spike=3.56
- KWIN.CA: score=10.3 buy_ready=False sector_rank=10 price=86.66 support=71.25 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=28.43 liquidity=1402702.13 spike=0.03
- KZPC.CA: score=25.62 buy_ready=False sector_rank=10 price=10.9 support=8.42 resistance=10.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=87.35 liquidity=16263519.0 spike=1.36
- LCSW.CA: score=21.72 buy_ready=False sector_rank=2 price=33.35 support=30.2 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=41.64 liquidity=5820757.0 spike=0.14
- LUTS.CA: score=22.9 buy_ready=False sector_rank=10 price=0.99 support=0.54 resistance=1.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=83.89 liquidity=38730948.0 spike=0.62
- MAAL.CA: score=15.44 buy_ready=False sector_rank=10 price=8.63 support=8.22 resistance=9.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=47.78 liquidity=1537715.0 spike=0.1
- MASR.CA: score=18.9 buy_ready=False sector_rank=10 price=7.6 support=7.45 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=29.49 liquidity=16541550.0 spike=0.21
- MBSC.CA: score=13.6 buy_ready=False sector_rank=2 price=401.28 support=382.0 resistance=405.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=87695672.0 spike=1.35
- MCQE.CA: score=24.9 buy_ready=False sector_rank=2 price=253.89 support=175.51 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=80.96 liquidity=30242320.0 spike=0.75
- MCRO.CA: score=25.9 buy_ready=True sector_rank=10 price=1.57 support=1.32 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=13142221.0 spike=0.07
- MENA.CA: score=19.11 buy_ready=False sector_rank=12 price=7.01 support=6.83 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=61.02 liquidity=3210819.5 spike=0.52
- MEPA.CA: score=17.2 buy_ready=True sector_rank=10 price=1.87 support=1.65 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=47.73 liquidity=1299783.25 spike=0.02
- MFPC.CA: score=24.9 buy_ready=False sector_rank=7 price=41.13 support=35.37 resistance=40.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=77.82 liquidity=75145320.0 spike=0.85
- MFSC.CA: score=18.39 buy_ready=True sector_rank=10 price=51.2 support=45.95 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=56.01 liquidity=2493929.25 spike=0.2
- MHOT.CA: score=17.57 buy_ready=False sector_rank=6 price=18.9 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=63.66 liquidity=3670341.25 spike=0.22
- MICH.CA: score=23.81 buy_ready=True sector_rank=10 price=48.02 support=37.6 resistance=53.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=67.37 liquidity=7906880.5 spike=0.23
- MILS.CA: score=17.91 buy_ready=True sector_rank=10 price=191.35 support=135.3 resistance=211.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=60.57 liquidity=2013242.75 spike=0.03
- MIPH.CA: score=17.65 buy_ready=True sector_rank=4 price=773.73 support=709.95 resistance=828.36 source=Yahoo Finance as_of=2026-08-12T21:00:00+00:00 freshness=FRESH RSI=62.17 liquidity=1746308.57 spike=0.41
- MOED.CA: score=14.47 buy_ready=False sector_rank=10 price=0.69 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=32.0 liquidity=9573073.0 spike=0.27
- MOIL.CA: score=13.31 buy_ready=False sector_rank=17 price=0.66 support=0.53 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=74.14 liquidity=76999.55 spike=0.12
- MOIN.CA: score=14.54 buy_ready=False sector_rank=10 price=38.74 support=34.2 resistance=40.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=72740152.0 spike=2.82
- MOSC.CA: score=24.9 buy_ready=False sector_rank=10 price=325.0 support=277.42 resistance=370.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=87.05 liquidity=10684658.0 spike=0.55
- MPCI.CA: score=25.9 buy_ready=False sector_rank=10 price=382.36 support=242.02 resistance=460.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=73.12 liquidity=20716444.0 spike=0.14
- MPCO.CA: score=25.9 buy_ready=False sector_rank=5 price=2.2 support=1.82 resistance=2.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=74.58 liquidity=28209118.0 spike=0.27
- MPRC.CA: score=18.1 buy_ready=True sector_rank=10 price=46.58 support=42.02 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=56.52 liquidity=2199064.25 spike=0.08
- MTIE.CA: score=27.9 buy_ready=True sector_rank=14 price=9.57 support=8.01 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=52.66 liquidity=11270342.0 spike=0.23
- NAHO.CA: score=6.16 buy_ready=False sector_rank=10 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:59 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=260089.59 spike=9.22
- NCCW.CA: score=14.62 buy_ready=False sector_rank=10 price=6.02 support=5.67 resistance=7.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=3718678.25 spike=0.1
- NEDA.CA: score=11.26 buy_ready=False sector_rank=10 price=2.7 support=2.7 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=357278.75 spike=0.48
- NHPS.CA: score=22.05 buy_ready=True sector_rank=10 price=90.5 support=82.1 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=6146165.5 spike=0.09
- NINH.CA: score=17.93 buy_ready=False sector_rank=10 price=21.91 support=17.86 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=51.29 liquidity=4031132.0 spike=0.07
- NIPH.CA: score=22.9 buy_ready=False sector_rank=4 price=402.34 support=186.3 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=79.34 liquidity=78287464.0 spike=0.27
- OBRI.CA: score=10.38 buy_ready=False sector_rank=10 price=32.82 support=31.61 resistance=36.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=31.61 liquidity=3483296.25 spike=0.11
- OCDI.CA: score=24.9 buy_ready=False sector_rank=12 price=35.02 support=26.56 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=93.51 liquidity=16005683.0 spike=0.12
- OCPH.CA: score=14.34 buy_ready=False sector_rank=10 price=280.59 support=225.0 resistance=496.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=27.48 liquidity=6437496.5 spike=0.18
- ODIN.CA: score=22.59 buy_ready=False sector_rank=10 price=3.42 support=2.41 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=73.42 liquidity=6687493.5 spike=0.19
- OFH.CA: score=22.57 buy_ready=False sector_rank=10 price=0.88 support=0.64 resistance=0.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=9673488.0 spike=0.11
- OIH.CA: score=22.05 buy_ready=False sector_rank=15 price=1.79 support=1.41 resistance=1.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=92.5 liquidity=7330974.0 spike=0.07
- OLFI.CA: score=23.33 buy_ready=True sector_rank=11 price=24.84 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=62.63 liquidity=5433285.0 spike=0.08
- ORAS.CA: score=9.1 buy_ready=False sector_rank=20 price=767.1 support=751.5 resistance=772.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=137321936.0 spike=1.0
- ORHD.CA: score=27.9 buy_ready=False sector_rank=12 price=43.06 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=74.71 liquidity=25345764.0 spike=0.15
- ORWE.CA: score=22.56 buy_ready=False sector_rank=16 price=26.59 support=22.5 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=79.01 liquidity=25725556.0 spike=0.35
- PHAR.CA: score=25.9 buy_ready=False sector_rank=4 price=142.14 support=86.0 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=73.1 liquidity=93352680.0 spike=0.25
- PHDC.CA: score=25.9 buy_ready=True sector_rank=12 price=15.3 support=14.32 resistance=15.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=66.28 liquidity=11400383.0 spike=0.05
- PHTV.CA: score=3.68 buy_ready=False sector_rank=10 price=364.42 support=361.0 resistance=390.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2721063.5 spike=1.03
- POUL.CA: score=21.9 buy_ready=True sector_rank=11 price=38.93 support=36.5 resistance=40.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=57.73 liquidity=3995179.75 spike=0.14
- PRCL.CA: score=14.96 buy_ready=False sector_rank=2 price=33.51 support=32.76 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=31.31 liquidity=4062052.5 spike=0.12
- PRDC.CA: score=20.41 buy_ready=False sector_rank=12 price=8.98 support=8.7 resistance=10.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=37.67 liquidity=6505340.5 spike=0.06
- PRMH.CA: score=16.95 buy_ready=False sector_rank=10 price=2.66 support=2.56 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=4049886.75 spike=0.28
- RACC.CA: score=27.9 buy_ready=True sector_rank=10 price=10.49 support=9.8 resistance=10.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=66.0 liquidity=11192284.0 spike=0.46
- RAKT.CA: score=12.13 buy_ready=False sector_rank=10 price=22.63 support=21.66 resistance=24.0 source=Yahoo Finance as_of=2026-08-12T21:00:00+00:00 freshness=FRESH RSI=49.49 liquidity=229219.26 spike=0.89
- RAYA.CA: score=11.9 buy_ready=False sector_rank=21 price=7.15 support=6.97 resistance=8.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=19.77 liquidity=17650462.0 spike=0.18
- RMDA.CA: score=22.16 buy_ready=False sector_rank=4 price=6.54 support=4.95 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=73.31 liquidity=6255858.0 spike=0.05
- ROTO.CA: score=24.9 buy_ready=False sector_rank=10 price=51.63 support=40.5 resistance=51.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=79.44 liquidity=18382848.0 spike=0.78
- RREI.CA: score=25.5 buy_ready=True sector_rank=10 price=4.5 support=3.72 resistance=4.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=63.16 liquidity=9599326.0 spike=0.15
- RTVC.CA: score=12.21 buy_ready=False sector_rank=10 price=3.82 support=3.73 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:01 AM market time freshness=DELAYED_CURRENT RSI=36.99 liquidity=1311257.0 spike=0.28
- RUBX.CA: score=12.15 buy_ready=False sector_rank=10 price=12.56 support=12.02 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=30.98 liquidity=3246017.0 spike=0.1
- SAUD.CA: score=22.83 buy_ready=True sector_rank=8 price=23.31 support=21.3 resistance=23.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=63.37 liquidity=2929563.5 spike=0.17
- SCEM.CA: score=29.9 buy_ready=True sector_rank=2 price=97.89 support=61.97 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=63.85 liquidity=107773408.0 spike=0.65
- SCFM.CA: score=17.73 buy_ready=True sector_rank=10 price=286.3 support=252.2 resistance=319.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:02 AM market time freshness=DELAYED_CURRENT RSI=55.04 liquidity=1827358.38 spike=0.07
- SCTS.CA: score=20.18 buy_ready=True sector_rank=3 price=617.35 support=602.0 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=51.27 liquidity=1283556.5 spike=0.17
- SDTI.CA: score=16.27 buy_ready=False sector_rank=10 price=70.1 support=46.6 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=80.95 liquidity=3366690.0 spike=0.12
- SEIG.CA: score=15.56 buy_ready=False sector_rank=10 price=282.68 support=237.0 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=87.07 liquidity=663933.5 spike=0.05
- SIPC.CA: score=18.66 buy_ready=False sector_rank=10 price=4.64 support=3.47 resistance=5.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=70.19 liquidity=2761982.5 spike=0.05
- SKPC.CA: score=26.9 buy_ready=True sector_rank=7 price=16.93 support=14.8 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=64.85 liquidity=34632520.0 spike=0.74
- SMFR.CA: score=20.18 buy_ready=False sector_rank=10 price=267.05 support=223.0 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=71.76 liquidity=4279264.0 spike=0.11
- SNFC.CA: score=16.77 buy_ready=False sector_rank=10 price=11.03 support=10.6 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=37.61 liquidity=3871727.75 spike=0.32
- SPIN.CA: score=13.7 buy_ready=False sector_rank=16 price=19.44 support=16.5 resistance=19.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=75682664.0 spike=2.57
- SPMD.CA: score=22.23 buy_ready=True sector_rank=10 price=0.49 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=65.09 liquidity=8326094.0 spike=0.25
- SUGR.CA: score=26.06 buy_ready=True sector_rank=11 price=51.06 support=46.47 resistance=51.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=67.01 liquidity=15315692.0 spike=1.08
- SVCE.CA: score=25.9 buy_ready=False sector_rank=10 price=11.04 support=9.06 resistance=12.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=73.96 liquidity=53623560.0 spike=0.57
- SWDY.CA: score=10.27 buy_ready=False sector_rank=19 price=114.0 support=108.0 resistance=114.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=86571568.0 spike=1.34
- TALM.CA: score=23.77 buy_ready=False sector_rank=3 price=19.53 support=15.6 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=75.35 liquidity=9870021.0 spike=0.23
- TMGH.CA: score=23.9 buy_ready=False sector_rank=12 price=98.41 support=95.2 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=45.62 liquidity=37460844.0 spike=0.11
- TRTO.CA: score=24.92 buy_ready=False sector_rank=10 price=0.04 support=0.03 resistance=0.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=21261.14 spike=9.37
- UEFM.CA: score=16.78 buy_ready=False sector_rank=10 price=567.97 support=511.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=68.89 liquidity=877259.38 spike=0.16
- UEGC.CA: score=19.62 buy_ready=True sector_rank=10 price=2.51 support=2.08 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=51.35 liquidity=3719858.5 spike=0.08
- UNIP.CA: score=20.63 buy_ready=True sector_rank=10 price=0.41 support=0.34 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=49.04 liquidity=4726328.5 spike=0.17
- UNIT.CA: score=16.38 buy_ready=False sector_rank=12 price=20.25 support=17.32 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:53 AM market time freshness=DELAYED_CURRENT RSI=67.27 liquidity=479174.56 spike=0.03
- WCDF.CA: score=13.87 buy_ready=False sector_rank=10 price=637.35 support=519.26 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=79.39 liquidity=966434.44 spike=0.2
- WKOL.CA: score=20.61 buy_ready=True sector_rank=10 price=328.31 support=307.0 resistance=363.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=54.23 liquidity=4712933.0 spike=0.21
- ZEOT.CA: score=10.9 buy_ready=False sector_rank=10 price=14.38 support=13.75 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24252100.0 spike=0.7
- ZMID.CA: score=24.68 buy_ready=True sector_rank=12 price=7.65 support=7.06 resistance=7.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=55.12 liquidity=8775428.0 spike=0.04

## Backtesting Lite
- ETEL.CA: 180d return=82.39%, max drawdown=-30.44%, MA20>MA50 days last20=17, as_of=2026-08-12T21:00:00+00:00
- COSG.CA: 180d return=31.43%, max drawdown=-18.87%, MA20>MA50 days last20=20, as_of=2026-08-12T21:00:00+00:00
- SCEM.CA: 180d return=50.2%, max drawdown=-14.53%, MA20>MA50 days last20=16, as_of=2026-08-12T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ETEL.CA: status=RECENT_ACCEPTED latest=2026-08-13 age_days=3 sources=3 expected=Telecom Egypt summary=Telecom Egypt (ETEL.CA) has reported its Q2 2026 financial results on August 13, 2026, showing improved profitability and efficiency in H1 2026. The company also announced on July 16, 2026, that it would not proceed with a proposed transaction with Helios Investments for a stake in its Regional Data Center Hub. Earlier in the year, Q1 2026 results were released on May 23, 2026, and the full-year 2025 results were announced on December 31, 2025. The company also signed agreements with Vodafone Egypt for network expansion and 5G rollout.
  - Q2 2026 Results: Telecom Egypt Reports Improved Profitability and Efficiency in H1 2026 (August 13, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxDK7FrQCSD4osBorg6h3E57eBH-dNgEURabIbpeYx4Xk7cysU0uv_cGDXf91B2erLeRcmA6kls3O94d8tZWDqEHkCmJ5sKdDERYI=
  - Telecom Egypt Announces It Will Not Proceed with the Proposed RDH Transaction with Helios Investments (July 16, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxDK7FrQCSD4osBorg6h3E57eBH-dNgEURabIbpeYx4Xk7cysU0uv_cGDXf91B2erLeRcmA6kls3O94d8tZWDqEHkCmJ5sKdDERYI=
  - Telecom Egypt Company to Report Q2, 2026 Results on Aug 13, 2026 (July 30, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzDVS0zvId-LmqEGcNxH8UkEekoupTD_kimarV1oPPW1d0OiysRsNVyDmpw3KR9vokk0qdB0vYvpyqbDkRp_aOFHtCP7X5EpVOKGECG2IarAR0QRrCampJSkR_vrYazQ==
- COSG.CA: status=RECENT_ACCEPTED latest=2026-03-31 age_days=138 sources=3 expected=Cairo Oil & Soap Company summary=Cairo Oil & Soap Company (COSG.CA) reported a net income of 6.735 million EGP for the latest quarter, with revenue reaching 283.633 million EGP, an increase from the previous quarter's revenue of 180.316 million EGP and a net loss of -14.984 million EGP. The company's income statement for March 31, 2026, is available.
  - Cairo Oils & Soap - Financials (Latest Quarter): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENmVMGDdxLjriZ_CKg2-O2kZ7RNH1QJueneMS2muHn8qv7qMfg5xinXWIq0H8sPMrPCcpCdyH79sqq_gTosg0X4__cB-gqgEsRdCD8-_peYxIXEDU5IocQajJlCinfS53pfvXIMj5VpSkE0L9jmFmtHA4NWU3jCphUE8nR_A==
  - Cairo Oil & Soap Company (EGX:COSG) Income Statement (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEYtVePOScqTX7qHjaIXv4Mgz-ZbaZyIV3XjvB4JMq8ii_A7J-JeylucRzBB2uNLxna41rOUNV3Ql4hXXHHD76GNkZItiaikBuwb5qFPzZRizQjgPEC7Wf6FM6b3LLGqNtelj3odMdzYkjZm8j3a1rcvA-sykMyUVWtFi6NX11
  - Cairo Oil & Soap Company (EGX:COSG) Financials Overview (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzvzIOCy3bYPf53NEJ-vTFULbab4OGtfOD1FTGKS62S-Qa-T0jDvxLjks4wgyvya6yF5MVIWbONunyQ5X4zoU6HoV0czw9ml10XRJl7UmLutypa3mTeAwVF2sOdet_AvfbRbm6cirywEjsEGVsbQ==
- SCEM.CA: status=RECENT_ACCEPTED latest=2026-07-22 age_days=25 sources=3 expected=Sinai Cement summary=Sinai Cement (SCEM.CA) reported revenue of 2.14 billion EGP in the quarter ending March 31, 2026, with a 5.92% growth. The company's revenue for the last twelve months reached 9.21 billion EGP, up 26.50% year-over-year, and annual revenue for 2025 was 9.09 billion EGP with 41.40% growth. Recent corporate news includes a disclosure form for the Board of Directors and shareholders' structure on July 22, 2026, and amendments to the Board of Directors on May 14, 2026.
  - Sinai Cement Co. (S.A.E) Revenue (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBvpEPfNmqLIprD7fJA4IH3y3E7XcTJ_IygXlocPHKLctKyYqGRFkSH8rWYOZTJJT-IzuRxJFVL4OfYBNLUFg3irE_57GLZkXwzbImj_G5zhIZJnYYKjYWkdmPEf9mgI1XQae-2X_qWbZQ6w==
  - Sinai Cement Co. (S.A.E) (EGX:SCEM) Income Statement (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJAZ_gpqO-4VT0d7xetBFHQtzaFGzmD9OElnJ-E9j9ja2sKYWzsLe0osZLTJ7j3R3Utvl_uFXujErnq9NmBJFnV0Lqx7mGV0JyzcE8U1XfBRkX9TjGPS0CEsMk9M2H7SfLAJXCSMlX6hsFRVKauA==
  - Sinai Cement (SCEM.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 22, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFY2UwbXzSHcyuMFKvGSfb9M0Usote4XZP82U74shfbBIOBkbtxE_eTUd2tENFFlfyW-XWcXGeiof2hEb3jPMjnzkicOOAPmKDlbROLtPSfz3qnQVBalLD0wIsQdSUGeQ_FUk0SVrxuKGKbk653XiY=
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- ORHD.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Development Egypt summary=Evidence rejected for ORHD.CA: source text did not clearly match ORHD.CA / Orascom Development Egypt.
- ALCN.CA: status=RECENT_ACCEPTED latest=2026-08-10 age_days=6 sources=3 expected=Alexandria Containers and Cargo Handling summary=Alexandria Containers and Cargo Handling (ALCN.CA) reported an 18% year-on-year increase in net profit after tax for the first half of 2026, reaching EGP 3.798 billion. Revenue for the same period increased by 3% to approximately EGP 4.575 billion. The company's income statement for March 31, 2026, is also available.
  - Alexandria Container's H1 2026 profits rise 18% YoY (August 10, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEigXqmPrq_B9HTmGDovGKVi7GkcnsmGnzr_k-cQrHcQSxX8a2OS_xcU2eUsnP6wS82oRglC5m4jgOUxeT7sr-TgvYRE62yPAnw91nwJlOkX5Gue0VtP06BGI387Vz1NHC5IwRbL47hBvEbd2RzXCX5nPksqCVhOw1T9nxeT1JorSzs8Kh_pPNQI4rBifGwhvLE7a1iEDPf4UlPT6V7j5SQj27Jkhg=
  - Alexandria Container&Cargo Handling Company (EGX:ALCN) Income Statement (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHw4op-es3aaI8z-dICshAAGl4S-0AuL6f969H_y37WlphNi309zEnwqFnNSmLSx8MjnE-mPdI_LuzeSbcmji-91abWxanKgnevGGx6etiR8a_BlbolxRg2Ahe0meWQcteDKTTeydjKw6t6F2AweQWhk_UwN8AT81potbvX_Zx_
  - Alexandria Container&Cargo Handling Company (EGX:ALCN) Stock Price & Overview (2025 Financial Performance): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsQQctFAiHjKlq2-U4C3cCc9_EekFMYiZqdwE1MpPyrZh8LBO5oNy9kExlBOeyMBbliW3W6Oz4G0ZBHwG6iynHGPcDADu7KPAV6t1Cuyq0RsfgsCOTpFwUV6Lpdh3wdBzYRic=
- MTIE.CA: status=RECENT_ACCEPTED latest=2026-05-20 age_days=88 sources=3 expected=MM Group For Industry and International Trade summary=MM Group For Industry and International Trade (MTIE.CA) reported consolidated financial results for the period from January 1, 2026, to March 31, 2026, with a net profit of 318,204,650 EGP. The latest quarter's net income was 304.99 million EGP. The company's income statement for March 31, 2026, is available.
  - MM Group For Industry And International Trade (MTIE.CA) Reports its Financial Results (Consolidated) for the Period from 01/01/2026 to 31/03/2026 (May 20, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3k2s9ySEJYq-6W7pMuvEMKwM7wma8NBcdZFdMBV6YRL39wIXMylzzQ9oTw18M6Gts4hr5iULrZVyX-CgALc7sWqCwsbFVlZe-6FFroDqvpihWzEtfn6GI281J5zgpjwSRbDqO8AQ4jUyx2KeYVZsLtvE=
  - MM Group for Industry and International Trade S.A.E. (EGX:MTIE) Income Statement (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEk7bkNnrbkldE7r5SDxNvtUXRsYOWfpvRp9AsiK3siE546DBjtlbBl1PqZk6PMXA7fOmy0yDxwIZ_LdaV9IB34cMhNGHDFGCDFTAWFW07CtfThHM1exJcwKn8ogRG5OoLSw_a_N4o0it4fHNcUuiBN8PE9ZzUK7Ib2LdRWuk8M
  - EGX:MTIE Financials | MM Group for Industry (Latest Quarter Net Income): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtqu4ChgmlinC8ptwljIQPysllX6CbxgrcLgjg3Cd2wCH1uNeSlPtOqbSIjxLClbETEinTBOlV4YGTxZVO3Qo9fMzaLRpY65gr35O4L5eCNUv_Be8XJsWtv0QRM4lbBpgsMF7vsR0HGHvZzOV0MMzqlNv_gCEiK_Fkd_O3TpIpFgh3sdA=
- AJWA.CA: status=RECENT_ACCEPTED latest=2026-08-06 age_days=10 sources=3 expected=AJWA For Food Industries Co. Egypt summary=AJWA For Food Industries Co. Egypt (AJWA.CA) held its Annual General Meeting (AGM) on August 2, 2026, with minutes released on August 6, 2026, and decisions on August 3, 2026. The company reported latest quarter sales of 469.05 million EGP and a net income of 5.40 million EGP. In 2024, the company's revenue was 1.70 billion EGP.
  - AJWA for Food Industries company Egypt (AJWA.CA) - AGM Minutes (August 6, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGf8EIQkdClq7ebnkOAq0PJHdwrptuTtL4EJcgcPcE0LRHLWHfaIIhNpaGGdVNOsrIsWw9e_wlmifzqxj1gNyY6i2HiGd2Z208FyqgEtKCWRaW5_RhcpkobMtoR6Lick3Mim3KHxJmbPDPFiCTVyOI
  - AJWA for Food Industries company - Egypt (AJWA.CA) - AGM Decisions (August 3, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGf8EIQkdClq7ebnkOAq0PJHdwrptuTtL4EJcgcPcE0LRHLWHfaIIhNpaGGdVNOsrIsWw9e_wlmifzqxj1gNyY6i2HiGd2Z208FyqgEtKCWRaW5_RhcpkobMtoR6Lick3Mim3KHxJmbPDPFiCTVyOI
  - AJWA For Food Industries Co. Egypt, Annual General Meeting, Aug 02, 2026: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQap5rxhoHmbHQLR4zLaqLL6Pdis4hn0_6dMATz8d-kCbL1CSSR6xLM8J61eNeRLDMxGZzjKx2isP4Us5pupXzzscnshsXmpb4YIsZqhCQ0X0sGRKiEM1_w7nHqEUCMQ==

## Warnings
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence rejected for ORHD.CA: source text did not clearly match ORHD.CA / Orascom Development Egypt.
