# Telegram-First EGX Scanner Report

Scan phase: Evening tomorrow plan
Generated UTC: 2026-09-20T18:58:31.444936+00:00
Generated Cairo: 2026-09-20 21:58
Run timing: target 19:30 Cairo | generated Cairo 2026-09-20 21:58 | cron 30 16 * * 0-4
Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-09-20 21:55

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 161/187
- Top sector: Investment Holding

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, September 20
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 50.0% / above MA50 55.56%
- EGX70 regime: BEARISH / above MA20 37.14% / above MA50 54.29%
- Sector breadth: 14.29%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=1107262720.0 spike=1.33 score=24.06
- MPCO.CA: liquidity=431222560.0 spike=2.8 score=8.76
- ABUK.CA: liquidity=302148288.0 spike=1.92 score=7.49
- MFPC.CA: liquidity=274081952.0 spike=1.92 score=21.49
- TMGH.CA: liquidity=234061712.0 spike=0.84 score=14.55

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are both in a bearish regime with low sector breadth (14.29%), triggering a defensive risk mode that blocks new buys despite individual bullish‑watch signals.
- Market regime: EGX30 trend BEARISH, EGX70 trend BEARISH, breadth weak; risk mode set to DEFENSIVE_NO_NEW_BUY, overriding scanner’s bullish watch outlook.
- Prioritized tickets (e.g., GBCO.CA, BINV.CA, OIH.CA) show high rank scores, accumulation‑spike liquidity, elevated RSI, and prices sitting close to 20‑day resistance with tight support distance, suggesting short‑term ups
- Sector breadth is low; leading sectors are Investment Holding, Telecommunications, and Energy & Petrochemicals, yet most constituents remain below their 20‑day MA, limiting sustained follow‑through.
- Uncertainty: resistance proximity, overheated RSI, and cooling liquidity spikes imply any upside could be fragile; expect range‑bound or modest pullback over the next 1‑3 days unless the EGX regime shifts.

