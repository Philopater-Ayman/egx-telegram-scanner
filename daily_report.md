# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-07-29T10:45:37.961589+00:00
Generated Cairo: 2026-07-29 13:45
Run timing: target 11:00 Cairo | generated Cairo 2026-07-29 13:45 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-07-29 13:33

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 61
- Data quality issues: 1
- Tradeable price/liquidity tickers: 178/189
- Top sector: Agriculture & Food Production

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, July 29
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 55.0% / above MA50 45.0%
- EGX70 regime: BULLISH / above MA20 69.23% / above MA50 82.05%
- Sector breadth: 52.38%
- Risk mode: SELECTIVE_SMALL_MID_SWINGS

## Top Liquidity
- MPCO.CA: liquidity=413271584.0 spike=6.84 score=34.4
- EAST.CA: liquidity=340085152.0 spike=5.5 score=17.16
- BIOC.CA: liquidity=272161184.0 spike=5.33 score=14.4
- CCAP.CA: liquidity=268666336.0 spike=0.39 score=24.34
- COMI.CA: liquidity=246454976.0 spike=0.57 score=28.4

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 trend is mixed while EGX70 is bullish; sector breadth around 52% and risk mode set to selective small‑mid swings. The scanner flagged MPCO.CA, ARCC.CA and AJWA.CA as priority tickets because they show liquidity accumulation spikes, belong to leading sectors (Agriculture & Food Production, Building Materials, General/Verified EGX Expansion), trade near their 20‑day support levels and carry a BULLISH_WATCH outlook.
- Selection driven by strong liquidity spikes (accumulation regime) and sector leadership, suggesting short‑term buying interest.
- Prices sit a modest distance above 20‑day support and 20‑day resistance; holding support could yield a 1‑3 day bounce, but a break below support raises downside risk.
- EGX30’s mixed trend (weak MA50 breadth) adds caution, whereas EGX70’s bullish bias supports the selective small‑mid swing risk mode.
- Uncertainty remains due to limited fundamental evidence for some tickets, elevated RSI readings, and sectors that are not uniformly leading.

## Top Liquidity Spikes
- TALM.CA: spike=12.16 liquidity=203080960.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MPCO.CA: spike=6.84 liquidity=413271584.0 outlook=BULLISH_WATCH score=100 buy_ready=True
- EAST.CA: spike=5.5 liquidity=340085152.0 outlook=WEAK_OR_RISKY score=13.9 buy_ready=False
- BIOC.CA: spike=5.33 liquidity=272161184.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- PHAR.CA: spike=4.33 liquidity=214450624.0 outlook=CONSTRUCTIVE score=63.27 buy_ready=False

## Sector Leaderboard
- #1 Agriculture & Food Production: score=14.3 5d=3.72% 20d=5.58% aboveMA50=100.0%
- #2 Textiles: score=10.49 5d=3.67% 20d=13.7% aboveMA50=75.0%
- #3 Building Materials: score=9.21 5d=0.39% 20d=14.49% aboveMA50=83.33%
- #4 Industrial Goods & Cables: score=9.11 5d=1.41% 20d=8.41% aboveMA50=100.0%
- #5 Real Estate: score=8.45 5d=0.49% 20d=16.03% aboveMA50=76.92%
- #6 Education: score=8.38 5d=0.01% 20d=12.8% aboveMA50=66.67%
- #7 General / Verified EGX Expansion: score=8.12 5d=0.39% 20d=13.55% aboveMA50=77.67%
- #8 Healthcare: score=7.27 5d=-0.47% 20d=8.3% aboveMA50=83.33%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MPCO.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- ARCC.CA: BULLISH_WATCH score=100 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- MCQE.CA: BULLISH_WATCH score=95.21 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- AJWA.CA: BULLISH_WATCH score=95.12 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- IFAP.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- PRCL.CA: BULLISH_WATCH score=89.21 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MTIE.CA: BULLISH_WATCH score=87.86 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- WCDF.CA: BULLISH_WATCH score=87.12 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended
- ROTO.CA: BULLISH_WATCH score=86.12 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ATQA.CA: BULLISH_WATCH score=85.55 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading

