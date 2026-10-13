# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-10-13T12:58:54.449406+00:00
Generated Cairo: 2026-10-13 15:58
Run timing: target 08:45 Cairo | generated Cairo 2026-10-13 15:58 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-10-13 15:55

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 7
- Tradeable price/liquidity tickers: 79/183
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, October 13
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 18.75% / above MA50 25.0%
- EGX70 regime: BEARISH / above MA20 18.18% / above MA50 22.73%
- Sector breadth: 5.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=684136640.0 spike=1.31 score=9.11
- CCAP.CA: liquidity=414912544.0 spike=0.55 score=15.66
- TMGH.CA: liquidity=413241568.0 spike=1.94 score=10.53
- ORAS.CA: liquidity=402873600.0 spike=1.0 score=4.6
- ETEL.CA: liquidity=271802816.0 spike=1.03 score=24.46

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner holds all tickets; EGX30/EGX70 bearish breadth and defensive risk mode block new buys despite a few bullish‑watch signals.
- EGX30/EGX70 trend BEARISH with <20% of stocks above MA20/MA50 keeps risk mode DEFENSIVE_NO_NEW_BUY.
- Top picks (ARAB.CA, ETEL.CA, BINV.CA) show high rank scores and liquidity spikes but outlooks are WATCH‑only; support is distant and resistance near, limiting near‑term upside.
- Sector breadth is narrow at 5%; only Telecommunications shows >50% above MA20, reducing conviction across the market.
- Uncertainty persists from mixed RSI readings, cooling liquidity in several names, and weak sector leadership.

