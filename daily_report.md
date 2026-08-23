# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-08-23T07:01:50.506607+00:00
Generated Cairo: 2026-08-23 10:01
Run timing: target 09:15 Cairo | generated Cairo 2026-08-23 10:01 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-08-23 09:58

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 186/189
- Top sector: Textiles

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, August 20
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 75.0% / above MA50 75.0%
- EGX70 regime: MIXED / above MA20 55.0% / above MA50 75.0%
- Sector breadth: 33.33%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=644385216.0 spike=1.33 score=15.06
- LUTS.CA: liquidity=637980416.0 spike=4.39 score=23.3
- CCAP.CA: liquidity=444538624.0 spike=0.75 score=25.4
- GTWL.CA: liquidity=384987776.0 spike=2.05 score=20.4
- ZMID.CA: liquidity=365721536.0 spike=1.5 score=21.26

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are both in a mixed trend with weak sector breadth (33.3%), prompting a defensive risk mode that blocks new buys. The scanner flagged several tickets with accumulation-spike liquidity and constructive/outlook scores, but their RSI is overheated, prices sit far above 20‑day support, and their sectors are not among the leaders, limiting near‑term upside.
- Liquidity shows accumulation spikes, indicating short‑term buying interest, yet RSI >70 for many tickets signals overheating.
- Prices are well above 20‑day support (support distance 9‑29%) and close to resistance, leaving limited room for gains before a pull‑back.
- Sectors of the highlighted stocks (General/Verified EGX Expansion, Textiles, Transportation) are not leading, reducing conviction in sustained moves.
- EGX30/EGX70 mixed trend and low breadth keep the market in a defensive regime, so any upside is uncertain and likely limited to 1‑3 days.
- Outlook tags range from constructive to bullish watch, but the defensive risk mode and weak breadth introduce notable uncertainty.

## Top Liquidity Spikes
- AXPH.CA: spike=7.94 liquidity=52138472.0 outlook=CONSTRUCTIVE score=69.74 buy_ready=False
- KZPC.CA: spike=7.92 liquidity=310351552.0 outlook=CONSTRUCTIVE score=69.74 buy_ready=False
- GRCA.CA: spike=5.19 liquidity=137979168.0 outlook=BULLISH_WATCH score=93.74 buy_ready=False
- LUTS.CA: spike=4.39 liquidity=637980416.0 outlook=CONSTRUCTIVE score=55.74 buy_ready=False
- MOED.CA: spike=4.37 liquidity=324859456.0 outlook=CONSTRUCTIVE score=63.74 buy_ready=False