## BUY-Ready Candidates
- MPCO.CA: rank=34.4 outlook=BULLISH_WATCH outlook_score=100 sector_rank=1 price=1.99 support=1.7 resistance=1.95 liquidity=413271584.0
- ATQA.CA: rank=30.7 outlook=BULLISH_WATCH outlook_score=85.55 sector_rank=18 price=10.17 support=9.35 resistance=10.16 liquidity=90098192.0
- ARCC.CA: rank=30.26 outlook=BULLISH_WATCH outlook_score=100 sector_rank=3 price=56.99 support=53.5 resistance=58.5 liquidity=37605724.0
- RMDA.CA: rank=29.2 outlook=BULLISH_WATCH outlook_score=83.27 sector_rank=8 price=5.27 support=4.81 resistance=5.35 liquidity=62229528.0
- COMI.CA: rank=28.4 outlook=BULLISH_WATCH outlook_score=74.05 sector_rank=9 price=141.24 support=126.21 resistance=142.55 liquidity=246454976.0
- AJWA.CA: rank=26.74 outlook=BULLISH_WATCH outlook_score=95.12 sector_rank=7 price=192.99 support=161.0 resistance=210.0 liquidity=54002696.0
- MCQE.CA: rank=26.5 outlook=BULLISH_WATCH outlook_score=95.21 sector_rank=3 price=184.91 support=167.02 resistance=195.0 liquidity=9103804.0
- ADIB.CA: rank=26.4 outlook=CONSTRUCTIVE outlook_score=60.05 sector_rank=9 price=52.1 support=44.31 resistance=52.88 liquidity=80266520.0
- EFIH.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=71.51 sector_rank=11 price=22.79 support=20.1 resistance=24.0 liquidity=21828854.0
- TMGH.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=78.45 sector_rank=5 price=99.38 support=92.1 resistance=103.87 liquidity=166615424.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=21.97 buy_ready=True sector_rank=7 price=238.69 support=197.0 resistance=255.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=59.21 liquidity=5567438.5 spike=0.27
- ABUK.CA: score=22.42 buy_ready=False sector_rank=18 price=71.46 support=66.66 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=55.49 liquidity=20311620.0 spike=0.13
- ACAMD.CA: score=26.4 buy_ready=True sector_rank=7 price=2.36 support=2.15 resistance=2.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=51.43 liquidity=29935756.0 spike=0.4
- ACGC.CA: score=26.4 buy_ready=True sector_rank=2 price=10.54 support=8.92 resistance=11.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=68.85 liquidity=16133059.0 spike=0.54
- ADCI.CA: score=14.56 buy_ready=False sector_rank=7 price=256.1 support=230.0 resistance=269.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=76.53 liquidity=3163652.5 spike=0.28
- ADIB.CA: score=26.4 buy_ready=True sector_rank=9 price=52.1 support=44.31 resistance=52.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=69.6 liquidity=80266520.0 spike=0.62
- ADPC.CA: score=24.4 buy_ready=False sector_rank=7 price=3.97 support=3.32 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=73.68 liquidity=26681496.0 spike=0.81
- AFDI.CA: score=24.4 buy_ready=True sector_rank=7 price=50.76 support=41.84 resistance=52.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=67.14 liquidity=10228412.0 spike=0.61
- AFMC.CA: score=14.22 buy_ready=False sector_rank=7 price=155.64 support=124.0 resistance=155.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=163068384.0 spike=3.41
- AJWA.CA: score=26.74 buy_ready=True sector_rank=7 price=192.99 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=60.64 liquidity=54002696.0 spike=2.17
- ALCN.CA: score=21.09 buy_ready=True sector_rank=17 price=29.25 support=27.7 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=53.97 liquidity=5201966.0 spike=0.23
- ALUM.CA: score=15.05 buy_ready=False sector_rank=7 price=23.09 support=20.55 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=53.41 liquidity=1650876.38 spike=0.26
- AMER.CA: score=23.4 buy_ready=False sector_rank=5 price=4.59 support=2.28 resistance=4.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=89.78 liquidity=83959832.0 spike=0.76
- AMES.CA: score=24.4 buy_ready=False sector_rank=7 price=122.98 support=45.15 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=72.06 liquidity=27461302.0 spike=0.25
- AMIA.CA: score=23.94 buy_ready=False sector_rank=7 price=11.2 support=8.42 resistance=11.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=71.3 liquidity=7540578.0 spike=0.53
- AMOC.CA: score=26.4 buy_ready=True sector_rank=12 price=8.26 support=7.42 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=64.12 liquidity=20778762.0 spike=0.35
- APSW.CA: score=16.09 buy_ready=False sector_rank=7 price=8.85 support=8.0 resistance=9.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=61.29 liquidity=688297.13 spike=0.41
- ARAB.CA: score=24.4 buy_ready=True sector_rank=5 price=0.25 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=41586076.0 spike=0.31
- ARCC.CA: score=30.26 buy_ready=True sector_rank=3 price=56.99 support=53.5 resistance=58.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=59.77 liquidity=37605724.0 spike=1.43
- AREH.CA: score=15.05 buy_ready=False sector_rank=7 price=1.46 support=1.44 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=38.18 liquidity=5645386.0 spike=0.19
- ARVA.CA: score=14.4 buy_ready=False sector_rank=7 price=12.35 support=10.5 resistance=12.6 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=70.61 liquidity=0.0 spike=0.0
- ASCM.CA: score=22.4 buy_ready=False sector_rank=7 price=63.73 support=57.1 resistance=66.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=71.17 liquidity=28613112.0 spike=0.52
- ASPI.CA: score=23.4 buy_ready=False sector_rank=7 price=0.44 support=0.3 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=93.41 liquidity=25742800.0 spike=0.68
- ATLC.CA: score=15.28 buy_ready=False sector_rank=16 price=5.16 support=4.92 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=46.03 liquidity=3069290.5 spike=0.44
- ATQA.CA: score=30.7 buy_ready=True sector_rank=18 price=10.17 support=9.35 resistance=10.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=64.46 liquidity=90098192.0 spike=2.64
- AXPH.CA: score=10.83 buy_ready=False sector_rank=7 price=1208.89 support=1075.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=79.08 liquidity=1426422.88 spike=0.37
- BINV.CA: score=14.87 buy_ready=False sector_rank=15 price=47.88 support=44.98 resistance=51.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=42.4 liquidity=2533462.5 spike=0.35
- BIOC.CA: score=14.4 buy_ready=False sector_rank=7 price=199.8 support=170.0 resistance=199.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=272161184.0 spike=5.33
- BTFH.CA: score=26.21 buy_ready=True sector_rank=16 price=3.1 support=2.91 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=52.5 liquidity=52465904.0 spike=0.24
- CAED.CA: score=21.4 buy_ready=False sector_rank=7 price=128.96 support=69.02 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=77.42 liquidity=52652984.0 spike=0.8
- CANA.CA: score=26.4 buy_ready=True sector_rank=9 price=38.17 support=34.7 resistance=39.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=67.38 liquidity=10952581.0 spike=0.65
- CCAP.CA: score=24.34 buy_ready=True sector_rank=15 price=5.3 support=4.65 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=57.29 liquidity=268666336.0 spike=0.39
- CCRS.CA: score=24.03 buy_ready=True sector_rank=7 price=2.6 support=2.18 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=64.47 liquidity=7634628.0 spike=0.43
- CEFM.CA: score=11.78 buy_ready=False sector_rank=7 price=139.86 support=122.1 resistance=139.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40135208.0 spike=2.19
- CERA.CA: score=24.4 buy_ready=True sector_rank=7 price=1.32 support=1.19 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=62.86 liquidity=13633928.0 spike=0.57
- CFGH.CA: score=15.41 buy_ready=False sector_rank=7 price=0.11 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=60.61 liquidity=10295.54 spike=0.67
- CICH.CA: score=17.36 buy_ready=True sector_rank=16 price=12.16 support=11.6 resistance=12.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=51.3 liquidity=1154816.5 spike=0.22
- CIEB.CA: score=17.47 buy_ready=False sector_rank=9 price=24.1 support=23.3 resistance=24.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=38.46 liquidity=5070628.5 spike=0.58
- CIRA.CA: score=23.82 buy_ready=False sector_rank=6 price=35.77 support=27.45 resistance=36.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=81.31 liquidity=59916156.0 spike=1.21
- CLHO.CA: score=24.4 buy_ready=True sector_rank=8 price=16.85 support=15.9 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=56.17 liquidity=16865218.0 spike=0.38
- CNFN.CA: score=24.21 buy_ready=True sector_rank=16 price=4.85 support=4.61 resistance=5.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=64.1 liquidity=16119004.0 spike=0.79
- COMI.CA: score=28.4 buy_ready=True sector_rank=9 price=141.24 support=126.21 resistance=142.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=58.92 liquidity=246454976.0 spike=0.57
- COPR.CA: score=20.4 buy_ready=False sector_rank=7 price=0.41 support=0.35 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=81.52 liquidity=17269992.0 spike=0.58
- COSG.CA: score=24.4 buy_ready=True sector_rank=7 price=1.67 support=1.47 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=65.22 liquidity=15627396.0 spike=0.35
- CPCI.CA: score=17.4 buy_ready=False sector_rank=7 price=464.84 support=370.1 resistance=512.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=73.91 liquidity=3000392.75 spike=0.26
- CSAG.CA: score=17.12 buy_ready=False sector_rank=17 price=32.33 support=31.57 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=50.22 liquidity=5231556.0 spike=0.34
- DAPH.CA: score=25.6 buy_ready=False sector_rank=7 price=96.89 support=78.8 resistance=98.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=72.96 liquidity=26340450.0 spike=1.6
- DEIN.CA: score=-0.6 buy_ready=False sector_rank=7 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=12.28 buy_ready=False sector_rank=19 price=26.67 support=26.06 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=44.07 liquidity=1122211.75 spike=0.34
- DSCW.CA: score=21.4 buy_ready=False sector_rank=7 price=1.95 support=1.71 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=82.76 liquidity=25541518.0 spike=0.48
- DTPP.CA: score=24.4 buy_ready=False sector_rank=7 price=242.92 support=120.0 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=71.42 liquidity=20757200.0 spike=0.27
- EALR.CA: score=21.15 buy_ready=True sector_rank=7 price=363.66 support=335.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=40.28 liquidity=4746818.5 spike=0.26
- EASB.CA: score=19.29 buy_ready=True sector_rank=7 price=7.54 support=6.88 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=62.87 liquidity=4885172.5 spike=0.35
- EAST.CA: score=17.16 buy_ready=False sector_rank=19 price=36.4 support=36.01 resistance=38.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=31.93 liquidity=340085152.0 spike=5.5
- EBSC.CA: score=8.84 buy_ready=False sector_rank=7 price=1.9 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=29.63 liquidity=1438852.0 spike=0.18
- ECAP.CA: score=17.55 buy_ready=True sector_rank=7 price=33.5 support=31.52 resistance=34.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=62.89 liquidity=1152148.5 spike=0.19
- EDFM.CA: score=17.2 buy_ready=False sector_rank=7 price=388.1 support=310.2 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=73.24 liquidity=2803987.0 spike=0.64
- EEII.CA: score=21.55 buy_ready=False sector_rank=7 price=2.69 support=2.35 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=38.18 liquidity=9154817.0 spike=0.41
- EFIC.CA: score=21.42 buy_ready=False sector_rank=18 price=189.37 support=180.02 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=51.61 liquidity=10931873.0 spike=0.97
- EFID.CA: score=16.52 buy_ready=False sector_rank=19 price=26.98 support=25.85 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=29.81 liquidity=118881864.0 spike=2.68
- EFIH.CA: score=26.4 buy_ready=True sector_rank=11 price=22.79 support=20.1 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=42.67 liquidity=21828854.0 spike=0.35
- EGAL.CA: score=20.42 buy_ready=False sector_rank=18 price=295.59 support=272.28 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=48.3 liquidity=15256649.0 spike=0.36
- EGAS.CA: score=18.58 buy_ready=True sector_rank=12 price=52.33 support=48.1 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=61.84 liquidity=2179769.75 spike=0.17
- EGBE.CA: score=13.23 buy_ready=False sector_rank=9 price=0.47 support=-0.34 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=96.42 liquidity=91736.74 spike=1.87
- EGCH.CA: score=22.42 buy_ready=False sector_rank=18 price=12.93 support=12.13 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=56.22 liquidity=17582910.0 spike=0.29
- EGSA.CA: score=9.41 buy_ready=False sector_rank=13 price=8.86 support=8.67 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=51.52 liquidity=7398.27 spike=0.41
- EGTS.CA: score=11.58 buy_ready=False sector_rank=5 price=17.91 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=33.42 liquidity=7181265.5 spike=0.16
- EHDR.CA: score=24.4 buy_ready=True sector_rank=7 price=2.85 support=2.37 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=65.52 liquidity=28833986.0 spike=0.71
- EKHO.CA: score=8.4 buy_ready=False sector_rank=12 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=25.4 buy_ready=True sector_rank=4 price=2.17 support=2.04 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=62.16 liquidity=40089664.0 spike=0.59
- ELKA.CA: score=24.4 buy_ready=False sector_rank=7 price=1.86 support=1.19 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=72.82 liquidity=46625364.0 spike=0.63
- ELNA.CA: score=16.76 buy_ready=False sector_rank=7 price=38.89 support=36.01 resistance=40.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=50.7 liquidity=360361.94 spike=0.6
- ELSH.CA: score=24.4 buy_ready=True sector_rank=7 price=14.6 support=11.15 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=61.03 liquidity=53841096.0 spike=0.38
- ELWA.CA: score=16.95 buy_ready=False sector_rank=7 price=1.78 support=1.82 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=37.84 liquidity=3851651.5 spike=2.85
- EMFD.CA: score=19.4 buy_ready=False sector_rank=5 price=11.41 support=11.25 resistance=12.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=40.35 liquidity=24240830.0 spike=0.4
- ENGC.CA: score=23.62 buy_ready=False sector_rank=7 price=42.82 support=36.0 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=71.27 liquidity=7221135.5 spike=0.29
- EOSB.CA: score=14.4 buy_ready=False sector_rank=7 price=1.48 support=1.5 resistance=1.55 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=3806.56 spike=0.1
- EPCO.CA: score=21.06 buy_ready=False sector_rank=7 price=10.94 support=8.5 resistance=11.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=77.19 liquidity=9658742.0 spike=0.33
- EPPK.CA: score=17.36 buy_ready=False sector_rank=7 price=15.09 support=12.81 resistance=15.93 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=50.29 liquidity=956374.03 spike=0.78
- ETEL.CA: score=26.4 buy_ready=False sector_rank=13 price=106.5 support=89.01 resistance=107.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=72.61 liquidity=63230656.0 spike=0.77
- ETRS.CA: score=24.4 buy_ready=True sector_rank=7 price=10.63 support=10.39 resistance=10.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=28937344.0 spike=1.0
- EXPA.CA: score=21.42 buy_ready=False sector_rank=9 price=19.89 support=18.05 resistance=20.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=78.76 liquidity=30275634.0 spike=1.01
- FAIT.CA: score=9.91 buy_ready=False sector_rank=9 price=36.83 support=35.06 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=61.71 liquidity=508480.53 spike=0.17
- FAITA.CA: score=9.43 buy_ready=False sector_rank=9 price=0.97 support=0.96 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=41.79 liquidity=25969.85 spike=0.61
- FERC.CA: score=17.39 buy_ready=True sector_rank=18 price=77.49 support=72.75 resistance=85.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=58.06 liquidity=2967495.75 spike=0.25
- FWRY.CA: score=23.4 buy_ready=False sector_rank=11 price=19.0 support=18.15 resistance=19.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=40.59 liquidity=27373628.0 spike=0.21
- GBCO.CA: score=22.34 buy_ready=False sector_rank=14 price=30.16 support=30.12 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=45.23 liquidity=38712236.0 spike=0.53
- GDWA.CA: score=24.08 buy_ready=False sector_rank=7 price=0.82 support=0.76 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=72.67 liquidity=212528288.0 spike=2.34
- GGCC.CA: score=21.4 buy_ready=False sector_rank=7 price=0.84 support=0.45 resistance=0.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=82.85 liquidity=18961108.0 spike=0.5
- GIHD.CA: score=23.4 buy_ready=False sector_rank=7 price=59.34 support=40.66 resistance=65.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=78.97 liquidity=37957148.0 spike=0.75
- GMCI.CA: score=15.22 buy_ready=False sector_rank=7 price=2.07 support=1.71 resistance=2.26 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=49.28 liquidity=820034.61 spike=0.62
- GRCA.CA: score=18.29 buy_ready=False sector_rank=7 price=60.9 support=48.0 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=74.0 liquidity=3887695.0 spike=0.24
- GSSC.CA: score=21.78 buy_ready=True sector_rank=7 price=276.45 support=240.52 resistance=288.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=64.56 liquidity=5379015.0 spike=0.54
- GTWL.CA: score=24.4 buy_ready=True sector_rank=7 price=103.16 support=60.3 resistance=118.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=51.57 liquidity=82090032.0 spike=0.6
- HDBK.CA: score=22.4 buy_ready=False sector_rank=9 price=81.69 support=76.9 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=48.3 liquidity=15273267.0 spike=0.5
- HELI.CA: score=21.4 buy_ready=False sector_rank=5 price=8.05 support=6.36 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=85.71 liquidity=134821632.0 spike=0.71
- HRHO.CA: score=13.21 buy_ready=False sector_rank=16 price=26.48 support=26.09 resistance=27.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=33.73 liquidity=24303958.0 spike=0.28
- ICID.CA: score=18.42 buy_ready=True sector_rank=7 price=8.11 support=6.55 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=54.66 liquidity=4022578.5 spike=0.57
- IDRE.CA: score=24.4 buy_ready=True sector_rank=7 price=47.64 support=41.1 resistance=52.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=66.32 liquidity=10447603.0 spike=0.4
- IFAP.CA: score=26.31 buy_ready=True sector_rank=1 price=19.72 support=18.47 resistance=20.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=54.42 liquidity=6908606.0 spike=0.75
- INFI.CA: score=21.3 buy_ready=False sector_rank=7 price=107.0 support=88.51 resistance=111.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=75.05 liquidity=7904982.0 spike=0.48
- IRON.CA: score=7.09 buy_ready=False sector_rank=18 price=30.76 support=30.45 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=4670286.0 spike=0.69
- ISMA.CA: score=21.54 buy_ready=False sector_rank=7 price=31.62 support=26.54 resistance=32.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=79.46 liquidity=26500946.0 spike=1.07
- ISMQ.CA: score=23.42 buy_ready=True sector_rank=18 price=9.55 support=9.05 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=74067936.0 spike=0.77
- ISPH.CA: score=21.4 buy_ready=False sector_rank=8 price=11.5 support=11.2 resistance=11.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=43.51 liquidity=23041640.0 spike=0.47
- JUFO.CA: score=13.16 buy_ready=False sector_rank=19 price=28.79 support=28.5 resistance=31.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=16.41 liquidity=11505544.0 spike=0.44
- KABO.CA: score=26.4 buy_ready=True sector_rank=2 price=8.0 support=6.04 resistance=8.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=68.56 liquidity=16194025.0 spike=0.34
- KWIN.CA: score=23.4 buy_ready=False sector_rank=7 price=101.01 support=65.0 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=89.58 liquidity=37130396.0 spike=0.73
- KZPC.CA: score=13.19 buy_ready=False sector_rank=7 price=8.49 support=8.26 resistance=8.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=55.36 liquidity=2793947.25 spike=0.55
- LCSW.CA: score=25.4 buy_ready=False sector_rank=3 price=33.92 support=27.43 resistance=37.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=71.46 liquidity=25122300.0 spike=0.34
- LUTS.CA: score=10.67 buy_ready=False sector_rank=7 price=0.56 support=0.57 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=19.38 liquidity=7265877.5 spike=0.21
- MAAL.CA: score=16.76 buy_ready=False sector_rank=7 price=8.75 support=6.92 resistance=8.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=78.06 liquidity=7357623.0 spike=0.45
- MASR.CA: score=24.4 buy_ready=True sector_rank=7 price=7.98 support=6.82 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=58.55 liquidity=30831650.0 spike=0.34
- MBSC.CA: score=21.6 buy_ready=False sector_rank=3 price=245.51 support=222.66 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=49.26 liquidity=7204192.5 spike=0.37
- MCQE.CA: score=26.5 buy_ready=True sector_rank=3 price=184.91 support=167.02 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=58.38 liquidity=9103804.0 spike=0.51
- MCRO.CA: score=24.86 buy_ready=False sector_rank=7 price=1.54 support=1.17 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=207235600.0 spike=1.73
- MENA.CA: score=13.45 buy_ready=False sector_rank=5 price=7.02 support=6.61 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=53.23 liquidity=1046469.13 spike=0.13
- MEPA.CA: score=24.4 buy_ready=True sector_rank=7 price=1.86 support=1.52 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=69.09 liquidity=33276944.0 spike=0.71
- MFPC.CA: score=20.42 buy_ready=False sector_rank=18 price=36.65 support=34.3 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=55.66 liquidity=21502470.0 spike=0.24
- MFSC.CA: score=11.14 buy_ready=False sector_rank=7 price=46.95 support=45.05 resistance=53.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=35.76 liquidity=1744912.63 spike=0.3
- MHOT.CA: score=21.9 buy_ready=False sector_rank=10 price=17.11 support=16.2 resistance=18.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=43.38 liquidity=9502459.0 spike=0.81
- MICH.CA: score=20.03 buy_ready=True sector_rank=7 price=40.87 support=34.0 resistance=43.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=68.11 liquidity=5631744.0 spike=0.35
- MILS.CA: score=10.08 buy_ready=False sector_rank=7 price=188.73 support=167.0 resistance=188.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51812684.0 spike=1.34
- MIPH.CA: score=15.85 buy_ready=False sector_rank=8 price=733.85 support=630.5 resistance=780.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=71.65 liquidity=1449367.63 spike=0.43
- MOED.CA: score=18.92 buy_ready=False sector_rank=7 price=0.7 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=46.9 liquidity=27958390.0 spike=1.26
- MOIL.CA: score=17.75 buy_ready=False sector_rank=12 price=0.68 support=0.46 resistance=0.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=88.24 liquidity=1532178.62 spike=2.41
- MOIN.CA: score=8.59 buy_ready=False sector_rank=7 price=23.6 support=22.66 resistance=24.76 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=41.28 liquidity=185661.2 spike=0.24
- MOSC.CA: score=22.57 buy_ready=True sector_rank=7 price=284.3 support=250.55 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=61.26 liquidity=6166679.0 spike=0.48
- MPCI.CA: score=23.4 buy_ready=False sector_rank=7 price=296.99 support=223.51 resistance=298.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=88.57 liquidity=69676624.0 spike=0.7
- MPCO.CA: score=34.4 buy_ready=True sector_rank=1 price=1.99 support=1.7 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=61.7 liquidity=413271584.0 spike=6.84
- MPRC.CA: score=24.4 buy_ready=False sector_rank=7 price=46.99 support=37.15 resistance=45.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=73.54 liquidity=20441660.0 spike=0.67
- MTIE.CA: score=26.22 buy_ready=True sector_rank=14 price=9.54 support=8.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=51.91 liquidity=43569640.0 spike=1.94
- NAHO.CA: score=3.43 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=26192.19 spike=0.81
- NCCW.CA: score=26.4 buy_ready=False sector_rank=7 price=7.02 support=5.82 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=73.8 liquidity=25644820.0 spike=0.96
- NEDA.CA: score=11.16 buy_ready=False sector_rank=7 price=2.72 support=2.7 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=43.9 liquidity=997176.75 spike=1.38
- NHPS.CA: score=24.4 buy_ready=False sector_rank=7 price=86.75 support=61.55 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=72.3 liquidity=16280548.0 spike=0.19
- NINH.CA: score=21.4 buy_ready=False sector_rank=7 price=22.11 support=17.4 resistance=23.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=75.5 liquidity=12897332.0 spike=0.3
- NIPH.CA: score=21.4 buy_ready=False sector_rank=8 price=225.91 support=157.01 resistance=242.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=80.94 liquidity=91838288.0 spike=0.6
- OBRI.CA: score=19.4 buy_ready=False sector_rank=7 price=33.96 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=38.98 liquidity=20832982.0 spike=0.51
- OCDI.CA: score=25.62 buy_ready=True sector_rank=5 price=28.67 support=23.91 resistance=28.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=57.83 liquidity=141926480.0 spike=1.61
- OCPH.CA: score=22.17 buy_ready=False sector_rank=7 price=469.77 support=341.4 resistance=496.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=94.23 liquidity=8771760.0 spike=0.36
- ODIN.CA: score=11.34 buy_ready=False sector_rank=7 price=2.74 support=2.54 resistance=2.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32465624.0 spike=1.97
- OFH.CA: score=23.4 buy_ready=False sector_rank=7 price=0.72 support=0.57 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=81.48 liquidity=14308534.0 spike=0.22
- OIH.CA: score=26.34 buy_ready=False sector_rank=15 price=1.49 support=1.4 resistance=1.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=73.33 liquidity=20021006.0 spike=0.29
- OLFI.CA: score=25.16 buy_ready=True sector_rank=19 price=22.99 support=21.0 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=53.91 liquidity=10877284.0 spike=0.31
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=715.51 support=712.0 resistance=717.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=77103272.0 spike=1.0
- ORHD.CA: score=26.4 buy_ready=True sector_rank=5 price=39.93 support=37.2 resistance=40.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=54.71 liquidity=60763704.0 spike=0.41
- ORWE.CA: score=25.4 buy_ready=False sector_rank=2 price=22.85 support=21.95 resistance=23.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=47.9 liquidity=19968354.0 spike=0.83
- PHAR.CA: score=31.4 buy_ready=False sector_rank=8 price=96.13 support=83.6 resistance=97.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=73.1 liquidity=214450624.0 spike=4.33
- PHDC.CA: score=19.4 buy_ready=False sector_rank=5 price=14.61 support=14.3 resistance=15.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=44.13 liquidity=103338264.0 spike=0.44
- PHTV.CA: score=16.1 buy_ready=False sector_rank=7 price=326.73 support=255.0 resistance=327.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=84.68 liquidity=2698210.0 spike=0.5
- POUL.CA: score=16.16 buy_ready=False sector_rank=19 price=37.99 support=36.52 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=32.01 liquidity=10833120.0 spike=0.31
- PRCL.CA: score=22.14 buy_ready=True sector_rank=3 price=35.4 support=30.21 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=50.12 liquidity=6743770.0 spike=0.14
- PRDC.CA: score=24.4 buy_ready=True sector_rank=5 price=9.4 support=7.0 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=56.05 liquidity=97847928.0 spike=0.83
- PRMH.CA: score=16.2 buy_ready=False sector_rank=7 price=2.66 support=2.36 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=54.39 liquidity=3802212.5 spike=0.22
- RACC.CA: score=20.32 buy_ready=True sector_rank=7 price=10.14 support=9.36 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=49.27 liquidity=5916504.5 spike=0.27
- RAKT.CA: score=12.9 buy_ready=False sector_rank=7 price=22.63 support=21.25 resistance=23.7 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=47.93 liquidity=316254.24 spike=1.09
- RAYA.CA: score=16.77 buy_ready=False sector_rank=21 price=7.51 support=7.01 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=35.81 liquidity=80546840.0 spike=0.59
- RMDA.CA: score=29.2 buy_ready=True sector_rank=8 price=5.27 support=4.81 resistance=5.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=62229528.0 spike=2.4
- ROTO.CA: score=24.11 buy_ready=True sector_rank=7 price=43.97 support=38.0 resistance=46.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=58.75 liquidity=5712267.5 spike=0.28
- RREI.CA: score=14.4 buy_ready=False sector_rank=7 price=4.93 support=4.54 resistance=4.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=161271008.0 spike=3.75
- RTVC.CA: score=17.33 buy_ready=False sector_rank=7 price=3.88 support=3.55 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=2929668.75 spike=0.65
- RUBX.CA: score=22.4 buy_ready=False sector_rank=7 price=12.85 support=11.07 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=50.28 liquidity=10148639.0 spike=0.14
- SAUD.CA: score=22.13 buy_ready=True sector_rank=9 price=22.32 support=20.0 resistance=22.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=57.75 liquidity=5729088.0 spike=0.6
- SCEM.CA: score=24.4 buy_ready=False sector_rank=3 price=83.99 support=60.14 resistance=87.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=87.72 liquidity=68506104.0 spike=0.99
- SCFM.CA: score=9.86 buy_ready=False sector_rank=7 price=305.13 support=272.0 resistance=307.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26574724.0 spike=1.23
- SCTS.CA: score=16.02 buy_ready=True sector_rank=6 price=612.74 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=44.86 liquidity=1615533.25 spike=0.23
- SDTI.CA: score=24.48 buy_ready=False sector_rank=7 price=56.63 support=45.55 resistance=58.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=85.44 liquidity=19592016.0 spike=1.54
- SEIG.CA: score=16.52 buy_ready=True sector_rank=7 price=249.51 support=183.0 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=59.26 liquidity=2124914.75 spike=0.09
- SIPC.CA: score=21.62 buy_ready=False sector_rank=7 price=3.95 support=3.25 resistance=4.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=75.26 liquidity=25515228.0 spike=1.11
- SKPC.CA: score=19.36 buy_ready=False sector_rank=18 price=15.93 support=14.8 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=49.88 liquidity=9938808.0 spike=0.28
- SMFR.CA: score=16.77 buy_ready=True sector_rank=7 price=231.11 support=189.3 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=66.44 liquidity=2371540.5 spike=0.11
- SNFC.CA: score=14.1 buy_ready=False sector_rank=7 price=11.12 support=11.04 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=44.54 liquidity=4695753.0 spike=0.42
- SPIN.CA: score=24.22 buy_ready=False sector_rank=2 price=15.83 support=14.0 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=77.36 liquidity=32644042.0 spike=1.41
- SPMD.CA: score=26.86 buy_ready=False sector_rank=7 price=0.46 support=0.41 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=74.24 liquidity=31896782.0 spike=1.23
- SUGR.CA: score=13.72 buy_ready=False sector_rank=19 price=47.03 support=45.31 resistance=47.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=46.03 liquidity=2555906.5 spike=0.47
- SVCE.CA: score=22.4 buy_ready=False sector_rank=7 price=9.25 support=8.8 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=44.85 liquidity=11921424.0 spike=0.22
- SWDY.CA: score=24.4 buy_ready=False sector_rank=4 price=93.88 support=84.3 resistance=97.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=70.73 liquidity=11630763.0 spike=0.56
- TALM.CA: score=14.4 buy_ready=False sector_rank=6 price=18.1 support=16.35 resistance=19.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=203080960.0 spike=12.16
- TMGH.CA: score=26.4 buy_ready=True sector_rank=5 price=99.38 support=92.1 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=54.91 liquidity=166615424.0 spike=0.46
- TRTO.CA: score=10.4 buy_ready=False sector_rank=7 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=170.0 spike=0.15
- UEFM.CA: score=8.25 buy_ready=False sector_rank=7 price=587.89 support=536.0 resistance=594.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7391422.0 spike=1.73
- UEGC.CA: score=21.7 buy_ready=False sector_rank=7 price=2.41 support=1.33 resistance=2.74 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=80.0 liquidity=57821567.97 spike=1.15
- UNIP.CA: score=24.86 buy_ready=False sector_rank=7 price=0.39 support=0.3 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=75.86 liquidity=68092568.0 spike=2.73
- UNIT.CA: score=15.49 buy_ready=True sector_rank=5 price=17.96 support=12.0 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=53.41 liquidity=1085640.0 spike=0.04
- WCDF.CA: score=22.43 buy_ready=True sector_rank=7 price=595.0 support=504.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=64.97 liquidity=4426260.0 spike=1.8
- WKOL.CA: score=18.94 buy_ready=True sector_rank=7 price=310.32 support=273.1 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=43.6 liquidity=2539194.25 spike=0.25
- ZEOT.CA: score=24.4 buy_ready=False sector_rank=7 price=11.92 support=10.6 resistance=12.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=71.56 liquidity=12212865.0 spike=0.37
- ZMID.CA: score=24.4 buy_ready=False sector_rank=5 price=7.69 support=6.19 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=70.62 liquidity=163342672.0 spike=0.65

