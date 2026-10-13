# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-10-13T19:28:08.120048+00:00
Generated Cairo: 2026-10-13 22:28
Run timing: target 15:30 Cairo | generated Cairo 2026-10-13 22:28 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-10-13 22:23

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 153/186
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, October 13
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 15.79% / above MA50 21.05%
- EGX70 regime: BEARISH / above MA20 5.41% / above MA50 13.51%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=684136640.0 spike=1.28 score=8.02
- CCAP.CA: liquidity=414912544.0 spike=0.58 score=13.68
- TMGH.CA: liquidity=413241568.0 spike=1.92 score=8.8
- ORAS.CA: liquidity=402873600.0 spike=1.0 score=4.6
- ETEL.CA: liquidity=271802816.0 spike=1.03 score=26.2

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with weak breadth, putting the market in DEFENSIVE_NO_NEW_BUY mode; the scanner therefore flags the top‑ranked tickets as HOLD despite some bullish watches.
- ETEL.CA leads the Telecommunications sector with tradeable liquidity, moderate support distance (17%) and RSI ~60, but the bearish regime keeps it HOLD despite a BULLISH_WATCH outlook.
- EFIH.CA shows a liquidity spike and CONSTRUCTIVE outlook, yet it trades below the MA50 and the defensive risk mode overrides any buy signal.
- ARAB.CA exhibits an accumulation‑spike liquidity regime and sits near resistance, but its overheated RSI and non‑leading sector result in a HOLD recommendation.
- BINV.CA and AJWA.CA present mixed signals—BINV.CA has neutral RSI and tradeable liquidity, AJWA.CA shows overheated RSI close to resistance—both remain HOLD under the current bearish breadth.

