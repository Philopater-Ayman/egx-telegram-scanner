# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-06-14T10:12:05.601608+00:00
Generated Cairo: 2026-06-14 13:12
Run timing: target 09:15 Cairo | generated Cairo 2026-06-14 13:12 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-06-14 12:54

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 187/190
- Top sector: Automotive & Distribution

## Market Context
- Market trend: Unavailable
- Source: Market context unavailable
- As of: None
- Freshness: MISSING
- EGX30 regime: BEARISH / above MA20 4.76% / above MA50 38.1%
- EGX70 regime: BEARISH / above MA20 42.5% / above MA50 77.5%
- Sector breadth: 4.76%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=581263489.8 spike=0.78 score=18.32
- COMI.CA: liquidity=479660290.25 spike=0.93 score=14.38
- FWRY.CA: liquidity=285162306.78 spike=1.16 score=7.82
- TMGH.CA: liquidity=274423353.59 spike=0.7 score=14.44
- ABUK.CA: liquidity=147343590.0 spike=1.4 score=9.38

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The local scanner stays on HOLD because both EGX30 and EGX70 are in a bearish regime with weak sector breadth (4.76%). Liquidity is cooling on many top‑ranked stocks and RSI levels are high, so the market risk mode is DEFENSIVE_NO_NEW_BUY. Expect limited upside and heightened uncertainty over the next 1‑3 days.
- EGX30/EGX70 trends bearish; median 5‑day returns negative, breadth below MA20/MA50.
- Top‑ranked tickets show constructive or bullish‑watch outlooks but face cooling liquidity and overheated RSI.
- Leading sectors (Automotive, Textiles, Real Estate) show mixed returns and limited above‑MA20 coverage.
- Risk mode is defensive; new buys are not supported until market breadth improves.
- Short‑term outlook remains uncertain; monitor liquidity spikes and support/resistance breaches.