## Sector Leaderboard
- #1 Textiles: score=13.63 5d=8.11% 20d=16.16% aboveMA50=100.0%
- #2 Transportation & Logistics: score=11.06 5d=-1.54% 20d=14.23% aboveMA50=100.0%
- #3 Education: score=10.16 5d=0.4% 20d=17.32% aboveMA50=100.0%
- #4 Healthcare: score=8.84 5d=-4.19% 20d=17.75% aboveMA50=100.0%
- #5 Banking & Financials: score=8.7 5d=0.24% 20d=9.59% aboveMA50=90.0%
- #6 Building Materials: score=8.69 5d=-1.94% 20d=20.36% aboveMA50=83.33%
- #7 Investment Holding: score=7.98 5d=3.83% 20d=1.63% aboveMA50=100.0%
- #8 Agriculture & Food Production: score=7.86 5d=-1.62% 20d=13.87% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- KABO.CA: BULLISH_WATCH score=99 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- ALCN.CA: BULLISH_WATCH score=99 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- SCTS.CA: BULLISH_WATCH score=96 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- GRCA.CA: BULLISH_WATCH score=93.74 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- KWIN.CA: BULLISH_WATCH score=91.74 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- CIRA.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- TALM.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- MIPH.CA: BULLISH_WATCH score=83.84 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- EXPA.CA: BULLISH_WATCH score=83.7 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA20
- NHPS.CA: BULLISH_WATCH score=81.74 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=23.3 buy_ready=False sector_rank=12 price=320.43 support=235.7 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=53.37 liquidity=24734320.0 spike=0.42
- ABUK.CA: score=23.4 buy_ready=False sector_rank=11 price=75.86 support=70.6 resistance=80.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=54.85 liquidity=75610176.0 spike=0.67
- ACAMD.CA: score=11.3 buy_ready=False sector_rank=12 price=2.09 support=2.09 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=31.75 liquidity=57209004.0 spike=0.96
- ACGC.CA: score=23.98 buy_ready=False sector_rank=1 price=13.61 support=10.12 resistance=13.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=77.37 liquidity=56789812.0 spike=1.29
- ADCI.CA: score=18.36 buy_ready=False sector_rank=12 price=286.96 support=245.0 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=48.93 liquidity=7062755.5 spike=0.32
- ADIB.CA: score=21.4 buy_ready=False sector_rank=5 price=54.0 support=48.62 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=51.58 liquidity=85355288.0 spike=0.78
- ADPC.CA: score=19.3 buy_ready=False sector_rank=12 price=3.98 support=3.81 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=42527192.0 spike=0.81
- AFDI.CA: score=19.3 buy_ready=False sector_rank=12 price=62.53 support=48.35 resistance=69.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=66.32 liquidity=10990752.0 spike=0.45
- AFMC.CA: score=21.3 buy_ready=False sector_rank=12 price=229.02 support=102.11 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=53.06 liquidity=67262016.0 spike=0.38
- AJWA.CA: score=21.3 buy_ready=False sector_rank=12 price=192.0 support=175.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=51.21 liquidity=24281582.0 spike=0.52
- ALCN.CA: score=25.52 buy_ready=False sector_rank=2 price=31.59 support=28.8 resistance=32.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=65.03 liquidity=49238444.0 spike=2.06
- ALUM.CA: score=19.1 buy_ready=False sector_rank=12 price=26.58 support=22.72 resistance=30.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:13 PM market time freshness=DELAYED_CURRENT RSI=68.23 liquidity=7802107.0 spike=0.38
- AMER.CA: score=20.26 buy_ready=False sector_rank=17 price=5.74 support=4.14 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=59.61 liquidity=73311792.0 spike=0.73
- AMES.CA: score=24.66 buy_ready=False sector_rank=12 price=149.6 support=110.54 resistance=173.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=69.62 liquidity=187827088.0 spike=2.68
- AMIA.CA: score=19.82 buy_ready=False sector_rank=12 price=16.1 support=10.2 resistance=17.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=94.38 liquidity=60799616.0 spike=1.76
- AMOC.CA: score=21.16 buy_ready=False sector_rank=13 price=11.4 support=8.23 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=72.41 liquidity=103927512.0 spike=0.77
- APSW.CA: score=9.56 buy_ready=False sector_rank=12 price=8.79 support=8.6 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=52.67 liquidity=1266763.13 spike=0.65
- ARAB.CA: score=15.26 buy_ready=False sector_rank=17 price=0.23 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=36.67 liquidity=38480652.0 spike=0.5
- ARCC.CA: score=18.4 buy_ready=False sector_rank=6 price=72.49 support=55.4 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=79.63 liquidity=31745292.0 spike=0.32
- AREH.CA: score=16.3 buy_ready=False sector_rank=12 price=1.46 support=1.38 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=54.0 liquidity=11327742.0 spike=0.35
- ARVA.CA: score=6.3 buy_ready=False sector_rank=12 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=14.3 buy_ready=False sector_rank=12 price=63.89 support=60.99 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=34.64 liquidity=29155050.0 spike=0.5
- ASPI.CA: score=21.3 buy_ready=False sector_rank=12 price=0.5 support=0.36 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=66.37 liquidity=35242188.0 spike=0.86
- ATLC.CA: score=16.68 buy_ready=False sector_rank=19 price=5.26 support=5.0 resistance=5.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=45.31 liquidity=9143313.0 spike=0.48
- ATQA.CA: score=18.4 buy_ready=False sector_rank=11 price=11.0 support=9.66 resistance=11.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=77.25 liquidity=56051008.0 spike=0.73
- AXPH.CA: score=28.3 buy_ready=False sector_rank=12 price=1442.39 support=1121.56 resistance=1630.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=73.95 liquidity=52138472.0 spike=7.94
- BINV.CA: score=10.78 buy_ready=False sector_rank=7 price=48.44 support=46.01 resistance=50.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=54.73 liquidity=1383349.0 spike=0.2
- BIOC.CA: score=21.3 buy_ready=False sector_rank=12 price=425.03 support=116.25 resistance=563.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=63.54 liquidity=86135152.0 spike=0.37
- BTFH.CA: score=8.54 buy_ready=False sector_rank=19 price=2.98 support=2.98 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=207124160.0 spike=0.93
- CAED.CA: score=18.3 buy_ready=False sector_rank=12 price=164.93 support=118.0 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=78.03 liquidity=51510180.0 spike=0.92
- CANA.CA: score=18.4 buy_ready=False sector_rank=5 price=41.63 support=36.5 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=76.15 liquidity=16523238.0 spike=0.78
- CCAP.CA: score=25.4 buy_ready=False sector_rank=7 price=5.59 support=5.14 resistance=5.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=62.37 liquidity=444538624.0 spike=0.75
- CCRS.CA: score=7.71 buy_ready=False sector_rank=12 price=2.41 support=2.4 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=34.78 liquidity=6416074.0 spike=0.38
- CEFM.CA: score=25.3 buy_ready=False sector_rank=12 price=151.16 support=121.4 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=63.22 liquidity=31726376.0 spike=0.86
- CERA.CA: score=13.06 buy_ready=False sector_rank=12 price=1.26 support=1.23 resistance=1.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=35.71 liquidity=6768865.0 spike=0.41
- CFGH.CA: score=5.3 buy_ready=False sector_rank=12 price=0.11 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=81.25 liquidity=4728.98 spike=0.31
- CICH.CA: score=13.78 buy_ready=False sector_rank=19 price=12.24 support=11.92 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=38.75 liquidity=6248458.0 spike=0.89
- CIEB.CA: score=20.1 buy_ready=False sector_rank=5 price=24.58 support=23.75 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=60.23 liquidity=6698972.5 spike=0.49
- CIRA.CA: score=22.4 buy_ready=False sector_rank=3 price=37.18 support=31.61 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=52.16 liquidity=13177185.0 spike=0.24
- CLHO.CA: score=21.88 buy_ready=False sector_rank=4 price=17.43 support=16.0 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=36.44 liquidity=78454216.0 spike=1.24
- CNFN.CA: score=17.54 buy_ready=False sector_rank=19 price=4.81 support=4.68 resistance=5.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=47.17 liquidity=12935078.0 spike=0.66
- COMI.CA: score=15.06 buy_ready=False sector_rank=5 price=138.03 support=135.35 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=28.45 liquidity=644385216.0 spike=1.33
- COPR.CA: score=28.3 buy_ready=False sector_rank=12 price=0.52 support=0.39 resistance=0.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=74.44 liquidity=281856128.0 spike=3.65
- COSG.CA: score=22.96 buy_ready=False sector_rank=12 price=1.82 support=1.6 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=69.44 liquidity=92513640.0 spike=1.83
- CPCI.CA: score=20.92 buy_ready=False sector_rank=12 price=532.09 support=440.01 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=67.16 liquidity=15056711.0 spike=1.81
- CSAG.CA: score=24.82 buy_ready=False sector_rank=2 price=41.52 support=31.35 resistance=43.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=73.88 liquidity=41400800.0 spike=1.71
- DAPH.CA: score=23.78 buy_ready=False sector_rank=12 price=110.32 support=92.1 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=59.86 liquidity=52061976.0 spike=1.24
- DEIN.CA: score=-3.7 buy_ready=False sector_rank=12 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=13.92 buy_ready=False sector_rank=16 price=28.13 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=57.91 liquidity=5602023.0 spike=0.37
- DSCW.CA: score=19.3 buy_ready=False sector_rank=12 price=1.91 support=1.89 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=44.23 liquidity=61884408.0 spike=0.67
- DTPP.CA: score=19.3 buy_ready=False sector_rank=12 price=296.22 support=225.11 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=71.07 liquidity=20961340.0 spike=0.38
- EALR.CA: score=23.3 buy_ready=False sector_rank=12 price=394.03 support=362.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=48.71 liquidity=18019578.0 spike=0.37
- EASB.CA: score=12.61 buy_ready=False sector_rank=12 price=7.18 support=6.71 resistance=8.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=6309801.0 spike=0.64
- EAST.CA: score=16.32 buy_ready=False sector_rank=16 price=36.03 support=36.0 resistance=37.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=42.21 liquidity=24816720.0 spike=0.41
- EBSC.CA: score=8.81 buy_ready=False sector_rank=12 price=1.89 support=1.85 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=48.0 liquidity=2513759.0 spike=0.47
- ECAP.CA: score=23.3 buy_ready=False sector_rank=12 price=36.23 support=32.12 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=57.82 liquidity=11863147.0 spike=0.94
- EDFM.CA: score=10.74 buy_ready=False sector_rank=12 price=407.14 support=352.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:08 PM market time freshness=DELAYED_CURRENT RSI=65.26 liquidity=1444224.88 spike=0.36
- EEII.CA: score=22.72 buy_ready=False sector_rank=12 price=3.04 support=2.54 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=40432348.0 spike=1.71
- EFIC.CA: score=23.4 buy_ready=False sector_rank=11 price=213.65 support=184.0 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=61.75 liquidity=29552814.0 spike=0.65
- EFID.CA: score=17.32 buy_ready=False sector_rank=16 price=32.17 support=26.64 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=83.6 liquidity=18746882.0 spike=0.21
- EFIH.CA: score=21.4 buy_ready=False sector_rank=9 price=24.46 support=22.15 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=65.65 liquidity=61508124.0 spike=0.51
- EGAL.CA: score=21.4 buy_ready=False sector_rank=11 price=331.78 support=292.0 resistance=359.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=70.89 liquidity=74328072.0 spike=0.72
- EGAS.CA: score=10.13 buy_ready=False sector_rank=13 price=56.99 support=50.0 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=30.48 liquidity=5973912.5 spike=0.24
- EGBE.CA: score=14.54 buy_ready=False sector_rank=5 price=0.55 support=0.47 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=69.5 liquidity=681962.25 spike=3.23
- EGCH.CA: score=19.4 buy_ready=False sector_rank=11 price=13.79 support=12.69 resistance=14.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=52.29 liquidity=96747720.0 spike=0.79
- EGSA.CA: score=6.2 buy_ready=False sector_rank=14 price=8.69 support=8.65 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:02 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=17387.16 spike=1.02
- EGTS.CA: score=16.16 buy_ready=False sector_rank=17 price=16.79 support=16.63 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=42.76 liquidity=49698956.0 spike=1.45
- EHDR.CA: score=23.3 buy_ready=False sector_rank=12 price=2.96 support=2.71 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=58.62 liquidity=27063748.0 spike=0.63
- EKHO.CA: score=7.16 buy_ready=False sector_rank=13 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=12.82 buy_ready=False sector_rank=10 price=2.07 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=27.78 liquidity=138492128.0 spike=2.21
- ELKA.CA: score=19.3 buy_ready=False sector_rank=12 price=1.72 support=1.69 resistance=2.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=46.15 liquidity=39018580.0 spike=0.57
- ELNA.CA: score=3.43 buy_ready=False sector_rank=12 price=36.45 support=36.1 resistance=39.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=30.18 liquidity=1055775.38 spike=2.04
- ELSH.CA: score=11.3 buy_ready=False sector_rank=12 price=13.22 support=13.14 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=24.49 liquidity=41122292.0 spike=0.53
- ELWA.CA: score=15.13 buy_ready=False sector_rank=12 price=1.74 support=1.62 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:13 PM market time freshness=DELAYED_CURRENT RSI=47.5 liquidity=3875918.75 spike=2.48
- EMFD.CA: score=20.26 buy_ready=False sector_rank=17 price=11.81 support=11.08 resistance=12.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=63.58 liquidity=49533952.0 spike=0.82
- ENGC.CA: score=19.3 buy_ready=False sector_rank=12 price=45.53 support=40.11 resistance=54.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=58.78 liquidity=11631949.0 spike=0.41
- EOSB.CA: score=13.3 buy_ready=False sector_rank=12 price=1.55 support=1.53 resistance=1.62 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=266.6 spike=0.01
- EPCO.CA: score=19.3 buy_ready=False sector_rank=12 price=11.32 support=10.32 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=52.75 liquidity=16641701.0 spike=0.67
- EPPK.CA: score=1.79 buy_ready=False sector_rank=12 price=12.94 support=12.62 resistance=15.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:13 PM market time freshness=DELAYED_CURRENT RSI=23.4 liquidity=492237.19 spike=0.57
- ETEL.CA: score=23.14 buy_ready=False sector_rank=14 price=114.63 support=102.5 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=52.91 liquidity=106013960.0 spike=0.75
- ETRS.CA: score=23.3 buy_ready=False sector_rank=12 price=10.94 support=10.21 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=58.79 liquidity=20749752.0 spike=0.66
- EXPA.CA: score=21.04 buy_ready=False sector_rank=5 price=20.29 support=19.6 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=50.16 liquidity=68896832.0 spike=1.82
- FAIT.CA: score=22.47 buy_ready=False sector_rank=5 price=42.44 support=36.1 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=72.89 liquidity=8928466.0 spike=2.07
- FAITA.CA: score=13.4 buy_ready=False sector_rank=5 price=0.99 support=0.96 resistance=1.0 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=57.75 liquidity=4570.83 spike=0.12
- FERC.CA: score=18.4 buy_ready=False sector_rank=11 price=77.0 support=75.01 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=51.99 liquidity=15609411.0 spike=0.67
- FWRY.CA: score=23.4 buy_ready=False sector_rank=9 price=19.2 support=18.69 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=51.28 liquidity=85373920.0 spike=0.71
- GBCO.CA: score=12.4 buy_ready=False sector_rank=21 price=29.36 support=29.31 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=44.83 liquidity=40952604.0 spike=0.82
- GDWA.CA: score=10.3 buy_ready=False sector_rank=12 price=0.79 support=0.78 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=33.87 liquidity=38169936.0 spike=0.36
- GGCC.CA: score=19.3 buy_ready=False sector_rank=12 price=0.93 support=0.81 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=55.65 liquidity=35960384.0 spike=0.71
- GIHD.CA: score=19.3 buy_ready=False sector_rank=12 price=60.7 support=56.51 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=30265624.0 spike=0.73
- GMCI.CA: score=1.37 buy_ready=False sector_rank=12 price=1.91 support=1.88 resistance=2.1 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=17.39 liquidity=71053.91 spike=0.14
- GRCA.CA: score=28.3 buy_ready=False sector_rank=12 price=61.12 support=54.7 resistance=66.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=55.3 liquidity=137979168.0 spike=5.19
- GSSC.CA: score=20.63 buy_ready=False sector_rank=12 price=283.06 support=264.0 resistance=301.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=48.98 liquidity=9333206.0 spike=0.49
- GTWL.CA: score=20.4 buy_ready=False sector_rank=12 price=194.73 support=85.0 resistance=219.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=82.44 liquidity=384987776.0 spike=2.05
- HDBK.CA: score=14.4 buy_ready=False sector_rank=5 price=92.42 support=80.8 resistance=93.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=76.45 liquidity=23612398.0 spike=0.56
- HELI.CA: score=13.48 buy_ready=False sector_rank=17 price=7.65 support=7.5 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=21.26 liquidity=183334048.0 spike=1.11
- HRHO.CA: score=13.54 buy_ready=False sector_rank=19 price=26.25 support=25.95 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=46.92 liquidity=49294152.0 spike=0.5
- ICID.CA: score=22.52 buy_ready=False sector_rank=12 price=16.69 support=7.85 resistance=16.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=98.22 liquidity=47295772.0 spike=2.11
- IDRE.CA: score=15.33 buy_ready=False sector_rank=12 price=51.92 support=46.04 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=60.43 liquidity=6029777.5 spike=0.21
- IFAP.CA: score=19.4 buy_ready=False sector_rank=8 price=20.55 support=19.0 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=10236515.0 spike=0.34
- INFI.CA: score=21.3 buy_ready=False sector_rank=12 price=157.68 support=104.0 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=72.54 liquidity=37430468.0 spike=0.61
- IRON.CA: score=18.28 buy_ready=False sector_rank=11 price=31.76 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=56.8 liquidity=8880431.0 spike=0.82
- ISMA.CA: score=20.3 buy_ready=False sector_rank=12 price=36.55 support=28.11 resistance=36.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=89.06 liquidity=20131696.0 spike=0.68
- ISMQ.CA: score=19.4 buy_ready=False sector_rank=11 price=9.16 support=8.96 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=21482426.0 spike=0.38
- ISPH.CA: score=21.4 buy_ready=False sector_rank=4 price=13.2 support=11.3 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=61.93 liquidity=73346592.0 spike=0.39
- JUFO.CA: score=13.32 buy_ready=False sector_rank=16 price=26.71 support=22.78 resistance=29.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=83.06 liquidity=15056212.0 spike=0.25
- KABO.CA: score=25.98 buy_ready=False sector_rank=1 price=9.0 support=7.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=69.69 liquidity=76191104.0 spike=1.79
- KWIN.CA: score=27.84 buy_ready=False sector_rank=12 price=102.28 support=84.08 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=54.52 liquidity=191850608.0 spike=3.27
- KZPC.CA: score=25.3 buy_ready=False sector_rank=12 price=14.51 support=8.42 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=96.9 liquidity=310351552.0 spike=7.92
- LCSW.CA: score=19.4 buy_ready=False sector_rank=6 price=34.23 support=30.2 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=45.34 liquidity=17509716.0 spike=0.4
- LUTS.CA: score=23.3 buy_ready=False sector_rank=12 price=1.73 support=0.54 resistance=1.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=95.42 liquidity=637980416.0 spike=4.39
- MAAL.CA: score=11.97 buy_ready=False sector_rank=12 price=8.69 support=8.32 resistance=9.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=42.59 liquidity=2674990.25 spike=0.21
- MASR.CA: score=16.3 buy_ready=False sector_rank=12 price=7.67 support=7.45 resistance=8.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=35.42 liquidity=34362984.0 spike=0.5
- MBSC.CA: score=18.4 buy_ready=False sector_rank=6 price=373.25 support=240.02 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=83.28 liquidity=48500632.0 spike=0.61
- MCQE.CA: score=21.4 buy_ready=False sector_rank=6 price=218.22 support=178.0 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=65.47 liquidity=31338448.0 spike=0.59
- MCRO.CA: score=19.3 buy_ready=False sector_rank=12 price=1.51 support=1.44 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=52.27 liquidity=99718320.0 spike=0.56
- MENA.CA: score=10.93 buy_ready=False sector_rank=17 price=6.94 support=6.82 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=47.27 liquidity=5677909.0 spike=0.92
- MEPA.CA: score=19.3 buy_ready=False sector_rank=12 price=1.82 support=1.78 resistance=2.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=12810056.0 spike=0.21
- MFPC.CA: score=23.4 buy_ready=False sector_rank=11 price=39.12 support=35.37 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=63.91 liquidity=62721472.0 spike=0.75
- MFSC.CA: score=6.55 buy_ready=False sector_rank=12 price=49.01 support=46.02 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=26.1 liquidity=2254405.0 spike=0.2
- MHOT.CA: score=12.16 buy_ready=False sector_rank=15 price=18.26 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=61.01 liquidity=3486668.75 spike=0.2
- MICH.CA: score=22.84 buy_ready=False sector_rank=12 price=50.0 support=39.01 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=70.61 liquidity=74307256.0 spike=1.77
- MILS.CA: score=24.06 buy_ready=False sector_rank=12 price=225.13 support=165.55 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=57.01 liquidity=122580904.0 spike=1.38
- MIPH.CA: score=17.04 buy_ready=False sector_rank=4 price=790.19 support=722.7 resistance=828.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=54.24 liquidity=5119201.0 spike=1.26
- MOED.CA: score=25.3 buy_ready=False sector_rank=12 price=0.83 support=0.65 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=92.27 liquidity=324859456.0 spike=4.37
- MOIL.CA: score=9.47 buy_ready=False sector_rank=13 price=0.66 support=0.58 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:13 PM market time freshness=DELAYED_CURRENT RSI=40.7 liquidity=316148.41 spike=0.52
- MOIN.CA: score=21.3 buy_ready=False sector_rank=12 price=34.74 support=23.11 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=70.36 liquidity=19549922.0 spike=0.64
- MOSC.CA: score=17.05 buy_ready=False sector_rank=12 price=330.04 support=282.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=77.74 liquidity=8756172.0 spike=0.61
- MPCI.CA: score=21.3 buy_ready=False sector_rank=12 price=375.63 support=278.02 resistance=460.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=70.23 liquidity=95437416.0 spike=0.59
- MPCO.CA: score=22.0 buy_ready=False sector_rank=8 price=2.22 support=1.83 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=67.61 liquidity=153759728.0 spike=1.3
- MPRC.CA: score=19.46 buy_ready=False sector_rank=12 price=42.88 support=39.5 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=42.49 liquidity=29924484.0 spike=1.08
- MTIE.CA: score=12.4 buy_ready=False sector_rank=21 price=8.46 support=8.25 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=36.65 liquidity=25944740.0 spike=0.48
- NAHO.CA: score=9.6 buy_ready=False sector_rank=12 price=0.15 support=0.1 resistance=0.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 12:59 PM market time freshness=DELAYED_CURRENT RSI=92.16 liquidity=139586.62 spike=1.58
- NCCW.CA: score=16.3 buy_ready=False sector_rank=12 price=5.8 support=5.59 resistance=7.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=45.65 liquidity=25126916.0 spike=0.77
- NEDA.CA: score=13.27 buy_ready=False sector_rank=12 price=2.76 support=2.7 resistance=2.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:08 PM market time freshness=DELAYED_CURRENT RSI=50.94 liquidity=1537765.25 spike=1.72
- NHPS.CA: score=21.3 buy_ready=False sector_rank=12 price=88.79 support=82.25 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=61.02 liquidity=39904128.0 spike=0.89
- NINH.CA: score=14.3 buy_ready=False sector_rank=12 price=21.71 support=21.22 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=21.27 liquidity=16135633.0 spike=0.44
- NIPH.CA: score=21.4 buy_ready=False sector_rank=4 price=333.91 support=209.0 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=63.99 liquidity=222778992.0 spike=0.74
- OBRI.CA: score=17.3 buy_ready=False sector_rank=12 price=32.33 support=31.61 resistance=35.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=51.34 liquidity=16287106.0 spike=0.47
- OCDI.CA: score=20.26 buy_ready=False sector_rank=17 price=32.74 support=26.6 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=63.99 liquidity=83954776.0 spike=0.63
- OCPH.CA: score=14.45 buy_ready=False sector_rank=12 price=248.3 support=225.0 resistance=488.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=9151210.0 spike=0.36
- ODIN.CA: score=23.3 buy_ready=False sector_rank=12 price=3.19 support=2.54 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=58.12 liquidity=34128244.0 spike=0.83
- OFH.CA: score=20.3 buy_ready=False sector_rank=12 price=0.91 support=0.69 resistance=0.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=86.77 liquidity=59974580.0 spike=0.78
- OIH.CA: score=20.4 buy_ready=False sector_rank=7 price=1.88 support=1.43 resistance=1.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=88.68 liquidity=110361496.0 spike=0.82
- OLFI.CA: score=14.06 buy_ready=False sector_rank=16 price=23.98 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=55.84 liquidity=5740719.0 spike=0.09
- ORAS.CA: score=4.6 buy_ready=False sector_rank=18 price=757.19 support=740.0 resistance=760.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=125781992.0 spike=1.0
- ORHD.CA: score=18.26 buy_ready=False sector_rank=17 price=40.99 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=61.0 liquidity=152962832.0 spike=0.96
- ORWE.CA: score=22.4 buy_ready=False sector_rank=1 price=25.26 support=22.55 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=72.2 liquidity=15747608.0 spike=0.21
- PHAR.CA: score=21.4 buy_ready=False sector_rank=4 price=130.35 support=90.01 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=53.49 liquidity=241171152.0 spike=0.55
- PHDC.CA: score=20.26 buy_ready=False sector_rank=17 price=15.13 support=14.32 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=64.14 liquidity=138087504.0 spike=0.57
- PHTV.CA: score=10.0 buy_ready=False sector_rank=12 price=375.0 support=310.0 resistance=447.99 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=65.28 liquidity=704250.0 spike=0.29
- POUL.CA: score=15.32 buy_ready=False sector_rank=16 price=37.33 support=36.5 resistance=40.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=45.82 liquidity=10261873.0 spike=0.39
- PRCL.CA: score=11.4 buy_ready=False sector_rank=6 price=32.5 support=32.0 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=33.61 liquidity=21086086.0 spike=0.67
- PRDC.CA: score=18.26 buy_ready=False sector_rank=17 price=9.05 support=8.7 resistance=9.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=37.64 liquidity=63977936.0 spike=0.88
- PRMH.CA: score=14.53 buy_ready=False sector_rank=12 price=2.36 support=2.36 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=8235302.5 spike=0.68
- RACC.CA: score=16.34 buy_ready=False sector_rank=12 price=10.03 support=9.8 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=44.55 liquidity=20242782.0 spike=1.02
- RAKT.CA: score=1.1 buy_ready=False sector_rank=12 price=22.25 support=21.65 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:12 PM market time freshness=DELAYED_CURRENT RSI=22.55 liquidity=367054.94 spike=1.22
- RAYA.CA: score=8.26 buy_ready=False sector_rank=20 price=7.0 support=6.95 resistance=7.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=19.32 liquidity=28215234.0 spike=0.33
- RMDA.CA: score=21.4 buy_ready=False sector_rank=4 price=6.12 support=4.98 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=60.92 liquidity=33235898.0 spike=0.28
- ROTO.CA: score=19.3 buy_ready=False sector_rank=12 price=46.33 support=41.85 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=55.44 liquidity=15071082.0 spike=0.62
- RREI.CA: score=19.3 buy_ready=False sector_rank=12 price=4.46 support=3.76 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=45.4 liquidity=29716220.0 spike=0.44
- RTVC.CA: score=24.04 buy_ready=False sector_rank=12 price=4.2 support=3.73 resistance=4.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=81.82 liquidity=22274982.0 spike=2.87
- RUBX.CA: score=17.83 buy_ready=False sector_rank=12 price=12.44 support=12.02 resistance=13.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=50.29 liquidity=8531778.0 spike=0.42
- SAUD.CA: score=21.54 buy_ready=False sector_rank=5 price=24.5 support=21.4 resistance=24.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=88.45 liquidity=35751016.0 spike=1.57
- SCEM.CA: score=21.4 buy_ready=False sector_rank=6 price=99.0 support=76.75 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=70.54 liquidity=149273952.0 spike=0.71
- SCFM.CA: score=21.3 buy_ready=False sector_rank=12 price=283.01 support=270.51 resistance=319.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=43.62 liquidity=17580182.0 spike=0.63
- SCTS.CA: score=18.09 buy_ready=False sector_rank=3 price=620.16 support=603.13 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=61.7 liquidity=3686153.75 spike=0.36
- SDTI.CA: score=19.17 buy_ready=False sector_rank=12 price=68.08 support=50.3 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=60.97 liquidity=7870118.0 spike=0.25
- SEIG.CA: score=10.48 buy_ready=False sector_rank=12 price=263.41 support=242.1 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=55.69 liquidity=1185175.63 spike=0.11
- SIPC.CA: score=21.3 buy_ready=False sector_rank=12 price=4.73 support=3.76 resistance=5.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=53.04 liquidity=14292390.0 spike=0.23
- SKPC.CA: score=22.3 buy_ready=False sector_rank=11 price=17.73 support=15.61 resistance=18.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=84.15 liquidity=133216192.0 spike=1.95
- SMFR.CA: score=19.01 buy_ready=False sector_rank=12 price=261.9 support=228.88 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=64.94 liquidity=7714296.0 spike=0.28
- SNFC.CA: score=17.4 buy_ready=False sector_rank=12 price=11.0 support=10.6 resistance=11.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=46.62 liquidity=9102761.0 spike=0.76
- SPIN.CA: score=24.4 buy_ready=False sector_rank=1 price=18.31 support=14.91 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=65.62 liquidity=11838994.0 spike=0.25
- SPMD.CA: score=19.3 buy_ready=False sector_rank=12 price=0.46 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=42.47 liquidity=10657907.0 spike=0.35
- SUGR.CA: score=20.32 buy_ready=False sector_rank=16 price=50.67 support=46.47 resistance=53.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=72.94 liquidity=14489821.0 spike=0.67
- SVCE.CA: score=21.3 buy_ready=False sector_rank=12 price=10.5 support=9.06 resistance=12.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=65.56 liquidity=29282988.0 spike=0.29
- SWDY.CA: score=21.4 buy_ready=False sector_rank=10 price=116.51 support=91.8 resistance=133.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=68.64 liquidity=76819720.0 spike=0.84
- TALM.CA: score=24.4 buy_ready=False sector_rank=3 price=19.4 support=15.7 resistance=20.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=61.1 liquidity=30658148.0 spike=0.7
- TMGH.CA: score=15.26 buy_ready=False sector_rank=17 price=96.54 support=95.2 resistance=101.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=45.01 liquidity=211126000.0 spike=0.74
- TRTO.CA: score=15.3 buy_ready=False sector_rank=12 price=0.05 support=0.03 resistance=0.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 11:15 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=7434.21 spike=0.73
- UEFM.CA: score=10.06 buy_ready=False sector_rank=12 price=538.85 support=531.0 resistance=594.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:12 PM market time freshness=DELAYED_CURRENT RSI=46.53 liquidity=766820.81 spike=0.14
- UEGC.CA: score=14.3 buy_ready=False sector_rank=12 price=2.1 support=1.95 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=34.45 liquidity=34184772.0 spike=0.9
- UNIP.CA: score=16.94 buy_ready=False sector_rank=12 price=0.36 support=0.35 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=35.79 liquidity=50973416.0 spike=1.32
- UNIT.CA: score=12.84 buy_ready=False sector_rank=17 price=18.81 support=17.32 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=55.67 liquidity=2588434.75 spike=0.2
- WCDF.CA: score=9.68 buy_ready=False sector_rank=12 price=639.6 support=555.55 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:10 PM market time freshness=DELAYED_CURRENT RSI=76.66 liquidity=1382065.13 spike=0.28
- WKOL.CA: score=23.3 buy_ready=False sector_rank=12 price=333.95 support=310.0 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=46.35 liquidity=11248994.0 spike=0.33
- ZEOT.CA: score=21.23 buy_ready=False sector_rank=12 price=13.81 support=11.56 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=64.74 liquidity=7934828.0 spike=0.3
- ZMID.CA: score=21.26 buy_ready=False sector_rank=17 price=7.85 support=7.06 resistance=8.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=71.63 liquidity=365721536.0 spike=1.5

