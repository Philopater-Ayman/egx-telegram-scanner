# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-06-10T11:38:53.466930+00:00
Generated Cairo: 2026-06-10 14:38
Run timing: target 11:00 Cairo | generated Cairo 2026-06-10 14:38 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-06-10 14:35

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 177/190
- Top sector: Automotive & Distribution

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, June 10
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 10.0% / above MA50 40.0%
- EGX70 regime: BEARISH / above MA20 35.14% / above MA50 78.38%
- Sector breadth: 19.05%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=1098636160.0 spike=1.3 score=5.14
- COMI.CA: liquidity=547218304.0 spike=0.81 score=15.11
- ELSH.CA: liquidity=505603584.0 spike=3.84 score=11.91
- ORAS.CA: liquidity=432585216.0 spike=1.0 score=4.6
- FWRY.CA: liquidity=362695744.0 spike=1.21 score=13.21

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The local scanner kept all tickets on HOLD because the EGX30 and EGX70 are both in a bearish regime with weak breadth (19.05%). Risk mode is set to DEFENSIVE_NO_NEW_BUY, so new long entries are blocked despite several stocks showing bullish watch outlooks and solid liquidity.
- Bearish EGX30/EGX70 trends and low sector breadth limit buying power for the next 1‑3 days.
- Real Estate and General/Verified EGX Expansion sectors lead the scan, but most stocks sit near resistance or have overheated RSI.
- Liquidity is adequate (e.g., ZMID.CA tradeable, ADCI.CA accumulation spike), yet market regime overrides entry signals.
- Support levels are modestly distant; resistance is close for many tickets, adding short‑term upside uncertainty.
- Overall outlook remains defensive with high uncertainty; monitor regime shifts before considering new positions.

