# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-10-14T13:19:11.619578+00:00
Generated Cairo: 2026-10-14 16:19
Run timing: target 11:00 Cairo | generated Cairo 2026-10-14 16:19 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-10-14 16:14

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 5
- Tradeable price/liquidity tickers: 171/185
- Top sector: Telecommunications

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, October 14
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 16.67% / above MA50 16.67%
- EGX70 regime: BEARISH / above MA20 10.53% / above MA50 15.79%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=758744448.0 spike=1.42 score=8.47
- ORAS.CA: liquidity=432261824.0 spike=1.0 score=5.6
- CCAP.CA: liquidity=356053856.0 spike=0.57 score=11.95
- ETEL.CA: liquidity=292474720.0 spike=1.08 score=24.56
- TMGH.CA: liquidity=205810672.0 spike=0.92 score=6.4

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with weak breadth, putting the market in defensive mode; the scanner flags a few tradeable stocks with bullish‑watch outlooks but notes cooling liquidity and mixed sector leadership, so no new buys are advised.

## Top Liquidity Spikes
- MOSC.CA: spike=3.34 liquidity=10906855.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ZEOT.CA: spike=3.19 liquidity=17970370.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MTIE.CA: spike=2.66 liquidity=45101824.0 outlook=WEAK_OR_RISKY score=28 buy_ready=False
- FAITA.CA: spike=2.3 liquidity=68021.46 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ACAMD.CA: spike=2.15 liquidity=91765712.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=9.23 5d=-1.39% 20d=7.18% aboveMA50=100.0%
- #2 Fintech & Payments: score=3.08 5d=-1.84% 20d=0.58% aboveMA50=50.0%
- #3 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #4 Energy & Petrochemicals: score=0.24 5d=-3.74% 20d=0.0% aboveMA50=33.33%
- #5 Transportation & Logistics: score=-0.0 5d=-5.39% 20d=-0.61% aboveMA50=50.0%
- #6 Investment Holding: score=-0.12 5d=-5.29% 20d=-8.61% aboveMA50=66.67%
- #7 Automotive & Distribution: score=-0.89 5d=-7.09% 20d=-3.71% aboveMA50=0.0%
- #8 Banking & Financials: score=-0.93 5d=-4.62% 20d=-4.87% aboveMA50=10.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ETEL.CA: BULLISH_WATCH score=94.23 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- EFIH.CA: BULLISH_WATCH score=83.08 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- TALM.CA: CONSTRUCTIVE score=65 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- SDTI.CA: CONSTRUCTIVE score=65 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- AMOC.CA: CONSTRUCTIVE score=58.24 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; below MA20
- ICID.CA: CONSTRUCTIVE score=58 liquidity=TRADEABLE sector=LAGGING risk=below MA20; sector is not leading
- ALCN.CA: CONSTRUCTIVE score=58 liquidity=TRADEABLE sector=NEUTRAL risk=liquidity is cooling; below MA20
- BINV.CA: CONSTRUCTIVE score=58 liquidity=TRADEABLE sector=NEUTRAL risk=liquidity is cooling; momentum is extended; far above support
- ARAB.CA: CONSTRUCTIVE score=55 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; far above support; sector is not leading
- RUBX.CA: CONSTRUCTIVE score=55 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; far above support; sector is not leading; high short-term volatility

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- MICH.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=1.08 buy_ready=False sector_rank=18 price=234.92 support=225.0 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=23.05 liquidity=3684397.0 spike=0.19
- ABUK.CA: score=7.4 buy_ready=False sector_rank=15 price=84.14 support=83.0 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.06 liquidity=48501764.0 spike=0.52
- ACAMD.CA: score=4.7 buy_ready=False sector_rank=18 price=2.12 support=1.97 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=91765712.0 spike=2.15
- ACGC.CA: score=5.58 buy_ready=False sector_rank=17 price=13.18 support=12.81 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.41 liquidity=3184045.0 spike=0.18
- ADCI.CA: score=4.02 buy_ready=False sector_rank=18 price=262.24 support=250.06 resistance=288.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.41 liquidity=1615326.88 spike=0.74
- ADIB.CA: score=4.31 buy_ready=False sector_rank=8 price=46.76 support=44.63 resistance=47.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=102457808.0 spike=1.34
- ADPC.CA: score=1.19 buy_ready=False sector_rank=18 price=3.19 support=3.01 resistance=4.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=15.32 liquidity=4790143.5 spike=0.31
- AFDI.CA: score=1.12 buy_ready=False sector_rank=18 price=50.33 support=46.12 resistance=56.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.49 liquidity=1722745.63 spike=0.26
- AFMC.CA: score=5.76 buy_ready=False sector_rank=18 price=134.3 support=122.0 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.45 liquidity=8361114.5 spike=0.4
- AJWA.CA: score=4.12 buy_ready=False sector_rank=18 price=221.9 support=210.01 resistance=222.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48646464.0 spike=1.86
- ALCN.CA: score=15.03 buy_ready=False sector_rank=5 price=33.02 support=30.4 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.53 liquidity=8028317.0 spike=0.23
- ALUM.CA: score=-1.06 buy_ready=False sector_rank=18 price=21.25 support=20.52 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=23.54 liquidity=2539811.75 spike=0.54
- AMER.CA: score=14.4 buy_ready=False sector_rank=16 price=4.76 support=4.05 resistance=5.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.92 liquidity=50113780.0 spike=0.9
- AMES.CA: score=8.4 buy_ready=False sector_rank=18 price=39.83 support=38.02 resistance=59.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=28.79 liquidity=42528556.0 spike=0.43
- AMIA.CA: score=9.1 buy_ready=False sector_rank=18 price=18.42 support=17.12 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.66 liquidity=3699773.0 spike=0.2
- AMOC.CA: score=17.1 buy_ready=False sector_rank=4 price=13.51 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=62409508.0 spike=0.49
- APSW.CA: score=2.06 buy_ready=False sector_rank=18 price=7.91 support=7.81 resistance=8.92 source=Yahoo Finance as_of=2026-10-12T21:00:00+00:00 freshness=FRESH RSI=42.21 liquidity=659891.74 spike=0.96
- ARAB.CA: score=19.4 buy_ready=False sector_rank=16 price=0.27 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.67 liquidity=68019152.0 spike=0.69
- ARCC.CA: score=12.94 buy_ready=False sector_rank=11 price=66.95 support=60.01 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.62 liquidity=17377148.0 spike=0.55
- AREH.CA: score=0.92 buy_ready=False sector_rank=18 price=1.18 support=1.11 resistance=1.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.92 liquidity=4523704.0 spike=0.54
- ASCM.CA: score=1.56 buy_ready=False sector_rank=18 price=50.24 support=48.0 resistance=61.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=24.83 liquidity=5155075.5 spike=0.58
- ASPI.CA: score=6.4 buy_ready=False sector_rank=18 price=0.33 support=0.31 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=22.8 liquidity=12029290.0 spike=0.35
- ATLC.CA: score=0.04 buy_ready=False sector_rank=10 price=5.56 support=5.38 resistance=5.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6705141.0 spike=0.65
- ATQA.CA: score=2.42 buy_ready=False sector_rank=15 price=11.8 support=11.14 resistance=12.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=74135640.0 spike=1.01
- AXPH.CA: score=2.01 buy_ready=False sector_rank=18 price=1408.31 support=1300.0 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=18.49 liquidity=4606770.5 spike=0.66
- BINV.CA: score=12.69 buy_ready=False sector_rank=6 price=60.12 support=49.91 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.17 liquidity=3733656.0 spike=0.14
- BIOC.CA: score=16.4 buy_ready=False sector_rank=18 price=300.09 support=225.21 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.45 liquidity=73725360.0 spike=0.72
- BTFH.CA: score=7.33 buy_ready=False sector_rank=10 price=2.68 support=2.55 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.86 liquidity=84133112.0 spike=0.85
- CAED.CA: score=6.12 buy_ready=False sector_rank=18 price=106.29 support=95.0 resistance=145.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=33.02 liquidity=8715110.0 spike=0.88
- CANA.CA: score=16.63 buy_ready=False sector_rank=8 price=43.95 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.05 liquidity=14905070.0 spike=0.62
- CCAP.CA: score=11.95 buy_ready=False sector_rank=6 price=6.2 support=6.07 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=24.04 liquidity=356053856.0 spike=0.57
- CCRS.CA: score=1.49 buy_ready=False sector_rank=18 price=2.07 support=1.87 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.18 liquidity=4089247.25 spike=0.31
- CEFM.CA: score=-1.12 buy_ready=False sector_rank=18 price=126.04 support=113.0 resistance=152.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.95 liquidity=1484694.25 spike=0.54
- CERA.CA: score=12.4 buy_ready=False sector_rank=18 price=1.29 support=1.18 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.47 liquidity=119852256.0 spike=0.98
- CFGH.CA: score=-1.39 buy_ready=False sector_rank=18 price=0.1 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-12T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=12242.47 spike=2.1
- CICH.CA: score=4.37 buy_ready=False sector_rank=10 price=11.08 support=10.6 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.38 liquidity=5034630.5 spike=1.5
- CIEB.CA: score=9.77 buy_ready=False sector_rank=8 price=22.98 support=22.56 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=26.5 liquidity=14676281.0 spike=1.57
- CIRA.CA: score=11.44 buy_ready=False sector_rank=9 price=38.19 support=35.51 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.28 liquidity=11334533.0 spike=0.44
- CLHO.CA: score=8.02 buy_ready=False sector_rank=14 price=13.92 support=13.9 resistance=16.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.06 liquidity=67131592.0 spike=1.81
- CNFN.CA: score=1.49 buy_ready=False sector_rank=10 price=4.01 support=3.8 resistance=4.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=30.72 liquidity=4162173.0 spike=0.48
- COMI.CA: score=8.47 buy_ready=False sector_rank=8 price=122.53 support=120.0 resistance=134.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=13.94 liquidity=758744448.0 spike=1.42
- COPR.CA: score=12.4 buy_ready=False sector_rank=18 price=0.46 support=0.44 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=40.43 liquidity=12997891.0 spike=0.53
- COSG.CA: score=6.4 buy_ready=False sector_rank=18 price=1.46 support=1.34 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=20.63 liquidity=13524384.0 spike=0.9
- CPCI.CA: score=10.8 buy_ready=False sector_rank=18 price=606.98 support=530.0 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=70.44 liquidity=3397113.0 spike=0.84
- CSAG.CA: score=5.47 buy_ready=False sector_rank=5 price=35.86 support=34.06 resistance=39.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=32.98 liquidity=6471245.0 spike=0.81
- DAPH.CA: score=7.4 buy_ready=False sector_rank=18 price=97.15 support=89.1 resistance=129.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.81 liquidity=24139262.0 spike=0.6
- DEIN.CA: score=5.4 buy_ready=False sector_rank=18 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 09:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37.26 spike=0.01
- DOMT.CA: score=-2.81 buy_ready=False sector_rank=13 price=23.25 support=22.85 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=25.45 liquidity=786412.38 spike=0.16
- DSCW.CA: score=6.4 buy_ready=False sector_rank=18 price=1.62 support=1.55 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=20.0 liquidity=11175598.0 spike=0.63
- DTPP.CA: score=2.4 buy_ready=False sector_rank=18 price=230.35 support=225.0 resistance=269.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19381780.0 spike=0.26
- EALR.CA: score=-1.51 buy_ready=False sector_rank=18 price=311.86 support=290.17 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=23.48 liquidity=2087530.63 spike=0.22
- EASB.CA: score=5.62 buy_ready=False sector_rank=18 price=6.99 support=6.04 resistance=8.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.21 liquidity=3218281.0 spike=0.48
- EAST.CA: score=6.4 buy_ready=False sector_rank=13 price=27.77 support=27.01 resistance=34.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.31 liquidity=23533022.0 spike=0.49
- EBSC.CA: score=-2.35 buy_ready=False sector_rank=18 price=1.64 support=1.5 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.05 liquidity=1252093.75 spike=0.53
- ECAP.CA: score=-2.14 buy_ready=False sector_rank=18 price=28.31 support=27.5 resistance=32.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=18.18 liquidity=1461262.5 spike=0.34
- EDFM.CA: score=2.98 buy_ready=False sector_rank=18 price=393.23 support=335.2 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.63 liquidity=580646.81 spike=0.51
- EEII.CA: score=1.36 buy_ready=False sector_rank=18 price=1.95 support=1.83 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=28.17 liquidity=4964914.5 spike=0.55
- EFIC.CA: score=6.4 buy_ready=False sector_rank=15 price=154.11 support=147.0 resistance=203.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=22.24 liquidity=14020734.0 spike=0.36
- EFID.CA: score=8.4 buy_ready=False sector_rank=13 price=18.6 support=18.07 resistance=31.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.74 liquidity=42008028.0 spike=0.83
- EFIH.CA: score=24.23 buy_ready=False sector_rank=2 price=23.84 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=54.41 liquidity=27107944.0 spike=0.4
- EGAL.CA: score=7.58 buy_ready=False sector_rank=15 price=312.97 support=306.1 resistance=376.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=14.6 liquidity=59584232.0 spike=1.09
- EGAS.CA: score=1.52 buy_ready=False sector_rank=4 price=52.0 support=48.08 resistance=60.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.41 liquidity=2424107.25 spike=0.21
- EGBE.CA: score=4.86 buy_ready=False sector_rank=8 price=0.51 support=0.49 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=188942.2 spike=1.52
- EGCH.CA: score=6.4 buy_ready=False sector_rank=15 price=12.11 support=11.86 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=21.23 liquidity=58015584.0 spike=0.71
- EGSA.CA: score=11.51 buy_ready=False sector_rank=1 price=8.95 support=8.82 resistance=9.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=11.76 liquidity=14868.3 spike=2.05
- EGTS.CA: score=7.4 buy_ready=False sector_rank=16 price=14.08 support=13.56 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=14.74 liquidity=29317958.0 spike=0.84
- EHDR.CA: score=5.64 buy_ready=False sector_rank=18 price=2.26 support=2.1 resistance=2.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=24.36 liquidity=9242008.0 spike=0.79
- ELEC.CA: score=6.4 buy_ready=False sector_rank=19 price=1.72 support=1.65 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.08 liquidity=17119900.0 spike=0.31
- ELKA.CA: score=5.9 buy_ready=False sector_rank=18 price=1.51 support=1.38 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.79 liquidity=9497539.0 spike=0.79
- ELNA.CA: score=3.55 buy_ready=False sector_rank=18 price=35.22 support=33.46 resistance=36.4 source=Yahoo Finance as_of=2026-10-12T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=145599.49 spike=0.93
- ELSH.CA: score=8.06 buy_ready=False sector_rank=18 price=10.93 support=10.76 resistance=13.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=28.97 liquidity=26516012.0 spike=1.33
- ELWA.CA: score=6.52 buy_ready=False sector_rank=18 price=1.65 support=1.43 resistance=1.78 source=Yahoo Finance as_of=2026-10-12T21:00:00+00:00 freshness=FRESH RSI=45.45 liquidity=118291.8 spike=0.2
- EMFD.CA: score=7.4 buy_ready=False sector_rank=16 price=11.95 support=11.7 resistance=14.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=32.87 liquidity=18085414.0 spike=0.27
- ENGC.CA: score=3.88 buy_ready=False sector_rank=18 price=33.84 support=32.37 resistance=45.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.35 liquidity=7477638.0 spike=0.41
- EOSB.CA: score=7.42 buy_ready=False sector_rank=18 price=1.57 support=1.64 resistance=1.64 source=Yahoo Finance as_of=2026-10-12T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=23903.25 spike=0.54
- EPCO.CA: score=-1.17 buy_ready=False sector_rank=18 price=8.89 support=8.0 resistance=11.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=20.51 liquidity=2427487.0 spike=0.41
- EPPK.CA: score=-7.18 buy_ready=False sector_rank=18 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=24.56 buy_ready=False sector_rank=1 price=144.55 support=126.02 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.5 liquidity=292474720.0 spike=1.08
- ETRS.CA: score=10.66 buy_ready=False sector_rank=18 price=10.48 support=9.82 resistance=11.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.94 liquidity=8261037.5 spike=0.77
- EXPA.CA: score=7.63 buy_ready=False sector_rank=8 price=14.58 support=14.02 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=8.73 liquidity=23826712.0 spike=0.62
- FAIT.CA: score=0.46 buy_ready=False sector_rank=8 price=42.86 support=38.48 resistance=47.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=28.64 liquidity=1831299.5 spike=0.62
- FAITA.CA: score=5.3 buy_ready=False sector_rank=8 price=0.98 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=68021.46 spike=2.3
- FERC.CA: score=-0.1 buy_ready=False sector_rank=15 price=69.94 support=66.72 resistance=82.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=23.08 liquidity=3499149.75 spike=0.62
- FWRY.CA: score=18.23 buy_ready=False sector_rank=2 price=18.46 support=17.5 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.93 liquidity=61035712.0 spike=0.54
- GBCO.CA: score=13.64 buy_ready=False sector_rank=7 price=30.25 support=27.0 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.25 liquidity=96086480.0 spike=0.93
- GDWA.CA: score=4.1 buy_ready=False sector_rank=18 price=0.62 support=0.6 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=17.27 liquidity=7701764.5 spike=0.37
- GGCC.CA: score=5.25 buy_ready=False sector_rank=18 price=0.64 support=0.61 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=21.97 liquidity=7846722.0 spike=0.61
- GIHD.CA: score=7.4 buy_ready=False sector_rank=18 price=55.39 support=53.3 resistance=78.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=26.04 liquidity=12337347.0 spike=0.63
- GMCI.CA: score=3.7 buy_ready=False sector_rank=18 price=1.61 support=1.49 resistance=1.82 source=Yahoo Finance as_of=2026-10-12T21:00:00+00:00 freshness=FRESH RSI=36.84 liquidity=298038.37 spike=0.7
- GRCA.CA: score=2.63 buy_ready=False sector_rank=18 price=32.68 support=30.51 resistance=46.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=28.64 liquidity=4226498.5 spike=0.3
- GSSC.CA: score=-1.98 buy_ready=False sector_rank=18 price=264.43 support=246.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.63 liquidity=617400.75 spike=0.19
- HDBK.CA: score=7.63 buy_ready=False sector_rank=8 price=102.76 support=98.01 resistance=121.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=26.44 liquidity=21117582.0 spike=0.78
- HELI.CA: score=7.4 buy_ready=False sector_rank=16 price=7.22 support=6.92 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.04 liquidity=43045332.0 spike=0.4
- HRHO.CA: score=16.33 buy_ready=False sector_rank=10 price=25.5 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.07 liquidity=42690628.0 spike=0.31
- ICID.CA: score=16.24 buy_ready=False sector_rank=18 price=17.9 support=16.52 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=54.6 liquidity=11027072.0 spike=1.42
- IDRE.CA: score=0.12 buy_ready=False sector_rank=18 price=43.62 support=40.05 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=27.17 liquidity=2722231.25 spike=0.18
- IFAP.CA: score=-1.54 buy_ready=False sector_rank=21 price=18.27 support=17.17 resistance=21.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=20.51 liquidity=2059678.75 spike=0.27
- INFI.CA: score=12.42 buy_ready=False sector_rank=18 price=117.46 support=104.0 resistance=142.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.12 liquidity=13521207.0 spike=1.01
- IRON.CA: score=11.07 buy_ready=False sector_rank=15 price=26.47 support=25.01 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=49.06 liquidity=7669578.5 spike=0.69
- ISMA.CA: score=3.12 buy_ready=False sector_rank=18 price=22.57 support=18.91 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=23.65 liquidity=5718968.0 spike=0.72
- ISMQ.CA: score=6.4 buy_ready=False sector_rank=15 price=7.51 support=7.14 resistance=9.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.18 liquidity=13327637.0 spike=0.68
- ISPH.CA: score=6.4 buy_ready=False sector_rank=14 price=11.13 support=10.03 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.95 liquidity=16895486.0 spike=0.28
- JUFO.CA: score=6.4 buy_ready=False sector_rank=13 price=24.27 support=23.5 resistance=27.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=23.47 liquidity=10733103.0 spike=0.62
- KABO.CA: score=5.51 buy_ready=False sector_rank=17 price=7.61 support=7.3 resistance=10.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=8109342.5 spike=0.3
- KWIN.CA: score=1.24 buy_ready=False sector_rank=18 price=67.68 support=60.0 resistance=93.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=22.64 liquidity=4839435.0 spike=0.5
- KZPC.CA: score=15.64 buy_ready=False sector_rank=18 price=13.12 support=12.15 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.33 liquidity=10989201.0 spike=1.12
- LCSW.CA: score=16.94 buy_ready=False sector_rank=11 price=33.88 support=28.86 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.16 liquidity=14000550.0 spike=0.7
- LUTS.CA: score=12.4 buy_ready=False sector_rank=18 price=0.77 support=0.65 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.78 liquidity=44805788.0 spike=0.7
- MAAL.CA: score=12.46 buy_ready=False sector_rank=18 price=9.03 support=8.45 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.7 liquidity=24549300.0 spike=1.03
- MASR.CA: score=12.4 buy_ready=False sector_rank=18 price=7.3 support=6.82 resistance=8.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.91 liquidity=33600220.0 spike=0.57
- MBSC.CA: score=14.94 buy_ready=False sector_rank=11 price=340.87 support=288.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.43 liquidity=31615258.0 spike=0.37
- MCQE.CA: score=11.94 buy_ready=False sector_rank=11 price=177.21 support=170.0 resistance=228.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.83 liquidity=47754392.0 spike=0.89
- MCRO.CA: score=7.4 buy_ready=False sector_rank=18 price=1.39 support=1.25 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=49131168.0 spike=0.74
- MENA.CA: score=-2.01 buy_ready=False sector_rank=16 price=6.02 support=5.72 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=28.21 liquidity=588684.81 spike=0.35
- MEPA.CA: score=-1.45 buy_ready=False sector_rank=18 price=1.64 support=1.57 resistance=1.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6154362.5 spike=0.6
- MFPC.CA: score=10.4 buy_ready=False sector_rank=15 price=44.0 support=42.0 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.36 liquidity=19091050.0 spike=0.21
- MFSC.CA: score=-2.19 buy_ready=False sector_rank=18 price=38.49 support=36.25 resistance=49.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=22.89 liquidity=413821.63 spike=0.17
- MHOT.CA: score=4.11 buy_ready=False sector_rank=12 price=15.94 support=15.08 resistance=19.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.11 liquidity=2188540.75 spike=0.12
- MILS.CA: score=2.16 buy_ready=False sector_rank=18 price=156.37 support=147.06 resistance=207.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.25 liquidity=4759599.0 spike=0.59
- MIPH.CA: score=-1.91 buy_ready=False sector_rank=14 price=790.87 support=666.66 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=30.18 liquidity=690998.0 spike=0.08
- MOED.CA: score=3.7 buy_ready=False sector_rank=18 price=0.61 support=0.57 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=28.14 liquidity=7295444.0 spike=0.36
- MOIL.CA: score=-0.74 buy_ready=False sector_rank=4 price=0.68 support=0.63 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=28.99 liquidity=165432.64 spike=0.57
- MOIN.CA: score=7.4 buy_ready=False sector_rank=18 price=31.99 support=31.0 resistance=39.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.49 liquidity=10068868.0 spike=0.8
- MOSC.CA: score=7.08 buy_ready=False sector_rank=18 price=270.89 support=243.15 resistance=286.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10906855.0 spike=3.34
- MPCI.CA: score=7.4 buy_ready=False sector_rank=18 price=315.64 support=294.2 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=23.99 liquidity=41608976.0 spike=0.39
- MPCO.CA: score=7.4 buy_ready=False sector_rank=21 price=2.13 support=2.0 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=15.96 liquidity=60781816.0 spike=0.43
- MPRC.CA: score=8.99 buy_ready=False sector_rank=18 price=37.04 support=34.53 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=40.83 liquidity=6585670.5 spike=0.39
- MTIE.CA: score=10.96 buy_ready=False sector_rank=7 price=7.82 support=7.27 resistance=8.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.48 liquidity=45101824.0 spike=2.66
- NAHO.CA: score=2.41 buy_ready=False sector_rank=18 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=46.15 liquidity=14681.78 spike=0.41
- NCCW.CA: score=7.4 buy_ready=False sector_rank=18 price=5.96 support=5.3 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.37 liquidity=18364814.0 spike=0.38
- NEDA.CA: score=-2.41 buy_ready=False sector_rank=18 price=2.6 support=2.47 resistance=2.8 source=Yahoo Finance as_of=2026-10-12T21:00:00+00:00 freshness=FRESH RSI=27.27 liquidity=192412.99 spike=0.28
- NHPS.CA: score=8.98 buy_ready=False sector_rank=18 price=66.13 support=63.02 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.24 liquidity=7578147.0 spike=0.53
- NINH.CA: score=6.48 buy_ready=False sector_rank=18 price=16.8 support=16.27 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=18.5 liquidity=9084026.0 spike=0.62
- NIPH.CA: score=7.4 buy_ready=False sector_rank=14 price=275.74 support=241.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.74 liquidity=112421968.0 spike=0.9
- OBRI.CA: score=10.91 buy_ready=False sector_rank=18 price=26.1 support=22.8 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.97 liquidity=7514127.5 spike=0.53
- OCDI.CA: score=7.4 buy_ready=False sector_rank=16 price=25.15 support=24.2 resistance=30.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.11 liquidity=28471774.0 spike=0.63
- OCPH.CA: score=-1.63 buy_ready=False sector_rank=18 price=204.74 support=190.0 resistance=251.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.14 liquidity=1972997.38 spike=0.53
- ODIN.CA: score=0.26 buy_ready=False sector_rank=18 price=2.26 support=2.11 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=22.12 liquidity=2862432.25 spike=0.32
- OFH.CA: score=7.4 buy_ready=False sector_rank=18 price=0.8 support=0.76 resistance=1.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.05 liquidity=27046222.0 spike=0.28
- OIH.CA: score=8.95 buy_ready=False sector_rank=6 price=1.81 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=24.64 liquidity=44256136.0 spike=0.48
- OLFI.CA: score=3.99 buy_ready=False sector_rank=13 price=20.83 support=19.8 resistance=23.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=7.03 liquidity=7588758.5 spike=0.42
- ORAS.CA: score=5.6 buy_ready=False sector_rank=3 price=906.61 support=882.75 resistance=925.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=432261824.0 spike=1.0
- ORHD.CA: score=6.4 buy_ready=False sector_rank=16 price=10.88 support=10.01 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=2.52 liquidity=112541608.0 spike=0.74
- ORWE.CA: score=17.4 buy_ready=False sector_rank=17 price=27.26 support=26.01 resistance=28.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.2 liquidity=33557896.0 spike=0.87
- PHAR.CA: score=12.4 buy_ready=False sector_rank=14 price=107.24 support=102.0 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.51 liquidity=30670174.0 spike=0.43
- PHDC.CA: score=14.4 buy_ready=False sector_rank=16 price=12.7 support=12.35 resistance=13.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.68 liquidity=84806144.0 spike=0.89
- PHTV.CA: score=3.88 buy_ready=False sector_rank=18 price=335.0 support=315.1 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=51.46 liquidity=1237349.0 spike=1.12
- POUL.CA: score=6.4 buy_ready=False sector_rank=13 price=9.68 support=9.12 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=1.91 liquidity=17392762.0 spike=0.52
- PRCL.CA: score=1.15 buy_ready=False sector_rank=11 price=22.87 support=21.63 resistance=22.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8205568.0 spike=0.73
- PRDC.CA: score=7.4 buy_ready=False sector_rank=16 price=6.35 support=6.07 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=33.41 liquidity=19847560.0 spike=0.56
- PRMH.CA: score=-1.87 buy_ready=False sector_rank=18 price=2.02 support=1.97 resistance=2.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5114437.0 spike=1.31
- RACC.CA: score=-1.44 buy_ready=False sector_rank=18 price=9.06 support=8.51 resistance=10.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.76 liquidity=2155521.25 spike=0.33
- RAKT.CA: score=4.62 buy_ready=False sector_rank=18 price=22.06 support=20.26 resistance=25.08 source=Yahoo Finance as_of=2026-10-12T21:00:00+00:00 freshness=FRESH RSI=49.81 liquidity=480885.93 spike=1.37
- RAYA.CA: score=6.44 buy_ready=False sector_rank=20 price=5.9 support=5.7 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=29.37 liquidity=36722736.0 spike=1.02
- RMDA.CA: score=7.4 buy_ready=False sector_rank=14 price=5.21 support=4.83 resistance=6.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.39 liquidity=22099456.0 spike=0.79
- ROTO.CA: score=10.97 buy_ready=False sector_rank=18 price=37.8 support=35.56 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.98 liquidity=6570665.5 spike=0.76
- RREI.CA: score=1.81 buy_ready=False sector_rank=18 price=3.6 support=3.29 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=25.79 liquidity=4413519.5 spike=0.46
- RTVC.CA: score=-2.54 buy_ready=False sector_rank=18 price=3.42 support=3.31 resistance=4.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=27.62 liquidity=1064774.25 spike=0.39
- RUBX.CA: score=19.4 buy_ready=False sector_rank=18 price=16.52 support=12.72 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.24 liquidity=69838328.0 spike=0.69
- SAUD.CA: score=0.68 buy_ready=False sector_rank=8 price=21.87 support=20.2 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.94 liquidity=2047179.13 spike=0.1
- SCEM.CA: score=16.94 buy_ready=False sector_rank=11 price=86.63 support=74.55 resistance=97.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.17 liquidity=39927384.0 spike=0.64
- SCFM.CA: score=-2.87 buy_ready=False sector_rank=18 price=234.79 support=220.35 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=27.94 liquidity=729058.0 spike=0.39
- SCTS.CA: score=0.72 buy_ready=False sector_rank=9 price=485.26 support=500.0 resistance=619.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=25.46 liquidity=1435657.5 spike=1.42
- SDTI.CA: score=17.4 buy_ready=False sector_rank=18 price=85.01 support=73.0 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=61.52 liquidity=14165346.0 spike=0.43
- SEIG.CA: score=-0.96 buy_ready=False sector_rank=18 price=197.67 support=173.1 resistance=267.0 source=Yahoo Finance as_of=2026-10-12T21:00:00+00:00 freshness=FRESH RSI=30.73 liquidity=1636707.58 spike=0.71
- SIPC.CA: score=4.5 buy_ready=False sector_rank=18 price=6.0 support=5.32 resistance=6.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=99508304.0 spike=2.05
- SKPC.CA: score=6.4 buy_ready=False sector_rank=15 price=15.26 support=14.98 resistance=18.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=16.48 liquidity=52210424.0 spike=0.62
- SMFR.CA: score=7.31 buy_ready=False sector_rank=18 price=199.1 support=181.6 resistance=255.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.32 liquidity=5053277.0 spike=1.43
- SNFC.CA: score=5.8 buy_ready=False sector_rank=18 price=11.24 support=10.8 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.86 liquidity=5395404.0 spike=0.47
- SPIN.CA: score=1.35 buy_ready=False sector_rank=17 price=15.06 support=14.94 resistance=18.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=25.53 liquidity=3950741.75 spike=0.67
- SPMD.CA: score=3.22 buy_ready=False sector_rank=18 price=0.35 support=0.34 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.14 liquidity=6820439.5 spike=0.1
- SUGR.CA: score=4.54 buy_ready=False sector_rank=13 price=54.65 support=50.5 resistance=62.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=29.69 liquidity=7139485.5 spike=0.64
- SVCE.CA: score=7.4 buy_ready=False sector_rank=18 price=9.26 support=8.81 resistance=12.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.54 liquidity=46552632.0 spike=0.54
- SWDY.CA: score=7.4 buy_ready=False sector_rank=19 price=113.73 support=102.31 resistance=128.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=33.64 liquidity=41505480.0 spike=0.68
- TALM.CA: score=20.44 buy_ready=False sector_rank=9 price=21.15 support=18.71 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.14 liquidity=11270577.0 spike=0.2
- TMGH.CA: score=6.4 buy_ready=False sector_rank=16 price=83.61 support=81.22 resistance=96.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=13.61 liquidity=205810672.0 spike=0.92
- TRTO.CA: score=4.4 buy_ready=False sector_rank=18 price=0.07 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-10-12T21:00:00+00:00 freshness=FRESH RSI=78.95 liquidity=3294.61 spike=0.33
- UEFM.CA: score=4.32 buy_ready=False sector_rank=18 price=476.42 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=52.92 liquidity=915075.75 spike=0.29
- UEGC.CA: score=8.4 buy_ready=False sector_rank=18 price=1.43 support=1.34 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=28.36 liquidity=17590168.0 spike=0.52
- UNIP.CA: score=0.86 buy_ready=False sector_rank=18 price=0.32 support=0.31 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.67 liquidity=4460344.5 spike=0.43
- UNIT.CA: score=-1.95 buy_ready=False sector_rank=16 price=16.9 support=16.15 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=34.17 liquidity=651676.31 spike=0.07
- WCDF.CA: score=-1.63 buy_ready=False sector_rank=18 price=546.9 support=515.0 resistance=721.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=25.45 liquidity=966982.56 spike=0.27
- WKOL.CA: score=0.21 buy_ready=False sector_rank=18 price=281.05 support=266.18 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=22.4 liquidity=3808206.5 spike=0.34
- ZEOT.CA: score=6.78 buy_ready=False sector_rank=18 price=11.11 support=10.31 resistance=11.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17970370.0 spike=3.19
- ZMID.CA: score=7.4 buy_ready=False sector_rank=16 price=7.15 support=6.83 resistance=9.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.44 liquidity=62746132.0 spike=0.6

