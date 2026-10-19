# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-10-19T15:15:42.477498+00:00
Generated Cairo: 2026-10-19 18:15
Run timing: target 11:00 Cairo | generated Cairo 2026-10-19 18:15 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-10-19 18:12

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 173/187
- Top sector: Telecommunications

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, October 19
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 5.56% / above MA50 11.11%
- EGX70 regime: BEARISH / above MA20 2.5% / above MA50 10.0%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=627607744.0 spike=1.07 score=8.16
- COMI.CA: liquidity=555990912.0 spike=1.14 score=14.18
- NIPH.CA: liquidity=348441856.0 spike=2.9 score=6.47
- ARCC.CA: liquidity=264521392.0 spike=8.43 score=17.41
- POUL.CA: liquidity=253806336.0 spike=9.0 score=12.03

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with weak breadth (0% sector upside), keeping risk mode defensive and blocking new buys; the scanner highlights a handful of top‑ranked tickets that show constructive outlooks but sit in a cooling liquidity environment.
- Tickets were picked for their highest rank scores and sector leadership (Telecom, Fintech, etc.) despite the overall bearish EGX30/EGX70 regime.
- Liquidity is mostly TRADEABLE or ACCUMULATION_SPIKE, yet liquidity_spike values are modest or cooling, suggesting limited short‑term trading capacity.
- Each ticket lies a single‑digit to low‑double‑digit percent above its 20‑day support and similarly below resistance, implying modest upside potential over the next 1‑3 days.
- Outlooks range from BULLISH_WATCH to CONSTRUCTIVE to NEUTRAL, but the defensive market regime adds uncertainty—any gains could reverse quickly if breadth does not improve.

