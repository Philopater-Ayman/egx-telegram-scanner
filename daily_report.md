# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-11-04T15:57:38.503284+00:00
Generated Cairo: 2026-11-04 17:57
Run timing: target 11:00 Cairo | generated Cairo 2026-11-04 17:57 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-11-04 17:54

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 6
- Tradeable price/liquidity tickers: 156/184
- Top sector: Fintech & Payments

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, November 04
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 43.75% / above MA50 12.5%
- EGX70 regime: BEARISH / above MA20 25.71% / above MA50 5.71%
- Sector breadth: 4.76%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=452623488.0 spike=1.06 score=13.29
- COMI.CA: liquidity=380469920.0 spike=0.72 score=17.51
- ORHD.CA: liquidity=227865872.0 spike=1.98 score=19.1
- EGAL.CA: liquidity=218775296.0 spike=2.48 score=5.81
- BIOC.CA: liquidity=217109088.0 spike=2.76 score=24.5

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- ELWA.CA: spike=31.99 liquidity=9424553.0 outlook=WEAK_OR_RISKY score=23 buy_ready=False
- AALR.CA: spike=15.49 liquidity=138537968.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EALR.CA: spike=11.36 liquidity=37595984.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GRCA.CA: spike=9.2 liquidity=47896912.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CICH.CA: spike=5.56 liquidity=10504793.0 outlook=WEAK_OR_RISKY score=21 buy_ready=False