## Backtesting Lite
- MPCO.CA: 180d return=9.04%, max drawdown=-20.56%, MA20>MA50 days last20=20, as_of=2026-07-27T21:00:00+00:00
- PHAR.CA: 180d return=23.98%, max drawdown=-11.3%, MA20>MA50 days last20=15, as_of=2026-07-27T21:00:00+00:00
- ATQA.CA: 180d return=-1.65%, max drawdown=-22.5%, MA20>MA50 days last20=1, as_of=2026-07-27T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=574 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- PHAR.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian International Pharmaceutical Industries summary=Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
- ATQA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr National Steel Ataqa summary=Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- ARCC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=574 sources=3 expected=Arabian Cement Company summary=Arabian Cement to pay out EGP 2bn dividends for 2025; Arabian Cement’s EGM approves nearly EGP 8m capital cut; Arabian Cement’s consolidated profits near EGP 3.6bn in 2025
  - Arabian Cement to pay out EGP 2bn dividends for 2025: https://english.mubasher.info/news/4587912/Arabian-Cement-to-pay-out-EGP-2bn-dividends-for-2025/
  - Arabian Cement’s EGM approves nearly EGP 8m capital cut: https://english.mubasher.info/news/4583762/Arabian-Cement-s-EGM-approves-nearly-EGP-8m-capital-cut/
  - Arabian Cement’s consolidated profits near EGP 3.6bn in 2025: https://english.mubasher.info/news/4562679/Arabian-Cement-s-consolidated-profits-near-EGP-3-6bn-in-2025/