## Top Liquidity Spikes
- EASB.CA: spike=10.53 liquidity=11115410.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- TRTO.CA: spike=8.0 liquidity=5988.11 outlook=NEUTRAL score=39.33 buy_ready=False
- LUTS.CA: spike=6.25 liquidity=127604856.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ANFI.CA: spike=3.32 liquidity=143236051.08 outlook=BULLISH_WATCH score=71.33 buy_ready=False
- CFGH.CA: spike=3.0 liquidity=18482.3 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=4.73 5d=1.06% 20d=-4.12% aboveMA50=100.0%
- #2 Textiles: score=4.13 5d=-1.86% 20d=4.28% aboveMA50=75.0%
- #3 Real Estate: score=3.61 5d=-3.97% 20d=1.4% aboveMA50=92.31%
- #4 Education: score=3.58 5d=-2.15% 20d=-3.64% aboveMA50=100.0%
- #5 Investment Holding: score=3.29 5d=-4.1% 20d=7.16% aboveMA50=66.67%
- #6 Energy & Petrochemicals: score=2.99 5d=-1.29% 20d=0.1% aboveMA50=75.0%
- #7 General / Verified EGX Expansion: score=2.33 5d=-2.54% 20d=-2.19% aboveMA50=66.35%
- #8 Healthcare: score=2.11 5d=-3.22% 20d=-4.87% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- KABO.CA: BULLISH_WATCH score=84.13 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ZMID.CA: BULLISH_WATCH score=83.61 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MENA.CA: BULLISH_WATCH score=83.61 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- SDTI.CA: BULLISH_WATCH score=81.33 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- COSG.CA: BULLISH_WATCH score=78.33 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MPRC.CA: BULLISH_WATCH score=78.33 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MEPA.CA: BULLISH_WATCH score=78.33 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- EEII.CA: BULLISH_WATCH score=78.33 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- KZPC.CA: BULLISH_WATCH score=78.33 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ROTO.CA: BULLISH_WATCH score=78.33 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=11.47 buy_ready=False sector_rank=7 price=207.0 support=195.1 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=56.02 liquidity=1537226.13 spike=0.2
- ABUK.CA: score=9.38 buy_ready=False sector_rank=19 price=76.5 support=75.8 resistance=90.87 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=17.05 liquidity=147343590.0 spike=1.4
- ACAMD.CA: score=19.93 buy_ready=False sector_rank=7 price=2.35 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=64.18 liquidity=81063496.0 spike=0.63
- ACGC.CA: score=9.72 buy_ready=False sector_rank=2 price=9.38 support=8.89 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=33.8 liquidity=4065142.75 spike=0.07
- ADCI.CA: score=22.59 buy_ready=False sector_rank=7 price=227.56 support=202.22 resistance=228.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=71.49 liquidity=15058975.0 spike=2.33
- ADIB.CA: score=14.38 buy_ready=False sector_rank=11 price=44.1 support=44.01 resistance=49.9 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=36.64 liquidity=61289207.68 spike=0.65
- ADPC.CA: score=4.17 buy_ready=False sector_rank=7 price=3.57 support=3.45 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=27.91 liquidity=4241068.5 spike=0.17
- AFDI.CA: score=13.46 buy_ready=False sector_rank=7 price=41.5 support=40.15 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=43.03 liquidity=5531070.5 spike=0.31
- AFMC.CA: score=8.73 buy_ready=False sector_rank=7 price=70.75 support=67.0 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=43.18 liquidity=796127.75 spike=0.12
- AJWA.CA: score=20.27 buy_ready=False sector_rank=7 price=159.0 support=130.01 resistance=154.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=86.04 liquidity=31273988.0 spike=1.67
- ALCN.CA: score=13.61 buy_ready=False sector_rank=18 price=28.7 support=25.51 resistance=30.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=42.22 liquidity=10983477.0 spike=0.58
- ALUM.CA: score=10.44 buy_ready=False sector_rank=7 price=23.81 support=23.05 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=46.41 liquidity=2505985.75 spike=0.12
- AMER.CA: score=19.44 buy_ready=False sector_rank=3 price=2.66 support=2.52 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=30078784.0 spike=0.27
- AMES.CA: score=4.29 buy_ready=False sector_rank=7 price=49.62 support=48.0 resistance=57.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=14.17 liquidity=1355826.63 spike=0.26
- AMIA.CA: score=17.56 buy_ready=False sector_rank=7 price=9.13 support=8.54 resistance=9.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:11 AM market time freshness=DELAYED_CURRENT RSI=64.1 liquidity=7627326.0 spike=0.34
- AMOC.CA: score=10.2 buy_ready=False sector_rank=6 price=7.92 support=7.92 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=29.46 liquidity=35598596.0 spike=0.46
- ANFI.CA: score=23.57 buy_ready=False sector_rank=7 price=21.65 support=13.52 resistance=22.8 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=91.11 liquidity=143236051.08 spike=3.32
- APSW.CA: score=1.16 buy_ready=False sector_rank=7 price=8.6 support=8.24 resistance=9.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT RSI=34.67 liquidity=1388919.13 spike=1.42
- ARAB.CA: score=21.44 buy_ready=False sector_rank=3 price=0.21 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=63.33 liquidity=61643144.0 spike=0.72
- ARCC.CA: score=19.06 buy_ready=False sector_rank=13 price=56.62 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=50.58 liquidity=15693048.0 spike=0.37
- AREH.CA: score=16.93 buy_ready=False sector_rank=7 price=1.52 support=1.27 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=81.82 liquidity=18581816.0 spike=0.7
- ARVA.CA: score=18.95 buy_ready=False sector_rank=7 price=12.29 support=7.71 resistance=11.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=87.58 liquidity=24971534.0 spike=1.01
- ASCM.CA: score=16.93 buy_ready=False sector_rank=7 price=57.9 support=47.3 resistance=59.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=75.66 liquidity=37885024.0 spike=0.53
- ASPI.CA: score=21.93 buy_ready=False sector_rank=7 price=0.32 support=0.25 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=62.87 liquidity=40164576.0 spike=0.6
- ATLC.CA: score=3.72 buy_ready=False sector_rank=20 price=4.79 support=4.7 resistance=5.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=47.14 liquidity=777330.69 spike=0.15
- ATQA.CA: score=12.58 buy_ready=False sector_rank=19 price=9.39 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=42.56 liquidity=15258259.0 spike=0.41
- AXPH.CA: score=8.4 buy_ready=False sector_rank=7 price=1132.66 support=1111.0 resistance=1190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=38.06 liquidity=463034.59 spike=0.12
- BINV.CA: score=13.79 buy_ready=False sector_rank=5 price=45.5 support=40.8 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=63.13 liquidity=1471067.88 spike=0.13
- BIOC.CA: score=9.07 buy_ready=False sector_rank=7 price=70.33 support=68.34 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=41.63 liquidity=1142235.25 spike=0.21
- BTFH.CA: score=11.94 buy_ready=False sector_rank=20 price=3.02 support=2.96 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=44.07 liquidity=61285724.0 spike=0.26
- CAED.CA: score=5.59 buy_ready=False sector_rank=7 price=69.3 support=67.21 resistance=82.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=16.38 liquidity=2655559.75 spike=0.21
- CANA.CA: score=13.18 buy_ready=False sector_rank=11 price=36.16 support=34.07 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=59.43 liquidity=1800695.88 spike=0.12
- CCAP.CA: score=18.32 buy_ready=False sector_rank=5 price=5.14 support=4.82 resistance=5.78 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=49.06 liquidity=581263489.8 spike=0.78
- CCRS.CA: score=10.77 buy_ready=False sector_rank=7 price=2.39 support=2.21 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:12 AM market time freshness=DELAYED_CURRENT RSI=49.21 liquidity=2840685.5 spike=0.11
- CEFM.CA: score=3.38 buy_ready=False sector_rank=7 price=106.07 support=100.53 resistance=119.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:00 AM market time freshness=DELAYED_CURRENT RSI=31.67 liquidity=451503.22 spike=0.12
- CERA.CA: score=10.53 buy_ready=False sector_rank=7 price=1.17 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=58.33 liquidity=3593207.25 spike=0.26
- CFGH.CA: score=2.95 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=18482.3 spike=3.0
- CICH.CA: score=-1.02 buy_ready=False sector_rank=20 price=11.52 support=11.1 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=15.82 liquidity=1043997.75 spike=0.23
- CIEB.CA: score=10.8 buy_ready=False sector_rank=11 price=23.3 support=23.27 resistance=24.09 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=44.55 liquidity=6283497.19 spike=1.07
- CIRA.CA: score=11.8 buy_ready=False sector_rank=4 price=27.0 support=25.23 resistance=28.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=32.41 liquidity=6368126.0 spike=0.23
- CLHO.CA: score=11.61 buy_ready=False sector_rank=8 price=15.09 support=14.25 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=36.15 liquidity=3762203.0 spike=0.11
- CNFN.CA: score=1.87 buy_ready=False sector_rank=20 price=4.43 support=4.36 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=34.85 liquidity=1929930.88 spike=0.12
- COMI.CA: score=14.38 buy_ready=False sector_rank=11 price=131.69 support=129.8 resistance=136.8 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.51 liquidity=479660290.25 spike=0.93
- COPR.CA: score=16.93 buy_ready=False sector_rank=7 price=0.35 support=0.32 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=48.65 liquidity=38007260.0 spike=0.96
- COSG.CA: score=19.93 buy_ready=False sector_rank=7 price=1.59 support=1.49 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=55.0 liquidity=29185920.0 spike=0.43
- CPCI.CA: score=11.38 buy_ready=False sector_rank=7 price=361.33 support=340.01 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=64.68 liquidity=1450730.88 spike=0.49
- CSAG.CA: score=14.57 buy_ready=False sector_rank=18 price=31.01 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=45.14 liquidity=7963401.5 spike=0.55
- DAPH.CA: score=-0.04 buy_ready=False sector_rank=7 price=77.71 support=76.6 resistance=92.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=25.25 liquidity=1028316.25 spike=0.03
- DEIN.CA: score=5.93 buy_ready=False sector_rank=7 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=1.19 buy_ready=False sector_rank=9 price=24.31 support=23.7 resistance=26.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=29.8 liquidity=1374254.5 spike=0.53
- DSCW.CA: score=15.93 buy_ready=False sector_rank=7 price=1.76 support=1.71 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=17425264.0 spike=0.33
- DTPP.CA: score=0.61 buy_ready=False sector_rank=7 price=120.35 support=117.01 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:09 AM market time freshness=DELAYED_CURRENT RSI=21.72 liquidity=676919.31 spike=0.23
- EALR.CA: score=8.98 buy_ready=False sector_rank=7 price=352.56 support=346.01 resistance=386.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=48.98 liquidity=1048606.88 spike=0.22
- EASB.CA: score=9.93 buy_ready=False sector_rank=7 price=5.99 support=5.06 resistance=6.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11115410.0 spike=10.53
- EAST.CA: score=19.82 buy_ready=False sector_rank=9 price=38.03 support=37.01 resistance=39.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=50.78 liquidity=29425564.0 spike=0.44
- EBSC.CA: score=13.3 buy_ready=False sector_rank=7 price=1.83 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT RSI=62.79 liquidity=1366715.75 spike=0.52
- ECAP.CA: score=19.51 buy_ready=False sector_rank=7 price=31.31 support=28.7 resistance=32.39 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=89.69 liquidity=8654678.74 spike=1.96
- EDFM.CA: score=8.4 buy_ready=False sector_rank=7 price=334.55 support=320.2 resistance=355.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=50.76 liquidity=463002.47 spike=0.68
- EEII.CA: score=12.65 buy_ready=False sector_rank=7 price=2.39 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=53.49 liquidity=2717286.0 spike=0.14
- EFIC.CA: score=-1.04 buy_ready=False sector_rank=19 price=205.0 support=192.01 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=15.17 liquidity=1382150.38 spike=0.39
- EFID.CA: score=17.82 buy_ready=False sector_rank=9 price=27.96 support=27.06 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=38.41 liquidity=11087546.0 spike=0.15
- EFIH.CA: score=7.5 buy_ready=False sector_rank=21 price=20.42 support=20.2 resistance=22.78 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=30.35 liquidity=35215331.55 spike=0.79
- EGAL.CA: score=11.58 buy_ready=False sector_rank=19 price=312.92 support=305.01 resistance=344.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=15.38 liquidity=25944666.0 spike=0.25
- EGAS.CA: score=15.44 buy_ready=False sector_rank=6 price=51.51 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=62.8 liquidity=5247738.5 spike=0.44
- EGBE.CA: score=2.4 buy_ready=False sector_rank=11 price=0.44 support=0.44 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=30.82 liquidity=16370.96 spike=0.12
- EGCH.CA: score=16.58 buy_ready=False sector_rank=19 price=13.46 support=13.2 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=47.28 liquidity=36886092.0 spike=0.32
- EGSA.CA: score=1.96 buy_ready=False sector_rank=16 price=8.74 support=8.3 resistance=9.19 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=25.37 liquidity=6598.7 spike=0.45
- EGTS.CA: score=19.44 buy_ready=False sector_rank=3 price=18.5 support=13.61 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=47.27 liquidity=21882820.0 spike=0.18
- EHDR.CA: score=19.93 buy_ready=False sector_rank=7 price=2.75 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=70.71 liquidity=46600036.0 spike=0.88
- EKHO.CA: score=10.2 buy_ready=False sector_rank=6 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=9.88 buy_ready=False sector_rank=17 price=2.12 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=46.43 liquidity=6999278.0 spike=0.26
- ELKA.CA: score=20.93 buy_ready=False sector_rank=7 price=1.25 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=62.86 liquidity=12973842.0 spike=0.29
- ELNA.CA: score=6.43 buy_ready=False sector_rank=7 price=37.64 support=37.11 resistance=41.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=43.61 liquidity=759040.75 spike=1.87
- ELSH.CA: score=16.93 buy_ready=False sector_rank=7 price=13.71 support=8.1 resistance=14.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=78.34 liquidity=97436280.0 spike=0.59
- ELWA.CA: score=7.46 buy_ready=False sector_rank=7 price=2.14 support=1.79 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=78.95 liquidity=529104.69 spike=0.2
- EMFD.CA: score=23.44 buy_ready=False sector_rank=3 price=11.21 support=9.83 resistance=12.6 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=63.49 liquidity=132140308.02 spike=0.59
- ENGC.CA: score=18.98 buy_ready=False sector_rank=7 price=34.56 support=32.31 resistance=35.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=58.88 liquidity=7051871.5 spike=0.51
- EOSB.CA: score=15.41 buy_ready=False sector_rank=7 price=1.48 support=1.34 resistance=1.49 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=299753.28 spike=2.59
- EPCO.CA: score=10.96 buy_ready=False sector_rank=7 price=9.12 support=8.56 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=47.45 liquidity=1031044.81 spike=0.09
- EPPK.CA: score=5.28 buy_ready=False sector_rank=7 price=12.07 support=11.67 resistance=13.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=51.18 liquidity=349576.25 spike=0.31
- ETEL.CA: score=8.96 buy_ready=False sector_rank=16 price=90.82 support=89.8 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=28.49 liquidity=45624284.0 spike=0.54
- ETRS.CA: score=19.93 buy_ready=False sector_rank=7 price=9.29 support=7.37 resistance=9.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=71.97 liquidity=17330168.0 spike=0.3
- EXPA.CA: score=17.06 buy_ready=False sector_rank=11 price=18.57 support=18.31 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=47.4 liquidity=9683120.0 spike=0.26
- FAIT.CA: score=3.78 buy_ready=False sector_rank=11 price=35.5 support=35.0 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=22.01 liquidity=1395115.13 spike=0.23
- FAITA.CA: score=7.38 buy_ready=False sector_rank=11 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=4132.26 spike=0.1
- FERC.CA: score=4.92 buy_ready=False sector_rank=19 price=76.54 support=75.0 resistance=81.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=1347687.13 spike=0.24
- FWRY.CA: score=7.82 buy_ready=False sector_rank=21 price=17.8 support=17.71 resistance=20.74 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=29.48 liquidity=285162306.78 spike=1.16
- GBCO.CA: score=23.89 buy_ready=False sector_rank=1 price=28.31 support=25.25 resistance=29.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=72.17 liquidity=71554248.0 spike=0.61
- GDWA.CA: score=9.43 buy_ready=False sector_rank=7 price=0.79 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=51.89 liquidity=5498303.0 spike=0.42
- GGCC.CA: score=11.03 buy_ready=False sector_rank=7 price=0.41 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=2094352.0 spike=0.28
- GIHD.CA: score=8.55 buy_ready=False sector_rank=7 price=40.74 support=35.15 resistance=44.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:13 AM market time freshness=DELAYED_CURRENT RSI=49.48 liquidity=621807.06 spike=0.13
- GMCI.CA: score=4.37 buy_ready=False sector_rank=7 price=1.7 support=1.68 resistance=1.84 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=39.29 liquidity=355529.51 spike=1.04
- GRCA.CA: score=6.37 buy_ready=False sector_rank=7 price=53.92 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:10 AM market time freshness=DELAYED_CURRENT RSI=36.73 liquidity=1434772.63 spike=0.16
- GSSC.CA: score=0.73 buy_ready=False sector_rank=7 price=249.44 support=228.1 resistance=272.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=12.69 liquidity=795756.25 spike=0.13
- GTWL.CA: score=1.18 buy_ready=False sector_rank=7 price=47.09 support=45.47 resistance=59.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=25.6 liquidity=1244546.0 spike=0.18
- HDBK.CA: score=14.96 buy_ready=False sector_rank=11 price=138.0 support=138.0 resistance=146.58 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=37.06 liquidity=13569678.0 spike=1.29
- HELI.CA: score=19.44 buy_ready=False sector_rank=3 price=6.4 support=6.28 resistance=6.87 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=52.56 liquidity=69176762.63 spike=0.53
- HRHO.CA: score=11.94 buy_ready=False sector_rank=20 price=26.03 support=25.8 resistance=29.1 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=42.27 liquidity=62693048.41 spike=0.54
- ICID.CA: score=16.93 buy_ready=False sector_rank=7 price=7.0 support=4.5 resistance=6.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT RSI=87.25 liquidity=13191991.0 spike=0.85
- IDRE.CA: score=12.9 buy_ready=False sector_rank=7 price=42.16 support=41.01 resistance=49.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=44.29 liquidity=4964181.5 spike=0.15
- IFAP.CA: score=-0.01 buy_ready=False sector_rank=14 price=19.18 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=32.23 liquidity=1936041.25 spike=0.2
- INFI.CA: score=5.1 buy_ready=False sector_rank=7 price=100.21 support=97.0 resistance=109.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=24.0 liquidity=3170096.0 spike=0.21
- IRON.CA: score=8.47 buy_ready=False sector_rank=19 price=32.7 support=31.3 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT RSI=50.36 liquidity=3897930.75 spike=0.5
- ISMA.CA: score=18.93 buy_ready=False sector_rank=7 price=30.6 support=22.7 resistance=30.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=90.06 liquidity=29870914.0 spike=0.73
- ISMQ.CA: score=22.66 buy_ready=False sector_rank=19 price=8.51 support=7.27 resistance=8.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=71.36 liquidity=125417880.0 spike=2.04
- ISPH.CA: score=19.84 buy_ready=False sector_rank=8 price=11.95 support=11.12 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=54.32 liquidity=34125220.0 spike=0.26
- JUFO.CA: score=21.82 buy_ready=False sector_rank=9 price=29.88 support=26.51 resistance=30.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=64.57 liquidity=10889370.0 spike=0.24
- KABO.CA: score=16.64 buy_ready=False sector_rank=2 price=6.28 support=5.92 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=60.91 liquidity=3984598.0 spike=0.19
- KWIN.CA: score=10.72 buy_ready=False sector_rank=7 price=71.66 support=69.0 resistance=78.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=48.18 liquidity=2783427.0 spike=0.65
- KZPC.CA: score=12.44 buy_ready=False sector_rank=7 price=10.69 support=10.3 resistance=11.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=53.62 liquidity=2506471.75 spike=0.19
- LCSW.CA: score=9.0 buy_ready=False sector_rank=13 price=26.7 support=26.0 resistance=28.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=49.63 liquidity=1940533.75 spike=0.13
- LUTS.CA: score=9.93 buy_ready=False sector_rank=7 price=0.71 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=127604856.0 spike=6.25
- MAAL.CA: score=10.14 buy_ready=False sector_rank=7 price=5.75 support=4.44 resistance=6.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=78.07 liquidity=3206911.5 spike=0.24
- MASR.CA: score=17.93 buy_ready=False sector_rank=7 price=6.9 support=6.54 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=44.8 liquidity=25539836.0 spike=0.42
- MBSC.CA: score=12.06 buy_ready=False sector_rank=13 price=272.74 support=261.52 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=31.43 liquidity=25786128.0 spike=0.55
- MCQE.CA: score=8.09 buy_ready=False sector_rank=13 price=178.04 support=174.0 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=11.65 liquidity=9021187.0 spike=0.5
- MCRO.CA: score=13.93 buy_ready=False sector_rank=7 price=1.24 support=1.2 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=14751736.0 spike=0.25
- MENA.CA: score=19.97 buy_ready=False sector_rank=3 price=6.7 support=5.83 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=60.35 liquidity=8523836.0 spike=0.51
- MEPA.CA: score=14.15 buy_ready=False sector_rank=7 price=1.71 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=4213475.0 spike=0.23
- MFPC.CA: score=9.1 buy_ready=False sector_rank=19 price=38.82 support=39.47 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=24.69 liquidity=104127320.0 spike=1.26
- MFSC.CA: score=4.66 buy_ready=False sector_rank=7 price=45.16 support=43.0 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=19.86 liquidity=1731596.0 spike=0.11
- MHOT.CA: score=8.62 buy_ready=False sector_rank=10 price=29.7 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=44.87 liquidity=1232519.75 spike=0.06
- MICH.CA: score=19.84 buy_ready=False sector_rank=7 price=36.97 support=35.01 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=63.94 liquidity=7906365.5 spike=0.55
- MILS.CA: score=17.35 buy_ready=False sector_rank=7 price=146.95 support=127.01 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=60.02 liquidity=7420328.5 spike=0.39
- MIPH.CA: score=8.52 buy_ready=False sector_rank=8 price=658.75 support=640.0 resistance=717.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:09 AM market time freshness=DELAYED_CURRENT RSI=52.05 liquidity=673134.19 spike=0.23
- MOED.CA: score=1.48 buy_ready=False sector_rank=7 price=0.68 support=0.65 resistance=0.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=26.97 liquidity=2551048.5 spike=0.21
- MOIL.CA: score=8.24 buy_ready=False sector_rank=6 price=0.47 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=63.77 liquidity=40720.31 spike=0.21
- MOIN.CA: score=7.15 buy_ready=False sector_rank=7 price=25.01 support=24.02 resistance=26.4 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=55.88 liquidity=213810.49 spike=0.14
- MOSC.CA: score=8.51 buy_ready=False sector_rank=7 price=298.21 support=254.15 resistance=298.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26295964.0 spike=2.79
- MPCI.CA: score=19.93 buy_ready=False sector_rank=7 price=220.0 support=197.0 resistance=238.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=64.0 liquidity=19914014.0 spike=0.22
- MPCO.CA: score=21.06 buy_ready=False sector_rank=14 price=1.78 support=1.54 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=64.15 liquidity=41380604.0 spike=0.55
- MPRC.CA: score=19.5 buy_ready=False sector_rank=7 price=32.15 support=30.61 resistance=34.55 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=61.21 liquidity=9565139.85 spike=0.52
- MTIE.CA: score=16.53 buy_ready=False sector_rank=1 price=8.9 support=8.65 resistance=9.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=4634202.5 spike=0.23
- NAHO.CA: score=3.94 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=6412.78 spike=0.2
- NCCW.CA: score=16.93 buy_ready=False sector_rank=7 price=6.57 support=5.13 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=76.78 liquidity=14628886.0 spike=0.55
- NEDA.CA: score=8.64 buy_ready=False sector_rank=7 price=2.75 support=2.65 resistance=2.87 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=53.57 liquidity=503871.5 spike=1.1
- NHPS.CA: score=4.78 buy_ready=False sector_rank=7 price=67.83 support=65.03 resistance=72.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=42.32 liquidity=843682.06 spike=0.14
- NINH.CA: score=4.55 buy_ready=False sector_rank=7 price=17.16 support=16.8 resistance=20.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT RSI=24.12 liquidity=1613852.63 spike=0.19
- NIPH.CA: score=19.84 buy_ready=False sector_rank=8 price=164.87 support=155.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=52.42 liquidity=41756292.0 spike=0.41
- OBRI.CA: score=15.34 buy_ready=False sector_rank=7 price=35.83 support=33.63 resistance=39.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=40.93 liquidity=8403554.0 spike=0.71
- OCDI.CA: score=16.44 buy_ready=False sector_rank=3 price=20.04 support=20.0 resistance=23.67 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=46.58 liquidity=28647181.31 spike=0.96
- OCPH.CA: score=4.92 buy_ready=False sector_rank=7 price=346.06 support=337.0 resistance=404.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=28.14 liquidity=1986991.63 spike=0.25
- ODIN.CA: score=14.41 buy_ready=False sector_rank=7 price=2.07 support=1.89 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=62.96 liquidity=2473091.25 spike=0.23
- OFH.CA: score=15.43 buy_ready=False sector_rank=7 price=0.6 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=45.54 liquidity=37376340.0 spike=1.75
- OIH.CA: score=10.32 buy_ready=False sector_rank=5 price=1.38 support=1.33 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=32887374.0 spike=0.33
- OLFI.CA: score=17.2 buy_ready=False sector_rank=9 price=22.3 support=21.0 resistance=22.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=75.88 liquidity=22013862.0 spike=1.19
- ORAS.CA: score=5.0 buy_ready=False sector_rank=15 price=71.05 support=71.05 resistance=71.05 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ORHD.CA: score=19.44 buy_ready=False sector_rank=3 price=36.11 support=33.0 resistance=39.61 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=46.85 liquidity=138212616.18 spike=0.9
- ORWE.CA: score=22.65 buy_ready=False sector_rank=2 price=23.26 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=64.63 liquidity=12903280.0 spike=0.29
- PHAR.CA: score=15.42 buy_ready=False sector_rank=8 price=85.11 support=83.02 resistance=92.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=48.57 liquidity=7576534.5 spike=0.24
- PHDC.CA: score=19.44 buy_ready=False sector_rank=3 price=14.5 support=13.01 resistance=16.08 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=58.71 liquidity=133961889.5 spike=0.44
- PHTV.CA: score=4.5 buy_ready=False sector_rank=7 price=205.05 support=201.55 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=25.56 liquidity=1569915.25 spike=0.11
- POUL.CA: score=15.16 buy_ready=False sector_rank=9 price=36.0 support=34.8 resistance=39.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=47.04 liquidity=7342445.0 spike=0.16
- PRCL.CA: score=19.06 buy_ready=False sector_rank=13 price=24.42 support=21.01 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=59.4 liquidity=12582476.0 spike=0.44
- PRDC.CA: score=18.44 buy_ready=False sector_rank=3 price=6.3 support=5.3 resistance=6.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=80.77 liquidity=13032716.0 spike=0.15
- PRMH.CA: score=20.33 buy_ready=False sector_rank=7 price=2.74 support=2.19 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=69.7 liquidity=17810726.0 spike=1.2
- RACC.CA: score=10.37 buy_ready=False sector_rank=7 price=9.81 support=9.38 resistance=10.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=2439571.75 spike=0.18
- RAKT.CA: score=1.19 buy_ready=False sector_rank=7 price=23.11 support=22.1 resistance=25.0 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=34.13 liquidity=253031.4 spike=1.0
- RAYA.CA: score=17.22 buy_ready=False sector_rank=12 price=6.96 support=6.7 resistance=8.0 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=45.9 liquidity=76206843.06 spike=0.92
- RMDA.CA: score=17.84 buy_ready=False sector_rank=8 price=4.97 support=4.92 resistance=5.38 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=47.83 liquidity=27203775.94 spike=0.33
- ROTO.CA: score=11.98 buy_ready=False sector_rank=7 price=33.94 support=32.66 resistance=36.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:11 AM market time freshness=DELAYED_CURRENT RSI=52.08 liquidity=2043899.0 spike=0.15
- RREI.CA: score=13.04 buy_ready=False sector_rank=7 price=3.39 support=3.32 resistance=3.85 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.7 liquidity=8104157.98 spike=0.44
- RTVC.CA: score=9.65 buy_ready=False sector_rank=7 price=3.84 support=3.75 resistance=4.14 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=52.11 liquidity=2722133.7 spike=0.55
- RUBX.CA: score=8.74 buy_ready=False sector_rank=7 price=9.87 support=9.8 resistance=11.55 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=40.41 liquidity=4803344.01 spike=0.46
- SAUD.CA: score=15.68 buy_ready=False sector_rank=11 price=21.4 support=20.82 resistance=23.85 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=37.87 liquidity=16258906.51 spike=1.65
- SCEM.CA: score=5.12 buy_ready=False sector_rank=13 price=61.51 support=59.3 resistance=69.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=29.59 liquidity=6054754.5 spike=0.15
- SCFM.CA: score=4.09 buy_ready=False sector_rank=7 price=249.09 support=248.1 resistance=315.0 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=26.94 liquidity=4153824.78 spike=0.37
- SCTS.CA: score=4.52 buy_ready=False sector_rank=4 price=612.04 support=590.01 resistance=689.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=25.78 liquidity=1084823.38 spike=0.11
- SDTI.CA: score=23.77 buy_ready=False sector_rank=7 price=46.7 support=43.4 resistance=47.88 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=62.56 liquidity=26769888.14 spike=1.92
- SEIG.CA: score=10.09 buy_ready=False sector_rank=7 price=180.15 support=173.35 resistance=205.7 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=53.36 liquidity=2154053.48 spike=0.48
- SIPC.CA: score=12.0 buy_ready=False sector_rank=7 price=3.42 support=3.4 resistance=3.74 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=40.82 liquidity=7070686.0 spike=0.62
- SKPC.CA: score=13.36 buy_ready=False sector_rank=19 price=16.4 support=16.29 resistance=18.24 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=37.6 liquidity=66898747.24 spike=1.39
- SMFR.CA: score=2.82 buy_ready=False sector_rank=7 price=195.37 support=192.0 resistance=222.2 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=28.85 liquidity=2890303.71 spike=0.75
- SNFC.CA: score=17.93 buy_ready=False sector_rank=7 price=12.27 support=11.68 resistance=12.99 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=46.44 liquidity=10663685.62 spike=0.43
- SPIN.CA: score=8.43 buy_ready=False sector_rank=2 price=14.0 support=13.61 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=41.94 liquidity=781101.81 spike=0.17
- SPMD.CA: score=17.93 buy_ready=False sector_rank=7 price=0.4 support=0.38 resistance=0.44 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=56.19 liquidity=10394871.75 spike=0.46
- SUGR.CA: score=8.76 buy_ready=False sector_rank=9 price=48.82 support=48.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=46.0 liquidity=1941867.13 spike=0.13
- SVCE.CA: score=12.93 buy_ready=False sector_rank=7 price=8.32 support=8.11 resistance=9.87 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=27.69 liquidity=18996639.3 spike=0.25
- SWDY.CA: score=17.08 buy_ready=False sector_rank=17 price=84.41 support=84.01 resistance=90.77 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=39.98 liquidity=20701300.17 spike=1.1
- TALM.CA: score=8.16 buy_ready=False sector_rank=4 price=16.1 support=15.12 resistance=16.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=79.26 liquidity=731498.38 spike=0.06
- TMGH.CA: score=14.44 buy_ready=False sector_rank=3 price=92.91 support=91.87 resistance=101.4 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=28.48 liquidity=274423353.59 spike=0.7
- TRTO.CA: score=10.94 buy_ready=False sector_rank=7 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=5988.11 spike=8.0
- UEFM.CA: score=0.09 buy_ready=False sector_rank=7 price=468.99 support=455.6 resistance=500.0 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=26.76 liquidity=796813.99 spike=1.18
- UEGC.CA: score=16.93 buy_ready=False sector_rank=7 price=1.36 support=1.3 resistance=1.58 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=56.67 liquidity=14372760.31 spike=0.62
- UNIP.CA: score=15.93 buy_ready=False sector_rank=7 price=0.32 support=0.28 resistance=0.34 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=80.39 liquidity=16376910.89 spike=0.88
- UNIT.CA: score=12.32 buy_ready=False sector_rank=3 price=13.93 support=12.07 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=61.5 liquidity=880133.19 spike=0.08
- WCDF.CA: score=8.22 buy_ready=False sector_rank=7 price=539.84 support=531.0 resistance=555.0 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=38.12 liquidity=285575.37 spike=0.92
- WKOL.CA: score=6.82 buy_ready=False sector_rank=7 price=291.98 support=290.0 resistance=319.6 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=49.89 liquidity=1890278.59 spike=0.64
- ZEOT.CA: score=20.51 buy_ready=False sector_rank=7 price=8.99 support=8.41 resistance=9.5 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=63.78 liquidity=9800259.46 spike=1.89
- ZMID.CA: score=21.44 buy_ready=False sector_rank=3 price=6.27 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=59.69 liquidity=109327416.0 spike=0.46

