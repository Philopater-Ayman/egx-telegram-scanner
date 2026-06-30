# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-06-30T10:57:28.165678+00:00
Generated Cairo: 2026-06-30 13:57
Run timing: target 11:00 Cairo | generated Cairo 2026-06-30 13:57 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-06-30 13:52

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 182/190
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, June 30
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 15.0% / above MA50 20.0%
- EGX70 regime: BEARISH / above MA20 45.0% / above MA50 62.5%
- Sector breadth: 9.52%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=266419216.0 spike=0.45 score=14.46
- TMGH.CA: liquidity=264403040.0 spike=0.71 score=14.47
- CCAP.CA: liquidity=194324480.0 spike=0.29 score=8.87
- RAYA.CA: liquidity=173754864.0 spike=2.07 score=24.54
- PHDC.CA: liquidity=154491152.0 spike=0.38 score=17.47

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b-20230311:free
- Summary: Scanner highlighted CSAG.CA, MHOT.CA, RAYA.CA and similar tickets due to strong accumulation spikes and bullish‑watch outlook, but the EGX30/EGX70 bearish regime and narrow sector breadth keep the risk mode defensive, so no new buys are advised.
- Liquidity regimes show accumulation spikes (e.g., RAYA.CA liquidity_spike 2.07, CSAG.CA 1.65), signaling short‑term buying interest despite overall bearish breadth.
- Tickets sit in leading sectors (Tourism & Leisure, Technology & Distribution, Transportation & Logistics) where sector scores are relatively higher, giving them a relative edge.
- Support/resistance distances are modest (CSAG.CA 3.3 % to resistance, MHOT.CA 17 % to support) and RSI values hover near neutral‑to‑overbought, limiting near‑term upside potential.
- EGX30 and EGX70 are both BEARISH with low above‑MA20/MA50 percentages and negative median returns, shifting risk mode to DEFENSIVE_NO_NEW_BUY; thus the scanner maintains HOLD positions, acknowledging uncertainty if the r

## Top Liquidity Spikes
- AMES.CA: spike=33.76 liquidity=144590352.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DTPP.CA: spike=16.02 liquidity=32225548.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- NHPS.CA: spike=6.1 liquidity=21228308.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SCTS.CA: spike=5.59 liquidity=17398578.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MOIN.CA: spike=5.37 liquidity=4390051.0 outlook=WEAK_OR_RISKY score=24.26 buy_ready=False

