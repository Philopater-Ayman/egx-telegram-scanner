# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-06-14T14:42:34.337595+00:00
Generated Cairo: 2026-06-14 17:42
Run timing: target 15:30 Cairo | generated Cairo 2026-06-14 17:42 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-06-14 17:37

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 172/190
- Top sector: Automotive & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, June 14
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 10.53% / above MA50 47.37%
- EGX70 regime: BEARISH / above MA20 44.44% / above MA50 77.78%
- Sector breadth: 4.76%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- PHDC.CA: liquidity=810569984.0 spike=2.22 score=9.08
- CCAP.CA: liquidity=581263489.8 spike=0.78 score=17.13
- COMI.CA: liquidity=479660290.25 spike=0.93 score=14.64
- TMGH.CA: liquidity=455823712.0 spike=1.02 score=16.68
- ABUK.CA: liquidity=338685984.0 spike=2.85 score=12.26

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The local scanner stays on HOLD as EGX30 and EGX70 are both in a bearish regime with weak breadth (4.76%). Liquidity is modest and most sectors show limited upside, so new buys are blocked. The defensive risk mode reflects uncertainty over the next 1‑3 days, with support levels still far below current prices and resistance nearby for several stocks.
- EGX30/EG70 trends bearish; median 5‑day returns –5% to –4%, few stocks above MA20.
- Sector breadth low; only Automotive & Distribution, Textiles, Real Estate lead but show mixed returns.
- Top tickers (ISMQ, ADCI, GBCO, ANFI, ORWE) have high RSI or are near resistance, limiting short‑term upside.
- Liquidity spikes present but cooling; market regime flags DEFENSIVE_NO_NEW_BUY.
- Outlook remains uncertain – support levels distant, resistance close, risk mode stays defensive.