## Top Liquidity Spikes
- POUL.CA: spike=9.0 liquidity=253806336.0 outlook=WEAK_OR_RISKY score=22 buy_ready=False
- ARCC.CA: spike=8.43 liquidity=264521392.0 outlook=NEUTRAL score=48 buy_ready=False
- CPCI.CA: spike=3.81 liquidity=15746233.0 outlook=CONSTRUCTIVE score=62 buy_ready=False
- NIPH.CA: spike=2.9 liquidity=348441856.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MOIL.CA: spike=2.72 liquidity=785710.75 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=2.48 5d=-2.54% 20d=1.09% aboveMA50=50.0%
- #2 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #3 Fintech & Payments: score=1.44 5d=-2.15% 20d=-2.04% aboveMA50=0.0%
- #4 Energy & Petrochemicals: score=-0.49 5d=-4.88% 20d=-5.29% aboveMA50=33.33%
- #5 Transportation & Logistics: score=-0.88 5d=-3.85% 20d=-6.69% aboveMA50=0.0%
- #6 Tourism & Leisure: score=-2.38 5d=-3.41% 20d=-6.57% aboveMA50=0.0%
- #7 Food, Beverages & Tobacco: score=-2.42 5d=-1.88% 20d=-13.16% aboveMA50=0.0%
- #8 Investment Holding: score=-2.46 5d=-5.32% 20d=-14.68% aboveMA50=33.33%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ETEL.CA: BULLISH_WATCH score=70.48 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20
- AMOC.CA: CONSTRUCTIVE score=63 liquidity=TRADEABLE sector=NEUTRAL risk=below MA20
- CPCI.CA: CONSTRUCTIVE score=62 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=below MA20; momentum is extended; sector is not leading
- SIPC.CA: CONSTRUCTIVE score=60 liquidity=TRADEABLE sector=LAGGING risk=far above support; sector is not leading; high short-term volatility
- EFIH.CA: CONSTRUCTIVE score=59.44 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA50
- ARAB.CA: CONSTRUCTIVE score=58 liquidity=TRADEABLE sector=LAGGING risk=momentum is extended; far above support; sector is not leading
- BINV.CA: CONSTRUCTIVE score=58 liquidity=TRADEABLE sector=LAGGING risk=below MA20; sector is not leading
- TALM.CA: CONSTRUCTIVE score=58 liquidity=TRADEABLE sector=LAGGING risk=below MA20; sector is not leading
- INFI.CA: CONSTRUCTIVE score=56 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=below MA50; far above support; sector is not leading
- RUBX.CA: CONSTRUCTIVE score=55 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; far above support; sector is not leading; high short-term volatility

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=3.22 buy_ready=False sector_rank=17 price=218.95 support=214.0 resistance=316.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=25.72 liquidity=5823610.5 spike=0.49
- ABUK.CA: score=3.08 buy_ready=False sector_rank=19 price=87.63 support=80.5 resistance=88.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=110657352.0 spike=1.34
- ACAMD.CA: score=14.72 buy_ready=False sector_rank=17 price=2.04 support=1.87 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.86 liquidity=54040472.0 spike=1.16
- ACGC.CA: score=7.96 buy_ready=False sector_rank=15 price=12.87 support=12.6 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.02 liquidity=5557863.0 spike=0.49
- ADCI.CA: score=5.51 buy_ready=False sector_rank=17 price=256.27 support=250.06 resistance=288.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=2552253.75 spike=1.28
- ADIB.CA: score=7.9 buy_ready=False sector_rank=9 price=45.05 support=43.5 resistance=54.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.12 liquidity=73422592.0 spike=0.99
- ADPC.CA: score=6.4 buy_ready=False sector_rank=17 price=3.1 support=3.01 resistance=4.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.09 liquidity=10047717.0 spike=0.69
- AFDI.CA: score=5.64 buy_ready=False sector_rank=17 price=47.12 support=45.6 resistance=56.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.4 liquidity=3238697.25 spike=0.6
- AFMC.CA: score=12.4 buy_ready=False sector_rank=17 price=125.7 support=120.1 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.91 liquidity=19291102.0 spike=0.99
- AJWA.CA: score=14.4 buy_ready=False sector_rank=17 price=220.0 support=176.0 resistance=229.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=79.43 liquidity=21530354.0 spike=0.69
- ALCN.CA: score=13.65 buy_ready=False sector_rank=5 price=31.01 support=31.25 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.24 liquidity=17379258.0 spike=0.6
- ALUM.CA: score=0.55 buy_ready=False sector_rank=17 price=19.5 support=19.26 resistance=27.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=27.49 liquidity=4152122.25 spike=0.99
- AMER.CA: score=7.66 buy_ready=False sector_rank=18 price=4.1 support=4.05 resistance=5.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.25 liquidity=54997060.0 spike=1.13
- AMES.CA: score=8.4 buy_ready=False sector_rank=17 price=36.06 support=35.1 resistance=54.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.56 liquidity=49390696.0 spike=0.62
- AMIA.CA: score=15.64 buy_ready=False sector_rank=17 price=17.77 support=17.3 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.48 liquidity=19962966.0 spike=1.12
- AMOC.CA: score=16.82 buy_ready=False sector_rank=4 price=13.0 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.16 liquidity=120667504.0 spike=1.01
- APSW.CA: score=1.86 buy_ready=False sector_rank=17 price=7.88 support=7.81 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=44.09 liquidity=463152.28 spike=0.74
- ARAB.CA: score=17.4 buy_ready=False sector_rank=18 price=0.26 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.07 liquidity=88414408.0 spike=0.84
- ARCC.CA: score=17.41 buy_ready=False sector_rank=13 price=65.97 support=60.01 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=54.01 liquidity=264521392.0 spike=8.43
- AREH.CA: score=4.12 buy_ready=False sector_rank=17 price=1.14 support=1.1 resistance=1.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.69 liquidity=7720499.5 spike=0.92
- ASCM.CA: score=7.22 buy_ready=False sector_rank=17 price=45.8 support=45.5 resistance=61.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=23.71 liquidity=12156337.0 spike=1.41
- ASPI.CA: score=11.4 buy_ready=False sector_rank=17 price=0.32 support=0.31 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.43 liquidity=23334136.0 spike=0.84
- ATLC.CA: score=11.81 buy_ready=False sector_rank=14 price=5.1 support=4.84 resistance=7.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=9006277.0 spike=1.2
- ATQA.CA: score=7.4 buy_ready=False sector_rank=19 price=10.6 support=10.61 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.87 liquidity=25268198.0 spike=0.35
- AXPH.CA: score=4.45 buy_ready=False sector_rank=17 price=1292.12 support=1300.0 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=24.16 liquidity=6890960.0 spike=1.08
- BINV.CA: score=16.16 buy_ready=False sector_rank=8 price=58.0 support=52.11 resistance=67.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=58.12 liquidity=16816000.0 spike=1.07
- BIOC.CA: score=3.48 buy_ready=False sector_rank=17 price=290.33 support=257.0 resistance=297.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=158309664.0 spike=1.54
- BTFH.CA: score=11.4 buy_ready=False sector_rank=14 price=2.69 support=2.55 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.25 liquidity=84903640.0 spike=0.8
- CAED.CA: score=13.74 buy_ready=False sector_rank=17 price=93.69 support=95.0 resistance=136.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=36.17 liquidity=13488071.0 spike=1.67
- CANA.CA: score=7.9 buy_ready=False sector_rank=9 price=40.12 support=42.03 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.04 liquidity=21587936.0 spike=0.94
- CCAP.CA: score=8.16 buy_ready=False sector_rank=8 price=6.15 support=5.92 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.86 liquidity=627607744.0 spike=1.07
- CCRS.CA: score=1.96 buy_ready=False sector_rank=17 price=1.87 support=1.83 resistance=2.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=16.09 liquidity=5559187.0 spike=0.62
- CEFM.CA: score=3.66 buy_ready=False sector_rank=17 price=126.28 support=113.0 resistance=152.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.65 liquidity=1259702.0 spike=0.48
- CERA.CA: score=11.4 buy_ready=False sector_rank=17 price=1.23 support=1.18 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.68 liquidity=108240888.0 spike=0.91
- CFGH.CA: score=-3.51 buy_ready=False sector_rank=17 price=0.11 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-17T21:00:00+00:00 freshness=FRESH RSI=9.09 liquidity=6587.26 spike=1.04
- CICH.CA: score=-1.26 buy_ready=False sector_rank=14 price=10.89 support=9.63 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=28.8 liquidity=1337009.88 spike=0.38
- CIEB.CA: score=7.7 buy_ready=False sector_rank=9 price=22.04 support=21.97 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=28.84 liquidity=13240101.0 spike=1.4
- CIRA.CA: score=7.74 buy_ready=False sector_rank=11 price=35.19 support=35.01 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=33.6 liquidity=13093503.0 spike=0.61
- CLHO.CA: score=6.67 buy_ready=False sector_rank=12 price=13.72 support=13.0 resistance=16.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=33.05 liquidity=41087192.0 spike=1.0
- CNFN.CA: score=11.8 buy_ready=False sector_rank=14 price=3.99 support=3.8 resistance=4.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.64 liquidity=10960638.0 spike=1.2
- COMI.CA: score=14.18 buy_ready=False sector_rank=9 price=124.36 support=120.0 resistance=134.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.04 liquidity=555990912.0 spike=1.14
- COPR.CA: score=12.4 buy_ready=False sector_rank=17 price=0.44 support=0.41 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.87 liquidity=11303245.0 spike=0.55
- COSG.CA: score=6.64 buy_ready=False sector_rank=17 price=1.38 support=1.34 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.82 liquidity=16971966.0 spike=1.12
- CPCI.CA: score=20.4 buy_ready=False sector_rank=17 price=573.86 support=546.54 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=63.76 liquidity=15746233.0 spike=3.81
- CSAG.CA: score=15.77 buy_ready=False sector_rank=5 price=33.97 support=34.06 resistance=39.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.24 liquidity=12967513.0 spike=2.06
- DAPH.CA: score=12.0 buy_ready=False sector_rank=17 price=83.47 support=85.3 resistance=126.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.3 liquidity=53075364.0 spike=1.3
- DEIN.CA: score=5.4 buy_ready=False sector_rank=17 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 09:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37.26 spike=0.01
- DOMT.CA: score=3.12 buy_ready=False sector_rank=7 price=23.09 support=22.85 resistance=27.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.53 liquidity=1089938.63 spike=0.25
- DSCW.CA: score=6.4 buy_ready=False sector_rank=17 price=1.53 support=1.45 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.92 liquidity=14206490.0 spike=0.79
- DTPP.CA: score=7.4 buy_ready=False sector_rank=17 price=243.49 support=225.0 resistance=358.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.72 liquidity=22312434.0 spike=0.4
- EALR.CA: score=-1.35 buy_ready=False sector_rank=17 price=290.33 support=290.17 resistance=387.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.16 liquidity=2252673.75 spike=0.55
- EASB.CA: score=5.15 buy_ready=False sector_rank=17 price=6.14 support=6.04 resistance=8.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.49 liquidity=7012874.0 spike=1.37
- EAST.CA: score=14.03 buy_ready=False sector_rank=7 price=28.8 support=27.01 resistance=32.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.82 liquidity=14019393.0 spike=0.33
- EBSC.CA: score=4.4 buy_ready=False sector_rank=17 price=1.52 support=1.45 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=28.09 liquidity=5218965.0 spike=2.39
- ECAP.CA: score=-2.6 buy_ready=False sector_rank=17 price=27.41 support=27.0 resistance=32.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.54 liquidity=997087.06 spike=0.24
- EDFM.CA: score=3.18 buy_ready=False sector_rank=17 price=386.09 support=335.2 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=52.41 liquidity=777259.75 spike=0.67
- EEII.CA: score=1.74 buy_ready=False sector_rank=17 price=1.83 support=1.78 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=20.97 liquidity=5336181.5 spike=0.58
- EFIC.CA: score=11.4 buy_ready=False sector_rank=19 price=149.0 support=147.0 resistance=199.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.45 liquidity=18885004.0 spike=0.59
- EFID.CA: score=14.03 buy_ready=False sector_rank=7 price=18.13 support=18.07 resistance=21.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.62 liquidity=34685836.0 spike=0.74
- EFIH.CA: score=19.58 buy_ready=False sector_rank=3 price=23.63 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=55.02 liquidity=49623496.0 spike=0.75
- EGAL.CA: score=9.76 buy_ready=False sector_rank=19 price=295.51 support=280.0 resistance=376.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=12.62 liquidity=187459584.0 spike=2.68
- EGAS.CA: score=3.86 buy_ready=False sector_rank=4 price=50.51 support=48.08 resistance=60.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.37 liquidity=5054178.0 spike=0.62
- EGBE.CA: score=2.9 buy_ready=False sector_rank=9 price=0.51 support=0.5 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=7780.51 spike=0.06
- EGCH.CA: score=6.4 buy_ready=False sector_rank=19 price=11.49 support=10.85 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=12.78 liquidity=70273576.0 spike=0.86
- EGSA.CA: score=4.22 buy_ready=False sector_rank=1 price=8.76 support=8.75 resistance=9.09 source=Yahoo Finance as_of=2026-10-17T21:00:00+00:00 freshness=FRESH RSI=22.73 liquidity=8541.0 spike=1.61
- EGTS.CA: score=6.4 buy_ready=False sector_rank=18 price=13.15 support=12.62 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=16.43 liquidity=28645126.0 spike=0.79
- EHDR.CA: score=3.06 buy_ready=False sector_rank=17 price=2.24 support=2.08 resistance=2.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14176806.0 spike=1.33
- ELEC.CA: score=6.4 buy_ready=False sector_rank=16 price=1.65 support=1.6 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=28.07 liquidity=32861522.0 spike=0.87
- ELKA.CA: score=11.4 buy_ready=False sector_rank=17 price=1.47 support=1.38 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=46.38 liquidity=10400380.0 spike=0.78
- ELNA.CA: score=3.5 buy_ready=False sector_rank=17 price=35.22 support=33.46 resistance=36.4 source=Yahoo Finance as_of=2026-10-17T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=99743.04 spike=0.6
- ELSH.CA: score=12.4 buy_ready=False sector_rank=17 price=10.47 support=10.35 resistance=13.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.73 liquidity=14361091.0 spike=0.7
- ELWA.CA: score=6.46 buy_ready=False sector_rank=17 price=1.65 support=1.43 resistance=1.74 source=Yahoo Finance as_of=2026-10-17T21:00:00+00:00 freshness=FRESH RSI=52.78 liquidity=57608.1 spike=0.13
- EMFD.CA: score=12.4 buy_ready=False sector_rank=18 price=11.86 support=11.2 resistance=14.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.32 liquidity=29978506.0 spike=0.5
- ENGC.CA: score=5.5 buy_ready=False sector_rank=17 price=31.38 support=31.2 resistance=45.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=25.09 liquidity=9098785.0 spike=0.51
- EOSB.CA: score=4.4 buy_ready=False sector_rank=17 price=1.57 support=1.57 resistance=1.64 source=Yahoo Finance as_of=2026-10-17T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- EPCO.CA: score=0.68 buy_ready=False sector_rank=17 price=8.27 support=8.0 resistance=11.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.15 liquidity=4277604.5 spike=0.87
- EPPK.CA: score=-7.18 buy_ready=False sector_rank=17 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=20.99 buy_ready=False sector_rank=1 price=140.5 support=129.0 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.51 liquidity=184003584.0 spike=0.76
- ETRS.CA: score=13.7 buy_ready=False sector_rank=17 price=10.21 support=9.82 resistance=11.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.4 liquidity=16543187.0 spike=1.65
- EXPA.CA: score=6.9 buy_ready=False sector_rank=9 price=14.08 support=14.0 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=8.13 liquidity=20167764.0 spike=0.52
- FAIT.CA: score=7.46 buy_ready=False sector_rank=9 price=42.38 support=38.48 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.93 liquidity=3843401.5 spike=1.36
- FAITA.CA: score=5.41 buy_ready=False sector_rank=9 price=0.99 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=57.32 liquidity=49486.32 spike=1.23
- FERC.CA: score=-0.73 buy_ready=False sector_rank=19 price=64.2 support=64.01 resistance=82.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=23.46 liquidity=2870055.75 spike=0.64
- FWRY.CA: score=14.58 buy_ready=False sector_rank=3 price=18.4 support=17.5 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.74 liquidity=93578776.0 spike=0.86
- GBCO.CA: score=12.74 buy_ready=False sector_rank=10 price=29.41 support=27.0 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=44.46 liquidity=27400098.0 spike=0.25
- GDWA.CA: score=6.4 buy_ready=False sector_rank=17 price=0.6 support=0.58 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=31.34 liquidity=14171002.0 spike=0.75
- GGCC.CA: score=12.72 buy_ready=False sector_rank=17 price=0.64 support=0.61 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.58 liquidity=18767426.0 spike=1.16
- GIHD.CA: score=6.37 buy_ready=False sector_rank=17 price=47.58 support=48.48 resistance=78.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=15.21 liquidity=9966710.0 spike=0.52
- GMCI.CA: score=1.59 buy_ready=False sector_rank=17 price=1.54 support=1.47 resistance=1.78 source=Yahoo Finance as_of=2026-10-17T21:00:00+00:00 freshness=FRESH RSI=40.38 liquidity=187829.18 spike=0.49
- GRCA.CA: score=5.73 buy_ready=False sector_rank=17 price=28.82 support=29.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.07 liquidity=7334332.0 spike=1.0
- GSSC.CA: score=2.97 buy_ready=False sector_rank=17 price=262.91 support=246.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=41.05 liquidity=574986.94 spike=0.25
- GTWL.CA: score=2.96 buy_ready=False sector_rank=17 price=125.0 support=108.1 resistance=127.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=208948864.0 spike=1.28
- HDBK.CA: score=7.88 buy_ready=False sector_rank=9 price=93.59 support=96.1 resistance=121.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=29.19 liquidity=30176600.0 spike=1.49
- HELI.CA: score=7.4 buy_ready=False sector_rank=18 price=6.81 support=6.8 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.91 liquidity=80312080.0 spike=1.0
- HRHO.CA: score=13.4 buy_ready=False sector_rank=14 price=24.59 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.6 liquidity=61172316.0 spike=0.45
- ICID.CA: score=8.27 buy_ready=False sector_rank=17 price=16.87 support=16.3 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=42.54 liquidity=2873908.75 spike=0.35
- IDRE.CA: score=6.25 buy_ready=False sector_rank=17 price=40.01 support=40.05 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=36.34 liquidity=4850939.0 spike=0.48
- IFAP.CA: score=4.35 buy_ready=False sector_rank=21 price=17.92 support=17.17 resistance=21.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=26.04 liquidity=7651119.0 spike=1.15
- INFI.CA: score=17.74 buy_ready=False sector_rank=17 price=126.27 support=104.0 resistance=138.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=52.9 liquidity=30750998.0 spike=1.67
- IRON.CA: score=11.72 buy_ready=False sector_rank=19 price=26.35 support=25.01 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.15 liquidity=11988352.0 spike=1.16
- ISMA.CA: score=2.52 buy_ready=False sector_rank=17 price=21.31 support=19.22 resistance=21.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9502126.0 spike=1.31
- ISMQ.CA: score=6.58 buy_ready=False sector_rank=19 price=7.23 support=7.07 resistance=9.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=31.38 liquidity=20860916.0 spike=1.09
- ISPH.CA: score=6.67 buy_ready=False sector_rank=12 price=10.6 support=10.03 resistance=12.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.75 liquidity=38088820.0 spike=0.8
- JUFO.CA: score=7.57 buy_ready=False sector_rank=7 price=23.05 support=23.1 resistance=27.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.74 liquidity=21597634.0 spike=1.27
- KABO.CA: score=6.4 buy_ready=False sector_rank=15 price=7.05 support=6.91 resistance=9.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=33.19 liquidity=14849424.0 spike=0.65
- KWIN.CA: score=-0.91 buy_ready=False sector_rank=17 price=63.13 support=60.0 resistance=93.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=19.53 liquidity=2693565.25 spike=0.32
- KZPC.CA: score=8.19 buy_ready=False sector_rank=17 price=12.91 support=12.15 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=2786163.5 spike=0.33
- LCSW.CA: score=14.41 buy_ready=False sector_rank=13 price=32.55 support=28.86 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=55.88 liquidity=10557393.0 spike=0.52
- LUTS.CA: score=2.92 buy_ready=False sector_rank=17 price=0.7 support=0.63 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=69020664.0 spike=1.26
- MAAL.CA: score=2.4 buy_ready=False sector_rank=17 price=7.88 support=7.0 resistance=8.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11124039.0 spike=0.44
- MASR.CA: score=12.66 buy_ready=False sector_rank=17 price=7.01 support=6.82 resistance=7.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.04 liquidity=61859992.0 spike=1.13
- MBSC.CA: score=12.41 buy_ready=False sector_rank=13 price=334.83 support=288.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.98 liquidity=51204576.0 spike=0.57
- MCQE.CA: score=11.41 buy_ready=False sector_rank=13 price=161.97 support=160.0 resistance=224.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=36.18 liquidity=49534004.0 spike=0.85
- MCRO.CA: score=6.4 buy_ready=False sector_rank=17 price=1.32 support=1.25 resistance=1.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.91 liquidity=33920832.0 spike=0.62
- MENA.CA: score=-1.11 buy_ready=False sector_rank=18 price=5.93 support=5.57 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=32.71 liquidity=1487640.25 spike=0.92
- MEPA.CA: score=9.66 buy_ready=False sector_rank=17 price=1.53 support=1.49 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.66 liquidity=8257381.0 spike=0.88
- MFPC.CA: score=15.4 buy_ready=False sector_rank=19 price=43.92 support=42.0 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.26 liquidity=56039876.0 spike=0.84
- MFSC.CA: score=-2.17 buy_ready=False sector_rank=17 price=37.08 support=36.25 resistance=49.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=20.12 liquidity=1434070.63 spike=0.65
- MHOT.CA: score=0.6 buy_ready=False sector_rank=6 price=15.58 support=15.08 resistance=19.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=30.23 liquidity=3548176.5 spike=0.2
- MICH.CA: score=10.87 buy_ready=False sector_rank=17 price=39.35 support=38.0 resistance=47.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.02 liquidity=8471937.0 spike=0.98
- MILS.CA: score=3.06 buy_ready=False sector_rank=17 price=146.17 support=141.0 resistance=207.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=24.99 liquidity=5664590.0 spike=0.72
- MIPH.CA: score=4.67 buy_ready=False sector_rank=12 price=755.83 support=666.66 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.49 liquidity=1998461.75 spike=0.21
- MOED.CA: score=6.4 buy_ready=False sector_rank=17 price=0.56 support=0.57 resistance=0.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.17 liquidity=14336129.0 spike=0.89
- MOIL.CA: score=3.03 buy_ready=False sector_rank=4 price=0.67 support=0.63 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=22.83 liquidity=785710.75 spike=2.72
- MOIN.CA: score=3.37 buy_ready=False sector_rank=17 price=29.52 support=28.8 resistance=38.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.88 liquidity=5968822.0 spike=0.61
- MOSC.CA: score=4.53 buy_ready=False sector_rank=17 price=250.03 support=231.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=37.42 liquidity=2132041.25 spike=0.62
- MPCI.CA: score=8.48 buy_ready=False sector_rank=17 price=304.96 support=294.2 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.71 liquidity=159738912.0 spike=1.54
- MPCO.CA: score=7.4 buy_ready=False sector_rank=21 price=1.93 support=1.84 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.68 liquidity=106371256.0 spike=0.84
- MPRC.CA: score=8.12 buy_ready=False sector_rank=17 price=35.29 support=32.15 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=33.86 liquidity=22683718.0 spike=1.36
- MTIE.CA: score=6.74 buy_ready=False sector_rank=10 price=7.26 support=7.27 resistance=8.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.91 liquidity=16826980.0 spike=0.91
- NAHO.CA: score=3.73 buy_ready=False sector_rank=17 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=47.06 liquidity=50753.7 spike=1.64
- NCCW.CA: score=6.4 buy_ready=False sector_rank=17 price=5.51 support=5.3 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=31.55 liquidity=20070900.0 spike=0.53
- NEDA.CA: score=4.55 buy_ready=False sector_rank=17 price=2.6 support=2.47 resistance=2.8 source=Yahoo Finance as_of=2026-10-17T21:00:00+00:00 freshness=FRESH RSI=60.0 liquidity=154640.19 spike=0.24
- NHPS.CA: score=1.89 buy_ready=False sector_rank=17 price=61.22 support=61.18 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.23 liquidity=5486804.0 spike=0.38
- NINH.CA: score=6.4 buy_ready=False sector_rank=17 price=15.17 support=15.19 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=19.22 liquidity=12974692.0 spike=0.96
- NIPH.CA: score=6.47 buy_ready=False sector_rank=12 price=296.06 support=230.01 resistance=302.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=348441856.0 spike=2.9
- OBRI.CA: score=13.4 buy_ready=False sector_rank=17 price=25.21 support=22.8 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.7 liquidity=12414781.0 spike=0.85
- OCDI.CA: score=7.4 buy_ready=False sector_rank=18 price=24.49 support=24.0 resistance=30.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=33.09 liquidity=21609078.0 spike=0.52
- OCPH.CA: score=6.74 buy_ready=False sector_rank=17 price=193.08 support=190.0 resistance=247.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.51 liquidity=4602532.5 spike=1.37
- ODIN.CA: score=2.88 buy_ready=False sector_rank=17 price=2.2 support=1.91 resistance=2.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10618417.0 spike=1.24
- OFH.CA: score=7.4 buy_ready=False sector_rank=17 price=0.73 support=0.73 resistance=1.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.84 liquidity=26906454.0 spike=0.29
- OIH.CA: score=8.02 buy_ready=False sector_rank=8 price=1.77 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=33989412.0 spike=0.43
- OLFI.CA: score=5.09 buy_ready=False sector_rank=7 price=20.07 support=19.8 resistance=23.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=22.65 liquidity=8059097.5 spike=0.49
- ORAS.CA: score=6.6 buy_ready=False sector_rank=2 price=854.47 support=830.0 resistance=875.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=152243520.0 spike=1.0
- ORHD.CA: score=6.4 buy_ready=False sector_rank=18 price=10.07 support=10.01 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=2.84 liquidity=108817808.0 spike=0.74
- ORWE.CA: score=12.4 buy_ready=False sector_rank=15 price=26.1 support=26.01 resistance=28.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.75 liquidity=23164360.0 spike=0.51
- PHAR.CA: score=13.29 buy_ready=False sector_rank=12 price=104.22 support=101.5 resistance=122.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.96 liquidity=84067248.0 spike=1.31
- PHDC.CA: score=14.4 buy_ready=False sector_rank=18 price=12.43 support=12.2 resistance=13.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.52 liquidity=69046104.0 spike=0.73
- PHTV.CA: score=5.34 buy_ready=False sector_rank=17 price=330.0 support=315.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=42.94 liquidity=1479257.25 spike=1.73
- POUL.CA: score=12.03 buy_ready=False sector_rank=7 price=10.2 support=9.12 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=3.26 liquidity=253806336.0 spike=9.0
- PRCL.CA: score=6.99 buy_ready=False sector_rank=13 price=20.33 support=20.01 resistance=32.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=27.37 liquidity=13914684.0 spike=1.29
- PRDC.CA: score=11.4 buy_ready=False sector_rank=18 price=6.06 support=5.91 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.46 liquidity=17598654.0 spike=0.5
- PRMH.CA: score=-4.47 buy_ready=False sector_rank=17 price=2.03 support=1.81 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3126007.25 spike=0.86
- RACC.CA: score=7.41 buy_ready=False sector_rank=17 price=8.06 support=8.14 resistance=10.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.9 liquidity=9789227.0 spike=1.61
- RAKT.CA: score=1.68 buy_ready=False sector_rank=17 price=22.06 support=20.26 resistance=25.08 source=Yahoo Finance as_of=2026-10-17T21:00:00+00:00 freshness=FRESH RSI=49.81 liquidity=282787.13 spike=0.78
- RAYA.CA: score=11.4 buy_ready=False sector_rank=20 price=5.79 support=5.61 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.04 liquidity=19572888.0 spike=0.56
- RMDA.CA: score=7.89 buy_ready=False sector_rank=12 price=5.04 support=4.83 resistance=6.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.77 liquidity=30101978.0 spike=1.11
- ROTO.CA: score=6.21 buy_ready=False sector_rank=17 price=34.55 support=35.56 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=36.12 liquidity=4812441.5 spike=0.56
- RREI.CA: score=3.0 buy_ready=False sector_rank=17 price=3.29 support=3.29 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=32.76 liquidity=6597546.5 spike=0.81
- RTVC.CA: score=-1.09 buy_ready=False sector_rank=17 price=3.26 support=3.26 resistance=4.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.67 liquidity=2510017.25 spike=0.98
- RUBX.CA: score=17.4 buy_ready=False sector_rank=17 price=16.61 support=12.9 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.7 liquidity=62347632.0 spike=0.59
- SAUD.CA: score=12.9 buy_ready=False sector_rank=9 price=20.56 support=20.2 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.56 liquidity=14345343.0 spike=0.66
- SCEM.CA: score=16.41 buy_ready=False sector_rank=13 price=85.86 support=74.55 resistance=95.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.79 liquidity=21196352.0 spike=0.32
- SCFM.CA: score=9.32 buy_ready=False sector_rank=17 price=217.75 support=220.35 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.17 liquidity=4576884.0 spike=2.67
- SCTS.CA: score=-0.41 buy_ready=False sector_rank=11 price=476.54 support=460.0 resistance=611.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=22.15 liquidity=1228592.0 spike=1.31
- SDTI.CA: score=14.79 buy_ready=False sector_rank=17 price=83.1 support=76.1 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=42.97 liquidity=9389217.0 spike=0.29
- SEIG.CA: score=4.94 buy_ready=False sector_rank=17 price=202.44 support=173.1 resistance=259.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.34 liquidity=2262563.25 spike=1.14
- SIPC.CA: score=17.94 buy_ready=False sector_rank=17 price=5.54 support=4.22 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=54.65 liquidity=68244544.0 spike=1.27
- SKPC.CA: score=6.4 buy_ready=False sector_rank=19 price=14.95 support=14.6 resistance=18.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.3 liquidity=44023960.0 spike=0.59
- SMFR.CA: score=3.81 buy_ready=False sector_rank=17 price=191.7 support=181.6 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.16 liquidity=2409698.5 spike=0.76
- SNFC.CA: score=12.79 buy_ready=False sector_rank=17 price=11.33 support=10.81 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.42 liquidity=7389906.5 spike=0.69
- SPIN.CA: score=1.0 buy_ready=False sector_rank=15 price=13.99 support=14.06 resistance=17.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=30.14 liquidity=4601934.5 spike=0.87
- SPMD.CA: score=3.68 buy_ready=False sector_rank=17 price=0.38 support=0.34 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25703564.0 spike=1.64
- SUGR.CA: score=11.4 buy_ready=False sector_rank=7 price=54.67 support=50.5 resistance=60.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=51.16 liquidity=6370142.0 spike=0.64
- SVCE.CA: score=6.4 buy_ready=False sector_rank=17 price=8.92 support=8.81 resistance=12.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=47755728.0 spike=0.6
- SWDY.CA: score=12.7 buy_ready=False sector_rank=16 price=108.89 support=102.31 resistance=128.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.0 liquidity=70477496.0 spike=1.15
- TALM.CA: score=15.74 buy_ready=False sector_rank=11 price=20.08 support=18.71 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.15 liquidity=28113912.0 spike=0.81
- TMGH.CA: score=6.4 buy_ready=False sector_rank=18 price=81.8 support=81.22 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=20.13 liquidity=146444016.0 spike=0.66
- TRTO.CA: score=0.13 buy_ready=False sector_rank=17 price=0.06 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-10-17T21:00:00+00:00 freshness=FRESH RSI=78.95 liquidity=13117.0 spike=1.36
- UEFM.CA: score=3.12 buy_ready=False sector_rank=17 price=480.03 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.2 liquidity=1724866.63 spike=0.56
- UEGC.CA: score=16.06 buy_ready=False sector_rank=17 price=1.57 support=1.34 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.12 liquidity=65369952.0 spike=1.33
- UNIP.CA: score=10.34 buy_ready=False sector_rank=17 price=0.31 support=0.3 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.38 liquidity=8918669.0 spike=1.01
- UNIT.CA: score=3.46 buy_ready=False sector_rank=18 price=16.29 support=16.0 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=39.88 liquidity=1060986.25 spike=0.24
- WCDF.CA: score=-4.88 buy_ready=False sector_rank=17 price=479.21 support=432.5 resistance=511.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2720858.75 spike=0.93
- WKOL.CA: score=8.48 buy_ready=False sector_rank=17 price=257.86 support=266.01 resistance=352.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=29.25 liquidity=12241521.0 spike=2.04
- ZEOT.CA: score=13.0 buy_ready=False sector_rank=17 price=10.61 support=9.75 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=39.77 liquidity=10661886.0 spike=1.3
- ZMID.CA: score=7.4 buy_ready=False sector_rank=18 price=6.88 support=6.5 resistance=9.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.84 liquidity=57604520.0 spike=0.6

