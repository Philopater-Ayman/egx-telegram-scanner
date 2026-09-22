# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-09-22T10:20:30.217834+00:00
Generated Cairo: 2026-09-22 13:20
Run timing: target 08:45 Cairo | generated Cairo 2026-09-22 13:20 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-22 13:17

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 179/186
- Top sector: Investment Holding

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, September 22
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 21.05% / above MA50 57.89%
- EGX70 regime: BEARISH / above MA20 30.0% / above MA50 52.5%
- Sector breadth: 38.1%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=779249152.0 spike=1.26 score=11.92
- CCAP.CA: liquidity=407191648.0 spike=0.48 score=21.4
- NIPH.CA: liquidity=327223008.0 spike=2.18 score=6.29
- ETEL.CA: liquidity=257410848.0 spike=1.02 score=22.44
- ORHD.CA: liquidity=213590368.0 spike=1.57 score=18.09

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with weak breadth; the scanner stays in defensive mode (no new buys) and highlights a watchlist of tickets based on rank score, outlook and liquidity cues.
- Tickets were picked for their highest rank scores and bullish‑watch/constructive outlooks, indicating short‑term interest despite the broader bearish regime.
- Liquidity shows accumulation spikes or tradeable conditions but many are cooling, suggesting the current interest may be fragile and uncertain over the next 1‑3 days.
- Most highlighted stocks sit near their 20‑day resistance or above support (e.g., GBCO.CA close to resistance, ETEL.CA far above support), so a breakout or pullback could occur soon.
- EGX30/EGX70 bearish trend and low sector breadth shift risk mode to DEFENSIVE_NO_NEW_BUY, meaning any near‑term moves are likely limited or corrective rather than new buying opportunities.

