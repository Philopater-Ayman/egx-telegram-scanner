# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-10-15T10:20:35.935169+00:00
Generated Cairo: 2026-10-15 13:20
Run timing: target 08:45 Cairo | generated Cairo 2026-10-15 13:20 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-10-15 13:16

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 178/187
- Top sector: Telecommunications

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, October 15
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 15.79% / above MA50 21.05%
- EGX70 regime: BEARISH / above MA20 10.0% / above MA50 12.5%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=229297008.0 spike=0.43 score=7.37
- CCAP.CA: liquidity=220342928.0 spike=0.36 score=8.69
- UEGC.CA: liquidity=193333584.0 spike=5.69 score=7.4
- ETEL.CA: liquidity=148544640.0 spike=0.56 score=23.8
- TMGH.CA: liquidity=140730096.0 spike=0.62 score=6.4

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with weak breadth (sector breadth 0%), risk mode is DEFENSIVE_NO_NEW_BUY, so the scanner holds all tickets; the prioritized tickets show relative strength but face cooling liquidity, extended distance from support, and non‑leading sectors, giving only short‑term watch potential.
- EFIH.CA and ETEL.CA top the rank scores with BULLISH_WATCH outlook, yet liquidity is cooling and they sit only 4‑13% above 20‑day support in defensive telecom/fintech sectors.
- ACAMD.CA and SIPC.CA have CONSTRUCTIVE outlook but high liquidity spikes and prices far above 20‑day support (≈13‑37%), belonging to non‑leading sectors, limiting near‑term upside.
- ARAB.CA, SUGR.CA, ORWE.CA, RUBX.CA show lower scores, NEUTRAL/CONSTRUCTIVE outlooks, liquidity cooling or extended momentum, and are well above support, indicating limited short‑term gain.
- The bearish EGX30/EGX70 regime shifts risk mode to DEFENSIVE_NO_NEW_BUY, so even tickets with positive outlook are treated as HOLD/watch with uncertainty about near‑term direction.

