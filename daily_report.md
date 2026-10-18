# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-10-18T11:01:45.910480+00:00
Generated Cairo: 2026-10-18 14:01
Run timing: target 09:15 Cairo | generated Cairo 2026-10-18 14:01 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-10-18 13:57

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 124/187
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, October 18
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 0.0% / above MA50 7.14%
- EGX70 regime: BEARISH / above MA20 3.45% / above MA50 17.24%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=621613568.0 spike=1.06 score=8.01
- ETEL.CA: liquidity=232987424.0 spike=0.87 score=21.47
- EGAL.CA: liquidity=203690656.0 spike=3.24 score=7.35
- UEGC.CA: liquidity=156201840.0 spike=3.7 score=9.55
- ORHD.CA: liquidity=148043264.0 spike=0.99 score=7.21

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are BEARISH with 0% sector breadth, triggering DEFENSIVE_NO_NEW_BUY risk mode; scanner highlights top‑ranked tickets despite no new BUY signal.
- Top tickets (INFI.CA, SIPC.CA, ETEL.CA) show constructive outlooks and liquidity accumulation spikes, but sit far above 20‑day support in a bearish market.
- Sector breadth is nil; leading sectors (Telecom, Transport & Logistics, Industrial) have limited MA‑above‑50 presence, reducing conviction for new longs.
- RSI readings vary (50‑72) with some overheated (AJWA.CA) and others neutral, indicating mixed short‑term momentum amid uncertainty.
- Given the defensive regime, the scanner maintains HOLD/LOW‑confidence stance; any near‑term move depends on whether support holds or resistance breaks.

