# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-07-09T09:02:43.690585+00:00
Generated Cairo: 2026-07-09 12:02
Run timing: target 08:45 Cairo | generated Cairo 2026-07-09 12:02 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-07-09 11:58

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 63
- Data quality issues: 0
- Tradeable price/liquidity tickers: 181/190
- Top sector: Fintech & Payments

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, July 09
- Freshness: DELAYED
- EGX30 regime: CONSTRUCTIVE / above MA20 65.0% / above MA50 50.0%
- EGX70 regime: BULLISH / above MA20 79.49% / above MA50 74.36%
- Sector breadth: 57.14%
- Risk mode: BROAD_RISK_ON

## Top Liquidity
- HELI.CA: liquidity=276693024.0 spike=2.28 score=30.46
- CCAP.CA: liquidity=188245488.0 spike=0.27 score=27.9
- AMES.CA: liquidity=142686464.0 spike=5.55 score=15.44
- COMI.CA: liquidity=114737528.0 spike=0.25 score=27.05
- ZMID.CA: liquidity=108946472.0 spike=0.52 score=27.9

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b-20230311:free
- Summary: Scanner prioritized tickets with high rank scores, liquidity accumulation spikes, and BULLISH_WATCH outlook while EGX30 is constructive and EGX70 bullish, pushing risk mode to BROAD_RISK_ON but confidence remains low due to mixed evidence and extended momentum.
- Selection driven by top rank_score, ACCUMULATION_SPIKE liquidity regime, and BULLISH_WATCH outlook, favoring stocks in leading sectors like Fintech & Payments and Technology & Distribution.
- Liquidity spikes and support/resistance distances suggest near‑term upside potential (e.g., AFMC.CA close to resistance, EFIH.CA cooling liquidity), yet sector breadth at 57% shows only moderate market participation.
- EGX30 constructive and EGX70 bullish regimes shift risk mode to BROAD_RISK_ON, allowing more buy‑ready signals but introducing uncertainty as momentum appears extended and RSI approaches overbought levels.
- Many tickets lack clear fundamental evidence (source counts zero) and the primary tickets remain HOLD with LOW confidence, underscoring the need for caution despite the bullish watch outlook.

## Top Liquidity Spikes
- UEFM.CA: spike=6.28 liquidity=6931039.5 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AFMC.CA: spike=6.25 liquidity=15860709.0 outlook=BULLISH_WATCH score=74.86 buy_ready=True
- NEDA.CA: spike=5.71 liquidity=1905448.07 outlook=WEAK_OR_RISKY score=20.86 buy_ready=False
- AMES.CA: spike=5.55 liquidity=142686464.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SCFM.CA: spike=5.45 liquidity=21984296.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Fintech & Payments: score=8.76 5d=7.64% 20d=4.37% aboveMA50=50.0%
- #2 Technology & Distribution: score=8.33 5d=1.56% 20d=4.56% aboveMA50=100.0%
- #3 Telecommunications: score=8.28 5d=3.06% 20d=2.85% aboveMA50=100.0%
- #4 Real Estate: score=7.16 5d=3.49% 20d=2.08% aboveMA50=92.31%
- #5 Transportation & Logistics: score=6.8 5d=-0.59% 20d=1.07% aboveMA50=100.0%
- #6 Investment Holding: score=6.66 5d=3.23% 20d=0.71% aboveMA50=66.67%
- #7 Textiles: score=6.62 5d=2.95% 20d=0.0% aboveMA50=100.0%
- #8 Automotive & Distribution: score=6.3 5d=-2.15% 20d=4.7% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ETEL.CA: BULLISH_WATCH score=94.28 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- HELI.CA: BULLISH_WATCH score=88.16 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- EFIH.CA: BULLISH_WATCH score=86.76 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- MENA.CA: BULLISH_WATCH score=83.16 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- BIOC.CA: BULLISH_WATCH score=82.86 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- ACGC.CA: BULLISH_WATCH score=82.62 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ALCN.CA: BULLISH_WATCH score=81.8 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- CERA.CA: BULLISH_WATCH score=80.86 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- EALR.CA: BULLISH_WATCH score=80.86 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- EDFM.CA: BULLISH_WATCH score=80.86 liquidity=TRADEABLE sector=IMPROVING risk=close to resistance; sector is not leading