## Top Liquidity Spikes
- SEIG.CA: spike=2.32 liquidity=3990148.5 outlook=WEAK_OR_RISKY score=28.73 buy_ready=False
- POUL.CA: spike=2.28 liquidity=58845364.0 outlook=WEAK_OR_RISKY score=26.58 buy_ready=False
- NIPH.CA: spike=2.18 liquidity=327223008.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GBCO.CA: spike=2.11 liquidity=147309840.0 outlook=BULLISH_WATCH score=72.4 buy_ready=False
- RUBX.CA: spike=1.91 liquidity=73395880.0 outlook=BULLISH_WATCH score=74.73 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=12.67 5d=4.09% 20d=21.55% aboveMA50=100.0%
- #2 Telecommunications: score=10.29 5d=2.98% 20d=9.42% aboveMA50=100.0%
- #3 Agriculture & Food Production: score=8.04 5d=5.68% 20d=12.05% aboveMA50=50.0%
- #4 Transportation & Logistics: score=7.43 5d=5.21% 20d=1.09% aboveMA50=100.0%
- #5 Energy & Petrochemicals: score=6.91 5d=4.48% 20d=3.4% aboveMA50=66.67%
- #6 Banking & Financials: score=6.09 5d=2.82% 20d=4.7% aboveMA50=70.0%
- #7 Automotive & Distribution: score=5.4 5d=2.42% 20d=-1.41% aboveMA50=50.0%
- #8 Education: score=4.48 5d=-4.53% 20d=8.4% aboveMA50=66.67%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- SAUD.CA: BULLISH_WATCH score=82.09 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended
- OIH.CA: BULLISH_WATCH score=82 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- RUBX.CA: BULLISH_WATCH score=74.73 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- CPCI.CA: BULLISH_WATCH score=73.73 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- AMOC.CA: BULLISH_WATCH score=72.91 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; far above support
- ORWE.CA: BULLISH_WATCH score=72.49 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- GBCO.CA: BULLISH_WATCH score=72.4 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; close to resistance
- IDRE.CA: BULLISH_WATCH score=71.73 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- GSSC.CA: BULLISH_WATCH score=71.73 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- KZPC.CA: BULLISH_WATCH score=71.73 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- CICH.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=17.29 buy_ready=False sector_rank=14 price=290.39 support=288.01 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=41.82 liquidity=12080135.0 spike=0.47
- ABUK.CA: score=22.71 buy_ready=False sector_rank=9 price=94.2 support=75.01 resistance=96.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=59.62 liquidity=32641998.0 spike=0.18
- ACAMD.CA: score=16.29 buy_ready=False sector_rank=14 price=2.03 support=1.99 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=10934972.0 spike=0.19
- ACGC.CA: score=10.9 buy_ready=False sector_rank=12 price=14.05 support=13.55 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=48.89 liquidity=3308373.25 spike=0.1
- ADCI.CA: score=4.84 buy_ready=False sector_rank=14 price=282.12 support=267.66 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=20.86 liquidity=2544531.75 spike=0.52
- ADIB.CA: score=19.4 buy_ready=False sector_rank=6 price=52.5 support=50.51 resistance=55.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=43.3 liquidity=33040948.0 spike=0.42
- ADPC.CA: score=17.27 buy_ready=False sector_rank=14 price=3.97 support=3.81 resistance=4.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=48.28 liquidity=26909028.0 spike=1.49
- AFDI.CA: score=1.86 buy_ready=False sector_rank=14 price=52.49 support=51.6 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=32.99 liquidity=2565556.75 spike=0.1
- AFMC.CA: score=8.59 buy_ready=False sector_rank=14 price=159.42 support=153.0 resistance=239.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=35.79 liquidity=4294656.5 spike=0.07
- AJWA.CA: score=8.05 buy_ready=False sector_rank=14 price=180.0 support=175.15 resistance=199.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=47.21 liquidity=3761600.75 spike=0.08
- ALCN.CA: score=23.4 buy_ready=False sector_rank=4 price=33.86 support=30.03 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=62.47 liquidity=24049932.0 spike=0.68
- ALUM.CA: score=0.77 buy_ready=False sector_rank=14 price=25.57 support=25.0 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=30.52 liquidity=1481808.25 spike=0.11
- AMER.CA: score=13.95 buy_ready=False sector_rank=17 price=5.25 support=4.8 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=40.37 liquidity=30937452.0 spike=0.56
- AMES.CA: score=8.29 buy_ready=False sector_rank=14 price=51.61 support=48.45 resistance=158.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=9.27 liquidity=57852284.0 spike=0.22
- AMIA.CA: score=12.29 buy_ready=False sector_rank=14 price=18.41 support=17.12 resistance=21.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=33.83 liquidity=22166434.0 spike=0.45
- AMOC.CA: score=21.4 buy_ready=False sector_rank=5 price=13.5 support=10.65 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=56.3 liquidity=31536910.0 spike=0.18
- APSW.CA: score=-0.07 buy_ready=False sector_rank=14 price=8.3 support=8.2 resistance=8.79 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=34.38 liquidity=1113868.33 spike=1.26
- ARAB.CA: score=8.95 buy_ready=False sector_rank=17 price=0.25 support=0.24 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=32.61 liquidity=12206073.0 spike=0.12
- ARCC.CA: score=8.8 buy_ready=False sector_rank=21 price=70.54 support=69.0 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=20.43 liquidity=7385308.0 spike=0.19
- AREH.CA: score=6.33 buy_ready=False sector_rank=14 price=1.41 support=1.39 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=2039493.12 spike=0.14
- ASCM.CA: score=2.86 buy_ready=False sector_rank=14 price=58.95 support=58.16 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=31.4 liquidity=3565604.0 spike=0.18
- ASPI.CA: score=14.29 buy_ready=False sector_rank=14 price=0.43 support=0.41 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=49.41 liquidity=26620772.0 spike=0.43
- ATLC.CA: score=12.41 buy_ready=False sector_rank=10 price=7.03 support=5.35 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=52.63 liquidity=2431895.0 spike=0.08
- ATQA.CA: score=24.71 buy_ready=False sector_rank=9 price=13.28 support=11.0 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=64.31 liquidity=49632012.0 spike=0.45
- AXPH.CA: score=18.26 buy_ready=False sector_rank=14 price=1688.02 support=1501.0 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=36.72 liquidity=8972120.0 spike=0.97
- BINV.CA: score=21.4 buy_ready=False sector_rank=1 price=56.96 support=48.04 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=75.89 liquidity=17550088.0 spike=0.73
- BIOC.CA: score=4.29 buy_ready=False sector_rank=14 price=276.66 support=266.0 resistance=288.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48885984.0 spike=0.51
- BTFH.CA: score=15.98 buy_ready=False sector_rank=10 price=2.92 support=2.87 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=46.34 liquidity=53930188.0 spike=0.66
- CAED.CA: score=1.32 buy_ready=False sector_rank=14 price=125.98 support=122.6 resistance=173.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=32.49 liquidity=2023213.63 spike=0.09
- CANA.CA: score=17.73 buy_ready=False sector_rank=6 price=46.91 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=70.58 liquidity=4328925.0 spike=0.19
- CCAP.CA: score=21.4 buy_ready=False sector_rank=1 price=7.25 support=5.72 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=407191648.0 spike=0.48
- CCRS.CA: score=13.11 buy_ready=False sector_rank=14 price=2.64 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=48.74 liquidity=3817359.75 spike=0.07
- CEFM.CA: score=7.94 buy_ready=False sector_rank=14 price=143.76 support=135.0 resistance=167.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=43.55 liquidity=648838.69 spike=0.06
- CERA.CA: score=17.29 buy_ready=False sector_rank=14 price=1.39 support=1.22 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=54.92 liquidity=57743756.0 spike=0.46
- CFGH.CA: score=7.3 buy_ready=False sector_rank=14 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=8967.17 spike=0.54
- CIEB.CA: score=12.61 buy_ready=False sector_rank=6 price=24.75 support=24.01 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=50.7 liquidity=3213040.0 spike=0.23
- CIRA.CA: score=19.79 buy_ready=False sector_rank=8 price=39.96 support=32.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=75.87 liquidity=13968414.0 spike=0.35
- CLHO.CA: score=8.93 buy_ready=False sector_rank=18 price=15.84 support=15.4 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=12.13 liquidity=15806983.0 spike=0.21
- CNFN.CA: score=3.32 buy_ready=False sector_rank=10 price=4.54 support=4.46 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=30.59 liquidity=4339825.5 spike=0.37
- COMI.CA: score=11.92 buy_ready=False sector_rank=6 price=131.94 support=131.11 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=32.85 liquidity=779249152.0 spike=1.26
- COPR.CA: score=13.99 buy_ready=False sector_rank=14 price=0.49 support=0.46 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=45.4 liquidity=6693040.0 spike=0.14
- COSG.CA: score=14.15 buy_ready=False sector_rank=14 price=1.8 support=1.78 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=6856626.0 spike=0.2
- CPCI.CA: score=13.77 buy_ready=False sector_rank=14 price=561.13 support=530.0 resistance=584.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=60.45 liquidity=2474595.25 spike=0.75
- CSAG.CA: score=6.86 buy_ready=False sector_rank=4 price=38.19 support=36.5 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=27.53 liquidity=2461217.75 spike=0.16
- DAPH.CA: score=9.29 buy_ready=False sector_rank=14 price=112.52 support=108.11 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=21.49 liquidity=11346764.0 spike=0.19
- DEIN.CA: score=7.29 buy_ready=False sector_rank=14 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=0.96 buy_ready=False sector_rank=15 price=26.53 support=25.56 resistance=29.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=26.65 liquidity=1724216.13 spike=0.32
- DSCW.CA: score=2.78 buy_ready=False sector_rank=14 price=1.8 support=1.77 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=32.35 liquidity=4484165.0 spike=0.15
- DTPP.CA: score=19.73 buy_ready=False sector_rank=14 price=340.0 support=294.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=57.6 liquidity=91249976.0 spike=1.22
- EALR.CA: score=3.0 buy_ready=False sector_rank=14 price=364.67 support=340.0 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=33.51 liquidity=3708829.0 spike=0.26
- EASB.CA: score=10.04 buy_ready=False sector_rank=14 price=7.63 support=7.2 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=55.61 liquidity=2743160.75 spike=0.16
- EAST.CA: score=7.32 buy_ready=False sector_rank=15 price=31.61 support=31.31 resistance=36.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=11.07 liquidity=9092150.0 spike=0.12
- EBSC.CA: score=3.6 buy_ready=False sector_rank=14 price=2.0 support=1.91 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=30.26 liquidity=1311587.38 spike=0.09
- ECAP.CA: score=6.39 buy_ready=False sector_rank=14 price=31.89 support=31.16 resistance=36.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=46.37 liquidity=2102832.25 spike=0.19
- EDFM.CA: score=7.77 buy_ready=False sector_rank=14 price=402.83 support=390.0 resistance=465.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=43.16 liquidity=473268.34 spike=0.26
- EEII.CA: score=3.03 buy_ready=False sector_rank=14 price=2.26 support=2.15 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=33.9 liquidity=4738897.5 spike=0.31
- EFIC.CA: score=14.71 buy_ready=False sector_rank=9 price=183.61 support=183.0 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=43.33 liquidity=16122667.0 spike=0.05
- EFID.CA: score=17.23 buy_ready=False sector_rank=15 price=30.63 support=29.71 resistance=32.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=53.36 liquidity=16999154.0 spike=0.26
- EFIH.CA: score=14.0 buy_ready=False sector_rank=16 price=22.7 support=22.16 resistance=24.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=49.2 liquidity=43337056.0 spike=0.73
- EGAL.CA: score=16.64 buy_ready=False sector_rank=9 price=367.03 support=345.0 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=52.02 liquidity=7932845.5 spike=0.08
- EGAS.CA: score=9.8 buy_ready=False sector_rank=5 price=56.85 support=55.0 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=38.42 liquidity=3401535.5 spike=0.29
- EGBE.CA: score=1.41 buy_ready=False sector_rank=6 price=0.51 support=0.49 resistance=0.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=8072.95 spike=0.1
- EGCH.CA: score=18.71 buy_ready=False sector_rank=9 price=13.96 support=13.3 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=32908966.0 spike=0.27
- EGSA.CA: score=10.4 buy_ready=False sector_rank=2 price=9.0 support=8.68 resistance=9.1 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=78.18 liquidity=3654.0 spike=0.59
- EGTS.CA: score=19.61 buy_ready=False sector_rank=17 price=17.63 support=16.51 resistance=17.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=49.02 liquidity=41084924.0 spike=1.83
- EHDR.CA: score=3.55 buy_ready=False sector_rank=14 price=2.67 support=2.65 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=34.43 liquidity=4255982.5 spike=0.23
- ELEC.CA: score=8.37 buy_ready=False sector_rank=13 price=1.97 support=1.92 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=24084872.0 spike=0.31
- ELKA.CA: score=4.56 buy_ready=False sector_rank=14 price=1.67 support=1.64 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=13.16 liquidity=5272496.5 spike=0.14
- ELNA.CA: score=-1.55 buy_ready=False sector_rank=14 price=35.22 support=33.96 resistance=38.99 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=24.57 liquidity=154827.13 spike=0.42
- ELSH.CA: score=10.8 buy_ready=False sector_rank=14 price=12.71 support=12.55 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=35.74 liquidity=6512419.5 spike=0.17
- ELWA.CA: score=-0.29 buy_ready=False sector_rank=14 price=1.66 support=1.66 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=28.95 liquidity=415724.62 spike=0.19
- EMFD.CA: score=16.95 buy_ready=False sector_rank=17 price=13.45 support=12.1 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=46.19 liquidity=21878424.0 spike=0.13
- ENGC.CA: score=11.68 buy_ready=False sector_rank=14 price=42.36 support=41.0 resistance=47.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=49.72 liquidity=7392672.5 spike=0.46
- EOSB.CA: score=9.77 buy_ready=False sector_rank=14 price=1.57 support=1.53 resistance=1.64 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=76532.79 spike=1.2
- EPCO.CA: score=7.7 buy_ready=False sector_rank=14 price=10.82 support=10.6 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=44.78 liquidity=3408459.5 spike=0.21
- EPPK.CA: score=-5.29 buy_ready=False sector_rank=14 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=22.44 buy_ready=False sector_rank=2 price=137.48 support=112.5 resistance=136.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=85.57 liquidity=257410848.0 spike=1.02
- ETRS.CA: score=8.53 buy_ready=False sector_rank=14 price=10.87 support=10.66 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=35.51 liquidity=1235613.38 spike=0.09
- EXPA.CA: score=23.4 buy_ready=False sector_rank=6 price=22.0 support=19.96 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=64.72 liquidity=28180674.0 spike=0.76
- FAIT.CA: score=10.32 buy_ready=False sector_rank=6 price=46.35 support=41.52 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=67.5 liquidity=920117.63 spike=0.11
- FAITA.CA: score=6.42 buy_ready=False sector_rank=6 price=0.99 support=0.98 resistance=1.02 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=41.18 liquidity=16085.14 spike=0.33
- FERC.CA: score=9.34 buy_ready=False sector_rank=9 price=78.42 support=77.3 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=2626209.5 spike=0.18
- FWRY.CA: score=14.0 buy_ready=False sector_rank=16 price=18.95 support=18.66 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=48.24 liquidity=20198878.0 spike=0.15
- GBCO.CA: score=25.38 buy_ready=False sector_rank=7 price=31.8 support=27.51 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=63.86 liquidity=147309840.0 spike=2.11
- GDWA.CA: score=8.29 buy_ready=False sector_rank=14 price=0.75 support=0.75 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=13.22 liquidity=13511721.0 spike=0.31
- GGCC.CA: score=14.29 buy_ready=False sector_rank=14 price=0.82 support=0.83 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=10151449.0 spike=0.31
- GIHD.CA: score=11.28 buy_ready=False sector_rank=14 price=72.07 support=61.61 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=50.29 liquidity=1985938.75 spike=0.07
- GMCI.CA: score=-1.48 buy_ready=False sector_rank=14 price=1.76 support=1.69 resistance=1.94 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=30.0 liquidity=224906.88 spike=0.47
- GRCA.CA: score=2.04 buy_ready=False sector_rank=14 price=39.6 support=38.7 resistance=85.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=20.93 liquidity=3750956.5 spike=0.06
- GSSC.CA: score=13.4 buy_ready=False sector_rank=14 price=307.31 support=278.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=61.87 liquidity=2111437.75 spike=0.23
- GTWL.CA: score=17.29 buy_ready=False sector_rank=14 price=230.59 support=201.3 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=52.63 liquidity=56879884.0 spike=0.28
- HDBK.CA: score=17.58 buy_ready=False sector_rank=6 price=118.17 support=90.51 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=52.79 liquidity=4177939.5 spike=0.07
- HELI.CA: score=20.95 buy_ready=False sector_rank=17 price=8.11 support=7.34 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=56.92 liquidity=58993252.0 spike=0.34
- HRHO.CA: score=8.98 buy_ready=False sector_rank=10 price=24.55 support=24.83 resistance=26.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=32.67 liquidity=63498216.0 spike=0.64
- ICID.CA: score=8.95 buy_ready=False sector_rank=14 price=17.23 support=16.2 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=45.78 liquidity=1659384.25 spike=0.14
- IDRE.CA: score=15.84 buy_ready=False sector_rank=14 price=54.65 support=51.0 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=47.86 liquidity=4546038.0 spike=0.28
- IFAP.CA: score=11.14 buy_ready=False sector_rank=3 price=20.3 support=19.05 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=40.05 liquidity=3738172.5 spike=0.16
- INFI.CA: score=3.67 buy_ready=False sector_rank=14 price=127.92 support=123.0 resistance=168.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=19.11 liquidity=4382200.0 spike=0.16
- IRON.CA: score=1.33 buy_ready=False sector_rank=9 price=27.56 support=26.3 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=24.29 liquidity=1613723.5 spike=0.11
- ISMA.CA: score=6.8 buy_ready=False sector_rank=14 price=29.43 support=28.05 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=35.67 liquidity=2506394.5 spike=0.11
- ISMQ.CA: score=7.52 buy_ready=False sector_rank=9 price=8.76 support=8.68 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=32.39 liquidity=6807205.0 spike=0.26
- ISPH.CA: score=8.93 buy_ready=False sector_rank=18 price=12.1 support=11.9 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=32.5 liquidity=22134080.0 spike=0.31
- JUFO.CA: score=20.23 buy_ready=False sector_rank=15 price=27.24 support=26.45 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=49.83 liquidity=10248244.0 spike=0.48
- KABO.CA: score=14.5 buy_ready=False sector_rank=12 price=9.28 support=8.9 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=45.27 liquidity=6900689.0 spike=0.16
- KWIN.CA: score=1.55 buy_ready=False sector_rank=14 price=86.12 support=82.5 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=18.91 liquidity=2258452.5 spike=0.04
- KZPC.CA: score=10.92 buy_ready=False sector_rank=14 price=13.67 support=12.6 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=56.9 liquidity=1631516.25 spike=0.04
- LCSW.CA: score=8.42 buy_ready=False sector_rank=21 price=32.68 support=31.61 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=25.24 liquidity=10671351.0 spike=0.44
- LUTS.CA: score=17.29 buy_ready=False sector_rank=14 price=0.89 support=0.83 resistance=1.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=40.2 liquidity=24224930.0 spike=0.13
- MAAL.CA: score=13.55 buy_ready=False sector_rank=14 price=8.99 support=8.18 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=19119714.0 spike=1.63
- MASR.CA: score=14.29 buy_ready=False sector_rank=14 price=7.63 support=7.49 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=45.56 liquidity=26777414.0 spike=0.27
- MBSC.CA: score=11.42 buy_ready=False sector_rank=21 price=348.99 support=340.66 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=20.64 liquidity=12808681.0 spike=0.26
- MCQE.CA: score=8.42 buy_ready=False sector_rank=21 price=204.0 support=207.1 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=23.89 liquidity=14274809.0 spike=0.46
- MCRO.CA: score=19.29 buy_ready=False sector_rank=14 price=1.68 support=1.48 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=113615048.0 spike=0.93
- MENA.CA: score=4.53 buy_ready=False sector_rank=17 price=6.6 support=6.58 resistance=7.13 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=38.32 liquidity=580714.19 spike=0.37
- MEPA.CA: score=13.82 buy_ready=False sector_rank=14 price=1.91 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=46.91 liquidity=6523893.0 spike=0.17
- MFPC.CA: score=17.71 buy_ready=False sector_rank=9 price=49.07 support=39.02 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=76.27 liquidity=27893490.0 spike=0.16
- MFSC.CA: score=8.07 buy_ready=False sector_rank=14 price=49.72 support=48.5 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=44.06 liquidity=782351.56 spike=0.16
- MHOT.CA: score=-0.11 buy_ready=False sector_rank=20 price=17.57 support=16.61 resistance=19.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=27.1 liquidity=2428477.75 spike=0.25
- MICH.CA: score=13.58 buy_ready=False sector_rank=14 price=47.5 support=47.51 resistance=53.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=6289018.0 spike=0.39
- MILS.CA: score=10.06 buy_ready=False sector_rank=14 price=191.88 support=180.01 resistance=232.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=35.45 liquidity=5763030.5 spike=0.22
- MIPH.CA: score=5.61 buy_ready=False sector_rank=18 price=873.12 support=870.0 resistance=941.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14879291.0 spike=1.84
- MOED.CA: score=8.29 buy_ready=False sector_rank=14 price=0.72 support=0.7 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=22.78 liquidity=14060177.0 spike=0.19
- MOIL.CA: score=13.54 buy_ready=False sector_rank=5 price=0.7 support=0.66 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=58.57 liquidity=144198.05 spike=0.67
- MOIN.CA: score=12.92 buy_ready=False sector_rank=14 price=35.78 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=54.45 liquidity=5628487.5 spike=0.18
- MOSC.CA: score=0.2 buy_ready=False sector_rank=14 price=299.22 support=290.0 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=32.83 liquidity=904374.19 spike=0.13
- MPCI.CA: score=12.29 buy_ready=False sector_rank=14 price=401.68 support=371.11 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=16.95 liquidity=117716624.0 spike=0.82
- MPCO.CA: score=22.4 buy_ready=False sector_rank=3 price=2.79 support=2.07 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=72.25 liquidity=52162864.0 spike=0.31
- MPRC.CA: score=2.21 buy_ready=False sector_rank=14 price=38.15 support=37.65 resistance=46.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=30.87 liquidity=2919206.0 spike=0.07
- MTIE.CA: score=5.42 buy_ready=False sector_rank=7 price=8.19 support=8.02 resistance=8.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=21.74 liquidity=5257522.0 spike=0.17
- NAHO.CA: score=-5.66 buy_ready=False sector_rank=14 price=0.13 support=0.13 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=52972.13 spike=0.94
- NCCW.CA: score=21.29 buy_ready=False sector_rank=14 price=7.27 support=5.77 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=63.95 liquidity=38697564.0 spike=0.59
- NEDA.CA: score=7.11 buy_ready=False sector_rank=14 price=2.77 support=2.7 resistance=2.89 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=56.25 liquidity=655251.81 spike=1.08
- NHPS.CA: score=1.19 buy_ready=False sector_rank=14 price=73.18 support=72.52 resistance=98.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=9.18 liquidity=1895348.88 spike=0.11
- NINH.CA: score=4.58 buy_ready=False sector_rank=14 price=20.56 support=20.3 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=32.64 liquidity=5291209.0 spike=0.17
- NIPH.CA: score=6.29 buy_ready=False sector_rank=18 price=344.07 support=310.01 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=327223008.0 spike=2.18
- OBRI.CA: score=3.04 buy_ready=False sector_rank=14 price=30.05 support=29.51 resistance=34.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=16.11 liquidity=4751757.5 spike=0.31
- OCDI.CA: score=13.95 buy_ready=False sector_rank=17 price=29.0 support=29.25 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=42.29 liquidity=29851470.0 spike=0.36
- OCPH.CA: score=5.37 buy_ready=False sector_rank=14 price=240.91 support=210.0 resistance=277.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=34.17 liquidity=5074045.5 spike=0.76
- ODIN.CA: score=9.29 buy_ready=False sector_rank=14 price=2.84 support=2.55 resistance=3.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=33.8 liquidity=18900260.0 spike=0.85
- OFH.CA: score=5.55 buy_ready=False sector_rank=14 price=1.1 support=1.04 resistance=1.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=204329008.0 spike=1.63
- OIH.CA: score=22.4 buy_ready=False sector_rank=1 price=2.13 support=1.91 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=68.97 liquidity=33000046.0 spike=0.28
- OLFI.CA: score=8.21 buy_ready=False sector_rank=15 price=22.71 support=22.07 resistance=23.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=54.22 liquidity=3979549.75 spike=0.22
- ORAS.CA: score=4.6 buy_ready=False sector_rank=11 price=840.38 support=836.12 resistance=848.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=74869096.0 spike=1.0
- ORHD.CA: score=18.09 buy_ready=False sector_rank=17 price=41.96 support=40.85 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=52.18 liquidity=213590368.0 spike=1.57
- ORWE.CA: score=19.6 buy_ready=False sector_rank=12 price=27.3 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=52.06 liquidity=20348038.0 spike=0.36
- PHAR.CA: score=8.93 buy_ready=False sector_rank=18 price=118.0 support=111.55 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=26.6 liquidity=85469208.0 spike=0.79
- PHDC.CA: score=8.95 buy_ready=False sector_rank=17 price=13.44 support=12.91 resistance=15.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=22.14 liquidity=75594904.0 spike=0.44
- PHTV.CA: score=4.63 buy_ready=False sector_rank=14 price=337.83 support=311.27 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=49.26 liquidity=341932.16 spike=0.2
- POUL.CA: score=16.79 buy_ready=False sector_rank=15 price=38.55 support=37.15 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=21 September 01:28 PM market time freshness=DELAYED_CURRENT RSI=38.94 liquidity=58845364.0 spike=2.28
- PRCL.CA: score=6.04 buy_ready=False sector_rank=21 price=31.0 support=30.61 resistance=34.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=46.88 liquidity=2628303.25 spike=0.14
- PRDC.CA: score=6.51 buy_ready=False sector_rank=17 price=7.61 support=7.51 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=9.33 liquidity=7556197.5 spike=0.13
- PRMH.CA: score=6.55 buy_ready=False sector_rank=14 price=2.62 support=2.32 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=2253887.25 spike=0.21
- RACC.CA: score=5.18 buy_ready=False sector_rank=14 price=9.65 support=9.4 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=50.44 liquidity=883951.25 spike=0.05
- RAKT.CA: score=3.37 buy_ready=False sector_rank=14 price=22.08 support=21.4 resistance=23.02 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=47.17 liquidity=81607.68 spike=0.37
- RAYA.CA: score=13.76 buy_ready=False sector_rank=19 price=7.02 support=6.8 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=11100259.0 spike=0.21
- RMDA.CA: score=16.93 buy_ready=False sector_rank=18 price=6.05 support=5.77 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=12040575.0 spike=0.21
- ROTO.CA: score=2.33 buy_ready=False sector_rank=14 price=40.83 support=35.02 resistance=47.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=24.67 liquidity=3036249.0 spike=0.35
- RREI.CA: score=6.34 buy_ready=False sector_rank=14 price=4.21 support=4.2 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=40.62 liquidity=2049768.88 spike=0.11
- RTVC.CA: score=-0.33 buy_ready=False sector_rank=14 price=3.86 support=3.79 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=27.69 liquidity=376152.84 spike=0.08
- RUBX.CA: score=21.11 buy_ready=False sector_rank=14 price=14.45 support=12.42 resistance=17.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=66.71 liquidity=73395880.0 spike=1.91
- SAUD.CA: score=23.4 buy_ready=False sector_rank=6 price=25.0 support=22.7 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=65.55 liquidity=10542134.0 spike=0.58
- SCEM.CA: score=8.42 buy_ready=False sector_rank=21 price=87.5 support=87.02 resistance=105.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=21.91 liquidity=32621226.0 spike=0.29
- SCFM.CA: score=-0.07 buy_ready=False sector_rank=14 price=271.25 support=250.2 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=34.9 liquidity=636829.63 spike=0.08
- SCTS.CA: score=1.98 buy_ready=False sector_rank=8 price=581.77 support=566.66 resistance=640.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=22.63 liquidity=1191899.0 spike=0.41
- SDTI.CA: score=16.29 buy_ready=False sector_rank=14 price=79.21 support=67.0 resistance=79.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=75.63 liquidity=24878994.0 spike=0.96
- SEIG.CA: score=5.92 buy_ready=False sector_rank=14 price=240.38 support=228.13 resistance=274.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=29.74 liquidity=3990148.5 spike=2.32
- SIPC.CA: score=17.29 buy_ready=False sector_rank=14 price=5.49 support=4.1 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=56.94 liquidity=26489202.0 spike=0.38
- SKPC.CA: score=18.71 buy_ready=False sector_rank=9 price=18.0 support=17.0 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=52.39 liquidity=30238474.0 spike=0.23
- SMFR.CA: score=0.62 buy_ready=False sector_rank=14 price=233.19 support=226.1 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=26.93 liquidity=1323708.88 spike=0.16
- SNFC.CA: score=18.29 buy_ready=False sector_rank=14 price=11.46 support=10.26 resistance=11.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=79.25 liquidity=10353890.0 spike=0.66
- SPIN.CA: score=1.53 buy_ready=False sector_rank=12 price=17.25 support=16.1 resistance=20.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=24.6 liquidity=1934203.75 spike=0.14
- SPMD.CA: score=14.29 buy_ready=False sector_rank=14 price=0.41 support=0.41 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=47.24 liquidity=10564149.0 spike=0.14
- SUGR.CA: score=10.65 buy_ready=False sector_rank=15 price=57.99 support=55.06 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=53.46 liquidity=3420276.5 spike=0.05
- SVCE.CA: score=17.29 buy_ready=False sector_rank=14 price=11.45 support=9.6 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=35.71 liquidity=47071968.0 spike=0.24
- SWDY.CA: score=14.81 buy_ready=False sector_rank=13 price=125.71 support=122.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=46.17 liquidity=7441393.0 spike=0.11
- TALM.CA: score=20.79 buy_ready=False sector_rank=8 price=20.82 support=17.11 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=67.79 liquidity=27220526.0 spike=0.41
- TMGH.CA: score=13.95 buy_ready=False sector_rank=17 price=94.19 support=93.08 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=37.73 liquidity=89166472.0 spike=0.31
- TRTO.CA: score=7.83 buy_ready=False sector_rank=14 price=0.06 support=0.05 resistance=0.08 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=48.39 liquidity=35016.92 spike=1.25
- UEFM.CA: score=0.49 buy_ready=False sector_rank=14 price=480.61 support=440.66 resistance=574.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=32.59 liquidity=2193415.5 spike=0.73
- UEGC.CA: score=16.29 buy_ready=False sector_rank=14 price=1.72 support=1.66 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=51.06 liquidity=32981912.0 spike=0.65
- UNIP.CA: score=10.24 buy_ready=False sector_rank=14 price=0.37 support=0.37 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=5951923.0 spike=0.25
- UNIT.CA: score=4.82 buy_ready=False sector_rank=17 price=17.94 support=17.12 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=47.79 liquidity=870635.56 spike=0.06
- WCDF.CA: score=10.68 buy_ready=False sector_rank=14 price=710.09 support=636.31 resistance=796.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=67.72 liquidity=1384659.5 spike=0.27
- WKOL.CA: score=10.06 buy_ready=False sector_rank=14 price=334.85 support=325.0 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=45.17 liquidity=2765896.75 spike=0.19
- ZEOT.CA: score=8.42 buy_ready=False sector_rank=14 price=13.21 support=13.03 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=37.68 liquidity=1125474.88 spike=0.17
- ZMID.CA: score=16.95 buy_ready=False sector_rank=17 price=8.37 support=7.9 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=39.56 liquidity=43099392.0 spike=0.2