## Top Liquidity Spikes
- MICH.CA: spike=10.85 liquidity=96968560.0 outlook=BULLISH_WATCH score=73.77 buy_ready=False
- CFGH.CA: spike=5.57 liquidity=28866.03 outlook=WEAK_OR_RISKY score=1.77 buy_ready=False
- ADCI.CA: spike=4.86 liquidity=29282998.0 outlook=BULLISH_WATCH score=95.77 buy_ready=False
- ANFI.CA: spike=4.65 liquidity=134592218.23 outlook=BULLISH_WATCH score=77.77 buy_ready=False
- LUTS.CA: spike=3.99 liquidity=65599800.0 outlook=BULLISH_WATCH score=93.77 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=6.36 5d=2.17% 20d=-2.47% aboveMA50=100.0%
- #2 Real Estate: score=5.32 5d=-1.18% 20d=4.07% aboveMA50=69.23%
- #3 General / Verified EGX Expansion: score=4.77 5d=0.88% 20d=0.0% aboveMA50=71.15%
- #4 Textiles: score=4.69 5d=-0.81% 20d=5.88% aboveMA50=75.0%
- #5 Healthcare: score=4.36 5d=1.46% 20d=-1.7% aboveMA50=100.0%
- #6 Food, Beverages & Tobacco: score=4.22 5d=-0.66% 20d=1.51% aboveMA50=85.71%
- #7 Tourism & Leisure: score=4.08 5d=-5.99% 20d=14.85% aboveMA50=100.0%
- #8 Education: score=3.96 5d=0.51% 20d=-4.39% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- KZPC.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- ALUM.CA: BULLISH_WATCH score=98.77 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ZMID.CA: BULLISH_WATCH score=96.32 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- ADCI.CA: BULLISH_WATCH score=95.77 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended; close to resistance
- EEII.CA: BULLISH_WATCH score=95.77 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- RTVC.CA: BULLISH_WATCH score=95.77 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- GGCC.CA: BULLISH_WATCH score=94.77 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- LUTS.CA: BULLISH_WATCH score=93.77 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- COSG.CA: BULLISH_WATCH score=93.77 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- OLFI.CA: BULLISH_WATCH score=91.22 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=6.95 buy_ready=False sector_rank=3 price=200.18 support=200.0 resistance=224.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11329186.0 spike=1.02
- ABUK.CA: score=9.54 buy_ready=False sector_rank=17 price=79.51 support=81.2 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.35 liquidity=68215184.0 spike=0.57
- ACAMD.CA: score=24.31 buy_ready=False sector_rank=3 price=2.24 support=2.1 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=59.65 liquidity=257066800.0 spike=2.2
- ACGC.CA: score=18.88 buy_ready=False sector_rank=4 price=9.56 support=8.51 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.21 liquidity=34196880.0 spike=0.59
- ADCI.CA: score=26.91 buy_ready=False sector_rank=3 price=221.23 support=202.22 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=66.05 liquidity=29282998.0 spike=4.86
- ADIB.CA: score=15.11 buy_ready=False sector_rank=11 price=44.88 support=45.3 resistance=50.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.08 liquidity=99102192.0 spike=0.63
- ADPC.CA: score=11.91 buy_ready=False sector_rank=3 price=3.6 support=3.54 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.74 liquidity=10475726.0 spike=0.42
- AFDI.CA: score=21.91 buy_ready=False sector_rank=3 price=42.56 support=40.0 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=61.36 liquidity=13020087.0 spike=0.71
- AFMC.CA: score=12.97 buy_ready=False sector_rank=3 price=70.53 support=69.33 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=41.89 liquidity=3060623.5 spike=0.34
- AJWA.CA: score=22.19 buy_ready=False sector_rank=3 price=148.09 support=130.01 resistance=154.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=84.58 liquidity=28226630.0 spike=1.64
- ALCN.CA: score=14.52 buy_ready=False sector_rank=18 price=28.24 support=28.4 resistance=30.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.99 liquidity=16077718.0 spike=0.75
- ALUM.CA: score=25.91 buy_ready=False sector_rank=3 price=24.47 support=22.66 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.44 liquidity=11284748.0 spike=0.53
- AMER.CA: score=8.13 buy_ready=False sector_rank=2 price=2.6 support=2.58 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=94325768.0 spike=0.83
- AMES.CA: score=9.66 buy_ready=False sector_rank=3 price=49.85 support=48.0 resistance=57.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=18.46 liquidity=4747571.0 spike=0.81
- AMIA.CA: score=21.2 buy_ready=False sector_rank=3 price=8.93 support=8.54 resistance=10.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=64.0 liquidity=9296841.0 spike=0.33
- AMOC.CA: score=10.37 buy_ready=False sector_rank=10 price=8.11 support=8.1 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.36 liquidity=45088628.0 spike=0.55
- ANFI.CA: score=25.91 buy_ready=False sector_rank=3 price=18.62 support=13.5 resistance=18.62 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=79.32 liquidity=134592218.23 spike=4.65
- APSW.CA: score=5.95 buy_ready=False sector_rank=3 price=8.63 support=8.62 resistance=9.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.21 liquidity=1341995.63 spike=1.35
- ARAB.CA: score=19.47 buy_ready=False sector_rank=2 price=0.2 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.72 liquidity=167040464.0 spike=2.17
- ARCC.CA: score=18.58 buy_ready=False sector_rank=9 price=55.91 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=38547120.0 spike=0.9
- AREH.CA: score=20.91 buy_ready=False sector_rank=3 price=1.47 support=1.27 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=80.65 liquidity=19904116.0 spike=0.71
- ARVA.CA: score=21.91 buy_ready=False sector_rank=3 price=10.99 support=7.71 resistance=11.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=74.61 liquidity=17807128.0 spike=0.71
- ASCM.CA: score=19.23 buy_ready=False sector_rank=3 price=55.13 support=47.3 resistance=59.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=75.73 liquidity=78736184.0 spike=1.16
- ASPI.CA: score=6.91 buy_ready=False sector_rank=3 price=0.33 support=0.33 resistance=0.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51831400.0 spike=0.83
- ATLC.CA: score=10.3 buy_ready=False sector_rank=19 price=4.84 support=4.71 resistance=5.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=66.04 liquidity=2938119.5 spike=0.46
- ATQA.CA: score=15.54 buy_ready=False sector_rank=17 price=9.56 support=9.41 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=29928720.0 spike=0.74
- AXPH.CA: score=11.0 buy_ready=False sector_rank=3 price=1131.19 support=1100.12 resistance=1239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.16 liquidity=1089594.63 spike=0.19
- BINV.CA: score=12.58 buy_ready=False sector_rank=16 price=45.98 support=40.8 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=71.75 liquidity=3038479.25 spike=0.25
- BIOC.CA: score=13.96 buy_ready=False sector_rank=3 price=70.39 support=70.0 resistance=79.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=4050767.0 spike=0.63
- BTFH.CA: score=16.36 buy_ready=False sector_rank=19 price=3.04 support=3.03 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.27 liquidity=100856504.0 spike=0.42
- CAED.CA: score=7.37 buy_ready=False sector_rank=3 price=70.7 support=70.41 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.62 liquidity=2458989.0 spike=0.16
- CANA.CA: score=17.47 buy_ready=False sector_rank=11 price=36.22 support=34.01 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=65.43 liquidity=16933238.0 spike=1.18
- CCAP.CA: score=5.14 buy_ready=False sector_rank=16 price=5.14 support=5.13 resistance=5.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1098636160.0 spike=1.3
- CCRS.CA: score=21.75 buy_ready=False sector_rank=3 price=2.4 support=2.1 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.71 liquidity=9845614.0 spike=0.36
- CEFM.CA: score=5.9 buy_ready=False sector_rank=3 price=105.16 support=103.07 resistance=119.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=30.19 liquidity=995862.19 spike=0.21
- CERA.CA: score=24.91 buy_ready=False sector_rank=3 price=1.18 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=53.85 liquidity=10168171.0 spike=0.68
- CFGH.CA: score=5.94 buy_ready=False sector_rank=3 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=28866.03 spike=5.57
- CICH.CA: score=1.56 buy_ready=False sector_rank=19 price=11.6 support=11.71 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=24.14 liquidity=2193837.75 spike=0.47
- CIEB.CA: score=21.51 buy_ready=False sector_rank=11 price=23.63 support=23.31 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.39 liquidity=17106060.0 spike=1.7
- CIRA.CA: score=16.28 buy_ready=False sector_rank=8 price=25.91 support=23.23 resistance=28.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.54 liquidity=7695824.5 spike=0.26
- CLHO.CA: score=13.74 buy_ready=False sector_rank=5 price=14.91 support=14.83 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.36 liquidity=10297664.0 spike=0.29
- CNFN.CA: score=16.36 buy_ready=False sector_rank=19 price=4.43 support=4.47 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.94 liquidity=12065441.0 spike=0.71
- COMI.CA: score=15.11 buy_ready=False sector_rank=11 price=131.09 support=129.8 resistance=144.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.51 liquidity=547218304.0 spike=0.81
- COPR.CA: score=20.33 buy_ready=False sector_rank=3 price=0.36 support=0.32 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=67.35 liquidity=65842496.0 spike=1.71
- COSG.CA: score=25.13 buy_ready=False sector_rank=3 price=1.64 support=1.46 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=64.71 liquidity=97958600.0 spike=1.61
- CPCI.CA: score=10.43 buy_ready=False sector_rank=3 price=361.55 support=340.01 resistance=370.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=82.12 liquidity=3524489.75 spike=0.79
- CSAG.CA: score=17.52 buy_ready=False sector_rank=18 price=30.97 support=30.4 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.85 liquidity=14358764.0 spike=0.78
- DAPH.CA: score=9.43 buy_ready=False sector_rank=3 price=78.83 support=79.25 resistance=96.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=27.1 liquidity=7525847.0 spike=0.25
- DEIN.CA: score=7.91 buy_ready=False sector_rank=3 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=7.06 buy_ready=False sector_rank=6 price=24.05 support=24.24 resistance=26.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=29.8 liquidity=4550167.5 spike=1.91
- DSCW.CA: score=17.91 buy_ready=False sector_rank=3 price=1.77 support=1.71 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.16 liquidity=31241768.0 spike=0.52
- DTPP.CA: score=4.72 buy_ready=False sector_rank=3 price=120.3 support=123.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.06 liquidity=2816978.0 spike=0.73
- EALR.CA: score=12.74 buy_ready=False sector_rank=3 price=356.73 support=346.01 resistance=392.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=48.06 liquidity=2828535.0 spike=0.29
- EASB.CA: score=11.37 buy_ready=False sector_rank=3 price=4.96 support=4.61 resistance=5.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=72.58 liquidity=1342045.38 spike=1.06
- EAST.CA: score=16.85 buy_ready=False sector_rank=6 price=38.39 support=37.01 resistance=39.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=60.28 liquidity=6157625.0 spike=0.09
- EBSC.CA: score=14.77 buy_ready=False sector_rank=3 price=1.82 support=1.64 resistance=2.09 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=62.79 liquidity=862683.66 spike=0.35
- ECAP.CA: score=22.42 buy_ready=False sector_rank=3 price=31.09 support=28.7 resistance=32.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=88.3 liquidity=9810857.0 spike=1.85
- EDFM.CA: score=10.4 buy_ready=False sector_rank=3 price=334.11 support=320.2 resistance=355.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=38.06 liquidity=494012.97 spike=0.54
- EEII.CA: score=23.93 buy_ready=False sector_rank=3 price=2.39 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=19851676.0 spike=1.01
- EFIC.CA: score=0.21 buy_ready=False sector_rank=17 price=204.33 support=203.01 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=7.01 liquidity=1666096.25 spike=0.41
- EFID.CA: score=18.69 buy_ready=False sector_rank=6 price=27.8 support=27.49 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.57 liquidity=35673084.0 spike=0.46
- EFIH.CA: score=12.79 buy_ready=False sector_rank=21 price=20.8 support=21.0 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.32 liquidity=33095712.0 spike=0.51
- EGAL.CA: score=14.54 buy_ready=False sector_rank=17 price=310.93 support=304.0 resistance=344.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.47 liquidity=80106984.0 spike=0.72
- EGAS.CA: score=15.96 buy_ready=False sector_rank=10 price=49.96 support=46.51 resistance=51.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=42.63 liquidity=5591734.5 spike=0.42
- EGBE.CA: score=8.2 buy_ready=False sector_rank=11 price=0.44 support=0.44 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=42.52 liquidity=91505.61 spike=0.66
- EGCH.CA: score=19.54 buy_ready=False sector_rank=17 price=14.1 support=12.95 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.7 liquidity=36765044.0 spike=0.31
- EGSA.CA: score=8.86 buy_ready=False sector_rank=12 price=8.6 support=8.3 resistance=9.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=67.78 liquidity=36452.69 spike=2.43
- EGTS.CA: score=8.13 buy_ready=False sector_rank=2 price=18.38 support=18.21 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=92095352.0 spike=0.8
- EHDR.CA: score=7.91 buy_ready=False sector_rank=3 price=2.65 support=2.64 resistance=2.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=75541992.0 spike=1.5
- EKHO.CA: score=10.37 buy_ready=False sector_rank=10 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=15.75 buy_ready=False sector_rank=13 price=2.13 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.17 liquidity=12944390.0 spike=0.46
- ELKA.CA: score=21.83 buy_ready=False sector_rank=3 price=1.25 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=60927240.0 spike=1.46
- ELNA.CA: score=18.24 buy_ready=False sector_rank=3 price=41.26 support=37.11 resistance=42.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=38.94 liquidity=1332774.25 spike=3.71
- ELSH.CA: score=11.91 buy_ready=False sector_rank=3 price=14.04 support=13.03 resistance=14.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=505603584.0 spike=3.84
- ELWA.CA: score=12.91 buy_ready=False sector_rank=3 price=2.13 support=1.79 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=91.67 liquidity=2005345.5 spike=0.66
- EMFD.CA: score=20.13 buy_ready=False sector_rank=2 price=11.55 support=9.83 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=75.07 liquidity=226900128.0 spike=0.95
- ENGC.CA: score=23.67 buy_ready=False sector_rank=3 price=34.31 support=32.31 resistance=35.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=70.72 liquidity=24710166.0 spike=1.88
- EOSB.CA: score=12.3 buy_ready=False sector_rank=3 price=1.42 support=1.34 resistance=1.54 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=253701.45 spike=2.07
- EPCO.CA: score=15.72 buy_ready=False sector_rank=3 price=9.0 support=8.56 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.31 liquidity=6808633.0 spike=0.55
- EPPK.CA: score=7.27 buy_ready=False sector_rank=3 price=12.17 support=11.67 resistance=13.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=47.1 liquidity=363966.69 spike=0.31
- ETEL.CA: score=14.97 buy_ready=False sector_rank=12 price=92.59 support=92.17 resistance=99.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=50948212.0 spike=0.46
- ETRS.CA: score=22.47 buy_ready=False sector_rank=3 price=9.27 support=7.37 resistance=9.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=71459448.0 spike=1.28
- EXPA.CA: score=18.11 buy_ready=False sector_rank=11 price=18.63 support=18.34 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.93 liquidity=23319736.0 spike=0.59
- FAIT.CA: score=4.83 buy_ready=False sector_rank=11 price=35.95 support=34.11 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=32.88 liquidity=1718651.0 spike=0.26
- FAITA.CA: score=8.13 buy_ready=False sector_rank=11 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=58.82 liquidity=17939.61 spike=0.4
- FERC.CA: score=8.4 buy_ready=False sector_rank=17 price=76.88 support=76.5 resistance=83.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.33 liquidity=3859907.25 spike=0.62
- FWRY.CA: score=13.21 buy_ready=False sector_rank=21 price=18.09 support=18.32 resistance=21.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.53 liquidity=362695744.0 spike=1.21
- GBCO.CA: score=25.18 buy_ready=False sector_rank=1 price=27.62 support=25.25 resistance=29.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=65.27 liquidity=173443136.0 spike=1.39
- GDWA.CA: score=22.47 buy_ready=False sector_rank=3 price=0.79 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=64.71 liquidity=16788918.0 spike=1.78
- GGCC.CA: score=22.91 buy_ready=False sector_rank=3 price=0.42 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=14123178.0 spike=2.0
- GIHD.CA: score=14.09 buy_ready=False sector_rank=3 price=40.01 support=39.1 resistance=44.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.23 liquidity=3178657.75 spike=0.59
- GMCI.CA: score=9.21 buy_ready=False sector_rank=3 price=1.73 support=1.67 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=56.67 liquidity=305239.03 spike=0.76
- GRCA.CA: score=4.14 buy_ready=False sector_rank=3 price=52.2 support=53.16 resistance=60.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.97 liquidity=2234801.75 spike=0.25
- GSSC.CA: score=6.79 buy_ready=False sector_rank=3 price=249.27 support=228.1 resistance=272.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=9.47 liquidity=4878914.0 spike=0.66
- GTWL.CA: score=14.79 buy_ready=False sector_rank=3 price=47.61 support=45.47 resistance=59.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.28 liquidity=16910254.0 spike=2.44
- HDBK.CA: score=14.68 buy_ready=False sector_rank=11 price=139.07 support=138.75 resistance=149.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.01 liquidity=9571074.0 spike=0.63
- HELI.CA: score=21.33 buy_ready=False sector_rank=2 price=6.47 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.55 liquidity=182916304.0 spike=1.1
- HRHO.CA: score=13.36 buy_ready=False sector_rank=19 price=26.16 support=26.05 resistance=29.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.48 liquidity=106324312.0 spike=0.57
- ICID.CA: score=7.31 buy_ready=False sector_rank=3 price=6.53 support=6.45 resistance=6.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17223490.0 spike=1.2
- IDRE.CA: score=19.29 buy_ready=False sector_rank=3 price=43.54 support=39.8 resistance=49.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.64 liquidity=9379555.0 spike=0.28
- IFAP.CA: score=6.74 buy_ready=False sector_rank=20 price=19.31 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.74 liquidity=4009852.25 spike=0.32
- INFI.CA: score=17.74 buy_ready=False sector_rank=3 price=98.24 support=99.51 resistance=112.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.53 liquidity=8832462.0 spike=0.55
- IRON.CA: score=15.52 buy_ready=False sector_rank=17 price=32.1 support=31.83 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.2 liquidity=9540547.0 spike=1.22
- ISMA.CA: score=20.91 buy_ready=False sector_rank=3 price=29.56 support=20.66 resistance=30.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=92.96 liquidity=15262367.0 spike=0.3
- ISMQ.CA: score=25.42 buy_ready=False sector_rank=17 price=7.89 support=7.27 resistance=8.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=67.86 liquidity=149819040.0 spike=2.94
- ISPH.CA: score=22.74 buy_ready=False sector_rank=5 price=11.96 support=11.12 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=63.98 liquidity=86136736.0 spike=0.56
- JUFO.CA: score=19.69 buy_ready=False sector_rank=6 price=29.49 support=26.51 resistance=30.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=75.46 liquidity=24030582.0 spike=0.5
- KABO.CA: score=18.94 buy_ready=False sector_rank=4 price=6.2 support=5.92 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=72.34 liquidity=20610134.0 spike=1.03
- KWIN.CA: score=24.31 buy_ready=False sector_rank=3 price=71.92 support=69.0 resistance=80.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.39 liquidity=12422092.0 spike=3.2
- KZPC.CA: score=26.81 buy_ready=False sector_rank=3 price=10.71 support=10.3 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.59 liquidity=39887392.0 spike=3.45
- LCSW.CA: score=15.43 buy_ready=False sector_rank=9 price=26.42 support=26.16 resistance=29.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.42 liquidity=6851498.0 spike=0.44
- LUTS.CA: score=26.91 buy_ready=False sector_rank=3 price=0.64 support=0.54 resistance=0.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=68.55 liquidity=65599800.0 spike=3.99
- MAAL.CA: score=26.45 buy_ready=False sector_rank=3 price=5.89 support=4.44 resistance=6.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=16239657.0 spike=1.27
- MASR.CA: score=24.91 buy_ready=False sector_rank=3 price=6.88 support=6.63 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.34 liquidity=203695248.0 spike=3.51
- MBSC.CA: score=18.58 buy_ready=False sector_rank=9 price=270.98 support=261.52 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.97 liquidity=30583168.0 spike=0.63
- MCQE.CA: score=16.32 buy_ready=False sector_rank=9 price=180.0 support=185.59 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.13 liquidity=26313120.0 spike=1.37
- MCRO.CA: score=17.91 buy_ready=False sector_rank=3 price=1.23 support=1.21 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.89 liquidity=36796188.0 spike=0.43
- MENA.CA: score=25.13 buy_ready=False sector_rank=2 price=6.81 support=5.8 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.75 liquidity=13724338.0 spike=0.86
- MEPA.CA: score=21.91 buy_ready=False sector_rank=3 price=1.68 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=11610618.0 spike=0.61
- MFPC.CA: score=9.54 buy_ready=False sector_rank=17 price=41.22 support=42.01 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.62 liquidity=49459544.0 spike=0.57
- MFSC.CA: score=1.99 buy_ready=False sector_rank=3 price=44.0 support=43.0 resistance=47.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5078566.0 spike=0.33
- MHOT.CA: score=15.75 buy_ready=False sector_rank=7 price=30.01 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.18 liquidity=7118484.0 spike=0.34
- MICH.CA: score=26.91 buy_ready=False sector_rank=3 price=37.79 support=35.01 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=72.61 liquidity=96968560.0 spike=10.85
- MILS.CA: score=17.01 buy_ready=False sector_rank=3 price=138.55 support=127.01 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=70.06 liquidity=5098769.5 spike=0.23
- MIPH.CA: score=11.25 buy_ready=False sector_rank=5 price=658.09 support=640.0 resistance=729.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.51 liquidity=2501991.0 spike=0.79
- MOED.CA: score=10.91 buy_ready=False sector_rank=3 price=0.68 support=0.68 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.04 liquidity=11245331.0 spike=0.85
- MOIL.CA: score=12.51 buy_ready=False sector_rank=10 price=0.47 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=64.71 liquidity=145225.03 spike=0.77
- MOIN.CA: score=9.56 buy_ready=False sector_rank=3 price=25.01 support=24.02 resistance=26.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=67.2 liquidity=656316.88 spike=0.33
- MOSC.CA: score=6.85 buy_ready=False sector_rank=3 price=258.99 support=264.0 resistance=320.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.23 liquidity=1945154.63 spike=0.15
- MPCI.CA: score=23.91 buy_ready=False sector_rank=3 price=221.16 support=193.8 resistance=238.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=68.96 liquidity=59310712.0 spike=0.66
- MPCO.CA: score=3.73 buy_ready=False sector_rank=20 price=1.7 support=1.7 resistance=1.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51235912.0 spike=0.71
- MPRC.CA: score=23.91 buy_ready=False sector_rank=3 price=32.42 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=62.93 liquidity=21831300.0 spike=1.0
- MTIE.CA: score=22.4 buy_ready=False sector_rank=1 price=8.89 support=8.71 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.87 liquidity=12242283.0 spike=0.59
- NAHO.CA: score=5.92 buy_ready=False sector_rank=3 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=15884.53 spike=0.43
- NCCW.CA: score=22.19 buy_ready=False sector_rank=3 price=6.41 support=5.13 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=82.23 liquidity=40419672.0 spike=1.64
- NEDA.CA: score=12.27 buy_ready=False sector_rank=3 price=2.79 support=2.65 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=358087.06 spike=0.53
- NHPS.CA: score=9.12 buy_ready=False sector_rank=3 price=67.72 support=67.53 resistance=73.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.68 liquidity=3214370.0 spike=0.3
- NINH.CA: score=7.28 buy_ready=False sector_rank=3 price=17.13 support=17.53 resistance=20.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.42 liquidity=2369226.75 spike=0.24
- NIPH.CA: score=18.74 buy_ready=False sector_rank=5 price=162.9 support=155.1 resistance=186.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.17 liquidity=54594236.0 spike=0.47
- OBRI.CA: score=22.55 buy_ready=False sector_rank=3 price=34.9 support=33.63 resistance=39.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.8 liquidity=31952480.0 spike=2.82
- OCDI.CA: score=18.13 buy_ready=False sector_rank=2 price=20.67 support=20.19 resistance=23.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.38 liquidity=30369492.0 spike=0.71
- OCPH.CA: score=14.66 buy_ready=False sector_rank=3 price=350.66 support=350.0 resistance=409.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.02 liquidity=4756036.5 spike=0.5
- ODIN.CA: score=21.51 buy_ready=False sector_rank=3 price=2.08 support=1.89 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=79.07 liquidity=13732160.0 spike=1.3
- OFH.CA: score=18.91 buy_ready=False sector_rank=3 price=0.61 support=0.6 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=22214778.0 spike=1.0
- OIH.CA: score=9.54 buy_ready=False sector_rank=16 price=1.36 support=1.35 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=46766744.0 spike=0.4
- OLFI.CA: score=21.75 buy_ready=False sector_rank=6 price=21.8 support=21.0 resistance=22.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=61.66 liquidity=31885658.0 spike=1.53
- ORAS.CA: score=4.6 buy_ready=False sector_rank=15 price=733.91 support=722.0 resistance=763.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=432585216.0 spike=1.0
- ORHD.CA: score=24.05 buy_ready=False sector_rank=2 price=36.65 support=32.9 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.47 liquidity=300223008.0 spike=1.46
- ORWE.CA: score=20.88 buy_ready=False sector_rank=4 price=23.16 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=72.17 liquidity=24358628.0 spike=0.53
- PHAR.CA: score=18.74 buy_ready=False sector_rank=5 price=86.0 support=83.96 resistance=92.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=46.88 liquidity=11923313.0 spike=0.35
- PHDC.CA: score=21.13 buy_ready=False sector_rank=2 price=14.8 support=13.01 resistance=16.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=66.12 liquidity=205715840.0 spike=0.49
- PHTV.CA: score=16.29 buy_ready=False sector_rank=3 price=204.82 support=203.25 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.33 liquidity=6379493.5 spike=0.43
- POUL.CA: score=18.69 buy_ready=False sector_rank=6 price=36.0 support=34.8 resistance=39.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.22 liquidity=18344602.0 spike=0.39
- PRCL.CA: score=22.58 buy_ready=False sector_rank=9 price=24.51 support=21.01 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.27 liquidity=13750014.0 spike=0.39
- PRDC.CA: score=20.47 buy_ready=False sector_rank=2 price=6.09 support=5.3 resistance=6.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=76.3 liquidity=22892676.0 spike=1.17
- PRMH.CA: score=18.91 buy_ready=False sector_rank=3 price=2.64 support=2.17 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=77.53 liquidity=12464307.0 spike=0.83
- RACC.CA: score=16.86 buy_ready=False sector_rank=3 price=9.63 support=9.56 resistance=12.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.73 liquidity=6956065.0 spike=0.37
- RAKT.CA: score=10.23 buy_ready=False sector_rank=3 price=23.11 support=22.1 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=54.9 liquidity=563394.69 spike=1.88
- RAYA.CA: score=4.68 buy_ready=False sector_rank=14 price=6.96 support=6.9 resistance=7.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=117173832.0 spike=1.03
- RMDA.CA: score=20.74 buy_ready=False sector_rank=5 price=5.08 support=4.95 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=63.41 liquidity=31995912.0 spike=0.29
- ROTO.CA: score=22.3 buy_ready=False sector_rank=3 price=33.6 support=32.66 resistance=36.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=71.72 liquidity=8396888.0 spike=0.65
- RREI.CA: score=16.91 buy_ready=False sector_rank=3 price=3.42 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=14227506.0 spike=0.6
- RTVC.CA: score=19.71 buy_ready=False sector_rank=3 price=3.91 support=3.75 resistance=4.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.81 liquidity=5797385.0 spike=0.86
- RUBX.CA: score=8.71 buy_ready=False sector_rank=3 price=10.12 support=9.8 resistance=11.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.96 liquidity=7799547.0 spike=0.53
- SAUD.CA: score=15.21 buy_ready=False sector_rank=11 price=21.43 support=21.8 resistance=24.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.58 liquidity=14410138.0 spike=1.05
- SCEM.CA: score=18.58 buy_ready=False sector_rank=9 price=62.18 support=62.5 resistance=72.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.89 liquidity=32231104.0 spike=0.82
- SCFM.CA: score=8.69 buy_ready=False sector_rank=3 price=255.5 support=255.7 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=30.8 liquidity=3779670.25 spike=0.18
- SCTS.CA: score=8.18 buy_ready=False sector_rank=8 price=610.21 support=590.01 resistance=690.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=33.16 liquidity=4593378.0 spike=0.42
- SDTI.CA: score=23.91 buy_ready=False sector_rank=3 price=46.52 support=43.4 resistance=47.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=68.43 liquidity=10638804.0 spike=0.55
- SEIG.CA: score=13.97 buy_ready=False sector_rank=3 price=182.99 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=57.11 liquidity=2057579.13 spike=0.38
- SIPC.CA: score=22.43 buy_ready=False sector_rank=3 price=3.56 support=3.4 resistance=3.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=19642906.0 spike=1.26
- SKPC.CA: score=13.54 buy_ready=False sector_rank=17 price=16.97 support=16.8 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.27 liquidity=35247536.0 spike=0.52
- SMFR.CA: score=14.34 buy_ready=False sector_rank=3 price=201.06 support=203.51 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.22 liquidity=4427278.5 spike=0.74
- SNFC.CA: score=19.91 buy_ready=False sector_rank=3 price=12.12 support=11.66 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.28 liquidity=17607438.0 spike=0.65
- SPIN.CA: score=3.45 buy_ready=False sector_rank=4 price=13.8 support=13.69 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=23.93 liquidity=2575999.0 spike=0.52
- SPMD.CA: score=21.58 buy_ready=False sector_rank=3 price=0.42 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.42 liquidity=9674260.0 spike=0.38
- SUGR.CA: score=17.55 buy_ready=False sector_rank=6 price=49.25 support=48.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=42.71 liquidity=8865769.0 spike=0.56
- SVCE.CA: score=14.91 buy_ready=False sector_rank=3 price=8.45 support=8.33 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.71 liquidity=26989780.0 spike=0.23
- SWDY.CA: score=17.75 buy_ready=False sector_rank=13 price=86.21 support=85.25 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.88 liquidity=16843886.0 spike=0.49
- TALM.CA: score=21.35 buy_ready=False sector_rank=8 price=15.95 support=15.12 resistance=17.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=48.64 liquidity=8762471.0 spike=0.66
- TMGH.CA: score=16.13 buy_ready=False sector_rank=2 price=94.21 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.65 liquidity=224139376.0 spike=0.45
- TRTO.CA: score=7.91 buy_ready=False sector_rank=3 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=189.24 spike=0.4
- UEFM.CA: score=1.48 buy_ready=False sector_rank=3 price=473.85 support=455.6 resistance=504.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=33.63 liquidity=567872.25 spike=0.41
- UEGC.CA: score=23.45 buy_ready=False sector_rank=3 price=1.4 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=72.0 liquidity=45210904.0 spike=1.77
- UNIP.CA: score=25.91 buy_ready=False sector_rank=3 price=0.32 support=0.28 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=72.13 liquidity=57806344.0 spike=3.54
- UNIT.CA: score=22.23 buy_ready=False sector_rank=2 price=13.85 support=11.28 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.32 liquidity=9097987.0 spike=0.85
- WCDF.CA: score=5.73 buy_ready=False sector_rank=3 price=539.84 support=535.0 resistance=558.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=25.38 liquidity=577913.94 spike=1.12
- WKOL.CA: score=14.03 buy_ready=False sector_rank=3 price=297.99 support=290.0 resistance=324.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.9 liquidity=4125975.0 spike=0.66
- ZEOT.CA: score=1.65 buy_ready=False sector_rank=3 price=8.69 support=8.41 resistance=9.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4742225.0 spike=0.68
- ZMID.CA: score=27.13 buy_ready=False sector_rank=2 price=6.15 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=63.11 liquidity=206021552.0 spike=0.91

