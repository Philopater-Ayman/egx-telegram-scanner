# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-09-14T18:11:00.458982+00:00
Generated Cairo: 2026-09-14 21:11
Run timing: target 15:30 Cairo | generated Cairo 2026-09-14 21:11 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-09-14 21:07

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 164/189
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, September 14
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 35.0% / above MA50 50.0%
- EGX70 regime: BEARISH / above MA20 30.56% / above MA50 52.78%
- Sector breadth: 14.29%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=2039000832.0 spike=2.63 score=9.66
- COMI.CA: liquidity=693739008.0 spike=1.4 score=15.95
- CERA.CA: liquidity=392855296.0 spike=5.81 score=9.94
- TALM.CA: liquidity=345841440.0 spike=12.83 score=13.4
- DTPP.CA: liquidity=262243920.0 spike=6.12 score=9.94

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with weak breadth (sector breadth ~14%), putting the scanner in defensive mode that blocks new buys; the top tickets are flagged as bullish watch due to sector strength, liquidity spikes, and proximity to resistance, but the overall market regime limits upside potential.
- Tickets were prioritized for their bullish watch outlook, accumulation or tradeable liquidity regimes, and leadership in Telecommunications, Education, and Textiles sectors despite the bearish EGX30/EGX70 trend.
- Liquidity shows mixed signals—some spikes suggest short‑term interest, while many stocks sit far above 20‑day support and near 20‑day resistance, indicating limited room for gains in the next 1‑3 days and a risk of pullb
- The bearish EGX30/EGX70 regime and low sector breadth shift risk mode to DEFENSIVE_NO_NEW_BUY, so the scanner only advises holding or watching existing positions; uncertainty remains due to overheated RSI readings, cooli