## Top Liquidity Spikes
- EASB.CA: spike=19.05 liquidity=20099006.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- PRMH.CA: spike=12.67 liquidity=188261728.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- LUTS.CA: spike=8.12 liquidity=165799296.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- TRTO.CA: spike=8.0 liquidity=5988.11 outlook=NEUTRAL score=39.39 buy_ready=False
- ISMQ.CA: spike=3.35 liquidity=205608848.0 outlook=CONSTRUCTIVE score=62 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=5.05 5d=1.06% 20d=-4.12% aboveMA50=100.0%
- #2 Textiles: score=4.25 5d=-1.86% 20d=4.28% aboveMA50=75.0%
- #3 Real Estate: score=4.09 5d=-1.44% 20d=0.0% aboveMA50=69.23%
- #4 Education: score=3.74 5d=-2.15% 20d=-3.64% aboveMA50=100.0%
- #5 Energy & Petrochemicals: score=3.39 5d=-1.29% 20d=0.1% aboveMA50=75.0%
- #6 Food, Beverages & Tobacco: score=2.49 5d=-3.69% 20d=-1.35% aboveMA50=71.43%
- #7 General / Verified EGX Expansion: score=2.39 5d=-2.24% 20d=-2.17% aboveMA50=61.54%
- #8 Healthcare: score=2.29 5d=-2.42% 20d=-4.87% aboveMA50=83.33%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ZMID.CA: BULLISH_WATCH score=90.09 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- KABO.CA: BULLISH_WATCH score=84.25 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- HELI.CA: BULLISH_WATCH score=84.09 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MENA.CA: BULLISH_WATCH score=84.09 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- UNIT.CA: BULLISH_WATCH score=84.09 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MASR.CA: BULLISH_WATCH score=83.39 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- KWIN.CA: BULLISH_WATCH score=83.39 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ARAB.CA: BULLISH_WATCH score=81.09 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- UEGC.CA: BULLISH_WATCH score=78.39 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- COSG.CA: BULLISH_WATCH score=78.39 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=12.2 buy_ready=False sector_rank=7 price=207.76 support=195.1 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.02 liquidity=2245735.25 spike=0.29
- ABUK.CA: score=12.26 buy_ready=False sector_rank=20 price=72.78 support=75.8 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.05 liquidity=338685984.0 spike=2.85
- ACAMD.CA: score=20.08 buy_ready=False sector_rank=7 price=2.32 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.18 liquidity=136396096.0 spike=1.06
- ACGC.CA: score=15.19 buy_ready=False sector_rank=2 price=9.32 support=8.89 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=33.8 liquidity=9488114.0 spike=0.16
- ADCI.CA: score=24.56 buy_ready=False sector_rank=7 price=227.96 support=202.22 resistance=228.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=71.49 liquidity=21372468.0 spike=3.3
- ADIB.CA: score=17.64 buy_ready=False sector_rank=9 price=45.66 support=44.01 resistance=49.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.64 liquidity=82574408.0 spike=0.55
- ADPC.CA: score=6.04 buy_ready=False sector_rank=7 price=3.55 support=3.45 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=27.91 liquidity=6087547.0 spike=0.24
- AFDI.CA: score=4.96 buy_ready=False sector_rank=7 price=43.14 support=40.8 resistance=43.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14656765.0 spike=0.83
- AFMC.CA: score=10.2 buy_ready=False sector_rank=7 price=71.79 support=67.0 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.18 liquidity=2242228.0 spike=0.34
- AJWA.CA: score=21.76 buy_ready=False sector_rank=7 price=158.73 support=130.01 resistance=154.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=86.04 liquidity=45048868.0 spike=2.4
- ALCN.CA: score=13.86 buy_ready=False sector_rank=17 price=29.0 support=25.51 resistance=30.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.22 liquidity=17517240.0 spike=0.93
- ALUM.CA: score=12.61 buy_ready=False sector_rank=7 price=23.62 support=23.05 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.41 liquidity=4657036.5 spike=0.23
- AMER.CA: score=19.64 buy_ready=False sector_rank=3 price=2.65 support=2.52 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=56292968.0 spike=0.51
- AMES.CA: score=4.76 buy_ready=False sector_rank=7 price=49.63 support=48.0 resistance=57.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=14.17 liquidity=1799436.88 spike=0.34
- AMIA.CA: score=19.96 buy_ready=False sector_rank=7 price=9.13 support=8.54 resistance=9.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.1 liquidity=15847819.0 spike=0.71
- AMOC.CA: score=10.36 buy_ready=False sector_rank=5 price=7.93 support=7.92 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.46 liquidity=57502636.0 spike=0.74
- ANFI.CA: score=23.6 buy_ready=False sector_rank=7 price=21.65 support=13.52 resistance=22.8 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=91.11 liquidity=143236051.08 spike=3.32
- APSW.CA: score=2.82 buy_ready=False sector_rank=7 price=8.6 support=8.24 resistance=9.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.67 liquidity=1926113.25 spike=1.97
- ARAB.CA: score=21.64 buy_ready=False sector_rank=3 price=0.21 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=63.33 liquidity=81378792.0 spike=0.95
- ARCC.CA: score=17.25 buy_ready=False sector_rank=13 price=56.41 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.58 liquidity=28369506.0 spike=0.66
- AREH.CA: score=16.96 buy_ready=False sector_rank=7 price=1.52 support=1.27 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=81.82 liquidity=21848094.0 spike=0.83
- ARVA.CA: score=7.78 buy_ready=False sector_rank=7 price=13.1 support=11.6 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=59429624.0 spike=2.41
- ASCM.CA: score=7.08 buy_ready=False sector_rank=7 price=60.98 support=57.08 resistance=61.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=146909440.0 spike=2.06
- ASPI.CA: score=21.96 buy_ready=False sector_rank=7 price=0.32 support=0.25 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=62.87 liquidity=54018084.0 spike=0.81
- ATLC.CA: score=11.11 buy_ready=False sector_rank=18 price=4.92 support=4.7 resistance=5.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.14 liquidity=2323694.75 spike=0.44
- ATQA.CA: score=12.56 buy_ready=False sector_rank=20 price=9.44 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.56 liquidity=24152124.0 spike=0.65
- AXPH.CA: score=9.71 buy_ready=False sector_rank=7 price=1119.18 support=1111.0 resistance=1190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.06 liquidity=1756232.13 spike=0.45
- BINV.CA: score=0.5 buy_ready=False sector_rank=16 price=47.48 support=45.2 resistance=47.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6372436.5 spike=0.56
- BIOC.CA: score=10.36 buy_ready=False sector_rank=7 price=71.63 support=68.34 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=41.63 liquidity=2408887.75 spike=0.44
- BTFH.CA: score=15.78 buy_ready=False sector_rank=18 price=3.05 support=2.96 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.07 liquidity=101912200.0 spike=0.44
- CAED.CA: score=6.32 buy_ready=False sector_rank=7 price=69.31 support=67.21 resistance=82.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=16.38 liquidity=3359585.0 spike=0.27
- CANA.CA: score=13.03 buy_ready=False sector_rank=9 price=35.71 support=34.07 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=59.43 liquidity=4391352.0 spike=0.3
- CCAP.CA: score=17.13 buy_ready=False sector_rank=16 price=5.14 support=4.82 resistance=5.78 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=49.06 liquidity=581263489.8 spike=0.78
- CCRS.CA: score=12.94 buy_ready=False sector_rank=7 price=2.4 support=2.21 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.21 liquidity=4984312.0 spike=0.19
- CEFM.CA: score=4.23 buy_ready=False sector_rank=7 price=105.82 support=100.53 resistance=119.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=31.67 liquidity=1278027.63 spike=0.34
- CERA.CA: score=14.5 buy_ready=False sector_rank=7 price=1.18 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.33 liquidity=5539304.5 spike=0.41
- CFGH.CA: score=2.97 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=18482.3 spike=3.0
- CICH.CA: score=0.11 buy_ready=False sector_rank=18 price=11.55 support=11.1 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=15.82 liquidity=1321643.38 spike=0.3
- CIEB.CA: score=11.06 buy_ready=False sector_rank=9 price=23.3 support=23.27 resistance=24.09 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=44.55 liquidity=6283497.19 spike=1.07
- CIRA.CA: score=15.5 buy_ready=False sector_rank=4 price=26.87 support=25.23 resistance=28.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.41 liquidity=11281293.0 spike=0.41
- CLHO.CA: score=12.9 buy_ready=False sector_rank=8 price=15.16 support=14.25 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.15 liquidity=4987420.5 spike=0.15
- CNFN.CA: score=5.22 buy_ready=False sector_rank=18 price=4.45 support=4.36 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.85 liquidity=4437170.0 spike=0.27
- COMI.CA: score=14.64 buy_ready=False sector_rank=9 price=131.69 support=129.8 resistance=136.8 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.51 liquidity=479660290.25 spike=0.93
- COPR.CA: score=17.44 buy_ready=False sector_rank=7 price=0.36 support=0.32 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.65 liquidity=49275260.0 spike=1.24
- COSG.CA: score=19.96 buy_ready=False sector_rank=7 price=1.6 support=1.49 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.0 liquidity=43949368.0 spike=0.65
- CPCI.CA: score=12.05 buy_ready=False sector_rank=7 price=360.96 support=340.01 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=64.68 liquidity=2096219.38 spike=0.71
- CSAG.CA: score=16.96 buy_ready=False sector_rank=17 price=31.0 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.14 liquidity=15163448.0 spike=1.05
- DAPH.CA: score=2.04 buy_ready=False sector_rank=7 price=78.83 support=76.6 resistance=92.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=25.25 liquidity=3086663.75 spike=0.1
- DEIN.CA: score=5.96 buy_ready=False sector_rank=7 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=1.68 buy_ready=False sector_rank=6 price=24.33 support=23.7 resistance=26.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.8 liquidity=1688415.25 spike=0.65
- DSCW.CA: score=15.96 buy_ready=False sector_rank=7 price=1.77 support=1.71 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=26642880.0 spike=0.51
- DTPP.CA: score=0.73 buy_ready=False sector_rank=7 price=120.26 support=117.01 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=21.72 liquidity=777991.06 spike=0.26
- EALR.CA: score=9.69 buy_ready=False sector_rank=7 price=356.61 support=346.01 resistance=386.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.98 liquidity=1735712.63 spike=0.36
- EASB.CA: score=9.96 buy_ready=False sector_rank=7 price=6.12 support=5.06 resistance=6.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20099006.0 spike=19.05
- EAST.CA: score=20.0 buy_ready=False sector_rank=6 price=38.23 support=37.01 resistance=39.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.78 liquidity=36414032.0 spike=0.54
- EBSC.CA: score=-0.81 buy_ready=False sector_rank=7 price=1.89 support=1.78 resistance=1.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3556214.25 spike=1.34
- ECAP.CA: score=11.65 buy_ready=False sector_rank=7 price=31.92 support=28.7 resistance=32.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=89.69 liquidity=2692345.5 spike=0.5
- EDFM.CA: score=8.44 buy_ready=False sector_rank=7 price=334.76 support=320.2 resistance=355.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=50.76 liquidity=485850.63 spike=0.71
- EEII.CA: score=15.71 buy_ready=False sector_rank=7 price=2.39 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=53.49 liquidity=5757538.5 spike=0.29
- EFIC.CA: score=-0.37 buy_ready=False sector_rank=20 price=204.55 support=192.01 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=15.17 liquidity=2074727.0 spike=0.58
- EFID.CA: score=20.0 buy_ready=False sector_rank=6 price=28.69 support=27.06 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.41 liquidity=29857514.0 spike=0.39
- EFIH.CA: score=11.38 buy_ready=False sector_rank=21 price=21.1 support=20.2 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=30.35 liquidity=65151524.0 spike=1.15
- EGAL.CA: score=11.56 buy_ready=False sector_rank=20 price=313.21 support=305.01 resistance=344.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=15.38 liquidity=39106228.0 spike=0.38
- EGAS.CA: score=20.36 buy_ready=False sector_rank=5 price=52.52 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=62.8 liquidity=11650943.0 spike=0.98
- EGBE.CA: score=2.66 buy_ready=False sector_rank=9 price=0.44 support=0.44 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=30.82 liquidity=23749.06 spike=0.17
- EGCH.CA: score=16.56 buy_ready=False sector_rank=20 price=13.3 support=13.2 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.28 liquidity=69851656.0 spike=0.61
- EGSA.CA: score=2.43 buy_ready=False sector_rank=12 price=8.74 support=8.3 resistance=9.19 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=25.37 liquidity=6598.7 spike=0.45
- EGTS.CA: score=19.64 buy_ready=False sector_rank=3 price=18.47 support=13.61 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.27 liquidity=78349144.0 spike=0.65
- EHDR.CA: score=21.48 buy_ready=False sector_rank=7 price=2.79 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.71 liquidity=93126472.0 spike=1.76
- EKHO.CA: score=10.36 buy_ready=False sector_rank=5 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=12.72 buy_ready=False sector_rank=19 price=2.11 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=46.43 liquidity=10626683.0 spike=0.39
- ELKA.CA: score=20.96 buy_ready=False sector_rank=7 price=1.26 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.86 liquidity=30749038.0 spike=0.7
- ELNA.CA: score=6.89 buy_ready=False sector_rank=7 price=37.74 support=37.11 resistance=41.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=43.61 liquidity=831490.13 spike=2.05
- ELSH.CA: score=17.04 buy_ready=False sector_rank=7 price=13.27 support=8.1 resistance=14.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=78.34 liquidity=171622944.0 spike=1.04
- ELWA.CA: score=19.59 buy_ready=False sector_rank=7 price=2.15 support=1.79 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=78.95 liquidity=8375047.0 spike=3.13
- EMFD.CA: score=7.4 buy_ready=False sector_rank=3 price=12.02 support=11.46 resistance=12.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=327333376.0 spike=1.38
- ENGC.CA: score=21.96 buy_ready=False sector_rank=7 price=34.87 support=32.31 resistance=35.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=58.88 liquidity=10267742.0 spike=0.75
- EOSB.CA: score=15.44 buy_ready=False sector_rank=7 price=1.48 support=1.34 resistance=1.49 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=299753.28 spike=2.59
- EPCO.CA: score=9.82 buy_ready=False sector_rank=7 price=9.09 support=8.56 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.45 liquidity=1863824.38 spike=0.16
- EPPK.CA: score=6.03 buy_ready=False sector_rank=7 price=11.86 support=11.67 resistance=13.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=51.18 liquidity=1075914.13 spike=0.97
- ETEL.CA: score=11.62 buy_ready=False sector_rank=12 price=90.72 support=89.8 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=28.49 liquidity=176552480.0 spike=2.1
- ETRS.CA: score=5.06 buy_ready=False sector_rank=7 price=9.75 support=9.15 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=59669832.0 spike=1.05
- EXPA.CA: score=17.64 buy_ready=False sector_rank=9 price=18.57 support=18.31 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.4 liquidity=30592178.0 spike=0.83
- FAIT.CA: score=5.18 buy_ready=False sector_rank=9 price=36.46 support=35.0 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=22.01 liquidity=2539355.0 spike=0.41
- FAITA.CA: score=9.89 buy_ready=False sector_rank=9 price=1.0 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=46654.87 spike=1.1
- FERC.CA: score=5.92 buy_ready=False sector_rank=20 price=75.92 support=75.0 resistance=81.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=2356240.25 spike=0.42
- FWRY.CA: score=8.08 buy_ready=False sector_rank=21 price=18.46 support=17.71 resistance=20.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.48 liquidity=204596992.0 spike=0.75
- GBCO.CA: score=24.02 buy_ready=False sector_rank=1 price=28.37 support=25.25 resistance=29.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.17 liquidity=99497280.0 spike=0.84
- GDWA.CA: score=11.17 buy_ready=False sector_rank=7 price=0.79 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.89 liquidity=7209314.5 spike=0.55
- GGCC.CA: score=12.7 buy_ready=False sector_rank=7 price=0.41 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=3748689.0 spike=0.5
- GIHD.CA: score=7.84 buy_ready=False sector_rank=7 price=40.45 support=35.15 resistance=44.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=49.48 liquidity=882912.88 spike=0.19
- GMCI.CA: score=4.39 buy_ready=False sector_rank=7 price=1.7 support=1.68 resistance=1.84 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=39.29 liquidity=355529.51 spike=1.04
- GRCA.CA: score=6.63 buy_ready=False sector_rank=7 price=54.11 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.73 liquidity=1678164.5 spike=0.19
- GSSC.CA: score=1.96 buy_ready=False sector_rank=7 price=248.65 support=228.1 resistance=272.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=12.69 liquidity=2004417.88 spike=0.32
- GTWL.CA: score=2.36 buy_ready=False sector_rank=7 price=46.82 support=45.47 resistance=59.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=25.6 liquidity=2403199.25 spike=0.34
- HDBK.CA: score=15.22 buy_ready=False sector_rank=9 price=138.0 support=138.0 resistance=146.58 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=37.06 liquidity=13569678.0 spike=1.29
- HELI.CA: score=21.64 buy_ready=False sector_rank=3 price=6.57 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.56 liquidity=97570640.0 spike=0.59
- HRHO.CA: score=12.78 buy_ready=False sector_rank=18 price=26.6 support=25.8 resistance=29.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.27 liquidity=102756992.0 spike=0.69
- ICID.CA: score=17.02 buy_ready=False sector_rank=7 price=6.82 support=4.5 resistance=6.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=87.25 liquidity=15977579.0 spike=1.03
- IDRE.CA: score=15.98 buy_ready=False sector_rank=7 price=42.71 support=41.01 resistance=49.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.29 liquidity=8026341.5 spike=0.25
- IFAP.CA: score=2.45 buy_ready=False sector_rank=15 price=19.49 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=32.23 liquidity=4265727.0 spike=0.44
- INFI.CA: score=8.99 buy_ready=False sector_rank=7 price=98.0 support=97.0 resistance=109.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=24.0 liquidity=7037257.0 spike=0.47
- IRON.CA: score=9.19 buy_ready=False sector_rank=20 price=32.28 support=31.3 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.36 liquidity=6628499.5 spike=0.84
- ISMA.CA: score=18.96 buy_ready=False sector_rank=7 price=30.72 support=22.7 resistance=30.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=90.06 liquidity=37420888.0 spike=0.91
- ISMQ.CA: score=25.26 buy_ready=False sector_rank=20 price=8.37 support=7.27 resistance=8.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.36 liquidity=205608848.0 spike=3.35
- ISPH.CA: score=4.92 buy_ready=False sector_rank=8 price=12.03 support=11.82 resistance=12.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=95602576.0 spike=0.72
- JUFO.CA: score=22.0 buy_ready=False sector_rank=6 price=30.48 support=26.51 resistance=30.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.57 liquidity=20067008.0 spike=0.45
- KABO.CA: score=19.02 buy_ready=False sector_rank=2 price=6.26 support=5.92 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=60.91 liquidity=6317462.5 spike=0.3
- KWIN.CA: score=14.18 buy_ready=False sector_rank=7 price=72.0 support=69.0 resistance=78.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.18 liquidity=4226425.0 spike=0.98
- KZPC.CA: score=14.15 buy_ready=False sector_rank=7 price=10.64 support=10.3 resistance=11.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=53.62 liquidity=4195794.0 spike=0.32
- LCSW.CA: score=12.51 buy_ready=False sector_rank=13 price=26.67 support=26.0 resistance=28.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=49.63 liquidity=5256203.0 spike=0.35
- LUTS.CA: score=9.96 buy_ready=False sector_rank=7 price=0.72 support=0.65 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=165799296.0 spike=8.12
- MAAL.CA: score=11.51 buy_ready=False sector_rank=7 price=5.78 support=4.44 resistance=6.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=78.07 liquidity=4556184.0 spike=0.35
- MASR.CA: score=19.96 buy_ready=False sector_rank=7 price=6.95 support=6.54 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.8 liquidity=56499592.0 spike=0.93
- MBSC.CA: score=12.25 buy_ready=False sector_rank=13 price=273.87 support=261.52 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.43 liquidity=41309556.0 spike=0.88
- MCQE.CA: score=9.25 buy_ready=False sector_rank=13 price=179.93 support=174.0 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=11.65 liquidity=17472570.0 spike=0.97
- MCRO.CA: score=13.96 buy_ready=False sector_rank=7 price=1.24 support=1.2 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=23317356.0 spike=0.39
- MENA.CA: score=21.64 buy_ready=False sector_rank=3 price=6.69 support=5.83 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.35 liquidity=10759872.0 spike=0.64
- MEPA.CA: score=18.75 buy_ready=False sector_rank=7 price=1.72 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=8796484.0 spike=0.47
- MFPC.CA: score=10.98 buy_ready=False sector_rank=20 price=38.48 support=39.47 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.69 liquidity=183146704.0 spike=2.21
- MFSC.CA: score=7.78 buy_ready=False sector_rank=7 price=46.01 support=43.0 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=19.86 liquidity=4820987.5 spike=0.3
- MHOT.CA: score=10.44 buy_ready=False sector_rank=11 price=29.4 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.87 liquidity=3005931.25 spike=0.14
- MICH.CA: score=21.4 buy_ready=False sector_rank=7 price=36.94 support=35.01 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=63.94 liquidity=9442013.0 spike=0.66
- MILS.CA: score=19.96 buy_ready=False sector_rank=7 price=147.09 support=127.01 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.02 liquidity=17905082.0 spike=0.94
- MIPH.CA: score=8.75 buy_ready=False sector_rank=8 price=658.46 support=640.0 resistance=717.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=52.05 liquidity=837585.88 spike=0.28
- MOED.CA: score=3.24 buy_ready=False sector_rank=7 price=0.68 support=0.65 resistance=0.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=26.97 liquidity=4282047.5 spike=0.36
- MOIL.CA: score=8.44 buy_ready=False sector_rank=5 price=0.47 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=63.77 liquidity=85277.2 spike=0.44
- MOIN.CA: score=7.59 buy_ready=False sector_rank=7 price=24.99 support=24.02 resistance=26.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=55.88 liquidity=638638.81 spike=0.34
- MOSC.CA: score=8.74 buy_ready=False sector_rank=7 price=298.21 support=254.15 resistance=298.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27307492.0 spike=2.89
- MPCI.CA: score=19.96 buy_ready=False sector_rank=7 price=222.01 support=197.0 resistance=238.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.0 liquidity=43972156.0 spike=0.5
- MPCO.CA: score=21.18 buy_ready=False sector_rank=15 price=1.78 support=1.54 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=64.15 liquidity=54271492.0 spike=0.72
- MPRC.CA: score=19.52 buy_ready=False sector_rank=7 price=32.15 support=30.61 resistance=34.55 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=61.21 liquidity=9565139.85 spike=0.52
- MTIE.CA: score=20.43 buy_ready=False sector_rank=1 price=9.0 support=8.65 resistance=9.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=8407575.0 spike=0.42
- NAHO.CA: score=3.96 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=6412.78 spike=0.2
- NCCW.CA: score=16.96 buy_ready=False sector_rank=7 price=6.52 support=5.13 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=76.78 liquidity=21541562.0 spike=0.81
- NEDA.CA: score=8.66 buy_ready=False sector_rank=7 price=2.75 support=2.65 resistance=2.87 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=53.57 liquidity=503871.5 spike=1.1
- NHPS.CA: score=6.09 buy_ready=False sector_rank=7 price=67.76 support=65.03 resistance=72.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=42.32 liquidity=2132134.0 spike=0.35
- NINH.CA: score=5.14 buy_ready=False sector_rank=7 price=17.35 support=16.8 resistance=20.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=24.12 liquidity=2179252.5 spike=0.26
- NIPH.CA: score=19.92 buy_ready=False sector_rank=8 price=163.97 support=155.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.42 liquidity=80359528.0 spike=0.78
- OBRI.CA: score=9.04 buy_ready=False sector_rank=7 price=36.14 support=34.99 resistance=37.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35980044.0 spike=3.04
- OCDI.CA: score=17.26 buy_ready=False sector_rank=3 price=20.57 support=20.0 resistance=23.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=46.58 liquidity=49832636.0 spike=1.31
- OCPH.CA: score=5.41 buy_ready=False sector_rank=7 price=345.9 support=337.0 resistance=404.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=28.14 liquidity=2449263.5 spike=0.31
- ODIN.CA: score=5.02 buy_ready=False sector_rank=7 price=2.14 support=2.06 resistance=2.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11079854.0 spike=1.03
- OFH.CA: score=16.96 buy_ready=False sector_rank=7 price=0.61 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.54 liquidity=42702820.0 spike=2.0
- OIH.CA: score=9.13 buy_ready=False sector_rank=16 price=1.4 support=1.33 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=64454868.0 spike=0.64
- OLFI.CA: score=19.08 buy_ready=False sector_rank=6 price=22.64 support=21.0 resistance=22.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.88 liquidity=37714248.0 spike=2.04
- ORAS.CA: score=4.6 buy_ready=False sector_rank=10 price=767.38 support=756.01 resistance=779.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=278044064.0 spike=1.0
- ORHD.CA: score=7.84 buy_ready=False sector_rank=3 price=38.23 support=36.92 resistance=38.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=292637952.0 spike=1.6
- ORWE.CA: score=22.7 buy_ready=False sector_rank=2 price=23.21 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=64.63 liquidity=22590208.0 spike=0.5
- PHAR.CA: score=17.92 buy_ready=False sector_rank=8 price=84.26 support=83.02 resistance=92.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.57 liquidity=20298880.0 spike=0.64
- PHDC.CA: score=9.08 buy_ready=False sector_rank=3 price=15.75 support=15.01 resistance=16.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=810569984.0 spike=2.22
- PHTV.CA: score=4.61 buy_ready=False sector_rank=7 price=205.08 support=201.55 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=25.56 liquidity=1653637.88 spike=0.12
- POUL.CA: score=15.0 buy_ready=False sector_rank=6 price=35.08 support=34.8 resistance=39.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.04 liquidity=33152548.0 spike=0.72
- PRCL.CA: score=19.25 buy_ready=False sector_rank=13 price=24.3 support=21.01 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.4 liquidity=22188128.0 spike=0.78
- PRDC.CA: score=18.64 buy_ready=False sector_rank=3 price=6.42 support=5.3 resistance=6.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=80.77 liquidity=28179418.0 spike=0.32
- PRMH.CA: score=9.96 buy_ready=False sector_rank=7 price=2.86 support=2.67 resistance=2.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=188261728.0 spike=12.67
- RACC.CA: score=14.85 buy_ready=False sector_rank=7 price=9.84 support=9.38 resistance=10.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=6892887.5 spike=0.51
- RAKT.CA: score=2.08 buy_ready=False sector_rank=7 price=22.9 support=22.1 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=34.13 liquidity=421505.69 spike=1.35
- RAYA.CA: score=17.22 buy_ready=False sector_rank=14 price=6.96 support=6.7 resistance=8.0 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=45.9 liquidity=76206843.06 spike=0.92
- RMDA.CA: score=19.92 buy_ready=False sector_rank=8 price=5.2 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=33406418.0 spike=0.34
- ROTO.CA: score=14.39 buy_ready=False sector_rank=7 price=33.77 support=32.66 resistance=36.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=52.08 liquidity=4435845.0 spike=0.33
- RREI.CA: score=19.4 buy_ready=False sector_rank=7 price=3.53 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.7 liquidity=9444142.0 spike=0.42
- RTVC.CA: score=11.16 buy_ready=False sector_rank=7 price=3.83 support=3.75 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=52.11 liquidity=4205596.5 spike=0.62
- RUBX.CA: score=11.63 buy_ready=False sector_rank=7 price=10.03 support=9.8 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=40.41 liquidity=7676661.0 spike=0.56
- SAUD.CA: score=12.18 buy_ready=False sector_rank=9 price=21.53 support=20.82 resistance=23.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.87 liquidity=7535178.0 spike=0.54
- SCEM.CA: score=12.25 buy_ready=False sector_rank=13 price=62.3 support=59.3 resistance=69.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.59 liquidity=10110347.0 spike=0.26
- SCFM.CA: score=6.52 buy_ready=False sector_rank=7 price=252.57 support=248.1 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.94 liquidity=6567005.0 spike=0.49
- SCTS.CA: score=5.66 buy_ready=False sector_rank=4 price=609.76 support=590.01 resistance=689.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=25.78 liquidity=2164610.5 spike=0.22
- SDTI.CA: score=18.86 buy_ready=False sector_rank=7 price=47.52 support=43.4 resistance=47.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=62.56 liquidity=6901204.0 spike=0.37
- SEIG.CA: score=9.47 buy_ready=False sector_rank=7 price=180.81 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=53.36 liquidity=1514527.0 spike=0.29
- SIPC.CA: score=10.96 buy_ready=False sector_rank=7 price=3.47 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.82 liquidity=6001070.5 spike=0.41
- SKPC.CA: score=12.56 buy_ready=False sector_rank=20 price=16.53 support=16.29 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.6 liquidity=23693074.0 spike=0.38
- SMFR.CA: score=2.31 buy_ready=False sector_rank=7 price=201.06 support=192.0 resistance=222.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=28.85 liquidity=2353430.5 spike=0.4
- SNFC.CA: score=19.96 buy_ready=False sector_rank=7 price=12.41 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.44 liquidity=10322709.0 spike=0.38
- SPIN.CA: score=8.76 buy_ready=False sector_rank=2 price=14.01 support=13.61 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.94 liquidity=1057911.5 spike=0.22
- SPMD.CA: score=11.79 buy_ready=False sector_rank=7 price=0.41 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.19 liquidity=3835272.25 spike=0.16
- SUGR.CA: score=11.04 buy_ready=False sector_rank=6 price=48.95 support=48.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.0 liquidity=3046183.75 spike=0.2
- SVCE.CA: score=12.96 buy_ready=False sector_rank=7 price=8.44 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.69 liquidity=17134602.0 spike=0.18
- SWDY.CA: score=16.72 buy_ready=False sector_rank=19 price=86.37 support=84.01 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=39.98 liquidity=10287706.0 spike=0.43
- TALM.CA: score=10.15 buy_ready=False sector_rank=4 price=16.11 support=15.12 resistance=16.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.26 liquidity=2657439.75 spike=0.21
- TMGH.CA: score=16.68 buy_ready=False sector_rank=3 price=95.97 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.48 liquidity=455823712.0 spike=1.02
- TRTO.CA: score=10.96 buy_ready=False sector_rank=7 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=5988.11 spike=8.0
- UEFM.CA: score=-0.57 buy_ready=False sector_rank=7 price=468.67 support=455.6 resistance=500.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=26.76 liquidity=472015.81 spike=0.5
- UEGC.CA: score=21.96 buy_ready=False sector_rank=7 price=1.4 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.67 liquidity=12929501.0 spike=0.47
- UNIP.CA: score=15.96 buy_ready=False sector_rank=7 price=0.32 support=0.28 resistance=0.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=80.39 liquidity=17299114.0 spike=0.88
- UNIT.CA: score=12.89 buy_ready=False sector_rank=3 price=13.82 support=12.07 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=61.5 liquidity=1255649.38 spike=0.11
- WCDF.CA: score=-3.97 buy_ready=False sector_rank=7 price=507.59 support=450.0 resistance=544.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=469647.13 spike=1.3
- WKOL.CA: score=9.09 buy_ready=False sector_rank=7 price=292.5 support=290.0 resistance=319.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.89 liquidity=4093111.5 spike=1.02
- ZEOT.CA: score=20.01 buy_ready=False sector_rank=7 price=9.24 support=8.41 resistance=9.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=63.78 liquidity=7630162.5 spike=1.21
- ZMID.CA: score=21.64 buy_ready=False sector_rank=3 price=6.24 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.69 liquidity=151920240.0 spike=0.65

