# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-10-27T10:59:57.215468+00:00
Generated Cairo: 2026-10-27 13:59
Run timing: target 08:45 Cairo | generated Cairo 2026-10-27 13:59 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-10-27 13:56

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 5
- Tradeable price/liquidity tickers: 90/185
- Top sector: Telecommunications

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, October 27
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 13.33% / above MA50 13.33%
- EGX70 regime: BEARISH / above MA20 0.0% / above MA50 0.0%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=453496800.0 spike=0.92 score=14.42
- ETEL.CA: liquidity=268148384.0 spike=1.02 score=7.7
- ORAS.CA: liquidity=238460752.0 spike=1.0 score=6.6
- CCAP.CA: liquidity=199523488.0 spike=0.4 score=8.15
- TMGH.CA: liquidity=173914576.0 spike=0.69 score=14.1

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- DEIN.CA: spike=19.95 liquidity=12181.95 outlook=NEUTRAL score=48.23 buy_ready=False
- MEPA.CA: spike=8.37 liquidity=58510728.0 outlook=NEUTRAL score=39.23 buy_ready=False
- EOSB.CA: spike=6.71 liquidity=439274.01 outlook=CONSTRUCTIVE score=61.23 buy_ready=False
- ELNA.CA: spike=2.95 liquidity=1438920.01 outlook=BULLISH_WATCH score=91.23 buy_ready=False
- CFGH.CA: spike=2.7 liquidity=15859.32 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=1.64 5d=0.28% 20d=-1.05% aboveMA50=0.0%
- #2 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #3 General / Verified EGX Expansion: score=1.23 5d=0.0% 20d=0.0% aboveMA50=5.94%
- #4 Industrial Goods & Cables: score=1.06 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #5 Building Materials: score=0.99 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #6 Food, Beverages & Tobacco: score=0.94 5d=0.0% 20d=-0.81% aboveMA50=0.0%
- #7 Tourism & Leisure: score=0.83 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #8 Basic Resources & Chemicals: score=-0.19 5d=-1.35% 20d=-6.45% aboveMA50=20.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ELNA.CA: BULLISH_WATCH score=91.23 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- AJWA.CA: BULLISH_WATCH score=81.23 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- CPCI.CA: BULLISH_WATCH score=75.23 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ETRS.CA: BULLISH_WATCH score=70.23 liquidity=TRADEABLE sector=LEADING risk=below MA50
- SDTI.CA: CONSTRUCTIVE score=69.23 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20
- ABUK.CA: CONSTRUCTIVE score=65 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- EOSB.CA: CONSTRUCTIVE score=61.23 liquidity=THIN sector=LEADING risk=liquidity below minimum; momentum is extended
- MFPC.CA: CONSTRUCTIVE score=53 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; below MA20; sector is not leading
- DEIN.CA: NEUTRAL score=48.23 liquidity=THIN sector=LEADING risk=liquidity below minimum; below MA20
- RAKT.CA: NEUTRAL score=46.23 liquidity=THIN sector=LEADING risk=liquidity below minimum

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- SUGR.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=0.34 buy_ready=False sector_rank=3 price=204.89 support=171.02 resistance=205.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4851210.0 spike=0.54
- ABUK.CA: score=20.92 buy_ready=False sector_rank=8 price=90.18 support=80.5 resistance=95.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=52.37 liquidity=30297080.0 spike=0.39
- ACAMD.CA: score=9.49 buy_ready=False sector_rank=3 price=1.94 support=1.86 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=25762468.0 spike=0.59
- ACGC.CA: score=1.91 buy_ready=False sector_rank=11 price=12.91 support=12.25 resistance=12.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8694188.0 spike=0.85
- ADCI.CA: score=-3.53 buy_ready=False sector_rank=3 price=249.87 support=235.01 resistance=251.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=976003.44 spike=0.61
- ADIB.CA: score=8.84 buy_ready=False sector_rank=10 price=46.1 support=43.16 resistance=51.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=34.33 liquidity=93219904.0 spike=1.21
- ADPC.CA: score=3.99 buy_ready=False sector_rank=3 price=2.82 support=2.53 resistance=3.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=18.57 liquidity=4499491.0 spike=0.47
- AFDI.CA: score=-3.53 buy_ready=False sector_rank=3 price=41.43 support=39.96 resistance=41.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=973311.56 spike=0.23
- AFMC.CA: score=5.49 buy_ready=False sector_rank=3 price=110.91 support=102.0 resistance=110.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13397015.0 spike=0.74
- AJWA.CA: score=13.76 buy_ready=False sector_rank=3 price=202.69 support=176.0 resistance=229.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=53.09 liquidity=3268155.0 spike=0.09
- ALCN.CA: score=4.23 buy_ready=False sector_rank=17 price=31.39 support=27.11 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=32.21 liquidity=6645597.5 spike=0.31
- ALUM.CA: score=-2.03 buy_ready=False sector_rank=3 price=17.92 support=17.0 resistance=18.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2482704.0 spike=0.69
- AMER.CA: score=3.1 buy_ready=False sector_rank=14 price=3.8 support=3.55 resistance=3.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31659566.0 spike=0.6
- AMES.CA: score=5.49 buy_ready=False sector_rank=3 price=32.33 support=29.51 resistance=32.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31063502.0 spike=0.53
- AMIA.CA: score=4.91 buy_ready=False sector_rank=3 price=16.76 support=14.0 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=32.15 liquidity=4415928.0 spike=0.27
- AMOC.CA: score=12.4 buy_ready=False sector_rank=18 price=13.05 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=35.6 liquidity=51455232.0 spike=0.4
- APSW.CA: score=1.63 buy_ready=False sector_rank=3 price=7.12 support=7.1 resistance=8.92 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=10.0 liquidity=973396.54 spike=1.58
- ARAB.CA: score=13.1 buy_ready=False sector_rank=14 price=0.23 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=38.51 liquidity=50343764.0 spike=0.45
- ARCC.CA: score=4.4 buy_ready=False sector_rank=5 price=64.36 support=60.17 resistance=64.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29577588.0 spike=0.69
- AREH.CA: score=0.37 buy_ready=False sector_rank=3 price=1.02 support=0.96 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4879646.0 spike=0.6
- ASCM.CA: score=-0.32 buy_ready=False sector_rank=3 price=42.76 support=41.01 resistance=42.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4184780.25 spike=0.48
- ASPI.CA: score=5.49 buy_ready=False sector_rank=3 price=0.3 support=0.28 resistance=0.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15853455.0 spike=0.84
- ATLC.CA: score=4.84 buy_ready=False sector_rank=9 price=4.7 support=4.4 resistance=4.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11189015.0 spike=1.51
- ATQA.CA: score=3.92 buy_ready=False sector_rank=8 price=9.51 support=8.78 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25008146.0 spike=0.46
- AXPH.CA: score=-2.28 buy_ready=False sector_rank=3 price=1244.82 support=1185.0 resistance=1287.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2232556.75 spike=0.4
- BINV.CA: score=-0.36 buy_ready=False sector_rank=13 price=54.38 support=52.11 resistance=65.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=25.17 liquidity=1484123.25 spike=0.1
- BIOC.CA: score=5.49 buy_ready=False sector_rank=3 price=243.13 support=226.3 resistance=243.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29695172.0 spike=0.27
- BTFH.CA: score=7.82 buy_ready=False sector_rank=9 price=2.26 support=2.05 resistance=2.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=21.43 liquidity=85039048.0 spike=0.83
- CAED.CA: score=6.15 buy_ready=False sector_rank=3 price=80.6 support=69.0 resistance=81.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11228414.0 spike=1.33
- CANA.CA: score=13.42 buy_ready=False sector_rank=10 price=42.27 support=38.1 resistance=48.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=36.69 liquidity=15774475.0 spike=0.96
- CCAP.CA: score=8.15 buy_ready=False sector_rank=13 price=6.1 support=5.8 resistance=6.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=28.99 liquidity=199523488.0 spike=0.4
- CCRS.CA: score=-1.38 buy_ready=False sector_rank=3 price=1.59 support=1.53 resistance=1.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3129827.0 spike=0.46
- CEFM.CA: score=-1.85 buy_ready=False sector_rank=3 price=114.77 support=108.0 resistance=117.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2314707.5 spike=1.17
- CERA.CA: score=5.49 buy_ready=False sector_rank=3 price=1.04 support=1.0 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=57708228.0 spike=0.48
- CFGH.CA: score=2.91 buy_ready=False sector_rank=3 price=0.1 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=9.09 liquidity=15859.32 spike=2.7
- CICH.CA: score=-1.63 buy_ready=False sector_rank=9 price=10.27 support=9.63 resistance=12.38 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=18.93 liquidity=545449.99 spike=0.24
- CIEB.CA: score=0.44 buy_ready=False sector_rank=10 price=21.98 support=21.35 resistance=24.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=22.6 liquidity=3017778.25 spike=0.35
- CIRA.CA: score=2.7 buy_ready=False sector_rank=16 price=34.35 support=32.01 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=23.29 liquidity=4951760.0 spike=0.29
- CLHO.CA: score=7.17 buy_ready=False sector_rank=12 price=13.46 support=12.51 resistance=16.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=4.39 liquidity=35114480.0 spike=0.95
- CNFN.CA: score=-1.96 buy_ready=False sector_rank=9 price=3.8 support=3.6 resistance=3.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4217751.0 spike=0.45
- COMI.CA: score=14.42 buy_ready=False sector_rank=10 price=122.47 support=118.06 resistance=130.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=36.48 liquidity=453496800.0 spike=0.92
- COPR.CA: score=1.39 buy_ready=False sector_rank=3 price=0.39 support=0.37 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5900446.0 spike=0.36
- COSG.CA: score=5.49 buy_ready=False sector_rank=3 price=1.26 support=1.17 resistance=1.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10914393.0 spike=0.96
- CPCI.CA: score=13.04 buy_ready=False sector_rank=3 price=597.65 support=502.25 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=44.24 liquidity=2548199.0 spike=0.48
- CSAG.CA: score=-0.82 buy_ready=False sector_rank=17 price=32.37 support=30.1 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=24.06 liquidity=2594045.75 spike=0.37
- DAPH.CA: score=5.49 buy_ready=False sector_rank=3 price=76.42 support=69.0 resistance=76.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16490152.0 spike=0.4
- DEIN.CA: score=13.5 buy_ready=False sector_rank=3 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=12181.95 spike=19.95
- DOMT.CA: score=-4.28 buy_ready=False sector_rank=6 price=22.19 support=21.19 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1343434.5 spike=0.4
- DSCW.CA: score=9.49 buy_ready=False sector_rank=3 price=1.43 support=1.23 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=20.69 liquidity=13197148.0 spike=0.84
- DTPP.CA: score=5.49 buy_ready=False sector_rank=3 price=43.03 support=41.08 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19623272.0 spike=0.48
- EALR.CA: score=-3.63 buy_ready=False sector_rank=3 price=256.96 support=245.21 resistance=258.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=874530.5 spike=0.27
- EASB.CA: score=-1.11 buy_ready=False sector_rank=3 price=5.99 support=5.5 resistance=6.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3398859.75 spike=0.69
- EAST.CA: score=17.38 buy_ready=False sector_rank=6 price=30.8 support=27.01 resistance=30.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=56.91 liquidity=16756825.0 spike=0.35
- EBSC.CA: score=0.36 buy_ready=False sector_rank=3 price=1.31 support=1.2 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=13.58 liquidity=864584.75 spike=0.43
- ECAP.CA: score=0.05 buy_ready=False sector_rank=3 price=26.57 support=24.8 resistance=31.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=17.48 liquidity=560038.19 spike=0.16
- EDFM.CA: score=1.2 buy_ready=False sector_rank=3 price=366.36 support=335.2 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=23.78 liquidity=705505.75 spike=0.63
- EEII.CA: score=11.01 buy_ready=False sector_rank=3 price=1.6 support=1.42 resistance=2.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=14.46 liquidity=11289695.0 spike=1.76
- EFIC.CA: score=3.92 buy_ready=False sector_rank=8 price=135.62 support=129.0 resistance=136.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11065060.0 spike=0.43
- EFID.CA: score=4.38 buy_ready=False sector_rank=6 price=17.99 support=17.22 resistance=18.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16682905.0 spike=0.4
- EFIH.CA: score=6.4 buy_ready=False sector_rank=19 price=21.39 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=30.12 liquidity=30220458.0 spike=0.45
- EGAL.CA: score=8.92 buy_ready=False sector_rank=8 price=303.46 support=275.0 resistance=359.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=22.11 liquidity=63060260.0 spike=0.67
- EGAS.CA: score=-2.12 buy_ready=False sector_rank=18 price=45.89 support=43.0 resistance=58.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=17.74 liquidity=1476975.5 spike=0.28
- EGBE.CA: score=-1.54 buy_ready=False sector_rank=10 price=0.5 support=0.47 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=15.66 liquidity=36549.46 spike=0.35
- EGCH.CA: score=7.92 buy_ready=False sector_rank=8 price=10.6 support=10.0 resistance=13.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=20.23 liquidity=45149908.0 spike=0.75
- EGSA.CA: score=10.26 buy_ready=False sector_rank=1 price=8.81 support=8.75 resistance=9.09 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=46.05 liquidity=7990.67 spike=1.3
- EGTS.CA: score=2.15 buy_ready=False sector_rank=14 price=12.03 support=10.7 resistance=12.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9049433.0 spike=0.43
- EHDR.CA: score=1.44 buy_ready=False sector_rank=3 price=1.97 support=1.9 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5948541.5 spike=0.64
- ELEC.CA: score=4.42 buy_ready=False sector_rank=4 price=1.49 support=1.43 resistance=1.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30269898.0 spike=0.61
- ELKA.CA: score=2.6 buy_ready=False sector_rank=3 price=1.4 support=1.33 resistance=1.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7109443.0 spike=0.55
- ELNA.CA: score=14.83 buy_ready=False sector_rank=3 price=36.92 support=33.46 resistance=39.99 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=65.45 liquidity=1438920.01 spike=2.95
- ELSH.CA: score=0.59 buy_ready=False sector_rank=3 price=9.52 support=8.9 resistance=9.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5098626.0 spike=0.27
- ELWA.CA: score=11.49 buy_ready=False sector_rank=3 price=1.65 support=1.43 resistance=1.66 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=1288.65 spike=0.0
- EMFD.CA: score=8.1 buy_ready=False sector_rank=14 price=11.67 support=10.6 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=26.84 liquidity=12642092.0 spike=0.22
- ENGC.CA: score=0.98 buy_ready=False sector_rank=3 price=31.06 support=28.93 resistance=31.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5488449.5 spike=0.51
- EOSB.CA: score=15.93 buy_ready=False sector_rank=3 price=1.61 support=1.56 resistance=1.72 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=70.0 liquidity=439274.01 spike=6.71
- EPCO.CA: score=-1.57 buy_ready=False sector_rank=3 price=7.77 support=7.4 resistance=7.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2936535.25 spike=0.67
- EPPK.CA: score=-4.09 buy_ready=False sector_rank=3 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=7.7 buy_ready=False sector_rank=1 price=127.0 support=117.8 resistance=127.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=268148384.0 spike=1.02
- ETRS.CA: score=17.49 buy_ready=False sector_rank=3 price=10.45 support=9.51 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=10070053.0 spike=0.87
- EXPA.CA: score=3.42 buy_ready=False sector_rank=10 price=13.98 support=13.07 resistance=14.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10723349.0 spike=0.28
- FAIT.CA: score=4.75 buy_ready=False sector_rank=10 price=42.98 support=40.0 resistance=45.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=38.3 liquidity=1328850.13 spike=0.45
- FAITA.CA: score=5.43 buy_ready=False sector_rank=10 price=0.99 support=0.98 resistance=1.01 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=51.97 liquidity=11313.26 spike=0.32
- FERC.CA: score=0.0 buy_ready=False sector_rank=8 price=57.64 support=53.57 resistance=77.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=12.61 liquidity=2079333.13 spike=0.65
- FWRY.CA: score=6.4 buy_ready=False sector_rank=19 price=17.16 support=16.45 resistance=19.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=26.23 liquidity=52648888.0 spike=0.45
- GBCO.CA: score=6.4 buy_ready=False sector_rank=21 price=23.5 support=22.02 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=12.3 liquidity=40632428.0 spike=0.34
- GDWA.CA: score=2.53 buy_ready=False sector_rank=3 price=0.53 support=0.51 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7041489.5 spike=0.5
- GGCC.CA: score=5.49 buy_ready=False sector_rank=3 price=0.54 support=0.51 resistance=0.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10885796.0 spike=0.68
- GIHD.CA: score=5.49 buy_ready=False sector_rank=3 price=37.62 support=35.25 resistance=38.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11196623.0 spike=0.81
- GMCI.CA: score=1.58 buy_ready=False sector_rank=3 price=1.54 support=1.47 resistance=1.77 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=10.53 liquidity=89869.78 spike=0.3
- GRCA.CA: score=-2.09 buy_ready=False sector_rank=3 price=25.36 support=24.02 resistance=25.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2415061.25 spike=0.49
- GSSC.CA: score=0.02 buy_ready=False sector_rank=3 price=239.33 support=211.52 resistance=290.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT RSI=20.14 liquidity=523562.66 spike=0.43
- HDBK.CA: score=7.66 buy_ready=False sector_rank=10 price=96.26 support=83.01 resistance=112.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=33.91 liquidity=24630206.0 spike=1.12
- HELI.CA: score=8.1 buy_ready=False sector_rank=14 price=6.4 support=5.72 resistance=7.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=26.37 liquidity=36490104.0 spike=0.53
- HRHO.CA: score=7.82 buy_ready=False sector_rank=9 price=24.0 support=22.8 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=34.17 liquidity=22867012.0 spike=0.18
- ICID.CA: score=2.77 buy_ready=False sector_rank=3 price=16.01 support=14.26 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=29.73 liquidity=2278388.5 spike=0.33
- IDRE.CA: score=0.78 buy_ready=False sector_rank=3 price=34.22 support=30.1 resistance=34.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5288289.0 spike=0.94
- IFAP.CA: score=-1.79 buy_ready=False sector_rank=15 price=17.01 support=15.51 resistance=19.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=14.98 liquidity=1389597.5 spike=0.27
- INFI.CA: score=4.05 buy_ready=False sector_rank=3 price=109.37 support=103.51 resistance=109.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8554117.0 spike=0.42
- IRON.CA: score=1.24 buy_ready=False sector_rank=8 price=24.72 support=23.53 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=28.16 liquidity=3317707.25 spike=0.31
- ISMA.CA: score=6.1 buy_ready=False sector_rank=3 price=18.48 support=16.33 resistance=18.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9792178.0 spike=1.41
- ISMQ.CA: score=-0.76 buy_ready=False sector_rank=8 price=6.61 support=6.28 resistance=6.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5316831.0 spike=0.3
- ISPH.CA: score=7.17 buy_ready=False sector_rank=12 price=10.02 support=9.14 resistance=12.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=20.97 liquidity=33205672.0 spike=0.72
- JUFO.CA: score=2.41 buy_ready=False sector_rank=6 price=23.28 support=21.91 resistance=23.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8030080.0 spike=0.49
- KABO.CA: score=7.61 buy_ready=False sector_rank=11 price=6.69 support=5.58 resistance=9.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=31.42 liquidity=27578428.0 spike=1.2
- KWIN.CA: score=-0.34 buy_ready=False sector_rank=3 price=52.83 support=49.5 resistance=53.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4169958.0 spike=0.85
- KZPC.CA: score=-2.16 buy_ready=False sector_rank=3 price=12.5 support=12.1 resistance=12.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2347690.0 spike=0.32
- LCSW.CA: score=4.46 buy_ready=False sector_rank=5 price=33.33 support=31.2 resistance=33.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20450718.0 spike=1.03
- LUTS.CA: score=5.49 buy_ready=False sector_rank=3 price=0.57 support=0.53 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=38882268.0 spike=0.69
- MAAL.CA: score=0.26 buy_ready=False sector_rank=3 price=6.17 support=5.65 resistance=6.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4763123.5 spike=0.33
- MASR.CA: score=9.49 buy_ready=False sector_rank=3 price=6.48 support=5.6 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=28.05 liquidity=35859672.0 spike=0.72
- MBSC.CA: score=4.4 buy_ready=False sector_rank=5 price=307.92 support=285.5 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=44799160.0 spike=0.42
- MCQE.CA: score=4.4 buy_ready=False sector_rank=5 price=162.93 support=150.0 resistance=163.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42318556.0 spike=0.6
- MCRO.CA: score=5.49 buy_ready=False sector_rank=3 price=1.23 support=1.17 resistance=1.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=34832644.0 spike=0.77
- MENA.CA: score=-0.65 buy_ready=False sector_rank=14 price=5.73 support=5.45 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=25.93 liquidity=2246836.5 spike=0.9
- MEPA.CA: score=14.49 buy_ready=False sector_rank=3 price=1.24 support=1.14 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=17.44 liquidity=58510728.0 spike=8.37
- MFPC.CA: score=18.92 buy_ready=False sector_rank=8 price=45.13 support=40.66 resistance=47.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=45.06 liquidity=26443150.0 spike=0.53
- MFSC.CA: score=-2.77 buy_ready=False sector_rank=3 price=32.93 support=31.02 resistance=33.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1737998.0 spike=0.78
- MHOT.CA: score=-0.5 buy_ready=False sector_rank=7 price=14.38 support=13.16 resistance=14.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5164091.0 spike=0.55
- MICH.CA: score=7.69 buy_ready=False sector_rank=3 price=40.68 support=35.5 resistance=44.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=40.22 liquidity=2198061.25 spike=0.28
- MILS.CA: score=4.15 buy_ready=False sector_rank=3 price=118.27 support=107.01 resistance=118.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8478154.0 spike=1.09
- MIPH.CA: score=11.58 buy_ready=False sector_rank=12 price=752.0 support=610.0 resistance=879.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=37.34 liquidity=6852190.5 spike=1.78
- MOED.CA: score=5.49 buy_ready=False sector_rank=3 price=0.44 support=0.41 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11371919.0 spike=0.89
- MOIL.CA: score=-2.49 buy_ready=False sector_rank=18 price=0.64 support=0.6 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=21.97 liquidity=114037.66 spike=0.52
- MOIN.CA: score=0.29 buy_ready=False sector_rank=3 price=28.08 support=26.4 resistance=28.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4793447.0 spike=0.56
- MOSC.CA: score=-3.01 buy_ready=False sector_rank=3 price=234.72 support=221.11 resistance=243.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1500731.5 spike=0.44
- MPCI.CA: score=5.49 buy_ready=False sector_rank=3 price=270.59 support=256.0 resistance=273.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=73280248.0 spike=0.77
- MPCO.CA: score=2.82 buy_ready=False sector_rank=15 price=1.8 support=1.72 resistance=1.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=47135428.0 spike=0.51
- MPRC.CA: score=5.49 buy_ready=False sector_rank=3 price=31.0 support=28.06 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12528508.0 spike=0.75
- MTIE.CA: score=3.71 buy_ready=False sector_rank=21 price=6.83 support=6.05 resistance=8.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=29.45 liquidity=7311556.0 spike=0.35
- NAHO.CA: score=3.53 buy_ready=False sector_rank=3 price=0.12 support=0.12 resistance=0.13 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=27.78 liquidity=42676.34 spike=2.5
- NCCW.CA: score=4.0 buy_ready=False sector_rank=3 price=4.83 support=4.49 resistance=4.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8512975.0 spike=0.34
- NEDA.CA: score=2.56 buy_ready=False sector_rank=3 price=2.6 support=2.47 resistance=2.71 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=66674.4 spike=0.33
- NHPS.CA: score=1.14 buy_ready=False sector_rank=3 price=54.22 support=51.2 resistance=54.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5644832.0 spike=0.67
- NINH.CA: score=1.84 buy_ready=False sector_rank=3 price=14.05 support=12.92 resistance=14.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6351963.0 spike=0.63
- NIPH.CA: score=3.17 buy_ready=False sector_rank=12 price=237.66 support=229.0 resistance=239.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=70492560.0 spike=0.58
- OBRI.CA: score=4.67 buy_ready=False sector_rank=3 price=21.66 support=19.91 resistance=21.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9175370.0 spike=0.62
- OCDI.CA: score=3.1 buy_ready=False sector_rank=14 price=23.75 support=22.09 resistance=23.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22104690.0 spike=0.6
- OCPH.CA: score=-1.11 buy_ready=False sector_rank=3 price=163.38 support=153.88 resistance=166.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3218427.75 spike=1.09
- ODIN.CA: score=-1.37 buy_ready=False sector_rank=3 price=1.9 support=1.81 resistance=1.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3138723.75 spike=0.53
- OFH.CA: score=5.49 buy_ready=False sector_rank=3 price=0.69 support=0.66 resistance=0.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16706691.0 spike=0.43
- OIH.CA: score=3.15 buy_ready=False sector_rank=13 price=1.64 support=1.54 resistance=1.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33090280.0 spike=0.56
- OLFI.CA: score=4.51 buy_ready=False sector_rank=6 price=19.54 support=17.86 resistance=22.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=17.9 liquidity=6135210.5 spike=0.39
- ORAS.CA: score=6.6 buy_ready=False sector_rank=2 price=814.13 support=780.0 resistance=823.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=238460752.0 spike=1.0
- ORHD.CA: score=3.1 buy_ready=False sector_rank=14 price=9.7 support=9.15 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=115665064.0 spike=0.98
- ORWE.CA: score=8.21 buy_ready=False sector_rank=11 price=23.9 support=22.62 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=22.61 liquidity=18314860.0 spike=0.47
- PHAR.CA: score=8.43 buy_ready=False sector_rank=12 price=96.2 support=90.2 resistance=119.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=17.65 liquidity=65971828.0 spike=1.13
- PHDC.CA: score=7.1 buy_ready=False sector_rank=14 price=11.8 support=11.0 resistance=13.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=25.63 liquidity=31061964.0 spike=0.33
- PHTV.CA: score=0.88 buy_ready=False sector_rank=3 price=313.19 support=300.0 resistance=360.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=33.19 liquidity=387101.47 spike=0.4
- POUL.CA: score=10.38 buy_ready=False sector_rank=6 price=9.41 support=8.81 resistance=10.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=31.72 liquidity=41618412.0 spike=0.73
- PRCL.CA: score=0.51 buy_ready=False sector_rank=5 price=19.73 support=18.38 resistance=19.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6115170.5 spike=0.63
- PRDC.CA: score=6.92 buy_ready=False sector_rank=14 price=6.01 support=5.08 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=27.38 liquidity=9817742.0 spike=0.28
- PRMH.CA: score=-2.89 buy_ready=False sector_rank=3 price=1.87 support=1.78 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1618845.5 spike=0.53
- RACC.CA: score=5.54 buy_ready=False sector_rank=3 price=7.22 support=6.1 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=21.15 liquidity=6047248.0 spike=0.85
- RAKT.CA: score=12.72 buy_ready=False sector_rank=3 price=22.7 support=20.26 resistance=25.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=53.67 liquidity=543410.06 spike=1.34
- RAYA.CA: score=6.4 buy_ready=False sector_rank=20 price=5.49 support=5.02 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=16.91 liquidity=11525489.0 spike=0.47
- RMDA.CA: score=3.21 buy_ready=False sector_rank=12 price=5.06 support=4.8 resistance=5.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26156434.0 spike=1.02
- ROTO.CA: score=5.2 buy_ready=False sector_rank=3 price=29.03 support=25.0 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=22.34 liquidity=5703088.5 spike=0.71
- RREI.CA: score=6.21 buy_ready=False sector_rank=3 price=2.39 support=2.29 resistance=2.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11019219.0 spike=1.36
- RTVC.CA: score=1.82 buy_ready=False sector_rank=3 price=2.98 support=2.89 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=11.11 liquidity=2330425.75 spike=0.95
- RUBX.CA: score=5.49 buy_ready=False sector_rank=3 price=12.54 support=11.59 resistance=12.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48437872.0 spike=0.58
- SAUD.CA: score=6.07 buy_ready=False sector_rank=10 price=21.0 support=19.3 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=20.96 liquidity=7649949.5 spike=0.66
- SCEM.CA: score=5.26 buy_ready=False sector_rank=5 price=83.53 support=77.01 resistance=83.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=81595816.0 spike=1.43
- SCFM.CA: score=-2.03 buy_ready=False sector_rank=3 price=182.13 support=168.5 resistance=186.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2142622.5 spike=1.17
- SCTS.CA: score=13.64 buy_ready=False sector_rank=16 price=515.33 support=410.0 resistance=588.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=39.73 liquidity=6685454.5 spike=2.1
- SDTI.CA: score=15.13 buy_ready=False sector_rank=3 price=81.0 support=75.01 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=43.77 liquidity=6641053.5 spike=0.31
- SEIG.CA: score=-3.93 buy_ready=False sector_rank=3 price=159.69 support=155.5 resistance=164.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=574748.0 spike=0.28
- SIPC.CA: score=5.49 buy_ready=False sector_rank=3 price=4.44 support=4.11 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27324492.0 spike=0.47
- SKPC.CA: score=7.92 buy_ready=False sector_rank=8 price=14.5 support=14.01 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=40679592.0 spike=0.65
- SMFR.CA: score=-2.98 buy_ready=False sector_rank=3 price=180.27 support=169.0 resistance=188.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1523542.38 spike=0.51
- SNFC.CA: score=0.8 buy_ready=False sector_rank=3 price=10.6 support=10.08 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=1309263.38 spike=0.17
- SPIN.CA: score=3.4 buy_ready=False sector_rank=11 price=14.34 support=12.0 resistance=17.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=29.34 liquidity=5988098.5 spike=1.1
- SPMD.CA: score=2.91 buy_ready=False sector_rank=3 price=0.33 support=0.32 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7416596.0 spike=0.66
- SVCE.CA: score=5.49 buy_ready=False sector_rank=3 price=8.67 support=8.01 resistance=8.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37201824.0 spike=0.53
- SWDY.CA: score=4.42 buy_ready=False sector_rank=4 price=109.46 support=103.4 resistance=110.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=50074280.0 spike=0.81
- TALM.CA: score=7.75 buy_ready=False sector_rank=16 price=18.9 support=17.0 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=6.11 liquidity=12142227.0 spike=0.43
- TMGH.CA: score=14.1 buy_ready=False sector_rank=14 price=82.54 support=80.01 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=35.92 liquidity=173914576.0 spike=0.69
- TRTO.CA: score=0.68 buy_ready=False sector_rank=3 price=0.06 support=0.05 resistance=0.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:58 AM market time freshness=DELAYED_CURRENT RSI=27.78 liquidity=7715.85 spike=1.09
- UEFM.CA: score=0.41 buy_ready=False sector_rank=3 price=441.61 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=23.58 liquidity=917733.81 spike=0.32
- UEGC.CA: score=5.49 buy_ready=False sector_rank=3 price=1.42 support=1.32 resistance=1.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24208004.0 spike=0.53
- UNIP.CA: score=0.91 buy_ready=False sector_rank=3 price=0.28 support=0.27 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5419282.0 spike=0.67
- UNIT.CA: score=3.49 buy_ready=False sector_rank=14 price=16.27 support=15.06 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=35.8 liquidity=382297.06 spike=0.1
- WCDF.CA: score=0.03 buy_ready=False sector_rank=3 price=487.09 support=432.5 resistance=652.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=13.93 liquidity=540046.06 spike=0.22
- WKOL.CA: score=-0.43 buy_ready=False sector_rank=3 price=234.31 support=225.01 resistance=234.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4080541.0 spike=0.55
- ZEOT.CA: score=-1.1 buy_ready=False sector_rank=3 price=10.2 support=9.7 resistance=10.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3411760.0 spike=0.42
- ZMID.CA: score=7.1 buy_ready=False sector_rank=14 price=6.29 support=5.91 resistance=8.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=16.39 liquidity=32735990.0 spike=0.48