## BUY-Ready Candidates
- AFMC.CA: rank=32.44 outlook=BULLISH_WATCH outlook_score=74.86 sector_rank=11 price=73.93 support=66.0 resistance=74.79 liquidity=15860709.0
- EFIH.CA: rank=30.9 outlook=BULLISH_WATCH outlook_score=86.76 sector_rank=1 price=22.26 support=20.0 resistance=23.65 liquidity=15614052.0
- HELI.CA: rank=30.46 outlook=BULLISH_WATCH outlook_score=88.16 sector_rank=4 price=7.09 support=6.28 resistance=6.91 liquidity=276693024.0
- NHPS.CA: rank=30.44 outlook=BULLISH_WATCH outlook_score=78.86 sector_rank=11 price=71.29 support=61.55 resistance=75.49 liquidity=61332232.0
- RAYA.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=80.33 sector_rank=2 price=7.8 support=6.7 resistance=8.28 liquidity=55649828.0
- CERA.CA: rank=28.66 outlook=BULLISH_WATCH outlook_score=80.86 sector_rank=11 price=1.31 support=1.15 resistance=1.3 liquidity=31302242.0
- ARAB.CA: rank=28.24 outlook=BULLISH_WATCH outlook_score=76.16 sector_rank=4 price=0.23 support=0.2 resistance=0.24 liquidity=86938256.0
- TMGH.CA: rank=27.9 outlook=BULLISH_WATCH outlook_score=77.16 sector_rank=4 price=97.45 support=92.1 resistance=99.43 liquidity=27238468.0
- ALCN.CA: rank=27.9 outlook=BULLISH_WATCH outlook_score=81.8 sector_rank=5 price=29.24 support=25.51 resistance=33.2 liquidity=10747473.0
- ZMID.CA: rank=27.9 outlook=CONSTRUCTIVE outlook_score=57.16 sector_rank=4 price=6.87 support=6.03 resistance=6.96 liquidity=108946472.0

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=27.08 buy_ready=True sector_rank=11 price=223.79 support=196.0 resistance=247.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=62.25 liquidity=9635356.0 spike=0.72
- ABUK.CA: score=21.72 buy_ready=False sector_rank=19 price=70.68 support=66.66 resistance=81.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=50.59 liquidity=61399368.0 spike=0.45
- ACAMD.CA: score=25.44 buy_ready=False sector_rank=11 price=2.29 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=39045384.0 spike=0.38
- ACGC.CA: score=17.82 buy_ready=True sector_rank=7 price=9.49 support=8.92 resistance=10.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=51.27 liquidity=1922061.0 spike=0.08
- ADCI.CA: score=15.55 buy_ready=False sector_rank=11 price=230.8 support=219.0 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=56.4 liquidity=2107046.5 spike=0.18
- ADIB.CA: score=27.05 buy_ready=True sector_rank=14 price=46.84 support=44.01 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=43.33 liquidity=33577188.0 spike=0.38
- ADPC.CA: score=13.07 buy_ready=False sector_rank=11 price=3.54 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=45.79 liquidity=2624190.5 spike=0.2
- AFDI.CA: score=19.98 buy_ready=True sector_rank=11 price=45.25 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=58.78 liquidity=2531341.25 spike=0.21
- AFMC.CA: score=32.44 buy_ready=True sector_rank=11 price=73.93 support=66.0 resistance=74.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=49.04 liquidity=15860709.0 spike=6.25
- AJWA.CA: score=13.01 buy_ready=False sector_rank=11 price=176.91 support=144.0 resistance=190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=34.21 liquidity=2569547.5 spike=0.1
- ALCN.CA: score=27.9 buy_ready=True sector_rank=5 price=29.24 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=50.15 liquidity=10747473.0 spike=0.97
- ALUM.CA: score=19.6 buy_ready=False sector_rank=11 price=22.9 support=20.55 resistance=25.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=49.4 liquidity=5160371.0 spike=0.64
- AMER.CA: score=25.9 buy_ready=True sector_rank=4 price=2.87 support=2.28 resistance=2.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=67.05 liquidity=65452480.0 spike=0.97
- AMES.CA: score=15.44 buy_ready=False sector_rank=11 price=80.27 support=70.78 resistance=84.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=142686464.0 spike=5.55
- AMIA.CA: score=16.23 buy_ready=False sector_rank=11 price=9.0 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=45.05 liquidity=784456.38 spike=0.08
- AMOC.CA: score=24.3 buy_ready=False sector_rank=12 price=8.0 support=7.42 resistance=8.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=59.59 liquidity=53228044.0 spike=1.02
- ANFI.CA: score=11.78 buy_ready=False sector_rank=11 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=STALE RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=11.7 buy_ready=False sector_rank=11 price=8.49 support=8.0 resistance=8.98 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=48.41 liquidity=258860.09 spike=0.32
- ARAB.CA: score=28.24 buy_ready=True sector_rank=4 price=0.23 support=0.2 resistance=0.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=58.18 liquidity=86938256.0 spike=1.17
- ARCC.CA: score=12.65 buy_ready=False sector_rank=13 price=55.27 support=53.0 resistance=58.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=44.73 liquidity=2563488.5 spike=0.11
- AREH.CA: score=18.34 buy_ready=False sector_rank=11 price=1.56 support=1.42 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=4891508.5 spike=0.13
- ARVA.CA: score=14.61 buy_ready=False sector_rank=11 price=10.93 support=10.3 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=40.17 liquidity=1170790.75 spike=0.05
- ASCM.CA: score=21.15 buy_ready=False sector_rank=11 price=57.83 support=54.12 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=46.6 liquidity=7705882.0 spike=0.1
- ASPI.CA: score=16.82 buy_ready=False sector_rank=11 price=0.32 support=0.3 resistance=0.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=54.76 liquidity=3376538.5 spike=0.09
- ATLC.CA: score=15.34 buy_ready=False sector_rank=16 price=5.17 support=4.7 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=50.67 liquidity=500422.34 spike=0.07
- ATQA.CA: score=15.89 buy_ready=False sector_rank=19 price=9.53 support=9.02 resistance=10.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=42.75 liquidity=3164737.5 spike=0.1
- AXPH.CA: score=17.0 buy_ready=True sector_rank=11 price=1181.04 support=1073.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=65.94 liquidity=1558885.5 spike=0.51
- BINV.CA: score=16.88 buy_ready=False sector_rank=6 price=48.32 support=44.02 resistance=51.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=53.46 liquidity=983587.44 spike=0.14
- BIOC.CA: score=22.27 buy_ready=True sector_rank=11 price=74.5 support=66.75 resistance=76.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=54.48 liquidity=2823211.75 spike=0.85
- BTFH.CA: score=22.84 buy_ready=False sector_rank=16 price=3.05 support=2.91 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=54.9 liquidity=32891554.0 spike=0.17
- CAED.CA: score=20.4 buy_ready=True sector_rank=11 price=73.48 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=54.04 liquidity=2956868.25 spike=0.59
- CANA.CA: score=13.94 buy_ready=False sector_rank=14 price=36.32 support=34.5 resistance=38.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=39.38 liquidity=1887297.63 spike=0.16
- CCAP.CA: score=27.9 buy_ready=True sector_rank=6 price=5.22 support=4.65 resistance=5.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=54.9 liquidity=188245488.0 spike=0.27
- CCRS.CA: score=10.51 buy_ready=False sector_rank=11 price=2.37 support=2.18 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=32.2 liquidity=2068973.75 spike=0.16
- CEFM.CA: score=26.88 buy_ready=False sector_rank=11 price=105.11 support=95.75 resistance=109.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=45.41 liquidity=7438209.5 spike=4.11
- CERA.CA: score=28.66 buy_ready=True sector_rank=11 price=1.31 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=45.0 liquidity=31302242.0 spike=1.61
- CFGH.CA: score=6.45 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.1 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=1494.6 spike=0.32
- CICH.CA: score=12.88 buy_ready=False sector_rank=16 price=11.79 support=11.1 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=1041531.25 spike=0.3
- CIEB.CA: score=17.79 buy_ready=False sector_rank=14 price=24.11 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=50.86 liquidity=740327.13 spike=0.11
- CIRA.CA: score=18.94 buy_ready=True sector_rank=18 price=28.99 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=68.69 liquidity=6133566.0 spike=0.32
- CLHO.CA: score=17.35 buy_ready=True sector_rank=9 price=16.4 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=59.22 liquidity=1762961.25 spike=0.05
- CNFN.CA: score=19.57 buy_ready=True sector_rank=16 price=4.82 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=63.64 liquidity=2731971.5 spike=0.06
- COMI.CA: score=27.05 buy_ready=True sector_rank=14 price=134.71 support=126.21 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=49.31 liquidity=114737528.0 spike=0.25
- COPR.CA: score=17.43 buy_ready=False sector_rank=11 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=37.29 liquidity=4981880.5 spike=0.21
- COSG.CA: score=27.44 buy_ready=True sector_rank=11 price=1.6 support=1.47 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=45.16 liquidity=10700825.0 spike=0.23
- CPCI.CA: score=14.01 buy_ready=False sector_rank=11 price=397.08 support=354.0 resistance=434.99 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=75.84 liquidity=1562112.67 spike=0.63
- CSAG.CA: score=20.19 buy_ready=True sector_rank=5 price=32.5 support=30.08 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=61.35 liquidity=2287570.75 spike=0.13
- DAPH.CA: score=14.98 buy_ready=False sector_rank=11 price=81.57 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=49.3 liquidity=537887.06 spike=0.06
- DEIN.CA: score=0.44 buy_ready=False sector_rank=11 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=16.27 buy_ready=False sector_rank=10 price=26.84 support=23.7 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=72.53 liquidity=757775.25 spike=0.15
- DSCW.CA: score=13.87 buy_ready=False sector_rank=11 price=1.79 support=1.71 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=34.78 liquidity=5427628.5 spike=0.19
- DTPP.CA: score=24.44 buy_ready=False sector_rank=11 price=203.58 support=114.0 resistance=234.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=88.92 liquidity=11565277.0 spike=0.37
- EALR.CA: score=27.03 buy_ready=True sector_rank=11 price=369.79 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=53.5 liquidity=9586600.0 spike=0.95
- EASB.CA: score=25.44 buy_ready=True sector_rank=11 price=7.15 support=4.87 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=45.15 liquidity=13548729.0 spike=0.86
- EAST.CA: score=12.55 buy_ready=False sector_rank=10 price=37.01 support=36.63 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=31.59 liquidity=8037102.5 spike=0.18
- EBSC.CA: score=19.04 buy_ready=True sector_rank=11 price=1.92 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=51.95 liquidity=1598847.0 spike=0.32
- ECAP.CA: score=14.15 buy_ready=False sector_rank=11 price=32.35 support=30.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=49.25 liquidity=705014.0 spike=0.07
- EDFM.CA: score=19.71 buy_ready=True sector_rank=11 price=339.49 support=310.2 resistance=344.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=52.76 liquidity=1382913.63 spike=2.44
- EEII.CA: score=20.41 buy_ready=True sector_rank=11 price=2.75 support=2.3 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=67.03 liquidity=4961945.5 spike=0.23
- EFIC.CA: score=4.08 buy_ready=False sector_rank=19 price=182.58 support=180.02 resistance=208.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=15.88 liquidity=359335.94 spike=0.14
- EFID.CA: score=24.51 buy_ready=False sector_rank=10 price=28.25 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=48.68 liquidity=33621856.0 spike=0.44
- EFIH.CA: score=30.9 buy_ready=True sector_rank=1 price=22.26 support=20.0 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=62.91 liquidity=15614052.0 spike=0.36
- EGAL.CA: score=20.12 buy_ready=False sector_rank=19 price=292.87 support=272.28 resistance=318.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=45.46 liquidity=8399443.0 spike=0.17
- EGAS.CA: score=14.18 buy_ready=False sector_rank=12 price=50.0 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=42.74 liquidity=928104.81 spike=0.12
- EGBE.CA: score=17.07 buy_ready=False sector_rank=14 price=0.46 support=0.43 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=60.71 liquidity=18001.23 spike=0.27
- EGCH.CA: score=21.94 buy_ready=False sector_rank=19 price=13.1 support=12.13 resistance=14.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=38.61 liquidity=46423584.0 spike=1.11
- EGSA.CA: score=13.9 buy_ready=False sector_rank=3 price=8.87 support=8.62 resistance=8.93 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=80.0 liquidity=2386.03 spike=0.54
- EGTS.CA: score=27.9 buy_ready=True sector_rank=4 price=18.71 support=15.1 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=54.5 liquidity=11544024.0 spike=0.18
- EHDR.CA: score=23.44 buy_ready=False sector_rank=11 price=2.61 support=2.37 resistance=2.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=40.58 liquidity=13881174.0 spike=0.32
- EKHO.CA: score=12.26 buy_ready=False sector_rank=12 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=11.07 buy_ready=False sector_rank=15 price=2.09 support=2.04 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=2206001.5 spike=0.14
- ELKA.CA: score=10.46 buy_ready=False sector_rank=11 price=1.51 support=1.42 resistance=1.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=43970336.0 spike=1.01
- ELNA.CA: score=13.91 buy_ready=False sector_rank=11 price=38.83 support=35.55 resistance=41.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=35.49 liquidity=462600.91 spike=0.88
- ELSH.CA: score=25.44 buy_ready=True sector_rank=11 price=13.79 support=11.1 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=47.58 liquidity=69411736.0 spike=0.39
- ELWA.CA: score=10.77 buy_ready=False sector_rank=11 price=1.94 support=1.89 resistance=2.22 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=37.84 liquidity=324350.55 spike=0.21
- EMFD.CA: score=22.24 buy_ready=False sector_rank=4 price=11.66 support=11.11 resistance=12.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=35.26 liquidity=8337344.5 spike=0.04
- ENGC.CA: score=22.4 buy_ready=True sector_rank=11 price=38.78 support=33.0 resistance=39.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=66.28 liquidity=4953735.0 spike=0.32
- EOSB.CA: score=15.46 buy_ready=False sector_rank=11 price=1.48 support=1.42 resistance=1.55 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=11715.68 spike=0.12
- EPCO.CA: score=10.91 buy_ready=False sector_rank=11 price=8.97 support=8.5 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=465100.66 spike=0.07
- EPPK.CA: score=17.67 buy_ready=False sector_rank=11 price=14.32 support=11.72 resistance=15.25 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=74.03 liquidity=1344834.13 spike=1.44
- ETEL.CA: score=26.29 buy_ready=True sector_rank=3 price=96.37 support=89.01 resistance=101.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=60.23 liquidity=7389584.0 spike=0.1
- ETRS.CA: score=25.44 buy_ready=True sector_rank=11 price=10.7 support=8.77 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=57.43 liquidity=16181474.0 spike=0.21
- EXPA.CA: score=12.21 buy_ready=False sector_rank=14 price=18.47 support=18.03 resistance=19.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=41.76 liquidity=2158344.75 spike=0.07
- FAIT.CA: score=20.29 buy_ready=True sector_rank=14 price=37.0 support=35.01 resistance=37.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=41.72 liquidity=3922866.75 spike=1.66
- FAITA.CA: score=10.54 buy_ready=False sector_rank=14 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=52.0 liquidity=36826.02 spike=1.23
- FERC.CA: score=18.52 buy_ready=False sector_rank=19 price=76.44 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=55.95 liquidity=5052059.5 spike=1.37
- FWRY.CA: score=27.9 buy_ready=False sector_rank=1 price=19.26 support=17.71 resistance=19.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=61.9 liquidity=18083874.0 spike=0.08
- GBCO.CA: score=22.87 buy_ready=True sector_rank=8 price=30.85 support=26.62 resistance=32.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=63.86 liquidity=6970041.5 spike=0.08
- GDWA.CA: score=5.95 buy_ready=False sector_rank=11 price=0.77 support=0.76 resistance=0.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=28.72 liquidity=1510105.25 spike=0.11
- GGCC.CA: score=24.44 buy_ready=False sector_rank=11 price=0.56 support=0.4 resistance=0.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=91.88 liquidity=10760200.0 spike=0.65
- GIHD.CA: score=18.9 buy_ready=True sector_rank=11 price=43.42 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=58.15 liquidity=1451087.75 spike=0.16
- GMCI.CA: score=15.11 buy_ready=False sector_rank=11 price=2.21 support=1.66 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=85.45 liquidity=663315.81 spike=0.75
- GRCA.CA: score=6.51 buy_ready=False sector_rank=11 price=50.34 support=48.75 resistance=58.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=14.64 liquidity=1067984.25 spike=0.32
- GSSC.CA: score=28.7 buy_ready=False sector_rank=11 price=256.03 support=240.0 resistance=263.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=60.77 liquidity=11874843.0 spike=3.13
- GTWL.CA: score=24.44 buy_ready=False sector_rank=11 price=100.0 support=46.0 resistance=108.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=90.08 liquidity=33717384.0 spike=0.46
- HDBK.CA: score=14.05 buy_ready=False sector_rank=14 price=80.0 support=75.3 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=20.35 liquidity=13203904.0 spike=0.34
- HELI.CA: score=30.46 buy_ready=True sector_rank=4 price=7.09 support=6.28 resistance=6.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=66.93 liquidity=276693024.0 spike=2.28
- HRHO.CA: score=20.84 buy_ready=False sector_rank=16 price=26.71 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=35.4 liquidity=12742339.0 spike=0.09
- ICID.CA: score=16.07 buy_ready=False sector_rank=11 price=7.77 support=6.36 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=56.3 liquidity=624162.75 spike=0.06
- IDRE.CA: score=14.25 buy_ready=False sector_rank=11 price=43.15 support=41.1 resistance=46.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=42.22 liquidity=802129.06 spike=0.08
- IFAP.CA: score=18.6 buy_ready=False sector_rank=17 price=19.5 support=18.47 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=47.09 liquidity=4779384.0 spike=0.98
- INFI.CA: score=28.44 buy_ready=False sector_rank=11 price=97.02 support=88.51 resistance=102.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=40.25 liquidity=25850538.0 spike=4.24
- IRON.CA: score=14.81 buy_ready=False sector_rank=19 price=32.12 support=30.51 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=44.92 liquidity=2081912.75 spike=0.27
- ISMA.CA: score=10.75 buy_ready=False sector_rank=11 price=26.99 support=26.82 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=3.11 liquidity=2302895.5 spike=0.07
- ISMQ.CA: score=21.72 buy_ready=False sector_rank=19 price=9.73 support=7.67 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=77.42 liquidity=30927180.0 spike=0.22
- ISPH.CA: score=20.35 buy_ready=False sector_rank=9 price=11.4 support=11.2 resistance=12.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=37.45 liquidity=9762128.0 spike=0.13
- JUFO.CA: score=19.83 buy_ready=True sector_rank=10 price=30.91 support=28.5 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=51.44 liquidity=4322879.0 spike=0.15
- KABO.CA: score=19.5 buy_ready=False sector_rank=7 price=7.4 support=5.96 resistance=7.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=87.66 liquidity=4604310.0 spike=0.17
- KWIN.CA: score=8.73 buy_ready=False sector_rank=11 price=67.88 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=30.79 liquidity=4289721.0 spike=0.33
- KZPC.CA: score=10.16 buy_ready=False sector_rank=11 price=8.47 support=8.26 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=35.83 liquidity=714184.06 spike=0.11
- LCSW.CA: score=27.08 buy_ready=True sector_rank=13 price=31.37 support=26.0 resistance=31.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=68.46 liquidity=27913752.0 spike=0.53
- LUTS.CA: score=21.64 buy_ready=False sector_rank=11 price=0.73 support=0.62 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=49.66 liquidity=8196982.5 spike=0.15
- MAAL.CA: score=24.44 buy_ready=False sector_rank=11 price=8.18 support=5.52 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=99.42 liquidity=11146619.0 spike=0.67
- MASR.CA: score=27.44 buy_ready=True sector_rank=11 price=7.69 support=6.54 resistance=7.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=58.67 liquidity=32875508.0 spike=0.42
- MBSC.CA: score=18.78 buy_ready=False sector_rank=13 price=242.03 support=222.66 resistance=257.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=40.85 liquidity=6696155.0 spike=0.26
- MCQE.CA: score=17.03 buy_ready=False sector_rank=13 price=178.06 support=166.66 resistance=189.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=52.03 liquidity=2947895.5 spike=0.2
- MCRO.CA: score=26.44 buy_ready=True sector_rank=11 price=1.25 support=1.17 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=16890140.0 spike=0.55
- MENA.CA: score=18.94 buy_ready=True sector_rank=4 price=7.09 support=6.41 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=59.16 liquidity=1040520.44 spike=0.12
- MEPA.CA: score=23.54 buy_ready=False sector_rank=11 price=1.66 support=1.52 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=9092493.0 spike=0.82
- MFPC.CA: score=23.72 buy_ready=False sector_rank=19 price=37.11 support=34.22 resistance=42.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=51.97 liquidity=82119720.0 spike=0.85
- MFSC.CA: score=15.75 buy_ready=False sector_rank=11 price=46.92 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=58.57 liquidity=2309344.0 spike=0.32
- MHOT.CA: score=5.67 buy_ready=False sector_rank=21 price=16.94 support=16.12 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=24.36 liquidity=4767533.0 spike=0.31
- MICH.CA: score=18.91 buy_ready=False sector_rank=11 price=37.57 support=34.0 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=51.51 liquidity=5462301.0 spike=0.34
- MILS.CA: score=15.44 buy_ready=False sector_rank=11 price=137.49 support=129.05 resistance=141.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36960420.0 spike=4.08
- MIPH.CA: score=18.95 buy_ready=True sector_rank=9 price=690.69 support=630.13 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=59.58 liquidity=1363543.75 spike=0.6
- MOED.CA: score=13.16 buy_ready=False sector_rank=11 price=0.69 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=43.8 liquidity=1712106.25 spike=0.19
- MOIL.CA: score=15.31 buy_ready=False sector_rank=12 price=0.52 support=0.46 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=72.63 liquidity=51761.09 spike=0.18
- MOIN.CA: score=12.96 buy_ready=False sector_rank=11 price=23.99 support=22.6 resistance=25.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=41.18 liquidity=976670.06 spike=1.27
- MOSC.CA: score=11.09 buy_ready=False sector_rank=11 price=270.1 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=41.71 liquidity=647659.88 spike=0.07
- MPCI.CA: score=20.41 buy_ready=True sector_rank=11 price=238.14 support=213.0 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=61.06 liquidity=4969793.0 spike=0.05
- MPCO.CA: score=10.26 buy_ready=False sector_rank=17 price=1.81 support=1.66 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=2438978.75 spike=0.03
- MPRC.CA: score=22.5 buy_ready=False sector_rank=11 price=42.51 support=31.15 resistance=41.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=89.34 liquidity=47897564.0 spike=1.03
- MTIE.CA: score=22.13 buy_ready=True sector_rank=8 price=9.34 support=8.65 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=4230642.0 spike=0.21
- NAHO.CA: score=11.47 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=24715.65 spike=0.98
- NCCW.CA: score=20.69 buy_ready=False sector_rank=11 price=6.15 support=5.82 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=42.55 liquidity=7248387.5 spike=0.26
- NEDA.CA: score=12.35 buy_ready=False sector_rank=11 price=2.74 support=2.7 resistance=2.83 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=31.58 liquidity=1905448.07 spike=5.71
- NHPS.CA: score=30.44 buy_ready=True sector_rank=11 price=71.29 support=61.55 resistance=75.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=65.33 liquidity=61332232.0 spike=4.13
- NINH.CA: score=16.66 buy_ready=False sector_rank=11 price=17.79 support=16.8 resistance=18.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=47.76 liquidity=4212830.0 spike=0.61
- NIPH.CA: score=27.58 buy_ready=True sector_rank=9 price=176.09 support=157.01 resistance=185.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=64.8 liquidity=16069218.0 spike=0.17
- OBRI.CA: score=27.62 buy_ready=True sector_rank=11 price=36.81 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=46.72 liquidity=29685982.0 spike=1.09
- OCDI.CA: score=22.9 buy_ready=False sector_rank=4 price=26.96 support=20.0 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=81.43 liquidity=19198832.0 spike=0.2
- OCPH.CA: score=15.39 buy_ready=False sector_rank=11 price=355.18 support=337.0 resistance=374.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=58.42 liquidity=943168.81 spike=0.14
- ODIN.CA: score=20.57 buy_ready=True sector_rank=11 price=2.34 support=2.01 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=58.18 liquidity=3125610.75 spike=0.23
- OFH.CA: score=21.81 buy_ready=True sector_rank=11 price=0.63 support=0.57 resistance=0.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=58.14 liquidity=4370141.0 spike=0.22
- OIH.CA: score=22.9 buy_ready=False sector_rank=6 price=1.41 support=1.33 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=70.0 liquidity=11506527.0 spike=0.15
- OLFI.CA: score=26.0 buy_ready=True sector_rank=10 price=22.73 support=21.0 resistance=23.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=62.42 liquidity=8489994.0 spike=0.29
- ORAS.CA: score=9.1 buy_ready=False sector_rank=20 price=681.21 support=680.1 resistance=687.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=59786600.0 spike=1.0
- ORHD.CA: score=25.9 buy_ready=True sector_rank=4 price=38.86 support=35.01 resistance=39.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=57.63 liquidity=18346934.0 spike=0.11
- ORWE.CA: score=17.91 buy_ready=False sector_rank=7 price=22.83 support=21.95 resistance=23.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=42.11 liquidity=4013981.25 spike=0.19
- PHAR.CA: score=18.38 buy_ready=False sector_rank=9 price=86.9 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=58.51 liquidity=791813.0 spike=0.03
- PHDC.CA: score=18.9 buy_ready=False sector_rank=4 price=14.77 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=21.98 liquidity=38033872.0 spike=0.12
- PHTV.CA: score=16.64 buy_ready=False sector_rank=11 price=281.63 support=201.55 resistance=284.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=87.96 liquidity=2193495.0 spike=0.17
- POUL.CA: score=16.4 buy_ready=False sector_rank=10 price=39.53 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=66.8 liquidity=887839.5 spike=0.02
- PRCL.CA: score=23.48 buy_ready=False sector_rank=13 price=36.03 support=23.75 resistance=36.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=84.32 liquidity=9391481.0 spike=0.18
- PRDC.CA: score=26.41 buy_ready=True sector_rank=4 price=8.45 support=5.91 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=57.89 liquidity=8514680.0 spike=0.06
- PRMH.CA: score=10.22 buy_ready=False sector_rank=11 price=2.54 support=2.34 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=29.17 liquidity=1772257.25 spike=0.06
- RACC.CA: score=20.14 buy_ready=True sector_rank=11 price=9.95 support=9.36 resistance=10.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=57.74 liquidity=2692108.75 spike=0.26
- RAKT.CA: score=12.56 buy_ready=False sector_rank=11 price=22.35 support=21.4 resistance=23.79 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=41.67 liquidity=371568.76 spike=1.37
- RAYA.CA: score=29.9 buy_ready=True sector_rank=2 price=7.8 support=6.7 resistance=8.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=63.3 liquidity=55649828.0 spike=0.53
- RMDA.CA: score=17.07 buy_ready=False sector_rank=9 price=4.99 support=4.81 resistance=5.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=40.98 liquidity=3485926.75 spike=0.05
- ROTO.CA: score=19.09 buy_ready=True sector_rank=11 price=41.87 support=33.06 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=43.66 liquidity=3646243.5 spike=0.11
- RREI.CA: score=27.25 buy_ready=True sector_rank=11 price=3.75 support=3.34 resistance=3.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=58.46 liquidity=7809365.5 spike=0.45
- RTVC.CA: score=13.44 buy_ready=False sector_rank=11 price=3.76 support=3.55 resistance=4.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=45.21 liquidity=996862.5 spike=0.2
- RUBX.CA: score=22.44 buy_ready=False sector_rank=11 price=13.08 support=9.8 resistance=14.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=78.82 liquidity=12112807.0 spike=0.23
- SAUD.CA: score=13.04 buy_ready=False sector_rank=14 price=21.22 support=19.99 resistance=22.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=40.61 liquidity=996206.94 spike=0.14
- SCEM.CA: score=17.12 buy_ready=False sector_rank=13 price=62.88 support=59.3 resistance=67.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=49.89 liquidity=3037878.75 spike=0.18
- SCFM.CA: score=15.44 buy_ready=False sector_rank=11 price=259.98 support=243.5 resistance=269.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21984296.0 spike=5.45
- SCTS.CA: score=18.0 buy_ready=True sector_rank=18 price=618.99 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=57.13 liquidity=1196884.63 spike=0.23
- SDTI.CA: score=16.46 buy_ready=False sector_rank=11 price=46.28 support=45.55 resistance=49.5 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=44.19 liquidity=3011624.64 spike=0.5
- SEIG.CA: score=26.7 buy_ready=False sector_rank=11 price=246.38 support=180.0 resistance=272.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=96.63 liquidity=27614624.0 spike=2.13
- SIPC.CA: score=15.61 buy_ready=False sector_rank=11 price=3.46 support=3.25 resistance=3.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=47.44 liquidity=1169875.88 spike=0.12
- SKPC.CA: score=22.72 buy_ready=False sector_rank=19 price=16.37 support=15.58 resistance=17.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=52.23 liquidity=21507274.0 spike=0.66
- SMFR.CA: score=15.01 buy_ready=False sector_rank=11 price=203.33 support=187.01 resistance=209.99 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=49.19 liquidity=566070.73 spike=0.33
- SNFC.CA: score=5.99 buy_ready=False sector_rank=11 price=11.43 support=11.26 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=26.23 liquidity=541031.06 spike=0.05
- SPIN.CA: score=16.66 buy_ready=False sector_rank=7 price=14.55 support=13.3 resistance=14.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=70.21 liquidity=757091.13 spike=0.08
- SPMD.CA: score=25.4 buy_ready=True sector_rank=11 price=0.45 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=58.73 liquidity=9960034.0 spike=0.53
- SUGR.CA: score=5.78 buy_ready=False sector_rank=10 price=46.85 support=45.31 resistance=50.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=29.6 liquidity=1264159.63 spike=0.24
- SVCE.CA: score=27.01 buy_ready=True sector_rank=11 price=9.33 support=8.11 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=51.59 liquidity=9565977.0 spike=0.13
- SWDY.CA: score=19.78 buy_ready=True sector_rank=15 price=87.79 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=55.81 liquidity=2924669.75 spike=0.21
- TALM.CA: score=7.3 buy_ready=False sector_rank=18 price=15.41 support=15.27 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=23.53 liquidity=2491317.5 spike=0.22
- TMGH.CA: score=27.9 buy_ready=True sector_rank=4 price=97.45 support=92.1 resistance=99.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=57.6 liquidity=27238468.0 spike=0.07
- TRTO.CA: score=11.44 buy_ready=False sector_rank=11 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=12.38 buy_ready=False sector_rank=11 price=516.39 support=480.0 resistance=529.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6931039.5 spike=6.28
- UEGC.CA: score=24.44 buy_ready=False sector_rank=11 price=1.72 support=1.33 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=76.36 liquidity=11037345.0 spike=0.43
- UNIP.CA: score=18.28 buy_ready=True sector_rank=11 price=0.33 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=40.74 liquidity=2835889.5 spike=0.14
- UNIT.CA: score=15.9 buy_ready=False sector_rank=4 price=19.51 support=16.64 resistance=19.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=54804664.0 spike=5.12
- WCDF.CA: score=12.75 buy_ready=False sector_rank=11 price=523.65 support=450.0 resistance=544.99 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=37.43 liquidity=304240.66 spike=0.98
- WKOL.CA: score=20.36 buy_ready=True sector_rank=11 price=314.01 support=273.1 resistance=334.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=63.41 liquidity=2918770.5 spike=0.44
- ZEOT.CA: score=20.44 buy_ready=True sector_rank=11 price=11.01 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=46.51 liquidity=5000560.5 spike=0.13
- ZMID.CA: score=27.9 buy_ready=True sector_rank=4 price=6.87 support=6.03 resistance=6.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=63.95 liquidity=108946472.0 spike=0.52