## Sector Leaderboard
- #1 Fintech & Payments: score=5.54 5d=3.6% 20d=-1.5% aboveMA50=50.0%
- #2 Food, Beverages & Tobacco: score=3.24 5d=0.0% 20d=-6.42% aboveMA50=14.29%
- #3 Building Materials: score=1.63 5d=2.73% 20d=-16.11% aboveMA50=33.33%
- #4 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #5 Banking & Financials: score=1.28 5d=-0.38% 20d=-6.98% aboveMA50=10.0%
- #6 Tourism & Leisure: score=1.27 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #7 Healthcare: score=0.89 5d=0.0% 20d=-6.84% aboveMA50=0.0%
- #8 Transportation & Logistics: score=0.66 5d=4.05% 20d=-8.04% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- EFIH.CA: BULLISH_WATCH score=85.54 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- LCSW.CA: BULLISH_WATCH score=77.63 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- SCEM.CA: BULLISH_WATCH score=76.63 liquidity=TRADEABLE sector=LEADING risk=far above support
- ETRS.CA: BULLISH_WATCH score=76 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=sector is not leading
- UNIT.CA: BULLISH_WATCH score=74.36 liquidity=TRADEABLE sector=IMPROVING risk=far above support; sector is not leading
- POUL.CA: BULLISH_WATCH score=73.24 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=below MA50
- DOMT.CA: BULLISH_WATCH score=73.24 liquidity=TRADEABLE sector=LEADING risk=below MA50
- BIOC.CA: BULLISH_WATCH score=72 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=far above support; sector is not leading; high short-term volatility
- SEIG.CA: BULLISH_WATCH score=72 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=momentum is extended; far above support; sector is not leading; high short-term volatility
- CANA.CA: CONSTRUCTIVE score=67.28 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; far above support

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- WKOL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ZEOT.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=8.98 buy_ready=False sector_rank=13 price=250.9 support=218.15 resistance=258.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=138537968.0 spike=15.49
- ABUK.CA: score=12.85 buy_ready=False sector_rank=18 price=79.77 support=77.25 resistance=95.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=42.4 liquidity=85832776.0 spike=0.93
- ACAMD.CA: score=13.42 buy_ready=False sector_rank=13 price=2.01 support=1.86 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=122727232.0 spike=2.72
- ACGC.CA: score=8.44 buy_ready=False sector_rank=14 price=12.95 support=11.6 resistance=14.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=45.66 liquidity=4788656.5 spike=0.66
- ADCI.CA: score=8.89 buy_ready=False sector_rank=13 price=256.43 support=221.0 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=45.89 liquidity=2325639.0 spike=1.29
- ADIB.CA: score=19.49 buy_ready=False sector_rank=5 price=49.0 support=43.16 resistance=49.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=53.78 liquidity=118705088.0 spike=1.49
- ADPC.CA: score=8.36 buy_ready=False sector_rank=13 price=3.06 support=2.53 resistance=3.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=43.26 liquidity=3382976.5 spike=0.38
- AFDI.CA: score=3.56 buy_ready=False sector_rank=13 price=44.07 support=34.8 resistance=54.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=33.23 liquidity=2575668.75 spike=0.82
- AFMC.CA: score=20.3 buy_ready=False sector_rank=13 price=136.89 support=94.6 resistance=163.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=48.69 liquidity=35092752.0 spike=2.16
- AJWA.CA: score=18.98 buy_ready=False sector_rank=13 price=219.6 support=187.0 resistance=229.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=45.18 liquidity=13282162.0 spike=0.41
- ALCN.CA: score=9.56 buy_ready=False sector_rank=8 price=32.24 support=27.11 resistance=35.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=46.53 liquidity=5295035.5 spike=0.42
- ALUM.CA: score=10.21 buy_ready=False sector_rank=13 price=19.38 support=16.02 resistance=24.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=37.79 liquidity=4306806.0 spike=1.46
- AMER.CA: score=5.98 buy_ready=False sector_rank=10 price=4.51 support=4.34 resistance=4.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=105982728.0 spike=1.92
- AMES.CA: score=12.02 buy_ready=False sector_rank=13 price=33.96 support=28.0 resistance=49.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=34.56 liquidity=89926904.0 spike=2.02
- AMIA.CA: score=16.76 buy_ready=False sector_rank=13 price=17.98 support=14.0 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=44.88 liquidity=17586140.0 spike=1.39
- AMOC.CA: score=15.22 buy_ready=False sector_rank=15 price=13.3 support=12.55 resistance=15.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=49.34 liquidity=154216320.0 spike=0.97
- APSW.CA: score=-1.66 buy_ready=False sector_rank=13 price=7.4 support=7.1 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:13 PM market time freshness=DELAYED_CURRENT RSI=33.13 liquidity=361482.53 spike=0.72
- ARAB.CA: score=14.14 buy_ready=False sector_rank=10 price=0.24 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=36.76 liquidity=72753760.0 spike=0.64
- ARCC.CA: score=16.11 buy_ready=False sector_rank=3 price=65.16 support=58.01 resistance=73.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=39.39 liquidity=44020840.0 spike=1.23
- AREH.CA: score=14.82 buy_ready=False sector_rank=13 price=1.08 support=0.91 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=36.73 liquidity=9215633.0 spike=1.31
- ASCM.CA: score=5.04 buy_ready=False sector_rank=13 price=44.69 support=42.4 resistance=45.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11773850.0 spike=1.53
- ASPI.CA: score=5.18 buy_ready=False sector_rank=13 price=0.32 support=0.3 resistance=0.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27858896.0 spike=1.6
- ATLC.CA: score=19.85 buy_ready=False sector_rank=12 price=5.0 support=3.93 resistance=6.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=40.48 liquidity=19786182.0 spike=2.93
- ATQA.CA: score=6.85 buy_ready=False sector_rank=18 price=9.29 support=8.25 resistance=12.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=23.8 liquidity=33269382.0 spike=0.7
- AXPH.CA: score=11.54 buy_ready=False sector_rank=13 price=1319.29 support=1135.0 resistance=1538.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=42.06 liquidity=5321230.5 spike=1.12
- BINV.CA: score=8.55 buy_ready=False sector_rank=16 price=52.56 support=50.62 resistance=62.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=22.55 liquidity=12464158.0 spike=1.19
- BIOC.CA: score=24.5 buy_ready=False sector_rank=13 price=308.51 support=212.05 resistance=359.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=50.56 liquidity=217109088.0 spike=2.76
- BTFH.CA: score=9.73 buy_ready=False sector_rank=12 price=2.35 support=2.05 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=34.4 liquidity=206323328.0 spike=1.87
- CAED.CA: score=22.98 buy_ready=False sector_rank=13 price=102.64 support=64.0 resistance=125.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=45.7 liquidity=56183604.0 spike=4.87
- CANA.CA: score=21.51 buy_ready=False sector_rank=5 price=45.96 support=38.1 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=53.06 liquidity=13950383.0 spike=0.76
- CCAP.CA: score=13.29 buy_ready=False sector_rank=16 price=5.99 support=5.55 resistance=6.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.94 liquidity=452623488.0 spike=1.06
- CCRS.CA: score=8.98 buy_ready=False sector_rank=13 price=1.9 support=1.69 resistance=1.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28985242.0 spike=4.67
- CEFM.CA: score=6.11 buy_ready=False sector_rank=13 price=117.95 support=97.79 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:10 PM market time freshness=DELAYED_CURRENT RSI=43.84 liquidity=2125822.25 spike=0.98
- CERA.CA: score=7.98 buy_ready=False sector_rank=13 price=1.04 support=0.93 resistance=1.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=25.45 liquidity=50568692.0 spike=0.51
- CFGH.CA: score=1.72 buy_ready=False sector_rank=13 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-11-02T22:00:00+00:00 freshness=FRESH RSI=14.29 liquidity=16708.0 spike=2.86
- CICH.CA: score=17.99 buy_ready=False sector_rank=12 price=10.57 support=9.63 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.23 liquidity=10504793.0 spike=5.56
- CIEB.CA: score=10.36 buy_ready=False sector_rank=5 price=22.68 support=21.35 resistance=24.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=44.1 liquidity=2844977.0 spike=0.35
- CIRA.CA: score=20.88 buy_ready=False sector_rank=9 price=36.64 support=32.01 resistance=40.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=41.17 liquidity=31144848.0 spike=2.32
- CLHO.CA: score=15.36 buy_ready=False sector_rank=7 price=13.43 support=12.51 resistance=15.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=39.16 liquidity=28989684.0 spike=0.77
- CNFN.CA: score=9.67 buy_ready=False sector_rank=12 price=3.84 support=3.25 resistance=4.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=45.0 liquidity=4678264.5 spike=0.52
- COMI.CA: score=17.51 buy_ready=False sector_rank=5 price=125.84 support=117.41 resistance=129.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=52.46 liquidity=380469920.0 spike=0.72
- COPR.CA: score=13.98 buy_ready=False sector_rank=13 price=0.41 support=0.33 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=35.48 liquidity=13954438.0 spike=0.99
- COSG.CA: score=15.2 buy_ready=False sector_rank=13 price=1.29 support=1.11 resistance=1.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=35.71 liquidity=10088096.0 spike=1.11
- CPCI.CA: score=11.65 buy_ready=False sector_rank=13 price=601.11 support=502.25 resistance=620.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=45.21 liquidity=2674673.5 spike=0.56
- CSAG.CA: score=9.3 buy_ready=False sector_rank=8 price=34.1 support=30.1 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=3036723.0 spike=0.45
- DAPH.CA: score=9.98 buy_ready=False sector_rank=13 price=82.65 support=65.2 resistance=114.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=34.22 liquidity=19496924.0 spike=0.52
- DEIN.CA: score=6.98 buy_ready=False sector_rank=13 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=29 October 12:10 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=62.1 spike=0.02
- DOMT.CA: score=15.75 buy_ready=False sector_rank=2 price=23.47 support=20.27 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=48.41 liquidity=4017913.75 spike=1.72
- DSCW.CA: score=13.06 buy_ready=False sector_rank=13 price=1.45 support=1.23 resistance=1.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=35.14 liquidity=12897170.0 spike=1.04
- DTPP.CA: score=14.98 buy_ready=False sector_rank=13 price=47.15 support=36.0 resistance=334.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=38.76 liquidity=17485716.0 spike=0.46
- EALR.CA: score=8.98 buy_ready=False sector_rank=13 price=303.42 support=260.0 resistance=303.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37595984.0 spike=11.36
- EASB.CA: score=18.96 buy_ready=False sector_rank=13 price=6.51 support=5.03 resistance=8.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=45.49 liquidity=13330218.0 spike=2.49
- EAST.CA: score=21.3 buy_ready=False sector_rank=2 price=32.86 support=27.01 resistance=32.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=67.73 liquidity=34686304.0 spike=0.87
- EBSC.CA: score=12.69 buy_ready=False sector_rank=13 price=1.53 support=1.2 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=43.3 liquidity=5688340.0 spike=2.01
- ECAP.CA: score=9.37 buy_ready=False sector_rank=13 price=27.39 support=24.8 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=36.96 liquidity=3670189.5 spike=1.36
- EDFM.CA: score=6.54 buy_ready=False sector_rank=13 price=353.91 support=312.92 resistance=382.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=36.51 liquidity=1675014.5 spike=1.44
- EEII.CA: score=5.9 buy_ready=False sector_rank=13 price=1.8 support=1.7 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13022957.0 spike=1.96
- EFIC.CA: score=13.85 buy_ready=False sector_rank=18 price=140.83 support=121.0 resistance=171.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=37.29 liquidity=14181716.0 spike=0.77
- EFID.CA: score=8.48 buy_ready=False sector_rank=2 price=19.24 support=18.3 resistance=19.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=52271716.0 spike=1.59
- EFIH.CA: score=26.22 buy_ready=False sector_rank=1 price=23.79 support=20.3 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=48.12 liquidity=32928058.0 spike=0.5
- EGAL.CA: score=5.81 buy_ready=False sector_rank=18 price=320.31 support=307.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=218775296.0 spike=2.48
- EGAS.CA: score=5.26 buy_ready=False sector_rank=15 price=46.76 support=43.0 resistance=57.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=35.17 liquidity=3048807.0 spike=0.75
- EGBE.CA: score=4.57 buy_ready=False sector_rank=5 price=0.49 support=0.47 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:11 PM market time freshness=DELAYED_CURRENT RSI=38.83 liquidity=55879.89 spike=0.65
- EGCH.CA: score=6.85 buy_ready=False sector_rank=18 price=10.34 support=9.66 resistance=13.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=26.92 liquidity=31298076.0 spike=0.58
- EGSA.CA: score=-1.89 buy_ready=False sector_rank=17 price=8.71 support=8.7 resistance=9.09 source=Yahoo Finance as_of=2026-11-02T22:00:00+00:00 freshness=FRESH RSI=34.62 liquidity=435.5 spike=0.11
- EGTS.CA: score=5.46 buy_ready=False sector_rank=10 price=13.13 support=12.2 resistance=13.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28369744.0 spike=1.66
- EHDR.CA: score=4.92 buy_ready=False sector_rank=13 price=2.05 support=1.99 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12900795.0 spike=1.47
- ELEC.CA: score=15.02 buy_ready=False sector_rank=11 price=1.6 support=1.34 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=40.62 liquidity=36072760.0 spike=0.72
- ELKA.CA: score=17.98 buy_ready=False sector_rank=13 price=1.47 support=1.21 resistance=1.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=43.59 liquidity=10218663.0 spike=0.77
- ELNA.CA: score=9.36 buy_ready=False sector_rank=13 price=39.41 support=33.46 resistance=41.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=73.04 liquidity=380186.97 spike=0.59
- ELSH.CA: score=17.32 buy_ready=False sector_rank=13 price=10.23 support=8.57 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=41.35 liquidity=25726894.0 spike=1.67
- ELWA.CA: score=12.4 buy_ready=False sector_rank=13 price=1.4 support=1.36 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=9424553.0 spike=31.99
- EMFD.CA: score=20.66 buy_ready=False sector_rank=10 price=12.2 support=10.6 resistance=13.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=54.2 liquidity=124347872.0 spike=2.26
- ENGC.CA: score=18.7 buy_ready=False sector_rank=13 price=35.47 support=26.91 resistance=37.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=50.42 liquidity=16413788.0 spike=1.86
- EOSB.CA: score=9.05 buy_ready=False sector_rank=13 price=1.61 support=1.55 resistance=1.72 source=Yahoo Finance as_of=2026-11-02T22:00:00+00:00 freshness=FRESH RSI=70.0 liquidity=73647.84 spike=0.82
- EPCO.CA: score=6.59 buy_ready=False sector_rank=13 price=8.44 support=7.0 resistance=10.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=42.49 liquidity=1608378.63 spike=0.32
- EPPK.CA: score=-5.6 buy_ready=False sector_rank=13 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=8.11 buy_ready=False sector_rank=17 price=126.59 support=115.0 resistance=150.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=30.58 liquidity=168286704.0 spike=0.69
- ETRS.CA: score=22.76 buy_ready=False sector_rank=13 price=10.75 support=9.51 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=51.74 liquidity=24863094.0 spike=1.89
- EXPA.CA: score=15.51 buy_ready=False sector_rank=5 price=13.81 support=12.0 resistance=16.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=42.19 liquidity=13227866.0 spike=0.42
- FAIT.CA: score=7.51 buy_ready=False sector_rank=5 price=43.26 support=40.0 resistance=45.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=48.0 liquidity=1002118.56 spike=0.4
- FAITA.CA: score=6.54 buy_ready=False sector_rank=5 price=0.99 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=60.44 liquidity=25988.72 spike=0.83
- FERC.CA: score=-1.67 buy_ready=False sector_rank=18 price=60.02 support=53.57 resistance=77.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=32.82 liquidity=1477414.0 spike=0.41
- FWRY.CA: score=9.96 buy_ready=False sector_rank=1 price=16.93 support=16.25 resistance=17.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=161612288.0 spike=1.37
- GBCO.CA: score=7.42 buy_ready=False sector_rank=21 price=22.09 support=20.9 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=15.79 liquidity=157477296.0 spike=1.51
- GDWA.CA: score=14.98 buy_ready=False sector_rank=13 price=0.55 support=0.46 resistance=0.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=37.65 liquidity=11797518.0 spike=1.0
- GGCC.CA: score=6.76 buy_ready=False sector_rank=13 price=0.56 support=0.53 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=41892048.0 spike=2.39
- GIHD.CA: score=9.98 buy_ready=False sector_rank=13 price=43.79 support=32.1 resistance=66.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=31.61 liquidity=10331157.0 spike=0.74
- GMCI.CA: score=0.66 buy_ready=False sector_rank=13 price=1.36 support=1.34 resistance=1.77 source=Yahoo Finance as_of=2026-11-02T22:00:00+00:00 freshness=FRESH RSI=12.12 liquidity=624174.73 spike=2.03
- GRCA.CA: score=8.98 buy_ready=False sector_rank=13 price=33.85 support=30.02 resistance=34.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=47896912.0 spike=9.2
- GSSC.CA: score=5.78 buy_ready=False sector_rank=13 price=252.49 support=211.52 resistance=288.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:12 PM market time freshness=DELAYED_CURRENT RSI=37.02 liquidity=1555527.63 spike=1.62
- HDBK.CA: score=13.51 buy_ready=False sector_rank=5 price=96.9 support=83.01 resistance=111.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=40.96 liquidity=20315392.0 spike=0.87
- HELI.CA: score=15.72 buy_ready=False sector_rank=10 price=6.65 support=5.72 resistance=7.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=35.88 liquidity=119566552.0 spike=1.79
- HRHO.CA: score=7.99 buy_ready=False sector_rank=12 price=23.18 support=21.87 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=27.16 liquidity=43189532.0 spike=0.58
- ICID.CA: score=5.38 buy_ready=False sector_rank=13 price=17.24 support=14.26 resistance=18.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=44.17 liquidity=1396660.13 spike=0.26
- IDRE.CA: score=14.61 buy_ready=False sector_rank=13 price=38.67 support=29.11 resistance=52.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=38.67 liquidity=8525156.0 spike=1.55
- IFAP.CA: score=0.28 buy_ready=False sector_rank=20 price=16.2 support=15.12 resistance=19.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=27.26 liquidity=3880536.5 spike=0.8
- INFI.CA: score=3.98 buy_ready=False sector_rank=13 price=120.85 support=115.5 resistance=121.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20577838.0 spike=0.98
- IRON.CA: score=8.52 buy_ready=False sector_rank=18 price=24.08 support=23.13 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=35.6 liquidity=6664003.5 spike=0.62
- ISMA.CA: score=15.78 buy_ready=False sector_rank=13 price=19.47 support=14.11 resistance=26.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=37.46 liquidity=10269637.0 spike=1.4
- ISMQ.CA: score=16.39 buy_ready=False sector_rank=18 price=7.35 support=5.96 resistance=8.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=17847426.0 spike=1.27
- ISPH.CA: score=9.36 buy_ready=False sector_rank=7 price=10.1 support=9.7 resistance=10.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=193237376.0 spike=4.25
- JUFO.CA: score=20.52 buy_ready=False sector_rank=2 price=23.95 support=21.01 resistance=25.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=43.55 liquidity=23084302.0 spike=1.11
- KABO.CA: score=4.23 buy_ready=False sector_rank=14 price=7.17 support=6.66 resistance=7.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25916144.0 spike=1.29
- KWIN.CA: score=8.98 buy_ready=False sector_rank=13 price=72.86 support=66.0 resistance=76.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30901662.0 spike=5.19
- KZPC.CA: score=7.72 buy_ready=False sector_rank=13 price=12.65 support=11.56 resistance=13.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=46.42 liquidity=3743508.75 spike=0.55
- LCSW.CA: score=22.65 buy_ready=False sector_rank=3 price=34.77 support=28.0 resistance=36.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=55.88 liquidity=11424620.0 spike=0.46
- LUTS.CA: score=17.98 buy_ready=False sector_rank=13 price=0.72 support=0.47 resistance=0.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.97 liquidity=48117624.0 spike=0.81
- MAAL.CA: score=8.54 buy_ready=False sector_rank=13 price=6.96 support=4.88 resistance=11.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=33.09 liquidity=9562390.0 spike=0.85
- MASR.CA: score=15.98 buy_ready=False sector_rank=13 price=6.78 support=5.6 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=41.73 liquidity=29259256.0 spike=0.61
- MBSC.CA: score=15.65 buy_ready=False sector_rank=3 price=316.14 support=262.0 resistance=404.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=39.98 liquidity=55207044.0 spike=0.69
- MCQE.CA: score=16.65 buy_ready=False sector_rank=3 price=166.96 support=144.0 resistance=209.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=39.74 liquidity=46296372.0 spike=0.78
- MCRO.CA: score=14.98 buy_ready=False sector_rank=13 price=1.32 support=1.07 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.19 liquidity=36816228.0 spike=0.92
- MENA.CA: score=5.52 buy_ready=False sector_rank=10 price=5.86 support=5.45 resistance=6.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=42.59 liquidity=379619.5 spike=0.09
- MEPA.CA: score=7.98 buy_ready=False sector_rank=13 price=1.29 support=1.14 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=24.32 liquidity=10815107.0 spike=0.77
- MFPC.CA: score=13.79 buy_ready=False sector_rank=18 price=40.8 support=39.59 resistance=47.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=40.76 liquidity=77636400.0 spike=1.47
- MFSC.CA: score=3.75 buy_ready=False sector_rank=13 price=35.45 support=33.0 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5628001.0 spike=3.07
- MHOT.CA: score=-0.1 buy_ready=False sector_rank=6 price=16.07 support=14.81 resistance=16.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5387124.5 spike=0.85
- MICH.CA: score=8.74 buy_ready=False sector_rank=13 price=40.11 support=35.5 resistance=44.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=44.54 liquidity=2762962.0 spike=0.47
- MILS.CA: score=14.59 buy_ready=False sector_rank=13 price=128.51 support=94.24 resistance=183.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=35.33 liquidity=9214765.0 spike=1.2
- MIPH.CA: score=-3.24 buy_ready=False sector_rank=7 price=798.92 support=754.0 resistance=799.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2405742.5 spike=0.69
- MOED.CA: score=9.54 buy_ready=False sector_rank=13 price=0.48 support=0.39 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=27.38 liquidity=21205540.0 spike=1.78
- MOIL.CA: score=-1.76 buy_ready=False sector_rank=15 price=0.63 support=0.6 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=34.3 liquidity=19033.06 spike=0.1
- MOIN.CA: score=12.49 buy_ready=False sector_rank=13 price=28.87 support=25.7 resistance=36.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=35.21 liquidity=8111190.5 spike=1.2
- MOSC.CA: score=7.78 buy_ready=False sector_rank=13 price=249.2 support=234.32 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9077484.0 spike=3.36
- MPCI.CA: score=17.98 buy_ready=False sector_rank=13 price=313.1 support=238.6 resistance=360.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.66 liquidity=88668288.0 spike=0.91
- MPCO.CA: score=6.4 buy_ready=False sector_rank=20 price=1.83 support=1.55 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=34.75 liquidity=75904072.0 spike=0.97
- MPRC.CA: score=14.98 buy_ready=False sector_rank=13 price=33.96 support=27.0 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=40.23 liquidity=11215442.0 spike=0.8
- MTIE.CA: score=5.75 buy_ready=False sector_rank=21 price=6.8 support=6.05 resistance=8.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=33.97 liquidity=9350523.0 spike=0.51
- NAHO.CA: score=3.99 buy_ready=False sector_rank=13 price=0.12 support=0.12 resistance=0.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=36.84 liquidity=5956.25 spike=0.34
- NCCW.CA: score=15.0 buy_ready=False sector_rank=13 price=5.5 support=4.05 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=41.46 liquidity=16956820.0 spike=1.01
- NEDA.CA: score=-1.93 buy_ready=False sector_rank=13 price=2.36 support=2.3 resistance=2.67 source=Yahoo Finance as_of=2026-11-02T22:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=89781.48 spike=0.57
- NHPS.CA: score=6.6 buy_ready=False sector_rank=13 price=60.87 support=59.22 resistance=64.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15690349.0 spike=2.31
- NINH.CA: score=10.57 buy_ready=False sector_rank=13 price=15.19 support=12.36 resistance=19.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=37.15 liquidity=5586130.5 spike=0.65
- NIPH.CA: score=18.64 buy_ready=False sector_rank=7 price=278.28 support=205.0 resistance=327.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=49.34 liquidity=143375472.0 spike=1.14
- OBRI.CA: score=14.1 buy_ready=False sector_rank=13 price=23.44 support=18.11 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=39.45 liquidity=9121708.0 spike=0.8
- OCDI.CA: score=16.7 buy_ready=False sector_rank=10 price=24.43 support=21.0 resistance=28.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=43.9 liquidity=41036080.0 spike=1.28
- OCPH.CA: score=8.51 buy_ready=False sector_rank=13 price=186.97 support=147.96 resistance=230.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=37.32 liquidity=3314594.0 spike=1.11
- ODIN.CA: score=14.72 buy_ready=False sector_rank=13 price=2.05 support=1.7 resistance=2.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=39.37 liquidity=8955265.0 spike=1.39
- OFH.CA: score=11.24 buy_ready=False sector_rank=13 price=0.71 support=0.61 resistance=0.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=34.23 liquidity=24194050.0 spike=1.13
- OIH.CA: score=4.77 buy_ready=False sector_rank=16 price=1.73 support=1.63 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=72013400.0 spike=1.8
- OLFI.CA: score=6.72 buy_ready=False sector_rank=2 price=19.27 support=17.86 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=21.41 liquidity=5422386.0 spike=0.48
- ORAS.CA: score=4.6 buy_ready=False sector_rank=4 price=800.0 support=796.1 resistance=812.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=105094000.0 spike=1.0
- ORHD.CA: score=19.1 buy_ready=False sector_rank=10 price=10.35 support=8.5 resistance=12.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=40.45 liquidity=227865872.0 spike=1.98
- ORWE.CA: score=13.39 buy_ready=False sector_rank=14 price=24.99 support=22.2 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=36.54 liquidity=9746986.0 spike=0.28
- PHAR.CA: score=16.78 buy_ready=False sector_rank=7 price=101.87 support=90.2 resistance=115.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=39.24 liquidity=61439312.0 spike=1.21
- PHDC.CA: score=13.14 buy_ready=False sector_rank=10 price=11.37 support=10.33 resistance=13.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=36.12 liquidity=86763712.0 spike=0.9
- PHTV.CA: score=13.36 buy_ready=False sector_rank=13 price=320.06 support=300.0 resistance=355.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:00 PM market time freshness=DELAYED_CURRENT RSI=38.07 liquidity=4379469.5 spike=3.63
- POUL.CA: score=21.82 buy_ready=False sector_rank=2 price=10.1 support=8.81 resistance=10.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=54.76 liquidity=117146520.0 spike=1.76
- PRCL.CA: score=18.65 buy_ready=False sector_rank=3 price=21.68 support=16.65 resistance=26.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=43.86 liquidity=12459139.0 spike=0.9
- PRDC.CA: score=18.14 buy_ready=False sector_rank=10 price=6.34 support=5.08 resistance=7.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=45.22 liquidity=16452857.0 spike=0.7
- PRMH.CA: score=12.74 buy_ready=False sector_rank=13 price=1.96 support=1.7 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=45.71 liquidity=5797378.5 spike=1.98
- RACC.CA: score=3.68 buy_ready=False sector_rank=13 price=7.8 support=6.1 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=34.36 liquidity=5696666.5 spike=0.84
- RAKT.CA: score=3.0 buy_ready=False sector_rank=13 price=22.35 support=20.4 resistance=25.08 source=Yahoo Finance as_of=2026-11-02T22:00:00+00:00 freshness=FRESH RSI=53.99 liquidity=20383.2 spike=0.06
- RAYA.CA: score=7.02 buy_ready=False sector_rank=19 price=5.45 support=5.02 resistance=6.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=33.49 liquidity=24960910.0 spike=1.31
- RMDA.CA: score=7.26 buy_ready=False sector_rank=7 price=5.45 support=5.15 resistance=5.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=58792804.0 spike=2.45
- ROTO.CA: score=12.98 buy_ready=False sector_rank=13 price=31.81 support=25.0 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=32.35 liquidity=32902036.0 spike=4.5
- RREI.CA: score=6.37 buy_ready=False sector_rank=13 price=2.81 support=1.96 resistance=4.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=28.7 liquidity=8393501.0 spike=0.8
- RTVC.CA: score=0.0 buy_ready=False sector_rank=13 price=2.8 support=2.66 resistance=3.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=19.09 liquidity=2021587.75 spike=0.76
- RUBX.CA: score=8.98 buy_ready=False sector_rank=13 price=13.37 support=10.51 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=34.92 liquidity=57044760.0 spike=0.7
- SAUD.CA: score=3.21 buy_ready=False sector_rank=5 price=20.28 support=19.3 resistance=23.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=33.62 liquidity=4702838.5 spike=0.43
- SCEM.CA: score=22.69 buy_ready=False sector_rank=3 price=92.27 support=73.9 resistance=95.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=52.13 liquidity=50960888.0 spike=1.02
- SCFM.CA: score=9.32 buy_ready=False sector_rank=13 price=217.65 support=153.02 resistance=252.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:12 PM market time freshness=DELAYED_CURRENT RSI=42.32 liquidity=3199113.5 spike=1.57
- SCTS.CA: score=8.86 buy_ready=False sector_rank=9 price=494.45 support=410.0 resistance=579.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=51.01 liquidity=2616821.25 spike=0.59
- SDTI.CA: score=18.98 buy_ready=False sector_rank=13 price=88.79 support=75.01 resistance=90.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=53.12 liquidity=12836500.0 spike=0.71
- SEIG.CA: score=23.48 buy_ready=False sector_rank=13 price=254.57 support=142.0 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=67.37 liquidity=17556374.0 spike=2.25
- SIPC.CA: score=8.98 buy_ready=False sector_rank=13 price=4.67 support=3.73 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=29.92 liquidity=23951646.0 spike=0.42
- SKPC.CA: score=14.03 buy_ready=False sector_rank=18 price=14.67 support=14.01 resistance=16.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=40.28 liquidity=54407052.0 spike=1.09
- SMFR.CA: score=8.07 buy_ready=False sector_rank=13 price=189.76 support=165.0 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=41.27 liquidity=2954503.0 spike=1.07
- SNFC.CA: score=8.29 buy_ready=False sector_rank=13 price=10.65 support=10.08 resistance=11.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=34.76 liquidity=9731629.0 spike=1.29
- SPIN.CA: score=8.49 buy_ready=False sector_rank=14 price=14.45 support=12.0 resistance=17.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=45.66 liquidity=3845547.0 spike=0.72
- SPMD.CA: score=15.02 buy_ready=False sector_rank=13 price=0.34 support=0.3 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=46.0 liquidity=14428356.0 spike=1.02
- SUGR.CA: score=22.3 buy_ready=False sector_rank=2 price=48.2 support=44.62 resistance=54.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=42.67 liquidity=31221402.0 spike=3.69
- SVCE.CA: score=16.44 buy_ready=False sector_rank=13 price=8.82 support=7.01 resistance=10.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=40.49 liquidity=82491296.0 spike=1.73
- SWDY.CA: score=18.02 buy_ready=False sector_rank=11 price=111.97 support=97.0 resistance=120.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=43.02 liquidity=47005564.0 spike=0.96
- TALM.CA: score=9.36 buy_ready=False sector_rank=9 price=19.6 support=17.0 resistance=22.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=33.55 liquidity=24149128.0 spike=1.06
- TMGH.CA: score=13.14 buy_ready=False sector_rank=10 price=81.11 support=76.5 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=42.83 liquidity=214158512.0 spike=0.84
- TRTO.CA: score=-1.02 buy_ready=False sector_rank=13 price=0.05 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-11-02T22:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=2168.87 spike=0.38
- UEFM.CA: score=-0.81 buy_ready=False sector_rank=13 price=464.55 support=444.0 resistance=467.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:06 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3692632.0 spike=1.76
- UEGC.CA: score=16.98 buy_ready=False sector_rank=13 price=1.47 support=1.21 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=49.53 liquidity=40489452.0 spike=0.88
- UNIP.CA: score=8.51 buy_ready=False sector_rank=13 price=0.29 support=0.25 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=5533809.0 spike=0.77
- UNIT.CA: score=15.8 buy_ready=False sector_rank=10 price=18.51 support=15.06 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=57.94 liquidity=2652811.0 spike=0.87
- WCDF.CA: score=1.15 buy_ready=False sector_rank=13 price=501.84 support=432.5 resistance=630.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:04 PM market time freshness=DELAYED_CURRENT RSI=32.86 liquidity=1166686.25 spike=0.67
- ZMID.CA: score=17.38 buy_ready=False sector_rank=10 price=6.8 support=5.91 resistance=7.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=42.33 liquidity=111738864.0 spike=1.62