## Sector Leaderboard
- #1 Tourism & Leisure: score=8.91 5d=4.84% 20d=1.71% aboveMA50=100.0%
- #2 Automotive & Distribution: score=8.03 5d=2.47% 20d=7.28% aboveMA50=100.0%
- #3 Technology & Distribution: score=7.87 5d=-1.75% 20d=-2.67% aboveMA50=100.0%
- #4 Transportation & Logistics: score=4.41 5d=-0.26% 20d=-2.71% aboveMA50=50.0%
- #5 Food, Beverages & Tobacco: score=2.3 5d=-3.15% 20d=-0.4% aboveMA50=57.14%
- #6 Healthcare: score=2.02 5d=-4.29% 20d=-1.1% aboveMA50=83.33%
- #7 Education: score=1.53 5d=-3.06% 20d=0.0% aboveMA50=33.33%
- #8 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CSAG.CA: BULLISH_WATCH score=99.41 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- RAYA.CA: BULLISH_WATCH score=98.87 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- CAED.CA: BULLISH_WATCH score=89.26 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- GIHD.CA: BULLISH_WATCH score=83.26 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- FAIT.CA: BULLISH_WATCH score=83.16 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- MHOT.CA: BULLISH_WATCH score=80.91 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- ETRS.CA: BULLISH_WATCH score=79.26 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- POUL.CA: BULLISH_WATCH score=78.3 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- OLFI.CA: BULLISH_WATCH score=77.3 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- MASR.CA: BULLISH_WATCH score=77.26 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=2.42 buy_ready=False sector_rank=9 price=202.08 support=196.0 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=29.49 liquidity=2913540.0 spike=0.47
- ABUK.CA: score=8.17 buy_ready=False sector_rank=20 price=67.7 support=66.66 resistance=84.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=9.05 liquidity=44231452.0 spike=0.32
- ACAMD.CA: score=12.5 buy_ready=False sector_rank=9 price=2.2 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=34.78 liquidity=52606692.0 spike=0.43
- ACGC.CA: score=9.02 buy_ready=False sector_rank=16 price=9.16 support=8.92 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=32.99 liquidity=11656536.0 spike=0.31
- ADCI.CA: score=15.59 buy_ready=False sector_rank=9 price=241.23 support=211.0 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=84.3 liquidity=7088810.5 spike=0.69
- ADIB.CA: score=14.46 buy_ready=False sector_rank=11 price=45.95 support=44.01 resistance=48.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=38587416.0 spike=0.42
- ADPC.CA: score=8.73 buy_ready=False sector_rank=9 price=3.42 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=35.4 liquidity=5221732.0 spike=0.25
- AFDI.CA: score=19.96 buy_ready=False sector_rank=9 price=43.93 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=45.35 liquidity=18160934.0 spike=1.23
- AFMC.CA: score=1.29 buy_ready=False sector_rank=9 price=68.62 support=66.0 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=28.48 liquidity=1783095.88 spike=0.78
- AJWA.CA: score=16.92 buy_ready=False sector_rank=9 price=177.0 support=132.0 resistance=188.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=74.49 liquidity=7418477.0 spike=0.27
- ALCN.CA: score=10.94 buy_ready=False sector_rank=4 price=28.4 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=32.53 liquidity=13289921.0 spike=1.09
- ALUM.CA: score=3.71 buy_ready=False sector_rank=9 price=21.15 support=20.55 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=11.73 liquidity=4202802.5 spike=0.44
- AMER.CA: score=9.47 buy_ready=False sector_rank=10 price=2.41 support=2.28 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=19.28 liquidity=67641216.0 spike=0.95
- AMES.CA: score=9.5 buy_ready=False sector_rank=9 price=66.32 support=57.23 resistance=66.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=144590352.0 spike=33.76
- AMIA.CA: score=3.28 buy_ready=False sector_rank=9 price=8.51 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=28.97 liquidity=3778393.0 spike=0.28
- AMOC.CA: score=9.04 buy_ready=False sector_rank=15 price=7.6 support=7.42 resistance=8.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=17.54 liquidity=24640216.0 spike=0.51
- ANFI.CA: score=5.84 buy_ready=False sector_rank=9 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=STALE RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=-0.65 buy_ready=False sector_rank=9 price=8.29 support=8.0 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=7.62 liquidity=849507.19 spike=0.96
- ARAB.CA: score=14.47 buy_ready=False sector_rank=10 price=0.21 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=55.88 liquidity=20406320.0 spike=0.24
- ARCC.CA: score=9.25 buy_ready=False sector_rank=14 price=54.8 support=53.0 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=27.87 liquidity=26738356.0 spike=0.78
- AREH.CA: score=19.5 buy_ready=False sector_rank=9 price=1.55 support=1.34 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=21042950.0 spike=0.61
- ARVA.CA: score=15.24 buy_ready=False sector_rank=9 price=10.85 support=9.43 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=46.86 liquidity=7738270.0 spike=0.24
- ASCM.CA: score=19.5 buy_ready=False sector_rank=9 price=59.02 support=47.7 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=54.53 liquidity=33948688.0 spike=0.36
- ASPI.CA: score=12.5 buy_ready=False sector_rank=9 price=0.31 support=0.27 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=29.06 liquidity=10864084.0 spike=0.15
- ATLC.CA: score=10.28 buy_ready=False sector_rank=12 price=5.1 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=48.0 liquidity=996198.19 spike=0.16
- ATQA.CA: score=12.17 buy_ready=False sector_rank=20 price=9.45 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=36.19 liquidity=15523226.0 spike=0.47
- AXPH.CA: score=9.97 buy_ready=False sector_rank=9 price=1117.91 support=1073.0 resistance=1174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=42.94 liquidity=462932.81 spike=0.31
- BINV.CA: score=8.97 buy_ready=False sector_rank=17 price=46.0 support=44.02 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=39.7 liquidity=2106628.25 spike=0.21
- BIOC.CA: score=4.94 buy_ready=False sector_rank=9 price=68.78 support=66.75 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=35.71 liquidity=438796.41 spike=0.17
- BTFH.CA: score=13.29 buy_ready=False sector_rank=12 price=2.99 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=37.7 liquidity=121626016.0 spike=0.67
- CAED.CA: score=24.12 buy_ready=False sector_rank=9 price=72.07 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=44.96 liquidity=13754026.0 spike=3.31
- CANA.CA: score=19.24 buy_ready=False sector_rank=11 price=35.51 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=37.78 liquidity=25758176.0 spike=2.39
- CCAP.CA: score=8.87 buy_ready=False sector_rank=17 price=4.79 support=4.65 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=18.55 liquidity=194324480.0 spike=0.29
- CCRS.CA: score=3.96 buy_ready=False sector_rank=9 price=2.2 support=2.22 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=4459204.0 spike=0.26
- CEFM.CA: score=1.01 buy_ready=False sector_rank=9 price=100.19 support=95.75 resistance=109.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=20.18 liquidity=1508167.13 spike=0.84
- CERA.CA: score=11.29 buy_ready=False sector_rank=9 price=1.21 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=4785685.0 spike=0.29
- CFGH.CA: score=-1.49 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=4880.0 spike=0.79
- CICH.CA: score=6.74 buy_ready=False sector_rank=12 price=11.89 support=11.1 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=48.77 liquidity=449338.34 spike=0.14
- CIEB.CA: score=6.25 buy_ready=False sector_rank=11 price=23.56 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=51.06 liquidity=1787036.25 spike=0.27
- CIRA.CA: score=18.19 buy_ready=False sector_rank=7 price=28.51 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=61.39 liquidity=8582345.0 spike=0.5
- CLHO.CA: score=19.81 buy_ready=False sector_rank=6 price=16.24 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=66.94 liquidity=17584200.0 spike=0.48
- CNFN.CA: score=21.29 buy_ready=False sector_rank=12 price=4.72 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=53.55 liquidity=14361112.0 spike=0.35
- COMI.CA: score=14.46 buy_ready=False sector_rank=11 price=128.96 support=126.21 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=35.45 liquidity=266419216.0 spike=0.45
- COPR.CA: score=14.77 buy_ready=False sector_rank=9 price=0.35 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=43.55 liquidity=8265021.0 spike=0.3
- COSG.CA: score=9.5 buy_ready=False sector_rank=9 price=1.51 support=1.47 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=27.78 liquidity=12525249.0 spike=0.23
- CPCI.CA: score=18.78 buy_ready=False sector_rank=9 price=395.96 support=350.04 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=71.98 liquidity=5031431.5 spike=2.12
- CSAG.CA: score=26.06 buy_ready=False sector_rank=4 price=32.76 support=30.08 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=61.3 liquidity=27416168.0 spike=1.65
- DAPH.CA: score=11.65 buy_ready=False sector_rank=9 price=80.5 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=48.28 liquidity=3145882.25 spike=0.31
- DEIN.CA: score=5.5 buy_ready=False sector_rank=9 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=11.62 buy_ready=False sector_rank=5 price=26.88 support=23.7 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=70.34 liquidity=1699810.0 spike=0.43
- DSCW.CA: score=13.5 buy_ready=False sector_rank=9 price=1.74 support=1.71 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=36.11 liquidity=13648496.0 spike=0.39
- DTPP.CA: score=9.5 buy_ready=False sector_rank=9 price=166.05 support=153.55 resistance=166.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32225548.0 spike=16.02
- EALR.CA: score=0.38 buy_ready=False sector_rank=9 price=340.9 support=332.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=25.74 liquidity=875703.88 spike=0.28
- EASB.CA: score=12.94 buy_ready=False sector_rank=9 price=7.5 support=4.66 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=75.15 liquidity=6440017.5 spike=0.5
- EAST.CA: score=8.92 buy_ready=False sector_rank=5 price=36.89 support=36.86 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=31.93 liquidity=12206471.0 spike=0.32
- EBSC.CA: score=4.93 buy_ready=False sector_rank=9 price=1.75 support=1.69 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=421594.09 spike=0.16
- ECAP.CA: score=11.85 buy_ready=False sector_rank=9 price=32.17 support=29.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=54.65 liquidity=2347328.75 spike=0.26
- EDFM.CA: score=-0.24 buy_ready=False sector_rank=9 price=330.59 support=320.29 resistance=355.0 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=30.71 liquidity=253893.12 spike=0.52
- EEII.CA: score=19.3 buy_ready=False sector_rank=9 price=2.45 support=2.3 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=9798864.0 spike=0.74
- EFIC.CA: score=-0.91 buy_ready=False sector_rank=20 price=186.8 support=189.01 resistance=212.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=6.38 liquidity=1918840.5 spike=0.98
- EFID.CA: score=14.92 buy_ready=False sector_rank=5 price=27.2 support=25.5 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=41.64 liquidity=58694796.0 spike=0.77
- EFIH.CA: score=12.85 buy_ready=False sector_rank=21 price=20.29 support=20.0 resistance=22.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=36.37 liquidity=10908378.0 spike=0.25
- EGAL.CA: score=8.17 buy_ready=False sector_rank=20 price=284.45 support=272.28 resistance=334.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=10.71 liquidity=30565830.0 spike=0.48
- EGAS.CA: score=9.39 buy_ready=False sector_rank=15 price=49.31 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=44.48 liquidity=2357156.25 spike=0.25
- EGBE.CA: score=9.51 buy_ready=False sector_rank=11 price=0.46 support=0.43 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=45592.28 spike=0.53
- EGCH.CA: score=8.17 buy_ready=False sector_rank=20 price=12.25 support=12.13 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=19.35 liquidity=20926680.0 spike=0.4
- EGSA.CA: score=7.27 buy_ready=False sector_rank=13 price=8.75 support=8.55 resistance=9.1 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=42.86 liquidity=5801.25 spike=0.62
- EGTS.CA: score=12.47 buy_ready=False sector_rank=10 price=17.25 support=15.1 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=29.08 liquidity=20551970.0 spike=0.23
- EHDR.CA: score=12.5 buy_ready=False sector_rank=9 price=2.47 support=2.32 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=26.74 liquidity=18372870.0 spike=0.32
- EKHO.CA: score=6.04 buy_ready=False sector_rank=15 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=7.58 buy_ready=False sector_rank=19 price=2.08 support=2.05 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=32.14 liquidity=15574849.0 spike=0.82
- ELKA.CA: score=6.04 buy_ready=False sector_rank=9 price=1.33 support=1.21 resistance=1.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=71439832.0 spike=1.77
- ELNA.CA: score=-0.87 buy_ready=False sector_rank=9 price=37.81 support=35.55 resistance=41.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=33.43 liquidity=481836.25 spike=1.07
- ELSH.CA: score=17.5 buy_ready=False sector_rank=9 price=11.74 support=9.33 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=38.89 liquidity=54130280.0 spike=0.28
- ELWA.CA: score=3.43 buy_ready=False sector_rank=9 price=1.99 support=1.95 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=31.91 liquidity=929304.88 spike=0.3
- EMFD.CA: score=17.47 buy_ready=False sector_rank=10 price=11.52 support=11.11 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=41.0 liquidity=54876864.0 spike=0.19
- ENGC.CA: score=17.17 buy_ready=False sector_rank=9 price=36.56 support=33.0 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=56.36 liquidity=5662886.5 spike=0.39
- EOSB.CA: score=11.54 buy_ready=False sector_rank=9 price=1.48 support=1.39 resistance=1.55 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=36743.96 spike=0.28
- EPCO.CA: score=1.47 buy_ready=False sector_rank=9 price=8.64 support=8.5 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=28.31 liquidity=1964197.75 spike=0.23
- EPPK.CA: score=18.24 buy_ready=False sector_rank=9 price=13.67 support=11.67 resistance=13.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=70.53 liquidity=3836554.25 spike=3.45
- ETEL.CA: score=14.26 buy_ready=False sector_rank=13 price=93.01 support=89.01 resistance=97.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=35.42 liquidity=56692320.0 spike=0.81
- ETRS.CA: score=23.44 buy_ready=False sector_rank=9 price=10.82 support=8.5 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=145608880.0 spike=1.97
- EXPA.CA: score=6.01 buy_ready=False sector_rank=11 price=18.21 support=18.03 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=27.33 liquidity=6550052.5 spike=0.2
- FAIT.CA: score=21.02 buy_ready=False sector_rank=11 price=36.97 support=35.01 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=43.7 liquidity=7978925.0 spike=2.79
- FAITA.CA: score=4.48 buy_ready=False sector_rank=11 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=38.71 liquidity=13054.19 spike=0.32
- FERC.CA: score=0.75 buy_ready=False sector_rank=20 price=73.62 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=12.94 liquidity=3573721.5 spike=0.94
- FWRY.CA: score=12.85 buy_ready=False sector_rank=21 price=18.45 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=42.96 liquidity=119006696.0 spike=0.49
- GBCO.CA: score=20.4 buy_ready=False sector_rank=2 price=31.91 support=25.25 resistance=32.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=83.43 liquidity=74486632.0 spike=0.82
- GDWA.CA: score=8.5 buy_ready=False sector_rank=9 price=0.77 support=0.76 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=13134605.0 spike=0.94
- GGCC.CA: score=22.12 buy_ready=False sector_rank=9 price=0.48 support=0.4 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=67.68 liquidity=20655844.0 spike=1.81
- GIHD.CA: score=20.72 buy_ready=False sector_rank=9 price=41.93 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=46.44 liquidity=13224858.0 spike=1.61
- GMCI.CA: score=16.31 buy_ready=False sector_rank=9 price=1.81 support=1.66 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=1801102.75 spike=4.49
- GRCA.CA: score=5.45 buy_ready=False sector_rank=9 price=51.92 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=42.98 liquidity=948431.44 spike=0.21
- GSSC.CA: score=1.19 buy_ready=False sector_rank=9 price=244.44 support=228.1 resistance=257.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=23.83 liquidity=1682913.0 spike=0.57
- GTWL.CA: score=9.5 buy_ready=False sector_rank=9 price=88.2 support=76.25 resistance=88.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=126920728.0 spike=5.08
- HDBK.CA: score=19.92 buy_ready=False sector_rank=11 price=158.6 support=138.0 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=66.54 liquidity=34958916.0 spike=1.23
- HELI.CA: score=17.47 buy_ready=False sector_rank=10 price=6.45 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=36597744.0 spike=0.32
- HRHO.CA: score=13.29 buy_ready=False sector_rank=12 price=26.6 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=41928472.0 spike=0.31
- ICID.CA: score=21.13 buy_ready=False sector_rank=9 price=7.86 support=5.24 resistance=8.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=61.75 liquidity=9624073.0 spike=0.58
- IDRE.CA: score=6.54 buy_ready=False sector_rank=9 price=42.11 support=41.1 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=33.22 liquidity=4037745.25 spike=0.3
- IFAP.CA: score=3.79 buy_ready=False sector_rank=18 price=19.07 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=40.08 liquidity=964499.44 spike=0.14
- INFI.CA: score=0.29 buy_ready=False sector_rank=9 price=90.16 support=88.51 resistance=105.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=9.75 liquidity=1787326.5 spike=0.29
- IRON.CA: score=11.67 buy_ready=False sector_rank=20 price=32.87 support=30.51 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=48.72 liquidity=7494209.0 spike=0.97
- ISMA.CA: score=12.5 buy_ready=False sector_rank=9 price=28.04 support=25.99 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=33.55 liquidity=11217276.0 spike=0.31
- ISMQ.CA: score=20.17 buy_ready=False sector_rank=20 price=9.18 support=7.56 resistance=9.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=68.24 liquidity=87302512.0 spike=0.76
- ISPH.CA: score=14.81 buy_ready=False sector_rank=6 price=11.58 support=11.2 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=36.75 liquidity=31617806.0 spike=0.28
- JUFO.CA: score=17.61 buy_ready=False sector_rank=5 price=29.71 support=28.5 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=39.34 liquidity=9688698.0 spike=0.31
- KABO.CA: score=17.02 buy_ready=False sector_rank=16 price=6.25 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=42.25 liquidity=10244950.0 spike=0.64
- KWIN.CA: score=10.71 buy_ready=False sector_rank=9 price=67.4 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=7204444.5 spike=0.62
- KZPC.CA: score=1.52 buy_ready=False sector_rank=9 price=8.38 support=8.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=12.29 liquidity=3016174.75 spike=0.48
- LCSW.CA: score=21.27 buy_ready=False sector_rank=14 price=27.5 support=26.0 resistance=31.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=53.11 liquidity=29226738.0 spike=1.01
- LUTS.CA: score=19.5 buy_ready=False sector_rank=9 price=0.75 support=0.56 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=64.74 liquidity=29840422.0 spike=0.65
- MAAL.CA: score=16.79 buy_ready=False sector_rank=9 price=7.11 support=5.25 resistance=7.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=77.89 liquidity=8285136.5 spike=0.46
- MASR.CA: score=21.9 buy_ready=False sector_rank=9 price=7.35 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=55.61 liquidity=125953976.0 spike=2.2
- MBSC.CA: score=9.25 buy_ready=False sector_rank=14 price=237.38 support=222.66 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=14.67 liquidity=16408484.0 spike=0.49
- MCQE.CA: score=9.25 buy_ready=False sector_rank=14 price=170.21 support=166.66 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=24.62 liquidity=10778413.0 spike=0.76
- MCRO.CA: score=8.5 buy_ready=False sector_rank=9 price=1.2 support=1.17 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=25617382.0 spike=0.74
- MENA.CA: score=11.66 buy_ready=False sector_rank=10 price=6.88 support=6.32 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=52.69 liquidity=2185840.25 spike=0.17
- MEPA.CA: score=3.45 buy_ready=False sector_rank=9 price=1.57 support=1.52 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=17.24 liquidity=4941511.0 spike=0.44
- MFPC.CA: score=8.17 buy_ready=False sector_rank=20 price=35.16 support=34.22 resistance=43.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=9.0 liquidity=34201476.0 spike=0.4
- MFSC.CA: score=9.9 buy_ready=False sector_rank=9 price=46.85 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=51.33 liquidity=2397881.75 spike=0.28
- MHOT.CA: score=25.03 buy_ready=False sector_rank=1 price=33.75 support=28.83 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=63.86 liquidity=8633690.0 spike=0.42
- MICH.CA: score=13.9 buy_ready=False sector_rank=9 price=37.64 support=34.0 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=45.35 liquidity=4396191.5 spike=0.29
- MILS.CA: score=3.77 buy_ready=False sector_rank=9 price=128.22 support=126.5 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=29.31 liquidity=4265494.5 spike=0.45
- MIPH.CA: score=8.16 buy_ready=False sector_rank=6 price=656.66 support=630.13 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=46.04 liquidity=356659.31 spike=0.18
- MOED.CA: score=2.74 buy_ready=False sector_rank=9 price=0.67 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=34.35 liquidity=4239944.0 spike=0.46
- MOIL.CA: score=7.09 buy_ready=False sector_rank=15 price=0.47 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=36.21 liquidity=54900.28 spike=0.28
- MOIN.CA: score=7.89 buy_ready=False sector_rank=9 price=24.0 support=22.6 resistance=25.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=4390051.0 spike=5.37
- MOSC.CA: score=12.46 buy_ready=False sector_rank=9 price=275.15 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=56.3 liquidity=2951622.75 spike=0.31
- MPCI.CA: score=19.56 buy_ready=False sector_rank=9 price=238.79 support=204.36 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=54.8 liquidity=98099464.0 spike=1.03
- MPCO.CA: score=16.82 buy_ready=False sector_rank=18 price=1.79 support=1.6 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=44.78 liquidity=42730252.0 spike=0.4
- MPRC.CA: score=16.5 buy_ready=False sector_rank=9 price=38.31 support=31.15 resistance=40.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=77.97 liquidity=13565205.0 spike=0.31
- MTIE.CA: score=21.4 buy_ready=False sector_rank=2 price=8.97 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=42.65 liquidity=10289548.0 spike=0.63
- NAHO.CA: score=5.52 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=15906.69 spike=0.44
- NCCW.CA: score=10.66 buy_ready=False sector_rank=9 price=6.12 support=5.29 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=28.48 liquidity=8157745.5 spike=0.25
- NEDA.CA: score=-0.4 buy_ready=False sector_rank=9 price=2.74 support=2.68 resistance=2.84 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=33.33 liquidity=92390.06 spike=0.25
- NHPS.CA: score=9.5 buy_ready=False sector_rank=9 price=66.8 support=62.1 resistance=71.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21228308.0 spike=6.1
- NINH.CA: score=23.5 buy_ready=False sector_rank=9 price=17.84 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=50.18 liquidity=21274102.0 spike=5.08
- NIPH.CA: score=17.81 buy_ready=False sector_rank=6 price=162.69 support=157.01 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=42.84 liquidity=21733628.0 spike=0.32
- OBRI.CA: score=9.82 buy_ready=False sector_rank=9 price=32.8 support=31.5 resistance=37.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=30.98 liquidity=16398500.0 spike=1.16
- OCDI.CA: score=19.47 buy_ready=False sector_rank=10 price=24.59 support=20.0 resistance=25.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=66.71 liquidity=21066672.0 spike=0.27
- OCPH.CA: score=13.93 buy_ready=False sector_rank=9 price=354.57 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=41.47 liquidity=4425316.5 spike=0.71
- ODIN.CA: score=14.21 buy_ready=False sector_rank=9 price=2.12 support=1.94 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=38.3 liquidity=6702990.5 spike=0.61
- OFH.CA: score=7.6 buy_ready=False sector_rank=9 price=0.59 support=0.57 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=22.09 liquidity=9093427.0 spike=0.48
- OIH.CA: score=17.87 buy_ready=False sector_rank=17 price=1.41 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=25337892.0 spike=0.33
- OLFI.CA: score=20.14 buy_ready=False sector_rank=5 price=22.23 support=21.0 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=53.18 liquidity=22913634.0 spike=1.11
- ORAS.CA: score=4.6 buy_ready=False sector_rank=8 price=719.9 support=704.52 resistance=728.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=144195216.0 spike=1.0
- ORHD.CA: score=17.47 buy_ready=False sector_rank=10 price=37.78 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=53.68 liquidity=108656784.0 spike=0.64
- ORWE.CA: score=7.72 buy_ready=False sector_rank=16 price=22.39 support=21.95 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=19.64 liquidity=8699580.0 spike=0.24
- PHAR.CA: score=20.69 buy_ready=False sector_rank=6 price=87.8 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=43.72 liquidity=48902196.0 spike=1.44
- PHDC.CA: score=17.47 buy_ready=False sector_rank=10 price=14.64 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=44.1 liquidity=154491152.0 spike=0.38
- PHTV.CA: score=10.38 buy_ready=False sector_rank=9 price=270.4 support=201.55 resistance=275.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=90.82 liquidity=1871981.75 spike=0.13
- POUL.CA: score=18.85 buy_ready=False sector_rank=5 price=37.46 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=52.46 liquidity=6930933.5 spike=0.19
- PRCL.CA: score=19.25 buy_ready=False sector_rank=14 price=30.87 support=22.86 resistance=32.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=68.92 liquidity=39933552.0 spike=0.99
- PRDC.CA: score=17.47 buy_ready=False sector_rank=10 price=7.34 support=5.86 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=65.55 liquidity=52845188.0 spike=0.45
- PRMH.CA: score=15.11 buy_ready=False sector_rank=9 price=2.48 support=2.28 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=38.26 liquidity=7602692.0 spike=0.24
- RACC.CA: score=7.46 buy_ready=False sector_rank=9 price=9.63 support=9.36 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=36.84 liquidity=2958305.75 spike=0.32
- RAKT.CA: score=0.07 buy_ready=False sector_rank=9 price=21.68 support=21.96 resistance=24.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=30.46 liquidity=444380.06 spike=1.56
- RAYA.CA: score=24.54 buy_ready=False sector_rank=3 price=7.58 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=46.49 liquidity=173754864.0 spike=2.07
- RMDA.CA: score=11.17 buy_ready=False sector_rank=6 price=4.93 support=4.81 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=30.3 liquidity=8366639.5 spike=0.11
- ROTO.CA: score=19.5 buy_ready=False sector_rank=9 price=41.8 support=33.0 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=66.01 liquidity=22350584.0 spike=0.77
- RREI.CA: score=10.56 buy_ready=False sector_rank=9 price=3.48 support=3.34 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=41.1 liquidity=6051810.5 spike=0.36
- RTVC.CA: score=4.92 buy_ready=False sector_rank=9 price=3.79 support=3.55 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=21.43 liquidity=5340553.0 spike=1.04
- RUBX.CA: score=21.8 buy_ready=False sector_rank=9 price=11.16 support=9.8 resistance=12.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=61.35 liquidity=20657956.0 spike=1.15
- SAUD.CA: score=3.46 buy_ready=False sector_rank=11 price=20.76 support=19.99 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=27.42 liquidity=3996244.0 spike=0.47
- SCEM.CA: score=14.87 buy_ready=False sector_rank=14 price=62.61 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=38.22 liquidity=22910402.0 spike=1.31
- SCFM.CA: score=1.39 buy_ready=False sector_rank=9 price=240.27 support=226.5 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=27.28 liquidity=1882557.5 spike=0.42
- SCTS.CA: score=9.61 buy_ready=False sector_rank=7 price=624.21 support=543.01 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17398578.0 spike=5.59
- SDTI.CA: score=9.87 buy_ready=False sector_rank=9 price=45.88 support=44.17 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=38.33 liquidity=2370774.0 spike=0.2
- SEIG.CA: score=10.6 buy_ready=False sector_rank=9 price=187.83 support=180.0 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=36.97 liquidity=1091548.0 spike=0.26
- SIPC.CA: score=4.48 buy_ready=False sector_rank=9 price=3.32 support=3.25 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=23.88 liquidity=4973831.5 spike=0.43
- SKPC.CA: score=5.93 buy_ready=False sector_rank=20 price=15.95 support=15.58 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=24.44 liquidity=8757149.0 spike=0.25
- SMFR.CA: score=-0.12 buy_ready=False sector_rank=9 price=192.99 support=187.01 resistance=214.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=27.39 liquidity=377298.5 spike=0.18
- SNFC.CA: score=8.63 buy_ready=False sector_rank=9 price=11.96 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=46.46 liquidity=4123082.25 spike=0.24
- SPIN.CA: score=9.71 buy_ready=False sector_rank=16 price=14.17 support=13.3 resistance=14.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=53.9 liquidity=1681757.75 spike=0.28
- SPMD.CA: score=14.2 buy_ready=False sector_rank=9 price=0.42 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=6697525.0 spike=0.28
- SUGR.CA: score=4.7 buy_ready=False sector_rank=5 price=46.43 support=45.31 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=15.05 liquidity=5775277.0 spike=0.78
- SVCE.CA: score=15.61 buy_ready=False sector_rank=9 price=8.97 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=53.31 liquidity=8109820.5 spike=0.13
- SWDY.CA: score=12.16 buy_ready=False sector_rank=19 price=85.9 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=38.97 liquidity=8571809.0 spike=0.5
- TALM.CA: score=1.8 buy_ready=False sector_rank=7 price=15.63 support=15.38 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=28.89 liquidity=2189594.5 spike=0.3
- TMGH.CA: score=14.47 buy_ready=False sector_rank=10 price=94.26 support=92.1 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=37.8 liquidity=264403040.0 spike=0.71
- TRTO.CA: score=5.5 buy_ready=False sector_rank=9 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=235.59 spike=0.33
- UEFM.CA: score=7.63 buy_ready=False sector_rank=9 price=470.0 support=460.0 resistance=505.0 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=47.13 liquidity=1309420.0 spike=1.41
- UEGC.CA: score=17.2 buy_ready=False sector_rank=9 price=1.4 support=1.33 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=9698000.0 spike=0.41
- UNIP.CA: score=10.84 buy_ready=False sector_rank=9 price=0.32 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=49.41 liquidity=3335274.0 spike=0.14
- UNIT.CA: score=9.17 buy_ready=False sector_rank=10 price=13.03 support=12.0 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=16.59 liquidity=6597359.0 spike=1.05
- WCDF.CA: score=5.62 buy_ready=False sector_rank=9 price=518.05 support=450.0 resistance=547.9 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=38.07 liquidity=396308.24 spike=1.36
- WKOL.CA: score=0.0 buy_ready=False sector_rank=9 price=279.26 support=273.1 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=17.3 liquidity=500319.97 spike=0.18
- ZEOT.CA: score=19.5 buy_ready=False sector_rank=9 price=10.86 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=66.72 liquidity=19569914.0 spike=0.63
- ZMID.CA: score=19.47 buy_ready=False sector_rank=10 price=6.49 support=5.96 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=42.03 liquidity=143084928.0 spike=0.68