## Backtesting Lite
- ISMQ.CA: 180d return=39.19%, max drawdown=-16.39%, MA20>MA50 days last20=20, as_of=2026-06-10T21:00:00+00:00
- ADCI.CA: 180d return=35.14%, max drawdown=-38.87%, MA20>MA50 days last20=20, as_of=2026-06-10T21:00:00+00:00
- GBCO.CA: 180d return=31.89%, max drawdown=-24.35%, MA20>MA50 days last20=20, as_of=2026-06-10T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ISMQ.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Iron and Steel for Mines and Quarries summary=Iron and Steel for Mines and Quarries stock stabilizes above key support after correction; Will Iron and Steel for Mines and Quarries stock hit new historical peaks?; Iron and Steel for Mines and Quarries expects EGP 448m net profit in FY24/25
  - Iron and Steel for Mines and Quarries stock stabilizes above key support after correction: https://english.mubasher.info/news/4578786/Iron-and-Steel-for-Mines-and-Quarries-stock-stabilizes-above-key-support-after-correction/
  - Will Iron and Steel for Mines and Quarries stock hit new historical peaks?: https://english.mubasher.info/news/4556956/Will-Iron-and-Steel-for-Mines-and-Quarries-stock-hit-new-historical-peaks-/
  - Iron and Steel for Mines and Quarries expects EGP 448m net profit in FY24/25: https://english.mubasher.info/news/4249734/Iron-and-Steel-for-Mines-and-Quarries-expects-EGP-448m-net-profit-in-FY24-25/
