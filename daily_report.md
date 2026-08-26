# Telegram-First EGX Scanner Report

Scan phase: Evening tomorrow plan
Generated UTC: 2026-08-26T18:13:57.404741+00:00
Generated Cairo: 2026-08-26 21:13
Run timing: target 19:30 Cairo | generated Cairo 2026-08-26 21:13 | cron 30 16 * * 0-4
Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-08-26 21:10

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 176/189
- Top sector: Textiles

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, August 26
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 65.0% / above MA50 75.0%
- EGX70 regime: MIXED / above MA20 50.0% / above MA50 71.05%
- Sector breadth: 14.29%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=812925376.0 spike=1.81 score=23.02
- ZMID.CA: liquidity=510322784.0 spike=2.2 score=7.97
- LUTS.CA: liquidity=426493344.0 spike=2.03 score=20.12
- OFH.CA: liquidity=351260096.0 spike=4.47 score=11.06
- GTWL.CA: liquidity=331213152.0 spike=1.0 score=21.06

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: 

## Top Liquidity Spikes
- FAIT.CA: spike=9.37 liquidity=40687024.0 outlook=CONSTRUCTIVE score=62.3 buy_ready=False
- AXPH.CA: spike=5.7 liquidity=48271428.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- OFH.CA: spike=4.47 liquidity=351260096.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CCRS.CA: spike=4.19 liquidity=165983760.0 outlook=BULLISH_WATCH score=79.15 buy_ready=False
- DAPH.CA: spike=3.47 liquidity=136610016.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Textiles: score=10.44 5d=-0.36% 20d=14.88% aboveMA50=100.0%
- #2 Building Materials: score=10.03 5d=2.89% 20d=18.64% aboveMA50=83.33%
- #3 Investment Holding: score=9.9 5d=5.42% 20d=10.0% aboveMA50=100.0%
- #4 Agriculture & Food Production: score=8.83 5d=-0.43% 20d=11.6% aboveMA50=100.0%
- #5 Healthcare: score=8.46 5d=-0.95% 20d=16.1% aboveMA50=100.0%
- #6 Transportation & Logistics: score=8.06 5d=0.02% 20d=13.8% aboveMA50=100.0%
- #7 Banking & Financials: score=7.3 5d=-0.43% 20d=4.43% aboveMA50=90.0%
- #8 Basic Resources & Chemicals: score=5.73 5d=-0.86% 20d=7.04% aboveMA50=80.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- SPIN.CA: BULLISH_WATCH score=95 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended; far above support
- COMI.CA: BULLISH_WATCH score=94.3 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- ORWE.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- KABO.CA: BULLISH_WATCH score=87 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- IFAP.CA: BULLISH_WATCH score=84.83 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- CLHO.CA: BULLISH_WATCH score=84.46 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- SAUD.CA: BULLISH_WATCH score=83.3 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- CIEB.CA: BULLISH_WATCH score=82.3 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ARAB.CA: BULLISH_WATCH score=79.92 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- EBSC.CA: BULLISH_WATCH score=79.15 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=overheated RSI; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=21.06 buy_ready=False sector_rank=10 price=306.44 support=236.15 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=54.02 liquidity=15927062.0 spike=0.26
- ABUK.CA: score=23.29 buy_ready=False sector_rank=8 price=75.76 support=70.9 resistance=80.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.83 liquidity=89219728.0 spike=0.85
- ACAMD.CA: score=17.14 buy_ready=False sector_rank=10 price=2.06 support=1.95 resistance=2.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.62 liquidity=86579976.0 spike=1.54
- ACGC.CA: score=21.68 buy_ready=False sector_rank=1 price=14.68 support=10.12 resistance=14.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=78.5 liquidity=49229092.0 spike=1.14
- ADCI.CA: score=14.76 buy_ready=False sector_rank=10 price=292.35 support=245.0 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=57.23 liquidity=3700088.0 spike=0.18
- ADIB.CA: score=21.4 buy_ready=False sector_rank=7 price=53.56 support=50.1 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.82 liquidity=37781564.0 spike=0.48
- ADPC.CA: score=11.06 buy_ready=False sector_rank=10 price=3.87 support=3.81 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.45 liquidity=13592836.0 spike=0.29
- AFDI.CA: score=6.38 buy_ready=False sector_rank=10 price=55.33 support=55.2 resistance=59.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32421336.0 spike=1.16
- AFMC.CA: score=19.06 buy_ready=False sector_rank=10 price=216.48 support=124.0 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.26 liquidity=41747272.0 spike=0.25
- AJWA.CA: score=11.06 buy_ready=False sector_rank=10 price=181.83 support=180.01 resistance=204.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=33.85 liquidity=14842382.0 spike=0.31
- ALCN.CA: score=19.4 buy_ready=False sector_rank=6 price=30.25 support=28.8 resistance=32.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.79 liquidity=13430188.0 spike=0.54
- ALUM.CA: score=23.4 buy_ready=False sector_rank=10 price=29.65 support=22.72 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=73.19 liquidity=29445542.0 spike=1.17
- AMER.CA: score=5.83 buy_ready=False sector_rank=16 price=6.24 support=5.65 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=103748312.0 spike=1.13
- AMES.CA: score=18.06 buy_ready=False sector_rank=10 price=147.75 support=110.54 resistance=173.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=76.19 liquidity=26821194.0 spike=0.38
- AMIA.CA: score=18.06 buy_ready=False sector_rank=10 price=19.01 support=10.6 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=89.86 liquidity=30490688.0 spike=0.59
- AMOC.CA: score=20.7 buy_ready=False sector_rank=13 price=10.9 support=8.23 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.25 liquidity=109384936.0 spike=0.76
- APSW.CA: score=6.56 buy_ready=False sector_rank=10 price=8.51 support=8.41 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.06 liquidity=1498274.75 spike=0.93
- ARAB.CA: score=26.77 buy_ready=False sector_rank=16 price=0.26 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.1 liquidity=251086624.0 spike=3.1
- ARCC.CA: score=22.4 buy_ready=False sector_rank=2 price=76.19 support=55.4 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=83.29 liquidity=20649798.0 spike=0.2
- AREH.CA: score=11.06 buy_ready=False sector_rank=10 price=1.46 support=1.38 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=26.67 liquidity=10376353.0 spike=0.35
- ARVA.CA: score=6.06 buy_ready=False sector_rank=10 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=14.06 buy_ready=False sector_rank=10 price=62.5 support=61.0 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=21.79 liquidity=12447719.0 spike=0.23
- ASPI.CA: score=19.06 buy_ready=False sector_rank=10 price=0.48 support=0.4 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=60.07 liquidity=40991048.0 spike=0.99
- ATLC.CA: score=14.91 buy_ready=False sector_rank=20 price=5.48 support=5.0 resistance=5.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.41 liquidity=5499467.0 spike=0.28
- ATQA.CA: score=22.07 buy_ready=False sector_rank=8 price=11.53 support=9.66 resistance=11.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.55 liquidity=155634816.0 spike=1.89
- AXPH.CA: score=11.06 buy_ready=False sector_rank=10 price=1687.5 support=1560.0 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48271428.0 spike=5.7
- BINV.CA: score=11.4 buy_ready=False sector_rank=3 price=48.58 support=46.01 resistance=50.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.59 liquidity=997878.63 spike=0.16
- BIOC.CA: score=19.06 buy_ready=False sector_rank=10 price=441.0 support=170.0 resistance=563.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.42 liquidity=81918328.0 spike=0.34
- BTFH.CA: score=8.41 buy_ready=False sector_rank=20 price=2.98 support=2.95 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.42 liquidity=51091464.0 spike=0.24
- CAED.CA: score=21.06 buy_ready=False sector_rank=10 price=149.95 support=118.01 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=70.55 liquidity=15441522.0 spike=0.3
- CANA.CA: score=15.51 buy_ready=False sector_rank=7 price=41.92 support=36.62 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=72.48 liquidity=4111797.75 spike=0.22
- CCAP.CA: score=21.4 buy_ready=False sector_rank=3 price=5.77 support=5.14 resistance=5.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.85 liquidity=298997664.0 spike=0.49
- CCRS.CA: score=26.06 buy_ready=False sector_rank=10 price=2.84 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.04 liquidity=165983760.0 spike=4.19
- CEFM.CA: score=18.1 buy_ready=False sector_rank=10 price=144.24 support=122.1 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=59.41 liquidity=5039040.0 spike=0.16
- CERA.CA: score=11.31 buy_ready=False sector_rank=10 price=1.29 support=1.23 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.91 liquidity=5252667.5 spike=0.35
- CFGH.CA: score=8.07 buy_ready=False sector_rank=10 price=0.11 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=75.0 liquidity=11315.3 spike=0.76
- CICH.CA: score=8.93 buy_ready=False sector_rank=20 price=12.3 support=11.92 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=29.61 liquidity=6523823.5 spike=0.9
- CIEB.CA: score=23.4 buy_ready=False sector_rank=7 price=24.99 support=23.75 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=58.44 liquidity=11285260.0 spike=0.87
- CIRA.CA: score=18.12 buy_ready=False sector_rank=17 price=34.3 support=34.3 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=49.14 liquidity=17403194.0 spike=0.35
- CLHO.CA: score=21.4 buy_ready=False sector_rank=5 price=17.5 support=16.0 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.6 liquidity=33853552.0 spike=0.55
- CNFN.CA: score=14.41 buy_ready=False sector_rank=20 price=4.78 support=4.68 resistance=5.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.08 liquidity=11060822.0 spike=0.56
- COMI.CA: score=23.02 buy_ready=False sector_rank=7 price=139.73 support=135.35 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.51 liquidity=812925376.0 spike=1.81
- COPR.CA: score=20.66 buy_ready=False sector_rank=10 price=0.54 support=0.39 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.87 liquidity=111805904.0 spike=1.3
- COSG.CA: score=23.06 buy_ready=False sector_rank=10 price=1.8 support=1.6 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=45260596.0 spike=0.9
- CPCI.CA: score=14.87 buy_ready=False sector_rank=10 price=544.16 support=440.01 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=69.05 liquidity=5809718.0 spike=0.69
- CSAG.CA: score=23.4 buy_ready=False sector_rank=6 price=39.87 support=31.35 resistance=43.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.57 liquidity=12167074.0 spike=0.51
- DAPH.CA: score=11.0 buy_ready=False sector_rank=10 price=116.0 support=108.25 resistance=124.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=136610016.0 spike=3.47
- DEIN.CA: score=-3.94 buy_ready=False sector_rank=10 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=10.29 buy_ready=False sector_rank=14 price=28.78 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.55 liquidity=4612711.0 spike=0.29
- DSCW.CA: score=11.06 buy_ready=False sector_rank=10 price=1.89 support=1.84 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.73 liquidity=23382180.0 spike=0.26
- DTPP.CA: score=19.06 buy_ready=False sector_rank=10 price=296.1 support=235.59 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.97 liquidity=11189880.0 spike=0.21
- EALR.CA: score=20.62 buy_ready=False sector_rank=10 price=402.29 support=363.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=54.47 liquidity=7564955.5 spike=0.16
- EASB.CA: score=3.52 buy_ready=False sector_rank=10 price=7.66 support=7.61 resistance=8.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7457732.5 spike=0.91
- EAST.CA: score=14.68 buy_ready=False sector_rank=14 price=35.3 support=35.0 resistance=37.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.03 liquidity=62537780.0 spike=0.96
- EBSC.CA: score=27.04 buy_ready=False sector_rank=10 price=2.05 support=1.85 resistance=2.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=73.91 liquidity=24227306.0 spike=2.99
- ECAP.CA: score=16.06 buy_ready=False sector_rank=10 price=33.02 support=32.12 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.67 liquidity=12842143.0 spike=0.91
- EDFM.CA: score=9.72 buy_ready=False sector_rank=10 price=400.84 support=375.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=56.94 liquidity=656559.13 spike=0.22
- EEII.CA: score=21.06 buy_ready=False sector_rank=10 price=2.92 support=2.54 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.93 liquidity=12443882.0 spike=0.48
- EFIC.CA: score=18.29 buy_ready=False sector_rank=8 price=200.35 support=184.0 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.84 liquidity=23515248.0 spike=0.48
- EFID.CA: score=20.68 buy_ready=False sector_rank=14 price=32.09 support=26.7 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=56.76 liquidity=14852475.0 spike=0.17
- EFIH.CA: score=17.78 buy_ready=False sector_rank=18 price=23.85 support=22.15 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.06 liquidity=45375888.0 spike=0.4
- EGAL.CA: score=23.35 buy_ready=False sector_rank=8 price=361.03 support=292.0 resistance=359.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=82.51 liquidity=303730208.0 spike=2.53
- EGAS.CA: score=14.55 buy_ready=False sector_rank=13 price=56.18 support=51.5 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.22 liquidity=5851946.0 spike=0.24
- EGBE.CA: score=11.54 buy_ready=False sector_rank=7 price=0.54 support=0.47 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=60.64 liquidity=143345.28 spike=0.71
- EGCH.CA: score=14.29 buy_ready=False sector_rank=8 price=13.62 support=12.69 resistance=14.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=30.94 liquidity=35060512.0 spike=0.28
- EGSA.CA: score=0.61 buy_ready=False sector_rank=15 price=8.69 support=8.65 resistance=8.99 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=28.0 liquidity=434.5 spike=0.05
- EGTS.CA: score=15.57 buy_ready=False sector_rank=16 price=17.02 support=16.17 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=39.5 liquidity=11446372.0 spike=0.32
- EHDR.CA: score=19.06 buy_ready=False sector_rank=10 price=2.85 support=2.71 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=51.72 liquidity=13693781.0 spike=0.35
- EKHO.CA: score=6.7 buy_ready=False sector_rank=13 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=10.19 buy_ready=False sector_rank=9 price=2.08 support=2.05 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=22.73 liquidity=40701708.0 spike=0.73
- ELKA.CA: score=21.06 buy_ready=False sector_rank=10 price=1.75 support=1.69 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=49302632.0 spike=0.76
- ELNA.CA: score=5.12 buy_ready=False sector_rank=10 price=37.01 support=36.1 resistance=39.24 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=43.32 liquidity=62657.93 spike=0.17
- ELSH.CA: score=11.06 buy_ready=False sector_rank=10 price=13.34 support=12.97 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=15.98 liquidity=27999610.0 spike=0.45
- ELWA.CA: score=13.16 buy_ready=False sector_rank=10 price=1.85 support=1.62 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=64.29 liquidity=2582257.5 spike=1.26
- EMFD.CA: score=22.57 buy_ready=False sector_rank=16 price=12.17 support=11.08 resistance=12.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.28 liquidity=62239184.0 spike=0.77
- ENGC.CA: score=19.06 buy_ready=False sector_rank=10 price=45.88 support=40.11 resistance=54.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.99 liquidity=13168203.0 spike=0.47
- EOSB.CA: score=13.09 buy_ready=False sector_rank=10 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=25892.44 spike=0.46
- EPCO.CA: score=16.09 buy_ready=False sector_rank=10 price=11.06 support=10.32 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.27 liquidity=7025257.5 spike=0.33
- EPPK.CA: score=3.47 buy_ready=False sector_rank=10 price=13.3 support=12.3 resistance=15.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=32.82 liquidity=1285292.63 spike=1.56
- ETEL.CA: score=22.61 buy_ready=False sector_rank=15 price=116.29 support=102.75 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.44 liquidity=117136480.0 spike=0.91
- ETRS.CA: score=19.24 buy_ready=False sector_rank=10 price=10.88 support=10.21 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.07 liquidity=8180087.5 spike=0.27
- EXPA.CA: score=19.4 buy_ready=False sector_rank=7 price=19.98 support=19.7 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=40.86 liquidity=22287284.0 spike=0.59
- FAIT.CA: score=26.4 buy_ready=False sector_rank=7 price=43.52 support=36.1 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.65 liquidity=40687024.0 spike=9.37
- FAITA.CA: score=17.01 buy_ready=False sector_rank=7 price=1.02 support=0.97 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=58.46 liquidity=126473.92 spike=2.74
- FERC.CA: score=12.23 buy_ready=False sector_rank=8 price=77.98 support=75.01 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=55.05 liquidity=3940641.5 spike=0.22
- FWRY.CA: score=9.88 buy_ready=False sector_rank=18 price=18.85 support=18.69 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.42 liquidity=127267312.0 spike=1.05
- GBCO.CA: score=9.32 buy_ready=False sector_rank=21 price=28.6 support=28.12 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.53 liquidity=75405520.0 spike=1.59
- GDWA.CA: score=10.06 buy_ready=False sector_rank=10 price=0.79 support=0.77 resistance=0.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=19.48 liquidity=24974248.0 spike=0.36
- GGCC.CA: score=8.66 buy_ready=False sector_rank=10 price=0.96 support=0.88 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=99955496.0 spike=2.3
- GIHD.CA: score=20.85 buy_ready=False sector_rank=10 price=64.9 support=56.51 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.32 liquidity=9785073.0 spike=0.31
- GMCI.CA: score=3.35 buy_ready=False sector_rank=10 price=1.91 support=1.83 resistance=2.1 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=25.0 liquidity=834507.64 spike=1.73
- GRCA.CA: score=6.06 buy_ready=False sector_rank=10 price=72.64 support=72.33 resistance=79.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48961604.0 spike=0.99
- GSSC.CA: score=13.67 buy_ready=False sector_rank=10 price=286.29 support=266.65 resistance=301.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=60.21 liquidity=2614296.5 spike=0.14
- GTWL.CA: score=21.06 buy_ready=False sector_rank=10 price=218.85 support=211.0 resistance=211.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=331213152.0 spike=1.0
- HDBK.CA: score=17.44 buy_ready=False sector_rank=7 price=96.02 support=80.8 resistance=93.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.51 liquidity=40913752.0 spike=1.02
- HELI.CA: score=14.15 buy_ready=False sector_rank=16 price=7.6 support=7.34 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=20.38 liquidity=200493312.0 spike=1.29
- HRHO.CA: score=8.41 buy_ready=False sector_rank=20 price=25.9 support=25.49 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=13.19 liquidity=47510552.0 spike=0.48
- ICID.CA: score=18.3 buy_ready=False sector_rank=10 price=16.88 support=7.85 resistance=18.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=93.68 liquidity=28953656.0 spike=1.12
- IDRE.CA: score=14.11 buy_ready=False sector_rank=10 price=52.69 support=46.04 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.52 liquidity=3053339.5 spike=0.15
- IFAP.CA: score=21.4 buy_ready=False sector_rank=4 price=20.87 support=19.0 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.08 liquidity=13184511.0 spike=0.42
- INFI.CA: score=21.06 buy_ready=False sector_rank=10 price=157.03 support=104.0 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.95 liquidity=16771566.0 spike=0.24
- IRON.CA: score=10.29 buy_ready=False sector_rank=8 price=30.77 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.69 liquidity=10056090.0 spike=0.85
- ISMA.CA: score=8.32 buy_ready=False sector_rank=10 price=39.26 support=37.0 resistance=39.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=63332528.0 spike=2.13
- ISMQ.CA: score=16.29 buy_ready=False sector_rank=8 price=9.13 support=8.96 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.28 liquidity=19821626.0 spike=0.36
- ISPH.CA: score=19.4 buy_ready=False sector_rank=5 price=12.91 support=11.3 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.22 liquidity=64482592.0 spike=0.34
- JUFO.CA: score=19.68 buy_ready=False sector_rank=14 price=27.11 support=22.78 resistance=28.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.45 liquidity=23217248.0 spike=0.42
- KABO.CA: score=22.42 buy_ready=False sector_rank=1 price=9.16 support=7.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=65.76 liquidity=40125900.0 spike=1.01
- KWIN.CA: score=23.18 buy_ready=False sector_rank=10 price=107.84 support=84.08 resistance=118.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.81 liquidity=61706560.0 spike=1.06
- KZPC.CA: score=18.06 buy_ready=False sector_rank=10 price=12.78 support=8.42 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=76.06 liquidity=19561192.0 spike=0.4
- LCSW.CA: score=21.4 buy_ready=False sector_rank=2 price=34.3 support=30.2 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=50.52 liquidity=21780662.0 spike=0.61
- LUTS.CA: score=20.12 buy_ready=False sector_rank=10 price=1.59 support=0.54 resistance=1.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.16 liquidity=426493344.0 spike=2.03
- MAAL.CA: score=21.06 buy_ready=False sector_rank=10 price=9.48 support=8.32 resistance=9.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.47 liquidity=10137698.0 spike=0.82
- MASR.CA: score=16.06 buy_ready=False sector_rank=10 price=7.52 support=7.45 resistance=8.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.34 liquidity=56319532.0 spike=0.83
- MBSC.CA: score=20.4 buy_ready=False sector_rank=2 price=392.52 support=240.02 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.98 liquidity=47758764.0 spike=0.58
- MCQE.CA: score=23.4 buy_ready=False sector_rank=2 price=234.54 support=178.0 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=68.8 liquidity=15979102.0 spike=0.28
- MCRO.CA: score=19.06 buy_ready=False sector_rank=10 price=1.5 support=1.44 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=42886128.0 spike=0.29
- MENA.CA: score=7.05 buy_ready=False sector_rank=16 price=6.9 support=6.82 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=51.89 liquidity=1484442.0 spike=0.25
- MEPA.CA: score=19.06 buy_ready=False sector_rank=10 price=1.8 support=1.78 resistance=2.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.59 liquidity=10641012.0 spike=0.31
- MFPC.CA: score=21.29 buy_ready=False sector_rank=8 price=39.13 support=35.37 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.39 liquidity=39032524.0 spike=0.45
- MFSC.CA: score=11.92 buy_ready=False sector_rank=10 price=49.32 support=46.02 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=36.11 liquidity=2859463.75 spike=0.25
- MHOT.CA: score=20.58 buy_ready=False sector_rank=12 price=18.38 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.36 liquidity=31624594.0 spike=1.81
- MICH.CA: score=21.06 buy_ready=False sector_rank=10 price=49.01 support=39.01 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.74 liquidity=17202094.0 spike=0.41
- MILS.CA: score=23.06 buy_ready=False sector_rank=10 price=216.04 support=167.0 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.94 liquidity=23524466.0 spike=0.28
- MIPH.CA: score=13.95 buy_ready=False sector_rank=5 price=790.75 support=722.7 resistance=828.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=38.23 liquidity=2546432.25 spike=0.62
- MOED.CA: score=20.06 buy_ready=False sector_rank=10 price=0.79 support=0.65 resistance=0.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=72.93 liquidity=51096608.0 spike=0.57
- MOIL.CA: score=8.84 buy_ready=False sector_rank=13 price=0.66 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=139697.2 spike=0.26
- MOIN.CA: score=21.54 buy_ready=False sector_rank=10 price=34.9 support=23.11 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.4 liquidity=39262784.0 spike=1.24
- MOSC.CA: score=11.93 buy_ready=False sector_rank=10 price=328.57 support=282.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=81.31 liquidity=3869156.25 spike=0.26
- MPCI.CA: score=21.06 buy_ready=False sector_rank=10 price=402.89 support=287.01 resistance=460.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.84 liquidity=95717256.0 spike=0.57
- MPCO.CA: score=21.4 buy_ready=False sector_rank=4 price=2.23 support=1.88 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.6 liquidity=64255856.0 spike=0.5
- MPRC.CA: score=20.46 buy_ready=False sector_rank=10 price=42.5 support=39.5 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.16 liquidity=48143312.0 spike=1.7
- MTIE.CA: score=13.14 buy_ready=False sector_rank=21 price=8.51 support=8.01 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.05 liquidity=24593580.0 spike=0.38
- NAHO.CA: score=8.09 buy_ready=False sector_rank=10 price=0.14 support=0.1 resistance=0.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=85.45 liquidity=30668.69 spike=0.34
- NCCW.CA: score=10.19 buy_ready=False sector_rank=10 price=5.87 support=5.59 resistance=7.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.25 liquidity=4131138.0 spike=0.13
- NEDA.CA: score=13.46 buy_ready=False sector_rank=10 price=2.78 support=2.7 resistance=2.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=50.85 liquidity=396499.97 spike=0.46
- NHPS.CA: score=21.06 buy_ready=False sector_rank=10 price=91.57 support=82.25 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.34 liquidity=21324382.0 spike=0.61
- NINH.CA: score=21.28 buy_ready=False sector_rank=10 price=24.5 support=21.22 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.56 liquidity=45859592.0 spike=1.11
- NIPH.CA: score=21.4 buy_ready=False sector_rank=5 price=372.48 support=209.0 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.41 liquidity=161577200.0 spike=0.48
- OBRI.CA: score=17.06 buy_ready=False sector_rank=10 price=32.47 support=31.61 resistance=34.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.76 liquidity=15429106.0 spike=0.5
- OCDI.CA: score=18.67 buy_ready=False sector_rank=16 price=31.8 support=27.7 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.22 liquidity=142656944.0 spike=1.05
- OCPH.CA: score=13.85 buy_ready=False sector_rank=10 price=257.08 support=225.0 resistance=341.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=54.91 liquidity=6793879.5 spike=0.3
- ODIN.CA: score=21.92 buy_ready=False sector_rank=10 price=3.29 support=2.54 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.5 liquidity=62550936.0 spike=1.43
- OFH.CA: score=11.06 buy_ready=False sector_rank=10 price=1.09 support=0.98 resistance=1.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=351260096.0 spike=4.47
- OIH.CA: score=22.18 buy_ready=False sector_rank=3 price=2.0 support=1.43 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=84.91 liquidity=186580880.0 spike=1.39
- OLFI.CA: score=15.36 buy_ready=False sector_rank=14 price=23.45 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.85 liquidity=6679722.5 spike=0.12
- ORAS.CA: score=4.6 buy_ready=False sector_rank=19 price=832.99 support=813.0 resistance=840.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=262314256.0 spike=1.0
- ORHD.CA: score=20.57 buy_ready=False sector_rank=16 price=42.25 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.02 liquidity=75082600.0 spike=0.51
- ORWE.CA: score=24.4 buy_ready=False sector_rank=1 price=25.52 support=22.55 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.3 liquidity=44284052.0 spike=0.57
- PHAR.CA: score=19.4 buy_ready=False sector_rank=5 price=131.17 support=93.4 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.16 liquidity=98289936.0 spike=0.21
- PHDC.CA: score=15.57 buy_ready=False sector_rank=16 price=14.7 support=14.32 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.0 liquidity=215152224.0 spike=0.94
- PHTV.CA: score=9.7 buy_ready=False sector_rank=10 price=347.01 support=312.0 resistance=447.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.68 liquidity=638083.5 spike=0.23
- POUL.CA: score=17.68 buy_ready=False sector_rank=14 price=38.21 support=36.5 resistance=40.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.24 liquidity=13427537.0 spike=0.51
- PRCL.CA: score=15.69 buy_ready=False sector_rank=2 price=33.2 support=32.0 resistance=37.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.72 liquidity=7290408.0 spike=0.25
- PRDC.CA: score=20.57 buy_ready=False sector_rank=16 price=9.44 support=8.7 resistance=9.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.86 liquidity=36539180.0 spike=0.59
- PRMH.CA: score=7.75 buy_ready=False sector_rank=10 price=2.46 support=2.28 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=32.26 liquidity=6687067.5 spike=0.46
- RACC.CA: score=10.45 buy_ready=False sector_rank=10 price=9.76 support=9.7 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=31.58 liquidity=9389377.0 spike=0.49
- RAKT.CA: score=0.22 buy_ready=False sector_rank=10 price=22.25 support=21.65 resistance=24.0 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=9.2 liquidity=156417.5 spike=0.58
- RAYA.CA: score=18.51 buy_ready=False sector_rank=11 price=7.39 support=6.95 resistance=7.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=88078728.0 spike=1.24
- RMDA.CA: score=21.4 buy_ready=False sector_rank=5 price=6.13 support=5.08 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=58.96 liquidity=16588810.0 spike=0.13
- ROTO.CA: score=19.06 buy_ready=False sector_rank=10 price=44.43 support=41.85 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.6 liquidity=11205486.0 spike=0.48
- RREI.CA: score=19.06 buy_ready=False sector_rank=10 price=4.27 support=4.28 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=24409296.0 spike=0.35
- RTVC.CA: score=15.24 buy_ready=False sector_rank=10 price=4.13 support=3.73 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.56 liquidity=4177473.5 spike=0.53
- RUBX.CA: score=18.48 buy_ready=False sector_rank=10 price=13.01 support=12.02 resistance=13.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=55.58 liquidity=5424671.0 spike=0.3
- SAUD.CA: score=23.4 buy_ready=False sector_rank=7 price=23.03 support=21.4 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.38 liquidity=11258951.0 spike=0.51
- SCEM.CA: score=23.4 buy_ready=False sector_rank=2 price=98.0 support=76.75 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.51 liquidity=130657624.0 spike=0.61
- SCFM.CA: score=21.06 buy_ready=False sector_rank=10 price=288.1 support=272.0 resistance=319.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=52.6 liquidity=12027404.0 spike=0.57
- SCTS.CA: score=9.04 buy_ready=False sector_rank=17 price=620.69 support=603.13 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=76.64 liquidity=1918338.5 spike=0.2
- SDTI.CA: score=21.06 buy_ready=False sector_rank=10 price=70.0 support=55.1 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.12 liquidity=14892661.0 spike=0.44
- SEIG.CA: score=10.09 buy_ready=False sector_rank=10 price=259.1 support=242.1 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.73 liquidity=1027123.0 spike=0.11
- SIPC.CA: score=18.86 buy_ready=False sector_rank=10 price=4.81 support=3.82 resistance=5.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.8 liquidity=7802890.0 spike=0.12
- SKPC.CA: score=18.29 buy_ready=False sector_rank=8 price=17.2 support=15.61 resistance=18.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.11 liquidity=38584192.0 spike=0.54
- SMFR.CA: score=15.73 buy_ready=False sector_rank=10 price=260.85 support=228.88 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=71.33 liquidity=6668944.5 spike=0.25
- SNFC.CA: score=17.16 buy_ready=False sector_rank=10 price=10.61 support=10.3 resistance=11.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.31 liquidity=14906938.0 spike=1.05
- SPIN.CA: score=26.78 buy_ready=False sector_rank=1 price=19.16 support=15.3 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=66.56 liquidity=86287224.0 spike=2.19
- SPMD.CA: score=11.14 buy_ready=False sector_rank=10 price=0.46 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.76 liquidity=7083349.5 spike=0.25
- SUGR.CA: score=20.68 buy_ready=False sector_rank=14 price=57.24 support=46.47 resistance=61.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.14 liquidity=42106348.0 spike=0.82
- SVCE.CA: score=21.06 buy_ready=False sector_rank=10 price=10.95 support=9.06 resistance=12.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=70.37 liquidity=30594062.0 spike=0.3
- SWDY.CA: score=21.19 buy_ready=False sector_rank=9 price=127.99 support=91.8 resistance=133.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.16 liquidity=32954468.0 spike=0.31
- TALM.CA: score=18.12 buy_ready=False sector_rank=17 price=17.54 support=16.35 resistance=20.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.35 liquidity=39844892.0 spike=0.89
- TMGH.CA: score=18.57 buy_ready=False sector_rank=16 price=97.7 support=95.2 resistance=100.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.31 liquidity=152766032.0 spike=0.63
- TRTO.CA: score=15.06 buy_ready=False sector_rank=10 price=0.05 support=0.03 resistance=0.05 source=Yahoo Finance as_of=2026-08-24T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=331.5 spike=0.03
- UEFM.CA: score=10.5 buy_ready=False sector_rank=10 price=537.75 support=531.0 resistance=594.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=45.54 liquidity=1437053.88 spike=0.31
- UEGC.CA: score=15.44 buy_ready=False sector_rank=10 price=2.03 support=1.95 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.95 liquidity=117375248.0 spike=3.19
- UNIP.CA: score=19.06 buy_ready=False sector_rank=10 price=0.37 support=0.35 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.96 liquidity=13214199.0 spike=0.38
- UNIT.CA: score=11.57 buy_ready=False sector_rank=16 price=18.61 support=17.32 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.98 liquidity=3004558.75 spike=0.24
- WCDF.CA: score=9.16 buy_ready=False sector_rank=10 price=642.05 support=571.0 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=75.72 liquidity=1097928.63 spike=0.25
- WKOL.CA: score=17.63 buy_ready=False sector_rank=10 price=347.66 support=310.0 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.37 liquidity=4565616.0 spike=0.13
- ZEOT.CA: score=16.13 buy_ready=False sector_rank=10 price=13.81 support=11.86 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.18 liquidity=5069028.0 spike=0.2
- ZMID.CA: score=7.97 buy_ready=False sector_rank=16 price=8.56 support=7.91 resistance=8.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=510322784.0 spike=2.2