## Top Liquidity Spikes
- ASCM.CA: spike=2.39 liquidity=20470022.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- WCDF.CA: spike=2.01 liquidity=6850844.5 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GIHD.CA: spike=1.97 liquidity=36659320.0 outlook=WEAK_OR_RISKY score=28 buy_ready=False
- ISMA.CA: spike=1.95 liquidity=14883393.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CFGH.CA: spike=1.94 liquidity=12275.24 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=5.34 5d=-2.41% 20d=5.13% aboveMA50=100.0%
- #2 Fintech & Payments: score=2.66 5d=-0.81% 20d=-0.39% aboveMA50=0.0%
- #3 Investment Holding: score=1.69 5d=-6.42% 20d=-0.48% aboveMA50=66.67%
- #4 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #5 Transportation & Logistics: score=1.1 5d=-5.0% 20d=-0.06% aboveMA50=50.0%
- #6 Energy & Petrochemicals: score=0.3 5d=-4.57% 20d=-1.04% aboveMA50=33.33%
- #7 Banking & Financials: score=-1.34 5d=-5.04% 20d=-7.27% aboveMA50=20.0%
- #8 General / Verified EGX Expansion: score=-1.54 5d=-3.96% 20d=-7.89% aboveMA50=7.84%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ETEL.CA: BULLISH_WATCH score=90.34 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- BINV.CA: BULLISH_WATCH score=86.69 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- EFIH.CA: CONSTRUCTIVE score=65.66 liquidity=TRADEABLE sector=LEADING risk=below MA50
- ARAB.CA: CONSTRUCTIVE score=64 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=momentum is extended; far above support; sector is not leading
- AMOC.CA: CONSTRUCTIVE score=63.3 liquidity=TRADEABLE sector=IMPROVING risk=below MA20
- ALCN.CA: CONSTRUCTIVE score=59.1 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; below MA20
- SDTI.CA: CONSTRUCTIVE score=57 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; momentum is extended; sector is not leading
- AJWA.CA: CONSTRUCTIVE score=56 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=overheated RSI; close to resistance; sector is not leading
- CPCI.CA: CONSTRUCTIVE score=54 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=overheated RSI; sector is not leading
- AMIA.CA: CONSTRUCTIVE score=53 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; below MA20; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- MHOT.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=1.95 buy_ready=False sector_rank=8 price=232.02 support=225.0 resistance=250.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8564062.0 spike=0.43
- ABUK.CA: score=11.09 buy_ready=False sector_rank=12 price=84.29 support=83.55 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.85 liquidity=56441784.0 spike=0.61
- ACAMD.CA: score=14.54 buy_ready=False sector_rank=8 price=1.96 support=1.87 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=45955632.0 spike=1.08
- ACGC.CA: score=13.05 buy_ready=False sector_rank=13 price=13.11 support=12.9 resistance=15.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=39.22 liquidity=11989551.0 spike=0.64
- ADCI.CA: score=5.35 buy_ready=False sector_rank=8 price=268.99 support=256.0 resistance=288.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.0 liquidity=1961785.25 spike=0.88
- ADIB.CA: score=9.2 buy_ready=False sector_rank=7 price=45.66 support=45.5 resistance=54.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=21.15 liquidity=102599288.0 spike=1.37
- ADPC.CA: score=8.06 buy_ready=False sector_rank=8 price=3.11 support=3.25 resistance=4.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=22.41 liquidity=20057804.0 spike=1.34
- AFDI.CA: score=-0.43 buy_ready=False sector_rank=8 price=49.02 support=46.12 resistance=51.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6185701.0 spike=0.92
- AFMC.CA: score=15.38 buy_ready=False sector_rank=8 price=135.46 support=131.0 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=36.69 liquidity=17029426.0 spike=0.78
- AJWA.CA: score=18.72 buy_ready=False sector_rank=8 price=208.92 support=176.0 resistance=212.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=88.97 liquidity=41653528.0 spike=1.67
- ALCN.CA: score=17.44 buy_ready=False sector_rank=5 price=33.2 support=30.4 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.77 liquidity=17274376.0 spike=0.5
- ALUM.CA: score=4.1 buy_ready=False sector_rank=8 price=21.07 support=21.65 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.99 liquidity=6191117.5 spike=1.26
- AMER.CA: score=15.88 buy_ready=False sector_rank=14 price=4.72 support=4.05 resistance=5.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.78 liquidity=77774832.0 spike=1.46
- AMES.CA: score=3.38 buy_ready=False sector_rank=8 price=39.36 support=38.02 resistance=42.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=70960104.0 spike=0.66
- AMIA.CA: score=16.38 buy_ready=False sector_rank=8 price=18.33 support=17.12 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.95 liquidity=11213405.0 spike=0.6
- AMOC.CA: score=17.12 buy_ready=False sector_rank=6 price=13.46 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.27 liquidity=113828672.0 spike=0.87
- APSW.CA: score=5.05 buy_ready=False sector_rank=8 price=7.91 support=7.81 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=663592.88 spike=0.95
- ARAB.CA: score=20.96 buy_ready=False sector_rank=14 price=0.27 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.25 liquidity=143442432.0 spike=1.5
- ARCC.CA: score=15.14 buy_ready=False sector_rank=10 price=65.78 support=60.01 resistance=75.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.58 liquidity=29068188.0 spike=0.92
- AREH.CA: score=6.88 buy_ready=False sector_rank=8 price=1.16 support=1.14 resistance=1.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.92 liquidity=9315682.0 spike=1.09
- ASCM.CA: score=6.16 buy_ready=False sector_rank=8 price=49.19 support=48.0 resistance=53.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20470022.0 spike=2.39
- ASPI.CA: score=7.38 buy_ready=False sector_rank=8 price=0.32 support=0.33 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.66 liquidity=21245628.0 spike=0.59
- ATLC.CA: score=6.08 buy_ready=False sector_rank=11 price=5.29 support=5.2 resistance=7.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.47 liquidity=7948181.0 spike=0.75
- ATQA.CA: score=9.17 buy_ready=False sector_rank=12 price=11.21 support=10.91 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=25.65 liquidity=110096648.0 spike=1.54
- AXPH.CA: score=8.25 buy_ready=False sector_rank=8 price=1373.94 support=1334.35 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.04 liquidity=9109660.0 spike=1.38
- BINV.CA: score=20.68 buy_ready=False sector_rank=3 price=59.73 support=49.91 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=45.19 liquidity=22789116.0 spike=0.9
- BIOC.CA: score=17.38 buy_ready=False sector_rank=8 price=297.27 support=225.21 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=59.51 liquidity=75599656.0 spike=0.75
- BTFH.CA: score=8.71 buy_ready=False sector_rank=11 price=2.67 support=2.64 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.78 liquidity=168393664.0 spike=1.79
- CAED.CA: score=7.84 buy_ready=False sector_rank=8 price=104.22 support=103.1 resistance=150.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.67 liquidity=9460705.0 spike=0.6
- CANA.CA: score=16.46 buy_ready=False sector_rank=7 price=44.97 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=35.25 liquidity=10280070.0 spike=0.43
- CCAP.CA: score=13.68 buy_ready=False sector_rank=3 price=6.25 support=6.18 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=27.37 liquidity=414912544.0 spike=0.58
- CCRS.CA: score=7.71 buy_ready=False sector_rank=8 price=2.08 support=2.06 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=15.56 liquidity=9324919.0 spike=0.66
- CEFM.CA: score=-4.35 buy_ready=False sector_rank=8 price=121.45 support=115.17 resistance=135.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2265271.25 spike=0.78
- CERA.CA: score=12.38 buy_ready=False sector_rank=8 price=1.22 support=1.18 resistance=1.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=106964320.0 spike=0.79
- CFGH.CA: score=-4.72 buy_ready=False sector_rank=8 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12275.24 spike=1.94
- CICH.CA: score=3.4 buy_ready=False sector_rank=11 price=11.0 support=10.75 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=31.85 liquidity=4571412.0 spike=1.35
- CIEB.CA: score=8.04 buy_ready=False sector_rank=7 price=22.75 support=22.94 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.39 liquidity=12332515.0 spike=1.29
- CIRA.CA: score=8.22 buy_ready=False sector_rank=9 price=36.54 support=36.05 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=24.53 liquidity=20594258.0 spike=0.6
- CLHO.CA: score=7.04 buy_ready=False sector_rank=16 price=14.11 support=13.9 resistance=16.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.36 liquidity=45521452.0 spike=1.22
- CNFN.CA: score=8.73 buy_ready=False sector_rank=11 price=3.93 support=3.84 resistance=4.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=29.94 liquidity=15045433.0 spike=1.8
- COMI.CA: score=8.02 buy_ready=False sector_rank=7 price=122.63 support=121.1 resistance=136.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=13.8 liquidity=684136640.0 spike=1.28
- COPR.CA: score=13.44 buy_ready=False sector_rank=8 price=0.46 support=0.44 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.58 liquidity=25745320.0 spike=1.03
- COSG.CA: score=7.38 buy_ready=False sector_rank=8 price=1.39 support=1.46 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=22.03 liquidity=15095526.0 spike=0.98
- CPCI.CA: score=15.64 buy_ready=False sector_rank=8 price=594.11 support=530.0 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=71.98 liquidity=6117744.0 spike=1.57
- CSAG.CA: score=10.74 buy_ready=False sector_rank=5 price=35.19 support=34.52 resistance=39.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=30.33 liquidity=12575869.0 spike=1.65
- DAPH.CA: score=8.8 buy_ready=False sector_rank=8 price=95.95 support=89.1 resistance=129.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.99 liquidity=47080192.0 spike=1.21
- DEIN.CA: score=6.38 buy_ready=False sector_rank=8 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 09:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37.26 spike=0.01
- DOMT.CA: score=4.61 buy_ready=False sector_rank=17 price=23.23 support=23.45 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=35.18 liquidity=3205131.25 spike=0.63
- DSCW.CA: score=7.4 buy_ready=False sector_rank=8 price=1.58 support=1.58 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=21.88 liquidity=18864840.0 spike=1.01
- DTPP.CA: score=3.38 buy_ready=False sector_rank=8 price=260.61 support=250.0 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32511478.0 spike=0.38
- EALR.CA: score=1.23 buy_ready=False sector_rank=8 price=309.99 support=312.0 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.38 liquidity=3841540.5 spike=0.4
- EASB.CA: score=-0.08 buy_ready=False sector_rank=8 price=6.87 support=6.54 resistance=7.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6540063.5 spike=0.89
- EAST.CA: score=6.4 buy_ready=False sector_rank=17 price=27.34 support=27.16 resistance=34.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=14.7 liquidity=35666404.0 spike=0.75
- EBSC.CA: score=-5.0 buy_ready=False sector_rank=8 price=1.59 support=1.5 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1616932.88 spike=0.66
- ECAP.CA: score=-1.08 buy_ready=False sector_rank=8 price=27.97 support=27.5 resistance=30.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5097380.0 spike=1.22
- EDFM.CA: score=7.45 buy_ready=False sector_rank=8 price=390.57 support=354.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=47.76 liquidity=1469299.75 spike=1.3
- EEII.CA: score=6.29 buy_ready=False sector_rank=8 price=1.94 support=1.83 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=32.84 liquidity=6904070.0 spike=0.73
- EFIC.CA: score=7.09 buy_ready=False sector_rank=12 price=153.76 support=147.0 resistance=211.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=22.43 liquidity=29045558.0 spike=0.67
- EFID.CA: score=8.88 buy_ready=False sector_rank=17 price=18.23 support=18.1 resistance=31.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.05 liquidity=64103628.0 spike=1.24
- EFIH.CA: score=21.78 buy_ready=False sector_rank=2 price=23.64 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.77 liquidity=89450968.0 spike=1.36
- EGAL.CA: score=9.17 buy_ready=False sector_rank=12 price=315.95 support=325.07 resistance=376.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=16.82 liquidity=81716920.0 spike=1.54
- EGAS.CA: score=9.09 buy_ready=False sector_rank=6 price=51.4 support=51.0 resistance=60.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.11 liquidity=9972754.0 spike=0.89
- EGBE.CA: score=3.67 buy_ready=False sector_rank=7 price=0.52 support=0.49 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=64.1 liquidity=127710.8 spike=1.04
- EGCH.CA: score=4.63 buy_ready=False sector_rank=12 price=11.99 support=11.86 resistance=12.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=139005232.0 spike=1.77
- EGSA.CA: score=7.14 buy_ready=False sector_rank=1 price=8.87 support=8.82 resistance=9.08 source=Yahoo Finance as_of=2026-10-11T21:00:00+00:00 freshness=FRESH RSI=11.76 liquidity=0.0 spike=0.0
- EGTS.CA: score=12.96 buy_ready=False sector_rank=14 price=13.83 support=14.02 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=35.11 liquidity=15246098.0 spike=0.44
- EHDR.CA: score=7.98 buy_ready=False sector_rank=8 price=2.25 support=2.31 resistance=2.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=25.33 liquidity=15099010.0 spike=1.3
- ELEC.CA: score=6.4 buy_ready=False sector_rank=18 price=1.69 support=1.72 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=25.53 liquidity=40164104.0 spike=0.69
- ELKA.CA: score=12.5 buy_ready=False sector_rank=8 price=1.46 support=1.43 resistance=1.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.09 liquidity=14186696.0 spike=1.06
- ELNA.CA: score=4.48 buy_ready=False sector_rank=8 price=35.22 support=33.46 resistance=36.4 source=Yahoo Finance as_of=2026-10-11T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=97418.52 spike=0.62
- ELSH.CA: score=8.44 buy_ready=False sector_rank=8 price=10.9 support=10.8 resistance=13.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.81 liquidity=21358222.0 spike=1.03
- ELWA.CA: score=7.56 buy_ready=False sector_rank=8 price=1.65 support=1.43 resistance=1.8 source=Yahoo Finance as_of=2026-10-11T21:00:00+00:00 freshness=FRESH RSI=46.67 liquidity=179741.1 spike=0.29
- EMFD.CA: score=12.96 buy_ready=False sector_rank=14 price=11.96 support=11.7 resistance=14.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.89 liquidity=35698084.0 spike=0.5
- ENGC.CA: score=7.9 buy_ready=False sector_rank=8 price=33.37 support=33.33 resistance=45.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=24.36 liquidity=22406912.0 spike=1.26
- EOSB.CA: score=9.46 buy_ready=False sector_rank=8 price=1.57 support=1.64 resistance=1.64 source=Yahoo Finance as_of=2026-10-11T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=79288.14 spike=1.5
- EPCO.CA: score=-1.81 buy_ready=False sector_rank=8 price=8.7 support=8.0 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4807763.5 spike=0.74
- EPPK.CA: score=-6.2 buy_ready=False sector_rank=8 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=26.2 buy_ready=False sector_rank=1 price=145.48 support=124.01 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.43 liquidity=271802816.0 spike=1.03
- ETRS.CA: score=13.88 buy_ready=False sector_rank=8 price=10.46 support=9.82 resistance=11.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=13258793.0 spike=1.25
- EXPA.CA: score=7.46 buy_ready=False sector_rank=7 price=14.39 support=14.8 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=9.08 liquidity=27429300.0 spike=0.71
- FAIT.CA: score=2.55 buy_ready=False sector_rank=7 price=42.5 support=38.48 resistance=47.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.79 liquidity=3648163.0 spike=1.22
- FAITA.CA: score=4.48 buy_ready=False sector_rank=7 price=0.98 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=17230.25 spike=0.59
- FERC.CA: score=2.5 buy_ready=False sector_rank=12 price=69.75 support=70.0 resistance=82.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.99 liquidity=5415675.0 spike=0.9
- FWRY.CA: score=18.06 buy_ready=False sector_rank=2 price=18.34 support=17.5 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.76 liquidity=82911240.0 spike=0.72
- GBCO.CA: score=12.93 buy_ready=False sector_rank=15 price=29.8 support=27.0 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.81 liquidity=74686536.0 spike=0.74
- GDWA.CA: score=7.38 buy_ready=False sector_rank=8 price=0.61 support=0.61 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=18.1 liquidity=13202059.0 spike=0.6
- GGCC.CA: score=8.14 buy_ready=False sector_rank=8 price=0.64 support=0.65 resistance=0.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=22.26 liquidity=9757902.0 spike=0.74
- GIHD.CA: score=10.32 buy_ready=False sector_rank=8 price=55.84 support=53.3 resistance=78.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.06 liquidity=36659320.0 spike=1.97
- GMCI.CA: score=4.62 buy_ready=False sector_rank=8 price=1.61 support=1.49 resistance=1.87 source=Yahoo Finance as_of=2026-10-11T21:00:00+00:00 freshness=FRESH RSI=36.84 liquidity=232163.61 spike=0.52
- GRCA.CA: score=1.45 buy_ready=False sector_rank=8 price=32.03 support=30.51 resistance=34.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8067048.5 spike=0.49
- GSSC.CA: score=-0.97 buy_ready=False sector_rank=8 price=256.99 support=246.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=30.7 liquidity=642145.31 spike=0.18
- GTWL.CA: score=9.62 buy_ready=False sector_rank=8 price=142.17 support=124.5 resistance=241.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.59 liquidity=244123824.0 spike=1.62
- HDBK.CA: score=10.46 buy_ready=False sector_rank=7 price=103.48 support=102.03 resistance=121.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.94 liquidity=27331494.0 spike=1.0
- HELI.CA: score=7.96 buy_ready=False sector_rank=14 price=7.12 support=6.94 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.63 liquidity=68122016.0 spike=0.62
- HRHO.CA: score=16.13 buy_ready=False sector_rank=11 price=25.19 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.67 liquidity=96683928.0 spike=0.72
- ICID.CA: score=8.84 buy_ready=False sector_rank=8 price=17.53 support=16.52 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=58.89 liquidity=2458744.75 spike=0.32
- IDRE.CA: score=6.58 buy_ready=False sector_rank=8 price=42.02 support=42.1 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.62 liquidity=9193871.0 spike=0.62
- IFAP.CA: score=6.85 buy_ready=False sector_rank=19 price=18.26 support=17.17 resistance=21.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.32 liquidity=9889883.0 spike=1.28
- INFI.CA: score=14.11 buy_ready=False sector_rank=8 price=113.87 support=104.0 resistance=146.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.31 liquidity=8725219.0 spike=0.62
- IRON.CA: score=14.09 buy_ready=False sector_rank=12 price=26.92 support=25.01 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=51.58 liquidity=11512691.0 spike=0.99
- ISMA.CA: score=5.28 buy_ready=False sector_rank=8 price=21.62 support=18.91 resistance=24.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14883393.0 spike=1.95
- ISMQ.CA: score=7.09 buy_ready=False sector_rank=12 price=7.47 support=7.6 resistance=9.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.71 liquidity=16568647.0 spike=0.84
- ISPH.CA: score=6.8 buy_ready=False sector_rank=16 price=11.15 support=11.09 resistance=12.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.36 liquidity=67893632.0 spike=1.1
- JUFO.CA: score=7.24 buy_ready=False sector_rank=17 price=24.02 support=24.4 resistance=27.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.89 liquidity=23752846.0 spike=1.42
- KABO.CA: score=3.17 buy_ready=False sector_rank=13 price=7.52 support=7.36 resistance=8.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28967876.0 spike=1.06
- KWIN.CA: score=1.61 buy_ready=False sector_rank=8 price=65.38 support=60.0 resistance=71.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8227114.5 spike=0.83
- KZPC.CA: score=16.82 buy_ready=False sector_rank=8 price=12.76 support=12.15 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.13 liquidity=12783795.0 spike=1.22
- LCSW.CA: score=15.3 buy_ready=False sector_rank=10 price=32.8 support=28.86 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.87 liquidity=20755948.0 spike=1.08
- LUTS.CA: score=3.52 buy_ready=False sector_rank=8 price=0.77 support=0.65 resistance=0.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=68833864.0 spike=1.07
- MAAL.CA: score=3.25 buy_ready=False sector_rank=8 price=8.98 support=8.8 resistance=9.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9861140.0 spike=0.42
- MASR.CA: score=15.9 buy_ready=False sector_rank=8 price=7.12 support=6.82 resistance=8.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.76 liquidity=77383648.0 spike=1.26
- MBSC.CA: score=15.14 buy_ready=False sector_rank=10 price=332.53 support=288.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.58 liquidity=73039008.0 spike=0.88
- MCQE.CA: score=13.26 buy_ready=False sector_rank=10 price=176.0 support=177.02 resistance=228.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.76 liquidity=78857464.0 spike=1.56
- MCRO.CA: score=8.38 buy_ready=False sector_rank=8 price=1.36 support=1.41 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.43 liquidity=31642436.0 spike=0.43
- MENA.CA: score=5.93 buy_ready=False sector_rank=14 price=5.87 support=5.8 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=36.61 liquidity=974687.75 spike=0.58
- MEPA.CA: score=6.09 buy_ready=False sector_rank=8 price=1.56 support=1.56 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=29.58 liquidity=8708850.0 spike=0.77
- MFPC.CA: score=11.09 buy_ready=False sector_rank=12 price=44.02 support=43.0 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=29.49 liquidity=62748952.0 spike=0.66
- MFSC.CA: score=-1.37 buy_ready=False sector_rank=8 price=38.18 support=39.0 resistance=49.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=28.76 liquidity=1242974.75 spike=0.48
- MICH.CA: score=13.58 buy_ready=False sector_rank=8 price=44.07 support=42.01 resistance=50.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.68 liquidity=10285165.0 spike=1.1
- MILS.CA: score=0.37 buy_ready=False sector_rank=8 price=155.22 support=147.06 resistance=174.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6985233.0 spike=0.82
- MIPH.CA: score=2.47 buy_ready=False sector_rank=16 price=770.74 support=739.69 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=26.09 liquidity=4861342.0 spike=0.57
- MOED.CA: score=3.38 buy_ready=False sector_rank=8 price=0.6 support=0.57 resistance=0.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18859902.0 spike=0.61
- MOIL.CA: score=1.35 buy_ready=False sector_rank=6 price=0.67 support=0.67 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=26.47 liquidity=509528.41 spike=1.86
- MOIN.CA: score=3.38 buy_ready=False sector_rank=8 price=31.66 support=31.0 resistance=34.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11597797.0 spike=0.9
- MOSC.CA: score=4.99 buy_ready=False sector_rank=8 price=257.94 support=257.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.35 liquidity=1607280.38 spike=0.5
- MPCI.CA: score=8.38 buy_ready=False sector_rank=8 price=310.64 support=305.45 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.43 liquidity=94996664.0 spike=0.9
- MPCO.CA: score=7.44 buy_ready=False sector_rank=19 price=2.11 support=2.17 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=15.62 liquidity=145840608.0 spike=1.02
- MPRC.CA: score=15.38 buy_ready=False sector_rank=8 price=36.39 support=36.53 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.59 liquidity=13155448.0 spike=0.76
- MTIE.CA: score=7.57 buy_ready=False sector_rank=15 price=7.46 support=7.5 resistance=8.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=30.32 liquidity=22466790.0 spike=1.32
- NAHO.CA: score=3.4 buy_ready=False sector_rank=8 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=46.15 liquidity=16969.67 spike=0.47
- NCCW.CA: score=3.38 buy_ready=False sector_rank=8 price=5.9 support=5.3 resistance=6.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28418404.0 spike=0.56
- NEDA.CA: score=-1.45 buy_ready=False sector_rank=8 price=2.6 support=2.48 resistance=2.8 source=Yahoo Finance as_of=2026-10-11T21:00:00+00:00 freshness=FRESH RSI=25.71 liquidity=166428.59 spike=0.24
- NHPS.CA: score=11.24 buy_ready=False sector_rank=8 price=65.21 support=66.0 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=41.45 liquidity=8856222.0 spike=0.61
- NINH.CA: score=8.42 buy_ready=False sector_rank=8 price=16.63 support=17.27 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=20.63 liquidity=14796876.0 spike=1.02
- NIPH.CA: score=2.6 buy_ready=False sector_rank=16 price=273.3 support=241.0 resistance=299.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=119572776.0 spike=0.96
- OBRI.CA: score=14.76 buy_ready=False sector_rank=8 price=25.28 support=22.8 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.96 liquidity=16649942.0 spike=1.19
- OCDI.CA: score=7.96 buy_ready=False sector_rank=14 price=25.0 support=24.2 resistance=31.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=29.11 liquidity=20895538.0 spike=0.42
- OCPH.CA: score=7.35 buy_ready=False sector_rank=8 price=201.57 support=190.0 resistance=251.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=35.21 liquidity=2968972.5 spike=0.8
- ODIN.CA: score=5.22 buy_ready=False sector_rank=8 price=2.2 support=2.29 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.36 liquidity=7832034.0 spike=0.87
- OFH.CA: score=8.38 buy_ready=False sector_rank=8 price=0.79 support=0.81 resistance=1.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.31 liquidity=30509866.0 spike=0.31
- OIH.CA: score=10.68 buy_ready=False sector_rank=3 price=1.79 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.4 liquidity=82145328.0 spike=0.91
- OLFI.CA: score=6.4 buy_ready=False sector_rank=17 price=20.23 support=20.8 resistance=23.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=19.38 liquidity=11576561.0 spike=0.64
- ORAS.CA: score=4.6 buy_ready=False sector_rank=4 price=884.22 support=845.02 resistance=900.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=402873600.0 spike=1.0
- ORHD.CA: score=7.36 buy_ready=False sector_rank=14 price=10.76 support=10.9 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=2.71 liquidity=179385888.0 spike=1.2
- ORWE.CA: score=13.07 buy_ready=False sector_rank=13 price=26.54 support=26.01 resistance=28.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=44.94 liquidity=39331900.0 spike=1.01
- PHAR.CA: score=12.6 buy_ready=False sector_rank=16 price=105.14 support=102.0 resistance=125.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=40.69 liquidity=54286912.0 spike=0.73
- PHDC.CA: score=14.96 buy_ready=False sector_rank=14 price=12.52 support=12.36 resistance=14.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.0 liquidity=92015120.0 spike=0.94
- PHTV.CA: score=3.98 buy_ready=False sector_rank=8 price=337.0 support=315.1 resistance=378.89 source=Yahoo Finance as_of=2026-10-11T21:00:00+00:00 freshness=FRESH RSI=43.38 liquidity=595816.0 spike=0.51
- POUL.CA: score=6.4 buy_ready=False sector_rank=17 price=9.52 support=9.12 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=1.92 liquidity=23587450.0 spike=0.71
- PRCL.CA: score=3.18 buy_ready=False sector_rank=10 price=21.55 support=21.0 resistance=24.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12338662.0 spike=1.02
- PRDC.CA: score=13.2 buy_ready=False sector_rank=14 price=6.31 support=6.62 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.9 liquidity=39246972.0 spike=1.12
- PRMH.CA: score=-1.96 buy_ready=False sector_rank=8 price=1.86 support=1.8 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4395964.0 spike=1.13
- RACC.CA: score=8.04 buy_ready=False sector_rank=8 price=8.84 support=8.51 resistance=10.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.75 liquidity=5653803.5 spike=0.85
- RAKT.CA: score=5.79 buy_ready=False sector_rank=8 price=22.06 support=20.26 resistance=25.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=64.25 liquidity=482543.84 spike=1.46
- RAYA.CA: score=6.44 buy_ready=False sector_rank=20 price=5.89 support=5.72 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=31.78 liquidity=36499364.0 spike=1.02
- RMDA.CA: score=7.6 buy_ready=False sector_rank=16 price=5.25 support=4.83 resistance=6.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.52 liquidity=25929750.0 spike=0.92
- ROTO.CA: score=14.36 buy_ready=False sector_rank=8 price=37.23 support=35.02 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=42.55 liquidity=8893029.0 spike=1.04
- RREI.CA: score=8.44 buy_ready=False sector_rank=8 price=3.44 support=3.46 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=25.79 liquidity=10215251.0 spike=1.03
- RTVC.CA: score=3.17 buy_ready=False sector_rank=8 price=3.39 support=3.37 resistance=4.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.93 liquidity=4427682.5 spike=1.68
- RUBX.CA: score=3.38 buy_ready=False sector_rank=8 price=15.75 support=14.01 resistance=17.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=89858544.0 spike=0.92
- SAUD.CA: score=5.48 buy_ready=False sector_rank=7 price=21.5 support=21.6 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=26.82 liquidity=7019435.5 spike=0.36
- SCEM.CA: score=15.14 buy_ready=False sector_rank=10 price=83.66 support=74.55 resistance=98.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.15 liquidity=34671804.0 spike=0.55
- SCFM.CA: score=-1.52 buy_ready=False sector_rank=8 price=232.24 support=223.11 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=33.07 liquidity=1095816.63 spike=0.56
- SCTS.CA: score=-1.14 buy_ready=False sector_rank=9 price=510.15 support=511.01 resistance=635.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=29.73 liquidity=635312.63 spike=0.42
- SDTI.CA: score=16.38 buy_ready=False sector_rank=8 price=83.15 support=71.5 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.77 liquidity=16328046.0 spike=0.49
- SEIG.CA: score=-4.96 buy_ready=False sector_rank=8 price=197.67 support=173.1 resistance=219.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1652853.13 spike=0.73
- SIPC.CA: score=15.9 buy_ready=False sector_rank=8 price=5.12 support=4.22 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.97 liquidity=61342124.0 spike=1.26
- SKPC.CA: score=7.63 buy_ready=False sector_rank=12 price=15.1 support=15.4 resistance=18.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=18.27 liquidity=105154232.0 spike=1.27
- SMFR.CA: score=-0.44 buy_ready=False sector_rank=8 price=206.08 support=181.6 resistance=234.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5251058.5 spike=1.46
- SNFC.CA: score=9.24 buy_ready=False sector_rank=8 price=11.06 support=10.58 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.91 liquidity=5859424.0 spike=0.47
- SPIN.CA: score=5.04 buy_ready=False sector_rank=13 price=15.0 support=15.11 resistance=18.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.15 liquidity=6710484.5 spike=1.14
- SPMD.CA: score=7.38 buy_ready=False sector_rank=8 price=0.35 support=0.36 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=12564150.0 spike=0.17
- SUGR.CA: score=12.25 buy_ready=False sector_rank=17 price=52.51 support=50.5 resistance=63.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.14 liquidity=9848663.0 spike=0.8
- SVCE.CA: score=8.38 buy_ready=False sector_rank=8 price=9.36 support=9.24 resistance=12.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=29.67 liquidity=60181412.0 spike=0.66
- SWDY.CA: score=7.76 buy_ready=False sector_rank=18 price=111.18 support=102.31 resistance=129.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.65 liquidity=70856256.0 spike=1.18
- TALM.CA: score=18.22 buy_ready=False sector_rank=9 price=21.14 support=18.71 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.36 liquidity=42052632.0 spike=0.58
- TMGH.CA: score=8.8 buy_ready=False sector_rank=14 price=83.78 support=84.08 resistance=98.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.62 liquidity=413241568.0 spike=1.92
- TRTO.CA: score=5.39 buy_ready=False sector_rank=8 price=0.07 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-10-11T21:00:00+00:00 freshness=FRESH RSI=78.95 liquidity=5386.9 spike=0.54
- UEFM.CA: score=7.11 buy_ready=False sector_rank=8 price=494.16 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.11 liquidity=1729977.25 spike=0.52
- UEGC.CA: score=9.38 buy_ready=False sector_rank=8 price=1.4 support=1.37 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.76 liquidity=20335078.0 spike=0.61
- UNIP.CA: score=3.52 buy_ready=False sector_rank=8 price=0.31 support=0.31 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11064430.0 spike=1.07
- UNIT.CA: score=5.62 buy_ready=False sector_rank=14 price=16.61 support=16.41 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=36.2 liquidity=2659239.75 spike=0.16
- WCDF.CA: score=2.25 buy_ready=False sector_rank=8 price=549.27 support=515.0 resistance=599.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6850844.5 spike=2.01
- WKOL.CA: score=-0.37 buy_ready=False sector_rank=8 price=275.13 support=266.18 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.27 liquidity=2241511.25 spike=0.2
- ZEOT.CA: score=1.83 buy_ready=False sector_rank=8 price=10.17 support=9.75 resistance=11.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7663534.0 spike=1.39
- ZMID.CA: score=7.96 buy_ready=False sector_rank=14 price=7.2 support=7.07 resistance=9.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=17.99 liquidity=77211888.0 spike=0.74

## Backtesting Lite
- ETEL.CA: 180d return=109.78%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-10-11T21:00:00+00:00
- EFIH.CA: 180d return=27.23%, max drawdown=-22.68%, MA20>MA50 days last20=8, as_of=2026-10-11T21:00:00+00:00
- ARAB.CA: 180d return=36.63%, max drawdown=-26.79%, MA20>MA50 days last20=12, as_of=2026-10-11T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- AJWA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=AJWA For Food Industries Co. Egypt summary=Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture; AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3; Ajwa Egypt turns to losses in 9M
  - Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture: https://english.mubasher.info/news/4532004/Ajwa-Egypt-s-board-approves-capital-increase-to-EGP-500m-joins-new-food-venture/
  - AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3: https://english.mubasher.info/news/4527545/AJWA-Egypt-s-standalone-net-profits-retreat-to-EGP-14m-in-9M-25-amid-shift-to-profitability-in-Q3/
  - Ajwa Egypt turns to losses in 9M: https://english.mubasher.info/news/3883210/Ajwa-Egypt-turns-to-losses-in-9M/
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- FWRY.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Fawry For Banking Technology and Electronic Payments summary=Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.

## Warnings
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Evidence for AJWA.CA matches the company but no source/report date was detected.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
