# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-09-22T11:33:56.113090+00:00
Generated Cairo: 2026-09-22 14:33
Run timing: target 09:15 Cairo | generated Cairo 2026-09-22 14:33 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-09-22 14:30

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 177/186
- Top sector: Investment Holding

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, September 22
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 21.05% / above MA50 57.89%
- EGX70 regime: BEARISH / above MA20 30.0% / above MA50 55.0%
- Sector breadth: 38.1%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=919093312.0 spike=1.48 score=12.36
- CCAP.CA: liquidity=663280704.0 spike=0.78 score=21.4
- ETEL.CA: liquidity=438792160.0 spike=1.73 score=23.86
- NIPH.CA: liquidity=413324000.0 spike=2.75 score=7.49
- ORHD.CA: liquidity=303930464.0 spike=2.24 score=19.41

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are both bearish with weak breadth, putting the scanner in defensive mode; it flags a few stocks with accumulation spikes and bullish watch outlooks but keeps them on HOLD due to the overall risk‑off regime.
- High‑rank tickets (e.g., GBCO.CA, ETEL.CA) show liquidity accumulation spikes and bullish watch scores, suggesting short‑term buying interest.
- Most of these tickets sit near resistance with support far below, so any upside is likely limited to 1‑3 days before hitting resistance.
- Sector strength is concentrated in Investment Holding, Telecommunications and Agriculture, but the broader market remains below MA20, keeping risk mode defensive.
- Given the bearish EGX30/EGX70 trend and low confidence, the scanner treats these signals as uncertain and maintains HOLD positions.

