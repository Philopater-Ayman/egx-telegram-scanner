# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-07-08T10:15:33.841396+00:00
Generated Cairo: 2026-07-08 13:15
Run timing: target 11:00 Cairo | generated Cairo 2026-07-08 13:15 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-07-08 13:11

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 59
- Data quality issues: 0
- Tradeable price/liquidity tickers: 185/190
- Top sector: Technology & Distribution

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, July 08
- Freshness: DELAYED
- EGX30 regime: CONSTRUCTIVE / above MA20 60.0% / above MA50 50.0%
- EGX70 regime: BULLISH / above MA20 72.5% / above MA50 75.0%
- Sector breadth: 71.43%
- Risk mode: BROAD_RISK_ON

## Top Liquidity
- CCAP.CA: liquidity=817579584.0 spike=1.24 score=26.38
- TMGH.CA: liquidity=251456832.0 spike=0.7 score=30.9
- COMI.CA: liquidity=243258800.0 spike=0.53 score=29.4
- ORAS.CA: liquidity=196972160.0 spike=1.0 score=9.1
- GTWL.CA: liquidity=193510864.0 spike=3.1 score=29.1

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b-20230311:free
- Summary: Scanner highlighted several tickets with accumulation spikes and bullish‑watch outlooks while EGX30 shows a constructive trend and EGX70 is bullish, pushing risk mode to broad risk‑on; however, limited evidence and proximity to resistance keep the outlook uncertain for the next 1‑3 days.
- Liquidity: most flagged stocks exhibit accumulation spikes (liquidity_spike >4) indicating short‑term buying interest, though a few show cooling liquidity.
- Sector & technicals: tickets are generally close to their 20‑day resistance (small resistance_distance_pct) while support lies farther away, suggesting limited upside in the short term unless resistance breaks.
- Market regime: EGX30 constructive (≈60% above MA20) and EGX70 bullish (≈73% above MA20) shift risk mode to broad risk‑on, allowing higher tolerance but still dependent on overall breadth.
- Uncertainty: evidence scores are low or rejected for most tickers, sector ranks are not in leading groups, so the bullish watch remains tentative and a pull‑back is possible if resistance holds.

## Top Liquidity Spikes
- SEIG.CA: spike=19.38 liquidity=89949536.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AMES.CA: spike=6.9 liquidity=123135264.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MIPH.CA: spike=4.98 liquidity=9449643.0 outlook=BULLISH_WATCH score=83.39 buy_ready=True
- BIOC.CA: spike=4.75 liquidity=12576788.0 outlook=BULLISH_WATCH score=82.82 buy_ready=True
- RREI.CA: spike=4.61 liquidity=68347744.0 outlook=BULLISH_WATCH score=84.82 buy_ready=True

## Sector Leaderboard
- #1 Technology & Distribution: score=13.02 5d=10.27% 20d=8.05% aboveMA50=100.0%
- #2 Fintech & Payments: score=11.3 5d=10.64% 20d=8.23% aboveMA50=50.0%
- #3 Real Estate: score=10.88 5d=6.47% 20d=8.54% aboveMA50=100.0%
- #4 Telecommunications: score=10.08 5d=5.4% 20d=2.71% aboveMA50=100.0%
- #5 Investment Holding: score=9.82 5d=7.61% 20d=0.71% aboveMA50=66.67%
- #6 Transportation & Logistics: score=8.58 5d=3.08% 20d=2.75% aboveMA50=100.0%
- #7 Textiles: score=8.25 5d=4.93% 20d=1.46% aboveMA50=100.0%
- #8 Automotive & Distribution: score=8.01 5d=2.21% 20d=10.79% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ARAB.CA: BULLISH_WATCH score=100 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- MENA.CA: BULLISH_WATCH score=100 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- TMGH.CA: BULLISH_WATCH score=98 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- EALR.CA: BULLISH_WATCH score=94.82 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- SPMD.CA: BULLISH_WATCH score=94.82 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- MICH.CA: BULLISH_WATCH score=94.82 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- PRDC.CA: BULLISH_WATCH score=94 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- HELI.CA: BULLISH_WATCH score=93 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended; close to resistance
- BINV.CA: BULLISH_WATCH score=90.82 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ORHD.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended

## BUY-Ready Candidates
- RREI.CA: rank=34.9 outlook=BULLISH_WATCH outlook_score=84.82 sector_rank=11 price=3.78 support=3.34 resistance=3.81 liquidity=68347744.0
- BIOC.CA: rank=32.9 outlook=BULLISH_WATCH outlook_score=82.82 sector_rank=11 price=73.4 support=66.75 resistance=74.2 liquidity=12576788.0
- MIPH.CA: rank=32.35 outlook=BULLISH_WATCH outlook_score=83.39 sector_rank=10 price=699.82 support=630.13 resistance=710.0 liquidity=9449643.0
- PRDC.CA: rank=30.9 outlook=BULLISH_WATCH outlook_score=94 sector_rank=3 price=8.4 support=5.91 resistance=9.0 liquidity=60709856.0
- TMGH.CA: rank=30.9 outlook=BULLISH_WATCH outlook_score=98 sector_rank=3 price=96.45 support=92.1 resistance=99.43 liquidity=251456832.0
- LCSW.CA: rank=30.28 outlook=BULLISH_WATCH outlook_score=76.65 sector_rank=12 price=31.0 support=26.0 resistance=31.33 liquidity=103995776.0
- EALR.CA: rank=29.96 outlook=BULLISH_WATCH outlook_score=94.82 sector_rank=11 price=369.85 support=332.0 resistance=425.0 liquidity=18521188.0
- HELI.CA: rank=29.94 outlook=BULLISH_WATCH outlook_score=93 sector_rank=3 price=6.76 support=6.28 resistance=6.84 liquidity=166815696.0
- MASR.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=70.82 sector_rank=11 price=7.6 support=6.54 resistance=7.84 liquidity=65346692.0
- COMI.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=77.76 sector_rank=17 price=134.52 support=126.21 resistance=137.98 liquidity=243258800.0

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=25.42 buy_ready=False sector_rank=11 price=223.93 support=196.0 resistance=247.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=77.59 liquidity=15908447.0 spike=1.26
- ABUK.CA: score=21.92 buy_ready=False sector_rank=19 price=70.92 support=66.66 resistance=82.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=42.97 liquidity=140517264.0 spike=1.13
- ACAMD.CA: score=27.9 buy_ready=True sector_rank=11 price=2.32 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=51.43 liquidity=52393872.0 spike=0.47
- ACGC.CA: score=25.9 buy_ready=True sector_rank=7 price=9.53 support=8.92 resistance=10.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=55.8 liquidity=10249210.0 spike=0.36
- ADCI.CA: score=18.8 buy_ready=False sector_rank=11 price=232.41 support=215.04 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=60.85 liquidity=4903688.5 spike=0.41
- ADIB.CA: score=27.4 buy_ready=True sector_rank=17 price=46.68 support=44.01 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=49.7 liquidity=84633848.0 spike=0.98
- ADPC.CA: score=16.81 buy_ready=False sector_rank=11 price=3.53 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=47.12 liquidity=5909565.5 spike=0.4
- AFDI.CA: score=20.03 buy_ready=True sector_rank=11 price=45.35 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=65.15 liquidity=4127573.25 spike=0.32
- AFMC.CA: score=22.5 buy_ready=True sector_rank=11 price=71.94 support=66.0 resistance=74.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=59.46 liquidity=2564538.5 spike=1.02
- AJWA.CA: score=19.58 buy_ready=True sector_rank=11 price=177.0 support=135.0 resistance=190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=39.45 liquidity=3683722.0 spike=0.14
- ALCN.CA: score=26.86 buy_ready=True sector_rank=6 price=28.98 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=58.48 liquidity=6963358.0 spike=0.61
- ALUM.CA: score=29.32 buy_ready=True sector_rank=11 price=23.5 support=20.55 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=53.5 liquidity=13896651.0 spike=1.71
- AMER.CA: score=30.08 buy_ready=False sector_rank=3 price=2.75 support=2.28 resistance=2.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=70.24 liquidity=103842384.0 spike=1.59
- AMES.CA: score=15.9 buy_ready=False sector_rank=11 price=67.5 support=58.32 resistance=69.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=123135264.0 spike=6.9
- AMIA.CA: score=22.79 buy_ready=False sector_rank=11 price=8.93 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=53.76 liquidity=6888627.5 spike=0.65
- AMOC.CA: score=28.04 buy_ready=False sector_rank=14 price=8.11 support=7.42 resistance=8.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=45.37 liquidity=117680720.0 spike=2.57
- ANFI.CA: score=12.23 buy_ready=False sector_rank=11 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=STALE RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=12.58 buy_ready=False sector_rank=11 price=8.49 support=8.0 resistance=9.0 source=Yahoo Finance as_of=2026-07-06T21:00:00+00:00 freshness=FRESH RSI=48.41 liquidity=677867.05 spike=0.84
- ARAB.CA: score=29.36 buy_ready=True sector_rank=3 price=0.22 support=0.2 resistance=0.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=58.18 liquidity=87363368.0 spike=1.23
- ARCC.CA: score=20.9 buy_ready=False sector_rank=12 price=55.19 support=53.0 resistance=58.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=49.07 liquidity=11061604.0 spike=0.44
- AREH.CA: score=23.9 buy_ready=False sector_rank=11 price=1.55 support=1.42 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=51.28 liquidity=10251676.0 spike=0.27
- ARVA.CA: score=19.15 buy_ready=False sector_rank=11 price=10.92 support=10.3 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=48.17 liquidity=5254292.5 spike=0.2
- ASCM.CA: score=23.9 buy_ready=False sector_rank=11 price=57.76 support=54.12 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=49.68 liquidity=16189535.0 spike=0.19
- ASPI.CA: score=23.9 buy_ready=False sector_rank=11 price=0.32 support=0.3 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=54.76 liquidity=12777560.0 spike=0.23
- ATLC.CA: score=20.55 buy_ready=True sector_rank=15 price=5.17 support=4.7 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=54.29 liquidity=2654505.5 spike=0.37
- ATQA.CA: score=22.66 buy_ready=False sector_rank=19 price=9.61 support=9.02 resistance=10.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=52.68 liquidity=17888012.0 spike=0.51
- AXPH.CA: score=21.87 buy_ready=True sector_rank=11 price=1177.42 support=1073.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=62.2 liquidity=3533873.0 spike=1.22
- BINV.CA: score=21.46 buy_ready=True sector_rank=5 price=47.28 support=44.02 resistance=51.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=56.15 liquidity=5563794.5 spike=0.8
- BIOC.CA: score=32.9 buy_ready=True sector_rank=11 price=73.4 support=66.75 resistance=74.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=50.68 liquidity=12576788.0 spike=4.75
- BTFH.CA: score=23.9 buy_ready=False sector_rank=15 price=3.05 support=2.91 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=60.87 liquidity=177890992.0 spike=0.91
- CAED.CA: score=21.47 buy_ready=True sector_rank=11 price=71.52 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=56.68 liquidity=3572707.75 spike=0.73
- CANA.CA: score=15.66 buy_ready=False sector_rank=17 price=36.03 support=34.5 resistance=39.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=43.5 liquidity=3260124.0 spike=0.29
- CCAP.CA: score=26.38 buy_ready=True sector_rank=5 price=5.23 support=4.65 resistance=5.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=52.08 liquidity=817579584.0 spike=1.24
- CCRS.CA: score=12.25 buy_ready=False sector_rank=11 price=2.33 support=2.18 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=33.93 liquidity=3345207.25 spike=0.25
- CEFM.CA: score=16.18 buy_ready=False sector_rank=11 price=104.5 support=95.75 resistance=109.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=58.09 liquidity=1280232.5 spike=0.72
- CERA.CA: score=25.9 buy_ready=True sector_rank=11 price=1.24 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=38.89 liquidity=12369968.0 spike=0.65
- CFGH.CA: score=4.9 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.1 source=Yahoo Finance as_of=2026-07-06T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=2151.8 spike=0.4
- CICH.CA: score=16.47 buy_ready=False sector_rank=15 price=11.98 support=11.1 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=1565087.5 spike=0.47
- CIEB.CA: score=22.12 buy_ready=True sector_rank=17 price=24.07 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=62.71 liquidity=2713252.75 spike=0.4
- CIRA.CA: score=25.9 buy_ready=False sector_rank=13 price=28.43 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=72.06 liquidity=13325768.0 spike=0.71
- CLHO.CA: score=26.28 buy_ready=True sector_rank=10 price=16.32 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=61.79 liquidity=43011708.0 spike=1.19
- CNFN.CA: score=27.9 buy_ready=True sector_rank=15 price=4.82 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=63.64 liquidity=18616788.0 spike=0.42
- COMI.CA: score=29.4 buy_ready=True sector_rank=17 price=134.52 support=126.21 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=57.68 liquidity=243258800.0 spike=0.53
- COPR.CA: score=18.05 buy_ready=False sector_rank=11 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=5149624.5 spike=0.21
- COSG.CA: score=27.9 buy_ready=True sector_rank=11 price=1.59 support=1.47 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=19935408.0 spike=0.35
- CPCI.CA: score=13.83 buy_ready=False sector_rank=11 price=397.91 support=354.0 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=76.2 liquidity=926895.38 spike=0.31
- CSAG.CA: score=23.88 buy_ready=False sector_rank=6 price=32.25 support=30.08 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=72.99 liquidity=7978904.5 spike=0.45
- DAPH.CA: score=17.32 buy_ready=False sector_rank=11 price=81.53 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=57.74 liquidity=2418010.5 spike=0.26
- DEIN.CA: score=0.9 buy_ready=False sector_rank=11 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=1.0
- DOMT.CA: score=16.62 buy_ready=False sector_rank=9 price=26.84 support=23.7 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=78.25 liquidity=3720653.25 spike=0.75
- DSCW.CA: score=18.9 buy_ready=False sector_rank=11 price=1.79 support=1.71 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=34.78 liquidity=19714412.0 spike=0.62
- DTPP.CA: score=25.58 buy_ready=False sector_rank=11 price=203.07 support=114.0 resistance=234.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=87.66 liquidity=62642472.0 spike=2.34
- EALR.CA: score=29.96 buy_ready=True sector_rank=11 price=369.85 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=68.21 liquidity=18521188.0 spike=2.03
- EASB.CA: score=18.74 buy_ready=False sector_rank=11 price=7.01 support=4.87 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=47.52 liquidity=4836922.5 spike=0.31
- EAST.CA: score=19.9 buy_ready=False sector_rank=9 price=37.04 support=36.63 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=35.75 liquidity=13604590.0 spike=0.3
- EBSC.CA: score=23.59 buy_ready=True sector_rank=11 price=1.95 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=58.82 liquidity=5585254.5 spike=1.05
- ECAP.CA: score=20.9 buy_ready=True sector_rank=11 price=32.85 support=30.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=51.21 liquidity=4996140.5 spike=0.51
- EDFM.CA: score=16.39 buy_ready=False sector_rank=11 price=333.23 support=310.2 resistance=355.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=50.85 liquidity=494240.09 spike=0.89
- EEII.CA: score=24.9 buy_ready=False sector_rank=11 price=2.75 support=2.3 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=77.22 liquidity=15284286.0 spike=0.71
- EFIC.CA: score=5.5 buy_ready=False sector_rank=19 price=182.59 support=180.02 resistance=208.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=16.76 liquidity=1840995.75 spike=0.73
- EFID.CA: score=24.9 buy_ready=False sector_rank=9 price=28.3 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=53.54 liquidity=23700482.0 spike=0.31
- EFIH.CA: score=24.9 buy_ready=False sector_rank=2 price=22.5 support=20.0 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=75.71 liquidity=39284756.0 spike=0.95
- EGAL.CA: score=21.66 buy_ready=False sector_rank=19 price=291.24 support=272.28 resistance=323.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=49.99 liquidity=35387896.0 spike=0.71
- EGAS.CA: score=23.3 buy_ready=False sector_rank=14 price=49.94 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=43.39 liquidity=9097148.0 spike=1.15
- EGBE.CA: score=17.41 buy_ready=False sector_rank=17 price=0.45 support=0.43 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=8952.23 spike=0.12
- EGCH.CA: score=14.66 buy_ready=False sector_rank=19 price=12.8 support=12.13 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=30.47 liquidity=33451810.0 spike=0.81
- EGSA.CA: score=13.45 buy_ready=False sector_rank=4 price=8.87 support=8.55 resistance=8.93 source=Yahoo Finance as_of=2026-07-06T21:00:00+00:00 freshness=FRESH RSI=80.0 liquidity=7770.12 spike=1.27
- EGTS.CA: score=28.9 buy_ready=True sector_rank=3 price=18.73 support=15.1 resistance=20.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=60.05 liquidity=38373988.0 spike=0.57
- EHDR.CA: score=23.9 buy_ready=False sector_rank=11 price=2.59 support=2.37 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=45.9 liquidity=26243156.0 spike=0.49
- EKHO.CA: score=12.9 buy_ready=False sector_rank=14 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-06T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=16.33 buy_ready=False sector_rank=16 price=2.09 support=2.04 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=42.11 liquidity=6615042.5 spike=0.37
- ELKA.CA: score=26.9 buy_ready=True sector_rank=11 price=1.41 support=1.19 resistance=1.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=63.83 liquidity=21994430.0 spike=0.48
- ELNA.CA: score=12.32 buy_ready=False sector_rank=11 price=38.22 support=35.55 resistance=41.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=45.61 liquidity=421326.72 spike=0.89
- ELSH.CA: score=25.9 buy_ready=True sector_rank=11 price=13.27 support=11.1 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=51.0 liquidity=75305064.0 spike=0.4
- ELWA.CA: score=6.51 buy_ready=False sector_rank=11 price=1.92 support=1.89 resistance=2.22 source=Yahoo Finance as_of=2026-07-06T21:00:00+00:00 freshness=FRESH RSI=34.29 liquidity=612756.47 spike=0.39
- EMFD.CA: score=24.9 buy_ready=False sector_rank=3 price=11.54 support=11.11 resistance=12.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=38.73 liquidity=68118816.0 spike=0.28
- ENGC.CA: score=29.22 buy_ready=True sector_rank=11 price=38.83 support=33.0 resistance=38.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=66.0 liquidity=23554660.0 spike=1.66
- EOSB.CA: score=17.94 buy_ready=False sector_rank=11 price=1.48 support=1.42 resistance=1.55 source=Yahoo Finance as_of=2026-07-06T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=36612.24 spike=0.34
- EPCO.CA: score=14.35 buy_ready=False sector_rank=11 price=8.92 support=8.5 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=3451716.0 spike=0.46
- EPPK.CA: score=14.18 buy_ready=False sector_rank=11 price=14.34 support=11.72 resistance=15.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=90.24 liquidity=1178633.25 spike=1.05
- ETEL.CA: score=27.9 buy_ready=True sector_rank=4 price=96.37 support=89.01 resistance=101.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=66.95 liquidity=42939676.0 spike=0.56
- ETRS.CA: score=25.9 buy_ready=True sector_rank=11 price=10.63 support=8.77 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=58.61 liquidity=26508752.0 spike=0.33
- EXPA.CA: score=22.4 buy_ready=False sector_rank=17 price=18.39 support=18.03 resistance=19.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=45.24 liquidity=10331273.0 spike=0.34
- FAIT.CA: score=14.31 buy_ready=False sector_rank=17 price=36.2 support=35.01 resistance=37.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=39.17 liquidity=910227.19 spike=0.39
- FAITA.CA: score=10.43 buy_ready=False sector_rank=17 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=38.46 liquidity=23052.4 spike=0.57
- FERC.CA: score=17.72 buy_ready=False sector_rank=19 price=76.01 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=41.41 liquidity=4534738.0 spike=1.26
- FWRY.CA: score=28.9 buy_ready=False sector_rank=2 price=18.97 support=17.71 resistance=19.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=63.41 liquidity=56434940.0 spike=0.24
- GBCO.CA: score=25.9 buy_ready=False sector_rank=8 price=30.86 support=26.62 resistance=32.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=72.53 liquidity=13234120.0 spike=0.14
- GDWA.CA: score=9.21 buy_ready=False sector_rank=11 price=0.77 support=0.76 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=31.4 liquidity=4308962.0 spike=0.29
- GGCC.CA: score=18.25 buy_ready=False sector_rank=11 price=0.51 support=0.4 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=90.0 liquidity=6351499.5 spike=0.37
- GIHD.CA: score=21.16 buy_ready=True sector_rank=11 price=43.45 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=61.42 liquidity=3264759.0 spike=0.35
- GMCI.CA: score=18.27 buy_ready=False sector_rank=11 price=2.18 support=1.66 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=82.22 liquidity=1533147.0 spike=1.92
- GRCA.CA: score=8.38 buy_ready=False sector_rank=11 price=50.15 support=50.14 resistance=58.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=16.28 liquidity=2483170.75 spike=0.6
- GSSC.CA: score=20.26 buy_ready=False sector_rank=11 price=253.41 support=240.0 resistance=263.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=63.43 liquidity=3360305.75 spike=0.93
- GTWL.CA: score=29.1 buy_ready=False sector_rank=11 price=99.47 support=46.0 resistance=102.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=89.98 liquidity=193510864.0 spike=3.1
- HDBK.CA: score=19.4 buy_ready=False sector_rank=17 price=81.28 support=82.52 resistance=82.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=30051220.0 spike=1.0
- HELI.CA: score=29.94 buy_ready=True sector_rank=3 price=6.76 support=6.28 resistance=6.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=63.48 liquidity=166815696.0 spike=1.52
- HRHO.CA: score=21.9 buy_ready=False sector_rank=15 price=26.79 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=43.44 liquidity=37613712.0 spike=0.28
- ICID.CA: score=17.16 buy_ready=True sector_rank=11 price=7.6 support=6.12 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=59.26 liquidity=1263057.63 spike=0.11
- IDRE.CA: score=16.67 buy_ready=False sector_rank=11 price=42.74 support=41.1 resistance=46.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=47.53 liquidity=5769427.5 spike=0.52
- IFAP.CA: score=14.89 buy_ready=False sector_rank=18 price=19.28 support=18.47 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=54.27 liquidity=3793073.5 spike=0.74
- INFI.CA: score=15.58 buy_ready=False sector_rank=11 price=94.08 support=88.51 resistance=103.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=43.08 liquidity=3681957.5 spike=0.59
- IRON.CA: score=13.74 buy_ready=False sector_rank=19 price=32.0 support=30.51 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=44.4 liquidity=3076336.25 spike=0.39
- ISMA.CA: score=18.62 buy_ready=False sector_rank=11 price=27.09 support=26.9 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=3.51 liquidity=9719859.0 spike=0.29
- ISMQ.CA: score=21.66 buy_ready=False sector_rank=19 price=9.88 support=7.67 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=76.67 liquidity=120251032.0 spike=0.88
- ISPH.CA: score=20.9 buy_ready=False sector_rank=10 price=11.39 support=11.2 resistance=12.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=42.19 liquidity=44191072.0 spike=0.5
- JUFO.CA: score=27.9 buy_ready=True sector_rank=9 price=30.78 support=28.5 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=58.14 liquidity=16009977.0 spike=0.52
- KABO.CA: score=26.04 buy_ready=False sector_rank=7 price=7.46 support=5.96 resistance=7.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=87.33 liquidity=39830328.0 spike=1.57
- KWIN.CA: score=11.54 buy_ready=False sector_rank=11 price=67.35 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=31.77 liquidity=6641013.5 spike=0.52
- KZPC.CA: score=12.68 buy_ready=False sector_rank=11 price=8.51 support=8.26 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=36.13 liquidity=2777584.25 spike=0.42
- LCSW.CA: score=30.28 buy_ready=True sector_rank=12 price=31.0 support=26.0 resistance=31.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=65.12 liquidity=103995776.0 spike=2.19
- LUTS.CA: score=25.9 buy_ready=True sector_rank=11 price=0.74 support=0.62 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=29197792.0 spike=0.53
- MAAL.CA: score=22.73 buy_ready=False sector_rank=11 price=7.73 support=5.52 resistance=7.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=99.4 liquidity=7833405.0 spike=0.49
- MASR.CA: score=29.9 buy_ready=True sector_rank=11 price=7.6 support=6.54 resistance=7.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=63.54 liquidity=65346692.0 spike=0.87
- MBSC.CA: score=22.9 buy_ready=False sector_rank=12 price=243.03 support=222.66 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=43.85 liquidity=10072510.0 spike=0.38
- MCQE.CA: score=24.9 buy_ready=False sector_rank=12 price=178.55 support=166.66 resistance=192.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=59.25 liquidity=10087630.0 spike=0.72
- MCRO.CA: score=21.9 buy_ready=False sector_rank=11 price=1.23 support=1.17 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=16257927.0 spike=0.53
- MENA.CA: score=28.14 buy_ready=True sector_rank=3 price=7.02 support=6.41 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=60.43 liquidity=9137202.0 spike=1.05
- MEPA.CA: score=20.86 buy_ready=False sector_rank=11 price=1.63 support=1.52 resistance=1.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=45.16 liquidity=7964978.5 spike=0.66
- MFPC.CA: score=21.84 buy_ready=False sector_rank=19 price=36.62 support=34.22 resistance=42.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=38.72 liquidity=93919216.0 spike=1.09
- MFSC.CA: score=18.2 buy_ready=True sector_rank=11 price=47.74 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=62.69 liquidity=2299691.25 spike=0.3
- MHOT.CA: score=18.1 buy_ready=False sector_rank=21 price=17.13 support=17.55 resistance=17.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=10017092.0 spike=1.0
- MICH.CA: score=27.84 buy_ready=True sector_rank=11 price=38.05 support=34.0 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=51.37 liquidity=28770910.0 spike=1.97
- MILS.CA: score=13.03 buy_ready=False sector_rank=11 price=130.76 support=126.31 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=32.05 liquidity=7131036.5 spike=0.78
- MIPH.CA: score=32.35 buy_ready=True sector_rank=10 price=699.82 support=630.13 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=55.65 liquidity=9449643.0 spike=4.98
- MOED.CA: score=19.95 buy_ready=False sector_rank=11 price=0.69 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=48.0 liquidity=8052155.5 spike=0.89
- MOIL.CA: score=15.99 buy_ready=False sector_rank=14 price=0.52 support=0.46 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=76.67 liquidity=373865.38 spike=1.36
- MOIN.CA: score=12.4 buy_ready=False sector_rank=11 price=23.9 support=22.6 resistance=25.3 source=Yahoo Finance as_of=2026-07-06T21:00:00+00:00 freshness=FRESH RSI=43.49 liquidity=501493.69 spike=0.77
- MOSC.CA: score=12.22 buy_ready=False sector_rank=11 price=271.92 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=43.77 liquidity=1323072.13 spike=0.14
- MPCI.CA: score=25.9 buy_ready=True sector_rank=11 price=241.09 support=213.0 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=61.37 liquidity=38107496.0 spike=0.37
- MPCO.CA: score=18.1 buy_ready=False sector_rank=18 price=1.8 support=1.66 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=30.3 liquidity=21755168.0 spike=0.2
- MPRC.CA: score=24.9 buy_ready=False sector_rank=11 price=40.99 support=31.15 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=92.18 liquidity=37702000.0 spike=0.83
- MTIE.CA: score=25.44 buy_ready=False sector_rank=8 price=9.11 support=8.65 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=53.85 liquidity=9542159.0 spike=0.48
- NAHO.CA: score=13.91 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=11396.41 spike=0.36
- NCCW.CA: score=23.05 buy_ready=False sector_rank=11 price=6.11 support=5.82 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=49.59 liquidity=9147622.0 spike=0.26
- NEDA.CA: score=16.49 buy_ready=False sector_rank=11 price=2.82 support=2.7 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=46.15 liquidity=405636.59 spike=1.09
- NHPS.CA: score=27.9 buy_ready=True sector_rank=11 price=70.84 support=61.55 resistance=75.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=67.11 liquidity=11165820.0 spike=0.79
- NINH.CA: score=21.26 buy_ready=False sector_rank=11 price=17.84 support=16.8 resistance=18.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=53.04 liquidity=6363351.0 spike=0.98
- NIPH.CA: score=25.98 buy_ready=True sector_rank=10 price=177.49 support=157.01 resistance=185.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=65.34 liquidity=96158792.0 spike=1.04
- OBRI.CA: score=25.14 buy_ready=False sector_rank=11 price=35.72 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=49.47 liquidity=29348392.0 spike=1.12
- OCDI.CA: score=26.1 buy_ready=False sector_rank=3 price=26.66 support=20.0 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=87.6 liquidity=99669600.0 spike=1.1
- OCPH.CA: score=25.87 buy_ready=False sector_rank=11 price=354.19 support=337.0 resistance=374.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=60.85 liquidity=9827158.0 spike=1.57
- ODIN.CA: score=27.9 buy_ready=True sector_rank=11 price=2.32 support=2.01 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=69.57 liquidity=12874543.0 spike=0.92
- OFH.CA: score=24.9 buy_ready=True sector_rank=11 price=0.62 support=0.57 resistance=0.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=58.14 liquidity=15472997.0 spike=0.74
- OIH.CA: score=22.08 buy_ready=False sector_rank=5 price=1.41 support=1.33 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=77.78 liquidity=90253136.0 spike=1.09
- OLFI.CA: score=29.02 buy_ready=True sector_rank=9 price=22.84 support=21.0 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=67.91 liquidity=41440312.0 spike=1.56
- ORAS.CA: score=9.1 buy_ready=False sector_rank=20 price=682.94 support=680.0 resistance=706.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=196972160.0 spike=1.0
- ORHD.CA: score=26.9 buy_ready=True sector_rank=3 price=38.77 support=35.01 resistance=39.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=65.28 liquidity=71300008.0 spike=0.42
- ORWE.CA: score=23.9 buy_ready=False sector_rank=7 price=22.7 support=21.95 resistance=23.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=48.48 liquidity=13088661.0 spike=0.6
- PHAR.CA: score=22.94 buy_ready=True sector_rank=10 price=87.0 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=60.19 liquidity=5043991.5 spike=0.2
- PHDC.CA: score=19.9 buy_ready=False sector_rank=3 price=14.6 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=23.39 liquidity=79146936.0 spike=0.24
- PHTV.CA: score=17.82 buy_ready=False sector_rank=11 price=268.07 support=201.55 resistance=277.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=85.91 liquidity=4917693.0 spike=0.41
- POUL.CA: score=27.9 buy_ready=False sector_rank=9 price=39.48 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=72.22 liquidity=14716139.0 spike=0.39
- PRCL.CA: score=24.9 buy_ready=False sector_rank=12 price=35.99 support=23.75 resistance=35.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=84.04 liquidity=49073292.0 spike=0.99
- PRDC.CA: score=30.9 buy_ready=True sector_rank=3 price=8.4 support=5.91 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=61.97 liquidity=60709856.0 spike=0.44
- PRMH.CA: score=14.85 buy_ready=False sector_rank=11 price=2.55 support=2.34 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=31.82 liquidity=5951182.0 spike=0.2
- RACC.CA: score=29.28 buy_ready=False sector_rank=11 price=9.96 support=9.36 resistance=10.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=71.32 liquidity=16513868.0 spike=1.69
- RAKT.CA: score=13.98 buy_ready=False sector_rank=11 price=22.75 support=21.4 resistance=23.98 source=Yahoo Finance as_of=2026-07-06T21:00:00+00:00 freshness=FRESH RSI=46.2 liquidity=78737.75 spike=0.3
- RAYA.CA: score=28.9 buy_ready=True sector_rank=1 price=7.84 support=6.7 resistance=8.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=69.12 liquidity=90762808.0 spike=0.87
- RMDA.CA: score=23.9 buy_ready=False sector_rank=10 price=4.97 support=4.81 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=13362416.0 spike=0.17
- ROTO.CA: score=21.55 buy_ready=False sector_rank=11 price=41.52 support=33.06 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=71.36 liquidity=5653111.5 spike=0.18
- RREI.CA: score=34.9 buy_ready=True sector_rank=11 price=3.78 support=3.34 resistance=3.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=57.81 liquidity=68347744.0 spike=4.61
- RTVC.CA: score=14.61 buy_ready=False sector_rank=11 price=3.74 support=3.55 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=2705724.75 spike=0.54
- RUBX.CA: score=23.18 buy_ready=False sector_rank=11 price=13.07 support=9.8 resistance=14.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=81.21 liquidity=55372648.0 spike=1.14
- SAUD.CA: score=16.43 buy_ready=False sector_rank=17 price=21.28 support=19.99 resistance=22.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=46.63 liquidity=4024514.0 spike=0.55
- SCEM.CA: score=21.19 buy_ready=False sector_rank=12 price=62.84 support=59.3 resistance=67.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=57.79 liquidity=6289980.0 spike=0.34
- SCFM.CA: score=15.57 buy_ready=False sector_rank=11 price=243.87 support=226.5 resistance=265.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=46.36 liquidity=2666846.25 spike=0.64
- SCTS.CA: score=17.55 buy_ready=False sector_rank=13 price=610.37 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=61.71 liquidity=2652588.0 spike=0.52
- SDTI.CA: score=15.42 buy_ready=False sector_rank=11 price=46.62 support=45.55 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=51.65 liquidity=1517307.25 spike=0.16
- SEIG.CA: score=15.9 buy_ready=False sector_rank=11 price=244.0 support=228.51 resistance=259.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=89949536.0 spike=19.38
- SIPC.CA: score=18.15 buy_ready=False sector_rank=11 price=3.45 support=3.25 resistance=3.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=54.41 liquidity=5245882.0 spike=0.5
- SKPC.CA: score=22.98 buy_ready=False sector_rank=19 price=16.42 support=15.58 resistance=17.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=43.39 liquidity=37249504.0 spike=1.16
- SMFR.CA: score=27.49 buy_ready=True sector_rank=11 price=205.26 support=187.01 resistance=209.99 source=Yahoo Finance as_of=2026-07-06T21:00:00+00:00 freshness=FRESH RSI=52.4 liquidity=5406548.26 spike=3.09
- SNFC.CA: score=11.71 buy_ready=False sector_rank=11 price=11.41 support=11.26 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=26.37 liquidity=5814479.0 spike=0.46
- SPIN.CA: score=19.22 buy_ready=True sector_rank=7 price=14.59 support=13.3 resistance=14.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=69.34 liquidity=3323765.75 spike=0.38
- SPMD.CA: score=28.38 buy_ready=True sector_rank=11 price=0.44 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=57.02 liquidity=40315312.0 spike=2.24
- SUGR.CA: score=8.08 buy_ready=False sector_rank=9 price=46.58 support=45.31 resistance=50.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=31.53 liquidity=3181115.0 spike=0.58
- SVCE.CA: score=27.9 buy_ready=True sector_rank=11 price=9.2 support=8.11 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=57.48 liquidity=19731460.0 spike=0.27
- SWDY.CA: score=27.72 buy_ready=True sector_rank=16 price=87.52 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=67.21 liquidity=10606493.0 spike=0.79
- TALM.CA: score=15.9 buy_ready=False sector_rank=13 price=15.47 support=15.38 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=28.35 liquidity=10752523.0 spike=0.92
- TMGH.CA: score=30.9 buy_ready=True sector_rank=3 price=96.45 support=92.1 resistance=99.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=59.88 liquidity=251456832.0 spike=0.7
- TRTO.CA: score=13.96 buy_ready=False sector_rank=11 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-07-06T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=1232.06 spike=2.03
- UEFM.CA: score=15.7 buy_ready=False sector_rank=11 price=480.32 support=460.0 resistance=505.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=59.39 liquidity=799913.69 spike=0.74
- UEGC.CA: score=27.9 buy_ready=False sector_rank=11 price=1.59 support=1.33 resistance=1.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=71.74 liquidity=10167412.0 spike=0.35
- UNIP.CA: score=17.29 buy_ready=False sector_rank=11 price=0.32 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=45.21 liquidity=3391813.75 spike=0.14
- UNIT.CA: score=27.02 buy_ready=False sector_rank=3 price=16.94 support=12.0 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=80.22 liquidity=15643454.0 spike=1.56
- WCDF.CA: score=6.18 buy_ready=False sector_rank=11 price=506.06 support=450.0 resistance=544.99 source=Yahoo Finance as_of=2026-07-06T21:00:00+00:00 freshness=FRESH RSI=8.18 liquidity=281369.36 spike=0.93
- WKOL.CA: score=20.92 buy_ready=False sector_rank=11 price=313.75 support=273.1 resistance=334.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=75.27 liquidity=6020346.5 spike=0.95
- ZEOT.CA: score=25.9 buy_ready=True sector_rank=11 price=10.99 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=49.08 liquidity=11659971.0 spike=0.3
- ZMID.CA: score=28.9 buy_ready=False sector_rank=3 price=6.69 support=6.03 resistance=6.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=72.37 liquidity=79460968.0 spike=0.38

