# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-09-28T13:48:40.359650+00:00
Generated Cairo: 2026-09-28 16:48
Run timing: target 09:15 Cairo | generated Cairo 2026-09-28 16:48 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-09-28 16:45

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 152/187
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, September 28
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 5.26% / above MA50 26.32%
- EGX70 regime: BEARISH / above MA20 8.57% / above MA50 20.0%
- Sector breadth: 4.76%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=440664704.0 spike=0.5 score=21.47
- COMI.CA: liquidity=292904704.0 spike=0.48 score=9.52
- TMGH.CA: liquidity=276571936.0 spike=0.95 score=6.83
- ETEL.CA: liquidity=246676880.0 spike=0.86 score=24.4
- GTWL.CA: liquidity=238225648.0 spike=1.85 score=4.69

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with weak breadth (≈5% above MA20, sector breadth 4.8%), triggering DEFENSIVE_NO_NEW_BUY risk mode; the scanner highlights a few tickets with constructive/ bullish‑watch outlooks and liquidity spikes, but maintains HOLD due to the prevailing regime.
- Top tickets (ETEL.CA, EXPA.CA, CIRA.CA) show constructive or bullish‑watch outlooks and liquidity spikes, yet are flagged HOLD because the bearish regime overrides short‑term signals.
- Liquidity spikes (>1.7×) in ETEL.CA and MAAL.CA hint at short‑term interest, but support lies far below current prices, limiting near‑term downside protection.
- Sector leadership is confined to Telecommunications and Education; overall sector breadth remains low (<5%), suggesting any strength may be isolated and prone to reversal.
- EGX30/EGX70 bearish trend shifts risk mode to DEFENSIVE_NO_NEW_BUY, adding uncertainty; a sustained move above MA20 or a sector‑breadth rebound would be required to ease the hold stance.

