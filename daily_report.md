# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-08-26T13:43:19.234223+00:00
Generated Cairo: 2026-08-26 16:43
Run timing: target 15:30 Cairo | generated Cairo 2026-08-26 16:43 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-08-26 16:31

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 179/189
- Top sector: Building Materials

## Market Context
- Market trend: Unavailable
- Source: Market context unavailable
- As of: None
- Freshness: MISSING
- EGX30 regime: MIXED / above MA20 71.43% / above MA50 71.43%
- EGX70 regime: MIXED / above MA20 45.0% / above MA50 67.5%
- Sector breadth: 19.05%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=1030593144.29 spike=2.62 score=24.64
- LUTS.CA: liquidity=426493344.0 spike=2.03 score=20.12
- OFH.CA: liquidity=351260096.0 spike=4.47 score=11.06
- GTWL.CA: liquidity=331213152.0 spike=1.0 score=21.06
- EAST.CA: liquidity=321334062.05 spike=5.35 score=19.14

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 both display a mixed trend with weak sector breadth (19.05%), triggering a defensive risk mode that blocks new buys; the scanner highlights accumulation‑spike liquidity in several tickets but notes overheated RSI and proximity to resistance, suggesting limited upside in the next 1‑3 days.
- Top tickets (EBSC.CA, FAIT.CA, CCRS.CA) show accumulation‑spike liquidity but RSI >70, indicating short‑term overextension and limited room to rise.
- Support/resistance distances are tight (e.g., COMI.CA within ~4% of support and ~1.4% of resistance), so any move is likely to be capped near current levels over the next few days.
- Sector breadth is low (19.05%); leading sectors are Building Materials, Textiles, Investment Holding, yet most flagged stocks sit outside these leaders, reducing conviction for sustained upside.
- Mixed EGX30/EGX70 regime shifts risk mode to DEFENSIVE_NO_NEW_BUY, adding uncertainty that even bullish‑watch outlooks may fail if breadth does not improve.

## Top Liquidity Spikes
- FAIT.CA: spike=9.37 liquidity=40687024.0 outlook=CONSTRUCTIVE score=62.13 buy_ready=False
- AXPH.CA: spike=5.7 liquidity=48271428.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EAST.CA: spike=5.35 liquidity=321334062.05 outlook=WEAK_OR_RISKY score=11.86 buy_ready=False
- OFH.CA: spike=4.47 liquidity=351260096.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CCRS.CA: spike=4.19 liquidity=165983760.0 outlook=BULLISH_WATCH score=79.15 buy_ready=False