## Backtesting Lite
- CSAG.CA: 180d return=13.61%, max drawdown=-28.0%, MA20>MA50 days last20=20, as_of=2026-06-28T21:00:00+00:00
- MHOT.CA: 180d return=39.65%, max drawdown=-15.7%, MA20>MA50 days last20=20, as_of=2026-06-28T21:00:00+00:00
- RAYA.CA: 180d return=153.47%, max drawdown=-12.86%, MA20>MA50 days last20=20, as_of=2026-06-28T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CSAG.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Canal Shipping Agencies summary=Canal Shipping Agencies targets EGP 970m net profits in FY26/27; Canal Shipping Agencies’ stock rebounds; Canal Shipping Agencies mulls EGP 100m capital raise
  - Canal Shipping Agencies targets EGP 970m net profits in FY26/27: https://english.mubasher.info/news/4582423/Canal-Shipping-Agencies-targets-EGP-970m-net-profits-in-FY26-27/
  - Canal Shipping Agencies’ stock rebounds: https://english.mubasher.info/news/4564447/Canal-Shipping-Agencies-stock-rebounds/
  - Canal Shipping Agencies mulls EGP 100m capital raise: https://english.mubasher.info/news/4191441/Canal-Shipping-Agencies-mulls-EGP-100m-capital-raise/