## Top Liquidity Spikes
- UEGC.CA: spike=5.69 liquidity=193333584.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ZEOT.CA: spike=5.11 liquidity=32005026.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GGCC.CA: spike=3.87 liquidity=48034040.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CLHO.CA: spike=3.21 liquidity=124465136.0 outlook=WEAK_OR_RISKY score=23 buy_ready=False
- ELKA.CA: spike=2.24 liquidity=26113922.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=4.5 5d=-1.18% 20d=4.64% aboveMA50=50.0%
- #2 Fintech & Payments: score=2.34 5d=-2.77% 20d=-0.64% aboveMA50=50.0%
- #3 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #4 Transportation & Logistics: score=1.06 5d=-3.55% 20d=1.78% aboveMA50=50.0%
- #5 Education: score=-0.36 5d=-3.29% 20d=-7.64% aboveMA50=33.33%
- #6 Energy & Petrochemicals: score=-0.5 5d=-5.24% 20d=1.34% aboveMA50=33.33%
- #7 Investment Holding: score=-0.77 5d=-3.21% 20d=-8.02% aboveMA50=33.33%
- #8 Automotive & Distribution: score=-1.42 5d=-3.83% 20d=-2.92% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ETEL.CA: BULLISH_WATCH score=84.5 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- EFIH.CA: BULLISH_WATCH score=72.34 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- AMIA.CA: BULLISH_WATCH score=71 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- SUGR.CA: BULLISH_WATCH score=70 liquidity=TRADEABLE sector=LAGGING risk=sector is not leading
- ORWE.CA: BULLISH_WATCH score=70 liquidity=TRADEABLE sector=LAGGING risk=sector is not leading
- TALM.CA: BULLISH_WATCH score=70 liquidity=TRADEABLE sector=NEUTRAL risk=liquidity is cooling
- ACAMD.CA: CONSTRUCTIVE score=64 liquidity=TRADEABLE sector=LAGGING risk=momentum is extended; sector is not leading
- SIPC.CA: CONSTRUCTIVE score=60 liquidity=TRADEABLE sector=LAGGING risk=far above support; sector is not leading; high short-term volatility
- ALCN.CA: CONSTRUCTIVE score=59.06 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; below MA20
- AMOC.CA: CONSTRUCTIVE score=58 liquidity=TRADEABLE sector=NEUTRAL risk=liquidity is cooling; below MA20

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=-0.61 buy_ready=False sector_rank=19 price=233.19 support=225.0 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=24.7 liquidity=1989153.38 spike=0.1
- ABUK.CA: score=10.45 buy_ready=False sector_rank=16 price=85.17 support=83.0 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=32.15 liquidity=13210585.0 spike=0.14
- ACAMD.CA: score=21.4 buy_ready=False sector_rank=19 price=2.11 support=1.87 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=62.07 liquidity=41006772.0 spike=0.9
- ACGC.CA: score=3.62 buy_ready=False sector_rank=14 price=13.06 support=12.81 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=39.75 liquidity=988754.63 spike=0.08
- ADCI.CA: score=-1.92 buy_ready=False sector_rank=19 price=257.94 support=250.06 resistance=288.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=32.29 liquidity=683724.88 spike=0.33
- ADIB.CA: score=8.37 buy_ready=False sector_rank=10 price=47.36 support=43.5 resistance=54.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=30.8 liquidity=36441936.0 spike=0.46
- ADPC.CA: score=0.24 buy_ready=False sector_rank=19 price=3.18 support=3.01 resistance=4.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=20.45 liquidity=3843702.5 spike=0.26
- AFDI.CA: score=3.02 buy_ready=False sector_rank=19 price=49.89 support=46.12 resistance=56.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=43.15 liquidity=623196.31 spike=0.1
- AFMC.CA: score=4.01 buy_ready=False sector_rank=19 price=133.48 support=122.0 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=34.51 liquidity=6613667.5 spike=0.32
- AJWA.CA: score=16.4 buy_ready=False sector_rank=19 price=223.57 support=176.0 resistance=222.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=88.63 liquidity=16986916.0 spike=0.6
- ALCN.CA: score=11.6 buy_ready=False sector_rank=4 price=33.19 support=30.55 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=44.75 liquidity=4174191.75 spike=0.12
- ALUM.CA: score=-1.07 buy_ready=False sector_rank=19 price=21.01 support=20.52 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=26.87 liquidity=2525887.0 spike=0.55
- AMER.CA: score=14.4 buy_ready=False sector_rank=17 price=4.69 support=4.05 resistance=5.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=23830538.0 spike=0.48
- AMES.CA: score=8.4 buy_ready=False sector_rank=19 price=39.52 support=38.02 resistance=59.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=23559788.0 spike=0.25
- AMIA.CA: score=11.73 buy_ready=False sector_rank=19 price=18.87 support=17.12 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=51.65 liquidity=4332007.5 spike=0.24
- AMOC.CA: score=16.8 buy_ready=False sector_rank=6 price=13.42 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=52.03 liquidity=39693384.0 spike=0.31
- APSW.CA: score=1.58 buy_ready=False sector_rank=19 price=7.91 support=7.81 resistance=8.92 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=39.15 liquidity=183875.86 spike=0.28
- ARAB.CA: score=19.4 buy_ready=False sector_rank=17 price=0.27 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=64.91 liquidity=38313568.0 spike=0.39
- ARCC.CA: score=9.92 buy_ready=False sector_rank=13 price=66.59 support=60.01 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=47.31 liquidity=7208999.5 spike=0.23
- AREH.CA: score=3.47 buy_ready=False sector_rank=19 price=1.2 support=1.11 resistance=1.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=29.63 liquidity=7073085.0 spike=0.85
- ASCM.CA: score=-0.63 buy_ready=False sector_rank=19 price=50.5 support=48.0 resistance=61.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=30.22 liquidity=2968406.0 spike=0.35
- ASPI.CA: score=3.0 buy_ready=False sector_rank=19 price=0.33 support=0.31 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=27.32 liquidity=6598557.0 spike=0.2
- ATLC.CA: score=0.36 buy_ready=False sector_rank=12 price=5.47 support=5.2 resistance=7.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=33.96 liquidity=2427525.5 spike=0.25
- ATQA.CA: score=12.45 buy_ready=False sector_rank=16 price=11.74 support=10.61 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=37.75 liquidity=15205700.0 spike=0.21
- AXPH.CA: score=-0.32 buy_ready=False sector_rank=19 price=1387.6 support=1300.0 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=24.72 liquidity=2277378.75 spike=0.33
- BINV.CA: score=9.43 buy_ready=False sector_rank=7 price=59.06 support=50.0 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=64.99 liquidity=740233.25 spike=0.03
- BIOC.CA: score=16.4 buy_ready=False sector_rank=19 price=299.46 support=225.21 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=59.39 liquidity=21367578.0 spike=0.2
- BTFH.CA: score=6.97 buy_ready=False sector_rank=12 price=2.76 support=2.55 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=34.85 liquidity=102415000.0 spike=1.02
- CAED.CA: score=4.93 buy_ready=False sector_rank=19 price=105.53 support=95.0 resistance=136.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=37.43 liquidity=2531678.75 spike=0.29
- CANA.CA: score=7.74 buy_ready=False sector_rank=10 price=43.66 support=41.7 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=41.51 liquidity=1376786.75 spike=0.06
- CCAP.CA: score=8.69 buy_ready=False sector_rank=7 price=6.15 support=6.07 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=24.86 liquidity=220342928.0 spike=0.36
- CCRS.CA: score=-0.67 buy_ready=False sector_rank=19 price=2.05 support=1.87 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=18.42 liquidity=1934065.25 spike=0.16
- CEFM.CA: score=2.78 buy_ready=False sector_rank=19 price=126.35 support=113.0 resistance=152.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=35.75 liquidity=378857.88 spike=0.14
- CERA.CA: score=12.4 buy_ready=False sector_rank=19 price=1.28 support=1.18 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=46.84 liquidity=120704360.0 spike=0.99
- CFGH.CA: score=-3.6 buy_ready=False sector_rank=19 price=0.1 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=2652.3 spike=0.46
- CICH.CA: score=-1.22 buy_ready=False sector_rank=12 price=11.01 support=10.6 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=29.55 liquidity=848195.81 spike=0.24
- CIEB.CA: score=2.42 buy_ready=False sector_rank=10 price=22.94 support=22.56 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=30.26 liquidity=5051949.5 spike=0.52
- CIRA.CA: score=11.45 buy_ready=False sector_rank=5 price=37.04 support=35.51 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=40.69 liquidity=7595598.5 spike=0.32
- CLHO.CA: score=10.9 buy_ready=False sector_rank=15 price=14.15 support=13.86 resistance=16.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=25.89 liquidity=124465136.0 spike=3.21
- CNFN.CA: score=7.78 buy_ready=False sector_rank=12 price=4.08 support=3.8 resistance=4.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=36.13 liquidity=5852236.0 spike=0.67
- COMI.CA: score=7.37 buy_ready=False sector_rank=10 price=123.77 support=120.0 resistance=134.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=24.92 liquidity=229297008.0 spike=0.43
- COPR.CA: score=7.95 buy_ready=False sector_rank=19 price=0.47 support=0.44 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=42.03 liquidity=5553153.5 spike=0.24
- COSG.CA: score=4.31 buy_ready=False sector_rank=19 price=1.46 support=1.34 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=30.16 liquidity=7905230.0 spike=0.53
- CPCI.CA: score=7.23 buy_ready=False sector_rank=19 price=604.41 support=531.02 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=75.91 liquidity=831124.44 spike=0.2
- CSAG.CA: score=9.78 buy_ready=False sector_rank=4 price=36.37 support=34.06 resistance=39.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=40.41 liquidity=5353385.5 spike=0.71
- DAPH.CA: score=12.4 buy_ready=False sector_rank=19 price=95.06 support=89.1 resistance=129.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=37.77 liquidity=20264272.0 spike=0.5
- DEIN.CA: score=5.4 buy_ready=False sector_rank=19 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 09:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37.26 spike=0.01
- DOMT.CA: score=-2.56 buy_ready=False sector_rank=11 price=23.51 support=22.85 resistance=27.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=27.6 liquidity=404845.25 spike=0.09
- DSCW.CA: score=1.88 buy_ready=False sector_rank=19 price=1.6 support=1.55 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=28.95 liquidity=5481759.0 spike=0.31
- DTPP.CA: score=2.4 buy_ready=False sector_rank=19 price=258.6 support=246.6 resistance=264.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=50857224.0 spike=0.69
- EALR.CA: score=-2.11 buy_ready=False sector_rank=19 price=305.93 support=290.17 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=25.33 liquidity=1488228.88 spike=0.16
- EASB.CA: score=3.77 buy_ready=False sector_rank=19 price=7.05 support=6.04 resistance=8.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=36.5 liquidity=1368485.63 spike=0.23
- EAST.CA: score=7.04 buy_ready=False sector_rank=11 price=29.0 support=27.01 resistance=33.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=20.59 liquidity=41013784.0 spike=0.89
- EBSC.CA: score=-1.88 buy_ready=False sector_rank=19 price=1.64 support=1.5 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=29.63 liquidity=1720667.5 spike=0.75
- ECAP.CA: score=-2.6 buy_ready=False sector_rank=19 price=28.93 support=27.5 resistance=32.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=23.9 liquidity=1001451.38 spike=0.24
- EDFM.CA: score=2.78 buy_ready=False sector_rank=19 price=385.56 support=335.2 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=50.14 liquidity=376315.41 spike=0.33
- EEII.CA: score=-2.12 buy_ready=False sector_rank=19 price=1.93 support=1.83 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=1479746.75 spike=0.16
- EFIC.CA: score=3.43 buy_ready=False sector_rank=16 price=155.57 support=147.0 resistance=199.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=26.89 liquidity=6977424.0 spike=0.2
- EFID.CA: score=9.04 buy_ready=False sector_rank=11 price=18.68 support=18.07 resistance=31.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=32.98 liquidity=18145020.0 spike=0.38
- EFIH.CA: score=23.94 buy_ready=False sector_rank=2 price=24.27 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=53.64 liquidity=20514418.0 spike=0.3
- EGAL.CA: score=8.97 buy_ready=False sector_rank=16 price=305.15 support=306.1 resistance=376.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=16.96 liquidity=96546832.0 spike=1.76
- EGAS.CA: score=6.3 buy_ready=False sector_rank=6 price=52.48 support=48.08 resistance=60.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=36.26 liquidity=2504935.25 spike=0.22
- EGBE.CA: score=3.43 buy_ready=False sector_rank=10 price=0.51 support=0.5 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=45.57 liquidity=61557.11 spike=0.47
- EGCH.CA: score=6.45 buy_ready=False sector_rank=16 price=12.02 support=11.86 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=24.18 liquidity=24978682.0 spike=0.31
- EGSA.CA: score=8.81 buy_ready=False sector_rank=1 price=8.84 support=8.82 resistance=9.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=6185.77 spike=0.83
- EGTS.CA: score=2.65 buy_ready=False sector_rank=17 price=13.97 support=13.56 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=18.84 liquidity=5248768.0 spike=0.15
- EHDR.CA: score=2.49 buy_ready=False sector_rank=19 price=2.31 support=2.1 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=27.03 liquidity=6094837.0 spike=0.54
- ELEC.CA: score=6.4 buy_ready=False sector_rank=18 price=1.72 support=1.65 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=27.78 liquidity=17774300.0 spike=0.33
- ELKA.CA: score=4.88 buy_ready=False sector_rank=19 price=1.63 support=1.5 resistance=1.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26113922.0 spike=2.24
- ELNA.CA: score=4.61 buy_ready=False sector_rank=19 price=35.22 support=33.46 resistance=36.4 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=229528.75 spike=1.49
- ELSH.CA: score=7.4 buy_ready=False sector_rank=19 price=11.3 support=10.76 resistance=13.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=30.9 liquidity=13575232.0 spike=0.66
- ELWA.CA: score=6.43 buy_ready=False sector_rank=19 price=1.65 support=1.43 resistance=1.75 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=45.45 liquidity=30036.6 spike=0.06
- EMFD.CA: score=7.4 buy_ready=False sector_rank=17 price=11.98 support=11.7 resistance=14.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=16001714.0 spike=0.24
- ENGC.CA: score=1.27 buy_ready=False sector_rank=19 price=33.95 support=32.37 resistance=45.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=25.39 liquidity=4873623.0 spike=0.27
- EOSB.CA: score=7.4 buy_ready=False sector_rank=19 price=1.57 support=1.64 resistance=1.64 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=157.0 spike=0.0
- EPCO.CA: score=-2.96 buy_ready=False sector_rank=19 price=8.93 support=8.0 resistance=11.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=25.56 liquidity=637184.44 spike=0.12
- EPPK.CA: score=-7.18 buy_ready=False sector_rank=19 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=23.8 buy_ready=False sector_rank=1 price=145.53 support=128.52 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=58.33 liquidity=148544640.0 spike=0.56
- ETRS.CA: score=3.56 buy_ready=False sector_rank=19 price=10.45 support=9.82 resistance=11.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=47.76 liquidity=1161734.0 spike=0.11
- EXPA.CA: score=7.37 buy_ready=False sector_rank=10 price=14.45 support=14.02 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=9.23 liquidity=13185785.0 spike=0.35
- FAIT.CA: score=2.96 buy_ready=False sector_rank=10 price=44.01 support=38.48 resistance=47.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=32.45 liquidity=1591219.63 spike=0.53
- FAITA.CA: score=3.68 buy_ready=False sector_rank=10 price=0.98 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=45.9 liquidity=53206.1 spike=1.63
- FERC.CA: score=-2.55 buy_ready=False sector_rank=16 price=70.27 support=66.72 resistance=82.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=25.03 liquidity=1001218.44 spike=0.18
- FWRY.CA: score=15.94 buy_ready=False sector_rank=2 price=18.49 support=17.5 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=42.09 liquidity=53157348.0 spike=0.47
- GBCO.CA: score=13.43 buy_ready=False sector_rank=8 price=30.35 support=27.0 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=44.58 liquidity=54019424.0 spike=0.51
- GDWA.CA: score=1.72 buy_ready=False sector_rank=19 price=0.63 support=0.6 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=22.94 liquidity=5320987.0 spike=0.26
- GGCC.CA: score=7.4 buy_ready=False sector_rank=19 price=0.7 support=0.63 resistance=0.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48034040.0 spike=3.87
- GIHD.CA: score=2.03 buy_ready=False sector_rank=19 price=54.88 support=53.3 resistance=78.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=22.82 liquidity=4633025.5 spike=0.24
- GMCI.CA: score=3.75 buy_ready=False sector_rank=19 price=1.54 support=1.49 resistance=1.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=40.38 liquidity=348787.56 spike=0.84
- GRCA.CA: score=1.1 buy_ready=False sector_rank=19 price=33.02 support=30.51 resistance=46.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=28.85 liquidity=2695948.25 spike=0.21
- GSSC.CA: score=-1.03 buy_ready=False sector_rank=19 price=270.08 support=246.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=34.66 liquidity=1574948.25 spike=0.51
- GTWL.CA: score=7.4 buy_ready=False sector_rank=19 price=131.45 support=116.16 resistance=241.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=21.24 liquidity=95247584.0 spike=0.6
- HDBK.CA: score=6.17 buy_ready=False sector_rank=10 price=101.85 support=98.01 resistance=121.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=31.61 liquidity=8802768.0 spike=0.33
- HELI.CA: score=7.4 buy_ready=False sector_rank=17 price=7.21 support=6.92 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=30.98 liquidity=17269362.0 spike=0.17
- HRHO.CA: score=15.93 buy_ready=False sector_rank=12 price=25.7 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=58.06 liquidity=38710612.0 spike=0.29
- ICID.CA: score=5.77 buy_ready=False sector_rank=19 price=17.5 support=16.52 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=59.11 liquidity=373533.03 spike=0.05
- IDRE.CA: score=-0.87 buy_ready=False sector_rank=19 price=42.87 support=40.05 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=32.67 liquidity=1732250.5 spike=0.13
- IFAP.CA: score=-0.64 buy_ready=False sector_rank=20 price=18.11 support=17.17 resistance=21.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=23.77 liquidity=2958757.25 spike=0.42
- INFI.CA: score=4.8 buy_ready=False sector_rank=19 price=125.32 support=111.25 resistance=127.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29279782.0 spike=2.2
- IRON.CA: score=12.44 buy_ready=False sector_rank=16 price=27.03 support=25.01 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=44.3 liquidity=8990902.0 spike=0.83
- ISMA.CA: score=-0.99 buy_ready=False sector_rank=19 price=22.6 support=18.91 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=28.72 liquidity=1611550.5 spike=0.21
- ISMQ.CA: score=-0.07 buy_ready=False sector_rank=16 price=7.59 support=7.14 resistance=9.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=32.26 liquidity=3478249.0 spike=0.18
- ISPH.CA: score=6.48 buy_ready=False sector_rank=15 price=11.15 support=10.03 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=34.03 liquidity=14223886.0 spike=0.24
- JUFO.CA: score=0.21 buy_ready=False sector_rank=11 price=24.26 support=23.5 resistance=27.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=28.95 liquidity=3167158.25 spike=0.19
- KABO.CA: score=-0.07 buy_ready=False sector_rank=14 price=7.58 support=7.3 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=34.35 liquidity=2297020.75 spike=0.09
- KWIN.CA: score=-1.63 buy_ready=False sector_rank=19 price=66.49 support=60.0 resistance=93.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=19.32 liquidity=1967948.38 spike=0.21
- KZPC.CA: score=7.2 buy_ready=False sector_rank=19 price=13.06 support=12.15 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=41.76 liquidity=1799509.13 spike=0.19
- LCSW.CA: score=12.16 buy_ready=False sector_rank=13 price=33.53 support=28.86 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=56.59 liquidity=5451646.0 spike=0.28
- LUTS.CA: score=12.4 buy_ready=False sector_rank=19 price=0.76 support=0.65 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=40.26 liquidity=27590474.0 spike=0.46
- MAAL.CA: score=8.61 buy_ready=False sector_rank=19 price=8.8 support=8.45 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=38.04 liquidity=6213315.5 spike=0.25
- MASR.CA: score=12.4 buy_ready=False sector_rank=19 price=7.35 support=6.82 resistance=7.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=44.57 liquidity=23116252.0 spike=0.41
- MBSC.CA: score=14.71 buy_ready=False sector_rank=13 price=339.94 support=288.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=49.92 liquidity=27249598.0 spike=0.32
- MCQE.CA: score=11.71 buy_ready=False sector_rank=13 price=173.46 support=170.0 resistance=228.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=39.19 liquidity=30226128.0 spike=0.55
- MCRO.CA: score=7.4 buy_ready=False sector_rank=19 price=1.4 support=1.25 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=25710660.0 spike=0.44
- MENA.CA: score=-0.8 buy_ready=False sector_rank=17 price=6.05 support=5.57 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=34.83 liquidity=1721049.75 spike=1.04
- MEPA.CA: score=4.23 buy_ready=False sector_rank=19 price=1.62 support=1.53 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=2831144.0 spike=0.29
- MFPC.CA: score=15.45 buy_ready=False sector_rank=16 price=43.72 support=42.0 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=36.16 liquidity=15438945.0 spike=0.17
- MFSC.CA: score=-2.19 buy_ready=False sector_rank=19 price=38.49 support=36.25 resistance=49.37 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=17.38 liquidity=412035.47 spike=0.18
- MHOT.CA: score=0.24 buy_ready=False sector_rank=9 price=15.8 support=15.08 resistance=19.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=33.08 liquidity=2822521.0 spike=0.16
- MICH.CA: score=4.26 buy_ready=False sector_rank=19 price=41.32 support=38.91 resistance=47.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=44.71 liquidity=1857351.5 spike=0.21
- MILS.CA: score=0.7 buy_ready=False sector_rank=19 price=156.08 support=147.06 resistance=207.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=26.66 liquidity=3302545.0 spike=0.41
- MIPH.CA: score=3.41 buy_ready=False sector_rank=15 price=792.94 support=666.66 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=40.54 liquidity=924866.38 spike=0.11
- MOED.CA: score=0.17 buy_ready=False sector_rank=19 price=0.61 support=0.57 resistance=0.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=31.09 liquidity=3769761.0 spike=0.21
- MOIL.CA: score=-1.19 buy_ready=False sector_rank=6 price=0.68 support=0.63 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=34.67 liquidity=7147.71 spike=0.02
- MOIN.CA: score=-0.54 buy_ready=False sector_rank=19 price=31.64 support=31.0 resistance=38.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=34.61 liquidity=2057656.25 spike=0.2
- MOSC.CA: score=6.1 buy_ready=False sector_rank=19 price=266.03 support=231.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=38.82 liquidity=3697306.25 spike=0.98
- MPCI.CA: score=7.4 buy_ready=False sector_rank=19 price=315.17 support=294.2 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=27.56 liquidity=16219106.0 spike=0.16
- MPCO.CA: score=7.4 buy_ready=False sector_rank=20 price=2.09 support=2.0 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=20.24 liquidity=30555924.0 spike=0.23
- MPRC.CA: score=5.31 buy_ready=False sector_rank=19 price=36.02 support=34.53 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=39.67 liquidity=2909198.75 spike=0.18
- MTIE.CA: score=10.11 buy_ready=False sector_rank=8 price=7.69 support=7.27 resistance=8.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=40.7 liquidity=7681947.5 spike=0.42
- NAHO.CA: score=2.41 buy_ready=False sector_rank=19 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=61.9 liquidity=12042.57 spike=0.41
- NCCW.CA: score=7.4 buy_ready=False sector_rank=19 price=5.91 support=5.3 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=27.82 liquidity=11206132.0 spike=0.26
- NEDA.CA: score=-2.55 buy_ready=False sector_rank=19 price=2.6 support=2.47 resistance=2.8 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=27.27 liquidity=51441.0 spike=0.08
- NHPS.CA: score=2.11 buy_ready=False sector_rank=19 price=65.89 support=63.02 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=26.15 liquidity=5705485.5 spike=0.4
- NINH.CA: score=7.4 buy_ready=False sector_rank=19 price=16.52 support=16.02 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=21.33 liquidity=13729695.0 spike=0.96
- NIPH.CA: score=7.48 buy_ready=False sector_rank=15 price=272.17 support=241.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=19524802.0 spike=0.16
- OBRI.CA: score=11.72 buy_ready=False sector_rank=19 price=26.98 support=22.8 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=40.7 liquidity=8323146.0 spike=0.6
- OCDI.CA: score=7.4 buy_ready=False sector_rank=17 price=25.5 support=24.2 resistance=30.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=32.64 liquidity=15238955.0 spike=0.35
- OCPH.CA: score=-1.58 buy_ready=False sector_rank=19 price=199.95 support=190.0 resistance=251.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=34.19 liquidity=2019141.63 spike=0.57
- ODIN.CA: score=1.1 buy_ready=False sector_rank=19 price=2.26 support=2.11 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=27.93 liquidity=3700276.5 spike=0.43
- OFH.CA: score=4.63 buy_ready=False sector_rank=19 price=0.8 support=0.76 resistance=1.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=25.96 liquidity=7229035.0 spike=0.08
- OIH.CA: score=5.31 buy_ready=False sector_rank=7 price=1.79 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=23.53 liquidity=6615167.5 spike=0.08
- OLFI.CA: score=-0.68 buy_ready=False sector_rank=11 price=20.7 support=19.8 resistance=23.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=24.12 liquidity=2277243.75 spike=0.13
- ORAS.CA: score=5.6 buy_ready=False sector_rank=3 price=895.74 support=891.15 resistance=914.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=65250752.0 spike=1.0
- ORHD.CA: score=6.4 buy_ready=False sector_rank=17 price=10.83 support=10.01 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=3.34 liquidity=43306064.0 spike=0.28
- ORWE.CA: score=17.91 buy_ready=False sector_rank=14 price=27.6 support=26.01 resistance=28.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=45006852.0 spike=1.14
- PHAR.CA: score=11.58 buy_ready=False sector_rank=15 price=106.84 support=102.0 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=40.86 liquidity=9097380.0 spike=0.13
- PHDC.CA: score=9.4 buy_ready=False sector_rank=17 price=12.9 support=12.35 resistance=13.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=34.5 liquidity=62120752.0 spike=0.66
- PHTV.CA: score=4.19 buy_ready=False sector_rank=19 price=335.0 support=315.0 resistance=378.89 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=48.45 liquidity=1252565.0 spike=1.27
- POUL.CA: score=7.04 buy_ready=False sector_rank=11 price=9.94 support=9.12 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=2.43 liquidity=18266478.0 spike=0.54
- PRCL.CA: score=-1.49 buy_ready=False sector_rank=13 price=22.36 support=21.0 resistance=33.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=26.9 liquidity=1794380.13 spike=0.16
- PRDC.CA: score=12.4 buy_ready=False sector_rank=17 price=6.5 support=6.07 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=37.71 liquidity=13715356.0 spike=0.38
- PRMH.CA: score=-1.39 buy_ready=False sector_rank=19 price=2.03 support=1.8 resistance=2.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=25.22 liquidity=2213035.5 spike=0.55
- RACC.CA: score=7.74 buy_ready=False sector_rank=19 price=9.1 support=8.51 resistance=10.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=39.34 liquidity=6344127.0 spike=1.0
- RAKT.CA: score=3.52 buy_ready=False sector_rank=19 price=22.06 support=20.26 resistance=25.08 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=49.81 liquidity=120822.62 spike=0.35
- RAYA.CA: score=6.4 buy_ready=False sector_rank=21 price=6.0 support=5.7 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=28.03 liquidity=11428046.0 spike=0.31
- RMDA.CA: score=6.2 buy_ready=False sector_rank=15 price=5.2 support=4.83 resistance=6.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=8711331.0 spike=0.33
- ROTO.CA: score=4.35 buy_ready=False sector_rank=19 price=37.5 support=35.56 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=37.96 liquidity=1953064.5 spike=0.22
- RREI.CA: score=1.02 buy_ready=False sector_rank=19 price=3.58 support=3.29 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=34.76 liquidity=3624596.25 spike=0.39
- RTVC.CA: score=-2.79 buy_ready=False sector_rank=19 price=3.44 support=3.31 resistance=4.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=31.07 liquidity=808415.5 spike=0.29
- RUBX.CA: score=17.4 buy_ready=False sector_rank=19 price=16.42 support=12.9 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=48.47 liquidity=23580562.0 spike=0.23
- SAUD.CA: score=9.27 buy_ready=False sector_rank=10 price=22.35 support=20.2 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=32.01 liquidity=27420096.0 spike=1.45
- SCEM.CA: score=16.71 buy_ready=False sector_rank=13 price=87.71 support=74.55 resistance=96.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=53.53 liquidity=23987386.0 spike=0.38
- SCFM.CA: score=-3.14 buy_ready=False sector_rank=19 price=232.34 support=220.35 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=31.34 liquidity=462443.13 spike=0.25
- SCTS.CA: score=1.14 buy_ready=False sector_rank=5 price=485.26 support=463.13 resistance=616.97 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=20.97 liquidity=1427634.95 spike=1.43
- SDTI.CA: score=15.4 buy_ready=False sector_rank=19 price=86.47 support=73.02 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=66.01 liquidity=10601890.0 spike=0.32
- SEIG.CA: score=-1.81 buy_ready=False sector_rank=19 price=194.51 support=173.1 resistance=267.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=33.48 liquidity=788955.31 spike=0.35
- SIPC.CA: score=20.04 buy_ready=False sector_rank=19 price=5.78 support=4.22 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=57.62 liquidity=68460056.0 spike=1.32
- SKPC.CA: score=6.45 buy_ready=False sector_rank=16 price=15.18 support=14.98 resistance=18.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=22.06 liquidity=26274956.0 spike=0.32
- SMFR.CA: score=3.35 buy_ready=False sector_rank=19 price=199.61 support=181.6 resistance=255.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=35.69 liquidity=1953600.0 spike=0.54
- SNFC.CA: score=8.73 buy_ready=False sector_rank=19 price=11.11 support=10.81 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=40.51 liquidity=3327796.0 spike=0.29
- SPIN.CA: score=1.39 buy_ready=False sector_rank=14 price=15.0 support=14.94 resistance=18.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=28.13 liquidity=3759538.25 spike=0.68
- SPMD.CA: score=2.4 buy_ready=False sector_rank=19 price=0.37 support=0.34 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18250880.0 spike=0.48
- SUGR.CA: score=18.4 buy_ready=False sector_rank=11 price=57.12 support=50.5 resistance=61.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=40.55 liquidity=12163043.0 spike=1.18
- SVCE.CA: score=7.4 buy_ready=False sector_rank=19 price=9.34 support=8.81 resistance=12.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=30.27 liquidity=24002540.0 spike=0.29
- SWDY.CA: score=12.4 buy_ready=False sector_rank=18 price=113.64 support=102.31 resistance=128.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=18749860.0 spike=0.31
- TALM.CA: score=15.62 buy_ready=False sector_rank=5 price=21.06 support=18.71 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=52.86 liquidity=6765720.5 spike=0.16
- TMGH.CA: score=6.4 buy_ready=False sector_rank=17 price=84.48 support=81.22 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=15.12 liquidity=140730096.0 spike=0.62
- TRTO.CA: score=4.4 buy_ready=False sector_rank=19 price=0.07 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=88.24 liquidity=4962.82 spike=0.51
- UEFM.CA: score=4.31 buy_ready=False sector_rank=19 price=476.42 support=407.57 resistance=550.0 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=49.89 liquidity=911867.91 spike=0.29
- UEGC.CA: score=7.4 buy_ready=False sector_rank=19 price=1.7 support=1.5 resistance=1.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=193333584.0 spike=5.69
- UNIP.CA: score=4.04 buy_ready=False sector_rank=19 price=0.33 support=0.31 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=34.0 liquidity=6636497.5 spike=0.68
- UNIT.CA: score=4.8 buy_ready=False sector_rank=17 price=17.4 support=16.15 resistance=20.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=38.75 liquidity=2402606.5 spike=0.36
- WCDF.CA: score=-1.49 buy_ready=False sector_rank=19 price=545.27 support=515.0 resistance=720.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=21.47 liquidity=1110334.5 spike=0.34
- WKOL.CA: score=-1.82 buy_ready=False sector_rank=19 price=277.15 support=266.18 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=27.19 liquidity=1782069.63 spike=0.16
- ZEOT.CA: score=7.4 buy_ready=False sector_rank=19 price=11.82 support=10.61 resistance=12.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32005026.0 spike=5.11
- ZMID.CA: score=7.4 buy_ready=False sector_rank=17 price=7.24 support=6.83 resistance=9.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=18.48 liquidity=50423248.0 spike=0.5

