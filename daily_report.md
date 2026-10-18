# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-10-18T16:04:45.356930+00:00
Generated Cairo: 2026-10-18 19:04
Run timing: target 15:30 Cairo | generated Cairo 2026-10-18 19:04 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-10-18 19:01

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 93/187
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, October 18
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 15.38% / above MA50 15.38%
- EGX70 regime: BEARISH / above MA20 4.76% / above MA50 23.81%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=685932032.0 spike=1.17 score=8.31
- ETEL.CA: liquidity=271794944.0 spike=1.02 score=24.03
- EGAL.CA: liquidity=241426144.0 spike=3.84 score=9.15
- COMI.CA: liquidity=199767856.0 spike=0.36 score=12.99
- UEGC.CA: liquidity=177150128.0 spike=4.2 score=9.57

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are both BEARISH with sector breadth at 0%, triggering a DEFENSIVE_NO_NEW_BUY risk mode; the scanner therefore flags tickets for watch‑list only, prioritizing them by rank_score, outlook, liquidity regime and sector strength while acknowledging uncertainty.
- EFIH.CA (Fintech & Payments) and ETEL.CA (Telecom) top the list due to high rank scores, BULLISH_WATCH outlooks, TRADEABLE liquidity and leading sector ranks, but the bearish index backdrop keeps them on hold.
- INFI.CA shows an ACCUMULATION_SPIKE liquidity burst yet trades far above its 20‑day support and sits below the 50‑day MA, signaling uncertain short‑term momentum.
- ARAB.CA and RUBX.CA display elevated RSI or cooling liquidity spikes, suggesting possible overextension and heightened volatility despite constructive outlooks.
- Overall, the defensive market regime means no new BUYs are allowed; tickets are monitored for any shift in trend, liquidity or sector leadership before action.