## Top Liquidity Spikes
- NEDA.CA: spike=11.88 liquidity=7372879.0 outlook=NEUTRAL score=42.6 buy_ready=False
- EGTS.CA: spike=4.82 liquidity=108399576.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- NIPH.CA: spike=2.75 liquidity=413324000.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SEIG.CA: spike=2.44 liquidity=4200065.0 outlook=WEAK_OR_RISKY score=28.6 buy_ready=False
- GBCO.CA: spike=2.38 liquidity=166097776.0 outlook=BULLISH_WATCH score=78.68 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=13.12 5d=4.09% 20d=21.55% aboveMA50=100.0%
- #2 Telecommunications: score=10.82 5d=2.98% 20d=9.42% aboveMA50=100.0%
- #3 Agriculture & Food Production: score=9.78 5d=5.68% 20d=12.05% aboveMA50=100.0%
- #4 Transportation & Logistics: score=7.84 5d=5.21% 20d=1.09% aboveMA50=100.0%
- #5 Energy & Petrochemicals: score=7.24 5d=4.48% 20d=3.4% aboveMA50=66.67%
- #6 Banking & Financials: score=6.72 5d=2.82% 20d=4.7% aboveMA50=80.0%
- #7 Automotive & Distribution: score=5.68 5d=2.42% 20d=-1.41% aboveMA50=50.0%
- #8 Basic Resources & Chemicals: score=4.61 5d=1.92% 20d=2.73% aboveMA50=60.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ETEL.CA: BULLISH_WATCH score=83 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support
- DTPP.CA: BULLISH_WATCH score=82.6 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- OIH.CA: BULLISH_WATCH score=82 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- GBCO.CA: BULLISH_WATCH score=78.68 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- CPCI.CA: BULLISH_WATCH score=78.6 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- IFAP.CA: BULLISH_WATCH score=77.78 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20
- SAUD.CA: BULLISH_WATCH score=75.72 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended
- EXPA.CA: BULLISH_WATCH score=73.72 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended
- AMOC.CA: BULLISH_WATCH score=73.24 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; far above support
- BINV.CA: BULLISH_WATCH score=73 liquidity=TRADEABLE sector=LEADING risk=overheated RSI

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- CICH.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=14.24 buy_ready=False sector_rank=16 price=290.0 support=288.01 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.82 liquidity=14376219.0 spike=0.56
- ABUK.CA: score=22.84 buy_ready=False sector_rank=8 price=93.73 support=75.01 resistance=96.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=59.62 liquidity=93342360.0 spike=0.51
- ACAMD.CA: score=16.24 buy_ready=False sector_rank=16 price=2.03 support=1.99 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=16873184.0 spike=0.3
- ACGC.CA: score=14.01 buy_ready=False sector_rank=12 price=14.09 support=13.55 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.89 liquidity=6003334.5 spike=0.18
- ADCI.CA: score=5.29 buy_ready=False sector_rank=16 price=283.19 support=267.66 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=20.86 liquidity=3047506.75 spike=0.62
- ADIB.CA: score=19.4 buy_ready=False sector_rank=6 price=52.48 support=50.51 resistance=55.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.3 liquidity=43611476.0 spike=0.56
- ADPC.CA: score=17.64 buy_ready=False sector_rank=16 price=3.98 support=3.81 resistance=4.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.28 liquidity=30611842.0 spike=1.7
- AFDI.CA: score=4.69 buy_ready=False sector_rank=16 price=52.77 support=51.6 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=32.99 liquidity=5447219.0 spike=0.22
- AFMC.CA: score=11.14 buy_ready=False sector_rank=16 price=159.58 support=153.0 resistance=239.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.79 liquidity=6903232.5 spike=0.11
- AJWA.CA: score=9.88 buy_ready=False sector_rank=16 price=180.0 support=175.15 resistance=199.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=47.21 liquidity=5636622.0 spike=0.13
- ALCN.CA: score=23.7 buy_ready=False sector_rank=4 price=34.08 support=30.03 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.47 liquidity=40540500.0 spike=1.15
- ALUM.CA: score=2.15 buy_ready=False sector_rank=16 price=25.5 support=25.0 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=30.52 liquidity=2908886.5 spike=0.21
- AMER.CA: score=13.93 buy_ready=False sector_rank=19 price=5.24 support=4.8 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.37 liquidity=37750800.0 spike=0.68
- AMES.CA: score=8.24 buy_ready=False sector_rank=16 price=51.09 support=48.45 resistance=158.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=9.27 liquidity=77266880.0 spike=0.29
- AMIA.CA: score=12.24 buy_ready=False sector_rank=16 price=18.49 support=17.12 resistance=21.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=33.83 liquidity=23665816.0 spike=0.48
- AMOC.CA: score=21.4 buy_ready=False sector_rank=5 price=13.44 support=10.65 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.3 liquidity=55333548.0 spike=0.31
- APSW.CA: score=-1.31 buy_ready=False sector_rank=16 price=8.22 support=8.2 resistance=8.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=34.38 liquidity=452155.53 spike=0.48
- ARAB.CA: score=8.93 buy_ready=False sector_rank=19 price=0.24 support=0.24 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.61 liquidity=42256524.0 spike=0.41
- ARCC.CA: score=11.48 buy_ready=False sector_rank=21 price=70.52 support=69.0 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=20.43 liquidity=10739420.0 spike=0.27
- AREH.CA: score=7.07 buy_ready=False sector_rank=16 price=1.41 support=1.39 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=2826160.5 spike=0.19
- ASCM.CA: score=4.15 buy_ready=False sector_rank=16 price=59.02 support=58.16 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=31.4 liquidity=4910598.5 spike=0.25
- ASPI.CA: score=14.24 buy_ready=False sector_rank=16 price=0.43 support=0.41 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.41 liquidity=34955064.0 spike=0.56
- ATLC.CA: score=14.18 buy_ready=False sector_rank=10 price=7.01 support=5.35 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=52.63 liquidity=4062990.25 spike=0.14
- ATQA.CA: score=24.84 buy_ready=False sector_rank=8 price=13.11 support=11.0 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=64.31 liquidity=75185376.0 spike=0.68
- AXPH.CA: score=19.37 buy_ready=False sector_rank=16 price=1691.79 support=1501.0 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=36.72 liquidity=9973425.0 spike=1.08
- BINV.CA: score=21.4 buy_ready=False sector_rank=1 price=57.27 support=48.04 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=75.89 liquidity=20803704.0 spike=0.86
- BIOC.CA: score=9.24 buy_ready=False sector_rank=16 price=271.12 support=247.03 resistance=488.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.38 liquidity=54902796.0 spike=0.57
- BTFH.CA: score=16.12 buy_ready=False sector_rank=10 price=2.92 support=2.87 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.34 liquidity=72535160.0 spike=0.89
- CAED.CA: score=3.83 buy_ready=False sector_rank=16 price=124.46 support=122.6 resistance=173.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.49 liquidity=4594526.5 spike=0.2
- CANA.CA: score=20.76 buy_ready=False sector_rank=6 price=47.51 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=70.58 liquidity=7355288.0 spike=0.32
- CCAP.CA: score=21.4 buy_ready=False sector_rank=1 price=7.2 support=5.72 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=663280704.0 spike=0.78
- CCRS.CA: score=13.88 buy_ready=False sector_rank=16 price=2.57 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=48.74 liquidity=7643335.0 spike=0.14
- CEFM.CA: score=8.21 buy_ready=False sector_rank=16 price=143.19 support=135.0 resistance=167.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.55 liquidity=966143.06 spike=0.09
- CERA.CA: score=17.24 buy_ready=False sector_rank=16 price=1.39 support=1.22 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.92 liquidity=74035160.0 spike=0.59
- CFGH.CA: score=7.25 buy_ready=False sector_rank=16 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=7714.89 spike=0.44
- CIEB.CA: score=15.41 buy_ready=False sector_rank=6 price=24.79 support=24.01 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.7 liquidity=6008660.0 spike=0.44
- CIRA.CA: score=19.82 buy_ready=False sector_rank=9 price=40.31 support=32.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=75.87 liquidity=16153941.0 spike=0.4
- CLHO.CA: score=8.99 buy_ready=False sector_rank=18 price=15.83 support=15.4 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=12.13 liquidity=23768852.0 spike=0.32
- CNFN.CA: score=6.03 buy_ready=False sector_rank=10 price=4.51 support=4.46 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.59 liquidity=6916159.0 spike=0.59
- COMI.CA: score=12.36 buy_ready=False sector_rank=6 price=131.85 support=131.11 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.85 liquidity=919093312.0 spike=1.48
- COPR.CA: score=17.12 buy_ready=False sector_rank=16 price=0.49 support=0.46 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.4 liquidity=9879147.0 spike=0.21
- COSG.CA: score=14.24 buy_ready=False sector_rank=16 price=1.78 support=1.78 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=12950432.0 spike=0.38
- CPCI.CA: score=13.99 buy_ready=False sector_rank=16 price=564.43 support=530.0 resistance=584.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=60.45 liquidity=2754758.0 spike=0.83
- CSAG.CA: score=8.01 buy_ready=False sector_rank=4 price=38.39 support=36.5 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=27.53 liquidity=3607392.75 spike=0.23
- DAPH.CA: score=9.24 buy_ready=False sector_rank=16 price=110.54 support=108.11 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=21.49 liquidity=15631300.0 spike=0.27
- DEIN.CA: score=7.24 buy_ready=False sector_rank=16 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=1.62 buy_ready=False sector_rank=15 price=26.47 support=25.56 resistance=29.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.65 liquidity=2305096.5 spike=0.43
- DSCW.CA: score=7.87 buy_ready=False sector_rank=16 price=1.79 support=1.77 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.35 liquidity=9629979.0 spike=0.31
- DTPP.CA: score=20.8 buy_ready=False sector_rank=16 price=336.13 support=294.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.6 liquidity=133247856.0 spike=1.78
- EALR.CA: score=6.87 buy_ready=False sector_rank=16 price=369.73 support=340.0 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=33.51 liquidity=7632856.0 spike=0.53
- EASB.CA: score=10.56 buy_ready=False sector_rank=16 price=7.66 support=7.2 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=55.61 liquidity=3318269.5 spike=0.2
- EAST.CA: score=8.32 buy_ready=False sector_rank=15 price=31.86 support=31.31 resistance=36.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=11.07 liquidity=15433571.0 spike=0.2
- EBSC.CA: score=4.09 buy_ready=False sector_rank=16 price=2.0 support=1.91 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=30.26 liquidity=1846979.13 spike=0.12
- ECAP.CA: score=14.28 buy_ready=False sector_rank=16 price=31.89 support=31.16 resistance=36.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=46.37 liquidity=11379295.0 spike=1.02
- EDFM.CA: score=4.91 buy_ready=False sector_rank=16 price=400.02 support=390.0 resistance=465.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=43.16 liquidity=674084.5 spike=0.37
- EEII.CA: score=4.07 buy_ready=False sector_rank=16 price=2.25 support=2.15 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=33.9 liquidity=5834523.0 spike=0.38
- EFIC.CA: score=14.84 buy_ready=False sector_rank=8 price=184.91 support=183.0 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.33 liquidity=21844728.0 spike=0.06
- EFID.CA: score=17.32 buy_ready=False sector_rank=15 price=30.63 support=29.71 resistance=32.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.36 liquidity=26312544.0 spike=0.4
- EFIH.CA: score=14.17 buy_ready=False sector_rank=17 price=22.93 support=22.16 resistance=24.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.2 liquidity=59914372.0 spike=1.01
- EGAL.CA: score=18.84 buy_ready=False sector_rank=8 price=366.14 support=345.0 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.02 liquidity=28330090.0 spike=0.28
- EGAS.CA: score=12.43 buy_ready=False sector_rank=5 price=56.55 support=55.0 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.42 liquidity=6027463.0 spike=0.51
- EGBE.CA: score=4.48 buy_ready=False sector_rank=6 price=0.52 support=0.49 resistance=0.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=78808.98 spike=0.96
- EGCH.CA: score=18.84 buy_ready=False sector_rank=8 price=13.91 support=13.3 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=49981976.0 spike=0.41
- EGSA.CA: score=10.4 buy_ready=False sector_rank=2 price=9.0 support=8.68 resistance=9.1 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=78.18 liquidity=3654.0 spike=0.59
- EGTS.CA: score=8.93 buy_ready=False sector_rank=19 price=18.71 support=16.85 resistance=18.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=108399576.0 spike=4.82
- EHDR.CA: score=5.92 buy_ready=False sector_rank=16 price=2.65 support=2.65 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.43 liquidity=6681975.0 spike=0.36
- ELEC.CA: score=8.45 buy_ready=False sector_rank=14 price=1.96 support=1.92 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=40802128.0 spike=0.52
- ELKA.CA: score=5.18 buy_ready=False sector_rank=16 price=1.67 support=1.64 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=13.16 liquidity=5936661.5 spike=0.16
- ELNA.CA: score=-1.61 buy_ready=False sector_rank=16 price=35.22 support=33.96 resistance=38.99 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=24.57 liquidity=154827.13 spike=0.42
- ELSH.CA: score=12.5 buy_ready=False sector_rank=16 price=12.71 support=12.55 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.74 liquidity=8256776.0 spike=0.22
- ELWA.CA: score=0.05 buy_ready=False sector_rank=16 price=1.69 support=1.66 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.95 liquidity=814831.5 spike=0.38
- EMFD.CA: score=16.93 buy_ready=False sector_rank=19 price=13.48 support=12.1 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.19 liquidity=36578280.0 spike=0.22
- ENGC.CA: score=14.82 buy_ready=False sector_rank=16 price=41.47 support=41.0 resistance=47.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.72 liquidity=20854276.0 spike=1.29
- EOSB.CA: score=9.72 buy_ready=False sector_rank=16 price=1.57 support=1.53 resistance=1.64 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=76532.79 spike=1.2
- EPCO.CA: score=9.64 buy_ready=False sector_rank=16 price=10.77 support=10.6 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=44.78 liquidity=5396458.5 spike=0.33
- EPPK.CA: score=-5.34 buy_ready=False sector_rank=16 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=23.86 buy_ready=False sector_rank=2 price=138.53 support=112.5 resistance=136.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=85.57 liquidity=438792160.0 spike=1.73
- ETRS.CA: score=9.59 buy_ready=False sector_rank=16 price=10.87 support=10.66 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=35.51 liquidity=2354753.25 spike=0.17
- EXPA.CA: score=23.4 buy_ready=False sector_rank=6 price=21.95 support=19.96 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=64.72 liquidity=35198380.0 spike=0.95
- FAIT.CA: score=10.88 buy_ready=False sector_rank=6 price=47.08 support=41.52 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=67.5 liquidity=1475027.13 spike=0.18
- FAITA.CA: score=6.42 buy_ready=False sector_rank=6 price=0.99 support=0.98 resistance=1.02 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=41.18 liquidity=16085.14 spike=0.33
- FERC.CA: score=11.16 buy_ready=False sector_rank=8 price=78.22 support=77.3 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=4319732.0 spike=0.29
- FWRY.CA: score=14.15 buy_ready=False sector_rank=17 price=18.93 support=18.66 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.24 liquidity=49959056.0 spike=0.36
- GBCO.CA: score=26.03 buy_ready=False sector_rank=7 price=31.12 support=27.51 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=63.86 liquidity=166097776.0 spike=2.38
- GDWA.CA: score=8.24 buy_ready=False sector_rank=16 price=0.75 support=0.75 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=13.22 liquidity=15177702.0 spike=0.35
- GGCC.CA: score=14.24 buy_ready=False sector_rank=16 price=0.81 support=0.83 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=18898264.0 spike=0.57
- GIHD.CA: score=13.39 buy_ready=False sector_rank=16 price=72.44 support=61.61 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.29 liquidity=4149850.75 spike=0.15
- GMCI.CA: score=-1.54 buy_ready=False sector_rank=16 price=1.76 support=1.69 resistance=1.94 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=30.0 liquidity=224906.88 spike=0.47
- GRCA.CA: score=3.74 buy_ready=False sector_rank=16 price=39.53 support=38.7 resistance=85.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=20.93 liquidity=5501025.5 spike=0.09
- GSSC.CA: score=14.47 buy_ready=False sector_rank=16 price=304.9 support=278.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=61.87 liquidity=3227560.0 spike=0.35
- GTWL.CA: score=19.24 buy_ready=False sector_rank=16 price=237.45 support=201.3 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.63 liquidity=88419280.0 spike=0.44
- HDBK.CA: score=23.36 buy_ready=False sector_rank=6 price=118.35 support=90.51 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.79 liquidity=9955415.0 spike=0.16
- HELI.CA: score=20.93 buy_ready=False sector_rank=19 price=8.15 support=7.34 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.92 liquidity=97972648.0 spike=0.57
- HRHO.CA: score=9.9 buy_ready=False sector_rank=10 price=24.58 support=24.83 resistance=26.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.67 liquidity=138881520.0 spike=1.39
- ICID.CA: score=10.01 buy_ready=False sector_rank=16 price=17.1 support=16.2 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.78 liquidity=2770278.25 spike=0.23
- IDRE.CA: score=15.04 buy_ready=False sector_rank=16 price=54.24 support=51.0 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.86 liquidity=5802369.0 spike=0.35
- IFAP.CA: score=16.21 buy_ready=False sector_rank=3 price=20.59 support=19.05 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.05 liquidity=5814113.0 spike=0.25
- INFI.CA: score=5.48 buy_ready=False sector_rank=16 price=126.94 support=123.0 resistance=168.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.11 liquidity=6243660.5 spike=0.22
- IRON.CA: score=2.79 buy_ready=False sector_rank=8 price=27.17 support=26.3 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.29 liquidity=2947739.0 spike=0.21
- ISMA.CA: score=7.93 buy_ready=False sector_rank=16 price=29.46 support=28.05 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.67 liquidity=3688500.25 spike=0.16
- ISMQ.CA: score=10.84 buy_ready=False sector_rank=8 price=8.77 support=8.68 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.39 liquidity=10624104.0 spike=0.41
- ISPH.CA: score=8.99 buy_ready=False sector_rank=18 price=12.19 support=11.9 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.5 liquidity=28594118.0 spike=0.4
- JUFO.CA: score=20.32 buy_ready=False sector_rank=15 price=27.18 support=26.45 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.83 liquidity=13627599.0 spike=0.64
- KABO.CA: score=18.01 buy_ready=False sector_rank=12 price=9.27 support=8.9 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.27 liquidity=18273420.0 spike=0.43
- KWIN.CA: score=3.03 buy_ready=False sector_rank=16 price=86.14 support=82.5 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=18.91 liquidity=3786462.25 spike=0.07
- KZPC.CA: score=12.42 buy_ready=False sector_rank=16 price=13.69 support=12.6 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.9 liquidity=3184189.5 spike=0.09
- LCSW.CA: score=8.48 buy_ready=False sector_rank=21 price=33.33 support=31.61 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=25.24 liquidity=18163872.0 spike=0.75
- LUTS.CA: score=17.24 buy_ready=False sector_rank=16 price=0.89 support=0.83 resistance=1.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.2 liquidity=32554144.0 spike=0.17
- MAAL.CA: score=5.64 buy_ready=False sector_rank=16 price=9.14 support=8.7 resistance=9.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20004538.0 spike=1.7
- MASR.CA: score=14.24 buy_ready=False sector_rank=16 price=7.69 support=7.49 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.56 liquidity=40457740.0 spike=0.41
- MBSC.CA: score=11.48 buy_ready=False sector_rank=21 price=338.63 support=340.66 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=20.64 liquidity=20695450.0 spike=0.42
- MCQE.CA: score=8.48 buy_ready=False sector_rank=21 price=206.96 support=207.1 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=23.89 liquidity=23177502.0 spike=0.75
- MCRO.CA: score=19.4 buy_ready=False sector_rank=16 price=1.67 support=1.48 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=132089544.0 spike=1.08
- MENA.CA: score=4.5 buy_ready=False sector_rank=19 price=6.72 support=6.58 resistance=7.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=38.32 liquidity=565802.94 spike=0.31
- MEPA.CA: score=15.96 buy_ready=False sector_rank=16 price=1.91 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.91 liquidity=8723193.0 spike=0.22
- MFPC.CA: score=17.84 buy_ready=False sector_rank=8 price=48.82 support=39.02 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=76.27 liquidity=68908504.0 spike=0.38
- MFSC.CA: score=8.17 buy_ready=False sector_rank=16 price=49.64 support=48.5 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=44.06 liquidity=929903.63 spike=0.19
- MHOT.CA: score=10.12 buy_ready=False sector_rank=11 price=17.9 support=16.61 resistance=19.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=27.1 liquidity=8102555.0 spike=0.84
- MICH.CA: score=17.24 buy_ready=False sector_rank=16 price=47.53 support=47.51 resistance=53.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=10163868.0 spike=0.63
- MILS.CA: score=11.52 buy_ready=False sector_rank=16 price=191.26 support=180.01 resistance=232.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=35.45 liquidity=7278509.5 spike=0.27
- MIPH.CA: score=6.67 buy_ready=False sector_rank=18 price=879.95 support=861.0 resistance=941.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18962834.0 spike=2.34
- MOED.CA: score=8.24 buy_ready=False sector_rank=16 price=0.72 support=0.7 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=22.78 liquidity=18265560.0 spike=0.24
- MOIL.CA: score=14.13 buy_ready=False sector_rank=5 price=0.7 support=0.66 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=58.57 liquidity=266822.66 spike=1.23
- MOIN.CA: score=14.19 buy_ready=False sector_rank=16 price=35.69 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.45 liquidity=6945982.5 spike=0.23
- MOSC.CA: score=0.3 buy_ready=False sector_rank=16 price=299.38 support=290.0 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.83 liquidity=1061057.63 spike=0.15
- MPCI.CA: score=12.58 buy_ready=False sector_rank=16 price=393.07 support=371.11 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=16.95 liquidity=167424768.0 spike=1.17
- MPCO.CA: score=22.4 buy_ready=False sector_rank=3 price=2.79 support=2.07 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=72.25 liquidity=91890944.0 spike=0.54
- MPRC.CA: score=5.31 buy_ready=False sector_rank=16 price=38.29 support=37.65 resistance=46.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.87 liquidity=6068764.0 spike=0.15
- MTIE.CA: score=8.97 buy_ready=False sector_rank=7 price=8.19 support=8.02 resistance=8.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=21.74 liquidity=8700944.0 spike=0.27
- NAHO.CA: score=-4.59 buy_ready=False sector_rank=16 price=0.13 support=0.13 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=86983.35 spike=1.54
- NCCW.CA: score=21.24 buy_ready=False sector_rank=16 price=7.21 support=5.77 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=63.95 liquidity=52500532.0 spike=0.8
- NEDA.CA: score=16.61 buy_ready=False sector_rank=16 price=2.75 support=2.7 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=7372879.0 spike=11.88
- NHPS.CA: score=1.91 buy_ready=False sector_rank=16 price=73.25 support=72.52 resistance=98.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=9.18 liquidity=2667781.0 spike=0.15
- NINH.CA: score=6.91 buy_ready=False sector_rank=16 price=20.41 support=20.3 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.64 liquidity=7674225.5 spike=0.25
- NIPH.CA: score=7.49 buy_ready=False sector_rank=18 price=340.87 support=310.01 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=413324000.0 spike=2.75
- OBRI.CA: score=4.59 buy_ready=False sector_rank=16 price=30.1 support=29.51 resistance=34.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=16.11 liquidity=6347114.5 spike=0.41
- OCDI.CA: score=13.93 buy_ready=False sector_rank=19 price=29.19 support=29.25 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.29 liquidity=38049000.0 spike=0.46
- OCPH.CA: score=5.99 buy_ready=False sector_rank=16 price=240.64 support=210.0 resistance=277.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=34.17 liquidity=5745128.0 spike=0.87
- ODIN.CA: score=9.36 buy_ready=False sector_rank=16 price=2.82 support=2.55 resistance=3.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:15 PM market time freshness=DELAYED_CURRENT RSI=33.8 liquidity=23467814.0 spike=1.06
- OFH.CA: score=6.1 buy_ready=False sector_rank=16 price=1.09 support=1.04 resistance=1.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=241953088.0 spike=1.93
- OIH.CA: score=22.4 buy_ready=False sector_rank=1 price=2.13 support=1.91 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=68.97 liquidity=55186708.0 spike=0.46
- OLFI.CA: score=10.08 buy_ready=False sector_rank=15 price=22.71 support=22.07 resistance=23.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.22 liquidity=5765774.5 spike=0.32
- ORAS.CA: score=4.6 buy_ready=False sector_rank=13 price=841.52 support=836.12 resistance=848.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=98741448.0 spike=1.0
- ORHD.CA: score=19.41 buy_ready=False sector_rank=19 price=42.02 support=40.85 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.18 liquidity=303930464.0 spike=2.24
- ORWE.CA: score=20.01 buy_ready=False sector_rank=12 price=27.78 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.06 liquidity=31230326.0 spike=0.55
- PHAR.CA: score=8.99 buy_ready=False sector_rank=18 price=115.68 support=111.55 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.6 liquidity=96399088.0 spike=0.89
- PHDC.CA: score=8.93 buy_ready=False sector_rank=19 price=13.36 support=12.91 resistance=15.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=22.14 liquidity=85381296.0 spike=0.5
- PHTV.CA: score=5.1 buy_ready=False sector_rank=16 price=335.17 support=311.27 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=49.26 liquidity=862860.56 spike=0.51
- POUL.CA: score=16.88 buy_ready=False sector_rank=15 price=38.55 support=37.15 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=21 September 01:28 PM market time freshness=DELAYED_CURRENT RSI=38.94 liquidity=58845364.0 spike=2.28
- PRCL.CA: score=8.96 buy_ready=False sector_rank=21 price=30.95 support=30.61 resistance=34.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=46.88 liquidity=5479674.5 spike=0.3
- PRDC.CA: score=8.93 buy_ready=False sector_rank=19 price=7.56 support=7.51 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=9.33 liquidity=14629211.0 spike=0.25
- PRMH.CA: score=7.8 buy_ready=False sector_rank=16 price=2.59 support=2.32 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=3558851.5 spike=0.34
- RACC.CA: score=5.84 buy_ready=False sector_rank=16 price=9.69 support=9.4 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.44 liquidity=1600696.75 spike=0.09
- RAKT.CA: score=3.32 buy_ready=False sector_rank=16 price=22.08 support=21.4 resistance=23.02 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=47.17 liquidity=81607.68 spike=0.37
- RAYA.CA: score=13.8 buy_ready=False sector_rank=20 price=7.0 support=6.8 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=14756161.0 spike=0.27
- RMDA.CA: score=16.99 buy_ready=False sector_rank=18 price=6.06 support=5.77 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=14272387.0 spike=0.24
- ROTO.CA: score=5.86 buy_ready=False sector_rank=16 price=40.7 support=35.02 resistance=47.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.67 liquidity=6623861.0 spike=0.77
- RREI.CA: score=8.19 buy_ready=False sector_rank=16 price=4.21 support=4.2 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.62 liquidity=3949696.5 spike=0.22
- RTVC.CA: score=0.16 buy_ready=False sector_rank=16 price=3.86 support=3.79 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.69 liquidity=915922.5 spike=0.21
- RUBX.CA: score=6.92 buy_ready=False sector_rank=16 price=14.12 support=14.07 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=89751304.0 spike=2.34
- SAUD.CA: score=23.4 buy_ready=False sector_rank=6 price=25.6 support=22.7 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=65.55 liquidity=17498606.0 spike=0.96
- SCEM.CA: score=8.48 buy_ready=False sector_rank=21 price=85.93 support=87.02 resistance=105.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=21.91 liquidity=40560896.0 spike=0.36
- SCFM.CA: score=0.29 buy_ready=False sector_rank=16 price=270.3 support=250.2 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=34.9 liquidity=1046218.06 spike=0.14
- SCTS.CA: score=2.12 buy_ready=False sector_rank=9 price=581.8 support=566.66 resistance=640.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=22.63 liquidity=1304219.0 spike=0.45
- SDTI.CA: score=16.64 buy_ready=False sector_rank=16 price=78.84 support=67.0 resistance=79.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=75.63 liquidity=30931548.0 spike=1.2
- SEIG.CA: score=6.32 buy_ready=False sector_rank=16 price=239.4 support=228.13 resistance=274.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=29.74 liquidity=4200065.0 spike=2.44
- SIPC.CA: score=17.24 buy_ready=False sector_rank=16 price=5.47 support=4.1 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.94 liquidity=29226880.0 spike=0.42
- SKPC.CA: score=18.84 buy_ready=False sector_rank=8 price=17.92 support=17.0 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.39 liquidity=52862532.0 spike=0.41
- SMFR.CA: score=0.94 buy_ready=False sector_rank=16 price=232.05 support=226.1 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=26.93 liquidity=1703453.5 spike=0.21
- SNFC.CA: score=18.24 buy_ready=False sector_rank=16 price=11.54 support=10.26 resistance=11.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=79.25 liquidity=13551740.0 spike=0.86
- SPIN.CA: score=6.44 buy_ready=False sector_rank=12 price=17.3 support=16.1 resistance=20.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.6 liquidity=3431087.0 spike=0.25
- SPMD.CA: score=14.24 buy_ready=False sector_rank=16 price=0.41 support=0.41 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.24 liquidity=14854247.0 spike=0.2
- SUGR.CA: score=14.46 buy_ready=False sector_rank=15 price=59.42 support=55.06 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.46 liquidity=7148679.5 spike=0.11
- SVCE.CA: score=17.24 buy_ready=False sector_rank=16 price=11.3 support=9.6 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.71 liquidity=62190140.0 spike=0.31
- SWDY.CA: score=17.45 buy_ready=False sector_rank=14 price=125.55 support=122.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.17 liquidity=10192385.0 spike=0.15
- TALM.CA: score=20.82 buy_ready=False sector_rank=9 price=20.86 support=17.11 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=67.79 liquidity=32608542.0 spike=0.49
- TMGH.CA: score=13.93 buy_ready=False sector_rank=19 price=94.18 support=93.08 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.73 liquidity=152019104.0 spike=0.53
- TRTO.CA: score=7.78 buy_ready=False sector_rank=16 price=0.06 support=0.05 resistance=0.08 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=48.39 liquidity=35016.92 spike=1.25
- UEFM.CA: score=0.81 buy_ready=False sector_rank=16 price=480.2 support=440.66 resistance=574.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=32.59 liquidity=2570455.75 spike=0.85
- UEGC.CA: score=16.76 buy_ready=False sector_rank=16 price=1.7 support=1.66 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.06 liquidity=63414604.0 spike=1.26
- UNIP.CA: score=11.23 buy_ready=False sector_rank=16 price=0.37 support=0.37 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=6990749.0 spike=0.3
- UNIT.CA: score=5.87 buy_ready=False sector_rank=19 price=18.13 support=17.12 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.79 liquidity=1940164.25 spike=0.13
- WCDF.CA: score=11.29 buy_ready=False sector_rank=16 price=706.22 support=636.31 resistance=796.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=67.72 liquidity=2051701.75 spike=0.4
- WKOL.CA: score=11.12 buy_ready=False sector_rank=16 price=334.07 support=325.0 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.17 liquidity=3883356.75 spike=0.27
- ZEOT.CA: score=8.82 buy_ready=False sector_rank=16 price=13.2 support=13.03 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.68 liquidity=1577992.88 spike=0.24
- ZMID.CA: score=16.93 buy_ready=False sector_rank=19 price=8.39 support=7.9 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.56 liquidity=87115888.0 spike=0.41