## Sector Leaderboard
- #1 Building Materials: score=11.06 5d=2.89% 20d=18.64% aboveMA50=100.0%
- #2 Textiles: score=10.04 5d=-0.36% 20d=14.88% aboveMA50=100.0%
- #3 Investment Holding: score=9.9 5d=5.42% 20d=10.0% aboveMA50=100.0%
- #4 Agriculture & Food Production: score=9.39 5d=-0.43% 20d=11.6% aboveMA50=100.0%
- #5 Healthcare: score=8.43 5d=-0.95% 20d=16.1% aboveMA50=100.0%
- #6 Transportation & Logistics: score=7.74 5d=0.02% 20d=13.8% aboveMA50=100.0%
- #7 Banking & Financials: score=7.13 5d=-0.43% 20d=4.43% aboveMA50=90.0%
- #8 Industrial Goods & Cables: score=6.21 5d=-2.35% 20d=13.16% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CLHO.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- IFAP.CA: BULLISH_WATCH score=90.39 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- LCSW.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ORWE.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- COMI.CA: BULLISH_WATCH score=88.13 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance
- KABO.CA: BULLISH_WATCH score=87 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- RTVC.CA: BULLISH_WATCH score=85.15 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- SAUD.CA: BULLISH_WATCH score=83.13 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- CIEB.CA: BULLISH_WATCH score=82.13 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- EMFD.CA: BULLISH_WATCH score=81.34 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=21.06 buy_ready=False sector_rank=11 price=306.44 support=236.15 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=54.02 liquidity=15927062.0 spike=0.26
- ABUK.CA: score=23.21 buy_ready=False sector_rank=9 price=76.37 support=70.9 resistance=80.3 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=64.83 liquidity=44750225.03 spike=0.52
- ACAMD.CA: score=17.14 buy_ready=False sector_rank=11 price=2.06 support=1.95 resistance=2.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.62 liquidity=86579976.0 spike=1.54
- ACGC.CA: score=21.64 buy_ready=False sector_rank=2 price=14.01 support=10.12 resistance=14.3 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=78.5 liquidity=61002202.9 spike=1.62
- ADCI.CA: score=14.76 buy_ready=False sector_rank=11 price=292.35 support=245.0 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=57.23 liquidity=3700088.0 spike=0.18
- ADIB.CA: score=21.4 buy_ready=False sector_rank=7 price=53.61 support=50.1 resistance=55.65 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=60.82 liquidity=26072258.82 spike=0.45
- ADPC.CA: score=11.06 buy_ready=False sector_rank=11 price=3.87 support=3.81 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.45 liquidity=13592836.0 spike=0.29
- AFDI.CA: score=6.38 buy_ready=False sector_rank=11 price=55.33 support=55.2 resistance=59.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32421336.0 spike=1.16
- AFMC.CA: score=19.06 buy_ready=False sector_rank=11 price=216.48 support=124.0 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.26 liquidity=41747272.0 spike=0.25
- AJWA.CA: score=11.06 buy_ready=False sector_rank=11 price=181.83 support=180.01 resistance=204.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=33.85 liquidity=14842382.0 spike=0.31
- ALCN.CA: score=18.75 buy_ready=False sector_rank=6 price=30.63 support=28.8 resistance=32.61 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=43.79 liquidity=9347663.14 spike=0.4
- ALUM.CA: score=23.4 buy_ready=False sector_rank=11 price=29.65 support=22.72 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=73.19 liquidity=29445542.0 spike=1.17
- AMER.CA: score=19.14 buy_ready=False sector_rank=10 price=5.75 support=4.44 resistance=8.47 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=45.48 liquidity=30786218.75 spike=0.39
- AMES.CA: score=18.06 buy_ready=False sector_rank=11 price=147.75 support=110.54 resistance=173.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=76.19 liquidity=26821194.0 spike=0.38
- AMIA.CA: score=18.06 buy_ready=False sector_rank=11 price=19.01 support=10.6 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=89.86 liquidity=30490688.0 spike=0.59
- AMOC.CA: score=20.88 buy_ready=False sector_rank=13 price=10.9 support=8.23 resistance=12.25 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=72.25 liquidity=151437618.7 spike=1.09
- APSW.CA: score=6.56 buy_ready=False sector_rank=11 price=8.51 support=8.41 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.06 liquidity=1498274.75 spike=0.93
- ARAB.CA: score=24.56 buy_ready=False sector_rank=10 price=0.25 support=0.23 resistance=0.26 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=64.1 liquidity=106216682.11 spike=1.71
- ARCC.CA: score=23.4 buy_ready=False sector_rank=1 price=77.0 support=55.4 resistance=91.72 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=83.29 liquidity=69248025.0 spike=0.71
- AREH.CA: score=11.06 buy_ready=False sector_rank=11 price=1.46 support=1.38 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=26.67 liquidity=10376353.0 spike=0.35
- ARVA.CA: score=6.06 buy_ready=False sector_rank=11 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=14.06 buy_ready=False sector_rank=11 price=62.5 support=61.0 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=21.79 liquidity=12447719.0 spike=0.23
- ASPI.CA: score=19.06 buy_ready=False sector_rank=11 price=0.48 support=0.4 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=60.07 liquidity=40991048.0 spike=0.99
- ATLC.CA: score=15.46 buy_ready=False sector_rank=19 price=5.41 support=5.0 resistance=5.95 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=54.41 liquidity=5936836.45 spike=0.31
- ATQA.CA: score=21.99 buy_ready=False sector_rank=9 price=11.53 support=9.66 resistance=11.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.55 liquidity=155634816.0 spike=1.89
- AXPH.CA: score=11.06 buy_ready=False sector_rank=11 price=1687.5 support=1560.0 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48271428.0 spike=5.7
- BINV.CA: score=11.4 buy_ready=False sector_rank=3 price=48.58 support=46.01 resistance=50.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.59 liquidity=997878.63 spike=0.16
- BIOC.CA: score=19.06 buy_ready=False sector_rank=11 price=441.0 support=170.0 resistance=563.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.42 liquidity=81918328.0 spike=0.34
- BTFH.CA: score=8.53 buy_ready=False sector_rank=19 price=2.96 support=2.95 resistance=3.26 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=18.42 liquidity=69252154.97 spike=0.4
- CAED.CA: score=21.06 buy_ready=False sector_rank=11 price=149.95 support=118.01 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=70.55 liquidity=15441522.0 spike=0.3
- CANA.CA: score=15.51 buy_ready=False sector_rank=7 price=41.92 support=36.62 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=72.48 liquidity=4111797.75 spike=0.22
- CCAP.CA: score=21.4 buy_ready=False sector_rank=3 price=5.77 support=5.14 resistance=5.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.85 liquidity=298997664.0 spike=0.49
- CCRS.CA: score=26.06 buy_ready=False sector_rank=11 price=2.84 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.04 liquidity=165983760.0 spike=4.19
- CEFM.CA: score=18.1 buy_ready=False sector_rank=11 price=144.24 support=122.1 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=59.41 liquidity=5039040.0 spike=0.16
- CERA.CA: score=11.31 buy_ready=False sector_rank=11 price=1.29 support=1.23 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.91 liquidity=5252667.5 spike=0.35
- CFGH.CA: score=8.07 buy_ready=False sector_rank=11 price=0.11 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=75.0 liquidity=11315.3 spike=0.76
- CICH.CA: score=9.05 buy_ready=False sector_rank=19 price=12.3 support=11.92 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=29.61 liquidity=6523823.5 spike=0.9
- CIEB.CA: score=23.4 buy_ready=False sector_rank=7 price=24.99 support=23.75 resistance=25.6 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=58.44 liquidity=10648088.96 spike=0.94
- CIRA.CA: score=18.21 buy_ready=False sector_rank=16 price=35.49 support=34.3 resistance=40.8 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=49.14 liquidity=16903958.78 spike=0.5
- CLHO.CA: score=24.14 buy_ready=False sector_rank=5 price=17.5 support=16.0 resistance=19.72 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=52.6 liquidity=135617562.5 spike=2.37
- CNFN.CA: score=14.53 buy_ready=False sector_rank=19 price=4.81 support=4.68 resistance=5.01 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=43.08 liquidity=11791758.15 spike=0.68
- COMI.CA: score=24.64 buy_ready=False sector_rank=7 price=140.96 support=135.35 resistance=142.88 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=57.51 liquidity=1030593144.29 spike=2.62
- COPR.CA: score=20.66 buy_ready=False sector_rank=11 price=0.54 support=0.39 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.87 liquidity=111805904.0 spike=1.3
- COSG.CA: score=23.06 buy_ready=False sector_rank=11 price=1.8 support=1.6 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=45260596.0 spike=0.9
- CPCI.CA: score=14.87 buy_ready=False sector_rank=11 price=544.16 support=440.01 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=69.05 liquidity=5809718.0 spike=0.69
- CSAG.CA: score=18.45 buy_ready=False sector_rank=6 price=40.23 support=31.35 resistance=43.86 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=64.57 liquidity=5054054.61 spike=0.23
- DAPH.CA: score=11.0 buy_ready=False sector_rank=11 price=116.0 support=108.25 resistance=124.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=136610016.0 spike=3.47
- DEIN.CA: score=-3.94 buy_ready=False sector_rank=11 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=8.08 buy_ready=False sector_rank=17 price=27.88 support=26.01 resistance=32.0 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=27.55 liquidity=4936376.89 spike=0.32
- DSCW.CA: score=11.06 buy_ready=False sector_rank=11 price=1.89 support=1.84 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.73 liquidity=23382180.0 spike=0.26
- DTPP.CA: score=19.06 buy_ready=False sector_rank=11 price=296.1 support=235.59 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.97 liquidity=11189880.0 spike=0.21
- EALR.CA: score=20.62 buy_ready=False sector_rank=11 price=402.29 support=363.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=54.47 liquidity=7564955.5 spike=0.16
- EASB.CA: score=3.52 buy_ready=False sector_rank=11 price=7.66 support=7.61 resistance=8.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7457732.5 spike=0.91
- EAST.CA: score=19.14 buy_ready=False sector_rank=17 price=35.4 support=35.0 resistance=37.1 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=38.03 liquidity=321334062.05 spike=5.35
- EBSC.CA: score=27.04 buy_ready=False sector_rank=11 price=2.05 support=1.85 resistance=2.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=73.91 liquidity=24227306.0 spike=2.99
- ECAP.CA: score=16.06 buy_ready=False sector_rank=11 price=33.02 support=32.12 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.67 liquidity=12842143.0 spike=0.91
- EDFM.CA: score=9.72 buy_ready=False sector_rank=11 price=400.84 support=375.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=56.94 liquidity=656559.13 spike=0.22
- EEII.CA: score=21.06 buy_ready=False sector_rank=11 price=2.92 support=2.54 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.93 liquidity=12443882.0 spike=0.48
- EFIC.CA: score=18.21 buy_ready=False sector_rank=9 price=200.35 support=184.0 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.84 liquidity=23515248.0 spike=0.48
- EFID.CA: score=20.14 buy_ready=False sector_rank=17 price=31.7 support=26.7 resistance=34.89 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=56.76 liquidity=31442343.16 spike=0.39
- EFIH.CA: score=18.37 buy_ready=False sector_rank=15 price=23.64 support=22.15 resistance=25.4 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=47.06 liquidity=79107688.32 spike=0.79
- EGAL.CA: score=22.95 buy_ready=False sector_rank=9 price=352.75 support=292.0 resistance=359.85 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=82.51 liquidity=272511015.75 spike=2.37
- EGAS.CA: score=14.55 buy_ready=False sector_rank=13 price=56.18 support=51.5 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.22 liquidity=5851946.0 spike=0.24
- EGBE.CA: score=11.54 buy_ready=False sector_rank=7 price=0.54 support=0.47 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=60.64 liquidity=143345.28 spike=0.71
- EGCH.CA: score=11.21 buy_ready=False sector_rank=9 price=13.38 support=12.69 resistance=14.79 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=30.94 liquidity=71671977.61 spike=0.63
- EGSA.CA: score=0.5 buy_ready=False sector_rank=14 price=8.69 support=8.65 resistance=8.99 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=28.0 liquidity=434.5 spike=0.05
- EGTS.CA: score=16.14 buy_ready=False sector_rank=10 price=17.02 support=16.17 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=39.5 liquidity=11446372.0 spike=0.32
- EHDR.CA: score=19.06 buy_ready=False sector_rank=11 price=2.85 support=2.71 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=51.72 liquidity=13693781.0 spike=0.35
- EKHO.CA: score=6.7 buy_ready=False sector_rank=13 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=10.4 buy_ready=False sector_rank=8 price=2.08 support=2.05 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=22.73 liquidity=40701708.0 spike=0.73
- ELKA.CA: score=21.06 buy_ready=False sector_rank=11 price=1.75 support=1.69 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=49302632.0 spike=0.76
- ELNA.CA: score=5.12 buy_ready=False sector_rank=11 price=37.01 support=36.1 resistance=39.24 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=43.32 liquidity=62657.93 spike=0.17
- ELSH.CA: score=11.06 buy_ready=False sector_rank=11 price=13.34 support=12.97 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=15.98 liquidity=27999610.0 spike=0.45
- ELWA.CA: score=13.16 buy_ready=False sector_rank=11 price=1.85 support=1.62 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=64.29 liquidity=2582257.5 spike=1.26
- EMFD.CA: score=24.6 buy_ready=False sector_rank=10 price=12.13 support=11.08 resistance=12.32 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=51.28 liquidity=129091730.98 spike=1.73
- ENGC.CA: score=19.06 buy_ready=False sector_rank=11 price=45.88 support=40.11 resistance=54.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.99 liquidity=13168203.0 spike=0.47
- EOSB.CA: score=13.09 buy_ready=False sector_rank=11 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=25892.44 spike=0.46
- EPCO.CA: score=16.09 buy_ready=False sector_rank=11 price=11.06 support=10.32 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.27 liquidity=7025257.5 spike=0.33
- EPPK.CA: score=3.47 buy_ready=False sector_rank=11 price=13.3 support=12.3 resistance=15.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=32.82 liquidity=1285292.63 spike=1.56
- ETEL.CA: score=22.5 buy_ready=False sector_rank=14 price=116.1 support=102.75 resistance=120.0 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=59.44 liquidity=61027499.8 spike=0.53
- ETRS.CA: score=19.24 buy_ready=False sector_rank=11 price=10.88 support=10.21 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.07 liquidity=8180087.5 spike=0.27
- EXPA.CA: score=19.4 buy_ready=False sector_rank=7 price=19.98 support=19.7 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=40.86 liquidity=22287284.0 spike=0.59
- FAIT.CA: score=26.4 buy_ready=False sector_rank=7 price=43.52 support=36.1 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.65 liquidity=40687024.0 spike=9.37
- FAITA.CA: score=17.01 buy_ready=False sector_rank=7 price=1.02 support=0.97 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=58.46 liquidity=126473.92 spike=2.74
- FERC.CA: score=12.15 buy_ready=False sector_rank=9 price=77.98 support=75.01 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=55.05 liquidity=3940641.5 spike=0.22
- FWRY.CA: score=13.63 buy_ready=False sector_rank=15 price=18.9 support=18.69 resistance=19.81 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=32.42 liquidity=297480437.4 spike=2.63
- GBCO.CA: score=9.37 buy_ready=False sector_rank=21 price=28.6 support=28.12 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.53 liquidity=75405520.0 spike=1.59
- GDWA.CA: score=10.06 buy_ready=False sector_rank=11 price=0.79 support=0.77 resistance=0.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=19.48 liquidity=24974248.0 spike=0.36
- GGCC.CA: score=8.66 buy_ready=False sector_rank=11 price=0.96 support=0.88 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=99955496.0 spike=2.3
- GIHD.CA: score=20.85 buy_ready=False sector_rank=11 price=64.9 support=56.51 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.32 liquidity=9785073.0 spike=0.31
- GMCI.CA: score=3.35 buy_ready=False sector_rank=11 price=1.91 support=1.83 resistance=2.1 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=25.0 liquidity=834507.64 spike=1.73
- GRCA.CA: score=6.06 buy_ready=False sector_rank=11 price=72.64 support=72.33 resistance=79.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48961604.0 spike=0.99
- GSSC.CA: score=13.67 buy_ready=False sector_rank=11 price=286.29 support=266.65 resistance=301.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=60.21 liquidity=2614296.5 spike=0.14
- GTWL.CA: score=21.06 buy_ready=False sector_rank=11 price=218.85 support=211.0 resistance=211.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=331213152.0 spike=1.0
- HDBK.CA: score=17.4 buy_ready=False sector_rank=7 price=92.4 support=80.8 resistance=93.88 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=72.51 liquidity=24335665.6 spike=0.65
- HELI.CA: score=11.14 buy_ready=False sector_rank=10 price=7.35 support=7.34 resistance=8.65 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=20.38 liquidity=73655010.54 spike=0.56
- HRHO.CA: score=10.41 buy_ready=False sector_rank=19 price=25.76 support=25.49 resistance=28.1 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=13.19 liquidity=172812455.62 spike=1.94
- ICID.CA: score=18.3 buy_ready=False sector_rank=11 price=16.88 support=7.85 resistance=18.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=93.68 liquidity=28953656.0 spike=1.12
- IDRE.CA: score=14.11 buy_ready=False sector_rank=11 price=52.69 support=46.04 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.52 liquidity=3053339.5 spike=0.15
- IFAP.CA: score=21.4 buy_ready=False sector_rank=4 price=20.91 support=19.0 resistance=22.7 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=44.08 liquidity=26359584.92 spike=0.96
- INFI.CA: score=21.06 buy_ready=False sector_rank=11 price=157.03 support=104.0 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.95 liquidity=16771566.0 spike=0.24
- IRON.CA: score=10.21 buy_ready=False sector_rank=9 price=30.63 support=30.14 resistance=34.99 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=26.69 liquidity=10446116.17 spike=0.98
- ISMA.CA: score=8.32 buy_ready=False sector_rank=11 price=39.26 support=37.0 resistance=39.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=63332528.0 spike=2.13
- ISMQ.CA: score=16.21 buy_ready=False sector_rank=9 price=9.13 support=8.96 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.28 liquidity=19821626.0 spike=0.36
- ISPH.CA: score=19.4 buy_ready=False sector_rank=5 price=13.11 support=11.3 resistance=16.93 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=50.22 liquidity=44082937.58 spike=0.24
- JUFO.CA: score=18.14 buy_ready=False sector_rank=17 price=26.89 support=22.78 resistance=28.8 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=51.45 liquidity=14926880.67 spike=0.3
- KABO.CA: score=21.48 buy_ready=False sector_rank=2 price=9.0 support=7.75 resistance=9.75 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=65.76 liquidity=35317053.0 spike=1.04
- KWIN.CA: score=23.18 buy_ready=False sector_rank=11 price=107.84 support=84.08 resistance=118.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.81 liquidity=61706560.0 spike=1.06
- KZPC.CA: score=18.06 buy_ready=False sector_rank=11 price=12.78 support=8.42 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=76.06 liquidity=19561192.0 spike=0.4
- LCSW.CA: score=24.4 buy_ready=False sector_rank=1 price=34.75 support=30.2 resistance=37.79 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=50.52 liquidity=20735081.75 spike=0.77
- LUTS.CA: score=20.12 buy_ready=False sector_rank=11 price=1.59 support=0.54 resistance=1.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.16 liquidity=426493344.0 spike=2.03
- MAAL.CA: score=21.06 buy_ready=False sector_rank=11 price=9.48 support=8.32 resistance=9.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.47 liquidity=10137698.0 spike=0.82
- MASR.CA: score=16.06 buy_ready=False sector_rank=11 price=7.52 support=7.45 resistance=8.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.34 liquidity=56319532.0 spike=0.83
- MBSC.CA: score=21.4 buy_ready=False sector_rank=1 price=382.34 support=240.02 resistance=434.99 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=79.98 liquidity=23177068.24 spike=0.29
- MCQE.CA: score=24.4 buy_ready=False sector_rank=1 price=234.54 support=178.0 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=68.8 liquidity=15979102.0 spike=0.28
- MCRO.CA: score=19.06 buy_ready=False sector_rank=11 price=1.5 support=1.44 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=42886128.0 spike=0.29
- MENA.CA: score=7.17 buy_ready=False sector_rank=10 price=6.97 support=6.82 resistance=7.78 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=51.89 liquidity=1037352.04 spike=0.19
- MEPA.CA: score=19.06 buy_ready=False sector_rank=11 price=1.8 support=1.78 resistance=2.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.59 liquidity=10641012.0 spike=0.31
- MFPC.CA: score=21.21 buy_ready=False sector_rank=9 price=39.4 support=35.37 resistance=41.0 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=72.39 liquidity=55423154.75 spike=0.77
- MFSC.CA: score=11.92 buy_ready=False sector_rank=11 price=49.32 support=46.02 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=36.11 liquidity=2859463.75 spike=0.25
- MHOT.CA: score=20.58 buy_ready=False sector_rank=12 price=18.38 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.36 liquidity=31624594.0 spike=1.81
- MICH.CA: score=21.06 buy_ready=False sector_rank=11 price=49.01 support=39.01 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.74 liquidity=17202094.0 spike=0.41
- MILS.CA: score=23.06 buy_ready=False sector_rank=11 price=216.04 support=167.0 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.94 liquidity=23524466.0 spike=0.28
- MIPH.CA: score=13.95 buy_ready=False sector_rank=5 price=790.75 support=722.7 resistance=828.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=38.23 liquidity=2546432.25 spike=0.62
- MOED.CA: score=20.06 buy_ready=False sector_rank=11 price=0.79 support=0.65 resistance=0.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=72.93 liquidity=51096608.0 spike=0.57
- MOIL.CA: score=8.84 buy_ready=False sector_rank=13 price=0.66 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=139697.2 spike=0.26
- MOIN.CA: score=21.54 buy_ready=False sector_rank=11 price=34.9 support=23.11 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.4 liquidity=39262784.0 spike=1.24
- MOSC.CA: score=11.93 buy_ready=False sector_rank=11 price=328.57 support=282.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=81.31 liquidity=3869156.25 spike=0.26
- MPCI.CA: score=21.06 buy_ready=False sector_rank=11 price=402.89 support=287.01 resistance=460.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.84 liquidity=95717256.0 spike=0.57
- MPCO.CA: score=21.4 buy_ready=False sector_rank=4 price=2.26 support=1.88 resistance=2.38 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=68.6 liquidity=79426621.64 spike=0.7
- MPRC.CA: score=20.46 buy_ready=False sector_rank=11 price=42.5 support=39.5 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.16 liquidity=48143312.0 spike=1.7
- MTIE.CA: score=13.19 buy_ready=False sector_rank=21 price=8.6 support=8.01 resistance=10.4 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=44.05 liquidity=34448987.13 spike=0.55
- NAHO.CA: score=8.09 buy_ready=False sector_rank=11 price=0.14 support=0.1 resistance=0.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=85.45 liquidity=30668.69 spike=0.34
- NCCW.CA: score=10.19 buy_ready=False sector_rank=11 price=5.87 support=5.59 resistance=7.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.25 liquidity=4131138.0 spike=0.13
- NEDA.CA: score=13.46 buy_ready=False sector_rank=11 price=2.78 support=2.7 resistance=2.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=50.85 liquidity=396499.97 spike=0.46
- NHPS.CA: score=21.06 buy_ready=False sector_rank=11 price=91.57 support=82.25 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.34 liquidity=21324382.0 spike=0.61
- NINH.CA: score=21.28 buy_ready=False sector_rank=11 price=24.5 support=21.22 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.56 liquidity=45859592.0 spike=1.11
- NIPH.CA: score=21.4 buy_ready=False sector_rank=5 price=372.48 support=209.0 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.41 liquidity=161577200.0 spike=0.48
- OBRI.CA: score=17.06 buy_ready=False sector_rank=11 price=32.47 support=31.61 resistance=34.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.76 liquidity=15429106.0 spike=0.5
- OCDI.CA: score=21.3 buy_ready=False sector_rank=10 price=32.35 support=27.7 resistance=36.97 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=57.22 liquidity=127450712.39 spike=1.08
- OCPH.CA: score=13.85 buy_ready=False sector_rank=11 price=257.08 support=225.0 resistance=341.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=54.91 liquidity=6793879.5 spike=0.3
- ODIN.CA: score=21.92 buy_ready=False sector_rank=11 price=3.29 support=2.54 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.5 liquidity=62550936.0 spike=1.43
- OFH.CA: score=11.06 buy_ready=False sector_rank=11 price=1.09 support=0.98 resistance=1.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=351260096.0 spike=4.47
- OIH.CA: score=22.24 buy_ready=False sector_rank=3 price=1.95 support=1.43 resistance=1.96 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=84.91 liquidity=176828767.47 spike=1.42
- OLFI.CA: score=14.29 buy_ready=False sector_rank=17 price=23.12 support=22.25 resistance=26.52 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=37.85 liquidity=9141255.29 spike=0.17
- ORAS.CA: score=5.0 buy_ready=False sector_rank=20 price=71.05 support=71.05 resistance=71.05 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ORHD.CA: score=21.14 buy_ready=False sector_rank=10 price=42.2 support=38.0 resistance=44.0 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=52.02 liquidity=77340701.0 spike=0.6
- ORWE.CA: score=23.4 buy_ready=False sector_rank=2 price=25.52 support=22.55 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.3 liquidity=44284052.0 spike=0.57
- PHAR.CA: score=19.4 buy_ready=False sector_rank=5 price=131.5 support=93.4 resistance=178.99 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=51.16 liquidity=137430518.5 spike=0.31
- PHDC.CA: score=16.14 buy_ready=False sector_rank=10 price=14.85 support=14.32 resistance=16.2 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=35.0 liquidity=149858184.85 spike=0.74
- PHTV.CA: score=9.7 buy_ready=False sector_rank=11 price=347.01 support=312.0 resistance=447.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.68 liquidity=638083.5 spike=0.23
- POUL.CA: score=15.14 buy_ready=False sector_rank=17 price=37.5 support=36.5 resistance=40.24 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=44.24 liquidity=16450612.5 spike=0.76
- PRCL.CA: score=18.11 buy_ready=False sector_rank=1 price=33.61 support=32.0 resistance=37.8 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=41.72 liquidity=5706339.51 spike=0.28
- PRDC.CA: score=21.14 buy_ready=False sector_rank=10 price=9.44 support=8.7 resistance=9.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.86 liquidity=36539180.0 spike=0.59
- PRMH.CA: score=7.75 buy_ready=False sector_rank=11 price=2.46 support=2.28 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=32.26 liquidity=6687067.5 spike=0.46
- RACC.CA: score=10.45 buy_ready=False sector_rank=11 price=9.76 support=9.7 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=31.58 liquidity=9389377.0 spike=0.49
- RAKT.CA: score=0.22 buy_ready=False sector_rank=11 price=22.25 support=21.65 resistance=24.0 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=9.2 liquidity=156417.5 spike=0.58
- RAYA.CA: score=15.93 buy_ready=False sector_rank=18 price=7.25 support=6.95 resistance=7.66 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=39.13 liquidity=81834759.25 spike=1.48
- RMDA.CA: score=21.4 buy_ready=False sector_rank=5 price=6.15 support=5.08 resistance=7.39 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=58.96 liquidity=28044080.38 spike=0.25
- ROTO.CA: score=19.06 buy_ready=False sector_rank=11 price=44.43 support=41.85 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.6 liquidity=11205486.0 spike=0.48
- RREI.CA: score=19.06 buy_ready=False sector_rank=11 price=4.27 support=4.28 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=24409296.0 spike=0.35
- RTVC.CA: score=22.94 buy_ready=False sector_rank=11 price=4.12 support=3.73 resistance=4.36 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=65.56 liquidity=13710498.54 spike=1.94
- RUBX.CA: score=18.48 buy_ready=False sector_rank=11 price=13.01 support=12.02 resistance=13.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=55.58 liquidity=5424671.0 spike=0.3
- SAUD.CA: score=21.89 buy_ready=False sector_rank=7 price=23.32 support=21.4 resistance=24.6 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=58.38 liquidity=8489739.17 spike=0.45
- SCEM.CA: score=24.4 buy_ready=False sector_rank=1 price=98.0 support=76.75 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.51 liquidity=130657624.0 spike=0.61
- SCFM.CA: score=21.06 buy_ready=False sector_rank=11 price=288.1 support=272.0 resistance=319.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=52.6 liquidity=12027404.0 spike=0.57
- SCTS.CA: score=9.13 buy_ready=False sector_rank=16 price=620.69 support=603.13 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=76.64 liquidity=1918338.5 spike=0.2
- SDTI.CA: score=21.06 buy_ready=False sector_rank=11 price=70.0 support=55.1 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.12 liquidity=14892661.0 spike=0.44
- SEIG.CA: score=10.09 buy_ready=False sector_rank=11 price=259.1 support=242.1 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.73 liquidity=1027123.0 spike=0.11
- SIPC.CA: score=18.86 buy_ready=False sector_rank=11 price=4.81 support=3.82 resistance=5.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.8 liquidity=7802890.0 spike=0.12
- SKPC.CA: score=18.21 buy_ready=False sector_rank=9 price=17.46 support=15.61 resistance=18.15 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=75.11 liquidity=31792807.57 spike=0.47
- SMFR.CA: score=15.73 buy_ready=False sector_rank=11 price=260.85 support=228.88 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=71.33 liquidity=6668944.5 spike=0.25
- SNFC.CA: score=17.16 buy_ready=False sector_rank=11 price=10.61 support=10.3 resistance=11.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.31 liquidity=14906938.0 spike=1.05
- SPIN.CA: score=21.26 buy_ready=False sector_rank=2 price=18.62 support=15.3 resistance=21.88 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=66.56 liquidity=7856132.13 spike=0.21
- SPMD.CA: score=11.14 buy_ready=False sector_rank=11 price=0.46 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.76 liquidity=7083349.5 spike=0.25
- SUGR.CA: score=20.14 buy_ready=False sector_rank=17 price=57.24 support=46.47 resistance=61.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.14 liquidity=42106348.0 spike=0.82
- SVCE.CA: score=21.06 buy_ready=False sector_rank=11 price=10.95 support=9.06 resistance=12.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=70.37 liquidity=30594062.0 spike=0.3
- SWDY.CA: score=21.98 buy_ready=False sector_rank=8 price=126.6 support=91.8 resistance=133.98 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=72.16 liquidity=128689278.25 spike=1.29
- TALM.CA: score=18.21 buy_ready=False sector_rank=16 price=18.4 support=16.35 resistance=20.86 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=53.35 liquidity=38956368.79 spike=0.94
- TMGH.CA: score=21.14 buy_ready=False sector_rank=10 price=98.5 support=95.2 resistance=100.1 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=42.31 liquidity=130648824.0 spike=0.64
- TRTO.CA: score=15.06 buy_ready=False sector_rank=11 price=0.05 support=0.03 resistance=0.05 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=331.5 spike=0.03
- UEFM.CA: score=10.5 buy_ready=False sector_rank=11 price=537.75 support=531.0 resistance=594.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=45.54 liquidity=1437053.88 spike=0.31
- UEGC.CA: score=15.44 buy_ready=False sector_rank=11 price=2.03 support=1.95 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.95 liquidity=117375248.0 spike=3.19
- UNIP.CA: score=19.06 buy_ready=False sector_rank=11 price=0.37 support=0.35 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.96 liquidity=13214199.0 spike=0.38
- UNIT.CA: score=12.14 buy_ready=False sector_rank=10 price=18.61 support=17.32 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.98 liquidity=3004558.75 spike=0.24
- WCDF.CA: score=9.16 buy_ready=False sector_rank=11 price=642.05 support=571.0 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=75.72 liquidity=1097928.63 spike=0.25
- WKOL.CA: score=17.63 buy_ready=False sector_rank=11 price=347.66 support=310.0 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.37 liquidity=4565616.0 spike=0.13
- ZEOT.CA: score=16.13 buy_ready=False sector_rank=11 price=13.81 support=11.86 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.18 liquidity=5069028.0 spike=0.2
- ZMID.CA: score=21.14 buy_ready=False sector_rank=10 price=7.9 support=7.06 resistance=8.25 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=67.01 liquidity=106637495.59 spike=0.55