## Backtesting Lite
- AXPH.CA: 180d return=77.42%, max drawdown=-8.16%, MA20>MA50 days last20=20, as_of=2026-08-19T21:00:00+00:00
- COPR.CA: 180d return=-2.78%, max drawdown=-52.45%, MA20>MA50 days last20=20, as_of=2026-08-19T21:00:00+00:00
- GRCA.CA: 180d return=111.6%, max drawdown=-18.71%, MA20>MA50 days last20=17, as_of=2026-08-19T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- AXPH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria Co. For Pharmaceuticals & Chemical Industries summary=Alexandria Pharmaceuticals’ profits retreat 25% in 8M-21/22; Alexandria Pharmaceuticals profits fall 22.5% in 7M-21/22; Alexandria Pharmaceuticals posts 27% lower profits in 6M
  - Alexandria Pharmaceuticals’ profits retreat 25% in 8M-21/22: https://english.mubasher.info/news/3938982/Alexandria-Pharmaceuticals-profits-retreat-25-in-8M-21-22/
  - Alexandria Pharmaceuticals profits fall 22.5% in 7M-21/22: https://english.mubasher.info/news/3923195/Alexandria-Pharmaceuticals-profits-fall-22-5-in-7M-21-22/
  - Alexandria Pharmaceuticals posts 27% lower profits in 6M: https://english.mubasher.info/news/3906523/Alexandria-Pharmaceuticals-posts-27-lower-profits-in-6M/