## Top Liquidity Spikes
- INFI.CA: spike=4.28 liquidity=67956488.0 outlook=CONSTRUCTIVE score=62.37 buy_ready=False
- SEIG.CA: spike=3.93 liquidity=6752923.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- UEGC.CA: spike=3.7 liquidity=156201840.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ORWE.CA: spike=3.35 liquidity=138894864.0 outlook=NEUTRAL score=48 buy_ready=False
- EGAL.CA: spike=3.24 liquidity=203690656.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=3.67 5d=-1.22% 20d=4.32% aboveMA50=50.0%
- #2 Transportation & Logistics: score=2.6 5d=-0.55% 20d=4.02% aboveMA50=50.0%
- #3 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #4 General / Verified EGX Expansion: score=1.37 5d=0.0% 20d=0.0% aboveMA50=10.78%
- #5 Fintech & Payments: score=0.06 5d=-2.47% 20d=2.06% aboveMA50=0.0%
- #6 Non-bank Financial Services: score=-0.54 5d=-0.72% 20d=-5.82% aboveMA50=0.0%
- #7 Energy & Petrochemicals: score=-0.69 5d=-5.72% 20d=0.22% aboveMA50=33.33%
- #8 Textiles: score=-0.72 5d=-2.9% 20d=-3.12% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ETEL.CA: BULLISH_WATCH score=76.67 liquidity=TRADEABLE sector=LEADING risk=below MA20
- ALCN.CA: BULLISH_WATCH score=70.6 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20
- CPCI.CA: CONSTRUCTIVE score=68.37 liquidity=TRADEABLE sector=IMPROVING risk=overheated RSI
- SDTI.CA: CONSTRUCTIVE score=63.37 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended
- INFI.CA: CONSTRUCTIVE score=62.37 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA50; far above support
- SIPC.CA: CONSTRUCTIVE score=61.37 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; far above support; high short-term volatility
- RUBX.CA: CONSTRUCTIVE score=61.37 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; far above support; high short-term volatility
- KZPC.CA: CONSTRUCTIVE score=59.37 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; below MA20
- AMIA.CA: CONSTRUCTIVE score=59.37 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; below MA20
- ICID.CA: CONSTRUCTIVE score=59.37 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; below MA20

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=10.47 buy_ready=False sector_rank=4 price=230.06 support=225.0 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=25.33 liquidity=26048194.0 spike=1.46
- ABUK.CA: score=12.87 buy_ready=False sector_rank=20 price=84.11 support=83.0 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=44.33 liquidity=65664684.0 spike=0.71
- ACAMD.CA: score=18.55 buy_ready=False sector_rank=4 price=2.07 support=1.87 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=67.86 liquidity=38716304.0 spike=0.83
- ACGC.CA: score=8.72 buy_ready=False sector_rank=8 price=13.0 support=12.81 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=40.2 liquidity=5007085.5 spike=0.4
- ADCI.CA: score=0.17 buy_ready=False sector_rank=4 price=257.9 support=250.06 resistance=288.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=33.73 liquidity=621400.63 spike=0.3
- ADIB.CA: score=3.56 buy_ready=False sector_rank=11 price=44.54 support=44.53 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37476748.0 spike=0.48
- ADPC.CA: score=0.16 buy_ready=False sector_rank=4 price=3.07 support=3.05 resistance=3.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5615915.5 spike=0.38
- AFDI.CA: score=-2.86 buy_ready=False sector_rank=4 price=47.21 support=46.5 resistance=50.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2596444.75 spike=0.43
- AFMC.CA: score=-0.9 buy_ready=False sector_rank=4 price=124.81 support=124.0 resistance=132.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4547396.0 spike=0.23
- AJWA.CA: score=18.55 buy_ready=False sector_rank=4 price=222.0 support=176.0 resistance=227.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=89.12 liquidity=20885590.0 spike=0.7
- ALCN.CA: score=16.71 buy_ready=False sector_rank=2 price=32.35 support=30.7 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=51.2 liquidity=6672007.0 spike=0.19
- ALUM.CA: score=0.87 buy_ready=False sector_rank=4 price=20.58 support=20.52 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=29.94 liquidity=2317075.0 spike=0.5
- AMER.CA: score=3.21 buy_ready=False sector_rank=17 price=4.14 support=4.14 resistance=4.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30979212.0 spike=0.63
- AMES.CA: score=4.55 buy_ready=False sector_rank=4 price=35.65 support=35.57 resistance=38.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36472080.0 spike=0.45
- AMIA.CA: score=12.02 buy_ready=False sector_rank=4 price=18.49 support=17.2 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=52.51 liquidity=4472391.0 spike=0.24
- AMOC.CA: score=16.72 buy_ready=False sector_rank=7 price=13.11 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=51.0 liquidity=43283352.0 spike=0.35
- APSW.CA: score=4.15 buy_ready=False sector_rank=4 price=8.01 support=7.81 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=44.57 liquidity=603644.25 spike=0.93
- ARAB.CA: score=18.75 buy_ready=False sector_rank=17 price=0.26 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=72.55 liquidity=125710336.0 spike=1.27
- ARCC.CA: score=13.44 buy_ready=False sector_rank=13 price=65.47 support=60.01 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=49.86 liquidity=22368366.0 spike=0.72
- AREH.CA: score=5.04 buy_ready=False sector_rank=4 price=1.14 support=1.11 resistance=1.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=32.69 liquidity=6488209.5 spike=0.78
- ASCM.CA: score=2.73 buy_ready=False sector_rank=4 price=46.23 support=45.52 resistance=50.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8185302.0 spike=0.96
- ASPI.CA: score=4.55 buy_ready=False sector_rank=4 price=0.32 support=0.32 resistance=0.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24391386.0 spike=0.79
- ATLC.CA: score=2.03 buy_ready=False sector_rank=6 price=5.03 support=5.02 resistance=5.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8248766.5 spike=0.85
- ATQA.CA: score=2.87 buy_ready=False sector_rank=20 price=10.91 support=10.9 resistance=11.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28951446.0 spike=0.4
- AXPH.CA: score=3.03 buy_ready=False sector_rank=4 price=1337.53 support=1300.0 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=23.63 liquidity=3486871.0 spike=0.52
- BINV.CA: score=11.07 buy_ready=False sector_rank=19 price=57.99 support=52.11 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=57.37 liquidity=5182006.0 spike=0.25
- BIOC.CA: score=4.55 buy_ready=False sector_rank=4 price=276.93 support=268.0 resistance=305.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39380068.0 spike=0.39
- BTFH.CA: score=12.78 buy_ready=False sector_rank=6 price=2.64 support=2.55 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=44.78 liquidity=77135128.0 spike=0.74
- CAED.CA: score=0.09 buy_ready=False sector_rank=4 price=96.14 support=96.0 resistance=107.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5541661.0 spike=0.68
- CANA.CA: score=8.56 buy_ready=False sector_rank=11 price=42.58 support=41.7 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=32.48 liquidity=18120676.0 spike=0.73
- CCAP.CA: score=8.01 buy_ready=False sector_rank=19 price=5.97 support=6.04 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=22.75 liquidity=621613568.0 spike=1.06
- CCRS.CA: score=-0.19 buy_ready=False sector_rank=4 price=1.92 support=1.9 resistance=2.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5266054.5 spike=0.45
- CEFM.CA: score=5.29 buy_ready=False sector_rank=4 price=125.47 support=113.0 resistance=152.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=38.49 liquidity=745096.44 spike=0.28
- CERA.CA: score=13.55 buy_ready=False sector_rank=4 price=1.22 support=1.18 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=48.05 liquidity=61933664.0 spike=0.5
- CFGH.CA: score=-1.37 buy_ready=False sector_rank=4 price=0.11 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=9.09 liquidity=6303.18 spike=1.04
- CICH.CA: score=-1.64 buy_ready=False sector_rank=6 price=10.56 support=10.6 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=579333.31 spike=0.16
- CIEB.CA: score=5.69 buy_ready=False sector_rank=11 price=22.79 support=22.56 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=36.01 liquidity=3128012.5 spike=0.32
- CIRA.CA: score=1.15 buy_ready=False sector_rank=10 price=35.65 support=35.51 resistance=37.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7565139.5 spike=0.33
- CLHO.CA: score=3.13 buy_ready=False sector_rank=18 price=13.19 support=13.0 resistance=14.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20632000.0 spike=0.47
- CNFN.CA: score=10.38 buy_ready=False sector_rank=6 price=3.99 support=3.8 resistance=4.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=45.57 liquidity=5592027.0 spike=0.61
- COMI.CA: score=12.56 buy_ready=False sector_rank=11 price=123.0 support=120.0 resistance=134.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=39.38 liquidity=125468704.0 spike=0.23
- COPR.CA: score=2.63 buy_ready=False sector_rank=4 price=0.44 support=0.44 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8079312.5 spike=0.38
- COSG.CA: score=11.45 buy_ready=False sector_rank=4 price=1.41 support=1.34 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=35.0 liquidity=7901708.5 spike=0.52
- CPCI.CA: score=12.42 buy_ready=False sector_rank=4 price=588.59 support=532.24 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=77.64 liquidity=3876535.25 spike=0.93
- CSAG.CA: score=10.63 buy_ready=False sector_rank=2 price=34.98 support=34.06 resistance=39.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=3589573.0 spike=0.5
- DAPH.CA: score=4.55 buy_ready=False sector_rank=4 price=87.74 support=87.11 resistance=93.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16613651.0 spike=0.4
- DEIN.CA: score=7.55 buy_ready=False sector_rank=4 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 09:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37.26 spike=0.01
- DOMT.CA: score=-1.5 buy_ready=False sector_rank=16 price=23.0 support=22.85 resistance=27.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=31.95 liquidity=1235869.25 spike=0.28
- DSCW.CA: score=8.55 buy_ready=False sector_rank=4 price=1.55 support=1.55 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=10730215.0 spike=0.61
- DTPP.CA: score=4.55 buy_ready=False sector_rank=4 price=250.0 support=250.0 resistance=265.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26307218.0 spike=0.42
- EALR.CA: score=2.55 buy_ready=False sector_rank=4 price=303.04 support=290.17 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=30.09 liquidity=4003221.25 spike=0.53
- EASB.CA: score=-2.89 buy_ready=False sector_rank=4 price=6.44 support=6.11 resistance=6.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2561745.25 spike=0.5
- EAST.CA: score=14.26 buy_ready=False sector_rank=16 price=28.37 support=27.01 resistance=33.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=35.52 liquidity=12448596.0 spike=0.28
- EBSC.CA: score=-2.52 buy_ready=False sector_rank=4 price=1.5 support=1.45 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2650924.5 spike=1.14
- ECAP.CA: score=1.08 buy_ready=False sector_rank=4 price=27.8 support=27.5 resistance=32.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=26.3 liquidity=2533228.0 spike=0.6
- EDFM.CA: score=5.26 buy_ready=False sector_rank=4 price=388.68 support=335.2 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=48.78 liquidity=707396.13 spike=0.6
- EEII.CA: score=-1.46 buy_ready=False sector_rank=4 price=1.81 support=1.8 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3989222.0 spike=0.44
- EFIC.CA: score=6.87 buy_ready=False sector_rank=20 price=148.98 support=147.0 resistance=199.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=30.02 liquidity=14210527.0 spike=0.42
- EFID.CA: score=14.6 buy_ready=False sector_rank=16 price=18.31 support=18.07 resistance=31.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=40.89 liquidity=55777696.0 spike=1.17
- EFIH.CA: score=16.02 buy_ready=False sector_rank=5 price=23.55 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=59.32 liquidity=36506536.0 spike=0.54
- EGAL.CA: score=7.35 buy_ready=False sector_rank=20 price=283.25 support=283.03 resistance=305.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=203690656.0 spike=3.24
- EGAS.CA: score=8.38 buy_ready=False sector_rank=7 price=50.55 support=48.08 resistance=60.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=42.53 liquidity=4659343.5 spike=0.41
- EGBE.CA: score=3.62 buy_ready=False sector_rank=11 price=0.5 support=0.5 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=60428.26 spike=0.44
- EGCH.CA: score=2.87 buy_ready=False sector_rank=20 price=11.19 support=11.07 resistance=12.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=54245512.0 spike=0.67
- EGSA.CA: score=4.54 buy_ready=False sector_rank=1 price=8.81 support=8.8 resistance=9.09 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=25.64 liquidity=7488.5 spike=1.53
- EGTS.CA: score=7.21 buy_ready=False sector_rank=17 price=13.32 support=13.56 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=19.18 liquidity=16704951.0 spike=0.47
- EHDR.CA: score=1.32 buy_ready=False sector_rank=4 price=2.13 support=2.12 resistance=2.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6769985.0 spike=0.64
- ELEC.CA: score=7.33 buy_ready=False sector_rank=15 price=1.65 support=1.65 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=30.77 liquidity=28070548.0 spike=0.56
- ELKA.CA: score=5.29 buy_ready=False sector_rank=4 price=1.49 support=1.48 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17647508.0 spike=1.37
- ELNA.CA: score=7.19 buy_ready=False sector_rank=4 price=35.22 support=33.46 resistance=36.4 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=281266.93 spike=1.68
- ELSH.CA: score=2.22 buy_ready=False sector_rank=4 price=10.6 support=10.56 resistance=11.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7668091.0 spike=0.37
- ELWA.CA: score=8.66 buy_ready=False sector_rank=4 price=1.65 support=1.43 resistance=1.74 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=54.05 liquidity=110069.85 spike=0.24
- EMFD.CA: score=13.21 buy_ready=False sector_rank=17 price=11.65 support=11.7 resistance=14.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=35.01 liquidity=19318898.0 spike=0.31
- ENGC.CA: score=-0.77 buy_ready=False sector_rank=4 price=31.87 support=31.2 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4682902.5 spike=0.25
- EOSB.CA: score=9.55 buy_ready=False sector_rank=4 price=1.57 support=1.64 resistance=1.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=15 October 12:37 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=401.8 spike=0.01
- EPCO.CA: score=-3.67 buy_ready=False sector_rank=4 price=8.42 support=8.33 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1783940.13 spike=0.35
- EPPK.CA: score=-5.03 buy_ready=False sector_rank=4 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=21.47 buy_ready=False sector_rank=1 price=140.15 support=128.52 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=61.77 liquidity=232987424.0 spike=0.87
- ETRS.CA: score=7.19 buy_ready=False sector_rank=4 price=10.22 support=9.82 resistance=11.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=52.1 liquidity=2638721.75 spike=0.25
- EXPA.CA: score=7.56 buy_ready=False sector_rank=11 price=14.19 support=14.0 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=10.28 liquidity=28391394.0 spike=0.75
- FAIT.CA: score=5.29 buy_ready=False sector_rank=11 price=43.02 support=38.48 resistance=47.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=37.34 liquidity=1729723.5 spike=0.58
- FAITA.CA: score=10.6 buy_ready=False sector_rank=11 price=1.0 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=58.75 liquidity=36569.14 spike=0.9
- FERC.CA: score=-1.5 buy_ready=False sector_rank=20 price=66.96 support=66.72 resistance=82.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=26.04 liquidity=1628843.75 spike=0.3
- FWRY.CA: score=15.02 buy_ready=False sector_rank=5 price=18.23 support=17.5 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=50.59 liquidity=35603844.0 spike=0.31
- GBCO.CA: score=3.66 buy_ready=False sector_rank=9 price=28.83 support=28.7 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=86326320.0 spike=0.81
- GDWA.CA: score=4.55 buy_ready=False sector_rank=4 price=0.59 support=0.59 resistance=0.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11463417.0 spike=0.57
- GGCC.CA: score=6.85 buy_ready=False sector_rank=4 price=0.64 support=0.64 resistance=0.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32680888.0 spike=2.15
- GIHD.CA: score=0.62 buy_ready=False sector_rank=4 price=50.01 support=49.51 resistance=53.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6074887.5 spike=0.32
- GMCI.CA: score=5.92 buy_ready=False sector_rank=4 price=1.54 support=1.49 resistance=1.78 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=36.21 liquidity=371782.17 spike=0.95
- GRCA.CA: score=-2.96 buy_ready=False sector_rank=4 price=31.17 support=31.0 resistance=33.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2487436.75 spike=0.29
- GSSC.CA: score=6.4 buy_ready=False sector_rank=4 price=266.24 support=246.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=40.19 liquidity=1856044.88 spike=0.61
- GTWL.CA: score=4.55 buy_ready=False sector_rank=4 price=123.27 support=120.6 resistance=129.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=74757736.0 spike=0.46
- HDBK.CA: score=7.56 buy_ready=False sector_rank=11 price=98.21 support=98.01 resistance=121.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=33.86 liquidity=20088154.0 spike=0.84
- HELI.CA: score=13.21 buy_ready=False sector_rank=17 price=7.05 support=6.92 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=38110308.0 spike=0.39
- HRHO.CA: score=3.78 buy_ready=False sector_rank=6 price=24.5 support=24.49 resistance=25.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=56180244.0 spike=0.42
- ICID.CA: score=10.67 buy_ready=False sector_rank=4 price=17.38 support=16.52 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=53.35 liquidity=3126528.25 spike=0.38
- IDRE.CA: score=-3.48 buy_ready=False sector_rank=4 price=41.07 support=40.17 resistance=43.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1967616.5 spike=0.15
- IFAP.CA: score=1.05 buy_ready=False sector_rank=12 price=18.23 support=17.17 resistance=21.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=27.7 liquidity=3534272.25 spike=0.5
- INFI.CA: score=23.55 buy_ready=False sector_rank=4 price=129.19 support=104.0 resistance=142.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=50.24 liquidity=67956488.0 spike=4.28
- IRON.CA: score=11.87 buy_ready=False sector_rank=20 price=25.54 support=25.01 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=43.3 liquidity=10229489.0 spike=0.98
- ISMA.CA: score=-2.4 buy_ready=False sector_rank=4 price=20.56 support=20.05 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3051412.75 spike=0.41
- ISMQ.CA: score=5.37 buy_ready=False sector_rank=20 price=7.22 support=7.14 resistance=9.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=32.5 liquidity=8497702.0 spike=0.45
- ISPH.CA: score=12.13 buy_ready=False sector_rank=18 price=10.71 support=10.03 resistance=12.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=43.8 liquidity=15820843.0 spike=0.29
- JUFO.CA: score=12.42 buy_ready=False sector_rank=16 price=23.36 support=23.5 resistance=27.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=35.62 liquidity=18429232.0 spike=1.08
- KABO.CA: score=3.71 buy_ready=False sector_rank=8 price=7.0 support=6.92 resistance=8.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13287041.0 spike=0.58
- KWIN.CA: score=-3.54 buy_ready=False sector_rank=4 price=62.87 support=62.0 resistance=66.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1909536.38 spike=0.22
- KZPC.CA: score=12.87 buy_ready=False sector_rank=4 price=12.9 support=12.15 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=44.59 liquidity=5318907.0 spike=0.59
- LCSW.CA: score=11.82 buy_ready=False sector_rank=13 price=32.72 support=28.86 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=61.67 liquidity=6379782.5 spike=0.31
- LUTS.CA: score=4.55 buy_ready=False sector_rank=4 price=0.68 support=0.68 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36051068.0 spike=0.64
- MAAL.CA: score=4.55 buy_ready=False sector_rank=4 price=7.83 support=7.7 resistance=8.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13816093.0 spike=0.55
- MASR.CA: score=4.55 buy_ready=False sector_rank=4 price=7.07 support=7.03 resistance=7.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24003544.0 spike=0.42
- MBSC.CA: score=15.44 buy_ready=False sector_rank=13 price=338.99 support=288.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=66907832.0 spike=0.78
- MCQE.CA: score=12.44 buy_ready=False sector_rank=13 price=170.34 support=170.0 resistance=224.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=36.32 liquidity=51708148.0 spike=0.93
- MCRO.CA: score=5.01 buy_ready=False sector_rank=4 price=1.29 support=1.29 resistance=1.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=66987720.0 spike=1.23
- MENA.CA: score=2.66 buy_ready=False sector_rank=17 price=5.73 support=5.57 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=35.53 liquidity=450060.41 spike=0.26
- MEPA.CA: score=7.54 buy_ready=False sector_rank=4 price=1.57 support=1.53 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=40.28 liquidity=3992411.75 spike=0.41
- MFPC.CA: score=12.87 buy_ready=False sector_rank=20 price=42.99 support=42.0 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=37.35 liquidity=39718860.0 spike=0.48
- MFSC.CA: score=-0.99 buy_ready=False sector_rank=4 price=38.21 support=36.25 resistance=49.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=18.42 liquidity=460459.59 spike=0.2
- MHOT.CA: score=4.59 buy_ready=False sector_rank=14 price=15.85 support=15.08 resistance=19.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=30.38 liquidity=7177653.5 spike=0.41
- MICH.CA: score=9.75 buy_ready=False sector_rank=4 price=39.74 support=38.91 resistance=47.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=39.22 liquidity=5200955.0 spike=0.6
- MILS.CA: score=3.25 buy_ready=False sector_rank=4 price=148.71 support=147.06 resistance=207.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=28.06 liquidity=3697432.25 spike=0.47
- MIPH.CA: score=5.79 buy_ready=False sector_rank=18 price=705.77 support=686.2 resistance=798.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19608388.0 spike=2.33
- MOED.CA: score=8.19 buy_ready=False sector_rank=4 price=0.58 support=0.57 resistance=0.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=32.55 liquidity=9646047.0 spike=0.58
- MOIL.CA: score=-1.17 buy_ready=False sector_rank=7 price=0.66 support=0.63 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=31.08 liquidity=104395.23 spike=0.37
- MOIN.CA: score=1.76 buy_ready=False sector_rank=4 price=29.4 support=29.11 resistance=31.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7216550.0 spike=0.69
- MOSC.CA: score=5.86 buy_ready=False sector_rank=4 price=254.45 support=231.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=40.15 liquidity=1316518.25 spike=0.34
- MPCI.CA: score=9.55 buy_ready=False sector_rank=4 price=305.37 support=294.2 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=28.71 liquidity=82745568.0 spike=0.82
- MPCO.CA: score=3.52 buy_ready=False sector_rank=12 price=1.89 support=1.86 resistance=2.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=54050416.0 spike=0.42
- MPRC.CA: score=15.31 buy_ready=False sector_rank=4 price=35.01 support=34.53 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=35.94 liquidity=21811610.0 spike=1.38
- MTIE.CA: score=12.66 buy_ready=False sector_rank=9 price=7.3 support=7.27 resistance=8.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=37.85 liquidity=10105661.0 spike=0.55
- NAHO.CA: score=6.08 buy_ready=False sector_rank=4 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=50227.81 spike=1.74
- NCCW.CA: score=4.55 buy_ready=False sector_rank=4 price=5.57 support=5.56 resistance=5.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10535342.0 spike=0.26
- NEDA.CA: score=-0.39 buy_ready=False sector_rank=4 price=2.6 support=2.47 resistance=2.8 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=32.14 liquidity=59974.2 spike=0.09
- NHPS.CA: score=3.77 buy_ready=False sector_rank=4 price=62.19 support=63.02 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=29.36 liquidity=5226471.0 spike=0.36
- NINH.CA: score=8.51 buy_ready=False sector_rank=4 price=15.82 support=16.02 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=21.16 liquidity=9958452.0 spike=0.7
- NIPH.CA: score=8.13 buy_ready=False sector_rank=18 price=261.44 support=241.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=29.65 liquidity=79550200.0 spike=0.66
- OBRI.CA: score=2.04 buy_ready=False sector_rank=4 price=25.02 support=25.0 resistance=27.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7491906.0 spike=0.52
- OCDI.CA: score=13.21 buy_ready=False sector_rank=17 price=24.99 support=24.2 resistance=30.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=38.69 liquidity=27756080.0 spike=0.65
- OCPH.CA: score=-0.29 buy_ready=False sector_rank=4 price=195.2 support=190.0 resistance=247.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=34.95 liquidity=1158924.75 spike=0.34
- ODIN.CA: score=-2.27 buy_ready=False sector_rank=4 price=2.12 support=2.1 resistance=2.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3185582.5 spike=0.37
- OFH.CA: score=4.55 buy_ready=False sector_rank=4 price=0.74 support=0.74 resistance=0.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11939523.0 spike=0.13
- OIH.CA: score=7.89 buy_ready=False sector_rank=19 price=1.75 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=30642232.0 spike=0.37
- OLFI.CA: score=-0.14 buy_ready=False sector_rank=16 price=20.37 support=19.8 resistance=23.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=24.92 liquidity=2597874.75 spike=0.15
- ORAS.CA: score=5.6 buy_ready=False sector_rank=3 price=850.12 support=850.0 resistance=893.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=106391416.0 spike=1.0
- ORHD.CA: score=7.21 buy_ready=False sector_rank=17 price=10.2 support=10.01 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=2.79 liquidity=148043264.0 spike=0.99
- ORWE.CA: score=18.41 buy_ready=False sector_rank=8 price=26.85 support=26.01 resistance=28.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=58.11 liquidity=138894864.0 spike=3.35
- PHAR.CA: score=13.13 buy_ready=False sector_rank=18 price=102.71 support=102.0 resistance=122.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=45.41 liquidity=23903320.0 spike=0.37
- PHDC.CA: score=15.21 buy_ready=False sector_rank=17 price=12.41 support=12.35 resistance=13.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=35.62 liquidity=28674974.0 spike=0.3
- PHTV.CA: score=5.02 buy_ready=False sector_rank=4 price=338.3 support=315.0 resistance=377.96 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=41.91 liquidity=474634.88 spike=0.55
- POUL.CA: score=7.26 buy_ready=False sector_rank=16 price=9.83 support=9.12 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=3.27 liquidity=12706898.0 spike=0.4
- PRCL.CA: score=-2.81 buy_ready=False sector_rank=13 price=20.47 support=20.21 resistance=22.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3745235.0 spike=0.35
- PRDC.CA: score=3.21 buy_ready=False sector_rank=17 price=6.01 support=6.0 resistance=6.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16615571.0 spike=0.46
- PRMH.CA: score=-3.93 buy_ready=False sector_rank=4 price=1.9 support=1.87 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1522086.38 spike=0.38
- RACC.CA: score=7.5 buy_ready=False sector_rank=4 price=8.68 support=8.51 resistance=10.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=42.67 liquidity=3955795.0 spike=0.6
- RAKT.CA: score=3.86 buy_ready=False sector_rank=4 price=22.06 support=20.26 resistance=25.08 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=49.81 liquidity=308795.87 spike=0.87
- RAYA.CA: score=6.4 buy_ready=False sector_rank=21 price=5.83 support=5.7 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=31.66 liquidity=10524643.0 spike=0.29
- RMDA.CA: score=8.17 buy_ready=False sector_rank=18 price=4.95 support=4.83 resistance=6.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=27.97 liquidity=26608256.0 spike=1.02
- ROTO.CA: score=8.36 buy_ready=False sector_rank=4 price=36.0 support=35.56 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=42.3 liquidity=4816271.0 spike=0.57
- RREI.CA: score=-2.65 buy_ready=False sector_rank=4 price=3.38 support=3.35 resistance=3.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2800180.5 spike=0.3
- RTVC.CA: score=0.58 buy_ready=False sector_rank=4 price=3.3 support=3.31 resistance=4.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=34.37 liquidity=2031721.0 spike=0.75
- RUBX.CA: score=19.55 buy_ready=False sector_rank=4 price=16.14 support=12.9 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=44.48 liquidity=63602388.0 spike=0.62
- SAUD.CA: score=13.56 buy_ready=False sector_rank=11 price=21.42 support=20.2 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=39.87 liquidity=19670630.0 spike=0.93
- SCEM.CA: score=17.9 buy_ready=False sector_rank=13 price=85.65 support=74.55 resistance=95.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=57.0 liquidity=78942928.0 spike=1.23
- SCFM.CA: score=-0.95 buy_ready=False sector_rank=4 price=229.6 support=220.35 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=33.98 liquidity=506344.06 spike=0.28
- SCTS.CA: score=-1.05 buy_ready=False sector_rank=10 price=482.31 support=463.13 resistance=615.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=24.24 liquidity=358780.72 spike=0.36
- SDTI.CA: score=19.51 buy_ready=False sector_rank=4 price=84.0 support=73.3 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=63.73 liquidity=9964888.0 spike=0.29
- SEIG.CA: score=6.3 buy_ready=False sector_rank=4 price=204.03 support=193.0 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6752923.0 spike=3.93
- SIPC.CA: score=21.55 buy_ready=False sector_rank=4 price=5.48 support=4.22 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=54.87 liquidity=33558024.0 spike=0.63
- SKPC.CA: score=6.87 buy_ready=False sector_rank=20 price=14.84 support=14.98 resistance=18.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=24.66 liquidity=21499210.0 spike=0.28
- SMFR.CA: score=5.26 buy_ready=False sector_rank=4 price=196.37 support=181.6 resistance=255.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=38.5 liquidity=1708469.13 spike=0.48
- SNFC.CA: score=10.38 buy_ready=False sector_rank=4 price=11.08 support=10.81 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=41.25 liquidity=2835492.75 spike=0.25
- SPIN.CA: score=2.19 buy_ready=False sector_rank=8 price=14.3 support=14.8 resistance=18.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=28.97 liquidity=4478609.0 spike=0.84
- SPMD.CA: score=8.55 buy_ready=False sector_rank=4 price=0.35 support=0.34 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=31.82 liquidity=11188688.0 spike=0.52
- SUGR.CA: score=3.68 buy_ready=False sector_rank=16 price=55.4 support=55.14 resistance=58.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12491436.0 spike=1.21
- SVCE.CA: score=9.55 buy_ready=False sector_rank=4 price=9.12 support=8.81 resistance=12.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=31.55 liquidity=44603420.0 spike=0.54
- SWDY.CA: score=3.33 buy_ready=False sector_rank=15 price=106.2 support=106.01 resistance=112.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39757128.0 spike=0.66
- TALM.CA: score=16.59 buy_ready=False sector_rank=10 price=20.47 support=18.71 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=55.34 liquidity=11151459.0 spike=0.29
- TMGH.CA: score=7.21 buy_ready=False sector_rank=17 price=82.41 support=81.22 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=21.82 liquidity=69984648.0 spike=0.31
- TRTO.CA: score=11.92 buy_ready=False sector_rank=4 price=0.07 support=0.05 resistance=0.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=11648.73 spike=1.18
- UEFM.CA: score=6.4 buy_ready=False sector_rank=4 price=479.55 support=407.57 resistance=550.0 source=Yahoo Finance as_of=2026-10-14T21:00:00+00:00 freshness=FRESH RSI=54.34 liquidity=850242.13 spike=0.27
- UEGC.CA: score=9.55 buy_ready=False sector_rank=4 price=1.58 support=1.56 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=156201840.0 spike=3.7
- UNIP.CA: score=7.79 buy_ready=False sector_rank=4 price=0.32 support=0.31 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=38.89 liquidity=4241290.0 spike=0.44
- UNIT.CA: score=-4.94 buy_ready=False sector_rank=17 price=16.01 support=16.0 resistance=17.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1850085.38 spike=0.34
- WCDF.CA: score=0.26 buy_ready=False sector_rank=4 price=519.34 support=515.0 resistance=719.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=21.81 liquidity=1715022.0 spike=0.54
- WKOL.CA: score=6.97 buy_ready=False sector_rank=4 price=272.82 support=266.18 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=27.55 liquidity=8424300.0 spike=0.83
- ZEOT.CA: score=1.0 buy_ready=False sector_rank=4 price=10.42 support=10.4 resistance=11.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6447968.5 spike=0.8
- ZMID.CA: score=4.15 buy_ready=False sector_rank=17 price=6.8 support=6.76 resistance=7.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=146812000.0 spike=1.47