- ADCI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=The Arab Drug Company summary=ADCO’s net profits after tax cross EGP 182.5m in 8M-25/26; Arab Drug unveils cash dividends for FY22/23; Arab Drug’s OGM approves FY21/22 dividends
  - ADCO’s net profits after tax cross EGP 182.5m in 8M-25/26: https://english.mubasher.info/news/4587961/ADCO-s-net-profits-after-tax-cross-EGP-182-5m-in-8M-25-26/
  - Arab Drug unveils cash dividends for FY22/23: https://english.mubasher.info/news/4193946/Arab-Drug-unveils-cash-dividends-for-FY22-23/
  - Arab Drug’s OGM approves FY21/22 dividends: https://english.mubasher.info/news/4022664/Arab-Drug-s-OGM-approves-FY21-22-dividends/
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- ANFI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tycoon Holding Company For Financial Investments summary=Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- ORWE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=529 sources=3 expected=Oriental Weavers summary=Oriental Weavers to disburse EGP 1.5/shr dividends for 2025; Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025; Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25
  - Oriental Weavers to disburse EGP 1.5/shr dividends for 2025: https://english.mubasher.info/news/4590236/Oriental-Weavers-to-disburse-EGP-1-5-shr-dividends-for-2025/
  - Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025: https://english.mubasher.info/news/4562972/Oriental-Weavers-consolidated-profits-cross-EGP-2-2bn-in-2025/
  - Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25: https://english.mubasher.info/news/4487417/Oriental-Weavers-generates-EGP-12-5bn-consolidated-sales-in-H1-25/