## Backtesting Lite
- EBSC.CA: 180d return=25.88%, max drawdown=-23.41%, MA20>MA50 days last20=20, as_of=2026-08-24T21:00:00+00:00
- FAIT.CA: 180d return=39.87%, max drawdown=-8.36%, MA20>MA50 days last20=18, as_of=2026-08-24T21:00:00+00:00
- CCRS.CA: 180d return=100.0%, max drawdown=-34.85%, MA20>MA50 days last20=20, as_of=2026-08-24T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- EBSC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Osool ESB Securities Brokerage summary=Evidence rejected for EBSC.CA: source text did not clearly match EBSC.CA / Osool ESB Securities Brokerage.
- FAIT.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=602 sources=3 expected=Faisal Islamic Bank of Egypt summary=Faisal Islamic Bank of Egypt unveils dividends for 2025; Faisal Islamic Bank of Egypt’s consolidated net profits drop to EGP 4.6bn in 2025; Faisal Islamic Bank of Egypt posts 63% lower standalone net profits in 2025
  - Faisal Islamic Bank of Egypt unveils dividends for 2025: https://english.mubasher.info/news/4585552/Faisal-Islamic-Bank-of-Egypt-unveils-dividends-for-2025/
  - Faisal Islamic Bank of Egypt’s consolidated net profits drop to EGP 4.6bn in 2025: https://english.mubasher.info/news/4582812/Faisal-Islamic-Bank-of-Egypt-s-consolidated-net-profits-drop-to-EGP-4-6bn-in-2025/
  - Faisal Islamic Bank of Egypt posts 63% lower standalone net profits in 2025: https://english.mubasher.info/news/4548875/Faisal-Islamic-Bank-of-Egypt-posts-63-lower-standalone-net-profits-in-2025/