## Backtesting Lite
- GBCO.CA: 180d return=31.89%, max drawdown=-24.35%, MA20>MA50 days last20=20, as_of=2026-06-10T21:00:00+00:00
- SDTI.CA: 180d return=184.58%, max drawdown=-10.12%, MA20>MA50 days last20=20, as_of=2026-06-10T21:00:00+00:00
- ANFI.CA: 180d return=235.87%, max drawdown=-19.31%, MA20>MA50 days last20=20, as_of=2026-06-10T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- SDTI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=SHARM DREAMS Co. for Touristic Investment S.A.E summary=Evidence rejected for SDTI.CA: source text did not clearly match SDTI.CA / SHARM DREAMS Co. for Touristic Investment S.A.E.
- ANFI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tycoon Holding Company For Financial Investments summary=Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- EMFD.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Emaar Misr for Development summary=Evidence rejected for EMFD.CA: source text did not clearly match EMFD.CA / Emaar Misr for Development.
- ISMQ.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Iron and Steel for Mines and Quarries summary=Evidence rejected for ISMQ.CA: source text did not clearly match ISMQ.CA / Iron and Steel for Mines and Quarries.
- ORWE.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Oriental Weavers summary=Evidence rejected for ORWE.CA: source text did not clearly match ORWE.CA / Oriental Weavers.
- ADCI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=The Arab Drug Company summary=Evidence rejected for ADCI.CA: source text did not clearly match ADCI.CA / The Arab Drug Company.
- ASPI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Aspire Capital Holding for Financial Investments summary=Evidence rejected for ASPI.CA: source text did not clearly match ASPI.CA / Aspire Capital Holding for Financial Investments.