## Backtesting Lite
- INFI.CA: 180d return=12.06%, max drawdown=-37.66%, MA20>MA50 days last20=8, as_of=2026-10-14T21:00:00+00:00
- SIPC.CA: 180d return=67.95%, max drawdown=-31.27%, MA20>MA50 days last20=20, as_of=2026-10-14T21:00:00+00:00
- ETEL.CA: 180d return=117.39%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-10-14T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- INFI.CA: status=RECENT_ACCEPTED latest=2026-01-01 age_days=290 sources=3 expected=Ismailia National Co. for Food Industries summary=Foodico stock targets higher levels; Foodico plans to log nearly EGP 70.5m profits in 2026; Foodico to secure EGP 12m loan from national bank
  - Foodico stock targets higher levels: https://english.mubasher.info/news/4564894/Foodico-stock-targets-higher-levels/
  - Foodico plans to log nearly EGP 70.5m profits in 2026: https://english.mubasher.info/news/4541309/Foodico-plans-to-log-nearly-EGP-70-5m-profits-in-2026/
  - Foodico to secure EGP 12m loan from national bank: https://english.mubasher.info/news/3888447/Foodico-to-secure-EGP-12m-loan-from-national-bank/
- SIPC.CA: status=OLD_ACCEPTED latest=2020-01-01 age_days=2482 sources=3 expected=Sabaa International Company for Pharmaceutical and Chemical Industry summary=Sabaa Pharmaceutical&#39;s shareholders approve capital raise via bonus issue; FRA approves Sabaa Pharmaceutical&#39;s capital raise; Sabaa Pharmaceutical&#39;s profit leaps 76% in 2020 initial results
  - Sabaa Pharmaceutical&#39;s shareholders approve capital raise via bonus issue: https://english.mubasher.info/news/3809286/Sabaa-Pharmaceutical-s-shareholders-approve-capital-raise-via-bonus-issue/
  - FRA approves Sabaa Pharmaceutical&#39;s capital raise: https://english.mubasher.info/news/3789753/FRA-approves-Sabaa-Pharmaceutical-s-capital-raise/
  - Sabaa Pharmaceutical&#39;s profit leaps 76% in 2020 initial results: https://english.mubasher.info/news/3779465/Sabaa-Pharmaceutical-s-profit-leaps-76-in-2020-initial-results/
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- RUBX.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Rubex International for Plastic and Acrylic Manufacturing summary=Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- SDTI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=SHARM DREAMS Co. for Touristic Investment S.A.E summary=Sharm Dreams stock maintains strong uptrend - Analysis; Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis; Sharm Dreams stock hits historic level halting driving buying force
  - Sharm Dreams stock maintains strong uptrend - Analysis: https://english.mubasher.info/news/4577977/Sharm-Dreams-stock-maintains-strong-uptrend-Analysis/
  - Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis: https://english.mubasher.info/news/4547831/Sharm-Dreams-stock-is-experiencing-sideways-movement-amid-anticipation-of-next-trend-Analysis/
  - Sharm Dreams stock hits historic level halting driving buying force: https://english.mubasher.info/news/4529096/Sharm-Dreams-stock-hits-historic-level-halting-driving-buying-force/
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- ACAMD.CA: status=OLD_ACCEPTED latest=2020-01-01 age_days=2482 sources=3 expected=Arab Co.,for asset management and development summary=Arab Company for Asset Management shifts to EGP 7m net profits in 9M-25; Arab Co. for Asset Management approves offer to sell land in El-Minya; Arab Co. Asset Management swings to loss in 2020
  - Arab Company for Asset Management shifts to EGP 7m net profits in 9M-25: https://english.mubasher.info/news/4543171/Arab-Company-for-Asset-Management-shifts-to-EGP-7m-net-profits-in-9M-25/
  - Arab Co. for Asset Management approves offer to sell land in El-Minya: https://english.mubasher.info/news/3777445/Arab-Co-for-Asset-Management-approves-offer-to-sell-land-in-El-Minya/
  - Arab Co. Asset Management swings to loss in 2020: https://english.mubasher.info/news/3767136/Arab-Co-Asset-Management-swings-to-loss-in-2020/
- AJWA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=AJWA For Food Industries Co. Egypt summary=Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture; AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3; Ajwa Egypt turns to losses in 9M
  - Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture: https://english.mubasher.info/news/4532004/Ajwa-Egypt-s-board-approves-capital-increase-to-EGP-500m-joins-new-food-venture/
  - AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3: https://english.mubasher.info/news/4527545/AJWA-Egypt-s-standalone-net-profits-retreat-to-EGP-14m-in-9M-25-amid-shift-to-profitability-in-Q3/
  - Ajwa Egypt turns to losses in 9M: https://english.mubasher.info/news/3883210/Ajwa-Egypt-turns-to-losses-in-9M/

## Warnings
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for SIPC.CA matches the company but appears old; latest detected date is 2020-01-01.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Evidence for SDTI.CA matches the company but no source/report date was detected.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence for ACAMD.CA matches the company but appears old; latest detected date is 2020-01-01.
- Evidence for AJWA.CA matches the company but no source/report date was detected.
