# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-10-22T11:47:15.707158+00:00
Generated Cairo: 2026-10-22 14:47
Run timing: target 09:15 Cairo | generated Cairo 2026-10-22 14:47 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-10-22 14:43

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 148/186
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, October 22
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 21.43% / above MA50 7.14%
- EGX70 regime: BEARISH / above MA20 2.78% / above MA50 8.33%
- Sector breadth: 4.76%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=648232832.0 spike=1.42 score=18.33
- ETEL.CA: liquidity=590606336.0 spike=2.64 score=12.39
- CCAP.CA: liquidity=580847040.0 spike=1.1 score=17.26
- TMGH.CA: liquidity=355078816.0 spike=1.42 score=15.32
- EGAL.CA: liquidity=191996304.0 spike=2.34 score=11.78

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- SCTS.CA: spike=23.09 liquidity=21837944.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ELNA.CA: spike=16.63 liquidity=2647890.0 outlook=BULLISH_WATCH score=85 buy_ready=False
- MFSC.CA: spike=5.93 liquidity=11233482.0 outlook=WEAK_OR_RISKY score=17 buy_ready=False
- PHTV.CA: spike=5.63 liquidity=4500461.5 outlook=NEUTRAL score=48 buy_ready=False
- EXPA.CA: spike=3.68 liquidity=125375296.0 outlook=WEAK_OR_RISKY score=23.23 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=5.28 5d=0.45% 20d=0.17% aboveMA50=50.0%
- #2 Fintech & Payments: score=1.59 5d=0.24% 20d=-1.16% aboveMA50=0.0%
- #3 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #4 Banking & Financials: score=1.23 5d=0.04% 20d=-6.16% aboveMA50=10.0%
- #5 Transportation & Logistics: score=0.85 5d=-0.77% 20d=-5.46% aboveMA50=50.0%
- #6 Food, Beverages & Tobacco: score=0.47 5d=1.08% 20d=-10.66% aboveMA50=0.0%
- #7 Tourism & Leisure: score=0.35 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #8 Basic Resources & Chemicals: score=0.24 5d=0.0% 20d=-6.77% aboveMA50=10.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ELNA.CA: BULLISH_WATCH score=85 liquidity=TRADEABLE sector=LAGGING risk=sector is not leading
- ABUK.CA: BULLISH_WATCH score=76.24 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- KZPC.CA: BULLISH_WATCH score=76 liquidity=TRADEABLE sector=LAGGING risk=sector is not leading
- CPCI.CA: CONSTRUCTIVE score=65 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- EAST.CA: CONSTRUCTIVE score=60.47 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA50
- ALCN.CA: CONSTRUCTIVE score=58.85 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; below MA20
- BINV.CA: CONSTRUCTIVE score=58.16 liquidity=TRADEABLE sector=IMPROVING risk=below MA20; sector is not leading
- CCAP.CA: CONSTRUCTIVE score=58.16 liquidity=TRADEABLE sector=IMPROVING risk=below MA20; sector is not leading
- AMOC.CA: CONSTRUCTIVE score=58 liquidity=TRADEABLE sector=LAGGING risk=below MA20; sector is not leading
- SNFC.CA: CONSTRUCTIVE score=58 liquidity=TRADEABLE sector=LAGGING risk=below MA20; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- DTPP.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=6.98 buy_ready=False sector_rank=14 price=224.0 support=201.0 resistance=309.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.04 liquidity=3496682.25 spike=0.34
- ABUK.CA: score=24.22 buy_ready=False sector_rank=8 price=93.14 support=80.5 resistance=95.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=64.47 liquidity=120219848.0 spike=1.56
- ACAMD.CA: score=14.48 buy_ready=False sector_rank=14 price=2.01 support=1.87 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=51.16 liquidity=28031408.0 spike=0.59
- ACGC.CA: score=8.48 buy_ready=False sector_rank=15 price=13.0 support=12.5 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=10188696.0 spike=0.92
- ADCI.CA: score=4.34 buy_ready=False sector_rank=14 price=254.67 support=241.55 resistance=288.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=43.36 liquidity=858687.56 spike=0.51
- ADIB.CA: score=14.83 buy_ready=False sector_rank=4 price=45.8 support=43.45 resistance=52.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=42.67 liquidity=84158424.0 spike=1.17
- ADPC.CA: score=7.22 buy_ready=False sector_rank=14 price=2.93 support=2.85 resistance=4.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.2 liquidity=9739717.0 spike=0.87
- AFDI.CA: score=-3.59 buy_ready=False sector_rank=14 price=43.15 support=43.0 resistance=47.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2928179.5 spike=0.66
- AFMC.CA: score=3.05 buy_ready=False sector_rank=14 price=117.38 support=115.5 resistance=123.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9566016.0 spike=0.52
- AJWA.CA: score=15.48 buy_ready=False sector_rank=14 price=214.23 support=176.0 resistance=229.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=79.73 liquidity=26644596.0 spike=0.77
- ALCN.CA: score=17.34 buy_ready=False sector_rank=5 price=32.77 support=30.19 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.75 liquidity=10304872.0 spike=0.45
- ALUM.CA: score=5.71 buy_ready=False sector_rank=14 price=19.98 support=18.01 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=3228490.5 spike=0.81
- AMER.CA: score=13.48 buy_ready=False sector_rank=16 price=4.07 support=3.8 resistance=5.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.51 liquidity=19194304.0 spike=0.37
- AMES.CA: score=9.48 buy_ready=False sector_rank=14 price=33.3 support=32.8 resistance=51.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.93 liquidity=25963742.0 spike=0.42
- AMIA.CA: score=6.11 buy_ready=False sector_rank=14 price=17.71 support=17.0 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=46.95 liquidity=2622788.25 spike=0.16
- AMOC.CA: score=17.16 buy_ready=False sector_rank=12 price=13.57 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=54.64 liquidity=136474528.0 spike=1.11
- APSW.CA: score=2.83 buy_ready=False sector_rank=14 price=7.78 support=7.72 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=343664.88 spike=0.58
- ARAB.CA: score=13.48 buy_ready=False sector_rank=16 price=0.25 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.07 liquidity=72708480.0 spike=0.67
- ARCC.CA: score=13.88 buy_ready=False sector_rank=13 price=65.47 support=60.01 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.0 liquidity=12313443.0 spike=0.28
- AREH.CA: score=8.94 buy_ready=False sector_rank=14 price=1.08 support=1.09 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.55 liquidity=6452061.5 spike=0.8
- ASCM.CA: score=1.43 buy_ready=False sector_rank=14 price=46.6 support=44.25 resistance=61.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=33.09 liquidity=3949153.0 spike=0.41
- ASPI.CA: score=12.48 buy_ready=False sector_rank=14 price=0.31 support=0.3 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.04 liquidity=14353845.0 spike=0.66
- ATLC.CA: score=14.62 buy_ready=False sector_rank=17 price=4.85 support=4.72 resistance=7.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.05 liquidity=14575240.0 spike=2.08
- ATQA.CA: score=4.1 buy_ready=False sector_rank=8 price=10.03 support=9.9 resistance=10.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=53964524.0 spike=0.96
- AXPH.CA: score=1.71 buy_ready=False sector_rank=14 price=1258.26 support=1200.12 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.27 liquidity=3227249.5 spike=0.52
- BINV.CA: score=17.3 buy_ready=False sector_rank=10 price=57.24 support=52.11 resistance=65.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.41 liquidity=15480145.0 spike=1.12
- BIOC.CA: score=8.48 buy_ready=False sector_rank=14 price=260.03 support=225.21 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.74 liquidity=30496478.0 spike=0.28
- BTFH.CA: score=12.46 buy_ready=False sector_rank=17 price=2.56 support=2.55 resistance=2.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.81 liquidity=93364816.0 spike=0.96
- CAED.CA: score=2.34 buy_ready=False sector_rank=14 price=84.09 support=83.0 resistance=92.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8694938.0 spike=1.08
- CANA.CA: score=14.49 buy_ready=False sector_rank=4 price=42.5 support=38.1 resistance=48.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=43.3 liquidity=11241271.0 spike=0.63
- CCAP.CA: score=17.26 buy_ready=False sector_rank=10 price=6.34 support=5.87 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.72 liquidity=580847040.0 spike=1.1
- CCRS.CA: score=-0.52 buy_ready=False sector_rank=14 price=1.89 support=1.89 resistance=2.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5993944.0 spike=0.86
- CEFM.CA: score=4.07 buy_ready=False sector_rank=14 price=126.71 support=113.0 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=44.37 liquidity=582342.25 spike=0.28
- CERA.CA: score=3.48 buy_ready=False sector_rank=14 price=1.14 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=100665896.0 spike=0.82
- CFGH.CA: score=-2.52 buy_ready=False sector_rank=14 price=0.11 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-20T21:00:00+00:00 freshness=FRESH RSI=16.67 liquidity=471.7 spike=0.09
- CICH.CA: score=4.44 buy_ready=False sector_rank=17 price=10.87 support=9.63 resistance=12.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.44 liquidity=1982273.88 spike=0.86
- CIEB.CA: score=12.29 buy_ready=False sector_rank=4 price=22.99 support=21.4 resistance=24.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.57 liquidity=8799241.0 spike=0.95
- CIRA.CA: score=12.95 buy_ready=False sector_rank=19 price=35.86 support=33.15 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.33 liquidity=11586533.0 spike=0.65
- CLHO.CA: score=6.74 buy_ready=False sector_rank=21 price=13.21 support=13.0 resistance=16.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.02 liquidity=28697684.0 spike=0.79
- CNFN.CA: score=15.86 buy_ready=False sector_rank=17 price=4.04 support=3.72 resistance=4.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.1 liquidity=15268077.0 spike=1.7
- COMI.CA: score=18.33 buy_ready=False sector_rank=4 price=125.98 support=120.0 resistance=132.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=58.36 liquidity=648232832.0 spike=1.42
- COPR.CA: score=3.48 buy_ready=False sector_rank=14 price=0.4 support=0.39 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11347753.0 spike=0.67
- COSG.CA: score=7.78 buy_ready=False sector_rank=14 price=1.32 support=1.29 resistance=1.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.06 liquidity=5295979.0 spike=0.41
- CPCI.CA: score=11.14 buy_ready=False sector_rank=14 price=590.26 support=502.25 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=56.95 liquidity=2660549.75 spike=0.58
- CSAG.CA: score=8.07 buy_ready=False sector_rank=5 price=34.79 support=33.68 resistance=38.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.41 liquidity=3725198.25 spike=0.55
- DAPH.CA: score=12.48 buy_ready=False sector_rank=14 price=81.0 support=82.0 resistance=114.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.46 liquidity=17659682.0 spike=0.41
- DEIN.CA: score=6.48 buy_ready=False sector_rank=14 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 09:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37.26 spike=0.01
- DOMT.CA: score=6.47 buy_ready=False sector_rank=6 price=22.78 support=22.5 resistance=26.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=42.06 liquidity=1285229.88 spike=0.34
- DSCW.CA: score=12.48 buy_ready=False sector_rank=14 price=1.49 support=1.45 resistance=1.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.78 liquidity=10717457.0 spike=0.67
- EALR.CA: score=4.73 buy_ready=False sector_rank=14 price=282.28 support=270.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.61 liquidity=2248300.5 spike=0.62
- EASB.CA: score=5.46 buy_ready=False sector_rank=14 price=6.28 support=5.6 resistance=8.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=44.42 liquidity=1974248.5 spike=0.37
- EAST.CA: score=19.27 buy_ready=False sector_rank=6 price=30.39 support=27.01 resistance=32.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=59.69 liquidity=83734296.0 spike=2.04
- EBSC.CA: score=3.87 buy_ready=False sector_rank=14 price=1.45 support=1.33 resistance=2.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=1387703.12 spike=0.67
- ECAP.CA: score=0.19 buy_ready=False sector_rank=14 price=27.14 support=25.7 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.38 liquidity=2703694.25 spike=0.73
- EDFM.CA: score=4.12 buy_ready=False sector_rank=14 price=383.81 support=335.2 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=50.02 liquidity=634617.19 spike=0.57
- EEII.CA: score=1.02 buy_ready=False sector_rank=14 price=1.72 support=1.71 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=29.23 liquidity=3535554.0 spike=0.44
- EFIC.CA: score=4.1 buy_ready=False sector_rank=8 price=149.23 support=148.23 resistance=159.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11229779.0 spike=0.38
- EFID.CA: score=15.19 buy_ready=False sector_rank=6 price=18.47 support=16.98 resistance=20.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.33 liquidity=23112648.0 spike=0.52
- EFIH.CA: score=6.84 buy_ready=False sector_rank=2 price=22.66 support=21.0 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=69038560.0 spike=1.1
- EGAL.CA: score=11.78 buy_ready=False sector_rank=8 price=303.5 support=275.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=33.11 liquidity=191996304.0 spike=2.34
- EGAS.CA: score=6.64 buy_ready=False sector_rank=12 price=49.41 support=47.0 resistance=60.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.3 liquidity=2708109.75 spike=0.37
- EGBE.CA: score=4.56 buy_ready=False sector_rank=4 price=0.5 support=0.5 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.84 liquidity=72096.33 spike=0.56
- EGCH.CA: score=8.1 buy_ready=False sector_rank=8 price=11.19 support=10.67 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.88 liquidity=44956688.0 spike=0.62
- EGSA.CA: score=16.11 buy_ready=False sector_rank=1 price=9.03 support=8.75 resistance=9.09 source=Yahoo Finance as_of=2026-10-20T21:00:00+00:00 freshness=FRESH RSI=66.07 liquidity=677.25 spike=0.12
- EGTS.CA: score=7.48 buy_ready=False sector_rank=16 price=12.58 support=12.06 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.63 liquidity=14827548.0 spike=0.5
- EHDR.CA: score=6.14 buy_ready=False sector_rank=14 price=2.14 support=2.07 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.62 liquidity=3655007.0 spike=0.35
- ELEC.CA: score=14.49 buy_ready=False sector_rank=18 price=1.61 support=1.55 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.31 liquidity=99556888.0 spike=2.12
- ELKA.CA: score=10.61 buy_ready=False sector_rank=14 price=1.43 support=1.38 resistance=1.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.25 liquidity=8124390.5 spike=0.62
- ELNA.CA: score=19.13 buy_ready=False sector_rank=14 price=36.98 support=33.46 resistance=35.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=2647890.0 spike=16.63
- ELSH.CA: score=9.82 buy_ready=False sector_rank=14 price=10.19 support=10.0 resistance=12.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.09 liquidity=6333460.5 spike=0.31
- ELWA.CA: score=2.49 buy_ready=False sector_rank=14 price=1.65 support=1.43 resistance=1.73 source=Yahoo Finance as_of=2026-10-20T21:00:00+00:00 freshness=FRESH RSI=90.48 liquidity=5243.7 spike=0.01
- EMFD.CA: score=9.64 buy_ready=False sector_rank=16 price=11.5 support=11.2 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=24.07 liquidity=92807984.0 spike=1.58
- ENGC.CA: score=6.94 buy_ready=False sector_rank=14 price=31.43 support=30.0 resistance=43.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.23 liquidity=4452845.0 spike=0.36
- EOSB.CA: score=5.48 buy_ready=False sector_rank=14 price=1.57 support=1.57 resistance=1.64 source=Yahoo Finance as_of=2026-10-20T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=277.89 spike=0.01
- EPCO.CA: score=-4.29 buy_ready=False sector_rank=14 price=8.24 support=8.23 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2224577.75 spike=0.51
- EPPK.CA: score=-6.1 buy_ready=False sector_rank=14 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=12.39 buy_ready=False sector_rank=1 price=131.15 support=128.6 resistance=140.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=590606336.0 spike=2.64
- ETRS.CA: score=9.63 buy_ready=False sector_rank=14 price=10.28 support=9.61 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=57.7 liquidity=4141041.75 spike=0.4
- EXPA.CA: score=13.49 buy_ready=False sector_rank=4 price=14.38 support=12.0 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.5 liquidity=125375296.0 spike=3.68
- FAIT.CA: score=8.94 buy_ready=False sector_rank=4 price=43.31 support=40.4 resistance=47.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=52.95 liquidity=3831500.5 spike=1.31
- FAITA.CA: score=11.52 buy_ready=False sector_rank=4 price=1.0 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=52.22 liquidity=25324.06 spike=0.73
- FERC.CA: score=0.55 buy_ready=False sector_rank=8 price=63.84 support=60.51 resistance=79.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=30.36 liquidity=2454392.25 spike=0.7
- FWRY.CA: score=16.04 buy_ready=False sector_rank=2 price=17.58 support=17.5 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=53.24 liquidity=133812800.0 spike=1.2
- GBCO.CA: score=5.68 buy_ready=False sector_rank=9 price=24.98 support=24.6 resistance=26.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=191349952.0 spike=1.8
- GDWA.CA: score=12.48 buy_ready=False sector_rank=14 price=0.58 support=0.57 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=11203244.0 spike=0.66
- GGCC.CA: score=3.48 buy_ready=False sector_rank=14 price=0.58 support=0.58 resistance=0.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12497218.0 spike=0.78
- GIHD.CA: score=1.74 buy_ready=False sector_rank=14 price=43.53 support=43.0 resistance=46.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8255735.0 spike=0.43
- GMCI.CA: score=4.68 buy_ready=False sector_rank=14 price=1.54 support=1.47 resistance=1.77 source=Yahoo Finance as_of=2026-10-20T21:00:00+00:00 freshness=FRESH RSI=45.16 liquidity=197232.42 spike=0.54
- GRCA.CA: score=-2.24 buy_ready=False sector_rank=14 price=28.0 support=28.0 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4280275.5 spike=0.67
- GSSC.CA: score=5.65 buy_ready=False sector_rank=14 price=260.36 support=246.0 resistance=309.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.97 liquidity=1668383.5 spike=1.25
- GTWL.CA: score=3.48 buy_ready=False sector_rank=14 price=105.29 support=104.1 resistance=113.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=93887256.0 spike=0.56
- HDBK.CA: score=4.49 buy_ready=False sector_rank=4 price=94.01 support=93.0 resistance=99.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14985278.0 spike=0.72
- HELI.CA: score=13.48 buy_ready=False sector_rank=16 price=6.75 support=6.63 resistance=8.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.9 liquidity=59263312.0 spike=0.81
- HRHO.CA: score=12.46 buy_ready=False sector_rank=17 price=24.5 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=56.16 liquidity=53932984.0 spike=0.42
- ICID.CA: score=7.97 buy_ready=False sector_rank=14 price=16.8 support=16.0 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.03 liquidity=4482243.5 spike=0.56
- IDRE.CA: score=4.67 buy_ready=False sector_rank=14 price=39.47 support=38.17 resistance=55.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.09 liquidity=2181827.0 spike=0.36
- IFAP.CA: score=2.72 buy_ready=False sector_rank=11 price=17.95 support=17.17 resistance=20.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=30.5 liquidity=4746975.5 spike=0.84
- INFI.CA: score=15.48 buy_ready=False sector_rank=14 price=121.82 support=104.0 resistance=138.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.21 liquidity=14478519.0 spike=0.7
- IRON.CA: score=9.22 buy_ready=False sector_rank=8 price=25.86 support=24.25 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=56.68 liquidity=6120062.0 spike=0.56
- ISMA.CA: score=5.13 buy_ready=False sector_rank=14 price=20.37 support=18.91 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=43.31 liquidity=2645562.5 spike=0.37
- ISMQ.CA: score=8.74 buy_ready=False sector_rank=8 price=7.17 support=6.61 resistance=8.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.16 liquidity=5641870.0 spike=0.32
- ISPH.CA: score=6.74 buy_ready=False sector_rank=21 price=10.13 support=10.03 resistance=12.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=34.66 liquidity=43466976.0 spike=0.95
- JUFO.CA: score=16.27 buy_ready=False sector_rank=6 price=23.46 support=22.1 resistance=27.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.42 liquidity=41589704.0 spike=2.54
- KABO.CA: score=-0.01 buy_ready=False sector_rank=15 price=7.29 support=7.15 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6509847.0 spike=0.3
- KWIN.CA: score=-0.03 buy_ready=False sector_rank=14 price=60.47 support=58.12 resistance=93.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.98 liquidity=2487071.5 spike=0.34
- KZPC.CA: score=15.47 buy_ready=False sector_rank=14 price=13.16 support=12.15 resistance=14.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.61 liquidity=6983950.5 spike=0.84
- LCSW.CA: score=18.26 buy_ready=False sector_rank=13 price=33.51 support=28.86 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=23300422.0 spike=1.19
- LUTS.CA: score=7.48 buy_ready=False sector_rank=14 price=0.64 support=0.63 resistance=0.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.84 liquidity=30096046.0 spike=0.56
- MAAL.CA: score=3.48 buy_ready=False sector_rank=14 price=6.57 support=6.5 resistance=7.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14391403.0 spike=0.58
- MASR.CA: score=13.48 buy_ready=False sector_rank=14 price=6.8 support=6.66 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.08 liquidity=32600942.0 spike=0.67
- MBSC.CA: score=13.88 buy_ready=False sector_rank=13 price=317.65 support=288.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.97 liquidity=48865524.0 spike=0.52
- MCQE.CA: score=12.88 buy_ready=False sector_rank=13 price=165.91 support=144.0 resistance=224.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.77 liquidity=51595620.0 spike=0.84
- MCRO.CA: score=12.48 buy_ready=False sector_rank=14 price=1.3 support=1.21 resistance=1.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.09 liquidity=14502232.0 spike=0.3
- MENA.CA: score=4.24 buy_ready=False sector_rank=16 price=5.94 support=5.57 resistance=7.05 source=Yahoo Finance as_of=2026-10-20T21:00:00+00:00 freshness=FRESH RSI=44.2 liquidity=757421.29 spike=0.37
- MEPA.CA: score=8.15 buy_ready=False sector_rank=14 price=1.48 support=1.47 resistance=1.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.59 liquidity=5664086.5 spike=0.77
- MFPC.CA: score=4.4 buy_ready=False sector_rank=8 price=45.09 support=45.05 resistance=47.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=54136072.0 spike=1.15
- MFSC.CA: score=12.48 buy_ready=False sector_rank=14 price=38.16 support=33.1 resistance=49.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=18.44 liquidity=11233482.0 spike=5.93
- MHOT.CA: score=-1.83 buy_ready=False sector_rank=7 price=14.66 support=14.03 resistance=15.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4028787.5 spike=0.23
- MICH.CA: score=11.98 buy_ready=False sector_rank=14 price=41.27 support=35.5 resistance=45.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.88 liquidity=6492527.0 spike=0.75
- MILS.CA: score=1.58 buy_ready=False sector_rank=14 price=133.0 support=132.1 resistance=146.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7920587.5 spike=1.09
- MIPH.CA: score=3.17 buy_ready=False sector_rank=21 price=742.36 support=666.66 resistance=915.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.23 liquidity=429357.25 spike=0.1
- MOED.CA: score=0.61 buy_ready=False sector_rank=14 price=0.53 support=0.53 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7125516.5 spike=0.54
- MOIL.CA: score=-1.0 buy_ready=False sector_rank=12 price=0.66 support=0.63 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=28.85 liquidity=62449.83 spike=0.25
- MOIN.CA: score=9.92 buy_ready=False sector_rank=14 price=30.07 support=28.71 resistance=37.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=33.27 liquidity=15898936.0 spike=1.72
- MOSC.CA: score=3.96 buy_ready=False sector_rank=14 price=250.18 support=228.05 resistance=310.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=49.21 liquidity=472603.16 spike=0.14
- MPCI.CA: score=13.48 buy_ready=False sector_rank=14 price=298.24 support=271.0 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=39.88 liquidity=62836140.0 spike=0.63
- MPCO.CA: score=3.97 buy_ready=False sector_rank=11 price=1.92 support=1.9 resistance=2.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=75789128.0 spike=0.74
- MPRC.CA: score=5.18 buy_ready=False sector_rank=14 price=32.68 support=32.01 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.7 liquidity=7699183.5 spike=0.46
- MTIE.CA: score=13.08 buy_ready=False sector_rank=9 price=7.35 support=7.05 resistance=8.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.92 liquidity=13411471.0 spike=0.66
- NAHO.CA: score=3.93 buy_ready=False sector_rank=14 price=0.13 support=0.12 resistance=0.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=23750.08 spike=1.21
- NCCW.CA: score=6.22 buy_ready=False sector_rank=14 price=5.26 support=5.05 resistance=7.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=24.19 liquidity=8731785.0 spike=0.27
- NEDA.CA: score=0.64 buy_ready=False sector_rank=14 price=2.6 support=2.47 resistance=2.75 source=Yahoo Finance as_of=2026-10-20T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=160677.39 spike=0.65
- NHPS.CA: score=6.12 buy_ready=False sector_rank=14 price=59.24 support=56.13 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.55 liquidity=3637418.25 spike=0.25
- NINH.CA: score=3.07 buy_ready=False sector_rank=14 price=14.49 support=14.13 resistance=20.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=18.02 liquidity=5587990.0 spike=0.5
- NIPH.CA: score=12.74 buy_ready=False sector_rank=21 price=267.07 support=230.01 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.57 liquidity=68866024.0 spike=0.57
- OBRI.CA: score=8.7 buy_ready=False sector_rank=14 price=24.57 support=22.8 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=54.59 liquidity=4215464.5 spike=0.29
- OCDI.CA: score=4.08 buy_ready=False sector_rank=16 price=24.87 support=24.53 resistance=26.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48108644.0 spike=1.3
- OCPH.CA: score=-0.42 buy_ready=False sector_rank=14 price=184.94 support=185.93 resistance=244.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.61 liquidity=2099097.25 spike=0.71
- ODIN.CA: score=-0.18 buy_ready=False sector_rank=14 price=2.06 support=2.04 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6332963.5 spike=1.0
- OFH.CA: score=3.48 buy_ready=False sector_rank=14 price=0.72 support=0.71 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21888360.0 spike=0.3
- OIH.CA: score=14.26 buy_ready=False sector_rank=10 price=1.77 support=1.7 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=39.39 liquidity=82156904.0 spike=1.1
- OLFI.CA: score=8.19 buy_ready=False sector_rank=6 price=19.76 support=19.4 resistance=22.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.28 liquidity=10409688.0 spike=0.7
- ORAS.CA: score=5.6 buy_ready=False sector_rank=3 price=841.66 support=834.0 resistance=861.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=143284688.0 spike=1.0
- ORHD.CA: score=3.48 buy_ready=False sector_rank=16 price=9.82 support=9.8 resistance=10.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=58977920.0 spike=0.43
- ORWE.CA: score=13.48 buy_ready=False sector_rank=15 price=25.22 support=25.01 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=42.75 liquidity=25809458.0 spike=0.61
- PHAR.CA: score=7.74 buy_ready=False sector_rank=21 price=101.62 support=98.05 resistance=119.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.59 liquidity=36413052.0 spike=0.61
- PHDC.CA: score=15.48 buy_ready=False sector_rank=16 price=12.54 support=12.2 resistance=13.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.67 liquidity=97639728.0 spike=1.0
- PHTV.CA: score=12.98 buy_ready=False sector_rank=14 price=325.31 support=310.02 resistance=370.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.46 liquidity=4500461.5 spike=5.63
- POUL.CA: score=15.55 buy_ready=False sector_rank=6 price=9.66 support=9.12 resistance=38.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.33 liquidity=61090372.0 spike=1.18
- PRCL.CA: score=8.46 buy_ready=False sector_rank=13 price=21.49 support=19.02 resistance=31.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.06 liquidity=5584476.5 spike=0.53
- PRDC.CA: score=13.48 buy_ready=False sector_rank=16 price=6.22 support=5.72 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.28 liquidity=13428251.0 spike=0.36
- PRMH.CA: score=4.5 buy_ready=False sector_rank=14 price=1.95 support=1.8 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.74 liquidity=2011021.38 spike=0.64
- RACC.CA: score=9.5 buy_ready=False sector_rank=14 price=8.07 support=7.93 resistance=9.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.16 liquidity=6880377.0 spike=1.07
- RAKT.CA: score=11.73 buy_ready=False sector_rank=14 price=23.06 support=20.26 resistance=25.08 source=Yahoo Finance as_of=2026-10-20T21:00:00+00:00 freshness=FRESH RSI=66.11 liquidity=850821.74 spike=2.2
- RAYA.CA: score=11.87 buy_ready=False sector_rank=20 price=5.63 support=5.36 resistance=7.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.41 liquidity=13932835.0 spike=0.42
- RMDA.CA: score=12.74 buy_ready=False sector_rank=21 price=5.05 support=4.8 resistance=6.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.45 liquidity=15363128.0 spike=0.55
- ROTO.CA: score=5.02 buy_ready=False sector_rank=14 price=31.2 support=30.77 resistance=34.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14618023.0 spike=1.77
- RREI.CA: score=1.43 buy_ready=False sector_rank=14 price=3.02 support=3.0 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7787867.0 spike=1.08
- RTVC.CA: score=3.53 buy_ready=False sector_rank=14 price=3.2 support=3.1 resistance=3.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.8 liquidity=1049739.88 spike=0.41
- RUBX.CA: score=3.72 buy_ready=False sector_rank=14 price=15.62 support=15.39 resistance=18.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=105192736.0 spike=1.12
- SAUD.CA: score=14.71 buy_ready=False sector_rank=4 price=21.0 support=20.2 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.22 liquidity=14986227.0 spike=1.11
- SCEM.CA: score=15.88 buy_ready=False sector_rank=13 price=84.52 support=74.55 resistance=95.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=63.91 liquidity=24523654.0 spike=0.4
- SCFM.CA: score=3.24 buy_ready=False sector_rank=14 price=218.11 support=200.22 resistance=272.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.46 liquidity=754208.13 spike=0.44
- SCTS.CA: score=7.95 buy_ready=False sector_rank=19 price=489.2 support=443.0 resistance=530.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21837944.0 spike=23.09
- SDTI.CA: score=16.48 buy_ready=False sector_rank=14 price=82.21 support=76.1 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.81 liquidity=13834224.0 spike=0.51
- SEIG.CA: score=-0.35 buy_ready=False sector_rank=14 price=172.15 support=170.0 resistance=190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4003638.5 spike=2.08
- SIPC.CA: score=3.48 buy_ready=False sector_rank=14 price=5.05 support=4.98 resistance=5.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=34192888.0 spike=0.61
- SKPC.CA: score=13.1 buy_ready=False sector_rank=8 price=15.14 support=14.4 resistance=18.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.47 liquidity=42450072.0 spike=0.61
- SMFR.CA: score=3.96 buy_ready=False sector_rank=14 price=196.17 support=180.11 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=45.14 liquidity=1477162.5 spike=0.47
- SNFC.CA: score=13.86 buy_ready=False sector_rank=14 price=11.14 support=10.8 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.85 liquidity=7376605.0 spike=0.84
- SPIN.CA: score=9.96 buy_ready=False sector_rank=15 price=14.12 support=13.5 resistance=17.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.94 liquidity=11450763.0 spike=2.24
- SPMD.CA: score=2.36 buy_ready=False sector_rank=14 price=0.35 support=0.34 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8871513.0 spike=0.66
- SUGR.CA: score=16.51 buy_ready=False sector_rank=6 price=55.0 support=50.5 resistance=59.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.62 liquidity=10461895.0 spike=1.16
- SVCE.CA: score=12.48 buy_ready=False sector_rank=14 price=8.81 support=8.41 resistance=11.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.55 liquidity=31417034.0 spike=0.44
- SWDY.CA: score=13.25 buy_ready=False sector_rank=18 price=106.54 support=101.5 resistance=126.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=33350248.0 spike=0.51
- TALM.CA: score=12.95 buy_ready=False sector_rank=19 price=19.19 support=18.28 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=55.19 liquidity=12755403.0 spike=0.43
- TMGH.CA: score=15.32 buy_ready=False sector_rank=16 price=86.92 support=80.01 resistance=94.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=57.47 liquidity=355078816.0 spike=1.42
- TRTO.CA: score=-1.52 buy_ready=False sector_rank=14 price=0.06 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-10-20T21:00:00+00:00 freshness=FRESH RSI=78.95 liquidity=398.84 spike=0.06
- UEFM.CA: score=3.25 buy_ready=False sector_rank=14 price=471.92 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=42.94 liquidity=762119.25 spike=0.26
- UEGC.CA: score=3.48 buy_ready=False sector_rank=14 price=1.44 support=1.42 resistance=1.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30519584.0 spike=0.66
- UNIP.CA: score=11.4 buy_ready=False sector_rank=14 price=0.3 support=0.29 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.46 liquidity=8753218.0 spike=1.08
- UNIT.CA: score=6.27 buy_ready=False sector_rank=16 price=16.89 support=15.6 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=55.36 liquidity=787920.75 spike=0.2
- WCDF.CA: score=-1.52 buy_ready=False sector_rank=14 price=496.19 support=432.5 resistance=686.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.82 liquidity=991801.69 spike=0.37
- WKOL.CA: score=8.08 buy_ready=False sector_rank=14 price=267.25 support=241.1 resistance=343.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=49.1 liquidity=5600786.0 spike=0.76
- ZEOT.CA: score=6.58 buy_ready=False sector_rank=14 price=11.0 support=9.75 resistance=13.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.65 liquidity=3091626.5 spike=0.38
- ZMID.CA: score=8.48 buy_ready=False sector_rank=16 price=6.77 support=6.4 resistance=8.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.5 liquidity=45883444.0 spike=0.57