## Backtesting Lite
- ABUK.CA: 180d return=44.57%, max drawdown=-26.86%, MA20>MA50 days last20=20, as_of=2026-10-25T21:00:00+00:00
- MFPC.CA: 180d return=46.58%, max drawdown=-26.33%, MA20>MA50 days last20=20, as_of=2026-10-25T21:00:00+00:00
- ETRS.CA: 180d return=36.5%, max drawdown=-16.61%, MA20>MA50 days last20=3, as_of=2026-10-25T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ABUK.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Qir Fertilizers summary=Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results; Abu Qir Fertilizers&#39; board approves $5.6m coated urea project; Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26
  - Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results: https://english.mubasher.info/news/4604919/Abu-Qir-Fertilizers-generates-EGP-5-6bn-net-profits-in-Q1-26-unaudited-results/
  - Abu Qir Fertilizers&#39; board approves $5.6m coated urea project: https://english.mubasher.info/news/4585599/Abu-Qir-Fertilizers-board-approves-5-6m-coated-urea-project/
  - Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26: https://english.mubasher.info/news/4554415/Abu-Qir-Fertilizers-profits-exceed-EGP-5-1bn-in-H1-25-26/
- MFPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr Fertilizers Production summary=Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- ETRS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Transport and Commercial Services Company S.A.E. summary=Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- EAST.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Eastern Company summary=Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- EOSB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Orouba Securities Brokerage summary=El Orouba Brokerage turns profitable in Q4; El Orouba Securities suffers 598,000 losses in Q3; El Orouba Securities H1 losses down 7%
  - El Orouba Brokerage turns profitable in Q4: https://english.mubasher.info/news/3067539/El-Orouba-Brokerage-turns-profitable-in-Q4/
  - El Orouba Securities suffers 598,000 losses in Q3: https://english.mubasher.info/news/3016624/El-Orouba-Securities-suffers-598-000-losses-in-Q3/
  - El Orouba Securities H1 losses down 7%: https://english.mubasher.info/news/2984110/El-Orouba-Securities-H1-losses-down-7-/