- MHOT.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Hotels summary=Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26; Shareholder buys EGP 3.39m worth of shares in Misr Hotels; Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits
  - Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26: https://english.mubasher.info/news/4602482/Misr-Hotels-net-profits-cross-EGP-1-1bn-in-9M-25-26/
  - Shareholder buys EGP 3.39m worth of shares in Misr Hotels: https://english.mubasher.info/news/4013808/Shareholder-buys-EGP-3-39m-worth-of-shares-in-Misr-Hotels/
  - Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits: https://english.mubasher.info/news/3975543/Misr-Hotels-repays-EGP-383m-of-NBE-s-loan-unveils-estimated-profits/
- RAYA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=545 sources=3 expected=Raya Holding summary=Raya stock maintains bullish momentum above EGP 9; Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt; Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn
  - Raya stock maintains bullish momentum above EGP 9: https://english.mubasher.info/news/4601857/Raya-stock-maintains-bullish-momentum-above-EGP-9/
  - Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt: https://english.mubasher.info/news/4577815/Aman-Holding-MSMEDA-partner-to-inject-EGP-300m-into-SMEs-across-Egypt/
  - Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn: https://english.mubasher.info/news/4564195/Raya-Holding-s-consolidated-profits-surge-in-2025-revenues-hit-EGP-63-8bn/
