# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-09-29T11:36:21.118798+00:00
Generated Cairo: 2026-09-29 14:36
Run timing: target 08:45 Cairo | generated Cairo 2026-09-29 14:36 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-29 14:33

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 170/186
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, September 29
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 5.88% / above MA50 29.41%
- EGX70 regime: BEARISH / above MA20 5.41% / above MA50 18.92%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=433368064.0 spike=0.76 score=9.0
- GTWL.CA: liquidity=424411072.0 spike=3.38 score=7.28
- CCAP.CA: liquidity=362656768.0 spike=0.43 score=21.52
- NIPH.CA: liquidity=163405952.0 spike=1.34 score=8.11
- ETEL.CA: liquidity=155937952.0 spike=0.54 score=24.4

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with weak breadth (sector breadth 0%), triggering a defensive risk mode that blocks new buys; the scanner therefore holds and highlights a few tickets with constructive or bullish‑watch outlooks, though liquidity is cooling and technical extremes suggest caution.
- Tickets were prioritized by rank score and sector strength (Telecom, Energy & Petrochemicals, Investment Holding) despite the overall bearish regime.
- Liquidity remains tradeable but is cooling (liquidity spikes <0.6), keeping support/resistance distances tight and limiting near‑term upside.
- Sector outlook shows Telecommunications with a positive 20‑day median return, yet zero sector breadth means any strength may be isolated and short‑lived.
- EGX30/EGX70 trend is bearish, below MA20 and MA50, so risk mode is DEFENSIVE_NO_NEW_BUY, which overrides individual ticket outlooks for new entries.
- Uncertainty remains from cooling liquidity and overbought RSI readings on some stocks, raising the chance of a pullback in the next 1‑3 days.