## Backtesting Lite
- RREI.CA: 180d return=55.6%, max drawdown=-27.36%, MA20>MA50 days last20=4, as_of=2026-07-06T21:00:00+00:00
- BIOC.CA: 180d return=2.34%, max drawdown=-19.91%, MA20>MA50 days last20=17, as_of=2026-07-06T21:00:00+00:00
- MIPH.CA: 180d return=113.77%, max drawdown=-11.96%, MA20>MA50 days last20=19, as_of=2026-07-06T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- RREI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Arab Real Estate Investment Co. summary=Evidence rejected for RREI.CA: source text did not clearly match RREI.CA / Arab Real Estate Investment Co..
- BIOC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GlaxoSmithKline S.A.E summary=Evidence rejected for BIOC.CA: source text did not clearly match BIOC.CA / GlaxoSmithKline S.A.E.
- MIPH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Minapharm Pharmaceuticals summary=Minapharm’ consolidated net profits retreat to EGP 62m in 9M-25; Minapharm posts EGP 66.5m standalone net profits in 9M-25; sales hit EGP 2.8bn; Investor buys EGP 1.3bn stake in Minapharm Pharmaceuticals
  - Minapharm’ consolidated net profits retreat to EGP 62m in 9M-25: https://english.mubasher.info/news/4531893/Minapharm-consolidated-net-profits-retreat-to-EGP-62m-in-9M-25/
  - Minapharm posts EGP 66.5m standalone net profits in 9M-25; sales hit EGP 2.8bn: https://english.mubasher.info/news/4528557/Minapharm-posts-EGP-66-5m-standalone-net-profits-in-9M-25-sales-hit-EGP-2-8bn/
  - Investor buys EGP 1.3bn stake in Minapharm Pharmaceuticals: https://english.mubasher.info/news/4295954/Investor-buys-EGP-1-3bn-stake-in-Minapharm-Pharmaceuticals/