- CAED.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Educational Services SAE summary=Cairo Educational Services&#39; OGM approves EGP 1/shr coupon distribution; Cairo Educational Services’ board proposes 80 piastres per-share dividends; Cairo Educational Services’ profit declines in FY18/19
  - Cairo Educational Services&#39; OGM approves EGP 1/shr coupon distribution: https://english.mubasher.info/news/3884789/Cairo-Educational-Services-OGM-approves-EGP-1-shr-coupon-distribution/
  - Cairo Educational Services’ board proposes 80 piastres per-share dividends: https://english.mubasher.info/news/3556129/Cairo-Educational-Services-board-proposes-80-piastres-per-share-dividends/
  - Cairo Educational Services’ profit declines in FY18/19: https://english.mubasher.info/news/3556119/Cairo-Educational-Services-profit-declines-in-FY18-19/
- NINH.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=545 sources=3 expected=Nozha International Hospital summary=Nozha International Hospital’s net profits cross EGP 174m in 2025; Nozha International Hospital unveils EGP 58m capital increase, new asset details; Nozha International Hospital registers EGP 11.3m block trading
  - Nozha International Hospital’s net profits cross EGP 174m in 2025: https://english.mubasher.info/news/4558517/Nozha-International-Hospital-s-net-profits-cross-EGP-174m-in-2025/
  - Nozha International Hospital unveils EGP 58m capital increase, new asset details: https://english.mubasher.info/news/4558456/Nozha-International-Hospital-unveils-EGP-58m-capital-increase-new-asset-details/
  - Nozha International Hospital registers EGP 11.3m block trading: https://english.mubasher.info/news/4056645/Nozha-International-Hospital-registers-EGP-11-3m-block-trading/