## Top Liquidity Spikes
- EGSA.CA: spike=3.76 liquidity=29497.65 outlook=WEAK_OR_RISKY score=4.05 buy_ready=False
- UEFM.CA: spike=3.55 liquidity=10868695.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GTWL.CA: spike=3.38 liquidity=424411072.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RAKT.CA: spike=3.19 liquidity=530176.88 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CPCI.CA: spike=2.53 liquidity=7795760.5 outlook=CONSTRUCTIVE score=54 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=8.05 5d=-0.2% 20d=9.54% aboveMA50=50.0%
- #2 Energy & Petrochemicals: score=4.25 5d=-0.57% 20d=3.34% aboveMA50=66.67%
- #3 Investment Holding: score=3.79 5d=-6.17% 20d=7.69% aboveMA50=66.67%
- #4 Education: score=1.79 5d=-5.78% 20d=8.12% aboveMA50=66.67%
- #5 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #6 Transportation & Logistics: score=0.35 5d=-6.62% 20d=-3.58% aboveMA50=50.0%
- #7 Banking & Financials: score=0.01 5d=-4.11% 20d=-2.48% aboveMA50=40.0%
- #8 Tourism & Leisure: score=-0.23 5d=-0.75% 20d=-6.7% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- BINV.CA: BULLISH_WATCH score=83.79 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- CCAP.CA: BULLISH_WATCH score=83.79 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- CANA.CA: BULLISH_WATCH score=76.01 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ALCN.CA: CONSTRUCTIVE score=64.35 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ETEL.CA: CONSTRUCTIVE score=60.05 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; overheated RSI
- TALM.CA: CONSTRUCTIVE score=59.79 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; below MA20
- EXPA.CA: CONSTRUCTIVE score=58.01 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; below MA20
- SNFC.CA: CONSTRUCTIVE score=57 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; momentum is extended; sector is not leading
- CPCI.CA: CONSTRUCTIVE score=54 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=overheated RSI; close to resistance; sector is not leading
- CIRA.CA: CONSTRUCTIVE score=53.79 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; below MA20

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- EFID.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=4.5 buy_ready=False sector_rank=16 price=253.24 support=240.1 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=18.56 liquidity=6976842.0 spike=0.29
- ABUK.CA: score=16.06 buy_ready=False sector_rank=13 price=88.64 support=80.7 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.46 liquidity=35789480.0 spike=0.2
- ACAMD.CA: score=7.52 buy_ready=False sector_rank=16 price=2.03 support=1.87 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.09 liquidity=44482304.0 spike=0.87
- ACGC.CA: score=11.49 buy_ready=False sector_rank=10 price=13.95 support=13.11 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=25.89 liquidity=13075790.0 spike=0.52
- ADCI.CA: score=-0.52 buy_ready=False sector_rank=16 price=271.5 support=256.0 resistance=311.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=30.37 liquidity=1955981.88 spike=0.63
- ADIB.CA: score=14.0 buy_ready=False sector_rank=7 price=50.42 support=49.0 resistance=54.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.97 liquidity=36677640.0 spike=0.43
- ADPC.CA: score=2.47 buy_ready=False sector_rank=16 price=3.49 support=3.4 resistance=4.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=23.26 liquidity=5950276.0 spike=0.31
- AFDI.CA: score=1.61 buy_ready=False sector_rank=16 price=49.9 support=48.03 resistance=57.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=33.09 liquidity=4088841.25 spike=0.39
- AFMC.CA: score=2.52 buy_ready=False sector_rank=16 price=151.0 support=133.17 resistance=153.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42806504.0 spike=0.85
- AJWA.CA: score=9.05 buy_ready=False sector_rank=16 price=179.25 support=175.15 resistance=188.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=47.0 liquidity=4529067.0 spike=0.26
- ALCN.CA: score=19.14 buy_ready=False sector_rank=6 price=33.8 support=30.16 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.87 liquidity=21710426.0 spike=0.57
- ALUM.CA: score=1.58 buy_ready=False sector_rank=16 price=22.58 support=21.65 resistance=30.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=16.94 liquidity=4063651.5 spike=0.64
- AMER.CA: score=3.02 buy_ready=False sector_rank=14 price=4.29 support=4.21 resistance=4.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=34395056.0 spike=0.79
- AMES.CA: score=6.52 buy_ready=False sector_rank=16 price=42.98 support=40.15 resistance=126.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=16.63 liquidity=57777440.0 spike=0.21
- AMIA.CA: score=12.26 buy_ready=False sector_rank=16 price=18.3 support=17.12 resistance=21.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.52 liquidity=6741917.5 spike=0.21
- AMOC.CA: score=20.7 buy_ready=False sector_rank=2 price=13.37 support=12.18 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.22 liquidity=86017088.0 spike=0.54
- APSW.CA: score=-2.98 buy_ready=False sector_rank=16 price=8.03 support=7.81 resistance=8.75 source=Yahoo Finance as_of=2026-09-27T21:00:00+00:00 freshness=FRESH RSI=26.81 liquidity=499811.27 spike=0.67
- ARAB.CA: score=7.02 buy_ready=False sector_rank=14 price=0.22 support=0.2 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=23.88 liquidity=34563384.0 spike=0.45
- ARCC.CA: score=7.4 buy_ready=False sector_rank=21 price=62.64 support=60.01 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=8.41 liquidity=14956808.0 spike=0.53
- AREH.CA: score=4.41 buy_ready=False sector_rank=16 price=1.2 support=1.2 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=10.81 liquidity=7886249.0 spike=0.58
- ASCM.CA: score=1.35 buy_ready=False sector_rank=16 price=56.36 support=56.1 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=16.64 liquidity=3832485.5 spike=0.23
- ASPI.CA: score=6.52 buy_ready=False sector_rank=16 price=0.34 support=0.34 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=21.74 liquidity=12412827.0 spike=0.23
- ATLC.CA: score=1.27 buy_ready=False sector_rank=19 price=5.45 support=5.41 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.62 liquidity=3866201.5 spike=0.13
- ATQA.CA: score=16.06 buy_ready=False sector_rank=13 price=11.45 support=11.05 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.46 liquidity=22819306.0 spike=0.23
- AXPH.CA: score=8.97 buy_ready=False sector_rank=16 price=1541.15 support=1334.35 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=28.58 liquidity=8014698.0 spike=1.22
- BINV.CA: score=21.52 buy_ready=False sector_rank=3 price=57.92 support=49.51 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=61.46 liquidity=10565926.0 spike=0.48
- BIOC.CA: score=4.96 buy_ready=False sector_rank=16 price=267.04 support=235.53 resistance=275.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=132573600.0 spike=2.22
- BTFH.CA: score=6.54 buy_ready=False sector_rank=19 price=2.7 support=2.65 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.19 liquidity=95983120.0 spike=1.07
- CAED.CA: score=2.52 buy_ready=False sector_rank=16 price=112.0 support=105.03 resistance=118.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14891494.0 spike=0.76
- CANA.CA: score=21.0 buy_ready=False sector_rank=7 price=45.14 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.04 liquidity=13814257.0 spike=0.56
- CCAP.CA: score=21.52 buy_ready=False sector_rank=3 price=6.78 support=5.85 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=61.93 liquidity=362656768.0 spike=0.43
- CCRS.CA: score=10.44 buy_ready=False sector_rank=16 price=2.3 support=2.23 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.96 liquidity=7916362.0 spike=0.4
- CEFM.CA: score=-2.86 buy_ready=False sector_rank=16 price=134.12 support=127.15 resistance=145.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4620206.0 spike=0.6
- CERA.CA: score=6.52 buy_ready=False sector_rank=16 price=1.2 support=1.18 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=21.25 liquidity=57602424.0 spike=0.39
- CFGH.CA: score=-3.47 buy_ready=False sector_rank=16 price=0.11 support=0.11 resistance=0.12 source=Yahoo Finance as_of=2026-09-27T21:00:00+00:00 freshness=FRESH RSI=8.33 liquidity=13449.59 spike=0.95
- CICH.CA: score=-0.21 buy_ready=False sector_rank=19 price=11.41 support=10.75 resistance=13.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=28.22 liquidity=2389167.75 spike=0.38
- CIEB.CA: score=4.75 buy_ready=False sector_rank=7 price=23.59 support=23.7 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.44 liquidity=5747804.0 spike=0.43
- CIRA.CA: score=16.65 buy_ready=False sector_rank=4 price=38.23 support=33.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.15 liquidity=8934347.0 spike=0.23
- CLHO.CA: score=7.43 buy_ready=False sector_rank=17 price=15.3 support=13.9 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=16.8 liquidity=19967746.0 spike=0.3
- CNFN.CA: score=0.71 buy_ready=False sector_rank=19 price=3.96 support=3.84 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=13.45 liquidity=4313766.0 spike=0.39
- COMI.CA: score=9.0 buy_ready=False sector_rank=7 price=128.08 support=126.81 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.56 liquidity=433368064.0 spike=0.76
- COPR.CA: score=7.52 buy_ready=False sector_rank=16 price=0.45 support=0.44 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.06 liquidity=12296225.0 spike=0.39
- COSG.CA: score=6.52 buy_ready=False sector_rank=16 price=1.52 support=1.51 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=16.67 liquidity=10448453.0 spike=0.38
- CPCI.CA: score=16.38 buy_ready=False sector_rank=16 price=575.51 support=530.0 resistance=584.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=70.88 liquidity=7795760.5 spike=2.53
- CSAG.CA: score=4.61 buy_ready=False sector_rank=6 price=35.29 support=35.01 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=21.68 liquidity=5465907.0 spike=0.38
- DAPH.CA: score=7.52 buy_ready=False sector_rank=16 price=94.19 support=91.65 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=11.0 liquidity=19981584.0 spike=0.58
- DEIN.CA: score=5.52 buy_ready=False sector_rank=16 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=2.28 buy_ready=False sector_rank=15 price=24.68 support=24.01 resistance=29.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=21.84 liquidity=5480558.0 spike=1.08
- DSCW.CA: score=6.52 buy_ready=False sector_rank=16 price=1.7 support=1.67 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=14.71 liquidity=15604661.0 spike=0.73
- DTPP.CA: score=15.52 buy_ready=False sector_rank=16 price=291.17 support=290.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.4 liquidity=35158908.0 spike=0.42
- EALR.CA: score=-1.18 buy_ready=False sector_rank=16 price=331.76 support=322.52 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=20.63 liquidity=2299257.5 spike=0.18
- EASB.CA: score=6.04 buy_ready=False sector_rank=16 price=7.1 support=6.04 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.87 liquidity=3521143.75 spike=0.23
- EAST.CA: score=6.84 buy_ready=False sector_rank=15 price=29.0 support=29.55 resistance=36.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=3.42 liquidity=48524688.0 spike=1.1
- EBSC.CA: score=-1.7 buy_ready=False sector_rank=16 price=1.7 support=1.65 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=28.74 liquidity=1780578.88 spike=0.23
- ECAP.CA: score=-1.74 buy_ready=False sector_rank=16 price=30.0 support=29.13 resistance=34.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=21.04 liquidity=1737409.88 spike=0.24
- EDFM.CA: score=0.0 buy_ready=False sector_rank=16 price=387.28 support=354.0 resistance=465.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=25.24 liquidity=2081691.5 spike=1.2
- EEII.CA: score=11.3 buy_ready=False sector_rank=16 price=2.09 support=2.06 resistance=2.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.66 liquidity=7783876.5 spike=0.67
- EFIC.CA: score=7.06 buy_ready=False sector_rank=13 price=160.88 support=147.0 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=7.94 liquidity=25119092.0 spike=0.07
- EFIH.CA: score=8.38 buy_ready=False sector_rank=11 price=22.3 support=20.2 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=33.64 liquidity=24491686.0 spike=0.45
- EGAL.CA: score=11.06 buy_ready=False sector_rank=13 price=342.53 support=340.0 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.42 liquidity=27379896.0 spike=0.46
- EGAS.CA: score=12.9 buy_ready=False sector_rank=2 price=55.84 support=53.62 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.11 liquidity=5204748.0 spike=0.4
- EGBE.CA: score=4.01 buy_ready=False sector_rank=7 price=0.51 support=0.49 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=7247.65 spike=0.08
- EGCH.CA: score=13.06 buy_ready=False sector_rank=13 price=13.47 support=13.4 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.41 liquidity=62713240.0 spike=0.46
- EGSA.CA: score=9.43 buy_ready=False sector_rank=1 price=8.85 support=8.82 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=28 September 12:29 PM market time freshness=DELAYED_CURRENT RSI=17.24 liquidity=29497.65 spike=3.76
- EGTS.CA: score=17.02 buy_ready=False sector_rank=14 price=17.36 support=16.51 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=59.56 liquidity=11941392.0 spike=0.34
- EHDR.CA: score=5.95 buy_ready=False sector_rank=16 price=2.44 support=2.43 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=12.86 liquidity=8427596.0 spike=0.49
- ELEC.CA: score=6.4 buy_ready=False sector_rank=18 price=1.8 support=1.72 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=22.22 liquidity=25464740.0 spike=0.32
- ELKA.CA: score=3.07 buy_ready=False sector_rank=16 price=1.49 support=1.43 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=9.09 liquidity=6548622.5 spike=0.25
- ELNA.CA: score=-3.37 buy_ready=False sector_rank=16 price=35.22 support=33.46 resistance=38.99 source=Yahoo Finance as_of=2026-09-27T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=106787.04 spike=0.31
- ELSH.CA: score=6.53 buy_ready=False sector_rank=16 price=11.2 support=10.8 resistance=14.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=15.95 liquidity=9011593.0 spike=0.3
- ELWA.CA: score=-2.96 buy_ready=False sector_rank=16 price=1.51 support=1.55 resistance=1.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=6.67 liquidity=522967.78 spike=0.46
- EMFD.CA: score=8.02 buy_ready=False sector_rank=14 price=12.23 support=12.0 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.22 liquidity=40127884.0 spike=0.32
- ENGC.CA: score=2.52 buy_ready=False sector_rank=16 price=35.96 support=35.7 resistance=39.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15994737.0 spike=0.89
- EOSB.CA: score=7.54 buy_ready=False sector_rank=16 price=1.57 support=1.53 resistance=1.64 source=Yahoo Finance as_of=2026-09-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=23771.37 spike=0.38
- EPCO.CA: score=-0.48 buy_ready=False sector_rank=16 price=9.8 support=9.25 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.73 liquidity=1995627.38 spike=0.13
- EPPK.CA: score=-7.06 buy_ready=False sector_rank=16 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=24.4 buy_ready=False sector_rank=1 price=134.0 support=112.5 resistance=140.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=74.45 liquidity=155937952.0 spike=0.54
- ETRS.CA: score=7.6 buy_ready=False sector_rank=16 price=9.99 support=10.02 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=20.51 liquidity=12685720.0 spike=1.04
- EXPA.CA: score=19.0 buy_ready=False sector_rank=7 price=21.3 support=20.6 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.4 liquidity=11970374.0 spike=0.33
- FAIT.CA: score=4.27 buy_ready=False sector_rank=7 price=43.58 support=38.48 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=27.29 liquidity=2264330.0 spike=0.41
- FAITA.CA: score=3.03 buy_ready=False sector_rank=7 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=25148.02 spike=0.7
- FERC.CA: score=-1.31 buy_ready=False sector_rank=13 price=73.74 support=70.42 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=33.78 liquidity=1628320.75 spike=0.12
- FWRY.CA: score=7.38 buy_ready=False sector_rank=11 price=18.24 support=17.5 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=11.19 liquidity=30752562.0 spike=0.29
- GBCO.CA: score=13.34 buy_ready=False sector_rank=12 price=29.46 support=27.0 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.13 liquidity=11485121.0 spike=0.15
- GDWA.CA: score=6.52 buy_ready=False sector_rank=16 price=0.65 support=0.61 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=7.03 liquidity=16322349.0 spike=0.38
- GGCC.CA: score=6.63 buy_ready=False sector_rank=16 price=0.67 support=0.67 resistance=0.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=21.75 liquidity=9112010.0 spike=0.45
- GIHD.CA: score=15.52 buy_ready=False sector_rank=16 price=66.89 support=66.1 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.19 liquidity=18294170.0 spike=0.63
- GMCI.CA: score=-2.95 buy_ready=False sector_rank=16 price=1.5 support=1.56 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=10.26 liquidity=494315.53 spike=1.02
- GRCA.CA: score=0.69 buy_ready=False sector_rank=16 price=34.01 support=32.11 resistance=63.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=11.94 liquidity=4170317.75 spike=0.12
- GSSC.CA: score=0.19 buy_ready=False sector_rank=16 price=263.85 support=246.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=31.66 liquidity=2665054.25 spike=0.34
- GTWL.CA: score=7.28 buy_ready=False sector_rank=16 price=151.96 support=151.96 resistance=199.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=424411072.0 spike=3.38
- HDBK.CA: score=16.0 buy_ready=False sector_rank=7 price=107.34 support=102.5 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.2 liquidity=14355945.0 spike=0.27
- HELI.CA: score=13.02 buy_ready=False sector_rank=14 price=7.31 support=7.02 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.74 liquidity=39132724.0 spike=0.25
- HRHO.CA: score=6.4 buy_ready=False sector_rank=19 price=23.59 support=23.02 resistance=26.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=9.56 liquidity=47384088.0 spike=0.61
- ICID.CA: score=11.42 buy_ready=False sector_rank=16 price=17.6 support=16.52 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.71 liquidity=5903310.5 spike=0.64
- IDRE.CA: score=7.21 buy_ready=False sector_rank=16 price=45.76 support=45.0 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.31 liquidity=4687723.0 spike=0.28
- IFAP.CA: score=2.78 buy_ready=False sector_rank=9 price=19.09 support=17.17 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=24.95 liquidity=5185567.5 spike=0.29
- INFI.CA: score=7.8 buy_ready=False sector_rank=16 price=116.5 support=104.0 resistance=160.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=17.79 liquidity=19716136.0 spike=1.14
- IRON.CA: score=1.99 buy_ready=False sector_rank=13 price=26.09 support=25.82 resistance=30.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.2 liquidity=4926146.0 spike=0.37
- ISMA.CA: score=7.52 buy_ready=False sector_rank=16 price=23.92 support=24.51 resistance=37.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=22.33 liquidity=11230304.0 spike=0.68
- ISMQ.CA: score=7.06 buy_ready=False sector_rank=13 price=7.77 support=7.7 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=16.67 liquidity=22003320.0 spike=0.88
- ISPH.CA: score=7.43 buy_ready=False sector_rank=17 price=11.71 support=11.22 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.75 liquidity=44386816.0 spike=0.65
- JUFO.CA: score=6.64 buy_ready=False sector_rank=15 price=24.92 support=24.5 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.54 liquidity=13065733.0 spike=0.65
- KABO.CA: score=10.45 buy_ready=False sector_rank=10 price=8.32 support=8.2 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.35 liquidity=6965781.5 spike=0.21
- KWIN.CA: score=1.63 buy_ready=False sector_rank=16 price=77.57 support=74.0 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=27.88 liquidity=4108228.5 spike=0.18
- KZPC.CA: score=8.99 buy_ready=False sector_rank=16 price=12.9 support=12.8 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.98 liquidity=8468304.0 spike=0.28
- LCSW.CA: score=2.14 buy_ready=False sector_rank=21 price=29.94 support=29.2 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=15.12 liquidity=4736605.5 spike=0.21
- LUTS.CA: score=12.52 buy_ready=False sector_rank=16 price=0.82 support=0.72 resistance=1.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.78 liquidity=77908088.0 spike=0.7
- MAAL.CA: score=17.52 buy_ready=False sector_rank=16 price=10.79 support=8.18 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=70.42 liquidity=12804566.0 spike=0.55
- MASR.CA: score=7.52 buy_ready=False sector_rank=16 price=7.31 support=6.82 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=13.33 liquidity=53031924.0 spike=0.56
- MBSC.CA: score=8.42 buy_ready=False sector_rank=21 price=300.38 support=295.22 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=10.5 liquidity=65130356.0 spike=1.51
- MCQE.CA: score=7.4 buy_ready=False sector_rank=21 price=183.37 support=180.04 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=10.83 liquidity=16645881.0 spike=0.7
- MCRO.CA: score=7.52 buy_ready=False sector_rank=16 price=1.45 support=1.41 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.19 liquidity=49119444.0 spike=0.39
- MENA.CA: score=-1.35 buy_ready=False sector_rank=14 price=6.2 support=5.8 resistance=7.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.09 liquidity=625966.13 spike=0.45
- MEPA.CA: score=3.35 buy_ready=False sector_rank=16 price=1.6 support=1.61 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=13.56 liquidity=6830557.0 spike=0.18
- MFPC.CA: score=16.06 buy_ready=False sector_rank=13 price=46.06 support=41.56 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.02 liquidity=30121670.0 spike=0.18
- MFSC.CA: score=4.77 buy_ready=False sector_rank=16 price=47.72 support=45.22 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.04 liquidity=2254522.5 spike=0.5
- MHOT.CA: score=14.91 buy_ready=False sector_rank=8 price=17.25 support=16.61 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.22 liquidity=16241035.0 spike=0.94
- MICH.CA: score=7.66 buy_ready=False sector_rank=16 price=42.97 support=43.5 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=23.0 liquidity=14098203.0 spike=1.07
- MILS.CA: score=7.52 buy_ready=False sector_rank=16 price=180.14 support=165.5 resistance=232.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=18.07 liquidity=17089498.0 spike=0.93
- MIPH.CA: score=5.91 buy_ready=False sector_rank=17 price=786.76 support=700.2 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=48.27 liquidity=3478119.5 spike=0.36
- MOED.CA: score=6.52 buy_ready=False sector_rank=16 price=0.63 support=0.62 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=10.48 liquidity=11760664.0 spike=0.22
- MOIL.CA: score=12.36 buy_ready=False sector_rank=2 price=0.71 support=0.67 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=81.03 liquidity=277216.28 spike=1.19
- MOIN.CA: score=5.96 buy_ready=False sector_rank=16 price=34.86 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.96 liquidity=5437174.5 spike=0.18
- MOSC.CA: score=0.31 buy_ready=False sector_rank=16 price=271.33 support=257.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=9.65 liquidity=2785707.0 spike=0.7
- MPCI.CA: score=7.52 buy_ready=False sector_rank=16 price=339.43 support=341.01 resistance=472.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=12.77 liquidity=115465136.0 spike=0.97
- MPCO.CA: score=16.6 buy_ready=False sector_rank=9 price=2.37 support=2.07 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.26 liquidity=103816232.0 spike=0.56
- MPRC.CA: score=7.52 buy_ready=False sector_rank=16 price=38.0 support=37.65 resistance=44.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.97 liquidity=14802252.0 spike=0.46
- MTIE.CA: score=7.34 buy_ready=False sector_rank=12 price=7.82 support=7.5 resistance=8.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=21.77 liquidity=16711343.0 spike=0.7
- NAHO.CA: score=5.53 buy_ready=False sector_rank=16 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance as_of=2026-09-27T21:00:00+00:00 freshness=FRESH RSI=40.0 liquidity=7671.55 spike=0.15
- NCCW.CA: score=15.52 buy_ready=False sector_rank=16 price=6.95 support=5.83 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=43768320.0 spike=0.55
- NEDA.CA: score=-2.16 buy_ready=False sector_rank=16 price=2.66 support=2.48 resistance=2.89 source=Yahoo Finance as_of=2026-09-27T21:00:00+00:00 freshness=FRESH RSI=30.61 liquidity=317904.59 spike=0.34
- NHPS.CA: score=4.88 buy_ready=False sector_rank=16 price=69.68 support=70.8 resistance=91.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.43 liquidity=8364158.0 spike=0.57
- NINH.CA: score=7.52 buy_ready=False sector_rank=16 price=19.32 support=18.53 resistance=24.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=16.67 liquidity=16422635.0 spike=0.98
- NIPH.CA: score=8.11 buy_ready=False sector_rank=17 price=305.64 support=290.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=33.96 liquidity=163405952.0 spike=1.34
- OBRI.CA: score=6.48 buy_ready=False sector_rank=16 price=24.07 support=24.0 resistance=34.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=9.54 liquidity=9964072.0 spike=0.76
- OCDI.CA: score=3.02 buy_ready=False sector_rank=14 price=25.0 support=24.5 resistance=27.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=60509052.0 spike=0.94
- OCPH.CA: score=3.06 buy_ready=False sector_rank=16 price=208.47 support=190.0 resistance=263.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=17.08 liquidity=6121810.5 spike=1.21
- ODIN.CA: score=3.45 buy_ready=False sector_rank=16 price=2.46 support=2.35 resistance=3.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=26.73 liquidity=5929532.0 spike=0.42
- OFH.CA: score=7.52 buy_ready=False sector_rank=16 price=0.87 support=0.83 resistance=1.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=23.91 liquidity=39419156.0 spike=0.3
- OIH.CA: score=11.52 buy_ready=False sector_rank=3 price=1.79 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.0 liquidity=109225512.0 spike=0.98
- OLFI.CA: score=2.93 buy_ready=False sector_rank=15 price=22.04 support=21.2 resistance=23.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=31.39 liquidity=6298409.5 spike=0.37
- ORAS.CA: score=4.6 buy_ready=False sector_rank=5 price=777.66 support=776.0 resistance=805.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=92314456.0 spike=1.0
- ORHD.CA: score=8.02 buy_ready=False sector_rank=14 price=38.79 support=38.02 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.5 liquidity=81493536.0 spike=0.48
- ORWE.CA: score=16.49 buy_ready=False sector_rank=10 price=26.8 support=26.01 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.1 liquidity=24942228.0 spike=0.44
- PHAR.CA: score=8.77 buy_ready=False sector_rank=17 price=108.0 support=102.0 resistance=133.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=14.63 liquidity=137291984.0 spike=1.67
- PHDC.CA: score=8.02 buy_ready=False sector_rank=14 price=12.88 support=12.5 resistance=15.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=12.45 liquidity=62942524.0 spike=0.45
- PHTV.CA: score=3.24 buy_ready=False sector_rank=16 price=331.71 support=320.11 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.87 liquidity=723792.94 spike=0.44
- POUL.CA: score=7.66 buy_ready=False sector_rank=15 price=9.77 support=9.12 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=5.69 liquidity=42098316.0 spike=1.51
- PRCL.CA: score=-2.68 buy_ready=False sector_rank=21 price=25.04 support=24.25 resistance=27.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4924791.5 spike=0.29
- PRDC.CA: score=8.02 buy_ready=False sector_rank=14 price=7.2 support=6.81 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=17.09 liquidity=32551096.0 spike=0.67
- PRMH.CA: score=5.03 buy_ready=False sector_rank=16 price=2.24 support=2.2 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=25.81 liquidity=7071090.5 spike=1.22
- RACC.CA: score=-0.5 buy_ready=False sector_rank=16 price=9.1 support=8.51 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=22.11 liquidity=2977414.25 spike=0.22
- RAKT.CA: score=1.43 buy_ready=False sector_rank=16 price=21.32 support=21.2 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=30.86 liquidity=530176.88 spike=3.19
- RAYA.CA: score=7.4 buy_ready=False sector_rank=20 price=6.14 support=5.72 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=16.67 liquidity=38060156.0 spike=0.72
- RMDA.CA: score=7.43 buy_ready=False sector_rank=17 price=5.29 support=4.83 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=12.67 liquidity=29904798.0 spike=0.5
- ROTO.CA: score=2.05 buy_ready=False sector_rank=16 price=38.63 support=35.02 resistance=45.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.25 liquidity=4525482.0 spike=0.56
- RREI.CA: score=-4.65 buy_ready=False sector_rank=16 price=3.64 support=3.6 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2825932.0 spike=0.19
- RTVC.CA: score=1.12 buy_ready=False sector_rank=16 price=3.41 support=3.43 resistance=4.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=20.0 liquidity=3803677.5 spike=1.4
- RUBX.CA: score=2.52 buy_ready=False sector_rank=16 price=14.19 support=14.16 resistance=15.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=49209724.0 spike=0.75
- SAUD.CA: score=12.86 buy_ready=False sector_rank=7 price=22.02 support=21.6 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.54 liquidity=8859382.0 spike=0.43
- SCEM.CA: score=7.4 buy_ready=False sector_rank=21 price=76.95 support=76.01 resistance=105.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=4.19 liquidity=24100636.0 spike=0.3
- SCFM.CA: score=0.67 buy_ready=False sector_rank=16 price=250.72 support=223.11 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=15.65 liquidity=4151898.5 spike=0.68
- SCTS.CA: score=0.44 buy_ready=False sector_rank=4 price=543.3 support=520.3 resistance=639.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=17.03 liquidity=724842.44 spike=0.32
- SDTI.CA: score=16.52 buy_ready=False sector_rank=16 price=84.02 support=68.57 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=77.45 liquidity=17350132.0 spike=0.51
- SEIG.CA: score=-2.09 buy_ready=False sector_rank=16 price=218.01 support=211.15 resistance=268.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=28.8 liquidity=385021.84 spike=0.21
- SIPC.CA: score=2.52 buy_ready=False sector_rank=16 price=4.92 support=4.5 resistance=4.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=44134652.0 spike=0.62
- SKPC.CA: score=7.06 buy_ready=False sector_rank=13 price=15.92 support=15.7 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.04 liquidity=96259480.0 spike=0.71
- SMFR.CA: score=-1.72 buy_ready=False sector_rank=16 price=217.04 support=205.01 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=9.13 liquidity=757463.5 spike=0.11
- SNFC.CA: score=14.63 buy_ready=False sector_rank=16 price=11.42 support=10.26 resistance=11.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=66.46 liquidity=7106305.5 spike=0.5
- SPIN.CA: score=6.34 buy_ready=False sector_rank=10 price=16.13 support=15.11 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=18.11 liquidity=7770751.5 spike=1.04
- SPMD.CA: score=11.41 buy_ready=False sector_rank=16 price=0.37 support=0.37 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.01 liquidity=9892715.0 spike=0.13
- SUGR.CA: score=5.21 buy_ready=False sector_rank=15 price=52.99 support=51.2 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.07 liquidity=7578219.5 spike=0.25
- SVCE.CA: score=7.52 buy_ready=False sector_rank=16 price=9.73 support=9.6 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=10.4 liquidity=60694408.0 spike=0.31
- SWDY.CA: score=7.6 buy_ready=False sector_rank=18 price=107.97 support=108.01 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=11.28 liquidity=70501792.0 spike=1.1
- TALM.CA: score=17.72 buy_ready=False sector_rank=4 price=19.6 support=17.61 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.61 liquidity=29875540.0 spike=0.46
- TMGH.CA: score=7.02 buy_ready=False sector_rank=14 price=87.21 support=86.1 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=14.82 liquidity=137024032.0 spike=0.5
- TRTO.CA: score=-2.48 buy_ready=False sector_rank=16 price=0.05 support=0.05 resistance=0.08 source=Yahoo Finance as_of=2026-09-27T21:00:00+00:00 freshness=FRESH RSI=12.0 liquidity=3716.5 spike=0.13
- UEFM.CA: score=7.52 buy_ready=False sector_rank=16 price=509.46 support=437.5 resistance=509.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10868695.0 spike=3.55
- UEGC.CA: score=6.52 buy_ready=False sector_rank=16 price=1.43 support=1.42 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=21.82 liquidity=22331890.0 spike=0.52
- UNIP.CA: score=2.5 buy_ready=False sector_rank=16 price=0.32 support=0.32 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=20.59 liquidity=5977074.5 spike=0.29
- UNIT.CA: score=13.08 buy_ready=False sector_rank=14 price=17.0 support=16.66 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=41.72 liquidity=14764456.0 spike=1.03
- WCDF.CA: score=4.31 buy_ready=False sector_rank=16 price=625.44 support=575.5 resistance=796.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.96 liquidity=6411452.0 spike=1.19
- WKOL.CA: score=6.52 buy_ready=False sector_rank=16 price=291.32 support=293.03 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=20.92 liquidity=10624949.0 spike=0.79
- ZEOT.CA: score=2.77 buy_ready=False sector_rank=16 price=11.26 support=10.6 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=13.13 liquidity=5249810.5 spike=0.86
- ZMID.CA: score=3.02 buy_ready=False sector_rank=14 price=7.41 support=7.3 resistance=7.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=70262696.0 spike=0.41