## Top Liquidity Spikes
- EGSA.CA: spike=4.49 liquidity=29497.65 outlook=WEAK_OR_RISKY score=25.05 buy_ready=False
- SDTI.CA: spike=2.72 liquidity=83420320.0 outlook=CONSTRUCTIVE score=58 buy_ready=False
- POUL.CA: spike=2.14 liquidity=55180564.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MAAL.CA: spike=1.97 liquidity=43040624.0 outlook=BULLISH_WATCH score=78 buy_ready=False
- MHOT.CA: spike=1.95 liquidity=32332246.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=9.05 5d=0.56% 20d=9.04% aboveMA50=50.0%
- #2 Education: score=4.4 5d=-5.13% 20d=14.1% aboveMA50=66.67%
- #3 Investment Holding: score=3.68 5d=-6.08% 20d=6.8% aboveMA50=66.67%
- #4 Energy & Petrochemicals: score=3.24 5d=-3.36% 20d=2.46% aboveMA50=66.67%
- #5 Tourism & Leisure: score=2.92 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #6 Transportation & Logistics: score=2.27 5d=-3.14% 20d=-1.93% aboveMA50=50.0%
- #7 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #8 Banking & Financials: score=1.3 5d=-2.7% 20d=-1.48% aboveMA50=40.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- EXPA.CA: BULLISH_WATCH score=83.3 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- BINV.CA: BULLISH_WATCH score=81.68 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- CIRA.CA: BULLISH_WATCH score=80.4 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- ALCN.CA: BULLISH_WATCH score=78.27 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MAAL.CA: BULLISH_WATCH score=78 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=momentum is extended; far above support; sector is not leading
- CANA.CA: BULLISH_WATCH score=77.3 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- EGTS.CA: BULLISH_WATCH score=76 liquidity=TRADEABLE sector=LAGGING risk=sector is not leading
- CCAP.CA: BULLISH_WATCH score=75.68 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- CPCI.CA: BULLISH_WATCH score=74 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=momentum is extended; sector is not leading
- TALM.CA: CONSTRUCTIVE score=66.4 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=2.24 buy_ready=False sector_rank=16 price=250.9 support=240.1 resistance=271.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9245596.0 spike=0.38
- ABUK.CA: score=16.54 buy_ready=False sector_rank=13 price=88.16 support=78.26 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.97 liquidity=90409784.0 spike=0.5
- ACAMD.CA: score=2.99 buy_ready=False sector_rank=16 price=1.97 support=1.88 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=45956108.0 spike=0.91
- ACGC.CA: score=8.31 buy_ready=False sector_rank=12 price=13.55 support=13.58 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.48 liquidity=6714494.0 spike=0.27
- ADCI.CA: score=-0.93 buy_ready=False sector_rank=16 price=270.25 support=267.66 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=31.41 liquidity=1078552.25 spike=0.24
- ADIB.CA: score=14.94 buy_ready=False sector_rank=8 price=51.07 support=49.0 resistance=55.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.11 liquidity=104450952.0 spike=1.21
- ADPC.CA: score=6.99 buy_ready=False sector_rank=16 price=3.51 support=3.51 resistance=4.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=21.05 liquidity=13630241.0 spike=0.71
- AFDI.CA: score=5.44 buy_ready=False sector_rank=16 price=50.79 support=50.6 resistance=61.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.06 liquidity=2445885.25 spike=0.15
- AFMC.CA: score=6.95 buy_ready=False sector_rank=16 price=135.69 support=140.02 resistance=217.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=10.04 liquidity=8962571.0 spike=0.17
- AJWA.CA: score=14.99 buy_ready=False sector_rank=16 price=179.83 support=175.15 resistance=199.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=40.69 liquidity=11067287.0 spike=0.26
- ALCN.CA: score=21.91 buy_ready=False sector_rank=6 price=32.43 support=30.05 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.18 liquidity=22127132.0 spike=0.58
- ALUM.CA: score=4.39 buy_ready=False sector_rank=16 price=22.58 support=22.7 resistance=30.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=20.14 liquidity=6393009.5 spike=0.94
- AMER.CA: score=2.83 buy_ready=False sector_rank=17 price=4.53 support=4.45 resistance=4.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42085280.0 spike=0.89
- AMES.CA: score=2.99 buy_ready=False sector_rank=16 price=42.45 support=40.15 resistance=45.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=55687224.0 spike=0.2
- AMIA.CA: score=15.99 buy_ready=False sector_rank=16 price=18.69 support=17.12 resistance=21.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.11 liquidity=15094376.0 spike=0.44
- AMOC.CA: score=18.3 buy_ready=False sector_rank=4 price=13.09 support=11.49 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.18 liquidity=131438528.0 spike=0.8
- APSW.CA: score=-2.51 buy_ready=False sector_rank=16 price=8.03 support=8.13 resistance=8.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=31.45 liquidity=499108.19 spike=0.64
- ARAB.CA: score=6.83 buy_ready=False sector_rank=17 price=0.22 support=0.21 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.91 liquidity=50461204.0 spike=0.64
- ARCC.CA: score=8.49 buy_ready=False sector_rank=14 price=62.01 support=63.25 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=8.56 liquidity=23124742.0 spike=0.72
- AREH.CA: score=7.11 buy_ready=False sector_rank=16 price=1.21 support=1.25 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=17.65 liquidity=14253089.0 spike=1.06
- ASCM.CA: score=7.71 buy_ready=False sector_rank=16 price=56.52 support=57.24 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=21.6 liquidity=9720791.0 spike=0.54
- ASPI.CA: score=7.99 buy_ready=False sector_rank=16 price=0.35 support=0.36 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=30.66 liquidity=24386130.0 spike=0.41
- ATLC.CA: score=7.4 buy_ready=False sector_rank=19 price=5.65 support=5.43 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=23.81 liquidity=11151598.0 spike=0.38
- ATQA.CA: score=16.54 buy_ready=False sector_rank=13 price=11.77 support=11.56 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.59 liquidity=56010204.0 spike=0.55
- AXPH.CA: score=11.3 buy_ready=False sector_rank=16 price=1541.48 support=1580.0 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.66 liquidity=9566836.0 spike=1.37
- BINV.CA: score=17.94 buy_ready=False sector_rank=3 price=55.1 support=49.51 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.4 liquidity=4465164.5 spike=0.19
- BIOC.CA: score=7.99 buy_ready=False sector_rank=16 price=232.56 support=237.0 resistance=453.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=16.58 liquidity=22306572.0 spike=0.27
- BTFH.CA: score=7.26 buy_ready=False sector_rank=19 price=2.66 support=2.71 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=24.59 liquidity=125268504.0 spike=1.43
- CAED.CA: score=-1.22 buy_ready=False sector_rank=16 price=103.89 support=103.1 resistance=117.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5789329.0 spike=0.29
- CANA.CA: score=21.56 buy_ready=False sector_rank=8 price=45.01 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=60.35 liquidity=24509466.0 spike=1.02
- CCAP.CA: score=21.47 buy_ready=False sector_rank=3 price=6.69 support=5.79 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.28 liquidity=440664704.0 spike=0.5
- CCRS.CA: score=9.64 buy_ready=False sector_rank=16 price=2.33 support=2.4 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.61 liquidity=6645919.5 spike=0.31
- CEFM.CA: score=-4.52 buy_ready=False sector_rank=16 price=126.15 support=113.0 resistance=133.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2488070.0 spike=0.29
- CERA.CA: score=7.99 buy_ready=False sector_rank=16 price=1.24 support=1.2 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=16.87 liquidity=109362240.0 spike=0.77
- CFGH.CA: score=-6.99 buy_ready=False sector_rank=16 price=0.11 support=0.11 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13510.05 spike=0.84
- CICH.CA: score=13.92 buy_ready=False sector_rank=19 price=11.35 support=11.53 resistance=13.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.51 liquidity=10405239.0 spike=1.76
- CIEB.CA: score=6.12 buy_ready=False sector_rank=8 price=23.72 support=23.9 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=28.13 liquidity=6595229.0 spike=0.47
- CIRA.CA: score=22.76 buy_ready=False sector_rank=2 price=38.63 support=32.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=58.81 liquidity=24421678.0 spike=0.61
- CLHO.CA: score=7.68 buy_ready=False sector_rank=18 price=15.24 support=15.04 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=13.53 liquidity=39207256.0 spike=0.58
- CNFN.CA: score=6.4 buy_ready=False sector_rank=19 price=3.98 support=4.09 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=14.55 liquidity=11317655.0 spike=1.0
- COMI.CA: score=9.52 buy_ready=False sector_rank=8 price=128.04 support=126.81 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.17 liquidity=292904704.0 spike=0.48
- COPR.CA: score=7.99 buy_ready=False sector_rank=16 price=0.45 support=0.46 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.34 liquidity=16255653.0 spike=0.48
- COSG.CA: score=6.99 buy_ready=False sector_rank=16 price=1.55 support=1.58 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.31 liquidity=15186712.0 spike=0.54
- CPCI.CA: score=14.98 buy_ready=False sector_rank=16 price=560.71 support=530.0 resistance=584.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=69.7 liquidity=5483596.5 spike=1.75
- CSAG.CA: score=9.24 buy_ready=False sector_rank=6 price=35.12 support=36.1 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=21.26 liquidity=9335164.0 spike=0.63
- DAPH.CA: score=7.99 buy_ready=False sector_rank=16 price=94.52 support=98.8 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=20.16 liquidity=29140678.0 spike=0.67
- DEIN.CA: score=5.99 buy_ready=False sector_rank=16 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=0.09 buy_ready=False sector_rank=15 price=24.48 support=24.73 resistance=29.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=23.64 liquidity=2866838.0 spike=0.54
- DSCW.CA: score=6.99 buy_ready=False sector_rank=16 price=1.68 support=1.71 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=16.67 liquidity=18546238.0 spike=0.81
- DTPP.CA: score=2.99 buy_ready=False sector_rank=16 price=294.75 support=290.0 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40848988.0 spike=0.49
- EALR.CA: score=1.81 buy_ready=False sector_rank=16 price=328.41 support=340.0 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=23.03 liquidity=4818935.0 spike=0.37
- EASB.CA: score=5.56 buy_ready=False sector_rank=16 price=6.96 support=7.03 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.26 liquidity=2572165.0 spike=0.16
- EAST.CA: score=7.22 buy_ready=False sector_rank=15 price=29.62 support=30.52 resistance=36.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=3.34 liquidity=48200288.0 spike=0.81
- EBSC.CA: score=-5.09 buy_ready=False sector_rank=16 price=1.73 support=1.65 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1919586.13 spike=0.18
- ECAP.CA: score=1.22 buy_ready=False sector_rank=16 price=30.21 support=30.0 resistance=34.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=15.36 liquidity=4223667.5 spike=0.51
- EDFM.CA: score=-1.68 buy_ready=False sector_rank=16 price=374.57 support=375.2 resistance=465.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=30.07 liquidity=328064.31 spike=0.19
- EEII.CA: score=9.05 buy_ready=False sector_rank=16 price=2.16 support=2.15 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=34.52 liquidity=12333091.0 spike=1.03
- EFIC.CA: score=7.54 buy_ready=False sector_rank=13 price=160.4 support=157.42 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.67 liquidity=63473936.0 spike=0.18
- EFID.CA: score=8.22 buy_ready=False sector_rank=15 price=28.34 support=28.56 resistance=32.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=33.73 liquidity=60089332.0 spike=0.85
- EFIH.CA: score=14.5 buy_ready=False sector_rank=9 price=22.01 support=22.16 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.7 liquidity=65492992.0 spike=1.19
- EGAL.CA: score=16.54 buy_ready=False sector_rank=13 price=340.63 support=340.0 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.06 liquidity=64381384.0 spike=0.96
- EGAS.CA: score=14.08 buy_ready=False sector_rank=4 price=55.99 support=53.62 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.13 liquidity=8783241.0 spike=0.65
- EGBE.CA: score=4.57 buy_ready=False sector_rank=8 price=0.51 support=0.49 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=48.91 liquidity=51207.82 spike=0.51
- EGCH.CA: score=13.54 buy_ready=False sector_rank=13 price=13.59 support=13.57 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.0 liquidity=105804944.0 spike=0.79
- EGSA.CA: score=14.43 buy_ready=False sector_rank=1 price=8.85 support=8.84 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=29497.65 spike=4.49
- EGTS.CA: score=19.83 buy_ready=False sector_rank=17 price=18.04 support=16.51 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.9 liquidity=30658010.0 spike=0.87
- EHDR.CA: score=7.99 buy_ready=False sector_rank=16 price=2.45 support=2.44 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=14.52 liquidity=10745235.0 spike=0.61
- ELEC.CA: score=6.4 buy_ready=False sector_rank=20 price=1.82 support=1.87 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.73 liquidity=48888936.0 spike=0.62
- ELKA.CA: score=6.99 buy_ready=False sector_rank=16 price=1.47 support=1.51 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=10.0 liquidity=12787059.0 spike=0.44
- ELNA.CA: score=-2.87 buy_ready=False sector_rank=16 price=35.22 support=33.47 resistance=38.99 source=Yahoo Finance as_of=2026-09-26T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=139541.64 spike=0.4
- ELSH.CA: score=7.99 buy_ready=False sector_rank=16 price=11.2 support=11.06 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=19.82 liquidity=27906200.0 spike=0.85
- ELWA.CA: score=-2.63 buy_ready=False sector_rank=16 price=1.58 support=1.57 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=8.0 liquidity=374359.19 spike=0.27
- EMFD.CA: score=7.83 buy_ready=False sector_rank=17 price=12.4 support=12.63 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.95 liquidity=94682824.0 spike=0.7
- ENGC.CA: score=7.99 buy_ready=False sector_rank=16 price=38.01 support=39.11 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=26.41 liquidity=12963550.0 spike=0.72
- EOSB.CA: score=8.0 buy_ready=False sector_rank=16 price=1.57 support=1.53 resistance=1.64 source=Yahoo Finance as_of=2026-09-26T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=4342.62 spike=0.07
- EPCO.CA: score=4.06 buy_ready=False sector_rank=16 price=9.75 support=9.71 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=34.14 liquidity=6064405.5 spike=0.41
- EPPK.CA: score=-6.59 buy_ready=False sector_rank=16 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=24.4 buy_ready=False sector_rank=1 price=135.6 support=112.5 resistance=140.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.23 liquidity=246676880.0 spike=0.86
- ETRS.CA: score=7.83 buy_ready=False sector_rank=16 price=10.04 support=10.32 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=22.75 liquidity=9837959.0 spike=0.78
- EXPA.CA: score=23.1 buy_ready=False sector_rank=8 price=21.55 support=20.22 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=54.64 liquidity=63713452.0 spike=1.79
- FAIT.CA: score=5.59 buy_ready=False sector_rank=8 price=43.04 support=38.48 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=29.18 liquidity=3067190.25 spike=0.5
- FAITA.CA: score=3.56 buy_ready=False sector_rank=8 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=37224.68 spike=0.93
- FERC.CA: score=1.21 buy_ready=False sector_rank=13 price=73.4 support=73.9 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=32.24 liquidity=3663382.0 spike=0.27
- FWRY.CA: score=8.12 buy_ready=False sector_rank=9 price=18.4 support=17.5 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=12.1 liquidity=49064944.0 spike=0.39
- GBCO.CA: score=15.82 buy_ready=False sector_rank=10 price=29.44 support=27.0 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=44.15 liquidity=44834540.0 spike=0.61
- GDWA.CA: score=6.99 buy_ready=False sector_rank=16 price=0.65 support=0.67 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=7.43 liquidity=31366124.0 spike=0.73
- GGCC.CA: score=4.84 buy_ready=False sector_rank=16 price=0.69 support=0.7 resistance=0.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.11 liquidity=6850114.0 spike=0.29
- GIHD.CA: score=2.99 buy_ready=False sector_rank=16 price=67.53 support=66.1 resistance=71.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12518832.0 spike=0.4
- GMCI.CA: score=-1.7 buy_ready=False sector_rank=16 price=1.57 support=1.62 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=12.5 liquidity=627015.56 spike=1.34
- GRCA.CA: score=3.91 buy_ready=False sector_rank=16 price=34.88 support=35.1 resistance=85.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=14.23 liquidity=6921192.0 spike=0.19
- GSSC.CA: score=-4.58 buy_ready=False sector_rank=16 price=269.96 support=246.0 resistance=289.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2425789.0 spike=0.3
- GTWL.CA: score=4.69 buy_ready=False sector_rank=16 price=189.94 support=168.44 resistance=208.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=238225648.0 spike=1.85
- HDBK.CA: score=16.52 buy_ready=False sector_rank=8 price=107.02 support=96.5 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=50.87 liquidity=23565556.0 spike=0.4
- HELI.CA: score=12.83 buy_ready=False sector_rank=17 price=7.4 support=7.59 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.44 liquidity=128676960.0 spike=0.8
- HRHO.CA: score=6.54 buy_ready=False sector_rank=19 price=23.4 support=23.6 resistance=26.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=8.46 liquidity=106337512.0 spike=1.07
- ICID.CA: score=11.22 buy_ready=False sector_rank=16 price=17.29 support=16.2 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.15 liquidity=5229283.0 spike=0.55
- IDRE.CA: score=7.99 buy_ready=False sector_rank=16 price=47.21 support=46.0 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.61 liquidity=10468113.0 spike=0.62
- IFAP.CA: score=7.19 buy_ready=False sector_rank=11 price=19.31 support=19.05 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=28.75 liquidity=9486367.0 spike=0.51
- INFI.CA: score=2.24 buy_ready=False sector_rank=16 price=115.8 support=104.0 resistance=123.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9247086.0 spike=0.51
- IRON.CA: score=7.54 buy_ready=False sector_rank=13 price=25.96 support=26.3 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=32.0 liquidity=12341028.0 spike=0.91
- ISMA.CA: score=2.43 buy_ready=False sector_rank=16 price=24.72 support=24.51 resistance=27.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9433771.0 spike=0.55
- ISMQ.CA: score=4.48 buy_ready=False sector_rank=13 price=7.72 support=7.7 resistance=8.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36117428.0 spike=1.47
- ISPH.CA: score=7.68 buy_ready=False sector_rank=18 price=11.7 support=11.5 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=14.51 liquidity=60075696.0 spike=0.87
- JUFO.CA: score=7.22 buy_ready=False sector_rank=15 price=25.01 support=25.5 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=21.27 liquidity=20444514.0 spike=0.97
- KABO.CA: score=13.6 buy_ready=False sector_rank=12 price=8.26 support=8.6 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.28 liquidity=15741314.0 spike=0.43
- KWIN.CA: score=2.99 buy_ready=False sector_rank=16 price=79.08 support=74.0 resistance=84.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11663179.0 spike=0.38
- KZPC.CA: score=10.03 buy_ready=False sector_rank=16 price=13.41 support=12.72 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.53 liquidity=4041808.25 spike=0.13
- LCSW.CA: score=8.49 buy_ready=False sector_rank=14 price=30.25 support=31.0 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=15.94 liquidity=10747803.0 spike=0.46
- LUTS.CA: score=2.99 buy_ready=False sector_rank=16 price=0.81 support=0.72 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=110060096.0 spike=0.93
- MAAL.CA: score=21.93 buy_ready=False sector_rank=16 price=11.14 support=8.18 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.03 liquidity=43040624.0 spike=1.97
- MASR.CA: score=7.99 buy_ready=False sector_rank=16 price=7.01 support=7.04 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=12.26 liquidity=60954008.0 spike=0.63
- MBSC.CA: score=3.49 buy_ready=False sector_rank=14 price=299.26 support=295.22 resistance=326.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23761734.0 spike=0.54
- MCQE.CA: score=4.27 buy_ready=False sector_rank=14 price=184.64 support=180.04 resistance=197.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35151876.0 spike=1.39
- MCRO.CA: score=7.99 buy_ready=False sector_rank=16 price=1.46 support=1.48 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.0 liquidity=44703888.0 spike=0.35
- MENA.CA: score=-1.39 buy_ready=False sector_rank=17 price=6.27 support=6.36 resistance=7.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=29.82 liquidity=782898.19 spike=0.5
- MEPA.CA: score=6.54 buy_ready=False sector_rank=16 price=1.64 support=1.7 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=13.79 liquidity=9546342.0 spike=0.24
- MFPC.CA: score=16.54 buy_ready=False sector_rank=13 price=46.04 support=40.55 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=39.62 liquidity=70326864.0 spike=0.41
- MFSC.CA: score=1.15 buy_ready=False sector_rank=16 price=47.22 support=45.22 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.61 liquidity=3158515.25 spike=0.69
- MHOT.CA: score=7.07 buy_ready=False sector_rank=5 price=17.27 support=17.23 resistance=19.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32332246.0 spike=1.95
- MICH.CA: score=7.99 buy_ready=False sector_rank=16 price=44.43 support=45.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=22.98 liquidity=11417669.0 spike=0.86
- MILS.CA: score=0.06 buy_ready=False sector_rank=16 price=171.65 support=165.5 resistance=182.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7069488.5 spike=0.36
- MIPH.CA: score=16.24 buy_ready=False sector_rank=18 price=791.85 support=700.2 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.43 liquidity=12055038.0 spike=1.28
- MOED.CA: score=6.99 buy_ready=False sector_rank=16 price=0.63 support=0.66 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=11.71 liquidity=16934036.0 spike=0.28
- MOIL.CA: score=9.47 buy_ready=False sector_rank=4 price=0.71 support=0.67 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=81.36 liquidity=178848.86 spike=0.73
- MOIN.CA: score=8.66 buy_ready=False sector_rank=16 price=35.26 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=25.02 liquidity=7670062.5 spike=0.26
- MOSC.CA: score=-4.86 buy_ready=False sector_rank=16 price=259.81 support=257.0 resistance=283.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2149761.75 spike=0.4
- MPCI.CA: score=7.99 buy_ready=False sector_rank=16 price=346.71 support=363.63 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=14.19 liquidity=119171328.0 spike=0.86
- MPCO.CA: score=16.71 buy_ready=False sector_rank=11 price=2.38 support=2.07 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.4 liquidity=170038880.0 spike=0.93
- MPRC.CA: score=8.55 buy_ready=False sector_rank=16 price=37.92 support=37.65 resistance=46.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=33.54 liquidity=41183240.0 spike=1.28
- MTIE.CA: score=7.82 buy_ready=False sector_rank=10 price=7.9 support=8.02 resistance=8.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.89 liquidity=21910468.0 spike=0.89
- NAHO.CA: score=6.0 buy_ready=False sector_rank=16 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=7664.29 spike=0.15
- NCCW.CA: score=3.45 buy_ready=False sector_rank=16 price=7.06 support=6.48 resistance=7.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=93279944.0 spike=1.23
- NEDA.CA: score=-1.69 buy_ready=False sector_rank=16 price=2.66 support=2.57 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=32.0 liquidity=317052.78 spike=0.33
- NHPS.CA: score=6.18 buy_ready=False sector_rank=16 price=71.66 support=72.52 resistance=92.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=29.86 liquidity=8192553.0 spike=0.53
- NINH.CA: score=7.99 buy_ready=False sector_rank=16 price=18.96 support=19.31 resistance=24.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=23.17 liquidity=14626485.0 spike=0.8
- NIPH.CA: score=12.68 buy_ready=False sector_rank=18 price=298.34 support=290.0 resistance=401.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.62 liquidity=116320600.0 spike=0.82
- OBRI.CA: score=2.99 buy_ready=False sector_rank=16 price=24.18 support=24.0 resistance=27.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12500878.0 spike=0.87
- OCDI.CA: score=7.83 buy_ready=False sector_rank=17 price=26.65 support=27.4 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=6.55 liquidity=30866036.0 spike=0.46
- OCPH.CA: score=1.63 buy_ready=False sector_rank=16 price=205.31 support=207.0 resistance=277.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=17.65 liquidity=4637097.5 spike=0.76
- ODIN.CA: score=6.97 buy_ready=False sector_rank=16 price=2.42 support=2.45 resistance=3.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=26.73 liquidity=8981555.0 spike=0.58
- OFH.CA: score=2.99 buy_ready=False sector_rank=16 price=0.84 support=0.83 resistance=0.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=84769808.0 spike=0.63
- OIH.CA: score=7.13 buy_ready=False sector_rank=3 price=1.85 support=1.7 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=150306912.0 spike=1.33
- OLFI.CA: score=8.0 buy_ready=False sector_rank=15 price=21.85 support=22.07 resistance=23.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.1 liquidity=24553510.0 spike=1.39
- ORAS.CA: score=4.6 buy_ready=False sector_rank=7 price=791.99 support=780.01 resistance=820.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=177026592.0 spike=1.0
- ORHD.CA: score=7.83 buy_ready=False sector_rank=17 price=38.71 support=39.1 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.69 liquidity=118792240.0 spike=0.7
- ORWE.CA: score=16.6 buy_ready=False sector_rank=12 price=26.9 support=25.76 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.43 liquidity=47260204.0 spike=0.84
- PHAR.CA: score=7.68 buy_ready=False sector_rank=18 price=104.72 support=107.0 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=16.98 liquidity=64942628.0 spike=0.7
- PHDC.CA: score=7.83 buy_ready=False sector_rank=17 price=12.53 support=12.71 resistance=15.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=12.99 liquidity=93131584.0 spike=0.65
- PHTV.CA: score=4.57 buy_ready=False sector_rank=16 price=340.16 support=311.27 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=48.09 liquidity=1574697.0 spike=0.97
- POUL.CA: score=5.5 buy_ready=False sector_rank=15 price=9.7 support=9.12 resistance=10.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=55180564.0 spike=2.14
- PRCL.CA: score=4.09 buy_ready=False sector_rank=14 price=26.89 support=26.33 resistance=28.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22175902.0 spike=1.3
- PRDC.CA: score=7.83 buy_ready=False sector_rank=17 price=7.09 support=6.91 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=11.57 liquidity=21814662.0 spike=0.39
- PRMH.CA: score=0.8 buy_ready=False sector_rank=16 price=2.33 support=2.35 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.09 liquidity=2808046.0 spike=0.4
- RACC.CA: score=3.12 buy_ready=False sector_rank=16 price=8.99 support=9.01 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=21.67 liquidity=6128437.0 spike=0.43
- RAKT.CA: score=-2.75 buy_ready=False sector_rank=16 price=22.08 support=21.2 resistance=23.0 source=Yahoo Finance as_of=2026-09-26T21:00:00+00:00 freshness=FRESH RSI=30.86 liquidity=197858.88 spike=1.03
- RAYA.CA: score=7.4 buy_ready=False sector_rank=21 price=6.28 support=6.32 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=18.37 liquidity=50333772.0 spike=0.93
- RMDA.CA: score=7.68 buy_ready=False sector_rank=18 price=5.47 support=4.83 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=19.46 liquidity=46069516.0 spike=0.76
- ROTO.CA: score=9.87 buy_ready=False sector_rank=16 price=39.45 support=35.02 resistance=45.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=21.72 liquidity=15035606.0 spike=1.94
- RREI.CA: score=0.05 buy_ready=False sector_rank=16 price=3.86 support=3.86 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=27.68 liquidity=2055673.0 spike=0.13
- RTVC.CA: score=0.22 buy_ready=False sector_rank=16 price=3.53 support=3.6 resistance=4.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=21.62 liquidity=3027862.75 spike=1.1
- RUBX.CA: score=2.99 buy_ready=False sector_rank=16 price=15.14 support=14.72 resistance=16.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=52891304.0 spike=0.83
- SAUD.CA: score=14.52 buy_ready=False sector_rank=8 price=21.87 support=22.21 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=39.89 liquidity=13475043.0 spike=0.66
- SCEM.CA: score=8.49 buy_ready=False sector_rank=14 price=78.26 support=80.15 resistance=105.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=4.08 liquidity=58012676.0 spike=0.7
- SCFM.CA: score=-1.18 buy_ready=False sector_rank=16 price=239.08 support=242.4 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=17.48 liquidity=1827914.75 spike=0.29
- SCTS.CA: score=3.76 buy_ready=False sector_rank=2 price=547.93 support=556.5 resistance=639.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=20.65 liquidity=997862.44 spike=0.42
- SDTI.CA: score=20.43 buy_ready=False sector_rank=16 price=87.89 support=68.57 resistance=91.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.01 liquidity=83420320.0 spike=2.72
- SEIG.CA: score=-1.45 buy_ready=False sector_rank=16 price=215.07 support=218.02 resistance=271.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.56 liquidity=557605.81 spike=0.3
- SIPC.CA: score=2.99 buy_ready=False sector_rank=16 price=4.33 support=4.22 resistance=4.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14452690.0 spike=0.2
- SKPC.CA: score=7.54 buy_ready=False sector_rank=13 price=16.25 support=16.3 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.86 liquidity=48679976.0 spike=0.35
- SMFR.CA: score=0.2 buy_ready=False sector_rank=16 price=214.42 support=205.2 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=12.68 liquidity=2209913.75 spike=0.3
- SNFC.CA: score=18.41 buy_ready=False sector_rank=16 price=11.4 support=10.26 resistance=11.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=66.46 liquidity=16821858.0 spike=1.21
- SPIN.CA: score=3.39 buy_ready=False sector_rank=12 price=16.0 support=15.7 resistance=20.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=15.1 liquidity=4793898.5 spike=0.6
- SPMD.CA: score=11.99 buy_ready=False sector_rank=16 price=0.38 support=0.38 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.3 liquidity=11891088.0 spike=0.16
- SUGR.CA: score=7.65 buy_ready=False sector_rank=15 price=53.4 support=55.0 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=36.29 liquidity=4427372.5 spike=0.13
- SVCE.CA: score=7.99 buy_ready=False sector_rank=16 price=9.82 support=9.6 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=9.94 liquidity=96626848.0 spike=0.49
- SWDY.CA: score=7.52 buy_ready=False sector_rank=20 price=112.36 support=112.6 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=10.72 liquidity=67678992.0 spike=1.06
- TALM.CA: score=20.76 buy_ready=False sector_rank=2 price=19.3 support=17.11 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.26 liquidity=24135562.0 spike=0.36
- TMGH.CA: score=6.83 buy_ready=False sector_rank=17 price=86.58 support=88.7 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=16.3 liquidity=276571936.0 spike=0.95
- TRTO.CA: score=-2.01 buy_ready=False sector_rank=16 price=0.05 support=0.05 resistance=0.08 source=Yahoo Finance as_of=2026-09-26T21:00:00+00:00 freshness=FRESH RSI=10.71 liquidity=1546.88 spike=0.05
- UEFM.CA: score=-5.48 buy_ready=False sector_rank=16 price=424.55 support=421.1 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1528802.63 spike=0.5
- UEGC.CA: score=6.99 buy_ready=False sector_rank=16 price=1.45 support=1.47 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=20.69 liquidity=28783762.0 spike=0.63
- UNIP.CA: score=6.32 buy_ready=False sector_rank=16 price=0.33 support=0.33 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=21.21 liquidity=8323719.0 spike=0.4
- UNIT.CA: score=6.74 buy_ready=False sector_rank=17 price=17.38 support=16.66 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=39.51 liquidity=3909185.25 spike=0.27
- WCDF.CA: score=-2.85 buy_ready=False sector_rank=16 price=618.73 support=575.5 resistance=660.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4158175.0 spike=0.79
- WKOL.CA: score=2.1 buy_ready=False sector_rank=16 price=297.55 support=307.5 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=22.45 liquidity=5103862.5 spike=0.38
- ZEOT.CA: score=-0.81 buy_ready=False sector_rank=16 price=11.12 support=10.6 resistance=11.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6174893.5 spike=1.01
- ZMID.CA: score=7.83 buy_ready=False sector_rank=17 price=7.75 support=7.75 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=19.62 liquidity=69285008.0 spike=0.38