## Backtesting Lite
- ETEL.CA: 180d return=91.76%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-10-17T21:00:00+00:00
- CPCI.CA: 180d return=121.04%, max drawdown=-7.27%, MA20>MA50 days last20=20, as_of=2026-10-17T21:00:00+00:00
- EFIH.CA: 180d return=20.49%, max drawdown=-22.68%, MA20>MA50 days last20=4, as_of=2026-10-17T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- CPCI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Kahira Pharmaceuticals & Chemical Industries Company summary=Kahira Pharmaceuticals&#39; net profits up 22.5% in H1-21/22; Kahira Pharmaceuticals sees EGP 9m block trading deal; Adel Taha Abdel Wahab named Chairman of Kahira Pharmaceuticals
  - Kahira Pharmaceuticals&#39; net profits up 22.5% in H1-21/22: https://english.mubasher.info/news/3910780/Kahira-Pharmaceuticals-net-profits-up-22-5-in-H1-21-22/
  - Kahira Pharmaceuticals sees EGP 9m block trading deal: https://english.mubasher.info/news/3903033/Kahira-Pharmaceuticals-sees-EGP-9m-block-trading-deal/
  - Adel Taha Abdel Wahab named Chairman of Kahira Pharmaceuticals: https://english.mubasher.info/news/3816375/Adel-Taha-Abdel-Wahab-named-Chairman-of-Kahira-Pharmaceuticals/
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- SIPC.CA: status=OLD_ACCEPTED latest=2020-01-01 age_days=2483 sources=3 expected=Sabaa International Company for Pharmaceutical and Chemical Industry summary=Sabaa Pharmaceutical&#39;s shareholders approve capital raise via bonus issue; FRA approves Sabaa Pharmaceutical&#39;s capital raise; Sabaa Pharmaceutical&#39;s profit leaps 76% in 2020 initial results
  - Sabaa Pharmaceutical&#39;s shareholders approve capital raise via bonus issue: https://english.mubasher.info/news/3809286/Sabaa-Pharmaceutical-s-shareholders-approve-capital-raise-via-bonus-issue/
  - FRA approves Sabaa Pharmaceutical&#39;s capital raise: https://english.mubasher.info/news/3789753/FRA-approves-Sabaa-Pharmaceutical-s-capital-raise/
  - Sabaa Pharmaceutical&#39;s profit leaps 76% in 2020 initial results: https://english.mubasher.info/news/3779465/Sabaa-Pharmaceutical-s-profit-leaps-76-in-2020-initial-results/