## Backtesting Lite
- ETEL.CA: 180d return=101.7%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-09-27T21:00:00+00:00
- BINV.CA: 180d return=52.39%, max drawdown=-17.77%, MA20>MA50 days last20=20, as_of=2026-09-27T21:00:00+00:00
- CCAP.CA: 180d return=99.7%, max drawdown=-17.02%, MA20>MA50 days last20=20, as_of=2026-09-27T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- CANA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=636 sources=3 expected=Suez Canal Bank summary=Suez Canal Bank delivers EGP 1.6bn profits in Q1-26; Suez Canal Bank unveils details for previous dividends payout; Suez Canal Bank to distribute EGP 5bn bonus shares for 2025
  - Suez Canal Bank delivers EGP 1.6bn profits in Q1-26: https://english.mubasher.info/news/4611255/Suez-Canal-Bank-delivers-EGP-1-6bn-profits-in-Q1-26/
  - Suez Canal Bank unveils details for previous dividends payout: https://english.mubasher.info/news/4586807/Suez-Canal-Bank-unveils-details-for-previous-dividends-payout/
  - Suez Canal Bank to distribute EGP 5bn bonus shares for 2025: https://english.mubasher.info/news/4581661/Suez-Canal-Bank-to-distribute-EGP-5bn-bonus-shares-for-2025/
- AMOC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria Mineral Oils summary=AMOC achieves EGP 10.5bn consolidated sales in Q1-26; AMOC studies potential project with Germany’s SULZER; AMOC to pay out EGP 0.4/shr dividends for H2-25
  - AMOC achieves EGP 10.5bn consolidated sales in Q1-26: https://english.mubasher.info/news/4604903/AMOC-achieves-EGP-10-5bn-consolidated-sales-in-Q1-26/
  - AMOC studies potential project with Germany’s SULZER: https://english.mubasher.info/news/4586853/AMOC-studies-potential-project-with-Germany-s-SULZER/
  - AMOC to pay out EGP 0.4/shr dividends for H2-25: https://english.mubasher.info/news/4586775/AMOC-to-pay-out-EGP-0-4-shr-dividends-for-H2-25/
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- EXPA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Export Development Bank of Egypt summary=Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.

## Warnings
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