- COPR.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Copper for Commercial Investment & Real Estate Development summary=Copper for Commercial Investment swings to EGP 7m net losses in 9M-25; NRPD’s EGM approves capital cut, increase; Two shareholders sell entire stakes in NRPD
  - Copper for Commercial Investment swings to EGP 7m net losses in 9M-25: https://english.mubasher.info/news/4530417/Copper-for-Commercial-Investment-swings-to-EGP-7m-net-losses-in-9M-25/
  - NRPD’s EGM approves capital cut, increase: https://english.mubasher.info/news/4042300/NRPD-s-EGM-approves-capital-cut-increase/
  - Two shareholders sell entire stakes in NRPD: https://english.mubasher.info/news/4006432/Two-shareholders-sell-entire-stakes-in-NRPD/
- GRCA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Grand Capital for Financial Investments summary=Grand Investment Capital logs lower consolidated net profits in H1-25/26; Grand Investment Capital sees EGP 8m block-trading deal; Grand Investment Capital’s profit hikes 131% in 12M
  - Grand Investment Capital logs lower consolidated net profits in H1-25/26: https://english.mubasher.info/news/4527603/Grand-Investment-Capital-logs-lower-consolidated-net-profits-in-H1-25-26/
  - Grand Investment Capital sees EGP 8m block-trading deal: https://english.mubasher.info/news/3765574/Grand-Investment-Capital-sees-EGP-8m-block-trading-deal/
  - Grand Investment Capital’s profit hikes 131% in 12M: https://english.mubasher.info/news/3481392/Grand-Investment-Capital-s-profit-hikes-131-in-12M/