## Backtesting Lite
- AFMC.CA: 180d return=-4.97%, max drawdown=-29.5%, MA20>MA50 days last20=13, as_of=2026-07-07T21:00:00+00:00
- EFIH.CA: 180d return=72.25%, max drawdown=-22.68%, MA20>MA50 days last20=11, as_of=2026-07-07T21:00:00+00:00
- HELI.CA: 180d return=128.56%, max drawdown=-14.36%, MA20>MA50 days last20=20, as_of=2026-07-07T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- AFMC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria Flour Mills summary=Alexandria Flour Mills spends EGP 39m of capital raise proceeds; Alexandria Flour Mills sees 23% higher net profits in H1-20/21; Alexandria Mills’ profits plunge 69% in Q1-19/20
  - Alexandria Flour Mills spends EGP 39m of capital raise proceeds: https://english.mubasher.info/news/3987227/Alexandria-Flour-Mills-spends-EGP-39m-of-capital-raise-proceeds/
  - Alexandria Flour Mills sees 23% higher net profits in H1-20/21: https://english.mubasher.info/news/3754531/Alexandria-Flour-Mills-sees-23-higher-net-profits-in-H1-20-21/
  - Alexandria Mills’ profits plunge 69% in Q1-19/20: https://english.mubasher.info/news/3547654/Alexandria-Mills-profits-plunge-69-in-Q1-19-20/
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- HELI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Heliopolis Housing summary=Evidence rejected for HELI.CA: source text did not clearly match HELI.CA / Heliopolis Housing.
- NHPS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=National Company for Housing Professional Syndicates SAE summary=Evidence rejected for NHPS.CA: source text did not clearly match NHPS.CA / National Company for Housing Professional Syndicates SAE.
- RAYA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=554 sources=3 expected=Raya Holding summary=Raya stock maintains bullish momentum above EGP 9; Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt; Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn
  - Raya stock maintains bullish momentum above EGP 9: https://english.mubasher.info/news/4601857/Raya-stock-maintains-bullish-momentum-above-EGP-9/
  - Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt: https://english.mubasher.info/news/4577815/Aman-Holding-MSMEDA-partner-to-inject-EGP-300m-into-SMEs-across-Egypt/
  - Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn: https://english.mubasher.info/news/4564195/Raya-Holding-s-consolidated-profits-surge-in-2025-revenues-hit-EGP-63-8bn/