## Backtesting Lite
- ZMID.CA: 180d return=62.61%, max drawdown=-19.84%, MA20>MA50 days last20=20, as_of=2026-06-08T21:00:00+00:00
- ADCI.CA: 180d return=34.64%, max drawdown=-38.87%, MA20>MA50 days last20=20, as_of=2026-06-08T21:00:00+00:00
- LUTS.CA: 180d return=15.02%, max drawdown=-19.88%, MA20>MA50 days last20=20, as_of=2026-06-08T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ZMID.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=525 sources=3 expected=Zahraa Maadi Investment and Development summary=Zahraa Maadi unveils distribution date for 2025 cash dividends; Zahraa Maadi to disburse EGP 250m dividends for 2025; Zahraa Maadi’s stock faces key resistance at EGP 5.22
  - Zahraa Maadi unveils distribution date for 2025 cash dividends: https://english.mubasher.info/news/4594804/Zahraa-Maadi-unveils-distribution-date-for-2025-cash-dividends/
  - Zahraa Maadi to disburse EGP 250m dividends for 2025: https://english.mubasher.info/news/4583591/Zahraa-Maadi-to-disburse-EGP-250m-dividends-for-2025/
  - Zahraa Maadi’s stock faces key resistance at EGP 5.22: https://english.mubasher.info/news/4563531/Zahraa-Maadi-s-stock-faces-key-resistance-at-EGP-5-22/