## Top Liquidity Spikes
- INFI.CA: spike=4.8 liquidity=76361696.0 outlook=CONSTRUCTIVE score=62.43 buy_ready=False
- SEIG.CA: spike=4.26 liquidity=7315332.0 outlook=WEAK_OR_RISKY score=28.43 buy_ready=False
- UEGC.CA: spike=4.2 liquidity=177150128.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EGAL.CA: spike=3.84 liquidity=241426144.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ORWE.CA: spike=3.79 liquidity=157041888.0 outlook=NEUTRAL score=48.36 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=4.97 5d=-1.22% 20d=4.32% aboveMA50=50.0%
- #2 Fintech & Payments: score=3.37 5d=-2.47% 20d=2.06% aboveMA50=50.0%
- #3 Transportation & Logistics: score=2.9 5d=-0.55% 20d=4.02% aboveMA50=50.0%
- #4 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #5 General / Verified EGX Expansion: score=1.43 5d=0.0% 20d=0.0% aboveMA50=7.84%
- #6 Textiles: score=1.36 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #7 Real Estate: score=1.33 5d=0.0% 20d=0.0% aboveMA50=7.69%
- #8 Energy & Petrochemicals: score=1.21 5d=-1.46% 20d=0.22% aboveMA50=33.33%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ETEL.CA: BULLISH_WATCH score=95.97 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- EFIH.CA: BULLISH_WATCH score=83.37 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- SUGR.CA: BULLISH_WATCH score=76 liquidity=TRADEABLE sector=LAGGING risk=sector is not leading
- ALCN.CA: BULLISH_WATCH score=70.9 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20
- CPCI.CA: CONSTRUCTIVE score=68.43 liquidity=TRADEABLE sector=IMPROVING risk=overheated RSI
- SDTI.CA: CONSTRUCTIVE score=63.43 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended
- INFI.CA: CONSTRUCTIVE score=62.43 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA50; far above support
- ARAB.CA: CONSTRUCTIVE score=62.33 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=overheated RSI; far above support
- RUBX.CA: CONSTRUCTIVE score=61.43 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; far above support; high short-term volatility
- SCEM.CA: CONSTRUCTIVE score=60.84 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA50; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=5.79 buy_ready=False sector_rank=5 price=214.91 support=214.0 resistance=250.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28721594.0 spike=1.61
- ABUK.CA: score=14.15 buy_ready=False sector_rank=14 price=83.43 support=83.0 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.33 liquidity=84497304.0 spike=0.91
- ACAMD.CA: score=18.59 buy_ready=False sector_rank=5 price=2.07 support=1.87 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=67.86 liquidity=46967404.0 spike=1.01
- ACGC.CA: score=12.42 buy_ready=False sector_rank=6 price=12.91 support=12.81 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.2 liquidity=7872304.0 spike=0.62
- ADCI.CA: score=0.31 buy_ready=False sector_rank=5 price=257.35 support=250.06 resistance=288.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=33.73 liquidity=733862.63 spike=0.36
- ADIB.CA: score=3.99 buy_ready=False sector_rank=15 price=44.59 support=44.53 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=47698088.0 spike=0.61
- ADPC.CA: score=1.43 buy_ready=False sector_rank=5 price=3.06 support=3.03 resistance=3.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6859905.5 spike=0.46
- AFDI.CA: score=-1.56 buy_ready=False sector_rank=5 price=46.98 support=45.6 resistance=50.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3869060.5 spike=0.64
- AFMC.CA: score=1.21 buy_ready=False sector_rank=5 price=121.69 support=120.1 resistance=132.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6635684.5 spike=0.33
- AJWA.CA: score=18.83 buy_ready=False sector_rank=5 price=218.62 support=176.0 resistance=227.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=89.12 liquidity=33836896.0 spike=1.13
- ALCN.CA: score=18.14 buy_ready=False sector_rank=3 price=32.33 support=30.7 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.2 liquidity=8981755.0 spike=0.26
- ALUM.CA: score=-2.38 buy_ready=False sector_rank=5 price=19.32 support=19.26 resistance=21.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3043887.5 spike=0.66
- AMER.CA: score=4.53 buy_ready=False sector_rank=7 price=4.15 support=4.1 resistance=4.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37289504.0 spike=0.76
- AMES.CA: score=4.57 buy_ready=False sector_rank=5 price=35.28 support=35.1 resistance=38.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=44885788.0 spike=0.55
- AMIA.CA: score=2.28 buy_ready=False sector_rank=5 price=17.33 support=17.3 resistance=19.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7703415.5 spike=0.42
- AMOC.CA: score=17.48 buy_ready=False sector_rank=8 price=13.05 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.0 liquidity=59597356.0 spike=0.48
- APSW.CA: score=4.27 buy_ready=False sector_rank=5 price=7.97 support=7.81 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=44.57 liquidity=659303.38 spike=1.02
- ARAB.CA: score=20.81 buy_ready=False sector_rank=7 price=0.26 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.55 liquidity=162127520.0 spike=1.64
- ARCC.CA: score=14.34 buy_ready=False sector_rank=12 price=65.39 support=60.01 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.86 liquidity=25457438.0 spike=0.82
- AREH.CA: score=4.99 buy_ready=False sector_rank=5 price=1.11 support=1.1 resistance=1.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10100412.0 spike=1.21
- ASCM.CA: score=5.59 buy_ready=False sector_rank=5 price=46.59 support=45.5 resistance=50.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12819953.0 spike=1.51
- ASPI.CA: score=4.57 buy_ready=False sector_rank=5 price=0.31 support=0.31 resistance=0.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30673574.0 spike=0.99
- ATLC.CA: score=4.67 buy_ready=False sector_rank=11 price=4.92 support=4.84 resistance=5.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10666039.0 spike=1.11
- ATQA.CA: score=4.15 buy_ready=False sector_rank=14 price=10.8 support=10.72 resistance=11.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=44857592.0 spike=0.62
- AXPH.CA: score=3.53 buy_ready=False sector_rank=5 price=1327.83 support=1300.0 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=23.63 liquidity=3956011.25 spike=0.59
- BINV.CA: score=14.24 buy_ready=False sector_rank=21 price=58.18 support=52.11 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.37 liquidity=8271375.5 spike=0.4
- BIOC.CA: score=4.57 buy_ready=False sector_rank=5 price=273.58 support=268.0 resistance=305.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46497268.0 spike=0.46
- BTFH.CA: score=4.45 buy_ready=False sector_rank=11 price=2.6 support=2.59 resistance=2.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=95384760.0 spike=0.91
- CAED.CA: score=1.13 buy_ready=False sector_rank=5 price=96.95 support=95.02 resistance=107.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6559831.5 spike=0.8
- CANA.CA: score=8.99 buy_ready=False sector_rank=15 price=42.1 support=41.7 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=32.48 liquidity=19474934.0 spike=0.79
- CCAP.CA: score=8.31 buy_ready=False sector_rank=21 price=5.93 support=6.04 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=22.75 liquidity=685932032.0 spike=1.17
- CCRS.CA: score=1.87 buy_ready=False sector_rank=5 price=1.83 support=1.83 resistance=2.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7297554.0 spike=0.63
- CEFM.CA: score=5.55 buy_ready=False sector_rank=5 price=124.09 support=113.0 resistance=152.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=38.49 liquidity=982211.69 spike=0.37
- CERA.CA: score=13.57 buy_ready=False sector_rank=5 price=1.22 support=1.18 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.05 liquidity=82971264.0 spike=0.67
- CFGH.CA: score=-1.34 buy_ready=False sector_rank=5 price=0.11 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=9.09 liquidity=6303.18 spike=1.04
- CICH.CA: score=1.13 buy_ready=False sector_rank=11 price=10.51 support=10.6 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=2685643.75 spike=0.75
- CIEB.CA: score=10.41 buy_ready=False sector_rank=15 price=22.11 support=22.56 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.01 liquidity=7422032.0 spike=0.76
- CIRA.CA: score=3.68 buy_ready=False sector_rank=18 price=35.4 support=35.01 resistance=37.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11268573.0 spike=0.49
- CLHO.CA: score=8.45 buy_ready=False sector_rank=10 price=13.57 support=13.51 resistance=16.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.5 liquidity=32273480.0 spike=0.73
- CNFN.CA: score=1.28 buy_ready=False sector_rank=11 price=3.89 support=3.86 resistance=4.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6831119.0 spike=0.74
- COMI.CA: score=12.99 buy_ready=False sector_rank=15 price=123.16 support=120.0 resistance=134.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.38 liquidity=199767856.0 spike=0.36
- COPR.CA: score=4.57 buy_ready=False sector_rank=5 price=0.43 support=0.41 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13596310.0 spike=0.63
- COSG.CA: score=4.57 buy_ready=False sector_rank=5 price=1.37 support=1.36 resistance=1.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11078329.0 spike=0.73
- CPCI.CA: score=13.84 buy_ready=False sector_rank=5 price=587.68 support=532.24 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.64 liquidity=4908541.5 spike=1.18
- CSAG.CA: score=12.17 buy_ready=False sector_rank=3 price=34.79 support=34.06 resistance=39.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=6006790.0 spike=0.83
- DAPH.CA: score=4.57 buy_ready=False sector_rank=5 price=85.85 support=85.3 resistance=93.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20508546.0 spike=0.49
- DEIN.CA: score=7.57 buy_ready=False sector_rank=5 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 09:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37.26 spike=0.01
- DOMT.CA: score=0.14 buy_ready=False sector_rank=17 price=23.49 support=22.85 resistance=27.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=31.95 liquidity=2406455.5 spike=0.55
- DSCW.CA: score=4.57 buy_ready=False sector_rank=5 price=1.46 support=1.45 resistance=1.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17116186.0 spike=0.97
- DTPP.CA: score=4.57 buy_ready=False sector_rank=5 price=244.19 support=241.11 resistance=265.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33252850.0 spike=0.53
- EALR.CA: score=3.69 buy_ready=False sector_rank=5 price=291.19 support=290.17 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=30.09 liquidity=5115323.5 spike=0.67
- EASB.CA: score=-2.1 buy_ready=False sector_rank=5 price=6.17 support=6.11 resistance=6.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3325657.0 spike=0.64
- EAST.CA: score=14.74 buy_ready=False sector_rank=17 price=28.16 support=27.01 resistance=33.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=35.52 liquidity=16999276.0 spike=0.38
- EBSC.CA: score=-2.16 buy_ready=False sector_rank=5 price=1.49 support=1.45 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2827619.25 spike=1.22
- ECAP.CA: score=1.56 buy_ready=False sector_rank=5 price=27.46 support=27.5 resistance=32.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.3 liquidity=2990586.5 spike=0.71
- EDFM.CA: score=5.34 buy_ready=False sector_rank=5 price=388.4 support=335.2 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=48.78 liquidity=764748.63 spike=0.65
- EEII.CA: score=-0.74 buy_ready=False sector_rank=5 price=1.8 support=1.78 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4685894.0 spike=0.52
- EFIC.CA: score=8.15 buy_ready=False sector_rank=14 price=148.87 support=147.0 resistance=199.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=30.02 liquidity=19605164.0 spike=0.58
- EFID.CA: score=15.56 buy_ready=False sector_rank=17 price=18.42 support=18.07 resistance=31.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.89 liquidity=66999204.0 spike=1.41
- EFIH.CA: score=24.35 buy_ready=False sector_rank=2 price=23.71 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=59.32 liquidity=45812584.0 spike=0.68
- EGAL.CA: score=9.15 buy_ready=False sector_rank=14 price=281.31 support=280.0 resistance=305.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=241426144.0 spike=3.84
- EGAS.CA: score=0.46 buy_ready=False sector_rank=8 price=50.01 support=50.0 resistance=53.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5973320.5 spike=0.53
- EGBE.CA: score=4.1 buy_ready=False sector_rank=15 price=0.5 support=0.5 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=108000.55 spike=0.79
- EGCH.CA: score=4.47 buy_ready=False sector_rank=14 price=11.01 support=10.85 resistance=12.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=93405392.0 spike=1.16
- EGSA.CA: score=4.22 buy_ready=False sector_rank=1 price=8.76 support=8.8 resistance=9.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=25.64 liquidity=8549.79 spike=1.11
- EGTS.CA: score=4.53 buy_ready=False sector_rank=7 price=12.8 support=12.62 resistance=14.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20474710.0 spike=0.58
- EHDR.CA: score=4.09 buy_ready=False sector_rank=5 price=2.09 support=2.07 resistance=2.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9520212.0 spike=0.9
- ELEC.CA: score=4.48 buy_ready=False sector_rank=9 price=1.62 support=1.6 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35550344.0 spike=0.7
- ELKA.CA: score=5.73 buy_ready=False sector_rank=5 price=1.45 support=1.44 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20437850.0 spike=1.58
- ELNA.CA: score=7.21 buy_ready=False sector_rank=5 price=35.22 support=33.46 resistance=36.4 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=281266.93 spike=1.68
- ELSH.CA: score=4.41 buy_ready=False sector_rank=5 price=10.45 support=10.35 resistance=11.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9833967.0 spike=0.47
- ELWA.CA: score=8.68 buy_ready=False sector_rank=5 price=1.65 support=1.43 resistance=1.74 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=54.05 liquidity=110069.85 spike=0.24
- EMFD.CA: score=14.53 buy_ready=False sector_rank=7 price=11.73 support=11.7 resistance=14.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.01 liquidity=32202504.0 spike=0.51
- ENGC.CA: score=0.21 buy_ready=False sector_rank=5 price=31.63 support=31.2 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5634225.0 spike=0.31
- EOSB.CA: score=9.57 buy_ready=False sector_rank=5 price=1.57 support=1.64 resistance=1.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=15 October 12:37 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=401.8 spike=0.01
- EPCO.CA: score=-2.86 buy_ready=False sector_rank=5 price=8.18 support=8.11 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2572070.25 spike=0.51
- EPPK.CA: score=-5.01 buy_ready=False sector_rank=5 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=24.03 buy_ready=False sector_rank=1 price=140.92 support=128.52 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.77 liquidity=271794944.0 spike=1.02
- ETRS.CA: score=8.29 buy_ready=False sector_rank=5 price=10.1 support=9.82 resistance=11.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=52.1 liquidity=3713630.5 spike=0.36
- EXPA.CA: score=7.99 buy_ready=False sector_rank=15 price=14.27 support=14.0 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=10.28 liquidity=35973748.0 spike=0.95
- FAIT.CA: score=6.06 buy_ready=False sector_rank=15 price=42.88 support=38.48 resistance=47.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.34 liquidity=2071746.13 spike=0.69
- FAITA.CA: score=11.36 buy_ready=False sector_rank=15 price=1.0 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=58.75 liquidity=47263.14 spike=1.16
- FERC.CA: score=-3.29 buy_ready=False sector_rank=14 price=65.37 support=64.01 resistance=70.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2557246.5 spike=0.47
- FWRY.CA: score=18.35 buy_ready=False sector_rank=2 price=18.2 support=17.5 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.59 liquidity=66754256.0 spike=0.59
- GBCO.CA: score=4.34 buy_ready=False sector_rank=16 price=29.0 support=28.7 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=127571112.0 spike=1.19
- GDWA.CA: score=8.57 buy_ready=False sector_rank=5 price=0.6 support=0.6 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.29 liquidity=15035988.0 spike=0.75
- GGCC.CA: score=7.33 buy_ready=False sector_rank=5 price=0.62 support=0.62 resistance=0.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36249216.0 spike=2.38
- GIHD.CA: score=1.62 buy_ready=False sector_rank=5 price=48.73 support=48.48 resistance=53.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7051132.5 spike=0.37
- GMCI.CA: score=5.94 buy_ready=False sector_rank=5 price=1.54 support=1.49 resistance=1.78 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=36.21 liquidity=371782.17 spike=0.95
- GRCA.CA: score=-2.33 buy_ready=False sector_rank=5 price=29.44 support=29.0 resistance=33.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3099296.75 spike=0.36
- GSSC.CA: score=7.26 buy_ready=False sector_rank=5 price=266.97 support=246.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.19 liquidity=2688614.75 spike=0.89
- GTWL.CA: score=4.57 buy_ready=False sector_rank=5 price=117.85 support=116.5 resistance=129.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=96181368.0 spike=0.59
- HDBK.CA: score=4.07 buy_ready=False sector_rank=15 price=96.47 support=96.1 resistance=101.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24841826.0 spike=1.04
- HELI.CA: score=4.53 buy_ready=False sector_rank=7 price=6.82 support=6.8 resistance=7.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51387332.0 spike=0.53
- HRHO.CA: score=4.45 buy_ready=False sector_rank=11 price=24.5 support=24.03 resistance=25.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=68910600.0 spike=0.51
- ICID.CA: score=-0.41 buy_ready=False sector_rank=5 price=16.6 support=16.3 resistance=17.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5022170.0 spike=0.61
- IDRE.CA: score=-1.89 buy_ready=False sector_rank=5 price=40.27 support=40.17 resistance=43.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3540069.75 spike=0.27
- IFAP.CA: score=2.65 buy_ready=False sector_rank=19 price=18.06 support=17.17 resistance=21.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=27.7 liquidity=5006946.0 spike=0.71
- INFI.CA: score=23.57 buy_ready=False sector_rank=5 price=125.29 support=104.0 resistance=142.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.24 liquidity=76361696.0 spike=4.8
- IRON.CA: score=14.23 buy_ready=False sector_rank=14 price=25.1 support=25.01 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.3 liquidity=16031611.0 spike=1.54
- ISMA.CA: score=-1.61 buy_ready=False sector_rank=5 price=20.24 support=20.05 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3822548.75 spike=0.51
- ISMQ.CA: score=4.15 buy_ready=False sector_rank=14 price=7.09 support=7.07 resistance=7.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13414005.0 spike=0.7
- ISPH.CA: score=4.45 buy_ready=False sector_rank=10 price=10.6 support=10.54 resistance=11.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24529054.0 spike=0.45
- JUFO.CA: score=13.24 buy_ready=False sector_rank=17 price=23.31 support=23.5 resistance=27.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.62 liquidity=21466544.0 spike=1.25
- KABO.CA: score=4.54 buy_ready=False sector_rank=6 price=7.0 support=6.91 resistance=8.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16609038.0 spike=0.73
- KWIN.CA: score=-2.7 buy_ready=False sector_rank=5 price=62.21 support=61.03 resistance=66.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2725405.75 spike=0.31
- KZPC.CA: score=14.0 buy_ready=False sector_rank=5 price=12.87 support=12.15 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.59 liquidity=6431946.5 spike=0.72
- LCSW.CA: score=16.34 buy_ready=False sector_rank=12 price=32.59 support=28.86 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=61.67 liquidity=11815458.0 spike=0.58
- LUTS.CA: score=4.57 buy_ready=False sector_rank=5 price=0.66 support=0.66 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=44938232.0 spike=0.8
- MAAL.CA: score=4.57 buy_ready=False sector_rank=5 price=7.49 support=7.38 resistance=8.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15402566.0 spike=0.61
- MASR.CA: score=14.57 buy_ready=False sector_rank=5 price=7.11 support=6.82 resistance=7.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.19 liquidity=35982516.0 spike=0.64
- MBSC.CA: score=16.34 buy_ready=False sector_rank=12 price=333.17 support=288.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=85437856.0 spike=1.0
- MCQE.CA: score=4.96 buy_ready=False sector_rank=12 price=160.5 support=160.0 resistance=184.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=72788400.0 spike=1.31
- MCRO.CA: score=5.31 buy_ready=False sector_rank=5 price=1.27 support=1.26 resistance=1.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=74564336.0 spike=1.37
- MENA.CA: score=4.21 buy_ready=False sector_rank=7 price=5.7 support=5.57 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=35.53 liquidity=678314.75 spike=0.4
- MEPA.CA: score=0.28 buy_ready=False sector_rank=5 price=1.51 support=1.49 resistance=1.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5709098.0 spike=0.59
- MFPC.CA: score=14.15 buy_ready=False sector_rank=14 price=42.22 support=42.0 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.35 liquidity=56975684.0 spike=0.68
- MFSC.CA: score=-0.71 buy_ready=False sector_rank=5 price=37.44 support=36.25 resistance=49.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=18.42 liquidity=719102.38 spike=0.31
- MHOT.CA: score=5.25 buy_ready=False sector_rank=20 price=15.68 support=15.08 resistance=19.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=30.38 liquidity=7818686.0 spike=0.44
- MICH.CA: score=1.62 buy_ready=False sector_rank=5 price=38.23 support=38.0 resistance=41.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7043494.0 spike=0.81
- MILS.CA: score=-0.48 buy_ready=False sector_rank=5 price=142.31 support=141.0 resistance=158.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4950633.0 spike=0.62
- MIPH.CA: score=8.09 buy_ready=False sector_rank=10 price=750.0 support=686.2 resistance=798.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23748730.0 spike=2.82
- MOED.CA: score=4.57 buy_ready=False sector_rank=5 price=0.57 support=0.57 resistance=0.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11452479.0 spike=0.69
- MOIL.CA: score=-0.37 buy_ready=False sector_rank=8 price=0.66 support=0.63 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=31.08 liquidity=143465.52 spike=0.5
- MOIN.CA: score=3.21 buy_ready=False sector_rank=5 price=29.17 support=28.8 resistance=31.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8642349.0 spike=0.82
- MOSC.CA: score=-3.95 buy_ready=False sector_rank=5 price=250.22 support=245.02 resistance=269.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1480708.25 spike=0.38
- MPCI.CA: score=4.57 buy_ready=False sector_rank=5 price=299.66 support=296.0 resistance=326.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=93928912.0 spike=0.93
- MPCO.CA: score=3.65 buy_ready=False sector_rank=19 price=1.88 support=1.84 resistance=2.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=82562344.0 spike=0.65
- MPRC.CA: score=16.35 buy_ready=False sector_rank=5 price=34.62 support=34.53 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.94 liquidity=29822810.0 spike=1.89
- MTIE.CA: score=13.28 buy_ready=False sector_rank=16 price=7.34 support=7.27 resistance=8.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.85 liquidity=21284834.0 spike=1.16
- NAHO.CA: score=6.1 buy_ready=False sector_rank=5 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=50231.71 spike=1.74
- NCCW.CA: score=4.57 buy_ready=False sector_rank=5 price=5.47 support=5.41 resistance=5.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17381068.0 spike=0.44
- NEDA.CA: score=-0.37 buy_ready=False sector_rank=5 price=2.6 support=2.47 resistance=2.8 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=32.14 liquidity=59974.2 spike=0.09
- NHPS.CA: score=0.74 buy_ready=False sector_rank=5 price=61.75 support=61.18 resistance=66.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6168739.5 spike=0.42
- NINH.CA: score=4.57 buy_ready=False sector_rank=5 price=15.32 support=15.19 resistance=16.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10976955.0 spike=0.77
- NIPH.CA: score=4.45 buy_ready=False sector_rank=10 price=251.78 support=250.11 resistance=281.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=92872752.0 spike=0.77
- OBRI.CA: score=4.57 buy_ready=False sector_rank=5 price=25.4 support=24.85 resistance=27.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10446229.0 spike=0.73
- OCDI.CA: score=4.53 buy_ready=False sector_rank=7 price=24.05 support=24.0 resistance=25.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=34530612.0 spike=0.81
- OCPH.CA: score=0.11 buy_ready=False sector_rank=5 price=191.92 support=190.0 resistance=247.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.95 liquidity=1538114.25 spike=0.45
- ODIN.CA: score=-0.45 buy_ready=False sector_rank=5 price=2.06 support=2.05 resistance=2.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4975415.0 spike=0.58
- OFH.CA: score=4.57 buy_ready=False sector_rank=5 price=0.73 support=0.73 resistance=0.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16737655.0 spike=0.18
- OIH.CA: score=7.97 buy_ready=False sector_rank=21 price=1.78 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=41450688.0 spike=0.5
- OLFI.CA: score=1.37 buy_ready=False sector_rank=17 price=20.19 support=19.8 resistance=23.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.92 liquidity=3633809.75 spike=0.22
- ORAS.CA: score=4.6 buy_ready=False sector_rank=4 price=861.03 support=850.0 resistance=893.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=147702720.0 spike=1.0
- ORHD.CA: score=4.85 buy_ready=False sector_rank=7 price=10.1 support=10.06 resistance=10.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=174557024.0 spike=1.16
- ORWE.CA: score=19.54 buy_ready=False sector_rank=6 price=26.42 support=26.01 resistance=28.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.11 liquidity=157041888.0 spike=3.79
- PHAR.CA: score=4.45 buy_ready=False sector_rank=10 price=101.87 support=101.5 resistance=107.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36643132.0 spike=0.56
- PHDC.CA: score=16.53 buy_ready=False sector_rank=7 price=12.54 support=12.35 resistance=13.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=35.62 liquidity=51999792.0 spike=0.54
- PHTV.CA: score=5.05 buy_ready=False sector_rank=5 price=338.3 support=315.0 resistance=377.96 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=41.91 liquidity=474634.88 spike=0.55
- POUL.CA: score=7.74 buy_ready=False sector_rank=17 price=9.8 support=9.12 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=3.27 liquidity=19268946.0 spike=0.61
- PRCL.CA: score=-1.08 buy_ready=False sector_rank=12 price=20.13 support=20.01 resistance=22.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4585148.0 spike=0.42
- PRDC.CA: score=4.53 buy_ready=False sector_rank=7 price=6.01 support=5.91 resistance=6.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22308792.0 spike=0.62
- PRMH.CA: score=-3.21 buy_ready=False sector_rank=5 price=1.85 support=1.84 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2219444.0 spike=0.56
- RACC.CA: score=0.46 buy_ready=False sector_rank=5 price=8.15 support=8.14 resistance=9.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5886575.0 spike=0.9
- RAKT.CA: score=3.88 buy_ready=False sector_rank=5 price=22.06 support=20.26 resistance=25.08 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=49.81 liquidity=308795.87 spike=0.87
- RAYA.CA: score=4.28 buy_ready=False sector_rank=13 price=5.66 support=5.61 resistance=6.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16893584.0 spike=0.47
- RMDA.CA: score=10.27 buy_ready=False sector_rank=10 price=4.91 support=4.83 resistance=6.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.97 liquidity=36742876.0 spike=1.41
- ROTO.CA: score=12.39 buy_ready=False sector_rank=5 price=35.9 support=35.56 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.3 liquidity=8754100.0 spike=1.03
- RREI.CA: score=-1.93 buy_ready=False sector_rank=5 price=3.33 support=3.3 resistance=3.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3498956.5 spike=0.38
- RTVC.CA: score=1.34 buy_ready=False sector_rank=5 price=3.26 support=3.31 resistance=4.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.37 liquidity=2748278.0 spike=1.01
- RUBX.CA: score=19.57 buy_ready=False sector_rank=5 price=16.03 support=12.9 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.48 liquidity=71915776.0 spike=0.7
- SAUD.CA: score=14.19 buy_ready=False sector_rank=15 price=21.0 support=20.2 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=39.87 liquidity=23051746.0 spike=1.1
- SCEM.CA: score=19.38 buy_ready=False sector_rank=12 price=85.66 support=74.55 resistance=95.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=57.0 liquidity=97072592.0 spike=1.52
- SCFM.CA: score=-0.83 buy_ready=False sector_rank=5 price=227.39 support=220.35 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=33.98 liquidity=600446.38 spike=0.33
- SCTS.CA: score=-1.79 buy_ready=False sector_rank=18 price=471.56 support=463.13 resistance=615.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=24.24 liquidity=521016.88 spike=0.53
- SDTI.CA: score=19.57 buy_ready=False sector_rank=5 price=83.47 support=73.3 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=63.73 liquidity=11892879.0 spike=0.35
- SEIG.CA: score=11.89 buy_ready=False sector_rank=5 price=199.11 support=173.1 resistance=259.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.17 liquidity=7315332.0 spike=4.26
- SIPC.CA: score=4.57 buy_ready=False sector_rank=5 price=5.29 support=5.23 resistance=5.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42502208.0 spike=0.8
- SKPC.CA: score=8.15 buy_ready=False sector_rank=14 price=14.82 support=14.98 resistance=18.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=24.66 liquidity=36716952.0 spike=0.47
- SMFR.CA: score=5.49 buy_ready=False sector_rank=5 price=193.82 support=181.6 resistance=255.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.5 liquidity=1913141.75 spike=0.53
- SNFC.CA: score=11.98 buy_ready=False sector_rank=5 price=11.13 support=10.81 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.25 liquidity=4412424.5 spike=0.39
- SPIN.CA: score=0.47 buy_ready=False sector_rank=6 price=14.14 support=14.06 resistance=14.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5761468.5 spike=1.08
- SPMD.CA: score=8.57 buy_ready=False sector_rank=5 price=0.35 support=0.34 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.82 liquidity=13518593.0 spike=0.63
- SUGR.CA: score=21.34 buy_ready=False sector_rank=17 price=55.74 support=50.5 resistance=61.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=53.51 liquidity=13460259.0 spike=1.3
- SVCE.CA: score=8.57 buy_ready=False sector_rank=5 price=8.9 support=8.81 resistance=12.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.55 liquidity=56928764.0 spike=0.69
- SWDY.CA: score=4.48 buy_ready=False sector_rank=9 price=105.76 support=104.5 resistance=112.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=53982976.0 spike=0.9
- TALM.CA: score=16.68 buy_ready=False sector_rank=18 price=20.1 support=18.71 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.34 liquidity=16257889.0 spike=0.42
- TMGH.CA: score=8.53 buy_ready=False sector_rank=7 price=82.74 support=81.22 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.82 liquidity=121740296.0 spike=0.54
- TRTO.CA: score=12.27 buy_ready=False sector_rank=5 price=0.07 support=0.05 resistance=0.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=13236.36 spike=1.34
- UEFM.CA: score=6.16 buy_ready=False sector_rank=5 price=475.07 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=54.34 liquidity=589941.0 spike=0.19
- UEGC.CA: score=9.57 buy_ready=False sector_rank=5 price=1.53 support=1.52 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=177150128.0 spike=4.2
- UNIP.CA: score=0.5 buy_ready=False sector_rank=5 price=0.3 support=0.3 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5923674.5 spike=0.62
- UNIT.CA: score=-3.56 buy_ready=False sector_rank=7 price=16.02 support=16.0 resistance=17.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1903841.25 spike=0.35
- WCDF.CA: score=-3.23 buy_ready=False sector_rank=5 price=511.84 support=506.1 resistance=539.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2201321.75 spike=0.7
- WKOL.CA: score=7.89 buy_ready=False sector_rank=5 price=266.65 support=266.18 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=27.55 liquidity=9315909.0 spike=0.92
- ZEOT.CA: score=2.21 buy_ready=False sector_rank=5 price=10.25 support=10.15 resistance=11.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7638270.5 spike=0.95
- ZMID.CA: score=6.01 buy_ready=False sector_rank=7 price=6.75 support=6.5 resistance=7.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=173686000.0 spike=1.74