## Backtesting Lite
- EFIH.CA: 180d return=3.16%, max drawdown=-22.68%, MA20>MA50 days last20=0, as_of=2026-11-02T22:00:00+00:00
- BIOC.CA: 180d return=361.98%, max drawdown=-58.13%, MA20>MA50 days last20=0, as_of=2026-11-02T22:00:00+00:00
- SEIG.CA: 180d return=69.87%, max drawdown=-46.21%, MA20>MA50 days last20=0, as_of=2026-11-02T22:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- BIOC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GlaxoSmithKline S.A.E summary=Evidence rejected for BIOC.CA: source text did not clearly match BIOC.CA / GlaxoSmithKline S.A.E.
- SEIG.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=672 sources=3 expected=Saudi Egyptian Investment & Finance Co. S.A.E summary=Saudi Egyptian Investment unveils EGP 2/shr dividends for 2025; Saudi Egyptian Investment and Finance sees 15% higher profit in 2020; Saudi Egyptian Investment records higher profit in 2019
  - Saudi Egyptian Investment unveils EGP 2/shr dividends for 2025: https://english.mubasher.info/news/4590273/Saudi-Egyptian-Investment-unveils-EGP-2-shr-dividends-for-2025/
  - Saudi Egyptian Investment and Finance sees 15% higher profit in 2020: https://english.mubasher.info/news/3766715/Saudi-Egyptian-Investment-and-Finance-sees-15-higher-profit-in-2020/
  - Saudi Egyptian Investment records higher profit in 2019: https://english.mubasher.info/news/3588475/Saudi-Egyptian-Investment-records-higher-profit-in-2019/