## Top Liquidity Spikes
- CANA.CA: spike=7.92 liquidity=113486960.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RUBX.CA: spike=5.61 liquidity=109538520.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- IDRE.CA: spike=5.36 liquidity=54910400.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ENGC.CA: spike=4.75 liquidity=57743504.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SDTI.CA: spike=4.52 liquidity=93724832.0 outlook=BULLISH_WATCH score=70.17 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=18.37 5d=12.95% 20d=25.96% aboveMA50=100.0%
- #2 Telecommunications: score=9.81 5d=1.89% 20d=8.38% aboveMA50=100.0%
- #3 Energy & Petrochemicals: score=6.63 5d=-4.2% 20d=3.69% aboveMA50=100.0%
- #4 Education: score=6.47 5d=1.67% 20d=3.61% aboveMA50=66.67%
- #5 Automotive & Distribution: score=5.43 5d=-0.07% 20d=0.23% aboveMA50=50.0%
- #6 Banking & Financials: score=4.14 5d=-1.22% 20d=-0.15% aboveMA50=60.0%
- #7 Basic Resources & Chemicals: score=4.13 5d=-1.64% 20d=-0.13% aboveMA50=50.0%
- #8 Textiles: score=4.0 5d=-4.62% 20d=4.21% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ALCN.CA: BULLISH_WATCH score=91.99 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- EGAS.CA: BULLISH_WATCH score=91.63 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- EGCH.CA: BULLISH_WATCH score=91.13 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- FERC.CA: BULLISH_WATCH score=85.13 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- OIH.CA: BULLISH_WATCH score=84 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- WKOL.CA: BULLISH_WATCH score=81.17 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- EXPA.CA: BULLISH_WATCH score=79.14 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- MFSC.CA: BULLISH_WATCH score=78.17 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- BINV.CA: BULLISH_WATCH score=77 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support; close to resistance
- SNFC.CA: BULLISH_WATCH score=76.17 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=17.93 buy_ready=False sector_rank=13 price=306.61 support=295.0 resistance=345.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=61.15 liquidity=21767872.0 spike=1.03
- ABUK.CA: score=7.49 buy_ready=False sector_rank=7 price=94.67 support=93.0 resistance=96.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=302148288.0 spike=1.92
- ACAMD.CA: score=18.87 buy_ready=False sector_rank=13 price=2.08 support=1.95 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=54460608.0 spike=0.92
- ACGC.CA: score=16.44 buy_ready=False sector_rank=8 price=14.25 support=12.56 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.61 liquidity=7841480.0 spike=0.2
- ADCI.CA: score=10.88 buy_ready=False sector_rank=13 price=284.29 support=267.66 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.15 liquidity=3008419.75 spike=0.51
- ADIB.CA: score=19.26 buy_ready=False sector_rank=6 price=52.75 support=50.51 resistance=55.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.56 liquidity=92866456.0 spike=1.3
- ADPC.CA: score=17.93 buy_ready=False sector_rank=13 price=3.94 support=3.81 resistance=4.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.28 liquidity=31273340.0 spike=1.53
- AFDI.CA: score=14.29 buy_ready=False sector_rank=13 price=55.04 support=51.6 resistance=68.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.6 liquidity=9424284.0 spike=0.38
- AFMC.CA: score=9.87 buy_ready=False sector_rank=13 price=162.81 support=153.0 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.35 liquidity=31770550.0 spike=0.48
- AJWA.CA: score=14.87 buy_ready=False sector_rank=13 price=180.0 support=175.15 resistance=199.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.93 liquidity=11032143.0 spike=0.23
- ALCN.CA: score=22.62 buy_ready=False sector_rank=9 price=32.51 support=30.03 resistance=34.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.87 liquidity=58377892.0 spike=2.01
- ALUM.CA: score=7.76 buy_ready=False sector_rank=13 price=26.73 support=25.0 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=22.55 liquidity=4888143.0 spike=0.34
- AMER.CA: score=12.55 buy_ready=False sector_rank=16 price=5.4 support=4.8 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.13 liquidity=19883844.0 spike=0.32
- AMES.CA: score=4.87 buy_ready=False sector_rank=13 price=49.82 support=49.65 resistance=53.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=94245024.0 spike=0.34
- AMIA.CA: score=4.87 buy_ready=False sector_rank=13 price=18.44 support=17.91 resistance=18.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17516962.0 spike=0.3
- AMOC.CA: score=20.4 buy_ready=False sector_rank=3 price=14.1 support=10.65 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.24 liquidity=149464336.0 spike=0.85
- APSW.CA: score=4.22 buy_ready=False sector_rank=13 price=8.52 support=8.37 resistance=8.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=44.94 liquidity=356149.41 spike=0.34
- ARAB.CA: score=14.55 buy_ready=False sector_rank=16 price=0.25 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=48811044.0 spike=0.44
- ARCC.CA: score=17.27 buy_ready=False sector_rank=19 price=73.28 support=71.5 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.26 liquidity=14112404.0 spike=0.34
- AREH.CA: score=14.59 buy_ready=False sector_rank=13 price=1.43 support=1.39 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=9721760.0 spike=0.65
- ASCM.CA: score=9.53 buy_ready=False sector_rank=13 price=61.33 support=60.15 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.59 liquidity=4661437.0 spike=0.21
- ASPI.CA: score=18.59 buy_ready=False sector_rank=13 price=0.46 support=0.41 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.27 liquidity=76578344.0 spike=1.36
- ATLC.CA: score=18.12 buy_ready=False sector_rank=12 price=7.12 support=5.2 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=66.16 liquidity=11293576.0 spike=0.41
- ATQA.CA: score=6.47 buy_ready=False sector_rank=7 price=13.23 support=12.71 resistance=13.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=147830144.0 spike=1.41
- AXPH.CA: score=15.57 buy_ready=False sector_rank=13 price=1673.69 support=1362.0 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=55.4 liquidity=3705218.5 spike=0.3
- BINV.CA: score=25.74 buy_ready=False sector_rank=1 price=61.72 support=47.07 resistance=62.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=83.0 liquidity=37246228.0 spike=2.17
- BIOC.CA: score=9.87 buy_ready=False sector_rank=13 price=273.69 support=272.01 resistance=506.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=14.21 liquidity=19579188.0 spike=0.17
- BTFH.CA: score=18.18 buy_ready=False sector_rank=12 price=3.03 support=2.87 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.93 liquidity=190532864.0 spike=2.03
- CAED.CA: score=12.87 buy_ready=False sector_rank=13 price=129.31 support=123.56 resistance=181.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.76 liquidity=11486515.0 spike=0.33
- CANA.CA: score=10.66 buy_ready=False sector_rank=6 price=46.5 support=44.0 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=113486960.0 spike=7.92
- CCAP.CA: score=24.06 buy_ready=False sector_rank=1 price=7.2 support=5.42 resistance=6.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.08 liquidity=1107262720.0 spike=1.33
- CCRS.CA: score=17.87 buy_ready=False sector_rank=13 price=2.62 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.91 liquidity=22102638.0 spike=0.42
- CEFM.CA: score=17.57 buy_ready=False sector_rank=13 price=146.21 support=143.0 resistance=167.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=53.61 liquidity=7700137.0 spike=0.49
- CERA.CA: score=19.87 buy_ready=False sector_rank=13 price=1.47 support=1.22 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.63 liquidity=60016152.0 spike=0.54
- CFGH.CA: score=7.88 buy_ready=False sector_rank=13 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=63.16 liquidity=11881.23 spike=0.6
- CICH.CA: score=14.32 buy_ready=False sector_rank=12 price=13.05 support=12.0 resistance=13.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=54.91 liquidity=4195916.5 spike=0.71
- CIEB.CA: score=18.85 buy_ready=False sector_rank=6 price=25.49 support=24.01 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.05 liquidity=8194392.5 spike=0.6
- CIRA.CA: score=21.4 buy_ready=False sector_rank=4 price=40.39 support=32.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=36452748.0 spike=1.0
- CLHO.CA: score=9.3 buy_ready=False sector_rank=21 price=15.95 support=15.81 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.81 liquidity=98875392.0 spike=1.28
- CNFN.CA: score=16.34 buy_ready=False sector_rank=12 price=4.7 support=4.46 resistance=4.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.47 liquidity=19542212.0 spike=1.61
- COMI.CA: score=10.66 buy_ready=False sector_rank=6 price=133.12 support=131.11 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.43 liquidity=154435680.0 spike=0.28
- COPR.CA: score=17.87 buy_ready=False sector_rank=13 price=0.51 support=0.46 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.82 liquidity=44886724.0 spike=0.62
- COSG.CA: score=19.87 buy_ready=False sector_rank=13 price=1.88 support=1.74 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.72 liquidity=29587648.0 spike=0.73
- CPCI.CA: score=13.78 buy_ready=False sector_rank=13 price=556.96 support=525.1 resistance=569.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.95 liquidity=7330072.5 spike=1.79
- CSAG.CA: score=3.75 buy_ready=False sector_rank=9 price=38.33 support=38.2 resistance=39.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8149050.0 spike=0.49
- DAPH.CA: score=17.87 buy_ready=False sector_rank=13 price=120.76 support=108.11 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.89 liquidity=18648542.0 spike=0.3
- DEIN.CA: score=7.87 buy_ready=False sector_rank=13 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=4.18 buy_ready=False sector_rank=17 price=26.0 support=26.51 resistance=29.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=28.18 liquidity=4756927.0 spike=0.85
- DSCW.CA: score=13.87 buy_ready=False sector_rank=13 price=1.83 support=1.8 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.93 liquidity=30623862.0 spike=0.8
- DTPP.CA: score=20.27 buy_ready=False sector_rank=13 price=341.01 support=292.5 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.84 liquidity=77923928.0 spike=1.2
- EALR.CA: score=9.66 buy_ready=False sector_rank=13 price=380.87 support=340.0 resistance=415.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=4790747.0 spike=0.34
- EASB.CA: score=18.57 buy_ready=False sector_rank=13 price=8.11 support=7.16 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.2 liquidity=6702966.0 spike=0.39
- EAST.CA: score=8.43 buy_ready=False sector_rank=17 price=32.06 support=32.0 resistance=36.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=28.11 liquidity=38620772.0 spike=0.54
- EBSC.CA: score=15.02 buy_ready=False sector_rank=13 price=2.07 support=1.88 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.96 liquidity=7152635.5 spike=0.49
- ECAP.CA: score=8.61 buy_ready=False sector_rank=13 price=32.27 support=31.16 resistance=37.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=43.33 liquidity=3737169.25 spike=0.32
- EDFM.CA: score=10.35 buy_ready=False sector_rank=13 price=412.56 support=399.0 resistance=465.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.7 liquidity=484849.03 spike=0.25
- EEII.CA: score=4.87 buy_ready=False sector_rank=13 price=2.34 support=2.23 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17725512.0 spike=0.83
- EFIC.CA: score=14.65 buy_ready=False sector_rank=7 price=193.0 support=192.75 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=48746232.0 spike=0.14
- EFID.CA: score=19.43 buy_ready=False sector_rank=17 price=31.6 support=29.71 resistance=33.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.83 liquidity=41332164.0 spike=0.67
- EFIH.CA: score=13.92 buy_ready=False sector_rank=20 price=23.28 support=22.16 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=41.65 liquidity=64905640.0 spike=1.04
- EGAL.CA: score=20.65 buy_ready=False sector_rank=7 price=372.01 support=321.01 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.36 liquidity=28130062.0 spike=0.27
- EGAS.CA: score=21.46 buy_ready=False sector_rank=3 price=58.98 support=55.0 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.63 liquidity=8957573.0 spike=1.05
- EGBE.CA: score=3.77 buy_ready=False sector_rank=6 price=0.5 support=0.49 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=29.63 liquidity=117494.98 spike=0.99
- EGCH.CA: score=22.01 buy_ready=False sector_rank=7 price=14.28 support=13.3 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=58.58 liquidity=194157040.0 spike=1.68
- EGSA.CA: score=11.39 buy_ready=False sector_rank=2 price=9.0 support=8.67 resistance=9.1 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=78.18 liquidity=10413.0 spike=1.49
- EGTS.CA: score=15.97 buy_ready=False sector_rank=16 price=16.94 support=16.17 resistance=17.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=47.02 liquidity=42204772.0 spike=1.71
- EHDR.CA: score=14.28 buy_ready=False sector_rank=13 price=2.78 support=2.73 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=9414454.0 spike=0.47
- ELEC.CA: score=9.11 buy_ready=False sector_rank=14 price=2.02 support=1.93 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.56 liquidity=84422008.0 spike=1.23
- ELKA.CA: score=14.87 buy_ready=False sector_rank=13 price=1.73 support=1.7 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=47.17 liquidity=13974225.0 spike=0.32
- ELNA.CA: score=-0.75 buy_ready=False sector_rank=13 price=35.22 support=33.96 resistance=38.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=28.76 liquidity=383835.38 spike=0.79
- ELSH.CA: score=14.87 buy_ready=False sector_rank=13 price=13.22 support=12.67 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.01 liquidity=34969324.0 spike=0.9
- ELWA.CA: score=5.25 buy_ready=False sector_rank=13 price=1.7 support=1.62 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=383444.84 spike=0.15
- EMFD.CA: score=17.55 buy_ready=False sector_rank=16 price=13.86 support=11.55 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=73.27 liquidity=76525904.0 spike=0.45
- ENGC.CA: score=9.87 buy_ready=False sector_rank=13 price=44.27 support=42.41 resistance=45.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=57743504.0 spike=4.75
- EOSB.CA: score=10.09 buy_ready=False sector_rank=13 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=77512.47 spike=1.07
- EPCO.CA: score=19.87 buy_ready=False sector_rank=13 price=11.22 support=10.8 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.6 liquidity=13245832.0 spike=0.71
- EPPK.CA: score=-4.71 buy_ready=False sector_rank=13 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=20.4 buy_ready=False sector_rank=2 price=131.56 support=112.5 resistance=135.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=83.97 liquidity=73551424.0 spike=0.35
- ETRS.CA: score=19.87 buy_ready=False sector_rank=13 price=11.14 support=10.66 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.74 liquidity=12491651.0 spike=0.82
- EXPA.CA: score=21.1 buy_ready=False sector_rank=6 price=21.41 support=19.8 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.73 liquidity=46209344.0 spike=1.22
- FAIT.CA: score=12.14 buy_ready=False sector_rank=6 price=47.6 support=39.58 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=66.22 liquidity=3487580.5 spike=0.41
- FAITA.CA: score=5.81 buy_ready=False sector_rank=6 price=0.99 support=0.98 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=9.76 liquidity=152701.55 spike=3.54
- FERC.CA: score=20.67 buy_ready=False sector_rank=7 price=81.2 support=76.9 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.29 liquidity=17981834.0 spike=1.01
- FWRY.CA: score=13.84 buy_ready=False sector_rank=20 price=18.99 support=18.66 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.8 liquidity=37518308.0 spike=0.26
- GBCO.CA: score=26.95 buy_ready=False sector_rank=5 price=31.48 support=27.51 resistance=31.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=62.31 liquidity=165716272.0 spike=2.89
- GDWA.CA: score=13.87 buy_ready=False sector_rank=13 price=0.78 support=0.76 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.92 liquidity=26504296.0 spike=0.6
- GGCC.CA: score=14.58 buy_ready=False sector_rank=13 price=0.86 support=0.83 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.36 liquidity=9709277.0 spike=0.27
- GIHD.CA: score=17.87 buy_ready=False sector_rank=13 price=72.96 support=58.01 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.35 liquidity=15850143.0 spike=0.55
- GMCI.CA: score=-0.76 buy_ready=False sector_rank=13 price=1.76 support=1.69 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=23.33 liquidity=370145.09 spike=0.72
- GRCA.CA: score=4.87 buy_ready=False sector_rank=13 price=41.31 support=40.8 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16077009.0 spike=0.19
- GSSC.CA: score=6.13 buy_ready=False sector_rank=13 price=311.01 support=310.33 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14990589.0 spike=1.63
- GTWL.CA: score=19.87 buy_ready=False sector_rank=13 price=234.05 support=181.52 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=62.29 liquidity=84930456.0 spike=0.33
- HDBK.CA: score=18.66 buy_ready=False sector_rank=6 price=120.5 support=89.01 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.08 liquidity=32252984.0 spike=0.56
- HELI.CA: score=21.55 buy_ready=False sector_rank=16 price=8.35 support=7.34 resistance=8.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=68.15 liquidity=155712816.0 spike=1.0
- HRHO.CA: score=14.12 buy_ready=False sector_rank=12 price=25.33 support=25.04 resistance=26.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.38 liquidity=80680232.0 spike=0.8
- ICID.CA: score=15.02 buy_ready=False sector_rank=13 price=17.97 support=15.25 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=60.06 liquidity=5154460.5 spike=0.31
- IDRE.CA: score=9.87 buy_ready=False sector_rank=13 price=58.45 support=55.7 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=54910400.0 spike=5.36
- IFAP.CA: score=18.16 buy_ready=False sector_rank=11 price=20.56 support=20.05 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=40.41 liquidity=10331887.0 spike=0.37
- INFI.CA: score=10.38 buy_ready=False sector_rank=13 price=133.7 support=130.15 resistance=174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=16.41 liquidity=7512417.0 spike=0.24
- IRON.CA: score=9.65 buy_ready=False sector_rank=7 price=28.01 support=26.3 resistance=32.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=2.57 liquidity=13057939.0 spike=0.91
- ISMA.CA: score=9.87 buy_ready=False sector_rank=13 price=30.71 support=28.05 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=18.03 liquidity=11156691.0 spike=0.43
- ISMQ.CA: score=16.45 buy_ready=False sector_rank=7 price=9.08 support=8.68 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.6 liquidity=38072564.0 spike=1.4
- ISPH.CA: score=8.74 buy_ready=False sector_rank=21 price=12.15 support=11.9 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=34.75 liquidity=62712120.0 spike=0.91
- JUFO.CA: score=15.43 buy_ready=False sector_rank=17 price=26.9 support=26.45 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=47.98 liquidity=10802204.0 spike=0.51
- KABO.CA: score=20.6 buy_ready=False sector_rank=8 price=9.37 support=8.82 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=53.97 liquidity=22972676.0 spike=0.47
- KWIN.CA: score=9.87 buy_ready=False sector_rank=13 price=90.54 support=84.5 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.99 liquidity=16031470.0 spike=0.24
- KZPC.CA: score=17.87 buy_ready=False sector_rank=13 price=14.4 support=12.6 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.6 liquidity=14807662.0 spike=0.23
- LCSW.CA: score=14.27 buy_ready=False sector_rank=19 price=33.06 support=32.42 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.62 liquidity=12815192.0 spike=0.48
- LUTS.CA: score=4.87 buy_ready=False sector_rank=13 price=0.94 support=0.93 resistance=0.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=34379372.0 spike=0.13
- MAAL.CA: score=14.78 buy_ready=False sector_rank=13 price=8.7 support=8.18 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.22 liquidity=9909875.0 spike=0.95
- MASR.CA: score=14.87 buy_ready=False sector_rank=13 price=7.76 support=7.49 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.91 liquidity=76096072.0 spike=0.81
- MBSC.CA: score=17.27 buy_ready=False sector_rank=19 price=364.19 support=363.0 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.6 liquidity=20651062.0 spike=0.39
- MCQE.CA: score=17.27 buy_ready=False sector_rank=19 price=218.89 support=213.0 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=41.55 liquidity=14179682.0 spike=0.41
- MCRO.CA: score=16.87 buy_ready=False sector_rank=13 price=1.7 support=1.44 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.49 liquidity=50511984.0 spike=0.4
- MENA.CA: score=5.09 buy_ready=False sector_rank=16 price=6.69 support=6.58 resistance=7.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=546213.31 spike=0.23
- MEPA.CA: score=19.87 buy_ready=False sector_rank=13 price=1.98 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=58.97 liquidity=30427878.0 spike=0.79
- MFPC.CA: score=21.49 buy_ready=False sector_rank=7 price=49.8 support=39.02 resistance=48.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=81.52 liquidity=274081952.0 spike=1.92
- MFSC.CA: score=17.4 buy_ready=False sector_rank=13 price=50.82 support=48.5 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=6811162.5 spike=1.36
- MHOT.CA: score=18.26 buy_ready=False sector_rank=10 price=17.96 support=17.62 resistance=19.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.64 liquidity=13443138.0 spike=1.34
- MICH.CA: score=17.44 buy_ready=False sector_rank=13 price=49.16 support=47.2 resistance=53.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.52 liquidity=9572355.0 spike=0.46
- MILS.CA: score=11.83 buy_ready=False sector_rank=13 price=201.01 support=198.0 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=32.69 liquidity=8957508.0 spike=0.2
- MIPH.CA: score=3.22 buy_ready=False sector_rank=21 price=873.46 support=811.03 resistance=878.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7578327.5 spike=1.95
- MOED.CA: score=16.87 buy_ready=False sector_rank=13 price=0.79 support=0.74 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.14 liquidity=15103465.0 spike=0.13
- MOIL.CA: score=18.23 buy_ready=False sector_rank=3 price=0.7 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.11 liquidity=832064.75 spike=3.97
- MOIN.CA: score=19.87 buy_ready=False sector_rank=13 price=36.73 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=53.32 liquidity=11112239.0 spike=0.36
- MOSC.CA: score=13.99 buy_ready=False sector_rank=13 price=310.32 support=302.0 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.09 liquidity=11748619.0 spike=1.56
- MPCI.CA: score=17.87 buy_ready=False sector_rank=13 price=402.45 support=345.0 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.38 liquidity=115101880.0 spike=0.73
- MPCO.CA: score=8.76 buy_ready=False sector_rank=11 price=2.94 support=2.72 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=431222560.0 spike=2.8
- MPRC.CA: score=14.87 buy_ready=False sector_rank=13 price=39.64 support=38.31 resistance=46.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.32 liquidity=18340602.0 spike=0.44
- MTIE.CA: score=16.17 buy_ready=False sector_rank=5 price=8.49 support=8.1 resistance=8.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=45.86 liquidity=12540060.0 spike=0.33
- NAHO.CA: score=-5.11 buy_ready=False sector_rank=13 price=0.13 support=0.13 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19077.63 spike=0.29
- NCCW.CA: score=4.95 buy_ready=False sector_rank=13 price=7.73 support=7.72 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=63649504.0 spike=1.04
- NEDA.CA: score=10.42 buy_ready=False sector_rank=13 price=2.78 support=2.7 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=40.62 liquidity=552614.5 spike=0.77
- NHPS.CA: score=9.81 buy_ready=False sector_rank=13 price=77.04 support=75.31 resistance=98.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=6.12 liquidity=9945469.0 spike=0.5
- NINH.CA: score=11.05 buy_ready=False sector_rank=13 price=21.54 support=20.5 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.28 liquidity=48417136.0 spike=1.59
- NIPH.CA: score=11.74 buy_ready=False sector_rank=21 price=312.57 support=301.0 resistance=414.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.33 liquidity=44282268.0 spike=0.23
- OBRI.CA: score=11.64 buy_ready=False sector_rank=13 price=31.41 support=30.1 resistance=34.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.87 liquidity=7771411.5 spike=0.46
- OCDI.CA: score=14.55 buy_ready=False sector_rank=16 price=30.16 support=29.25 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.46 liquidity=60505348.0 spike=0.74
- OCPH.CA: score=4.46 buy_ready=False sector_rank=13 price=240.67 support=210.0 resistance=277.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=33.91 liquidity=3592289.25 spike=0.43
- ODIN.CA: score=10.15 buy_ready=False sector_rank=13 price=2.86 support=2.55 resistance=3.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=13.51 liquidity=28318564.0 spike=1.14
- OFH.CA: score=19.91 buy_ready=False sector_rank=13 price=1.09 support=0.88 resistance=1.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=126222776.0 spike=1.02
- OIH.CA: score=24.4 buy_ready=False sector_rank=1 price=2.18 support=1.83 resistance=2.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.0 liquidity=94732096.0 spike=0.76
- OLFI.CA: score=14.43 buy_ready=False sector_rank=17 price=22.62 support=22.07 resistance=24.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.47 liquidity=10685550.0 spike=0.66
- ORAS.CA: score=4.6 buy_ready=False sector_rank=15 price=855.01 support=850.4 resistance=875.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=138694688.0 spike=1.0
- ORHD.CA: score=20.13 buy_ready=False sector_rank=16 price=42.69 support=40.28 resistance=43.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.0 liquidity=171136368.0 spike=1.29
- ORWE.CA: score=20.6 buy_ready=False sector_rank=8 price=28.05 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=57.35 liquidity=52453412.0 spike=1.0
- PHAR.CA: score=8.74 buy_ready=False sector_rank=21 price=117.52 support=117.01 resistance=141.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.74 liquidity=60218820.0 spike=0.41
- PHDC.CA: score=9.83 buy_ready=False sector_rank=16 price=13.22 support=13.65 resistance=15.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.85 liquidity=195523280.0 spike=1.14
- PHTV.CA: score=12.84 buy_ready=False sector_rank=13 price=358.0 support=311.27 resistance=382.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=64.27 liquidity=2449351.25 spike=1.26
- POUL.CA: score=17.43 buy_ready=False sector_rank=17 price=38.72 support=37.03 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.07 liquidity=15587020.0 spike=0.66
- PRCL.CA: score=15.59 buy_ready=False sector_rank=19 price=32.04 support=30.9 resistance=35.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.64 liquidity=31325594.0 spike=1.66
- PRDC.CA: score=9.55 buy_ready=False sector_rank=16 price=7.86 support=7.68 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=23.25 liquidity=13309448.0 spike=0.2
- PRMH.CA: score=2.01 buy_ready=False sector_rank=13 price=2.7 support=2.66 resistance=2.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7145923.5 spike=0.66
- RACC.CA: score=10.11 buy_ready=False sector_rank=13 price=9.83 support=9.4 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.29 liquidity=5239703.0 spike=0.27
- RAKT.CA: score=6.73 buy_ready=False sector_rank=13 price=22.08 support=21.4 resistance=23.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.94 liquidity=342569.81 spike=1.26
- RAYA.CA: score=14.3 buy_ready=False sector_rank=18 price=7.1 support=6.95 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=36222660.0 spike=0.65
- RMDA.CA: score=16.74 buy_ready=False sector_rank=21 price=6.1 support=5.77 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=19186104.0 spike=0.31
- ROTO.CA: score=4.37 buy_ready=False sector_rank=13 price=41.09 support=35.02 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=21.14 liquidity=4506430.5 spike=0.45
- RREI.CA: score=17.87 buy_ready=False sector_rank=13 price=4.36 support=4.24 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.07 liquidity=24355128.0 spike=0.97
- RTVC.CA: score=2.15 buy_ready=False sector_rank=13 price=3.89 support=3.85 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=28.33 liquidity=2284951.75 spike=0.35
- RUBX.CA: score=9.87 buy_ready=False sector_rank=13 price=16.27 support=12.9 resistance=16.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=109538520.0 spike=5.61
- SAUD.CA: score=6.18 buy_ready=False sector_rank=6 price=24.28 support=23.46 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16080581.0 spike=1.26
- SCEM.CA: score=17.27 buy_ready=False sector_rank=19 price=94.5 support=94.0 resistance=105.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.55 liquidity=98942680.0 spike=0.78
- SCFM.CA: score=2.63 buy_ready=False sector_rank=13 price=274.21 support=265.51 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=30.39 liquidity=2761424.0 spike=0.29
- SCTS.CA: score=2.34 buy_ready=False sector_rank=4 price=606.0 support=566.66 resistance=640.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=32.18 liquidity=938124.63 spike=0.29
- SDTI.CA: score=22.87 buy_ready=False sector_rank=13 price=77.98 support=67.0 resistance=76.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=65.18 liquidity=93724832.0 spike=4.52
- SEIG.CA: score=5.69 buy_ready=False sector_rank=13 price=241.17 support=228.13 resistance=274.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=43.16 liquidity=823344.56 spike=0.47
- SIPC.CA: score=19.87 buy_ready=False sector_rank=13 price=5.79 support=4.1 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.96 liquidity=18941306.0 spike=0.27
- SKPC.CA: score=20.65 buy_ready=False sector_rank=7 price=18.65 support=17.0 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.27 liquidity=106079344.0 spike=0.73
- SMFR.CA: score=2.14 buy_ready=False sector_rank=13 price=241.34 support=236.0 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=27.28 liquidity=2273641.5 spike=0.23
- SNFC.CA: score=21.09 buy_ready=False sector_rank=13 price=11.3 support=10.26 resistance=11.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=65.24 liquidity=23273784.0 spike=1.61
- SPIN.CA: score=5.15 buy_ready=False sector_rank=8 price=17.56 support=17.01 resistance=20.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=28.6 liquidity=1554361.13 spike=0.09
- SPMD.CA: score=4.87 buy_ready=False sector_rank=13 price=0.44 support=0.44 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=45920740.0 spike=0.7
- SUGR.CA: score=19.43 buy_ready=False sector_rank=17 price=59.62 support=50.0 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.65 liquidity=10426207.0 spike=0.16
- SVCE.CA: score=19.87 buy_ready=False sector_rank=13 price=11.95 support=10.28 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.57 liquidity=88513376.0 spike=0.47
- SWDY.CA: score=19.65 buy_ready=False sector_rank=14 price=127.78 support=115.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.09 liquidity=22036986.0 spike=0.29
- TALM.CA: score=18.4 buy_ready=False sector_rank=4 price=21.43 support=17.11 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=80.86 liquidity=42788164.0 spike=0.72
- TMGH.CA: score=14.55 buy_ready=False sector_rank=16 price=94.28 support=94.86 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.75 liquidity=234061712.0 spike=0.84
- TRTO.CA: score=-5.11 buy_ready=False sector_rank=13 price=0.06 support=0.06 resistance=0.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20077.87 spike=0.74
- UEFM.CA: score=-3.77 buy_ready=False sector_rank=13 price=507.6 support=500.0 resistance=528.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1361765.88 spike=0.44
- UEGC.CA: score=9.87 buy_ready=False sector_rank=13 price=1.79 support=1.66 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.88 liquidity=31198850.0 spike=0.63
- UNIP.CA: score=14.87 buy_ready=False sector_rank=13 price=0.38 support=0.35 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=52.13 liquidity=12592286.0 spike=0.39
- UNIT.CA: score=-1.09 buy_ready=False sector_rank=16 price=18.62 support=18.6 resistance=19.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4359296.5 spike=0.3
- WCDF.CA: score=11.48 buy_ready=False sector_rank=13 price=742.49 support=630.06 resistance=796.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=81.23 liquidity=2611875.75 spike=0.57
- WKOL.CA: score=20.13 buy_ready=False sector_rank=13 price=345.27 support=332.56 resistance=369.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.88 liquidity=8261781.0 spike=0.73
- ZEOT.CA: score=22.01 buy_ready=False sector_rank=13 price=13.55 support=13.03 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.16 liquidity=20145510.0 spike=3.07
- ZMID.CA: score=4.55 buy_ready=False sector_rank=16 price=8.75 support=8.71 resistance=9.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=185956592.0 spike=0.74