## Backtesting Lite
- EFIH.CA: 180d return=22.76%, max drawdown=-22.68%, MA20>MA50 days last20=5, as_of=2026-10-14T21:00:00+00:00
- ETEL.CA: 180d return=117.39%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-10-14T21:00:00+00:00
- INFI.CA: 180d return=12.06%, max drawdown=-37.66%, MA20>MA50 days last20=8, as_of=2026-10-14T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- INFI.CA: status=RECENT_ACCEPTED latest=2026-01-01 age_days=290 sources=3 expected=Ismailia National Co. for Food Industries summary=Foodico stock targets higher levels; Foodico plans to log nearly EGP 70.5m profits in 2026; Foodico to secure EGP 12m loan from national bank
  - Foodico stock targets higher levels: https://english.mubasher.info/news/4564894/Foodico-stock-targets-higher-levels/
  - Foodico plans to log nearly EGP 70.5m profits in 2026: https://english.mubasher.info/news/4541309/Foodico-plans-to-log-nearly-EGP-70-5m-profits-in-2026/
  - Foodico to secure EGP 12m loan from national bank: https://english.mubasher.info/news/3888447/Foodico-to-secure-EGP-12m-loan-from-national-bank/
- SUGR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=655 sources=3 expected=Delta Sugar summary=Delta Sugar’s net profits fall 74% in Q1-26; Delta Sugar stock tests key resistance near EGP 50 amid downtrend; Delta Sugar turns to EGP 346m net losses in 2025
  - Delta Sugar’s net profits fall 74% in Q1-26: https://english.mubasher.info/news/4604921/Delta-Sugar-s-net-profits-fall-74-in-Q1-26/
  - Delta Sugar stock tests key resistance near EGP 50 amid downtrend: https://english.mubasher.info/news/4584932/Delta-Sugar-stock-tests-key-resistance-near-EGP-50-amid-downtrend/
  - Delta Sugar turns to EGP 346m net losses in 2025: https://english.mubasher.info/news/4557875/Delta-Sugar-turns-to-EGP-346m-net-losses-in-2025/
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- RUBX.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Rubex International for Plastic and Acrylic Manufacturing summary=Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- SDTI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=SHARM DREAMS Co. for Touristic Investment S.A.E summary=Sharm Dreams stock maintains strong uptrend - Analysis; Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis; Sharm Dreams stock hits historic level halting driving buying force
  - Sharm Dreams stock maintains strong uptrend - Analysis: https://english.mubasher.info/news/4577977/Sharm-Dreams-stock-maintains-strong-uptrend-Analysis/
  - Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis: https://english.mubasher.info/news/4547831/Sharm-Dreams-stock-is-experiencing-sideways-movement-amid-anticipation-of-next-trend-Analysis/
  - Sharm Dreams stock hits historic level halting driving buying force: https://english.mubasher.info/news/4529096/Sharm-Dreams-stock-hits-historic-level-halting-driving-buying-force/
- ORWE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=655 sources=3 expected=Oriental Weavers summary=Oriental Weavers to disburse EGP 1.5/shr dividends for 2025; Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025; Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25
  - Oriental Weavers to disburse EGP 1.5/shr dividends for 2025: https://english.mubasher.info/news/4590236/Oriental-Weavers-to-disburse-EGP-1-5-shr-dividends-for-2025/
  - Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025: https://english.mubasher.info/news/4562972/Oriental-Weavers-consolidated-profits-cross-EGP-2-2bn-in-2025/
  - Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25: https://english.mubasher.info/news/4487417/Oriental-Weavers-generates-EGP-12-5bn-consolidated-sales-in-H1-25/

## Warnings
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for SUGR.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Evidence for SDTI.CA matches the company but no source/report date was detected.
- Evidence for ORWE.CA matches the company but appears old; latest detected date is 2025-01-01.