- ETRS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Transport and Commercial Services Company S.A.E. summary=Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- GGCC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Giza General - Contracting and Real Estate Investment S.A.E summary=EGX approves listing EGP 144m capital increase for Giza Contracting; Giza Contracting tests key EGP 0.51 level; Giza Contracting’s consolidated net profits leap to EGP 140m in 9M-25
  - EGX approves listing EGP 144m capital increase for Giza Contracting: https://english.mubasher.info/news/4588793/EGX-approves-listing-EGP-144m-capital-increase-for-Giza-Contracting/
  - Giza Contracting tests key EGP 0.51 level: https://english.mubasher.info/news/4563778/Giza-Contracting-tests-key-EGP-0-51-level/
  - Giza Contracting’s consolidated net profits leap to EGP 140m in 9M-25: https://english.mubasher.info/news/4530408/Giza-Contracting-s-consolidated-net-profits-leap-to-EGP-140m-in-9M-25/
- MASR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=545 sources=3 expected=Madinet Masr For Housing and Development summary=Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval; Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended; Madinet Masr to distribute treasury stocks in first-ever move
  - Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval: https://english.mubasher.info/news/4601386/Madinet-Masr-to-pay-out-EGP-0-15-shr-for-2025-upon-equityholders-approval/
  - Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended: https://english.mubasher.info/news/4578449/Madinet-Masr-logs-24-higher-consolidated-profits-in-2025-dividends-recommended/
  - Madinet Masr to distribute treasury stocks in first-ever move: https://english.mubasher.info/news/4577724/Madinet-Masr-to-distribute-treasury-stocks-in-first-ever-move/

## Warnings
- Evidence for CSAG.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for MHOT.CA matches the company but no source/report date was detected.
- Evidence for RAYA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CAED.CA matches the company but no source/report date was detected.
- Evidence for NINH.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- Evidence for GGCC.CA matches the company but no source/report date was detected.
- Evidence for MASR.CA matches the company but appears old; latest detected date is 2025-01-01.