## Backtesting Lite
- EBSC.CA: 180d return=25.88%, max drawdown=-23.41%, MA20>MA50 days last20=20, as_of=2026-08-24T21:00:00+00:00
- SPIN.CA: 180d return=83.63%, max drawdown=-9.8%, MA20>MA50 days last20=20, as_of=2026-08-24T21:00:00+00:00
- ARAB.CA: 180d return=-1.18%, max drawdown=-38.02%, MA20>MA50 days last20=20, as_of=2026-08-24T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- EBSC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Osool ESB Securities Brokerage summary=Evidence rejected for EBSC.CA: source text did not clearly match EBSC.CA / Osool ESB Securities Brokerage.
- SPIN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Spinning and Weaving summary=Evidence rejected for SPIN.CA: source text did not clearly match SPIN.CA / Alexandria Spinning and Weaving.
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- FAIT.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=602 sources=3 expected=Faisal Islamic Bank of Egypt summary=Faisal Islamic Bank of Egypt unveils dividends for 2025; Faisal Islamic Bank of Egypt’s consolidated net profits drop to EGP 4.6bn in 2025; Faisal Islamic Bank of Egypt posts 63% lower standalone net profits in 2025
  - Faisal Islamic Bank of Egypt unveils dividends for 2025: https://english.mubasher.info/news/4585552/Faisal-Islamic-Bank-of-Egypt-unveils-dividends-for-2025/
  - Faisal Islamic Bank of Egypt’s consolidated net profits drop to EGP 4.6bn in 2025: https://english.mubasher.info/news/4582812/Faisal-Islamic-Bank-of-Egypt-s-consolidated-net-profits-drop-to-EGP-4-6bn-in-2025/
  - Faisal Islamic Bank of Egypt posts 63% lower standalone net profits in 2025: https://english.mubasher.info/news/4548875/Faisal-Islamic-Bank-of-Egypt-posts-63-lower-standalone-net-profits-in-2025/