- PRDC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Pioneers Properties For Urban Development summary=Evidence rejected for PRDC.CA: source text did not clearly match PRDC.CA / Pioneers Properties For Urban Development.
- TMGH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talaat Moustafa Group Holding summary=Evidence rejected for TMGH.CA: source text did not clearly match TMGH.CA / Talaat Moustafa Group Holding.
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- AMER.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=553 sources=3 expected=Amer Group Holding summary=Amer Group stock holds above EGP 1.95 as bulls target higher levels; Amer Group’s consolidated profits hit EGP 196m in 2025; Amer Group stock’s technical outlook on profit-taking, holding above main support – Analysis
  - Amer Group stock holds above EGP 1.95 as bulls target higher levels: https://english.mubasher.info/news/4583812/Amer-Group-stock-holds-above-EGP-1-95-as-bulls-target-higher-levels/
  - Amer Group’s consolidated profits hit EGP 196m in 2025: https://english.mubasher.info/news/4563160/Amer-Group-s-consolidated-profits-hit-EGP-196m-in-2025/
  - Amer Group stock’s technical outlook on profit-taking, holding above main support – Analysis: https://english.mubasher.info/news/4546813/Amer-Group-stock-s-technical-outlook-on-profit-taking-holding-above-main-support-Analysis/
