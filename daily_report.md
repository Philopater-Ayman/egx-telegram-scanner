# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-08-17T08:39:54.236473+00:00
Generated Cairo: 2026-08-17 11:39
Run timing: target 11:00 Cairo | generated Cairo 2026-08-17 11:39 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-08-17 11:35

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 51
- Data quality issues: 1
- Tradeable price/liquidity tickers: 165/189
- Top sector: Transportation & Logistics

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, August 17
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 72.22% / above MA50 72.22%
- EGX70 regime: BULLISH / above MA20 74.29% / above MA50 91.43%
- Sector breadth: 61.9%
- Risk mode: SELECTIVE_SMALL_MID_SWINGS

## Top Liquidity
- PHAR.CA: liquidity=319175776.0 spike=0.84 score=25.4
- GTWL.CA: liquidity=249109472.0 spike=2.68 score=12.73
- NIPH.CA: liquidity=184476608.0 spike=0.63 score=22.4
- CCAP.CA: liquidity=154481920.0 spike=0.25 score=24.36
- BIOC.CA: liquidity=150780512.0 spike=0.7 score=23.37

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner flagged COPR.CA, ETEL.CA and RACC.CA as watch/buy setups because each shows price above short‑term averages, RSI near 60‑65, and liquidity still above the tradeable threshold, though cooling liquidity, extended momentum and non‑leading sectors keep confidence low; the EGX30’s mixed trend versus the EGX70’s bullish breadth shifts risk mode to selective small‑mid swings, adding uncertainty for the next 1‑3 days.
- COPR.CA: price above MA20/MA50, RSI 59.3, support 0.37/resistance 0.45, liquidity cooling but still tradeable, outlook constructive.
- ETEL.CA: price above MA20/MA50, RSI 64.0, support 97.5/resistance 116.3, liquidity cooling with extended momentum, outlook constructive.
- RACC.CA: price above MA20/MA50, RSI 65.3, support 9.8/resistance 10.6, liquidity cooling, momentum extended, outlook bullish watch.
- EGX30 mixed (slightly negative 5‑day return) vs EGX70 bullish (positive 5‑day return) creates a selective small‑mid swing risk mode, raising uncertainty for short‑term moves.

## Top Liquidity Spikes
- NAHO.CA: spike=11.01 liquidity=310588.5 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- TRTO.CA: spike=9.77 liquidity=22014.61 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- KZPC.CA: spike=4.23 liquidity=50635400.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SPIN.CA: spike=4.09 liquidity=120654320.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GTWL.CA: spike=2.68 liquidity=249109472.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Transportation & Logistics: score=13.36 5d=8.95% 20d=17.76% aboveMA50=100.0%
- #2 Agriculture & Food Production: score=12.01 5d=6.85% 20d=13.71% aboveMA50=100.0%
- #3 Healthcare: score=11.9 5d=1.24% 20d=24.07% aboveMA50=100.0%
- #4 Education: score=11.85 5d=4.4% 20d=19.47% aboveMA50=100.0%
- #5 Tourism & Leisure: score=10.49 5d=11.05% 20d=13.34% aboveMA50=0.0%
- #6 Banking & Financials: score=9.27 5d=3.32% 20d=10.07% aboveMA50=90.0%
- #7 Fintech & Payments: score=8.12 5d=0.91% 20d=5.08% aboveMA50=100.0%
- #8 Basic Resources & Chemicals: score=7.92 5d=3.41% 20d=5.37% aboveMA50=80.0%

## Today's Prioritized Action Tickets
- Priority #1: BUY COPR.CA
  - Entry: 0.45 | Take profit: 0.49 | Stop loss: 0.43
  - Confidence: LOW | score=28.37 | outlook=CONSTRUCTIVE 68.93
  - Reason: WATCH/BUY SETUP: COPR.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 59.26, support 0.37, resistance 0.45, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY ETEL.CA
  - Entry: 117.46 | Take profit: 126.86 | Stop loss: 112.76
  - Confidence: LOW | score=28.15 | outlook=CONSTRUCTIVE 60.37
  - Reason: WATCH/BUY SETUP: ETEL.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 64.0, support 97.54, resistance 116.25, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY RACC.CA
  - Entry: 10.67 | Take profit: 11.53 | Stop loss: 10.24
  - Confidence: LOW | score=26.73 | outlook=BULLISH_WATCH 75.93
  - Reason: WATCH/BUY SETUP: RACC.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 65.31, support 9.8, resistance 10.6, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CLHO.CA: BULLISH_WATCH score=96 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- SCTS.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- CIEB.CA: BULLISH_WATCH score=79.27 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- FWRY.CA: BULLISH_WATCH score=78.12 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ISPH.CA: BULLISH_WATCH score=78 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended; far above support