## Top Liquidity Spikes
- UNIT.CA: spike=24.38 liquidity=145631696.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SPMD.CA: spike=14.0 liquidity=154314880.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- TALM.CA: spike=12.83 liquidity=345841440.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DTPP.CA: spike=6.12 liquidity=262243920.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CERA.CA: spike=5.81 liquidity=392855296.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=11.16 5d=4.71% 20d=7.92% aboveMA50=100.0%
- #2 Education: score=10.65 5d=0.0% 20d=0.0% aboveMA50=33.33%
- #3 Textiles: score=9.94 5d=4.06% 20d=13.56% aboveMA50=100.0%
- #4 Investment Holding: score=6.83 5d=3.57% 20d=4.29% aboveMA50=66.67%
- #5 Basic Resources & Chemicals: score=4.49 5d=-2.21% 20d=3.93% aboveMA50=70.0%
- #6 Energy & Petrochemicals: score=4.12 5d=0.0% 20d=0.07% aboveMA50=75.0%
- #7 Banking & Financials: score=2.88 5d=-1.4% 20d=-0.05% aboveMA50=60.0%
- #8 Industrial Goods & Cables: score=2.72 5d=-3.25% 20d=5.64% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CIRA.CA: BULLISH_WATCH score=99 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=far above support; close to resistance
- MOED.CA: BULLISH_WATCH score=84.35 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- KABO.CA: BULLISH_WATCH score=81.94 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; overheated RSI
- SKPC.CA: BULLISH_WATCH score=80.49 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- SNFC.CA: BULLISH_WATCH score=78.35 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance; sector is not leading
- ACGC.CA: BULLISH_WATCH score=77.94 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended; far above support
- ORWE.CA: BULLISH_WATCH score=77.94 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20
- ETEL.CA: BULLISH_WATCH score=75 liquidity=TRADEABLE sector=LEADING risk=overheated RSI
- BINV.CA: BULLISH_WATCH score=74.83 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended
- HELI.CA: BULLISH_WATCH score=73.58 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=12.94 buy_ready=False sector_rank=11 price=311.36 support=295.0 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=24.51 liquidity=11730995.0 spike=0.33
- ABUK.CA: score=20.8 buy_ready=False sector_rank=5 price=89.28 support=75.01 resistance=94.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.87 liquidity=49328600.0 spike=0.29
- ACAMD.CA: score=16.94 buy_ready=False sector_rank=11 price=2.05 support=1.95 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.45 liquidity=38949424.0 spike=0.69
- ACGC.CA: score=24.4 buy_ready=False sector_rank=3 price=14.51 support=11.25 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=62.68 liquidity=31065342.0 spike=0.74
- ADCI.CA: score=6.25 buy_ready=False sector_rank=11 price=275.45 support=280.0 resistance=319.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.68 liquidity=3306852.5 spike=0.41
- ADIB.CA: score=15.31 buy_ready=False sector_rank=7 price=51.3 support=51.15 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.52 liquidity=74943872.0 spike=1.08
- ADPC.CA: score=14.94 buy_ready=False sector_rank=11 price=3.83 support=3.85 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=13835517.0 spike=0.5
- AFDI.CA: score=5.59 buy_ready=False sector_rank=11 price=51.88 support=52.11 resistance=68.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=17.72 liquidity=5649678.0 spike=0.21
- AFMC.CA: score=9.94 buy_ready=False sector_rank=11 price=160.5 support=157.0 resistance=267.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=21.7 liquidity=34529860.0 spike=0.48
- AJWA.CA: score=14.94 buy_ready=False sector_rank=11 price=180.04 support=175.15 resistance=202.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=39.16 liquidity=18009970.0 spike=0.33
- ALCN.CA: score=18.92 buy_ready=False sector_rank=19 price=30.73 support=30.03 resistance=34.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.26 liquidity=11113032.0 spike=0.35
- ALUM.CA: score=4.94 buy_ready=False sector_rank=11 price=25.48 support=25.34 resistance=27.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10525317.0 spike=0.5
- AMER.CA: score=10.03 buy_ready=False sector_rank=10 price=4.98 support=5.12 resistance=6.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.85 liquidity=39265588.0 spike=0.53
- AMES.CA: score=5.04 buy_ready=False sector_rank=11 price=54.23 support=53.4 resistance=59.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=241686800.0 spike=1.05
- AMIA.CA: score=4.94 buy_ready=False sector_rank=11 price=17.58 support=17.51 resistance=18.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19546502.0 spike=0.28
- AMOC.CA: score=17.65 buy_ready=False sector_rank=6 price=13.09 support=10.3 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=75.7 liquidity=187181936.0 spike=0.96
- APSW.CA: score=4.88 buy_ready=False sector_rank=11 price=8.5 support=8.41 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=39.78 liquidity=941127.13 spike=0.79
- ARAB.CA: score=18.03 buy_ready=False sector_rank=10 price=0.25 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.36 liquidity=84957624.0 spike=0.87
- ARCC.CA: score=17.87 buy_ready=False sector_rank=12 price=72.79 support=71.51 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.5 liquidity=30724460.0 spike=0.36
- AREH.CA: score=16.94 buy_ready=False sector_rank=11 price=1.42 support=1.39 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.16 liquidity=13045154.0 spike=0.73
- ARVA.CA: score=4.94 buy_ready=False sector_rank=11 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=14.94 buy_ready=False sector_rank=11 price=61.01 support=62.01 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.04 liquidity=13419726.0 spike=0.51
- ASPI.CA: score=12.98 buy_ready=False sector_rank=11 price=0.44 support=0.41 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.89 liquidity=53850244.0 spike=1.02
- ATLC.CA: score=19.84 buy_ready=False sector_rank=13 price=6.81 support=5.2 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=12967195.0 spike=0.44
- ATQA.CA: score=17.8 buy_ready=False sector_rank=5 price=12.48 support=10.8 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=82.14 liquidity=75874592.0 spike=0.7
- AXPH.CA: score=10.58 buy_ready=False sector_rank=11 price=1664.97 support=1305.43 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=73.88 liquidity=2639208.0 spike=0.22
- BINV.CA: score=13.12 buy_ready=False sector_rank=4 price=51.76 support=46.25 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=65.86 liquidity=1715054.25 spike=0.15
- BIOC.CA: score=9.94 buy_ready=False sector_rank=11 price=281.55 support=285.0 resistance=555.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=8.94 liquidity=40334596.0 spike=0.27
- BTFH.CA: score=13.84 buy_ready=False sector_rank=13 price=2.89 support=2.91 resistance=3.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.71 liquidity=82236328.0 spike=0.8
- CAED.CA: score=9.94 buy_ready=False sector_rank=11 price=135.59 support=131.0 resistance=150.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=135212144.0 spike=3.52
- CANA.CA: score=18.15 buy_ready=False sector_rank=7 price=41.57 support=41.0 resistance=44.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.8 liquidity=13288325.0 spike=0.76
- CCAP.CA: score=9.66 buy_ready=False sector_rank=4 price=6.84 support=6.25 resistance=6.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2039000832.0 spike=2.63
- CCRS.CA: score=14.94 buy_ready=False sector_rank=11 price=2.45 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=27373970.0 spike=0.55
- CEFM.CA: score=15.31 buy_ready=False sector_rank=11 price=144.98 support=133.1 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=43.38 liquidity=5374856.0 spike=0.35
- CERA.CA: score=9.94 buy_ready=False sector_rank=11 price=1.38 support=1.34 resistance=1.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=392855296.0 spike=5.81
- CFGH.CA: score=7.95 buy_ready=False sector_rank=11 price=0.12 support=0.1 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=8781.11 spike=0.34
- CICH.CA: score=17.73 buy_ready=False sector_rank=13 price=12.55 support=12.0 resistance=13.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=62.81 liquidity=5553481.0 spike=1.17
- CIEB.CA: score=15.31 buy_ready=False sector_rank=7 price=24.4 support=24.3 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.13 liquidity=15883110.0 spike=1.08
- CIRA.CA: score=32.4 buy_ready=False sector_rank=2 price=39.34 support=32.1 resistance=39.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=56.62 liquidity=198532384.0 spike=5.77
- CLHO.CA: score=9.5 buy_ready=False sector_rank=16 price=16.0 support=16.0 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.96 liquidity=51238296.0 spike=0.64
- CNFN.CA: score=6.16 buy_ready=False sector_rank=13 price=4.54 support=4.72 resistance=4.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=33.93 liquidity=7315270.0 spike=0.51
- COMI.CA: score=15.95 buy_ready=False sector_rank=7 price=133.32 support=135.35 resistance=142.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.06 liquidity=693739008.0 spike=1.4
- COPR.CA: score=12.94 buy_ready=False sector_rank=11 price=0.46 support=0.43 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.48 liquidity=33353364.0 spike=0.35
- COSG.CA: score=17.94 buy_ready=False sector_rank=11 price=1.83 support=1.74 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.28 liquidity=22277996.0 spike=0.39
- CPCI.CA: score=6.71 buy_ready=False sector_rank=11 price=530.32 support=525.01 resistance=569.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=26.53 liquidity=3774265.5 spike=0.78
- CSAG.CA: score=12.46 buy_ready=False sector_rank=19 price=38.62 support=38.13 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.24 liquidity=5543412.5 spike=0.28
- DAPH.CA: score=17.94 buy_ready=False sector_rank=11 price=117.41 support=108.11 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=52.07 liquidity=18542172.0 spike=0.29
- DEIN.CA: score=7.94 buy_ready=False sector_rank=11 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=11.38 buy_ready=False sector_rank=17 price=27.23 support=27.79 resistance=29.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.73 liquidity=7082228.0 spike=0.88
- DSCW.CA: score=13.94 buy_ready=False sector_rank=11 price=1.81 support=1.84 resistance=2.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=39253724.0 spike=0.71
- DTPP.CA: score=9.94 buy_ready=False sector_rank=11 price=332.0 support=330.02 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=262243920.0 spike=6.12
- EALR.CA: score=8.31 buy_ready=False sector_rank=11 price=376.03 support=340.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=30.67 liquidity=8373395.5 spike=0.3
- EASB.CA: score=5.24 buy_ready=False sector_rank=11 price=8.72 support=8.54 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18060320.0 spike=1.15
- EAST.CA: score=8.3 buy_ready=False sector_rank=17 price=33.23 support=34.29 resistance=37.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=29.75 liquidity=40815152.0 spike=0.62
- EBSC.CA: score=15.04 buy_ready=False sector_rank=11 price=2.07 support=1.88 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.76 liquidity=3099320.75 spike=0.21
- ECAP.CA: score=2.78 buy_ready=False sector_rank=11 price=32.24 support=31.16 resistance=40.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=29.42 liquidity=2843084.25 spike=0.21
- EDFM.CA: score=11.06 buy_ready=False sector_rank=11 price=411.09 support=394.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=64.44 liquidity=1115534.0 spike=0.57
- EEII.CA: score=4.94 buy_ready=False sector_rank=11 price=2.17 support=2.15 resistance=2.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14096104.0 spike=0.5
- EFIC.CA: score=17.28 buy_ready=False sector_rank=5 price=199.0 support=192.75 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.16 liquidity=117443424.0 spike=1.24
- EFID.CA: score=18.44 buy_ready=False sector_rank=17 price=30.3 support=29.71 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.72 liquidity=87803240.0 spike=1.57
- EFIH.CA: score=14.5 buy_ready=False sector_rank=15 price=22.96 support=22.16 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.62 liquidity=35769800.0 spike=0.45
- EGAL.CA: score=18.8 buy_ready=False sector_rank=5 price=360.9 support=321.01 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=70.98 liquidity=56145572.0 spike=0.39
- EGAS.CA: score=14.78 buy_ready=False sector_rank=6 price=56.12 support=55.21 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.96 liquidity=6131300.0 spike=0.61
- EGBE.CA: score=3.24 buy_ready=False sector_rank=7 price=0.49 support=0.51 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=15.69 liquidity=88136.3 spike=0.54
- EGCH.CA: score=18.8 buy_ready=False sector_rank=5 price=13.72 support=13.3 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=52.4 liquidity=78442056.0 spike=0.59
- EGSA.CA: score=12.31 buy_ready=False sector_rank=1 price=8.98 support=8.66 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=83.67 liquidity=11204.4 spike=1.45
- EGTS.CA: score=17.03 buy_ready=False sector_rank=10 price=16.81 support=16.17 resistance=19.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.57 liquidity=18308878.0 spike=0.64
- EHDR.CA: score=14.94 buy_ready=False sector_rank=11 price=2.83 support=2.81 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.51 liquidity=14248027.0 spike=0.56
- EKHO.CA: score=6.65 buy_ready=False sector_rank=6 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-09-12T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=14.75 buy_ready=False sector_rank=8 price=1.99 support=2.02 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.24 liquidity=89033680.0 spike=1.33
- ELKA.CA: score=14.94 buy_ready=False sector_rank=11 price=1.71 support=1.7 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=48.21 liquidity=43335160.0 spike=0.87
- ELNA.CA: score=-0.96 buy_ready=False sector_rank=11 price=35.74 support=35.17 resistance=38.99 source=Yahoo Finance as_of=2026-09-12T21:00:00+00:00 freshness=FRESH RSI=22.51 liquidity=95425.8 spike=0.21
- ELSH.CA: score=14.94 buy_ready=False sector_rank=11 price=12.84 support=12.97 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=48.39 liquidity=37988248.0 spike=0.91
- ELWA.CA: score=5.98 buy_ready=False sector_rank=11 price=1.72 support=1.62 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=47.69 liquidity=1043497.12 spike=0.41
- EMFD.CA: score=17.03 buy_ready=False sector_rank=10 price=14.21 support=11.51 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=89.83 liquidity=110018232.0 spike=0.69
- ENGC.CA: score=9.73 buy_ready=False sector_rank=11 price=41.53 support=41.8 resistance=54.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.42 liquidity=9787472.0 spike=0.58
- EOSB.CA: score=11.96 buy_ready=False sector_rank=11 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-09-12T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=20235.73 spike=0.35
- EPCO.CA: score=17.94 buy_ready=False sector_rank=11 price=11.0 support=10.8 resistance=12.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=51.0 liquidity=15404424.0 spike=0.7
- EPPK.CA: score=-4.64 buy_ready=False sector_rank=11 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=26.4 buy_ready=False sector_rank=1 price=127.0 support=112.1 resistance=131.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=153461264.0 spike=0.8
- ETRS.CA: score=17.94 buy_ready=False sector_rank=11 price=10.8 support=10.7 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.16 liquidity=11612840.0 spike=0.49
- EXPA.CA: score=20.15 buy_ready=False sector_rank=7 price=20.71 support=19.8 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.66 liquidity=32248488.0 spike=0.87
- FAIT.CA: score=14.22 buy_ready=False sector_rank=7 price=46.01 support=39.58 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.18 liquidity=4066110.75 spike=0.46
- FAITA.CA: score=5.16 buy_ready=False sector_rank=7 price=0.98 support=0.98 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=46.51 liquidity=10860.24 spike=0.2
- FERC.CA: score=19.8 buy_ready=False sector_rank=5 price=78.31 support=76.7 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.57 liquidity=13054769.0 spike=0.63
- FWRY.CA: score=16.5 buy_ready=False sector_rank=15 price=18.99 support=18.66 resistance=19.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.84 liquidity=124094896.0 spike=0.91
- GBCO.CA: score=15.72 buy_ready=False sector_rank=20 price=29.02 support=27.51 resistance=31.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.7 liquidity=28739136.0 spike=0.57
- GDWA.CA: score=13.94 buy_ready=False sector_rank=11 price=0.77 support=0.77 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.45 liquidity=34315408.0 spike=0.81
- GGCC.CA: score=14.94 buy_ready=False sector_rank=11 price=0.86 support=0.83 resistance=1.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.87 liquidity=18926304.0 spike=0.42
- GIHD.CA: score=19.94 buy_ready=False sector_rank=11 price=73.0 support=58.01 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=74.67 liquidity=19917412.0 spike=0.64
- GMCI.CA: score=5.25 buy_ready=False sector_rank=11 price=1.8 support=1.79 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=35.0 liquidity=672799.5 spike=1.32
- GRCA.CA: score=4.94 buy_ready=False sector_rank=11 price=42.01 support=41.41 resistance=48.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=57442964.0 spike=0.76
- GSSC.CA: score=15.27 buy_ready=False sector_rank=11 price=285.74 support=278.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.31 liquidity=5329470.5 spike=0.4
- GTWL.CA: score=17.94 buy_ready=False sector_rank=11 price=236.59 support=133.35 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.58 liquidity=112951096.0 spike=0.37
- HDBK.CA: score=19.15 buy_ready=False sector_rank=7 price=107.63 support=87.45 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.2 liquidity=36527076.0 spike=0.64
- HELI.CA: score=22.03 buy_ready=False sector_rank=10 price=7.96 support=7.34 resistance=8.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.13 liquidity=106163728.0 spike=0.67
- HRHO.CA: score=15.84 buy_ready=False sector_rank=13 price=25.3 support=25.33 resistance=26.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=41.03 liquidity=53618408.0 spike=0.54
- ICID.CA: score=12.2 buy_ready=False sector_rank=11 price=18.11 support=13.4 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=64.78 liquidity=2263440.75 spike=0.08
- IDRE.CA: score=12.94 buy_ready=False sector_rank=11 price=51.35 support=51.02 resistance=57.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.57 liquidity=5002252.0 spike=0.48
- IFAP.CA: score=14.17 buy_ready=False sector_rank=18 price=20.36 support=20.2 resistance=22.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.05 liquidity=13639462.0 spike=0.53
- INFI.CA: score=4.94 buy_ready=False sector_rank=11 price=133.58 support=131.01 resistance=146.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20525362.0 spike=0.48
- IRON.CA: score=11.04 buy_ready=False sector_rank=5 price=27.95 support=27.84 resistance=33.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=7.12 liquidity=22182572.0 spike=1.62
- ISMA.CA: score=14.72 buy_ready=False sector_rank=11 price=29.83 support=29.0 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.94 liquidity=9777238.0 spike=0.35
- ISMQ.CA: score=15.8 buy_ready=False sector_rank=5 price=8.93 support=9.0 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.28 liquidity=22225804.0 spike=0.65
- ISPH.CA: score=9.94 buy_ready=False sector_rank=16 price=12.34 support=12.75 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.17 liquidity=85838344.0 spike=1.22
- JUFO.CA: score=15.3 buy_ready=False sector_rank=17 price=26.62 support=26.45 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=54.37 liquidity=12537262.0 spike=0.47
- KABO.CA: score=24.4 buy_ready=False sector_rank=3 price=9.61 support=8.77 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=71.57 liquidity=38096456.0 spike=0.73
- KWIN.CA: score=14.94 buy_ready=False sector_rank=11 price=86.52 support=84.5 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.6 liquidity=12379135.0 spike=0.19
- KZPC.CA: score=21.94 buy_ready=False sector_rank=11 price=13.89 support=10.48 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=51.86 liquidity=26207076.0 spike=0.4
- LCSW.CA: score=13.31 buy_ready=False sector_rank=12 price=33.74 support=32.61 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=48.41 liquidity=8434727.0 spike=0.27
- LUTS.CA: score=4.94 buy_ready=False sector_rank=11 price=0.9 support=0.87 resistance=0.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=78869536.0 spike=0.29
- MAAL.CA: score=9.94 buy_ready=False sector_rank=11 price=8.57 support=8.18 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.46 liquidity=5004966.5 spike=0.43
- MASR.CA: score=19.56 buy_ready=False sector_rank=11 price=7.91 support=7.49 resistance=8.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.19 liquidity=118290168.0 spike=1.31
- MBSC.CA: score=17.87 buy_ready=False sector_rank=12 price=397.46 support=355.04 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.91 liquidity=18036342.0 spike=0.2
- MCQE.CA: score=17.87 buy_ready=False sector_rank=12 price=217.73 support=212.01 resistance=255.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.82 liquidity=25571154.0 spike=0.48
- MCRO.CA: score=21.36 buy_ready=False sector_rank=11 price=1.73 support=1.44 resistance=1.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.79 liquidity=180932752.0 spike=1.71
- MENA.CA: score=0.92 buy_ready=False sector_rank=10 price=6.64 support=6.58 resistance=7.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=32.14 liquidity=887412.38 spike=0.15
- MEPA.CA: score=21.94 buy_ready=False sector_rank=11 price=1.96 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=62.16 liquidity=30141912.0 spike=0.87
- MFPC.CA: score=17.8 buy_ready=False sector_rank=5 price=47.39 support=38.93 resistance=48.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=80.13 liquidity=103471256.0 spike=0.76
- MFSC.CA: score=11.75 buy_ready=False sector_rank=11 price=49.77 support=48.88 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=3806186.75 spike=0.68
- MHOT.CA: score=13.88 buy_ready=False sector_rank=9 price=17.88 support=17.72 resistance=19.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=4807012.5 spike=0.35
- MICH.CA: score=14.13 buy_ready=False sector_rank=11 price=48.97 support=47.11 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.42 liquidity=6194560.5 spike=0.22
- MILS.CA: score=12.94 buy_ready=False sector_rank=11 price=200.0 support=190.25 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.05 liquidity=15846564.0 spike=0.27
- MIPH.CA: score=11.57 buy_ready=False sector_rank=16 price=807.87 support=700.2 resistance=820.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.98 liquidity=2066028.0 spike=0.5
- MOED.CA: score=21.98 buy_ready=False sector_rank=11 price=0.81 support=0.68 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.41 liquidity=232805472.0 spike=2.02
- MOIL.CA: score=8.85 buy_ready=False sector_rank=6 price=0.67 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=198268.67 spike=0.86
- MOIN.CA: score=4.94 buy_ready=False sector_rank=11 price=34.51 support=34.08 resistance=37.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16491344.0 spike=0.56
- MOSC.CA: score=4.17 buy_ready=False sector_rank=11 price=306.07 support=300.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=32.6 liquidity=1230627.38 spike=0.1
- MPCI.CA: score=17.94 buy_ready=False sector_rank=11 price=407.59 support=345.0 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.17 liquidity=99159792.0 spike=0.59
- MPCO.CA: score=5.05 buy_ready=False sector_rank=18 price=2.56 support=2.53 resistance=2.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=211243152.0 spike=1.44
- MPRC.CA: score=14.94 buy_ready=False sector_rank=11 price=38.99 support=38.6 resistance=46.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.6 liquidity=26180102.0 spike=0.62
- MTIE.CA: score=15.72 buy_ready=False sector_rank=20 price=8.3 support=8.25 resistance=9.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.37 liquidity=24248318.0 spike=0.44
- NAHO.CA: score=-5.04 buy_ready=False sector_rank=11 price=0.13 support=0.13 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16870.88 spike=0.16
- NCCW.CA: score=6.52 buy_ready=False sector_rank=11 price=7.89 support=7.61 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=89744272.0 spike=1.79
- NEDA.CA: score=5.97 buy_ready=False sector_rank=11 price=2.73 support=2.7 resistance=2.97 source=Yahoo Finance as_of=2026-09-12T21:00:00+00:00 freshness=FRESH RSI=43.18 liquidity=965194.24 spike=1.03
- NHPS.CA: score=9.94 buy_ready=False sector_rank=11 price=76.74 support=80.5 resistance=98.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=19.41 liquidity=13615511.0 spike=0.52
- NINH.CA: score=14.94 buy_ready=False sector_rank=11 price=21.55 support=21.53 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.66 liquidity=12058035.0 spike=0.4
- NIPH.CA: score=12.5 buy_ready=False sector_rank=16 price=319.14 support=326.51 resistance=414.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=16.88 liquidity=124125624.0 spike=0.49
- OBRI.CA: score=4.94 buy_ready=False sector_rank=11 price=30.35 support=30.1 resistance=32.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15128504.0 spike=0.69
- OCDI.CA: score=18.65 buy_ready=False sector_rank=10 price=30.5 support=30.03 resistance=35.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.73 liquidity=120048624.0 spike=1.31
- OCPH.CA: score=4.65 buy_ready=False sector_rank=11 price=244.55 support=242.0 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.32 liquidity=3708270.75 spike=0.3
- ODIN.CA: score=9.94 buy_ready=False sector_rank=11 price=2.71 support=2.55 resistance=3.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=28.05 liquidity=11731197.0 spike=0.35
- OFH.CA: score=17.94 buy_ready=False sector_rank=11 price=1.07 support=0.86 resistance=1.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=69.62 liquidity=67109152.0 spike=0.6
- OIH.CA: score=23.4 buy_ready=False sector_rank=4 price=2.12 support=1.75 resistance=2.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.14 liquidity=49137916.0 spike=0.36
- OLFI.CA: score=9.3 buy_ready=False sector_rank=17 price=22.2 support=22.07 resistance=25.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=34.56 liquidity=13589931.0 spike=0.29
- ORAS.CA: score=4.6 buy_ready=False sector_rank=14 price=850.79 support=845.0 resistance=868.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=152856512.0 spike=1.0
- ORHD.CA: score=20.03 buy_ready=False sector_rank=10 price=42.26 support=40.28 resistance=43.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.82 liquidity=120556176.0 spike=0.89
- ORWE.CA: score=22.4 buy_ready=False sector_rank=3 price=26.57 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=59.88 liquidity=45950804.0 spike=0.78
- PHAR.CA: score=4.5 buy_ready=False sector_rank=16 price=118.31 support=118.16 resistance=125.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=109775784.0 spike=0.49
- PHDC.CA: score=10.03 buy_ready=False sector_rank=10 price=13.8 support=13.82 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.01 liquidity=153630704.0 spike=0.72
- PHTV.CA: score=9.3 buy_ready=False sector_rank=11 price=347.0 support=311.27 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=38.58 liquidity=1359688.25 spike=0.66
- POUL.CA: score=18.3 buy_ready=False sector_rank=17 price=38.73 support=36.97 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.0 liquidity=17070144.0 spike=0.72
- PRCL.CA: score=15.37 buy_ready=False sector_rank=12 price=32.24 support=30.9 resistance=36.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=42.03 liquidity=26561250.0 spike=1.25
- PRDC.CA: score=10.03 buy_ready=False sector_rank=10 price=7.96 support=8.0 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=24.0 liquidity=32278326.0 spike=0.48
- PRMH.CA: score=8.61 buy_ready=False sector_rank=11 price=2.54 support=2.28 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=67.07 liquidity=3665160.5 spike=0.3
- RACC.CA: score=16.3 buy_ready=False sector_rank=11 price=9.59 support=9.4 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.26 liquidity=9356027.0 spike=0.39
- RAKT.CA: score=6.85 buy_ready=False sector_rank=11 price=22.15 support=21.4 resistance=23.09 source=Yahoo Finance as_of=2026-09-12T21:00:00+00:00 freshness=FRESH RSI=47.52 liquidity=334376.39 spike=1.29
- RAYA.CA: score=15.56 buy_ready=False sector_rank=21 price=7.13 support=6.95 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.72 liquidity=33410242.0 spike=0.53
- RMDA.CA: score=17.5 buy_ready=False sector_rank=16 price=6.1 support=5.77 resistance=6.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.09 liquidity=28968980.0 spike=0.45
- ROTO.CA: score=6.71 buy_ready=False sector_rank=11 price=40.55 support=42.05 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=17.15 liquidity=6770392.5 spike=0.46
- RREI.CA: score=17.94 buy_ready=False sector_rank=11 price=4.35 support=4.24 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.04 liquidity=15070577.0 spike=0.5
- RTVC.CA: score=10.13 buy_ready=False sector_rank=11 price=3.97 support=3.76 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.23 liquidity=2186721.75 spike=0.29
- RUBX.CA: score=16.74 buy_ready=False sector_rank=11 price=12.72 support=12.36 resistance=13.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=56.52 liquidity=9797494.0 spike=0.47
- SAUD.CA: score=15.75 buy_ready=False sector_rank=7 price=22.84 support=22.85 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=40.77 liquidity=7602877.5 spike=0.46
- SCEM.CA: score=17.87 buy_ready=False sector_rank=12 price=96.0 support=94.0 resistance=112.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=49779844.0 spike=0.26
- SCFM.CA: score=7.78 buy_ready=False sector_rank=11 price=270.17 support=270.55 resistance=305.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.15 liquidity=2842093.75 spike=0.26
- SCTS.CA: score=20.78 buy_ready=False sector_rank=2 price=603.01 support=566.66 resistance=660.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.8 liquidity=10793362.0 spike=2.19
- SDTI.CA: score=20.52 buy_ready=False sector_rank=11 price=73.0 support=67.0 resistance=76.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.09 liquidity=25767962.0 spike=1.29
- SEIG.CA: score=6.06 buy_ready=False sector_rank=11 price=247.68 support=250.02 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.16 liquidity=1118296.0 spike=0.5
- SIPC.CA: score=20.22 buy_ready=False sector_rank=11 price=5.92 support=4.1 resistance=6.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.96 liquidity=67228976.0 spike=1.14
- SKPC.CA: score=22.8 buy_ready=False sector_rank=5 price=17.85 support=16.6 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.85 liquidity=93589632.0 spike=0.67
- SMFR.CA: score=11.16 buy_ready=False sector_rank=11 price=241.09 support=246.0 resistance=276.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=35.05 liquidity=6218429.5 spike=0.5
- SNFC.CA: score=23.4 buy_ready=False sector_rank=11 price=11.18 support=10.26 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=45.77 liquidity=23041064.0 spike=1.73
- SPIN.CA: score=16.5 buy_ready=False sector_rank=3 price=18.33 support=16.5 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.82 liquidity=6096598.5 spike=0.17
- SPMD.CA: score=9.94 buy_ready=False sector_rank=11 price=0.52 support=0.43 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=154314880.0 spike=14.0
- SUGR.CA: score=4.3 buy_ready=False sector_rank=17 price=60.07 support=58.03 resistance=63.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32514648.0 spike=0.45
- SVCE.CA: score=19.94 buy_ready=False sector_rank=11 price=11.68 support=10.28 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.07 liquidity=163056960.0 spike=0.89
- SWDY.CA: score=18.09 buy_ready=False sector_rank=8 price=125.51 support=107.53 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.9 liquidity=50264024.0 spike=0.53
- TALM.CA: score=13.4 buy_ready=False sector_rank=2 price=22.68 support=19.45 resistance=22.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=345841440.0 spike=12.83
- TMGH.CA: score=17.03 buy_ready=False sector_rank=10 price=96.13 support=94.9 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.36 liquidity=248803856.0 spike=0.92
- TRTO.CA: score=9.97 buy_ready=False sector_rank=11 price=0.07 support=0.04 resistance=0.08 source=Yahoo Finance as_of=2026-09-12T21:00:00+00:00 freshness=FRESH RSI=67.92 liquidity=27071.03 spike=0.84
- UEFM.CA: score=14.22 buy_ready=False sector_rank=11 price=534.5 support=440.66 resistance=570.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT RSI=44.04 liquidity=5739929.0 spike=1.27
- UEGC.CA: score=9.94 buy_ready=False sector_rank=11 price=1.69 support=1.66 resistance=2.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=18.92 liquidity=13357934.0 spike=0.29
- UNIP.CA: score=16.94 buy_ready=False sector_rank=11 price=0.37 support=0.35 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.57 liquidity=13455898.0 spike=0.37
- UNIT.CA: score=10.03 buy_ready=False sector_rank=10 price=21.81 support=18.25 resistance=21.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=145631696.0 spike=24.38
- WCDF.CA: score=11.06 buy_ready=False sector_rank=11 price=711.57 support=630.0 resistance=729.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=82.65 liquidity=2123373.75 spike=0.55
- WKOL.CA: score=13.76 buy_ready=False sector_rank=11 price=342.61 support=323.02 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.78 liquidity=5819745.0 spike=0.29
- ZEOT.CA: score=13.17 buy_ready=False sector_rank=11 price=13.13 support=13.25 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=42.48 liquidity=5233414.5 spike=0.4
- ZMID.CA: score=20.03 buy_ready=False sector_rank=10 price=9.4 support=7.39 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.16 liquidity=62440972.0 spike=0.25