- RMDA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tenth of Ramadan Pharmaceutical Industries summary=Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- COMI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Commercial International Bank Egypt summary=Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- SPMD.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Speed Medical Co summary=Speed Medical’s stock reflects strong technical breakthrough; Speed Medical turns to losses in 9M-22; Shareholder ups stake in Speed Medical for EGP 3.5m
  - Speed Medical’s stock reflects strong technical breakthrough: https://english.mubasher.info/news/4546374/Speed-Medical-s-stock-reflects-strong-technical-breakthrough/
  - Speed Medical turns to losses in 9M-22: https://english.mubasher.info/news/4054471/Speed-Medical-turns-to-losses-in-9M-22/
  - Shareholder ups stake in Speed Medical for EGP 3.5m: https://english.mubasher.info/news/4049449/Shareholder-ups-stake-in-Speed-Medical-for-EGP-3-5m/
- AJWA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=AJWA For Food Industries Co. Egypt summary=Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture; AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3; Ajwa Egypt turns to losses in 9M
  - Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture: https://english.mubasher.info/news/4532004/Ajwa-Egypt-s-board-approves-capital-increase-to-EGP-500m-joins-new-food-venture/
  - AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3: https://english.mubasher.info/news/4527545/AJWA-Egypt-s-standalone-net-profits-retreat-to-EGP-14m-in-9M-25-amid-shift-to-profitability-in-Q3/
  - Ajwa Egypt turns to losses in 9M: https://english.mubasher.info/news/3883210/Ajwa-Egypt-turns-to-losses-in-9M/

## Warnings
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
- Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- Evidence for ARCC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- Evidence for SPMD.CA matches the company but no source/report date was detected.
- Evidence for AJWA.CA matches the company but no source/report date was detected.