## Backtesting Lite
- ETEL.CA: 180d return=95.8%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-09-26T21:00:00+00:00
- EXPA.CA: 180d return=43.87%, max drawdown=-10.49%, MA20>MA50 days last20=20, as_of=2026-09-26T21:00:00+00:00
- CIRA.CA: 180d return=126.49%, max drawdown=-16.44%, MA20>MA50 days last20=20, as_of=2026-09-26T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- EXPA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Export Development Bank of Egypt summary=Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- CIRA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Investment and Real Estate Development summary=CIRA Education take over 51% of L’École Française Hurghada; CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion; CIRA Education launches Middle East’s 1st initiative for care economy
  - CIRA Education take over 51% of L’École Française Hurghada: https://english.mubasher.info/news/4488666/CIRA-Education-take-over-51-of-L-%C3%89cole-Fran%C3%A7aise-Hurghada/
  - CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion: https://english.mubasher.info/news/4393636/CIRA-s-majority-shareholder-acquires-37-5-additional-equity-backs-regional-expansion/
  - CIRA Education launches Middle East’s 1st initiative for care economy: https://english.mubasher.info/news/4391766/CIRA-Education-launches-Middle-East-s-1st-initiative-for-care-economy/
- MAAL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Marseille Almasreia Alkhalegeya For Holding Investment SAE summary=Evidence rejected for MAAL.CA: source text did not clearly match MAAL.CA / Marseille Almasreia Alkhalegeya For Holding Investment SAE.
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- CANA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=635 sources=3 expected=Suez Canal Bank summary=Suez Canal Bank delivers EGP 1.6bn profits in Q1-26; Suez Canal Bank unveils details for previous dividends payout; Suez Canal Bank to distribute EGP 5bn bonus shares for 2025
  - Suez Canal Bank delivers EGP 1.6bn profits in Q1-26: https://english.mubasher.info/news/4611255/Suez-Canal-Bank-delivers-EGP-1-6bn-profits-in-Q1-26/
  - Suez Canal Bank unveils details for previous dividends payout: https://english.mubasher.info/news/4586807/Suez-Canal-Bank-unveils-details-for-previous-dividends-payout/
  - Suez Canal Bank to distribute EGP 5bn bonus shares for 2025: https://english.mubasher.info/news/4581661/Suez-Canal-Bank-to-distribute-EGP-5bn-bonus-shares-for-2025/
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.

## Warnings
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
- Evidence rejected for MAAL.CA: source text did not clearly match MAAL.CA / Marseille Almasreia Alkhalegeya For Holding Investment SAE.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