## Backtesting Lite
- EFIH.CA: 180d return=22.52%, max drawdown=-22.68%, MA20>MA50 days last20=6, as_of=2026-10-13T21:00:00+00:00
- ETEL.CA: 180d return=115.84%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-10-13T21:00:00+00:00
- ACAMD.CA: 180d return=27.97%, max drawdown=-26.43%, MA20>MA50 days last20=0, as_of=2026-10-13T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- ACAMD.CA: status=OLD_ACCEPTED latest=2020-01-01 age_days=2479 sources=3 expected=Arab Co.,for asset management and development summary=Arab Company for Asset Management shifts to EGP 7m net profits in 9M-25; Arab Co. for Asset Management approves offer to sell land in El-Minya; Arab Co. Asset Management swings to loss in 2020
  - Arab Company for Asset Management shifts to EGP 7m net profits in 9M-25: https://english.mubasher.info/news/4543171/Arab-Company-for-Asset-Management-shifts-to-EGP-7m-net-profits-in-9M-25/
  - Arab Co. for Asset Management approves offer to sell land in El-Minya: https://english.mubasher.info/news/3777445/Arab-Co-for-Asset-Management-approves-offer-to-sell-land-in-El-Minya/
  - Arab Co. Asset Management swings to loss in 2020: https://english.mubasher.info/news/3767136/Arab-Co-Asset-Management-swings-to-loss-in-2020/