## Backtesting Lite
- GBCO.CA: 180d return=17.08%, max drawdown=-24.35%, MA20>MA50 days last20=0, as_of=2026-09-20T21:00:00+00:00
- ATQA.CA: 180d return=33.43%, max drawdown=-21.44%, MA20>MA50 days last20=20, as_of=2026-09-20T21:00:00+00:00
- ETEL.CA: 180d return=109.1%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-09-20T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- ATQA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr National Steel Ataqa summary=Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- SAUD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=629 sources=3 expected=Al Baraka Bank Egypt summary=Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26; Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE; Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025
  - Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26: https://english.mubasher.info/news/4611927/Al-Baraka-Bank-Egypt-records-EGP-2-2bn-operating-income-in-Q1-26/
  - Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE: https://english.mubasher.info/news/4583822/Al-Baraka-Bank-Egypt-files-MTO-to-acquire-majority-stake-in-A-T-LEASE/
  - Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025: https://english.mubasher.info/news/4583458/Al-Baraka-Bank-Egypt-to-pay-EGP-1-1-share-dividends-for-2025/
- EXPA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Export Development Bank of Egypt summary=Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- HDBK.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Housing and Development Bank Egypt summary=Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- ABUK.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Qir Fertilizers summary=Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results; Abu Qir Fertilizers&#39; board approves $5.6m coated urea project; Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26
  - Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results: https://english.mubasher.info/news/4604919/Abu-Qir-Fertilizers-generates-EGP-5-6bn-net-profits-in-Q1-26-unaudited-results/
  - Abu Qir Fertilizers&#39; board approves $5.6m coated urea project: https://english.mubasher.info/news/4585599/Abu-Qir-Fertilizers-board-approves-5-6m-coated-urea-project/
  - Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26: https://english.mubasher.info/news/4554415/Abu-Qir-Fertilizers-profits-exceed-EGP-5-1bn-in-H1-25-26/

## Warnings
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence for SAUD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- Evidence for ABUK.CA matches the company but no source/report date was detected.