## Backtesting Lite
- ABUK.CA: 180d return=66.94%, max drawdown=-26.86%, MA20>MA50 days last20=20, as_of=2026-10-20T21:00:00+00:00
- EAST.CA: 180d return=-17.36%, max drawdown=-33.66%, MA20>MA50 days last20=0, as_of=2026-10-20T21:00:00+00:00
- ELNA.CA: 180d return=-11.13%, max drawdown=-15.86%, MA20>MA50 days last20=0, as_of=2026-10-20T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ABUK.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Qir Fertilizers summary=Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results; Abu Qir Fertilizers&#39; board approves $5.6m coated urea project; Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26
  - Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results: https://english.mubasher.info/news/4604919/Abu-Qir-Fertilizers-generates-EGP-5-6bn-net-profits-in-Q1-26-unaudited-results/
  - Abu Qir Fertilizers&#39; board approves $5.6m coated urea project: https://english.mubasher.info/news/4585599/Abu-Qir-Fertilizers-board-approves-5-6m-coated-urea-project/
  - Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26: https://english.mubasher.info/news/4554415/Abu-Qir-Fertilizers-profits-exceed-EGP-5-1bn-in-H1-25-26/
- EAST.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Eastern Company summary=Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- ELNA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Nasr Manufacturing Agricultural Crops S.A.E summary=Consortium offers to acquire controlling stake in El Nasr for Agricultural Crops; El Nasr for Agricultural Crops to sell Sohag factory land for EGP 650m; EGX halts trading on El Nasr for Manufacturing Agricultural Crops
  - Consortium offers to acquire controlling stake in El Nasr for Agricultural Crops: https://english.mubasher.info/news/3749421/Consortium-offers-to-acquire-controlling-stake-in-El-Nasr-for-Agricultural-Crops/
  - El Nasr for Agricultural Crops to sell Sohag factory land for EGP 650m: https://english.mubasher.info/news/3685533/El-Nasr-for-Agricultural-Crops-to-sell-Sohag-factory-land-for-EGP-650m/
  - EGX halts trading on El Nasr for Manufacturing Agricultural Crops: https://english.mubasher.info/news/3489525/EGX-halts-trading-on-El-Nasr-for-Manufacturing-Agricultural-Crops/
- COMI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Commercial International Bank Egypt summary=Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.

## Warnings
- OpenRouter API error: 404
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- Evidence for ELNA.CA matches the company but no source/report date was detected.
- Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
