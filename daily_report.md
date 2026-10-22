# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-10-22T10:39:10.124207+00:00
Generated Cairo: 2026-10-22 13:39
Run timing: target 08:45 Cairo | generated Cairo 2026-10-22 13:39 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-10-22 13:36

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 5
- Tradeable price/liquidity tickers: 162/185
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, October 22
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 22.22% / above MA50 11.11%
- EGX70 regime: BEARISH / above MA20 5.13% / above MA50 5.13%
- Sector breadth: 4.76%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=538417216.0 spike=1.18 score=17.51
- ETEL.CA: liquidity=491083296.0 spike=2.19 score=11.36
- CCAP.CA: liquidity=460497760.0 spike=0.87 score=16.95
- TMGH.CA: liquidity=227851312.0 spike=0.91 score=14.08
- EGAL.CA: liquidity=139291728.0 spike=1.7 score=9.93

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- SCTS.CA: spike=20.83 liquidity=19700312.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ELNA.CA: spike=14.04 liquidity=2235193.25 outlook=BULLISH_WATCH score=85 buy_ready=False
- PHTV.CA: spike=5.54 liquidity=4425313.0 outlook=NEUTRAL score=48 buy_ready=False
- MFSC.CA: spike=4.95 liquidity=9366113.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EXPA.CA: spike=3.54 liquidity=120525832.0 outlook=WEAK_OR_RISKY score=22.37 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=4.94 5d=0.45% 20d=0.17% aboveMA50=50.0%
- #2 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #3 Fintech & Payments: score=1.12 5d=0.37% 20d=0.86% aboveMA50=0.0%
- #4 Energy & Petrochemicals: score=0.71 5d=-1.56% 20d=-5.44% aboveMA50=33.33%
- #5 Banking & Financials: score=0.37 5d=0.0% 20d=-7.46% aboveMA50=10.0%
- #6 Tourism & Leisure: score=0.29 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #7 Food, Beverages & Tobacco: score=-0.07 5d=1.08% 20d=-10.66% aboveMA50=0.0%
- #8 Investment Holding: score=-0.13 5d=-2.21% 20d=-13.04% aboveMA50=66.67%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ELNA.CA: BULLISH_WATCH score=85 liquidity=TRADEABLE sector=LAGGING risk=sector is not leading
- AMOC.CA: BULLISH_WATCH score=76.71 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MFPC.CA: CONSTRUCTIVE score=65 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- CPCI.CA: CONSTRUCTIVE score=65 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- ABUK.CA: CONSTRUCTIVE score=64 liquidity=TRADEABLE sector=LAGGING risk=momentum is extended; sector is not leading
- BINV.CA: CONSTRUCTIVE score=58 liquidity=TRADEABLE sector=LAGGING risk=below MA20; sector is not leading
- CCAP.CA: CONSTRUCTIVE score=58 liquidity=TRADEABLE sector=LAGGING risk=below MA20; sector is not leading
- EAST.CA: CONSTRUCTIVE score=54 liquidity=TRADEABLE sector=NEUTRAL risk=below MA50
- SDTI.CA: CONSTRUCTIVE score=53 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; below MA20; sector is not leading
- COMI.CA: NEUTRAL score=48.37 liquidity=TRADEABLE sector=IMPROVING risk=below MA50

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- DTPP.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=5.98 buy_ready=False sector_rank=16 price=224.19 support=201.0 resistance=309.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=42.04 liquidity=2971053.25 spike=0.29
- ABUK.CA: score=22.69 buy_ready=False sector_rank=11 price=93.05 support=80.5 resistance=95.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=64.47 liquidity=83242192.0 spike=1.08
- ACAMD.CA: score=14.01 buy_ready=False sector_rank=16 price=2.01 support=1.87 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=51.16 liquidity=24435454.0 spike=0.51
- ACGC.CA: score=1.35 buy_ready=False sector_rank=13 price=13.04 support=12.5 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=3121919.5 spike=0.28
- ADCI.CA: score=3.52 buy_ready=False sector_rank=16 price=256.71 support=241.55 resistance=288.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=43.36 liquidity=509790.53 spike=0.3
- ADIB.CA: score=14.15 buy_ready=False sector_rank=5 price=46.28 support=43.45 resistance=52.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=42.67 liquidity=65702012.0 spike=0.91
- ADPC.CA: score=4.37 buy_ready=False sector_rank=16 price=2.94 support=2.85 resistance=4.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=32.2 liquidity=7358856.0 spike=0.66
- AFDI.CA: score=-5.34 buy_ready=False sector_rank=16 price=44.57 support=44.22 resistance=47.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1652942.88 spike=0.37
- AFMC.CA: score=0.88 buy_ready=False sector_rank=16 price=116.3 support=115.5 resistance=123.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7863118.0 spike=0.43
- AJWA.CA: score=15.01 buy_ready=False sector_rank=16 price=213.62 support=176.0 resistance=229.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=79.73 liquidity=21894414.0 spike=0.63
- ALCN.CA: score=11.51 buy_ready=False sector_rank=10 price=32.25 support=30.19 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=51.75 liquidity=7850773.0 spike=0.34
- ALUM.CA: score=4.71 buy_ready=False sector_rank=16 price=20.23 support=18.01 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=2699885.75 spike=0.68
- AMER.CA: score=13.08 buy_ready=False sector_rank=15 price=4.09 support=3.8 resistance=5.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=48.51 liquidity=15829423.0 spike=0.3
- AMES.CA: score=9.01 buy_ready=False sector_rank=16 price=33.62 support=32.8 resistance=51.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=26.93 liquidity=20620682.0 spike=0.33
- AMIA.CA: score=4.99 buy_ready=False sector_rank=16 price=17.61 support=17.0 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=46.95 liquidity=1976922.0 spike=0.12
- AMOC.CA: score=19.28 buy_ready=False sector_rank=4 price=13.64 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=54.64 liquidity=66925120.0 spike=0.54
- APSW.CA: score=2.35 buy_ready=False sector_rank=16 price=7.78 support=7.72 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=337707.28 spike=0.57
- ARAB.CA: score=13.08 buy_ready=False sector_rank=15 price=0.25 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=62.07 liquidity=58069660.0 spike=0.53
- ARCC.CA: score=12.84 buy_ready=False sector_rank=9 price=65.52 support=60.01 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=57.0 liquidity=9003859.0 spike=0.2
- AREH.CA: score=5.56 buy_ready=False sector_rank=16 price=1.1 support=1.09 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=42.55 liquidity=3549441.25 spike=0.44
- ASCM.CA: score=0.19 buy_ready=False sector_rank=16 price=46.43 support=44.25 resistance=61.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=33.09 liquidity=3174251.25 spike=0.33
- ASPI.CA: score=11.17 buy_ready=False sector_rank=16 price=0.31 support=0.3 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=43.04 liquidity=9161622.0 spike=0.42
- ATLC.CA: score=13.29 buy_ready=False sector_rank=12 price=4.81 support=4.72 resistance=7.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=43.05 liquidity=10518359.0 spike=1.5
- ATQA.CA: score=13.53 buy_ready=False sector_rank=11 price=10.64 support=10.15 resistance=13.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=47.29 liquidity=25816800.0 spike=0.46
- AXPH.CA: score=0.18 buy_ready=False sector_rank=16 price=1278.8 support=1200.12 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=34.27 liquidity=2163436.5 spike=0.35
- BINV.CA: score=17.07 buy_ready=False sector_rank=8 price=57.04 support=52.11 resistance=65.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=40.41 liquidity=14729898.0 spike=1.06
- BIOC.CA: score=8.01 buy_ready=False sector_rank=16 price=264.52 support=225.21 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=33.74 liquidity=24743972.0 spike=0.23
- BTFH.CA: score=12.29 buy_ready=False sector_rank=12 price=2.58 support=2.55 resistance=2.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=38.81 liquidity=67080212.0 spike=0.69
- CAED.CA: score=0.08 buy_ready=False sector_rank=16 price=86.01 support=83.0 resistance=92.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7071585.5 spike=0.88
- CANA.CA: score=14.15 buy_ready=False sector_rank=5 price=42.04 support=38.1 resistance=48.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=43.3 liquidity=10200543.0 spike=0.57
- CCAP.CA: score=16.95 buy_ready=False sector_rank=8 price=6.39 support=5.87 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=40.72 liquidity=460497760.0 spike=0.87
- CCRS.CA: score=1.61 buy_ready=False sector_rank=16 price=1.96 support=1.78 resistance=2.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=32.97 liquidity=4599228.0 spike=0.66
- CEFM.CA: score=3.59 buy_ready=False sector_rank=16 price=126.74 support=113.0 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=44.37 liquidity=573815.38 spike=0.27
- CERA.CA: score=3.01 buy_ready=False sector_rank=16 price=1.15 support=1.14 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=78154592.0 spike=0.64
- CFGH.CA: score=-2.99 buy_ready=False sector_rank=16 price=0.11 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-20T21:00:00+00:00 freshness=FRESH RSI=16.67 liquidity=471.7 spike=0.09
- CICH.CA: score=3.38 buy_ready=False sector_rank=12 price=10.62 support=9.63 resistance=12.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=38.44 liquidity=1085097.13 spike=0.47
- CIEB.CA: score=7.05 buy_ready=False sector_rank=5 price=22.26 support=21.4 resistance=24.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=41.57 liquidity=3902208.5 spike=0.42
- CIRA.CA: score=11.57 buy_ready=False sector_rank=17 price=35.98 support=33.15 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=41.33 liquidity=8717768.0 spike=0.49
- CLHO.CA: score=6.64 buy_ready=False sector_rank=19 price=13.35 support=13.0 resistance=16.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=31.02 liquidity=14741170.0 spike=0.4
- CNFN.CA: score=15.13 buy_ready=False sector_rank=12 price=4.04 support=3.72 resistance=4.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=52.1 liquidity=12755797.0 spike=1.42
- COMI.CA: score=17.51 buy_ready=False sector_rank=5 price=126.76 support=120.0 resistance=132.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=58.36 liquidity=538417216.0 spike=1.18
- COPR.CA: score=8.75 buy_ready=False sector_rank=16 price=0.41 support=0.41 resistance=0.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=38.79 liquidity=5740970.5 spike=0.34
- COSG.CA: score=6.1 buy_ready=False sector_rank=16 price=1.33 support=1.29 resistance=1.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=39.06 liquidity=4091692.0 spike=0.32
- CPCI.CA: score=9.76 buy_ready=False sector_rank=16 price=588.36 support=502.25 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=56.95 liquidity=1752147.0 spike=0.38
- CSAG.CA: score=6.17 buy_ready=False sector_rank=10 price=34.94 support=33.68 resistance=38.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=45.41 liquidity=2513629.5 spike=0.37
- DAPH.CA: score=12.01 buy_ready=False sector_rank=16 price=81.12 support=82.0 resistance=114.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=40.46 liquidity=12289808.0 spike=0.29
- DEIN.CA: score=6.01 buy_ready=False sector_rank=16 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 09:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37.26 spike=0.01
- DOMT.CA: score=6.02 buy_ready=False sector_rank=7 price=22.98 support=22.5 resistance=26.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=42.06 liquidity=1045385.25 spike=0.27
- DSCW.CA: score=10.46 buy_ready=False sector_rank=16 price=1.5 support=1.45 resistance=1.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=38.78 liquidity=8447632.0 spike=0.53
- EALR.CA: score=3.75 buy_ready=False sector_rank=16 price=284.94 support=270.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=36.61 liquidity=1733035.75 spike=0.48
- EASB.CA: score=-5.66 buy_ready=False sector_rank=16 price=6.11 support=6.06 resistance=6.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1332589.38 spike=0.25
- EAST.CA: score=17.25 buy_ready=False sector_rank=7 price=29.98 support=27.01 resistance=32.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=59.69 liquidity=46882928.0 spike=1.14
- EBSC.CA: score=3.08 buy_ready=False sector_rank=16 price=1.46 support=1.33 resistance=2.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=1063586.5 spike=0.52
- ECAP.CA: score=-1.01 buy_ready=False sector_rank=16 price=27.11 support=25.7 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=34.38 liquidity=1974983.25 spike=0.53
- EDFM.CA: score=3.4 buy_ready=False sector_rank=16 price=384.99 support=335.2 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=50.02 liquidity=389579.44 spike=0.35
- EEII.CA: score=-1.1 buy_ready=False sector_rank=16 price=1.76 support=1.71 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=29.23 liquidity=1886168.63 spike=0.24
- EFIC.CA: score=12.76 buy_ready=False sector_rank=11 price=151.87 support=140.0 resistance=186.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=42.59 liquidity=8228549.0 spike=0.28
- EFID.CA: score=14.97 buy_ready=False sector_rank=7 price=18.5 support=16.98 resistance=20.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=54.33 liquidity=12011607.0 spike=0.27
- EFIH.CA: score=15.45 buy_ready=False sector_rank=3 price=23.04 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=60.66 liquidity=33403876.0 spike=0.53
- EGAL.CA: score=9.93 buy_ready=False sector_rank=11 price=304.22 support=275.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=33.11 liquidity=139291728.0 spike=1.7
- EGAS.CA: score=6.38 buy_ready=False sector_rank=4 price=50.17 support=47.0 resistance=60.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=37.3 liquidity=2094560.13 spike=0.28
- EGBE.CA: score=4.21 buy_ready=False sector_rank=5 price=0.5 support=0.5 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=37.84 liquidity=63983.83 spike=0.49
- EGCH.CA: score=7.53 buy_ready=False sector_rank=11 price=11.4 support=10.67 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=28.88 liquidity=30816900.0 spike=0.42
- EGSA.CA: score=15.98 buy_ready=False sector_rank=1 price=9.03 support=8.75 resistance=9.09 source=Yahoo Finance as_of=2026-10-20T21:00:00+00:00 freshness=FRESH RSI=66.07 liquidity=677.25 spike=0.12
- EGTS.CA: score=5.76 buy_ready=False sector_rank=15 price=12.42 support=12.06 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=24.63 liquidity=8675117.0 spike=0.29
- EHDR.CA: score=4.89 buy_ready=False sector_rank=16 price=2.14 support=2.07 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=40.62 liquidity=2879184.75 spike=0.27
- ELEC.CA: score=13.46 buy_ready=False sector_rank=14 price=1.6 support=1.55 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=42.31 liquidity=79416800.0 spike=1.69
- ELKA.CA: score=7.17 buy_ready=False sector_rank=16 price=1.45 support=1.38 resistance=1.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=49.25 liquidity=5155334.5 spike=0.39
- ELNA.CA: score=18.25 buy_ready=False sector_rank=16 price=36.98 support=33.46 resistance=35.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=2235193.25 spike=14.04
- ELSH.CA: score=8.05 buy_ready=False sector_rank=16 price=10.24 support=10.0 resistance=12.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=42.09 liquidity=5037708.0 spike=0.25
- ELWA.CA: score=2.02 buy_ready=False sector_rank=16 price=1.65 support=1.43 resistance=1.73 source=Yahoo Finance as_of=2026-10-20T21:00:00+00:00 freshness=FRESH RSI=90.48 liquidity=5243.7 spike=0.01
- EMFD.CA: score=8.08 buy_ready=False sector_rank=15 price=11.5 support=11.2 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=24.07 liquidity=51599136.0 spike=0.88
- ENGC.CA: score=5.08 buy_ready=False sector_rank=16 price=31.94 support=30.0 resistance=43.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=43.23 liquidity=3069707.0 spike=0.25
- EOSB.CA: score=5.01 buy_ready=False sector_rank=16 price=1.57 support=1.57 resistance=1.64 source=Yahoo Finance as_of=2026-10-20T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=277.89 spike=0.01
- EPCO.CA: score=-5.79 buy_ready=False sector_rank=16 price=8.35 support=8.24 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1202991.63 spike=0.28
- EPPK.CA: score=-6.57 buy_ready=False sector_rank=16 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=11.36 buy_ready=False sector_rank=1 price=132.67 support=128.6 resistance=140.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=491083296.0 spike=2.19
- ETRS.CA: score=7.84 buy_ready=False sector_rank=16 price=10.33 support=9.61 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=57.7 liquidity=2831731.75 spike=0.27
- EXPA.CA: score=13.15 buy_ready=False sector_rank=5 price=14.3 support=12.0 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=30.5 liquidity=120525832.0 spike=3.54
- FAIT.CA: score=6.3 buy_ready=False sector_rank=5 price=43.92 support=40.4 resistance=47.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=52.95 liquidity=2151730.75 spike=0.74
- FAITA.CA: score=11.16 buy_ready=False sector_rank=5 price=1.0 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=52.22 liquidity=10756.05 spike=0.31
- FERC.CA: score=-0.84 buy_ready=False sector_rank=11 price=64.48 support=60.51 resistance=79.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=30.36 liquidity=1627964.75 spike=0.46
- FWRY.CA: score=14.45 buy_ready=False sector_rank=3 price=17.93 support=17.5 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=53.24 liquidity=59536824.0 spike=0.54
- GBCO.CA: score=6.62 buy_ready=False sector_rank=21 price=25.9 support=26.16 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=34.29 liquidity=117643688.0 spike=1.11
- GDWA.CA: score=10.47 buy_ready=False sector_rank=16 price=0.58 support=0.57 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=8460614.0 spike=0.5
- GGCC.CA: score=9.23 buy_ready=False sector_rank=16 price=0.6 support=0.61 resistance=0.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=43.28 liquidity=7215402.5 spike=0.45
- GIHD.CA: score=-0.6 buy_ready=False sector_rank=16 price=44.1 support=43.0 resistance=46.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6390338.5 spike=0.33
- GMCI.CA: score=4.21 buy_ready=False sector_rank=16 price=1.54 support=1.47 resistance=1.77 source=Yahoo Finance as_of=2026-10-20T21:00:00+00:00 freshness=FRESH RSI=45.16 liquidity=197232.42 spike=0.54
- GRCA.CA: score=6.67 buy_ready=False sector_rank=16 price=28.84 support=26.91 resistance=42.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=38.54 liquidity=2658359.0 spike=0.42
- GSSC.CA: score=5.14 buy_ready=False sector_rank=16 price=260.39 support=246.0 resistance=309.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=52.97 liquidity=1648376.25 spike=1.24
- HDBK.CA: score=13.15 buy_ready=False sector_rank=5 price=95.15 support=90.26 resistance=118.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=41.65 liquidity=10779050.0 spike=0.52
- HELI.CA: score=13.08 buy_ready=False sector_rank=15 price=6.79 support=6.63 resistance=8.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=43.9 liquidity=41367284.0 spike=0.57
- HRHO.CA: score=12.29 buy_ready=False sector_rank=12 price=24.5 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=56.16 liquidity=38104848.0 spike=0.3
- ICID.CA: score=4.42 buy_ready=False sector_rank=16 price=16.82 support=16.0 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=36.03 liquidity=1404795.63 spike=0.18
- IDRE.CA: score=3.52 buy_ready=False sector_rank=16 price=39.37 support=38.17 resistance=55.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=36.09 liquidity=1505346.25 spike=0.25
- IFAP.CA: score=-0.42 buy_ready=False sector_rank=20 price=18.01 support=17.17 resistance=20.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=30.5 liquidity=3184974.5 spike=0.56
- INFI.CA: score=17.01 buy_ready=False sector_rank=16 price=123.97 support=104.0 resistance=138.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=55.21 liquidity=11381293.0 spike=0.55
- IRON.CA: score=7.19 buy_ready=False sector_rank=11 price=26.02 support=24.25 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=56.68 liquidity=4662254.0 spike=0.43
- ISMA.CA: score=4.38 buy_ready=False sector_rank=16 price=20.51 support=18.91 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=43.31 liquidity=2368603.0 spike=0.33
- ISMQ.CA: score=7.08 buy_ready=False sector_rank=11 price=7.23 support=6.61 resistance=8.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=42.16 liquidity=4555156.5 spike=0.26
- ISPH.CA: score=6.64 buy_ready=False sector_rank=19 price=10.19 support=10.03 resistance=12.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=34.66 liquidity=26827722.0 spike=0.59
- JUFO.CA: score=15.35 buy_ready=False sector_rank=7 price=23.45 support=22.1 resistance=27.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=46.42 liquidity=35733992.0 spike=2.19
- KABO.CA: score=-2.13 buy_ready=False sector_rank=13 price=7.27 support=7.15 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4640271.5 spike=0.21
- KWIN.CA: score=-1.2 buy_ready=False sector_rank=16 price=61.55 support=58.12 resistance=93.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=29.98 liquidity=1785665.75 spike=0.25
- KZPC.CA: score=7.13 buy_ready=False sector_rank=16 price=13.11 support=12.15 resistance=14.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=58.61 liquidity=4121894.5 spike=0.5
- LCSW.CA: score=17.84 buy_ready=False sector_rank=9 price=33.52 support=28.86 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=13906921.0 spike=0.71
- LUTS.CA: score=7.01 buy_ready=False sector_rank=16 price=0.65 support=0.63 resistance=0.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=27.84 liquidity=23424780.0 spike=0.43
- MAAL.CA: score=3.01 buy_ready=False sector_rank=16 price=6.82 support=6.63 resistance=7.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10733587.0 spike=0.43
- MASR.CA: score=13.01 buy_ready=False sector_rank=16 price=6.9 support=6.66 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=41.08 liquidity=21390928.0 spike=0.44
- MBSC.CA: score=13.84 buy_ready=False sector_rank=9 price=317.82 support=288.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=58.97 liquidity=44479552.0 spike=0.47
- MCQE.CA: score=12.84 buy_ready=False sector_rank=9 price=163.98 support=144.0 resistance=224.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=45.77 liquidity=39876496.0 spike=0.65
- MCRO.CA: score=11.75 buy_ready=False sector_rank=16 price=1.32 support=1.21 resistance=1.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=35.09 liquidity=9739509.0 spike=0.2
- MENA.CA: score=3.84 buy_ready=False sector_rank=15 price=5.94 support=5.57 resistance=7.05 source=Yahoo Finance as_of=2026-10-20T21:00:00+00:00 freshness=FRESH RSI=44.2 liquidity=757421.29 spike=0.37
- MEPA.CA: score=6.68 buy_ready=False sector_rank=16 price=1.47 support=1.47 resistance=1.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=44.59 liquidity=4671099.5 spike=0.64
- MFPC.CA: score=18.53 buy_ready=False sector_rank=11 price=45.63 support=40.66 resistance=48.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=59.16 liquidity=37441608.0 spike=0.79
- MFSC.CA: score=7.38 buy_ready=False sector_rank=16 price=39.25 support=38.25 resistance=42.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9366113.0 spike=4.95
- MHOT.CA: score=-2.59 buy_ready=False sector_rank=6 price=14.61 support=14.03 resistance=15.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3295401.75 spike=0.19
- MICH.CA: score=10.57 buy_ready=False sector_rank=16 price=41.34 support=35.5 resistance=45.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=53.88 liquidity=5559339.0 spike=0.64
- MILS.CA: score=-1.15 buy_ready=False sector_rank=16 price=135.8 support=134.0 resistance=146.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5836584.0 spike=0.8
- MIPH.CA: score=2.97 buy_ready=False sector_rank=19 price=741.97 support=666.66 resistance=915.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=42.23 liquidity=331951.41 spike=0.07
- MOED.CA: score=1.37 buy_ready=False sector_rank=16 price=0.54 support=0.52 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=33.46 liquidity=4358687.5 spike=0.33
- MOIL.CA: score=-0.67 buy_ready=False sector_rank=4 price=0.66 support=0.63 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=28.85 liquidity=48760.43 spike=0.2
- MOIN.CA: score=8.73 buy_ready=False sector_rank=16 price=30.0 support=28.71 resistance=37.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=33.27 liquidity=12592532.0 spike=1.36
- MOSC.CA: score=3.44 buy_ready=False sector_rank=16 price=250.96 support=228.05 resistance=310.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=49.21 liquidity=427843.38 spike=0.13
- MPCI.CA: score=13.01 buy_ready=False sector_rank=16 price=298.18 support=271.0 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=39.88 liquidity=35512192.0 spike=0.36
- MPCO.CA: score=7.4 buy_ready=False sector_rank=20 price=1.94 support=1.79 resistance=2.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=33.93 liquidity=50849528.0 spike=0.5
- MPRC.CA: score=3.9 buy_ready=False sector_rank=16 price=33.33 support=32.01 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=34.7 liquidity=6889519.5 spike=0.41
- MTIE.CA: score=11.4 buy_ready=False sector_rank=21 price=7.38 support=7.05 resistance=8.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=42.92 liquidity=10753383.0 spike=0.53
- NAHO.CA: score=3.31 buy_ready=False sector_rank=16 price=0.13 support=0.12 resistance=0.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=22318.95 spike=1.14
- NCCW.CA: score=3.9 buy_ready=False sector_rank=16 price=5.31 support=5.05 resistance=7.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=24.19 liquidity=6889966.5 spike=0.21
- NEDA.CA: score=0.17 buy_ready=False sector_rank=16 price=2.6 support=2.47 resistance=2.75 source=Yahoo Finance as_of=2026-10-20T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=160677.39 spike=0.65
- NHPS.CA: score=5.05 buy_ready=False sector_rank=16 price=58.94 support=56.13 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=37.55 liquidity=3034379.5 spike=0.21
- NINH.CA: score=1.38 buy_ready=False sector_rank=16 price=14.58 support=14.13 resistance=20.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=18.02 liquidity=4371738.5 spike=0.39
- NIPH.CA: score=12.64 buy_ready=False sector_rank=19 price=268.41 support=230.01 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=36.57 liquidity=60604596.0 spike=0.51
- OBRI.CA: score=7.7 buy_ready=False sector_rank=16 price=24.67 support=22.8 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=54.59 liquidity=3688966.25 spike=0.25
- OCDI.CA: score=15.08 buy_ready=False sector_rank=15 price=25.0 support=22.6 resistance=29.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=53.54 liquidity=22859650.0 spike=0.62
- OCPH.CA: score=-1.24 buy_ready=False sector_rank=16 price=185.33 support=185.93 resistance=244.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=34.61 liquidity=1743444.5 spike=0.59
- ODIN.CA: score=6.55 buy_ready=False sector_rank=16 price=2.13 support=1.91 resistance=2.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=39.45 liquidity=4536405.0 spike=0.72
- OFH.CA: score=8.01 buy_ready=False sector_rank=16 price=0.73 support=0.69 resistance=1.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=17.28 liquidity=17213674.0 spike=0.23
- OIH.CA: score=13.95 buy_ready=False sector_rank=8 price=1.73 support=1.7 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=39.39 liquidity=68081856.0 spike=0.91
- OLFI.CA: score=3.98 buy_ready=False sector_rank=7 price=19.67 support=19.4 resistance=22.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=21.28 liquidity=6007578.5 spike=0.41
- ORAS.CA: score=6.6 buy_ready=False sector_rank=2 price=840.23 support=834.0 resistance=861.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=93782136.0 spike=1.0
- ORHD.CA: score=9.08 buy_ready=False sector_rank=15 price=10.0 support=9.5 resistance=42.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=31.68 liquidity=41648968.0 spike=0.3
- ORWE.CA: score=13.23 buy_ready=False sector_rank=13 price=25.32 support=25.01 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=42.75 liquidity=17034242.0 spike=0.41
- PHAR.CA: score=7.64 buy_ready=False sector_rank=19 price=101.87 support=98.05 resistance=119.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=31.59 liquidity=24690016.0 spike=0.41
- PHDC.CA: score=15.08 buy_ready=False sector_rank=15 price=12.59 support=12.2 resistance=13.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=51.67 liquidity=59591880.0 spike=0.61
- PHTV.CA: score=12.44 buy_ready=False sector_rank=16 price=325.12 support=310.02 resistance=370.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=52.46 liquidity=4425313.0 spike=5.54
- POUL.CA: score=14.97 buy_ready=False sector_rank=7 price=9.67 support=9.12 resistance=38.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=48.33 liquidity=49017712.0 spike=0.95
- PRCL.CA: score=7.55 buy_ready=False sector_rank=9 price=21.52 support=19.02 resistance=31.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=47.06 liquidity=4709211.5 spike=0.45
- PRDC.CA: score=10.95 buy_ready=False sector_rank=15 price=6.19 support=5.72 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=41.28 liquidity=8870176.0 spike=0.24
- PRMH.CA: score=-5.55 buy_ready=False sector_rank=16 price=1.88 support=1.86 resistance=2.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1437544.5 spike=0.46
- RACC.CA: score=5.81 buy_ready=False sector_rank=16 price=8.13 support=7.93 resistance=9.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=43.16 liquidity=3793512.75 spike=0.59
- RAKT.CA: score=11.26 buy_ready=False sector_rank=16 price=23.06 support=20.26 resistance=25.08 source=Yahoo Finance as_of=2026-10-20T21:00:00+00:00 freshness=FRESH RSI=66.11 liquidity=850821.74 spike=2.2
- RAYA.CA: score=11.82 buy_ready=False sector_rank=18 price=5.66 support=5.36 resistance=7.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=42.41 liquidity=11646649.0 spike=0.35
- RMDA.CA: score=12.64 buy_ready=False sector_rank=19 price=5.04 support=4.8 resistance=6.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=43.45 liquidity=11560267.0 spike=0.42
- ROTO.CA: score=1.76 buy_ready=False sector_rank=16 price=31.57 support=31.07 resistance=34.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8645362.0 spike=1.05
- RREI.CA: score=-2.84 buy_ready=False sector_rank=16 price=3.04 support=3.02 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4149327.25 spike=0.58
- RTVC.CA: score=2.98 buy_ready=False sector_rank=16 price=3.21 support=3.1 resistance=3.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=35.8 liquidity=969564.13 spike=0.38
- RUBX.CA: score=3.01 buy_ready=False sector_rank=16 price=16.0 support=15.6 resistance=18.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=88565696.0 spike=0.94
- SAUD.CA: score=13.79 buy_ready=False sector_rank=5 price=21.0 support=20.2 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=43.22 liquidity=9645899.0 spike=0.71
- SCEM.CA: score=15.84 buy_ready=False sector_rank=9 price=84.04 support=74.55 resistance=95.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=63.91 liquidity=12858910.0 spike=0.21
- SCFM.CA: score=2.59 buy_ready=False sector_rank=16 price=218.44 support=200.22 resistance=272.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=36.46 liquidity=579549.13 spike=0.34
- SCTS.CA: score=7.85 buy_ready=False sector_rank=17 price=502.74 support=443.0 resistance=530.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19700312.0 spike=20.83
- SDTI.CA: score=8.55 buy_ready=False sector_rank=16 price=82.16 support=76.1 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=50.81 liquidity=2540683.0 spike=0.09
- SEIG.CA: score=-1.78 buy_ready=False sector_rank=16 price=171.12 support=170.0 resistance=190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3523749.25 spike=1.84
- SIPC.CA: score=3.01 buy_ready=False sector_rank=16 price=5.07 support=5.02 resistance=5.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25939932.0 spike=0.46
- SKPC.CA: score=12.53 buy_ready=False sector_rank=11 price=15.12 support=14.4 resistance=18.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=47.47 liquidity=28743364.0 spike=0.41
- SMFR.CA: score=3.12 buy_ready=False sector_rank=16 price=192.37 support=180.11 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=45.14 liquidity=1106533.63 spike=0.35
- SNFC.CA: score=5.59 buy_ready=False sector_rank=16 price=11.05 support=10.8 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=41.85 liquidity=2573398.75 spike=0.29
- SPIN.CA: score=8.88 buy_ready=False sector_rank=13 price=14.42 support=13.5 resistance=17.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=26.94 liquidity=9809382.0 spike=1.92
- SPMD.CA: score=-0.63 buy_ready=False sector_rank=16 price=0.35 support=0.35 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6360234.5 spike=0.47
- SUGR.CA: score=13.24 buy_ready=False sector_rank=7 price=55.0 support=50.5 resistance=59.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=58.62 liquidity=7263191.5 spike=0.8
- SVCE.CA: score=12.01 buy_ready=False sector_rank=16 price=8.91 support=8.41 resistance=11.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=45.55 liquidity=23369842.0 spike=0.33
- SWDY.CA: score=13.08 buy_ready=False sector_rank=14 price=106.28 support=101.5 resistance=126.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=24390582.0 spike=0.38
- TALM.CA: score=9.62 buy_ready=False sector_rank=17 price=19.17 support=18.28 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=55.19 liquidity=6772914.5 spike=0.23
- TMGH.CA: score=14.08 buy_ready=False sector_rank=15 price=86.77 support=80.01 resistance=94.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=57.47 liquidity=227851312.0 spike=0.91
- TRTO.CA: score=-1.99 buy_ready=False sector_rank=16 price=0.06 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-10-20T21:00:00+00:00 freshness=FRESH RSI=78.95 liquidity=398.84 spike=0.06
- UEFM.CA: score=2.57 buy_ready=False sector_rank=16 price=473.38 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=42.94 liquidity=557989.63 spike=0.19
- UEGC.CA: score=14.01 buy_ready=False sector_rank=16 price=1.45 support=1.34 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=52.38 liquidity=23007660.0 spike=0.5
- UNIP.CA: score=6.65 buy_ready=False sector_rank=16 price=0.3 support=0.29 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=39.46 liquidity=4636610.0 spike=0.57
- UNIT.CA: score=5.59 buy_ready=False sector_rank=15 price=16.97 support=15.6 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=55.36 liquidity=512777.38 spike=0.13
- WCDF.CA: score=-2.26 buy_ready=False sector_rank=16 price=492.87 support=432.5 resistance=686.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=26.82 liquidity=726442.5 spike=0.27
- WKOL.CA: score=6.99 buy_ready=False sector_rank=16 price=267.11 support=241.1 resistance=343.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=49.1 liquidity=4977137.5 spike=0.68
- ZEOT.CA: score=5.26 buy_ready=False sector_rank=16 price=10.88 support=9.75 resistance=13.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=47.65 liquidity=2243309.75 spike=0.28
- ZMID.CA: score=8.08 buy_ready=False sector_rank=15 price=6.71 support=6.4 resistance=8.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=34.5 liquidity=24146792.0 spike=0.3