## Top Liquidity Spikes
- ASCM.CA: spike=2.35 liquidity=20470022.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AJWA.CA: spike=1.98 liquidity=41653528.0 outlook=CONSTRUCTIVE score=63.63 buy_ready=False
- CNFN.CA: spike=1.95 liquidity=15045433.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- TMGH.CA: spike=1.94 liquidity=413241568.0 outlook=WEAK_OR_RISKY score=18.63 buy_ready=False
- MOIL.CA: spike=1.93 liquidity=509528.41 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=7.67 5d=2.38% 20d=6.78% aboveMA50=100.0%
- #2 Investment Holding: score=4.14 5d=-2.95% 20d=4.83% aboveMA50=66.67%
- #3 Fintech & Payments: score=3.66 5d=1.69% 20d=-0.5% aboveMA50=0.0%
- #4 Transportation & Logistics: score=3.39 5d=-1.1% 20d=-3.75% aboveMA50=50.0%
- #5 Non-bank Financial Services: score=2.58 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #6 Education: score=2.0 5d=-2.89% 20d=1.43% aboveMA50=33.33%
- #7 Basic Resources & Chemicals: score=1.95 5d=0.0% 20d=-0.47% aboveMA50=20.0%
- #8 General / Verified EGX Expansion: score=1.63 5d=0.0% 20d=0.0% aboveMA50=9.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- BINV.CA: BULLISH_WATCH score=89.14 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- EFIH.CA: BULLISH_WATCH score=88.66 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- ETEL.CA: BULLISH_WATCH score=84.67 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- ALCN.CA: BULLISH_WATCH score=79.39 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ARAB.CA: BULLISH_WATCH score=73.63 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support; sector is not leading
- TALM.CA: CONSTRUCTIVE score=68.0 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; far above support
- AJWA.CA: CONSTRUCTIVE score=63.63 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=overheated RSI; sector is not leading
- AMOC.CA: CONSTRUCTIVE score=59.45 liquidity=TRADEABLE sector=IMPROVING risk=below MA20; sector is not leading
- SDTI.CA: CONSTRUCTIVE score=58.63 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended; sector is not leading
- CPCI.CA: CONSTRUCTIVE score=55.63 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=overheated RSI; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ISPH.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- MHOT.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- WCDF.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=3.22 buy_ready=False sector_rank=8 price=232.02 support=225.0 resistance=250.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8564062.0 spike=0.42
- ABUK.CA: score=12.78 buy_ready=False sector_rank=7 price=84.29 support=83.55 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.44 liquidity=56441784.0 spike=0.61
- ACAMD.CA: score=15.79 buy_ready=False sector_rank=8 price=1.96 support=1.87 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.82 liquidity=45955632.0 spike=1.07
- ACGC.CA: score=4.6 buy_ready=False sector_rank=12 price=13.11 support=12.81 resistance=13.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11989551.0 spike=0.64
- ADCI.CA: score=6.61 buy_ready=False sector_rank=8 price=268.99 support=256.0 resistance=293.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.2 liquidity=1961785.25 spike=0.86
- ADIB.CA: score=10.31 buy_ready=False sector_rank=15 price=45.66 support=46.6 resistance=54.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=20.97 liquidity=102599288.0 spike=1.41
- ADPC.CA: score=5.35 buy_ready=False sector_rank=8 price=3.11 support=3.01 resistance=3.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20057804.0 spike=1.35
- AFDI.CA: score=0.84 buy_ready=False sector_rank=8 price=49.02 support=46.12 resistance=51.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6185701.0 spike=0.91
- AFMC.CA: score=4.65 buy_ready=False sector_rank=8 price=135.46 support=122.0 resistance=146.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17029426.0 spike=0.65
- AJWA.CA: score=20.61 buy_ready=False sector_rank=8 price=208.92 support=176.0 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=81.83 liquidity=41653528.0 spike=1.98
- ALCN.CA: score=20.36 buy_ready=False sector_rank=4 price=33.2 support=30.4 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.5 liquidity=17274376.0 spike=0.5
- ALUM.CA: score=1.38 buy_ready=False sector_rank=8 price=21.07 support=20.52 resistance=22.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6191117.5 spike=1.27
- AMER.CA: score=5.69 buy_ready=False sector_rank=9 price=4.72 support=4.38 resistance=5.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=77774832.0 spike=1.52
- AMES.CA: score=4.65 buy_ready=False sector_rank=8 price=39.36 support=38.02 resistance=42.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=70960104.0 spike=0.61
- AMIA.CA: score=17.65 buy_ready=False sector_rank=8 price=18.33 support=17.12 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.56 liquidity=11213405.0 spike=0.65
- AMOC.CA: score=17.58 buy_ready=False sector_rank=14 price=13.46 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.96 liquidity=113828672.0 spike=0.85
- APSW.CA: score=6.32 buy_ready=False sector_rank=8 price=7.91 support=7.81 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=663592.88 spike=0.96
- ARAB.CA: score=24.89 buy_ready=False sector_rank=9 price=0.27 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.35 liquidity=143442432.0 spike=1.62
- ARCC.CA: score=4.58 buy_ready=False sector_rank=13 price=65.78 support=64.0 resistance=68.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29068188.0 spike=0.94
- AREH.CA: score=4.03 buy_ready=False sector_rank=8 price=1.16 support=1.11 resistance=1.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9315682.0 spike=1.03
- ASCM.CA: score=7.35 buy_ready=False sector_rank=8 price=49.19 support=48.0 resistance=53.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20470022.0 spike=2.35
- ASPI.CA: score=4.65 buy_ready=False sector_rank=8 price=0.32 support=0.31 resistance=0.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21245628.0 spike=0.57
- ATLC.CA: score=2.98 buy_ready=False sector_rank=5 price=5.29 support=5.2 resistance=5.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7948181.0 spike=0.7
- ATQA.CA: score=5.86 buy_ready=False sector_rank=7 price=11.21 support=10.61 resistance=11.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=110096648.0 spike=1.54
- AXPH.CA: score=4.54 buy_ready=False sector_rank=8 price=1373.94 support=1300.0 resistance=1449.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9109660.0 spike=1.39
- BINV.CA: score=22.66 buy_ready=False sector_rank=2 price=59.73 support=49.91 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=41.17 liquidity=22789116.0 spike=0.93
- BIOC.CA: score=18.65 buy_ready=False sector_rank=8 price=297.27 support=225.21 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.37 liquidity=75599656.0 spike=0.8
- BTFH.CA: score=10.61 buy_ready=False sector_rank=5 price=2.67 support=2.65 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.4 liquidity=168393664.0 spike=1.79
- CAED.CA: score=4.11 buy_ready=False sector_rank=8 price=104.22 support=95.0 resistance=110.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9460705.0 spike=0.58
- CANA.CA: score=12.49 buy_ready=False sector_rank=15 price=44.97 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=30.43 liquidity=10280070.0 spike=0.45
- CCAP.CA: score=15.66 buy_ready=False sector_rank=2 price=6.25 support=6.25 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=29.38 liquidity=414912544.0 spike=0.55
- CCRS.CA: score=3.98 buy_ready=False sector_rank=8 price=2.08 support=1.87 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9324919.0 spike=0.66
- CEFM.CA: score=-3.08 buy_ready=False sector_rank=8 price=121.45 support=115.17 resistance=135.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2265271.25 spike=0.7
- CERA.CA: score=4.65 buy_ready=False sector_rank=8 price=1.22 support=1.21 resistance=1.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=106964320.0 spike=0.76
- CFGH.CA: score=-4.22 buy_ready=False sector_rank=8 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12275.24 spike=1.56
- CICH.CA: score=0.24 buy_ready=False sector_rank=5 price=11.0 support=10.6 resistance=11.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4571412.0 spike=1.32
- CIEB.CA: score=9.17 buy_ready=False sector_rank=15 price=22.75 support=23.0 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.05 liquidity=12332515.0 spike=1.34
- CIRA.CA: score=9.8 buy_ready=False sector_rank=6 price=36.54 support=36.8 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=33.09 liquidity=20594258.0 spike=0.58
- CLHO.CA: score=4.9 buy_ready=False sector_rank=16 price=14.11 support=14.01 resistance=14.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=45521452.0 spike=1.21
- CNFN.CA: score=6.93 buy_ready=False sector_rank=5 price=3.93 support=3.8 resistance=4.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15045433.0 spike=1.95
- COMI.CA: score=9.11 buy_ready=False sector_rank=15 price=122.63 support=122.7 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=13.49 liquidity=684136640.0 spike=1.31
- COPR.CA: score=14.71 buy_ready=False sector_rank=8 price=0.46 support=0.44 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.26 liquidity=25745320.0 spike=1.03
- COSG.CA: score=4.65 buy_ready=False sector_rank=8 price=1.39 support=1.34 resistance=1.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15095526.0 spike=0.95
- CPCI.CA: score=13.93 buy_ready=False sector_rank=8 price=594.11 support=530.0 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=78.97 liquidity=6117744.0 spike=1.58
- CSAG.CA: score=16.56 buy_ready=False sector_rank=4 price=35.19 support=34.52 resistance=40.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.57 liquidity=12575869.0 spike=1.6
- DAPH.CA: score=5.13 buy_ready=False sector_rank=8 price=95.95 support=90.5 resistance=103.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=47080192.0 spike=1.24
- DEIN.CA: score=7.65 buy_ready=False sector_rank=8 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 09:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37.26 spike=0.01
- DOMT.CA: score=5.07 buy_ready=False sector_rank=20 price=23.23 support=23.81 resistance=28.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=35.57 liquidity=3205131.25 spike=0.61
- DSCW.CA: score=4.65 buy_ready=False sector_rank=8 price=1.58 support=1.55 resistance=1.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18864840.0 spike=1.0
- DTPP.CA: score=4.65 buy_ready=False sector_rank=8 price=260.61 support=250.0 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32511478.0 spike=0.33
- EALR.CA: score=-1.51 buy_ready=False sector_rank=8 price=309.99 support=290.17 resistance=323.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3841540.5 spike=0.4
- EASB.CA: score=1.19 buy_ready=False sector_rank=8 price=6.87 support=6.54 resistance=7.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6540063.5 spike=0.75
- EAST.CA: score=6.86 buy_ready=False sector_rank=20 price=27.34 support=27.91 resistance=34.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=16.38 liquidity=35666404.0 spike=0.78
- EBSC.CA: score=-3.73 buy_ready=False sector_rank=8 price=1.59 support=1.5 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1616932.88 spike=0.6
- ECAP.CA: score=0.15 buy_ready=False sector_rank=8 price=27.97 support=27.5 resistance=30.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5097380.0 spike=1.2
- EDFM.CA: score=8.62 buy_ready=False sector_rank=8 price=390.57 support=354.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=43.38 liquidity=1469299.75 spike=1.25
- EEII.CA: score=1.56 buy_ready=False sector_rank=8 price=1.94 support=1.84 resistance=2.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6904070.0 spike=0.73
- EFIC.CA: score=8.78 buy_ready=False sector_rank=7 price=153.76 support=147.0 resistance=217.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=20.62 liquidity=29045558.0 spike=0.63
- EFID.CA: score=9.34 buy_ready=False sector_rank=20 price=18.23 support=18.1 resistance=31.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=27.23 liquidity=64103628.0 spike=1.24
- EFIH.CA: score=21.2 buy_ready=False sector_rank=3 price=23.64 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.2 liquidity=89450968.0 spike=1.37
- EGAL.CA: score=5.9 buy_ready=False sector_rank=7 price=315.95 support=306.1 resistance=326.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=81716920.0 spike=1.56
- EGAS.CA: score=4.55 buy_ready=False sector_rank=14 price=51.4 support=48.08 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9972754.0 spike=0.89
- EGBE.CA: score=1.64 buy_ready=False sector_rank=15 price=0.52 support=0.49 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=75.34 liquidity=127710.8 spike=1.01
- EGCH.CA: score=6.1 buy_ready=False sector_rank=7 price=11.99 support=11.86 resistance=12.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=139005232.0 spike=1.66
- EGSA.CA: score=7.4 buy_ready=False sector_rank=1 price=8.87 support=8.82 resistance=9.08 source=Yahoo Finance as_of=2026-10-10T21:00:00+00:00 freshness=FRESH RSI=11.76 liquidity=691.86 spike=0.12
- EGTS.CA: score=4.65 buy_ready=False sector_rank=9 price=13.83 support=13.56 resistance=15.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15246098.0 spike=0.42
- EHDR.CA: score=5.25 buy_ready=False sector_rank=8 price=2.25 support=2.1 resistance=2.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15099010.0 spike=1.3
- ELEC.CA: score=3.59 buy_ready=False sector_rank=19 price=1.69 support=1.65 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40164104.0 spike=0.65
- ELKA.CA: score=10.71 buy_ready=False sector_rank=8 price=1.46 support=1.43 resistance=1.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=14186696.0 spike=1.03
- ELNA.CA: score=7.28 buy_ready=False sector_rank=8 price=35.22 support=33.46 resistance=36.98 source=Yahoo Finance as_of=2026-10-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=264150.01 spike=1.68
- ELSH.CA: score=4.65 buy_ready=False sector_rank=8 price=10.9 support=10.76 resistance=11.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21358222.0 spike=1.0
- ELWA.CA: score=9.01 buy_ready=False sector_rank=8 price=1.65 support=1.43 resistance=1.84 source=Yahoo Finance as_of=2026-10-10T21:00:00+00:00 freshness=FRESH RSI=44.68 liquidity=361348.34 spike=0.48
- EMFD.CA: score=9.65 buy_ready=False sector_rank=9 price=11.96 support=11.7 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.75 liquidity=35698084.0 spike=0.46
- ENGC.CA: score=5.19 buy_ready=False sector_rank=8 price=33.37 support=32.37 resistance=34.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22406912.0 spike=1.27
- EOSB.CA: score=9.66 buy_ready=False sector_rank=8 price=1.57 support=1.6 resistance=1.64 source=Yahoo Finance as_of=2026-10-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=7162.34 spike=0.14
- EPCO.CA: score=-0.54 buy_ready=False sector_rank=8 price=8.7 support=8.0 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4807763.5 spike=0.5
- EPPK.CA: score=-4.93 buy_ready=False sector_rank=8 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=24.46 buy_ready=False sector_rank=1 price=145.48 support=124.01 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.03 liquidity=271802816.0 spike=1.03
- ETRS.CA: score=17.43 buy_ready=False sector_rank=8 price=10.46 support=9.82 resistance=11.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=41.06 liquidity=13258793.0 spike=1.39
- EXPA.CA: score=4.49 buy_ready=False sector_rank=15 price=14.39 support=14.02 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27429300.0 spike=0.72
- FAIT.CA: score=3.58 buy_ready=False sector_rank=15 price=42.5 support=38.48 resistance=48.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=33.4 liquidity=3648163.0 spike=1.22
- FAITA.CA: score=5.51 buy_ready=False sector_rank=15 price=0.98 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=17230.25 spike=0.65
- FERC.CA: score=0.2 buy_ready=False sector_rank=7 price=69.75 support=66.72 resistance=72.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5415675.0 spike=0.91
- FWRY.CA: score=17.46 buy_ready=False sector_rank=3 price=18.34 support=17.5 resistance=19.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.34 liquidity=82911240.0 spike=0.75
- GBCO.CA: score=15.74 buy_ready=False sector_rank=18 price=29.8 support=27.0 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.81 liquidity=74686536.0 spike=0.74
- GDWA.CA: score=4.65 buy_ready=False sector_rank=8 price=0.61 support=0.6 resistance=0.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13202059.0 spike=0.57
- GGCC.CA: score=4.41 buy_ready=False sector_rank=8 price=0.64 support=0.61 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9757902.0 spike=0.67
- GIHD.CA: score=6.41 buy_ready=False sector_rank=8 price=55.84 support=54.0 resistance=59.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36659320.0 spike=1.88
- GMCI.CA: score=6.45 buy_ready=False sector_rank=8 price=1.61 support=1.49 resistance=1.9 source=Yahoo Finance as_of=2026-10-10T21:00:00+00:00 freshness=FRESH RSI=36.84 liquidity=539179.34 spike=1.13
- GRCA.CA: score=2.72 buy_ready=False sector_rank=8 price=32.03 support=30.51 resistance=34.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8067048.5 spike=0.43
- GSSC.CA: score=-4.71 buy_ready=False sector_rank=8 price=256.99 support=250.11 resistance=266.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=642145.31 spike=0.18
- HDBK.CA: score=11.49 buy_ready=False sector_rank=15 price=103.48 support=102.03 resistance=121.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.03 liquidity=27331494.0 spike=0.99
- HELI.CA: score=9.65 buy_ready=False sector_rank=9 price=7.12 support=6.94 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.5 liquidity=68122016.0 spike=0.62
- HRHO.CA: score=18.03 buy_ready=False sector_rank=5 price=25.19 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.97 liquidity=96683928.0 spike=0.73
- ICID.CA: score=10.11 buy_ready=False sector_rank=8 price=17.53 support=16.52 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.13 liquidity=2458744.75 spike=0.31
- IDRE.CA: score=3.85 buy_ready=False sector_rank=8 price=42.02 support=40.05 resistance=45.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9193871.0 spike=0.63
- IFAP.CA: score=8.65 buy_ready=False sector_rank=17 price=18.26 support=17.17 resistance=21.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.55 liquidity=9889883.0 spike=1.28
- INFI.CA: score=3.38 buy_ready=False sector_rank=8 price=113.87 support=106.01 resistance=120.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8725219.0 spike=0.63
- IRON.CA: score=15.8 buy_ready=False sector_rank=7 price=26.92 support=25.01 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=51.18 liquidity=11512691.0 spike=1.01
- ISMA.CA: score=5.87 buy_ready=False sector_rank=8 price=21.62 support=18.91 resistance=24.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14883393.0 spike=1.61
- ISMQ.CA: score=4.78 buy_ready=False sector_rank=7 price=7.47 support=7.14 resistance=7.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16568647.0 spike=0.83
- JUFO.CA: score=7.72 buy_ready=False sector_rank=20 price=24.02 support=24.4 resistance=27.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.7 liquidity=23752846.0 spike=1.43
- KABO.CA: score=4.6 buy_ready=False sector_rank=12 price=7.52 support=7.36 resistance=8.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28967876.0 spike=0.95
- KWIN.CA: score=2.88 buy_ready=False sector_rank=8 price=65.38 support=60.0 resistance=71.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8227114.5 spike=0.77
- KZPC.CA: score=12.85 buy_ready=False sector_rank=8 price=12.76 support=12.15 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.64 liquidity=12783795.0 spike=1.1
- LCSW.CA: score=16.76 buy_ready=False sector_rank=13 price=32.8 support=28.86 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.42 liquidity=20755948.0 spike=1.09
- LUTS.CA: score=4.69 buy_ready=False sector_rank=8 price=0.77 support=0.65 resistance=0.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=68833864.0 spike=1.02
- MAAL.CA: score=4.51 buy_ready=False sector_rank=8 price=8.98 support=8.8 resistance=9.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9861140.0 spike=0.42
- MASR.CA: score=4.79 buy_ready=False sector_rank=8 price=7.12 support=6.9 resistance=7.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=77383648.0 spike=1.07
- MBSC.CA: score=4.58 buy_ready=False sector_rank=13 price=332.53 support=317.21 resistance=358.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=73039008.0 spike=0.9
- MCQE.CA: score=5.78 buy_ready=False sector_rank=13 price=176.0 support=170.0 resistance=185.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=78857464.0 spike=1.6
- MCRO.CA: score=4.65 buy_ready=False sector_rank=8 price=1.36 support=1.25 resistance=1.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31642436.0 spike=0.4
- MENA.CA: score=-4.37 buy_ready=False sector_rank=9 price=5.87 support=5.72 resistance=6.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=974687.75 spike=0.78
- MEPA.CA: score=3.36 buy_ready=False sector_rank=8 price=1.56 support=1.53 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8708850.0 spike=0.7
- MFPC.CA: score=12.78 buy_ready=False sector_rank=7 price=44.02 support=43.0 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.74 liquidity=62748952.0 spike=0.65
- MFSC.CA: score=-4.11 buy_ready=False sector_rank=8 price=38.18 support=36.25 resistance=40.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1242974.75 spike=0.49
- MICH.CA: score=4.79 buy_ready=False sector_rank=8 price=44.07 support=43.0 resistance=45.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10285165.0 spike=1.07
- MILS.CA: score=1.64 buy_ready=False sector_rank=8 price=155.22 support=147.06 resistance=174.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6985233.0 spike=0.72
- MIPH.CA: score=9.34 buy_ready=False sector_rank=16 price=770.74 support=739.69 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=40.02 liquidity=4861342.0 spike=0.56
- MOED.CA: score=4.65 buy_ready=False sector_rank=8 price=0.6 support=0.57 resistance=0.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18859902.0 spike=0.6
- MOIL.CA: score=1.95 buy_ready=False sector_rank=14 price=0.67 support=0.67 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=31.58 liquidity=509528.41 spike=1.93
- MOIN.CA: score=4.65 buy_ready=False sector_rank=8 price=31.66 support=31.0 resistance=34.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11597797.0 spike=0.83
- MOSC.CA: score=-3.74 buy_ready=False sector_rank=8 price=257.94 support=231.0 resistance=268.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1607280.38 spike=0.49
- MPCI.CA: score=4.65 buy_ready=False sector_rank=8 price=310.64 support=294.2 resistance=324.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=94996664.0 spike=0.9
- MPCO.CA: score=4.2 buy_ready=False sector_rank=17 price=2.11 support=2.0 resistance=2.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=145840608.0 spike=0.91
- MPRC.CA: score=4.65 buy_ready=False sector_rank=8 price=36.39 support=34.53 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13155448.0 spike=0.65
- MTIE.CA: score=10.3 buy_ready=False sector_rank=18 price=7.46 support=7.5 resistance=8.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=29.75 liquidity=22466790.0 spike=1.28
- NAHO.CA: score=4.67 buy_ready=False sector_rank=8 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=48.15 liquidity=16969.67 spike=0.46
- NCCW.CA: score=4.65 buy_ready=False sector_rank=8 price=5.9 support=5.3 resistance=6.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28418404.0 spike=0.5
- NEDA.CA: score=-0.01 buy_ready=False sector_rank=8 price=2.6 support=2.48 resistance=2.8 source=Yahoo Finance as_of=2026-10-10T21:00:00+00:00 freshness=FRESH RSI=25.0 liquidity=339450.79 spike=0.47
- NHPS.CA: score=3.51 buy_ready=False sector_rank=8 price=65.21 support=63.02 resistance=69.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8856222.0 spike=0.6
- NINH.CA: score=4.71 buy_ready=False sector_rank=8 price=16.63 support=16.27 resistance=17.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14796876.0 spike=1.03
- NIPH.CA: score=4.48 buy_ready=False sector_rank=16 price=273.3 support=241.0 resistance=299.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=119572776.0 spike=0.97
- OBRI.CA: score=5.07 buy_ready=False sector_rank=8 price=25.28 support=24.0 resistance=27.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16649942.0 spike=1.21
- OCDI.CA: score=4.65 buy_ready=False sector_rank=9 price=25.0 support=24.51 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20895538.0 spike=0.41
- OCPH.CA: score=-2.38 buy_ready=False sector_rank=8 price=201.57 support=195.0 resistance=209.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2968972.5 spike=0.81
- ODIN.CA: score=2.48 buy_ready=False sector_rank=8 price=2.2 support=2.11 resistance=2.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7832034.0 spike=0.86
- OFH.CA: score=4.65 buy_ready=False sector_rank=8 price=0.79 support=0.76 resistance=0.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30509866.0 spike=0.31
- OIH.CA: score=12.66 buy_ready=False sector_rank=2 price=1.79 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.64 liquidity=82145328.0 spike=0.9
- OLFI.CA: score=6.86 buy_ready=False sector_rank=20 price=20.23 support=20.82 resistance=23.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=21.29 liquidity=11576561.0 spike=0.66
- ORAS.CA: score=4.6 buy_ready=False sector_rank=11 price=884.22 support=845.02 resistance=900.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=402873600.0 spike=1.0
- ORHD.CA: score=4.99 buy_ready=False sector_rank=9 price=10.76 support=10.01 resistance=11.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=179385888.0 spike=1.17
- ORWE.CA: score=14.68 buy_ready=False sector_rank=12 price=26.54 support=26.01 resistance=28.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=36.06 liquidity=39331900.0 spike=1.04
- PHAR.CA: score=4.48 buy_ready=False sector_rank=16 price=105.14 support=102.0 resistance=109.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=54286912.0 spike=0.73
- PHDC.CA: score=16.65 buy_ready=False sector_rank=9 price=12.52 support=12.36 resistance=14.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.34 liquidity=92015120.0 spike=0.87
- PHTV.CA: score=8.26 buy_ready=False sector_rank=8 price=344.49 support=315.1 resistance=378.89 source=Yahoo Finance as_of=2026-10-10T21:00:00+00:00 freshness=FRESH RSI=41.35 liquidity=1364524.85 spike=1.12
- POUL.CA: score=6.86 buy_ready=False sector_rank=20 price=9.52 support=9.12 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=1.89 liquidity=23587450.0 spike=0.71
- PRCL.CA: score=4.58 buy_ready=False sector_rank=13 price=21.55 support=21.0 resistance=24.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12338662.0 spike=0.99
- PRDC.CA: score=4.91 buy_ready=False sector_rank=9 price=6.31 support=6.07 resistance=6.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39246972.0 spike=1.13
- PRMH.CA: score=-0.73 buy_ready=False sector_rank=8 price=1.86 support=1.8 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4395964.0 spike=1.11
- RACC.CA: score=6.31 buy_ready=False sector_rank=8 price=8.84 support=8.51 resistance=10.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.96 liquidity=5653803.5 spike=0.82
- RAKT.CA: score=7.01 buy_ready=False sector_rank=8 price=22.06 support=20.26 resistance=25.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=64.25 liquidity=482543.84 spike=1.44
- RAYA.CA: score=4.63 buy_ready=False sector_rank=10 price=5.89 support=5.7 resistance=6.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36499364.0 spike=1.01
- RMDA.CA: score=9.48 buy_ready=False sector_rank=16 price=5.25 support=4.83 resistance=6.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.08 liquidity=25929750.0 spike=0.8
- ROTO.CA: score=3.65 buy_ready=False sector_rank=8 price=37.23 support=35.56 resistance=39.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8893029.0 spike=1.05
- RREI.CA: score=4.65 buy_ready=False sector_rank=8 price=3.44 support=3.29 resistance=3.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10215251.0 spike=0.94
- RTVC.CA: score=0.42 buy_ready=False sector_rank=8 price=3.39 support=3.31 resistance=3.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4427682.5 spike=1.67
- RUBX.CA: score=4.65 buy_ready=False sector_rank=8 price=15.75 support=14.01 resistance=17.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=89858544.0 spike=0.96
- SAUD.CA: score=1.51 buy_ready=False sector_rank=15 price=21.5 support=20.2 resistance=21.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7019435.5 spike=0.37
- SCEM.CA: score=4.58 buy_ready=False sector_rank=13 price=83.66 support=80.5 resistance=88.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=34671804.0 spike=0.51
- SCFM.CA: score=-0.25 buy_ready=False sector_rank=8 price=232.24 support=223.11 resistance=290.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=31.78 liquidity=1095816.63 spike=0.5
- SCTS.CA: score=0.44 buy_ready=False sector_rank=6 price=510.15 support=520.3 resistance=635.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=26.52 liquidity=635312.63 spike=0.4
- SDTI.CA: score=19.65 buy_ready=False sector_rank=8 price=83.15 support=71.0 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.0 liquidity=16328046.0 spike=0.49
- SEIG.CA: score=-3.7 buy_ready=False sector_rank=8 price=197.67 support=173.1 resistance=219.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1652853.13 spike=0.73
- SIPC.CA: score=4.93 buy_ready=False sector_rank=8 price=5.12 support=4.98 resistance=5.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=61342124.0 spike=1.14
- SKPC.CA: score=9.22 buy_ready=False sector_rank=7 price=15.1 support=15.4 resistance=18.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=17.27 liquidity=105154232.0 spike=1.22
- SMFR.CA: score=0.78 buy_ready=False sector_rank=8 price=206.08 support=181.6 resistance=234.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5251058.5 spike=1.44
- SNFC.CA: score=15.51 buy_ready=False sector_rank=8 price=11.06 support=10.58 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.69 liquidity=5859424.0 spike=0.48
- SPIN.CA: score=1.51 buy_ready=False sector_rank=12 price=15.0 support=14.94 resistance=15.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6710484.5 spike=1.1
- SPMD.CA: score=4.65 buy_ready=False sector_rank=8 price=0.35 support=0.34 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12564150.0 spike=0.17
- SUGR.CA: score=2.71 buy_ready=False sector_rank=20 price=52.51 support=51.5 resistance=54.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9848663.0 spike=0.68
- SVCE.CA: score=4.65 buy_ready=False sector_rank=8 price=9.36 support=8.81 resistance=9.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=60181412.0 spike=0.64
- SWDY.CA: score=8.97 buy_ready=False sector_rank=19 price=111.18 support=102.31 resistance=129.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.52 liquidity=70856256.0 spike=1.19
- TALM.CA: score=21.8 buy_ready=False sector_rank=6 price=21.14 support=17.61 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.58 liquidity=42052632.0 spike=0.58
- TMGH.CA: score=10.53 buy_ready=False sector_rank=9 price=83.78 support=84.4 resistance=99.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.64 liquidity=413241568.0 spike=1.94
- TRTO.CA: score=9.66 buy_ready=False sector_rank=8 price=0.07 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-10-10T21:00:00+00:00 freshness=FRESH RSI=65.22 liquidity=4054.65 spike=0.37
- UEFM.CA: score=8.38 buy_ready=False sector_rank=8 price=494.16 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.53 liquidity=1729977.25 spike=0.48
- UEGC.CA: score=4.65 buy_ready=False sector_rank=8 price=1.4 support=1.34 resistance=1.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20335078.0 spike=0.61
- UNIP.CA: score=4.65 buy_ready=False sector_rank=8 price=0.31 support=0.31 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11064430.0 spike=0.97
- UNIT.CA: score=7.31 buy_ready=False sector_rank=9 price=16.61 support=16.41 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=37.1 liquidity=2659239.75 spike=0.16
- WKOL.CA: score=0.89 buy_ready=False sector_rank=8 price=275.13 support=266.18 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.59 liquidity=2241511.25 spike=0.19
- ZEOT.CA: score=3.14 buy_ready=False sector_rank=8 price=10.17 support=9.75 resistance=11.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7663534.0 spike=1.41
- ZMID.CA: score=9.65 buy_ready=False sector_rank=9 price=7.2 support=7.07 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=16.35 liquidity=77211888.0 spike=0.72