- SDTI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=SHARM DREAMS Co. for Touristic Investment S.A.E summary=Sharm Dreams stock maintains strong uptrend - Analysis; Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis; Sharm Dreams stock hits historic level halting driving buying force
  - Sharm Dreams stock maintains strong uptrend - Analysis: https://english.mubasher.info/news/4577977/Sharm-Dreams-stock-maintains-strong-uptrend-Analysis/
  - Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis: https://english.mubasher.info/news/4547831/Sharm-Dreams-stock-is-experiencing-sideways-movement-amid-anticipation-of-next-trend-Analysis/
  - Sharm Dreams stock hits historic level halting driving buying force: https://english.mubasher.info/news/4529096/Sharm-Dreams-stock-hits-historic-level-halting-driving-buying-force/
- ELNA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Nasr Manufacturing Agricultural Crops S.A.E summary=Consortium offers to acquire controlling stake in El Nasr for Agricultural Crops; El Nasr for Agricultural Crops to sell Sohag factory land for EGP 650m; EGX halts trading on El Nasr for Manufacturing Agricultural Crops
  - Consortium offers to acquire controlling stake in El Nasr for Agricultural Crops: https://english.mubasher.info/news/3749421/Consortium-offers-to-acquire-controlling-stake-in-El-Nasr-for-Agricultural-Crops/
  - El Nasr for Agricultural Crops to sell Sohag factory land for EGP 650m: https://english.mubasher.info/news/3685533/El-Nasr-for-Agricultural-Crops-to-sell-Sohag-factory-land-for-EGP-650m/
  - EGX halts trading on El Nasr for Manufacturing Agricultural Crops: https://english.mubasher.info/news/3489525/EGX-halts-trading-on-El-Nasr-for-Manufacturing-Agricultural-Crops/
- MEPA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Medical Packaging Company summary=Medical Packaging stock close to break above EGP 1.7; Medical Packaging announces EGP 62m capital hike; Medical Packaging&#39;s profit jumps 54% in Q1-21
  - Medical Packaging stock close to break above EGP 1.7: https://english.mubasher.info/news/4598700/Medical-Packaging-stock-close-to-break-above-EGP-1-7/
  - Medical Packaging announces EGP 62m capital hike: https://english.mubasher.info/news/3936298/Medical-Packaging-announces-EGP-62m-capital-hike/
  - Medical Packaging&#39;s profit jumps 54% in Q1-21: https://english.mubasher.info/news/3815448/Medical-Packaging-s-profit-jumps-54-in-Q1-21/

## Warnings
- OpenRouter API error: 404
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- Evidence for EOSB.CA matches the company but no source/report date was detected.
- Evidence for SDTI.CA matches the company but no source/report date was detected.
- Evidence for ELNA.CA matches the company but no source/report date was detected.
- Evidence for MEPA.CA matches the company but no source/report date was detected.