- EGTS.CA: BULLISH_WATCH score=76.99 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- ASCM.CA: BULLISH_WATCH score=76.93 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- EALR.CA: BULLISH_WATCH score=76.93 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- WKOL.CA: BULLISH_WATCH score=76.93 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- MAAL.CA: BULLISH_WATCH score=76.93 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- AJWA.CA: rank=28.37 outlook=CONSTRUCTIVE outlook_score=66.93 sector_rank=11 price=199.35 support=161.0 resistance=210.0 liquidity=21395660.0
- COPR.CA: rank=28.37 outlook=CONSTRUCTIVE outlook_score=68.93 sector_rank=11 price=0.45 support=0.37 resistance=0.45 liquidity=27006542.0
- ETEL.CA: rank=28.15 outlook=CONSTRUCTIVE outlook_score=60.37 sector_rank=14 price=117.46 support=97.54 resistance=116.25 liquidity=85088152.0
- RACC.CA: rank=26.73 outlook=BULLISH_WATCH outlook_score=75.93 sector_rank=11 price=10.67 support=9.8 resistance=10.6 liquidity=22085736.0
- EFIH.CA: rank=26.4 outlook=CONSTRUCTIVE outlook_score=64.12 sector_rank=7 price=25.13 support=21.9 resistance=25.0 liquidity=59647956.0
- COSG.CA: rank=26.37 outlook=CONSTRUCTIVE outlook_score=64.93 sector_rank=11 price=1.84 support=1.6 resistance=1.93 liquidity=13598451.0
- ADPC.CA: rank=26.37 outlook=CONSTRUCTIVE outlook_score=54.93 sector_rank=11 price=4.53 support=3.76 resistance=4.6 liquidity=13620735.0
- EHDR.CA: rank=26.37 outlook=CONSTRUCTIVE outlook_score=58.93 sector_rank=11 price=3.13 support=2.69 resistance=3.19 liquidity=17474884.0
- SAUD.CA: rank=25.82 outlook=BULLISH_WATCH outlook_score=73.27 sector_rank=6 price=23.56 support=21.3 resistance=23.62 liquidity=7415551.5
- ZMID.CA: rank=25.7 outlook=BULLISH_WATCH outlook_score=70.99 sector_rank=10 price=7.53 support=7.06 resistance=7.8 liquidity=9305573.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=24.37 buy_ready=True sector_rank=11 price=314.77 support=227.0 resistance=325.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=68.26 liquidity=12270302.0 spike=0.29
- ABUK.CA: score=23.4 buy_ready=False sector_rank=8 price=79.23 support=70.6 resistance=78.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=77.87 liquidity=32600426.0 spike=0.21
- ACAMD.CA: score=18.74 buy_ready=False sector_rank=11 price=2.24 support=2.2 resistance=2.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=45.24 liquidity=9369456.0 spike=0.16
- ACGC.CA: score=7.96 buy_ready=False sector_rank=18 price=13.21 support=12.8 resistance=13.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24748910.0 spike=0.73
- ADCI.CA: score=20.04 buy_ready=True sector_rank=11 price=311.06 support=235.45 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=65.17 liquidity=5666514.5 spike=0.25
- ADIB.CA: score=23.4 buy_ready=False sector_rank=6 price=55.0 support=46.02 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=77.1 liquidity=11688904.0 spike=0.1
- ADPC.CA: score=26.37 buy_ready=True sector_rank=11 price=4.53 support=3.76 resistance=4.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=60.36 liquidity=13620735.0 spike=0.27
- AFDI.CA: score=13.84 buy_ready=False sector_rank=11 price=65.43 support=46.57 resistance=69.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:58 AM market time freshness=DELAYED_CURRENT RSI=81.92 liquidity=2469972.0 spike=0.1
- AFMC.CA: score=24.37 buy_ready=False sector_rank=11 price=240.26 support=77.25 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=73.06 liquidity=24410806.0 spike=0.15
- AJWA.CA: score=28.37 buy_ready=True sector_rank=11 price=199.35 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=64.69 liquidity=21395660.0 spike=0.54
- ALCN.CA: score=21.66 buy_ready=False sector_rank=1 price=32.12 support=28.8 resistance=32.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=79.56 liquidity=5255479.0 spike=0.21
- ALUM.CA: score=16.43 buy_ready=False sector_rank=11 price=28.97 support=22.72 resistance=30.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=80.47 liquidity=5059073.5 spike=0.27
- AMER.CA: score=24.4 buy_ready=False sector_rank=10 price=6.45 support=3.92 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=73.95 liquidity=16723732.0 spike=0.14
- AMES.CA: score=19.25 buy_ready=True sector_rank=11 price=121.31 support=106.59 resistance=136.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=43.67 liquidity=4880986.5 spike=0.07
- AMIA.CA: score=23.37 buy_ready=False sector_rank=11 price=13.39 support=9.41 resistance=13.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=89.6 liquidity=10875117.0 spike=0.61
- AMOC.CA: score=8.82 buy_ready=False sector_rank=15 price=11.34 support=10.91 resistance=11.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=84285792.0 spike=0.77
- APSW.CA: score=-0.07 buy_ready=False sector_rank=11 price=9.17 support=9.01 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=555395.44 spike=0.33
- ARAB.CA: score=21.09 buy_ready=False sector_rank=10 price=0.24 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=8689183.0 spike=0.09
- ARCC.CA: score=20.71 buy_ready=False sector_rank=17 price=75.27 support=55.16 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=83.71 liquidity=47015932.0 spike=0.51
- AREH.CA: score=14.6 buy_ready=False sector_rank=11 price=1.51 support=1.38 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=52.27 liquidity=3223043.5 spike=0.08
- ARVA.CA: score=10.37 buy_ready=False sector_rank=11 price=12.35 support=10.75 resistance=12.6 source=Yahoo Finance as_of=2026-08-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ASCM.CA: score=24.37 buy_ready=True sector_rank=11 price=64.39 support=60.63 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=58.16 liquidity=11235749.0 spike=0.18
- ASPI.CA: score=9.37 buy_ready=False sector_rank=11 price=0.55 support=0.54 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13026668.0 spike=0.3
- ATLC.CA: score=25.34 buy_ready=True sector_rank=16 price=5.53 support=5.0 resistance=5.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=63.85 liquidity=9521426.0 spike=0.52
- ATQA.CA: score=24.4 buy_ready=False sector_rank=8 price=10.98 support=9.56 resistance=11.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=74.75 liquidity=38584504.0 spike=0.66
- AXPH.CA: score=16.87 buy_ready=False sector_rank=11 price=1353.92 support=1121.56 resistance=1460.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=62.99 liquidity=495816.31 spike=0.1
- BINV.CA: score=12.36 buy_ready=False sector_rank=12 price=49.24 support=46.01 resistance=50.9 source=Yahoo Finance as_of=2026-08-15T21:00:00+00:00 freshness=FRESH RSI=73.26 liquidity=0.0 spike=0.0
- BIOC.CA: score=23.37 buy_ready=False sector_rank=11 price=533.0 support=106.61 resistance=563.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=84.02 liquidity=150780512.0 spike=0.7
- BTFH.CA: score=23.82 buy_ready=True sector_rank=16 price=3.13 support=3.05 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=51558816.0 spike=0.23
- CAED.CA: score=19.13 buy_ready=True sector_rank=11 price=130.22 support=96.96 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=39.52 liquidity=4757690.5 spike=0.07
- CANA.CA: score=16.48 buy_ready=False sector_rank=6 price=42.15 support=35.2 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:02 AM market time freshness=DELAYED_CURRENT RSI=78.06 liquidity=3084913.5 spike=0.14
- CCAP.CA: score=24.36 buy_ready=True sector_rank=12 price=5.37 support=5.14 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=45.56 liquidity=154481920.0 spike=0.25
- CCRS.CA: score=18.31 buy_ready=False sector_rank=11 price=2.55 support=2.44 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=27.91 liquidity=8935807.0 spike=0.47
- CEFM.CA: score=16.04 buy_ready=True sector_rank=11 price=135.7 support=108.01 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=55.92 liquidity=1670943.75 spike=0.05
- CERA.CA: score=13.94 buy_ready=False sector_rank=11 price=1.33 support=1.25 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=1564675.75 spike=0.08
- CFGH.CA: score=3.37 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-08-15T21:00:00+00:00 freshness=FRESH RSI=22.22 liquidity=0.0 spike=0.0
- CICH.CA: score=14.28 buy_ready=False sector_rank=16 price=12.63 support=11.8 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=63.19 liquidity=456826.28 spike=0.06
- CIEB.CA: score=22.12 buy_ready=True sector_rank=6 price=24.7 support=23.75 resistance=24.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=57.95 liquidity=5718018.0 spike=0.48
- CIRA.CA: score=24.4 buy_ready=True sector_rank=4 price=38.5 support=30.91 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=68.97 liquidity=10844662.0 spike=0.18
- CLHO.CA: score=25.4 buy_ready=True sector_rank=3 price=17.5 support=16.0 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=54.47 liquidity=17564920.0 spike=0.34
- CNFN.CA: score=23.82 buy_ready=True sector_rank=16 price=4.95 support=4.68 resistance=5.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=52.73 liquidity=14859853.0 spike=0.66
- COMI.CA: score=22.4 buy_ready=False sector_rank=6 price=139.2 support=132.81 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=46.19 liquidity=127266344.0 spike=0.29
- COPR.CA: score=28.37 buy_ready=True sector_rank=11 price=0.45 support=0.37 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=59.26 liquidity=27006542.0 spike=0.72
- COSG.CA: score=26.37 buy_ready=True sector_rank=11 price=1.84 support=1.6 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=67.5 liquidity=13598451.0 spike=0.28
- CPCI.CA: score=17.32 buy_ready=False sector_rank=11 price=543.5 support=440.01 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=71.71 liquidity=2946251.75 spike=0.19
- CSAG.CA: score=16.9 buy_ready=False sector_rank=1 price=41.99 support=31.35 resistance=43.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=85.18 liquidity=2502353.25 spike=0.1
- DAPH.CA: score=9.37 buy_ready=False sector_rank=11 price=131.05 support=130.5 resistance=136.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11830025.0 spike=0.3
- DEIN.CA: score=-0.63 buy_ready=False sector_rank=11 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=16.27 buy_ready=True sector_rank=9 price=29.35 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=65.7 liquidity=1867442.5 spike=0.13
- DSCW.CA: score=24.37 buy_ready=True sector_rank=11 price=2.08 support=1.89 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=70.0 liquidity=30439268.0 spike=0.32
- DTPP.CA: score=24.37 buy_ready=False sector_rank=11 price=298.72 support=222.0 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=74.68 liquidity=18238894.0 spike=0.28
- EALR.CA: score=21.51 buy_ready=True sector_rank=11 price=394.01 support=360.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=59.54 liquidity=5137321.0 spike=0.16
- EASB.CA: score=8.45 buy_ready=False sector_rank=11 price=7.65 support=7.52 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9081709.0 spike=0.91
- EAST.CA: score=22.4 buy_ready=False sector_rank=9 price=36.77 support=36.01 resistance=37.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=48.01 liquidity=29911490.0 spike=0.45
- EBSC.CA: score=15.25 buy_ready=False sector_rank=11 price=1.93 support=1.85 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=48.15 liquidity=881750.13 spike=0.16
- ECAP.CA: score=22.71 buy_ready=False sector_rank=11 price=39.39 support=32.12 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=70.13 liquidity=8340240.5 spike=0.72
- EDFM.CA: score=11.97 buy_ready=False sector_rank=11 price=415.55 support=352.0 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=82.27 liquidity=598166.5 spike=0.1
- EEII.CA: score=22.04 buy_ready=True sector_rank=11 price=3.09 support=2.54 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=61.68 liquidity=5672670.5 spike=0.29
- EFIC.CA: score=25.82 buy_ready=False sector_rank=8 price=235.0 support=184.0 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=78.16 liquidity=80207856.0 spike=2.21
- EFID.CA: score=23.4 buy_ready=False sector_rank=9 price=33.65 support=26.64 resistance=32.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=90.91 liquidity=22944850.0 spike=0.26
- EFIH.CA: score=26.4 buy_ready=True sector_rank=7 price=25.13 support=21.9 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=59647956.0 spike=0.57
- EGAL.CA: score=9.4 buy_ready=False sector_rank=8 price=355.6 support=345.0 resistance=358.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=77487184.0 spike=0.81
- EGAS.CA: score=14.86 buy_ready=True sector_rank=15 price=60.49 support=50.0 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=69.59 liquidity=1038265.94 spike=0.04
- EGBE.CA: score=12.41 buy_ready=False sector_rank=6 price=0.55 support=0.45 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=66.08 liquidity=8104.96 spike=0.05
- EGCH.CA: score=23.4 buy_ready=False sector_rank=8 price=14.48 support=12.69 resistance=14.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=75.57 liquidity=35981496.0 spike=0.31
- EGSA.CA: score=4.15 buy_ready=False sector_rank=14 price=8.66 support=8.65 resistance=9.21 source=Yahoo Finance as_of=2026-08-15T21:00:00+00:00 freshness=FRESH RSI=20.45 liquidity=0.0 spike=0.0
- EGTS.CA: score=23.04 buy_ready=True sector_rank=10 price=19.0 support=17.11 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=61.97 liquidity=6645755.0 spike=0.16
- EHDR.CA: score=26.37 buy_ready=True sector_rank=11 price=3.13 support=2.69 resistance=3.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=53.75 liquidity=17474884.0 spike=0.37
- EKHO.CA: score=9.82 buy_ready=False sector_rank=15 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=19.73 buy_ready=False sector_rank=19 price=2.19 support=2.12 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=12974132.0 spike=0.17
- ELKA.CA: score=16.4 buy_ready=False sector_rank=11 price=1.76 support=1.69 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=30.0 liquidity=9026216.0 spike=0.11
- ELNA.CA: score=5.37 buy_ready=False sector_rank=11 price=37.88 support=36.5 resistance=39.49 source=Yahoo Finance as_of=2026-08-15T21:00:00+00:00 freshness=FRESH RSI=24.19 liquidity=0.0 spike=0.0
- ELSH.CA: score=18.05 buy_ready=False sector_rank=11 price=14.02 support=13.31 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=35.9 liquidity=5680749.0 spike=0.06
- ELWA.CA: score=6.37 buy_ready=False sector_rank=11 price=1.75 support=1.65 resistance=2.09 source=Yahoo Finance as_of=2026-08-15T21:00:00+00:00 freshness=FRESH RSI=28.95 liquidity=0.0 spike=0.0
- EMFD.CA: score=20.19 buy_ready=False sector_rank=10 price=11.69 support=11.08 resistance=12.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=55.7 liquidity=8798873.0 spike=0.15
- ENGC.CA: score=23.97 buy_ready=False sector_rank=11 price=51.92 support=40.11 resistance=51.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=75.06 liquidity=33101340.0 spike=1.3
- EOSB.CA: score=18.37 buy_ready=False sector_rank=11 price=1.55 support=1.52 resistance=1.62 source=Yahoo Finance as_of=2026-08-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- EPCO.CA: score=24.25 buy_ready=True sector_rank=11 price=12.24 support=10.32 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=57.25 liquidity=7874837.0 spike=0.23
- EPPK.CA: score=4.81 buy_ready=False sector_rank=11 price=13.1 support=12.62 resistance=15.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=13.99 liquidity=442271.5 spike=0.49
- ETEL.CA: score=28.15 buy_ready=True sector_rank=14 price=117.46 support=97.54 resistance=116.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=64.0 liquidity=85088152.0 spike=0.69
- ETRS.CA: score=12.09 buy_ready=False sector_rank=11 price=11.47 support=11.36 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=57507844.0 spike=2.36
- EXPA.CA: score=15.24 buy_ready=False sector_rank=6 price=21.18 support=19.36 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=75.56 liquidity=1840090.0 spike=0.05
- FAIT.CA: score=16.77 buy_ready=False sector_rank=6 price=41.95 support=36.1 resistance=40.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=86.86 liquidity=3373675.5 spike=0.91
- FAITA.CA: score=16.42 buy_ready=False sector_rank=6 price=0.99 support=0.96 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:45 AM market time freshness=DELAYED_CURRENT RSI=58.11 liquidity=24095.82 spike=0.53
- FERC.CA: score=16.99 buy_ready=False sector_rank=8 price=81.27 support=75.01 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=70.94 liquidity=2589637.25 spike=0.15
- FWRY.CA: score=24.4 buy_ready=True sector_rank=7 price=19.42 support=18.69 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=48.98 liquidity=52891296.0 spike=0.41
- GBCO.CA: score=24.35 buy_ready=False sector_rank=13 price=30.59 support=29.53 resistance=33.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=58.52 liquidity=10471990.0 spike=0.17
- GDWA.CA: score=16.37 buy_ready=False sector_rank=11 price=0.82 support=0.8 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=18.95 liquidity=12916262.0 spike=0.12
- GGCC.CA: score=24.37 buy_ready=True sector_rank=11 price=1.04 support=0.73 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=59.24 liquidity=30860168.0 spike=0.62
- GIHD.CA: score=16.16 buy_ready=True sector_rank=11 price=65.98 support=49.32 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=66.46 liquidity=1787741.5 spike=0.04
- GMCI.CA: score=9.37 buy_ready=False sector_rank=11 price=1.9 support=1.88 resistance=2.2 source=Yahoo Finance as_of=2026-08-15T21:00:00+00:00 freshness=FRESH RSI=39.13 liquidity=0.0 spike=0.0
- GRCA.CA: score=6.11 buy_ready=False sector_rank=11 price=54.84 support=55.0 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=28.08 liquidity=1737046.0 spike=0.09
- GSSC.CA: score=16.01 buy_ready=True sector_rank=11 price=284.21 support=263.6 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=65.14 liquidity=3634971.25 spike=0.21
- GTWL.CA: score=12.73 buy_ready=False sector_rank=11 price=162.01 support=161.03 resistance=175.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=249109472.0 spike=2.68
- HDBK.CA: score=19.4 buy_ready=False sector_rank=6 price=89.11 support=77.03 resistance=87.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=83.5 liquidity=15678178.0 spike=0.41
- HELI.CA: score=22.4 buy_ready=False sector_rank=10 price=7.9 support=7.71 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=36.53 liquidity=43666656.0 spike=0.25
- HRHO.CA: score=17.82 buy_ready=False sector_rank=16 price=26.4 support=25.95 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=47.72 liquidity=25423852.0 spike=0.26
- ICID.CA: score=19.64 buy_ready=False sector_rank=11 price=14.05 support=7.83 resistance=13.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=93.87 liquidity=6272146.0 spike=0.43
- IDRE.CA: score=17.82 buy_ready=True sector_rank=11 price=54.77 support=44.52 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=64.99 liquidity=1450581.75 spike=0.05
- IFAP.CA: score=23.4 buy_ready=False sector_rank=2 price=20.78 support=18.96 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=77.55 liquidity=13554142.0 spike=0.59
- INFI.CA: score=21.37 buy_ready=False sector_rank=11 price=156.99 support=101.53 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=76.82 liquidity=21278830.0 spike=0.4
- IRON.CA: score=13.39 buy_ready=False sector_rank=8 price=30.51 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=49.51 liquidity=4985609.5 spike=0.55
- ISMA.CA: score=19.89 buy_ready=False sector_rank=11 price=34.5 support=27.27 resistance=36.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=74.68 liquidity=3520868.0 spike=0.13
- ISMQ.CA: score=21.12 buy_ready=True sector_rank=8 price=9.53 support=8.96 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=52.56 liquidity=6719464.5 spike=0.1
- ISPH.CA: score=25.4 buy_ready=True sector_rank=3 price=13.7 support=11.3 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=67.78 liquidity=81495608.0 spike=0.44
- JUFO.CA: score=23.4 buy_ready=False sector_rank=9 price=27.4 support=22.78 resistance=36.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=45.77 liquidity=14831845.0 spike=0.25
- KABO.CA: score=7.96 buy_ready=False sector_rank=18 price=9.26 support=9.2 resistance=9.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17810654.0 spike=0.48
- KWIN.CA: score=9.21 buy_ready=False sector_rank=11 price=86.18 support=79.02 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=31.43 liquidity=1839167.63 spike=0.03
- KZPC.CA: score=14.37 buy_ready=False sector_rank=11 price=12.59 support=11.5 resistance=13.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=50635400.0 spike=4.23
- LCSW.CA: score=15.91 buy_ready=False sector_rank=17 price=33.14 support=30.2 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=36.09 liquidity=4199967.0 spike=0.09
- LUTS.CA: score=9.49 buy_ready=False sector_rank=11 price=1.04 support=1.03 resistance=1.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=66425944.0 spike=1.06
- MAAL.CA: score=16.71 buy_ready=True sector_rank=11 price=8.89 support=8.32 resistance=9.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=47.19 liquidity=2338349.75 spike=0.16
- MASR.CA: score=22.37 buy_ready=False sector_rank=11 price=7.75 support=7.45 resistance=8.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=35.66 liquidity=11760910.0 spike=0.15
- MBSC.CA: score=8.71 buy_ready=False sector_rank=17 price=409.57 support=405.0 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=53673364.0 spike=0.81
- MCQE.CA: score=20.71 buy_ready=False sector_rank=17 price=248.11 support=175.55 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=80.41 liquidity=28306910.0 spike=0.71
- MCRO.CA: score=24.37 buy_ready=True sector_rank=11 price=1.56 support=1.32 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=23599002.0 spike=0.13
- MENA.CA: score=22.27 buy_ready=True sector_rank=10 price=7.42 support=6.83 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=56.19 liquidity=5869108.5 spike=0.96
- MEPA.CA: score=18.51 buy_ready=False sector_rank=11 price=1.86 support=1.69 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=46.51 liquidity=6137844.5 spike=0.1
- MFPC.CA: score=23.4 buy_ready=False sector_rank=8 price=40.41 support=35.37 resistance=40.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=81.4 liquidity=31483592.0 spike=0.36
- MFSC.CA: score=14.9 buy_ready=False sector_rank=11 price=50.39 support=46.0 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=55.73 liquidity=527670.69 spike=0.04
- MHOT.CA: score=16.98 buy_ready=False sector_rank=5 price=18.9 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=63.66 liquidity=4578746.0 spike=0.27
- MICH.CA: score=17.25 buy_ready=False sector_rank=11 price=47.9 support=37.7 resistance=53.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=70.32 liquidity=2881457.25 spike=0.08
- MILS.CA: score=24.37 buy_ready=True sector_rank=11 price=196.5 support=137.23 resistance=211.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=56.18 liquidity=15706377.0 spike=0.27
- MIPH.CA: score=15.73 buy_ready=False sector_rank=3 price=779.74 support=722.7 resistance=828.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=57.62 liquidity=329131.63 spike=0.07
- MOED.CA: score=20.37 buy_ready=False sector_rank=11 price=0.7 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=29.17 liquidity=11992885.0 spike=0.36
- MOIL.CA: score=11.98 buy_ready=False sector_rank=15 price=0.66 support=0.55 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=66.29 liquidity=160146.73 spike=0.26
- MOIN.CA: score=9.37 buy_ready=False sector_rank=11 price=39.2 support=38.0 resistance=39.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17771262.0 spike=0.69
- MOSC.CA: score=15.39 buy_ready=False sector_rank=11 price=334.14 support=282.0 resistance=370.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=87.47 liquidity=2018404.13 spike=0.13
- MPCI.CA: score=24.37 buy_ready=False sector_rank=11 price=391.05 support=242.02 resistance=460.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=73.12 liquidity=45586536.0 spike=0.32
- MPCO.CA: score=23.4 buy_ready=False sector_rank=2 price=2.16 support=1.82 resistance=2.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=77.19 liquidity=12762160.0 spike=0.12
- MPRC.CA: score=15.92 buy_ready=True sector_rank=11 price=46.16 support=43.02 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=55.51 liquidity=1543215.13 spike=0.06
- MTIE.CA: score=21.87 buy_ready=True sector_rank=13 price=9.61 support=8.01 resistance=11.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=51.62 liquidity=5517783.0 spike=0.12
- NAHO.CA: score=4.68 buy_ready=False sector_rank=11 price=0.15 support=0.14 resistance=0.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=310588.5 spike=11.01
- NCCW.CA: score=10.92 buy_ready=False sector_rank=11 price=6.12 support=5.67 resistance=7.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=32.5 liquidity=6543615.0 spike=0.18
- NEDA.CA: score=9.37 buy_ready=False sector_rank=11 price=2.71 support=2.7 resistance=2.95 source=Yahoo Finance as_of=2026-08-15T21:00:00+00:00 freshness=FRESH RSI=37.5 liquidity=0.0 spike=0.0
- NHPS.CA: score=24.37 buy_ready=True sector_rank=11 price=93.13 support=82.25 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=56.77 liquidity=29854706.0 spike=0.47
- NINH.CA: score=22.37 buy_ready=False sector_rank=11 price=22.23 support=20.85 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=47.9 liquidity=11762534.0 spike=0.21
- NIPH.CA: score=22.4 buy_ready=False sector_rank=3 price=399.18 support=193.0 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=81.51 liquidity=184476608.0 spike=0.63
- OBRI.CA: score=16.58 buy_ready=False sector_rank=11 price=33.15 support=31.61 resistance=36.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=35.19 liquidity=6208358.0 spike=0.19
- OCDI.CA: score=23.4 buy_ready=False sector_rank=10 price=34.38 support=26.6 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=92.97 liquidity=11108127.0 spike=0.08
- OCPH.CA: score=19.37 buy_ready=False sector_rank=11 price=283.6 support=225.0 resistance=500.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=38.65 liquidity=13529166.0 spike=0.39
- ODIN.CA: score=24.37 buy_ready=False sector_rank=11 price=3.43 support=2.42 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=73.08 liquidity=11341096.0 spike=0.31
- OFH.CA: score=21.37 buy_ready=False sector_rank=11 price=0.87 support=0.67 resistance=0.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=20548646.0 spike=0.22
- OIH.CA: score=23.36 buy_ready=False sector_rank=12 price=1.76 support=1.41 resistance=1.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=92.5 liquidity=15723895.0 spike=0.14
- OLFI.CA: score=19.68 buy_ready=True sector_rank=9 price=24.94 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=62.13 liquidity=3279292.0 spike=0.05
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=780.19 support=775.06 resistance=794.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=67616648.0 spike=1.0
- ORHD.CA: score=26.4 buy_ready=False sector_rank=10 price=42.62 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=71.98 liquidity=11648065.0 spike=0.07
- ORWE.CA: score=19.14 buy_ready=False sector_rank=18 price=26.31 support=22.55 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=78.85 liquidity=9180577.0 spike=0.12
- PHAR.CA: score=25.4 buy_ready=False sector_rank=3 price=144.95 support=88.05 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=72.45 liquidity=319175776.0 spike=0.84
- PHDC.CA: score=24.4 buy_ready=True sector_rank=10 price=15.17 support=14.32 resistance=15.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=13645295.0 spike=0.06
- PHTV.CA: score=11.72 buy_ready=False sector_rank=11 price=373.02 support=291.51 resistance=447.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=77.24 liquidity=349536.72 spike=0.13
- POUL.CA: score=19.21 buy_ready=False sector_rank=9 price=38.25 support=36.5 resistance=40.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=60.76 liquidity=4809463.0 spike=0.16
- PRCL.CA: score=16.21 buy_ready=False sector_rank=17 price=34.5 support=32.8 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=32.84 liquidity=9494716.0 spike=0.27
- PRDC.CA: score=20.73 buy_ready=False sector_rank=10 price=8.93 support=8.7 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=39.62 liquidity=8330897.0 spike=0.08
- PRMH.CA: score=13.58 buy_ready=False sector_rank=11 price=2.66 support=2.56 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=52.54 liquidity=2205278.5 spike=0.15
- RACC.CA: score=26.73 buy_ready=True sector_rank=11 price=10.67 support=9.8 resistance=10.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=65.31 liquidity=22085736.0 spike=1.18
- RAKT.CA: score=8.37 buy_ready=False sector_rank=11 price=22.63 support=21.66 resistance=24.0 source=Yahoo Finance as_of=2026-08-15T21:00:00+00:00 freshness=FRESH RSI=49.49 liquidity=0.0 spike=0.0
- RAYA.CA: score=10.67 buy_ready=False sector_rank=21 price=7.35 support=6.97 resistance=8.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=21.79 liquidity=53267824.0 spike=0.55
- RMDA.CA: score=25.4 buy_ready=False sector_rank=3 price=6.55 support=4.95 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=71.48 liquidity=33879944.0 spike=0.3
- ROTO.CA: score=20.33 buy_ready=False sector_rank=11 price=51.35 support=40.5 resistance=51.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=78.63 liquidity=6958877.0 spike=0.3
- RREI.CA: score=9.37 buy_ready=False sector_rank=11 price=4.68 support=4.66 resistance=4.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28599742.0 spike=0.44
- RTVC.CA: score=5.08 buy_ready=False sector_rank=11 price=3.79 support=3.73 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=34.29 liquidity=710170.25 spike=0.15
- RUBX.CA: score=9.37 buy_ready=False sector_rank=11 price=13.05 support=12.7 resistance=13.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23373748.0 spike=0.74
- SAUD.CA: score=25.82 buy_ready=True sector_rank=6 price=23.56 support=21.3 resistance=23.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=63.56 liquidity=7415551.5 spike=0.44
- SCEM.CA: score=8.71 buy_ready=False sector_rank=17 price=106.46 support=103.5 resistance=110.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=120198936.0 spike=0.67
- SCFM.CA: score=15.11 buy_ready=False sector_rank=11 price=281.23 support=258.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:01 AM market time freshness=DELAYED_CURRENT RSI=46.95 liquidity=2740760.5 spike=0.09
- SCTS.CA: score=17.46 buy_ready=True sector_rank=4 price=619.1 support=602.01 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=45.94 liquidity=1056205.75 spike=0.12
- SDTI.CA: score=14.39 buy_ready=False sector_rank=11 price=70.66 support=46.6 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=80.94 liquidity=3020870.75 spike=0.11
- SEIG.CA: score=14.33 buy_ready=False sector_rank=11 price=278.97 support=237.0 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=88.17 liquidity=954124.44 spike=0.08
- SIPC.CA: score=11.11 buy_ready=False sector_rank=11 price=5.27 support=5.12 resistance=5.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=106281000.0 spike=1.87
- SKPC.CA: score=23.7 buy_ready=True sector_rank=8 price=17.12 support=15.61 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=65.5 liquidity=54729872.0 spike=1.15
- SMFR.CA: score=22.98 buy_ready=False sector_rank=11 price=266.35 support=225.0 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=74.09 liquidity=8604953.0 spike=0.21
- SNFC.CA: score=13.04 buy_ready=False sector_rank=11 price=10.97 support=10.6 resistance=11.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=1668375.63 spike=0.13
- SPIN.CA: score=12.96 buy_ready=False sector_rank=18 price=20.1 support=19.82 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=120654320.0 spike=4.09
- SPMD.CA: score=20.16 buy_ready=True sector_rank=11 price=0.48 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=63.73 liquidity=5792960.5 spike=0.17
- SUGR.CA: score=24.42 buy_ready=False sector_rank=9 price=51.69 support=46.47 resistance=51.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=71.77 liquidity=14401713.0 spike=1.01
- SVCE.CA: score=21.37 buy_ready=False sector_rank=11 price=11.1 support=9.06 resistance=12.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=75.08 liquidity=27090444.0 spike=0.29
- SWDY.CA: score=7.73 buy_ready=False sector_rank=19 price=121.24 support=120.0 resistance=124.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39978804.0 spike=0.62
- TALM.CA: score=16.7 buy_ready=False sector_rank=4 price=19.64 support=15.65 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=75.04 liquidity=5295907.0 spike=0.13
- TMGH.CA: score=22.4 buy_ready=False sector_rank=10 price=98.0 support=95.2 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=40.91 liquidity=43288668.0 spike=0.13
- TRTO.CA: score=4.39 buy_ready=False sector_rank=11 price=0.05 support=0.04 resistance=0.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22014.61 spike=9.77
- UEFM.CA: score=15.94 buy_ready=True sector_rank=11 price=562.22 support=520.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=68.17 liquidity=1569292.75 spike=0.25
- UEGC.CA: score=13.84 buy_ready=False sector_rank=11 price=2.52 support=2.17 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=1464681.25 spike=0.03
- UNIP.CA: score=18.74 buy_ready=False sector_rank=11 price=0.4 support=0.36 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=45.36 liquidity=6370775.5 spike=0.23
- UNIT.CA: score=14.4 buy_ready=False sector_rank=10 price=20.18 support=17.32 resistance=23.0 source=Yahoo Finance as_of=2026-08-15T21:00:00+00:00 freshness=FRESH RSI=68.05 liquidity=0.0 spike=0.0
- WCDF.CA: score=11.81 buy_ready=False sector_rank=11 price=634.96 support=523.3 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=77.93 liquidity=442356.59 spike=0.08
- WKOL.CA: score=17.51 buy_ready=True sector_rank=11 price=330.76 support=307.0 resistance=363.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=54.62 liquidity=3134209.5 spike=0.13
- ZEOT.CA: score=20.52 buy_ready=False sector_rank=11 price=14.17 support=11.51 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=73.97 liquidity=4149652.0 spike=0.14
- ZMID.CA: score=25.7 buy_ready=True sector_rank=10 price=7.53 support=7.06 resistance=7.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=49.56 liquidity=9305573.0 spike=0.04