- KWIN.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Kahera El Watania Investment summary=ADIB Egypt&#39;s Cairo National unveils equity reduction transaction worth over EGP 3m; El Kahera El Watania to buy stake in Assiut for Agricultural Development; Tycoon Holding acquires 85% of Alexandria National Investment
  - ADIB Egypt&#39;s Cairo National unveils equity reduction transaction worth over EGP 3m: https://english.mubasher.info/news/4546852/ADIB-Egypt-s-Cairo-National-unveils-equity-reduction-transaction-worth-over-EGP-3m/
  - El Kahera El Watania to buy stake in Assiut for Agricultural Development: https://english.mubasher.info/news/4009433/El-Kahera-El-Watania-to-buy-stake-in-Assiut-for-Agricultural-Development/
  - Tycoon Holding acquires 85% of Alexandria National Investment: https://english.mubasher.info/news/3844623/Tycoon-Holding-acquires-85-of-Alexandria-National-Investment/
- KABO.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Nasr Clothing and Textiles summary=KABO posts EGP 17m in Q1-25/26 unaudited consolidated net profits; KABO sells over 1.9m shares in Spinalex for EGP 20m; KABO unveils international agreements, expansion plan including export lines
  - KABO posts EGP 17m in Q1-25/26 unaudited consolidated net profits: https://english.mubasher.info/news/4600162/KABO-posts-EGP-17m-in-Q1-25-26-unaudited-consolidated-net-profits/
  - KABO sells over 1.9m shares in Spinalex for EGP 20m: https://english.mubasher.info/news/4543747/KABO-sells-over-1-9m-shares-in-Spinalex-for-EGP-20m/
  - KABO unveils international agreements, expansion plan including export lines: https://english.mubasher.info/news/4533185/KABO-unveils-international-agreements-expansion-plan-including-export-lines/
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- CEFM.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Middle Egypt Flour Mills summary=Middle Egypt Flour Mills posts lower net profits at EGP 77m in 9M-25/26; Middle Egypt Flour Mills shareholders approve EGP 3.25/shr dividend; Middle Egypt Mills reports 23% profit drop in FY19/20
  - Middle Egypt Flour Mills posts lower net profits at EGP 77m in 9M-25/26: https://english.mubasher.info/news/4601809/Middle-Egypt-Flour-Mills-posts-lower-net-profits-at-EGP-77m-in-9M-25-26/
  - Middle Egypt Flour Mills shareholders approve EGP 3.25/shr dividend: https://english.mubasher.info/news/3870911/Middle-Egypt-Flour-Mills-shareholders-approve-EGP-3-25-shr-dividend/
  - Middle Egypt Mills reports 23% profit drop in FY19/20: https://english.mubasher.info/news/3703590/Middle-Egypt-Mills-reports-23-profit-drop-in-FY19-20/

## Warnings
- Evidence for AXPH.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for COPR.CA matches the company but no source/report date was detected.
- Evidence for GRCA.CA matches the company but no source/report date was detected.
- Evidence for KWIN.CA matches the company but no source/report date was detected.
- Evidence for KABO.CA matches the company but no source/report date was detected.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for CEFM.CA matches the company but no source/report date was detected.