## Backtesting Lite
- ARAB.CA: 180d return=41.09%, max drawdown=-26.79%, MA20>MA50 days last20=13, as_of=2026-10-10T21:00:00+00:00
- ETEL.CA: 180d return=113.46%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-10-10T21:00:00+00:00
- BINV.CA: 180d return=58.3%, max drawdown=-17.77%, MA20>MA50 days last20=20, as_of=2026-10-10T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- AJWA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=AJWA For Food Industries Co. Egypt summary=Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture; AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3; Ajwa Egypt turns to losses in 9M
  - Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture: https://english.mubasher.info/news/4532004/Ajwa-Egypt-s-board-approves-capital-increase-to-EGP-500m-joins-new-food-venture/
  - AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3: https://english.mubasher.info/news/4527545/AJWA-Egypt-s-standalone-net-profits-retreat-to-EGP-14m-in-9M-25-amid-shift-to-profitability-in-Q3/
  - Ajwa Egypt turns to losses in 9M: https://english.mubasher.info/news/3883210/Ajwa-Egypt-turns-to-losses-in-9M/
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- SDTI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=SHARM DREAMS Co. for Touristic Investment S.A.E summary=Sharm Dreams stock maintains strong uptrend - Analysis; Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis; Sharm Dreams stock hits historic level halting driving buying force
  - Sharm Dreams stock maintains strong uptrend - Analysis: https://english.mubasher.info/news/4577977/Sharm-Dreams-stock-maintains-strong-uptrend-Analysis/
  - Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis: https://english.mubasher.info/news/4547831/Sharm-Dreams-stock-is-experiencing-sideways-movement-amid-anticipation-of-next-trend-Analysis/
  - Sharm Dreams stock hits historic level halting driving buying force: https://english.mubasher.info/news/4529096/Sharm-Dreams-stock-hits-historic-level-halting-driving-buying-force/

## Warnings
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence for AJWA.CA matches the company but no source/report date was detected.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence for SDTI.CA matches the company but no source/report date was detected.