- SIPC.CA: status=OLD_ACCEPTED latest=2020-01-01 age_days=2479 sources=3 expected=Sabaa International Company for Pharmaceutical and Chemical Industry summary=Sabaa Pharmaceutical&#39;s shareholders approve capital raise via bonus issue; FRA approves Sabaa Pharmaceutical&#39;s capital raise; Sabaa Pharmaceutical&#39;s profit leaps 76% in 2020 initial results
  - Sabaa Pharmaceutical&#39;s shareholders approve capital raise via bonus issue: https://english.mubasher.info/news/3809286/Sabaa-Pharmaceutical-s-shareholders-approve-capital-raise-via-bonus-issue/
  - FRA approves Sabaa Pharmaceutical&#39;s capital raise: https://english.mubasher.info/news/3789753/FRA-approves-Sabaa-Pharmaceutical-s-capital-raise/
  - Sabaa Pharmaceutical&#39;s profit leaps 76% in 2020 initial results: https://english.mubasher.info/news/3779465/Sabaa-Pharmaceutical-s-profit-leaps-76-in-2020-initial-results/
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- SUGR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=652 sources=3 expected=Delta Sugar summary=Delta Sugar’s net profits fall 74% in Q1-26; Delta Sugar stock tests key resistance near EGP 50 amid downtrend; Delta Sugar turns to EGP 346m net losses in 2025
  - Delta Sugar’s net profits fall 74% in Q1-26: https://english.mubasher.info/news/4604921/Delta-Sugar-s-net-profits-fall-74-in-Q1-26/
  - Delta Sugar stock tests key resistance near EGP 50 amid downtrend: https://english.mubasher.info/news/4584932/Delta-Sugar-stock-tests-key-resistance-near-EGP-50-amid-downtrend/
  - Delta Sugar turns to EGP 346m net losses in 2025: https://english.mubasher.info/news/4557875/Delta-Sugar-turns-to-EGP-346m-net-losses-in-2025/
- ORWE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=652 sources=3 expected=Oriental Weavers summary=Oriental Weavers to disburse EGP 1.5/shr dividends for 2025; Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025; Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25
  - Oriental Weavers to disburse EGP 1.5/shr dividends for 2025: https://english.mubasher.info/news/4590236/Oriental-Weavers-to-disburse-EGP-1-5-shr-dividends-for-2025/
  - Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025: https://english.mubasher.info/news/4562972/Oriental-Weavers-consolidated-profits-cross-EGP-2-2bn-in-2025/
  - Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25: https://english.mubasher.info/news/4487417/Oriental-Weavers-generates-EGP-12-5bn-consolidated-sales-in-H1-25/
- RUBX.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Rubex International for Plastic and Acrylic Manufacturing summary=Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.

## Warnings
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for ACAMD.CA matches the company but appears old; latest detected date is 2020-01-01.
- Evidence for SIPC.CA matches the company but appears old; latest detected date is 2020-01-01.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence for SUGR.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ORWE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