## Backtesting Lite
- ABUK.CA: 180d return=66.94%, max drawdown=-26.86%, MA20>MA50 days last20=20, as_of=2026-10-20T21:00:00+00:00
- AMOC.CA: 180d return=102.68%, max drawdown=-16.73%, MA20>MA50 days last20=20, as_of=2026-10-20T21:00:00+00:00
- MFPC.CA: 180d return=64.78%, max drawdown=-26.33%, MA20>MA50 days last20=20, as_of=2026-10-20T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ABUK.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Qir Fertilizers summary=Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results; Abu Qir Fertilizers&#39; board approves $5.6m coated urea project; Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26
  - Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results: https://english.mubasher.info/news/4604919/Abu-Qir-Fertilizers-generates-EGP-5-6bn-net-profits-in-Q1-26-unaudited-results/
  - Abu Qir Fertilizers&#39; board approves $5.6m coated urea project: https://english.mubasher.info/news/4585599/Abu-Qir-Fertilizers-board-approves-5-6m-coated-urea-project/
  - Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26: https://english.mubasher.info/news/4554415/Abu-Qir-Fertilizers-profits-exceed-EGP-5-1bn-in-H1-25-26/
- AMOC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria Mineral Oils summary=AMOC achieves EGP 10.5bn consolidated sales in Q1-26; AMOC studies potential project with Germany’s SULZER; AMOC to pay out EGP 0.4/shr dividends for H2-25
  - AMOC achieves EGP 10.5bn consolidated sales in Q1-26: https://english.mubasher.info/news/4604903/AMOC-achieves-EGP-10-5bn-consolidated-sales-in-Q1-26/
  - AMOC studies potential project with Germany’s SULZER: https://english.mubasher.info/news/4586853/AMOC-studies-potential-project-with-Germany-s-SULZER/
  - AMOC to pay out EGP 0.4/shr dividends for H2-25: https://english.mubasher.info/news/4586775/AMOC-to-pay-out-EGP-0-4-shr-dividends-for-H2-25/
- MFPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr Fertilizers Production summary=Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- ELNA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Nasr Manufacturing Agricultural Crops S.A.E summary=Consortium offers to acquire controlling stake in El Nasr for Agricultural Crops; El Nasr for Agricultural Crops to sell Sohag factory land for EGP 650m; EGX halts trading on El Nasr for Manufacturing Agricultural Crops
  - Consortium offers to acquire controlling stake in El Nasr for Agricultural Crops: https://english.mubasher.info/news/3749421/Consortium-offers-to-acquire-controlling-stake-in-El-Nasr-for-Agricultural-Crops/
  - El Nasr for Agricultural Crops to sell Sohag factory land for EGP 650m: https://english.mubasher.info/news/3685533/El-Nasr-for-Agricultural-Crops-to-sell-Sohag-factory-land-for-EGP-650m/
  - EGX halts trading on El Nasr for Manufacturing Agricultural Crops: https://english.mubasher.info/news/3489525/EGX-halts-trading-on-El-Nasr-for-Manufacturing-Agricultural-Crops/
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- COMI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Commercial International Bank Egypt summary=Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- EAST.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Eastern Company summary=Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.

## Warnings
- OpenRouter API error: 404
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- Evidence for ELNA.CA matches the company but no source/report date was detected.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