- CCRS.CA: status=OLD_ACCEPTED latest=2016-01-01 age_days=3890 sources=3 expected=Gulf Canadian Company for Arab Real Estate Investment summary=10 EGX-listed firms deny ties to UAE-based Abraaj; Gulf Canadian OGM to discuss 2016 financials Thursday; Gulf Canadian OGM to discuss 2016 results 22 March
  - 10 EGX-listed firms deny ties to UAE-based Abraaj: https://english.mubasher.info/news/3308086/10-EGX-listed-firms-deny-ties-to-UAE-based-Abraaj/
  - Gulf Canadian OGM to discuss 2016 financials Thursday: https://english.mubasher.info/news/3076282/Gulf-Canadian-OGM-to-discuss-2016-financials-Thursday/
  - Gulf Canadian OGM to discuss 2016 results 22 March: https://english.mubasher.info/news/3067564/Gulf-Canadian-OGM-to-discuss-2016-results-22-March/
- ORWE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=602 sources=3 expected=Oriental Weavers summary=Oriental Weavers to disburse EGP 1.5/shr dividends for 2025; Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025; Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25
  - Oriental Weavers to disburse EGP 1.5/shr dividends for 2025: https://english.mubasher.info/news/4590236/Oriental-Weavers-to-disburse-EGP-1-5-shr-dividends-for-2025/
  - Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025: https://english.mubasher.info/news/4562972/Oriental-Weavers-consolidated-profits-cross-EGP-2-2bn-in-2025/
  - Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25: https://english.mubasher.info/news/4487417/Oriental-Weavers-generates-EGP-12-5bn-consolidated-sales-in-H1-25/