## Backtesting Lite
- CIRA.CA: 180d return=117.93%, max drawdown=-16.44%, MA20>MA50 days last20=20, as_of=2026-09-12T21:00:00+00:00
- ETEL.CA: 180d return=101.4%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-09-12T21:00:00+00:00
- ACGC.CA: 180d return=81.51%, max drawdown=-15.74%, MA20>MA50 days last20=20, as_of=2026-09-12T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CIRA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Investment and Real Estate Development summary=CIRA Education take over 51% of L’École Française Hurghada; CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion; CIRA Education launches Middle East’s 1st initiative for care economy
  - CIRA Education take over 51% of L’École Française Hurghada: https://english.mubasher.info/news/4488666/CIRA-Education-take-over-51-of-L-%C3%89cole-Fran%C3%A7aise-Hurghada/
  - CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion: https://english.mubasher.info/news/4393636/CIRA-s-majority-shareholder-acquires-37-5-additional-equity-backs-regional-expansion/
  - CIRA Education launches Middle East’s 1st initiative for care economy: https://english.mubasher.info/news/4391766/CIRA-Education-launches-Middle-East-s-1st-initiative-for-care-economy/
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- ACGC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Cotton Ginning summary=Arab Cotton Ginning’s stock nears significant resistance level; Arab Cotton Ginning’s standalone profit grows 142% YoY in 9M-23/24; Arab Cotton Ginning’s consolidated profit leaps 371% YoY in H1-23/24
  - Arab Cotton Ginning’s stock nears significant resistance level: https://english.mubasher.info/news/4549011/Arab-Cotton-Ginning-s-stock-nears-significant-resistance-level/
  - Arab Cotton Ginning’s standalone profit grows 142% YoY in 9M-23/24: https://english.mubasher.info/news/4302757/Arab-Cotton-Ginning-s-standalone-profit-grows-142-YoY-in-9M-23-24/
  - Arab Cotton Ginning’s consolidated profit leaps 371% YoY in H1-23/24: https://english.mubasher.info/news/4279332/Arab-Cotton-Ginning-s-consolidated-profit-leaps-371-YoY-in-H1-23-24/