## Backtesting Lite
- GBCO.CA: 180d return=19.04%, max drawdown=-24.35%, MA20>MA50 days last20=1, as_of=2026-09-15T21:00:00+00:00
- BINV.CA: 180d return=70.75%, max drawdown=-17.77%, MA20>MA50 days last20=20, as_of=2026-09-15T21:00:00+00:00
- OIH.CA: 180d return=86.21%, max drawdown=-14.56%, MA20>MA50 days last20=20, as_of=2026-09-15T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- OIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Investment Holding summary=Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- SDTI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=SHARM DREAMS Co. for Touristic Investment S.A.E summary=Sharm Dreams stock maintains strong uptrend - Analysis; Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis; Sharm Dreams stock hits historic level halting driving buying force
  - Sharm Dreams stock maintains strong uptrend - Analysis: https://english.mubasher.info/news/4577977/Sharm-Dreams-stock-maintains-strong-uptrend-Analysis/
  - Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis: https://english.mubasher.info/news/4547831/Sharm-Dreams-stock-is-experiencing-sideways-movement-amid-anticipation-of-next-trend-Analysis/
  - Sharm Dreams stock hits historic level halting driving buying force: https://english.mubasher.info/news/4529096/Sharm-Dreams-stock-hits-historic-level-halting-driving-buying-force/
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- EGCH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Chemical Industries Kima summary=Evidence rejected for EGCH.CA: source text did not clearly match EGCH.CA / Egyptian Chemical Industries Kima.
- ZEOT.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Extracted Oil & Derivatives Co. summary=Extracted Oils stock nears record high on strong momentum; Extracted Oils stock witnesses increasing buying power amid current resistance – Analysis; Extracted Oils swings to nearly EGP 14.5m net profits in Q1-25/26
  - Extracted Oils stock nears record high on strong momentum: https://english.mubasher.info/news/4599376/Extracted-Oils-stock-nears-record-high-on-strong-momentum/
  - Extracted Oils stock witnesses increasing buying power amid current resistance – Analysis: https://english.mubasher.info/news/4555925/Extracted-Oils-stock-witnesses-increasing-buying-power-amid-current-resistance-Analysis/
  - Extracted Oils swings to nearly EGP 14.5m net profits in Q1-25/26: https://english.mubasher.info/news/4537956/Extracted-Oils-swings-to-nearly-EGP-14-5m-net-profits-in-Q1-25-26/

## Warnings
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for SDTI.CA matches the company but no source/report date was detected.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence rejected for EGCH.CA: source text did not clearly match EGCH.CA / Egyptian Chemical Industries Kima.
- Evidence for ZEOT.CA matches the company but no source/report date was detected.