- GSSC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=General Co. For Silos & Storage summary=General Company for Silos generates nearly EGP 62m net profits in Q1-25/26 audited financials; General Company for Silos to set up new firm with EGP 500m capital; General Company for Silos’ EGM nods to EGP 25m capital hike
  - General Company for Silos generates nearly EGP 62m net profits in Q1-25/26 audited financials: https://english.mubasher.info/news/4529067/General-Company-for-Silos-generates-nearly-EGP-62m-net-profits-in-Q1-25-26-audited-financials/
  - General Company for Silos to set up new firm with EGP 500m capital: https://english.mubasher.info/news/4043715/General-Company-for-Silos-to-set-up-new-firm-with-EGP-500m-capital/
  - General Company for Silos’ EGM nods to EGP 25m capital hike: https://english.mubasher.info/news/4018676/General-Company-for-Silos-EGM-nods-to-EGP-25m-capital-hike/
- CERA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=The Arab Ceramic Co. summary=Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- INFI.CA: status=RECENT_ACCEPTED latest=2026-01-01 age_days=189 sources=3 expected=Ismailia National Co. for Food Industries summary=Foodico stock targets higher levels; Foodico plans to log nearly EGP 70.5m profits in 2026; Foodico to secure EGP 12m loan from national bank
  - Foodico stock targets higher levels: https://english.mubasher.info/news/4564894/Foodico-stock-targets-higher-levels/
  - Foodico plans to log nearly EGP 70.5m profits in 2026: https://english.mubasher.info/news/4541309/Foodico-plans-to-log-nearly-EGP-70-5m-profits-in-2026/
  - Foodico to secure EGP 12m loan from national bank: https://english.mubasher.info/news/3888447/Foodico-to-secure-EGP-12m-loan-from-national-bank/

## Warnings
- Evidence for AFMC.CA matches the company but no source/report date was detected.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence rejected for HELI.CA: source text did not clearly match HELI.CA / Heliopolis Housing.
- Evidence rejected for NHPS.CA: source text did not clearly match NHPS.CA / National Company for Housing Professional Syndicates SAE.
- Evidence for RAYA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for GSSC.CA matches the company but no source/report date was detected.
- Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