- CAED.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Educational Services SAE summary=Cairo Educational Services&#39; OGM approves EGP 1/shr coupon distribution; Cairo Educational Services’ board proposes 80 piastres per-share dividends; Cairo Educational Services’ profit declines in FY18/19
  - Cairo Educational Services&#39; OGM approves EGP 1/shr coupon distribution: https://english.mubasher.info/news/3884789/Cairo-Educational-Services-OGM-approves-EGP-1-shr-coupon-distribution/
  - Cairo Educational Services’ board proposes 80 piastres per-share dividends: https://english.mubasher.info/news/3556129/Cairo-Educational-Services-board-proposes-80-piastres-per-share-dividends/
  - Cairo Educational Services’ profit declines in FY18/19: https://english.mubasher.info/news/3556119/Cairo-Educational-Services-profit-declines-in-FY18-19/
- ETRS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Transport and Commercial Services Company S.A.E. summary=Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- SCEM.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=672 sources=3 expected=Sinai Cement summary=Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn; Upward trend line ends several-day decline for Sinai Cement stock; Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25
  - Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn: https://english.mubasher.info/news/4564824/Sinai-Cement-s-consolidated-profits-fall-in-2025-net-sales-cross-EGP-9bn/
  - Upward trend line ends several-day decline for Sinai Cement stock: https://english.mubasher.info/news/4529647/Upward-trend-line-ends-several-day-decline-for-Sinai-Cement-stock/
  - Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25: https://english.mubasher.info/news/4526073/Sinai-Cement-reports-lower-consolidated-net-profits-at-EGP-1-5bn-in-9M-25/
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- SUGR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=672 sources=3 expected=Delta Sugar summary=Delta Sugar’s net profits fall 74% in Q1-26; Delta Sugar stock tests key resistance near EGP 50 amid downtrend; Delta Sugar turns to EGP 346m net losses in 2025
  - Delta Sugar’s net profits fall 74% in Q1-26: https://english.mubasher.info/news/4604921/Delta-Sugar-s-net-profits-fall-74-in-Q1-26/
  - Delta Sugar stock tests key resistance near EGP 50 amid downtrend: https://english.mubasher.info/news/4584932/Delta-Sugar-stock-tests-key-resistance-near-EGP-50-amid-downtrend/
  - Delta Sugar turns to EGP 346m net losses in 2025: https://english.mubasher.info/news/4557875/Delta-Sugar-turns-to-EGP-346m-net-losses-in-2025/

## Warnings
- OpenRouter API error: 404
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for BIOC.CA: source text did not clearly match BIOC.CA / GlaxoSmithKline S.A.E.
- Evidence for SEIG.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CAED.CA matches the company but no source/report date was detected.
- Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- Evidence for SCEM.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence for SUGR.CA matches the company but appears old; latest detected date is 2025-01-01.