## Backtesting Lite
- AJWA.CA: 180d return=60.21%, max drawdown=-21.78%, MA20>MA50 days last20=20, as_of=2026-08-15T21:00:00+00:00
- COPR.CA: 180d return=-22.9%, max drawdown=-53.13%, MA20>MA50 days last20=20, as_of=2026-08-15T21:00:00+00:00
- ETEL.CA: 180d return=78.18%, max drawdown=-30.44%, MA20>MA50 days last20=19, as_of=2026-08-15T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- AJWA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=AJWA For Food Industries Co. Egypt summary=Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture; AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3; Ajwa Egypt turns to losses in 9M Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture: https://english.mubasher.info/news/4532004/Ajwa-Egypt-s-board-approves-capital-increase-to-EGP-500m-joins-new-food-venture/
  - AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3: https://english.mubasher.info/news/4527545/AJWA-Egypt-s-standalone-net-profits-retreat-to-EGP-14m-in-9M-25-amid-shift-to-profitability-in-Q3/
  - Ajwa Egypt turns to losses in 9M: https://english.mubasher.info/news/3883210/Ajwa-Egypt-turns-to-losses-in-9M/
- COPR.CA: status=RECENT_ACCEPTED latest=2026-07-18 age_days=30 sources=3 expected=Copper for Commercial Investment & Real Estate Development summary=Recent disclosures and financial updates for Copper for Commercial Investment & Real Estate Development (COPR.CA) indicate ongoing corporate activities, including an annual general meeting, board decisions, and financial statement releases. The stock has experienced a significant change over the past year.
  - Copper for Commercial Investment & Real Estate Development, Annual General Meeting, Jul 18, 2026.: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYaiMEUyHMG_EJHyMeWzUmPsfqn7DRuV1cHnos3e9o2ExEqEmGYBJBUqfjDQKu8l7XlDzqHrjG0FOvPSV-Sguntl4rjCgQXVAkKuUP7VoCHiMptBrGqo3c92b4OoX5xw==
  - Release from Copper For Commercial Investment & Real Estate Development (COPR.CA) Concerning a Disclosure Form (June 29, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI7zP7DoOWEjaJkCIOz-IZZeKOXPuWXUXkT0oxFXqnuquztqTXTFkLnJMY7y3yCy4iFRI571sSz2rFWWl8aoFovGsX5l1_rvgy2_GhI26WzU7jU1kKXNWQhnt2iOVBH1rRmqw-Gmpz-ghN17aztzw==
  - Copper For Commercial Investment & Real Estate Development (COPR.CA) Financial Statements for the period ended 31/03/2026 (June 24, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI7zP7DoOWEjaJkCIOz-IZZeKOXPuWXUXkT0oxFXqnuquztqTXTFkLnJMY7y3yCy4iFRI571sSz2rFWWl8aoFovGsX5l1_rvgy2_GhI26WzU7jU1kKXNWQhnt2iOVBH1rRmqw-Gmpz-ghN17aztzw==
- ETEL.CA: status=RECENT_ACCEPTED latest=2026-08-13 age_days=4 sources=3 expected=Telecom Egypt summary=Telecom Egypt (ETEL.CA) has released its H1 2026 and Q1 2026 financial results, demonstrating improved profitability and strong underlying business performance. The company also announced a decision not to proceed with a proposed transaction for its Regional Data Center Hub and provided its 2026 financial guidance.
  - Q2 2026 Results: Telecom Egypt Reports Improved Profitability and Efficiency in H1 2026 (August 13, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAoKc_PL-diyd9SbzxBx8K2ci6-7qG2vMnkN1hlKPl3t0haGskQWnWsqtERLXtqZsTzWGL7C3d29TIehaBm1A8NW_x7DbrGzR9ofw=
  - Telecom Egypt Announces It Will Not Proceed with the Proposed RDH Transaction with Helios Investments (July 16, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAoKc_PL-diyd9SbzxBx8K2ci6-7qG2vMnkN1hlKPl3t0haGskQWnWsqtERLXtqZsTzWGL7C3d29TIehaBm1A8NW_x7DbrGzR9ofw=
  - Telecom Egypt (TEEG) Publishes Audited Financial Results for H1 2026 and Earnings Report (August 13, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEK7pHhij800wYAL8jd75NQCHpogy79NajHpGEF5E72_o_6dsiG4Vtnd9tjYwrEvkdE4lBdl1NeLUJrbRfmmt4Rsx6NCxdUl3kc-3jVHYBw5QOzJ-vO6ywQWdnIJbTrWEG2Qc5b_K2dRShmflSIiK6hEsJdGiwuaaA1uBowtUS3hdWz8rmo6zsgss5lUFOhp7YrdXiTNl-Qs9BB-tEZ68U9Scm2nYF55FzbYuvjTivjFCUX__U6m3pnk1WBGEcDtQk=
- RACC.CA: status=RECENT_ACCEPTED latest=2026-07-21 age_days=27 sources=3 expected=Raya Customer Experience summary=Raya Customer Experience (RACC.CA) has reported its Q1 2026 earnings results, showing a consolidated net profit of EGP 78.2 million. The company has also issued several recent disclosures regarding its Board of Directors, shareholder structure, and General Assembly meetings. Its 2025 revenue increased by 12.34%.
  - Raya Customer Experience Reports Earnings Results for the First Quarter Ended March 31, 2026 (May 12, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYVAWjFkvC_k-t3kaHaB1wSeTz1XU9MtVxmv9Pb4ffy7obzoVL75betDU2UCW0YC5-0u8KAyw-oH9YWr9_GYdM8VXj2GhPoepR_7aMfsgF-R1S5s12WkWU_r8AJ4sZC5pIkCamAjOT50aljxxEiUHQOECOuEkHjkVrLAi0_KyD5ac3_GtVBIs=
  - Raya Customer Experience Q1 consol net profit EGP 78.2 million (May 12, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYVAWjFkvC_k-t3kaHaB1wSeTz1XU9MtVxmv9Pb4ffy7obzoVL75betDU2UCW0YC5-0u8KAyw-oH9YWr9_GYdM8VXj2GhPoepR_7aMfsgF-R1S5s12WkWU_r8AJ4sZC5pIkCamAjOT50aljxxEiUHQOECOuEkHjkVrLAi0_KyD5ac3_GtVBIs=
  - Raya Customer Experience (RACC.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 21, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWNt4w26edPoK7QGM-aD3CMZVzJQwfdu48rGfM5NgrcoF8CJXh2oibCFM49kfVlCoBc4ZOJ0xGdWjPz0nEJMwXZGX8xRHwbLni5_gGHr9orNMMYplBGNcMftLZI7MJFCQIOtiW7aajS9WNAvoonNXN
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- ORHD.CA: status=RECENT_ACCEPTED latest=2026-07-15 age_days=33 sources=3 expected=Orascom Development Egypt summary=Orascom Development Egypt (ORHD.CA) has been active with recent financial releases, including FY 2025 and Q1 2026 earnings, presentations, and consolidated financial statements. The company also announced an EGP 18 billion loan for its O West project and held its AGM and EGM.
  - O West 18 billion loan (July 15, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkQ9uq4sLXAMKBFkrPuClkX-3V0xyUVUn0Z00azVyuEckpib92vZTFQ-pLb5UW4QbXqEZqS9ENw_grzB6Z8ZkWfh-3Xta7Yo4QwWe2g2dMmejyykHxkkjoFpBMz0M5Ta-8z0-dn1o=
  - AGM and EGM Invitations (May 12, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkQ9uq4sLXAMKBFkrPuClkX-3V0xyUVUn0Z00azVyuEckpib92vZTFQ-pLb5UW4QbXqEZqS9ENw_grzB6Z8ZkWfh-3Xta7Yo4QwWe2g2dMmejyykHxkkjoFpBMz0M5Ta-8z0-dn1o=
  - FY 2025 Earning Releases: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7yq4dgT0z0crr72n1Mz6fyloHa2rRiroA_cQfxLtVq9oqJ5dIbpyK73xFVCQB9lnFpwTK5qjKgJ7YwjY1IQA8Z-DFdT-vkT2fPlMtW4LTyHtL42oIHPNXC13vx2bUBnNyHbcBG-M=
- COSG.CA: status=RECENT_ACCEPTED latest=2026-07-07 age_days=41 sources=3 expected=Cairo Oil & Soap Company summary=Cairo Oil & Soap Company (COSG.CA) reported revenue growth in Q1 2026 and has released several recent disclosures regarding its Board of Directors, shareholder structure, and Annual General Meetings. The company, with Korra Company as a major shareholder, achieved a turnover of nearly 1 billion Egyptian pounds in 2023.
  - Cairo Oil & Soap Company revenue of 283.63M EGP in Q1 2026, with 13.01% growth (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcJSyH9y76HUPe9lrhhnIQY7NblBydLb8hc1LCe0lg4mabbPhfNmZSX7Ld6et7Vlzu2aWYXb2qxHEZVXyqSQYos6RMB6R7vymIaReS8ir6hH17KAsyirU1ILnNjroFCzme3lbEoJUkxFIKEA==
  - Cairo Oil & Soap Company trailing 12-month revenue of 802.09M EGP (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcJSyH9y76HUPe9lrhhnIQY7NblBydLb8hc1LCe0lg4mabbPhfNmZSX7Ld6et7Vlzu2aWYXb2qxHEZVXyqSQYos6RMB6R7vymIaReS8ir6hH17KAsyirU1ILnNjroFCzme3lbEoJUkxFIKEA==
  - Cairo Oils & Soap (COSG.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 7, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIFmc6JcT852JshbOntawsErclKEzYEDn114R44qkWm5uCQO1yxKsanIgVtrGMhwcXJcnnsNdCeryqQuiTjbYPWGrbdTwp_R2AkgdzqwBpA3b79NX_Rx6JHW7moY6bxqrtROZAOhvw5QtIqFGMGD7y
- ADPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=The Arab Dairy Products Co. summary=Evidence rejected for ADPC.CA: source text did not clearly match ADPC.CA / The Arab Dairy Products Co..

## Warnings
- Evidence for AJWA.CA matches the company but no source/report date was detected.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence rejected for ADPC.CA: source text did not clearly match ADPC.CA / The Arab Dairy Products Co..