## Backtesting Lite
- ETEL.CA: 180d return=117.72%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-10-12T21:00:00+00:00
- EFIH.CA: 180d return=20.23%, max drawdown=-22.68%, MA20>MA50 days last20=7, as_of=2026-10-12T21:00:00+00:00
- TALM.CA: 180d return=40.37%, max drawdown=-17.07%, MA20>MA50 days last20=20, as_of=2026-10-12T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- RUBX.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Rubex International for Plastic and Acrylic Manufacturing summary=Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- FWRY.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Fawry For Banking Technology and Electronic Payments summary=Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- ORWE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=651 sources=3 expected=Oriental Weavers summary=Oriental Weavers to disburse EGP 1.5/shr dividends for 2025; Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025; Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25
  - Oriental Weavers to disburse EGP 1.5/shr dividends for 2025: https://english.mubasher.info/news/4590236/Oriental-Weavers-to-disburse-EGP-1-5-shr-dividends-for-2025/
  - Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025: https://english.mubasher.info/news/4562972/Oriental-Weavers-consolidated-profits-cross-EGP-2-2bn-in-2025/
  - Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25: https://english.mubasher.info/news/4487417/Oriental-Weavers-generates-EGP-12-5bn-consolidated-sales-in-H1-25/
- SDTI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=SHARM DREAMS Co. for Touristic Investment S.A.E summary=Sharm Dreams stock maintains strong uptrend - Analysis; Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis; Sharm Dreams stock hits historic level halting driving buying force
  - Sharm Dreams stock maintains strong uptrend - Analysis: https://english.mubasher.info/news/4577977/Sharm-Dreams-stock-maintains-strong-uptrend-Analysis/
  - Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis: https://english.mubasher.info/news/4547831/Sharm-Dreams-stock-is-experiencing-sideways-movement-amid-anticipation-of-next-trend-Analysis/
  - Sharm Dreams stock hits historic level halting driving buying force: https://english.mubasher.info/news/4529096/Sharm-Dreams-stock-hits-historic-level-halting-driving-buying-force/

## Warnings
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- Evidence for ORWE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for SDTI.CA matches the company but no source/report date was detected.