- INFI.CA: status=RECENT_ACCEPTED latest=2026-01-01 age_days=291 sources=3 expected=Ismailia National Co. for Food Industries summary=Foodico stock targets higher levels; Foodico plans to log nearly EGP 70.5m profits in 2026; Foodico to secure EGP 12m loan from national bank
  - Foodico stock targets higher levels: https://english.mubasher.info/news/4564894/Foodico-stock-targets-higher-levels/
  - Foodico plans to log nearly EGP 70.5m profits in 2026: https://english.mubasher.info/news/4541309/Foodico-plans-to-log-nearly-EGP-70-5m-profits-in-2026/
  - Foodico to secure EGP 12m loan from national bank: https://english.mubasher.info/news/3888447/Foodico-to-secure-EGP-12m-loan-from-national-bank/
- ARCC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=656 sources=3 expected=Arabian Cement Company summary=Arabian Cement to pay out EGP 2bn dividends for 2025; Arabian Cement’s EGM approves nearly EGP 8m capital cut; Arabian Cement’s consolidated profits near EGP 3.6bn in 2025
  - Arabian Cement to pay out EGP 2bn dividends for 2025: https://english.mubasher.info/news/4587912/Arabian-Cement-to-pay-out-EGP-2bn-dividends-for-2025/
  - Arabian Cement’s EGM approves nearly EGP 8m capital cut: https://english.mubasher.info/news/4583762/Arabian-Cement-s-EGM-approves-nearly-EGP-8m-capital-cut/
  - Arabian Cement’s consolidated profits near EGP 3.6bn in 2025: https://english.mubasher.info/news/4562679/Arabian-Cement-s-consolidated-profits-near-EGP-3-6bn-in-2025/
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- RUBX.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Rubex International for Plastic and Acrylic Manufacturing summary=Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.

## Warnings
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for CPCI.CA matches the company but no source/report date was detected.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence for SIPC.CA matches the company but appears old; latest detected date is 2020-01-01.
- Evidence for ARCC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