- JUFO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Juhayna Food Industries summary=Evidence rejected for JUFO.CA: source text did not clearly match JUFO.CA / Juhayna Food Industries.
- ASPI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Aspire Capital Holding for Financial Investments summary=Aspire Capital records higher consolidated net profits at over EGP 42m in 9M-25; PREDCO, Aspire Holding consider establishing mortgage company; Pioneers Holding gets EGX&#39;s approval for capital cut, name change
  - Aspire Capital records higher consolidated net profits at over EGP 42m in 9M-25: https://english.mubasher.info/news/4541324/Aspire-Capital-records-higher-consolidated-net-profits-at-over-EGP-42m-in-9M-25/
  - PREDCO, Aspire Holding consider establishing mortgage company: https://english.mubasher.info/news/4185438/PREDCO-Aspire-Holding-consider-establishing-mortgage-company/
  - Pioneers Holding gets EGX&#39;s approval for capital cut, name change: https://english.mubasher.info/news/3861454/Pioneers-Holding-gets-EGX-s-approval-for-capital-cut-name-change/
- ENGC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Industrial Engineering Company for Construction and Development (ICON) (S.A.E) summary=Evidence rejected for ENGC.CA: source text did not clearly match ENGC.CA / Industrial Engineering Company for Construction and Development (ICON) (S.A.E).

## Warnings
- Evidence for ISMQ.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for ADCI.CA matches the company but no source/report date was detected.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- Evidence for ORWE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for JUFO.CA: source text did not clearly match JUFO.CA / Juhayna Food Industries.
- Evidence for ASPI.CA matches the company but no source/report date was detected.
- Evidence rejected for ENGC.CA: source text did not clearly match ENGC.CA / Industrial Engineering Company for Construction and Development (ICON) (S.A.E).