## Backtesting Lite
- GBCO.CA: 180d return=17.08%, max drawdown=-24.35%, MA20>MA50 days last20=0, as_of=2026-09-20T21:00:00+00:00
- ATQA.CA: 180d return=33.43%, max drawdown=-21.44%, MA20>MA50 days last20=20, as_of=2026-09-20T21:00:00+00:00
- SAUD.CA: 180d return=76.09%, max drawdown=-19.12%, MA20>MA50 days last20=20, as_of=2026-09-20T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- ATQA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr National Steel Ataqa summary=Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- SAUD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=629 sources=3 expected=Al Baraka Bank Egypt summary=Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26; Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE; Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025
  - Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26: https://english.mubasher.info/news/4611927/Al-Baraka-Bank-Egypt-records-EGP-2-2bn-operating-income-in-Q1-26/
  - Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE: https://english.mubasher.info/news/4583822/Al-Baraka-Bank-Egypt-files-MTO-to-acquire-majority-stake-in-A-T-LEASE/
  - Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025: https://english.mubasher.info/news/4583458/Al-Baraka-Bank-Egypt-to-pay-EGP-1-1-share-dividends-for-2025/
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- EXPA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Export Development Bank of Egypt summary=Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- ABUK.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Qir Fertilizers summary=Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results; Abu Qir Fertilizers&#39; board approves $5.6m coated urea project; Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26
  - Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results: https://english.mubasher.info/news/4604919/Abu-Qir-Fertilizers-generates-EGP-5-6bn-net-profits-in-Q1-26-unaudited-results/
  - Abu Qir Fertilizers&#39; board approves $5.6m coated urea project: https://english.mubasher.info/news/4585599/Abu-Qir-Fertilizers-board-approves-5-6m-coated-urea-project/
  - Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26: https://english.mubasher.info/news/4554415/Abu-Qir-Fertilizers-profits-exceed-EGP-5-1bn-in-H1-25-26/
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=629 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/

## Warnings
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- Evidence for SAUD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