- CCRS.CA: status=OLD_ACCEPTED latest=2016-01-01 age_days=3890 sources=3 expected=Gulf Canadian Company for Arab Real Estate Investment summary=10 EGX-listed firms deny ties to UAE-based Abraaj; Gulf Canadian OGM to discuss 2016 financials Thursday; Gulf Canadian OGM to discuss 2016 results 22 March
  - 10 EGX-listed firms deny ties to UAE-based Abraaj: https://english.mubasher.info/news/3308086/10-EGX-listed-firms-deny-ties-to-UAE-based-Abraaj/
  - Gulf Canadian OGM to discuss 2016 financials Thursday: https://english.mubasher.info/news/3076282/Gulf-Canadian-OGM-to-discuss-2016-financials-Thursday/
  - Gulf Canadian OGM to discuss 2016 results 22 March: https://english.mubasher.info/news/3067564/Gulf-Canadian-OGM-to-discuss-2016-results-22-March/
- COMI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Commercial International Bank Egypt summary=Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- EMFD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=602 sources=3 expected=Emaar Misr for Development summary=Emaar Misr posts higher revenues at EGP 19.8bn in 2025; Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25; Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea
  - Emaar Misr posts higher revenues at EGP 19.8bn in 2025: https://english.mubasher.info/news/4561643/Emaar-Misr-posts-higher-revenues-at-EGP-19-8bn-in-2025/
  - Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25: https://english.mubasher.info/news/4525192/Emaar-Misr-s-consolidated-net-profits-drop-to-EGP-4-2bn-in-9M-25/
  - Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea: https://english.mubasher.info/news/4495287/Emaar-Misr-Golden-Coast-to-establish-EGP-900bn-project-in-Red-Sea/
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- MCQE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=602 sources=3 expected=Misr Cement Qena summary=Misr Cement to distribute EGP 10/shr dividends for 2025; Misr Cement stock is testing technical level ahead of historical peak – Analysis; Misr Cement witnesses 3,254% remarkable jump in 9M-25 consolidated net profits
  - Misr Cement to distribute EGP 10/shr dividends for 2025: https://english.mubasher.info/news/4586191/Misr-Cement-to-distribute-EGP-10-shr-dividends-for-2025/
  - Misr Cement stock is testing technical level ahead of historical peak – Analysis: https://english.mubasher.info/news/4560306/Misr-Cement-stock-is-testing-technical-level-ahead-of-historical-peak-Analysis/
  - Misr Cement witnesses 3,254% remarkable jump in 9M-25 consolidated net profits: https://english.mubasher.info/news/4524754/Misr-Cement-witnesses-3-254-remarkable-jump-in-9M-25-consolidated-net-profits/

## Warnings
- Evidence rejected for EBSC.CA: source text did not clearly match EBSC.CA / Osool ESB Securities Brokerage.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for FAIT.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CCRS.CA matches the company but appears old; latest detected date is 2016-01-01.
- Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- Evidence for EMFD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence for MCQE.CA matches the company but appears old; latest detected date is 2025-01-01.