- EALR.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Company For Land Reclamation summary=El Arabia for Land Reclamation targets EGP 2.5m profits in FY22/23; El Arabia for Land Reclamation starts work on Bahariya Oasis project; El Arabia for Land Reclamation H1 losses down 16%
  - El Arabia for Land Reclamation targets EGP 2.5m profits in FY22/23: https://english.mubasher.info/news/3938373/El-Arabia-for-Land-Reclamation-targets-EGP-2-5m-profits-in-FY22-23/
  - El Arabia for Land Reclamation starts work on Bahariya Oasis project: https://english.mubasher.info/news/3493569/El-Arabia-for-Land-Reclamation-starts-work-on-Bahariya-Oasis-project/
  - El Arabia for Land Reclamation H1 losses down 16%: https://english.mubasher.info/news/3058199/El-Arabia-for-Land-Reclamation-H1-losses-down-16-/

## Warnings
- Evidence rejected for RREI.CA: source text did not clearly match RREI.CA / Arab Real Estate Investment Co..
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence rejected for BIOC.CA: source text did not clearly match BIOC.CA / GlaxoSmithKline S.A.E.
- Evidence for MIPH.CA matches the company but no source/report date was detected.
- Evidence rejected for PRDC.CA: source text did not clearly match PRDC.CA / Pioneers Properties For Urban Development.
- Evidence rejected for TMGH.CA: source text did not clearly match TMGH.CA / Talaat Moustafa Group Holding.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence for AMER.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for EALR.CA matches the company but no source/report date was detected.