- KABO.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Nasr Clothing and Textiles summary=KABO posts EGP 17m in Q1-25/26 unaudited consolidated net profits; KABO sells over 1.9m shares in Spinalex for EGP 20m; KABO unveils international agreements, expansion plan including export lines
  - KABO posts EGP 17m in Q1-25/26 unaudited consolidated net profits: https://english.mubasher.info/news/4600162/KABO-posts-EGP-17m-in-Q1-25-26-unaudited-consolidated-net-profits/
  - KABO sells over 1.9m shares in Spinalex for EGP 20m: https://english.mubasher.info/news/4543747/KABO-sells-over-1-9m-shares-in-Spinalex-for-EGP-20m/
  - KABO unveils international agreements, expansion plan including export lines: https://english.mubasher.info/news/4533185/KABO-unveils-international-agreements-expansion-plan-including-export-lines/
- OIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Investment Holding summary=Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- SNFC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Sharkia National Company for Food Security summary=Sharkia National Food sells EGP 6.5m asset; Sharkia Food turns profitable in Q4; Sharkia National Food turns profitable in Q4
  - Sharkia National Food sells EGP 6.5m asset: https://english.mubasher.info/news/3344769/Sharkia-National-Food-sells-EGP-6-5m-asset/
  - Sharkia Food turns profitable in Q4: https://english.mubasher.info/news/3055832/Sharkia-Food-turns-profitable-in-Q4/
  - Sharkia National Food turns profitable in Q4: https://english.mubasher.info/news/3053492/Sharkia-National-Food-turns-profitable-in-Q4/
- SKPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Sidi Kerir Petrochemicals summary=Evidence rejected for SKPC.CA: source text did not clearly match SKPC.CA / Sidi Kerir Petrochemicals.
- ORWE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=621 sources=3 expected=Oriental Weavers summary=Oriental Weavers to disburse EGP 1.5/shr dividends for 2025; Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025; Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25
  - Oriental Weavers to disburse EGP 1.5/shr dividends for 2025: https://english.mubasher.info/news/4590236/Oriental-Weavers-to-disburse-EGP-1-5-shr-dividends-for-2025/
  - Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025: https://english.mubasher.info/news/4562972/Oriental-Weavers-consolidated-profits-cross-EGP-2-2bn-in-2025/
  - Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25: https://english.mubasher.info/news/4487417/Oriental-Weavers-generates-EGP-12-5bn-consolidated-sales-in-H1-25/

## Warnings
- Evidence for CIRA.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for ACGC.CA matches the company but no source/report date was detected.
- Evidence for KABO.CA matches the company but no source/report date was detected.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence for SNFC.CA matches the company but no source/report date was detected.
- Evidence rejected for SKPC.CA: source text did not clearly match SKPC.CA / Sidi Kerir Petrochemicals.
- Evidence for ORWE.CA matches the company but appears old; latest detected date is 2025-01-01.