- ADCI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=The Arab Drug Company summary=ADCO’s net profits after tax cross EGP 182.5m in 8M-25/26; Arab Drug unveils cash dividends for FY22/23; Arab Drug’s OGM approves FY21/22 dividends
  - ADCO’s net profits after tax cross EGP 182.5m in 8M-25/26: https://english.mubasher.info/news/4587961/ADCO-s-net-profits-after-tax-cross-EGP-182-5m-in-8M-25-26/
  - Arab Drug unveils cash dividends for FY22/23: https://english.mubasher.info/news/4193946/Arab-Drug-unveils-cash-dividends-for-FY22-23/
  - Arab Drug’s OGM approves FY21/22 dividends: https://english.mubasher.info/news/4022664/Arab-Drug-s-OGM-approves-FY21-22-dividends/
- LUTS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lotus Agri Capital summary=Evidence rejected for LUTS.CA: source text did not clearly match LUTS.CA / Lotus Agri Capital.
- MICH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Chemical Industries Co. summary=Misr Chemical Industries’ net profits decline to EGP 397m in 9M-25/26; Surpassing Misr Chemical stock’s current levels would lead to historical levels – Analysis; Misr Chemical Industries posts 10% decrease in H1-25/26 net profits
  - Misr Chemical Industries’ net profits decline to EGP 397m in 9M-25/26: https://english.mubasher.info/news/4597505/Misr-Chemical-Industries-net-profits-decline-to-EGP-397m-in-9M-25-26/
  - Surpassing Misr Chemical stock’s current levels would lead to historical levels – Analysis: https://english.mubasher.info/news/4586207/Surpassing-Misr-Chemical-stock-s-current-levels-would-lead-to-historical-levels-Analysis/
  - Misr Chemical Industries posts 10% decrease in H1-25/26 net profits: https://english.mubasher.info/news/4554378/Misr-Chemical-Industries-posts-10-decrease-in-H1-25-26-net-profits/