## Warnings
- Mubasher stock-page evidence failed for GBCO.CA: HTTPSConnectionPool(host='english.mubasher.info', port=443): Read timed out. (read timeout=20)
- No Yahoo or Mubasher evidence found for GBCO.CA.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Mubasher stock-page evidence failed for SDTI.CA: HTTPSConnectionPool(host='english.mubasher.info', port=443): Read timed out. (read timeout=20)
- No Yahoo or Mubasher evidence found for SDTI.CA.
- Evidence rejected for SDTI.CA: source text did not clearly match SDTI.CA / SHARM DREAMS Co. for Touristic Investment S.A.E.
- Mubasher stock-page evidence failed for ANFI.CA: HTTPSConnectionPool(host='english.mubasher.info', port=443): Read timed out. (read timeout=20)
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- Mubasher stock-page evidence failed for EMFD.CA: HTTPSConnectionPool(host='english.mubasher.info', port=443): Read timed out. (read timeout=20)
- No Yahoo or Mubasher evidence found for EMFD.CA.
- Evidence rejected for EMFD.CA: source text did not clearly match EMFD.CA / Emaar Misr for Development.
- Mubasher stock-page evidence failed for ISMQ.CA: HTTPSConnectionPool(host='english.mubasher.info', port=443): Read timed out. (read timeout=20)
- No Yahoo or Mubasher evidence found for ISMQ.CA.
- Evidence rejected for ISMQ.CA: source text did not clearly match ISMQ.CA / Iron and Steel for Mines and Quarries.
- Mubasher stock-page evidence failed for ORWE.CA: HTTPSConnectionPool(host='english.mubasher.info', port=443): Read timed out. (read timeout=20)
- No Yahoo or Mubasher evidence found for ORWE.CA.
- Evidence rejected for ORWE.CA: source text did not clearly match ORWE.CA / Oriental Weavers.
- Mubasher stock-page evidence failed for ADCI.CA: HTTPSConnectionPool(host='english.mubasher.info', port=443): Read timed out. (read timeout=20)
- No Yahoo or Mubasher evidence found for ADCI.CA.
- Evidence rejected for ADCI.CA: source text did not clearly match ADCI.CA / The Arab Drug Company.
- Mubasher stock-page evidence failed for ASPI.CA: HTTPSConnectionPool(host='english.mubasher.info', port=443): Read timed out. (read timeout=20)
- No Yahoo or Mubasher evidence found for ASPI.CA.
- Evidence rejected for ASPI.CA: source text did not clearly match ASPI.CA / Aspire Capital Holding for Financial Investments.
