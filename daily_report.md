# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-08-26T08:38:47.819997+00:00
Generated Cairo: 2026-08-26 11:38
Run timing: target 11:00 Cairo | generated Cairo 2026-08-26 11:38 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-08-26 11:35

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 169/189
- Top sector: Investment Holding

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, August 26
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 68.42% / above MA50 73.68%
- EGX70 regime: MIXED / above MA20 55.26% / above MA50 76.32%
- Sector breadth: 14.29%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=375592288.0 spike=0.88 score=21.4
- EGAL.CA: liquidity=213462064.0 spike=1.98 score=7.99
- LUTS.CA: liquidity=205916192.0 spike=1.14 score=5.89
- ORAS.CA: liquidity=190160448.0 spike=1.0 score=4.6
- OFH.CA: liquidity=133110872.0 spike=1.8 score=7.21

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: {
  "summary": "EGX30 and EGX70 show mixed trends with weak sector breadth (14.29%), keeping risk mode defensive; scanner highlights tickets with constructive outlook and liquidity spikes but flags overheated RSI and proximity to resistance, implying limited upside and uncertainty over

## Top Liquidity Spikes
- EOSB.CA: spike=5.39 liquidity=300617.33 outlook=CONSTRUCTIVE score=59.03 buy_ready=False
- FAIT.CA: spike=5.06 liquidity=22323256.0 outlook=CONSTRUCTIVE score=59.26 buy_ready=False
- CCRS.CA: spike=3.64 liquidity=106550968.0 outlook=CONSTRUCTIVE score=62.03 buy_ready=False
- FAITA.CA: spike=2.22 liquidity=85652.26 outlook=CONSTRUCTIVE score=52.26 buy_ready=False
- EGAL.CA: spike=1.98 liquidity=213462064.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=10.51 5d=6.53% 20d=6.33% aboveMA50=100.0%
- #2 Agriculture & Food Production: score=9.69 5d=2.27% 20d=12.71% aboveMA50=100.0%
- #3 Textiles: score=9.12 5d=-1.27% 20d=15.95% aboveMA50=100.0%
- #4 Building Materials: score=8.35 5d=-2.52% 20d=21.3% aboveMA50=100.0%
- #5 Healthcare: score=8.02 5d=-0.84% 20d=13.41% aboveMA50=100.0%
- #6 Transportation & Logistics: score=7.88 5d=-0.73% 20d=16.23% aboveMA50=100.0%
- #7 Banking & Financials: score=6.26 5d=-0.79% 20d=4.84% aboveMA50=90.0%
- #8 Industrial Goods & Cables: score=5.61 5d=-0.62% 20d=12.86% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- IFAP.CA: BULLISH_WATCH score=95.69 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- BINV.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- CLHO.CA: BULLISH_WATCH score=84.02 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- RUBX.CA: BULLISH_WATCH score=83.03 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- KABO.CA: BULLISH_WATCH score=81.12 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- ISPH.CA: BULLISH_WATCH score=78.02 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- CIEB.CA: BULLISH_WATCH score=76.26 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- COMI.CA: BULLISH_WATCH score=75.26 liquidity=TRADEABLE sector=IMPROVING risk=close to resistance
- ORWE.CA: BULLISH_WATCH score=75.12 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; overheated RSI
- UNIT.CA: BULLISH_WATCH score=75.06 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=19.13 buy_ready=False sector_rank=13 price=316.05 support=236.15 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=64.48 liquidity=6516487.5 spike=0.1
- ABUK.CA: score=21.03 buy_ready=False sector_rank=9 price=75.46 support=70.88 resistance=80.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=70.75 liquidity=34821684.0 spike=0.33
- ACAMD.CA: score=10.61 buy_ready=False sector_rank=13 price=2.04 support=1.95 resistance=2.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=23.46 liquidity=36248772.0 spike=0.64
- ACGC.CA: score=21.4 buy_ready=False sector_rank=3 price=14.5 support=10.12 resistance=14.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=79.8 liquidity=16778974.0 spike=0.35
- ADCI.CA: score=11.37 buy_ready=False sector_rank=13 price=291.05 support=245.0 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=760345.63 spike=0.04
- ADIB.CA: score=14.46 buy_ready=False sector_rank=7 price=53.92 support=50.1 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=66.28 liquidity=5062866.0 spike=0.06
- ADPC.CA: score=12.96 buy_ready=False sector_rank=13 price=3.9 support=3.81 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=48.51 liquidity=4347232.0 spike=0.09
- AFDI.CA: score=3.88 buy_ready=False sector_rank=13 price=57.9 support=56.67 resistance=59.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8265576.0 spike=0.33
- AFMC.CA: score=17.94 buy_ready=False sector_rank=13 price=227.0 support=124.0 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=59.83 liquidity=7330449.5 spike=0.04
- AJWA.CA: score=11.2 buy_ready=False sector_rank=13 price=182.78 support=180.01 resistance=204.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=40.28 liquidity=2583615.5 spike=0.05
- ALCN.CA: score=15.16 buy_ready=False sector_rank=6 price=30.23 support=28.8 resistance=32.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=57.94 liquidity=5757714.5 spike=0.23
- ALUM.CA: score=22.61 buy_ready=False sector_rank=13 price=30.19 support=22.72 resistance=30.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=73.33 liquidity=19604954.0 spike=0.89
- AMER.CA: score=17.26 buy_ready=False sector_rank=12 price=5.73 support=4.44 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=52.97 liquidity=8637490.0 spike=0.09
- AMES.CA: score=17.61 buy_ready=False sector_rank=13 price=148.73 support=110.54 resistance=173.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=79.79 liquidity=15293114.0 spike=0.21
- AMIA.CA: score=14.71 buy_ready=False sector_rank=13 price=19.42 support=10.35 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=96.74 liquidity=5095891.0 spike=0.1
- AMOC.CA: score=17.49 buy_ready=False sector_rank=14 price=10.75 support=8.23 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=76.88 liquidity=26308158.0 spike=0.19
- APSW.CA: score=8.85 buy_ready=False sector_rank=13 price=8.69 support=8.41 resistance=9.39 source=Yahoo Finance as_of=2026-08-23T21:00:00+00:00 freshness=FRESH RSI=43.7 liquidity=1236187.2 spike=0.97
- ARAB.CA: score=18.62 buy_ready=False sector_rank=12 price=0.26 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=65.85 liquidity=67282648.0 spike=0.82
- ARCC.CA: score=14.55 buy_ready=False sector_rank=4 price=75.51 support=55.4 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=83.51 liquidity=6146136.5 spike=0.06
- AREH.CA: score=2.99 buy_ready=False sector_rank=13 price=1.46 support=1.38 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=25.81 liquidity=2378736.0 spike=0.08
- ARVA.CA: score=5.61 buy_ready=False sector_rank=13 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=6.69 buy_ready=False sector_rank=13 price=62.36 support=61.0 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=20.84 liquidity=3077543.0 spike=0.06
- ASPI.CA: score=20.61 buy_ready=False sector_rank=13 price=0.49 support=0.4 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=60.07 liquidity=12519598.0 spike=0.3
- ATLC.CA: score=10.24 buy_ready=False sector_rank=20 price=5.4 support=5.0 resistance=5.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=940375.44 spike=0.05
- ATQA.CA: score=18.03 buy_ready=False sector_rank=9 price=11.4 support=9.66 resistance=11.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=78.57 liquidity=60268556.0 spike=0.74
- AXPH.CA: score=1.37 buy_ready=False sector_rank=13 price=1586.17 support=1560.0 resistance=1595.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5756392.0 spike=0.7
- BINV.CA: score=16.93 buy_ready=False sector_rank=1 price=48.77 support=46.01 resistance=50.9 source=Yahoo Finance as_of=2026-08-23T21:00:00+00:00 freshness=FRESH RSI=44.34 liquidity=2533552.75 spike=0.47
- BIOC.CA: score=20.61 buy_ready=False sector_rank=13 price=455.0 support=142.5 resistance=563.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=55.1 liquidity=26159872.0 spike=0.11
- BTFH.CA: score=8.3 buy_ready=False sector_rank=20 price=3.0 support=2.96 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=31.82 liquidity=24800278.0 spike=0.12
- CAED.CA: score=16.91 buy_ready=False sector_rank=13 price=150.01 support=118.01 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=71.12 liquidity=6297896.0 spike=0.12
- CANA.CA: score=11.84 buy_ready=False sector_rank=7 price=41.6 support=36.62 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=71.43 liquidity=435884.0 spike=0.02
- CCAP.CA: score=24.4 buy_ready=False sector_rank=1 price=5.84 support=5.14 resistance=5.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=71.72 liquidity=94010832.0 spike=0.14
- CCRS.CA: score=27.61 buy_ready=False sector_rank=13 price=2.92 support=2.4 resistance=2.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=106550968.0 spike=3.64
- CEFM.CA: score=14.37 buy_ready=False sector_rank=13 price=145.93 support=122.1 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=63.21 liquidity=1755056.13 spike=0.05
- CERA.CA: score=6.41 buy_ready=False sector_rank=13 price=1.29 support=1.23 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=799013.94 spike=0.05
- CFGH.CA: score=9.62 buy_ready=False sector_rank=13 price=0.12 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-08-23T21:00:00+00:00 freshness=FRESH RSI=83.33 liquidity=12787.38 spike=0.86
- CICH.CA: score=5.5 buy_ready=False sector_rank=20 price=12.13 support=11.92 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=37.18 liquidity=1202157.5 spike=0.17
- CIEB.CA: score=14.72 buy_ready=False sector_rank=7 price=24.99 support=23.75 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=57.91 liquidity=1321201.5 spike=0.1
- CIRA.CA: score=10.32 buy_ready=False sector_rank=15 price=35.32 support=33.56 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=52.58 liquidity=1978334.63 spike=0.04
- CLHO.CA: score=21.4 buy_ready=False sector_rank=5 price=17.63 support=16.0 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=44.24 liquidity=11537379.0 spike=0.2
- CNFN.CA: score=10.75 buy_ready=False sector_rank=20 price=4.75 support=4.68 resistance=5.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=45.9 liquidity=6452328.5 spike=0.32
- COMI.CA: score=21.4 buy_ready=False sector_rank=7 price=141.3 support=135.35 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=46.78 liquidity=375592288.0 spike=0.88
- COPR.CA: score=5.61 buy_ready=False sector_rank=13 price=0.56 support=0.54 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=62995076.0 spike=0.73
- COSG.CA: score=15.94 buy_ready=False sector_rank=13 price=1.81 support=1.6 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=73.68 liquidity=5328774.0 spike=0.1
- CPCI.CA: score=9.14 buy_ready=False sector_rank=13 price=542.69 support=440.01 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=69.71 liquidity=531531.69 spike=0.06
- CSAG.CA: score=16.31 buy_ready=False sector_rank=6 price=39.71 support=31.35 resistance=43.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=75.25 liquidity=7913457.5 spike=0.33
- DAPH.CA: score=20.65 buy_ready=False sector_rank=13 price=113.32 support=92.1 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=58.15 liquidity=39927592.0 spike=1.02
- DEIN.CA: score=-4.39 buy_ready=False sector_rank=13 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=3.9 buy_ready=False sector_rank=16 price=28.02 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=28.54 liquidity=1029791.44 spike=0.07
- DSCW.CA: score=11.32 buy_ready=False sector_rank=13 price=1.86 support=1.86 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=38.46 liquidity=5704636.0 spike=0.06
- DTPP.CA: score=13.27 buy_ready=False sector_rank=13 price=296.8 support=235.59 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=74.08 liquidity=4654663.0 spike=0.09
- EALR.CA: score=15.64 buy_ready=False sector_rank=13 price=404.32 support=363.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=59.64 liquidity=3030574.25 spike=0.06
- EASB.CA: score=0.14 buy_ready=False sector_rank=13 price=7.81 support=7.8 resistance=8.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4530947.0 spike=0.6
- EAST.CA: score=8.49 buy_ready=False sector_rank=16 price=35.37 support=35.8 resistance=37.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=45.29 liquidity=2623573.5 spike=0.05
- EBSC.CA: score=5.35 buy_ready=False sector_rank=13 price=2.14 support=2.09 resistance=2.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8633496.0 spike=1.55
- ECAP.CA: score=1.02 buy_ready=False sector_rank=13 price=33.3 support=33.22 resistance=34.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5404920.5 spike=0.44
- EDFM.CA: score=11.38 buy_ready=False sector_rank=13 price=404.31 support=375.0 resistance=425.0 source=Yahoo Finance as_of=2026-08-23T21:00:00+00:00 freshness=FRESH RSI=56.63 liquidity=766167.45 spike=0.27
- EEII.CA: score=14.01 buy_ready=False sector_rank=13 price=2.89 support=2.54 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=60.45 liquidity=3398553.25 spike=0.13
- EFIC.CA: score=17.94 buy_ready=False sector_rank=9 price=200.11 support=184.0 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=62.37 liquidity=9914130.0 spike=0.21
- EFID.CA: score=12.32 buy_ready=False sector_rank=16 price=31.82 support=26.64 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=69.44 liquidity=2449611.5 spike=0.03
- EFIH.CA: score=17.55 buy_ready=False sector_rank=18 price=23.61 support=22.15 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=44.73 liquidity=9994769.0 spike=0.09
- EGAL.CA: score=7.99 buy_ready=False sector_rank=9 price=360.7 support=353.0 resistance=373.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=213462064.0 spike=1.98
- EGAS.CA: score=10.02 buy_ready=False sector_rank=14 price=57.31 support=50.0 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=43.54 liquidity=1528151.75 spike=0.06
- EGBE.CA: score=11.45 buy_ready=False sector_rank=7 price=0.54 support=0.47 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=63.68 liquidity=53986.1 spike=0.26
- EGCH.CA: score=14.03 buy_ready=False sector_rank=9 price=13.41 support=12.69 resistance=14.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=33.53 liquidity=10469683.0 spike=0.08
- EGSA.CA: score=0.79 buy_ready=False sector_rank=10 price=8.69 support=8.65 resistance=9.0 source=Yahoo Finance as_of=2026-08-23T21:00:00+00:00 freshness=FRESH RSI=28.0 liquidity=2693.9 spike=0.27
- EGTS.CA: score=8.17 buy_ready=False sector_rank=12 price=17.11 support=16.17 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=43.3 liquidity=2545136.0 spike=0.07
- EHDR.CA: score=13.23 buy_ready=False sector_rank=13 price=2.9 support=2.71 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=57.83 liquidity=4622995.5 spike=0.12
- EKHO.CA: score=6.49 buy_ready=False sector_rank=14 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-23T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=10.24 buy_ready=False sector_rank=8 price=2.07 support=2.06 resistance=2.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=14998953.0 spike=0.27
- ELKA.CA: score=18.61 buy_ready=False sector_rank=13 price=1.74 support=1.69 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=48.0 liquidity=11221960.0 spike=0.17
- ELNA.CA: score=4.67 buy_ready=False sector_rank=13 price=37.01 support=36.1 resistance=39.24 source=Yahoo Finance as_of=2026-08-23T21:00:00+00:00 freshness=FRESH RSI=44.41 liquidity=58845.9 spike=0.16
- ELSH.CA: score=4.39 buy_ready=False sector_rank=13 price=13.24 support=12.97 resistance=15.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=17.65 liquidity=3777362.25 spike=0.05
- ELWA.CA: score=14.68 buy_ready=False sector_rank=13 price=1.92 support=1.62 resistance=1.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=69.23 liquidity=1928494.38 spike=1.07
- EMFD.CA: score=22.62 buy_ready=False sector_rank=12 price=12.2 support=11.08 resistance=12.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=69.54 liquidity=45420260.0 spike=0.59
- ENGC.CA: score=9.48 buy_ready=False sector_rank=13 price=45.51 support=40.11 resistance=54.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=53.63 liquidity=870863.94 spike=0.03
- EOSB.CA: score=17.91 buy_ready=False sector_rank=13 price=1.57 support=1.5 resistance=1.62 source=Yahoo Finance as_of=2026-08-23T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=300617.33 spike=5.39
- EPCO.CA: score=11.07 buy_ready=False sector_rank=13 price=11.26 support=10.32 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=48.65 liquidity=2462991.75 spike=0.11
- EPPK.CA: score=1.17 buy_ready=False sector_rank=13 price=13.33 support=12.3 resistance=15.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:02 AM market time freshness=DELAYED_CURRENT RSI=33.64 liquidity=559838.81 spike=0.63
- ETEL.CA: score=22.79 buy_ready=False sector_rank=10 price=116.48 support=102.75 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=64.2 liquidity=25311240.0 spike=0.19
- ETRS.CA: score=11.82 buy_ready=False sector_rank=13 price=10.85 support=10.21 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=62.64 liquidity=1206255.5 spike=0.04
- EXPA.CA: score=15.13 buy_ready=False sector_rank=7 price=20.0 support=19.7 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=38.13 liquidity=5733337.0 spike=0.15
- FAIT.CA: score=26.4 buy_ready=False sector_rank=7 price=42.91 support=36.1 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=71.51 liquidity=22323256.0 spike=5.06
- FAITA.CA: score=15.93 buy_ready=False sector_rank=7 price=1.0 support=0.97 resistance=1.0 source=Yahoo Finance as_of=2026-08-23T21:00:00+00:00 freshness=FRESH RSI=67.86 liquidity=85652.26 spike=2.22
- FERC.CA: score=10.56 buy_ready=False sector_rank=9 price=78.49 support=75.01 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=55.64 liquidity=534522.81 spike=0.03
- FWRY.CA: score=16.56 buy_ready=False sector_rank=18 price=18.85 support=18.69 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=49.06 liquidity=26933068.0 spike=0.24
- GBCO.CA: score=3.44 buy_ready=False sector_rank=21 price=27.8 support=27.51 resistance=28.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32884070.0 spike=0.74
- GDWA.CA: score=6.65 buy_ready=False sector_rank=13 price=0.78 support=0.78 resistance=0.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=7036275.5 spike=0.09
- GGCC.CA: score=18.61 buy_ready=False sector_rank=13 price=0.93 support=0.81 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=40.73 liquidity=25760494.0 spike=0.55
- GIHD.CA: score=12.07 buy_ready=False sector_rank=13 price=62.34 support=56.51 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=60.28 liquidity=1460432.38 spike=0.04
- GMCI.CA: score=0.78 buy_ready=False sector_rank=13 price=1.91 support=1.88 resistance=2.1 source=Yahoo Finance as_of=2026-08-23T21:00:00+00:00 freshness=FRESH RSI=30.77 liquidity=171762.48 spike=0.36
- GRCA.CA: score=19.61 buy_ready=False sector_rank=13 price=75.35 support=54.7 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=85.39 liquidity=23192956.0 spike=0.5
- GSSC.CA: score=11.19 buy_ready=False sector_rank=13 price=287.9 support=266.0 resistance=301.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=62.13 liquidity=577070.56 spike=0.03
- GTWL.CA: score=20.61 buy_ready=False sector_rank=13 price=213.12 support=211.0 resistance=211.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=55007492.0 spike=1.0
- HDBK.CA: score=12.0 buy_ready=False sector_rank=7 price=92.98 support=80.8 resistance=93.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=70.44 liquidity=4604031.5 spike=0.12
- HELI.CA: score=13.62 buy_ready=False sector_rank=12 price=7.54 support=7.48 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=22.76 liquidity=69179216.0 spike=0.43
- HRHO.CA: score=8.3 buy_ready=False sector_rank=20 price=25.88 support=25.95 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=24.16 liquidity=13531084.0 spike=0.15
- ICID.CA: score=17.61 buy_ready=False sector_rank=13 price=17.07 support=7.85 resistance=18.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=94.28 liquidity=19616214.0 spike=0.77
- IDRE.CA: score=9.35 buy_ready=False sector_rank=13 price=51.76 support=46.04 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=62.24 liquidity=739940.13 spike=0.04
- IFAP.CA: score=19.95 buy_ready=False sector_rank=2 price=20.99 support=19.0 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=53.46 liquidity=6546112.5 spike=0.21
- INFI.CA: score=12.69 buy_ready=False sector_rank=13 price=159.5 support=104.0 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=75.04 liquidity=5073362.5 spike=0.07
- IRON.CA: score=8.76 buy_ready=False sector_rank=9 price=31.12 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=39.33 liquidity=3731041.25 spike=0.32
- ISMA.CA: score=3.02 buy_ready=False sector_rank=13 price=37.62 support=37.0 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7409913.5 spike=0.26
- ISMQ.CA: score=11.8 buy_ready=False sector_rank=9 price=9.16 support=8.96 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=52.63 liquidity=2773524.5 spike=0.05
- ISPH.CA: score=19.01 buy_ready=False sector_rank=5 price=13.1 support=11.3 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=44.09 liquidity=7611947.5 spike=0.04
- JUFO.CA: score=16.29 buy_ready=False sector_rank=16 price=26.87 support=22.78 resistance=28.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=51.15 liquidity=8426837.0 spike=0.15
- KABO.CA: score=24.4 buy_ready=False sector_rank=3 price=9.03 support=7.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=63.06 liquidity=13507572.0 spike=0.34
- KWIN.CA: score=5.61 buy_ready=False sector_rank=13 price=111.27 support=108.0 resistance=116.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31833626.0 spike=0.59
- KZPC.CA: score=15.52 buy_ready=False sector_rank=13 price=13.11 support=8.42 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=77.81 liquidity=7912803.0 spike=0.17
- LCSW.CA: score=12.05 buy_ready=False sector_rank=4 price=34.49 support=30.2 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=43.66 liquidity=2652015.0 spike=0.07
- LUTS.CA: score=5.89 buy_ready=False sector_rank=13 price=1.56 support=1.48 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=205916192.0 spike=1.14
- MAAL.CA: score=1.11 buy_ready=False sector_rank=13 price=9.25 support=9.17 resistance=9.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5502366.5 spike=0.48
- MASR.CA: score=15.61 buy_ready=False sector_rank=13 price=7.55 support=7.45 resistance=8.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=38.71 liquidity=12156726.0 spike=0.18
- MBSC.CA: score=12.61 buy_ready=False sector_rank=4 price=388.7 support=240.02 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=82.58 liquidity=4207184.0 spike=0.05
- MCQE.CA: score=16.22 buy_ready=False sector_rank=4 price=235.57 support=178.0 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=68.43 liquidity=4816380.0 spike=0.09
- MCRO.CA: score=13.44 buy_ready=False sector_rank=13 price=1.51 support=1.44 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=4832195.0 spike=0.03
- MENA.CA: score=6.3 buy_ready=False sector_rank=12 price=6.93 support=6.82 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=54.72 liquidity=672406.19 spike=0.11
- MEPA.CA: score=9.16 buy_ready=False sector_rank=13 price=1.81 support=1.78 resistance=2.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=551091.69 spike=0.01
- MFPC.CA: score=20.03 buy_ready=False sector_rank=9 price=39.21 support=35.37 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=79.84 liquidity=10844722.0 spike=0.12
- MFSC.CA: score=9.29 buy_ready=False sector_rank=13 price=49.37 support=46.02 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=52.44 liquidity=674908.19 spike=0.06
- MHOT.CA: score=18.76 buy_ready=False sector_rank=11 price=18.75 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=57.6 liquidity=17017194.0 spike=0.97
- MICH.CA: score=17.67 buy_ready=False sector_rank=13 price=49.0 support=39.01 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=51.97 liquidity=7054903.0 spike=0.17
- MILS.CA: score=18.73 buy_ready=False sector_rank=13 price=223.49 support=167.0 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=66.06 liquidity=8121457.5 spike=0.1
- MIPH.CA: score=10.56 buy_ready=False sector_rank=5 price=775.21 support=722.7 resistance=828.36 source=Yahoo Finance as_of=2026-08-23T21:00:00+00:00 freshness=FRESH RSI=41.63 liquidity=1156613.35 spike=0.3
- MOED.CA: score=16.61 buy_ready=False sector_rank=13 price=0.79 support=0.65 resistance=0.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=79.15 liquidity=22941626.0 spike=0.25
- MOIL.CA: score=8.54 buy_ready=False sector_rank=14 price=0.67 support=0.63 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=50.52 liquidity=51282.61 spike=0.1
- MOIN.CA: score=16.05 buy_ready=False sector_rank=13 price=34.49 support=23.11 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=59.48 liquidity=5439432.5 spike=0.17
- MOSC.CA: score=9.68 buy_ready=False sector_rank=13 price=328.51 support=282.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=79.55 liquidity=2070677.38 spike=0.14
- MPCI.CA: score=20.61 buy_ready=False sector_rank=13 price=405.65 support=284.0 resistance=460.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=73.15 liquidity=13572659.0 spike=0.08
- MPCO.CA: score=23.4 buy_ready=False sector_rank=2 price=2.28 support=1.84 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=68.6 liquidity=14366578.0 spike=0.11
- MPRC.CA: score=11.82 buy_ready=False sector_rank=13 price=41.77 support=39.5 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=43.93 liquidity=3211931.0 spike=0.11
- MTIE.CA: score=13.44 buy_ready=False sector_rank=21 price=8.52 support=8.01 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=52.31 liquidity=11181186.0 spike=0.17
- NAHO.CA: score=7.62 buy_ready=False sector_rank=13 price=0.14 support=0.1 resistance=0.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:49 AM market time freshness=DELAYED_CURRENT RSI=85.45 liquidity=9373.89 spike=0.1
- NCCW.CA: score=6.51 buy_ready=False sector_rank=13 price=5.85 support=5.59 resistance=7.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=52.87 liquidity=900007.19 spike=0.03
- NEDA.CA: score=9.93 buy_ready=False sector_rank=13 price=2.77 support=2.7 resistance=2.97 source=Yahoo Finance as_of=2026-08-23T21:00:00+00:00 freshness=FRESH RSI=53.57 liquidity=317309.04 spike=0.42
- NHPS.CA: score=15.62 buy_ready=False sector_rank=13 price=93.14 support=82.25 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=65.8 liquidity=7011564.5 spike=0.2
- NINH.CA: score=5.61 buy_ready=False sector_rank=13 price=24.86 support=24.53 resistance=25.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25479594.0 spike=0.79
- NIPH.CA: score=19.4 buy_ready=False sector_rank=5 price=379.08 support=209.0 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=66.64 liquidity=53715644.0 spike=0.16
- OBRI.CA: score=12.84 buy_ready=False sector_rank=13 price=31.91 support=31.61 resistance=34.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=49.04 liquidity=6228388.5 spike=0.19
- OCDI.CA: score=18.62 buy_ready=False sector_rank=12 price=31.71 support=27.7 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=64.55 liquidity=39258404.0 spike=0.29
- OCPH.CA: score=11.83 buy_ready=False sector_rank=13 price=265.08 support=225.0 resistance=341.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=56.61 liquidity=2213953.75 spike=0.1
- ODIN.CA: score=5.61 buy_ready=False sector_rank=13 price=3.28 support=3.26 resistance=3.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42762792.0 spike=0.99
- OFH.CA: score=7.21 buy_ready=False sector_rank=13 price=1.03 support=0.98 resistance=1.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=133110872.0 spike=1.8
- OIH.CA: score=23.4 buy_ready=False sector_rank=1 price=1.96 support=1.43 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=85.45 liquidity=53019232.0 spike=0.42
- OLFI.CA: score=9.49 buy_ready=False sector_rank=16 price=23.38 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=42.45 liquidity=1625251.88 spike=0.03
- ORAS.CA: score=4.6 buy_ready=False sector_rank=17 price=829.0 support=813.0 resistance=840.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=190160448.0 spike=1.0
- ORHD.CA: score=20.62 buy_ready=False sector_rank=12 price=42.01 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=56.03 liquidity=10247046.0 spike=0.06
- ORWE.CA: score=22.06 buy_ready=False sector_rank=3 price=25.67 support=22.55 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=72.05 liquidity=9660152.0 spike=0.12
- PHAR.CA: score=21.4 buy_ready=False sector_rank=5 price=131.71 support=92.85 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=49.64 liquidity=35599708.0 spike=0.08
- PHDC.CA: score=15.62 buy_ready=False sector_rank=12 price=14.74 support=14.32 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=37.2 liquidity=13660482.0 spike=0.06
- PHTV.CA: score=8.97 buy_ready=False sector_rank=13 price=350.19 support=312.0 resistance=447.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:02 AM market time freshness=DELAYED_CURRENT RSI=57.84 liquidity=356681.44 spike=0.13
- POUL.CA: score=8.3 buy_ready=False sector_rank=16 price=38.06 support=36.5 resistance=40.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=46.1 liquidity=3435015.5 spike=0.13
- PRCL.CA: score=11.31 buy_ready=False sector_rank=4 price=33.69 support=32.0 resistance=37.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=39.17 liquidity=1909345.5 spike=0.06
- PRDC.CA: score=11.36 buy_ready=False sector_rank=12 price=9.18 support=8.7 resistance=9.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=2734482.5 spike=0.04
- PRMH.CA: score=-1.07 buy_ready=False sector_rank=13 price=2.45 support=2.44 resistance=2.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3316509.75 spike=0.27
- RACC.CA: score=8.86 buy_ready=False sector_rank=13 price=9.77 support=9.8 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=38.0 liquidity=3245192.75 spike=0.17
- RAKT.CA: score=-0.21 buy_ready=False sector_rank=13 price=22.25 support=21.65 resistance=24.0 source=Yahoo Finance as_of=2026-08-23T21:00:00+00:00 freshness=FRESH RSI=9.2 liquidity=180514.25 spike=0.65
- RAYA.CA: score=11.52 buy_ready=False sector_rank=19 price=7.32 support=6.95 resistance=7.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=23.71 liquidity=33889292.0 spike=0.46
- RMDA.CA: score=18.78 buy_ready=False sector_rank=5 price=6.15 support=5.08 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=56.52 liquidity=7383157.5 spike=0.06
- ROTO.CA: score=11.68 buy_ready=False sector_rank=13 price=45.38 support=41.85 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=51.25 liquidity=3068273.5 spike=0.13
- RREI.CA: score=13.7 buy_ready=False sector_rank=13 price=4.36 support=4.26 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=50.6 liquidity=5085507.5 spike=0.07
- RTVC.CA: score=12.53 buy_ready=False sector_rank=13 price=4.15 support=3.73 resistance=4.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=69.66 liquidity=1915335.25 spike=0.26
- RUBX.CA: score=16.05 buy_ready=False sector_rank=13 price=12.98 support=12.02 resistance=13.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=58.63 liquidity=1439808.63 spike=0.08
- SAUD.CA: score=14.25 buy_ready=False sector_rank=7 price=23.22 support=21.4 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=71.81 liquidity=2854494.5 spike=0.13
- SCEM.CA: score=21.4 buy_ready=False sector_rank=4 price=95.06 support=76.75 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=65.94 liquidity=33643032.0 spike=0.16
- SCFM.CA: score=15.8 buy_ready=False sector_rank=13 price=286.51 support=272.0 resistance=319.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=56.42 liquidity=5186720.0 spike=0.24
- SCTS.CA: score=10.24 buy_ready=False sector_rank=15 price=623.0 support=603.13 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=79.83 liquidity=893992.38 spike=0.1
- SDTI.CA: score=16.84 buy_ready=False sector_rank=13 price=69.35 support=52.36 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=61.38 liquidity=6227219.5 spike=0.2
- SEIG.CA: score=9.63 buy_ready=False sector_rank=13 price=264.71 support=242.1 resistance=295.0 source=Yahoo Finance as_of=2026-08-23T21:00:00+00:00 freshness=FRESH RSI=50.58 liquidity=1013839.27 spike=0.12
- SIPC.CA: score=12.47 buy_ready=False sector_rank=13 price=4.85 support=3.82 resistance=5.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=54.76 liquidity=1854441.0 spike=0.03
- SKPC.CA: score=17.03 buy_ready=False sector_rank=9 price=17.17 support=15.61 resistance=18.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=79.36 liquidity=23560642.0 spike=0.33
- SMFR.CA: score=11.58 buy_ready=False sector_rank=13 price=261.65 support=228.88 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=72.82 liquidity=2966545.5 spike=0.11
- SNFC.CA: score=9.36 buy_ready=False sector_rank=13 price=10.39 support=10.3 resistance=11.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=45.1 liquidity=2745871.5 spike=0.21
- SPIN.CA: score=22.4 buy_ready=False sector_rank=3 price=19.72 support=15.3 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=70.84 liquidity=11665618.0 spike=0.25
- SPMD.CA: score=9.98 buy_ready=False sector_rank=13 price=0.46 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=35.19 liquidity=1370421.75 spike=0.05
- SUGR.CA: score=18.87 buy_ready=False sector_rank=16 price=57.74 support=46.47 resistance=61.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=87.62 liquidity=17495590.0 spike=0.37
- SVCE.CA: score=17.97 buy_ready=False sector_rank=13 price=10.77 support=9.06 resistance=12.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=70.6 liquidity=7360763.5 spike=0.07
- SWDY.CA: score=21.24 buy_ready=False sector_rank=8 price=127.9 support=91.8 resistance=133.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=66.62 liquidity=10526323.0 spike=0.11
- TALM.CA: score=5.02 buy_ready=False sector_rank=15 price=18.15 support=18.0 resistance=18.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9672903.0 spike=0.22
- TMGH.CA: score=15.62 buy_ready=False sector_rank=12 price=98.25 support=95.2 resistance=100.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=33.62 liquidity=49660096.0 spike=0.19
- TRTO.CA: score=14.62 buy_ready=False sector_rank=13 price=0.05 support=0.03 resistance=0.05 source=Yahoo Finance as_of=2026-08-23T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=4720.71 spike=0.42
- UEFM.CA: score=9.5 buy_ready=False sector_rank=13 price=541.56 support=531.0 resistance=594.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=887171.5 spike=0.19
- UEGC.CA: score=14.71 buy_ready=False sector_rank=13 price=2.05 support=1.95 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=24.14 liquidity=56200096.0 spike=1.55
- UNIP.CA: score=12.07 buy_ready=False sector_rank=13 price=0.37 support=0.35 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=3455998.25 spike=0.1
- UNIT.CA: score=16.5 buy_ready=False sector_rank=12 price=19.2 support=17.32 resistance=23.0 source=Yahoo Finance as_of=2026-08-23T21:00:00+00:00 freshness=FRESH RSI=55.06 liquidity=5874912.23 spike=0.51
- WCDF.CA: score=8.19 buy_ready=False sector_rank=13 price=639.38 support=571.0 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=76.03 liquidity=577977.13 spike=0.13
- WKOL.CA: score=13.79 buy_ready=False sector_rank=13 price=347.13 support=310.0 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=58.78 liquidity=1180222.63 spike=0.03
- ZEOT.CA: score=14.34 buy_ready=False sector_rank=13 price=13.79 support=11.7 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=55.18 liquidity=1730971.75 spike=0.07
- ZMID.CA: score=20.62 buy_ready=False sector_rank=12 price=8.1 support=7.06 resistance=8.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=71.79 liquidity=72536336.0 spike=0.3

## Backtesting Lite
- CCRS.CA: 180d return=108.57%, max drawdown=-34.85%, MA20>MA50 days last20=20, as_of=2026-08-23T21:00:00+00:00
- FAIT.CA: 180d return=38.24%, max drawdown=-8.36%, MA20>MA50 days last20=17, as_of=2026-08-23T21:00:00+00:00
- KABO.CA: 180d return=34.53%, max drawdown=-23.4%, MA20>MA50 days last20=20, as_of=2026-08-23T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CCRS.CA: status=OLD_ACCEPTED latest=2016-01-01 age_days=3890 sources=3 expected=Gulf Canadian Company for Arab Real Estate Investment summary=10 EGX-listed firms deny ties to UAE-based Abraaj; Gulf Canadian OGM to discuss 2016 financials Thursday; Gulf Canadian OGM to discuss 2016 results 22 March
  - 10 EGX-listed firms deny ties to UAE-based Abraaj: https://english.mubasher.info/news/3308086/10-EGX-listed-firms-deny-ties-to-UAE-based-Abraaj/
  - Gulf Canadian OGM to discuss 2016 financials Thursday: https://english.mubasher.info/news/3076282/Gulf-Canadian-OGM-to-discuss-2016-financials-Thursday/
  - Gulf Canadian OGM to discuss 2016 results 22 March: https://english.mubasher.info/news/3067564/Gulf-Canadian-OGM-to-discuss-2016-results-22-March/
- FAIT.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=602 sources=3 expected=Faisal Islamic Bank of Egypt summary=Faisal Islamic Bank of Egypt unveils dividends for 2025; Faisal Islamic Bank of Egypt’s consolidated net profits drop to EGP 4.6bn in 2025; Faisal Islamic Bank of Egypt posts 63% lower standalone net profits in 2025
  - Faisal Islamic Bank of Egypt unveils dividends for 2025: https://english.mubasher.info/news/4585552/Faisal-Islamic-Bank-of-Egypt-unveils-dividends-for-2025/
  - Faisal Islamic Bank of Egypt’s consolidated net profits drop to EGP 4.6bn in 2025: https://english.mubasher.info/news/4582812/Faisal-Islamic-Bank-of-Egypt-s-consolidated-net-profits-drop-to-EGP-4-6bn-in-2025/
  - Faisal Islamic Bank of Egypt posts 63% lower standalone net profits in 2025: https://english.mubasher.info/news/4548875/Faisal-Islamic-Bank-of-Egypt-posts-63-lower-standalone-net-profits-in-2025/
- KABO.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Nasr Clothing and Textiles summary=KABO posts EGP 17m in Q1-25/26 unaudited consolidated net profits; KABO sells over 1.9m shares in Spinalex for EGP 20m; KABO unveils international agreements, expansion plan including export lines
  - KABO posts EGP 17m in Q1-25/26 unaudited consolidated net profits: https://english.mubasher.info/news/4600162/KABO-posts-EGP-17m-in-Q1-25-26-unaudited-consolidated-net-profits/
  - KABO sells over 1.9m shares in Spinalex for EGP 20m: https://english.mubasher.info/news/4543747/KABO-sells-over-1-9m-shares-in-Spinalex-for-EGP-20m/
  - KABO unveils international agreements, expansion plan including export lines: https://english.mubasher.info/news/4533185/KABO-unveils-international-agreements-expansion-plan-including-export-lines/
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=602 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- OIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Investment Holding summary=Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- EMFD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=602 sources=3 expected=Emaar Misr for Development summary=Emaar Misr posts higher revenues at EGP 19.8bn in 2025; Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25; Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea
  - Emaar Misr posts higher revenues at EGP 19.8bn in 2025: https://english.mubasher.info/news/4561643/Emaar-Misr-posts-higher-revenues-at-EGP-19-8bn-in-2025/
  - Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25: https://english.mubasher.info/news/4525192/Emaar-Misr-s-consolidated-net-profits-drop-to-EGP-4-2bn-in-9M-25/
  - Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea: https://english.mubasher.info/news/4495287/Emaar-Misr-Golden-Coast-to-establish-EGP-900bn-project-in-Red-Sea/

## Warnings
- Evidence for CCRS.CA matches the company but appears old; latest detected date is 2016-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for FAIT.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for KABO.CA matches the company but no source/report date was detected.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for EMFD.CA matches the company but appears old; latest detected date is 2025-01-01.