- KZPC.CA: status=OLD_ACCEPTED latest=2024-01-01 age_days=891 sources=3 expected=Kafr El Zayat For Pesticides & Chemicals Co.(S.A.E) summary=Kafr El Zayat to set up fund with EGP 5m capital; Kafr El Zayat Pesticides targets EGP 1.73bn sales in 2024; Kafr El Zayat Pesticides’ EGM approves stock split, capital hike
  - Kafr El Zayat to set up fund with EGP 5m capital: https://english.mubasher.info/news/4201137/Kafr-El-Zayat-to-set-up-fund-with-EGP-5m-capital/
  - Kafr El Zayat Pesticides targets EGP 1.73bn sales in 2024: https://english.mubasher.info/news/4200526/Kafr-El-Zayat-Pesticides-targets-EGP-1-73bn-sales-in-2024/
  - Kafr El Zayat Pesticides’ EGM approves stock split, capital hike: https://english.mubasher.info/news/4052937/Kafr-El-Zayat-Pesticides-EGM-approves-stock-split-capital-hike/
- MAAL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Marseille Almasreia Alkhalegeya For Holding Investment SAE summary=Evidence rejected for MAAL.CA: source text did not clearly match MAAL.CA / Marseille Almasreia Alkhalegeya For Holding Investment SAE.
- ALUM.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Aluminum Company (S.A.E) summary=Arab Aluminum’s stock holds steady as bullish pattern breaks; Arab Aluminum profits rise 7% in H1-17; Arab Aluminum OGM approves EGP 1/shr dividends
  - Arab Aluminum’s stock holds steady as bullish pattern breaks: https://english.mubasher.info/news/4564438/Arab-Aluminum-s-stock-holds-steady-as-bullish-pattern-breaks/
  - Arab Aluminum profits rise 7% in H1-17: https://english.mubasher.info/news/3144589/Arab-Aluminum-profits-rise-7-in-H1-17/
  - Arab Aluminum OGM approves EGP 1/shr dividends: https://english.mubasher.info/news/3076498/Arab-Aluminum-OGM-approves-EGP-1-shr-dividends/
- ANFI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tycoon Holding Company For Financial Investments summary=Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.

## Warnings
- Evidence for ZMID.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for ADCI.CA matches the company but no source/report date was detected.
- Mubasher stock page returned no evidence titles for LUTS.CA.
- No Yahoo or Mubasher evidence found for LUTS.CA.
- Evidence rejected for LUTS.CA: source text did not clearly match LUTS.CA / Lotus Agri Capital.
- Evidence for MICH.CA matches the company but no source/report date was detected.
- Evidence for KZPC.CA matches the company but appears old; latest detected date is 2024-01-01.
- Evidence rejected for MAAL.CA: source text did not clearly match MAAL.CA / Marseille Almasreia Alkhalegeya For Holding Investment SAE.
- Evidence for ALUM.CA matches the company but no source/report date was detected.
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