- CIEB.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Credit Agricole Egypt summary=Evidence rejected for CIEB.CA: source text did not clearly match CIEB.CA / Credit Agricole Egypt.
- SAUD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=602 sources=3 expected=Al Baraka Bank Egypt summary=Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26; Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE; Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025
  - Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26: https://english.mubasher.info/news/4611927/Al-Baraka-Bank-Egypt-records-EGP-2-2bn-operating-income-in-Q1-26/
  - Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE: https://english.mubasher.info/news/4583822/Al-Baraka-Bank-Egypt-files-MTO-to-acquire-majority-stake-in-A-T-LEASE/
  - Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025: https://english.mubasher.info/news/4583458/Al-Baraka-Bank-Egypt-to-pay-EGP-1-1-share-dividends-for-2025/

## Warnings
- Evidence rejected for EBSC.CA: source text did not clearly match EBSC.CA / Osool ESB Securities Brokerage.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for SPIN.CA: source text did not clearly match SPIN.CA / Alexandria Spinning and Weaving.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence for FAIT.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CCRS.CA matches the company but appears old; latest detected date is 2016-01-01.
- Evidence for ORWE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for CIEB.CA: source text did not clearly match CIEB.CA / Credit Agricole Egypt.
- Evidence for SAUD.CA matches the company but appears old; latest detected date is 2025-01-01.
